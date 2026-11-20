# Maze design reference

A token set and component reference for Maze's public marketing site (https://maze.co/), a Gatsby site for a user-research product. Use it to build a marketing page that borrows its look: a warm off-white page, Phonic display type at 130px light, ink buttons (`#1c1c1c`, 8px radius, 40px tall), a lime chip (`#dbf570`), and a neutral ramp from white to `#1c1c1c`. It was captured signed out, in headless Chromium, on 2026-11-21. Desktop pages are 1440×900 at 1x. Phone pages are 390×844 CSS pixels at 2x (780×1688 PNG).

The site ships one light theme. No dark switch was found. The signed-in product (studies, reports, panel, builder) sits behind https://auth.maze.co/login and was not entered. Signup at https://auth.maze.co/signup/ was not entered. No form was submitted. The CookieYes banner was hidden with CSS and never accepted.

This package contains no Maze code, and none of its artwork has been redrawn. The screenshots belong to Maze ([docs/RIGHTS.md](../../docs/RIGHTS.md)). Borrow structure and proportions, not the logo, artwork or brand assets.

| File | What it is |
|---|---|
| [site-tree.md](site-tree.md) | The public site map: which control opens which page, menu, or wall, written before screenshots |
| [icon.png](icon.png) | The site icon, 128 px PNG, from the apple-touch-icon on maze.co |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the `:root` ramps, Phonic, radii, a short spacing pair, motion and three type styles. `light` holds the semantic roles. Every token has `$extensions.source` |
| [style-guide.html](style-guide.html) | The tokens rendered. Phonic is not loaded, so type falls back to the system sans. Open it from disk |
| [components.md](components.md) | Measured public controls, with crops, then a Gaps section |
| [patterns.md](patterns.md) | Header, hero, pricing, demo form, content indexes, consent |
| [components/crops/](components/crops) | Element crops from the live page |
| [screenshots/](screenshots) | Public captures, `{page}-light-{state}.png` at 1440×900 and `mobile-*` at 780 wide, quantised to 256 colours |
| [icons/](icons) | Index only. The logo was not extracted ([docs/RIGHTS.md](../../docs/RIGHTS.md)) |
| [raw/](raw) | `css-vars.json` (custom properties), `components-computed.json` (computed styles), `full/` (viewport sidecars) |
| [tools/](tools) | Capture scripts and the builders |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

Custom properties were read from the live homepage CSSOM with `tools/capture/public/vars-live.mjs` on 2026-11-21. Colours are declared as `oklch()` on `:root`. `tools/build_tokens.py` converts them to sRGB with the CSS Color 4 OKLab matrix and labels that hex Derived. Dimensions, font weights and cubic beziers were read as declared and labelled Measured. The 130px display size is the computed style of the homepage `h1`.

The CookieYes banner was hidden with CSS. Accept All was not clicked. Login and signup URLs were recorded in [site-tree.md](site-tree.md) and not opened.

## What to distrust

- Hex colours are Derived from oklch, not sampled from screenshots. Screenshots are 256-colour PNGs. Read colour from tokens.json.
- Header button crops in `components/crops/` are the wrapping link, which is transparent. The painted Get a demo button is the inner element: Phonic 17px, fill `#1c1c1c`, white text, 8px radius, 40px height, padding 8px 16px. That fill is `--color-neutral-700`.
- The 8px button radius is Tailwind `rounded-lg`, not one of the named `--radius-*` steps (those stop at 1rem).
- Focus ring, warning and info roles, disabled, loading and error states were not captured.
- There is no dark theme in this package. Do not invent one.
- DESIGN.md, the Brief section and the Health section are empty on purpose. `make design-md`, `make brief` and `make grade` read the catalog entry, and this capture was told not to edit catalog.json.
- Marketing illustrations of a study builder are public demos, not the signed-in app.

## Fonts

Phonic, served from https://maze.co/fonts/phonic/ as woff2 (weights 300, 400, 500, 700, plus italics). It is proprietary and is not committed. Tokens fall back to `sans-serif`. The body element itself computed to the system sans. Headings and the painted buttons computed to Phonic.

