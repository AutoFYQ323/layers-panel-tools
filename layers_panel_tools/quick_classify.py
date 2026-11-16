# -*- coding: utf-8 -*-
"""快速分类：点符号化分类，给选中要素赋值（自 AttributeTable 1.18.7 快速命名移植）。"""

from qgis.PyQt.QtCore import Qt, QTimer
from qgis.PyQt.QtGui import QColor, QIcon, QPixmap
from qgis.PyQt.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)
from qgis.core import QgsProject, QgsVectorLayer

from .buttons import make_menu_action as build_menu_action, make_toolbar_button
from .classify_assign import (
    apply_assignments,
    assignment_key,
    category_keys_for_fids,
    copy_geoms_and_assign,
    count_category_keys,
    format_assignments,
    layer_categories,
    layer_geom_kind,
    layers_are_same,
    notify_open_attribute_tables,
    refresh_layer_after_assign,
    refresh_legend_class_counts,
    save_edits_via_qgis,
)
from .i18n import language_changed, tr
from .icons import load_icon
from .qt_compat import qt_attr, user_role


def _qt(name, default=None):
    value = getattr(Qt, name, None)
    if value is not None:
        return value
    try:
        return qt_attr(Qt, name)
    except AttributeError:
        return default


_USER_ROLE = user_role()
_WAIT = _qt("WaitCursor")

# Register autosave labels for check_i18n (also used via tr(label) at runtime).
tr("不自动保存")
tr("1秒后保存")
tr("2秒后保存")
tr("3秒后保存")
tr("4秒后保存")
tr("5秒后保存")
tr("10秒后保存")


def _msg_yes():
    value = getattr(QMessageBox, "Yes", None)
    if value is not None:
        return value
    try:
        return QMessageBox.StandardButton.Yes
    except Exception:
        return 16384


