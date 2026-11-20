# Components

Signed-out controls measured on www.squarespace.com, /pricing, /templates, and login.squarespace.com on 2026-11-19. Crops are 2x.

## Button

Get Started is 60px tall, padding 23px 28px, radius 4px, Clarkson 14px weight 500, uppercase.

On the photo hero the fill is `#ffffff` and the label is `#000000`. A real hover in the preview tab moved the fill to `#dddddd`. On pricing and templates the same control is `#000000` with a `#ffffff` label.

![Get Started at rest](components/crops/nav-get-started-default.png)

![Get Started hover](components/crops/nav-get-started-hover.png)

The login LOG IN submit is a different control: 44px tall, 327px wide, radius 0, fill `#f2f2f2`, label `#b7b7b7`. It was disabled because the fields were empty.

![Disabled login submit](components/crops/login-submit-disabled.png)

Continue with Google, Apple, and Facebook are 55px tall, 327px wide, radius 0, 1px solid `#000000`, padding 0 22px, Clarkson 14px weight 500.

![Continue with Google](components/crops/login-google-default.png)

Try Blueprint AI Builder on /templates is 36px tall, padding 0 11px, radius 0, 1px solid `#e7e7e7`, label 12px weight 500, letter-spacing 0.5px, uppercase.

## Link

LOG IN in the marketing header is Clarkson 14px weight 500, uppercase, `#ffffff` on the photo hero. Create Account and Can't log in on the login page are 12px weight 500, letter-spacing 0.5px, uppercase, `#0e0e0e`.

![Log in](components/crops/nav-log-in-default.png)

## Text field

Login email and password are underlined, not boxed. The row is 327px wide and 50px tall with 11px vertical padding. The resting separator is 1px `#e7e7e7`. The focused separator child is 2px `#0e0e0e`. The label is 9.75px weight 500, letter-spacing 0.75px, uppercase, `#666666`. The input is 14px weight 400, `#0e0e0e`.

![Email field](components/crops/login-email-default.png)

The home domain search is a different field: 62px tall, radius 8px, background `rgba(255, 255, 255, 0.2)` on a dark section. The templates search wrapper is 60px tall, radius 6px, with a stacked shadow (`rgba(0, 0, 0, 0.1) 0px 4px 9px`, then 17px and 39px layers). Its placeholder computed `#666666` at 15px weight 500.

## Text area, select, switch, radio

Not present on the pages that loaded.

## Checkbox

/templates filter rows show a 14px checkbox. Accent color computed `auto`. Checked, disabled, and error states were not shown.

## Tabs

The pricing billing toggle is a 61px track, radius 1000px, padding 4px, background `rgba(0, 0, 0, 0.05)`. The selected pill is `#ffffff`, radius 1000px, 53px tall. Pay annually is `#000000`. Pay monthly is `#5a5a5a`. Both labels are Clarkson 15px weight 400, letter-spacing -0.015px.

## Menu

PRODUCTS, SOLUTIONS, and RESOURCES are header buttons, 80px tall at 1440. The open menu was off-screen in the first read (translated out of view) and was not captured as an open state.

## Card

Pricing plan cards are 443px wide, radius 24px, padding 32px 32px 40px, background `#ffffff`. The resting shadow starts `rgba(0, 0, 0, 0.03) 0px -1px 30px`. The emphasized card's shadow starts `rgba(0, 0, 0, 0.1) 0px -1px 30px`. Plan names are 20px weight 500, letter-spacing -0.2px.

Template cards are 349 by 218, radius 8px, background `#f9f9f9`, border `0.5px solid #e7e7e7`.

## Badge

The promo badge is `#0072f0`, radius 120px, padding 4px 12px, Clarkson 15px, `#ffffff`. Recommended on the Core plan is `#0072f0`, radius 30px, padding 8px 16px, 16px weight 400, `#ffffff`.

## Dialog, toast, tooltip, table, avatar

Not present on the signed-out pages that loaded. The promo offer is an inline pill, not a dialog.

## Gaps

- Button pressed, focus-visible, and disabled on the marketing Get Started were not shown.
- Login error text color `#c32d38` was read from an empty error node. The message itself was not shown.
- Checkbox checked state, select, radio, switch, text area, toast, tooltip, dialog, table, and avatar were not on these pages.
- The open nav menu was not captured.
