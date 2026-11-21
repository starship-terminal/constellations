# PostHog

PostHog is a product analytics platform (posthog.com). This package is the public marketing site, captured signed out on 2026-11-22. Themes: light. Widths: 1440 by 900 and 390 by 844. No account was used. No org was created.

The public site tree, dated 2026-11-22, is [site-tree.md](site-tree.md). Get started and the login URL were opened empty and photographed. `catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` stays not-started.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Header, footer, and the public links they open, dated 2026-11-22 |
| [DESIGN.md](DESIGN.md) | Pointer. Not generated, because catalog.json was left alone |
| [tokens.json](tokens.json) | Measured colours, type, and radii |
| [style-guide.html](style-guide.html) | Swatches from those tokens |
| [components.md](components.md) | Public controls and the shots that show them |
| [patterns.md](patterns.md) | Homepage, menus, pricing, and the empty walls |
| [login-review.json](login-review.json) | Empty signup and login walls. `loginExtracted` is not-started |
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

The homepage was opened signed out. `getComputedStyle` was read on the h1, the highlighted words in the h1, the Pricing link, and Get started – free. Screenshots were not sampled for colour.

Screenshots are the first viewport from headless Chromium at device pixel ratio 2, then quantised to 256 colours. The cookie banner was left on screen.

## What to distrust

The homepage h1 is 36px, weight 800, RoundHog. That is the measured hero, not a declared type scale. A larger display size was not found on this page.

Get started – free computed weight 400. The pill looks heavier than that. Trust the computed weight.

RoundHog is proprietary and is not in this package. The signup wall also names Inter in its font stack. Inter was not measured on a visible control.

The mark in `icons/mark.svg` and `icon.png` is a drawn stand-in. It is not the extracted logo.

No dark theme was painted. A `.dark` rule exists in the page CSS. `color-scheme` on the homepage was `normal`.

The homepage AI panel is a public demo with sample data. It is not a signed-in account.

## Fonts

| Family | Where | Licence |
|---|---|---|
| RoundHog | Homepage body, h1, header | Proprietary. Not committed |

## Coverage

| Checklist | Status |
|---|---|
| Colour roles | Captured in light from computed styles. [raw/components-computed.json](raw/components-computed.json) |
| Dark theme | Declared in CSS. Not painted |
| Type roles | Hero and nav measured |
| Spacing, radii | Button radius 6px. Nav radius 4px |
| Elevation | Not captured |
| Motion | Not captured |
| Button | Get started – free, default only. [home-light-1440](screenshots/home-light-1440.png) |
| Button hover, focus, pressed | Not captured |
| Link | Pricing, text, `#23251d`. Same shot |
| Text field | Signup and login email, empty. Sales form, empty |
| Select | Data region on the signup wall, closed |
| Text area, checkbox, radio, switch | Not measured |
| Menu | Products, Docs, Community, Company, More |
| Dialog | Search and AI chat were opened and closed. Display options was opened in the preview and closed |
| Card | Setup card on the homepage. Pricing copy in [pricing-light-1440](screenshots/pricing-light-1440.png) |
| App shell | Marketing header and side rail. The account was not opened |
| Form validation | Not captured. No form was submitted |
| Checkout, subscribe, signed-in account | Not captured. Stopped at login, signup, and the sales form |

The public walk is [site-tree.md](site-tree.md). catalog.json was left alone. `login-extracted` stays not-started.

## Do and don't

1. **Do paint the page a warm off-white.** Page is `#eeefe9`. Hero text is `#111827`. See [home-light-1440](screenshots/home-light-1440.png).
2. **Do set the hero in RoundHog.** The heading is 36px, weight 800, line height 40px, letter spacing -0.9px. Same shot.
3. **Do mark the key phrase in blue.** "context layer" is `#2f80fa` on a 10% wash, radius 6px. Same shot.
4. **Do make Get started an amber pill.** Fill `#cd8407`, text `#23251d`, 32px tall, radius 6px. Same shot.
5. **Don't invent a dark theme.** The public page did not paint one.
6. **Don't treat the homepage AI panel as a signed-in account.** It is a public demo with sample data.
7. **Don't submit Continue, Send, or Subscribe from this package.** All three were left alone.

## Rebuild

Tokens were written from computed styles in [raw/components-computed.json](raw/components-computed.json). From the repo root, after a catalog entry exists:

```bash
make design-md
make grade
make check
```

`catalog.json` was left alone, so those commands were not run for this package.
