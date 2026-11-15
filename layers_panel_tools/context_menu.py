# -*- coding: utf-8 -*-
"""图层面板右键菜单：调顺序、改显示名、隐藏，并用下拉框加入适合的本插件功能。"""

import json

from qgis.PyQt.QtCore import QEvent, QSize, Qt, QTimer
from qgis.PyQt.QtGui import QFont, QIcon

try:
    from qgis.PyQt.QtGui import QAction
except ImportError:
    from qgis.PyQt.QtWidgets import QAction

from qgis.PyQt.QtWidgets import (
    QAbstractItemView,
    QCheckBox,
    QComboBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMenu,
    QPushButton,
    QSizePolicy,
    QToolBar,
    QToolButton,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from .buttons import report
from .i18n import apply_direction, subscribe, tr
from .icons import load_icon
from .menu_extras import (
    algorithm_accepts_layer,
    can_add_entry,
    list_plugin_actions,
    new_id,
    trigger_thirdparty,
)
from . import shared_toolbar
from .plugin_settings import flush, plugin_qsettings
from .qt_compat import accepted, enum_int, qt_attr, run_dialog, user_role

_KEY = "menu_context"
_HOST = None
MAX_GROUPS = 20
# Solid, high-contrast text colors only (no row background). Users can override per group.
_GROUP_PALETTE = (
    "#E53935",
    "#1565C0",
    "#2E7D32",
    "#EF6C00",
    "#6A1B9A",
    "#00838F",
    "#C62828",
    "#283593",
    "#AD1457",
    "#0277BD",
    "#558B2F",
    "#D84315",
    "#4527A0",
    "#00695C",
    "#F57F17",
    "#5D4037",
    "#455A64",
    "#00897B",
    "#7B1FA2",
    "#E65100",
)

# 对着当前图层能做的功能，以及图层管理、按多边形选择、图层开关、底图切换、分类导出。
CANDIDATES = (
    ("lpt:solo", "独显图层"),
    ("lpt:flash", "闪烁定位"),
    ("lpt:opacity", "透明度"),
    ("lpt:layer_tags", "图层颜色标签"),
    ("lpt:repair", "修复数据源"),
    ("lpt:copy_files", "复制图层文件"),
    ("lpt:layer_ops", "图层操作"),
    ("lpt:class_export", "分类导出"),
    ("lpt:layer_manager", "图层管理"),
    ("lpt:poly_select", "按多边形选择"),
    ("lpt:switch", "图层开关"),
    ("lpt:basemap", "底图切换"),
)
_CANDIDATE_IDS = {item[0]: item[1] for item in CANDIDATES}

_ID = user_role()
_KIND = user_role(1)
_TITLE = user_role(2)
_GROUP = user_role(3)
_EXTRA = user_role(4)
_TB = user_role(5)
_RC = user_role(6)
_EXTRA_ICON = user_role(7)


_HOST = None
_IFACE = None


def bind_host(host, iface=None):
    global _HOST, _IFACE
    _HOST = host
    if iface is not None:
        _IFACE = iface


def _empty():
    return {
        "order": [],
        "hidden": [],
        "titles": {},
        "labels": {},
        "added": [],
        "thirdparty": [],
        "groups": [],
        "membership": {},
        "collapsed": [],
        "group_colors": {},
        "toolbar_hidden": [],
        "toolbar_proxies": [],
        "thirdparty_toolbar_hidden": [],
        "toolbar_homes": {},
    }


def _group_palette_entry(index):
    if index < 0:
        index = 0
    return _GROUP_PALETTE[int(index) % len(_GROUP_PALETTE)]


def _group_title_color(color_spec):
    """Normalize a stored color to a #RRGGBB text color. No background is applied."""
    if isinstance(color_spec, (tuple, list)) and color_spec:
        color_spec = color_spec[0]
    text = str(color_spec or "").strip()
    if len(text) == 7 and text.startswith("#"):
        return text
    if len(text) == 9 and text.startswith("#"):
        return text[:7]
    return "#c00000"


def _clean_group_colors(data, group_ids):
    source = data if isinstance(data, dict) else {}
    found = {}
    allowed = set(group_ids or [])
    for key, value in source.items():
        key = str(key)
        if key not in allowed:
            continue
        color = _group_title_color(value)
        if color:
            found[key] = color
    return found


def _clean_thirdparty(items):
    found = []
    seen = set()
    for item in items or []:
        if not isinstance(item, dict):
            continue
        key = str(item.get("id") or "")
        kind = str(item.get("kind") or "")
        if not key.startswith("tp:") or kind not in ("plugin_action", "algorithm"):
            continue
        if key in seen:
            continue
        seen.add(key)
        entry = {
            "id": key,
            "kind": kind,
            "plugin_id": str(item.get("plugin_id") or ""),
            "object_name": str(item.get("object_name") or ""),
            "label": str(item.get("label") or ""),
            "alg_id": str(item.get("alg_id") or ""),
        }
        found.append(entry)
    return found


def _clean_groups(items):
    found = []
    seen = set()
    for item in items or []:
        if not isinstance(item, dict):
            continue
        key = str(item.get("id") or "")
        if not key.startswith("grp:") or key in seen:
            continue
        seen.add(key)
        found.append({"id": key, "title": str(item.get("title") or "").strip()})
    return found


def _clean_membership(data, allowed):
    source = data if isinstance(data, dict) else {}
    found = {}
    groups = {item for item in allowed if str(item).startswith("grp:")}
    for key, group_id in source.items():
        key = str(key)
        group_id = str(group_id or "")
        if not key or key not in allowed or group_id not in groups or key.startswith("grp:"):
            continue
        found[key] = group_id
    return found


def load_menu():
    try:
        raw = plugin_qsettings().value(_KEY, "")
    except Exception:
        raw = ""
    if raw in (None, ""):
        return _empty()
    if not isinstance(raw, str):
        raw = str(raw)
    try:
        data = json.loads(raw)
    except Exception:
        return _empty()
    if not isinstance(data, dict):
        return _empty()
    found = _empty()
    found["order"] = [str(item) for item in data.get("order") or [] if str(item)]
    found["hidden"] = [str(item) for item in data.get("hidden") or [] if str(item)]
    titles = data.get("titles") if isinstance(data.get("titles"), dict) else {}
    labels = data.get("labels") if isinstance(data.get("labels"), dict) else {}
    found["titles"] = {str(key): str(value) for key, value in titles.items() if str(value or "").strip()}
    found["labels"] = {str(key): str(value) for key, value in labels.items() if str(value or "").strip()}
    found["added"] = [str(item) for item in data.get("added") or [] if str(item) in _CANDIDATE_IDS]
    found["thirdparty"] = _clean_thirdparty(data.get("thirdparty"))
    found["groups"] = _clean_groups(data.get("groups"))
    allowed = set(found["order"]) | set(found["added"]) | {item["id"] for item in found["thirdparty"]} | {item["id"] for item in found["groups"]}
    for item in found["thirdparty"]:
        if item["id"] not in found["order"]:
            found["order"].append(item["id"])
    for item in found["groups"]:
        if item["id"] not in found["order"]:
            found["order"].append(item["id"])
    found["membership"] = _clean_membership(data.get("membership"), allowed)
    group_ids = {item["id"] for item in found["groups"]}
    found["collapsed"] = [
        str(item) for item in data.get("collapsed") or [] if str(item) in group_ids
    ]
    found["group_colors"] = _clean_group_colors(data.get("group_colors"), group_ids)
    found["toolbar_hidden"] = [str(item) for item in data.get("toolbar_hidden") or [] if str(item)]
    # Legacy key kept empty: third-party items never hang on the Layers panel toolbar.
    found["toolbar_proxies"] = []
    found["thirdparty_toolbar_hidden"] = [
        str(item) for item in data.get("thirdparty_toolbar_hidden") or [] if str(item).startswith("tp:")
    ]
    homes = data.get("toolbar_homes") if isinstance(data.get("toolbar_homes"), dict) else {}
    found["toolbar_homes"] = {}
    for key, value in homes.items():
        if not isinstance(value, dict):
            continue
        name = str(value.get("name") or "")
        if not name:
            continue
        found["toolbar_homes"][str(key)] = {
            "name": name,
            "index": value.get("index", -1),
            "before": str(value.get("before") or ""),
        }
    return found



def save_menu(data):
    order = [str(item) for item in data.get("order") or [] if str(item)]
    allowed = set(order) | set(data.get("added") or [])
    payload = {
        "order": order,
        "hidden": list(data.get("hidden") or []),
        "titles": dict(data.get("titles") or {}),
        "labels": dict(data.get("labels") or {}),
        "added": [item for item in data.get("added") or [] if item in _CANDIDATE_IDS],
        "thirdparty": _clean_thirdparty(data.get("thirdparty")),
        "groups": _clean_groups(data.get("groups")),
        "membership": _clean_membership(data.get("membership"), allowed | {item["id"] for item in _clean_thirdparty(data.get("thirdparty"))} | {item["id"] for item in _clean_groups(data.get("groups"))}),
        "collapsed": [
            str(item)
            for item in data.get("collapsed") or []
            if str(item) in {entry["id"] for entry in _clean_groups(data.get("groups"))}
        ],
        "group_colors": _clean_group_colors(
            data.get("group_colors"),
            {entry["id"] for entry in _clean_groups(data.get("groups"))},
        ),
        "toolbar_hidden": [str(item) for item in data.get("toolbar_hidden") or [] if str(item)],
        "toolbar_proxies": [],
        "thirdparty_toolbar_hidden": [
            str(item) for item in data.get("thirdparty_toolbar_hidden") or [] if str(item).startswith("tp:")
        ],
        "toolbar_homes": shared_toolbar.dump_homes() or dict(data.get("toolbar_homes") or {}),
    }
    settings = plugin_qsettings()
    settings.setValue(_KEY, json.dumps(payload, ensure_ascii=False))
    flush()


def _clean_text(text):
    return str(text or "").replace("&", "").strip()


def _unique(base, seen):
    if base not in seen:
        return base
    number = 2
    while "%s#%d" % (base, number) in seen:
        number += 1
    return "%s#%d" % (base, number)


def describe_menu(menu):
    """(key, label, separator?) for each top-level action. Submenus stay one item."""
    actions = list(menu.actions()) if menu is not None else []
    found = []
    seen = set()
    for index, action in enumerate(actions):
        try:
            if action.property("lpt_ctx_id"):
                continue
            name = action.objectName() or ""
            if name.startswith("LayersPanelTools"):
                continue
        except Exception:
            _lpt_skip = True
        else:
            _lpt_skip = False
        if _lpt_skip:
            continue
        if action.isSeparator():
            anchor = ""
            for later in actions[index + 1:]:
                try:
                    if later.isSeparator():
                        continue
                    anchor = later.objectName() or _clean_text(later.text())
                except Exception:
                    _lpt_skip = True
                else:
                    _lpt_skip = False
                if _lpt_skip:
                    continue
                if anchor:
                    break
            key = _unique("sep:" + (anchor or str(index)), seen)
            seen.add(key)
            found.append((key, "", True))
            continue
        try:
            object_name = action.objectName() or ""
            label = _clean_text(action.text())
        except Exception:
            _lpt_skip = True
        else:
            _lpt_skip = False
        if _lpt_skip:
            continue
        if object_name:
            base = "obj:" + object_name
        else:
            base = "txt:" + (label or str(index))
        key = _unique(base, seen)
        seen.add(key)
        found.append((key, label, False))
    return found


def _remember(pairs, refresh_labels):
    data = load_menu()
    changed = False
    known = set(data["order"])
    for key, label, _separator in pairs:
        if key not in known:
            data["order"].append(key)
            known.add(key)
            changed = True
        if not label:
            continue
        saved_title = str(data["titles"].get(key) or "").strip()
        if saved_title and label == saved_title and data["labels"].get(key):
            continue
        if refresh_labels or key not in data["labels"]:
            if data["labels"].get(key) != label:
                data["labels"][key] = label
                changed = True
    if changed:
        save_menu(data)
    return data


def snapshot(iface):
    if iface is None:
        return []
    try:
        view = iface.layerTreeView()
    except Exception:
        view = None
    if view is None:
        return []
    try:
        provider = view.menuProvider()
    except Exception:
        provider = None
    if provider is None:
        return []
    try:
        menu = provider.createContextMenu()
    except Exception:
        return []
    if menu is None:
        return []
    try:
        return describe_menu(menu)
    finally:
        try:
            menu.deleteLater()
        except Exception:
            pass  # nosec


def _is_menu_native_key(key):
    """True for QGIS/other-plugin layer-menu items, not our adds/groups/separators."""
    key = str(key or "")
    if not key:
        return False
    if key in _CANDIDATE_IDS or key.startswith("lpt:"):
        return False
    if key.startswith("tp:") or key.startswith("grp:") or key.startswith("sep:"):
        return False
    return True


def _merge_uncaptured_commit(previous, order, hidden, titles, toolbar_hidden):
    """Keep saved native order/visibility when the page never captured the layer menu."""
    previous = previous or {}
    saved_order = [str(item) for item in (previous.get("order") or []) if str(item)]
    saved_natives = [key for key in saved_order if _is_menu_native_key(key)]
    non_native_order = [key for key in order if not _is_menu_native_key(key)]
    known = set(saved_natives)
    merged_order = list(saved_natives)
    for key in non_native_order:
        if key in known:
            continue
        merged_order.append(key)
        known.add(key)
    saved_hidden_natives = [
        key for key in (previous.get("hidden") or []) if _is_menu_native_key(str(key))
    ]
    ui_hidden_non = [key for key in hidden if not _is_menu_native_key(key)]
    merged_hidden = list(saved_hidden_natives) + ui_hidden_non
    merged_titles = {
        str(key): str(value)
        for key, value in dict(previous.get("titles") or {}).items()
        if _is_menu_native_key(str(key)) and str(value or "").strip()
    }
    for key, value in dict(titles or {}).items():
        if _is_menu_native_key(key):
            continue
        text = str(value or "").strip()
        if text:
            merged_titles[key] = text
    saved_toolbar_hidden = [
        key for key in (previous.get("toolbar_hidden") or []) if _is_menu_native_key(str(key))
    ]
    ui_toolbar_non = [key for key in toolbar_hidden if not _is_menu_native_key(key)]
    merged_toolbar_hidden = list(saved_toolbar_hidden) + ui_toolbar_non
    return merged_order, merged_hidden, merged_titles, merged_toolbar_hidden


def _toolbar_custom(button_id):
    host = _HOST
    if host is None:
        return ""
    try:
        return str(host.titles.get(button_id) or "").strip()
    except Exception:
        return ""


def _shown_title(key, saved):
    """右键上只显示自定义名。本插件按钮的自定义名跟工具条是同一份。"""
    if key in _CANDIDATE_IDS:
        return _toolbar_custom(key)
    text = str(saved or "").strip()
    if not text and _is_thirdparty(key):
        return _toolbar_custom(key)
    return text


def _is_group(key):
    return str(key or "").startswith("grp:")


def _is_thirdparty(key):
    return str(key or "").startswith("tp:")


def _display_name(base, custom):
    custom = str(custom or "").strip()
    base = str(base or "")
    if not custom:
        return base
    return "%s(%s)" % (base, custom)


def _toolbar_action(button_id):
    host = _HOST
    if host is None:
        return None
    try:
        return host.by_id.get(button_id)
    except Exception:
        return None


def _icon_for(button_id):
    action = _toolbar_action(button_id)
    if action is not None:
        try:
            icon = action.icon()
            if icon is not None and not icon.isNull():
                return icon
        except Exception:
            pass  # nosec
    return QIcon()


def _copy_tool_menu(button_id, proxy):
    proxy.clear()
    action = _toolbar_action(button_id)
    widget = None
    if action is not None:
        getter = getattr(action, "defaultWidget", None)
        if callable(getter):
            try:
                widget = getter()
            except Exception:
                widget = None
    source = None
    if widget is not None:
        try:
            source = widget.menu()
        except Exception:
            source = None
    if source is None:
        from . import subcommands

        iface = _IFACE
        if iface is None:
            return
        for sub_id, _msgid, _runner in subcommands.subcommands_of(button_id):
            subcommands.add_to_menu(iface, button_id, proxy, sub_id)
        return
    try:
        source.aboutToShow.emit()
    except Exception:
        pass  # nosec
    for item in list(source.actions()):
        proxy.addAction(item)


def _plugin_action(menu, button_id, title):
    msgid = _CANDIDATE_IDS.get(button_id, button_id)
    text = title or tr(msgid)
    action = QAction(_icon_for(button_id), text, menu)
    action.setProperty("lpt_ctx_id", button_id)
    tool = _toolbar_action(button_id)
    widget = None
    if tool is not None:
        getter = getattr(tool, "defaultWidget", None)
        if callable(getter):
            try:
                widget = getter()
            except Exception:
                widget = None
    has_menu = False
    if widget is not None:
        try:
            has_menu = widget.menu() is not None
        except Exception:
            has_menu = False
    if not has_menu:
        from . import subcommands

        has_menu = subcommands.has_subcommands(button_id)
    if has_menu:
        sub = QMenu(menu)
        sub.aboutToShow.connect(lambda bid=button_id, box=sub: _copy_tool_menu(bid, box))
        action.setMenu(sub)
        return action

    def fire(_checked=False, bid=button_id):
        target = _toolbar_action(bid)
        button = None
        if target is not None:
            getter = getattr(target, "defaultWidget", None)
            if callable(getter):
                try:
                    button = getter()
                except Exception:
                    button = None
        if button is not None:
            try:
                button.click()
                return
            except Exception:
                pass  # nosec
        if target is not None:
            try:
                target.trigger()
            except Exception:
                pass  # nosec

    action.triggered.connect(fire)
    return action


def _native_menu_proxy(menu, action, title):
    """Right-click-only stand-in so a custom title never mutates the original QAction."""
    text = title or ""
    try:
        icon = action.icon()
    except Exception:
        icon = None
    proxy = QAction(icon, text, menu) if icon is not None else QAction(text, menu)
    proxy.setProperty("lpt_ctx_id", "proxy:" + (action.objectName() or text))
    try:
        proxy.setCheckable(action.isCheckable())
        proxy.setChecked(action.isChecked())
        proxy.setEnabled(action.isEnabled())
        proxy.setToolTip(action.toolTip())
        proxy.setStatusTip(action.statusTip())
    except Exception:
        pass  # nosec

    def fire(_checked=False, src=action):
        try:
            src.trigger()
        except Exception:
            pass  # nosec

    proxy.triggered.connect(fire)
    return proxy


def _action_on_main_toolbars(iface, action):
    if iface is None or action is None:
        return False
    try:
        window = iface.mainWindow()
    except Exception:
        return False
    if window is None:
        return False
    try:
        toolbars = list(window.findChildren(QToolBar))
    except Exception:
        toolbars = []
    for toolbar in toolbars:
        try:
            actions = list(toolbar.actions())
        except Exception:
            actions = []
        if action in actions:
            return True
    return False


def apply_thirdparty_original_visibility(iface, data=None, restore_all=False):
    """Show/hide original third-party plugin actions (PROC-style), not only our Layers proxy."""
    if data is None:
        data = load_menu()
    hidden = set() if restore_all else set(str(item) for item in (data.get("thirdparty_toolbar_hidden") or []))
    for entry in data.get("thirdparty") or []:
        if not isinstance(entry, dict) or entry.get("kind") != "plugin_action":
            continue
        key = str(entry.get("id") or "")
        action = None
        try:
            from .menu_extras import find_plugin_action

            action = find_plugin_action(entry)
        except Exception:
            action = None
        if action is None:
            continue
        show = key not in hidden
        try:
            action.setVisible(show)
        except Exception:
            pass  # nosec
        if iface is None:
            continue
        try:
            if show:
                if not _action_on_main_toolbars(iface, action):
                    iface.addToolBarIcon(action)
            else:
                iface.removeToolBarIcon(action)
        except Exception:
            pass  # nosec


def apply_system_side_effects(iface, data=None, restore_toolbars=False):
    """Apply shared-action toolbar membership and third-party proxies after settings are saved."""
    if data is None:
        data = load_menu()
    shared_toolbar.apply_membership(iface, data, restore_all=restore_toolbars)
    try:
        apply_thirdparty_original_visibility(iface, data, restore_all=restore_toolbars)
    except Exception:
        pass  # nosec
    host = _HOST
    if host is not None and hasattr(host, "sync_thirdparty_proxies"):
        try:
            host.sync_thirdparty_proxies(data)
        except Exception:
            pass  # nosec


def apply_menu(menu, iface):
    """QGIS 生成菜单之后调用：重排、改名、隐藏，再插入用户加进来的功能。"""
    if menu is None:
        return
    described = []
    actions = []
    for key, label, separator in describe_menu(menu):
        described.append((key, label, separator))
    by_key = {}
    seen = set()
    raw = list(menu.actions())
    # describe_menu and this walk must agree. Rebuild the map from the same rules.
    for index, action in enumerate(raw):
        try:
            if action.property("lpt_ctx_id"):
                continue
            name = action.objectName() or ""
            if name.startswith("LayersPanelTools"):
                continue
        except Exception:
            _lpt_skip = True
        else:
            _lpt_skip = False
        if _lpt_skip:
            continue
        if action.isSeparator():
            anchor = ""
            for later in raw[index + 1:]:
                try:
                    if later.isSeparator():
                        continue
                    anchor = later.objectName() or _clean_text(later.text())
                except Exception:
                    _lpt_skip = True
                else:
                    _lpt_skip = False
                if _lpt_skip:
                    continue
                if anchor:
                    break
            key = _unique("sep:" + (anchor or str(index)), seen)
        else:
            try:
                object_name = action.objectName() or ""
                label = _clean_text(action.text())
            except Exception:
                _lpt_skip = True
            else:
                _lpt_skip = False
            if _lpt_skip:
                continue
            base = ("obj:" + object_name) if object_name else ("txt:" + (label or str(index)))
            key = _unique(base, seen)
        seen.add(key)
        by_key[key] = action
        actions.append(action)

    data = _remember([(key, label, sep) for key, label, sep in described], refresh_labels=False)
    # Restore titles only. Never apply_membership on the right-click hot path —
    # scanning/rewriting main-window toolbars here made Layer Properties lag for seconds.
    for key, action in by_key.items():
        if action is None or action.isSeparator():
            continue
        shared_toolbar.restore_action_text(action, key, data)
    hidden = set(data["hidden"])

    titles = data["titles"]
    added = [item for item in data["added"] if item in _CANDIDATE_IDS]
    thirdparty = {item["id"]: item for item in data.get("thirdparty") or []}
    groups = {item["id"]: item for item in data.get("groups") or []}
    membership = dict(data.get("membership") or {})
    present = set(by_key) | set(added) | set(thirdparty) | set(groups)
    order = [key for key in data["order"] if key in present]
    for key in by_key:
        if key not in order:
            order.append(key)
    for key in added:
        if key not in order:
            order.append(key)
    for key in list(thirdparty) + list(groups):
        if key not in order:
            order.append(key)
    for action in raw:
        try:
            menu.removeAction(action)
        except Exception:
            pass  # nosec

    def _add_native(key):
        action = by_key[key]
        if key in hidden:
            # Leave the original action alone: hide means "do not add to this menu".
            if not action.isSeparator():
                custom = _shown_title(key, titles.get(key))
                shared_toolbar.capture_base_text(action, custom)
                shared_toolbar.restore_action_text(action, key, data)
            return
        custom = ""
        if not action.isSeparator():
            custom = _shown_title(key, titles.get(key))
            shared_toolbar.capture_base_text(action, custom)
            shared_toolbar.restore_action_text(action, key, data)
        try:
            if custom and not action.isSeparator():
                menu.addAction(_native_menu_proxy(menu, action, custom))
            else:
                menu.addAction(action)
        except Exception:
            return

    def _child_action(owner, key):
        if key in _CANDIDATE_IDS:
            return _plugin_action(owner, key, _shown_title(key, ""))
        entry = thirdparty.get(key)
        if entry is not None:
            return _thirdparty_action(owner, entry, _shown_title(key, entry.get("label")), iface)
        action = by_key.get(key)
        if action is None or action.isSeparator():
            return None
        custom = _shown_title(key, titles.get(key))
        shared_toolbar.capture_base_text(action, custom)
        shared_toolbar.restore_action_text(action, key, data)
        if custom:
            return _native_menu_proxy(owner, action, custom)
        # Submenus need a proxy so the original QAction is not reparented out of QGIS.
        try:
            if action.menu() is not None:
                return _native_menu_proxy(owner, action, _clean_text(action.text()) or key)
        except Exception:
            pass  # nosec
        return _native_menu_proxy(owner, action, _clean_text(action.text()) or key)

    for key in order:
        if membership.get(key):
            continue
        if key in groups:
            members = [item for item in order if membership.get(item) == key and item not in hidden and item in present]
            # Empty groups stay in settings only; the live right-click menu skips them.
            if not members or key in hidden:
                continue
            title = _shown_title(key, groups[key].get("title")) or groups[key].get("title") or tr("未命名组")
            group_action = QAction(title, menu)
            group_action.setProperty("lpt_ctx_id", key)
            submenu = QMenu(menu)
            for child_key in members:
                child = _child_action(submenu, child_key)
                if child is not None:
                    submenu.addAction(child)
            group_action.setMenu(submenu)
            try:
                menu.addAction(group_action)
            except Exception:
                _lpt_skip = True
            else:
                _lpt_skip = False
            if _lpt_skip:
                continue
            continue
        if key in by_key:
            _add_native(key)
            continue
        if key in hidden:
            continue
        child = _child_action(menu, key)
        if child is not None:
            try:
                menu.addAction(child)
            except Exception:
                _lpt_skip = True
            else:
                _lpt_skip = False
            if _lpt_skip:
                continue


def _thirdparty_icon(entry):
    """Resolve icon only when building a menu item; never block the settings list fill."""
    entry = entry or {}
    icon = entry.get("icon")
    if icon is not None and not getattr(icon, "isNull", lambda: True)():
        return icon
    try:
        if entry.get("kind") == "plugin_action":
            from .menu_extras import find_plugin_action

            source = find_plugin_action(entry)
            if source is not None:
                icon = source.icon()
                if icon is not None and not icon.isNull():
                    return icon
    except Exception:
        pass  # nosec
    try:
        if entry.get("kind") == "algorithm":
            from .menu_extras import find_algorithm

            alg = find_algorithm(entry.get("alg_id"))
            if alg is not None:
                icon = alg.icon() if hasattr(alg, "icon") else None
                if icon is not None and not icon.isNull():
                    return icon
    except Exception:
        pass  # nosec
    return QIcon()


def _thirdparty_action(menu, entry, title, iface):
    text = title or str((entry or {}).get("label") or "")
    icon = _thirdparty_icon(entry)
    action = QAction(icon, text, menu) if icon is not None and not icon.isNull() else QAction(text, menu)
    action.setProperty("lpt_ctx_id", str((entry or {}).get("id") or ""))
    action.triggered.connect(lambda _checked=False, item=dict(entry): trigger_thirdparty(iface, item, menu))
    return action


class ContextMenus:
    def __init__(self, iface, host):
        self.iface = iface
        self.host = host
        self._view = None
        self._on = False

    def attach(self):
        bind_host(self.host, self.iface)
        try:
            view = self.iface.layerTreeView()
        except Exception:
            view = None
        if view is None:
            return False
        if self._on and self._view is view:
            return True
        self.detach()
        signal = getattr(view, "contextMenuAboutToShow", None)
        if signal is None:
            return False
        try:
            signal.connect(self._on_menu)
        except Exception:
            return False
        self._view = view
        self._on = True
        return True

    def detach(self):
        view = self._view
        self._view = None
        self._on = False
        if view is None:
            return
        signal = getattr(view, "contextMenuAboutToShow", None)
        if signal is None:
            return
        try:
            signal.disconnect(self._on_menu)
        except Exception:
            pass  # nosec

    def _on_menu(self, menu):
        apply_menu(menu, self.iface)


class _StillCombo(QComboBox):
    def wheelEvent(self, event):
        event.ignore()



_CHECK_MARGIN = (4, 0, 8, 0)
_CHECK_SPACING = 8


def _text_width(metrics, text):
    try:
        return metrics.horizontalAdvance(text)
    except Exception:
        return metrics.width(text)


def _check_column_width(header):
    box = QCheckBox()
    width = max(box.sizeHint().width(), 18)
    metrics = QLabel().fontMetrics()
    width = max(width, _text_width(metrics, header) + 8)
    return width


class _ElideLabel(QLabel):
    """One-line label that elides overflow and keeps the full text on hover."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._full = ""
        self.setWordWrap(False)
        self.setSizePolicy(qt_attr(QSizePolicy, "Ignored"), qt_attr(QSizePolicy, "Preferred"))

    def set_full_text(self, text):
        self._full = str(text or "")
        self.setToolTip(self._full)
        self._apply_elide()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._apply_elide()

    def _apply_elide(self):
        width = max(self.width(), 1)
        self.setText(self.fontMetrics().elidedText(self._full, qt_attr(Qt, "ElideRight"), width))


class _ListHeader(QWidget):
    """Column titles aligned with each row: Right-click, Toolbar, Name."""

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(*_CHECK_MARGIN)
        layout.setSpacing(_CHECK_SPACING)
        self.lbl_right = QLabel()
        self.lbl_bar = QLabel()
        self.lbl_name = QLabel()
        for label in (self.lbl_right, self.lbl_bar):
            label.setAlignment(qt_attr(Qt, "AlignCenter"))
        layout.addWidget(self.lbl_right, 0)
        layout.addWidget(self.lbl_bar, 0)
        layout.addWidget(self.lbl_name, 1)
        self.retranslate()

    def retranslate(self):
        self.lbl_right.setText(tr("菜单"))
        self.lbl_bar.setText(tr("工具栏"))
        self.lbl_name.setText(tr("名称"))
        self.apply_widths(_check_column_width(self.lbl_right.text()), _check_column_width(self.lbl_bar.text()))

    def apply_widths(self, right_w, bar_w):
        self.lbl_right.setFixedWidth(right_w)
        self.lbl_bar.setFixedWidth(bar_w)

    def column_widths(self):
        return self.lbl_right.width() or _check_column_width(tr("菜单")), self.lbl_bar.width() or _check_column_width(tr("工具栏"))


class _WrapButton(QPushButton):
    """Right-column button that wraps and grows taller instead of widening the dialog."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._full = ""
        self._label = QLabel(self)
        self._label.setWordWrap(True)
        self._label.setAlignment(qt_attr(Qt, "AlignCenter"))
        self._label.setAttribute(qt_attr(Qt, "WA_TransparentForMouseEvents"), True)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)
        layout.addWidget(self._label)
        self.setSizePolicy(qt_attr(QSizePolicy, "Ignored"), qt_attr(QSizePolicy, "Minimum"))
        self.setMinimumWidth(0)

    def setText(self, text):
        self._full = str(text or "")
        self._label.setText(self._full)
        super().setText("")
        self.updateGeometry()

    def text(self):
        return self._full

    def sizeHint(self):
        width = self.width() if self.width() > 20 else 40
        self._label.setFixedWidth(max(width - 16, 20))
        hint = self._label.sizeHint()
        self._label.setMaximumWidth(16777215)
        self._label.setMinimumWidth(0)
        return QSize(40, max(28, hint.height() + 12))

    def minimumSizeHint(self):
        return QSize(40, 28)


