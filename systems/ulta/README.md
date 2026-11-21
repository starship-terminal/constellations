# Ulta Beauty

Ulta Beauty is a public beauty shop. This package is a signed-out capture of [https://www.ulta.com](https://www.ulta.com) on 2026-11-22. The browser stayed on www.ulta.com. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Makeup grid, one public product, and About Us were photographed. A rewards popover was closed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Site favicon, 128 px |
| [icons/](icons/) | Header wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage, Makeup grid, product, About Us |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the wordmark black. The header mark is `#f37830`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint the utility links black. Join / Sign in is `#736d69`, 12px, weight 300. Same shot.
- Turn search into a pill. Search is an underline, 1px `#b2aba5`. Same shot.
- Paint Add to bag orange. Add to bag is a black pill, white type, radius 100px. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Stop at the sign-in wall. Join / Sign in points at `/auth/login` and was not opened. The bag link points at `/bag` and was not opened. Email signup was not filled.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Circular for nav, title, price, and buttons. Font files are not in this package |
| Spacing, radius, size | Captured for the utility bar, search underline, wordmark, and Add to bag |
| Button | Default only. Add to bag not clicked. Shop now measured on the homepage |
| Link, wordmark, card, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was on screen and not typed into. Email signup was not filled |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Shop menu labels were read. The open panel was not photographed. Replenish & Save was not checked. Other controls were not measured |
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

That checks the ink, page, muted, line, brand, and bag tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
