# Layers Panel Tools

QGIS plugin that adds buttons to the toolbar of the existing Layers panel. Version **1.0.12**. There is no icon on the main QGIS toolbar, and the built-in Layers panel is not replaced.

- **Page:** https://yuyouhui.online/tools/qgis/layers-panel-tools/
- **Issues:** https://github.com/AutoFYQ323/layers-panel-tools/issues
- **QGIS:** 3.28 through 4.99 (Qt 5 and Qt 6)
- **License:** GNU GPL v2 (`layers_panel_tools/LICENSE`)
- **Languages:** 中文, English, Español, Français, العربية. The first open follows the QGIS interface language, then the system language; anything else starts in English. The choice is remembered. Arabic lays plugin windows out from right to left.
- **Data:** local project layers and files you choose. This plugin does not download data, sign in to a website, or call an external service.

## On by default (14)

Labels, batch select, layer manager, edit timeline, batch export, polygon select, feature count, visibility schemes, basemap presets, solo, flash locate, layer actions, line marks, and class export.

Sixteen more are one click away in the settings button at the end of the same toolbar: **multi-point draw line**, **line direction check**, **quick classify**, organize, repair sources, find, show all, hide all, move, opacity, copy style, rename, copy files, color tags, scale check, and render check. The old “split by field into subset layers” button is gone. Writing one file per field value is class export.

## What 1.0.12 adds (from 1.0.5)

- **Line direction check:** pick a start point and several line layers; join only when endpoints meet within the tolerance; reverse wrong segments from the results. Toolbar slot sits between multi-point draw line and organize; **off by default**. Settings use this plugin’s own ini only (`line_dir_free` / `line_dir_tolerance`).
- **Quick classify:** assign selected features from symbology classes; pin a layer to copy geometry from another layer then classify; optional skip-confirm and timed auto-save. Same toolbar area; **off by default**.
- **Multi-point draw line:** pick points by rectangle, polygon, or a drawn line; yellow numbered snap badges appear as soon as each snap is satisfied; lines write automatically after the pick (no separate Generate button). Optional deduplication against a required reference line layer; output to a temporary layer or a chosen line layer. Still on the toolbar before organize; now **off by default** like the two tools above.
- **Settings gear:** stays on the current Layers toolbar layout and is forced visible like other buttons (checkbox required on). Unmatched native tip:/slot: ids no longer wipe the whole saved toolbar order.
- **System properties:** reorder, hide, rename, and group layer right-click items; add this plugin’s layer tools and **third-party installed plugin actions** (toolbox scripts are not listed). Groups are collapsible and color-coded (up to 20). Menu and Toolbar checkboxes: for third-party actions, Toolbar only shows or hides the original top toolbar (PROC-style) and never hangs an icon on the Layers panel toolbar. Opening an empty list silently captures default right-click items; OK on a still-blank page does not overwrite a previously saved order.
- **Stability / i18n:** unload disconnects color-tag and multi-point project listeners; line-direction legend names, “reversed”, and start/end map labels follow the five UI languages.

Each button, and each function inside a multi-function button, can have its own title and keyboard shortcut. Shortcuts work only while the QGIS main window has focus. A shortcut already used by QGIS or by another button is refused, and the holder is named.

When only a category row is selected, solo, flash, and “toggle the selected category” act on that category. A selected layer row still acts on the whole layer.

## Install

1. Download [layers_panel_tools_1.0.12.zip](https://github.com/AutoFYQ323/layers-panel-tools/releases), or use the `layers_panel_tools` folder in this repository. The same zip is also on the page above, named `layers-panel-tools-1.0.12.zip`. You can also search for Layers Panel Tools in the QGIS plugin repository.
2. In QGIS: **Plugins → Manage and Install Plugins → Install from ZIP**.
3. Quit QGIS completely and open it again. Buttons are on the Layers panel toolbar. Settings is the last button on that bar.

## Develop

Run checks with the QGIS Python (this machine: QGIS 3.40.11):

```
python layers_panel_tools/check_i18n.py
python layers_panel_tools/self_test.py
```

`check_i18n.py` requires every user-visible sentence in 中文, English, Español, Français, and العربية. Pack with `python TEST/pack_release.py`. The zip is written in `TEST` and is not committed.
