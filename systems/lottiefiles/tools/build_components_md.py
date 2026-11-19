#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
C = J["components"]

lines = ["# LottieFiles components", "",
         "Measured on lottiefiles.com, signed out, desktop 1440. Colours are computed styles. Crops are in [components/crops/](components/crops/).",
         "Log in, Sign up, checkout and the editor were never followed.", ""]

for key in sorted(C):
    comp = C[key]
    lines.append(f"## {comp.get('title') or key}")
    lines.append("")
    if comp.get("desc"):
        lines.append(comp["desc"])
        lines.append("")
    if comp.get("missing"):
        lines.append("Not found on the page during this run.")
        lines.append("")
        continue
    lines.append("| State | Size | Background | Text | Radius | Via |")
    lines.append("|---|---|---|---|---|---|")
    for state, s in comp.get("states", {}).items():
        if s.get("error"):
            lines.append(f"| {state} | | | | | {s['error'][:80]} |")
            continue
        rect = s.get("rect") or {}
        size = f"{rect.get('w', '?')} x {rect.get('h', '?')}"
        lines.append(f"| {state} | {size} | {s.get('backgroundColor', '')} | {s.get('color', '')} | {s.get('borderRadius', '')} | {s.get('via', '')} |")
    lines.append("")
    crops = [s.get("crop") for s in comp.get("states", {}).values() if s.get("crop")]
    if crops:
        lines.append("Crops: " + ", ".join(f"[{c.split('/')[-1]}]({c})" for c in crops))
        lines.append("")

lines += [
    "## Gaps",
    "",
    "Select, checkbox, radio, switch, tooltip, dialog, toast, table, avatar and badge were not isolated on the public pages.",
    "Text field and text area were not submitted. The header search opened as a focus shot only.",
    "The editor, dashboard, sign-in form and checkout were not opened.",
    "",
]
(ROOT / "components.md").write_text("\n".join(lines))
print("wrote components.md", len(C), "components")
