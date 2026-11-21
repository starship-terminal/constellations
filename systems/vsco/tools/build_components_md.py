#!/usr/bin/env python3
"""Write components.md from the measured component list. Deterministic."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
crops = sorted(p.name for p in (ROOT / "components" / "crops").glob("*.png"))
lines = ["# VSCO components", "",
         "Public marketing site and the login wall, measured 2026-11-21. Values are token names. Crops are the live elements.",
         "",
         "| Component | States | Crop | Notes |",
         "|---|---|---|---|"]
groups = {}
for name in crops:
    stem = name[:-4]
    comp, _, state = stem.rpartition("-")
    if state not in ("default", "hover", "focus-visible", "pressed", "selected", "focus", "disabled"):
        comp, state = stem, "default"
    groups.setdefault(comp, []).append(state)
notes = {
    "button-gold": "Fill `light.accent.gold`, text `light.text.onGold`, height `core.size.button`, radius `core.radius.pill`. Hover fill `light.accent.goldHover`.",
    "button-primary": "Fill `light.action.primary`, text `light.text.onAccent`, height `core.size.buttonSmall`. Hover computed style did not change.",
    "button-banner": "Fill `light.accent.pink`. Hover fill `light.accent.pinkHover` and the label went grey.",
    "button-outline": "Not captured as a crop. The LOG IN control is an outline pill in the header screenshot.",
    "button-disabled": "Not cropped. Disabled CONTINUE on the login URL email step is `light.action.disabled`.",
    "nav-menu": "15px / 500, transparent, 8px vertical padding. Focus-visible paints a 1px auto outline.",
    "menu-link": "Opens from PRODUCTS. 16px / 400. Transition 450ms.",
    "tab": "11px / 600, white on the dark band. Selected is a local pane, not a route.",
    "hero-heading": "100px / 500, black, two lines at 90px line height.",
    "badge": "4px radius. The NEW chip in the promo bar.",
    "accordion": "Plans FAQ row. Selected opens the answer on the same page. No dialog.",
    "icon-button": "Phone menu control, 24px.",
    "drawer-link": "PRICING in the phone drawer.",
    "text-field": "Login email input when the password form loaded. The later visit to the same URL showed an email-only step instead.",
    "field-shell": "Not captured. The input's parent painted no border in a later probe.",
    "card": "What's new card on the dark band.",
    "plan-cta": "SELECT VSCO ONE. Not clicked. Purchase path.",
    "link": "Footer link. Crop failed because the box was too small.",
}
for comp, states in groups.items():
    crop = f"[components/crops/{comp}-{states[0]}.png](components/crops/{comp}-{states[0]}.png)"
    lines.append(f"| {comp} | {', '.join(states)} | {crop} | {notes.get(comp, '')} |")

lines += ["", "## Gaps", "",
          "- Text area, select, checkbox, radio, switch, tooltip, toast, table, avatar: not present on the captured public pages.",
          "- Dialog: the OneTrust preference center exists and was not opened. No product dialog was opened.",
          "- Disabled, error, and loading on marketing buttons: not present. The login CONTINUE button is disabled until an email is typed. Email was not typed.",
          "- Hover on the ink button did not change computed color. Gold and pink did.",
          "- Focus ring colour is the browser auto outline, not a custom colour.",
          ""]
(ROOT / "components.md").write_text("\n".join(lines))
print("components", len(groups), "crops", len(crops))
