# Arc'teryx

Arc'teryx is a public outdoor shop. This package is a signed-out capture of [https://arcteryx.com](https://arcteryx.com) on 2026-11-22. The shop redirected to [https://arcteryx.com/ca/en](https://arcteryx.com/ca/en), the Canada English storefront. The utility bar shows a Canadian flag and EN. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, Women's Shell Jackets, one public product, and Who we are were photographed. Nothing was typed, submitted, or signed in.

The shared preview browser landed on the same Canada URL, then failed to produce screenshot frames twice. The shots here are from a later headless Chromium pass of the same public URLs.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Wordmark on white, 128 px |
| [icons/](icons/) | Header wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage, shell jackets, product, Who we are |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the utility bar white. It is `#000000`, 40px, full width, with white type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Round Add to cart. It is a 488 by 54 rectangle, radius 0, fill `#1a1a1a`, label 16px weight 700. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Set display type in Helvetica. Headings are Elan ITC Pro, uppercase, 32px on the hero and the category, 26px on the product title. Body and nav are Helvetica Now Display.
- Open a second regional slug. The walk stayed on `/ca/en` after the geo redirect. Region was not changed.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Helvetica Now Display for body, nav, price, and buttons. Elan ITC Pro for headings. Font files are not in this package |
| Spacing, radius, size | Captured for the utility bar, search, hero CTA, and Add to cart |
| Button | Default only. Add to cart not clicked. Shop women's measured, not followed |
| Link, wordmark, card, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was on screen and not typed into. Weekly signup was not filled |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menu links were read from the DOM. The open panel was not photographed. Colour swatches and the size row were not clicked. The cookie dialog was closed without a shot |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product and category | Captured |
| About | Captured. [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Not submitted |
| Dark theme | Not present on the public shop |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, promo, search, and bag tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
