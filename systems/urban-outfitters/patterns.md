# Patterns

How the measured pieces sit together on the signed-out site. Viewport shots from 2026-11-22 are in [screenshots/](screenshots/). The map of controls is [site-tree.md](site-tree.md).

## Shop chrome

The home header is sticky and 207px tall at 1440. From the top: a 45px promo strip, a utility row (Sign Up For SMS, Gift Cards, UO Rewards, Stores, Sign In / Sign Up) in 12px `#222222`, the wordmark, a search field on the right, then a 60px primary nav. The page background is `#ffffff`. The first promo slide is `#eb4034` with white 12px text. Later slides use `#222222`.

## Product grid

The women's clothing page heading is 18px Helvetica `#222222`, letter-spacing 0.5px. An "All Filters" control sits below it at 14px. Tiles are borderless. A regular price is `#222222`. A promotional line on the same tile is `#3a8700`. Seventy tiles were in the DOM.

## Product page

The title is 22px, weight 100, `#222222`. The sale price uses the same size in `#d83604`. The original price is 12px, `#222222`, and line-through. A green promo line (`#3a8700`) sits beside the price. Colour swatches are 36px circles. Size chips are 38px squares with a `#dddddd` border. The cart button is full width of the 520px buy column, black, square, and bold. Accordions stack under it. The button was not clicked.

## Sign-in dialog

Sign In opens as a 475px white dialog. It asks for a mobile number, with an Email tab beside it. A country select (radius 5px) sits left of a square phone field. Next is the black primary button. The form was closed without a phone number, email, or verification code.

## Phone

At 390px the utility row and primary nav collapse. Search, heart, bag, and Open navigation stay in the header. Open navigation is an in-page drawer with the same category links. The homepage then shows a two-column grid of black category tiles. See [screenshots/home-mobile.png](screenshots/home-mobile.png) and [screenshots/home-mobile-nav.png](screenshots/home-mobile-nav.png).

## What was not reached

Checkout, payment, and a signed-in account were not opened. The empty bag was. `/login` stopped at a captcha. No dark theme was offered on these pages.
