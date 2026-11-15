# -*- coding: utf-8 -*-
"""Main-window toolbar membership for QGIS actions shared with the layer context menu.

Never call setVisible/setHidden to hide these actions. Hide means removeAction on
one home toolbar only; show means insertAction/addAction on that same toolbar.
setVisible(True) is used only to undo an older accidental hide.
"""

from qgis.PyQt.QtWidgets import QToolBar

# iface getters for the three named shared actions, plus common aliases.
_IFACE_GETTERS = (
    "actionToggleEditing",
    "actionSaveActiveLayerEdits",
    "actionAllEdits",
    "actionSaveEdits",
    "actionCurrentEdits",
)

# Well-known object names, used when the context-menu key is available but the
# live QAction has not been resolved yet.
_KNOWN_OBJECT_NAMES = (
    "mActionToggleEditing",
    "mActionSaveLayerEdits",
    "mActionSaveActiveLayerEdits",
    "mActionSaveEdits",
    "mActionAllEdits",
    "mActionCurrentEdits",
)

# Session cache: menu key -> {name, index, before}
_HOMES = {}


def _clean_text(text):
    return str(text or "").replace("&", "").strip()


def _safe_object_name(widget):
    try:
        return str(widget.objectName() or "")
    except Exception:
        return ""


def _strip_unique_suffix(text):
    raw = str(text or "")
    if "#" in raw:
        head, tail = raw.rsplit("#", 1)
        if tail.isdigit():
            return head
    return raw


def _key_object_name(key):
    raw = _strip_unique_suffix(key)
    if raw.startswith("obj:"):
        return raw[4:]
    if raw in _KNOWN_OBJECT_NAMES:
        return raw
    return ""


def _key_label(key):
    raw = _strip_unique_suffix(key)
    if raw.startswith("txt:"):
        return raw[4:]
    return ""


def _layers_bars(iface):
    """Layers panel toolbars and this plugin's extra rows — never treat as the home bar."""
    found = set()
    try:
        from .toolbar_host import _is_extra_row_bar, _layout_toolbars, find_toolbar
    except Exception:
        _is_extra_row_bar = None
        _layout_toolbars = None
        find_toolbar = None
    if callable(_layout_toolbars):
        try:
            for bar in _layout_toolbars(iface) or []:
                found.add(bar)
        except Exception:
            pass  # nosec
    if callable(find_toolbar):
        try:
            native = find_toolbar(iface)
        except Exception:
            native = None
        if native is not None:
            found.add(native)
    main = None
    try:
        main = iface.mainWindow() if iface is not None else None
    except Exception:
        main = None
    if main is None:
        return found
    try:
        children = main.findChildren(QToolBar)
    except Exception:
        return found
    for bar in children:
        name = _safe_object_name(bar)
        if name.startswith("LayersPanelTools"):
            found.add(bar)
            continue
        if callable(_is_extra_row_bar):
            try:
                if _is_extra_row_bar(bar):
                    found.add(bar)
            except Exception:
                pass  # nosec
    return found


def _main_toolbars(iface):
    main = None
    try:
        main = iface.mainWindow() if iface is not None else None
    except Exception:
        main = None
    if main is None:
        return []
    skip = _layers_bars(iface)
    found = []
    try:
        children = main.findChildren(QToolBar)
    except Exception:
        return found
    for bar in children:
        if bar in skip:
            continue
        try:
            bar.actions()
        except Exception:
            _lpt_skip = True
        else:
            _lpt_skip = False
        if _lpt_skip:
            continue
        found.append(bar)
    return found


def iface_shared_actions(iface):
    found = []
    seen = set()
    if iface is None:
        return found
    for name in _IFACE_GETTERS:
        getter = getattr(iface, name, None)
        if not callable(getter):
            continue
        try:
            action = getter()
        except Exception:
            action = None
        if action is None:
            continue
        marker = id(action)
        if marker in seen:
            continue
        seen.add(marker)
        found.append(action)
    return found


def _action_on_bar(action, bar):
    if action is None or bar is None:
        return False
    try:
        return action in list(bar.actions())
    except Exception:
        return False


def action_home_toolbar(iface, action):
    """The one main-window toolbar this action already lives on, if any."""
    if action is None:
        return None
    for bar in _main_toolbars(iface):
        if _action_on_bar(action, bar):
            return bar
    return None


def is_shared_action(iface, action):
    if action is None:
        return False
    name = _safe_object_name(action)
    if name in _KNOWN_OBJECT_NAMES:
        return True
    for known in iface_shared_actions(iface):
        if action is known:
            return True
    # Prefer the cached main-toolbar index over scanning every bar again.
    try:
        index = action_index(iface)
        if name and index["by_name"].get(name) is action:
            return True
        label = _clean_text(action.text())
        if label and index["by_label"].get(label) is action:
            return True
    except Exception:
        pass  # nosec
    return False


