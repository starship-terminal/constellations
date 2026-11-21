# Strava

Strava is a public running, cycling, and hiking product. This package is a signed-out capture of [https://www.strava.com](https://www.strava.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage and the public Features page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, activities menu, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Site icon, 128 px, from the 192 px apple-touch source |
| [icons/](icons/) | Header echelon and wordmark, plus an index |
| [screenshots/](screenshots/) | Homepage and Features, first viewport |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the primary button black. Sign Up With Email is `#fc5200`, 404 by 44, radius 4px, white type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint the wordmark black. The header mark and wordmark are the same orange. [icons/wordmark.svg](icons/wordmark.svg)
- Round the Log In button past 4px. Header Log In is a white rectangle, 88 by 40, 1px border `#e0e0de`. Same homepage shot.
- Open Log In, Sign Up, Google, or Apple from this package. Those controls were on screen and were not used.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Boathouse on the homepage. BoathouseExtended on the Features heading. Font files are not in this package |
| Spacing, radius, size | Captured for the header, Log In, signup buttons, and the Features CTA |
| Button | Default only. Sign Up With Email, Google, Apple, and Dive into your Subscription were not clicked |
| Link, wordmark, card | Default. [screenshots/features-light-1440.png](screenshots/features-light-1440.png) |
| Text field | Not on the pages opened |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Activities is a button. The open panel was not photographed. Other controls were not on the public pages opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Features | Captured. First viewport only. The page is 8104px tall |
| About | Listed in the footer. Not photographed |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Login, signup, identity providers, subscribe checkout | Stopped. Not submitted |
| Dark theme | Not captured. The homepage is light. The Features hero is a dark photograph |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the orange, ink, page, footer, and signup tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
