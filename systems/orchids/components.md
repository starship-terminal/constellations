# Components

Measured on docs.orchids.app, 2026-11-19. Crops are from the 2x screenshots. Values are from computed styles, not from the crops.

## Button

Copy page is the only button with a border. It is 34 px tall, padding 6 px 12 px, radius 12 px on the left. Light face `#ffffff`, text `#46433f`, border `#e6e3df`. Dark face `#0e0c0c`, text `#d5d3cf`, border a 7% white oklab colour.

![Copy page, light](components/crops/button-copy-light.png)

![Copy page, dark](components/crops/button-copy-dark.png)

Hover, pressed, disabled, and loading were not captured.

## Icon button

The theme switch is three 20 px circles at radius 9999 px. The selected one (system, on this visit) is `#1e1b17` with icon `#e6e3df`. The others are transparent with icon `#777571`.

![Theme switch](components/crops/theme-switch-light.png)

## Link

Start a Project is 14 px medium Inter, colour `#fcaa26`, on a transparent anchor. Support beside it is `#575551`. The current sidebar link is the same amber, 14 px regular, 32 px row, padding 6 px 12 px 6 px 16 px.

![Start a Project](components/crops/link-accent-light.png)

![Selected nav](components/crops/nav-selected-light.png)

## Text field

Search is a 36 px button, radius 8 px, with a 1 px ring. It opens a dialog. The dialog input is transparent, 16 px, colour `#110f0b` in light, placeholder "Search...". Nothing was typed.

![Search, light](components/crops/search-light.png)

![Search, dark](components/crops/search-dark.png)

## Text area

The assistant field placeholder is "Ask a question...". Computed height 60 px, font 14 px, padding 10 px 40 px 10 px 14 px. The send button is 24 px, disabled, background `oklab(0.799063 0.0490309 0.15406 / 0.3)`.

## Card

Feature cards are 16 px radius, padding 20 px 24 px. Light fill `#ffffff` with a 10% oklab border. Dark fill `#0e0c0c`.

![Feature card](components/crops/card-features-light.png)

Plan cards on the pricing page use `rgba(255, 255, 255, 0.05)` and `rgba(255, 255, 255, 0.1)`, radius 8 px, padding 24 px. In light theme the fill is faint. Name 18 px / 600, price 20 px / 600, both `#46433f`.

![Plan card](components/crops/plan-card-light.png)

## Table

The annual plans table has 14 px headers at weight 600, colour `oklch(0.21 0.034 264.665)`, and 14 px cells at `#46433f`.

## Dialog

The search dialog is 640 px wide, radius 20 px, white in the light read, over an overlay of `oklab(0 0 0 / 0.4)`. Empty height was 62 px.

## Not on these pages

Select, checkbox, radio, switch, tabs as a widget, menu, tooltip, toast, avatar, and badge were not on the captured docs pages.

## Gaps

- No filled primary button.
- No hover, pressed, disabled, loading, or error state on a control.
- Focus outline computed as `none` even though the colour was the accent.
- Login and signup were the paused Vercel page. No field was filled.
- The assistant was not submitted.
