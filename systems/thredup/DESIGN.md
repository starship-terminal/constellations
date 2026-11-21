# ThredUp

Signed-out capture of https://www.thredup.com on 2026-11-22. This file is a hand copy of the measured tokens. `make design-md` was not run, because that command needs a catalog.json entry and this pass does not edit catalog.json.

## Colors

| Role | Value | Source |
|---|---|---|
| ink | `#000000` | body color, Add to Cart fill |
| page | `#ffffff` | body background |
| header | `#e9e9e9` | header background |
| promo | `#daefc6` | promo bar |
| sand | `#f3f2ee` | Shop/Sell pill, footer |
| field-border | `#b6b5b2` | search and email border |
| burgundy | `#83211d` | Holiday Shop, sale price, badge |
| cream | `#fffedc` | hero type |
| muted | `#3d3d3c` | struck price |
| on-ink | `#ffffff` | Add to Cart label |

The hero panel background computed as `rgb(131, 33, 30)`, one step from burgundy.

## Typography

Season Sans is the UI face. Season Serif is the display face. Neither file is in this package.

| Style | Face | Size | Weight |
|---|---|---|---|
| body | Season Sans | 14px | 400 |
| nav | Season Sans | 14px | 400 |
| toggle | Season Sans | 12px | 500, 1px tracking |
| button | Season Sans | 12px | 500, 2px tracking |
| hero | Season Serif | 36px | 400 |
| brand | Season Serif | 28px | 400 |
| price | Season Sans | 20px | 500 |

## Geometry

Header 176px. Promo bar 48px. Nav 52px. Controls 44px tall. Search 334px wide. Add to Cart 556px wide. Control radius 1px. Shop/Sell pill radius 999px.

## Do and don't

Use the green promo bar, the sand pill, and the burgundy sale price together. Do not treat a live price or the promo code as stable chrome. Do not invent a dark theme. The photographed shop is light.
