#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json. Values are copied from the readings."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
J = json.loads((HERE / "raw" / "components-computed.json").read_text())
C = J["components"]

KEEP = ["width", "height", "paddingTop", "paddingLeft", "borderTopLeftRadius", "backgroundColor", "color", "fontFamily", "fontSize", "fontWeight", "lineHeight"]

lines = [
    "# Components",
    "",
    "Public signed-out Discord, measured on the live page by `tools/capture/public/measure.mjs`. A value below is the computed style of that element. Hover is a real pointer hover. Nothing was submitted.",
    "",
]
for name, comp in C.items():
    lines.append(f"## {name}")
    lines.append("")
    for state, row in comp["states"].items():
        style = (row.get("style") or {}).get("style") or {}
        crop = row.get("crop") or "Not captured"
        lines.append(f"### {state}")
        lines.append("")
        if crop and not str(crop).startswith("crop failed"):
            lines.append(f"![{name} {state}]({crop})")
            lines.append("")
        lines.append("| Property | Value |")
        lines.append("|---|---|")
        for k in KEEP:
            if k in style:
                lines.append(f"| {k} | {style[k]} |")
        if row.get("note"):
            lines.append("")
            lines.append(row["note"])
        lines.append("")

lines += [
    "## Gaps",
    "",
    "| Component | Status |",
    "|---|---|",
    "| Button | Captured. Hero download (default and hover) and Open-in-browser (default). Pressed and disabled: Not captured |",
    "| Icon button | Not captured |",
    "| Link | Captured. Nav Download, default and hover |",
    "| Text field | Partial. Server search default and focused. Login email field measured empty. Not typed into |",
    "| Text area | Not present |",
    "| Select | Language menu photographed. A locale was not chosen, so no selected state |",
    "| Checkbox, radio, switch | Not captured. Register shows a checkbox and was not filled |",
    "| Tabs | Not present on the captured public pages |",
    "| Menu | Discover menu opened and cropped. Safety and Developers menus photographed |",
    "| Tooltip | Not captured |",
    "| Dialog | Cookie Settings not opened |",
    "| Toast | Not present |",
    "| Card, list row | Visible in screenshots. Not cropped |",
    "| Table | Not present |",
    "| Avatar, badge | Not captured |",
    "",
]
(HERE / "components.md").write_text("\n".join(lines))
print("wrote components.md", len(C), "components")
