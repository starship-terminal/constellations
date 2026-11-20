# Trip.com design reference

A token set and page reference for Trip.com's public site. Read from **www.trip.com**, which geo-redirected to **sg.trip.com** (`?locale=en-sg`), on **2026-11-21**, signed out, in headed Chrome (Playwright `channel: 'chrome'`, headless) at 1440×900 and 390×844. Headless Chromium is sent to a verification captcha and was not used. No account was created. No form was submitted. Google, Apple, and Facebook were not clicked.

The look is a white page, Trip Geom, and one blue (`#2c61fe`, `--smtcColorBgBrand` / `--coreColorBrandingBlue`) for Search and the logo wordmark. The orange brand mark is `#ffb400`. Product pages use a photo hero and a white search card. There is no dark theme on the public shell.

| File | What it is |
|---|---|
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or dialog, mapped before screenshots |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` (colour ramps, Trip Geom, radius, spacing, weights) and `light` (smtc semantic colours and button component tokens). Every token has `$extensions.source`. No dark set. |
| [DESIGN.md](DESIGN.md) | Not generated. catalog.json was not edited, and `make design-md` writes DESIGN.md from a catalog entry. |
| [style-guide.html](style-guide.html) | Renders the measured semantic colours, the blue ramp, radius, spacing, and the Search button. |
| [components.md](components.md) | Component inventory and gaps. No crops. |
| [patterns.md](patterns.md) | Shell, search, sign-in wall, language dialog, support. |
| [screenshots/](screenshots) | 23 quantised captures. Desktop 1440×900 at 1×. Phone shots are 780×1688 (390×844 at 2×). |
| [raw/](raw) | CSSOM custom properties (`css-vars.json`, 931 declarations, 926 resolved). |
| [tools/](tools) | Capture kit and the token and style-guide builders. |

## Brief

Trip.com's public site is a light travel marketplace. Brand blue `#2c61fe` is the only action colour. Type is Trip Geom. Radius on the Search button is 4px; cards use 8px and 12px. Take values from [tokens.json](tokens.json).

## Health

Not graded. catalog.json was not edited, so `make grade` cannot write a Health section for this package.

## How the values were read

[tools/capture/public/public.mjs](tools/capture/public/public.mjs) loaded public routes in headed Chrome. A separate probe walked `document.styleSheets` on the homepage and wrote every `--*` declaration and its computed value to [raw/css-vars.json](raw/css-vars.json). Five cross-origin sheets were unreadable to the CSSOM and are not in that file. [tools/build_tokens.py](tools/build_tokens.py) maps `--coreColor*`, `--coreBorderRadius*`, `--coreSpacing*`, `--coreFont*`, `--smtcColor*`, and a subset of `--compButton*` into tokens.json. Screenshots were quantised to 256 colours. Read colours from the tokens, not the images.

The language suggestion (`.online-language-match`) was hidden with CSS, never clicked. Search was not submitted. The sign-in dialog was opened and closed. Find bookings was opened only far enough to see the auth wall, then left.

## What to distrust

- **SG mirror.** Content, currency (SGD), and the suggested language are Singapore-market. The token names are the site's own.
- **Phone type scale.** Several `--smtcFontSize*` values resolve at 22–36px. Those are the declared mobile scale, not the 14–16px desktop UI. Desktop body size was measured on the Search button: 16px / 24px, weight 700, family Trip Geom.
- **No dark theme.** Two names contain "Dark" (`--coreTripBestBrownDark`, `--coreTripBestGoldA16Dark`). They are palette steps, not a theme.
- **Sign-in screenshot shows social buttons.** They were not clicked. The email field is empty.
- **Train page omitted.** The public trains form arrived with station names filled in. That PNG was deleted so no location string is in the package.
- **Quantised images.** Flat UI colours survive. Read values from tokens.json.

## Fonts

**Trip Geom** (Regular 400, Medium 500, Bold 700) is self-hosted by Trip.com. `--coreFontFamilySans` is `"Trip Geom"`. The style guide falls back to the system sans. Trip Geom is not committed.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Colour roles | captured | `light.color.*` from `--smtcColor*` |
| Type | partly | Family and weights captured. Desktop sizes measured on Search (16px) and the hero (40px/700). The `--smtcFontSize*` scale is the declared mobile scale. |
| Spacing, radii | captured | `core.spacing`, `core.radius` |
| Elevation | Not captured | No shadow custom properties in the CSSOM reading |
| Motion | Not captured | No duration or easing custom properties in the CSSOM reading |
| Button, link | captured | Search, Sign in/register, Claim all, in the screenshots |
| Text field | captured | Where to?, Leaving from, Going to. Not typed. Not submitted. |
| Radio, checkbox | captured | Flights radios and Direct checkbox |
| Tabs | captured | Product tabs, support chips |
| Dialog | captured | Currency dialog, sign-in dialog |
| Menu | captured | Phone menu |
| Card, badge | captured | Coupon cards, 1 night pill |
| Text area, select, switch, tooltip, toast, table, avatar | not present | Not on the public pages captured |
| Hover, focus-visible, pressed, disabled, loading, error | Not captured | Disabled button colours are declared (`--compButtonDisabled*`) and not painted in these shots |
| App shell | captured | [patterns.md](patterns.md) |
| Form validation, empty, loading, error, destructive, onboarding | Not captured | No form submitted. No such state seen. |
| Search submitted | Not captured | Search was not clicked |
| Themes | light only | No dark toggle |
| Widths 1440 and 390 | captured | Desktop shots 1440×900. Phone shots 780×1688 from a 390×844 viewport at 2× |
| Auth | stopped | `/account/signin` and `/passport/ordersearch/` are walls. Continue with Google was not clicked. |

## Do and don't

1. **Do use brand blue for the action that runs a search.** `#2c61fe` on Search. See [home-light-default](screenshots/home-light-default.png).
2. **Do keep the page white and the hero photographic.** Product pages put a white search card over a photo. See [hotels-light-default](screenshots/hotels-light-default.png).
3. **Do use 4px radius on the primary button and 8–12px on cards.** `core.radius.s` is 4px, `core.radius.m` is 8px, `core.radius.l` is 12px.
4. **Don't invent a dark theme.** The public shell does not paint one.
5. **Don't submit search or sign-in to match this package.** Those branches were not taken.
6. **Don't treat the trains form as evidence.** It was omitted because it arrived with station names filled in.

## Rebuild

```sh
cd systems/trip
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/public/public.mjs
python3 tools/capture/quantize.py ~/.design-systems/trip/raw-shots
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

catalog.json was intentionally not edited. `make design-md` and `make grade` need a catalog entry and were not run.