class _DualChecks(QWidget):
    """Two checkboxes to the left of the name. Toolbar may be read-only."""

    def __init__(self, name, right_on, bar_on, bar_enabled, widths, parent=None, icon=None):
        super().__init__(parent)
        self._bar_enabled = bool(bar_enabled)
        self._color_spec = None
        layout = QHBoxLayout(self)
        layout.setContentsMargins(*_CHECK_MARGIN)
        layout.setSpacing(_CHECK_SPACING)
        self.right = QCheckBox()
        self.bar = QCheckBox()
        self.icon_label = QLabel(self)
        self.icon_label.setAlignment(qt_attr(Qt, "AlignVCenter") | qt_attr(Qt, "AlignLeft"))
        self.name = _ElideLabel(self)
        self.right.setChecked(bool(right_on))
        self.bar.setChecked(bool(bar_on))
        self.bar.setEnabled(self._bar_enabled)
        layout.addWidget(self.right, 0)
        layout.addWidget(self.bar, 0)
        layout.addWidget(self.icon_label, 0)
        layout.addWidget(self.name, 1)
        self.apply_widths(*widths)
        self.set_name(name)
        self.set_icon(icon)
        self.retranslate()

    def apply_widths(self, right_w, bar_w):
        self.right.setFixedWidth(right_w)
        self.bar.setFixedWidth(bar_w)

    def sizeHint(self):
        height = max(24, self.right.sizeHint().height(), self.bar.sizeHint().height())
        return QSize(1, height)

    def minimumSizeHint(self):
        return self.sizeHint()

    def set_name(self, name):
        text = str(name or "")
        self.name.set_full_text(text)
        self.setToolTip(text.strip())

    def set_icon(self, icon):
        """Title-sized icon before the name; hide when missing so the list stays fast and clean."""
        if icon is None or getattr(icon, "isNull", lambda: True)():
            self.icon_label.clear()
            self.icon_label.hide()
            return
        size = max(12, int(self.name.fontMetrics().height()))
        try:
            pixmap = icon.pixmap(size, size)
        except Exception:
            pixmap = None
        if pixmap is None or pixmap.isNull():
            self.icon_label.clear()
            self.icon_label.hide()
            return
        self.icon_label.setFixedSize(size, size)
        self.icon_label.setPixmap(pixmap)
        self.icon_label.show()

    def set_group_color(self, color_spec):
        self._color_spec = color_spec
        self.setStyleSheet("")
        if color_spec:
            self.name.setStyleSheet("color: %s; font-weight: 600;" % _group_title_color(color_spec))
        else:
            self.name.setStyleSheet("")

    def retranslate(self):
        self.right.setToolTip(tr("菜单"))
        self.bar.setToolTip(tr("工具栏"))
        self.right.setText("")
        self.bar.setText("")


