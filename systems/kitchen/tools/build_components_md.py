#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
C = dict(J["components"])
app_path = ROOT / "raw" / "app-computed.json"
if app_path.exists():
    app = json.loads(app_path.read_text())
    for k, v in (app.get("components") or {}).items():
        C[k] = v

def hexish(c):
    return (c or "").replace("|", "/")

lines = []
W = lines.append
W("# Kitchen.co components")
W("")
W("Measured on kitchen.co on 2026-11-18. Public pages were signed out. Workspace components were measured on a free signed-in workspace at 1440 and 390. Hover is a real pointer. Focus-visible is keyboard focus. Pressed on marketing controls is a DevTools `:hover:active` force. Signup was completed; invites, creates, DocuMocu connect, Upgrade and Stripe checkout were not submitted.")
W("")
W("## Inventory")
W("")
W("| Component | Group | Page | States |")
W("|---|---|---|---|")

def cell(v):
    """Table-cell text: a "|" or a newline in captured text would break the row."""
    return " ".join(str(v).split("\n")).replace("|", "\\|")

for k, c in C.items():
    if c.get("missing"):
        W(f"| {cell(c.get('title', k))} | {cell(c.get('group', ''))} | {cell(c.get('page', ''))} | not present on the captured page |")
        continue
    states = ", ".join(c.get("states") or {})
    W(f"| {cell(c.get('title', k))} | {cell(c.get('group', ''))} | {cell(c.get('page', ''))} | {cell(states)} |")
W("")
W("## Entries")
W("")
for k, c in C.items():
    W(f"### {c.get('title', k)}")
    W("")
    W(c.get("desc") or "")
    W("")
    W(f"Selector `{c.get('selector', k)}` on `{c.get('url', '')}`.")
    W("")
    if c.get("missing"):
        W("Not on the page when it was captured.")
        W("")
        continue
    for state, st in (c.get("states") or {}).items():
        if "error" in st:
            W(f"- **{state}.** {st['error']}")
            continue
        s = st.get("style") or {}
        W(f"- **{state}.** {st.get('rect', {}).get('w')} x {st.get('rect', {}).get('h')} px. Background {hexish(s.get('backgroundColor'))}. Text {hexish(s.get('color'))}. Font {s.get('fontSize')} / {s.get('fontWeight')} {str(s.get('fontFamily','')).split(',')[0]}. Radius {s.get('borderTopLeftRadius')}. Padding {s.get('paddingTop')} {s.get('paddingRight')}.")
        if st.get("crop"):
            W(f"  ![{k} {state}]({st['crop']})")
    W("")

W("## Gaps")
W("")
W("- Marketing pages still omit text area, select, checkbox, radio, switch, tooltip, toast and badge.")
W("- The workspace shows tabs (All Tasks / Completed), a members table, a proposals dialog, empty states and a yellow Upgrade control. Invite Members, Create Client, Connect DocuMocu, Buy DocuMocu, Buy Lifetime Access and Upgrade were not pressed.")
W("- Theme customisation is paid: Settings > Branding > Theme & Colors shows Upgrade. The free workspace has one light theme.")
W("- Stripe checkout was not opened. Billing was captured as the free-plan settings page.")
(ROOT / "components.md").write_text("\n".join(lines) + "\n")
print("components.md", len(lines), "lines")
