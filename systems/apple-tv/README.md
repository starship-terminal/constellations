# Apple TV

Apple TV is a streaming storefront. This package is a public Playwright capture of [tv.apple.com](https://tv.apple.com/) on 2026-11-22, signed out. The header is black on a `#1f1f1f` page. Sign In is `#0a84ff`. Desktop width measured 1440 by 900. Phone width measured 390 by 844 on the home page. Nothing was typed, submitted, or subscribed.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, resized from the published 180 px apple-touch icon |
| [DESIGN.md](DESIGN.md) | Dark-theme copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Colour, type, radius, and size tokens |
| [style-guide.html](style-guide.html) | Specimens rendered from the tokens |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | Page patterns |
| [components/](components/) | Crops of Sign In, the offer button, search, a nav link, and a poster |
| [icons/](icons/) | The header search glyph and INDEX.tsv |
| [screenshots/](screenshots/) | Public pages, the phone menu, and the empty login wall |
| [raw/](raw/) | Computed styles and custom properties that were read |
| [site-tree.md](site-tree.md) | Which control opens which page |
| [login-review.json](login-review.json) | What the login wall asks for |
| [tools/](tools/) | Token check and the style-guide writer |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

Headless Playwright opened the public site at 1440 by 900, `devicePixelRatio` 1. Computed styles were read on the body, `.header`, the Sign In button, the search input, and a show poster link. `--systemBlue` and the type tokens were read from custom properties on the document element. Focus on the search field used `element.focus()`. No text was typed.

Phone home was requested at 390 by 844 with `deviceScaleFactor` 2. It measured `innerWidth` 390.

## What to distrust

This is the public browse page, not a signed-in library. Watchlist, purchases, and playback past the free-episode control were not entered.

The country bar resolved the browser to Singapore. Continue on that bar was not clicked. Closing it does not change the storefront.

Sign In computed to `rgb(10, 132, 255)`. The published `--systemBlue` token is `#007aff`. The button fill is the value used for accent. Hover on Sign In did not change the fill.

The login sheet is an iframe. Its email field was empty. A nested `idmsa.apple.com` frame listed a password field and was not submitted. The screenshot shows the painted email sheet, not that nested frame.

Poster radius is 14px on the link. The inner image computed to 0px. The visible corner is the link.

## Fonts

SF Pro is the product face, named in the computed body stack. Helvetica Neue, Helvetica, and Arial are the fallbacks in that stack. The font files are not in this package.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#1f1f1f` body |
| Text colour | Captured | `#ffffffeb` |
| Accent | Captured | Sign In `#0a84ff` |
| Header | Captured | `#000000` |
| Muted | Captured | Inactive nav `#ffffffa3` |
| Type | Captured | SF Pro stack, 13px body |
| Radius | Captured | 6px Sign In, 4px search, 14px posters |
| Button | Captured | [components/crops/button-signin-default.png](components/crops/button-signin-default.png) |
| Link | Captured | [components/crops/link-nav-default.png](components/crops/link-nav-default.png) |
| Text field | Captured | Empty search field |
| Menu | Captured | [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) |
| Card | Captured | Homepage posters |
| Dialog | Captured | [screenshots/login-light-default.png](screenshots/login-light-default.png) |
| App shell | Captured | [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Search | Captured, empty | Search focused. Not submitted. |
| Form validation | Not captured | Sign-in form was not submitted |
| Loading and error | Not captured | No form was submitted |
| Destructive confirmation | Not present | Not on the public pages opened |
| Onboarding | Not captured | Would require an account |
| Dark theme | Captured | The public browse page is dark |
| Light theme | Not present | No public theme switch on the pages opened |
| Desktop 1440 | Captured | Playwright innerWidth 1440 |
| Phone 390 | Captured | Home and menu |
| Signed-in app | Not captured | Login wall. Session absent |
| Subscribe | Not captured | Accept Offer was not clicked |

## Do and don't

- **Use blue for Sign In.** The header button is `#0a84ff` on white, 6px radius, 28px tall, weight 600. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Keep the browse page dark.** Body is `#1f1f1f`. The header is black. Selected nav text is `#ffffffeb`. Inactive nav text is `#ffffffa3`. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Round posters, not the header.** Show links are 14px. The header is a flat black bar. See [screenshots/show-light-default.png](screenshots/show-light-default.png).
- **Do not submit the sign-in sheet from this capture.** The first wall asks for an email and stops at Continue. The field was empty. See [screenshots/login-light-default.png](screenshots/login-light-default.png).
- **Do not follow Accept Offer and keep capturing.** That control starts a subscription. Record it and stop. See [login-review.json](login-review.json).

## Rebuild

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Run those from this folder. `tools/build_tokens.py` checks sources. It does not regenerate tokens.json. The tokens were written from the readings at capture time. `make design-md` cannot write this package's DESIGN.md until catalog.json has an `apple-tv` entry. This pass does not edit catalog.json.
