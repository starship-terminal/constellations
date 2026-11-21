# Ritual

Ritual is a vitamin and supplement shop (ritual.com). This package is the public marketing site, captured signed out on 2026-11-22. Themes: light only. Widths: 1440 by 900 and 390 by 844. No account was used.

The public site tree, dated 2026-11-22, is [site-tree.md](site-tree.md). Login and signup are one Shopify wall. It was opened empty and the screenshot was discarded because the painted URL carries OAuth state. `catalog.json` was left alone. `login-extracted` stays not-started.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Header, footer, and the public links they open, dated 2026-11-22 |
| [DESIGN.md](DESIGN.md) | Pointer. Not generated, because catalog.json was left alone |
| [tokens.json](tokens.json) | Declared colours, type, and radius |
| [style-guide.html](style-guide.html) | Swatches from those tokens |
| [components.md](components.md) | Public controls and the shots that show them |
| [patterns.md](patterns.md) | Homepage, menu, product, and editorial pages |
| [login-review.json](login-review.json) | Empty sign-in wall. Screenshot discarded. `loginExtracted` is not-started |
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

The homepage was opened signed out. Custom properties were parsed from the stylesheets and resolved on `:root`. `getComputedStyle` was read on the body, the homepage h1, and the Our Standards link. Screenshots were not sampled for colour.

Screenshots are the first viewport from headless Chromium at device pixel ratio 2, then quantised to 256 colours. A cookie banner (`aside.dg-consent-banner`) was hidden with CSS. Accept All and Manage Cookies were not clicked.

## What to distrust

The homepage h1 computed an empty text string. The visible heading "Black Friday Sale Starts Now" is still the h1 in the screenshot. The size 66px is the computed size at 1440. It was not remeasured at 390.

Shop Sale's own link computed a translucent card background, not the white pill. The pill is an inner control. Its radius was not measured. The declared primary button is `#142b6f` with white text. Hover `#ffd600` was not photographed.

CircularXX is proprietary and is not in this package. Tokens fall back to ui-sans-serif, system-ui, sans-serif.

The wordmark in `icons/mark.svg` is a drawn stand-in. It is not the extracted logo.

No dark theme was painted. `color-scheme` on the homepage was `light`.

The sign-in screenshot was discarded. Do not treat a missing login image as a missing wall. The wall painted, and its URL was not safe to keep.

## Fonts

| Family | Where | Licence |
|---|---|---|
| CircularXX | Body, hero, nav, wordmark | Proprietary. Not committed. Tokens fall back to ui-sans-serif, system-ui, sans-serif |

## Coverage

| Checklist | Status |
|---|---|
| Colour roles | Captured in light from declared custom properties. [raw/css-vars.json](raw/css-vars.json) |
| Dark theme | Not present on the homepage |
| Type roles | Hero and body captured. Other roles not measured |
| Spacing, radii | Declared radius steps captured. Spacing scale not measured |
| Elevation | Not measured |
| Motion | Not captured |
| Button | Add to Cart and Shop Sale, default only |
| Button hover, focus, pressed | Not captured. Hover colour is declared only |
| Link | Our Standards, 16px, `#142b6f` |
| Text field | Search field, empty, not submitted. Sign-in email field, empty, screenshot discarded |
| Text area, select, checkbox, radio, switch | Not measured |
| Menu | Shop drawer, desktop and phone |
| Dialog | Search drawer. Cookie banner hidden, not accepted |
| Card | Product cards in the menu and on collection pages |
| App shell | Marketing header and footer. The account was not opened |
| Form validation | Not captured. No form was submitted |
| Checkout, subscribe, signed-in account | Not captured. Stopped at login, signup, checkout, and subscribe |

The public walk is [site-tree.md](site-tree.md). catalog.json was left alone. `login-extracted` stays not-started.

## Do and don't

1. **Do paint the page white and the text navy.** Page is `#ffffff`. Text is `#142b6f`. See [home-light-1440](screenshots/home-light-1440.png).
2. **Do set the hero in CircularXX.** The heading is 66px, weight 450, letter-spacing -1.32px. Same shot.
3. **Do make the primary action a navy pill.** Add to Cart is `#142b6f` with white text. See [product-light-1440](screenshots/product-light-1440.png).
4. **Do keep the sale bar the same navy.** The announcement bar is navy with white type. Same home shot.
5. **Don't invent a dark theme.** The public homepage did not paint one.
6. **Don't treat the discarded sign-in shot as a gap in the product.** The wall painted. Its URL carried OAuth state, so the image was not kept.
7. **Don't submit the search field or Add to Cart from this package.** Both were left alone.

## Rebuild

Tokens were written from [raw/css-vars.json](raw/css-vars.json). From the repo root, after a catalog entry exists:

```bash
make design-md
make grade
make check
```

`catalog.json` was left alone, so those commands were not run for this package.
