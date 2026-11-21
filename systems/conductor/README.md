# Conductor design reference

Tokens and component notes for the public Conductor marketing site at [conductor.build](https://www.conductor.build/). Captured 2026-11-22. Desktop screenshots are 1440×900 CSS pixels. Phone screenshots are 390×844 CSS pixels. Dark is the colour scheme the site applied on its own. Light was read by setting `prefers-color-scheme: light`, which sets `html.light`.

This package is the public web site. The desktop app already lives at [systems/conductor-desktop](../conductor-desktop/). That package was not overwritten.

Public marketing pages, the header, the download dialog, the phone menu, and the signed-out login and signup walls only. No account was created. No email, password, code, or phone was typed. No identity provider was clicked. No form was submitted. No download was started. `login-extracted` stays not-started.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [icon.png](icon.png) | The site icon, 128px, resized from `/favicon.ico`. |
| [tokens.json](tokens.json) | DTCG tokens. `core` holds type, radius, space and motion. `dark` and `light` hold the semantic roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. The catalog generator was not run. |
| [style-guide.html](style-guide.html) | Renders the token roles with a theme toggle. Geist is not loaded. |
| [components.md](components.md) | Measured controls, and the gaps. |
| [patterns.md](patterns.md) | How the public pages are built, and where they stop. |
| [site-tree.md](site-tree.md) | Which header controls open which pages, menus, and walls. |
| [components/](components/) | Crop folder. Element crops were not cut. The page screenshots hold the controls. |
| [icons/](icons/) | The pixel mark, with [INDEX.tsv](icons/INDEX.tsv). |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. |
| [raw/](raw/) | Computed styles and the `.dark` custom-property block. |
| [tools/](tools/) | `test_tokens.py`. |

<!-- brief:start -->
<!-- brief:end -->

<!-- health:start -->
<!-- health:end -->

## How the values were read

Custom properties were read from the page stylesheets and from `getComputedStyle(document.documentElement)` on `https://www.conductor.build/` in headless Playwright on 2026-11-22. Dark values come from the `.dark` rule while `html` had `class="dark"`. Light values come from the `:root` rule, confirmed by setting `prefers-color-scheme: light`, which switched `html` to `class="light"` and painted the body `rgb(255, 255, 255)`.

Component sizes come from `getComputedStyle` on the homepage header, the Get Conductor link, and the announcement banner. The login wall was measured only for its body font and background. Its identity-provider buttons were not clicked.

## What to distrust

The marketing sans is declared as Geist. In the capture browser `--marketing-font-sans` computed to `ui-sans-serif, system-ui, sans-serif`. The login wall did resolve `Geist`. Do not treat the homepage stack as proof that Geist failed to load in the product's own browser.

The homepage headline copy changes. At 1440 dark it says "in the cloud." At 1440 light it says "on your Mac." At 390 it says "from your iPhone." The type size stayed 36px.

The light `--primary` is `#413030`. The light Get Conductor button computed as a white fill. The token and the button are different. The dark Download button fill is `#eae8e6`. Dark `--primary` is `#f3f2f1`. They are close and not the same.

Screenshots are 256-colour PNGs. Long pages (changelog, privacy, terms, docs API) were cropped to the first 900 CSS pixels after the full page was confirmed to have loaded. Read colours from `tokens.json`, not from the images.

The light homepage and docs shots were taken at device pixel ratio 1. The dark shots were taken at 2.

## Fonts

The stylesheet names Geist Sans for marketing (`--font-geist-sans-source`) and Geist Mono plus iA Writer Mono for product faces. The files are not in this package. The tokens fall back to the system sans and the system mono.

## Coverage

| Item | Status |
|---|---|
| Colour, type, space, radius | Captured from custom properties and computed styles. [tokens.json](tokens.json) |
| Dark theme | Captured. `html.dark` on the marketing site. |
| Light theme | Captured. `html.light` when `prefers-color-scheme` is light. [screenshots/home-light-desktop.png](screenshots/home-light-desktop.png) |
| Desktop 1440 | Captured for home, announcement, changelog, one changelog entry, docs, cloud FAQ, API, blog, brand kit, privacy, terms, the download dialog, and both auth walls. |
| Phone 390 | Captured for home, the expanded header menu, changelog, and the login wall. |
| Button, link, menu, dialog, card | Observed on public pages. See [components.md](components.md). |
| Text field, checkbox, radio, switch, select, toast, table | Not present on the public pages that were opened. |
| Pricing | Not present. No public pricing page. |
| Download page | Not present. Download is a dialog. The file was not fetched. |
| Signed-in app | Not entered. `login-extracted` is not-started. |
| Empty, loading, error | Not shown on the public pages. |

## Do and don't

- **Do paint the page `#141110` in dark and white in light.** The class on `html` is `dark` or `light`. [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)
- **Do set the headline in the sans at 36px, weight 600, with -0.9px tracking.** [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)
- **Do paint Download and Get Conductor as a light pill on the dark page.** The radius is 6px. The dark fill measured `#eae8e6`. [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)
- **Do keep Changelog, Docs, and Sign in as quiet text links.** [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)
- **Do put an announcement bar above the header when the site shows one.** On 2026-11-22 it said Conductor is joining Meta and was 44px tall. [screenshots/announcement-dark-desktop.png](screenshots/announcement-dark-desktop.png)
- **Don't invent a pricing page.** The public tree has no pricing control.
- **Don't treat the homepage product mock as the signed-in app.** It is a marketing demo. [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)
- **Don't click through the login wall.** It offers Google, GitHub, and ChatGPT. Those were not opened. [screenshots/login-wall-dark-desktop.png](screenshots/login-wall-dark-desktop.png)
- **Don't ship the Geist files.** They are licensed to the product.
- **Don't follow Download into a dmg.** The dialog was photographed and closed. [screenshots/site-tree/desktop-download-dialog.png](screenshots/site-tree/desktop-download-dialog.png)

## Rebuild

```bash
python3 tools/test_tokens.py
```

`tokens.json` and `DESIGN.md` were written from the readings in [raw/](raw/). `catalog.json` was left alone, so `make design-md` was not run for this package.
