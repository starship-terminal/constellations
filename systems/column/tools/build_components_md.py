#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json. Run after measure.mjs."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
src = HERE / "raw" / "components-computed.json"
if not src.exists():
    raise SystemExit("missing raw/components-computed.json; run measure.mjs first")
data = json.loads(src.read_text())
lines = [
    "# Column components",
    "",
    "Measured on the signed-out public site, 1440 CSS px, device pixel ratio 2. Nothing was typed or submitted.",
    "",
]
for name, comp in data.get("components", {}).items():
    lines.append(f"## {name}")
    lines.append("")
    for state, rec in comp.get("states", {}).items():
        style = rec.get("style", {})
        box = rec.get("box") or {}
        crop = rec.get("crop", "")
        lines.append(f"### {state}")
        lines.append("")
        if crop:
            lines.append(f"![{name} {state}]({crop})")
            lines.append("")
        lines.append(f"- Box: {round(box.get('w', 0))} x {round(box.get('h', 0))} px")
        lines.append(f"- Color: `{style.get('color')}` on `{style.get('backgroundColor')}`")
        lines.append(f"- Type: {style.get('fontFamily', '').split(',')[0]} {style.get('fontSize')} / {style.get('fontWeight')} / {style.get('lineHeight')}")
        lines.append(f"- Radius: `{style.get('borderRadius')}` padding `{style.get('padding')}`")
        if rec.get("note"):
            lines.append(f"- Note: {rec['note']}")
        lines.append("")
lines += [
    "## Gaps",
    "",
    "- Select, checkbox, radio, switch, tabs, tooltip, toast, table, avatar, badge: not measured as product components on the public marketing surface. Docs search dialog was opened and closed with nothing typed.",
    "- Disabled, loading, and error states: not present without submitting a form. Forms were not submitted.",
    "- Login wall controls were photographed and not measured as components, because interacting would mean typing or submitting.",
    "",
]
(HERE / "components.md").write_text("\n".join(lines))
print("components", len(data.get("components", {})))
