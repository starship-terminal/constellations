# Capy design reference

A token set and page captures for Capy's public marketing site. Captured **2026-11-22** from **https://capy.ai**, signed out. Desktop is **1440 by 900** at devicePixelRatio 1. Phone is **390 by 844** at devicePixelRatio 2 (PNG width 780). The site tree is [site-tree.md](site-tree.md). origin/main already had `systems/capy-desktop/` and did not have `systems/capy/`. This package is the public web site. `systems/capy-desktop/` was not overwritten. `catalog.json` was left alone, so `login-extracted` stays `not-started`.

The marketing site paints **one light theme**: white page, black header, hard offset buttons. There is no theme control. Sign-in and sign-up follow the browser colour scheme and were photographed empty in light and dark. The homepage product frame is a public demo.

**Boundary.** Sign-in and signup were photographed empty and the branch stopped. Nothing was typed. Nothing was submitted. Google, GitHub, and the passkey button were not clicked. Download files were not saved. Checkout was not entered.

| File | What it holds |
|---|---|
| [README.md](README.md) | This entry. |
| [DESIGN.md](DESIGN.md) | Hand-written token summary. `make design-md` was not run. |
| [tokens.json](tokens.json) | Measured colour, type, radius, size, and shadow tokens. |
| [site-tree.md](site-tree.md) | Which controls open which pages, menus, and the phone drawer. |
| [login-review.json](login-review.json) | Empty auth walls. `login-extracted` is `not-started`. |
| [style-guide.html](style-guide.html) | A page that renders the swatches, a drawn hero, and a drawn sign-in card from the tokens. |
| [components.md](components.md) | Component inventory and gaps. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [components/](components/) | Element crops of the primary button, secondary button, header button, both nav menus, the billing toggle, the sign-in card, and the 404 card. |
| [icons/](icons/) | `INDEX.tsv` only. UI SVGs were not exported. |
| [icon.png](icon.png) | 128px site icon. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. |
| [raw/](raw/) | Computed custom properties and the home and pricing readings. |
| [tools/](tools/) | `build_tokens.py`, `build_style_guide.py`, `build_components_md.py`, and the public capture script. |

## How the values were read

Computed style and named custom properties were read in the browser on the live page. Colour tokens are the declared hex, or a computed `rgb()` or `oklch()` converted to hex. The home h1 is 64px at 1440. The header is 65px. `--header-height` is 4rem.

At 390px the menu button is 24 by 24. The phone PNG is 780 wide.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. Gradients and the dither panels band. Read colours from the tokens and from [raw/css-vars.json](raw/css-vars.json), not from a PNG pixel.
- **The demo PNG was scaled.** The committed frame is 1440 by 900, scaled from a 2x capture. Placeholders were hidden so empty fields do not look filled. The values were empty.
- **`--color-primary` is `#7699fb`.** The painted home primary button is black. Both are recorded. The painted button is `light.color.primary` (`#000000`).
- **Auth is a different system.** Inter, 6px radius, and a blue Continue. It is not the marketing button. The dark auth hex values are converted from oklch and can be a step off the painted pixel.
- **Hover, pressed, disabled, and loading were not read.** Do not invent them from the 150ms nav transition.
- **bebasNeue, abcSocialMono, and Inter files are not shipped.** The tokens name the families.
- **The homepage product frame is a demo.** Names in it are the site's sample copy.

## Fonts

