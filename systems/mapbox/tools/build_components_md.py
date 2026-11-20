#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
C = J.get("components", {})
def cell(text):
    """A table cell: a pipe would split it and a newline would end the row."""
    return " ".join(str(text).split()).replace("|", "\\|")


lines = ["# Mapbox components", "", "Measured on the public signed-out site. A missing row was not on the page.", ""]
for key in sorted(C):
    c = C[key]
    lines.append(f"## {c.get('title') or key}")
    lines.append("")
    lines.append(f"{c.get('desc') or ''} Group: {c.get('group') or 'n/a'}. Selector: `{c.get('selector') or key}`.")
    lines.append("")
    if c.get("missing"):
        lines.append("Not present on the captured page.")
        lines.append("")
        continue
    lines.append("| State | Size | Background | Text | Via |")
    lines.append("|---|---|---|---|---|")
    for state, s in (c.get("states") or {}).items():
        if s.get("via") == "focus failed":
            # D4: keyboard focus never reached the element, so the reading is the element at rest. It
            # is listed as not captured rather than shown as the focus state, as the kit does.
            lines.append(f"| {cell(state)} |  |  |  | not captured: keyboard focus did not reach the element |")
            continue
        if s.get("error") and "style" not in s:
            lines.append(f"| {cell(state)} |  |  |  | {cell(s['error'][:80])} |")
            continue
        style = s.get("style") or {}
        rect = s.get("rect") or {}
        size = f"{rect.get('w', '')} x {rect.get('h', '')}"
        bg = style.get("backgroundColor", "")
        color = style.get("color", "")
        via = cell(s.get("via") or "")
        crop = s.get("crop")
        name = f"[{state}]({crop})" if crop else state
        lines.append(f"| {name} | {size} | {bg} | {color} | {via} |")
    lines.append("")
lines.append("## Gaps")
lines.append("")
lines.append("The account console, token creation, checkout and any submitted form sit behind sign-in or were not submitted. Checkbox, radio, switch, toast, avatar and table did not mount on the public pages captured. The contact form has no text area. The pricing number input is `display: none` beside the visible range.")
lines.append("")
(ROOT / "components.md").write_text("\n".join(lines))
print("components", len(C))
