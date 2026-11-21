#!/usr/bin/env python3
"""Write components.md from the measured public controls."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
C = J["components"]

lines = ["# Components", "", "Measured on byborre.com, signed out, 2026-11-21. Crops are in [components/crops](components/crops). Values are computed styles. A state row is omitted when the reading failed.", ""]
lines.append("| Component | States | Crop |")
lines.append("|---|---|---|")
for name, comp in C.items():
    states = []
    for st, s in comp.get("states", {}).items():
        if s.get("error"):
            states.append(f"{st} ({s['error']})")
        else:
            states.append(st)
    crop = next((s.get("crop") for s in comp.get("states", {}).values() if s.get("crop")), "")
    link = f"[crop]({crop})" if crop else ""
    lines.append(f"| {name} | {', '.join(states)} | {link} |")

lines += ["", "## Gaps", "",
          "Text area and select exist on the contact form and were measured at rest. Checkbox and radio exist as color and tone pickers. The color checkbox crop was a 1px input and was not kept.",
          "Switch, tabs, tooltip, toast, table and avatar are not on the public pages.",
          "Disabled, loading and error-on-field were not shown. No form was submitted, so validation was not captured.",
          "Pressed was not held. Hover and focus-visible were read where the control accepted them.",
          "The signed-in Design Studio was not entered. See [login-review.json](login-review.json).",
          ""]
(ROOT / "components.md").write_text("\n".join(lines))
print("components.md", len(C))
