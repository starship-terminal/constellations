#!/usr/bin/env python3
"""Write components.md from the measured Overflow components."""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
C = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]

ORDER = [
    ("hero-title", "Display heading", "Homepage and pricing h1, class intro-section__title."),
    ("hero-cta", "Button", "Black primary button, Download - free trial."),
    ("nav-cta", "Button", "Header Download for free, shorter than the hero button."),
    ("nav-signin", "Button", "Quiet Sign In control. Fill appears only while pressed."),
    ("nav-link", "Link", "Header text link. Hover and pressed shift to the blue accent."),
    ("product-trigger", "Link", "Product control that opens the mega menu."),
    ("product-menu", "Menu", "White mega menu, 1440 by 393, hairline #dadce0."),
    ("menu-link", "Link", "Mega menu item. Hover fills #f5f5f6."),
    ("logo", "Link", "Wordmark link. Computed color is the brand blue."),
    ("demo-link", "Link", "Watch product demo. Opens the video dialog."),
    ("plan-card", "Card", "Pricing card, 24px radius, soft shadow."),
    ("plan-cta", "Button", "Start free trial inside the plan card."),
    ("pricing-h1", "Display heading", "Pricing page title, same ramp as the homepage h1, ink on white."),
    ("faq-item", "Accordion", "Closed FAQ opener. Hover does not change the computed fill."),
    ("faq-open", "Accordion", "Same item after click, body opened."),
    ("download-mac", "Button", "Download for Mac. Class btn-gradient, painted black."),
    ("download-h1", "Display heading", "Download page title."),
    ("section-h2", "Heading", "Features section title, 48px extra-bold."),
    ("blog-card", "Badge", "Blog filter pill. The card selector missed the article grid."),
    ("m-menu-button", "Icon button", "Phone navbar toggler, 22px wide."),
    ("m-nav-item", "Link", "Phone menu row, 24px bold."),
]

lines = [
    "# Overflow components",
    "",
    "Measured on https://overflow.io/ on 2026-11-21, signed out, desktop 1440x900 and phone 390x844. Crops are 256-colour PNGs. Read colours from [tokens.json](tokens.json).",
    "",
]
for name, kind, note in ORDER:
    entry = C.get(name, {})
    lines.append(f"## {name}")
    lines.append("")
    lines.append(f"{kind}. {note}")
    lines.append("")
    states = entry.get("states") or {}
    if entry.get("missing") or not states:
        lines.append("Not captured: the selector did not land on a visible element.")
        lines.append("")
        continue
    lines.append("| State | Crop | What changed |")
    lines.append("|---|---|---|")
    base = (states.get("default") or {}).get("style") or {}
    for state, data in states.items():
        crop = f"components/crops/{name}-{state}.png"
        exists = (HERE / "components" / "crops" / f"{name}-{state}.png").exists()
        link = f"[{state}]({crop})" if exists else "no crop"
        style = data.get("style") or {}
        diffs = []
        for key in ("backgroundColor", "color", "transform", "boxShadow"):
            if style.get(key) and style.get(key) != base.get(key):
                diffs.append(f"{key} {style.get(key)}")
        if data.get("via"):
            diffs.append(data["via"])
        if state == "default":
            bg = style.get("backgroundColor", "")
            color = style.get("color", "")
            size = style.get("fontSize", "")
            diffs = [f"{color} on {bg}, {size}, {style.get('fontWeight', '')}"]
        lines.append(f"| {state} | {link} | {'; '.join(diffs) or 'same as default'} |")
    lines.append("")

lines += [
    "## Gaps",
    "",
    "- Text field, text area, select, checkbox, radio, and switch are not on the public marketing pages. The footer newsletter field was not filled.",
    "- Tooltip, toast, table, and avatar were not found as product controls. The homepage shows decorative avatars inside the product demo artwork.",
    "- Disabled, loading, and error states were not present on the captured controls.",
    "- Focus-visible on demo-link and faq-item failed: those nodes are not keyboard-focusable.",
    "- feature-card and integration-card selectors matched the page body. Those crops are not component evidence.",
    "- Success, warning, danger, and info roles were not painted as status colours.",
    "- Dark theme: not present. The site has no theme toggle.",
    "- Signed-in app, editor, and account screens: not captured. https://overflow.io/n/signin and https://overflow.io/n/signup?buy are walls.",
    "",
]
(HERE / "components.md").write_text("\n".join(lines))
print("components.md", len(lines), "lines")
