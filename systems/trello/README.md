# Trello

Trello is a visual work-management product (trello.com). This package is the public marketing site, captured signed out on 2026-11-22. Themes: light only. Widths: 1440 by 900 and 390 by 844. No account was used.

The public site tree, dated 2026-11-22, is [site-tree.md](site-tree.md). Login and signup are Atlassian walls. They were opened empty and the screenshots were discarded because the painted URLs carry session state. `catalog.json` was left alone. `login-extracted` stays not-started.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Header, footer, and the public links they open, dated 2026-11-22 |
| [DESIGN.md](DESIGN.md) | Pointer. Not generated, because catalog.json was left alone |
| [tokens.json](tokens.json) | Measured colours, type, and radius |
| [style-guide.html](style-guide.html) | Swatches from those tokens |
| [components.md](components.md) | Public controls and the shots that show them |
| [patterns.md](patterns.md) | Homepage, menus, pricing, and public pages |
| [login-review.json](login-review.json) | Empty login and signup walls. Screenshots discarded. `loginExtracted` is not-started |
| [icon.png](icon.png) | 128 px PNG from the site favicon |
| [components/crops/](components/crops) | Empty. Crops were not cut |
| [screenshots/](screenshots) | First-viewport shots of the public pages |
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

The homepage was opened signed out. Custom properties were parsed from the stylesheets. `getComputedStyle` was read on the body, the homepage h1, the Pricing link, the header Get Trello for free control, the email field, and the Sign up button. Screenshots were not sampled for colour.

Screenshots are the first viewport from headless Chromium at device pixel ratio 2, then quantised to 256 colours. A cookie banner (`#onetrust-consent-sdk`) was hidden with CSS. Accept all and Preferences were not clicked.

## What to distrust

The header Get Trello for free control computed a square radius. The homepage Sign up button computed 4.8px. Both fills are `#0065ff`. Do not treat them as one control.

Charlie Text and Charlie Display are proprietary and are not in this package. Tokens fall back to ui-sans-serif, system-ui, sans-serif.

The wordmark in `icons/mark.svg` is a drawn stand-in. It is not the extracted logo. `icon.png` is the site favicon, resized to 128 px.

No dark theme was painted. `color-scheme` on the homepage was `normal`.

The sign-in and signup screenshots were discarded. Do not treat a missing login image as a missing wall. The walls painted, and their URLs were not safe to keep.

`/webinars` redirects to `/home`. `/contact` ends on an Atlassian login wall. The footer Notice at Collection href was empty.

## Fonts

| Family | Where | Licence |
|---|---|---|
| Charlie Display | Homepage h1 | Proprietary. Not committed. Tokens fall back to ui-sans-serif, system-ui, sans-serif |
| Charlie Text | Body, nav, buttons | Proprietary. Not committed. Tokens fall back to ui-sans-serif, system-ui, sans-serif |

## Coverage

| Checklist | Status |
|---|---|
| Colour roles | Captured in light from computed styles and declared custom properties. [raw/css-vars.json](raw/css-vars.json) |
| Dark theme | Not present on the homepage |
| Type roles | Hero and body captured. Other roles not measured |
| Spacing, radii | Field and button radius captured. Spacing scale not measured |
| Elevation | Not measured |
| Motion | Not captured |
| Button | Header Get Trello for free and homepage Sign up, default only |
| Button hover, focus, pressed | Not captured |
| Link | Pricing, 16px, `#172b4d`. Learn more, `#0052cc` |
| Text field | Homepage email field, empty, not submitted. Login email and password fields, empty, screenshot discarded |
| Text area, select, checkbox, radio, switch | Not measured |
| Menu | Features, Solutions, Plans, Resources, and the phone drawer |
| Dialog | Cookie banner hidden, not accepted |
| Card | Pricing plan cards |
| App shell | Marketing header and footer. The account was not opened |
| Form validation | Not captured. No form was submitted |
| Checkout, subscribe, signed-in account | Not captured. Stopped at login, signup, and the contact login wall |

The public walk is [site-tree.md](site-tree.md). catalog.json was left alone. `login-extracted` stays not-started.

## Do and don't

1. **Do paint the page white and the text navy.** Page is `#ffffff`. Text is `#091e42`. See [home-light-1440](screenshots/home-light-1440.png).
2. **Do set the hero in Charlie Display.** The heading is 48px, weight 500, line-height 60px. Same shot.
3. **Do make the signup action a blue button.** Sign up is `#0065ff` with white text and a 4.8px radius. Same shot.
4. **Do keep the header control square.** Get Trello for free is the same blue with a 0 radius. Same shot.
5. **Don't invent a dark theme.** The public homepage did not paint one.
6. **Don't treat the discarded sign-in shot as a gap in the product.** The wall painted. Its URL carried session state, so the image was not kept.
7. **Don't submit the email field or create a board from this package.** Both were left alone.

## Rebuild

Tokens were written from computed styles on [https://trello.com/](https://trello.com/) and from [raw/css-vars.json](raw/css-vars.json). From the repo root, after a catalog entry exists:

```bash
make design-md
make grade
make check
```

`catalog.json` was left alone, so those commands were not run for this package.
