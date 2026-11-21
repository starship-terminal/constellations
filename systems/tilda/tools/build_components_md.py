#!/usr/bin/env python3
"""Write components.md from the measured public components."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = json.loads((ROOT / "raw" / "components-computed.json").read_text())["components"]
crops = sorted(p.name for p in (ROOT / "components" / "crops").glob("*.png"))

lines = [
    "# Tilda components",
    "",
    "Public English pages on tilda.cc, measured 2026-11-21. Crops are the live controls. Values are computed styles, named as tokens where a token exists.",
    "",
    "## Inventory",
    "",
]
for name, comp in C.items():
    lines.append(f"### {name}")
    lines.append("")
    lines.append(f"Page: {comp.get('page', '')}")
    lines.append("")
    for state, s in comp.get("states", {}).items():
        st = s.get("style", {})
        crop = f"{name}-{state}.png"
        link = f"[crop](components/crops/{crop})" if crop in crops else "no crop"
        lines.append(
            f"- {state} ({link}): {st.get('fontSize', '')} {st.get('fontWeight', '')} {st.get('color', '')} on {st.get('backgroundColor', '')}, radius {st.get('borderTopLeftRadius', '')}, height {st.get('height', '')}"
        )
    lines.append("")

lines += [
    "## Gaps",
    "",
    "- Button hover and pressed did not change the computed background on the coral CTA or the cream auth button. Those states are recorded as same-as-default.",
    "- The header PRICING link was not measured (selector missed the text node). LOG IN and SIGN UP were.",
    "- Currency select on /pricing/ had a 0×0 box, so no crop.",
    "- No checkbox, switch, tooltip, toast, table, avatar, or badge was measured as a product control. Template category radios and FAQ chips were.",
    "- Disabled, loading, and error states were not present on the public pages. Forms were not submitted.",
    "- Dark theme: not present.",
    "",
]
(ROOT / "components.md").write_text("\n".join(lines))
print("components", len(C), "crops", len(crops))
