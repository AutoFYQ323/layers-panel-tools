# -*- coding: utf-8 -*-
"""Build the Layers Panel Tools plugin zip. This script lives in TEST; the plugin directory stays beside TEST."""

import pathlib
import re
import subprocess
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "layers_panel_tools"
SKIP_DIRS = {"__pycache__"}
SKIP_FILES = {"self_test.py"}


def _version():
    text = (PLUGIN / "metadata.txt").read_text(encoding="utf-8")
    match = re.search(r"(?m)^version=(.+)$", text)
    if not match:
        raise SystemExit("metadata.txt missing version=")
    return match.group(1).strip()


def main():
    version = _version()
    out = pathlib.Path(__file__).resolve().parent / ("layers_panel_tools_%s.zip" % version)
    check = subprocess.run([sys.executable, str(PLUGIN / "check_i18n.py")], check=False)
    if check.returncode != 0:
        raise SystemExit(check.returncode)
    if out.exists():
        out.unlink()
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in PLUGIN.rglob("*"):
            if not path.is_file():
                continue
            if SKIP_DIRS.intersection(path.parts) or path.name in SKIP_FILES or path.suffix == ".pyc":
                continue
            archive.write(path, path.relative_to(ROOT).as_posix())
    print(out)


if __name__ == "__main__":
    main()
