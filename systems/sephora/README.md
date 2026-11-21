# Sephora

Sephora is a public beauty shop. This package is a signed-out capture of [https://www.sephora.com](https://www.sephora.com) on 2026-11-22. The browser stayed on www.sephora.com. A geo modal said the visit was outside the USA and Canada shipping region. The modal was closed and the walk continued on that storefront. Prices read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Makeup grid, and one public product were photographed. About Us was opened and not photographed. Nothing was typed, submitted, or signed in.

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
| [screenshots/](screenshots/) | Homepage, Makeup grid, product |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar black. It is `#510282`, 60px, full width, with white type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint the department bar white. It is `#000000`, 44px, with white labels. Sale & Offers is the same white. Same shot.
- Square the search field. Search is a 34px pill, radius 9999px, fill `#f6f6f8`, 1px black border. Add to Basket is the same pill, fill `#cf112c`. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Stop at the sign-in wall. Sign In was not completed. The basket link points at `/basket` and was not opened. The geo modal was closed, not followed to international sites.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Helvetica Neue for body, nav, title, and buttons. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, search, department bar, and Add to Basket |
| Button | Default only. Add to Basket not clicked |
| Link, wordmark, card, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was on screen and not typed into. Email and text signup were not filled |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menu links were read from the DOM. The open panel was not photographed. Color swatches and the quantity control were not clicked. Other controls were not on the public pages opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product and category | Captured |
| About | Opened at `/beauty/about-us`. Not photographed. Preview frames stopped, and a headless retry returned Access Denied |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Not submitted |
| Dark theme | Not present on the public shop |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, promo, nav, search, and bag tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
