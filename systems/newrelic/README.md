# New Relic

New Relic is an observability product (newrelic.com). This package is the public marketing site, captured signed out on 2026-11-22. The public homepage paints cream with near-black type and a green accent. Widths: 1440 by 900 and 390 by 844. No account was used.

The public site tree, dated 2026-11-22, is [site-tree.md](site-tree.md). Login is an app wall at one.newrelic.com. It was opened empty and stopped. Signup was opened empty and stopped. `catalog.json` was left alone. `login-extracted` stays not-started.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Header, footer, and the public links they open, dated 2026-11-22 |
| [DESIGN.md](DESIGN.md) | Pointer. Not generated, because catalog.json was left alone |
| [tokens.json](tokens.json) | Measured colours, type, and radius |
| [style-guide.html](style-guide.html) | Swatches from those tokens |
| [components.md](components.md) | Public controls and the shots that show them |
| [patterns.md](patterns.md) | Homepage, menu, pricing, and public pages |
| [login-review.json](login-review.json) | Empty login and signup walls. `loginExtracted` is not-started |
| [icon.png](icon.png) | 128 px PNG from the site icon |
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

The homepage was opened signed out. Custom properties were parsed from the stylesheets. `getComputedStyle` was read on the body, the homepage hero, the lede, the Platform button, the header Get Started Free control, the header Get Demo control, and Watch On Demand. Button, text, and link colours come from those computed styles. The page fill was sampled from the raw screenshot before quantising, because the painted page is lighter than the computed body background.

Font files on the homepage name Mona Sans for the hero and Inter for body, nav, and buttons. Geist Mono was loaded and not measured on a visible control. Those files are not committed.

Screenshots are the first viewport from headless Chromium at device pixel ratio 2, then quantised to 256 colours. A cookie banner was hidden with CSS. Accept and deny were not clicked.

## What to distrust

The homepage body background computed as `rgb(229, 228, 216)`. A sampled pixel in the left column was `#f1f0e4`. The token uses the sampled page colour.

Mona Sans and Inter are licensed and are not in this package. Tokens fall back to system sans-serif.

The wordmark in `icons/mark.svg` is a drawn stand-in. It is not the extracted logo. `icon.png` is the site apple-touch icon, resized to 128 px.

No dark marketing theme was painted. `color-scheme` on the homepage was `normal`. The shots use `light` in the filename so they match the rest of the library.

The stylesheet `--color-lightninggreen` is `#26a769`. The painted Get Started Free button is `#1ce783`. The accent token uses the painted button.

A login or signup screenshot was discarded when its painted URL carried a redirect, session, or OAuth query. Do not treat a missing wall image as a missing wall.

## Fonts

| Family | Where | Licence |
|---|---|---|
| Mona Sans | Homepage hero | Licensed. Not committed. Tokens fall back to ui-sans-serif, system-ui, sans-serif |
| Inter | Body, nav, buttons | Licensed. Not committed. Tokens fall back to ui-sans-serif, system-ui, sans-serif |
| Geist Mono | Loaded on the homepage | Licensed. Not committed. Not measured on a visible control |

## Coverage

| Checklist | Status |
|---|---|
| Colour roles | Captured from computed styles and sampled fills. [raw/components-computed.json](raw/components-computed.json) |
| Dark theme | Not present on the homepage. The public site paints cream |
| Type roles | Hero and body captured. Other roles not measured |
| Spacing, radii | Button radius and padding captured. Spacing scale not measured |
| Elevation | Not measured |
| Motion | Not captured. Stylesheet names `--fade-transition-time` 700ms and `--slide-transition-time` 400ms |
| Button | Header Get Started Free and hero Get Started Free, default only |
| Button hover, focus, pressed | Not captured |
| Link | Watch On Demand, 15px, `#1ce783` |
| Text field | Search toggle, empty, not submitted. Signup and login fields, empty |
| Text area, select, checkbox, radio, switch | Not measured on a public marketing page |
| Menu | Platform, Solutions, Pricing, Customers, Resources, and the phone drawer |
| Dialog | Cookie banner hidden, not accepted |
| Card | Pricing plan cards |
| App shell | Marketing header and footer. The account was not opened |
| Form validation | Not captured. No form was submitted |
| Checkout, subscribe, signed-in account | Not captured. Stopped at login, signup, demo, pricing request, and contact |

The public walk is [site-tree.md](site-tree.md). catalog.json was left alone. `login-extracted` stays not-started.

## Do and don't

1. **Do paint the page cream and the heading near black.** Page is `#f1f0e4`. Heading is `#080f11`. See [home-light-1440](screenshots/home-light-1440.png).
2. **Do set the hero in Mona Sans.** The heading is 132px, weight 864, line-height 108px, letter-spacing -4px. Same shot.
3. **Do make the header action a green pill.** Get Started Free is `#1ce783` with `#080f11` text, radius 36px. Same shot.
4. **Do keep body copy in Inter.** Body is 18px, weight 500, `#080f11`. The lede is 21px, weight 600. Same shot.
5. **Don't invent a dark marketing theme.** The public homepage did not paint one.
6. **Don't treat a discarded sign-in shot as a gap in the product.** The wall was opened. A URL with session state was not kept.
7. **Don't submit a form or create an account from this package.** Both were left alone.

## Rebuild

Tokens were written from computed styles on [https://newrelic.com/](https://newrelic.com/) and from [raw/css-vars.json](raw/css-vars.json). From the repo root, after a catalog entry exists:

```bash
make design-md
make grade
make check
```

`catalog.json` was left alone, so those commands were not run for this package.
