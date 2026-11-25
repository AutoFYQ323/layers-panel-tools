# -*- coding: utf-8 -*-
"""多点画线：从图层面板打开配置窗，框选或画线取点，按相邻两点各生成一段直线。"""

import json
import time
import uuid

from qgis.PyQt.QtCore import QRectF, Qt, QTimer, QVariant
from qgis.PyQt.QtGui import QBrush, QColor, QFont, QPainter, QPen
from qgis.PyQt.QtWidgets import (
    QAbstractItemView,
    QCheckBox,
    QComboBox,
    QDialog,
    QDoubleSpinBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)
from qgis.core import (
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsDistanceArea,
    QgsFeature,
    QgsFeatureRequest,
    QgsField,
    QgsGeometry,
    QgsPointXY,
    QgsProject,
    QgsRectangle,
    QgsUnitTypes,
    QgsVectorLayer,
    QgsWkbTypes,
)
from qgis.gui import QgsMapCanvasItem, QgsMapTool, QgsProjectionSelectionDialog, QgsRubberBand

from .buttons import make_menu_action as build_menu_action, make_toolbar_button
from .i18n import apply_direction, subscribe, tr
from .icons import load_icon
from .plugin_settings import flush, plugin_qsettings
from .qt_compat import accepted, enum_int, qt_attr, run_dialog, user_role

_DIALOG = None
_CONTROLLER = None
_SETTINGS_KEY = "multiline"
_TEMP_LAYER_NAME = "多点画线_临时"
_ID_ROLE = user_role()
_NAME_ROLE = user_role(1)
_PROJECT_GEN = [0]
_PROJECT_WATCHED = [False]


def _point_layer_caption(layer):
    name = ""
    try:
        name = layer.name() or ""
    except Exception:
        name = ""
    count = 0
    try:
        count = int(layer.featureCount())
    except Exception:
        count = 0
    if count < 0:
        count = 0
    return "%s(%d)" % (name, count)


def _notify(parent, title, text, warning=False):
    """多点画线不弹结果框；成功失败都静默。"""
    return


def _wkb(name, qgis_name):
    try:
        from qgis.core import Qgis

        group = getattr(Qgis, "GeometryType", None)
        if group is not None and hasattr(group, qgis_name):
            return getattr(group, qgis_name)
    except Exception:
        pass  # nosec
    return getattr(QgsWkbTypes, name, 0)


def _button(name):
    value = getattr(Qt, name, None)
    if value is None:
        value = getattr(getattr(Qt, "MouseButton", Qt), name, None)
    return value


def _align_center():
    # Qt5: Qt.AlignCenter; Qt6: Qt.AlignmentFlag.AlignCenter — qt_attr covers both.
    return qt_attr(Qt, "AlignCenter")


def _font_bold():
    weight = getattr(QFont, "Bold", None)
    if weight is not None:
        return weight
    group = getattr(QFont, "Weight", None)
    if group is not None:
        return getattr(group, "Bold", 75)
    return 75


def _string_type():
    value = getattr(QVariant, "String", None)
    if value is not None:
        return value
    typ = getattr(QVariant, "Type", None)
    if typ is not None:
        return getattr(typ, "String", 10)
    return 10


def _make_field(name):
    try:
        return QgsField(name, _string_type())
    except Exception:
        return QgsField(name=name, type=_string_type())


def _bump_project_gen(*_args):
    _PROJECT_GEN[0] = _PROJECT_GEN[0] + 1


def _watch_project():
    if _PROJECT_WATCHED[0]:
        return
    try:
        project = QgsProject.instance()
        project.cleared.connect(_bump_project_gen)
        project.readProject.connect(_bump_project_gen)
        _PROJECT_WATCHED[0] = True
    except Exception:
        pass  # nosec


def _unwatch_project():
    if not _PROJECT_WATCHED[0]:
        return
    _PROJECT_WATCHED[0] = False
    try:
        project = QgsProject.instance()
        project.cleared.disconnect(_bump_project_gen)
        project.readProject.disconnect(_bump_project_gen)
    except Exception:
        pass  # nosec


def _project_token():
    _watch_project()
    project = QgsProject.instance()
    path = ""
    try:
        path = (project.fileName() or "").strip()
    except Exception:
        path = ""
    if path:
        return "file:%s#%d" % (path, _PROJECT_GEN[0])
    return "mem:%d" % _PROJECT_GEN[0]


def _is_point_layer(layer):
    try:
        return hasattr(layer, "wkbType") and QgsWkbTypes.geometryType(layer.wkbType()) == _wkb(
            "PointGeometry", "Point"
        )
    except Exception:
        return False


def _is_line_layer(layer):
    try:
        return hasattr(layer, "wkbType") and QgsWkbTypes.geometryType(layer.wkbType()) == _wkb(
            "LineGeometry", "Line"
        )
    except Exception:
        return False


def _load_settings():
    found = {
        "source_point_layer_ids": [],
        "source_point_layer_names": [],
        "select_mode_index": 2,
        "auto_generate": True,
        "auto_generate_delay_ms": 300,
        "output_mode": 0,
        "output_layer_id": "",
        "reference_line_layer_id": "",
        "allow_duplicate_lines": False,
        "snap_distance_m": 3.0,
        "temp_line_crs": "",
    }
    try:
        raw = plugin_qsettings().value(_SETTINGS_KEY, "")
    except Exception:
        raw = ""
    if raw in (None, ""):
        return found
    if not isinstance(raw, str):
        raw = str(raw)
    try:
        data = json.loads(raw)
    except Exception:
        return found
    if not isinstance(data, dict):
        return found
    for key in found:
        if key not in data:
            continue
        found[key] = data[key]
    try:
        found["select_mode_index"] = int(found["select_mode_index"])
    except (TypeError, ValueError):
        found["select_mode_index"] = 2
    try:
        found["auto_generate_delay_ms"] = int(found["auto_generate_delay_ms"])
    except (TypeError, ValueError):
        found["auto_generate_delay_ms"] = 300
    try:
        found["output_mode"] = int(found["output_mode"])
    except (TypeError, ValueError):
        found["output_mode"] = 0
    try:
        found["snap_distance_m"] = float(found["snap_distance_m"])
    except (TypeError, ValueError):
        found["snap_distance_m"] = 3.0
    found["auto_generate"] = bool(found["auto_generate"])
    found["allow_duplicate_lines"] = bool(found["allow_duplicate_lines"])
    found["source_point_layer_ids"] = [str(item) for item in found["source_point_layer_ids"] or [] if str(item)]
    found["source_point_layer_names"] = [str(item) for item in found["source_point_layer_names"] or [] if str(item)]
    found["output_layer_id"] = str(found["output_layer_id"] or "")
    found["reference_line_layer_id"] = str(found["reference_line_layer_id"] or "")
    found["temp_line_crs"] = str(found["temp_line_crs"] or "").strip()
    if found["snap_distance_m"] < 0.1 or found["snap_distance_m"] > 10000:
        found["snap_distance_m"] = 3.0
    if found["auto_generate_delay_ms"] < 0 or found["auto_generate_delay_ms"] > 5000:
        found["auto_generate_delay_ms"] = 300
    if found["select_mode_index"] not in (0, 1, 2):
        found["select_mode_index"] = 2
    if found["output_mode"] not in (0, 1):
        found["output_mode"] = 0
    return found


def _save_settings(data):
    payload = {
        "source_point_layer_ids": list(data.get("source_point_layer_ids") or []),
        "source_point_layer_names": list(data.get("source_point_layer_names") or []),
        "select_mode_index": int(data.get("select_mode_index") or 0),
        "auto_generate": bool(data.get("auto_generate")),
        "auto_generate_delay_ms": int(data.get("auto_generate_delay_ms") or 0),
        "output_mode": int(data.get("output_mode") or 0),
        "output_layer_id": str(data.get("output_layer_id") or ""),
        "reference_line_layer_id": str(data.get("reference_line_layer_id") or ""),
        "allow_duplicate_lines": bool(data.get("allow_duplicate_lines")),
        "snap_distance_m": float(data.get("snap_distance_m") or 3.0),
        "temp_line_crs": str(data.get("temp_line_crs") or "").strip(),
    }
    settings = plugin_qsettings()
    settings.setValue(_SETTINGS_KEY, json.dumps(payload, ensure_ascii=False))
    flush()


def _unique_batch_field(layer):
    names = []
    try:
        names = [field.name() for field in layer.fields()]
    except Exception:
        names = []
    if "lpt_batch" not in names:
        return "lpt_batch"
    number = 2
    while "lpt_batch_%d" % number in names:
        number += 1
    return "lpt_batch_%d" % number


def _drop_field(layer, name):
    if layer is None or not name:
        return
    try:
        index = layer.fields().indexOf(name)
    except Exception:
        return
    if index < 0:
        return
    started = False
    try:
        if not layer.isEditable():
            if not layer.startEditing():
                return
            started = True
        layer.dataProvider().deleteAttributes([index])
        layer.updateFields()
        if started or layer.isEditable():
            layer.commitChanges()
    except Exception:
        try:
            layer.rollBack()
        except Exception:
            pass  # nosec


