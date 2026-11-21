# Credo Beauty

Credo Beauty is a public clean-beauty shop. This package is a signed-out capture of [https://credobeauty.com](https://credobeauty.com) on 2026-11-22. The browser stayed on credobeauty.com. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Makeup grid, and one public product were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Flower mark on white, 128 px |
| [icons/](icons/) | Wordmark SVG, flower SVG, and an index |
| [screenshots/](screenshots/) | Homepage, Makeup grid, product |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the utility bar white. It is `#001922`, 30px, with white 12px links. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint the department labels in the brand teal. They are `#001922`, 14px, weight 500, tracked 0.7px. The brand teal `#023e55` is the wordmark, the titles, and Add to Bag. Same shot.
- Round the search field into a pill. Search is 40px, radius 4px, 1px border `#00191e`. Add to Bag is the same 4px radius, fill `#023e55`, 38px. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Stop at the account wall. Account and Bag were not opened. The 10% popup was closed. Add to Bag was not clicked. Subscribe was not filled.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. urw-din for chrome and prices. Mercury Display for the hero and titles. Font files are not in this package |
| Spacing, radius, size | Captured for the promo strip, utility bar, search, department labels, and Add to Bag |
| Button | Default only. Add to Bag not clicked. SHOP NOW not followed |
| Link, wordmark, card, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was on screen and not typed into. Email signup was not filled |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menu links were read from the DOM. The open panel was not photographed. Filters and quantity were not changed. The 10% popup was closed |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured. [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Login, cart, checkout, subscribe | Stopped. Not opened |
| Phone width | Not captured. Desktop only |
| Dark theme | Not present. No theme control on the public shop |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the colour and size tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
