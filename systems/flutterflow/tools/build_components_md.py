#!/usr/bin/env python3
"""Write components.md from the measured public controls.

Readings live in raw/components-computed.json. Nothing is invented: a state
that was not measured is listed under Gaps.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((HERE / "raw" / "components-computed.json").read_text())

lines = [
    "# Components",
    "",
    "Public marketing controls on www.flutterflow.io, measured signed out on 2026-11-21 at 1440×900. Hover and focus were forced in Chromium. Nothing was submitted.",
    "",
]
for name, states in data["components"].items():
    lines.append(f"## {name}")
    lines.append("")
    for state, row in states.items():
        if row.get("miss"):
            lines.append(f"- **{state}**: not captured (selector missed)")
            continue
        s = row.get("style") or {}
        lines.append(
            f"- **{state}**: {s.get('text', '')}. "
            f"color {s.get('color')}, background {s.get('backgroundColor')}, "
            f"{s.get('fontWeight')} {s.get('fontSize')}, radius {s.get('borderRadius')}, "
            f"height {s.get('height')}, padding {s.get('padding')}."
        )
        if row.get("crop"):
            lines.append(f"  Crop: [components/crops/{row['crop']}](components/crops/{row['crop']})")
    lines.append("")

lines += [
    "## Gaps",
    "",
    "- Select, checkbox, radio (form), switch, tabs, tooltip, toast, table, avatar and badge were not present as product controls on the pages measured, or were not reached.",
    "- The footer theme control is a radio group (Match your system, Light, Dark). Its selected state was read for Match your system. Light and Dark were read at rest and not activated, so their selected paint is not captured.",
    "- Pressed and disabled states of the primary button were not held. The primary button's hover paint did not change in the computed style.",
    "- Signed-in app components (canvas, widget tree, property panel) were not captured. The walk stopped at the auth wall.",
    "- Warning and info colour roles are not declared in the public token set. Danger is `--ff-color-danger` (#c4320a light). It was not seen on a painted error.",
    "",
]
(HERE / "components.md").write_text("\n".join(lines))
print("components.md", len(lines))
