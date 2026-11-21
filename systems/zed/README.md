# Zed public surface

A token set and page captures for Zed's public marketing site at **https://zed.dev/**. First capture of this product into `systems/zed/` on **2026-11-22**, signed out. Desktop is **1440 by 900** at devicePixelRatio 1. Phone is **390 by 844** at devicePixelRatio 1. The site tree is [site-tree.md](site-tree.md).

origin/main did not have `systems/zed/`. This is a new package. `systems/zed-desktop/` was left alone. `catalog.json` was left alone, so `login-extracted` stays `not-started` and this README's Brief and Health are hand-written.

The marketing site paints **light and dark**. The root class follows the browser colour scheme. A command menu can switch the theme. That menu was opened and not used. The homepage hero is "Your last next editor". Download now is a blue pill. The footer is a blue band.

**Boundary.** `/sign_in` redirects to GitHub's login, photographed empty. `/sign_up` stays on zed.dev, photographed empty, with an unsolved Cloudflare check. Nothing was typed. Nothing was submitted. Google, Apple, and GitHub were not clicked. The download binaries were not kept.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, menu, drawer, footer and download controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | Empty sign-in and sign-up walls. login-extracted is not-started. |
| [icon.png](icon.png) | 128px raster of `/favicon_white_64.png` on the measured dark page. |
| [tokens.json](tokens.json) | W3C tokens. `core` holds type, radius, and the sampled blues. `dark` and `light` hold the painted roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | Swatches and the download pill in both themes. |
| [components.md](components.md) | What was on the signed-out pages. |
| [patterns.md](patterns.md) | How the homepage, download page, docs landing and auth walls are put together. |
| [components/](components/) | Empty of crops. Element shots are the full pages in `screenshots/`. |
| [icons/](icons/) | `INDEX.tsv` only. UI SVGs were not exported. |
| [screenshots/](screenshots/) | Quantised page shots. 18 PNGs. |
| [raw/](raw/) | The computed readings and the menu map. |
| [tools/](tools/) | `build_tokens.py` checks the token file against the readings. |

## How the values were read

Computed style was read in headless Chromium on the live homepage at 1440, dark scheme, then written to [raw/measure.json](raw/measure.json). The download blue `#1348dc` and the footer blue `#164adc` were sampled from the full-colour PNGs before quantize. Light page `#f4f4f2` was sampled the same way. Declared custom properties on `:root` were six motif colours, recorded in that file.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. The editor demo bands. Read colours from the tokens and from [raw/measure.json](raw/measure.json), not from a PNG pixel.
- **The download blue and the footer blue are not the same pixel.** Download now sampled `#1348dc`. The footer band sampled `#164adc`. `--motif-accent-1` is `#1e69f6`, a third blue.
- **The h1 colour is a computed lab value.** It was not converted to hex.
- **Hover, pressed, disabled, and loading were not read.** Do not invent them.
- **The home h1 size is the 1440 reading.** Do not treat 48px as the phone size.
- **The editor mock is a public demo.** It is not a signed-in account.
- **writer and plexSerif are the site's families.** They are not shipped.

## Fonts

- **plexSerif** for the homepage headline. 48px, weight 320, line height 57.6px at 1440. Not included.
- **writer** for body, nav, and buttons. 16px body, 14px controls. Not included.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured for page, text, text-strong, accent, and on-accent in dark. Light page and h1 captured. Status colours not isolated. |
| Type roles | Captured for the home h1, the download button, and the Docs nav link. |
| Spacing | Button padding measured: 0 6px 0 10px. No full scale. |
| Radii | Button 4px. |
| Borders | Clone source uses a 1px translucent border. Not tokenised beyond the reading. |
| Elevation | Not measured. |
| Motion | Reduced motion was requested in the capture browser and not compared. |
| Button | Download now and Clone source measured at rest. Hover, focus, pressed, disabled, and loading not measured. |
| Link | Nav and footer links observed. Hover not measured. |
| Text field | Docs search and the download newsletter field were on screen and left empty. GitHub username and password were empty. Not typed. |
| Text area, select, checkbox, radio, switch | Pricing has a Free Trial switch, photographed, not toggled. Signup has two unchecked boxes, not clicked. |
| Tabs | Download has Stable and Preview. Stable was selected. Preview was not opened. Docs has a sidebar, not tabs. |
| Menu | Product, Resources, the command menu, and the phone drawer captured. |
| Dialog | Command menu captured empty. Watch Demo was not played. |
| Card | Pricing plan cards and extension cards captured. |
| Badge, avatar, list row, table, toast, tooltip | Not isolated. Extension cards show a download count. |
| 404 | Captured. "Page Not Found." |
| Themes | Light and dark both paint. Command menu offers a theme switch. That row was not clicked. |
| Widths | Desktop 1440 and phone 390. Home at both. Phone menu open. |
| Login and signup walls | Captured empty. `login-extracted` is not-started. |
| Signed-in app | Not captured. |
| Download | Public. Version 1.29.2. Binary not kept. |

## Do and don't

1. **Do paint the dark page near `#141519`.** The body computed colour is `rgb(17, 18, 22)`.
2. **Do set the home headline in plexSerif at 48px, weight 320.** The line height is 57.6px at 1440.
3. **Do fill Download now with the sampled blue and white type.** The fill pixel is `#1348dc`. The label is `#ffffff`. Radius is 4px.
4. **Do keep Clone source quiet.** It sits on a 5% fill with a hairline border, not the blue.
5. **Do paint the footer as its own blue band.** That band sampled `#164adc`, not the button blue and not `--motif-accent-1`.
6. **Do not invent a signed-in editor from the homepage demo.** The mock is the site's illustration. The real editor is `systems/zed-desktop/`.

## Brief

Hand-written. `make brief` was not run, because that rewrites the catalog.

Read [tokens.json](tokens.json) before designing in this style. The dark page is `#141519`. The accent used on Download now is `#1348dc`. Display type is plexSerif at 48/57.6, weight 320. Controls are writer at 14/20, radius 4px.

## Health

Hand-written. `make grade` was not run, because that rewrites the catalog.

Not graded. `login-extracted` is not-started. The signed-in app was not entered.

## Rebuild

```bash
cd systems/zed && python3 tools/build_tokens.py
```

`build_tokens.py` checks `tokens.json` against `raw/measure.json`. It does not fetch the site. `make design-md` was not run on this pass, because it rewrites the catalog.
