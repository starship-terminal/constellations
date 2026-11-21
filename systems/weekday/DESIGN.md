# Weekday

Hand copy of the measured public shop tokens. Not written by `make design-md`. This pass does not edit catalog.json.

## Colors

| Role | Value | Source |
|---|---|---|
| page | `#ffffff` | body and header |
| text | `#000000` | body, homepage h1, product title |
| ink | `#1d1d1b` | nav, login, search, footer links, buttons |
| promo | `#ffff03` | promo bar, computed `rgb(255, 255, 3)`. Screenshot samples `#ffff55` |
| on-promo | `#1d1d1b` | promo type |
| sale | `#d1443b` | UP TO 50% OFF in the women mega-menu |
| button | `#1d1d1b` | ADD TO CART and shipping confirm. Not used to start checkout |
| on-button | `#ffffff` | primary label |
| border | `#1d1d1b` | JOIN NOW outline |
| footer line | `#b4b4b4` | footer hairline |

## Typography

Three computed faces. The files are not in this package. Weight on the measured styles is 400. Size and family carry the hierarchy.

| Style | Size | Face | Line | Tracking |
|---|---|---|---|---|
| body | 18px | weekdayRegularFont | 27px | 0 |
| nav | 16px | weekdayRegularFont | 22px | 0 |
| promo | 16px | weekdayMonoFont | 22px | 0 |
| home | 34px | weekdaySemiBoldFont | 38px | -0.85px |
| hero | 26px | weekdaySemiBoldFont | 30px | -0.52px |
| sale | 22px | weekdayRegularFont | 26px | 0 |
| category | 18px | weekdayRegularFont | 22px | 0 |
| product | 16px | weekdayRegularFont | 22px | 0 |
| about | 74px | weekdaySemiBoldFont | 100px | 1.48px |
| footer heading | 18px | weekdayRegularFont | 22px | -0.45px |
| footer link | 16px | weekdayRegularFont | 22px | 0 |
| button | 16px | weekdayRegularFont | 22px | 0 |

The About title is black type on a black hero band, so it does not show in the photograph.

## Geometry

The promo bar is 58px. The header is 56px, white, with no bottom border. Search is 394 by 56, padding 16px 56px 16px 48px. Primary buttons and JOIN NOW are 40px tall, radius 0. ADD TO CART is 432px wide. JOIN NOW is 137px wide.

## Components

See [components.md](components.md) and [patterns.md](patterns.md).