class _NameOnly(QWidget):
    """Group or separator row, name aligned with the name column."""

    def __init__(self, name, widths, group=False, collapsed=False, color_spec=None, on_fold=None, parent=None):
        super().__init__(parent)
        self._is_group = bool(group)
        self._collapsed = bool(collapsed)
        self._color_spec = color_spec
        self._on_fold = on_fold
        layout = QHBoxLayout(self)
        layout.setContentsMargins(*_CHECK_MARGIN)
        layout.setSpacing(_CHECK_SPACING)
        self._pad_right = QWidget(self)
        self._pad_bar = QWidget(self)
        self.fold = QToolButton(self)
        self.fold.setAutoRaise(True)
        self.fold.setFixedSize(18, 18)
        self.fold.setFocusPolicy(qt_attr(Qt, "NoFocus"))
        self.fold.clicked.connect(self._toggle_fold)
        self.name = _ElideLabel(self)
        layout.addWidget(self._pad_right, 0)
        layout.addWidget(self._pad_bar, 0)
        layout.addWidget(self.fold, 0)
        layout.addWidget(self.name, 1)
        self.fold.setVisible(self._is_group)
        self.apply_widths(*widths)
        self.set_name(name, group=group)
        self.set_collapsed(self._collapsed)
        self.set_group_color(color_spec)

    def apply_widths(self, right_w, bar_w):
        self._pad_right.setFixedWidth(right_w)
        self._pad_bar.setFixedWidth(bar_w)

    def sizeHint(self):
        return QSize(1, max(24, self.name.sizeHint().height() + 4))

    def minimumSizeHint(self):
        return self.sizeHint()

    def _toggle_fold(self):
        if not self._is_group or not callable(self._on_fold):
            return
        self._on_fold()

    def set_collapsed(self, collapsed):
        self._collapsed = bool(collapsed)
        if not self._is_group:
            self.fold.setVisible(False)
            return
        self.fold.setVisible(True)
        self.fold.setText("▶" if self._collapsed else "▼")
        self.fold.setToolTip(tr("展开组") if self._collapsed else tr("折叠组"))

    def set_group_color(self, color_spec):
        self._color_spec = color_spec
        self.setStyleSheet("")
        if not self._is_group:
            return
        self.set_name(self.name._full if hasattr(self.name, "_full") else "", group=True)

    def set_name(self, name, group=None):
        if group is not None:
            self._is_group = bool(group)
            self.fold.setVisible(self._is_group)
        text = str(name or "")
        self.name.set_full_text(text.strip())
        self.setToolTip(text.strip())
        font = QFont(self.font())
        self.setStyleSheet("")
        if getattr(self, "_is_group", False):
            font.setBold(True)
            size = font.pointSize()
            if size > 0:
                font.setPointSize(size + 1)
            self.name.setFont(font)
            color = _group_title_color(self._color_spec) if self._color_spec else "#c00000"
            self.name.setStyleSheet("color: %s;" % color)
        else:
            self.name.setFont(QFont(self.font()))
            self.name.setStyleSheet("")


