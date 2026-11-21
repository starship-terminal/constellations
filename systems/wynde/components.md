# Components

Public marketing components on https://wynde.io/, measured 21 November 2026. Values are token names. The crop is the real control.

## Button

Primary hero button. Fill `light.component.button-primary.bg` (`#000000`), label `light.component.button-primary.text` (`#ffffff`), Inter 20 px weight 600, padding 12 px 20 px, height 48 px, radius 52 px. No border, no shadow.

![Get started for free](components/crops/button-primary.png)

Nav primary is the same fill and label at 15 px weight 500, padding 2 px 8 px, height 31 px, radius 38 px.

![Nav Get started](components/crops/button-nav-primary.png)

Secondary hero button. Fill `light.component.button-secondary.bg` (`#dadfe5`), label `#2b2b2b`, same 48 px height and 52 px radius.

![Book a demo](components/crops/button-secondary.png)

Nav Log in. Fill `#edf1f5`, label `#181818`, height 31 px, radius 38 px.

![Log in](components/crops/button-nav-login.png)

Hover, pressed, disabled, and loading were not on screen. The CSSOM had no `:hover` rule on these button classes.

## Link

Nav links (Features, Pricing) are Inter 15 px weight 500, `#000000`, line-height 27 px, no underline. They transition colour over 300 ms with `cubic-bezier(0.44, 0, 0.56, 1)`. Footer links are Inter 15 px weight 400, `#4c5259`.

## Switch

Annual discount, at rest. Track 28 by 16 px, `#000000`, radius 40 px. Knob 8 px, `#ffffff`, radius 100%. Label Inter 15 px weight 500. Not a native `role=switch`. The on state was not toggled.

## Card

Pricing cards are white, radius 20 px, padding 24 px 20 px, 411 px wide at the 1440 read. The hairline is an `::after` border, `1px solid rgb(237, 240, 244)`, not `border` on the element and not a shadow. Plan names: Start `#4c5259`, Team `#f7511c`, Enterprise `#00528d`. Prices are Suisse Int'l Medium 28 px. Contact sales is a white pill, 200 by 48 px, radius 52 px, with an `::after` border `1px solid rgb(218, 223, 229)`. Its label is Inter 20 px weight 500. It has no href.

Feature tiles sit on `#cbf0ff` (computed `rgb(203, 240, 255)`), radius 20 px. Quote tiles sit on `#edf0f4`, radius 20 px.

## Text field

Not present on the marketing pages. The login screen at https://app.wynde.io/login has an empty email field. It was not typed in and not submitted. Its values are in [raw/login-boundary.json](raw/login-boundary.json), not in the marketing tokens. The 21 November read at 1440 by 900 matches the earlier one: placeholder "Enter your email here", white field, 280 by 32 px, radius 10 px, border `1px solid rgb(230, 233, 237)`, Inter 14 px.

## Gaps

- Button hover, focus-visible, pressed, disabled, loading: not shown. Browser focus on Log in was the default orange outline, not tokenised.
- Text field, text area, select, checkbox, radio: not on the public pages.
- Switch on-state: not toggled.
- Phone menu open state: captured. White panel, 390 by 271, fixed. [screenshots/home-light-phone-menu.png](screenshots/home-light-phone-menu.png)
- Dialog, toast, tooltip, tabs, table, avatar, badge: not present.
- Signed-in app: not entered. Login offers email plus Google. Google was not pressed. No phone, card, or company SSO was entered.
- Dark theme: not on the marketing site.
- Framer 404: not a Wynde component. Left out of the tokens.
