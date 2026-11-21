# Nordstrom

Nordstrom is a public clothing and beauty shop. This package is a signed-out capture of [https://www.nordstrom.com](https://www.nordstrom.com) on 2026-11-22. The browser stayed on www.nordstrom.com. The shipping bar says the visit is outside the U.S. and the country control reads Singapore. Prices read SGD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the women's clothing grid, one public product, and About Us were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Wordmark on white, 128 px |
| [icons/](icons/) | Header wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage, clothing grid, product, About Us |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar white. It is `#191a1b`, 41px, full width, with white type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint Black Friday & Sale in the same ink as Women. That label is `#b80009`. Same shot.
- Round the search field. Search is a 42px rectangle, radius 0, fill `#f0f3f5`. Add to Bag is the control with a 4px radius. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Stop at the sign-in wall. Sign In was not opened. The bag link points at `/shopping-bag` and was not opened. The bot wall that printed a phone number was discarded.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Brandon Text for body, nav, title, and buttons. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, search, and Add to Bag |
| Button | Default only. Add to Bag not clicked |
| Link, wordmark, card, price, badge | Default. [screenshots/collection-light-1440.png](screenshots/collection-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was on screen and not typed into. Email updates were not filled |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menu links were read from the DOM. The open panel was not photographed. Size chips were not clicked. Other controls were not on the public pages opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product and collection | Captured |
| About | Captured. [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Not submitted |
| Dark theme | Not present on the public shop |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, sale, search, price, and promo tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