def _distance_area(crs):
    da = QgsDistanceArea()
    da.setSourceCrs(crs, QgsProject.instance().transformContext())
    geographic = False
    try:
        geographic = bool(crs.isGeographic())
    except Exception:
        geographic = False
    if geographic:
        try:
            da.setEllipsoid(crs.ellipsoidAcronym() or "WGS84")
        except Exception:
            da.setEllipsoid("WGS84")
    return da


def _measure(da, crs, a, b):
    """Geographic: ellipsoidal metres. Metric projected: metres. Non-metric: map units."""
    geographic = False
    try:
        geographic = bool(crs is not None and crs.isGeographic())
    except Exception:
        geographic = False
    if geographic:
        try:
            return float(da.measureLine(a, b))
        except Exception:
            geographic = False
    metric = False
    try:
        units = crs.mapUnits()
        metres = getattr(QgsUnitTypes, "DistanceMeters", None)
        if metres is None:
            metres = getattr(getattr(QgsUnitTypes, "DistanceUnit", QgsUnitTypes), "DistanceMeters", None)
        metric = units == metres
    except Exception:
        metric = False
    if metric:
        try:
            return float(da.measureLine(a, b))
        except Exception:
            metric = False
    try:
        return float(a.distance(b))
    except Exception:
        try:
            return float(QgsGeometry.fromPointXY(a).distance(QgsGeometry.fromPointXY(b)))
        except Exception:
            return None


def make_action(iface):
    tr("多点画线")
    tr("多点画线_临时")
    tr("从点图层框选或画线取点，按相邻两点各生成一段直线")
    return make_toolbar_button(
        iface,
        "lpt:multiline",
        "LayersPanelToolsMultiline",
        "多点画线",
        "从点图层框选或画线取点，按相邻两点各生成一段直线",
        load_icon("multiline"),
        lambda: open_multiline(iface),
    )


def make_menu_action(iface):
    return build_menu_action(
        iface,
        "LayersPanelToolsMultilineMenu",
        "多点画线",
        "从点图层框选或画线取点，按相邻两点各生成一段直线",
        load_icon("multiline"),
        lambda: open_multiline(iface),
    )


def close_multiline():
    global _DIALOG, _CONTROLLER
    controller = _CONTROLLER
    _CONTROLLER = None
    if controller is not None:
        try:
            controller.cleanup()
        except Exception:
            pass  # nosec
    dialog = _DIALOG
    _DIALOG = None
    if dialog is not None:
        try:
            dialog.close()
        except RuntimeError:
            pass
    _unwatch_project()


def open_multiline(iface):
    global _DIALOG, _CONTROLLER
    if _DIALOG is not None:
        try:
            _DIALOG.show()
            _DIALOG.raise_()
            _DIALOG.activateWindow()
            return
        except RuntimeError:
            _DIALOG = None
            _CONTROLLER = None
    if _CONTROLLER is None:
        _CONTROLLER = MultilineController(iface)
    _DIALOG = MultilineDialog(iface, _CONTROLLER, iface.mainWindow())
    _DIALOG.show()
    _DIALOG.raise_()
    _DIALOG.activateWindow()


class PathNumberLabelItem(QgsMapCanvasItem):
    """画线框选预览上的 1、2、3… 序号。"""

    def __init__(self, canvas, map_point, number):
        super().__init__(canvas)
        self._map_point = QgsPointXY(map_point.x(), map_point.y())
        self._number = number
        try:
            crs = canvas.mapSettings().destinationCrs()
            size = 1e-5 if crs.isGeographic() else 0.5
        except Exception:
            size = 1e-5
        self.setRect(
            QgsRectangle(
                self._map_point.x() - size,
                self._map_point.y() - size,
                self._map_point.x() + size,
                self._map_point.y() + size,
            )
        )
        self.setZValue(1000)

    def paint(self, painter, option, widget=None):
        # Match LocalLinePlugin: yellow rounded badge centered on the snapped point.
        if painter is None:
            return
        pt_canvas = self.toCanvasCoordinates(self._map_point)
        try:
            pos = self.pos()
            local_x = pt_canvas.x() - pos.x()
            local_y = pt_canvas.y() - pos.y()
        except Exception:
            local_x = pt_canvas.x()
            local_y = pt_canvas.y()
        num_str = str(self._number)
        font = QFont("Arial", 14, _font_bold())
        painter.setFont(font)
        metrics = painter.fontMetrics()
        advance = metrics.horizontalAdvance(num_str) if hasattr(metrics, "horizontalAdvance") else metrics.width(num_str)
        w = max(advance + 14, 28)
        h = metrics.height() + 10
        x = local_x - w / 2
        y = local_y - h / 2
        painter.setPen(QPen(QColor(40, 40, 40), 2))
        painter.setBrush(QBrush(QColor(255, 220, 100)))
        painter.drawRoundedRect(QRectF(x, y, w, h), 5, 5)
        painter.setPen(QColor(40, 40, 40))
        painter.drawText(QRectF(x, y, w, h), _align_center(), num_str)


class RectangleMapTool(QgsMapTool):
    def __init__(self, canvas, on_done):
        super().__init__(canvas)
        self.canvas = canvas
        self.on_done = on_done
        self._start = None
        self._rb = QgsRubberBand(canvas, _wkb("PolygonGeometry", "Polygon"))
        self._rb.setStrokeColor(QColor(58, 139, 253))
        self._rb.setFillColor(QColor(58, 139, 253, 40))
        self._rb.setWidth(2)

    def canvasPressEvent(self, event):
        if event.button() == _button("LeftButton"):
            self._start = self.canvas.getCoordinateTransform().toMapCoordinates(event.pos().x(), event.pos().y())
            self._rb.reset(_wkb("PolygonGeometry", "Polygon"))

    def canvasMoveEvent(self, event):
        if self._start is None:
            return
        pt = self.canvas.getCoordinateTransform().toMapCoordinates(event.pos().x(), event.pos().y())
        self._rb.reset(_wkb("PolygonGeometry", "Polygon"))
        self._rb.addPoint(QgsPointXY(self._start.x(), self._start.y()), False)
        self._rb.addPoint(QgsPointXY(pt.x(), self._start.y()), False)
        self._rb.addPoint(QgsPointXY(pt.x(), pt.y()), False)
        self._rb.addPoint(QgsPointXY(self._start.x(), pt.y()), True)

    def canvasReleaseEvent(self, event):
        if event.button() != _button("LeftButton") or self._start is None:
            return
        pt = self.canvas.getCoordinateTransform().toMapCoordinates(event.pos().x(), event.pos().y())
        rect = QgsRectangle(self._start, pt)
        self._start = None
        self._rb.reset(_wkb("PolygonGeometry", "Polygon"))
        if not rect.isEmpty():
            try:
                self.on_done(rect, None)
            except Exception:
                pass  # nosec

    def deactivate(self):
        self._start = None
        self._rb.reset(_wkb("PolygonGeometry", "Polygon"))
        super().deactivate()


class PolygonMapTool(QgsMapTool):
    def __init__(self, canvas, on_done):
        super().__init__(canvas)
        self.canvas = canvas
        self.on_done = on_done
        self._points = []
        self._rb = QgsRubberBand(canvas, _wkb("PolygonGeometry", "Polygon"))
        self._rb.setStrokeColor(QColor(58, 139, 253))
        self._rb.setFillColor(QColor(58, 139, 253, 40))
        self._rb.setWidth(2)
        self._rb_temp = QgsRubberBand(canvas, _wkb("LineGeometry", "Line"))
        self._rb_temp.setStrokeColor(QColor(58, 139, 253))
        self._rb_temp.setWidth(2)

    def canvasPressEvent(self, event):
        if event.button() == _button("LeftButton"):
            pt = self.canvas.getCoordinateTransform().toMapCoordinates(event.pos().x(), event.pos().y())
            self._points.append(pt)
            self._update_rubber_band()
        elif event.button() == _button("RightButton"):
            if len(self._points) >= 3:
                polygon = QgsGeometry.fromPolygonXY([self._points + [self._points[0]]])
                rect = polygon.boundingBox()
                self._points = []
                self._rb.reset(_wkb("PolygonGeometry", "Polygon"))
                self._rb_temp.reset(_wkb("LineGeometry", "Line"))
                try:
                    self.on_done(rect, polygon)
                except Exception:
                    pass  # nosec
            else:
                self._points = []
                self._rb.reset(_wkb("PolygonGeometry", "Polygon"))
                self._rb_temp.reset(_wkb("LineGeometry", "Line"))

    def canvasMoveEvent(self, event):
        if not self._points:
            return
        pt = self.canvas.getCoordinateTransform().toMapCoordinates(event.pos().x(), event.pos().y())
        self._rb_temp.reset(_wkb("LineGeometry", "Line"))
        self._rb_temp.addPoint(self._points[-1], False)
        self._rb_temp.addPoint(pt, True)

    def _update_rubber_band(self):
        self._rb.reset(_wkb("PolygonGeometry", "Polygon"))
        for pt in self._points:
            self._rb.addPoint(pt, False)
        if self._points:
            self._rb.addPoint(self._points[0], True)

    def deactivate(self):
        self._points = []
        self._rb.reset(_wkb("PolygonGeometry", "Polygon"))
        self._rb_temp.reset(_wkb("LineGeometry", "Line"))
        super().deactivate()


