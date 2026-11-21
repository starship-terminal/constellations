# Booking.com

Booking.com is a travel marketplace from Booking Holdings. This package is a public Playwright capture of [booking.com](https://www.booking.com/) on 2026-11-22, signed out. The marketing site is light: a blue header (`#003b95`), a white page, and a yellow search frame (`#ffb700`). Desktop width measured 1440 by 900. Phone width measured 390 by 844 on the home page and the Genius page. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px icon, resized from the published apple-touch icon |
| [DESIGN.md](DESIGN.md) | Light-theme copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Colour, type, and radius tokens |
| [style-guide.html](style-guide.html) | Specimens rendered from the tokens |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | Page patterns |
| [components/](components/) | Crops of Search and Sign in |
| [icons/](icons/) | Header wordmark SVG and INDEX.tsv |
| [screenshots/](screenshots/) | Public pages, currency and language dialogs, and the login and signup wall |
| [raw/](raw/) | Computed styles that were read |
| [site-tree.md](site-tree.md) | Which control opens which page |
| [login-review.json](login-review.json) | What the login and signup wall asks for |
| [tools/](tools/) | Token check and the style-guide writer |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

Headless Playwright opened the public site at 1440 by 900, `devicePixelRatio` 1. `getComputedStyle` was read on the body, the header, the footer, the h2, Sign in, Register, Search, and the Stays tab. Hover on Sign in and Search was a real pointer move. Focus on Sign in was `element.focus()`. The Genius sign-in sheet was dismissed, not answered.

The Search button's computed background was transparent. The blue fill `#006ce4` was sampled from the screenshot. The yellow frame `#ffb700` was a computed style.

Phone shots were requested at 390 by 844 with `deviceScaleFactor` 2. The home phone shot measured `innerWidth` 390. The PNG is 780 by 1688.

## What to distrust

This is the marketing site, not a signed-in trip or a property page. Do not treat the Black Friday hero as the app chrome.

The homepage heading copy changed between loads ("Up to 40% off stays this Black Friday" and "Our biggest sale of the year"). The photographed home shot is the Black Friday line. The type measurement is from a later load of the same element.

No CSS custom properties were published on `:root`. Tokens are computed styles and sampled fills, not a product token file.

Sign in hover `#f0f6fd` is sampled from the crop. Search hover did not change the blue fill.

The sign-in wall heading used Blue Sans. The marketing headings used Avenir Next. The style guide uses Avenir Next and falls back to system-ui.

## Fonts

The UI face is the system stack. Avenir Next is the marketing heading face. Blue Sans is the account-wall heading face. These names were read from computed styles. The files are not in this package.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Colour, accent | Captured | Search fill `#006ce4` |
| Colour, status | Not present | No success, warning, or error state on the public pages that were opened |
| Type, display and UI | Captured | Home h2 and body |
| Type, code | Not present | No code sample on the public pages |
| Spacing scale | Derived | 4px unit from control padding. No named scale |
| Radius | Captured | 4px control, 8px search frame, pill tab |
| Elevation | Not captured | Sign in computed box-shadow none. Dialog shadow was not stored |
| Motion | Not captured | No duration was read |
| Button | Captured | [components/crops/button-search-default.png](components/crops/button-search-default.png) |
| Button hover | Captured | [components/crops/button-signin-hover.png](components/crops/button-signin-hover.png) |
| Button focus | Captured | [screenshots/home-light-signin-focus.png](screenshots/home-light-signin-focus.png) |
| Link | Captured | Recover link on the sign-in wall |
| Text field | Captured, empty | [screenshots/login-light-default.png](screenshots/login-light-default.png) |
| Text area | Not present | Not on the public pages that were opened |
| Select | Captured as dialogs | Currency and language |
| Checkbox | Captured, unchecked | [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Radio | Captured | Airport taxis one-way and return. Not toggled |
| Switch | Not present | Not on the public pages that were opened |
| Tabs | Captured | Product tabs and Help Center FAQ tabs. Only Stays was selected |
| Menu | Captured | Currency and language dialogs |
| Tooltip, toast | Not present | Not shown on the public pages |
| Dialog | Captured | [screenshots/home-light-menu-currency.png](screenshots/home-light-menu-currency.png) |
| Card | Captured | Why Booking.com cards |
| Table, list row, avatar | Not present | Not on the public pages that were opened |
| Icon button | Not captured | Phone menu button was visible and not opened |
| App shell | Captured | [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Form validation | Not captured | No form was submitted |
| Empty, loading, error | Not captured | Signed-in account was not entered |
| Destructive confirmation | Not present | Not on the public site |
| Search | Captured, empty | Homepage search. Not submitted |
| Onboarding | Not captured | Would require an account |
| Dark theme | Not present | Public marketing site is light |
| Light theme | Captured | Marketing site and the sign-in wall |
| Desktop 1440 | Captured | Playwright innerWidth 1440 |
| Phone 390 | Captured | Home and Genius |
| Signed-in account | Not captured | Login wall. Session absent |

## Do and don't

- **Use blue for the primary action.** Search and Continue with email are `#006ce4` on white text. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Keep the header on dark blue.** Header background is `#003b95`. The wordmark is white. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Put yellow on the search frame, not on the button.** The frame is `#ffb700`. The Search label sits on blue inside that frame. See [components/crops/button-search-default.png](components/crops/button-search-default.png).
- **Do not submit the sign-in form from this capture.** Register and Sign in are the same wall. It offers Google, Apple, and Facebook as well as email. No provider was clicked. No account was created. See [screenshots/login-light-default.png](screenshots/login-light-default.png).
- **Do not start a stay search and keep capturing.** Search, dates, and occupancy were left empty. Checkout was not opened.

## Rebuild

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Run those from this folder. `tools/build_tokens.py` checks sources. It does not regenerate tokens.json. The tokens were written from the readings at capture time. `make design-md` cannot write this package's DESIGN.md until catalog.json has a `booking` entry. This pass does not edit catalog.json.
