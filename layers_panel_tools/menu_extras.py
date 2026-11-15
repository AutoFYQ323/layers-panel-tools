# -*- coding: utf-8 -*-
"""第三方插件动作与工具箱算法：供系统属性页加入图层右键。不改、不依赖那些插件或 PROC。"""

import uuid

from qgis.PyQt.QtGui import QIcon

try:
    from qgis.PyQt.QtGui import QAction
except ImportError:
    from qgis.PyQt.QtWidgets import QAction

from .buttons import report
from .i18n import tr

OUR_PLUGIN_IDS = ("layers_panel_tools", "LayersPanelTools")


def new_id(prefix):
    return "%s:%s" % (prefix, uuid.uuid4().hex)


def current_layer(iface):
    if iface is None:
        return None
    layer = None
    try:
        layer = iface.activeLayer()
    except Exception:
        layer = None
    if layer is not None:
        return layer
    try:
        from .scope import selected_layers

        layers = selected_layers(iface)
        if layers:
            return layers[0]
    except Exception:
        return None
    return None


def _is_vector(layer):
    try:
        from qgis.core import QgsVectorLayer

        return isinstance(layer, QgsVectorLayer)
    except Exception:
        return False


def _is_raster(layer):
    try:
        from qgis.core import QgsRasterLayer

        return isinstance(layer, QgsRasterLayer)
    except Exception:
        return False


def _param_type(param):
    try:
        return str(param.type() or "")
    except Exception:
        return ""


def _is_destination(param):
    typ = _param_type(param).lower()
    name = ""
    try:
        name = type(param).__name__
    except Exception:
        name = ""
    if "Destination" in name or typ.endswith("destination") or typ in ("sink", "folderDestination", "fileDestination"):
        return True
    try:
        if callable(getattr(param, "isDestination", None)) and param.isDestination():
            return True
    except Exception:
        pass  # nosec
    return False


def _param_accepts_layer(param, layer):
    if param is None or layer is None or _is_destination(param):
        return False
    typ = _param_type(param).lower()
    name = type(param).__name__
    vectorish = typ in ("vector", "source", "multilayer") or "VectorLayer" in name or "FeatureSource" in name
    rasterish = typ in ("raster",) or "RasterLayer" in name
    mapish = typ in ("layer", "maplayer", "multiplelayers") or name in (
        "QgsProcessingParameterMapLayer",
        "QgsProcessingParameterMultipleLayers",
    )
    if rasterish and not vectorish:
        return _is_raster(layer)
    if vectorish:
        if not _is_vector(layer):
            return False
        types = []
        for reader in ("dataTypes", "allowedDataTypes"):
            probe = getattr(param, reader, None)
            if not callable(probe):
                continue
            try:
                types = list(probe() or [])
            except Exception:
                types = []
            break
        if not types:
            return True
        try:
            from qgis.core import QgsProcessing, QgsWkbTypes

            geom = QgsWkbTypes.geometryType(layer.wkbType())

            def _geom_type(name):
                # Qt6 / QGIS 4: QgsWkbTypes.GeometryType.PointGeometry; Qt5 keeps flat names.
                group = getattr(QgsWkbTypes, "GeometryType", None)
                if group is not None and hasattr(group, name):
                    return getattr(group, name)
                return getattr(QgsWkbTypes, name)

            mapping = {
                getattr(QgsProcessing, "TypeVectorPoint", "TypeVectorPoint"): _geom_type("PointGeometry"),
                getattr(QgsProcessing, "TypeVectorLine", "TypeVectorLine"): _geom_type("LineGeometry"),
                getattr(QgsProcessing, "TypeVectorPolygon", "TypeVectorPolygon"): _geom_type("PolygonGeometry"),
            }
            allowed = []
            any_vector = False
            for item in types:
                if item in (
                    getattr(QgsProcessing, "TypeVector", None),
                    getattr(QgsProcessing, "TypeVectorAnyGeometry", None),
                    getattr(QgsProcessing, "TypeMapLayer", None),
                ):
                    any_vector = True
                    continue
                if item in mapping:
                    allowed.append(mapping[item])
            if any_vector or not allowed:
                return True
            return geom in allowed
        except Exception:
            return True
    if mapish:
        return True
    return False