class PolylineMapTool(QgsMapTool):
    def __init__(self, canvas, on_done, preview_callback=None):
        super().__init__(canvas)
        self.canvas = canvas
        self.on_done = on_done
        self.preview_callback = preview_callback
        self._points = []
        self._rb = QgsRubberBand(canvas, _wkb("LineGeometry", "Line"))
        self._rb.setStrokeColor(QColor(255, 100, 100))
        self._rb.setWidth(3)
        self._rb_temp = QgsRubberBand(canvas, _wkb("LineGeometry", "Line"))
        self._rb_temp.setStrokeColor(QColor(255, 100, 100))
        self._rb_temp.setWidth(2)
        self._rb_preview = QgsRubberBand(canvas, _wkb("PointGeometry", "Point"))
        self._rb_preview.setStrokeColor(QColor(50, 205, 50))
        self._rb_preview.setFillColor(QColor(50, 205, 50, 180))
        self._rb_preview.setWidth(2)
        try:
            self._rb_preview.setIconSize(10)
        except Exception:
            pass  # nosec
        self._label_items = []
        self._committed_snaps = []
        self._preview_last_time = 0
        self._preview_throttle_ms = 80

    def canvasPressEvent(self, event):
        if event.button() == _button("LeftButton"):
            pt = self.canvas.getCoordinateTransform().toMapCoordinates(event.pos().x(), event.pos().y())
            self._points.append(pt)
            self._update_rubber_band()
            # Lock the nearest snap at this click immediately so badge N never waits for click N+1.
            self._commit_snap_at(pt)
            self._update_preview()
        elif event.button() == _button("RightButton"):
            self._finish_line_if_ready()

    def canvasDoubleClickEvent(self, event):
        if event.button() == _button("LeftButton") and len(self._points) >= 2:
            self._finish_line_if_ready()
            event.accept()
            return
        super().canvasDoubleClickEvent(event)

    def _finish_line_if_ready(self):
        if len(self._points) >= 2:
            line_geom = QgsGeometry.fromPolylineXY(self._points)
            rect = line_geom.boundingBox()
            self._points = []
            self._committed_snaps = []
            self._clear_preview()
            try:
                self.on_done(rect, line_geom)
            except Exception:
                pass  # nosec
        else:
            self._points = []
            self._committed_snaps = []
            self._clear_preview()

    def _snap_key(self, point):
        try:
            return (round(point.x(), 6), round(point.y(), 6))
        except Exception:
            return None

    def _commit_snap_at(self, map_point):
        """Remember the nearest source point at this click so its badge stays from that click on."""
        if not self.preview_callback or map_point is None:
            return
        try:
            points = list(self.preview_callback(map_point) or [])
        except Exception:
            points = []
        for point in points:
            key = self._snap_key(point)
            if key is None:
                continue
            if any(self._snap_key(existing) == key for existing in self._committed_snaps):
                continue
            self._committed_snaps.append(point)
            break

    def _clear_number_labels(self):
        try:
            scene = self.canvas.scene()
            for item in self._label_items:
                try:
                    scene.removeItem(item)
                except Exception:
                    pass  # nosec
            self._label_items = []
        except Exception:
            self._label_items = []

    def _clear_preview(self):
        self._rb.reset(_wkb("LineGeometry", "Line"))
        self._rb_temp.reset(_wkb("LineGeometry", "Line"))
        self._rb_preview.reset(_wkb("PointGeometry", "Point"))
        self._clear_number_labels()

    def _update_number_labels(self, points):
        self._clear_number_labels()
        if not points or not self.canvas:
            return
        try:
            scene = self.canvas.scene()
            for index, point in enumerate(points):
                item = PathNumberLabelItem(self.canvas, point, index + 1)
                scene.addItem(item)
                self._label_items.append(item)
                try:
                    item.updatePosition()
                except Exception:
                    pass  # nosec
            try:
                self.canvas.refresh()
            except Exception:
                pass  # nosec
        except Exception:
            self._clear_number_labels()

    def _show_preview_points(self, points):
        self._rb_preview.reset(_wkb("PointGeometry", "Point"))
        for point in points or []:
            self._rb_preview.addPoint(point, True)
        self._update_number_labels(points or [])

    def _preview_for_path(self, vertices):
        """All snapped points satisfied now — committed clicks plus live line/vertex snaps."""
        found = []
        seen = set()

        def _add(points):
            for point in points or []:
                key = self._snap_key(point)
                if key is None or key in seen:
                    continue
                seen.add(key)
                found.append(point)

        _add(self._committed_snaps)
        if not self.preview_callback or not vertices:
            return found
        if len(vertices) == 1:
            _add(self.preview_callback(vertices[0]))
            return found
        line_geom = QgsGeometry.fromPolylineXY(vertices)
        if line_geom.isEmpty():
            return found
        # Line search plus a per-vertex snap so endpoint N is not delayed until click N+1.
        _add(self.preview_callback(line_geom))
        for vertex in vertices:
            _add(self.preview_callback(vertex))
        try:
            found.sort(
                key=lambda point: (
                    line_geom.lineLocatePoint(QgsGeometry.fromPointXY(point)),
                    point.x(),
                    point.y(),
                )
            )
        except Exception:
            pass  # nosec
        return found

    def _update_preview(self):
        if not self.preview_callback or not self._points:
            self._rb_preview.reset(_wkb("PointGeometry", "Point"))
            self._clear_number_labels()
            return
        try:
            self._show_preview_points(self._preview_for_path(self._points))
        except Exception:
            self._rb_preview.reset(_wkb("PointGeometry", "Point"))
            self._clear_number_labels()

    def canvasMoveEvent(self, event):
        if not self._points:
            return
        pt = self.canvas.getCoordinateTransform().toMapCoordinates(event.pos().x(), event.pos().y())
        self._rb_temp.reset(_wkb("LineGeometry", "Line"))
        self._rb_temp.addPoint(self._points[-1], False)
        self._rb_temp.addPoint(pt, True)
        if not self.preview_callback:
            return
        now = time.time() * 1000
        if now - self._preview_last_time < self._preview_throttle_ms:
            return
        self._preview_last_time = now
        try:
            self._show_preview_points(self._preview_for_path(list(self._points) + [pt]))
        except Exception:
            self._rb_preview.reset(_wkb("PointGeometry", "Point"))
            self._clear_number_labels()

    def _update_rubber_band(self):
        self._rb.reset(_wkb("LineGeometry", "Line"))
        for index, pt in enumerate(self._points):
            self._rb.addPoint(pt, index == len(self._points) - 1)

    def deactivate(self):
        self._points = []
        self._committed_snaps = []
        self._clear_preview()
        super().deactivate()


