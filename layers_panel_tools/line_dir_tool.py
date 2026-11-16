# -*- coding: utf-8 -*-
"""线方向检查：自选起点与多个线图层，端点在容差内才相接（自 AttributeTable 1.18.11 移植）。"""

from .buttons import make_menu_action as build_menu_action, make_toolbar_button
from .i18n import tr
from .icons import load_icon
from .plugin_settings import plugin_qsettings

_HOST = None
_TOLERANCE_KEY = "line_dir_tolerance"


class _Log(object):
    def __init__(self):
        self.text = ""

    def setPlainText(self, text):
        self.text = text or ""


class _Host(object):
    def __init__(self, iface):
        self.iface = iface
        self.log = _Log()
        self.layers = {}
        self.tolerance = 0.6
        self.ui_parent = None
        try:
            raw = plugin_qsettings().value(_TOLERANCE_KEY, 0.6)
            self.tolerance = float(raw)
        except Exception:
            self.tolerance = 0.6
        if self.tolerance <= 0:
            self.tolerance = 0.6

    def _refresh_canvas(self):
        try:
            canvas = self.iface.mapCanvas()
            canvas.refresh()
        except Exception:
            pass  # nosec B110


def make_action(iface):
    tr("线方向检查")
    tr("自选起点和多个线图层，检查线方向是否从起点向外连贯，端点在容差内才算相接")
    return make_toolbar_button(
        iface,
        "lpt:line_dir",
        "LayersPanelToolsLineDir",
        "线方向检查",
        "自选起点和多个线图层，检查线方向是否从起点向外连贯，端点在容差内才算相接",
        load_icon("line_dir"),
        lambda: open_line_dir(iface),
    )


def make_menu_action(iface):
    return build_menu_action(
        iface,
        "LayersPanelToolsLineDirMenu",
        "线方向检查",
        "自选起点和多个线图层，检查线方向是否从起点向外连贯，端点在容差内才算相接",
        load_icon("line_dir"),
        lambda: open_line_dir(iface),
    )


def close_line_dir():
    global _HOST
    try:
        from .line_dir import ntal_line_dir_free as free_mod

        dlg = getattr(free_mod, "_SETUP_DLG", None)
        if dlg is not None:
            try:
                dlg.close()
            except RuntimeError:
                pass  # nosec B110
            free_mod._SETUP_DLG = None
        closer = getattr(free_mod, "close_free_line_dir", None)
        if callable(closer):
            closer()
    except Exception:
        pass  # nosec B110
    try:
        from .line_dir import ntal_line_dir as dir_mod

        old = getattr(dir_mod, "_DIR_DLG", None)
        if old is not None:
            try:
                old.close()
            except RuntimeError:
                pass  # nosec B110
            dir_mod._DIR_DLG = None
    except Exception:
        pass  # nosec B110
    _HOST = None


def open_line_dir(iface):
    global _HOST
    from .line_dir.ntal_line_dir_free import open_free_line_dir

    host = _Host(iface)
    try:
        host.ui_parent = iface.mainWindow()
    except Exception:
        host.ui_parent = None
    _HOST = host
    open_free_line_dir(host)
