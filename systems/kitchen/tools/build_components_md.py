#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
C = J["components"]

def hexish(c):
    return (c or "").replace("|", "/")

lines = []
W = lines.append
W("# Kitchen.co components")
W("")
W("Measured on kitchen.co on 2026-11-18, signed out, desktop 1440 and phone 390. Hover is a real pointer. Focus-visible is keyboard focus. Pressed is a DevTools `:hover:active` force, so no link fired. Login, signup, demo and Stripe checkout were not submitted.")
W("")
W("## Inventory")
W("")
W("| Component | Group | Page | States |")
W("|---|---|---|---|")
for k, c in C.items():
    if c.get("missing"):
        W(f"| {c.get('title', k)} | {c.get('group', '')} | {c.get('page', '')} | not present on the captured page |")
        continue
    states = ", ".join(c.get("states") or {})
    W(f"| {c.get('title', k)} | {c.get('group', '')} | {c.get('page', '')} | {states} |")
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
W("- Text area, select, checkbox, radio, switch, tooltip, dialog, toast, table and badge do not paint on the public marketing pages that were captured.")
W("- Tabs exist in the stylesheet (`.plans-tabs__button`, `.js-tabs-v2__tab`) but no plans tab was in the DOM on `/pricing` during this capture.")
W("- Feature cards use illustration bands rather than a `.card` atom on the home page, so that selector missed. The plan card, review card and article search field were measured instead.")
W("- Disabled, loading, error and selected states sit behind form submission, checkout or the signed-in app.")
W("- The product app at `*.kitchen.co` workspaces was not entered. Login stops at the workspace URL field.")
(ROOT / "components.md").write_text("\n".join(lines) + "\n")
print("components.md", len(lines), "lines")
