# Buffer

Buffer is a social media scheduler. This package is the public marketing site at [https://buffer.com/](https://buffer.com/), captured signed out on 2026-11-22. Themes: light only. Widths: 1440 × 900 and 390 × 844. No account was used. Login and signup were photographed empty and then stopped.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Header, footer, and the public links they open, dated 2026-11-22 |
| [DESIGN.md](DESIGN.md) | Generated token export |
| [tokens.json](tokens.json) | Computed colours, type, radius, and spacing |
| [style-guide.html](style-guide.html) | Renders the tokens |
| [components.md](components.md) | Public controls and the shots that show them |
| [patterns.md](patterns.md) | Header, hero, pricing, and the auth walls |
| [login-review.json](login-review.json) | Empty login and signup walls. `loginExtracted` is not-started |
| [components/crops/](components/crops) | Empty. Crops were not cut |
| [screenshots/](screenshots) | First-viewport shots of the public pages and the empty walls |
| [icons/](icons) | A drawn mark and [INDEX.tsv](icons/INDEX.tsv) |
| [raw/](raw) | [css-vars.json](raw/css-vars.json) and [components-computed.json](raw/components-computed.json) |
| [tools/](tools) | The capture kit and a package test |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

The homepage was opened signed out. `getComputedStyle` was read on the body, the hero heading, the brand button span, the email field, and the footer. No custom properties resolved on `:root`. Marketing CSS ships as hashed sheets on `static.buffer.com`.

Screenshots are the first viewport from headless Chromium at device pixel ratio 2. A cookie overlay was hidden with CSS. Its accept and reject buttons were not clicked.

## What to distrust

The brand button's own `a` computed a transparent background. The green fill is the inner span, `rgb(176, 236, 156)`.

The Log in outline is painted on a wrapper. That border colour was not measured.

The hero size 75.8px is the computed size at 1440. It was not remeasured at 390.

The three-bar mark was not extracted. It appears only in the screenshots.

The Insights panel on the signup wall is a marketing illustration. It is not a signed-in inbox.

No dark theme was painted. `color-scheme` on the homepage was `normal`.

## Fonts

| Family | Where | Licence |
|---|---|---|
| Stolzl | Hero, wordmark, muted count | Proprietary. Not committed. Tokens fall back to ui-sans-serif, system-ui, sans-serif |
| Figtree | Body, buttons, fields | Proprietary. Not committed. Same fallback |

## Coverage

| Checklist | Status |
|---|---|
| Colour roles | Captured in light from computed styles. [raw/components-computed.json](raw/components-computed.json) |
| Dark theme | Not present on the homepage |
| Type roles | Hero and body captured. Other roles not measured |
| Spacing, radii | Pill radius and field padding captured. The rest of the scale was not measured |
| Elevation | Email wrapper shadow captured. Other shadows not measured |
| Motion | Not captured |
| Button | Get started for free, default only |
| Button hover, focus, pressed | Not captured |
| Link | Log in, 18px, `#213130` |
| Text field | Homepage email field, empty, not submitted. Login and signup fields, empty |
| Text area, select, checkbox, radio, switch | Not measured on the captured pages |
| Menu | Four desktop panels and the phone drawer |
| Dialog, toast, tooltip | Not opened. Cookie banner was hidden, not accepted |
| Card | Pricing plan cards |
| App shell | Marketing header and footer. The publisher was not opened |
| Form validation | Not captured. No form was submitted |
| Checkout, subscribe, signed-in app | Not captured. Stopped at login and signup |

The public walk is [site-tree.md](site-tree.md). catalog.json was left alone. `login-extracted` stays not-started.

## Do and don't

1. **Do paint the page warm white and the text near-black.** Page is `#fefdfb`. Text is `#213130`. See [home-light-1440](screenshots/home-light-1440.png).
2. **Do set the hero in Stolzl.** The heading is 75.8px, weight 400, letter-spacing -1.516px. Same shot.
3. **Do make the primary action a green pill.** Get started for free is `#b0ec9c` with `#213130` text and a 1440px radius. Same shot.
4. **Do keep the footer the same near-black as the text.** Footer background is `#213130` with white type.
5. **Don't invent a dark theme.** The public homepage did not paint one.
6. **Don't treat the signup illustration as the product.** The Insights panel is marketing art. The publisher was not opened.
7. **Don't submit the email field from this package.** It was empty. Login and signup were stopped.

## Rebuild

Tokens were written from [raw/components-computed.json](raw/components-computed.json). `tools/build_tokens.py` is the kit builder and does not rebuild this file. From the repo root:

```bash
make design-md
make grade
make check
```
