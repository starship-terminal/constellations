# J.Crew

J.Crew is a public clothing shop. This package is a signed-out capture of [https://www.jcrew.com](https://www.jcrew.com) on 2026-11-22. The browser landed on the Singapore storefront, [https://www.jcrew.com/sg/](https://www.jcrew.com/sg/). Prices read SGD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the women's clothing grid, one public product, and Our Story were photographed. Nothing was typed, submitted, or signed in.

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
| [screenshots/](screenshots/) | Homepage, clothing grid, product, Our Story |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Keep the announcement black and the header white. The bar is `#000000`, 55px. The department row is `#ffffff`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint Gifts in the same black as the other departments. That label is `#d0021b`. Same shot.
- Round the primary action. Add to Bag is a 40px rectangle with a 0px radius. Search is the pill, 70px radius. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Stop at the sign-in wall. Sign In was not opened. The bag link points at checkout and was not opened. The welcome mat's phone number was discarded with that first screenshot.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. soleil body, Adobe Caslon Pro display. Font files are not in this package |
| Spacing, radius, size | Captured for announcement, header, search, hero CTA, Add to Bag |
| Button | Default only. Add to Bag not clicked |
| Link, wordmark, card, price, badge | Default. [screenshots/collection-light-1440.png](screenshots/collection-light-1440.png) |
| Text field | Search was on screen and not typed into. Subscribe was not filled |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menu links were read from the DOM. The open panel was not photographed. Size select was not opened. Other controls were not on the public pages opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product and collection | Captured |
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

That checks the page, gifts, story, footer, announcement, and radius tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
