#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json for the Jace public capture."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
C = J["components"]
lines = []
W = lines.append

W("# Jace AI components")
W("")
W("Public signed-out surfaces measured on 2026-11-18. Marketing pages are light. `app.jace.ai/signin` and `/signup` are the dark product boundary: Google, Outlook and SSO were measured, never pressed. Signup Continue and Continue to signup were clicked to open the OAuth card. There is no email field. The sales form was focused and a sample address was typed then deleted. Nothing was submitted.")
W("")
W("Crops live in [components/crops/](components/crops/). Full pages live in [screenshots/](screenshots/).")
W("")
W("## Inventory")
W("")
W("| Component | Group | States | Crop |")
W("|---|---|---|---|")
for key, c in C.items():
    states = ", ".join(c.get("states") or []) or ("missing" if c.get("missing") else "-")
    crop = ""
    for st, v in (c.get("states") or {}).items():
        if isinstance(v, dict) and v.get("crop"):
            crop = f"[`{key}-{st}`]({v['crop']})"
            break
    title = c.get("title") or key
    W(f"| {title} | {c.get('group','')} | {states} | {crop} |")
W("")
W("## Shared values")
W("")
W("Marketing body text is `rgb(45, 45, 45)` (`#2d2d2d`) in Geist Sans. Display type is Gelica. Pills on the marketing site use a 9999px radius. Product controls on the sign-in page use the `--button-*` and `--radius-*` tokens (6px to 8px on those buttons).")
W("")
W("## Gaps")
W("")
W("- The signed-in inbox, drafts, labels, Flows, settings and billing sit behind Google or Outlook OAuth. Signup was opened through the privacy notice to the OAuth card. There is no email or password field. Google, Outlook and SSO were not pressed.")
W("- The sales form at `/contact/sales` was not submitted, so a posted validation error was not captured. The empty required field was read at rest.")
W("- No textarea is on the sales form. The message control is a text field, not a separate text area. The page ships with sample placeholders, cleared in the committed screenshot.")
W("- The mobile home header has no separate hamburger. Log In and Get started sit in the bar, so the menu-open state is not present.")
W("- Checkbox, radio, switch, select, toast, dialog, tooltip and table are not on the public pages. The pricing FAQ is an accordion, recorded as the FAQ row.")
W("- The inbox table in the home hero is a public demo image, not the signed-in app.")
W("")
(ROOT / "components.md").write_text("\n".join(lines) + "\n")
print("components.md", len(C), "components")
