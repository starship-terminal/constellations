#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json and the crops."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "raw" / "components-computed.json").read_text())
comps = data["components"]

lines = [
    "# Zellerfeld components",
    "",
    "Measured on the public storefront on 2026-11-21, signed out, headed Chrome.",
    "Desktop 1440x900. Phone controls are the 390x844 rows. One theme.",
    "Hover is a real pointer. Focus-visible is keyboard Tab. Pressed is",
    "`CSS.forcePseudoState` with hover and active, so the control does not fire.",
    "A crop is the element screenshot. Values are computed styles.",
    "",
    "Shared values: page `#171717` (`light.background.page`), text `#ffffff`",
    "(`light.text.primary`), muted white at 50% (`light.text.muted`), ember",
    "`#ff5e3e` (`light.accent.default`), focus `#3773f5` (`light.focus.ring`),",
    "control face white at 10% (`light.background.muted`). Phonic is the",
    "control face. Lateral is the wordmark face. Exposure is the display face.",
    "",
]
order = [
    "nav-button", "wordmark", "create-link", "sign-in-button", "search-field",
    "nav-drawer", "nav-link", "sort-chip", "product-card", "buy-button",
    "wishlist-button", "color-swatch", "gallery-thumb", "accordion",
    "newsletter-field", "newsletter-submit", "footer-link",
    "mobile-nav-button", "mobile-nav-drawer", "cookie-accept",
]
for key in order:
    c = comps.get(key)
    if not c:
        continue
    lines.append(f"## {key}")
    lines.append("")
    if c.get("note"):
        lines.append(c["note"])
        lines.append("")
    lines.append(f"Page: {c.get('page', '')}. Role: {c.get('role', '')}.")
    lines.append("")
    lines.append("| State | How | Crop | Face | Text | Radius | Height |")
    lines.append("|---|---|---|---|---|---|---|")
    for state, row in c.get("states", {}).items():
        style = row.get("style") or {}
        crop = row.get("crop")
        crop_cell = f"[crop](components/crops/{crop})" if crop else "not captured"
        lines.append(
            "| {state} | {via} | {crop} | {bg} | {color} | {radius} | {height} |".format(
                state=state,
                via=row.get("via", ""),
                crop=crop_cell,
                bg=style.get("backgroundColor", ""),
                color=style.get("color", ""),
                radius=style.get("borderRadius", ""),
                height=style.get("height", ""),
            )
        )
    lines.append("")

lines += [
    "## Gaps",
    "",
    "- Text area, select, checkbox, radio, switch, tabs, tooltip, toast, table, avatar, badge: not present on the public pages that were opened.",
    "- Disabled and loading: not shown on a resting public control.",
    "- Error on a field: not captured. No form was submitted.",
    "- Cookie accept: the banner was removed before measurement so consent was never clicked. The cookie banner is in `screenshots/home-light-cookie.png`.",
    "- Dark theme: not present.",
    "- Signed-in account, cart, checkout, wishlist contents: behind the Clerk sign-in wall. Stopped.",
    "",
]
(ROOT / "components.md").write_text("\n".join(lines))
print("wrote components.md", len(order), "entries")
