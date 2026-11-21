#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = json.loads((ROOT / "raw" / "components-computed.json").read_text())["components"]
crops = sorted(p.name for p in (ROOT / "components" / "crops").glob("*.png"))

lines = [
    "# Glassnode components",
    "",
    "Measured on the public marketing site, the public Studio shell, and the empty Auth0 login wall on 2026-11-21. Signed out. Nothing was typed or submitted. Hover is a real pointer. Pressed is `CSS.forcePseudoState`, so a press crop is a reconstruction of the active state, not a click.",
    "",
    "Crops live in [components/crops/](components/crops/).",
    "",
]
order = [
    ("button-launch", "Button, marketing primary", "Launch Studio on glassnode.com. Near-black fill, white label, 2px radius."),
    ("button-primary", "Button, Studio primary", "Sign up on studio.glassnode.com. Same near-black fill."),
    ("button-login", "Button, quiet", "Log in. Transparent fill, near-black label."),
    ("button-contact", "Link, marketing accent", "Contact us. Lavender-blue label, no fill."),
    ("nav-link", "Link, nav", "About in the marketing header."),
    ("nav-studio", "Link, Studio nav", "Charts in the Studio header."),
    ("menu-trigger", "Menu trigger", "Products button."),
    ("menu-item", "Menu item", "Studio row inside the Products dropdown."),
    ("icon-button", "Icon button", "Studio search trigger."),
    ("text-field", "Text field", "Marketing newsletter email. Focused empty. Not typed, not submitted."),
    ("search-field", "Search field", "Studio header search input."),
    ("search-metrics", "Search field, catalog", "Search metrics on the data page. The reading is the placeholder text node, not the field chrome."),
    ("search-assets", "Search field, assets", "Filter assets. Same caveat."),
    ("radio", "Radio", "24h period label on Studio home. The control is a text toggle, not a native radio widget."),
    ("card", "Card", "A BTC link on Studio home. The measured node is the link, not the chart card chrome."),
    ("auth-email", "Text field, login", "Empty email on auth.glassnode.com. Not typed."),
    ("auth-password", "Text field, password", "Empty password. Not typed. Show-password was not clicked."),
    ("auth-continue", "Button, login submit", "Continue. Default and hover only. Not clicked."),
    ("auth-google", "Button, identity provider", "Continue with Google. Photographed. Not clicked."),
]
for key, title, note in order:
    states = C.get(key, {})
    lines.append(f"## {title}")
    lines.append("")
    lines.append(note)
    lines.append("")
    if not states:
        lines.append("Not captured.")
        lines.append("")
        continue
    lines.append("| State | Colour | Background | Size | Radius | Height | Crop |")
    lines.append("|---|---|---|---|---|---|---|")
    for state, row in states.items():
        if not isinstance(row, dict) or "color" not in row:
            lines.append(f"| {state} | | | | | | |")
            continue
        crop = f"{key}-{state}.png"
        crop_cell = f"[{crop}](components/crops/{crop})" if crop in crops else "no crop"
        lines.append(
            f"| {state} | {row.get('color','')} | {row.get('backgroundColor','')} | {row.get('fontSize','')} / {row.get('fontWeight','')} | {row.get('borderRadius','')} | {row.get('height','')} | {crop_cell} |"
        )
    lines.append("")

lines += [
    "## Gaps",
    "",
    "- Text area: not present on the captured public pages.",
    "- Select: the pricing Yearly control and asset pickers were not measured as their own component. Not captured.",
    "- Checkbox: the only checkboxes seen sat on a lead form. Not clicked. Not captured.",
    "- Switch: not present.",
    "- Tabs: Studio home has Overview / Fundamentals / Profit & Loss. Photographed in [studio-home-light-default.png](screenshots/studio-home-light-default.png). Not measured as a component.",
    "- Tooltip: not opened.",
    "- Dialog: the cookie banner was denied, not measured. Search overlay is a dialog-like panel, photographed, not measured.",
    "- Toast: not present.",
    "- Table: Studio home renders a public asset table. Photographed. Row styles not measured.",
    "- Avatar: not present on the signed-out shell.",
    "- Badge: Alpha Lab shows a small dot in the nav. Not measured.",
    "- Disabled, loading, error, validation: not shown on the empty public forms. The login wall shows a reCAPTCHA and was not solved.",
    "- Dark theme: not present. No theme switch was found.",
    "",
]
(ROOT / "components.md").write_text("\n".join(lines))
print("components.md", len(lines), "lines")
