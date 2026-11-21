# END.

END. is a public clothing shop. This package is a signed-out capture of [https://www.endclothing.com](https://www.endclothing.com) on 2026-11-22. The first load was Singapore. The footer country control was set to the United States, and the shop stayed on `/en-us` with USD prices. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, the men's collection, and the about page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Site favicon, resized to 128 px |
| [icons/](icons/) | Header wordmark SVG |
| [screenshots/](screenshots/) | Homepage, product, collection, about |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Keep the ticker black and the page white. The announcement bar is `#000000`. The header and page are `#ffffff`. Ink is `#1a1a1a`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Use a square for the one action. Shop Now, Select a Size, and Sign Up are 46 to 50px with a 2px radius. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Stop at the account wall. Account points at `/en-us/account`. It was not opened. Cart, wishlist, search, and the subscribe field were not submitted.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. proxima-nova for body, nav, prices, and buttons. Font files are not in this package |
| Spacing, radius, size | Captured for ticker, header, wordmark, and buttons |
| Button | Default only. Select a Size and Add to Cart were not clicked |
| Link, wordmark, card, price, colour thumb | Default. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Not captured. Search and subscribe were not opened or filled. The email field on the about page was empty and disabled |
| Hover, focus, pressed, disabled, loading, error | Sign Up was disabled while the email field was empty. Other states were not measured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar, badge | Menu links were read from the DOM. The open panel was not photographed. Size was not selected |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product and collection | Captured |
| About | Captured. [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Not submitted |
| Dark theme | Not present on the public shop |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. The homepage hero is a video. It was left playing. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, announcement, accent, and border tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