class _MenuList(QListWidget):
    """Reorder and drag into or out of groups, without starting a drag on a checkbox."""

    def __init__(self, owner, parent=None):
        super().__init__(parent)
        self._owner = owner
        self._drag_row = -1
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setDefaultDropAction(qt_attr(Qt, "MoveAction"))
        self.setDragDropMode(qt_attr(QAbstractItemView, "InternalMove"))
        self.setMinimumWidth(0)
        self.setSizePolicy(qt_attr(QSizePolicy, "Expanding"), qt_attr(QSizePolicy, "Expanding"))
        self.viewport().installEventFilter(self)

    def eventFilter(self, watched, event):
        if watched is self.viewport() and enum_int(event.type()) == enum_int(qt_attr(QEvent, "MouseButtonPress"), -1):
            item = self.itemAt(event.pos())
            widget = self.itemWidget(item) if item is not None else None
            if isinstance(widget, _DualChecks):
                local = widget.mapFrom(self.viewport(), event.pos())
                child = widget.childAt(local)
                on_check = False
                node = child
                while node is not None and node is not widget:
                    if node is widget.right or node is widget.bar:
                        on_check = True
                        break
                    node = node.parentWidget() if hasattr(node, "parentWidget") else None
                self.setDragEnabled(not on_check)
            else:
                self.setDragEnabled(True)
        return super().eventFilter(watched, event)

    def startDrag(self, actions):
        item = self.currentItem()
        self._drag_row = self.row(item) if item is not None else -1
        super().startDrag(actions)

    def dropEvent(self, event):
        source = self.item(self._drag_row) if self._drag_row >= 0 else self.currentItem()
        target = self.itemAt(event.pos())
        try:
            position = self.dropIndicatorPosition()
        except Exception:
            position = None
        self._owner._drop_item(source, target, position)
        # InternalMove + accept(MoveAction) makes QAbstractItemView::startDrag delete the
        # source after our manual takeItem/insertItem, so groups/items vanish. Ignore the
        # mime move; we already relocated the row ourselves.
        event.setDropAction(qt_attr(Qt, "IgnoreAction"))
        event.accept()
        self._drag_row = -1
        self.setDragEnabled(True)

    def sizeHint(self):
        return QSize(1, 100)

    def minimumSizeHint(self):
        return QSize(0, 0)