- **bebasNeue Inline** for marketing headings and the uppercase nav labels. The site serves it. It is licensed and not included. Fallback in the token is Impact, sans-serif.
- **abcSocialMono** for marketing UI and body. Not shipped. Fallback Menlo, Consolas, Courier, monospace.
- **DM Mono** on the open Product menu links.
- **Inter** on `/sign-in` and `/sign-up` only, with the system UI stack.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured from computed page, header, button, and custom properties. Marketing is light. Auth follows the browser scheme. |
| Type roles | Captured. Desktop computed sizes for h1, pricing title, body, and controls. |
| Spacing | Control padding measured (8px 12px 9px on marketing buttons, 0 10px on auth controls). No full spacing scale was declared as tokens beyond the radius and size steps. |
| Radii | Declared scale plus painted 8px controls, 6px auth controls, and a pill toggle. |
| Borders | Marketing buttons are 1px. Auth fields are 0.5px at 12% white in dark. |
| Elevation | Hard offset shadows on marketing buttons. No blur scale. |
| Motion | Nav trigger declares 150ms and `--ease-out-quart`. Reduced motion was requested in the headless capture. A full motion probe was not run. |
| Button | Default primary, secondary, and header Download measured. Hover, pressed, disabled, and loading not measured. |
| Link | Nav and menu links measured at rest. The focused menu item shows the orange outline. |
| Text field | Sign-in email, signup email and password, and the demo fields measured empty. Nothing typed. |
| Text area | Present on the demo page, empty, not submitted. |
| Radio | Team size on the demo page. Not changed. |
| Select, checkbox, switch | Not present on the measured pages. |
| Menu | Product and Resources panels, and the phone drawer, captured. |
| Dialog | The 404 is a card. No marketing dialog was opened. |
| Toast, tooltip, tabs, table, avatar, badge | Not isolated. The pricing "Save 20%" sticker is in the pricing screenshot. |
| Card | Pricing cards and the 404 card. |
| Pricing pattern | Monthly control opened. Checkout not entered. |
| 404 | Captured. |
| Themes | Marketing light only. Auth light and dark captured empty. |
| Widths | Desktop 1440 and phone 390. Home and pricing at both widths. |
| Login and signup walls | Captured empty. Stopped there. `login-extracted` is not-started. |
| Signed-in app | Not captured. |

## Do and don't

1. **Do paint marketing pages white with a black header.** The page is `#ffffff`. The header is `#000000` with white type.
2. **Do use a hard offset on marketing buttons.** Download is black with a gray `-2px 2px` offset. Continue in web is white with a black offset. Radius is 8px.
3. **Do set headings in bebasNeue Inline.** The home h1 is 64px at 1440 with a 64px line height. Body is abcSocialMono.
4. **Do keep the current nav item in capy blue.** The open item paints `#2a44af` (`light.color.link`).
5. **Don't style the app from the marketing buttons.** Sign-in uses Inter, 6px radius, and a blue Continue.
6. **Don't invent a marketing dark theme.** None was on the public site. The dark frames are the auth walls under a dark colour scheme.
7. **Don't follow signup, demo submit, or download from this package.** Those flows were not entered.
8. **Don't ship the wordmark or the font files.** The tokens name the families. The logo stays in the screenshots.

## Health

<!-- health:start -->

Not graded. catalog.json was left alone, so this package is not in the scorecard run.

<!-- health:end -->

## Rebuild

```bash
cd systems/capy
python3 tools/build_tokens.py
python3 tools/test_tokens.py
```

`build_style_guide.py` and `build_components_md.py` are the kit copies. The committed `style-guide.html` and `components.md` were written by hand so the catalog generator did not run.

## Brief

<!-- brief:start -->

Read this before designing in this style. Take every value from [tokens.json](tokens.json), never from the screenshots. catalog.json was not updated, so `python3 tools/catalog.py export capy` will not find this package until a later registration.

### Principles

1. Do paint marketing pages white with a black header.
2. Do use a hard offset on marketing buttons.
3. Do set headings in bebasNeue Inline.
4. Do keep the current nav item in capy blue.
5. Don't style the app from the marketing buttons.
6. Don't invent a marketing dark theme.
7. Don't follow signup, demo submit, or download from this package.
8. Don't ship the wordmark or the font files.

Each rule links the screenshot or crop that shows it, under [Do and don't](#do-and-dont).

### Using tokens

| Role | light |
|---|---|
| page | #ffffff `light.color.page` |
| text | #000000 `light.color.ink` |
| muted | #6d6d6d `light.color.muted` |
| accent | #7699fb `light.color.accent` |
| link | #2a44af `light.color.link` |
| header | #000000 `light.color.header` |

Fonts: `core.font.family.display` is bebasNeue Inline; `core.font.family.body` is abcSocialMono. The display step is 64px.

### Using components

Read [components.md](components.md) for the component inventory and [patterns.md](patterns.md) for how components combine into screens. Crops are in [components/crops/](components/crops). [style-guide.html](style-guide.html) renders the swatches and a drawn hero.

### Accessibility

| Theme | text on page | muted on page |
|---|---|---|
| light | #000 on #fff, passes 4.5:1 | #6d6d6d on #fff, passes 4.5:1 |

Focus: the Product menu link outline is `#e59700`, 1px, offset 1px.

<!-- brief:end -->
