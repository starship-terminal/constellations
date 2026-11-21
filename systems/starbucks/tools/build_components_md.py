#!/usr/bin/env python3
"""Write components.md from the captured public states. No invented values."""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
text = """# Starbucks components

Public site only, signed out, 2026-11-21. Crops were not cut; the states below are the full screenshots. Values are token names from [tokens.json](../tokens.json).

| Component | States captured | Where |
|---|---|---|
| Header nav link | default | [home-light-default.png](../screenshots/home-light-default.png) |
| Sign in pill | default | same |
| Join now pill | default, hover | [home-light-join-hover.png](../screenshots/home-light-join-hover.png) |
| Banner order button | default | home |
| Outline link | default | See the holiday menu on home |
| Product card | default | [menu-light-default.png](../screenshots/menu-light-default.png) |
| Size radio | default, selected | [product-light-size-selected.png](../screenshots/product-light-size-selected.png) |
| Select | default | product What's included |
| Primary order button | default, hover | [product-light-add-hover.png](../screenshots/product-light-add-hover.png) |
| Customize button | default, expanded | [product-light-customize.png](../screenshots/product-light-customize.png) |
| Text field | empty, focus | [signin-light-email-focus.png](../screenshots/signin-light-email-focus.png) |
| Password field | empty | [signin-light-wall.png](../screenshots/signin-light-wall.png) |
| Checkbox | checked (page default) | sign-in Keep me signed in |
| Dialog | open, empty fields | [gift-light-balance-dialog.png](../screenshots/gift-light-balance-dialog.png) |
| Accordion | open | [gift-light-faq-open.png](../screenshots/gift-light-faq-open.png) |
| Mobile menu | open | [mobile-home-light-menu.png](../screenshots/mobile-home-light-menu.png) |
| Empty state | favorites, previous | [menu-favorites-light-empty.png](../screenshots/menu-favorites-light-empty.png) |
| Error page | 404 | not screenshotted: the page prints a request id |

## Gaps

Text area, switch, tooltip, toast, table, avatar, and badge are not present as named controls on the captured public pages. A star chip on the product page is observed, not tokenised. Disabled, loading, and validation-error states were not reached: no form was submitted. Dark theme is not present. Focus-visible ring was not isolated; see tokens `light.focus.ring`.
"""
(HERE / "components.md").write_text(text)
print("components.md")
