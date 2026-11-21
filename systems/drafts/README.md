# Drafts public surface

A token set and page captures for Drafts' public marketing site at **https://getdrafts.com/**. First capture of this product into `systems/drafts/` on **2026-11-22**, signed out, in an incognito preview tab. Desktop is **1440 by 900** at devicePixelRatio 2 (PNG 2880 by 1800, or the full page height when the shot is full length). Phone is **390 by 844** at devicePixelRatio 2 (PNG 780 by 1688). The site tree is [site-tree.md](site-tree.md).

origin/main did not have `systems/drafts/`. This is a new package. The slug did not change from the product name. `catalog.json` and `webapps-manifest.json` were left alone, so `login-extracted` stays `not-started`. `systems/drafts-ios/` was not touched.

The marketing site paints **one light theme**. `color-scheme` on the root was `normal`. There is no theme control on the public header. The cover photograph is blue. The page below it is white. The footer is a darker blue.

**Boundary.** No public login or signup wall exists. `/login` and `/signup` rewrite to the Oops page. Closed theme-demo modals in the homepage source were not opened. Nothing was typed. Nothing was submitted. App Store links were not followed. Docs, the directory, the community, and the script reference were photographed at the first viewport only.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, drawer, and footer controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | No public login or signup wall. login-extracted is not-started. |
| [icon.png](icon.png) | 128px favicon, resized from android-chrome-192x192.png. |
| [tokens.json](tokens.json) | W3C tokens. `core` holds type, radii, and space. `light` holds the painted marketing roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | Swatches, the section heading, and the error-page button. |
| [components.md](components.md) | Component inventory and gaps. No crops. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [components/](components/) | `crops/` is empty. Element shots are the full pages in `screenshots/`. |
| [icons/](icons/) | `INDEX.tsv` only. UI SVGs were not exported. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. 13 PNGs. |
| [raw/](raw/) | [measured.json](raw/measured.json), the homepage and error-page readings. |
| [tools/](tools/) | `build_tokens.py` and `build_style_guide.py`. |

## Brief

Hand-written. `make brief` was not run, because that reads `catalog.json` and this package is not registered.

1. Paint the page white and the ink near-black.
2. Set the section heading in the system sans at 48/57.6, weight 400.
3. Fill the primary action with the declared blue, at a 6px radius.
4. Keep the cover as a photograph. Do not flatten it to the sampled blue.
5. Do not invent a signed-in editor from this package.

## Health

Not graded. `catalog.json` was left alone, so `make grade` was not run. Layout gaps: no component crops, icons are an index only.

## How the values were read

Computed style was read in a headless Chromium at 1440×900, devicePixelRatio 2, on `https://getdrafts.com/` and on `https://getdrafts.com/error`. The readings are in [raw/measured.json](raw/measured.json). Colour tokens for ink, the button, and the footer are those computed values. The cover sample is a 6×6 patch from the full-colour homepage PNG before quantize, because the cover is a photograph.

`tools/build_tokens.py` copies those readings into `tokens.json`. It does not sample the quantised screenshots.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. The cover photograph and the product shots band. Read colours from [tokens.json](tokens.json), not from a PNG pixel.
- **The cover sample is rgb(15, 65, 126).** The cover is a gradient photograph. Do not paint a flat hero with that one sample.
- **`--bs-primary` is #335eea.** The error-page button computed as rgb(51, 94, 234), which is the same blue. The footer is rgb(23, 57, 115), which is not that primary.
- **Hover, pressed, disabled, and loading were not read.** Do not invent them.
- **The h1 size is the 1440 reading.** It wraps on the phone. Do not treat 48px as the phone size.
- **There is no signed-in shell in this package.** There is no public login wall.
- **The system sans is not shipped.** The tokens name the computed stack.
- **The device collage is a public illustration.** Text inside those product shots is the site's sample copy.
- **Closed theme modals are not the product.** "Sign Up", "Schedule a demo", and "Add Payment" in the homepage source are unused Landkit leftovers. They were not opened.

## Fonts

- **System sans** for headlines, body, nav, and buttons. The computed stack is `-apple-system`, `"system-ui"`, `"Segoe UI"`, Roboto, `"Helvetica Neue"`, Arial, sans-serif. Not included.
- **Feather** is loaded as an icon font (`Feather.ttf`). Icon glyphs in the feature cards come from it. The font file was not copied into the package.

## Coverage

| Item | Status |
|---|---|
| Page colour, ink, muted, nav, cover sample, footer, CTA | Captured. [tokens.json](tokens.json), [screenshots/home-desktop.png](screenshots/home-desktop.png) |
| Type roles | Captured for display, body, and nav. Other sizes not measured. |
| Spacing and radii | Captured for the error-page button and the feature card. The rest of the scale was not measured. |
| Elevation | Card shadow captured as a computed value. Not tokenised beyond the reading. |
| Motion | Not captured. |
| Button | Captured default on the error page. Hover, focus, pressed, disabled, loading not captured. |
| Link | Captured as nav, footer, and award links. |
| Text field | Not present on the painted public pages. Closed theme modals were not opened. |
| Menu | Captured open on desktop and on the phone drawer. |
| Card | Feature cards on the homepage. |
| Empty | Oops page. [screenshots/not-found.png](screenshots/not-found.png) |
| Light theme | Captured. |
| Dark theme | Not present on the marketing site. The script reference has a theme control. It was not switched. |
| Desktop 1440 and phone 390 | Captured for the homepage. Phone menu captured. Other pages are desktop only. |
| Pricing | Not present. |
| Login and signup | Not present as public pages. login-extracted is not-started. |
| Signed-in app | Not captured. The product is an Apple app. |

## Do and don't

- **Paint the page white and the ink near-black.** The homepage h1 is rgb(22, 28, 45) on rgb(255, 255, 255). See [screenshots/home-desktop.png](screenshots/home-desktop.png).
- **Set section headings in the system sans at 48px, weight 400.** See the same shot.
- **Fill the recovery action with the primary blue, at 6px.** Drafts Home on the Oops page is rgb(51, 94, 234) with white type. See [screenshots/not-found.png](screenshots/not-found.png).
- **Don't flatten the cover to one blue.** The cover is a photograph. The sample in the tokens is one patch.
- **Don't style a signed-in editor from this package.** There is no public login wall. The device collage is an illustration.

## Rebuild

```bash
cd systems/drafts && python3 tools/build_tokens.py && python3 tools/build_style_guide.py
```

`make design-md` and `make brief` were not run. They rewrite catalog-backed files, and `catalog.json` was left alone.
