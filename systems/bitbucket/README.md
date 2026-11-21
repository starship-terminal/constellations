# Bitbucket

Bitbucket is a code and CI/CD product (bitbucket.org). This package is the public marketing site, captured signed out on 2026-11-22. Themes: light only. Widths: 1440 by 900 and 390 by 844. No account was used.

The public site tree, dated 2026-11-22, is [site-tree.md](site-tree.md). Login and signup are Atlassian walls. They were opened empty and the screenshots were discarded because the painted URLs carry session state. `catalog.json` was left alone. `login-extracted` stays not-started.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Header, footer, and the public links they open, dated 2026-11-22 |
| [DESIGN.md](DESIGN.md) | Pointer. Not generated, because catalog.json was left alone |
| [tokens.json](tokens.json) | Measured colours, type, and radius |
| [style-guide.html](style-guide.html) | Swatches from those tokens |
| [components.md](components.md) | Public controls and the shots that show them |
| [patterns.md](patterns.md) | Homepage, menu, pricing, and public pages |
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

The homepage was opened signed out. Custom properties were parsed from the stylesheets. `getComputedStyle` was read on the body, the homepage h1, the Pricing link, the header Get it Free control, the Watch demo link, and Sign in. Button, text, and link colours come from those computed styles. The page fill, the Premium button, and the status bar were sampled from the raw screenshot before quantising, because the homepage background computed as transparent.

Screenshots are the first viewport from headless Chromium at device pixel ratio 2, then quantised to 256 colours. A cookie banner (`#onetrust-consent-sdk`) was hidden with CSS. Accept all and Preferences were not clicked.

## What to distrust

The homepage body background computed as transparent. The painted page is white. Do not treat the computed value as the page colour.

Charlie Text and Charlie Display are proprietary and are not in this package. Tokens fall back to ui-sans-serif, system-ui, sans-serif.

The wordmark in `icons/mark.svg` is a drawn stand-in. It is not the extracted logo. `icon.png` is the site favicon, resized to 128 px.

No dark theme was painted. `color-scheme` on the homepage was `light`.

The sign-in and signup screenshots were discarded. Do not treat a missing login image as a missing wall. The walls painted, and their URLs were not safe to keep.

`/product/pricing` redirects to the Atlassian pricing page. Terms of use and Trust & security land on the same Customer Agreement. `/account/signup/` lands on the login wall.

## Fonts

| Family | Where | Licence |
|---|---|---|
| Charlie Display | Homepage h1 | Proprietary. Not committed. Tokens fall back to ui-sans-serif, system-ui, sans-serif |
| Charlie Text | Body, nav, buttons | Proprietary. Not committed. Tokens fall back to ui-sans-serif, system-ui, sans-serif |

## Coverage

| Checklist | Status |
|---|---|
| Colour roles | Captured in light from computed styles. [raw/components-computed.json](raw/components-computed.json) |
| Dark theme | Not present on the homepage |
| Type roles | Hero and body captured. Other roles not measured |
| Spacing, radii | Button radius captured. Spacing scale not measured |
| Elevation | Not measured |
| Motion | Not captured |
| Button | Header Get it Free and homepage Try it now, default only |
| Button hover, focus, pressed | Not captured |
| Link | Watch demo, 16px, `#1868db` |
| Text field | Header search, empty, not submitted. Login email and password fields, empty, screenshot discarded |
| Text area, select, checkbox, radio, switch | Not measured |
| Menu | Why Bitbucket, and the phone drawer |
| Dialog | Cookie banner hidden, not accepted |
| Card | Pricing plan cards |
| App shell | Marketing header and footer. The account was not opened |
| Form validation | Not captured. No form was submitted |
| Checkout, subscribe, signed-in account | Not captured. Stopped at login, signup, and the try-cloud wall |

The public walk is [site-tree.md](site-tree.md). catalog.json was left alone. `login-extracted` stays not-started.

## Do and don't

1. **Do paint the page white and the heading near black.** Page is `#ffffff`. Heading is `#101214`. See [home-light-1440](screenshots/home-light-1440.png).
2. **Do set the hero in Charlie Display.** The heading is 64px, weight 500, line-height 66.56px, letter-spacing -1.28px. Same shot.
3. **Do make the primary action a blue pill.** Get it Free is `#1868db` with white text and a 10000px radius. Same shot.
4. **Do keep body copy in Charlie Text.** Body is 16px, `#292a2e`. Same shot.
5. **Don't invent a dark theme.** The public homepage did not paint one.
6. **Don't treat the discarded sign-in shot as a gap in the product.** The wall painted. Its URL carried session state, so the image was not kept.
7. **Don't submit a form or create a repository from this package.** Both were left alone.

## Rebuild

Tokens were written from computed styles on [https://bitbucket.org/](https://bitbucket.org/) and from [raw/css-vars.json](raw/css-vars.json). From the repo root, after a catalog entry exists:

```bash
make design-md
make grade
make check
```

`catalog.json` was left alone, so those commands were not run for this package.
