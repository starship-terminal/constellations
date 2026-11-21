#!/usr/bin/env python3
"""Write components.md from the public crop list. python3 tools/build_components_md.py"""
import pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent
crops = sorted(p.name for p in (PKG / "components" / "crops").glob("*.png"))
lines = ["# Components", "", "Public Substack controls. Crops are 1x cuts from the 1440 captures.", ""]
for name in crops:
    lines.append(f"- [{name}](components/crops/{name})")
lines += [
    "",
    "## Gaps",
    "",
    "Hover, pressed, and loading were not isolated. Text area, radio, switch, tooltip, toast, table, and badge were not present on the public pages that were opened. The signup Continue is the disabled state.",
    "",
]
(PKG / "components.md").write_text("\n".join(lines))
print(len(crops), "crops")
