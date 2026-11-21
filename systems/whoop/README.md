# WHOOP

WHOOP is a public membership shop for a wearable and health insights. This package is a signed-out capture of [https://www.whoop.com](https://www.whoop.com) on 2026-11-22. The browser landed on [https://www.whoop.com/sg/en/](https://www.whoop.com/sg/en/). Prices on the Peak page read SGD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage and the Peak membership page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Wordmark on black, 128 px, cropped from the homepage shot |
| [icons/](icons/) | Header wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage and Peak membership page |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar black. It is a 50px steel gradient from `#3b526c` to `#5c7fa8`, with white type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint Gift WHOOP as the white JOIN NOW pill. Gift WHOOP uses the same steel gradient, 40px, radius 16px. JOIN NOW is white, 61px, black type, radius 16px. Same shot.
- Flatten the hero headline to the nav size. The headline is 96px Proxima Nova, weight 400, letter-spacing -3.6px. Nav labels are 16px, weight 600, uppercase.
- Open join.whoop.com, app.whoop.com/login, shop.whoop.com, or orderstatus.whoop.com from this package. Those walls were not entered. The Cloudflare block page was discarded.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Proxima Nova, with Readex Pro then Arial. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, Gift WHOOP, JOIN NOW, and the hero headline |
| Button | Default only. JOIN NOW and Gift WHOOP were not clicked |
| Link, wordmark, card, price | Default. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Not on the public pages opened |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Membership menu links were read from the DOM. The open panel was not photographed. Cookie buttons were not clicked |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured. Peak membership page |
| About | Listed at /sg/en/about/. Not photographed. A blocked headless load of that URL was discarded |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Join, gift, login, shop, and order status were not opened |
| Dark theme | The public marketing page is black chrome on a photographic hero. No theme toggle was on screen |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, steel, compare, card, and join radius tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
