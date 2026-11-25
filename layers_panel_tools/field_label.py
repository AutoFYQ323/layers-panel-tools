# -*- coding: utf-8 -*-
"""Pick one field on the current layer and use it as the label."""

from qgis.PyQt.QtWidgets import QMenu
from qgis.core import QgsPalLayerSettings, QgsVectorLayerSimpleLabeling

try:
    from qgis.PyQt.QtGui import QAction
except ImportError:
    from qgis.PyQt.QtWidgets import QAction

from .buttons import make_menu_action as build_menu_action, make_toolbar_button
from .i18n import tr
from .icons import load_icon
from .label_toggle import _placement
from .scope import is_vector, tell


def _icon():
    try:
        from qgis.core import QgsApplication

        icon = QgsApplication.getThemeIcon("/mActionLabeling.svg")
        if icon is not None and not icon.isNull():
            return icon
    except Exception:
        pass  # nosec
    return load_icon("labels")


def make_action(iface):
    tr("自定义标注")
    tr("点开后列出当前图层的字段。第一项是不显示；选一个字段就把该字段当作标注。")
    return make_toolbar_button(
        iface,
        "lpt:field_label",
        "LayersPanelToolsFieldLabel",
        "自定义标注",
        "点开后列出当前图层的字段。第一项是不显示；选一个字段就把该字段当作标注。",
        _icon(),
        None,
        menu=_build_menu(iface, iface.mainWindow()),
        popup="InstantPopup",
    )


def make_menu_action(iface):
    action = build_menu_action(
        iface,
        "LayersPanelToolsFieldLabelMenu",
        "自定义标注",
        "点开后列出当前图层的字段。第一项是不显示；选一个字段就把该字段当作标注。",
        _icon(),
        None,
    )
    action.setMenu(_build_menu(iface, iface.mainWindow()))
    return action


def _build_menu(iface, parent):
    menu = QMenu(parent)
    menu.setObjectName("LayersPanelToolsFieldLabelMenu")
    menu.aboutToShow.connect(lambda menu=menu: _fill_menu(iface, menu))
    return menu


def _current_layer(iface):
    layer = None
    try:
        layer = iface.activeLayer()
    except Exception:
        layer = None
    if is_vector(layer):
        return layer
    return None


def _current_field(layer):
    try:
        if not layer.labelsEnabled():
            return ""
        labeling = layer.labeling()
    except Exception:
        return ""
    if labeling is None:
        return ""
    try:
        settings = labeling.settings()
    except Exception:
        return ""
    try:
        name = str(settings.fieldName or "")
    except Exception:
        name = ""
    return name


def _field_names(layer):
    found = []
    try:
        fields = list(layer.fields())
    except Exception:
        return found
    for field in fields:
        try:
            name = str(field.name() or "")
        except Exception:
            name = ""
        if name:
            found.append(name)
    return found


def _fill_menu(iface, menu):
    menu.clear()
    layer = _current_layer(iface)
    current = _current_field(layer) if layer is not None else ""
    names = _field_names(layer) if layer is not None else []
    off = QAction(tr("不显示"), menu)
    off.setCheckable(True)
    off.setChecked(layer is not None and current not in names)
    off.triggered.connect(lambda *_args, target=layer: _apply(iface, target, ""))
    menu.addAction(off)
    if layer is None:
        off.setEnabled(False)
        missing = menu.addAction(tr("请先在图层面板里选中一个矢量图层。"))
        missing.setEnabled(False)
        return
    for name in names:
        action = QAction(name, menu)
        action.setCheckable(True)
        action.setChecked(name == current)
        action.triggered.connect(lambda *_args, target=layer, field=name: _apply(iface, target, field))
        menu.addAction(action)


def _apply(iface, layer, field_name):
    if layer is None or not is_vector(layer):
        tell(iface, tr("自定义标注"), tr("请先在图层面板里选中一个矢量图层。"), warning=True)
        return
    field_name = str(field_name or "")
    if not field_name:
        try:
            layer.setLabelsEnabled(False)
        except Exception:
            tell(iface, tr("自定义标注"), tr("没有矢量图层可切换标注。"), warning=True)
            return
        _repaint(iface, layer)
        return
    settings = QgsPalLayerSettings()
    settings.fieldName = field_name
    placement = _placement(layer)
    if placement is not None:
        try:
            settings.placement = placement
        except Exception:
            pass  # nosec
    try:
        layer.setLabeling(QgsVectorLayerSimpleLabeling(settings))
        layer.setLabelsEnabled(True)
    except Exception:
        tell(iface, tr("自定义标注"), tr("没有矢量图层可切换标注。"), warning=True)
        return
    _repaint(iface, layer)


def _repaint(iface, layer):
    try:
        layer.emitStyleChanged()
    except Exception:
        pass  # nosec
    try:
        layer.triggerRepaint()
    except Exception:
        pass  # nosec
    try:
        iface.mapCanvas().refresh()
    except Exception:
        pass  # nosec
