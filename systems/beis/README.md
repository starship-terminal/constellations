# Béis

Béis is a public luggage and bags shop. This package is a signed-out capture of [https://beistravel.com](https://beistravel.com) on 2026-11-22. Prices read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, the luggage collection, and the about page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Wordmark on the cream header colour |
| [screenshots/](screenshots/) | Homepage, product, collection, about |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Keep the header cream. The page is `#ffffff` and the bar is `#f2f1ec`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Use a square for the one action. Add to Cart and Shop Travel Essentials are 40px with a 9px radius. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Stop at the sign-in wall. It opened on `account.beistravel.com` with an OAuth query. The email field was empty. Submit was not clicked. That screenshot was discarded.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Helvetica body, cofo-sans-variable display. Font files are not in this package |
| Spacing, radius, size | Captured for header, announcement, buttons, swatches |
| Button | Default only. Add to Cart not clicked |
| Link, wordmark, card, price, swatch, size chip | Default. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Not captured. Subscribe and search were not opened. Login email was on an OAuth URL and was discarded |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar, badge | Menu links were read from the DOM. The open panel was not photographed. Other controls were not on the public pages opened |
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

That checks the page, header, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
