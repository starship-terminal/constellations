# Jira

Jira is Atlassian's project tracker (www.atlassian.com/software/jira). This package is the public marketing site, captured signed out on 2026-11-22. Themes: light only. Widths: 1440 by 900 and 390 by 844. No account was used. No site was created.

The public site tree, dated 2026-11-22, is [site-tree.md](site-tree.md). Sign in and signup were opened empty and photographed. `catalog.json` was left alone. `login-extracted` stays not-started. `systems/atlassian` was not touched.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Header, footer, and the public links they open, dated 2026-11-22 |
| [DESIGN.md](DESIGN.md) | Pointer. Not generated, because catalog.json was left alone |
| [tokens.json](tokens.json) | Declared colours, type, and spacing |
| [style-guide.html](style-guide.html) | Swatches from those tokens |
| [components.md](components.md) | Public controls and the shots that show them |
| [patterns.md](patterns.md) | Homepage, menus, pricing, and the empty walls |
| [login-review.json](login-review.json) | Empty sign-in and signup walls. `loginExtracted` is not-started |
| [icon.png](icon.png) | 128 px PNG. A drawn stand-in of the public mark |
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

The homepage was opened signed out. Custom properties were parsed from the three public stylesheets linked from the page and resolved on `:root`. `getComputedStyle` was read on the body, the homepage h1, and the Get it free link. Screenshots were not sampled for colour.

Screenshots are the first viewport from headless Chromium at device pixel ratio 2, then quantised to 256 colours. A cookie banner was hidden with CSS. Accept all and Reject all were not clicked on the marketing pages. The signup recapture also hid the banner with CSS.

## What to distrust

The homepage h1 is Charlie Display at 64px. Declared AtlasKit heading roles use Atlassian Sans. Both are in the tokens. Do not treat the declared heading role as the hero size.

Get it free computed a 10000px radius, a pill. Hover and pressed blues are declared. They were not photographed.

Charlie Display and Charlie Text are proprietary and are not in this package. Tokens name them and fall back to the system stack.

The mark in `icons/mark.svg` and `icon.png` is a drawn stand-in. It is not the extracted logo.

No dark theme was painted. `color-scheme` on the homepage was `light`.

The hero board is a public demo of a sample project. It is not a signed-in Jira site.

Impressum was discarded. Do not treat a missing impressum image as a missing page. The page painted a street address and a phone number, so the image was not kept.

## Fonts

| Family | Where | Licence |
|---|---|---|
| Charlie Display | Homepage h1 | Proprietary. Not committed |
| Charlie Text | Body | Proprietary. Not committed |
| Atlassian Sans | Declared AtlasKit heading and body roles | Proprietary. Not committed. Tokens fall back to ui-sans-serif |

## Coverage

| Checklist | Status |
|---|---|
| Colour roles | Captured in light from declared custom properties. [raw/css-vars.json](raw/css-vars.json) |
| Dark theme | Not present on the homepage |
| Type roles | Hero measured. Declared heading and body roles captured |
| Spacing, radii | Declared space steps captured. Pill radius measured on Get it free |
| Elevation | Declared overlay and raised shadows captured. Not photographed |
| Motion | Not captured |
| Button | Get it free and Sign up, default only. [home-light-1440](screenshots/home-light-1440.png) |
| Button hover, focus, pressed | Not captured. Hover and pressed blues are declared only |
| Link | Sign in, text, blue. Same shot |
| Text field | Homepage work-email field, empty, not submitted. Sign-in email field, empty |
| Text area, select, checkbox, radio, switch | Remember me checkbox on the sign-in wall. Others not measured |
| Menu | Features, Solutions, and Templates panels. Phone drawer |
| Dialog | Signup wall is a dialog over a greyed product demo |
| Card | Pricing plan cards. [pricing-light-1440](screenshots/pricing-light-1440.png) |
| App shell | Marketing header and footer. The account was not opened |
| Form validation | Not captured. No form was submitted |
| Checkout, subscribe, signed-in account | Not captured. Stopped at login, signup, trial, and subscribe |

The public walk is [site-tree.md](site-tree.md). catalog.json was left alone. `login-extracted` stays not-started.

## Do and don't

1. **Do paint the page white and the text near-black.** Page is `#ffffff`. Hero text is `#101214`. See [home-light-1440](screenshots/home-light-1440.png).
2. **Do set the hero in Charlie Display.** The heading is 64px, weight 500, letter-spacing -1.28px. Same shot.
3. **Do make the primary action a blue pill.** Get it free is `#1868db` with white text, 40px tall, radius 10000px. Same shot.
4. **Do keep Sign in as text.** It sits beside the pill, not inside a second button. Same shot.
5. **Don't invent a dark theme.** The public homepage did not paint one.
6. **Don't treat the hero board as a signed-in product.** It is a public demo.
7. **Don't submit Sign up, Continue, or a trial from this package.** All three were left alone.

## Rebuild

Tokens were written from [raw/css-vars.json](raw/css-vars.json). From the repo root, after a catalog entry exists:

```bash
make design-md
make grade
make check
```

`catalog.json` was left alone, so those commands were not run for this package.
