# Cursor public site

A token set and page captures for Cursor's public marketing site at **https://cursor.com**. First capture of this product into `systems/cursor/` on **2026-11-22**, signed out. Desktop is **1440 by 900** at devicePixelRatio 1. Phone is **390 by 844** at devicePixelRatio 2 (PNG width 780). The site tree is [site-tree.md](site-tree.md).

`origin/main` did not have `systems/cursor/`. [systems/cursor-desktop](../cursor-desktop) and [systems/cursor-ios](../cursor-ios) were not edited. `catalog.json` was left alone, so `login-extracted` stays `not-started`. This README's Brief and Health are hand-written. `make design-md` was not run, because that would rewrite the catalog.

The marketing site paints **one dark theme**. There is no theme control. The homepage stylesheet declares **642 custom properties**. Login is a separate app at authenticator.cursor.sh.

**Boundary.** The login wall was photographed empty. Signup stopped on a Cloudflare verification page. The checkbox was not clicked. Nothing was typed. Nothing was submitted. Google, GitHub, Apple, Grok, and X were not clicked.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, menu, drawer, footer and wall controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | Empty login wall. Signup stopped at a captcha. login-extracted is not-started. |
| [icon.png](icon.png) | The 192px marketing icon from cursor.com, scaled to 128px. |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds declared swatches, radii, and type. `dark` holds the painted roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | A page that renders the declared swatches and the light Download pill. |
| [components.md](components.md) | Component inventory and gaps. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [icons/](icons/) | `INDEX.tsv` only. UI SVGs were not exported. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone, plus the empty login wall. |
| [raw/](raw/) | The stylesheet readings. |
| [tools/](tools/) | `build_tokens.py`, `build_style_guide.py`, `build_components_md.py`, and the capture script under `tools/capture/`. |

## Brief

Dark page `#14120b`, text `#edecec`, accent `#f54e00`. Primary actions are light pills. One theme. Details are in [tokens.json](tokens.json).

## Health

Not graded. `catalog.json` was left alone, so this package is not in the scorecard yet.

## How the values were read

Declared custom properties were read in headless Chromium on the live homepage and written to [raw/css-vars.json](raw/css-vars.json). Computed body, h1, and button styles are in [raw/home-computed.json](raw/home-computed.json). Colour tokens are the declared hex. Mixes and `lab()` ramps were not converted. The nav Download button colours are the computed `rgb()` values, which match the declared page and foreground.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. Read colours from the tokens, not from a PNG pixel.
- **The login shot is scaled.** It came from a 2x preview frame and was resized to 1440 by 900. Headless Chromium hit a Cloudflare wall on the same URL.
- **Hover, pressed, disabled, and loading were not read.** Do not invent them.
- **Teams pricing was not switched.** Individual is the painted tab.
- **Secondary text is the declared `#d7d6d5`.** The 60% mix named `--color-theme-text-sec` was not resolved.
- **CursorGothic is not shipped.** The tokens name the family.
- **Homepage product frames are demos.** They are not a signed-in account.

## Fonts

- **CursorGothic** for marketing UI, headings, and body. The site serves it. It is licensed and not included. Fallback in the token is system-ui, Helvetica Neue, Helvetica, Arial, sans-serif.
- **cursorDisplay** is declared as `--font-cursor-display`. The painted h1 used CursorGothic.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured. Dark page, card, text, accent, success, danger. One theme. |
| Type roles | Captured. Desktop computed size for the home h1 and body. |
| Spacing | Button padding measured. The rest of the spacing scale was not tokenised. |
| Radii | Declared scale plus the painted pill button. |
| Borders | Declared as mixes of the foreground. Not resolved to hex. |
| Elevation | Not measured. |
| Motion | Not measured. |
| Button | Default primary and ghost measured at rest. Hover, focus, pressed, disabled, and loading not measured. |
| Link | Nav and footer links observed. Hover not measured. |
| Text field | Login email field measured empty. Nothing typed. |
| Text area, checkbox, radio, switch, select | Not present on the measured pages. The Cloudflare checkbox was not clicked. |
| Tabs | Pricing Individual and Teams observed. Individual painted. Teams not switched. |
| Menu | Desktop destinations read from the header. Phone drawer photographed. |
| Card | Pricing and download cards captured. |
| Badge | Most popular observed on Premium. |
| Avatar, list row, table, toast, tooltip, dialog | Not captured. The cookie dialog was removed, not accepted. |
| 404 | Captured. |
| Themes | Dark only. No public light theme. |
| Widths | Captured. Desktop 1440 and phone 390. Homepage at both widths. |
| Login wall | Captured empty. Stopped there. |
| Signup wall | Not captured. Cloudflare verification. Checkbox not clicked. |
| Signed-in app | Not captured. `login-extracted` is not-started. |

## Do and don't

- **One dark page.** The public site does not offer a light theme. [home-dark-default.png](screenshots/home-dark-default.png).
- **The accent is orange, the button is a light pill.** Do not paint the Download button orange. [home-dark-default.png](screenshots/home-dark-default.png).
- **Stop at the login wall.** The empty email field is the boundary. [login-dark-empty.png](screenshots/login-dark-empty.png).

## Rebuild

```bash
cd systems/cursor && python3 tools/build_tokens.py && python3 tools/build_style_guide.py && python3 tools/build_components_md.py
```

`catalog.json` was left alone, so `make brief` and `make design-md` were not run.
