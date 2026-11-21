# Components

Measured on the public marketing site on 2026-11-19, signed out. Values are token names. Readings are in [raw/notes.md](raw/notes.md).

`preview_snapshot` returned "The browser is not producing screenshot frames." Crops were not cut from invented frames. Component values come from computed styles.

## Button

The resting button is `light.component.button.bg` with `light.component.button.text` and a `core.border.button` (3px) `light.component.button.border`. Radius is `core.radius.none`. Height is `core.size.button-height` (46px). Padding is `core.spacing.button-top` (12px), `core.spacing.button-x` (20px), `core.spacing.button-bottom` (10px). Type is `core.typography.button`, uppercase.

SEE OUR ROOMS and BOOK ROOM, while `:hover` matched, computed to `light.component.button-hover.bg` and `light.component.button-hover.text`. The stylesheet transitions background and color over `core.motion.duration.button` with `core.motion.easing.ease`.

The top BOOK ROOM control on the Dutch home had a transparent fill and no border until hover. MENU uses `light.background.nav` and no border. Both are 43px tall (`core.size.nav-button`).

Pressed, disabled and loading were not kept as crops. `focus()` on SEE OUR ROOMS computed `outline: none` and `box-shadow: none`. Default and hover crops are [components/crops/button-default.png](crops/button-default.png) and [components/crops/button-hover.png](crops/button-hover.png).

## Link

Bottom nav links at 1440 are `core.typography.nav`, uppercase, in `light.text.primary`. At 390 the MENU label is `display: none`. The hamburger stays, 43px tall, white fill.

Footer rules links are `core.typography.footer-link` in `light.text.inverse`.

`.flowing-text a:not(.button):visited` declares `light.text.link`. An unvisited prose link was not sampled.

## Text field

Not on the pages measured as a product control. The newsletter page embeds a Sendinblue form in an iframe. The iframe was not entered. No email was typed.

The hidden booking date picker has `select` and day `button` elements. They were not opened. A hidden day computed color `light.text.disabled`.

## Text area

Not present.

## Select

BOOK ROOM opens a date dialog on the same URL. The month control is a visible `select`. No option was changed and Submit was not pressed. [screenshots/home-light-book-wall.png](../screenshots/home-light-book-wall.png)

The open menu paints EN and NL as a pair of links, not a native select.

## Checkbox, radio, switch

Cookiebot checkboxes were in the consent dialog. Necessary cookies only was chosen. Those checkboxes were not measured as product controls. No product checkbox, radio or switch was on the later pages.

## Tabs

On `/en/hotel/`, STANDARD ROOMS and SPECIAL ROOMS are `a.button.tab`. The active tab computed black fill, white text, and a 3px black border. The inactive tab has a transparent fill, black text, and the same border. Radius is 0. Crops: [components/crops/tab-selected.png](crops/tab-selected.png), [components/crops/tab-default.png](crops/tab-default.png).

Blog categories (PEOPLE, HOTSPOTS, MUSIC, ART & CULT, EXPERIMENTS, HOTEL) are text links, `core.typography.button` size, not a tab widget.

## Menu

A click on the MENU label opens `#main-nav-overlay`. It computed `display: block` and background `light.background.nav` (rgba(255, 255, 255, 0.97)). The painted links are Home, Hotel, Meetings & Events, Badplaats, Canvas, Werkplaats, Doka, Broedplaats, Blog, and Agenda. [screenshots/home-light-menu.png](../screenshots/home-light-menu.png). At 390 the same overlay opens from the hamburger. [screenshots/home-light-phone-menu.png](../screenshots/home-light-phone-menu.png). A hovered row was not recaptured.

## Tooltip

Not present.

## Dialog

Cookiebot was on the first paint and was removed from the DOM. It was not clicked. The booking date dialog was opened and not submitted. The menu overlay is a full-page menu, not a small dialog.

## Toast

Not present.

## Card

Hotel room cards are 458px wide (`core.size.card`), white, 1px `light.border.card`, radius 0. Blog cards are the same border and fill, with `.content` padding `0px 20px 20px` (`core.spacing.card`). The blog title is `core.typography.card-title`. The excerpt is `core.typography.muted` in `light.text.muted`.

## List row

Not present as a separate component. Footer columns are paragraphs, not rows.

## Table

Not present on the pages measured.

## Avatar, badge

Not present. Blog category labels are uppercase 13px spans, not badges with their own fill.

## Icon button

The hamburger is a 43px square (`core.size.hamburger`) with white fill. At 390 it measured 46 by 43. It has no text. Crop: [components/crops/icon-button-default.png](crops/icon-button-default.png). The SVG was not extracted.