class QuickClassifyDialog(QDialog):
    """Mini window: click a symbology class to assign its rule to selected features."""

    _instance = None
    _AUTOSAVE_CHOICES = (
        (0, "不自动保存"),
        (1000, "1秒后保存"),
        (2000, "2秒后保存"),
        (3000, "3秒后保存"),
        (4000, "4秒后保存"),
        (5000, "5秒后保存"),
        (10000, "10秒后保存"),
    )

    @classmethod
    def open_for(cls, iface, parent=None):
        dlg = cls._instance
        try:
            if dlg is not None:
                dlg.windowTitle()
        except Exception:
            dlg = None
            cls._instance = None
        if dlg is None:
            dlg = cls(iface, parent=parent)
            cls._instance = dlg
        dlg.show()
        dlg.raise_()
        dlg.activateWindow()
        return dlg

    def __init__(self, iface, parent=None):
        super().__init__(parent)
        self.iface = iface
        self._layer = None
        self._reloading = False
        self.setWindowTitle(tr("快速分类"))
        self.resize(300, 380)

        root = QVBoxLayout(self)
        self.lbl_layer = QLabel(tr("请选择矢量图层"))
        self.lbl_layer.setWordWrap(True)
        self.on_theme_changed()
        root.addWidget(self.lbl_layer)

        self.list = QListWidget()
        self.list.itemClicked.connect(self._on_item_clicked)
        root.addWidget(self.list, 1)

        pin_row = QHBoxLayout()
        self.chk_pin = QCheckBox(tr("钉住图层"))
        self.chk_pin.setChecked(False)
        self.chk_pin.setToolTip(
            tr("钉住当前分类图层。在本层选中要素再点分类：只改属性、不复制。"
            "在其他层选中再点分类：把几何复制进钉住层，再按该类规则赋值。"
            "来源图层不改；钉住层不增加来源字段。")
        )
        self.chk_pin.toggled.connect(self._on_pin_toggled)
        self.cmb_autosave = QComboBox()
        for ms, label in self._AUTOSAVE_CHOICES:
            self.cmb_autosave.addItem(tr(label), ms)
        self.cmb_autosave.setCurrentIndex(0)
        self.cmb_autosave.setSizeAdjustPolicy(getattr(getattr(QComboBox, "SizeAdjustPolicy", QComboBox), "AdjustToContents", 0))
        self.cmb_autosave.setToolTip(
            tr("默认「不自动保存」：还能撤销/回滚，QGIS 图例数量不会马上变。"
            "选「N秒后保存」：先只写入，等 N 秒再点一次 QGIS 自带的「保存图层编辑」。"
            "连续命名会按当前秒数重新计时，只存一次。中途改成不自动保存则取消这次预约。"
            "图例由 QGIS 自己刷。会保存该层当前所有未保存修改，这次不能再撤销。"
            "关掉窗口会立刻补存。3 秒已验证能跟上图例；1 秒可能仍偏赶。")
        )
        self.cmb_autosave.currentIndexChanged.connect(self._on_autosave_mode_changed)
        pin_row.addWidget(self.chk_pin)
        pin_row.addWidget(self.cmb_autosave)
        pin_row.addStretch(1)
        root.addLayout(pin_row)

        self.chk_skip_confirm = QCheckBox(tr("勾选后点分类不再确认，直接赋值"))
        self.chk_skip_confirm.setChecked(False)
        self.chk_skip_confirm.setToolTip(tr("默认不勾选：会弹出确认。勾选后直接写入。"))
        root.addWidget(self.chk_skip_confirm)

        self.btn_legend_count = QPushButton(tr("刷新图例计数"))
        self.btn_legend_count.clicked.connect(self._on_refresh_legend_counts)
        root.addWidget(self.btn_legend_count)

        self._pinned_layer = None
        self._saving = False
        self._touching_legend = False
        self._autosave_layer = None
        self._cat_items = []
        self._counts = {}
        self._other_count = 0
        self._reload_timer = QTimer(self)
        self._reload_timer.setSingleShot(True)
        self._reload_timer.timeout.connect(self.reload)
        self._autosave_timer = QTimer(self)
        self._autosave_timer.setSingleShot(True)
        self._autosave_timer.timeout.connect(self._flush_autosave)

        try:
            self.iface.currentLayerChanged.connect(self._on_qgis_layer_changed)
        except Exception:
            pass  # nosec B110
        try:
            QgsProject.instance().layersWillBeRemoved.connect(self._on_layers_removed)
        except Exception:
            pass  # nosec B110
        self._bind_layer(self._qgis_vector_layer())
        self._reload_timer.start(0)
        try:
            language_changed().connect(self._apply_language)
        except Exception:
            pass  # nosec B110

    def on_theme_changed(self):
        lbl = getattr(self, "lbl_layer", None)
        if lbl is None:
            return
        lbl.setStyleSheet("QLabel { font-size: 16px; font-weight: bold; }")

    def closeEvent(self, event):
        self._reload_timer.stop()
        if self._autosave_timer.isActive():
            self._autosave_timer.stop()
            self._flush_autosave()
        self._bind_layer(None)
        try:
            self.iface.currentLayerChanged.disconnect(self._on_qgis_layer_changed)
        except Exception:
            pass  # nosec B110
        try:
            QgsProject.instance().layersWillBeRemoved.disconnect(self._on_layers_removed)
        except Exception:
            pass  # nosec B110
        try:
            language_changed().disconnect(self._apply_language)
        except Exception:
            pass  # nosec B110
        QuickClassifyDialog._instance = None
        super().closeEvent(event)

    def _apply_language(self, *_args):
        self.setWindowTitle(tr("快速分类"))
        self.chk_pin.setText(tr("钉住图层"))
        self.chk_pin.setToolTip(
            tr("钉住当前分类图层。在本层选中要素再点分类：只改属性、不复制。"
            "在其他层选中再点分类：把几何复制进钉住层，再按该类规则赋值。"
            "来源图层不改；钉住层不增加来源字段。")
        )
        self.chk_skip_confirm.setText(tr("勾选后点分类不再确认，直接赋值"))
        self.chk_skip_confirm.setToolTip(tr("默认不勾选：会弹出确认。勾选后直接写入。"))
        self.btn_legend_count.setText(tr("刷新图例计数"))
        self.cmb_autosave.blockSignals(True)
        current = self.cmb_autosave.currentData()
        for i, (ms, label) in enumerate(self._AUTOSAVE_CHOICES):
            if self.cmb_autosave.itemData(i) == ms:
                self.cmb_autosave.setItemText(i, tr(label))
        idx = self.cmb_autosave.findData(current)
        if idx >= 0:
            self.cmb_autosave.setCurrentIndex(idx)
        self.cmb_autosave.blockSignals(False)
        self.cmb_autosave.setToolTip(
            tr("默认「不自动保存」：还能撤销/回滚，QGIS 图例数量不会马上变。"
            "选「N秒后保存」：先只写入，等 N 秒再点一次 QGIS 自带的「保存图层编辑」。"
            "连续命名会按当前秒数重新计时，只存一次。中途改成不自动保存则取消这次预约。"
            "图例由 QGIS 自己刷。会保存该层当前所有未保存修改，这次不能再撤销。"
            "关掉窗口会立刻补存。3 秒已验证能跟上图例；1 秒可能仍偏赶。")
        )
        self._refresh_layer_caption()
        self.reload()

    @staticmethod
    def _layer_in(layer, layer_ids):
        if layer is None:
            return False
        try:
            return layer.id() in layer_ids
        except RuntimeError:
            return True

    def _on_layers_removed(self, layer_ids):
        ids = set(layer_ids or [])
        if self._layer_in(self._autosave_layer, ids):
            self._autosave_timer.stop()
            self._flush_autosave()
            self._autosave_layer = None
        pinned_gone = self._layer_in(self._pinned_layer, ids)
        if pinned_gone:
            self._pinned_layer = None
            self.chk_pin.blockSignals(True)
            self.chk_pin.setChecked(False)
            self.chk_pin.blockSignals(False)
        if self._layer_in(self._layer, ids):
            self._bind_layer(None)
            self._layer = None
        if pinned_gone or self._layer is None:
            active = self._qgis_vector_layer()
            if self._layer_in(active, ids):
                active = None
            self._bind_layer(active)
            self._schedule_reload()

    def _as_vector(self, layer):
        if layer is None:
            return None
        if isinstance(layer, QgsVectorLayer):
            return layer
        return None

    def _qgis_vector_layer(self):
        layer = None
        try:
            layer = self.iface.activeLayer()
        except Exception:
            layer = None
        return self._as_vector(layer)

    def _on_pin_toggled(self, checked):
        if checked:
            self._pinned_layer = self._layer
            self._refresh_layer_caption()
            return
        self._pinned_layer = None
        self._bind_layer(self._qgis_vector_layer())
        self._schedule_reload()

    def _dest_layer(self):
        if self.chk_pin.isChecked() and self._pinned_layer is not None:
            return self._pinned_layer
        return self._layer

    def _selected_fids(self, layer):
        if layer is None:
            return []
        try:
            return [int(fid) for fid in layer.selectedFeatureIds()]
        except Exception:
            return []

    def _pick_source_layer(self, dest):
        active = self._qgis_vector_layer()
        if dest is None:
            return active
        if active is not None and not layers_are_same(active, dest) and self._selected_fids(active):
            return active
        if self._selected_fids(dest):
            return dest
        if self.chk_pin.isChecked():
            try:
                layers = QgsProject.instance().mapLayers().values()
            except Exception:
                layers = []
            for lyr in layers:
                lyr = self._as_vector(lyr)
                if lyr is None or layers_are_same(lyr, dest):
                    continue  # nosec B112
                if self._selected_fids(lyr) and layer_geom_kind(lyr) == layer_geom_kind(dest):
                    return lyr
        return dest if dest is not None else active

    def _autosave_delay_ms(self):
        try:
            return int(self.cmb_autosave.currentData() or 0)
        except (TypeError, ValueError):
            return 0

    def _on_autosave_mode_changed(self, _index):
        delay = self._autosave_delay_ms()
        if delay <= 0:
            self._autosave_timer.stop()
            self._autosave_layer = None
            return
        if self._autosave_layer is not None:
            self._autosave_timer.start(delay)

    def _schedule_autosave(self, dest):
        delay = self._autosave_delay_ms()
        if dest is None or delay <= 0:
            return
        pending = self._autosave_layer
        if pending is not None and not layers_are_same(pending, dest):
            self._autosave_timer.stop()
            self._flush_autosave()
        self._autosave_layer = dest
        self._autosave_timer.start(delay)

    def _flush_autosave(self):
        dest = self._autosave_layer
        self._autosave_layer = None
        if dest is None:
            return
        try:
            if not dest.isEditable() or not dest.isModified():
                return
        except Exception:
            return
        self._saving = True
        try:
            save_err = save_edits_via_qgis(dest, self.iface)
        finally:
            self._saving = False
        if save_err:
            QMessageBox.information(self, tr("快速分类"), tr("已写入，但 QGIS 保存失败：%s") % save_err)

    def _on_qgis_layer_changed(self, layer):
        if getattr(self, "_saving", False):
            return
        layer = self._as_vector(layer)
        if self.chk_pin.isChecked() and self._pinned_layer is not None:
            return
        self._bind_layer(layer)
        self._schedule_reload()

    def _schedule_reload(self):
        if self._reloading or getattr(self, "_touching_legend", False):
            return
        self._reload_timer.start(80)

    def _on_refresh_legend_counts(self):
        dest = self._dest_layer()
        if dest is None:
            QMessageBox.information(self, tr("快速分类"), tr("请先选择一个矢量图层。"))
            return
        self._touching_legend = True
        try:
            err = refresh_legend_class_counts(dest)
        finally:
            self._touching_legend = False
        if err:
            QMessageBox.information(self, tr("快速分类"), err)

    def _bind_layer(self, layer):
        old = self._layer
        if old is not None:
            for signal, slot in (
                (getattr(old, "rendererChanged", None), self._schedule_reload),
            ):
                if signal is None:
                    continue
                try:
                    signal.disconnect(slot)
                except Exception:
                    pass  # nosec B110
        self._layer = layer
        if layer is None:
            return
        try:
            layer.rendererChanged.connect(self._schedule_reload)
        except Exception:
            pass  # nosec B110

    def _displayed_total(self):
        total = 0
        for i in range(self.list.count()):
            try:
                total += int(self.list.item(i).data(_USER_ROLE + 4) or 0)
            except (TypeError, ValueError):
                pass  # nosec B110
        return total

    def _refresh_layer_caption(self):
        dest = self._dest_layer()
        if dest is None:
            self.lbl_layer.setText(tr("请在 QGIS 中选择一个矢量图层"))
            return
        name = dest.name()
        if self.chk_pin.isChecked():
            text = tr("钉住：%s") % name
        else:
            text = name
        if self.list.count():
            text = "%s（%s）" % (text, self._displayed_total())
        self.lbl_layer.setText(text)

    def reload(self):
        if self._reloading:
            return
        self._reloading = True
        layer = self._dest_layer()
        self.list.clear()
        self._cat_items = []
        self._counts = {}
        self._other_count = 0
        try:
            self._refresh_layer_caption()
            if layer is None:
                return
            try:
                items, _err = layer_categories(layer)
            except Exception:
                items = []
            self._cat_items = items
            if items:
                QApplication.setOverrideCursor(_WAIT)
                try:
                    self._counts, self._other_count = count_category_keys(layer, items)
                except Exception:
                    self._counts, self._other_count = {}, 0
                finally:
                    QApplication.restoreOverrideCursor()
            other_used = False
            for info in items:
                label = info.get("label") or tr("(未命名)")
                hint = tr(info.get("hint") or "")
                text = label
                if hint and hint != label:
                    text = "%s  [%s]" % (label, hint)
                key = assignment_key(info.get("assignments") or {})
                if key is None:
                    count = self._other_count if not other_used else 0
                    other_used = True
                else:
                    count = int(self._counts.get(key, 0))
                item = QListWidgetItem(_color_icon(info.get("color")), "%s  (%s)" % (text, count))
                item.setData(_USER_ROLE, info.get("assignments") or {})
                item.setData(_USER_ROLE + 1, bool(info.get("assignable")))
                item.setData(_USER_ROLE + 2, key)
                item.setData(_USER_ROLE + 3, text)
                item.setData(_USER_ROLE + 4, count)
                item.setToolTip(hint or label)
                if not info.get("assignable") or info.get("legend_on") is False:
                    item.setForeground(QColor("#888888"))
                self.list.addItem(item)
            self._refresh_layer_caption()
        finally:
            self._reloading = False

    def _adjust_item_count(self, key, delta):
        if not delta:
            return
        if key is None:
            self._other_count = max(0, self._other_count + delta)
        else:
            self._counts[key] = max(0, int(self._counts.get(key, 0)) + delta)
        other_used = False
        for i in range(self.list.count()):
            item = self.list.item(i)
            item_key = item.data(_USER_ROLE + 2)
            if item_key is None:
                if other_used:
                    continue
                other_used = True
                n = self._other_count
            elif item_key == key:
                n = int(self._counts.get(item_key, 0))
            else:
                continue
            base = item.data(_USER_ROLE + 3) or item.text()
            item.setData(_USER_ROLE + 4, n)
            item.setText("%s  (%s)" % (base, n))
        self._refresh_layer_caption()

    def _on_item_clicked(self, item):
        if item is None:
            return
        dest = self._dest_layer()
        if dest is None:
            return
        assignable = bool(item.data(_USER_ROLE + 1))
        assignments = item.data(_USER_ROLE) or {}
        if not assignable or not assignments:
            QMessageBox.information(self, tr("快速分类"), tr("这个分类无法从符号化规则反推出要写的字段值。"))
            return
        source = self._pick_source_layer(dest)
        fids = self._selected_fids(source)
        if not fids:
            QMessageBox.information(self, tr("快速分类"), tr("请先在地图或属性表中选中要素。"))
            return
        cat = item.data(_USER_ROLE + 3) or (item.text() or "").split("  (")[0]
        writes = format_assignments(assignments)
        same = layers_are_same(source, dest)
        if not self.chk_skip_confirm.isChecked():
            if same:
                msg = tr("已选中 %s 个要素。\n将归属到分类「%s」。\n写入：%s\n继续？") % (
                    len(fids),
                    cat,
                    writes,
                )
            else:
                msg = tr(
                    "将把 %s 个要素从「%s」复制到「%s」，并归属分类「%s」。\n"
                    "来源图层不改。写入：%s\n继续？"
                ) % (len(fids), source.name(), dest.name(), cat, writes)
            reply = QMessageBox.question(self, tr("快速分类"), msg)
            if reply != _msg_yes():
                return
        old_keys = {}
        if same:
            try:
                old_keys = category_keys_for_fids(dest, self._cat_items, fids)
            except Exception:
                old_keys = {}
        updated, err, changed = self._apply_with_busy_ui(source, dest, assignments, fids)
        if err:
            QMessageBox.information(self, tr("快速分类"), err)
            return
        if updated:
            new_key = assignment_key(assignments)
            if changed is None:
                self._adjust_item_count(new_key, int(updated))
            else:
                delta = {}
                for fid in changed:
                    old = old_keys.get(int(fid))
                    delta[old] = delta.get(old, 0) - 1
                    delta[new_key] = delta.get(new_key, 0) + 1
                for key, n in delta.items():
                    self._adjust_item_count(key, n)
            refresh_layer_after_assign(dest, self.iface)
            if self._autosave_delay_ms() > 0:
                self._schedule_autosave(dest)
            notify_open_attribute_tables(
                dest, list(assignments.keys()), force_reload=not same
            )

    def _apply_with_busy_ui(self, source, dest, assignments, fids):
        canvas = None
        frozen = False
        QApplication.setOverrideCursor(_WAIT)
        try:
            try:
                canvas = self.iface.mapCanvas()
                if canvas is not None and not canvas.isFrozen():
                    canvas.freeze(True)
                    frozen = True
            except Exception:
                frozen = False
            if layers_are_same(source, dest):
                return apply_assignments(dest, assignments, fids)
            return copy_geoms_and_assign(source, dest, fids, assignments)
        finally:
            if frozen and canvas is not None:
                try:
                    canvas.freeze(False)
                except Exception:
                    pass  # nosec B110
            QApplication.restoreOverrideCursor()



