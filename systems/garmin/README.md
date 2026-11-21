# Garmin

Garmin is a public shop for watches, bike computers, and outdoor electronics. This package is a signed-out capture of [https://www.garmin.com](https://www.garmin.com) on 2026-11-22. The browser geo-redirected to the Singapore storefront at [https://www.garmin.com.sg/](https://www.garmin.com.sg/). Prices read SGD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the smartwatch category, and the CIRQA Smart Band product page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Wordmark on white, 128 px, cropped from the homepage shot |
| [icons/](icons/) | Header wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage, smartwatch category, and CIRQA product page |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the header black. It is white, 65px, with a 1px `#d8d8d8` rule and a black wordmark. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Round Learn More or BUY ON CONVERGENT. Both report radius 0. Learn More is a white outline, 36px. BUY ON CONVERGENT is `#60cff6`, 54px, black type. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Paint the price black. SGD 279 is `#137ec1`, 24px, weight 600. Same shot.
- Follow Help, Search, Shop, Retail Store, Garmin Connect, or BUY ON CONVERGENT from this package. Those walls were not entered.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Roboto for body, Oswald for display. Font files are not in this package |
| Spacing, radius, size | Captured for header, Learn More, FEATURED, NEW, price, and BUY ON CONVERGENT |
| Button | Default only. Learn More and BUY ON CONVERGENT were not clicked |
| Link, wordmark, card, price | Default. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was not opened |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table | Category menus were read from the DOM. The open panel was not photographed. Cookie buttons were not clicked |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured. All wearables and smartwatches |
| Product | Captured. CIRQA Smart Band |
| About | Opened at www.garmin.com/en-SG/company/about-garmin/. Not photographed in this package. LOCATIONS was not opened |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Help, Search, Shop, Retail Store, Garmin Connect, and BUY ON CONVERGENT were not opened |
| Dark theme | No theme toggle was on screen |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. The hero carousel was not advanced |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, black, rule, link, and sky tokens, plus the buy radius and header height, against [raw/readings.json](raw/readings.json). It does not recapture the site.
