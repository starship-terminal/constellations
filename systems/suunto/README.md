# Suunto

Suunto is a public shop for sports watches, dive products, compasses, and accessories. This package is a signed-out capture of [https://www.suunto.com](https://www.suunto.com) on 2026-11-22. The browser stayed on [https://www.suunto.com/](https://www.suunto.com/). The header labels the region Global (EN). A region dialog named Singapore, currency SGD, shipping only to Singapore. Continue was not clicked. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage and the Race 3S Titanium Black product page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Site apple-touch icon, 128 px |
| [icons/](icons/) | Header wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage and Race 3S product page |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the shipping bar white. It is a 48px black strip with white 14px type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint Shop now as an outline. It is `#ef3340`, 150 by 50, radius 4px, white type, weight 800. Same shot.
- Flatten the hero headline to the nav size. The headline is 75px Proxima Nova, weight 800, letter-spacing -1.5px. Nav labels are 20px, weight 700.
- Open Sign in, Search, Buy now, Subscribe, or the region Continue control from this package. Those walls were not entered.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Proxima Nova. Font files are not in this package |
| Spacing, radius, size | Captured for the shipping bar, header, Shop now, Buy now, and the hero headline |
| Button | Default only. Shop now and Buy now were not clicked |
| Link, wordmark, card, swatch | Default. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Newsletter email is in the footer. Not photographed. Nothing was typed |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Product tabs Overview, Specifications, and Support were on screen. The open Products menu was not photographed. Cookie buttons were not clicked |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured. Race 3S Titanium Black. No price was on screen |
| About | Listed at /About-Suunto/heritage/. Not photographed |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Sign in, Search, Buy now, and Subscribe were not opened |
| Dark theme | The public marketing page is a white header over a photographic hero. No theme toggle was on screen |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. The hero carousel was not advanced. Pause was not clicked |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, brand, graphite, card rule, and footer tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