## Coverage

| Item | Status |
|---|---|
| Colour ramps | Captured. Neutral, blue, cyan, lime, purple, red, yellow in [tokens.json](tokens.json). Neutral has no 800 step |
| Page, surface, text, muted, accent, border | Captured. `light.*` |
| Raised, overlay, scrim | Not captured. Not declared on the public pages |
| Disabled text | Not captured |
| On-accent | Captured as `light.on-accent` (`--chips-text`) |
| Link colour | Captured. It aliases the same ink as text |
| Border strong, focus | Not captured. No dedicated tokens |
| Accent hover and pressed | Not captured as separate tokens. Button hover crops did not change the wrapping link |
| Success, danger | Captured as aliases of cyan-600 and red-500 |
| Warning, info | Not captured as roles. Yellow and blue ramps exist |
| Type | Partial. Display, body, label measured. Caption and code not captured as roles |
| Spacing scale | Partial. `--spacing` is 0.25rem and `--nav-height` is 80px. No 4/8 step scale was declared |
| Radii | Captured. `--radius-xs` through `--radius-2xl` |
| Border widths | Not captured as a scale |
| Elevation | Partial. `--shadow-nav` and `--shadow-modal` |
| Motion | Partial. 150ms default duration, two easings |
| Button, link | Captured. [components.md](components.md), [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Icon button | Not isolated |
| Text field, select | Captured empty on the demo page. Not submitted. [screenshots/demo-light-default.png](screenshots/demo-light-default.png) |
| Text area, checkbox, radio, switch | Not present on the pages measured |
| Tabs | Observed on /ai/ (in-page buttons). Not measured as a component |
| Menu | Captured. [screenshots/home-light-platform-menu.png](screenshots/home-light-platform-menu.png), [screenshots/mobile-home-light-nav-open.png](screenshots/mobile-home-light-nav-open.png) |
| Tooltip, dialog, toast, table, avatar, badge | Not captured as product components. Cookie dialog was not opened |
| Card | Observed in screenshots. Not a separate measured component |
| App shell | Not present. Marketing header only |
| Form with validation error | Not captured. Demo form was not submitted |
| Empty, loading, error, destructive confirm, search | Not present on the public site. App states are behind login |
| Light and dark | Light only. Dark is not present |
| Desktop 1440 and phone 390 | Captured. Sidecars in [raw/full/](raw/full) record innerWidth 1440 and, for phone, a 390 CSS viewport at deviceScaleFactor 2 |
| Login | Wall recorded and not entered. [screenshots/login-light-default.png](screenshots/login-light-default.png) shows the empty email and password form. No fields filled, no Google or Apple click |
| Signup | Not entered. https://auth.maze.co/signup/ is a wall |
| Product updates | Not captured. https://maze.co/product-updates/ returned 403 |
| Help Center | Not captured. https://help.maze.co/ is a separate host |
| Principles, voice, per-component a11y notes | Not applicable. No public design-system site was found |

## Do and don't

- **Keep the page warm and quiet.** Page is white, surfaces are `#f5f4f0`, text is `#1c1c1c`. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Use ink for the primary action.** Get a demo is a filled `#1c1c1c` button, 40px tall, 8px radius. Try Maze for free is a ghost outline. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Set display type in Phonic Light, tight tracking.** The homepage headline is 130px, weight 300, letter-spacing -11.7px. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Use lime as a chip, not as the page fill.** `--chips-background` is `#dbf570` on ink text. See [screenshots/home-light-platform-menu.png](screenshots/home-light-platform-menu.png).
- **Don't treat the marketing demos as the app.** Study-builder cards on the homepage are public illustrations. The product is behind login. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Don't accept the cookie banner to capture.** Hide it. Accept All submits consent. See [screenshots/home-light-consent.png](screenshots/home-light-consent.png).

## Rebuild

```bash
cd systems/maze
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/vars-live.mjs
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/build_components_md.py
```

Screenshots are recaptured with `node tools/capture/public/public.mjs` and quantised with `python3 tools/capture/quantize.py ~/.design-systems/maze/raw-shots`.
