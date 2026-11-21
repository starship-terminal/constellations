# Obsidian design reference

Tokens and component notes for the public Obsidian marketing site at [obsidian.md](https://obsidian.md/). Captured 2026-11-22. Desktop screenshots are 1440×900 CSS pixels at device pixel ratio 2. The phone homepage is 390×844 CSS pixels at device pixel ratio 2. The site stayed dark. `color-scheme` was `dark` and the body class was `theme-dark`.

This package is the public web site. origin/main did not have `systems/obsidian/`. The slug is `obsidian`. `catalog.json` and `webapps-manifest.json` were left alone, so `login-extracted` stays `not-started`.

Public marketing pages, the header, the footer, pricing, sync, download, the phone homepage and its menu, the 404 page, and the signed-out login and signup walls only. No account was created. No email, name, or password was typed. No identity provider was clicked. No form was submitted. No checkout was entered. No download was kept.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [icon.png](icon.png) | The site icon, 128px, resized from `/favicon.ico`. |
| [tokens.json](tokens.json) | DTCG tokens. `core` holds type, radius, and space. `dark` holds the semantic roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. The catalog generator was not run. |
| [style-guide.html](style-guide.html) | Renders the token roles. Inter is not loaded. |
| [components.md](components.md) | Measured controls, and the gaps. |
| [patterns.md](patterns.md) | How the public pages are built, and where they stop. |
| [site-tree.md](site-tree.md) | Which header and footer controls open which pages and walls. |
| [login-review.json](login-review.json) | Empty login and signup walls. login-extracted is not-started. |
| [components/](components/) | Crop folder. Element crops were not cut. The page screenshots hold the controls. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. |
| [raw/](raw/) | Computed styles from the homepage. |
| [tools/](tools/) | `test_tokens.py`. |

## How the values were read

Computed styles were read with `getComputedStyle` on `https://obsidian.md/` on 2026-11-22 at 1440×900: the html element, the body, the first `h1`, the lead paragraph, the Pricing link, and Get Obsidian for macOS. Colour roles come from those computed colours. `--color-accent-600` is declared as `#7c3aed` and matches the computed button fill.

## What to distrust

The marketing sans is the system stack: ui-sans-serif, system-ui, then Roboto, Inter, Helvetica Neue, Arial. Inter is named in the stack. The file is not in this package. The capture browser resolved the system sans.

The header background is transparent. The page fill is the html background, `#0f0f0f`. The body background computed as transparent.

The display token is the hero at 1440. At 390 the same heading computed at 50.7px. Do not treat 60px as the phone size.

Screenshots are 256-colour PNGs. Long pages were cropped to the first 900 CSS pixels after the page had loaded. Read colours from `tokens.json`, not from the images.

A light marketing theme was not on these pages. The declared `--color-primary` is `#0F0F0F`, the same dark page fill.

## Fonts

The computed family is ui-sans-serif, system-ui, -apple-system, system-ui, Roboto, Inter, Helvetica Neue, Arial, Noto Sans, sans-serif. Inter is not in this package. The tokens fall back to the system sans.

## Coverage

| Item | Status |
|---|---|
| Colour, type, space, radius | Captured from computed styles. [tokens.json](tokens.json) |
| Dark theme | Captured. Page background `#0f0f0f`. Body class `theme-dark`. |
| Light theme | Not present on the public marketing pages that were opened. |
| Desktop 1440 | Captured for home, pricing, sync, publish, enterprise, download, canvas, mobile, help, changelog, about, roadmap, blog, privacy, terms, security, the 404 page, and both auth walls. |
| Phone 390 | Captured for the homepage, closed and with the menu open. [screenshots/home-dark-phone.png](screenshots/home-dark-phone.png) |
| Button, link, text field | Observed on public pages and the empty auth walls. See [components.md](components.md). |
| Checkbox, radio, switch, select, toast, table, dialog | Not present on the pages that were opened. |
| Pricing | Captured. Sync $4 and Publish $8, yearly monthly equivalents. Monthly $5 and $10 were visible and not selected. [screenshots/pricing-dark-desktop.png](screenshots/pricing-dark-desktop.png) |
| Sync | Captured. [screenshots/sync-dark-desktop.png](screenshots/sync-dark-desktop.png) |
| Download page | Captured. The dmg, exe, apk, and store links were not fetched. [screenshots/download-dark-desktop.png](screenshots/download-dark-desktop.png) |
| Empty state | Captured. A missing path shows "404" and "You found an unresolved link." [screenshots/not-found-dark-desktop.png](screenshots/not-found-dark-desktop.png) |
| Signed-in app | Not entered. `login-extracted` is not-started. |
| Loading, error on a form | Not shown. Forms were not submitted. |

## Do and don't

- **Do paint the page `#0f0f0f`.** The headline is `#eeeeee` at 60px, weight 600, letter-spacing -1.2px. [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)
- **Do paint Get Obsidian for macOS as a `#7c3aed` button.** The radius is 8px. The label is white. The control is 60px tall. [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)
- **Do keep nav labels muted.** Pricing is `#bcbcbc` at 14px, weight 500. [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)
- **Don't invent a light marketing theme.** The public pages that were opened stayed on `theme-dark`.
- **Don't treat the homepage note mock as the signed-in app.** It is a marketing demo. [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)
- **Don't click through the login wall.** Email and Password were empty. Sign in was not clicked. [screenshots/login-wall-dark-desktop.png](screenshots/login-wall-dark-desktop.png)
- **Don't follow Download into a file.** The macOS control starts a dmg. The file was not kept.
- **Don't ship an Inter file.** The computed stack names it. The capture used the system sans.

## Rebuild

```bash
python3 tools/test_tokens.py
```

`tokens.json` and `DESIGN.md` were written from the readings in [raw/](raw/). `catalog.json` was left alone, so `make design-md` was not run for this package.