class MultilineController:
    def __init__(self, iface):
        self.iface = iface
        self.source_point_layers = []
        self.output_layer = None
        self._output_mode = 0
        self._output_layer_id = ""
        self._reference_line_layer_id = ""
        self._allow_duplicate_lines = False
        self._snap_distance_m = 3.0
        self._temp_line_crs = ""
        self._frame_extent = None
        self._frame_polygon = None
        self._frame_line = None
        self._prev_map_tool = None
        self._rect_tool = None
        self._polygon_tool = None
        self._polyline_tool = None
        self._undo = None
        self._added_field = None

    def cleanup(self):
        canvas = None
        try:
            canvas = self.iface.mapCanvas()
        except Exception:
            canvas = None
        for tool in (self._rect_tool, self._polygon_tool, self._polyline_tool):
            if tool is None or canvas is None:
                continue
            try:
                if canvas.mapTool() is tool:
                    canvas.unsetMapTool(tool)
            except Exception:
                pass  # nosec
        self._rect_tool = None
        self._polygon_tool = None
        self._polyline_tool = None

    def _transform_point(self, pt_xy, from_crs, to_crs):
        if not pt_xy or not from_crs or not to_crs or not from_crs.isValid() or not to_crs.isValid():
            return None
        try:
            xform = QgsCoordinateTransform(from_crs, to_crs, QgsProject.instance().transformContext())
            return xform.transform(pt_xy)
        except Exception:
            return None

    def preview_points_along_line(self, line_or_point):
        """Accept a line geometry or a single canvas QgsPointXY (first-click badge \"1\")."""
        if line_or_point is None:
            return []
        if not self.source_point_layers:
            return []
        try:
            canvas_crs = self.iface.mapCanvas().mapSettings().destinationCrs()
        except Exception:
            return []
        snap_m = float(self._snap_distance_m or 3.0)
        if snap_m <= 0:
            snap_m = 3.0
        single = isinstance(line_or_point, QgsPointXY)
        if single:
            line_out = QgsGeometry.fromPointXY(line_or_point)
        else:
            line_out = QgsGeometry(line_or_point)
            try:
                if line_out.isEmpty() or (not line_out.isMultipart() and len(line_out.asPolyline()) < 2):
                    return []
            except Exception:
                return []
        if line_out.isEmpty():
            return []
        line_bbox = line_out.boundingBox()
        if line_bbox.isEmpty() and not single:
            return []
        if canvas_crs.isGeographic():
            # ~meters to degrees; keep a usable search box for first-click snap.
            margin = max(0.0001, (snap_m / 111320.0) * 2.0)
        else:
            margin = max(snap_m * 2.0, 1.0)
        rect_expanded = QgsRectangle(
            line_bbox.xMinimum() - margin,
            line_bbox.yMinimum() - margin,
            line_bbox.xMaximum() + margin,
            line_bbox.yMaximum() + margin,
        )
        da = _distance_area(canvas_crs)
        candidates = []
        for layer in self.source_point_layers:
            try:
                try:
                    layer_crs = layer.crs() if (layer.crs() and layer.crs().isValid()) else canvas_crs
                except Exception:
                    layer_crs = canvas_crs
                if layer_crs != canvas_crs:
                    try:
                        xform = QgsCoordinateTransform(canvas_crs, layer_crs, QgsProject.instance().transformContext())
                        rect_layer = xform.transform(rect_expanded)
                    except Exception:
                        _lpt_skip = True
                    else:
                        _lpt_skip = False
                    if _lpt_skip:
                        continue
                else:
                    rect_layer = rect_expanded
                request = QgsFeatureRequest().setFilterRect(rect_layer)
                for feature in layer.getFeatures(request):
                    geom = feature.geometry()
                    if not geom or geom.isEmpty():
                        continue
                    try:
                        point = geom.asPoint()
                        pt_xy = QgsPointXY(point.x(), point.y())
                    except Exception:
                        _lpt_skip = True
                    else:
                        _lpt_skip = False
                    if _lpt_skip:
                        continue
                    pt_canvas = self._transform_point(pt_xy, layer_crs, canvas_crs)
                    if not pt_canvas:
                        continue
                    if single:
                        try:
                            dist = _measure(da, canvas_crs, pt_canvas, line_or_point)
                        except Exception:
                            _lpt_skip = True
                        else:
                            _lpt_skip = False
                        if _lpt_skip:
                            continue
                    else:
                        closest = line_out.nearestPoint(QgsGeometry.fromPointXY(pt_canvas))
                        if closest.isEmpty():
                            continue
                        try:
                            dist = _measure(da, canvas_crs, pt_canvas, closest.asPoint())
                        except Exception:
                            _lpt_skip = True
                        else:
                            _lpt_skip = False
                        if _lpt_skip:
                            continue
                    if dist is None or dist > snap_m:
                        continue
                    candidates.append(pt_canvas)
            except Exception:
                _lpt_skip = True
            else:
                _lpt_skip = False
            if _lpt_skip:
                continue
        if single:
            try:
                candidates.sort(
                    key=lambda point: (
                        _measure(da, canvas_crs, point, line_or_point) or 0.0,
                        point.x(),
                        point.y(),
                    )
                )
            except Exception:
                pass  # nosec
            return candidates[:1]
        try:
            candidates.sort(key=lambda point: (line_out.lineLocatePoint(QgsGeometry.fromPointXY(point)), point.x(), point.y()))
        except Exception:
            pass  # nosec
        return candidates

    def _desired_temp_crs(self):
        auth = (self._temp_line_crs or "").strip()
        if not auth:
            try:
                crs = QgsProject.instance().crs()
                auth = (crs.authid() if (crs and crs.isValid()) else "") or "EPSG:4326"
            except Exception:
                auth = "EPSG:4326"
        return auth or "EPSG:4326"

    def _ensure_output_layer(self, parent):
        if self._output_mode == 1 and self._output_layer_id:
            try:
                layer = QgsProject.instance().mapLayer(self._output_layer_id)
            except Exception:
                layer = None
            if layer is None or not _is_line_layer(layer):
                _notify(parent, tr("多点画线"), tr("指定的线图层无效或不存在。"), warning=True)
                return None
            try:
                if not layer.isValid():
                    _notify(parent, tr("多点画线"), tr("指定的线图层无效或不存在。"), warning=True)
                    return None
            except RuntimeError:
                _notify(parent, tr("多点画线"), tr("指定的线图层无效或不存在。"), warning=True)
                return None
            try:
                if callable(getattr(layer, "readOnly", None)) and layer.readOnly():
                    _notify(parent, tr("多点画线"), tr("指定的线图层是只读的，无法写入。"), warning=True)
                    return None
            except Exception:
                pass  # nosec
            self.output_layer = layer
            return layer

        want = self._desired_temp_crs()
        try:
            current = getattr(self, "output_layer", None)
            if current is not None and current.isValid() and current in list(QgsProject.instance().mapLayers().values()):
                provider = current.providerType() if callable(getattr(current, "providerType", None)) else ""
                if (provider == "memory" or (current.name() or "").strip() == tr(_TEMP_LAYER_NAME) or (current.name() or "").strip() == _TEMP_LAYER_NAME):
                    if current.crs() and current.crs().authid() == want:
                        return current
            self.output_layer = None
        except RuntimeError:
            self.output_layer = None
        except Exception:
            self.output_layer = None
        try:
            layer = QgsVectorLayer("LineString?crs=%s" % want, _TEMP_LAYER_NAME, "memory")
            if not layer.isValid():
                _notify(parent, tr("多点画线"), tr("无法创建临时线图层。"), warning=True)
                return None
            QgsProject.instance().addMapLayer(layer)
            self.output_layer = layer
            return layer
        except Exception:
            self.output_layer = None
            _notify(parent, tr("多点画线"), tr("无法创建临时线图层。"), warning=True)
            return None

    def start_pick(self, mode_index, parent):
        if not self.source_point_layers:
            _notify(parent, tr("多点画线"), tr("请先选择至少一个点图层。"), warning=True)
            return
        canvas = self.iface.mapCanvas()
        if canvas is None:
            return
        self._prev_map_tool = canvas.mapTool()
        if mode_index == 0:
            if self._rect_tool is None:
                self._rect_tool = RectangleMapTool(canvas, lambda rect, polygon=None: self._on_frame(rect, polygon, None, parent))
            canvas.setMapTool(self._rect_tool)
        elif mode_index == 1:
            if self._polygon_tool is None:
                self._polygon_tool = PolygonMapTool(canvas, lambda rect, polygon=None: self._on_frame(rect, polygon, None, parent))
            canvas.setMapTool(self._polygon_tool)
        else:
            if self._polyline_tool is None:
                self._polyline_tool = PolylineMapTool(
                    canvas,
                    lambda rect, line_geom: self._on_frame(rect, None, line_geom, parent),
                    preview_callback=self.preview_points_along_line,
                )
            canvas.setMapTool(self._polyline_tool)

    def restore_map_tool(self):
        canvas = None
        try:
            canvas = self.iface.mapCanvas()
        except Exception:
            canvas = None
        if canvas is None:
            return
        try:
            if self._prev_map_tool is not None:
                canvas.setMapTool(self._prev_map_tool)
            else:
                self.iface.actionPan().trigger()
        except Exception:
            try:
                self.iface.actionPan().trigger()
            except Exception:
                pass  # nosec

    def _on_frame(self, rect, polygon, line_geom, parent):
        self._frame_extent = rect
        self._frame_polygon = polygon
        self._frame_line = line_geom
        if parent is not None:
            try:
                parent.mark_frame(line_geom is not None, polygon is not None)
            except Exception:
                pass  # nosec
            if parent.auto_generate():
                delay = parent.auto_delay()

                def _run():
                    created = self.generate(parent)
                    if created is not None and created > 0:
                        QTimer.singleShot(500, lambda: self.start_pick(parent.select_mode(), parent))

                if delay <= 0:
                    _run()
                else:
                    QTimer.singleShot(delay, _run)
                return
        self.restore_map_tool()

    def generate(self, parent):
        if not self.source_point_layers:
            _notify(parent, tr("多点画线"), tr("请先选择至少一个点图层。"), warning=True)
            return None
        if not (self._reference_line_layer_id or "").strip():
            _notify(parent, tr("多点画线"), tr("请先选择参考线图层。参考线图层即使允许重复也必须选择。"), warning=True)
            return None
        try:
            ref_layer = QgsProject.instance().mapLayer(self._reference_line_layer_id)
        except Exception:
            ref_layer = None
        if ref_layer is None or not _is_line_layer(ref_layer):
            _notify(parent, tr("多点画线"), tr("请先选择参考线图层。参考线图层即使允许重复也必须选择。"), warning=True)
            return None
        out_layer = self._ensure_output_layer(parent)
        if out_layer is None:
            return None
        added_field = None
        try:
            return self._generate_into(parent, out_layer, ref_layer)
        except Exception:
            if added_field:
                _drop_field(out_layer, added_field)
            return None

    def _generate_into(self, parent, out_layer, ref_layer):
        rect = self._frame_extent
        polygon = self._frame_polygon
        frame_line = self._frame_line
        if not rect or rect.isEmpty():
            _notify(parent, tr("多点画线"), tr("请先框选或画线。"), warning=True)
            return None
        try:
            out_crs = out_layer.crs() if out_layer.crs() and out_layer.crs().isValid() else QgsCoordinateReferenceSystem("EPSG:4326")
        except RuntimeError:
            _notify(parent, tr("多点画线"), tr("指定的线图层无效或不存在。"), warning=True)
            return None
        except Exception:
            out_crs = QgsCoordinateReferenceSystem("EPSG:4326")
        try:
            canvas_crs = self.iface.mapCanvas().mapSettings().destinationCrs()
        except Exception:
            canvas_crs = out_crs
        use_line_mode = frame_line is not None and not frame_line.isEmpty()
        snap_m = float(self._snap_distance_m or 3.0)
        if snap_m <= 0:
            snap_m = 3.0
        ordered_points = []
        if use_line_mode:
            try:
                line_out = QgsGeometry(frame_line)
                if canvas_crs != out_crs:
                    xform = QgsCoordinateTransform(canvas_crs, out_crs, QgsProject.instance().transformContext())
                    line_out.transform(xform)
                if line_out.isEmpty() or (not line_out.isMultipart() and len(line_out.asPolyline()) < 2):
                    _notify(parent, tr("多点画线"), tr("画线起终点重合，请重新画线。"), warning=True)
                    return None
                line_bbox = line_out.boundingBox()
                if line_bbox.isEmpty() or (line_bbox.width() == 0 and line_bbox.height() == 0):
                    _notify(parent, tr("多点画线"), tr("画线起终点重合，请重新画线。"), warning=True)
                    return None
                if out_crs.isGeographic():
                    margin = max(0.0001, 0.00005)
                else:
                    margin = max(snap_m * 2.0, 1.0)
                rect_expanded = QgsRectangle(
                    line_bbox.xMinimum() - margin,
                    line_bbox.yMinimum() - margin,
                    line_bbox.xMaximum() + margin,
                    line_bbox.yMaximum() + margin,
                )
                da = _distance_area(out_crs)
                candidates = []
                for layer in self.source_point_layers:
                    try:
                        try:
                            layer_crs = layer.crs() if (layer.crs() and layer.crs().isValid()) else out_crs
                        except Exception:
                            layer_crs = out_crs
                        if layer_crs != out_crs:
                            try:
                                xform_layer = QgsCoordinateTransform(out_crs, layer_crs, QgsProject.instance().transformContext())
                                rect_layer = xform_layer.transform(rect_expanded)
                            except Exception:
                                _lpt_skip = True
                            else:
                                _lpt_skip = False
                            if _lpt_skip:
                                continue
                        else:
                            rect_layer = rect_expanded
                        request = QgsFeatureRequest().setFilterRect(rect_layer)
                        for feature in layer.getFeatures(request):
                            geom = feature.geometry()
                            if not geom or geom.isEmpty():
                                continue
                            try:
                                point = geom.asPoint()
                                pt_xy = QgsPointXY(point.x(), point.y())
                            except Exception:
                                _lpt_skip = True
                            else:
                                _lpt_skip = False
                            if _lpt_skip:
                                continue
                            pt_out = self._transform_point(pt_xy, layer_crs, out_crs)
                            if not pt_out:
                                continue
                            pt_geom = QgsGeometry.fromPointXY(pt_out)
                            closest = line_out.nearestPoint(pt_geom)
                            if closest.isEmpty():
                                continue
                            dist = _measure(da, out_crs, pt_out, closest.asPoint())
                            if dist is None or dist > snap_m:
                                continue
                            try:
                                pos = line_out.lineLocatePoint(pt_geom)
                            except Exception:
                                pos = 0.0
                            candidates.append((pos, pt_out))
                    except Exception:
                        _lpt_skip = True
                    else:
                        _lpt_skip = False
                    if _lpt_skip:
                        continue
                candidates.sort(key=lambda item: (item[0], item[1].x(), item[1].y()))
                ordered_points = [point for _pos, point in candidates]
                if len(ordered_points) < 2 and len(candidates) == 0:
                    _notify(parent, tr("多点画线"), tr("沿线附近未找到点。可增大吸附距离或检查点图层。"), warning=True)
                    return None
                if len(ordered_points) < 2:
                    _notify(parent, tr("多点画线"), tr("不足 2 个点，未生成线。"), warning=True)
                    return None
            except Exception:
                ordered_points = []
        else:
            for layer in self.source_point_layers:
                try:
                    try:
                        layer_crs = layer.crs() if (layer.crs() and layer.crs().isValid()) else canvas_crs
                    except Exception:
                        layer_crs = canvas_crs
                    if layer_crs != canvas_crs:
                        try:
                            xform = QgsCoordinateTransform(canvas_crs, layer_crs, QgsProject.instance().transformContext())
                            rect_layer = xform.transform(rect)
                        except Exception:
                            _lpt_skip = True
                        else:
                            _lpt_skip = False
                        if _lpt_skip:
                            continue
                        if polygon:
                            try:
                                polygon_layer = QgsGeometry(polygon)
                                polygon_layer.transform(xform)
                            except Exception:
                                _lpt_skip = True
                            else:
                                _lpt_skip = False
                            if _lpt_skip:
                                continue
                        else:
                            polygon_layer = None
                    else:
                        rect_layer = rect
                        polygon_layer = polygon
                    request = QgsFeatureRequest().setFilterRect(rect_layer)
                    for feature in layer.getFeatures(request):
                        geom = feature.geometry()
                        if not geom or geom.isEmpty():
                            continue
                        try:
                            point = geom.asPoint()
                            pt_xy = QgsPointXY(point.x(), point.y())
                        except Exception:
                            _lpt_skip = True
                        else:
                            _lpt_skip = False
                        if _lpt_skip:
                            continue
                        if polygon_layer:
                            if not polygon_layer.contains(QgsGeometry.fromPointXY(pt_xy)):
                                continue
                        pt_out = self._transform_point(pt_xy, layer_crs, out_crs)
                        if pt_out:
                            ordered_points.append(pt_out)
                except Exception:
                    _lpt_skip = True
                else:
                    _lpt_skip = False
                if _lpt_skip:
                    continue
            ordered_points = _reorder_nearest_neighbor(ordered_points)
        if len(ordered_points) < 2:
            _notify(parent, tr("多点画线"), tr("不足 2 个点，未生成线。"), warning=True)
            return None

        batch_id = str(uuid.uuid4())
        field_name = _unique_batch_field(out_layer)
        added_field = None
        try:
            if out_layer.fields().indexOf(field_name) < 0:
                if not out_layer.isEditable():
                    if callable(getattr(out_layer, "readOnly", None)) and out_layer.readOnly():
                        _notify(parent, tr("多点画线"), tr("指定的线图层是只读的，无法写入。"), warning=True)
                        return None
                    if not out_layer.startEditing():
                        _notify(parent, tr("多点画线"), tr("无法开始编辑指定的线图层。"), warning=True)
                        return None
                out_layer.dataProvider().addAttributes([_make_field(field_name)])
                out_layer.updateFields()
                added_field = field_name
        except Exception:
            _notify(parent, tr("多点画线"), tr("无法在输出图层上写入临时标记字段。"), warning=True)
            return None

        def _pt_key(point, precision=6):
            return (round(point.x(), precision), round(point.y(), precision))

        def _seg_key(first, second):
            left, right = _pt_key(first), _pt_key(second)
            return (left, right) if left <= right else (right, left)

        allow_dup = bool(self._allow_duplicate_lines)
        existing_keys = set()
        if not allow_dup:
            existing_keys.update(_segment_keys_from_line_layer(ref_layer, out_crs, _seg_key))
            try:
                if ref_layer.id() != out_layer.id():
                    existing_keys.update(_segment_keys_from_line_layer(out_layer, out_crs, _seg_key))
            except Exception:
                existing_keys.update(_segment_keys_from_line_layer(out_layer, out_crs, _seg_key))

        try:
            if not out_layer.isEditable():
                if callable(getattr(out_layer, "readOnly", None)) and out_layer.readOnly():
                    if added_field:
                        _drop_field(out_layer, added_field)
                    _notify(parent, tr("多点画线"), tr("指定的线图层是只读的，无法写入。"), warning=True)
                    return None
                if not out_layer.startEditing():
                    if added_field:
                        _drop_field(out_layer, added_field)
                    _notify(parent, tr("多点画线"), tr("无法开始编辑指定的线图层。"), warning=True)
                    return None
        except Exception:
            if added_field:
                _drop_field(out_layer, added_field)
            _notify(parent, tr("多点画线"), tr("无法开始编辑指定的线图层。"), warning=True)
            return None

        skipped_count = 0
        batch_keys = set()
        try:
            for index in range(len(ordered_points) - 1):
                first = ordered_points[index]
                second = ordered_points[index + 1]
                key = _seg_key(first, second)
                if not allow_dup and (key in existing_keys or key in batch_keys):
                    skipped_count += 1
                    continue
                batch_keys.add(key)
                feature = QgsFeature(out_layer.fields())
                feature.setGeometry(QgsGeometry.fromPolylineXY([first, second]))
                try:
                    feature.setAttribute(field_name, batch_id)
                except Exception:
                    pass  # nosec
                if not out_layer.addFeature(feature):
                    out_layer.rollBack()
                    if added_field:
                        _drop_field(out_layer, added_field)
                    _notify(parent, tr("多点画线"), tr("生成线失败。"), warning=True)
                    return None
            if not out_layer.commitChanges():
                try:
                    out_layer.rollBack()
                except Exception:
                    pass  # nosec
                if added_field:
                    _drop_field(out_layer, added_field)
                _notify(parent, tr("多点画线"), tr("生成线失败。"), warning=True)
                return None
        except Exception:
            try:
                out_layer.rollBack()
            except Exception:
                pass  # nosec
            if added_field:
                _drop_field(out_layer, added_field)
            _notify(parent, tr("多点画线"), tr("生成线失败。"), warning=True)
            return None

        fids = []
        try:
            if out_layer.fields().indexOf(field_name) >= 0:
                for feature in out_layer.getFeatures():
                    try:
                        if feature.attribute(field_name) == batch_id:
                            fids.append(feature.id())
                    except Exception:
                        _lpt_skip = True
                    else:
                        _lpt_skip = False
                    if _lpt_skip:
                        continue
        except Exception:
            fids = []
        if added_field:
            _drop_field(out_layer, added_field)
        try:
            out_layer.updateExtents()
            out_layer.triggerRepaint()
        except Exception:
            pass  # nosec
        created_n = len(fids) if fids else len(batch_keys)
        self._undo = {
            "token": _project_token(),
            "layer_id": out_layer.id(),
            "fids": list(fids),
            "batch_id": batch_id,
            "field_name": field_name,
        }
        if created_n <= 0 and skipped_count:
            _notify(parent, tr("多点画线"), tr("未生成新线，已跳过 %d 条重复线段。") % skipped_count)
            return 0
        if skipped_count > 0:
            _notify(parent, tr("多点画线"), tr("已生成 %d 条线，跳过 %d 条重复线段。") % (created_n, skipped_count))
        else:
            _notify(parent, tr("多点画线"), tr("已生成 %d 条线。") % created_n)
        return created_n

    def undo(self, parent):
        state = self._undo
        if not state:
            _notify(parent, tr("多点画线"), tr("没有可撤销的上次生成结果。"), warning=True)
            return
        if state.get("token") != _project_token():
            _notify(parent, tr("多点画线"), tr("撤销只针对当前工程、当前输出层的上一批，不能按旧的要素编号删除。"), warning=True)
            return
        out_layer = None
        try:
            out_layer = QgsProject.instance().mapLayer(state.get("layer_id") or "")
        except Exception:
            out_layer = None
        if out_layer is None:
            _notify(parent, tr("多点画线"), tr("撤销只针对当前工程、当前输出层的上一批，不能按旧的要素编号删除。"), warning=True)
            return
        current_id = ""
        if self._output_mode == 1:
            current_id = self._output_layer_id
        elif self.output_layer is not None:
            try:
                current_id = self.output_layer.id()
            except Exception:
                current_id = ""
        if current_id and current_id != state.get("layer_id"):
            _notify(parent, tr("多点画线"), tr("撤销只针对当前工程、当前输出层的上一批，不能按旧的要素编号删除。"), warning=True)
            return
        try:
            if callable(getattr(out_layer, "readOnly", None)) and out_layer.readOnly():
                _notify(parent, tr("多点画线"), tr("指定的线图层是只读的，无法写入。"), warning=True)
                return
        except Exception:
            pass  # nosec
        fids = list(state.get("fids") or [])
        field_name = state.get("field_name") or ""
        if not fids and state.get("batch_id") and field_name:
            try:
                if out_layer.fields().indexOf(field_name) >= 0:
                    for feature in out_layer.getFeatures():
                        try:
                            if feature.attribute(field_name) == state.get("batch_id"):
                                fids.append(feature.id())
                        except Exception:
                            _lpt_skip = True
                        else:
                            _lpt_skip = False
                        if _lpt_skip:
                            continue
            except Exception:
                pass  # nosec
        if not fids:
            _notify(parent, tr("多点画线"), tr("没有可撤销的上次生成结果。"), warning=True)
            return
        try:
            if not out_layer.isEditable() and not out_layer.startEditing():
                _notify(parent, tr("多点画线"), tr("无法开始编辑指定的线图层。"), warning=True)
                return
        except Exception:
            _notify(parent, tr("多点画线"), tr("无法开始编辑指定的线图层。"), warning=True)
            return
        ok = True
        for fid in fids:
            try:
                if not out_layer.deleteFeature(fid):
                    ok = False
            except Exception:
                ok = False
        try:
            if ok and out_layer.commitChanges():
                _notify(parent, tr("多点画线"), tr("已撤销 %d 条线。") % len(fids))
                self._undo = None
                return
        except Exception:
            pass  # nosec
        try:
            out_layer.rollBack()
        except Exception:
            pass  # nosec
        _notify(parent, tr("多点画线"), tr("撤销失败。"), warning=True)


