# Devin public surface

A token set and page captures for Devin's public marketing site at **https://devin.ai/**. First capture of this web site into `systems/devin/` on **2026-11-22**, signed out. Desktop is **1440 by 900** at devicePixelRatio 1. Phone is **390 by 844** CSS. The site tree is [site-tree.md](site-tree.md).

origin/main did not have `systems/devin/`. [systems/devin-desktop](../devin-desktop) is the macOS app and was not edited. `catalog.json` was left alone, so `login-extracted` stays `not-started` and this README's Brief and Health are hand-written.

The marketing site paints **one light theme**. There is no theme control. The homepage stylesheet declares **417 custom properties**. The login and signup walls are a separate app at app.devin.ai (Inter, dark Log in button, empty email field, GitHub, ChatGPT, and Google).

**Boundary.** Login and signup were photographed empty and the branch stopped. Nothing was typed. Nothing was submitted. GitHub, ChatGPT, and Google were not clicked. The demo and contact forms were photographed empty and not submitted. Pricing checkout was not entered. The Individual pricing tab was not switched.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, menu, drawer, footer and wall controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | Empty login and signup walls. Probe stopped there. login-extracted is not-started. |
| [icon.png](icon.png) | The 48px favicon from devin.ai, scaled to 128px. |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds measured swatches, radii, and type. `light` holds the painted roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | A page that renders the swatches and the two button fills. |
| [components.md](components.md) | Component inventory and gaps. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [icons/](icons/) | `INDEX.tsv` only. UI SVGs were not exported. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. |
| [raw/](raw/) | The stylesheet readings and the login and signup probes. |
| [tools/](tools/) | `build_tokens.py` checks `tokens.json` against `raw/css-vars.json`. The capture script is under `tools/capture/`. |

## How the values were read

Computed style and the custom properties were read in headless Chromium on the live homepage, then written to [raw/css-vars.json](raw/css-vars.json). Colour tokens are the declared `rgb()` converted to hex, or a declared hex. The nav Get started fill was read from computed style. Radius and type tokens are the declared rem values, or the computed pixel size when that is what the page paints (the home h1 is 36px at 1440, the pricing h1 is 64px).

Menus, the phone drawer, and the page shots are headless Chromium. The T3 preview was used to confirm the live nav before the script ran. Its pane could not hold a 1440 CSS viewport on the first open, so the committed desktop shots are the headless 1440 captures.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. The homepage product illustration bands. Read colours from the tokens and from [raw/css-vars.json](raw/css-vars.json), not from a PNG pixel.
- **The home h1 is not the declared display size.** `--text-dt-h1` is 4rem. The painted home heading is 36px. The pricing heading is the 64px display.
- **Lab greys were not converted.** `--color-gray-100` and similar stay as `lab()` in the raw file.
- **Hover, pressed, disabled, and loading were not read.** Do not invent them.
- **Teams and Enterprise is the painted pricing state.** Individual was not switched. Start with Teams, Get Pro, and Get Max were not clicked.
- **Login is a different system.** Inter, not Skandia. The dark button is the auth submit, not the marketing pill.
- **The homepage session is demo art.** The names in that illustration are the site's artwork, not an account.
- **Skandia is not shipped.** The tokens name the family.
- **Changelog and University leave devin.ai.** They were photographed at the host they redirected to. Docs and the Trust Center were not captured.
- **Phone devicePixelRatio is 1.** The 390 shot is 390 CSS pixels wide. It is not a 2x retina PNG.

## Fonts

- **Skandia** for marketing UI, headings, and body. The site serves it. It is licensed and not included. Fallback in the token is system-ui, sans-serif.
- **Inter** is the painted auth-wall family, and the declared product sans.
- **Geist Mono** is the declared mono. It was not the painted marketing body.
- **STK Bureau Serif** is declared and was not the painted h1.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured from declared swatches and computed button and body colours. One theme. Lab greys not converted. |
| Type roles | Captured. Desktop computed size for the home h1, the pricing h1, and body. |
| Spacing | Nav button padding measured. The fluid section scale is in raw/css-vars.json and was not tokenised step by step. |
| Radii | Declared scale plus the painted nav pill. |
| Borders | Nav ghost button is 1px at black 8%. |
| Elevation | Declared shadow tokens recorded. The menu sits over a blurred page. |
| Motion | Not measured. Reduced motion was not emulated. |
| Button | Default primary and secondary measured at rest. Hover, focus, pressed, disabled, and loading not measured. |
| Link | Nav and footer links observed. Hover not measured. |
| Text field | Signup and login email fields measured empty. Demo and contact fields photographed empty. Nothing typed. |
| Text area | Present on demo and contact. Empty. Not filled. |
| Select, checkbox, radio, switch | Not present on the measured pages. |
| Tabs | Pricing Teams and Enterprise painted. Individual not switched. Blog filter chips observed. Not switched. |
| Menu | Product, Solutions, Resources, and the phone drawer captured. |
| Dialog | Not opened. |
| Card | Pricing cards and community cards captured. |
| Badge | Recommended and Product observed. |
| Avatar, list row, table, toast, tooltip | Not present, except demo art on the homepage. |
| 404 | Captured. |
| Themes | Light only. No dark theme on the public site. |
| Widths | Captured. Desktop 1440 and phone 390 for the homepage. Other pages at 1440 only. |
| Login and signup walls | Captured empty. Stopped there. `login-extracted` is not-started. |
| Signed-in app | Not captured. |

## Do and don't

- Use one black pill for the primary action. The secondary action is a quiet outline pill.
- Keep the page on #fcfcfc with #191919 ink. The blue accent is for numerals, recommended marks, and a few headings, not for every button.
- Treat the homepage session as illustration. Do not read it as a signed-in product screen.
- Do not style the auth wall from the marketing type. The wall is Inter on the same paper, with identity-provider rows above the email field.
- Do not invent a dark theme. The public site did not paint one.
