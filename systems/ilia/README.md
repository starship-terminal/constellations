# ILIA

ILIA is a public clean-makeup shop. This package is a signed-out capture of [https://iliabeauty.com](https://iliabeauty.com) on 2026-11-22. The browser stayed on iliabeauty.com. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Best Sellers grid, and one public product were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Site mark, 128 px |
| [icons/](icons/) | Wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage, Best Sellers grid, product |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo strip white. It is `#a2605b`, 48px, with white 12px tracked type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Round SHOP THE SALE or Add to Bag. Both have radius 0. SHOP THE SALE is a 1.5px white outline, 49px. Add to Bag is fill `#271f1f`, 60px. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Set department labels in the rose promo colour. They are `#271f1f`, 12px, weight 500, letter-spacing 1.2px. The rose is only the top promo strip. Same homepage shot.
- Fill the email field or open Sign in. The walk stopped at login, bag, subscribe, and Add to Bag.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Post Grotesk for chrome, hero, and titles. Font files are not in this package |
| Spacing, radius, size | Captured for the promo strip, message band, nav, hero title, outline button, and Add to Bag |
| Button | Default only. SHOP THE SALE not followed. Add to Bag not clicked |
| Link, wordmark, card, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Email signup was on the footer and not typed into. Search was not opened |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menu links were read from the DOM. The open panel was not photographed. Shade and size were not changed. The promo drawer was not opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured. [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Listed at [https://iliabeauty.com/pages/about](https://iliabeauty.com/pages/about). Not opened. The product page stands in |
| Login, cart, checkout, subscribe | Stopped. Not opened |
| Phone width | Not captured. Desktop only |
| Dark theme | Not present. No theme control on the public shop |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the colour and size tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