class MenuSettingsPage(QWidget):
    def __init__(self, iface, parent=None):
        super().__init__(parent)
        self.iface = iface
        self._filling = False
        self._loaded = False
        self._labels_cache = {}
        self._toolbar_hidden_cache = None
        self._collapsed = set()
        self._group_colors = {}
        self._group_color_overrides = {}
        root = QHBoxLayout(self)
        root.setContentsMargins(0, 8, 0, 0)
        root.setSpacing(10)

        left = QWidget(self)
        left_layout = QVBoxLayout(left)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(2)
        self.list_header = _ListHeader(left)
        left_layout.addWidget(self.list_header)
        self._left = left
        left.setMinimumWidth(0)
        left.setSizePolicy(qt_attr(QSizePolicy, "Expanding"), qt_attr(QSizePolicy, "Expanding"))
        self.list = _MenuList(self, left)
        self.list.setMinimumWidth(0)
        self.list.setSizePolicy(qt_attr(QSizePolicy, "Expanding"), qt_attr(QSizePolicy, "Expanding"))
        self.list.setSelectionMode(qt_attr(QAbstractItemView, "SingleSelection"))
        self.list.setHorizontalScrollBarPolicy(qt_attr(Qt, "ScrollBarAlwaysOff"))
        self.list.setTextElideMode(qt_attr(Qt, "ElideRight"))
        # Keep third-party icons the same visual size as the name text.
        self.list.setIconSize(QSize(16, 16))
        left_layout.addWidget(self.list, 1)

        right = QWidget(self)
        self._right = right
        right.setMinimumWidth(0)
        right.setSizePolicy(qt_attr(QSizePolicy, "Preferred"), qt_attr(QSizePolicy, "Expanding"))
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(12)

        self.title_label = QLabel()
        self.title_label.setWordWrap(True)
        self.title_edit = QLineEdit()
        self.title_edit.setMinimumWidth(0)
        right_layout.addWidget(self.title_label)
        right_layout.addWidget(self.title_edit)

        self.btn_up = _WrapButton()
        self.btn_down = _WrapButton()
        move_row = QHBoxLayout()
        move_row.setContentsMargins(0, 0, 0, 0)
        move_row.setSpacing(8)
        move_row.addWidget(self.btn_up, 1)
        move_row.addWidget(self.btn_down, 1)
        right_layout.addLayout(move_row)

        self.add_label = QLabel()
        self.add_label.setWordWrap(True)
        self.add_combo = _StillCombo()
        self.add_combo.setMinimumWidth(0)
        self.add_combo.setSizePolicy(qt_attr(QSizePolicy, "Ignored"), qt_attr(QSizePolicy, "Fixed"))
        self.btn_add = _WrapButton()
        self.btn_remove = _WrapButton()
        right_layout.addWidget(self.add_label)
        right_layout.addWidget(self.add_combo)
        add_btns = QHBoxLayout()
        add_btns.setContentsMargins(0, 0, 0, 0)
        add_btns.setSpacing(8)
        add_btns.addWidget(self.btn_add, 1)
        add_btns.addWidget(self.btn_remove, 1)
        right_layout.addLayout(add_btns)

        self.btn_third = _WrapButton()
        right_layout.addWidget(self.btn_third)

        self.btn_new_group = _WrapButton()
        self.btn_rename_group = _WrapButton()
        self.btn_delete_group = _WrapButton()
        self.btn_group_color = _WrapButton()
        right_layout.addWidget(self.btn_new_group)
        right_layout.addWidget(self.btn_rename_group)
        right_layout.addWidget(self.btn_delete_group)
        right_layout.addWidget(self.btn_group_color)

        right_layout.addStretch(1)
        self.btn_reset = _WrapButton()
        right_layout.addWidget(self.btn_reset)

        root.addWidget(left, 4)
        root.addWidget(right, 1)
        root.setStretch(0, 4)
        root.setStretch(1, 1)
        self.list.currentItemChanged.connect(lambda *_args: self._show_title())
        self.title_edit.textChanged.connect(self._on_title)
        self.btn_up.clicked.connect(lambda: self._move(-1))
        self.btn_down.clicked.connect(lambda: self._move(1))
        self.btn_reset.clicked.connect(self._reset)
        self.btn_add.clicked.connect(self._add)
        self.btn_remove.clicked.connect(self._remove)
        self.btn_third.clicked.connect(self._add_thirdparty)
        self.btn_new_group.clicked.connect(self._new_group)
        self.btn_rename_group.clicked.connect(self._rename_group)
        self.btn_delete_group.clicked.connect(self._delete_group)
        self.btn_group_color.clicked.connect(self._configure_group_color)
        self.retranslate()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._apply_column_split()

    def _apply_column_split(self):
        """Keep the list at 80% and the button column at 20% of the page width."""
        total = max(int(self.width()), 1)
        spacing = 10
        right_w = max(1, int((total - spacing) * 0.2))
        self._right.setMaximumWidth(right_w)
        self._right.setMinimumWidth(0)
        if hasattr(self, "_left"):
            self._left.setMinimumWidth(0)
            self._left.setMaximumWidth(16777215)

    def retranslate(self):
        self.list_header.retranslate()
        self.title_label.setText(tr("自定义名称"))
        self.title_label.setWordWrap(True)
        self.title_edit.setPlaceholderText(tr("留空使用原名"))
        self.btn_reset.setText(tr("恢复默认"))
        self.btn_reset.setToolTip(tr("只恢复图层右键菜单，并把从主窗口原工具栏拿掉的按钮加回去。本插件工具栏上其它按钮不动；已挂上的第三方代理会撤掉。"))
        self.btn_up.setText(tr("上移"))
        self.btn_down.setText(tr("下移"))
        self.add_label.setText(tr("添加功能"))
        self.btn_add.setText(tr("添加"))
        self.btn_remove.setText(tr("移除"))
        self.btn_third.setText(tr("添加第三方功能"))
        self.btn_new_group.setText(tr("新建组"))
        self.btn_rename_group.setText(tr("重命名组"))
        self.btn_delete_group.setText(tr("删除组"))
        self.btn_group_color.setText(tr("组颜色配置"))
        self.btn_group_color.setToolTip(tr("先选中一个组，再选字体颜色。组名和组内功能用同一颜色，不铺底色。"))
        self._fill_combo()
        self._retitle_rows()
        self._retranslate_duals()

    def _fit_right_column(self):
        """Do not widen the dialog. Wrap buttons may grow taller at width 650."""
        for button in (
            self.btn_up,
            self.btn_down,
            self.btn_add,
            self.btn_remove,
            self.btn_third,
            self.btn_new_group,
            self.btn_rename_group,
            self.btn_delete_group,
            self.btn_group_color,
            self.btn_reset,
        ):
            button.updateGeometry()

    def ensure_loaded(self):
        if self._loaded:
            return
        # Reuse the session index; force rebuild only on explicit refresh.
        shared_toolbar.action_index(self.iface, force=False)
        self._fill_list()
        self._loaded = True

    def refresh(self):
        shared_toolbar.action_index(self.iface, force=True)
        self._fill_list()
        self._loaded = True

    def commit(self):
        if not self._loaded:
            return
        previous = load_menu()
        order = []
        hidden = []
        titles = {}
        added = []
        thirdparty = []
        groups = []
        membership = {}
        toolbar_hidden = []
        thirdparty_toolbar_hidden = []
        for row in range(self.list.count()):
            item = self.list.item(row)
            key = str(item.data(_ID) or "")
            if not key:
                continue
            order.append(key)
            kind = str(item.data(_KIND) or "")
            right_on, bar_on = self._dual_state(item)
            if not right_on:
                hidden.append(key)
            if kind == "native" and self._item_is_dual(item) and not bar_on:
                toolbar_hidden.append(key)
            title = str(item.data(_TITLE) or "").strip()
            if title and kind != "plugin":
                titles[key] = title
            if kind == "plugin":
                added.append(key)
            if kind == "thirdparty":
                entry = item.data(_EXTRA) or {}
                if isinstance(entry, dict):
                    entry = dict(entry)
                    entry["id"] = key
                    thirdparty.append(entry)
                    # Toolbar checkbox only toggles the plugin's original top toolbar icon
                    # (PROC-style). Never hang a proxy on this plugin's Layers panel toolbar.
                    if entry.get("kind") == "plugin_action" and not bar_on:
                        thirdparty_toolbar_hidden.append(key)
            if kind == "group":
                groups.append({"id": key, "title": title or str(item.data(_TITLE) or "")})
            group_id = str(item.data(_GROUP) or "")
            if group_id and kind != "group":
                membership[key] = group_id
        # Blank / never-captured page: OK must not overwrite a previously saved menu.
        ui_natives = [key for key in order if _is_menu_native_key(key)]
        saved_natives = [key for key in (previous.get("order") or []) if _is_menu_native_key(key)]
        if not order:
            if (
                previous.get("order")
                or previous.get("added")
                or previous.get("thirdparty")
                or previous.get("groups")
            ):
                return
            return
        if not ui_natives and saved_natives:
            order, hidden, titles, toolbar_hidden = _merge_uncaptured_commit(
                previous, order, hidden, titles, toolbar_hidden
            )
        data = dict(previous)
        data["order"] = order
        data["hidden"] = hidden
        data["titles"] = titles
        data["added"] = added
        data["thirdparty"] = thirdparty
        data["groups"] = groups
        data["membership"] = membership
        data["collapsed"] = [key for key in self._collapsed if key in {item["id"] for item in groups}]
        group_ids = {item["id"] for item in groups}
        data["group_colors"] = {
            key: _group_title_color(value)
            for key, value in dict(self._group_color_overrides or {}).items()
            if key in group_ids
        }
        data["toolbar_hidden"] = toolbar_hidden
        # Drop any legacy Layers-panel third-party proxies; Layers toolbar is only
        # controlled by this plugin's own toolbar settings page.
        data["toolbar_proxies"] = []
        data["thirdparty_toolbar_hidden"] = thirdparty_toolbar_hidden
        # Keep native labels that the blank page never showed.
        if not ui_natives and saved_natives:
            data["labels"] = dict(previous.get("labels") or {})
        save_menu(data)
        apply_system_side_effects(self.iface, data)

    def _item_flags(self, checkable=True):
        flags = (
            qt_attr(Qt, "ItemIsEnabled")
            | qt_attr(Qt, "ItemIsSelectable")
            | qt_attr(Qt, "ItemIsDragEnabled")
        )
        return flags

    def _item_is_dual(self, item, data=None):
        """Writable toolbar checkbox: shared native actions and third-party plugin actions only."""
        kind = str(item.data(_KIND) or "") if item is not None else ""
        if kind == "thirdparty":
            entry = item.data(_EXTRA) or {}
            # Toolbox algorithms have no top-toolbar button to toggle; Layers bar is separate.
            return str((entry or {}).get("kind") or "") == "plugin_action"
        if kind == "native":
            if data is None:
                try:
                    data = load_menu()
                except Exception:
                    data = None
            return shared_toolbar.is_shared_key(self.iface, str(item.data(_ID) or ""), data)
        return False

    def _has_checks(self, item):
        kind = str(item.data(_KIND) or "") if item is not None else ""
        return kind not in ("group", "sep")

    def _plugin_toolbar_on(self, key):
        dialog = self._settings()
        if dialog is not None and hasattr(dialog, "toolbar_item_visible"):
            return bool(dialog.toolbar_item_visible(key))
        hidden = getattr(self, "_toolbar_hidden_cache", None)
        if hidden is not None:
            return str(key or "") not in hidden
        try:
            from .settings_store import load_hidden
            return str(key or "") not in set(load_hidden() or [])
        except Exception:
            return False

    def _dual_state(self, item):
        """Return (right_click_visible, toolbar_on)."""
        widget = self.list.itemWidget(item) if item is not None else None
        if isinstance(widget, _DualChecks):
            return widget.right.isChecked(), widget.bar.isChecked()
        kind = str(item.data(_KIND) or "") if item is not None else ""
        if kind in ("group", "sep"):
            return True, False
        stored = item.data(_RC) if item is not None else None
        right_on = True if stored is None else bool(stored)
        bar_on = bool(item.data(_TB)) if item is not None else False
        return right_on, bar_on

    def _column_widths(self):
        return self.list_header.column_widths()

    def _bind_row(self, item, right_on=None, bar_on=None, data=None):
        if item is None:
            return
        kind = str(item.data(_KIND) or "")
        if right_on is None or bar_on is None:
            right_on, bar_on = self._dual_state(item)
        if kind == "plugin":
            bar_on = self._plugin_toolbar_on(str(item.data(_ID) or ""))
        elif kind not in ("group", "sep", "thirdparty") and not self._item_is_dual(item, data):
            bar_on = False
        item.setData(_TB, bool(bar_on))
        if kind not in ("group", "sep"):
            item.setData(_RC, bool(right_on))
        item.setText("")
        name = self._row_display_name(item)
        widths = self._column_widths()
        key = str(item.data(_ID) or "")
        color = self._color_for_item(item)
        # Title-sized third-party icons are filled later by _hydrate_thirdparty_icons
        # so opening this page stays as fast as now.
        row_icon = item.data(_EXTRA_ICON) if kind == "thirdparty" else None
        if kind in ("group", "sep"):
            widget = _NameOnly(
                name,
                widths,
                group=(kind == "group"),
                collapsed=(key in self._collapsed),
                color_spec=color if kind == "group" else None,
                on_fold=(lambda gid=key: self._toggle_group_collapse(gid)) if kind == "group" else None,
                parent=self.list,
            )
        else:
            writable = self._item_is_dual(item, data)
            widget = _DualChecks(name, right_on, bar_on, writable, widths, parent=self.list, icon=row_icon)

            def _store(_value=None, it=item, w=widget):
                it.setData(_RC, bool(w.right.isChecked()))
                it.setData(_TB, bool(w.bar.isChecked()))

            widget.right.stateChanged.connect(_store)
            widget.bar.stateChanged.connect(_store)
            widget.set_group_color(color)
        item.setFlags(self._item_flags(checkable=False))
        item.setSizeHint(widget.sizeHint())
        item.setToolTip(str(name or "").strip())
        self.list.setItemWidget(item, widget)

    def _rebind_duals(self):
        if self._filling:
            return
        for row in range(self.list.count()):
            self._bind_row(self.list.item(row))

    def _retranslate_duals(self):
        widths = self._column_widths()
        for row in range(self.list.count()):
            item = self.list.item(row)
            widget = self.list.itemWidget(item)
            if hasattr(widget, "apply_widths"):
                widget.apply_widths(*widths)
            if isinstance(widget, _DualChecks):
                widget.retranslate()

    def _rebuild_group_colors(self):
        """Keep manual overrides; otherwise assign distinct default text colors in list order."""
        group_ids = []
        for row in range(self.list.count()):
            item = self.list.item(row)
            if str(item.data(_KIND) or "") == "group":
                key = str(item.data(_ID) or "")
                if key and key not in group_ids:
                    group_ids.append(key)
        colors = {}
        for index, key in enumerate(group_ids[:MAX_GROUPS]):
            if key in self._group_color_overrides:
                colors[key] = _group_title_color(self._group_color_overrides[key])
            else:
                colors[key] = _group_title_color(_group_palette_entry(index))
        self._group_colors = colors

    def _color_for_item(self, item):
        if item is None:
            return None
        kind = str(item.data(_KIND) or "")
        if kind == "group":
            return self._group_colors.get(str(item.data(_ID) or ""))
        group_id = str(item.data(_GROUP) or "")
        if group_id:
            return self._group_colors.get(group_id)
        return None

    def _toggle_group_collapse(self, group_id):
        group_id = str(group_id or "")
        if not group_id:
            return
        if group_id in self._collapsed:
            self._collapsed.discard(group_id)
        else:
            self._collapsed.add(group_id)
        self._apply_collapse_visibility()
        for row in range(self.list.count()):
            item = self.list.item(row)
            if str(item.data(_ID) or "") != group_id:
                continue
            widget = self.list.itemWidget(item)
            if isinstance(widget, _NameOnly):
                widget.set_collapsed(group_id in self._collapsed)
            break

    def _apply_collapse_visibility(self):
        for row in range(self.list.count()):
            item = self.list.item(row)
            kind = str(item.data(_KIND) or "")
            if kind == "group":
                item.setHidden(False)
                continue
            group_id = str(item.data(_GROUP) or "")
            item.setHidden(bool(group_id and group_id in self._collapsed))

    def _refresh_group_look(self):
        self._rebuild_group_colors()
        for row in range(self.list.count()):
            item = self.list.item(row)
            widget = self.list.itemWidget(item)
            color = self._color_for_item(item)
            if isinstance(widget, _DualChecks):
                widget.set_group_color(color)
                widget.set_name(self._row_display_name(item))
            elif isinstance(widget, _NameOnly):
                key = str(item.data(_ID) or "")
                widget.set_group_color(color if str(item.data(_KIND) or "") == "group" else None)
                widget.set_collapsed(key in self._collapsed)
                widget.set_name(self._row_display_name(item), group=(str(item.data(_KIND) or "") == "group"))
        self._apply_collapse_visibility()

    def _fill_list(self):
        data = load_menu()
        # Only when nothing was ever captured: try one silent snapshot so a first open
        # is less often blank. Skip when we already have natives (keeps open fast).
        if not any(_is_menu_native_key(key) for key in (data.get("order") or [])):
            try:
                pairs = snapshot(self.iface)
                if pairs:
                    data = _remember(pairs, refresh_labels=True)
            except Exception:
                pass  # nosec
        self._labels_cache = dict(data.get("labels") or {})
        self._collapsed = set(str(item) for item in data.get("collapsed") or [])
        self._group_color_overrides = dict(data.get("group_colors") or {})
        try:
            from .settings_store import load_hidden

            self._toolbar_hidden_cache = set(load_hidden() or [])
        except Exception:
            self._toolbar_hidden_cache = set()
        order = list(data["order"])
        known = set(order)
        for key in data["added"]:
            if key not in known:
                order.append(key)
                known.add(key)
        for item in data.get("thirdparty") or []:
            if item["id"] not in known:
                order.append(item["id"])
                known.add(item["id"])
        for item in data.get("groups") or []:
            if item["id"] not in known:
                order.append(item["id"])
                known.add(item["id"])
        thirdparty = {item["id"]: item for item in data.get("thirdparty") or []}
        groups = {item["id"]: item for item in data.get("groups") or []}
        membership = dict(data.get("membership") or {})
        self._filling = True
        self.list.clear()
        for key in order:
            if str(key).startswith("lpt:") and key not in _CANDIDATE_IDS:
                continue
            if key.startswith("tp:") and key not in thirdparty:
                continue
            if key.startswith("grp:") and key not in groups:
                continue
            if key in _CANDIDATE_IDS:
                kind = "plugin"
            elif key.startswith("sep:"):
                kind = "sep"
            elif key in thirdparty:
                kind = "thirdparty"
            elif key in groups:
                kind = "group"
            else:
                kind = "native"
            if kind == "plugin" and key not in data["added"] and key not in data["order"]:
                continue
            item = QListWidgetItem()
            item.setData(_ID, key)
            item.setData(_KIND, kind)
            item.setData(_GROUP, membership.get(key, ""))
            item.setData(_TITLE, self._initial_title(key, kind, data, groups))
            if kind == "thirdparty":
                item.setData(_EXTRA, dict(thirdparty[key]))
            dual = self._item_is_dual(item, data)
            item.setFlags(self._item_flags(checkable=False))
            visible = key not in set(data["hidden"])
            if kind == "thirdparty":
                entry = thirdparty.get(key) or {}
                if entry.get("kind") == "plugin_action":
                    # Checked = original top toolbar visible (PROC-style). Never Layers bar.
                    bar_on = key not in set(data.get("thirdparty_toolbar_hidden") or [])
                else:
                    bar_on = False
            elif dual:
                bar_on = key not in set(data.get("toolbar_hidden") or [])
            elif kind == "plugin":
                bar_on = self._plugin_toolbar_on(key)
            else:
                bar_on = False
            item.setData(_TB, bar_on)
            if kind == "plugin":
                icon = _icon_for(key)
                if icon is not None and not icon.isNull():
                    item.setIcon(icon)
            self.list.addItem(item)
            self._paint_item(item)
            self._bind_row(item, visible, bar_on, data)
        self._filling = False
        self._refresh_group_look()
        self._fill_combo()
        if self.list.count():
            self.list.setCurrentRow(0)
        else:
            self._show_title()
        # Defer icon lookup so opening System Properties stays as fast as before.
        QTimer.singleShot(0, self._hydrate_thirdparty_icons)

    def _retitle_rows(self):
        if self._filling:
            return
        for row in range(self.list.count()):
            self._paint_item(self.list.item(row))

    def _settings(self):
        parent = self.parent()
        while parent is not None:
            if hasattr(parent, "title_for") and hasattr(parent, "set_button_title"):
                return parent
            parent = parent.parent()
        return None

    def _initial_title(self, key, kind, data, groups=None):
        if kind == "plugin":
            dialog = self._settings()
            if dialog is not None:
                return str(dialog.title_for(key) or "").strip()
            return _toolbar_custom(key)
        if kind == "group":
            groups = groups or {item["id"]: item for item in data.get("groups") or []}
            return str((groups.get(key) or {}).get("title") or data["titles"].get(key) or "").strip()
        return str(data["titles"].get(key) or "").strip()

    def _base_label(self, item):
        kind = str(item.data(_KIND) or "")
        key = str(item.data(_ID) or "")
        if kind == "plugin":
            return tr(_CANDIDATE_IDS.get(key, key))
        if kind == "sep":
            return tr("—— 分隔线 ——")
        if kind == "group":
            return str(item.data(_TITLE) or "").strip() or tr("未命名组")
        if kind == "thirdparty":
            entry = item.data(_EXTRA) or {}
            return str((entry or {}).get("label") or key)
        labels = getattr(self, "_labels_cache", None)
        if labels is None:
            labels = dict(load_menu().get("labels") or {})
            self._labels_cache = labels
        return labels.get(key) or key

    def _row_display_name(self, item):
        if item is None:
            return ""
        kind = str(item.data(_KIND) or "")
        group_id = str(item.data(_GROUP) or "")
        name = _display_name(self._base_label(item), item.data(_TITLE) if kind != "group" else "")
        if kind == "group":
            name = self._base_label(item)
        if group_id:
            name = "    " + name
        return name

    def _paint_item(self, item):
        if item is None:
            return
        kind = str(item.data(_KIND) or "")
        name = self._row_display_name(item)
        item.setText("")
        item.setToolTip(name.strip())
        widget = self.list.itemWidget(item)
        color = self._color_for_item(item)
        if isinstance(widget, _DualChecks):
            widget.set_name(name)
            widget.set_group_color(color)
        elif isinstance(widget, _NameOnly):
            widget.set_group_color(color if kind == "group" else None)
            widget.set_name(name, group=(kind == "group"))
            if kind == "group":
                widget.set_collapsed(str(item.data(_ID) or "") in self._collapsed)

    def sync_toolbar_titles(self):
        dialog = self._settings()
        if dialog is None:
            return
        self._filling = True
        for row in range(self.list.count()):
            item = self.list.item(row)
            kind = str(item.data(_KIND) or "")
            if kind not in ("plugin", "thirdparty"):
                continue
            title = dialog.title_for(str(item.data(_ID) or ""))
            if kind == "thirdparty" and not title:
                continue
            item.setData(_TITLE, title)
        self._filling = False
        self._retitle_rows()
        for row in range(self.list.count()):
            item = self.list.item(row)
            if str(item.data(_KIND) or "") == "plugin":
                self._bind_row(item)
        self._show_title()

    def _reset(self):
        data = _empty()
        save_menu(data)
        apply_system_side_effects(self.iface, data, restore_toolbars=True)
        self.refresh()

    def _fill_combo(self):
        present = set()
        for row in range(self.list.count()):
            present.add(str(self.list.item(row).data(_ID) or ""))
        current = str(self.add_combo.currentData() or "")
        self.add_combo.blockSignals(True)
        self.add_combo.clear()
        for button_id, msgid in CANDIDATES:
            if button_id in present:
                continue
            self.add_combo.addItem(tr(msgid), button_id)
        if current:
            index = self.add_combo.findData(current)
            if index >= 0:
                self.add_combo.setCurrentIndex(index)
        self.add_combo.blockSignals(False)
        self.btn_add.setEnabled(self.add_combo.count() > 0)

    def _show_title(self):
        item = self.list.currentItem()
        kind = str(item.data(_KIND) or "") if item is not None else ""
        plugin = kind == "plugin"
        third = kind == "thirdparty"
        group = kind == "group"
        editable = item is not None and kind != "sep"
        self.title_edit.blockSignals(True)
        self.title_edit.setEnabled(editable)
        self.title_edit.setText(str(item.data(_TITLE) or "") if editable else "")
        self.title_edit.blockSignals(False)
        self.btn_remove.setEnabled(plugin or third)
        self.btn_delete_group.setEnabled(group)
        self.btn_rename_group.setEnabled(group)
        self.btn_group_color.setEnabled(group)

    def _on_title(self, text):
        item = self.list.currentItem()
        if item is None or not self.title_edit.isEnabled():
            return
        item.setData(_TITLE, text)
        kind = str(item.data(_KIND) or "")
        if kind in ("plugin", "thirdparty"):
            dialog = self._settings()
            if dialog is not None:
                dialog.set_button_title(str(item.data(_ID) or ""), text)
        self._paint_item(item)

    def _move(self, delta):
        row = self.list.currentRow()
        if row < 0:
            return
        target = row + delta
        if target < 0 or target >= self.list.count():
            return
        item = self.list.item(row)
        right_on, bar_on = self._dual_state(item)
        item = self.list.takeItem(row)
        self.list.insertItem(target, item)
        self.list.setCurrentRow(target)
        self._bind_row(item, right_on, bar_on)
        self._paint_item(item)
        self._show_title()

    def _hydrate_thirdparty_icons(self):
        """Fill title-sized icons beside third-party names after the list is already shown."""
        if self._filling:
            return
        for row in range(self.list.count()):
            item = self.list.item(row)
            if item is None or str(item.data(_KIND) or "") != "thirdparty":
                continue
            existing = item.data(_EXTRA_ICON)
            if existing is not None and not getattr(existing, "isNull", lambda: True)():
                continue
            icon = _thirdparty_icon(item.data(_EXTRA) or {})
            if icon is None or icon.isNull():
                continue
            item.setData(_EXTRA_ICON, icon)
            widget = self.list.itemWidget(item)
            if isinstance(widget, _DualChecks):
                widget.set_icon(icon)

    def _make_item(self, key, kind, title="", extra=None, group_id="", icon=None):
        item = QListWidgetItem()
        item.setData(_ID, key)
        item.setData(_KIND, kind)
        item.setData(_TITLE, title)
        item.setData(_GROUP, group_id)
        if extra is not None:
            item.setData(_EXTRA, extra)
        item.setFlags(self._item_flags(checkable=False))
        if kind == "thirdparty":
            # plugin_action defaults to showing the original top toolbar; never Layers bar.
            bar_on = bool((extra or {}).get("kind") == "plugin_action")
            item.setData(_TB, bar_on)
            if icon is not None and not getattr(icon, "isNull", lambda: True)():
                item.setData(_EXTRA_ICON, icon)
        elif kind == "plugin":
            item.setData(_TB, self._plugin_toolbar_on(key))
        if kind == "plugin":
            plug_icon = _icon_for(key)
            if plug_icon is not None and not plug_icon.isNull():
                item.setIcon(plug_icon)
        self.list.addItem(item)
        self._paint_item(item)
        self._bind_row(item, True, bool(item.data(_TB)))
        self.list.setCurrentItem(item)
        return item

    def _add(self):
        button_id = str(self.add_combo.currentData() or "")
        if not button_id:
            return
        title = ""
        dialog = self._settings()
        if dialog is not None:
            title = dialog.title_for(button_id)
        self._make_item(button_id, "plugin", title)
        self._fill_combo()

    def _remove(self):
        item = self.list.currentItem()
        kind = str(item.data(_KIND) or "") if item is not None else ""
        if item is None or kind not in ("plugin", "thirdparty"):
            return
        row = self.list.row(item)
        self.list.takeItem(row)
        self._fill_combo()
        self._show_title()

    def _add_thirdparty(self):
        dialog = ThirdPartyPicker(self.iface, self)
        if not accepted(run_dialog(dialog)):
            return
        entry = dialog.chosen()
        if not entry:
            return
        ok, reason = can_add_entry(self.iface, entry)
        if not ok:
            report(self, tr("添加第三方功能"), reason, warning=True)
            return
        # Refuse duplicates of the same original action or algorithm.
        for row in range(self.list.count()):
            item = self.list.item(row)
            if str(item.data(_KIND) or "") != "thirdparty":
                continue
            other = item.data(_EXTRA) or {}
            if entry.get("kind") == "algorithm" and other.get("alg_id") == entry.get("alg_id"):
                report(self, tr("添加第三方功能"), tr("这个功能已经在列表里了。"), warning=True)
                return
            if (
                entry.get("kind") == "plugin_action"
                and other.get("plugin_id") == entry.get("plugin_id")
                and other.get("object_name") == entry.get("object_name")
                and other.get("label") == entry.get("label")
            ):
                report(self, tr("添加第三方功能"), tr("这个功能已经在列表里了。"), warning=True)
                return
        key = new_id("tp")
        payload = {
            "id": key,
            "kind": entry.get("kind"),
            "plugin_id": entry.get("plugin_id") or "",
            "object_name": entry.get("object_name") or "",
            "label": entry.get("label") or "",
            "alg_id": entry.get("alg_id") or "",
        }
        self._make_item(key, "thirdparty", "", payload, icon=entry.get("icon"))

    def _group_count(self):
        total = 0
        for row in range(self.list.count()):
            if str(self.list.item(row).data(_KIND) or "") == "group":
                total += 1
        return total

    def _new_group(self):
        if self._group_count() >= MAX_GROUPS:
            report(self, tr("新建组"), tr("最多只能建 %d 个组。") % MAX_GROUPS, warning=True)
            return
        key = new_id("grp")
        self._make_item(key, "group", tr("未命名组"))
        self._refresh_group_look()

    def _rename_group(self):
        item = self.list.currentItem()
        if item is None or str(item.data(_KIND) or "") != "group":
            return
        self.title_edit.setFocus()
        self.title_edit.selectAll()

    def _delete_group(self):
        item = self.list.currentItem()
        if item is None or str(item.data(_KIND) or "") != "group":
            return
        key = str(item.data(_ID) or "")
        self._collapsed.discard(key)
        self._group_color_overrides.pop(key, None)
        for row in range(self.list.count()):
            child = self.list.item(row)
            if str(child.data(_GROUP) or "") == key:
                child.setData(_GROUP, "")
                self._paint_item(child)
        self.list.takeItem(self.list.row(item))
        self._refresh_group_look()
        self._show_title()

    def _configure_group_color(self):
        item = self.list.currentItem()
        if item is None or str(item.data(_KIND) or "") != "group":
            report(self, tr("组颜色配置"), tr("请先选择一个组。"), warning=True)
            return
        key = str(item.data(_ID) or "")
        if not key:
            return
        from qgis.PyQt.QtGui import QColor
        from qgis.PyQt.QtWidgets import QColorDialog

        current = _group_title_color(self._group_colors.get(key) or self._group_color_overrides.get(key))
        picked = QColorDialog.getColor(QColor(current), self, tr("组颜色配置"))
        if not picked.isValid():
            return
        color = picked.name()
        self._group_color_overrides[key] = color
        self._group_colors[key] = color
        self._refresh_group_look()

    def _drop_item(self, source, target, position):
        if source is None:
            return
        source_row = self.list.row(source)
        if source_row < 0:
            return
        above = enum_int(qt_attr(QAbstractItemView, "AboveItem"), -3)
        on_item = enum_int(qt_attr(QAbstractItemView, "OnItem"), -2)
        pos = enum_int(position, -1)
        if target is None:
            dest = self.list.count()
            target_group = ""
        else:
            target_row = self.list.row(target)
            dest = target_row if pos == above else target_row + 1
            if str(target.data(_KIND) or "") == "group":
                # Drop above the header = leave the group. On/below = join it.
                target_group = "" if pos == above else str(target.data(_ID) or "")
                if pos == on_item:
                    dest = target_row + 1
            else:
                target_group = str(target.data(_GROUP) or "")
        source_kind = str(source.data(_KIND) or "")
        right_on, bar_on = self._dual_state(source)
        group_id = str(source.data(_ID) or "") if source_kind == "group" else ""
        member_bundle = []
        if source_kind == "group" and group_id:
            # Keep members with the header so dragging a group does not scatter or orphan them.
            for row in range(self.list.count()):
                child = self.list.item(row)
                if child is None or child is source:
                    continue
                if str(child.data(_GROUP) or "") == group_id:
                    member_bundle.append((child, self._dual_state(child)))
            source.setData(_GROUP, "")
        elif source_kind != "sep":
            # Native QGIS items, plugin tools, and third-party entries may join a group.
            source.setData(_GROUP, target_group)
            if target_group and target_group in self._collapsed:
                self._collapsed.discard(target_group)
        if dest > source_row:
            dest -= 1
        if dest < 0:
            dest = 0
        if dest != source_row:
            item = self.list.takeItem(source_row)
            self.list.insertItem(dest, item)
            self.list.setCurrentItem(item)
            source = item
        # takeItem drops the row widget; rebind only the moved row, not the whole list.
        self._bind_row(source, right_on, bar_on)
        self._paint_item(source)
        if member_bundle:
            for child, _state in member_bundle:
                self.list.takeItem(self.list.row(child))
            insert_at = self.list.row(source) + 1
            for child, state in member_bundle:
                self.list.insertItem(insert_at, child)
                self._bind_row(child, state[0], state[1])
                self._paint_item(child)
                insert_at += 1
        self._refresh_group_look()
        self._show_title()


