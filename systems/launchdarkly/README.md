# LaunchDarkly

LaunchDarkly is a feature-flag and runtime-control product (launchdarkly.com). This package is the public marketing site, captured signed out on 2026-11-22. The public pages paint dark. Widths: 1440 by 900 and 390 by 844. No account was used.

The public site tree, dated 2026-11-22, is [site-tree.md](site-tree.md). Login is an app wall. It was opened empty and the screenshot was discarded because the painted URL carries a redirect query. Signup was opened empty and kept. `catalog.json` was left alone. `login-extracted` stays not-started.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Header, footer, and the public links they open, dated 2026-11-22 |
| [DESIGN.md](DESIGN.md) | Pointer. Not generated, because catalog.json was left alone |
| [tokens.json](tokens.json) | Measured colours, type, and radius |
| [style-guide.html](style-guide.html) | Swatches from those tokens |
| [components.md](components.md) | Public controls and the shots that show them |
| [patterns.md](patterns.md) | Homepage, menu, pricing, and public pages |
| [login-review.json](login-review.json) | Empty login and signup walls. Login screenshot discarded. `loginExtracted` is not-started |
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

The homepage was opened signed out. Custom properties were parsed from the stylesheets. `getComputedStyle` was read on the body, the homepage h1, the lede, the Pricing link, the header Book a demo control, and Sign in. Button, text, and link colours come from those computed styles. The page fill and the status bar were sampled from the raw screenshots before quantising, because the painted page is darker than the computed body background.

Font files on the homepage name Söhne for body, Sora for the heading, and Söhne Mono. Those files are not committed.

Screenshots are the first viewport from headless Chromium at device pixel ratio 2, then quantised to 256 colours. A cookie banner (`#onetrust-consent-sdk`) was hidden with CSS. OK and Deny all were not clicked.

## What to distrust

The homepage body background computed as `rgb(25, 25, 25)`. A sampled pixel in the hero was `#0e0e0e`. The token uses the sampled page colour.

Söhne and Sora are licensed and are not in this package. Tokens fall back to ui-sans-serif, system-ui, sans-serif.

The wordmark in `icons/mark.svg` is a drawn stand-in. It is not the extracted logo. `icon.png` is the site icon, resized to 128 px.

No light theme was painted. `color-scheme` on the homepage was `normal`. The shots use `light` in the filename so they match the rest of the library. The pages are dark.

The sign-in screenshot was discarded. Do not treat a missing login image as a missing wall. The wall painted, and its URL was not safe to keep.

Help Center stayed on a Cloudflare verification page. Academy returned an error page. Trust Center did not paint. Those shots were not kept.

## Fonts

| Family | Where | Licence |
|---|---|---|
| Sora | Homepage h1, as headingFont3 | Licensed. Not committed. Tokens fall back to ui-sans-serif, system-ui, sans-serif |
| Söhne | Body, nav, buttons, as bodyFont | Licensed. Not committed. Tokens fall back to ui-sans-serif, system-ui, sans-serif |
| Söhne Mono | Loaded on the homepage | Licensed. Not committed. Not measured on a visible control |

## Coverage

| Checklist | Status |
|---|---|
| Colour roles | Captured from computed styles and two sampled fills. [raw/components-computed.json](raw/components-computed.json) |
| Light theme | Not present on the homepage. The public site paints dark |
| Type roles | Hero and body captured. Other roles not measured |
| Spacing, radii | Button and nav radius captured. Spacing scale not measured |
| Elevation | Not measured |
| Motion | Not captured |
| Button | Header Book a demo, default only |
| Button hover, focus, pressed | Not captured |
| Link | Pricing, 16px, `#ffffff` |
| Text field | Homepage email, empty, not submitted. Signup fields, empty. Login email and password, empty, screenshot discarded |
| Text area, select, checkbox, radio, switch | Not measured on a public marketing page |
| Menu | Platform, Solutions, Resources, Developers, and the phone drawer |
| Dialog | Cookie banner hidden, not accepted |
| Card | Pricing plan cards |
| App shell | Marketing header and footer. The account was not opened |
| Form validation | Not captured. No form was submitted |
| Checkout, subscribe, signed-in account | Not captured. Stopped at login, signup, demo, and contact |

The public walk is [site-tree.md](site-tree.md). catalog.json was left alone. `login-extracted` stays not-started.

## Do and don't

1. **Do paint the page near black and the heading near white.** Page is `#0e0e0e`. Heading is `#f8f8f8`. See [home-light-1440](screenshots/home-light-1440.png).
2. **Do set the hero in Sora.** The heading is 80px, weight 700, line-height 80px, letter-spacing -2px. Same shot.
3. **Do make the primary action a lime button.** Book a demo is `#ddff46` with `#191919` text. Same shot.
4. **Do keep body copy in Söhne.** Body is 16px, white. The lede is 20px, `#d1d6d9`. Same shot.
5. **Don't invent a light marketing theme.** The public homepage did not paint one.
6. **Don't treat the discarded sign-in shot as a gap in the product.** The wall painted. Its URL carried a redirect query, so the image was not kept.
7. **Don't submit a form or create an account from this package.** Both were left alone.

## Rebuild

Tokens were written from computed styles on [https://launchdarkly.com/](https://launchdarkly.com/) and from [raw/css-vars.json](raw/css-vars.json). From the repo root, after a catalog entry exists:

```bash
make design-md
make grade
make check
```

`catalog.json` was left alone, so those commands were not run for this package.
