#!/usr/bin/env python3
"""Write components.md from the measured crops and state readings."""
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
crops = sorted(p.name for p in (HERE / "components" / "crops").glob("*.png"))
lines = [
    "# Components",
    "",
    "Public PlayStation marketing site and PlayStation Store, en-sg, signed out, 2026-11-21. Crops are 2x element screenshots.",
    "",
    "| Component | States captured | Crop |",
    "|---|---|---|",
]
for name in crops:
    lines.append(f"| {name.removesuffix('.png')} | observed | [components/crops/{name}](components/crops/{name}) |")
lines += [
    "",
    "## Gaps",
    "",
    "- Text field, text area, checkbox, radio, switch, select, tooltip, toast, dialog, table, avatar: not present on the captured public pages, or only inside the Sony account wall.",
    "- Search field is visible in [screenshots/home-light-desktop-search.png](../screenshots/home-light-desktop-search.png). It was not typed into and not submitted.",
    "- Disabled, loading, and error states of buttons were not shown on the public pages.",
    "- Add to Cart focus painted no outline. Focus for that control is Not captured.",
    "- Dark theme controls were not displayed. Dark colour roles are declared CSS only.",
    "",
]
(HERE / "components.md").write_text("\n".join(lines))
print("components.md", len(crops), "crops")
