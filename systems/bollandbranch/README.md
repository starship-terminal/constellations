# Boll & Branch

Public capture of [https://www.bollandbranch.com](https://www.bollandbranch.com) on 2026-11-22. Signed out. The browser stayed on www.bollandbranch.com. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Sheet Sets grid, and one public product were photographed. Nothing was typed, submitted, or signed in.

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
| [screenshots/](screenshots/) | Homepage, Sheet Sets, product |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar black. It is `#77202e`, 46px, full width, with white type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint the interior header `#f9f8f3`. The header is `#fffdfb`. The page behind it is `#f9f8f3`. On the homepage the header is transparent and the wordmark is white. [screenshots/category-light-1440.png](screenshots/category-light-1440.png)
- Round Add to Bag. It is a 50px square button, radius 0, fill `#434a57`, label "ADD TO BAG". See it on your bed is the pill, radius 999px. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Stop at the account wall. Account points at account.bollandbranch.com and was not opened. The bag link points at `#cart` and was not opened.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Fakt for body, prices, and buttons. Louize for nav and the product title. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, header, Quick Add, size chips, See it on your bed, and Add to Bag |
| Button | Default only. Add to Bag and Quick Add not clicked |
| Link, wordmark, card, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was a closed icon and was not opened. Email signup was not filled |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menu links were read from the DOM. The open panel was not photographed. Sort showed Recommended selected. Size chips and color swatches were not clicked. Other controls were not on the public pages opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product and category | Captured |
| About | Listed at `/pages/world-of-boll-branch/`. Not opened |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Not submitted |
| Dark theme | Not present on the public shop |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, promo, header, band, sale, and bag tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
