# Components

Measured on www.pampam.city, signed out, 2026-11-19. Desktop viewport 1440×900, device pixel ratio 2. Colours are the computed values. Crops are from those pages.

## Button

Three faces.

| Face | Where | Fill | Text | Radius | Height | Padding |
|---|---|---|---|---|---|---|
| Primary | Make map, in the hero prompt | `#000000` | `#ffffff`, Inter 550 16px | 8px | 40px | 12px |
| Accent | Get Explorer, Get Business | `#4b72f3`, 1px `#2b3ea7` | `#ffffff`, Inter 550 19px | 12px | 64px | 20px 32px |
| Secondary | Try it for free, Contact us, See tutorial & docs | `#fefefe`, 1px `rgba(0,0,0,0.1)` | `#8a8a8a`, Inter 550 19px | 12px | 64px | 20px 32px |

Primary hover is declared as `rgba(0,0,0,0.8)` and was not forced. Accent shadow is `rgba(0,0,0,0.3) 0px 1px 2px` plus an inset lip `rgb(99,135,244) 0px 2px 0px`. Secondary shadow is `rgba(0,0,0,0.1) 0px 1px 3px`.

![Make map](components/crops/button-primary.png)

![Get Explorer](components/crops/button-accent.png)

![Try it for free](components/crops/button-secondary.png)

On the phone hero the label is hidden and the primary face is the icon only. [screenshots/home-light-phone.png](screenshots/home-light-phone.png)

## Google button

The header and `/login` sign-in control is a Google Identity Services iframe, title "Sign in with Google Button". Header size 204×44, theme outline. Login size 214×44, theme filled_blue. PamPam does not style the label. The button was not clicked.

![Header Google button](components/crops/google-button.png)

## Text field

The hero prompt is a 406×66 shell: white, 12px radius, 1px `rgba(0,0,0,0.1)`, stacked shadow at 5% black. The input is borderless, Inter 550 16px / 24px, colour `#222222`, padding 8px 0. Placeholder colour `#8f8f8f`. Nothing was typed.

![Prompt](components/crops/text-field.png)

## Nav link

Header links are Inter 550 16px / 24px, colour `#9894a8`, padding 8px 12px, radius 0. Hover opacity is 0.5, measured on Pricing. The header itself is fixed, 100px tall, background transparent.

![Pricing](components/crops/nav-link.png)

## Menu

Solutions and Products open a panel: white, 126×218, radius 6px, padding 8px 0, border 1px `rgba(0,0,0,0.05)`, shadow `rgba(14,18,22,0.2) 0px 6px 20px -10px`. Items are Inter 400 16px / 24px, colour `#666666`, padding 8px 12px. Hover is declared as colour `#aaaaaa` and background `rgba(0,0,0,0.06)`.

![Solutions menu](components/crops/menu.png)

## Switch

The yearly billing control is a 56×36 track, radius 24px, padding 8px. Off fill is declared `rgba(0,0,0,0.08)`. On, with Pay yearly selected, the inline background is `#006e0b` and the row reverses. Thumb is 20×20, radius 18px, white, shadow `rgba(38,38,38,0.15) 0px 0px 4px`. Track inset shadow is `rgba(0,0,0,0.18) 0px 0px 2px`. The control was read in the on state. It was not toggled, because that changes the prices.

![Yearly on](components/crops/switch-on.png)

## Badge

Save 37% is an h4, Inter 550 14px, colour `#00a917`, background `#e5ffe8`. Save 30% and Save 35% use the same colours.

![Save 37%](components/crops/badge.png)

## Card

Use-case cards are 216×186, fill `#faf2ec`, radius 16px, padding 24px, gap 12px, border 1px `rgba(0,0,0,0.02)`. Title is 16px weight 600. Body is `#9894a8`. Hover lifts 4px and darkens the border to `rgba(0,0,0,0.05)`, over 150ms ease. Focus-visible ring is declared as `0 0 0 2px #fff, 0 0 0 4px #ff9a50`.

Plan cards are `#fbfcfd`, radius 16px, padding 24px, gap 20px. The Business card adds a 2px `#dde1f1` border. Price is Inter 700 32px / 24px.

![Plan card](components/crops/plan-card.png)

## Link

Footer and Learn more links are Inter 550 16px / 24px, colour `#9894a8`, no underline. Login legal links are 12px, colour `#808080`, underlined.

## Accordion

FAQ rows have a 1px `rgba(0,0,0,0.1)` top border and 24px padding. The question is nineties 28px, computed 28px / 30.24px, colour `#1b1917`. The mark is 24px, `+` closed and `-` open. The open answer on the home page computed to 16px black through the system font, which does not match the muted colour in the screenshot. Treat the screenshot as the visual and the computed colour as the reading.

[screenshots/home-light-faq.png](screenshots/home-light-faq.png)

## Logo

The wordmark is an inline SVG, 67×40. [icons/logo.svg](icons/logo.svg)

![Logo](components/crops/logo.png)

## Gaps

| Component | Status |
|---|---|
| Icon button | The phone Make map face is the primary button with its label hidden. No separate icon-button style was measured. |
| Text area, select, checkbox, radio | Not on the public pages. |
| Tabs | Not present. Billing is a switch. |
| Tooltip, dialog, toast | Not opened. The menus are the only overlays. |
| Table | Not present. |
| Avatar | Not present. |
| Disabled, loading, error, pressed | Not on the public pages. |
| Focus-visible, painted | Declared on the use-case cards as `#ff9a50`. Not photographed. |
| Google button internals | Cross-origin iframe. Size and theme only. |
