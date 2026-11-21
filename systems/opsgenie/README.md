# Opsgenie

Opsgenie is Atlassian's alerting and on-call product (www.atlassian.com/software/opsgenie). This package is the public marketing site, captured signed out on 2026-11-22. The product URL 301s to a migration page. Themes: light only. Widths: 1440 by 900 and 390 by 844. No account was used. No site was created.

The public site tree, dated 2026-11-22, is [site-tree.md](site-tree.md). Sign in, the product login, and the signup redirect were opened empty and photographed. `catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` stays not-started. `systems/atlassian` was not touched.

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
| [icon.png](icon.png) | 128 px PNG. A drawn stand-in, not the extracted logo |
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

The migration page was opened signed out. Custom properties were parsed from the three public stylesheets linked from the page and resolved on `:root`. `getComputedStyle` was read on the h1, the body, Plan your migration, and Sign in. Screenshots were not sampled for colour.

Screenshots are the first viewport from headless Chromium at device pixel ratio 2, then quantised to 256 colours. A cookie banner was hidden with CSS. Accept all and Reject all were not clicked.

## What to distrust

The migration h1 is Charlie Display at 48px, weight 800. Declared AtlasKit heading roles use Atlassian Sans. Both are in the tokens. Do not treat the declared heading role as the hero size.

Plan your migration computed a 10000px radius, a pill, 48px tall. Hover and pressed blues are declared. They were not photographed.

Charlie Display, Charlie Text, and Atlassian Sans are proprietary and are not in this package.

The mark in `icons/mark.svg` and `icon.png` is a drawn stand-in. It is not the extracted logo.

No dark theme was painted. `color-scheme` on the migration page was `light`.

The homepage is a migration guide, not a signed-in Opsgenie account. Pricing says new signups and sales have ended. Several old feature URLs now redirect to Jira Service Management.

Impressum was not opened. Do not treat a missing impressum image as a missing page. The page prints a street address and a phone number, so it was left out.

## Fonts

| Family | Where | Licence |
|---|---|---|
| Charlie Display | Migration h1 | Proprietary. Not committed |
| Charlie Text | Plan your migration, Sign in | Proprietary. Not committed |
| Atlassian Sans | Declared AtlasKit heading and body roles | Proprietary. Not committed. Tokens fall back to ui-sans-serif |

## Coverage

| Checklist | Status |
|---|---|
| Colour roles | Captured in light from declared custom properties. [raw/css-vars.json](raw/css-vars.json) |
| Dark theme | Not present on the migration page |
| Type roles | Hero measured. Declared heading and body roles captured |
| Spacing, radii | Declared space steps captured. Pill radius measured on Plan your migration |
| Elevation | Declared overlay and raised shadows captured. Not photographed |
| Motion | Not captured |
| Button | Plan your migration, default only. [home-light-1440](screenshots/home-light-1440.png) |
| Button hover, focus, pressed | Not captured. Hover and pressed blues are declared only |
| Link | Sign in, text, near-black. Same shot |
| Text field | Sign-in email and password, empty. Signup work email, empty. Product login email, empty |
| Text area, select, checkbox, radio, switch | Remember me checkbox on the Atlassian sign-in wall. Others not measured |
| Menu | Products, AI, Solutions, Why Atlassian, Resources panels |
| Dialog | Signup wall is a page, not a dialog. Get it free on the shared bar did not open one |
| Card | Pricing plan cards. [pricing-light-1440](screenshots/pricing-light-1440.png) |
| App shell | Marketing header, product bar, and footer. The account was not opened |
| Form validation | Not captured. No form was submitted |
| Checkout, subscribe, signed-in account | Not captured. Stopped at login, signup, contact, and subscribe |

The public walk is [site-tree.md](site-tree.md). catalog.json was left alone. `login-extracted` stays not-started.

## Do and don't

1. **Do paint the page white and the text near-black.** Page is `#ffffff`. Hero text is `#292a2e`. See [home-light-1440](screenshots/home-light-1440.png).
2. **Do set the hero in Charlie Display.** The heading is 48px, weight 800, line height 56px. Same shot.
3. **Do make the primary action a blue pill.** Plan your migration is `#1868db` with white text, 48px tall, radius 10000px. Same shot.
4. **Do keep Sign in as text.** It sits beside Get it free, not inside a second button. Same shot.
5. **Don't invent a dark theme.** The public page did not paint one.
6. **Don't treat the migration page as a signed-in Opsgenie account.** It is a public guide. New signups have ended.
7. **Don't submit Sign up, Continue, Next, or Contact sales from this package.** All four were left alone.

## Rebuild

Tokens were written from [raw/css-vars.json](raw/css-vars.json). From the repo root, after a catalog entry exists:

```bash
make design-md
make grade
make check
```

`catalog.json` was left alone, so those commands were not run for this package.
