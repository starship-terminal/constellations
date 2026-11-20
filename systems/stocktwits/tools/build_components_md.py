#!/usr/bin/env python3
"""Write components.md from the measured component list. Crops are listed when the file exists."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
comp = json.loads((HERE / "raw" / "components-computed.json").read_text())
lines = [
    "# Components",
    "",
    "Measured on stocktwits.com, signed out, light theme, 2026-11-21. Crops are in [components/crops/](components/crops).",
    "",
]
for name, states in comp.get("components", {}).items():
    lines.append(f"## {name}")
    lines.append("")
    for state, row in states.items():
        style = row.get("style", {})
        bits = ", ".join(f"{k} {v}" for k, v in style.items() if k in ("color", "backgroundColor", "fontSize", "fontWeight", "borderRadius", "height") and v)
        crop = row.get("crop")
        crop_bit = f" Crop: [{crop}]({crop})." if crop else ""
        lines.append(f"- {state}: {bits}.{crop_bit} Page `{row.get('page', '')}`.")
    lines.append("")
lines += [
    "## Also measured, no crop",
    "",
    "- Bullish chip: fill rgb(224, 247, 239), 14px semibold, pill. [raw/extra-readings.json](raw/extra-readings.json).",
    "- Bearish chip: fill rgb(251, 230, 227), 14px semibold, pill.",
    "- Text field on /signin: fill #f2f2f7, radius 8px, height 40px. Placeholder Email or Username. Nothing typed.",
    "- Disabled Log In: fill #d1d1d6, white label, pill, 40px.",
    "",
    "## Gaps",
    "",
    "- Checkbox, radio, switch, select, text area, tooltip, toast, dialog (destructive): not present on the public pages that loaded, or not opened.",
    "- Focus ring: the search field and the login field were focused. Computed outline did not change in the reading. Focus colour is Not captured.",
    "- Pressed and loading: not held. Not captured.",
    "- Dark theme: the product stayed on `data-theme=light` with `prefers-color-scheme: dark`. Not present as a public theme.",
    "- Card radius: visible in screenshots, not read from a computed style. Not captured.",
    "- Hover on Sign Up was read (fill #2c2c2e). Other hovers were not.",
    "",
]
(HERE / "components.md").write_text("\n".join(lines))
print("wrote components.md")
