# Dermstore

A signed-out capture of the public Dermstore shop at [https://www.dermstore.com](https://www.dermstore.com), on 2026-11-22. The browser stayed on www.dermstore.com. A cookie banner was accepted. Prices read USD. Desktop 1440 by 900. The promo bar is `#cccccc`. The department bar is `#222222`. Add to Cart is `#000000`. Body type is Manrope. Display type is Libre Bodoni. Search and Add to Cart are square.

`catalog.json` was left alone, so this file is handwritten. Values come from [tokens.json](tokens.json) and [raw/readings.json](raw/readings.json).

## Colour

| Role | Value | Where |
|---|---|---|
| Page | `#ffffff` | header, product page |
| Ink | `#121212` | body text |
| Ink soft | `#000000` | promo text |
| On ink | `#ffffff` | department labels, Add to Cart text |
| Promo | `#cccccc` | holiday promo bar |
| Nav | `#222222` | department bar, wordmark fill |
| Trust | `#f2f2f2` | shipping strip |
| Search border | `#8c8c8c` | search wrap |
| Bag | `#000000` | Add to Cart, Quick Buy, Ask Derm AI |
| Muted | `#6b7280` | brand link |
| Title | `#111827` | product heading |
| Hero | `#8c040c` | sampled from the holiday photograph, not a CSS fill |

## Type

Manrope for body, nav, search, and buttons. Libre Bodoni for product titles, prices, the category heading, and the About heading. Body 16px, weight 400. Department labels 16px, weight 400, uppercase. Product title 37px, weight 400, letter-spacing -1px. Price 30px, weight 400. Font files are not in this package.

## Controls

Add to Cart is a black rectangle, 300 by 60, 14px, weight 600, radius 0, label "ADD TO CART". Search is 480 by 44, radius 0, white fill, 1px `#8c8c8c` border, placeholder "SEARCH". The promo bar is 44px, full width. The department bar is 44px, full width. The wordmark is an inline SVG, viewBox `0 0 259 64`.
