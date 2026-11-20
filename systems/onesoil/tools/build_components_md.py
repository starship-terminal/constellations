#!/usr/bin/env python3
"""Write components.md from the measured public controls. No invented states."""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
text = """# OneSoil components

Public marketing only, read on 2026-11-21 from onesoil.ai. Signed-in app components were not reached.

| Component | Status | Evidence |
|---|---|---|
| Button | captured | Header Schedule a demo (`button-primary`) and Try Free (`button-accent`). Default, hover, focus-visible, pressed. [components/crops/](components/crops) |
| Icon button | not present | No icon-only button on the marketing pages, apart from the chat bubble, which was not measured. |
| Link | captured | Header and footer links. Platform link colour is `light.text.link`. |
| Text field | captured | Contact name field, empty and focused. Nothing typed. [components/crops/text-field-default.png](components/crops/text-field-default.png) |
| Text area | captured | Contact message, empty. |
| Select | captured | Country select, closed. Options were not opened. |
| Checkbox | observed | Consent checkbox is on the contact form and was not toggled. Its computed box was 1px, so the visible control is a custom paint. Values for the visible box are not captured. |
| Radio | captured | Demo role chips are `role="radio"`. Default and selected (Agronomist). The form was not submitted. |
| Switch | not present | No switch on the public pages. |
| Tabs | not present | No tab list on the public pages. Testimonial dots move a carousel, not tabs. |
| Menu | captured | Products, Solutions, Company and language panels. Phone menu captured in screenshots. |
| Tooltip | not present | None observed. |
| Dialog | captured | Download popover on the platform page, with Close. Not a modal with a scrim. |
| Toast | not present | None observed. No form was submitted. |
| Card | captured | Products menu card, home audience card, resources category card. |
| List row | captured | Language rows and phone menu rows, in screenshots. Computed style of a language row was not captured (the locator missed it). |
| Table | not present | No data table on the public pages. |
| Avatar | not present | No avatar on the public pages. |
| Badge | not present | No badge on the public pages. |

## Gaps

- Disabled, loading and error states were not shown. Forms were not submitted, so validation was not captured.
- The language menu item's computed style was not captured. The panel is in [screenshots/home-light-language-menu.png](screenshots/home-light-language-menu.png).
- Help center search uses Noto Sans, not Geologica. It is a separate site.
- Signed-in components (map, fields, charts, account) sit behind https://app.onesoil.ai/auth/login and were not captured.
"""
(HERE / "components.md").write_text(text)
print("wrote components.md")
