# Banana Republic public chrome

Signed-out capture of [https://bananarepublic.gap.com](https://bananarepublic.gap.com) on 2026-11-22. Desktop 1440 by 900, `devicePixelRatio` 2. Values are computed styles from the live page, recorded in [tokens.json](tokens.json) and [raw/readings.json](raw/readings.json).

This file is a hand copy. `make design-md` was not run, because that command needs a catalog.json entry and this pass does not edit catalog.json.

## Colour

| Role | Value | Where |
|---|---|---|
| Page | `#ffffff` | Photographed fill. Body background computed transparent |
| Text | `#000000` | Body, departments, product title |
| Universal bar | `#e9e8e3` | Gap, Old Navy, Banana Republic, Athleta |
| Promo bar | `#000000` | Sale ticker, white type |
| Wordmark | `#ad280a` | SVG fill |
| Search rule | `#5e5c5a` | 1px bottom border |
| Chip line | `#e5e4e4` | Filter & Sort outline |
| Swatch line | `#999999` | 1px around the 30px colour square |
| Badge | `#f2f1ee` at 80% | Best Seller |
| Footer | `#f2f1ee` | Sitewide footer |
| Add to Bag | `#000000` / `#ffffff` | Not clicked |

## Type

| Role | Family | Size | Weight | Tracking |
|---|---|---|---|---|
| Body | Lynstone, Helvetica, Arial, sans-serif | 16px | 400 | 0 |
| Universal brand | Lynstone v1 | 12px | 350, current 600 | 0.2px |
| Promo | Lynstone v1 | 12px | 600 | 1px |
| Department | Banana v1 | 14px | 400 | 2px |
| Sale label | BananaSerif | 14px | 400 | 1.68px |
| Hero | BananaSerif | 48px | 300 | 0.375px |
| Category title | Linotype Didot BR | 72px | 300 | 0 |
| Product title | Banana v1 | 18px | 400 | 1px |
| Price and card | Lynstone v1 | 12 to 14px | 350 | 0.2px |

Font files are not in this package.

## Geometry

The header stack is 184px: 46px cream, 48px black, 90px white. Search is 270 by 32 with a square corner and a hairline rule. Hero chips and Add to Bag are 56px tall, radius 0. Size chips are 53 by 39, radius 0. Colour swatches are 30px inside a 36px cell, radius 0.

## What was not measured

Hover, focus, pressed, disabled, loading, and error. Phone width. Dark theme. Motion. A signed-in account. The bag.