_ACTION_INDEX = None


def invalidate_action_index():
    global _ACTION_INDEX
    _ACTION_INDEX = None


def action_index(iface, force=False):
    """One lookup table of shared and main-window toolbar actions. No per-key window scan."""
    global _ACTION_INDEX
    if _ACTION_INDEX is not None and not force:
        return _ACTION_INDEX
    by_name = {}
    by_label = {}

    def _add(action):
        if action is None:
            return
        name = _safe_object_name(action)
        label = _clean_text(action.text())
        if name:
            by_name[name] = action
        if label:
            by_label[label] = action

    for action in iface_shared_actions(iface):
        _add(action)
    for bar in _main_toolbars(iface):
        try:
            actions = list(bar.actions())
        except Exception:
            _lpt_skip = True
        else:
            _lpt_skip = False
        if _lpt_skip:
            continue
        for action in actions:
            _add(action)
    _ACTION_INDEX = {"by_name": by_name, "by_label": by_label}
    return _ACTION_INDEX


def find_action_for_key(iface, key):
    name = _key_object_name(key)
    label = _clean_text(_key_label(key))
    for action in iface_shared_actions(iface):
        if name and _safe_object_name(action) == name:
            return action
        if label and _clean_text(action.text()) == label:
            return action
    if not name and not label:
        return None
    index = action_index(iface)
    if name and name in index["by_name"]:
        return index["by_name"][name]
    if label and label in index["by_label"]:
        return index["by_label"][label]
    return None


def is_shared_key(iface, key, data=None):
    """True for known shared actions even if the key is not obj: or the live QAction is missing."""
    key = str(key or "")
    if not key:
        return False
    name = _key_object_name(key)
    if name in _KNOWN_OBJECT_NAMES:
        return True
    if key in _HOMES:
        return True
    if data:
        hidden = data.get("toolbar_hidden") or []
        if key in hidden:
            return True
        homes = data.get("toolbar_homes") or {}
        if isinstance(homes, dict) and key in homes:
            return True
    action = find_action_for_key(iface, key)
    if action is not None and is_shared_action(iface, action):
        return True
    label = _clean_text(_key_label(key))
    if label:
        for known in iface_shared_actions(iface):
            if _clean_text(known.text()) == label:
                return True
    return False


def remember_home(key, bar, action):
    if not key or bar is None or action is None:
        return
    try:
        actions = list(bar.actions())
    except Exception:
        return
    try:
        index = actions.index(action)
    except ValueError:
        index = len(actions)
    before = ""
    if index + 1 < len(actions):
        before = _safe_object_name(actions[index + 1])
    _HOMES[str(key)] = {
        "name": _safe_object_name(bar),
        "index": index,
        "before": before,
    }


def load_homes(data):
    source = data.get("toolbar_homes") if isinstance(data, dict) else None
    if not isinstance(source, dict):
        return
    for key, value in source.items():
        if not isinstance(value, dict):
            continue
        key = str(key)
        name = str(value.get("name") or "")
        before = str(value.get("before") or "")
        try:
            index = int(value.get("index", -1))
        except (TypeError, ValueError):
            index = -1
        if not name:
            continue
        _HOMES[key] = {"name": name, "index": index, "before": before}


def dump_homes():
    found = {}
    for key, value in _HOMES.items():
        if not isinstance(value, dict):
            continue
        name = str(value.get("name") or "")
        if not name:
            continue
        found[str(key)] = {
            "name": name,
            "index": int(value.get("index", -1) or -1),
            "before": str(value.get("before") or ""),
        }
    return found


def _fallback_bar(iface):
    for getter in ("digitizeToolBar", "advancedDigitizeToolBar"):
        fn = getattr(iface, getter, None) if iface is not None else None
        if not callable(fn):
            continue
        try:
            bar = fn()
        except Exception:
            bar = None
        if bar is not None:
            return bar
    main = None
    try:
        main = iface.mainWindow() if iface is not None else None
    except Exception:
        main = None
    if main is None:
        return None
    for name in ("mDigitizeToolBar", "mAdvancedDigitizeToolBar"):
        try:
            bar = main.findChild(QToolBar, name)
        except Exception:
            bar = None
        if bar is not None:
            return bar
    return None


def _bar_for_home(iface, action, key):
    current = action_home_toolbar(iface, action)
    if current is not None:
        remember_home(key, current, action)
        return current
    home = _HOMES.get(str(key)) or {}
    name = str(home.get("name") or "")
    if name:
        for bar in _main_toolbars(iface):
            if _safe_object_name(bar) == name:
                return bar
        main = None
        try:
            main = iface.mainWindow() if iface is not None else None
        except Exception:
            main = None
        if main is not None:
            try:
                bar = main.findChild(QToolBar, name)
            except Exception:
                bar = None
            if bar is not None and bar not in _layers_bars(iface):
                return bar
    return _fallback_bar(iface)


