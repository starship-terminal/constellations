# COS

COS is a public clothing shop. This package is a signed-out capture of [https://www.cos.com](https://www.cos.com) on 2026-11-22. The URL geo-redirected to the Singapore storefront, [https://www.cos.com/en-sg/](https://www.cos.com/en-sg/). Prices read SGD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the women's knitwear category, one public product, the About page, and the Women menu were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Wordmark on the ink colour, 128 px |
| [icons/](icons/) | Wordmark SVG copied from the live sprite, plus INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, category, product, About, Women menu |
| [raw/](raw/) | Computed styles the tokens were checked against |
| [tools/](tools/) | A check that the tokens match the readings |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Keep the page white and the bars black. The notice and the footer are `#080808`. The header is white. The wordmark is the same ink. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Leave the corners square. Add to Bag, the size chips, and the cookie buttons are 0px radius. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Stop at the bag, sign-in, and subscribe walls. Add to Bag was not clicked. Account, Sign in, and Subscribe point at login or newsletter pages. Those pages were not opened.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. SIM_Regular body, SuisseIntl display. Font files are not in this package |
| Spacing, radius, size | Captured for the notice, header, wordmark, Add to Bag, size chips, cookie buttons |
| Button | Default only. Add to Bag not clicked. Cookie buttons not clicked |
| Link, wordmark, card, price, size chip | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was an icon. It was not opened and not submitted |
| Hover, focus, pressed, disabled, loading, error | Not captured. Add to Bag was disabled until a size is chosen. That state was not isolated |
| Select, checkbox, radio, switch, tabs, tooltip, dialog, toast, table, avatar | Size is a chip grid, not a native select. The Women menu was photographed. Other controls were not on the public pages opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category and product | Captured |
| About | Captured. [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Women menu | Captured. [screenshots/women-menu-light-1440.png](screenshots/women-menu-light-1440.png) |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, bag, checkout, subscribe, login | Stopped. Not submitted |
| Dark theme | Not present on the public shop. The footer is a black band on a light page |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. The notice copy rotates. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, notice, wordmark, footer, and Add to Bag tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
