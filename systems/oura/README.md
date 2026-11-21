# Oura

Oura is a public smart-ring shop. This package is a signed-out capture of [https://ouraring.com](https://ouraring.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage and About Us were photographed. The Shop menu was read. The Ring 5 URL was opened and not photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Apple touch icon, 128 px |
| [icons/](icons/) | Header wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage and About Us |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the page white. The homepage surface is `#f7f1e8`. About Us is `#efe6db`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint Shop Sale in ink. It is a 48px pill, fill `#2a72de`, type white, weight 700. Same shot.
- Set the Black Friday badge in sentence case. It is 12px, weight 700, tracking 0.6px, fill `#1c1b1a`, type `#f7f1e8`, radius 8px. Same shot.
- Open the cart. The cart link points at `/cart` and was not opened. The footer email field was not filled. Membership was not started.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Editorial New for the homepage h1. AkkuratLL for body, nav, and Shop Sale. Font files are not in this package |
| Spacing, radius, size | Captured for the promo strip, header, Shop Sale, badge, and cart circle |
| Button | Default only. Shop Sale was not clicked as a purchase |
| Link, wordmark, badge | Default. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Text field | An email field was in the footer and not typed into |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menu links were read from the DOM. The open panel was not photographed. Other controls were not on the public pages opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| About | Captured. [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Product | URL opened, not photographed |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, membership, login | Stopped. Not submitted. No login form was on the homepage |
| Dark theme | Not present on the public shop |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, action, badge, and muted tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