def _reorder_nearest_neighbor(points):
    if len(points) <= 2:
        return points
    start = min(range(len(points)), key=lambda index: (points[index].x(), points[index].y()))
    remaining = list(points)
    path = [remaining.pop(start)]
    while remaining:
        last = path[-1]
        next_index = min(
            range(len(remaining)),
            key=lambda index: (last.sqrDist(remaining[index]), remaining[index].x(), remaining[index].y()),
        )
        path.append(remaining.pop(next_index))
    return path


def _extract_line_segments(geom):
    segments = []
    if geom.isMultipart():
        for part in geom.asMultiPolyline():
            if len(part) >= 2:
                for index in range(len(part) - 1):
                    segments.append((QgsPointXY(part[index]), QgsPointXY(part[index + 1])))
    else:
        try:
            line = geom.asPolyline()
            if len(line) >= 2:
                for index in range(len(line) - 1):
                    segments.append((QgsPointXY(line[index]), QgsPointXY(line[index + 1])))
        except Exception:
            pass  # nosec
    return segments


def _segment_keys_from_line_layer(line_layer, target_crs, seg_key):
    keys = set()
    try:
        layer_crs = line_layer.crs() if (line_layer.crs() and line_layer.crs().isValid()) else target_crs
    except Exception:
        layer_crs = target_crs
    xform = None
    try:
        if layer_crs != target_crs:
            xform = QgsCoordinateTransform(layer_crs, target_crs, QgsProject.instance().transformContext())
    except Exception:
        xform = None
    try:
        for feature in line_layer.getFeatures():
            geom = feature.geometry()
            if not geom or geom.isEmpty():
                continue
            try:
                for first, second in _extract_line_segments(geom):
                    if xform is not None:
                        try:
                            first = xform.transform(first)
                            second = xform.transform(second)
                        except Exception:
                            pass  # nosec
                    keys.add(seg_key(first, second))
            except Exception:
                _lpt_skip = True
            else:
                _lpt_skip = False
            if _lpt_skip:
                continue
    except Exception:
        pass  # nosec
    return keys


