#!/usr/bin/env python3
"""Write components.md from the SavvyCal public measurements."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
C = J["components"]
crops = sorted(p.name for p in (ROOT / "components" / "crops").glob("*.png"))

lines = []
w = lines.append
w("# SavvyCal components")
w("")
w("Measured on the public site on 2026-11-21, signed out. Values are computed styles. Crops are the element screenshots taken with those readings.")
w("")
w(f"{len(C)} components, {len(crops)} crops.")
w("")
w("## Inventory")
w("")
w("| Component | Group | Page | States |")
w("|---|---|---|---|")
for key, comp in C.items():
    states = ", ".join(comp.get("states", {})) or "missing"
    miss = " (missing)" if comp.get("missing") else ""
    w(f"| {comp.get('title', key)}{miss} | {comp.get('group', '')} | {comp.get('page', '')} | {states} |")
w("")
w("## Shared values")
w("")
w("Marketing pages paint oatmeal `#fcf7ed` as the page, sand `#f4ebda` as a raised band, orange `#f54320` as the accent, neon green `#b9ff78` on the login submit, and olive ink `#0c0c09` for text. Controls are pills (`border-radius` computed as a huge pixel value, tokenised as `9999px`). UI type is Inter Variable. Display type is GT Alpina Condensed.")
w("")
w("## Gaps")
w("")
w("- Text area, select, checkbox (beyond the login Remember me control, which was not measured), radio, switch, tooltip, dialog, toast, table, avatar, and badge are not present on the public marketing pages, or were not reached.")
w("- The login Remember me control is a checkbox. It was visible. It was not measured. Not captured.")
w("- Disabled, loading, and error states were not shown on the public pages. Not captured.")
w("- Pressed colour did not differ from default under a CDP active state. Not captured as a distinct colour.")
w("- Dark theme utilities exist in the login CSS. No control switched them. Not captured.")
w("- Signed-in app screens sit behind https://savvycal.com/login. Not captured.")
w("")
(ROOT / "components.md").write_text("\n".join(lines) + "\n")
print("components.md", len(C), "crops", len(crops))
