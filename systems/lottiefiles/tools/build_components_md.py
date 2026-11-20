#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
C = J["components"]

# Entries the measure pass could not read, described by hand at capture time from the page
# screenshot (no values were read for them).
HAND = {
    "animation-download": ("Download tab", [
        "The animation page already has Download selected. Clicking the tab did not open a new panel. Format buttons (MP4, WebM, MOV, SVG, GIF) are visible in the page screenshot. No file was downloaded. Some formats sit behind sign-in.",
        "The measure pass did not isolate a control named Download, so there is no crop. See [animation-light-download-tab.png](screenshots/animation-light-download-tab.png).",
    ]),
}


def cell(v):
    """A value written into a table cell: one line, no pipe."""
    return " ".join(str(v).split()).replace("|", "\\|")

lines = ["# LottieFiles components", "",
         "Measured on lottiefiles.com, signed out, desktop 1440. Colours are computed styles. Crops are in [components/crops/](components/crops/).",
         "Log in, Sign up, checkout and the editor were never followed.", ""]

for key in sorted(C):
    comp = C[key]
    usable = [v for v in comp.get("states", {}).values() if not v.get("error")]
    if key in HAND and (comp.get("missing") or not usable):
        # only while the capture has no reading of its own; a later reading replaces the hand text
        title, paras = HAND[key]
        lines += [f"## {title}", ""]
        for para in paras:
            lines += [para, ""]
        continue
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
            lines.append(f"| {cell(state)} | | | | | {cell(s['error'][:80])} |")
            continue
        rect = s.get("rect") or {}
        size = f"{rect.get('w', '?')} x {rect.get('h', '?')}"
        lines.append(f"| {cell(state)} | {size} | {cell(s.get('backgroundColor', ''))} | {cell(s.get('color', ''))} | {cell(s.get('borderRadius', ''))} | {cell(s.get('via', ''))} |")
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
# Every file the page links must exist (2026-11 audit 18-14: a link written relative to components/).
dead = sorted({t for t in re.findall(r"\]\(((?:screenshots|components|raw)/[^)#\s]+)\)", "\n".join(lines)) if not (ROOT / t).exists()})
if dead:
    raise SystemExit("components.md links files that do not exist: " + ", ".join(dead))
(ROOT / "components.md").write_text("\n".join(lines))
print("wrote components.md", len(C), "components")
