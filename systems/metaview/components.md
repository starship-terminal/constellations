# Components

Measured on www.metaview.ai and the signed-out app.metaview.ai sign-in and sign-up pages on 2026-11-19. Colours are the product's own custom properties. Crops are 256-colour cuts of the captures in [screenshots/](screenshots/).

## Button

The marketing primary is a pill. On the home hero it computed to 51px tall, 24px horizontal padding, radius 9999px, background `rgb(0, 8, 5)` (`--mv-color-light-color8`), label `rgb(255, 255, 255)` at Euclid Circular A 16px / 500. The header uses the same variant at a smaller size (38px, 13.3px type).

![Primary pill](components/crops/button-primary-default.png)

The outline pill on the same hero is white, 1px black border, radius 999px, black 16px / 500 label, 51px tall.

![Outline pill](components/crops/button-outline-default.png)

Hover, focus-visible, pressed and disabled were not forced. The resting styles are what the pages shipped.

## Link

Nav links (Pricing, Careers) compute to Euclid Circular A 16px / 400, colour `rgb(1, 5, 27)` (`--mv-color-text`). Text links in the sign-in footer are 11px Inter.

## Text field

Sign-in email input, dark theme: 34px tall, 8px radius, 8px horizontal padding, background `rgb(13, 14, 14)` (`--mv-uiBase`), border 1px `rgba(234, 248, 254, 0.15)` (`--mv-uiA4`), text `rgb(254, 254, 254)`, Inter 13px / 400. Light theme swaps those to white, `rgba(0, 0, 0, 0.08)` and `#202020`.

![Sign-in, dark](components/crops/form-signin-dark.png)

![Sign-in, light](components/crops/form-signin-light.png)

The sign-up field is the same family, with the submit sitting beside it.

![Sign-up](components/crops/form-signup-default.png)

Filled, error and focus-visible were not captured. Typing a fake address and submitting would start an account, so that flow stopped at the empty field.

## Tabs

Pricing uses a row of plan-family labels. The selected one (Sourcing) is a black pill; the others are text. The crop of that row missed the pills, so the state is the viewport shot.

![Pricing](screenshots/pricing-light-default.png)

## Menu

Platform opens a three-column panel under the nav: agent links, a "How it works" column, and a featured card. The panel computed to white, 1px `rgba(1, 5, 27, 0.06)` border, 32px padding, 1276px wide at a 1440 viewport.

![Platform menu](components/crops/menu-open.png)

## Card

Plan cards on Pricing sit on the mint page: a pale fill, a price line, and a full-width black pill. The shared banner above them is white with a 16px radius.

![Plan cards](components/crops/card-plan-default.png)

## Banner

The announcement bar is 42px, background `rgb(0, 8, 5)`, white 16px / 400 Euclid Circular A, full width.

![Announcement](components/crops/banner-default.png)

## Navigation

The marketing header is white, with the wordmark, three menus, two text links and two pills. On the home page the bar is not stuck to the top of the document; the announcement sits above it.

![Nav](components/crops/nav-default.png)

## Not in this capture

| Component | Why |
|---|---|
| Text area, select, checkbox, radio, switch | Not on the public pages or the signed-out auth screens |
| Toast, dialog, tooltip | No public page opened one. The Platform menu is the overlay that did open |
| Avatar, badge, table, list row | The signed-in product has these. Auth stopped at the email field |
| Button hover, focus-visible, pressed, disabled | Not forced. Resting styles are measured |
| Field error | Submitting the email form would start an account |