def _color_icon(color_name, size=16):
    pix = QPixmap(size, size)
    color = QColor(color_name) if color_name else QColor("#cccccc")
    if not color.isValid():
        color = QColor("#cccccc")
    pix.fill(color)
    return QIcon(pix)


def make_action(iface):
    tr("快速分类")
    tr("按图层符号化分类给选中要素赋值；可钉住图层，从其他层复制几何后再分类")
    return make_toolbar_button(
        iface,
        "lpt:quick_classify",
        "LayersPanelToolsQuickClassify",
        "快速分类",
        "按图层符号化分类给选中要素赋值；可钉住图层，从其他层复制几何后再分类",
        load_icon("quick_classify"),
        lambda: open_quick_classify(iface),
    )


def make_menu_action(iface):
    return build_menu_action(
        iface,
        "LayersPanelToolsQuickClassifyMenu",
        "快速分类",
        "按图层符号化分类给选中要素赋值；可钉住图层，从其他层复制几何后再分类",
        load_icon("quick_classify"),
        lambda: open_quick_classify(iface),
    )


def close_quick_classify():
    dlg = QuickClassifyDialog._instance
    QuickClassifyDialog._instance = None
    if dlg is not None:
        try:
            dlg.close()
        except RuntimeError:
            pass  # nosec B110


def open_quick_classify(iface):
    parent = None
    try:
        parent = iface.mainWindow()
    except Exception:
        parent = None  # nosec B110 — fallback parent
    return QuickClassifyDialog.open_for(iface, parent=parent)
