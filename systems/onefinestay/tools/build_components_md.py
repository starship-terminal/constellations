#!/usr/bin/env python3
"""Write components.md. Lists the screenshots that exist."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
shots = sorted(p.name for p in (ROOT / "screenshots").glob("*.png"))
lines = "\n".join(f"- `{name}`" for name in shots) or "- none"
text = f"""# Components

Public onefinestay.com, signed out, 2026-11-21. One light theme. Crops were not cut.

| Component | States | Evidence |
|---|---|---|
| Button (Inquire Now) | default, hover colour, focus ring | [tokens.json](tokens.json) `light.component.button-inquire`. [home-light-default.png](evidence/screenshots/home-light-default.png). Pressed, disabled, loading: Not captured. |
| Button (cookie Accept) | default, not activated | [home-light-cookie.png](evidence/screenshots/home-light-cookie.png). Fill is `light.accent.default`. Not clicked. |
| Link (nav) | default | `light.component.nav-link`. Hover and pressed: Not captured. |
| Text field | empty | Enquire and the login wall. Not filled. |
| Text area | empty | Enquire message. Not filled. |
| Select | sort on search | [search-light-default.png](evidence/screenshots/search-light-default.png). |
| Checkbox, radio, switch | not present | No product control. OneTrust checkboxes were not opened. |
| Tabs | Calendar and Flexible | [home-light-dates.png](evidence/screenshots/home-light-dates.png). |
| Menu | Destinations, Inspiration, account, phone drawer | [home-light-destinations.png](evidence/screenshots/home-light-destinations.png), [home-light-inspiration.png](evidence/screenshots/home-light-inspiration.png), [home-light-account-wall.png](evidence/screenshots/home-light-account-wall.png), [mobile-home-light-menu.png](evidence/screenshots/mobile-home-light-menu.png). |
| Tooltip | not present | |
| Dialog | cookie, dates, guests, login wall, gallery | cookie, dates, guests, account-wall, listing gallery screenshots. |
| Toast | not present | No action was submitted. |
| Card | home and search cards | Home and search screenshots. |
| List row | destination menu, FAQ | Destinations menu and FAQ screenshots. |
| Table | not present | |
| Avatar | not present | Account glyph only. |
| Badge | not present | |

## Gaps

- Dark theme: not present.
- Signed-in account, bookings, checkout: not captured. `/login` asks for email and password.
- Cookie preference center: not opened. Accept and Continue were not clicked.
- Hover, pressed, disabled, loading, and field error: Not captured, except Inquire Now hover and focus, which were read from computed style.
- Icons: not extracted. Brand artwork stays in the screenshots.
- Crops: not cut.

## Screenshots

{lines}
"""
(ROOT / "components.md").write_text(text)
print("wrote components.md", len(shots), "shots")
