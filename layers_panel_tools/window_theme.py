# -*- coding: utf-8 -*-
"""Parent window helpers for ported tool dialogs. No AttributeTable color theme."""


def register_tool_window(widget):
    """LPT keeps native QGIS styling; keep the hook so ported dialogs still call it."""
    _ = widget


def _is_widget(obj):
    if obj is None:
        return False
    try:
        from qgis.PyQt.QtWidgets import QWidget

        return isinstance(obj, QWidget)
    except Exception:
        return False


def resolve_tool_parent(host, fallback=None):
    """Prefer an explicit ui_parent, then the QGIS main window. Never return a non-widget host."""
    parent = getattr(host, "ui_parent", None)
    if _is_widget(parent):
        return parent
    if _is_widget(fallback):
        return fallback
    iface = getattr(host, "iface", None)
    if iface is not None:
        try:
            main = iface.mainWindow()
            if _is_widget(main):
                return main
        except Exception:
            pass  # nosec B110
    if _is_widget(host):
        return host
    return None
