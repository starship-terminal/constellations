# Disney+

Disney+ is the streaming service from The Walt Disney Company. This package is a public capture of [disneyplus.com](https://www.disneyplus.com/) on 2026-11-22, signed out. The homepage redirected to the Singapore marketing page. The page is dark (`#040714`) with a cyan plan button. Desktop width measured 1440 by 900. Phone width measured 390 by 844 on the home page. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, resized from the published favicon |
| [DESIGN.md](DESIGN.md) | Copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Colour, type, and radius tokens |
| [style-guide.html](style-guide.html) | Specimens rendered from the tokens |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | Page patterns |
| [components/](components/) | Crops of LOG IN, DISNEY+ ANNUAL, and the empty help search |
| [icons/](icons/) | Published mask icon SVG and INDEX.tsv |
| [screenshots/](screenshots/) | Public pages and the login and subscribe walls |
| [raw/](raw/) | Computed styles that were read |
| [site-tree.md](site-tree.md) | Which control opens which page |
| [login-review.json](login-review.json) | What the login and subscribe walls ask for |
| [tools/](tools/) | Token check and the style-guide writer |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

Headless Playwright opened the public site at 1440 by 900, `devicePixelRatio` 1. Computed styles were read on the body, the h1, LOG IN, DISNEY+ ANNUAL, and View plan details. Hover on LOG IN and DISNEY+ ANNUAL was a real pointer move. Focus on LOG IN was `element.focus()`.

The login email wall and the plan chooser were also opened in the shared preview browser at CSS 1440 by 900, `devicePixelRatio` 2. Those readings are in [raw/readings.json](raw/readings.json).

Phone shots were requested at 390 by 844 with `deviceScaleFactor` 2. The home phone shot measured `innerWidth` 390.

## What to distrust

This is the signed-out marketing site, plus the empty login wall and the plan chooser. It is not the signed-in player.

The homepage redirected to `/en-sg`. Prices are Singapore dollars. Another region would show a different plan table.

LOG IN hover was read as `color(srgb 0.90896 0.90896 0.91024)`, stored as `#e8e8e8`. DISNEY+ ANNUAL hover was read as `color(srgb 0.19136 0.804693 0.92864)`, stored as `#31cdf0`.

The login wall body is `#17171c`. The marketing page is `#040714`. They are different surfaces.

No error, warning, or success colour was on the pages that were opened. Those roles are not in the tokens.

Spacing is not a named scale. Control height is on the measured buttons.

## Fonts

Inspire is the UI face on the marketing page, the login wall, and the plan chooser. The help centre uses Avenir on its search field. These are commercial faces. The tokens name Inspire. The files are not in this package.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Colour, accent | Captured | DISNEY+ ANNUAL fill `#33ddff` |
| Colour, status | Not captured | No live error, warning, or success state was shown |
| Type, display and UI | Captured | Home h1 and body |
| Type, code | Not present | No code sample on the public pages |
| Spacing scale | Not captured | No named spacing tokens were published |
| Radius | Captured | 1000px pill on LOG IN and DISNEY+ ANNUAL |
| Elevation | Not captured | Computed box-shadow none on the measured controls |
| Motion | Not captured | Durations were not read |
| Button | Captured | [components/crops/button-annual-default.png](components/crops/button-annual-default.png) |
| Button hover | Captured | [screenshots/home-light-annual-hover.png](screenshots/home-light-annual-hover.png) |
| Button focus | Captured | [screenshots/home-light-login-focus.png](screenshots/home-light-login-focus.png) |
| Link | Captured | View plan details on the home shot |
| Text field | Captured, empty | [screenshots/login-light-default.png](screenshots/login-light-default.png) |
| Text area | Not present | Not on the public pages that were opened |
| Select | Not present | Not on the public pages that were opened |
| Checkbox, radio, switch | Not present | Not on the public pages that were opened |
| Tabs | Observed | Legal page section links. Not activated past Subscriber Agreement and Privacy |
| Menu | Not present | The Singapore header has no product menu |
| Tooltip, toast, dialog | Not present | Not shown on the public pages |
| Card | Captured | Plan cards in [screenshots/signup-light-default.png](screenshots/signup-light-default.png) |
| Table | Captured | Plan comparison on the home page |
| List row | Captured | Help articles in [screenshots/help-light-default.png](screenshots/help-light-default.png) |
| Avatar | Not present | Not on the signed-out pages |
| App shell | Captured, marketing | Header is logo plus LOG IN |
| Empty, loading, error | Not captured | Marketing pages loaded. No empty catalog state was opened |
| Login wall | Captured, stopped | [login-review.json](login-review.json) |
| Subscribe wall | Captured, stopped | Same file |

## Do and don't

- Keep the marketing page on `#040714`. The cyan fill is for the plan buttons, not for body text.
- Use a pill for LOG IN and the plan buttons. LOG IN is a quiet outlined pill. The plan button is the cyan fill.
- Stop at the email wall and the plan chooser. Do not treat SELECT PLAN as a completed signup.

## Rebuild

```bash
python3 systems/disneyplus/tools/build_tokens.py
python3 systems/disneyplus/tools/build_style_guide.py
python3 systems/disneyplus/tools/test_build_tokens.py
```
