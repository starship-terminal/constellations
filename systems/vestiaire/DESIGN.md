# Vestiaire Collective

Hand copy of the measured public shop tokens. Not written by `make design-md`. This pass does not edit catalog.json.

## Colors

| Role | Value | Source |
|---|---|---|
| page | `#ffffff` | sampled homepage |
| text | `#1e1e1e` | body, computed `rgb(30, 30, 30)` |
| text, quiet | `#656565` | breadcrumb and product brand |
| price | `#333333` | catalog price |
| search | `#f5f5f5` | search pill |
| hairline | `#ececec` | sampled under the header |
| sale | `#db2124` | Sale nav and a sale price |
| promo | `#d31e1e` | homepage offer bar |
| on promo | `#ffffff` | offer bar type |
| sell | `#000000` | Sell an item and Add to Bag |
| on sell | `#ffffff` | those labels |
| footer | `#000000` | footer block |
| footer link | `#ababab` | footer links |

## Typography

Albra-Regular carries titles. HelveticaNowText carries the shop. Neither file is in this package.

| Style | Size | Weight | Line | Tracking |
|---|---|---|---|---|
| body | 16px | 400 | normal | 0 |
| nav | 15px | 400 | 18px | 0 |
| search | 14px | 400 | normal | 0 |
| button | 14px | 500 | 20px | 0 |
| promo | 32px | 400 | normal | 0 |
| hero | 64px | 400 | normal | 0 |
| section | 40px | 400 | 52px | 0 |
| category | 40px | 400 | 40px | 0 |
| about | 54px | 400 | 54px | 0 |
| brand | 14px | 700 | 21px | 0 |
| price | 14px | 700 | 21px | 0 |
| footer label | 12px | 500 | 15px | 1.8px |
| footer link | 14px | 400 | normal | 0 |
| menu link | 15px | 400 | 26px | 0 |

## Geometry

The header is 132px. Search is 420 by 45, radius 33px. Sell an item is 111 by 36, radius 2px. Catalog chips are 44px tall with a 1px black border and no radius. Add to Bag is 48px tall, radius 2px. Shop markdowns is 180 by 48, radius 24px, a white outline on the hero.

## Components

Search sits at the left of the header. The wordmark sits in the center. Sell an item, Sign in, Sign up, and the bag sit at the right. The nav is a second row. The homepage opens with a red offer bar, then a full-width photograph, then named image rails. A catalog page puts a serif title over a row of square filter chips and a five-column product grid. About sets a serif title over centered 16px paragraphs.
