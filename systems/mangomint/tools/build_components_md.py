#!/usr/bin/env python3
"""Write components.md from the Mangomint measurements.

Reads raw/components-computed.json. Colours stay as the measured rgb/hex.
A crop path is linked when the file exists. Deterministic.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
C = J["components"]

ORDER = [
    "nav-trial", "nav-demo", "nav-login", "nav-businesses", "menu-item",
    "video-tour", "faq", "demo-chip", "demo-continue", "trial-chip",
    "login-email", "login-password", "login-toggle", "login-submit", "login-forgot",
    "forgot-email", "forgot-continue", "book-rebook", "learn-search",
]


def rgb(c):
    return c if c else ""


def line(state, s):
    if "error" in s:
        return f"| {state} | not read: {s['error'][:80]} |"
    st = s.get("style") or {}
    bits = [
        st.get("fontSize", ""),
        st.get("fontWeight", ""),
        st.get("color", ""),
        st.get("backgroundColor", ""),
        st.get("borderTopLeftRadius") or st.get("height", ""),
        (s.get("via") or "")[:48],
    ]
    crop = s.get("crop")
    link = f"[crop]({crop})" if crop else ""
    return "| " + state + " | " + " · ".join(b for b in bits if b) + " | " + link + " |"


parts = ["# Mangomint components", "",
         "Measured on the public pages, 2026-11-18, desktop 1440. Nothing was submitted, signed into, or booked.",
         "Pressed rows are CDP `forcePseudoState` (`:active` and `:hover`). A focus row whose `via` is `focus failed` did not land.",
         ""]
for key in ORDER:
    c = C.get(key)
    if not c:
        continue
    parts.append(f"## {c.get('title') or key}")
    parts.append("")
    parts.append(f"Group: {c.get('group', '')}. URL: `{c.get('url', '')}`.")
    parts.append("")
    if c.get("missing"):
        parts.append("Not found on the page.")
        parts.append("")
        continue
    parts.append("| State | Reading | Crop |")
    parts.append("|---|---|---|")
    for state, s in c.get("states", {}).items():
        parts.append(line(state, s))
    parts.append("")

parts += [
    "## Gaps",
    "",
    "Checkbox, radio, switch, select, text area, tabs, tooltip, toast, table, avatar and badge were not present on the captured signed-out surfaces.",
    "The public booking page at `booking.mangomint.com/737397` listed no services, so a service row, a slot, and a booking form were not captured. No appointment was booked.",
    "Demo and trial Continue were measured and not pressed, so step 2, validation, and any account creation were not reached.",
    "Log In was not pressed. The salon admin behind sign-in was not entered.",
    "",
]
(ROOT / "components.md").write_text("\n".join(parts))
print("components.md", len(parts))
