#!/usr/bin/env python3
"""Write components.md from the measured public controls. No guessed states."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
text = """# Scape components

Public marketing site only, captured 2026-11-21 from scape.com, signed out. One light theme. Values are token names. Crops were not cut: the states below are the whole-page screenshots that show them.

## Button

FIND A ROOM is a 40px pill, 14px uppercase Visuelt, cream fill, black text, 100px radius. Token roles: `light.action.primary.background`, `light.action.primary.text`, `core.radius.pill`, `core.size.button`.

| State | Where |
|---|---|
| default | [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| hover | Not captured. Dispatching mouseenter did not change the computed fill. `--button-primary-background-hover` is transparent. |
| focus-visible | Not captured as a held keyboard state. The declared ring is `light.focus.ring` (`1px dashed` black, 2px offset). |
| pressed | Not captured. `--button-primary-background-active` is transparent. |
| disabled | Not present on the public pages. |
| loading | The booking page body stayed on "Loading...". Not a button state. |

A second variant is declared as `--button-secondary-*`: black fill, cream text, same pill. It was not isolated on a labelled control in the measured set.

## Icon button

Favourites and booking are 40px circles, cream border, translucent black fill, on the transparent header. See the header in [screenshots/home-light-default.png](screenshots/home-light-default.png).

## Link

Nav links are 16px Visuelt. On the hero they are cream (`light.text.onDark`). Footer logo colour computed to pink (`light.text.link` / `core.color.pink`). `--link-color` aliases `--primary` (black) and did not match that painted link.

## Text field

Contact enquiry dialog was opened and not filled. The location select on the contact page is a 40px pill, 1px black border, 14px Visuelt. See [screenshots/contact-light-enquiry-dialog.png](screenshots/contact-light-enquiry-dialog.png) and [screenshots/contact-light-default.png](screenshots/contact-light-default.png).

Declared field tokens: `--form-input-border-radius` 4px, padding 12px 20px, focus border `--scape-black`. A 4px field was not the control measured on the contact select.

## Text area

Not captured. The enquiry dialog's fields were not read as a textarea. The dialog was closed without typing.

## Select

Location select on contact, and the room-search filter chips. Filter chips are 26px, 4px radius, 1px 20% black border. See [screenshots/rooms-light-filter-location.png](screenshots/rooms-light-filter-location.png).

## Checkbox, radio, switch

Not present on the captured public pages.

## Tabs

Stay-type buttons on Find a room (Full academic year, Semester stay, Flexible stay, Summer stay) and FAQ category chips. See [screenshots/rooms-light-default.png](screenshots/rooms-light-default.png) and [screenshots/faq-light-bookings-filter.png](screenshots/faq-light-bookings-filter.png).

## Menu

Our locations opens a mega menu. See [screenshots/home-light-locations-menu.png](screenshots/home-light-locations-menu.png). Phone nav opens a drawer. See [screenshots/home-light-mobile-menu.png](screenshots/home-light-mobile-menu.png).

## Tooltip

Not present.

## Dialog

OPEN FORM on contact opens an enquiry dialog. It was not submitted. See [screenshots/contact-light-enquiry-dialog.png](screenshots/contact-light-enquiry-dialog.png).

## Toast

Not present.

## Card

Room cards on Find a room, and city cards on the home page. Surface token `light.background.surface` (`--scape-card-bg`). Shadow `core.shadow.card`. See [screenshots/rooms-light-default.png](screenshots/rooms-light-default.png).

## List row

Footer link columns and FAQ accordions. An open FAQ question is in [screenshots/home-light-faq-open.png](screenshots/home-light-faq-open.png).

## Table

Not present.

## Avatar

Not present.

## Badge

Promo strip "RATES FOR 27/28 NOW LIVE" uses dark red text (`core.color.darkRed`). See the top of [screenshots/home-light-default.png](screenshots/home-light-default.png).

## Gaps

- Hover, pressed, disabled, loading and error were not read as computed state changes.
- Checkbox, radio, switch, tooltip, toast, table and avatar are not on the public marketing surface.
- Signed-in account, checkout and booking submit were not entered. [https://www.scape.com/my-account/](https://www.scape.com/my-account/) is a login wall.
- Dark theme is not present.
- Component crops were not cut. Screenshots are the evidence.
"""
(ROOT / "components.md").write_text(text)
print("components.md", len(text))
