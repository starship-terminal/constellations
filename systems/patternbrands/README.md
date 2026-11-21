# Pattern Brands design reference

A token set and component reference for the Pattern Brands public site (patternbrands.com), the holding page for Onsen, Miracle Made and GIR. Captured on 2026-11-21, signed out, in headless Chromium. Desktop shots are 1440×900 at 1x. Phone shots are 390×844 at 2x. The site has one light theme: `prefers-color-scheme: dark` left the page white with the same green footer.

There is no signed-in surface. `/login`, `/signin`, `/sign-in`, `/account` and `/auth` are the Webflow Page Not Found page. The map of controls is [site-tree.md](site-tree.md). The login probe is [login-review.json](login-review.json).

The page is worth a capture because almost every painted role is one green (`#084935`) on white, with ink `#1e1e1e`. A second green (`#1d9671`) appears only as the button hover circle. A third green (`#13af7f`) is painted onto the rotating word and is Sampled, not a custom property. Type is P22 Mackinac Pro for the page and Cadiz for the footer. Corners are square except the two buttons.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px, from the apple-touch-icon web clip |
| [tokens.json](tokens.json) | DTCG tokens: `core` and `light`. Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Generated after catalog registration. Until the batch merge, take values from tokens.json |
| [style-guide.html](style-guide.html) | Tokens and the main controls, rendered from tokens.json |
| [components.md](components.md) | Component inventory and states |
| [patterns.md](patterns.md) | How the home, legal and 404 pages are built |
| [site-tree.md](site-tree.md) | Which control opens which page |
| [login-review.json](login-review.json) | Sign-in probe. No signed-in surface |
| [components/crops/](components/crops) | 14 element crops from the raw captures |
| [screenshots/](screenshots) | Page captures at 1440 and 390, light only |
| [raw/](raw) | CSS custom properties, computed styles, dark-scheme check |
| [icons/](icons) | Index only. Artwork is not extracted |
| [tools/](tools) | Builders and the capture kit |

## Brief

<!-- brief:start -->
Brief is written by `make brief` after the catalog entry exists. The batch merge registers catalog.json. Until then, read tokens.json.
<!-- brief:end -->

## Health

<!-- health:start -->
Health is written by `make grade` after the catalog entry exists. The batch merge registers catalog.json.
<!-- health:end -->

## How the values were read

Headless Chromium loaded the public pages. Custom properties were read from the CSSOM on `:root` and resolved with `getComputedStyle(document.documentElement)`. Component values were read from computed styles at 1440×900 and 390×844. The rotating-word green was sampled from a flat run of pixels in the raw screenshot before quantize, because computed color stayed `#1e1e1e`. Screenshots were then quantised to 256-colour PNGs. Full-colour originals stay outside the repo at `~/.design-systems/patternbrands/raw-shots/`.

No `theme-color` meta, no mask-icon colour, and no web manifest were present.

## What to distrust

- `#13af7f` is Sampled. The stylesheet does not declare it. Anti-aliasing around the word also produced nearby greens.
- Webflow's starter palette (blue `#2d62ff`, pink, success, warning, error) is declared on `:root` and is not painted on the captured pages. It lives under `core.palette.starter` and is not a semantic role.
- The stylesheet's focus rule names `#4d65ff` for `[tabindex]:focus-visible`. Tab on Contact Us painted the browser outline `#005fcc` instead. The token records what painted.
- Button hover is a circle scaling over 700ms. The crop shows the end state.
- P22 Mackinac Pro and Cadiz are proprietary. The style guide falls back to Georgia and Arial.
- The Made in Webflow badge is Webflow's, not Pattern's.
- The published mailing address and contact email are masked in the footer screenshots. The footer column is still there. The text is not in the repo.

## Fonts

- P22 Mackinac Pro, weight 400, served as woff2 from the Webflow CDN. Proprietary. Fallback in tokens: Georgia, sans-serif.
- Cadiz, weight 400, same CDN. Proprietary. Fallback: Arial, sans-serif.
- webflow-icons is Webflow's icon font and is not used as a product type role.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Page, surface, text, accent, border | captured | `light.background.*`, `light.text.*`, `light.action.*` |
| Raised, overlay, scrim | not present | no dialog, menu or raised card |
| Disabled text | not present | no disabled control |
| Accent hover | captured | `light.action.primaryHover` `#1d9671` |
| Success, warning, danger, info | not present | declared in the starter palette, not painted |
| Dark theme | not present | `prefers-color-scheme: dark` did not change the page (`raw/dark-scheme.json`) |
| Type roles | captured | `core.typography` display, heading, body, label, footer |
| Spacing, radii, size | captured | `core.space`, `core.radius`, `core.size` |
| Elevation | not present | no box-shadow on the captured controls |
| Motion | captured | `core.motion` 700ms button, 1.1 image scale, 4px arrow |
| Layout | captured | 736px content, 40px / 20px padding, screenshots at 1440 and 390 |
| Button | captured | default, hover, focus-visible. Pressed colour unchanged. Disabled and loading not present |
| Link | captured | visit link and footer link |
| Card | captured | default and hover |
| Text field, text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, table, avatar, badge, list row | not present | not on the public site |
| App shell, search, filter, onboarding, destructive confirm | not present | marketing page only |
| Error page | captured | Webflow 404 at `/login` and other unknown paths |
| Form validation | not present | no form on the site |
| Signed-in product | not captured | no sign-in surface. See [login-review.json](login-review.json) |

## Do and don't

- **Do paint the page white and the footer green.** The home section and the legal pages sit on `#ffffff`. The footer is the only full-bleed green. See [home-light-default.png](screenshots/home-light-default.png).
- **Do use one green for fills and links.** Buttons, the footer and the visit links share `#084935`. See [button-default.png](components/crops/button-default.png) and [link-default.png](components/crops/link-default.png).
- **Do spend the lighter green only on the button hover and the rotating word.** Hover is `#1d9671`. The word is the sampled `#13af7f`. See [button-hover.png](components/crops/button-hover.png).
- **Do set the page in P22 Mackinac Pro and the footer in Cadiz.** Both are weight 400. See [heading-default.png](components/crops/heading-default.png) and [footer-default.png](components/crops/footer-default.png).
- **Do keep corners square except the two buttons.** Cards, images and the footer are 0. Contact Us is 24px. Go Home is a pill. See [card-default.png](components/crops/card-default.png).
- **Don't invent a dark theme.** The dark colour-scheme check did not change the page.

## Rebuild

```bash
cd systems/patternbrands
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

`make design-md` and `make grade` need a catalog entry. catalog.json was left for the batch merge.

## Capture notes

Viewport checks are in each `screenshots/*.png.capture.json`. Desktop `innerWidth` was 1440 and devicePixelRatio was 1. Phone `innerWidth` was 390 and devicePixelRatio was 2. Home at 1440 fits in one viewport (scroll height 900). Home at 390 is 2092px tall, so the phone footer is a separate shot.
