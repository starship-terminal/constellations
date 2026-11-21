# Vercel components

Measured on 2026-11-21 with headless Playwright, signed out. Desktop is
1440 by 900 at devicePixelRatio 1. Phone is 390 by 844 at devicePixelRatio 2.
Light is the default. Dark was set with the footer `dark` label.

## Button

Header "Sign Up" is an anchor.

| Theme | Background | Text | Height | Radius | Type |
|---|---|---|---|---|---|
| Light | `rgb(23, 23, 23)` | `rgb(255, 255, 255)` | 32px | 6px | GeistSans 14px weight 500, padding `0px 6px` |
| Dark | `rgb(237, 237, 237)` | `rgb(10, 10, 10)` | 32px | 6px | same size |

Header "Log In" swaps those fills: white on light, `rgb(10, 10, 10)` with
`rgb(237, 237, 237)` text in dark.

Login "Continue with Email" is a button, 40px, padding `0px 14px`, radius
8px, background `rgb(23, 23, 23)`, text `rgb(255, 255, 255)`. Crop:
[components/crops/button-primary-default.png](components/crops/button-primary-default.png).

"Continue with Google" is a white button, 40px, radius 8px, text
`rgb(23, 23, 23)`. Crop:
[components/crops/button-secondary-default.png](components/crops/button-secondary-default.png).
It was not clicked. GitHub, ChatGPT, SAML SSO, Passkey, and Apple were not clicked.

Hover, pressed, disabled, and loading were not forced.

## Link

Login "Sign Up" is a blue text link under the form. Its colour was not
isolated from the link custom property. `--geist-link-color` is
`hsla(212, 100%, 48%, 1)` in light and `hsla(210, 100%, 66%, 1)` in dark.

## Text field

Login email input, empty, placeholder "Email Address". 40px height, padding
`0px 12px`, radius 0 on the input, background `rgb(255, 255, 255)`, color
`rgb(0, 0, 0)`. Focus did not change those computed colours. The field was
not filled. The form was not submitted.

Crops: [text-field-default.png](components/crops/text-field-default.png),
[text-field-focus.png](components/crops/text-field-focus.png).

## Text area, select, checkbox, radio, switch

Not present on the pages that were opened.

## Menu and dialog

Products and Resources open one dialog, "Navigation menu". Phone "Open menu"
opens a full-screen dialog. Screenshots:
[products-menu-light-desktop.png](screenshots/products-menu-light-desktop.png),
[products-menu-dark-desktop.png](screenshots/products-menu-dark-desktop.png),
[menu-light-phone.png](screenshots/menu-light-phone.png),
[menu-dark-phone.png](screenshots/menu-dark-phone.png).

Tooltip, toast, and a search dialog were not opened.

## Card, table, list row, avatar, badge

Pricing plan columns are visible in
[pricing-light-desktop.png](screenshots/pricing-light-desktop.png). Their
boxes were not isolated. Table, list row, avatar, and badge were not captured
as components.

## Code

Docs `pre` on the light docs landing is Geist Mono 16px weight 400,
background `rgb(255, 255, 255)`, color `rgb(23, 23, 23)`, radius
`0px 0px 8px 8px`, padding `16px 0px`.
