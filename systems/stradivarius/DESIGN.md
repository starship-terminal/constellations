# Stradivarius

A signed-out capture of the public Stradivarius shop at [https://www.stradivarius.com/us/](https://www.stradivarius.com/us/) on 2026-11-22. The start URL is a location picker, not a geo-redirect. This file records the United States English storefront. Desktop 1440 by 900, `devicePixelRatio` 2. The page is white. Body type is STRADIVARIUS WEB 2025 at 10px. The product title is 28px, weight 600, `#1d1d1d`. Special prices are `#d0024c`.

`catalog.json` was left alone, so this file is handwritten. Values come from [tokens.json](tokens.json) and [raw/readings.json](raw/readings.json).

## Colour

| Role | Value | Where |
|---|---|---|
| Page | `#ffffff` | Storefront sections, company profile |
| Text | `#000000` | Body, prices, Filters label on black |
| Product ink | `#1d1d1d` | Product title, computed rgb(29, 29, 29) |
| Grey dark | `#151515` | Named `--colors-grey-dark` |
| Muted | `#707070` | Named `--colors-grey-dim` |
| Divider | `#e7e7e7` | Named `--colors-grey-light` |
| Wash | `#f5f5f5` | Named `--colors-grey-clear`. Search pill at 30% |
| Sale | `#d0024c` | Named `--colors-red-dark`. Special prices |
| Search text | `#333333` | Search pill computed rgb(51, 51, 51) |

## Type

STRADIVARIUS WEB 2025 on the body, the menu, the category title, and the product title. Body is 10px, weight 400. Menu labels are 16px, weight 600, uppercase. The category title is 32px, weight 400, line-height 44px. The product title is 28px, weight 600, uppercase, line-height 38px. A tile price is 12px, weight 600. The product price is 22px, weight 600. Font files are not in this package. The site falls back to sans-serif.

## Controls

Search is a 4px-radius pill. Filters is a black button, radius 2px, white 16px type. Size chips are transparent, 14px, padding 1px 6px. The primary button fill is black and the text is white. The secondary button fill is white and the text is black. Add to bag was not shown and was not clicked.

## Do and don't

- Keep the shop black on white. Do not invent a dark theme. `color-scheme` was `normal`.
- Set menu labels in STRADIVARIUS WEB 2025, 16px, weight 600, uppercase.
- Use `#d0024c` only for sale and special prices.
- Do not ship the font files. They were not captured.
