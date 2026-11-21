# Ride with GPS

Ride with GPS is a public cycling route planner and navigation product. This package is a signed-out capture of [https://ridewithgps.com](https://ridewithgps.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage and the public Route Planner page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, homepage, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Site icon, 128 px, scaled from the 180 px apple-touch PNG |
| [icons/](icons/) | Header wordmark, plus an index |
| [screenshots/](screenshots/) | Homepage and Route Planner, first viewport |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint Get Started blue. It is `#fa6400`, 148 by 48, radius 3px, white type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint the page white. The page shell is ink `#0b1c1c`. The white band is a later block, not the fold. Same homepage shot.
- Round the primary button to 16px. Get Started, Join for free, and Plan a Route use 3px. [screenshots/planner-light-1440.png](screenshots/planner-light-1440.png)
- Open Log In, Get Started, or Plan a Route from this package. Those controls were on screen and were not used.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. aktiv-grotesk for body and controls. The display family loads as a hashed name. Font files are not in this package |
| Spacing, radius, size | Captured for the header, Get Started, Join for free, and Plan a Route |
| Button | Default only. Get Started, Join for free, and Plan a Route were not clicked |
| Link, mark | Default. See How It Works is yellow `#ffd771`. [screenshots/planner-light-1440.png](screenshots/planner-light-1440.png) |
| Text field | Not on the pages photographed. Search is a button and was not opened |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Stories and English are buttons. Their menus were not opened. Other controls were not on the public pages photographed |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Route Planner | Captured. First viewport only |
| About | Opened for text only. It names people, so it was not photographed |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages photographed |
| Login, signup, identity providers, subscribe | Stopped. Not submitted |
| Dark theme | Not captured. The public pages are one scheme. The hero is a photograph |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, white, orange, nav, and yellow tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
