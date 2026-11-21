# Tower 28

Tower 28 is a public clean-beauty shop. This package is a signed-out capture of [https://tower28beauty.com](https://tower28beauty.com) on 2026-11-22. The browser stayed on www.tower28beauty.com. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Makeup grid, and one public product were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, Shop menu, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Site favicon, 128 px |
| [icons/](icons/) | Wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage, Makeup grid, product |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the announcement bar white. It is `#d74015`, 29px, with white 12px type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint nav labels in the wordmark coral. They are `#872626`, 15px. The wordmark fill is `#ee542f`. Same shot.
- Square the Shop Now pill. It is 38px, radius 40px, fill `#d74015`. Add on the product is 44px with the same radius. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Stop at the login wall. Log in and Cart were not opened. Add was not clicked. Subscribe was not filled.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Scto Grotesk A Medium for chrome and prices. Cooper Lt BT for headings. Font files are not in this package |
| Spacing, radius, size | Captured for the announcement bar, header, Shop Now, Save pill, and Add |
| Button | Default only. Shop Now not followed. Add not clicked |
| Link, wordmark, card, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was on screen and not typed into. Email signup was not filled |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Shop links were read from the DOM. The open panel was not photographed. Sort and shade were not changed. Subscribe was not checked |
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