def _insert_on_bar(bar, action, home):
    if bar is None or action is None:
        return
    if _action_on_bar(action, bar):
        return
    before = None
    home = home or {}
    before_name = str(home.get("before") or "")
    try:
        actions = list(bar.actions())
    except Exception:
        actions = []
    if before_name:
        for other in actions:
            if _safe_object_name(other) == before_name:
                before = other
                break
    if before is None:
        try:
            index = int(home.get("index", -1))
        except (TypeError, ValueError):
            index = -1
        if 0 <= index < len(actions):
            before = actions[index]
    try:
        if before is not None:
            bar.insertAction(before, action)
        else:
            bar.addAction(action)
    except Exception:
        pass  # nosec


def restore_action_text(action, key=None, data=None):
    """If an older apply_menu wrote a custom title onto the original QAction, put the original text back."""
    if action is None:
        return
    data = data or {}
    custom = ""
    if key:
        custom = str((data.get("titles") or {}).get(key) or "").strip()
    try:
        base = str(action.property("_lpt_base_text") or "")
    except Exception:
        base = ""
    if base:
        try:
            if action.text() != base:
                action.setText(base)
        except Exception:
            pass  # nosec
        return
    if not custom:
        return
    try:
        current = action.text()
    except Exception:
        return
    if _clean_text(current) != _clean_text(custom):
        return
    original = ""
    if key:
        original = str((data.get("labels") or {}).get(key) or "").strip()
    if original and _clean_text(original) != _clean_text(custom):
        try:
            action.setText(original)
        except Exception:
            pass  # nosec


def capture_base_text(action, custom=""):
    """Remember the original text once, without overwriting it with a previously applied custom title."""
    if action is None:
        return
    try:
        existing = str(action.property("_lpt_base_text") or "")
    except Exception:
        existing = ""
    if existing:
        return
    try:
        current = action.text()
    except Exception:
        return
    if custom and _clean_text(current) == _clean_text(custom):
        return
    try:
        action.setProperty("_lpt_base_text", current)
    except Exception:
        pass  # nosec


def _ensure_visible(action):
    """Undo an older accidental setVisible(False). Never used to hide."""
    if action is None:
        return
    try:
        if not action.isVisible():
            action.setVisible(True)
    except Exception:
        pass  # nosec


def _iter_targets(iface, data):
    """(key, action) pairs for known shared actions plus remembered homes."""
    data = data or {}
    seen = set()
    by_name = {}
    for action in iface_shared_actions(iface):
        name = _safe_object_name(action)
        if name:
            by_name[name] = action
        key = "obj:" + name if name else ""
        if key:
            yield key, action
            seen.add(id(action))
    for key in list(data.get("toolbar_hidden") or []) + list(_HOMES):
        key = str(key)
        if not key:
            continue
        action = find_action_for_key(iface, key)
        if action is None:
            name = _key_object_name(key)
            action = by_name.get(name)
        if action is None or id(action) in seen:
            continue
        seen.add(id(action))
        yield key, action
    # Any other action on a main-window toolbar that a context-menu key may later use
    # is resolved when apply_menu or the settings page passes extra actions.


def apply_membership(iface, data=None, extra_actions=None, restore_all=False):
    """Apply or restore main-window toolbar membership.

    restore_all=True puts every tracked button back (unload / restore defaults).
    Otherwise toolbar_hidden keys are removed from their home bar only.
    """
    if iface is None:
        return
    try:
        from .context_menu import load_menu
    except Exception:
        load_menu = None
    if data is None and callable(load_menu):
        try:
            data = load_menu()
        except Exception:
            data = {}
    data = data or {}
    load_homes(data)
    hidden = set() if restore_all else set(str(item) for item in (data.get("toolbar_hidden") or []))
    extras = list(extra_actions or [])
    targets = list(_iter_targets(iface, data))
    have = {id(action) for _key, action in targets}
    for key, action in extras:
        if action is None:
            continue
        if id(action) in have:
            continue
        if key or is_shared_action(iface, action):
            token = str(key or "") or ("obj:" + _safe_object_name(action))
            targets.append((token, action))
            have.add(id(action))
    for key, action in targets:
        restore_action_text(action, key, data)
        _ensure_visible(action)
        bar = _bar_for_home(iface, action, key)
        if bar is None:
            continue
        if _action_on_bar(action, bar):
            remember_home(key, bar, action)
        if key in hidden:
            if _action_on_bar(action, bar):
                remember_home(key, bar, action)
                try:
                    bar.removeAction(action)
                except Exception:
                    pass  # nosec
            continue
        _insert_on_bar(bar, action, _HOMES.get(str(key)))
        _ensure_visible(action)


def restore_all(iface, data=None):
    apply_membership(iface, data=data or {}, extra_actions=None, restore_all=True)