def algorithm_accepts_layer(alg, layer):
    if alg is None or layer is None:
        return False
    try:
        params = list(alg.parameterDefinitions())
    except Exception:
        return False
    for param in params:
        if _param_accepts_layer(param, layer):
            return True
    return False


def first_layer_param(alg, layer):
    if alg is None or layer is None:
        return ""
    try:
        params = list(alg.parameterDefinitions())
    except Exception:
        return ""
    for param in params:
        if _param_accepts_layer(param, layer):
            try:
                return str(param.name() or "")
            except Exception:
                return ""
    return ""


def list_algorithms():
    found = []
    try:
        from qgis.core import QgsApplication

        registry = QgsApplication.processingRegistry()
        algorithms = list(registry.algorithms())
    except Exception:
        return found
    for alg in algorithms:
        try:
            alg_id = str(alg.id() or "")
            if not alg_id:
                continue
            display = ""
            try:
                display = str(alg.displayName() or "") or alg_id
            except Exception:
                display = alg_id
            provider = ""
            try:
                provider = str(alg.provider().name() if alg.provider() is not None else "")
            except Exception:
                provider = ""
            icon = QIcon()
            try:
                icon = alg.icon() or QIcon()
            except Exception:
                icon = QIcon()
            found.append({"id": alg_id, "label": display, "provider": provider, "icon": icon, "alg": alg})
        except Exception:
            _lpt_skip = True
        else:
            _lpt_skip = False
        if _lpt_skip:
            continue
    found.sort(key=lambda item: (item.get("provider") or "", item.get("label") or "", item.get("id") or ""))
    return found


def _walk_leaf_actions(action, seen):
    if action is None:
        return
    ident = id(action)
    if ident in seen:
        return
    seen.add(ident)
    try:
        if action.isSeparator():
            return
    except Exception:
        return
    menu = None
    try:
        menu = action.menu()
    except Exception:
        menu = None
    if menu is not None:
        try:
            children = list(menu.actions())
        except Exception:
            children = []
        for child in children:
            for item in _walk_leaf_actions(child, seen):
                yield item
        return
    yield action


def list_plugin_actions():
    found = []
    seen = set()
    plugins = {}
    try:
        from qgis import utils as qgis_utils

        plugins = dict(getattr(qgis_utils, "plugins", {}) or {})
    except Exception:
        plugins = {}
    for plugin_id, plugin in plugins.items():
        if str(plugin_id) in OUR_PLUGIN_IDS:
            continue
    # continue below after collecting from each plugin
    for plugin_id, plugin in plugins.items():
        if str(plugin_id) in OUR_PLUGIN_IDS or plugin is None:
            continue
        actions = []
        for name in dir(plugin):
            if name.startswith("_"):
                continue
            try:
                value = getattr(plugin, name)
            except Exception:
                _lpt_skip = True
            else:
                _lpt_skip = False
            if _lpt_skip:
                continue
            if isinstance(value, QAction):
                actions.append(value)
            elif isinstance(value, (list, tuple)):
                for item in value:
                    if isinstance(item, QAction):
                        actions.append(item)
        iface = getattr(plugin, "iface", None)
        window = None
        try:
            if iface is not None:
                window = iface.mainWindow()
        except Exception:
            window = None
        # Prefer actions owned by this plugin object; do not scrape the whole main window.
        for action in actions:
            for leaf in _walk_leaf_actions(action, seen):
                label = ""
                try:
                    label = str(leaf.text() or "").replace("&", "").strip()
                except Exception:
                    label = ""
                if not label:
                    continue
                object_name = ""
                try:
                    object_name = str(leaf.objectName() or "")
                except Exception:
                    object_name = ""
                icon = QIcon()
                try:
                    icon = leaf.icon() or QIcon()
                except Exception:
                    icon = QIcon()
                found.append(
                    {
                        "plugin_id": str(plugin_id),
                        "object_name": object_name,
                        "label": label,
                        "icon": icon,
                        "action": leaf,
                    }
                )
    found.sort(key=lambda item: (item.get("plugin_id") or "", item.get("label") or ""))
    return found


