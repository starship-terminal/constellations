# HOKA

HOKA is a public running-shoe shop. This package is a signed-out capture of [https://www.hoka.com](https://www.hoka.com) on 2026-11-22. The first page was a region picker. Visit Site was clicked with United States and English already selected. The walk continued on [https://www.hoka.com/en/us/](https://www.hoka.com/en/us/). Prices read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage and the Women's grid were photographed. A product page and About were requested and came back as a captcha wall, which was not solved. Nothing was typed or submitted.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Region picker, header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Wordmark on white, 128 px |
| [icons/](icons/) | Header wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage and Women's grid |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the wordmark black. It is `#009dff`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint the utility bar white. It is `#000000`, 48px, with white type. Same shot.
- Square the search field. Search is a 36px pill, radius 52px, white fill, 1px black border. Shop Now is the same pill, 48px, white on the hero. Same shot.
- Paint sale copy black. Holiday Exclusive and "(20% Off)" are `#e10f00`. The struck list price is `#4d4d4d`. [screenshots/category-light-1440.png](screenshots/category-light-1440.png)
- Stop at the sign-in wall. Sign In, Join for Free, Account, and the cart were not completed. The cart link points at `/en/us/cart/` and was not opened.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. the-future for body, nav, title, and buttons. Font files are not in this package |
| Spacing, radius, size | Captured for utility bar, search, Ask HOKA, Shop Now, and the category title |
| Button | Default only. Shop Now and Ask HOKA were not clicked |
| Link, wordmark, card, price | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Text field | Search was on screen and not typed into. Email signup was not filled |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menu links were read from the DOM. The open panel was not photographed. Sort and size chips were on the grid and not clicked |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured. Women's view all, 227 results |
| Product | Listed on the grid. The product URL was requested and returned a captcha wall. Not photographed |
| About | Requested at `/en/us/about-hoka.html`. Same captcha wall. Not photographed |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Not submitted |
| Dark theme | Not present on the public shop |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, utility, mark, sale, and pill tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
