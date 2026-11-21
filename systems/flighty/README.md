# Flighty

Flighty is the flight tracker at [flighty.com](https://flighty.com). This package is a public capture from 2026-11-21, signed out. The site is marketing pages plus a public airports map. The product itself is the iOS app. There is no web login: `/login` returns the site's 404.

Which control opens which page, menu, or dialog is in [site-tree.md](site-tree.md).

| File | What it holds |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Homepage control map, written before the public screenshots. |
| [icon.png](icon.png) | Site icon, 128 px, from the public favicon. |
| [DESIGN.md](DESIGN.md) | Companion, hand-written. This PR does not edit catalog.json, so `make design-md` was not run. |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds type, radius, and control sizes. `light` is the homepage. `dark` is the pricing page and the 404, not a theme switch. Every token has `$extensions.source`. |
| [style-guide.html](style-guide.html) | Renders the homepage type, the pills, and the pricing accent. |
| [components.md](components.md) | Buttons, nav links, the download dialog, pricing tabs, and the gaps. |
| [patterns.md](patterns.md) | Header, download dialog, pricing, help, and the 404. |
| [login-review.json](login-review.json) | Public review: offered nav, settings, and create as objects, the screens, the gaps, and what was not submitted. |
| [screenshots/](screenshots/) | Public frames. Desktop PNGs are 2880x1800. [home-light-mobile.png](screenshots/home-light-mobile.png) is 780x1688. |
| [raw/](raw/) | Computed styles from the live pages. |
| [tools/](tools/) | [build_tokens.py](tools/build_tokens.py), [build_style_guide.py](tools/build_style_guide.py), and [build_components_md.py](tools/build_components_md.py). |

## Brief

<!-- brief:start -->

Not generated. This PR does not edit catalog.json, and `make brief` reads the catalog entry.

<!-- brief:end -->

## Health

<!-- health:start -->

Not graded. This PR does not edit catalog.json, and `make grade` reads the catalog entry.

Layout: no `components/` (page screenshots are the evidence; element crops were not cut), no `icons/` (no icon set was extracted; icon.png is the site favicon).

<!-- health:end -->

## How the values were read

`getComputedStyle` on the public homepage produced the h1, the nav Pricing label, the lede, Get the app, and both Give Flighty a try buttons. Those readings are in [raw/home-computed.json](raw/home-computed.json) and [raw/detail-computed.json](raw/detail-computed.json).

The promo strip's computed background was transparent. Its color is the median pixel of the raw homepage PNG, sampled before quantise: (18, 18, 140), stored as `#12128c`.

Try it for free on `/pricing` computed to `rgb(191, 89, 242)`. The same pixel was the mode of the purple region in the raw pricing PNG.

The cookie banner was hidden with CSS in the marketing screenshots. Reject and Accept were not clicked. The airports page still showed the banner, and that frame was not committed.

## What to distrust

`dark` is not a theme. It is the pricing page body (`#000000`) and the 404 body (`#161616`). There is no theme switch.

The Get the app anchor's own font-size computed as 12px. The visible label is the inner paragraph at 15px weight 500. Use the paragraph.

Screenshots are 256-colour PNGs. Do not sample tokens from them.

The airports disruption table was on screen and is not in this package. Do not treat a missing airports screenshot as evidence that the page is empty.

## Fonts

The measured stack is system-ui, then -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, and sans-serif. No webfont file was downloaded. The tokens use that stack as the fallback.

## Coverage

| Item | Status |
|---|---|
| Colour roles, light | Captured. [tokens.json](tokens.json) `light`, [home-light-default.png](screenshots/home-light-default.png). |
| Colour roles, dark theme | Not present. Pricing and the 404 paint dark. There is no theme switch. |
| Type roles | Captured. Display, heading, nav, body, button in [tokens.json](tokens.json). |
| Spacing, radii, control heights | Captured for the three buttons. The rest of the spacing scale was not tokenised. |
| Border widths | Captured as the white button's 1px rgba(0, 0, 0, 0.12) border, recorded in components.md. |
| Elevation | Not present on the measured controls. boxShadow was none. |
| Motion | Not captured. No duration or easing was read. |
| Button | Captured. Default only. [home-light-default.png](screenshots/home-light-default.png), [pricing-light-default.png](screenshots/pricing-light-default.png). |
| Icon button | Not present as its own control. The phone hamburger was not opened. |
| Link | Captured. Nav links in [home-light-default.png](screenshots/home-light-default.png). |
| Text field | Not captured. Help search is visible in [help-light-default.png](screenshots/help-light-default.png). The visible input's computed style was not read. |
| Text area | Not present. |
| Select | Not present. |
| Checkbox | Not present. |
| Radio | Present on gift cards, not changed. [gift-cards-light-default.png](screenshots/gift-cards-light-default.png). |
| Switch | Not present. |
| Tabs | Pricing plan tabs, Annual painted as selected. Other tabs not clicked. |
| Menu | Not present on desktop. Phone menu not opened. |
| Tooltip | Not present. |
| Dialog | Captured. [home-light-get-app.png](screenshots/home-light-get-app.png). |
| Toast | Not present. |
| Card | Captured. Pricing, gift cards, business. |
| List row | Captured. Help Center questions. |
| Table | Not captured. The airports table is live data and was not committed. |
| Avatar | Marketing artwork only. No account avatar. |
| Badge | Promo strip and the pricing "Most popular plan" pill. Not a status badge. |
| App shell | Not present. Marketing header only. |
| Form with validation | Not captured. No form was submitted. |
| Empty, loading | Not captured. |
| Error | Captured. [login-404-light-default.png](screenshots/login-404-light-default.png). |
| Destructive confirmation | Not present. |
| Feedback after an action | Not captured. Nothing was submitted. |
| Search and filtering | Help search photographed empty, not used. |
| Onboarding | The download dialog. No web onboarding. |
| Desktop 1440 | Captured. CSS 1440x900, PNG 2880x1800. |
| Phone 390 | Captured. CSS 390x844, PNG 780x1688. |

## Do and don't

- **One black headline on white.** The homepage h1 is 65px, weight 700, black on white. See [home-light-default.png](screenshots/home-light-default.png).
- **The promo strip is the only blue bar.** It sits above the nav. Do not invent a second blue accent. See [home-light-default.png](screenshots/home-light-default.png).
- **Primary actions are pills.** Get the app, Give Flighty a try, and Try it for free are all pills. The purple fill belongs to the Pro button. See [pricing-light-default.png](screenshots/pricing-light-default.png).
- **Get the app is a dialog, not a form.** It shows a QR code and an App Store link. Do not draw an email field there. See [home-light-get-app.png](screenshots/home-light-get-app.png).
- **Do not style a signed-in app from this package.** The site has no web login. `/login` is the 404 in [login-404-light-default.png](screenshots/login-404-light-default.png).

## Rebuild

```bash
cd systems/flighty
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/build_components_md.py
```

`make brief`, `make design-md`, and `make grade` need a catalog entry. This PR does not add one.
