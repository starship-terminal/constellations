# Runway design reference

A token set and component reference for Runway's public site. Read from **runway.com** (runwayml.com redirects there) on **2026-11-21**, signed out, in headless Chromium at 1440 x 900 and 390 x 844. The marketing site is light only. The signed-in product at app.runwayml.com was not entered.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px, from runway.com/icon.png |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` scales and a `light` semantic set. Every token has `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Generated from tokens.json and this README. One theme, no provenance. |
| [style-guide.html](style-guide.html) | Renders the measured roles and the main controls |
| [components.md](components.md) | Component inventory, crops, and gaps |
| [patterns.md](patterns.md) | How the header, pricing, form, phone sheet and login wall fit together |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or wall |
| [components/](components/) | Element crops |
| [icons/](icons/) | Inline header SVGs and INDEX.tsv |
| [screenshots/](screenshots/) | 67 page captures, 256-colour PNGs |
| [raw/](raw/) | css-vars.json and components-computed.json |
| [tools/](tools/) | Capture scripts and builders |

## Brief

<!-- brief:start -->
Read [tokens.json](tokens.json) before designing in this style. The public site is light only.

### Principles

1. **Keep the page white and the action near-black.** The filled header button is `#262626`, not the declared blue.
2. **Open sections from a hover menu.** Creative, Dev, Robotics, Research, Resources and Enterprise each open a panel. A click leaves the page.
3. **Put type on the media, not on a coloured band.** The hero title is white, 56px, weight 400, on a full-bleed image.
4. **Don't treat the declared blue as the marketing accent.** `#2c22fa` is a developer-stylesheet token. It is not the filled CTA.
5. **Don't style the editor from this package.** Login stops at auth.runwayml.com.

