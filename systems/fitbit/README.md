# Fitbit

Fitbit's public shop now lives on the Google Store. This package is a signed-out capture of [https://www.fitbit.com](https://www.fitbit.com) on 2026-11-22. The browser landed on [https://store.google.com/sg/category/watches_trackers](https://store.google.com/sg/category/watches_trackers). Prices read SGD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The category page and the Google Fitbit Edge product page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, product cards, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Google Store favicon, 128 px |
| [screenshots/](screenshots) | Category page and Google Fitbit Edge |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar white. It is 53px `#050505`, with white type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint Sign in as the white Shop holiday deals pill. Sign in is `#0b57d0`, 40px, radius 100px, white type. Shop holiday deals is white, 48px, ink type, same radius.
- Flatten the category headline to the nav size. The headline is 76px Google Sans Flex, weight 500, letter-spacing -1px. Nav labels are 14px, weight 500.
- Open accounts.google.com, the cart, or a config URL from this package. Those walls were not entered.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Google Sans Flex, with Google Sans Text on Sign in. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, Sign in, Buy, New, Save, and the hero stage |
| Button | Default only. Sign in and Buy were not clicked |
| Link, wordmark, card, price | Default. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was not opened. No field was on the photographed fold |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Overview and Tech specs were on the product page. The specs page was not opened. Tray menus were not opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured. Google Fitbit Edge |
| About | Fitbit Support is listed in the footer. Not photographed |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Sign in, cart, Buy, and config links were not opened |
| Dark theme | No theme toggle was on screen |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the colour tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
