# Withings

Withings is a public health-device shop. This package is a signed-out capture of [https://www.withings.com](https://www.withings.com) on 2026-11-22. The browser geo-redirected to the United States storefront at [https://www.withings.com/en-us](https://www.withings.com/en-us). A geo modal said the visit was from Singapore and that Withings does not ship there. The selector already showed United States (USD). The modal was closed and the walk stayed on that storefront. Prices read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage and the BodyScan 2 Black product were photographed. Nothing was typed, submitted, or signed in.

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
| [screenshots/](screenshots/) | Homepage and BodyScan 2 Black |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the header black. It is `#ffffff`, 70px, with ink `#0f0f0f`. The announcement bar under it is `#000000`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint Add to cart black. It is `#6784fe`, 16px radius, white type. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Square Shop now. It is a 121 by 51 white button, radius 16px, label "Shop now", on the black hero. Same homepage shot.
- Follow the Singapore shipping prompt. Confirm was not clicked. Account, cart, search, and the footer signup were not used.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Aeonik for body, nav, title, price, and buttons. Font files are not in this package |
| Spacing, radius, size | Captured for header, announcement bar, Shop now, and Add to cart |
| Button | Default only. Add to cart and Shop now were not clicked |
| Link, wordmark, price | Default. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search and the footer signup were on the page and not typed into |
| Hover, focus, pressed, disabled, loading, error | Not captured. Primary hover is declared `#5570e0` and was not sampled |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table | Menu links were read from the DOM. The open panel was not photographed. The geo dialog was closed. Plan radios on the product page were not selected |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured. BodyScan 2 Black, $599.95 USD |
| About | Not opened. Careers and Press are linked in the footer |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Not submitted |
| Dark theme | Not present on the public shop. The hero is a black photograph on a white page |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, page, promo, nav, and bag tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
