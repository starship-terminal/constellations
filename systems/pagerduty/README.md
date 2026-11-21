# PagerDuty

PagerDuty is an operations platform (www.pagerduty.com). This package is the public marketing site, captured signed out on 2026-11-22. Themes: light only. Widths: 1440 by 900 and 390 by 844. No account was used. No trial was started.

The public site tree, dated 2026-11-22, is [site-tree.md](site-tree.md). Log In and Start for Free were opened empty and photographed. `catalog.json` was left alone. `login-extracted` stays not-started.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Header, footer, and the public links they open, dated 2026-11-22 |
| [DESIGN.md](DESIGN.md) | Pointer. Not generated, because catalog.json was left alone |
| [tokens.json](tokens.json) | Measured colours, type, and radii |
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

The homepage was opened signed out. Custom properties were read from `:root` after the public stylesheets loaded. `getComputedStyle` was read on the body, the homepage h1, the Start for Free link, and the Log In link. Screenshots were not sampled for colour.

Screenshots are the first viewport from headless Chromium at device pixel ratio 2, then quantised to 256 colours. A cookie banner was hidden with CSS. Accept and Reject were not clicked.

## What to distrust

The homepage h1 is white because it sits on a dark campaign hero. Body text is `#1d1d1d`. Do not treat the hero colour as the page text colour.

Start for Free computed `#048a24`, 48px tall, radius 100px. Hover and pressed greens are declared as `--color-green-dark`. They were not photographed.

plainFont is proprietary and is not in this package. Tokens name it and fall back to Helvetica Neue, Arial, sans-serif.

The mark in `icons/mark.svg` and `icon.png` is a drawn stand-in. It is not the extracted logo.

No dark theme was painted. `color-scheme` on the homepage was `light`.

Contact Us was discarded. Do not treat a missing contact image as a missing page. The page printed a sales phone number, so the image was not kept. Privacy policy printed a street address and was discarded the same way. Request a demo is a contact form and was discarded. The public status page printed a live clock and was discarded.

## Fonts

| Family | Where | Licence |
|---|---|---|
| plainFont | Homepage h1, body, header | Proprietary. Not committed. Tokens fall back to Helvetica Neue, Arial, sans-serif |

## Coverage

| Checklist | Status |
|---|---|
| Colour roles | Captured in light from computed custom properties and the header buttons. [raw/css-vars.json](raw/css-vars.json) |
| Dark theme | Not present on the homepage. The hero is a dark campaign on a light page |
| Type roles | Hero and body measured |
| Spacing, radii | Pill radius measured on Start for Free and Log In. Declared `--radius-md` captured |
| Elevation | Not captured |
| Motion | Not captured |
| Button | Start for Free, default only. [home-light-1440](screenshots/home-light-1440.png) |
| Button hover, focus, pressed | Not captured |
| Link | Pricing, text, near-black. Same shot |
| Text field | Sign-in email field, empty. Signup work-email field, empty |
| Text area, select, checkbox, radio, switch | Two unchecked boxes on the signup wall. Others not measured |
| Menu | Products, Solutions, Company, Resources. Phone drawer |
| Dialog | Signup wall is a card over a green illustration |
| Card | Pricing plan cards. [pricing-light-1440](screenshots/pricing-light-1440.png) |
| App shell | Marketing header and footer. The account was not opened |
| Form validation | Not captured. No form was submitted |
| Checkout, subscribe, signed-in account | Not captured. Stopped at login, signup, and contact forms |

The public walk is [site-tree.md](site-tree.md). catalog.json was left alone. `login-extracted` stays not-started.

## Do and don't

1. **Do paint the page pale grey and the header white.** Page background is `#fafafa`. See [home-light-1440](screenshots/home-light-1440.png).
2. **Do set the hero in plainFont at 60px, weight 300.** The heading is white on a dark green campaign. Same shot.
3. **Do make the primary action a green pill.** Start for Free is `#048a24` with white text, 48px tall, radius 100px. Same shot.
4. **Do keep Log In as an outlined pill.** It has a 2px `#1d1d1d` border and a transparent fill. Same shot.
5. **Don't invent a dark theme.** The public homepage did not paint one.
6. **Don't treat the hero booth as a signed-in product.** It is a campaign for AWS re:Invent.
7. **Don't submit Next, Continue, or Start Free Trial from this package.** All three were left alone.

## Rebuild

Tokens were written from [raw/css-vars.json](raw/css-vars.json) and [raw/components-computed.json](raw/components-computed.json). From the repo root, after a catalog entry exists:

```bash
make design-md
make grade
make check
```

`catalog.json` was left alone, so those commands were not run for this package.
