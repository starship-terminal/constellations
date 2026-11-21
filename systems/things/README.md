# Things public surface

A token set and page captures for the Things marketing site at **https://culturedcode.com/things/**. First capture of this product into `systems/things/` on **2026-11-22**, signed out, in an incognito preview tab. Desktop is **1440 by 900** at devicePixelRatio 2 (PNG 2880 by 1800). Phone is **390 by 844** at devicePixelRatio 2 (PNG 780 by 1688). The site tree is [site-tree.md](site-tree.md).

origin/main did not have `systems/things/`. This is a new package. The slug did not change from the product name. `catalog.json` and `webapps-manifest.json` were left alone, so `login-extracted` stays `not-started`. `systems/things-ios/` was not touched.

The marketing site paints **one light theme**. `color-scheme` on the root was `normal`. There is no theme control on the public header.

**Boundary.** No public login or signup wall exists. `/login/`, `/signin/`, `/signup/`, and `/account/` are the public 404. `https://cloud.culturedcode.com/` returned an empty document. Nothing was typed. Nothing was submitted. The trial zip was not downloaded. The Mac App Store listing was photographed. Buy was not clicked.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, footer, buy, and download controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | No public wall. login-extracted is not-started. |
| [icon.png](icon.png) | 128px PNG scaled from the 180px apple-touch-icon on culturedcode.com. |
| [tokens.json](tokens.json) | W3C tokens. `core` holds type and radii. `light` holds the painted marketing roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | Swatches, the heading, the Subscribe button, and the link blue. |
| [components.md](components.md) | Component inventory and gaps. No crops. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [components/](components/) | `crops/` is empty. Element shots are the full pages in `screenshots/`. |
| [icons/](icons/) | `INDEX.tsv` only. UI images were not exported. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. 19 PNGs. |
| [raw/](raw/) | [measured.json](raw/measured.json), the homepage readings. |
| [tools/](tools/) | `build_tokens.py` and `build_style_guide.py`. |

## Brief

Hand-written. `make brief` was not run, because that reads `catalog.json` and this package is not registered.

1. Paint the marketing page a cool light gray, rgb(242, 245, 247), and the ink rgb(48, 51, 54).
2. Set section headings at 36px, weight 700, in the system sans stack.
3. Paint links and the play control rgb(92, 156, 245).
4. Fill Subscribe with rgb(79, 145, 251) and white type, at about an 8px radius.
5. Do not invent a signed-in Things Cloud account from this package.

## Health

Not graded. `catalog.json` was left alone, so `make grade` was not run. Layout gaps: no component crops, icons are an index only.

## How the values were read

Computed style was read in the incognito preview tab on `https://culturedcode.com/things/` at 1440×900, devicePixelRatio 2. The readings are in [raw/measured.json](raw/measured.json). Colour tokens are those computed values. The page fill is the computed body background, not a pixel sample.

`tools/build_tokens.py` copies those readings into `tokens.json`. It does not sample the quantised screenshots.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. Photographs and the product collage band. Read colours from [tokens.json](tokens.json), not from a PNG pixel.
- **The word Things is an image.** The h1 is visually hidden at 1px. Do not treat a computed h1 size as the wordmark.
- **Hover, pressed, disabled, and loading were not read.** Do not invent them. Focus was read once: the header link outline is rgb(229, 151, 0).
- **The heading size is the 1440 reading.** It wraps on the phone. Do not treat 36px as the phone size.
- **There is no signed-in shell in this package.** The cloud host returned an empty document. Account setup is in the native apps.
- **The system font stack is not a shipped file.** Roboto is named as a fallback. It was not downloaded.
- **The quote names are public posts on the page.** They are the site's illustration.

## Fonts

- **System sans.** The computed stack is ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif. Not included.
- **No display family was declared.** The wordmark is a PNG.

## Coverage

| Item | Status |
|---|---|
| Page colour, ink, muted, nav, link, button | Captured. [tokens.json](tokens.json), [screenshots/home-desktop.png](screenshots/home-desktop.png) |
| Type roles | Captured for heading, body, and nav. The wordmark is an image. |
| Spacing and radii | Captured for the button, the field, the nav link, and the product card. The rest of the scale was not measured. |
| Elevation, motion | Not captured. Product cards have no computed shadow. |
| Button | Captured default. Hover, pressed, disabled, loading not captured. |
| Link | Captured as nav, See features, and footer links. |
| Text field | Captured empty on the newsletter. Support search captured empty. Not typed. |
| Menu | Not present. The header is four links at 1440 and at 390. |
| Tabs | Features has Mac and iOS switches. Not opened. |
| Dialog | Not present on the pages opened. The video control was not clicked. |
| Card | Product cards and quote cards. |
| Empty | 404. [screenshots/not-found.png](screenshots/not-found.png) |
| Light theme | Captured. |
| Dark theme | Not present on the marketing site. |
| Desktop 1440 and phone 390 | Captured for the homepage. Other pages are desktop only. |
| Login and signup | No public wall. Cloud host returned an empty body. login-extracted is not-started. |
| Signed-in app | Not captured. Native apps were not opened. |

## Do and don't

- **Paint the page cool gray and the ink near-black.** Body is rgb(242, 245, 247). Ink is rgb(48, 51, 54). See [screenshots/home-desktop.png](screenshots/home-desktop.png).
- **Set section headings at 36px, weight 700.** See the same shot, heading "Simply Powerful".
- **Paint actions in the blue, and fill Subscribe with the brighter blue.** See features is rgb(92, 156, 245). Subscribe is rgb(79, 145, 251) with white type. See [screenshots/newsletter-empty.png](screenshots/newsletter-empty.png).
- **Keep the wordmark as an image.** Do not restyle it as live type from this package.
- **Don't style a signed-in Things Cloud account from this package.** The marketing page is [screenshots/cloud.png](screenshots/cloud.png). The cloud host had no form.

## Rebuild

```bash
cd systems/things && python3 tools/build_tokens.py && python3 tools/build_style_guide.py
```

`make design-md` and `make brief` were not run. They rewrite catalog-backed files, and `catalog.json` was left alone.
