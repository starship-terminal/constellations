#!/usr/bin/env python3
"""Write components.md for the Square public capture.

Component states that were not measured on a live element are listed as
Not captured. This builder does not invent computed styles.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
shots = sorted(p.name for p in (ROOT / "screenshots").glob("*.png")) if (ROOT / "screenshots").exists() else []
shot_list = "\n".join(f"- [{n}](screenshots/{n})" for n in shots) or "- none yet"

text = f"""# Square components

Public marketing site only, captured 2026-11-21 from https://squareup.com/us/en. Signed-in dashboard components are behind the login wall and are Not captured.

## What was seen

{shot_list}

## Inventory

| Component | On the public site | States captured | Gap |
|---|---|---|---|
| Button | Pill "Get started" and quiet "Contact sales" | default in screenshots | hover, focus-visible, pressed, disabled, loading: Not captured as separate crops |
| Icon button | Cart, carousel previous/next, mobile menu | default | hover and pressed: Not captured |
| Link | Header, footer, in-page | default | hover colour is `inherit` in the token file; a distinct hover style was not measured |
| Text field | Help search, contact form | focused screenshot where the page loaded | filled, error, disabled: Not captured. No text was typed |
| Text area | Contact form, if present | not separately cropped | Not captured |
| Select | Country switcher in the footer | opened enough to see Canada | options not captured as a component crop |
| Checkbox | Cookie dialog (hidden, not accepted) | Not captured | consent control was not clicked |
| Radio | Not seen on the captured pages | not present on the captured surface | |
| Switch | Not seen | not present on the captured surface | |
| Tabs | Homepage audience stats | default | selected state: Not captured as its own crop |
| Menu | Business types, Products, What's new, cart popover | open screenshots | item hover: Not captured |
| Tooltip | Not seen | not present on the captured surface | |
| Dialog | Cookie preferences on first paint | hidden, not accepted, so no committed screenshot of the dialog body | Not captured |
| Toast | Not seen | not present on the captured surface | |
| Card | Plan cards, hardware cards | default in page screenshots | hover: Not captured |
| List row | Footer link columns, help articles | default | |
| Table | Not seen on the captured marketing pages | not present on the captured surface | |
| Avatar | "Ask our team" faces in the launcher | observed in the homepage screenshot | not cropped |
| Badge | "BEST VALUE" on Square Plus | observed on the homepage | not cropped |

## Shared values

Taken from [tokens.json](tokens.json), not from screenshots.

- Page and surface are `#ffffff` in light and `#000000` in the declared dark set.
- Text is `#000000` on light and `#ffffff` on dark. Muted is `#707070` (light) and `#999999` (dark).
- Primary actions are black pills with white type, radius 50px on the live "Get started" link (computed on the homepage). The token `--action-variant-button-border-radius` is the design-system radius, recorded in `core.radius.button`.
- Focus colour token is the form-field focus custom property: `#000000` light, `#ffffff` dark. Focus ring width was not measured. Not captured as a crop.
- Motion durations: 150ms quick, 300ms default, 400ms slow. Easings are the four cubic-bezier tokens in `core.motion.easing`.

## Gaps

- Dashboard, POS, banking account, payroll and any signed-in screen: auth wall. Branch stopped at login and signup. Not captured.
- Dark theme as a painted page: the public homepage does not set `data-color-mode=dark`. Dark tokens are declared values, not a live screenshot.
- Hover, pressed, disabled, loading and error states were not forced into crops in this capture. Not captured.
- Cookie dialog was hidden rather than accepted. Its controls are Not captured.
"""
(ROOT / "components.md").write_text(text)
print("wrote components.md")
