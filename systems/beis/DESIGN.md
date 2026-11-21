# Béis

A signed-out capture of the public Béis shop at [https://beistravel.com](https://beistravel.com), on 2026-11-22. Prices read USD. Desktop 1440 by 900. The page is white, the header is cream `#f2f1ec`, and the wordmark and primary fill are `#2c2c2e`. Body type is Helvetica. Display type is cofo-sans-variable. Primary actions are 40px pills with a 9px radius.

`catalog.json` was left alone, so this file is handwritten. Values come from [tokens.json](tokens.json) and [raw/readings.json](raw/readings.json).

## Colour

| Role | Value | Where |
|---|---|---|
| Page | `#ffffff` | body, product page, footer |
| Header | `#f2f1ec` | header bar |
| Announcement | `#f6f6f7` | 34px strip above the header |
| Ink | `#000000` | nav, titles, prices |
| Accent | `#2c2c2e` | wordmark fill, Add to Cart fill |
| On accent | `#ffffff` | Add to Cart text, hero title |
| Muted | `#6b6b6b` | compare-at price |
| Border | `#e2e2e2` | declared `--color-border-light` |

## Type

Helvetica for body, nav, prices, and buttons. cofo-sans-variable for the hero, section titles, product title, collection title, and the subscribe heading. Body 14px, weight 400, line-height 24px, letter-spacing 0.6px. Nav is the same size. Hero and collection title 30px, weight 450, letter-spacing -0.5px. Product title 20px. Buttons 11px, uppercase. Font files are not in this package.

## Controls

Buttons use a 9px radius and are 40px tall. Add to Cart is a `#2c2c2e` fill, 278px wide. Shop Travel Essentials is the inverse: white fill, `#2c2c2e` text, 250px wide. Personalize is an outline of the same height. Size chips are 180 by 40, 12px, and were not selected. Colour swatches are 24px circles. The header is 71px. The announcement bar is 34px. The wordmark is 55 by 32.

`:root` sets `--buttons-radius` to `0px`. The live Add to Cart and hero CTA measure `9px`. The token uses the measured radius.
