# COROS

Public signed-out capture of the COROS shop at [https://coros.com](https://coros.com) on 2026-11-22. The browser stayed on the United States storefront. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage and the COROS PACE 4 product page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Promo bar, header, menu destinations, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | COROS favicon, 128 px |
| [screenshots/](screenshots) | Homepage and COROS PACE 4 |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar white. It is 36px `#000000`, with white 16px type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Round SHOP NOW. It is a 128 by 38 rectangle, radius 0, 2px white border, fill `rgba(255, 255, 255, 0.16)`.
- Paint sticky BUY NOW as that ghost button. Sticky BUY NOW is `#020015`, 98 by 30, type `#f1f1f1`, radius 0.
- Flatten the hero to the nav size. Holiday Gift Guide is 90px DINCOROS-Black. Nav labels are 13.5px PFDINTextPro-Medium.
- Open t.coros.com, the bag, or `/buy/`. Those walls were not entered.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. DINCOROS-Black, PFDINTextPro, Inter. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, nav, SHOP NOW, and sticky BUY NOW. Radius is 0 |
| Button | Default only. SHOP NOW and BUY NOW were not clicked |
| Link, wordmark, card | Default. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | No field was on the photographed fold |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | OVERVIEW, HIGHLIGHTS, SPECS, and COMPARE were on the product bar. SPECS and COMPARE were not opened. Mega menus were not opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured. COROS PACE 4 |
| About | Who We Are is listed. Not photographed |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Log in, Shopping Bag, and BUY NOW were not opened |
| Dark theme | No theme toggle was on screen |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run. Slide autoplay was paused before the homepage shot |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the colour tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
