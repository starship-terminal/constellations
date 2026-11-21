# Letterboxd design reference

A token set and page reference for Letterboxd's public, signed-out site. It was read from [letterboxd.com](https://letterboxd.com) on 2026-11-21, signed out, in headless Chromium at 1440 x 900 and 390 x 844. Captured: the homepage, films, a public film, lists, a public list, members, journal, about, Pro, apps, contact, welcome, a missing page, and the empty sign-in and create-account walls. Phone passes cover the homepage, its menu, and the film page. The site tree is [site-tree.md](site-tree.md). The empty login review is [login-review.json](login-review.json). `login_extracted` is `not-started`.

The site paints one dark field: `#14181c` page, `#9ab` body text, `#00e054` green, `#40bcf4` blue, `#ff8000` orange, set in Graphik with Tiempos for headlines. Sign-in, create-account, and reset password were not submitted. No identity provider was clicked. A Turnstile challenge that appeared once in headless Chromium was not solved.

| File | What it is |
|---|---|
| [icon.png](icon.png) | The site icon, 128 px, resized from the published favicon |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds Graphik and Tiempos, the type sizes, spacing, radii, and durations. `light` holds the colour roles of the one dark field. `dark` is empty. Every token carries `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. `catalog.json` was left alone, so `make design-md` was not run. |
| [style-guide.html](style-guide.html) | One page that renders the tokens |
| [components.md](components.md) | The controls the public site shows, with the screenshots that hold them |
| [patterns.md](patterns.md) | How the header, film page, list, Pro page, and phone menu combine |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or dialog, mapped from the homepage |
| [login-review.json](login-review.json) | Empty sign-in and create-account walls. `login_extracted` is `not-started` |
| [screenshots/](screenshots) | Quantised page captures. Desktop 1440 x 900. Phone viewport shots are 2x captures of 390 x 844. |
| [raw/](raw) | Unprocessed readings: [css-vars.json](raw/css-vars.json), [harvest.json](raw/harvest.json) |
| [tools/](tools) | The builders and the capture kit |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

| Step | What ran |
|---|---|
| Site tree | A preview tab on the homepage, then films, sign-in, and create-account. Controls recorded, not submitted. |
| Screenshots | `tools/capture/public/public.mjs` at 1440 x 900 and 390 x 844. |
| CSS harvest | `tools/capture/harvest.mjs` on the homepage. 345 custom properties resolved on `:root`. |
| Tokens | `tools/build_tokens.py` from `raw/css-vars.json`. |
| Guide | `tools/build_style_guide.py`. |

On 2026-11-21 the homepage was mapped before the screenshot pass. Search was left empty. The phone menu was opened. Sign-in and create-account were photographed empty. Nothing was typed or submitted.

## What to distrust

The set is named `light` because the catalog expects that name. The product does not paint a light theme. `dark` is empty on purpose.

`--duration-short` is `calc(1s * 1 / 3)`. The token stores `333ms`.

`--theme-button-destructive-outline-border-color` uses `rgb(from …)`. That value was not exported. The danger role is the destructive button surface, `#c40f00`.

Search focus was not recaptured after a Turnstile dialog blocked one headless click. The field's resting metrics are in [raw/harvest.json](raw/harvest.json).

Public film and list pages show other people's public display names. That is the site's public content. No signed-in session was used.

## Fonts

GraphikWeb (300, 400, 700, 800) and Tiempos Headline / Tiempos Text. Both are commercial faces served as woff2. They are named in the tokens and not shipped. The style guide falls back to the system sans and Georgia.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured in [tokens.json](tokens.json) `light`. One dark field. |
| Type | Graphik and Tiempos, heading and body sizes. [tokens.json](tokens.json) `core.font`. |
| Spacing, radii, duration | Captured from custom properties. |
| Elevation | Poster shadow radii captured. No multi-level shadow scale. |
| Button, link, text field, checkbox, menu, dialog, card, list row, tabs, badge | Seen on the public pages. See [components.md](components.md). |
| Text area, select, radio, switch, tooltip, toast, table | Not present on the signed-out surface. |
| Hover, focus-visible, pressed, disabled, loading, error | Not forced, except the missing-page still. |
| Empty sign-in and signup | [signin-light-default](screenshots/signin-light-default.png), [signup-light-default](screenshots/signup-light-default.png). |
| Missing page | [missing-light-default](screenshots/missing-light-default.png). |
| Desktop 1440 and phone 390 | Homepage and film. |
| Signed-in app | Not captured. `login_extracted` is `not-started`. |

## Do and don't

1. **Do keep the field `#14181c`.** The homepage, film page, and sign-in card sit on that colour. See [home-light-default](screenshots/home-light-default.png).
2. **Do spend green on the primary action.** Get started and Sign in are `#00ac1c`. See [home-light-default](screenshots/home-light-default.png) and [signin-light-default](screenshots/signin-light-default.png).
3. **Do set headlines in a serif and chrome in Graphik.** Film titles are Tiempos. Nav is uppercase Graphik. See [film-light-default](screenshots/film-light-default.png).
4. **Do keep the three brand dots on the wordmark.** Orange, green, blue. See [home-light-default](screenshots/home-light-default.png).
5. **Don't invent a light theme.** The public site does not switch.
6. **Don't submit sign-in or create-account from this reference.** Both walls were left empty. See [signup-light-default](screenshots/signup-light-default.png).

## Rebuild

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/harvest.mjs
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/capture/quantize.py ~/.design-systems/letterboxd/raw-shots screenshots
```

`catalog.json` was not edited. Do not run `make design-md` for this package until it is registered.