def find_plugin_action(entry):
    plugin_id = str((entry or {}).get("plugin_id") or "")
    object_name = str((entry or {}).get("object_name") or "")
    label = str((entry or {}).get("label") or "").replace("&", "").strip()
    if not plugin_id:
        return None
    plugins = {}
    try:
        from qgis import utils as qgis_utils

        plugins = dict(getattr(qgis_utils, "plugins", {}) or {})
    except Exception:
        return None
    plugin = plugins.get(plugin_id)
    if plugin is None:
        return None
    matches = []
    seen = set()
    for name in dir(plugin):
        if name.startswith("_"):
            continue
        try:
            value = getattr(plugin, name)
        except Exception:
            _lpt_skip = True
        else:
            _lpt_skip = False
        if _lpt_skip:
            continue
        candidates = []
        if isinstance(value, QAction):
            candidates = [value]
        elif isinstance(value, (list, tuple)):
            candidates = [item for item in value if isinstance(item, QAction)]
        for action in candidates:
            for leaf in _walk_leaf_actions(action, seen):
                try:
                    leaf_name = str(leaf.objectName() or "")
                    leaf_label = str(leaf.text() or "").replace("&", "").strip()
                except Exception:
                    _lpt_skip = True
                else:
                    _lpt_skip = False
                if _lpt_skip:
                    continue
                if object_name and leaf_name == object_name:
                    return leaf
                if leaf_label and label and leaf_label == label:
                    matches.append(leaf)
    if len(matches) == 1:
        return matches[0]
    return matches[0] if matches else None


def find_algorithm(alg_id):
    if not alg_id:
        return None
    try:
        from qgis.core import QgsApplication

        return QgsApplication.processingRegistry().algorithmById(str(alg_id))
    except Exception:
        return None


def trigger_thirdparty(iface, entry, parent=None):
    kind = str((entry or {}).get("kind") or "")
    layer = current_layer(iface)
    if layer is None:
        report(parent, tr("添加第三方功能"), tr("没有当前图层，无法运行该功能。"), warning=True)
        return
    if kind == "algorithm":
        alg_id = str(entry.get("alg_id") or "")
        alg = find_algorithm(alg_id)
        if alg is None:
            report(parent, tr("添加第三方功能"), tr("对方插件已卸载，或这个功能已经不可用。"), warning=True)
            return
        if not algorithm_accepts_layer(alg, layer):
            report(parent, tr("添加第三方功能"), tr("这个功能不能对着当前图层使用。"), warning=True)
            return
        param_name = first_layer_param(alg, layer)
        params = {}
        if param_name:
            params[param_name] = layer
        try:
            try:
                from qgis import processing
            except Exception:
                import processing
            processing.execAlgorithmDialog(alg_id, params)
        except Exception:
            report(parent, tr("添加第三方功能"), tr("打开该算法对话框失败。"), warning=True)
        return
    if kind == "plugin_action":
        action = find_plugin_action(entry)
        if action is None:
            report(parent, tr("添加第三方功能"), tr("对方插件已卸载，或这个功能已经不可用。"), warning=True)
            return
        try:
            action.trigger()
        except Exception:
            report(parent, tr("添加第三方功能"), tr("运行该功能失败。"), warning=True)
        return
    report(parent, tr("添加第三方功能"), tr("对方插件已卸载，或这个功能已经不可用。"), warning=True)


def can_add_entry(iface, entry):
    layer = current_layer(iface)
    if layer is None:
        return False, tr("请先在图层面板里选中一个图层，再添加能对着当前图层使用的功能。")
    kind = str((entry or {}).get("kind") or "")
    if kind == "algorithm":
        alg = entry.get("alg") or find_algorithm(entry.get("alg_id"))
        if alg is None:
            return False, tr("对方插件已卸载，或这个功能已经不可用。")
        if not algorithm_accepts_layer(alg, layer):
            return False, tr("这个功能不能对着当前图层使用。")
        return True, ""
    if kind == "plugin_action":
        # A leaf action is offered only when a current layer exists; the original
        # action is triggered as-is and never has its title rewritten.
        return True, ""
    return False, tr("这个功能不能对着当前图层使用。")