class MultilineDialog(QDialog):
    def __init__(self, iface, controller, parent=None):
        super().__init__(parent)
        self.iface = iface
        self.controller = controller
        self.setObjectName("LayersPanelToolsMultilineDialog")
        self.setModal(False)
        self.setMinimumWidth(500)
        self.setMaximumWidth(620)
        self.setMinimumHeight(560)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(12)

        self.left_panel = QWidget(self)
        left = QVBoxLayout(self.left_panel)
        left.setContentsMargins(0, 0, 0, 0)
        self.layer_title = QLabel(self)
        left.addWidget(self.layer_title)
        self.points_list = QListWidget(self)
        self.points_list.setSelectionMode(qt_attr(QAbstractItemView, "ExtendedSelection"))
        left.addWidget(self.points_list, 1)
        self.left_panel.setSizePolicy(qt_attr(QSizePolicy, "Ignored"), qt_attr(QSizePolicy, "Preferred"))
        layout.addWidget(self.left_panel, 1)

        right_panel = QWidget(self)
        right = QVBoxLayout(right_panel)
        right.setContentsMargins(0, 0, 0, 0)

        self.source_group = QGroupBox(self)
        source = QVBoxLayout(self.source_group)
        self.source_hint = QLabel(self)
        source.addWidget(self.source_hint)
        mode_row = QHBoxLayout()
        self.mode_label = QLabel(self)
        self.select_mode_combo = QComboBox(self)
        self.select_mode_combo.addItem("", 0)
        self.select_mode_combo.addItem("", 1)
        self.select_mode_combo.addItem("", 2)
        mode_row.addWidget(self.mode_label)
        mode_row.addWidget(self.select_mode_combo, 1)
        source.addLayout(mode_row)
        frame_row = QHBoxLayout()
        self.frame_btn = QPushButton(self)
        self.frame_hint = QLabel(self)
        frame_row.addWidget(self.frame_btn)
        frame_row.addWidget(self.frame_hint, 1)
        source.addLayout(frame_row)
        self.snap_container = QWidget(self)
        snap_row = QHBoxLayout(self.snap_container)
        snap_row.setContentsMargins(0, 0, 0, 0)
        self.snap_label = QLabel(self)
        self.snap_spin = QDoubleSpinBox(self)
        self.snap_spin.setRange(0.1, 10000.0)
        self.snap_spin.setDecimals(1)
        self.snap_spin.setSingleStep(0.5)
        self.snap_spin.setValue(3.0)
        snap_row.addWidget(self.snap_label)
        snap_row.addWidget(self.snap_spin, 1)
        source.addWidget(self.snap_container)
        right.addWidget(self.source_group)

        self.ref_group = QGroupBox(self)
        ref_layout = QVBoxLayout(self.ref_group)
        self.ref_hint = QLabel(self)
        self.ref_hint.setWordWrap(True)
        self.reference_combo = QComboBox(self)
        self.allow_duplicate = QCheckBox(self)
        ref_layout.addWidget(self.ref_hint)
        ref_layout.addWidget(self.reference_combo)
        ref_layout.addWidget(self.allow_duplicate)
        right.addWidget(self.ref_group)

        self.output_group = QGroupBox(self)
        out_layout = QVBoxLayout(self.output_group)
        out_row = QHBoxLayout()
        self.output_mode_label = QLabel(self)
        self.output_mode_combo = QComboBox(self)
        self.output_mode_combo.addItem("", 0)
        self.output_mode_combo.addItem("", 1)
        out_row.addWidget(self.output_mode_label)
        out_row.addWidget(self.output_mode_combo, 1)
        out_layout.addLayout(out_row)
        self.temp_crs_container = QWidget(self)
        crs_row = QHBoxLayout(self.temp_crs_container)
        crs_row.setContentsMargins(0, 0, 0, 0)
        self.temp_crs_label = QLabel(self)
        self.temp_crs_btn = QPushButton(self)
        self.temp_crs_value = QLabel(self)
        crs_row.addWidget(self.temp_crs_label)
        crs_row.addWidget(self.temp_crs_btn)
        crs_row.addWidget(self.temp_crs_value, 1)
        out_layout.addWidget(self.temp_crs_container)
        self.output_layer_label = QLabel(self)
        self.output_layer_combo = QComboBox(self)
        out_layout.addWidget(self.output_layer_label)
        out_layout.addWidget(self.output_layer_combo)
        right.addWidget(self.output_group)

        self.auto_group = QGroupBox(self)
        auto_layout = QVBoxLayout(self.auto_group)
        self.auto_checkbox = QCheckBox(self)
        delay_row = QHBoxLayout()
        self.delay_label = QLabel(self)
        self.delay_spin = QSpinBox(self)
        self.delay_spin.setRange(0, 5000)
        self.delay_spin.setSingleStep(50)
        self.delay_spin.setValue(300)
        delay_row.addWidget(self.delay_label)
        delay_row.addWidget(self.delay_spin, 1)
        auto_layout.addWidget(self.auto_checkbox)
        auto_layout.addLayout(delay_row)
        right.addWidget(self.auto_group)

        row1 = QHBoxLayout()
        self.undo_btn = QPushButton(self)
        self.close_btn = QPushButton(self)
        row1.addWidget(self.undo_btn)
        row1.addWidget(self.close_btn)
        right.addLayout(row1)
        row2 = QHBoxLayout()
        self.toggle_btn = QPushButton(self)
        self.refresh_btn = QPushButton(self)
        row2.addWidget(self.toggle_btn)
        row2.addWidget(self.refresh_btn)
        right.addLayout(row2)
        right_panel.setSizePolicy(qt_attr(QSizePolicy, "Ignored"), qt_attr(QSizePolicy, "Preferred"))
        layout.addWidget(right_panel, 3)

        self.frame_btn.clicked.connect(self._start_pick)
        self.undo_btn.clicked.connect(self._undo)
        self.close_btn.clicked.connect(self.close)
        self.toggle_btn.clicked.connect(self._toggle_list)
        self.refresh_btn.clicked.connect(self._refresh_layers)
        self.select_mode_combo.currentIndexChanged.connect(self._on_mode)
        self.output_mode_combo.currentIndexChanged.connect(self._on_output_mode)
        self.temp_crs_btn.clicked.connect(self._choose_crs)
        self.auto_checkbox.toggled.connect(lambda *_args: self._persist())
        self.delay_spin.valueChanged.connect(lambda *_args: self._persist())
        self.snap_spin.valueChanged.connect(lambda *_args: self._persist())
        self.output_layer_combo.currentIndexChanged.connect(lambda *_args: self._persist())
        self.reference_combo.currentIndexChanged.connect(lambda *_args: self._persist())
        self.allow_duplicate.toggled.connect(lambda *_args: self._persist())
        self.points_list.itemSelectionChanged.connect(self._persist)
        self.finished.connect(lambda *_args: self._on_finished())
        self._list_visible = True
        self._warned_specified = False
        self.retranslate()
        subscribe(self, self.retranslate)
        self._refresh_layers()
        self._apply_to_controller()

    def retranslate(self, *_args):
        self.setWindowTitle(tr("多点画线"))
        self.layer_title.setText(tr("点图层选择（可多选）"))
        self.source_group.setTitle(tr("取点方式"))
        self.source_hint.setText(tr("框选范围内的点（支持多图层）"))
        self.mode_label.setText(tr("框选方式"))
        self.select_mode_combo.setItemText(0, tr("矩形框选"))
        self.select_mode_combo.setItemText(1, tr("多边形框选"))
        self.select_mode_combo.setItemText(2, tr("画线框选"))
        self.snap_label.setText(tr("吸附距离"))
        self.snap_spin.setSuffix(" " + tr("米"))
        self.snap_spin.setToolTip(
            tr("默认单位是米。地理坐标系按椭球距离计算；米制投影直接用米；非米制投影时数值为图幅单位。")
        )
        self.ref_group.setTitle(tr("参考线图层（必选）"))
        self.ref_hint.setText(tr("用于检测两点之间是否已有线，避免重复。即使允许重复，也必须选择参考线图层。"))
        self.allow_duplicate.setText(tr("允许生成重复的线"))
        self.output_group.setTitle(tr("输出目标"))
        self.output_mode_label.setText(tr("输出方式"))
        self.output_mode_combo.setItemText(0, tr("临时线图层（内存）"))
        self.output_mode_combo.setItemText(1, tr("指定线图层"))
        self.temp_crs_label.setText(tr("临时图层坐标系"))
        self.temp_crs_btn.setText(tr("选择坐标系…"))
        self.output_layer_label.setText(tr("指定线图层"))
        self.auto_group.setTitle(tr("自动生成设置"))
        self.auto_checkbox.setText(tr("框选或画线后自动生成"))
        self.auto_checkbox.setToolTip(tr("勾选后，框选或画线结束即生成线段，无需再点生成。取消勾选则只取点，不写线。"))
        self.delay_label.setText(tr("延迟（毫秒）"))
        self.undo_btn.setText(tr("撤销"))
        self.close_btn.setText(tr("关闭"))
        self.refresh_btn.setText(tr("刷新图层"))
        self._sync_toggle_text()
        self._sync_frame_text()
        self._update_crs_label()
        apply_direction(self)

    def auto_generate(self):
        # No separate Generate button: generation runs only when this is on (default on).
        return bool(self.auto_checkbox.isChecked())

    def auto_delay(self):
        return int(self.delay_spin.value())

    def select_mode(self):
        return int(self.select_mode_combo.currentIndex())

    def mark_frame(self, is_line, is_polygon):
        if is_line:
            self.frame_hint.setText(tr("已画线"))
        elif is_polygon:
            self.frame_hint.setText(tr("已框选多边形范围"))
        else:
            self.frame_hint.setText(tr("已框选矩形范围"))

    def _sync_toggle_text(self):
        self.toggle_btn.setText(tr("隐藏图层列表") if self._list_visible else tr("显示图层列表"))

    def _sync_frame_text(self):
        line_mode = self.select_mode_combo.currentIndex() == 2
        self.frame_btn.setText(tr("开始画线") if line_mode else tr("开始框选"))
        self.snap_container.setVisible(line_mode)
        if not str(self.frame_hint.text() or "").strip():
            self.frame_hint.setText(tr("（未框选）"))

    def _toggle_list(self):
        self._list_visible = not self._list_visible
        self.left_panel.setVisible(self._list_visible)
        if self._list_visible:
            self.left_panel.setMaximumWidth(16777215)
            self.setMinimumWidth(500)
            self.setMaximumWidth(620)
        else:
            self.left_panel.setMaximumWidth(0)
            self.setMinimumWidth(380)
            self.setMaximumWidth(620)
        self._sync_toggle_text()
        try:
            self.adjustSize()
        except Exception:
            pass  # nosec

    def _on_mode(self, *_args):
        self._sync_frame_text()
        self._persist()

    def _on_output_mode(self, *_args):
        self._toggle_output_widgets()
        if self.output_mode_combo.currentIndex() == 1 and not self._warned_specified:
            self._warned_specified = True
            _notify(
                self,
                tr("多点画线"),
                tr("选择指定线图层后，撤销会用临时字段标记本批生成的线；结束后只删除我们加上的那一列，不会删掉图层里原有的字段。"),
            )
        self._persist()

    def _toggle_output_widgets(self):
        temp = self.output_mode_combo.currentIndex() == 0
        self.temp_crs_container.setVisible(temp)
        self.output_layer_label.setVisible(not temp)
        self.output_layer_combo.setVisible(not temp)
        self._update_crs_label()

    def _update_crs_label(self):
        auth = str(_load_settings().get("temp_line_crs") or "").strip()
        self.temp_crs_value.setText(auth or tr("未设置（将用工程坐标系，再没有则用 EPSG:4326）"))

    def _choose_crs(self):
        try:
            dialog = QgsProjectionSelectionDialog(self)
        except Exception:
            return
        auth = str(_load_settings().get("temp_line_crs") or "").strip()
        try:
            if auth:
                dialog.setCrs(QgsCoordinateReferenceSystem(auth))
            else:
                crs = QgsProject.instance().crs()
                if crs and crs.isValid():
                    dialog.setCrs(crs)
        except Exception:
            pass  # nosec
        if accepted(run_dialog(dialog)):
            try:
                crs = dialog.crs()
                if crs and crs.isValid():
                    data = _load_settings()
                    data["temp_line_crs"] = crs.authid() or ""
                    _save_settings(data)
                    self.controller._temp_line_crs = data["temp_line_crs"]
                    self._update_crs_label()
            except Exception:
                pass  # nosec

    def _refresh_line_combos(self, saved_output, saved_reference):
        self.output_layer_combo.blockSignals(True)
        self.reference_combo.blockSignals(True)
        try:
            self.output_layer_combo.clear()
            self.reference_combo.clear()
            self.reference_combo.addItem(tr("（请选择参考线图层）"), "")
            for layer in list(QgsProject.instance().mapLayers().values()):
                if not _is_line_layer(layer):
                    continue
                self.output_layer_combo.addItem(layer.name(), layer.id())
                self.reference_combo.addItem(layer.name(), layer.id())
            if saved_output:
                index = self.output_layer_combo.findData(saved_output)
                if index >= 0:
                    self.output_layer_combo.setCurrentIndex(index)
            if saved_reference:
                index = self.reference_combo.findData(saved_reference)
                if index >= 0:
                    self.reference_combo.setCurrentIndex(index)
        finally:
            self.output_layer_combo.blockSignals(False)
            self.reference_combo.blockSignals(False)

    def _refresh_layers(self):
        saved = _load_settings()
        selected_ids = {str(item.data(_ID_ROLE) or "") for item in self.points_list.selectedItems()}
        self.points_list.blockSignals(True)
        self.points_list.clear()
        for layer in list(QgsProject.instance().mapLayers().values()):
            if not _is_point_layer(layer):
                continue
            item = QListWidgetItem(_point_layer_caption(layer))
            item.setData(_ID_ROLE, layer.id())
            item.setData(_NAME_ROLE, layer.name() or "")
            self.points_list.addItem(item)
        if saved.get("source_point_layer_ids"):
            selected_ids = set(saved["source_point_layer_ids"])
        elif saved.get("source_point_layer_names") and not selected_ids:
            names = set(saved["source_point_layer_names"])
            for row in range(self.points_list.count()):
                item = self.points_list.item(row)
                stored = str(item.data(_NAME_ROLE) or "")
                if stored in names or item.text() in names:
                    item.setSelected(True)
            selected_ids = None
        if selected_ids is not None:
            for row in range(self.points_list.count()):
                item = self.points_list.item(row)
                if str(item.data(_ID_ROLE) or "") in selected_ids:
                    item.setSelected(True)
        self.points_list.blockSignals(False)
        self.select_mode_combo.blockSignals(True)
        self.output_mode_combo.blockSignals(True)
        self.auto_checkbox.blockSignals(True)
        self.allow_duplicate.blockSignals(True)
        self.snap_spin.blockSignals(True)
        self.delay_spin.blockSignals(True)
        try:
            self.select_mode_combo.setCurrentIndex(int(saved["select_mode_index"]))
            self.output_mode_combo.setCurrentIndex(int(saved["output_mode"]))
            self.auto_checkbox.setChecked(bool(saved["auto_generate"]))
            self.allow_duplicate.setChecked(bool(saved["allow_duplicate_lines"]))
            self.snap_spin.setValue(float(saved["snap_distance_m"]))
            self.delay_spin.setValue(int(saved["auto_generate_delay_ms"]))
        finally:
            self.select_mode_combo.blockSignals(False)
            self.output_mode_combo.blockSignals(False)
            self.auto_checkbox.blockSignals(False)
            self.allow_duplicate.blockSignals(False)
            self.snap_spin.blockSignals(False)
            self.delay_spin.blockSignals(False)
        self._refresh_line_combos(saved.get("output_layer_id"), saved.get("reference_line_layer_id"))
        self.controller._temp_line_crs = saved.get("temp_line_crs") or ""
        self._toggle_output_widgets()
        self._sync_frame_text()

    def _collect(self):
        point_ids = [str(item.data(_ID_ROLE) or "") for item in self.points_list.selectedItems() if item.data(_ID_ROLE)]
        point_names = [
            str(item.data(_NAME_ROLE) or item.text())
            for item in self.points_list.selectedItems()
        ]
        return {
            "source_point_layer_ids": point_ids,
            "source_point_layer_names": point_names,
            "select_mode_index": int(self.select_mode_combo.currentIndex()),
            "auto_generate": bool(self.auto_checkbox.isChecked()),
            "auto_generate_delay_ms": int(self.delay_spin.value()),
            "output_mode": int(self.output_mode_combo.currentIndex()),
            "output_layer_id": str(self.output_layer_combo.currentData() or ""),
            "reference_line_layer_id": str(self.reference_combo.currentData() or ""),
            "allow_duplicate_lines": bool(self.allow_duplicate.isChecked()),
            "snap_distance_m": float(self.snap_spin.value()),
            "temp_line_crs": str(_load_settings().get("temp_line_crs") or ""),
        }

    def _persist(self, *_args):
        data = self._collect()
        _save_settings(data)
        self._apply_to_controller(data)

    def _apply_to_controller(self, data=None):
        data = data or self._collect()
        layers = []
        by_id = {}
        for layer in list(QgsProject.instance().mapLayers().values()):
            if _is_point_layer(layer):
                by_id[layer.id()] = layer
        for layer_id in data.get("source_point_layer_ids") or []:
            if layer_id in by_id:
                layers.append(by_id[layer_id])
        self.controller.source_point_layers = layers
        self.controller._output_mode = int(data.get("output_mode") or 0)
        self.controller._output_layer_id = str(data.get("output_layer_id") or "")
        self.controller._reference_line_layer_id = str(data.get("reference_line_layer_id") or "")
        self.controller._allow_duplicate_lines = bool(data.get("allow_duplicate_lines"))
        self.controller._snap_distance_m = float(data.get("snap_distance_m") or 3.0)
        self.controller._temp_line_crs = str(data.get("temp_line_crs") or "")

    def _start_pick(self):
        self._persist()
        self.controller.start_pick(self.select_mode(), self)

    def _undo(self):
        self._persist()
        self.controller.undo(self)

    def _on_finished(self):
        global _DIALOG
        try:
            self._persist()
        except Exception:
            pass  # nosec
        if _DIALOG is self:
            _DIALOG = None

    def closeEvent(self, event):
        global _DIALOG
        try:
            self._persist()
        except Exception:
            pass  # nosec
        if _DIALOG is self:
            _DIALOG = None
        super().closeEvent(event)
