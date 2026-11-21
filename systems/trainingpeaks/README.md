# TrainingPeaks

TrainingPeaks is a public endurance training product. This package is a signed-out capture of [https://www.trainingpeaks.com](https://www.trainingpeaks.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage and the public Athlete Features page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Promo bar, header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Site icon, 128 px, from the 192 px favicon |
| [icons/](icons/) | Header wordmark, plus an index |
| [screenshots/](screenshots/) | Homepage hero and Athlete Features, first viewport |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar blue. The class is brand blue. The paint is `#f1fd53`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint Athlete Sign Up blue. That pill is `#010f31`. Coach Sign Up is the blue one. Same shot.
- Square the header buttons. Athlete Sign Up, Coach Sign Up, and Log In are pills. Same shot.
- Open Log In, Athlete Sign Up, Coach Sign Up, or the promo checkout from this package. Those controls were on screen and were not used.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Inter-Regular on the homepage. EncodeSansExpanded-ExtraBold on both headings. Font files are not in this package |
| Spacing, radius, size | Captured for the promo bar, header pills, hero pills, and the Features Sign up |
| Button | Default only. Signup, Log In, and checkout were not clicked |
| Link, wordmark, card | Default. [screenshots/features-light-1440.png](screenshots/features-light-1440.png) |
| Text field | Not on the pages opened |
| Hover, focus, pressed, disabled, loading, error | Not captured. `--mdc-theme-error` is declared and was not seen |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menus are buttons. The open panels were not photographed. Other controls were not on the public pages opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Features | Captured. First viewport only. The page is 7659px tall |
| About | Listed in the footer at `/about-us/`. Not photographed |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Login, signup, identity providers, subscribe checkout | Stopped. Not submitted |
| Dark theme | Not captured. The public pages opened are light, with photographic heroes |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. An unloaded homepage video was left out of the photograph |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the navy, blue, nav, heading, and lime tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
