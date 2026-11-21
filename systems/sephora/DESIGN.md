# Sephora

A signed-out capture of the public Sephora shop at [https://www.sephora.com](https://www.sephora.com), on 2026-11-22. The browser stayed on www.sephora.com. A geo modal said the visit was outside the USA and Canada shipping region. The modal was closed. Prices read USD. Desktop 1440 by 900. The promo bar is `#510282`. The department bar is `#000000`. Add to Basket is `#cf112c`. Body type is Helvetica Neue. Search and Add to Basket are pills.

`catalog.json` was left alone, so this file is handwritten. Values come from [tokens.json](tokens.json) and [raw/readings.json](raw/readings.json).

## Colour

| Role | Value | Where |
|---|---|---|
| Page | `#ffffff` | header, product page |
| Ink | `#000000` | body text, wordmark, product title |
| On ink | `#ffffff` | promo text, department labels, Add to Basket text |
| Promo | `#510282` | App Exclusive bar |
| Nav | `#000000` | department bar |
| Search | `#f6f6f8` | search field |
| Bag | `#cf112c` | Add to Basket |
| Link | `#136bea` | declared `--color-link`, not sampled from a painted link |

## Type

Helvetica Neue for body, nav, prices, buttons, and the product title. Helvetica and Arial are the fallbacks. Body 14px, weight 400. Department labels 14px, weight 400. Product title 16px, weight 400. Brand 14px, weight 700. Price 16px, weight 700. Hero titles 20px, weight 700. Font files are not in this package.

## Controls

Add to Basket is a red pill, 282 by 48, 14px, weight 700, radius 99999px, label "Add to Basket", sublabel "Get It Shipped". Search is 318 by 34, radius 9999px, fill `#f6f6f8`, 1px black border, placeholder "Search". The promo bar is 60px, full width. The department bar is 44px, full width. The wordmark is an inline SVG, viewBox `0 0 125 17`.
