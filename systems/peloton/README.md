# Peloton

Peloton is a public fitness equipment and membership marketing site. This package is a signed-out capture of [https://www.onepeloton.com](https://www.onepeloton.com) on 2026-11-22. Desktop width measured 1440 by 900. Saved screenshots are 2880 by 1800. The homepage and the Cross Training Bike page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Site apple-touch icon, 128 px |
| [icons/](icons/) | Header wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage and Bike page |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar ink. It is `#df1c2f`, 66px, full width, with white type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint Deals in the same white as Bikes. Deals is `#ff5a5a`. Same shot.
- Square the Shop now button. It is a pill, radius 28px, fill `#df1c2f`. [screenshots/bike-light-1440.png](screenshots/bike-light-1440.png)
- Open Account, Cart, or Membership from this package. Those walls were not crossed.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Inter for body, nav, title, and buttons. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, nav, Shop deals, and Shop now |
| Button | Default only. Shop now not clicked |
| Link, wordmark, card | Default. [screenshots/home-light-1440.png](screenshots/home-light-1440.png), [screenshots/bike-light-1440.png](screenshots/bike-light-1440.png) |
| Text field | Footer email field was on the page and not typed into |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menu links were read from the DOM. The open panel was not photographed. Country select was not submitted |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured. [screenshots/bike-light-1440.png](screenshots/bike-light-1440.png) |
| About | Listed. Our Story is [https://www.onepeloton.com/company](https://www.onepeloton.com/company). Not in the saved screenshot set |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login, membership | Stopped. Not submitted |
| Dark theme | The marketing shell is an ink nav on a light page. No theme toggle was used |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, red, deals, and pill tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
