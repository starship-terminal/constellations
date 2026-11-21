# Brooks Running

Brooks Running is a public running-shoe shop. This package is a signed-out capture of [https://www.brooksrunning.com](https://www.brooksrunning.com) on 2026-11-22. The first response redirected to [https://www.brooksrunning.com/en_us](https://www.brooksrunning.com/en_us). The country control was already United States. Prices read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage and the Women's shoes grid were photographed. Nothing was typed or submitted.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Promo bar, header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Wordmark on white, 128 px |
| [icons/](icons/) | Header wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage and Women's shoes |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the wordmark black. On the navy bar it is `#ffffff`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint the main bar black. It is `#003789`, 72px. Same shot.
- Paint the promo strip white. It is `#b8dde1`, 52px, with ink `#0e131f`. Same shot.
- Round the search field. Search is a 220 by 40 rectangle, radius 0, 1px white border, transparent fill. Same shot.
- Paint prices grey. The sale price on the grid is `#0e131f`, 16px, weight 400. [screenshots/category-light-1440.png](screenshots/category-light-1440.png)
- Stop at the sign-in wall. Log in points at `/en_us/account-login/`. The cart and Become a Member were not completed.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. GT America for body, nav, title, and prices. GT America Condensed for product names. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, navy bar, search, hero title, and the category title |
| Button | Default only. Hero links and size chips were on screen and not clicked |
| Link, wordmark, card, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Text field | Search was on screen and not typed into. Email signup was not filled |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menu links were read from the DOM. The open panel was not photographed. Sort and size chips were on the grid and not clicked |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured. Women's shoes, 49 products |
| Product | Listed on the grid. The product URL was not opened |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Not submitted |
| Dark theme | Not present on the public shop |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, page, banner, navy, and price tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
