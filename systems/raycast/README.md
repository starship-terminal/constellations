# Raycast design reference

Tokens and component notes for the public Raycast marketing site at [raycast.com](https://www.raycast.com/). Captured 2026-11-22. Desktop screenshots are 1440×900 CSS pixels at device pixel ratio 2. The phone homepage is 390×844 CSS pixels at device pixel ratio 2. The site stayed dark when `prefers-color-scheme` was light.

This package is the public web site. The desktop app already lives at [systems/raycast-desktop](../raycast-desktop/). That package was not overwritten.

Public marketing pages, the header, the footer, pricing, the store, the Homebrew dialog, the Download V1 dialog, the phone homepage, the 404 page, and the signed-out login and signup walls only. No account was created. No name, username, email, password, or code was typed. No identity provider was clicked. No form was submitted. No download was started. `login-extracted` stays not-started.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [icon.png](icon.png) | The site icon, 128px, resized from `/favicon-production.png`. |
| [tokens.json](tokens.json) | DTCG tokens. `core` holds type, radius, and space. `dark` holds the semantic roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. The catalog generator was not run. |
| [style-guide.html](style-guide.html) | Renders the token roles. Inter is not loaded. |
| [components.md](components.md) | Measured controls, and the gaps. |
| [patterns.md](patterns.md) | How the public pages are built, and where they stop. |
| [site-tree.md](site-tree.md) | Which header and footer controls open which pages, dialogs, and walls. |
| [components/](components/) | Crop folder. Element crops were not cut. The page screenshots hold the controls. |
| [icons/](icons/) | The pixel mark, with [INDEX.tsv](icons/INDEX.tsv). |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. |
| [raw/](raw/) | Computed custom properties from the homepage. |
| [tools/](tools/) | `test_tokens.py`. |

<!-- brief:start -->
<!-- brief:end -->

<!-- health:start -->
<!-- health:end -->

## How the values were read

Custom properties were read from `:root` and from `getComputedStyle(document.documentElement)` on `https://www.raycast.com/` on 2026-11-22. Component sizes come from `getComputedStyle` on the homepage `h1`, the hero paragraph, the Store link, and the Download link. The login wall was measured for its heading and the empty email field. Its identity buttons were not clicked.

## What to distrust

The marketing sans is Inter, with an Inter Fallback. JetBrains Mono is named for `--monospace-font`. Neither file is in this package. The capture browser resolved Inter on the homepage and on the login wall.

`--color-button-bg` is `#ffffffd0`. The Download link computed as `rgb(230, 230, 230)`, which is `--grey-50`. The token and the button are different.

The press page names Brand Red `#FF6363`. The homepage `:root` token `--color-red` is `#ff6161`. `--red-dark` is `#ff6363`. They are close and not the same.

`--navbar-height` is declared as 58px and computed as 76px on the homepage at 1440. The bar box measured 1204×76.

Screenshots are 256-colour PNGs. Long pages were cropped to the first 900 CSS pixels after the page had loaded. Read colours from `tokens.json`, not from the images.

Setting `prefers-color-scheme: light` did not switch the page. Body background stayed `rgb(7, 8, 10)`.

## Fonts

The stylesheet names Inter for `--main-font` and JetBrains Mono for `--monospace-font`. Geist Mono is also preloaded. The files are not in this package. The tokens fall back to the system sans and the system mono.

## Coverage

| Item | Status |
|---|---|
| Colour, type, space, radius | Captured from custom properties and computed styles. [tokens.json](tokens.json) |
| Dark theme | Captured. Page background `#07080a`. |
| Light theme | Not present on the public marketing pages. `prefers-color-scheme: light` left the page dark. |
| Desktop 1440 | Captured for home, store, pro, AI, iOS, Windows, teams, enterprise, blog, pricing, changelog, the MCP changelog entry, browser extension, developers, FAQ, privacy, terms, press, feedback, careers, customers, manifesto, notes, guides, manual, wallpapers, the 404 page, both dialogs, and both auth walls. |
| Phone 390 | Captured for the homepage. The header wraps. There is no menu button. [screenshots/home-dark-phone.png](screenshots/home-dark-phone.png) |
| Button, link, dialog, card, text field | Observed on public pages. See [components.md](components.md). |
| Checkbox, radio, switch, tabs, toast, table, select | The feedback page has a category select. The other controls were not present on the pages that were opened. |
| Pricing | Captured. [screenshots/pricing-dark-desktop.png](screenshots/pricing-dark-desktop.png) |
| Store | Captured. [screenshots/store-dark-desktop.png](screenshots/store-dark-desktop.png) |
| Download page | Not present as a page. `/download/mac` starts a file. The file was not saved. Homebrew and V1 are dialogs. |
| Empty state | Captured. A missing path shows "Page not found". [screenshots/not-found-dark-desktop.png](screenshots/not-found-dark-desktop.png) |
| Signed-in app | Not entered. `login-extracted` is not-started. |
| Loading, error on a form | Not shown. Forms were not submitted. |

## Do and don't

- **Do paint the page `#07080a`.** The navbar is a 1204px pill on that field. [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)
- **Do set the headline in Inter at 64px, weight 600, line-height 70.4px.** The copy is "Your shortcut to everything." [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)
- **Do paint Download as a light pill.** The radius is 8px. The fill measured `rgb(230, 230, 230)`. The label is 14px, weight 500. [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)
- **Do keep Store through Pricing as quiet 14px links in `#9c9c9d`.** [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)
- **Don't invent a light marketing theme.** A light colour-scheme preference left `--background` at `#07080a`.
- **Don't treat the homepage launcher mock as the signed-in app.** It is a marketing demo. [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)
- **Don't click through the login wall.** It offers icon identity buttons and Continue with ChatGPT. Those were not opened. [screenshots/login-wall-dark-desktop.png](screenshots/login-wall-dark-desktop.png)
- **Don't follow Download into a file.** The Homebrew dialog and the V1 confirm dialog were photographed and closed. [screenshots/site-tree/homebrew-dialog.png](screenshots/site-tree/homebrew-dialog.png)
- **Don't ship the Inter or JetBrains Mono files.** They are licensed to the product.

## Rebuild

```bash
python3 tools/test_tokens.py
```

`tokens.json` and `DESIGN.md` were written from the readings in [raw/](raw/). `catalog.json` was left alone, so `make design-md` was not run for this package.
