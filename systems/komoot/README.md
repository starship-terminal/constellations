# Komoot

Komoot is a public route planner for hikes, rides, and runs. This package is a signed-out capture of [https://www.komoot.com](https://www.komoot.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage and the public Help Guides page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, homepage, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Site icon, 128 px, scaled from the 96 px PNG the page links |
| [icons/](icons/) | Header pin, plus an index |
| [screenshots/](screenshots/) | Homepage and Help Guides, first viewport |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint Login or Signup orange. It is `#4f6814`, 135 by 43, radius 16px, cream type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint the page white. The page background is `#f5f3ec`. [screenshots/help-light-1440.png](screenshots/help-light-1440.png)
- Round the primary button to 4px. Login or Signup, Signup for Free, and App all use 16px. Same homepage shot.
- Open Login, Signup, or the App store dialog from this package. Those controls were on screen and were not used.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Satoshi for body and controls. Nohemi for the homepage heading and the Help Guides heading. Font files are not in this package |
| Spacing, radius, size | Captured for the header, Login or Signup, Signup for Free, App, and the Help Guides heading |
| Button | Default only. Login or Signup, Signup for Free, Login, and App were not clicked |
| Link, mark, card | Default. [screenshots/help-light-1440.png](screenshots/help-light-1440.png) |
| Text field | Not on the pages photographed. Discover has a search field and was not photographed |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | App is a button. The open store dialog was not photographed. The cookie dialog was removed from the DOM and not accepted. Other controls were not on the public pages photographed |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Help Guides | Captured. First viewport only |
| Features | Opened for the orange accent. Not photographed, because a phone mock prints a person's name |
| About | No public about page on www.komoot.com. Imprint names directors, so it was not photographed |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages photographed |
| Login, signup, identity providers, gift, subscribe | Stopped. Not submitted |
| Dark theme | Not captured. Help Guides is light. The homepage hero is a photograph |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, green, orange, and footer tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
