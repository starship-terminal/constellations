#!/usr/bin/env python3
"""Write components.md from the measured states. Deterministic."""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
text = """# Resend components

Public marketing and docs only. Signed out, 2026-11-21. Crops are in [components/crops/](components/crops/).

| Component | Status | Evidence |
|---|---|---|
| Button | Captured, partial | Header Get started: default, hover, focus-visible, pressed. [button-primary-default.png](components/crops/button-primary-default.png). Login submit is disabled until a field is filled, which was not done. |
| Icon button | Not present | No icon-only control was isolated on the public pages. The phone menu button is a labelled menu control. |
| Link | Captured, partial | Header Pricing link, default and hover. Hover did not change the computed colour. [link-nav-default.png](components/crops/link-nav-default.png) |
| Text field | Captured, partial | Login email field, default and focus. Nothing was typed. The placeholder was masked. [text-field-default.png](components/crops/text-field-default.png) |
| Text area | Not present | No public textarea. |
| Select | Captured, observed | Home "Select test mode" listbox is a public demo. Its open state was not cropped. |
| Checkbox | Not present | No public checkbox. |
| Radio | Not present | No public radio. |
| Switch | Not present | No public switch. Docs theme buttons are three buttons, not a switch. |
| Tabs | Captured | Pricing Transactional and Marketing tabs. [tab-selected.png](components/crops/tab-selected.png) |
| Menu | Captured | Features, Company, AI and Docs hover menus. [home-dark-features-menu.png](screenshots/home-dark-features-menu.png). Phone menu: [mobile-home-dark-menu.png](screenshots/mobile-home-dark-menu.png) |
| Tooltip | Not captured | Glossary buttons on the home page were not opened. |
| Dialog | Captured, partial | Docs search dialog. [docs-light-search.png](screenshots/docs-light-search.png). The crop measured the search bar, not the full popup. |
| Toast | Not present | No public toast. Nothing was submitted. |
| Card | Captured, observed | Pricing plan cards and docs quickstart cards are in the page screenshots. No separate crop. |
| List row | Not present | No app list. Docs sidebar links are navigation, not list rows. |
| Table | Not present | No public data table. |
| Avatar | Not present | No public avatar. |
| Badge | Not captured | Status pills on the marketing page were not isolated. |

## Gaps

- Signed-in dashboard, settings, and sending flows are behind login. Not captured.
- Button default fill computes to transparent. The painted fill is a white gradient the background-color does not report. See README.
- Focus-visible and pressed were forced with CDP pseudo states, not a real key press, so a navigation click could not fire.
- Disabled, loading, and error states of buttons were not reached. The login submit is disabled because the field was left empty.
- Checkbox, radio, switch, textarea, table, avatar, and toast do not appear on the public surface.
"""
(HERE / "components.md").write_text(text)
print("wrote components.md")
