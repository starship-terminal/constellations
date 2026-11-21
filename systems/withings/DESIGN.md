# Withings

A signed-out capture of the public Withings shop at [https://www.withings.com](https://www.withings.com), on 2026-11-22. The browser geo-redirected to the United States storefront at [https://www.withings.com/en-us](https://www.withings.com/en-us). A geo modal said the visit was from Singapore. The modal was closed. Prices read USD. Desktop 1440 by 900. The header is `#ffffff`. The announcement bar is `#000000`. Add to cart is `#6784fe`. Body type is Aeonik. Shop now and Add to cart use a 16px radius.

`catalog.json` was left alone, so this file is handwritten. Values come from [tokens.json](tokens.json) and [raw/readings.json](raw/readings.json).

## Colour

| Role | Value | Where |
|---|---|---|
| Page | `#ffffff` | header, product page |
| Ink | `#0f0f0f` | body text, wordmark, product title, price |
| On ink | `#ffffff` | announcement text |
| Promo | `#000000` | Black Friday announcement bar |
| Nav | `#ffffff` | header bar |
| Bag | `#6784fe` | Add to cart |
| On bag | `#ffffff` | Add to cart text |
| Sand | `#f2eeea` | declared `--color-sand`, not sampled |
| Sale | `#d93421` | declared compare-at price. Hero sale line was photographed, not sampled |

## Type

Aeonik for body, nav, prices, buttons, and headings. Body 14px, weight 400. Nav 16px, weight 400. Shop now and Add to cart 16px, weight 500. Product price 20px, weight 500. A visible heading, "Withings Ecosystem", measured 52px, weight 400. The page `h1` is 72px and visually hidden. Font files are not in this package.

## Controls

Add to cart is a blue button, 430 by 56, 16px, weight 500, radius 16px, fill `#6784fe`, label "Add to cart". A sticky bar repeats the price and the same label at 256 by 48, radius 999px. Shop now on the homepage hero is white, 121 by 51, radius 16px, ink black, label "Shop now". The announcement bar is 36px, radius 6px, fill `#000000`. The header is 70px, fill `#ffffff`. The wordmark is an SVG, viewBox `0 0 143 20`, fill `#0F0F0F`.
