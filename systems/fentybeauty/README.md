# Fenty Beauty

Public shop for Fenty Beauty by Rihanna. This package is a signed-out capture of [https://fentybeauty.com](https://fentybeauty.com) on 2026-11-22. The browser landed on [https://fentybeauty.com/en-sg](https://fentybeauty.com/en-sg). The country control reads Singapore | English. Prices read SGD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the All Makeup category, and the Glossy Posse IX lip set were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, nav, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Shop favicon, scaled to 128 px |
| [screenshots/](screenshots) | Homepage, All Makeup, and Glossy Posse IX |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar pink. It is 37px `#000000`, with white 12px type. The pink is the gift-guide panel, `#fdcbd4`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Round Get Giftin' or Add to Bag. Both are radius 0, fill `#000000`, white 12px, weight 700, uppercase, letter-spacing 0.3px.
- Paint Sign In as that black button. Sign In is a 12px text link, `#2d2929`, weight 400.
- Paint the compare price in the same grey as the sale price. The sale price is `#666666`. The compare price is `#bd0100` with a line-through. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Open `#rivo`, the cart, or Add to Bag from this package. Those walls were not entered.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Brown, with Brown Optical on buttons. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, wordmark, Get Giftin', Add to Bag, and the hero panel |
| Button | Default only. Get Giftin' and Add to Bag were not clicked |
| Link, wordmark, card, price | Default. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Quantity stepper was on the product page. It was not used. Search and subscribe were not opened |
| Hover, focus, pressed, disabled, loading, error | Not captured. Disabled fill `#a8a8a8` is a CSS token only |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Filters and Discover were not opened. Country selector was not opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured. All Makeup. [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured. Glossy Posse IX 4-Piece Lip Set |
| About | About the Brands is listed in the footer. Not photographed |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Sign In, cart, Add to Bag, and `#rivo` were not opened |
| Dark theme | No theme toggle was on screen |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the colour tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
