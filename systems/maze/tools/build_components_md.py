#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json. Deterministic."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
C = J["components"]

ORDER = [
    "button-primary", "button-secondary", "button-primary-hero", "plan-cta",
    "link-login", "nav-link", "footer-link", "display", "pricing-title",
    "text-field", "select", "footer", "plan-region",
]
LABELS = {
    "button-primary": "Primary button (header Get a demo link wrapper)",
    "button-secondary": "Secondary button (header Try Maze for free link wrapper)",
    "button-primary-hero": "Hero Get a demo link",
    "plan-cta": "Pricing plan call to action",
    "link-login": "Log in link (not followed)",
    "nav-link": "PRICING nav link",
    "footer-link": "Footer privacy link",
    "display": "Homepage display heading",
    "pricing-title": "Pricing heading",
    "text-field": "Demo email field (empty, not submitted)",
    "select": "Demo select (not changed)",
    "footer": "Homepage footer",
    "plan-region": "Pricing main region",
}

lines = [
    "# Maze components",
    "",
    "Measured on the public site, light theme, 1440 CSS pixels, 2026-11-21.",
    "Crops are in [components/crops/](components/crops). Login and signup were not opened. No form was submitted.",
    "",
    "The header call-to-action measurements below are on the wrapping `<a>`, whose background is transparent. The painted button inside Get a demo is Phonic 17px, fill `oklch(0.226 0 0)` (`#1c1c1c`), white text, 8px radius, 40px height, padding 8px 16px. That inner button is recorded in the README and in the style guide. A later measure pass should crop the inner button.",
    "",
]
for key in ORDER:
    if key not in C:
        continue
    comp = C[key]
    lines.append(f"## {LABELS.get(key, key)}")
    lines.append("")
    lines.append(f"Page: `{comp.get('page', '')}`.")
    lines.append("")
    lines.append("| State | Size | Weight | Colour | Background | Radius | Crop |")
    lines.append("|---|---|---|---|---|---|---|")
    for state, s in comp.get("states", {}).items():
        crop = s.get("crop") or ""
        crop_cell = f"[crops/{crop}](components/crops/{crop})" if crop else ""
        lines.append(
            f"| {state} | {s.get('fontSize','')} | {s.get('fontWeight','')} | {s.get('color','')} | {s.get('backgroundColor','')} | {s.get('borderRadius','')} | {crop_cell} |"
        )
    lines.append("")

lines += [
    "## Gaps",
    "",
    "- Checkbox, radio, switch, tabs, tooltip, dialog, toast, table, avatar and badge were not isolated as product components on the captured public pages. Pricing and AI pages have in-page toggles and tabs. Those are screenshots, not a measured component set.",
    "- Hover, focus-visible and pressed were forced with CSS pseudo-states on the wrapping link. Several crops show no paint change because the fill sits on the inner button.",
    "- Disabled, loading and error states were not present on the public pages.",
    "- Text area was not found on the demo page at capture time.",
    "- Dark theme is not present.",
    "- The signed-in app (studies, reports, panel, builder) is behind https://auth.maze.co/login and was not entered.",
    "- Focus ring token: Not captured. No dedicated focus custom property was declared.",
    "- Warning and info colour roles: Not captured as semantic tokens. Yellow and blue ramps exist. They are not aliased to warning or info.",
    "",
]
(ROOT / "components.md").write_text("\n".join(lines))
print("components", len([k for k in ORDER if k in C]))
