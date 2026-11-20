# Soundtrap components

Public surface only, captured 2026-11-21, signed out. Values are token names from [tokens.json](tokens.json). Crops were not cut: the states below are the full screenshots that show them. A state that was not reached says Not captured.

## Button

Hero pill on [home-light-default.png](screenshots/home-light-default.png). Fill `light.component.heroCta.background` (#eeeeee), text `light.component.heroCta.text`, radius `core.radius.pill`, height 80px at 1440. Hover lightens to #fcfcfc and shifts up 2px (computed 2026-11-21). Pressed and disabled: Not captured.

Header Get started is the same pill at a smaller size (padding 11px 16px, 16px type). Pricing Try it free is a white pill on the plan fill, text #5e49ff (computed). Login submit uses `light.accent` (#6551ff), white text, radius 8px, height 41px: [login-light-default.png](screenshots/login-light-default.png).

## Icon button

Play preview is a 32px circle, fill #28282e, on the originals row in [home-light-play-preview.png](screenshots/home-light-play-preview.png). Label flips from Play to Pause. Phone nav toggle is the circular menu control in [mobile-home-light-nav.png](screenshots/mobile-home-light-nav.png).

## Link

Header links are 15px Matter 700, colour #e6e6e6 on the dark marketing header, 0.3s colour transition. Inline product links use `light.link` (#553fff) on light sections. Login "Forgot your password?" is the same purple.

## Text field

Login and signup email and password: height 40px, radius 8px, fill `light.color.background.tinted-base` (rgba(0,0,0,0.07)), text `light.text`. Placeholder only. Focus, error, and disabled: Not captured. No value was typed.

## Text area

Developers page shows read-only sample textareas. Not measured as a form control. Not captured as an editable state.

## Select

Signup birth month, day, and year are selects. Not opened. Education and pricing language selects were not changed. Not captured beyond the closed default on [signup-light-default.png](screenshots/signup-light-default.png).

## Checkbox, radio, switch

Not present on the public pages captured. OneTrust checkboxes were hidden and not used.

## Tabs

Pricing Individual / Education are links, not tabs. Monthly / Yearly is a local toggle: [pricing-light-default.png](screenshots/pricing-light-default.png) (Yearly pressed) and [pricing-light-monthly.png](screenshots/pricing-light-monthly.png).

## Menu

Phone navigation menu: [mobile-home-light-nav.png](screenshots/mobile-home-light-nav.png). Footer language menu: [home-light-language-menu.png](screenshots/home-light-language-menu.png). Get started dialog is a two-link menu: [home-light-get-started-dialog.png](screenshots/home-light-get-started-dialog.png).

## Tooltip

Education pricing "More info" opens a tooltip. [pricing-education-light-tooltip.png](screenshots/pricing-education-light-tooltip.png). Copy read live: "Keep track of what collaborators have changed or restore previous project versions."

## Dialog

Get started for free opens a Radix dialog with Personal Use (`/signup`, wall) and Educational Use (`/edu/`). No other public dialog was opened. Login and signup are pages, not dialogs.

## Toast

Not present.

## Card

Pricing plan cards: purple, blue, red, and maroon fills on [pricing-light-default.png](screenshots/pricing-light-default.png). Originals pack cards sit in the home carousel.

## List row

Support category rows and footer link columns. Pricing comparison rows sit under the plan cards.

## Table

Pricing comparison is a row grid, not a data table with headers. No sortable table on the public surface.

## Avatar

Not present on the public pages. Marketing photos are not avatars.

## Badge

Not present as a component. Plan names are headings on the coloured cards.

## Gaps

- Signed-in studio controls (transport, mixer, piano roll, collaboration) are behind `/login`. The hero image is a marketing render, not the app.
- Dark theme tokens exist as `.st-dark-theme` and were not applied. Not captured as a live theme.
- Focus-visible, pressed, disabled, loading, and error were not held on public controls, except the CTA hover reading.
- Signup includes a Cloudflare "Verify you are human" widget. It was not solved.
- Checkbox, radio, switch, toast, and avatar were not on the public pages reached.
- Careers cookie banner was not dismissed, so that host has no screenshot.