Each rule links a screenshot under [Do and don't](#do-and-dont).

### Using tokens

| Role | light |
|---|---|
| page | #ffffff `core.color.gray.0` |
| surface | #eef1f5 `core.color.quiet` |
| text | #0c0c0c `core.color.ink` |
| muted | #646c78 `core.color.menu-muted` |
| accent | #2c22fa `core.color.interactive.primary` |
| border | rgba(0, 0, 0, 0.1) `light.border.DEFAULT` |

Font: `core.font.family.sans` is abcNormal, then a fallback. Radius steps: 6px, 8px, 12px, 16px, 999px. Spacing steps are the measured button and field paddings.

### Using components

Read [components.md](components.md). Patterns are in [patterns.md](patterns.md). Crops are in [components/crops/](components/crops). [style-guide.html](style-guide.html) renders the roles.

### Accessibility

Text on page is about 19:1. Muted `#646c78` on white is about 5.3:1. The declared danger colour was not seen on a control. Focus ring colour was not read from a held focus-visible state.

<!-- brief:end -->

## Health

<!-- health:start -->
Not graded in this capture. catalog.json was not edited, so `make grade` was not run for this package.

<!-- health:end -->

## How the values were read

Headless Chromium, Playwright, signed out, on 2026-11-21.

- **Tokens.** [tools/capture/vars.mjs](tools/capture/vars.mjs) collected stylesheet bodies from network responses and inline style tags on runway.com, dev.runwayml.com and docs.dev.runwayml.com, then parsed custom properties with `CSSStyleSheet`. The `--rw-gray-*` ramp, radii, font stacks and the interactive blues are declared variables. Marketing button colours were also read with `getComputedStyle` in [raw/components-computed.json](raw/components-computed.json).
- **Screenshots.** [tools/capture/public/public.mjs](tools/capture/public/public.mjs) shot each planned public page at 1440x900 (1x) and the phone set at 390x844 (2x). Sidecars record `innerWidth` 1440 and 390. Hover menus were recaptured after the first pass, because the first hover did not expand. [tools/capture/quantize.py](tools/capture/quantize.py) wrote 256-colour PNGs.
- **Consent.** The OneTrust banner was hidden with CSS. No consent button was clicked.

Nothing was signed into, bought, or submitted. Login and signup were opened only to record the empty walls. The password and email fields were not filled. Google, Apple and SSO were not clicked. Continue was not clicked. `login-extracted` stays not-started. catalog.json was not edited.

## What to distrust

- **This is the public site, not the editor.** Projects, the canvas, billing and onboarding sit behind auth.runwayml.com.
- **Light only.** There is no public theme toggle. The `--rw-*` gray ramp includes dark steps used by docs and the app shell. They are in `core`, not a captured dark theme.
- **The blue is declared, not the marketing CTA.** The filled button measures `#262626`.
- **Focus ring colour is not a held reading.** The hero CTA class names `ring-blue-500`. The token says so.
- **Quantised screenshots.** Read colours from tokens.json.
- **Pressed states were not held.** A pointerdown dispatch did not change the CTA fill.

## Fonts

**abcNormal** (declared as ABC Normal) runs the marketing pages and the header. Weights 300, 400, 500 and 600 are served as woff2. **timesNow** is declared and was not on the measured controls. **Akkurat Mono LL** is the first face of `--rw-font-mono`. None of these are in the package. The style guide uses the system sans.

## Coverage

| Item | Status |
|---|---|
| Colour roles, light | Captured. [tokens.json](tokens.json), [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Colour roles, dark | Not present as a public theme |
| Type | Captured. Hero 56/36, nav 16, button 14, field 16 |
| Spacing | Captured as component padding. No full spacing scale was declared on the marketing pages. |
| Radii | Captured. 6, 8, 12, 16, 999px |
| Borders | Captured. Menu divider is `border-black/10` |
| Elevation | Declared `--rw-drop-shadow-16`. Not seen on the measured marketing controls. |
| Motion | Captured. `--landing-duration` .25s, `--landing-ease` |
| Sizing | Captured. CTA 32px, nav link 40px, field 41px, content max 1232px |
| Layout | Captured at 1440 and 390. Sidecars confirm the CSS viewport. |
| Button | Captured. [components/crops/nav-cta-default.png](components/crops/nav-cta-default.png) |
| Link | Captured. Nav Pricing link |
| Text field, text area, select, checkbox | Captured on the enterprise form, empty |
| Tabs | Captured. Pricing yearly and API shots |
| Menu | Captured. Six desktop hover menus and the phone sheet |
| Dialog | Not captured. Cookie Settings was hidden, not opened |
| Card, list row, badge | Observed in screenshots. Not separately measured |
| Icon button, radio, switch, tooltip, toast, table, avatar | Not present on the captured public pages |
| Disabled, loading, error | Not present, or not reached because forms were not submitted |
| App shell of the signed-in product | Not captured. Login wall |
| Destructive confirmation, toast feedback, onboarding | Not captured. Behind the login wall, or not on the public pages |
| Search | Captured on the docs site. [screenshots/docs-light-search.png](screenshots/docs-light-search.png) |

## Do and don't

- **Do keep the page white and the action near-black.** The filled Try Runway button is `#262626` on a white header. [screenshots/home-light-default.png](screenshots/home-light-default.png)
- **Do open sections from a hover menu.** Creative opens a three-column panel without leaving the page. [screenshots/home-light-menu-creative.png](screenshots/home-light-menu-creative.png)
- **Do put type on the media.** The hero title is white on the image, not on a solid band. [screenshots/home-light-default.png](screenshots/home-light-default.png)
- **Don't treat the declared blue as the marketing accent.** `#2c22fa` lives on the developer stylesheets. The marketing CTA is near-black.
- **Don't style the editor from this package.** [screenshots/login-light-default.png](screenshots/login-light-default.png) and [screenshots/signup-light-default.png](screenshots/signup-light-default.png) are the empty walls. The canvas was not opened.
- **Don't submit the sales form to see its error state.** The empty form is the captured state. [screenshots/enterprise-contact-light-default.png](screenshots/enterprise-contact-light-default.png)

## Rebuild

```bash
cd systems/runway
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/public.mjs
python3 tools/capture/quantize.py ~/.design-systems/runway/raw-shots screenshots
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

catalog.json was not edited, by instruction. `make design-md` was not run against the catalog. DESIGN.md in this folder was written to match the generator's shape for a light-only package.
