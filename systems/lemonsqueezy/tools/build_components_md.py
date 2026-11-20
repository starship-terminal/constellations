#!/usr/bin/env python3
"""Write components.md from the measured public components."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = json.loads((ROOT / "raw" / "components-computed.json").read_text())["components"]

ORDER = [
    ("Buttons", ["nav-button", "button-primary", "button-orchid", "button-yellow", "button-green", "button-purple", "login-submit", "login-google", "docs-cta", "menu-button", "smp-cta"]),
    ("Links", ["nav-link", "footer-link", "text-link", "login-link"]),
    ("Fields", ["login-email", "login-password", "register-name", "select-country", "login-remember"]),
    ("Chrome", ["banner", "logo", "faq", "price-card", "docs-nav", "mobile-menu", "smp-card", "login-error"]),
]

def cell(text):
    """Text for one Markdown table cell: a pipe or a line break would split the row."""
    return " ".join(str(text).split()).replace("|", "\\|")


def line(key):
    c = C.get(key)
    if not c:
        return f"### {key}\n\nNot measured.\n"
    states = c.get("states") or {}
    if c.get("missing") or not states:
        return f"### {c.get('title', key)}\n\nNot captured. The selector did not match a visible element on {c.get('url', 'the page')}.\n"
    bits = [f"### {c.get('title', key)}", "", c.get("desc", ""), "", f"Page: {c.get('url', '')}", ""]
    bits.append("| State | Size | Fill | Text | Radius | Crop |")
    bits.append("|---|---|---|---|---|---|")
    for st, s in states.items():
        if s.get("error"):
            bits.append(f"| {st} | | | | | error: {cell(s['error'][:80])} |")
            continue
        style = s.get("style") or {}
        rect = s.get("rect") or {}
        crop = s.get("crop") or ""
        crop_cell = f"[crop]({crop})" if crop else ""
        bits.append(
            f"| {st} | {round(rect.get('w', 0))}×{round(rect.get('h', 0))} | {style.get('backgroundColor', '')} | {style.get('color', '')} | {style.get('borderTopLeftRadius', '')} | {crop_cell} |"
        )
    bits.append("")
    return "\n".join(bits)

parts = [
    "# Components",
    "",
    "Public Lemon Squeezy controls measured on 2026-11-18, plus the closed-signup card and a failed sign-in. Get started was not followed. The dashboard was not opened.",
    "Colours below are the computed values. The token names that hold the same values are in [tokens.json](tokens.json).",
    "",
    "Not present on the public surfaces: text area, radio, switch, tabs, tooltip, toast, table, avatar, badge. New store signups are closed, so the signed-in app was not reached.",
    "",
]
for title, keys in ORDER:
    parts.append(f"## {title}")
    parts.append("")
    for key in keys:
        parts.append(line(key))

gaps = """## Gaps

- Text area, radio, switch, tabs, tooltip, toast, table, avatar and badge do not appear on the public marketing site, the docs or the sign-in card.
- The docs search button and its dialog were not measured. The button's accessible name did not match the selector used on 2026-11-18. The search overlay is in [screenshots/docs-help-light-search.png](screenshots/docs-help-light-search.png).
- Disabled and loading are not shown on any public control. The sign-in error is the red sentence after a failed email/password submit. The register required-field tooltip is the browser's native one.
- Hover on the marketing pills often moves a child overlay rather than the measured node's own fill. The primary hero button does change its own fill to yellow on hover. The auth submit changes from #7047eb to #7e59ed.
- Focus on marketing links is the browser outline (1px auto, #005fcc). Focus on auth fields is a 2px #7047eb ring.
"""
parts.append(gaps)
(ROOT / "components.md").write_text("\n".join(parts))
print("components.md", len(C), "entries")
