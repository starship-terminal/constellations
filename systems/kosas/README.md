# Kosas

Public shop for Kosas Cosmetics. This package is a signed-out capture of [https://kosas.com](https://kosas.com) on 2026-11-22. The country control reads Singapore $SGD. Promo copy and product prices still read $. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Bestsellers category, and Cloud Set Mist were photographed. A signup popup was closed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, nav, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Shop favicon, scaled to 128 px |
| [screenshots/](screenshots) | Homepage, Bestsellers, and Cloud Set Mist |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar black or pink. It is 32px `#eeeec8`, with black 12px Founders Grotesk Mono, uppercase. The pink `#D33167` is a CSS token only. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Fill Shop Now black. Shop Now is an outline rectangle, radius 0, border 2px `#000000`, type black 16px. Add to Bag is the filled black rectangle. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Round Shop Now or Add to Bag. Both are radius 0. The only measured radius on the fold is the 6px checkout note and the 4px sale chip.
- Paint Search or Log in as a filled pill. Search is a 12px uppercase label. Log in is a 26px icon.
- Open `/account`, the bag, or Add to Bag from this package. Those walls were not entered.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Founders Grotesk and Founders Grotesk Mono. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, wordmark, Shop Now, Add to Bag, and the hero |
| Button | Default only. Shop Now and Add to Bag were not clicked |
| Link, wordmark, card, price | Default. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Quantity stepper was on the product page. It was not used. Search and the mailing list were not opened |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Shop All submenu and Sort by were not opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured. Bestsellers. [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured. Cloud Set Mist |
| About | Our Story is listed in the footer. Not photographed |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Log in, bag, Add to Bag, and Sign Up were not opened |
| Dark theme | No theme toggle was on screen |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the colour tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
