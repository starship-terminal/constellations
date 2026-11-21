# MERIT

Public shop for MERIT Beauty. This package is a signed-out capture of [https://meritbeauty.com](https://meritbeauty.com) on 2026-11-22. The browser landed on [https://www.meritbeauty.com/](https://www.meritbeauty.com/). Prices read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Makeup category, and The Minimalist were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, nav, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Shop favicon, scaled to 128 px |
| [screenshots/](screenshots) | Homepage, Makeup, and The Minimalist |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar black. It is 40px `#5b2128`, with cream 12px type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint the homepage nav burgundy. Over the hero it is cream `#f9f8f5`. Burgundy `#5b2128` is the nav on Makeup and the product page, on a cream bar.
- Round Select Shade, or paint it black. It is radius 0, fill `#62605e`, white 11px, weight 500, uppercase, letter-spacing 1.32px, and it is disabled until a shade is chosen. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Paint Shop Now as that grey rectangle. Shop Now is a 13px text link, `#000000`, letter-spacing 0.52px, with an arrow.
- Paint Account as a filled button. Account is a 13px text link.
- Paint the product subtitle in the same black as the title. The title is Caslon italic `#000000`. The eyebrow is 11px uppercase `#000000`. The description is `#62605e`.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Akzidenz Grotesk for the interface, Adobe Caslon Pro italic for display. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, wordmark, Shop Now, shade pill, and Select Shade |
| Button | Default only. Select Shade was disabled and was not clicked. Shop Now was not followed |
| Link, wordmark, card, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Text field | Shade picker was on the product page. It was not used. Search and subscribe were not opened |
| Hover, focus, pressed, disabled, loading, error | Select Shade disabled state only. Hover and focus were not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Shop and Makeup drawers were read, not opened. Sort was not opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured. Makeup, 20 products. [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured. The Minimalist |
| About | About Us is listed in the footer. Not photographed |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Account, cart, the sale waitlist, and the footer subscribe field were not opened |
| Dark theme | No theme toggle was on screen |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the colour tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
