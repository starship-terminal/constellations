# Nordstrom

A signed-out capture of the public Nordstrom shop at [https://www.nordstrom.com](https://www.nordstrom.com), on 2026-11-22. The browser stayed on www.nordstrom.com. The shipping bar says the visit is outside the U.S. and the country control reads Singapore. Prices read SGD. Desktop 1440 by 900. The promo bar is `#191a1b`. Black Friday & Sale is `#b80009`. The sale price is `#d82508`. Body type is Brandon Text. Search is a rectangle with a 0px radius. Add to Bag is 48px tall with a 4px radius.

`catalog.json` was left alone, so this file is handwritten. Values come from [tokens.json](tokens.json) and [raw/readings.json](raw/readings.json).

## Colour

| Role | Value | Where |
|---|---|---|
| Page | `#ffffff` | header, product page |
| Ink | `#191a1b` | body text, promo fill, Add to Bag fill, product title |
| On ink | `#ffffff` | promo text, Add to Bag text |
| Sale | `#b80009` | Black Friday & Sale nav label |
| Price | `#d82508` | sale price on the product page |
| Search | `#f0f3f5` | search field |

## Type

Brandon Text for body, nav, prices, buttons, and the product title. Arial is the fallback. Body 16px, weight 400. Nav 16px, weight 400. Product title 24px, weight 700. Collection title 28px, weight 700. Sale price 16px, weight 700. Font files are not in this package.

## Controls

Add to Bag is an ink rectangle, 570 by 48, 16px, weight 700, radius 4px. Search is 728 by 42, radius 0, fill `#f0f3f5`, placeholder "Search for products or brands". The promo bar is 41px, full width. The wordmark is 198 by 25. Singapore on the promo bar is 18px white.
