#!/usr/bin/env python3
"""Write components.md from the crop list and the measured readings."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
crops = sorted(p.name for p in (ROOT / "components" / "crops").glob("*.png"))
comp = json.loads((ROOT / "raw" / "components-computed.json").read_text())
lines = [
    "# Components",
    "",
    "Measured on www.ikea.com/sg/en, signed out, 2026-11-19. Add to cart and the login submit were never activated. Consent was hidden, never clicked.",
    "",
    "| Crop | What it shows |",
    "|---|---|",
]
for name in crops:
    lines.append(f"| [{name}](components/crops/{name}) | {name.removesuffix('.png').replace('-', ' ')} |")
lines += ["", "## Measured controls", ""]
for name, row in comp["components"].items():
    st = row.get("style", {})
    lines.append(
        f"- **{name}**: {row.get('text', '')[:60]} — bg {st.get('backgroundColor')}, text {st.get('color')}, {st.get('fontSize')}, radius {st.get('borderRadius')}, {row.get('rect')}"
    )
lines.append("")
(ROOT / "components.md").write_text("\n".join(lines))
print("components.md", len(crops), "crops")
