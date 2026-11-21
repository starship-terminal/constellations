# Meta

The public Meta shop at [https://www.meta.com/](https://www.meta.com/). On 2026-11-21 that URL returned 200 and landed on `https://www.meta.com/sg/`. The title was "Meta: Shop AI Glasses, Meta Glasses & Quest Headsets (en-SG)". Account: none. Theme: one light storefront. `color-scheme` on the root was `normal`. There is no theme toggle. Widths photographed: 1440 by 900 and 390 by 844.

This refresh replaces the earlier assistant capture. That pass recorded `www.meta.ai` and `auth.meta.com` and had no page screenshots. The live product at meta.com is the shop. Facebook, Instagram, and Threads are not this package.

The `/sg/` path is the geo redirect from this machine. It is not an account location. The delivery-country dialog was opened and not confirmed.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Which homepage control opens which page, menu, or dialog |
| [login-review.json](login-review.json) | Public nav that was opened, and the walls that stopped the walk |
| [screenshots/](screenshots/) | Public pages at desktop and phone width |
| [DESIGN.md](DESIGN.md) | Prior assistant export. Not regenerated. Catalog was not edited |
| [tokens.json](tokens.json) | Prior assistant readings from `www.meta.ai`. Do not apply them to the shop |
| [raw/shop-readings.json](raw/shop-readings.json) | A few computed styles from the shop homepage |
| [tools/](tools/) | Capture kit copy, plus the shop page runner |

## How the values were read

Playwright (Chromium, headless) opened `https://www.meta.com/` and the public shop paths in [site-tree.md](site-tree.md). Screenshots are 256-colour PNGs from `tools/capture/quantize.py`. The T3 preview browser could not produce frames ("The browser is not producing screenshot frames"), so it was not the camera.

Shop colours below are `getComputedStyle` on `https://www.meta.com/sg/` at 1440 by 900 on 2026-11-21. The page defines almost no custom properties (three rules on `:root` / `html`). These are component readings, not a token set.

| Role | Reading | Where |
|---|---|---|
| Page | `rgb(255, 255, 255)` | `body` background |
| Text | `rgb(28, 30, 33)` | `body` color |
| Accent | `rgb(0, 64, 220)` | Shop button background |
| On accent | `rgb(255, 255, 255)` | Shop button text |
| Display | Optimistic AI VF, then Montserrat, Helvetica, Arial, Noto Sans | Hero `h1`, 61 px, weight 500 |
| UI | Helvetica, Arial, sans-serif | Body and the Shop button, 12 px |

The Shop button is a pill: `border-radius: 100px`, padding `14px 30px`, height 52 px, width 100 px. No `theme-color` meta tag was present.

## What to distrust

- [tokens.json](tokens.json) and [DESIGN.md](DESIGN.md) are the 2026-11-19 assistant capture. They describe a dark `www.meta.ai` page, not this shop. Catalog was not edited, so DESIGN.md was not regenerated.
- The hero face computed as Optimistic AI VF. `document.fonts` was not checked, so a fallback may be what painted.
- Prices on the shop are SGD. That is the Singapore storefront, not a global price list.
- Full-page shots are capped. Quest and the product page are taller than the saved sheet.
- The phone menu shot is a drawer over the homepage. The hamburger was clicked. Nothing in the drawer was followed.

## Coverage

| Item | Status |
|---|---|
| Colour roles, light shop | Partial. Page, text, and the Shop accent are in [raw/shop-readings.json](raw/shop-readings.json). No token rebuild |
| Colour roles, dark theme | Not present. No toggle |
| Type roles | Partial. Hero and the Shop button only |
| Spacing, radii | Partial. Shop button radius and padding only |
| Button default | Photographed. Blue pill on the homepage. [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Button hover, focus, pressed | Not captured |
| Text field | Photographed empty. Search dialog and the bag newsletter field. Nothing typed |
| Menu | Captured. AI glasses, Quest, and Support flyouts |
| Dialog | Captured. Search, delivery country, filter, and the Meta account wall |
| Select, checkbox, radio, switch, tabs | Not captured as components. Filter chips are in the filter dialog |
| App shell | Captured. Header, promo bar, bag, phone drawer |
| Empty bag | Captured. [screenshots/bag-light-default.png](screenshots/bag-light-default.png) |
| Search | Captured. Dialog opened, field left empty |
| Filtering | Captured. Filter dialog opened. Apply was not pressed |
| Login | Stopped. [screenshots/home-light-login-wall.png](screenshots/home-light-login-wall.png) |
| Checkout | Not captured. Not opened |
| Desktop 1440 and phone 390 | Captured |

## Do and don't

- Keep the storefront white and the type near-black. The page background is white. Headings on photos are white.
- Use one blue pill for the primary action. Shop, Apply, and Sign up share `rgb(0, 64, 220)` and a full pill radius.
- Leave secondary actions quiet. Explore Quest 3 and Cancel are grey or text buttons beside the blue pill.
- Treat the account dialog as a wall. It offers Sign up or log in and was not submitted.
- Do not treat the assistant tokens as this shop. [tokens.json](tokens.json) is the prior `www.meta.ai` capture.

## Rebuild

```bash
RAW=/tmp/meta-ai-raw PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node systems/meta-ai/tools/capture/public/public.mjs
python3 systems/meta-ai/tools/capture/quantize.py /tmp/meta-ai-raw
```

`build_tokens.py` still checks the assistant readings. It does not browse the shop. Do not run it to invent shop tokens.
