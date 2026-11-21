#!/usr/bin/env python3
"""Write components.md from the crop filenames. python3 tools/build_components_md.py"""
import pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent
crops = sorted(p.name for p in (PKG / "components" / "crops").glob("*.png"))
lines = ["# Components", "", "Public Zoom controls. Crops are 1x cuts from the 1440 captures.", ""]
for name in crops:
    lines.append(f"- [{name}](components/crops/{name})")
lines += [
    "",
    "## Gaps",
    "",
    "Hover and pressed were not isolated. Text area, checkbox, radio, tooltip, toast, and table were not present on the public pages that were opened. The signup Continue is the disabled state. The annual switch is the selected state. The sign-in field crop includes the focus ring, because the field was focused when the page opened.",
    "",
]
(PKG / "components.md").write_text("\n".join(lines))
print("wrote", len(crops), "crops")
