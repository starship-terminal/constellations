# & Other Stories public chrome

Signed-out capture of [https://www.stories.com](https://www.stories.com) on 2026-11-22. The URL geo-redirected to [https://www.stories.com/en-ww/](https://www.stories.com/en-ww/), Guernsey / English, prices in USD. Desktop 1440 by 900, `devicePixelRatio` 2. Phone 390 by 844. Values are computed styles from the live page, recorded in [tokens.json](tokens.json) and [raw/readings.json](raw/readings.json).

This file is a hand copy. `make design-md` was not run, because that command needs a catalog.json entry and this pass does not edit catalog.json.

## Colour

| Role | Value | Where |
|---|---|---|
| Page | `#ffffff` | Photographed fill. Body background computed transparent |
| Text | `#000000` | Body, product title, footer links |
| Promo strip | `#f3f3f3` | Newsletter line above the header |
| Header | `#ffffff` | Desktop bar. Phone wordmark paints white over the hero |
| On photo | `#ffffff` | Hero "NEW IN" |
| Card well | `#f2f2f2` | Product image background |
| Last chance | `#cf0b00` | Shop drawer link |
| Footer heading | `#949494` | Column headings |
| Muted | `#757575` | Secondary heading, and the observed focus outline |
| Disabled | `#949494` / `#d9d9d9` | Choose size, not clicked |
| Wordmark | `#000000` | Sprite uses `currentColor`. Desktop header is black |

No dark theme was offered on the public shop. The about page uses a black editorial band. Its heading computed as black, so the type does not read in the screenshot.

## Type

| Role | Family | Size | Weight | Tracking |
|---|---|---|---|---|
| Body | Quadrant | 10px | 400 | 0 |
| Promo | Quadrant | 12px | 400 | 0 |
| Card name and price | Quadrant | 12px | 400 | 0 |
| Product title and price | Quadrant | 14px | 400 | 0 |
| Size chip | Quadrant | 10px | 400 | 0 |
| Shop now, Choose size | SansStories | 12px | 400 | 0.96px, uppercase |
| Hero | QuadrantMono | 34px | 400 | uppercase, line-height 37.4px |
| About heading | QuadrantMono | 24px | 400 | uppercase, line-height 26.4px |
| Footer heading | QuadrantMono | 16px | 400 | uppercase |

Loaded faces were SansStories 400, Quadrant 400, and QuadrantMono 400. SerifStories is named in `--font-serif` and was not loaded on the pages opened. Font files are not in this package.

## Geometry

The desktop stack is a 34px grey strip, then a 72px white header. The wordmark is 100 by 38. Shop now is 40px tall, padding 0 18px, radius 2px, white fill, 1px white border. Choose size is 382 by 40, padding 0 26px, radius 2px, grey until a size is picked. Size chips are 48 by 40. Phone promo strip is 52px. Phone header band is 64px. Shop now on the phone is 132 by 40.

## What was not measured

Hover, pressed, loading, and error. A selected size. Dark theme as a setting. Motion. A signed-in account. The bag. Search submit.