class ThirdPartyPicker(QDialog):
    def __init__(self, iface, parent=None):
        super().__init__(parent)
        self.iface = iface
        self._choice = None
        self.setObjectName("LayersPanelToolsThirdPartyPicker")
        self.resize(520, 420)
        layout = QVBoxLayout(self)
        self.hint = QLabel()
        self.hint.setWordWrap(True)
        layout.addWidget(self.hint)
        self.search = QLineEdit()
        layout.addWidget(self.search)
        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderHidden(True)
        self.tree.setSelectionMode(qt_attr(QAbstractItemView, "SingleSelection"))
        layout.addWidget(self.tree, 1)
        row = QHBoxLayout()
        self.btn_ok = QPushButton()
        self.btn_cancel = QPushButton()
        row.addStretch(1)
        row.addWidget(self.btn_ok)
        row.addWidget(self.btn_cancel)
        layout.addLayout(row)
        self.plugins_root = QTreeWidgetItem()
        self.tree.addTopLevelItem(self.plugins_root)
        self.plugins_root.setFlags(qt_attr(Qt, "ItemIsEnabled"))
        self.search.textChanged.connect(self._filter)
        self.btn_ok.clicked.connect(self._accept)
        self.btn_cancel.clicked.connect(self.reject)
        self.tree.itemDoubleClicked.connect(lambda *_args: self._accept())
        self._fill()
        self.retranslate()
        subscribe(self, self.retranslate)

    def retranslate(self, *_args):
        self.setWindowTitle(tr("添加第三方功能"))
        self.hint.setText(tr("只列出已安装的其它插件，可搜索。一个插件有多个动作就按项添加。不能对着当前图层使用的不能加入。不要把对方插件的子菜单整棵拆进来。"))
        self.search.setPlaceholderText(tr("搜索"))
        self.plugins_root.setText(0, tr("已安装插件"))
        self.btn_ok.setText(tr("添加"))
        self.btn_cancel.setText(tr("取消"))
        apply_direction(self)

    def _fill(self):
        self.plugins_root.takeChildren()
        for action in list_plugin_actions():
            item = QTreeWidgetItem([action["label"] + "  ·  " + action["plugin_id"]])
            icon = action.get("icon")
            if icon is not None and not getattr(icon, "isNull", lambda: True)():
                item.setIcon(0, icon)
            item.setData(0, _EXTRA, {
                "kind": "plugin_action",
                "plugin_id": action["plugin_id"],
                "object_name": action["object_name"],
                "label": action["label"],
                "alg_id": "",
                "icon": icon,
            })
            self.plugins_root.addChild(item)
        self.plugins_root.setExpanded(True)

    def _filter(self, text):
        needle = str(text or "").strip().lower()
        visible_any = False
        for row in range(self.plugins_root.childCount()):
            child = self.plugins_root.child(row)
            visible = (not needle) or needle in str(child.text(0) or "").lower()
            child.setHidden(not visible)
            visible_any = visible_any or visible
        self.plugins_root.setHidden(bool(needle) and not visible_any)

    def _accept(self):
        item = self.tree.currentItem()
        if item is None or item is self.plugins_root:
            report(self, tr("添加第三方功能"), tr("请先选择一项再添加。"), warning=True)
            return
        entry = item.data(0, _EXTRA) or {}
        if not isinstance(entry, dict) or entry.get("kind") != "plugin_action":
            report(self, tr("添加第三方功能"), tr("请先选择一项再添加。"), warning=True)
            return
        ok, reason = can_add_entry(self.iface, entry)
        if not ok:
            report(self, tr("添加第三方功能"), reason, warning=True)
            return
        self._choice = dict(entry)
        self.accept()

    def chosen(self):
        return self._choice
