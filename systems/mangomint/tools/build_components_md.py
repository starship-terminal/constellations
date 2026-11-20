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


def cell(text):
    """A table cell: a pipe would split it and a newline would end the row."""
    return " ".join(str(text).split()).replace("|", "\\|")


def line(state, s):
    if "skipped" in s:
        return f"| {cell(state)} | not captured: {cell(s['skipped'])} | |"
    if s.get("via") == "focus failed":
        # D4: keyboard focus never reached the element, so the reading is the element at rest. It is
        # listed as not captured rather than shown as the focus state (the kit's builder does this).
        return f"| {cell(state)} | not captured: keyboard focus did not reach the element | |"
    if "error" in s:
        return f"| {cell(state)} | not read: {cell(s['error'][:80])} | |"
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
    return "| " + cell(state) + " | " + cell(" · ".join(str(b) for b in bits if b)) + " | " + link + " |"


parts = ["# Mangomint components", "",
         "Measured on the public pages, 2026-11-18, desktop 1440. Nothing was submitted, signed into, or booked.",
         "Pressed rows are CDP `forcePseudoState` (`:active` and `:hover`). A focus row that keyboard focus never reached is listed as not captured. The pressed rows of Book a demo, Try it now, Businesses and Log In equal their default: the 2026-11-18 run forced the first pressed control on each page again, so they are not pressed readings.",
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
