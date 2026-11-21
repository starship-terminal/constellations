# Dermstore

Dermstore is a public beauty shop. This package is a signed-out capture of [https://www.dermstore.com](https://www.dermstore.com) on 2026-11-22. The browser stayed on www.dermstore.com. A cookie banner was accepted. Prices read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Skin Care grid, one public product, and About Us were photographed. Nothing was typed, submitted, or signed in.

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
| [screenshots/](screenshots/) | Homepage, Skin Care grid, product, About |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar black. It is `#cccccc`, 44px, full width, with black type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint the department bar white. It is `#222222`, 44px, with white uppercase labels. Same shot.
- Round the search field or Add to Cart. Search is a square field, radius 0, 1px `#8c8c8c` border. Add to Cart is a black rectangle, radius 0. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Set body type in Libre Bodoni. Body, nav, and buttons are Manrope. Libre Bodoni is the display face for titles and prices.
- Stop at the sign-in wall. Sign In was not opened. The cart link points at `/basket/` and was not opened. The cookie banner was accepted, not followed into a preference form.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Manrope for body, nav, and buttons. Libre Bodoni for titles and prices. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, search, department bar, trust strip, and Add to Cart |
| Button | Default only. Add to Cart and Quick Buy not clicked |
| Link, wordmark, card, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was on screen and not typed into. Email and SMS signup were not filled |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Filter controls were on the category page and not opened. Other controls were not on the public pages opened |
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

That checks the ink, promo, nav, search, and bag tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
