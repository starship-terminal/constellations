# Summer Fridays

Public capture of [https://summerfridays.com](https://summerfridays.com) on 2026-11-22. Signed out. The browser stayed on summerfridays.com. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, Shop All, and Lip Butter Balm Vanilla were photographed. Nothing was typed, submitted, or signed in.

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
| [screenshots/](screenshots/) | Homepage, Shop All, product |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar black. It is `#481f18`, 64px, full width, with white type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint the homepage header white. On the homepage the header is transparent and the wordmark is white. On Shop All the header is white and the wordmark is `#000418`. [screenshots/category-light-1440.png](screenshots/category-light-1440.png)
- Paint card Add to Bag the same blue as the product button. The card button is `#eeedec` with ink text. The product Add to Bag is `#5c7899` with white text, 394 by 40, radius 3px. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Stop at the account wall. Account points at `/account` and was not opened. The bag is a minicart button and was not opened.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Futura PT for body, nav, titles, and buttons. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, header, Shop Now, card Add to Bag, Buy Once, and product Add to Bag |
| Button | Default only. Add to Bag, Notify Me, and Subscribe not clicked |
| Link, wordmark, card, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was a closed icon and was not opened. Email and phone signup were not filled |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menu links were read from the DOM. The open panel was not photographed. Shade chips and the size chip were not clicked. Sort By was not changed |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product and category | Captured |
| About | Listed at `/pages/about`. Not opened |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Not submitted |
| Dark theme | Not present on the public shop |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, promo, header, card button, bag, and radius tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
