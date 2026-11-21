# Cult Beauty

Cult Beauty is a public beauty shop. This package is a signed-out capture of [https://www.cultbeauty.com](https://www.cultbeauty.com) on 2026-11-22. The browser stayed on cultbeauty.com and landed on the EU storefront, prices in EUR. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Makeup category, and one public product were photographed. Nothing was typed or submitted. Accept All Cookies was clicked so the homepage shot is the shop.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Site favicon, 128 px |
| [icons/](icons/) | Wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage, Makeup category, product |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo strip grey. The grey is the utility strip, `#efefef`, 50px. The promo is black, 44px, with white 16px tracked type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Round SHOP NOW or Add to Bag. Both have radius 0. SHOP NOW is 48px with a 1px black border. Add to Bag is 60px, 300px wide, with a 2px black border. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Set department labels in a brand colour. They are black, 16px, weight 400. Only Black Friday is a black chip with white type. Same homepage shot.
- Treat "25% OFF / 20 Brands" as a CSS type style. It is painted in the campaign image. The panel behind it is `#fbf3ee`, sampled from the screenshot.
- Fill the search field or open Account. The walk stopped at login, bag, search submit, ASK CULT, shade select, and signup.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured for chrome, nav, buttons, category title, and product title. Inter. Font files are not in this package. Hero title is in the campaign image |
| Spacing, radius, size | Captured for the utility strip, promo, search, ASK CULT, SHOP NOW, and Add to Bag |
| Button | Default only. SHOP NOW not followed. Add to Bag not clicked |
| Link, wordmark, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was on the header and not typed into. Email signup was not opened |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menu links were read from the DOM. The open panel was not photographed. Shade was not changed |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured. [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Listed at [https://www.cultbeauty.com/c/info/about-us/](https://www.cultbeauty.com/c/info/about-us/). Not opened. The product page stands in |
| Login, cart, checkout, subscribe | Stopped. Not opened |
| Phone width | Not captured. Desktop only |
| Dark theme | Not present. No theme control on the public shop |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the colour and size tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
