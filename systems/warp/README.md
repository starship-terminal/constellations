# Warp public surface

A token set and page captures for Warp's public marketing site at **https://www.warp.dev/**. First capture of this product into `systems/warp/` on **2026-11-22**, signed out, in an incognito preview tab. Desktop is **1440 by 900** at devicePixelRatio 2 (PNG 2880 by 1800). Phone is **390 by 844** at devicePixelRatio 2 (PNG 780 by 1688). The site tree is [site-tree.md](site-tree.md).

origin/main did not have `systems/warp/`. This is a new package. The slug did not change from the product name. `catalog.json` and `webapps-manifest.json` were left alone, so `login-extracted` stays `not-started`. `systems/warp-desktop/` was not touched.

The marketing site paints **one light theme**. `color-scheme` on the root was `normal`. There is no theme control on the public header. The login and signup walls paint a black card. That black is the auth surface, not a site-wide dark theme.

**Boundary.** Login and signup were photographed empty. Nothing was typed. Nothing was submitted. Continue with email, GitHub, Google, ChatGPT, and SSO were not clicked. The download binary was not fetched. Docs, status, and social hosts were not opened.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, drawer, footer, pricing, and download controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | Empty login and signup walls. login-extracted is not-started. |
| [icon.png](icon.png) | 128px favicon from www.warp.dev/favicon-128x128.png. |
| [tokens.json](tokens.json) | W3C tokens. `core` holds type, radii, and space. `light` holds the painted marketing roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | Swatches, the headline, the early-access button, and the yellow pill. |
| [components.md](components.md) | Component inventory and gaps. No crops. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [components/](components/) | `crops/` is empty. Element shots are the full pages in `screenshots/`. |
| [icons/](icons/) | `INDEX.tsv` only. UI SVGs were not exported. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. 31 PNGs. |
| [raw/](raw/) | [measured.json](raw/measured.json), the homepage readings. |
| [tools/](tools/) | `build_tokens.py` and `build_style_guide.py`. |

## Brief

Hand-written. `make brief` was not run, because that reads `catalog.json` and this package is not registered.

1. Paint the marketing page near-white and the ink near-black.
2. Set the headline in Azeret SemiMono at 54/64, weight 400.
3. Fill the primary action with the same ink, at a 4px radius.
4. Use the yellow pill for Book a demo, not the declared cyan accent.
5. Do not invent a signed-in terminal from this package.

## Health

Not graded. `catalog.json` was left alone, so `make grade` was not run. Layout gaps: no component crops, icons are an index only.

## How the values were read

Computed style was read in the incognito preview tab on `https://www.warp.dev/` at 1440×900, devicePixelRatio 2. The readings are in [raw/measured.json](raw/measured.json). Colour tokens for ink, buttons, and nav are those computed values. The page fill and the announcement bar were sampled from the full-colour PNG before quantize, because the page background is transparent over an oklch wash.

`tools/build_tokens.py` copies those readings into `tokens.json`. It does not sample the quantised screenshots.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. The factory-grid demo and photographs band. Read colours from [tokens.json](tokens.json), not from a PNG pixel.
- **The yellow pill computed as rgb(237, 248, 114).** A pixel in the full-colour shot was rgb(239, 248, 133). Use the computed value.
- **`--color-theme-accent` is #00c2ff.** It is declared. The painted marketing accent is the yellow pill. Do not swap them.
- **Hover, pressed, disabled, and loading were not read.** Do not invent them.
- **The h1 size is the 1440 reading.** It wraps on the phone. Do not treat 54px as the phone size.
- **There is no signed-in shell in this package.** Login and signup stop at the empty card.
- **Azeret SemiMono, Matter, and theFuture are not shipped.** The tokens name the families.
- **The factory grid is a public demo.** Task names in it are the site's sample copy.

## Fonts

- **Azeret SemiMono** for the headline, nav, and buttons. The computed stack is `azeretSemiMono`, then a fallback, then `"Azeret SemiMono"`, then ui-monospace. Not included.
- **Matter** for body. The computed stack is Matter, system-ui, sans-serif. Not included.
- **theFuture** is declared as `--font-display`. It was not the painted headline. Not included.

## Coverage

| Item | Status |
|---|---|
| Page colour, text, muted, nav, CTA, demo pill | Captured. [tokens.json](tokens.json), [screenshots/home-desktop.png](screenshots/home-desktop.png) |
| Type roles | Captured for display, body, and nav. Other sizes not measured. |
| Spacing and radii | Captured for the two buttons. The rest of the scale was not measured. |
| Elevation, motion | Not captured. Duration `.15s` is declared and was not timed. |
| Button | Captured default. Hover, focus, pressed, disabled, loading not captured. |
| Link | Captured as nav and footer links. |
| Text field | Captured empty on login, signup, get-started, and contact sales. Not typed. |
| Menu | Captured open for Products, Enterprise, Resources, Sign in, Get started, and the phone drawer. |
| Tabs | Pricing product tabs and the annual toggle. Monthly was not selected. |
| Dialog | Phone menu. No other dialog was opened. |
| Card | Pricing cards and the auth card. |
| Empty | 404. [screenshots/not-found.png](screenshots/not-found.png) |
| Light theme | Captured. |
| Dark theme | Not present on the marketing site. The auth card is black. |
| Desktop 1440 and phone 390 | Captured for the homepage. Phone menu captured. Other pages are desktop only. |
| Login and signup | Photographed empty. Stopped. login-extracted is not-started. |
| Signed-in app | Not captured. |

## Do and don't

- **Paint the page near-white and the ink near-black.** The homepage h1 is rgb(26, 21, 34) on a sampled page of rgb(254, 253, 254). See [screenshots/home-desktop.png](screenshots/home-desktop.png).
- **Set display type in Azeret SemiMono.** The h1 is 54px, weight 400. See the same shot.
- **Fill the primary action with ink, and keep Book a demo yellow.** request early access is rgb(26, 21, 34) at 4px. Book a demo is rgb(237, 248, 114) as a pill. See [screenshots/home-desktop.png](screenshots/home-desktop.png).
- **Don't style a signed-in terminal from this package.** The login wall is [screenshots/login-wall.png](screenshots/login-wall.png). The fields were empty. The app was not opened.
- **Don't treat the factory grid as a live account.** It is a public demo on the homepage.

## Rebuild

```bash
cd systems/warp && python3 tools/build_tokens.py && python3 tools/build_style_guide.py
```

`make design-md` and `make brief` were not run. They rewrite catalog-backed files, and `catalog.json` was left alone.
