# Datadog

Datadog is an observability and security product (www.datadoghq.com). This package is the public marketing site, captured signed out on 2026-11-22. Themes: light only. Widths: 1440 by 900 and 390 by 844. No account was used. No trial was started.

The public site tree, dated 2026-11-22, is [site-tree.md](site-tree.md). Login and the signup modal were opened empty and photographed. `catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` stays not-started.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Header, footer, and the public links they open, dated 2026-11-22 |
| [DESIGN.md](DESIGN.md) | Pointer. Not generated, because catalog.json was left alone |
| [tokens.json](tokens.json) | Declared colours, type, and spacing |
| [style-guide.html](style-guide.html) | Swatches from those tokens |
| [components.md](components.md) | Public controls and the shots that show them |
| [patterns.md](patterns.md) | Homepage, menus, pricing, and the empty walls |
| [login-review.json](login-review.json) | Empty login and signup walls. `loginExtracted` is not-started |
| [icon.png](icon.png) | 128 px PNG. A drawn stand-in, not the extracted logo |
| [components/crops/](components/crops) | Empty. Crops were not cut |
| [screenshots/](screenshots) | 182 first-viewport shots of the public pages |
| [icons/](icons) | A drawn mark and [INDEX.tsv](icons/INDEX.tsv) |
| [raw/](raw) | [css-vars.json](raw/css-vars.json) and [components-computed.json](raw/components-computed.json) |
| [tools/](tools) | How the shots were made |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

The homepage was opened signed out. Custom properties were read from `getComputedStyle` on `:root` after the public stylesheets loaded. Empty custom properties were dropped. `getComputedStyle` was also read on the h1, Free trial, See the platform, Login, and Get started free. Screenshots were not sampled for colour.

Screenshots are the first viewport from headless Chromium at device pixel ratio 2, then quantised to 256 colours. A cookie banner was hidden with CSS. Accept and reject were not clicked.

## What to distrust

The hero is NationalWeb at 68px, weight 600. Declared Bootstrap body size is not the hero size. Both are in the tokens.

Free trial computed a 4px radius, 54px tall, fill `#632ca6`. Hover and pressed were not photographed.

NationalWeb is proprietary and is not in this package. Tokens fall back to Helvetica, Arial, sans-serif.

The mark in `icons/mark.svg` and `icon.png` is a drawn stand-in. It is not the extracted logo.

No dark theme was painted on the marketing site. `color-scheme` on the homepage was `normal`. The login wall paints a dark geometric background. That is the login page, not a theme toggle.

The homepage is a public marketing page, not a signed-in Datadog account.

Contact was not kept. Do not treat a missing contact image as a missing page. The page prints a phone number, so it was left out.

A language cookie sent some first fetches to `/ko/`. Those shots were discarded and retaken on the English URL.

## Fonts

| Family | Where | Licence |
|---|---|---|
| NationalWeb | Homepage h1, body, Free trial, Login | Proprietary. Not committed. Tokens fall back to Helvetica, Arial, sans-serif |

## Coverage

| Checklist | Status |
|---|---|
| Colour roles | Captured in light from declared custom properties. [raw/css-vars.json](raw/css-vars.json) |
| Dark theme | Not present on the marketing page. The login wall is dark |
| Type roles | Hero measured. Body and button sizes measured |
| Spacing, radii | Control height and 4px radius measured on Free trial |
| Elevation | Not captured |
| Motion | Not captured |
| Button | Free trial and See the platform, default only. [home-light-1440](screenshots/home-light-1440.png) |
| Button hover, focus, pressed | Not captured |
| Link | Login, text, gray. Same shot |
| Text field | Login username and password, empty. Signup email, name, company, password, phone, empty |
| Select | Signup region, not changed |
| Text area, checkbox, radio, switch | Not measured |
| Menu | Product, Solutions, About, Blog, and the phone drawer |
| Dialog | Signup wall is a modal. Not submitted |
| Card | Pricing. [pricing-light-1440](screenshots/pricing-light-1440.png) |
| App shell | Marketing header and footer. The account was not opened |
| Form validation | Not captured. No form was submitted |
| Checkout, subscribe, signed-in account | Not captured. Stopped at login and signup |

The public walk is [site-tree.md](site-tree.md). catalog.json was left alone. `login-extracted` stays not-started.

## Do and don't

1. **Do paint the page white and the text near-black.** Page is `#ffffff`. Hero text is `#212529`. See [home-light-1440](screenshots/home-light-1440.png).
2. **Do set the hero in NationalWeb.** The heading is 68px, weight 600, line height 68px. Same shot.
3. **Do make the primary action a purple rectangle.** Free trial is `#632ca6` with white text, 54px tall, radius 4px. Same shot.
4. **Do keep Login as text.** It sits beside Get started free, not inside a second button. Same shot.
5. **Don't invent a marketing dark theme.** The public page did not paint one. The login wall is a separate dark page.
6. **Don't treat the homepage as a signed-in Datadog account.** It is a public marketing page.
7. **Don't submit Sign up, Log in, or Get started free from this package.** All three were left alone.

## Rebuild

Tokens were written from [raw/css-vars.json](raw/css-vars.json). From the repo root, after a catalog entry exists:

```bash
make design-md
make grade
make check
```

`catalog.json` was left alone, so those commands were not run for this package.
