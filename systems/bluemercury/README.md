# Bluemercury

Bluemercury is a public beauty shop. This package is a signed-out capture of [https://bluemercury.com](https://bluemercury.com) on 2026-11-22. The browser stayed on bluemercury.com. A BlueRewards dialog asked for Sign In or Create an Account. The dialog was closed and the walk continued. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Skincare grid, and one public product were photographed.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, department links, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Wordmark on white, 128 px |
| [icons/](icons/) | Header wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage, Skincare grid, product |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar black. It is `#2f394b`, 35px, full width, with 12px white uppercase type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint Gift Guide in ink. It is `#0b51c1`. The other department labels are `#1c262e`. Same shot.
- Round the search field or Add to Bag. Search is a 48px underline, radius 0, 1px `#6d7275` bottom border. Add to Bag is a 60px rectangle, fill `#2f394b`, radius 0. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Set the category title in Neue Haas. "Skincare" is Juana, 50px, weight 300. [screenshots/category-light-1440.png](screenshots/category-light-1440.png)
- Stop at the sign-in wall. Sign In was not opened. The bag link points at `/cart` and was not opened. The BlueRewards dialog was closed.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Neue Haas for body, nav, price, and buttons. Juana for the category title. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, search, chips, and Add to Bag. Radius is 0 on those controls |
| Button | Default only. Shop Now and Add to Bag were not clicked |
| Link, wordmark, card, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was on screen and not typed into. Email and text signup were not filled |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Category chips were on screen and not clicked. Quantity was on screen and not used. Mega menus were read from the DOM and not photographed. Other controls were not on the public pages opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product and category | Captured |
| About | Listed in the footer as Our Company at `/pages/our-company`. Not opened |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Not submitted |
| Dark theme | Not present on the public shop |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, promo, search, and bag tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
