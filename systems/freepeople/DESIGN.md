# Free People

Signed-out shop capture, 2026-11-22. Values are the ones measured on [https://www.freepeople.com](https://www.freepeople.com). This file is a hand copy. `make design-md` was not run, because that command needs a catalog.json entry and this pass does not edit catalog.json.

## Colour

| Token | Value | Where |
|---|---|---|
| page | `#FEFBFA` | Body background, `--creme-light` |
| promo | `#EDE6E0` | Global banner, `--creme-dark` |
| creme | `#FAF2ED` | `--creme` |
| ink | `#252423` | Nav, product title, price, `--stone-dark` |
| ink-strong | `#1A1A1A` | Promo heading |
| wordmark | `#2D2D2D` | Header SVG fill |
| pink | `#D52975` | Add to Bag, GIFTS, SALE, `--pink-dark` |
| pink-soft | `#FFAFAF` | `--pink` |
| on-pink | `#FFFFFF` | Add to Bag label |
| stone | `#998F8A` | `--stone` |
| stone-medium | `#7C706E` | `--stone-medium` |
| stone-light | `#D6D0CB` | `--stone-light` |
| green | `#057555` | `--green`, declared |
| red | `#D01302` | `--red`, declared as error |
| white | `#FFFFFF` | Menu panel, `--white` |

## Type

Karla, then Helvetica, for UI. Karla, then Georgia, for headings. The font file is not in this package.

| Role | Size | Weight | Tracking |
|---|---|---|---|
| Nav | 12px | 400 | 0.3px, uppercase |
| Promo | 12px | 700 | 0.3px |
| Product title, category title | 18px | 400 | 0.3px |
| Price | 16px | 400 | normal |
| Add to Bag | 12px | 400 | 1.2px, uppercase |
| Homepage tile heading | 32px | 400 | white on the photo |

## Space and shape

Promo bar 44px. Nav row 60px. Logo inset 24px. Product and about content inset 60px. Add to Bag is 45px tall and 465px wide on the 1440 viewport, radius 0. Search is 150 by 26, radius 0. Header shadow is none. `--popover-shadow` is `5px 5px 10px rgba(0, 0, 0, 0.2)`.
