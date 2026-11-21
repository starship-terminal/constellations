# Haus Labs

Public capture of [https://hauslabs.com](https://hauslabs.com) on 2026-11-22. Signed out. The browser stayed on hauslabs.com. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, Shop All, and Triclone Skin Tech Foundation were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Wordmark on white, 128 px |
| [screenshots/](screenshots/) | Homepage, Shop All, product |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar gray. It is `#000000`, 48px, full width, with white 13px type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint the hero title black. The photographed title sits on `#f1f1f1` and the letter pixels read `#686868`. Nav and Add to Bag ink are `#000000`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Round Add to Bag. It is 299 by 40, fill `#000000`, white type, radius 0. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Stop at the account wall. Account points at `/account` and was not opened. Bag is a button and was not opened. The subscribe dialog was closed and not submitted.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. SuisseIntl for body, nav, titles, and buttons. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, header, wordmark, and Add to Bag |
| Button | Default only. Add to Bag and Notify Me were not clicked. Sign Up was not clicked |
| Link, wordmark, card, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was a closed button and was not opened. Email signup and notify-me were not filled |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Shop menu links were read from the DOM. The open panel was not photographed. Shade chips were not clicked. Sort by and Show Filters were not opened. The subscribe dialog was closed |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product and category | Captured |
| About | Listed at `/pages/about`. Not opened. The third photograph is the product page |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Not submitted |
| Dark theme | Not present on the public shop |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. The homepage hero is a still frame of a video |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, promo, header, page, bag, notify, hero, muted, and radius tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
