# Components

Measured on the public marketing site on 2026-11-19, signed out. Values are token names. Readings are in [raw/notes.md](raw/notes.md).

`preview_snapshot` returned "The browser is not producing screenshot frames." Crops were not cut from invented frames. Component values come from computed styles.

## Button

The resting button is `light.component.button.bg` with `light.component.button.text` and a `core.border.button` (3px) `light.component.button.border`. Radius is `core.radius.none`. Height is `core.size.button-height` (46px). Padding is `core.spacing.button-top` (12px), `core.spacing.button-x` (20px), `core.spacing.button-bottom` (10px). Type is `core.typography.button`, uppercase.

SEE OUR ROOMS and BOOK ROOM, while `:hover` matched, computed to `light.component.button-hover.bg` and `light.component.button-hover.text`. The stylesheet transitions background and color over `core.motion.duration.button` with `core.motion.easing.ease`.

The top BOOK ROOM control on the Dutch home had a transparent fill and no border until hover. MENU uses `light.background.nav` and no border. Both are 43px tall (`core.size.nav-button`).

Pressed, disabled and loading were not painted. `focus()` on SEE OUR ROOMS computed `outline: none` and `box-shadow: none`.

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

The booking date picker has a room `select` and a month `select`. Both were `display` collapsed (height 0) on the pages measured. They were not opened, and no dates were chosen.

The menu stylesheet declares a language selector inside `#main-nav-overlay`. The overlay stayed `display: none`, so that control was not computed.

## Checkbox, radio, switch

Cookiebot checkboxes were in the consent dialog. Necessary cookies only was chosen. Those checkboxes were not measured as product controls. No product checkbox, radio or switch was on the later pages.

## Tabs

On `/en/hotel/`, STANDARD ROOMS and SPECIAL ROOMS are `a.button.tab`. The active tab is `light.component.tab-selected.bg` with `light.component.tab-selected.text`, a 3px black border, and padding `13px 40px 9px` (`core.spacing.tab-x`). The inactive tab has a transparent fill and black text. Radius is 0.

Blog categories (PEOPLE, HOTSPOTS, MUSIC, ART & CULT, EXPERIMENTS, HOTEL) are text links, `core.typography.button` size, not a tab widget.

## Menu

`#main-nav-overlay` computed `display: none` and background `light.background.nav`. A synthetic click on `.menu-button` did not open it. The stylesheet says overlay links are 40px with padding `8px 0px 12px`, and a hovered row is `rgba(0, 0, 0, 0.1)`. Those states were not computed on a painted menu.

## Tooltip

Not present.

## Dialog

Cookiebot was on the first paint. Necessary cookies only was clicked. The dialog was not measured as a product dialog. The booking date picker and the menu overlay were not opened.

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

The hamburger is a 43px square (`core.size.hamburger`) with white fill and padding `18px 10px`. At 390 it measured 46 by 43. It has no text. The close control on the promo sign measured 48 by 48. Neither was extracted as an SVG crop.
