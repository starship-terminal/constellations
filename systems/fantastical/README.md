# Fantastical design reference

Tokens and component notes for the public Fantastical marketing site at [flexibits.com/fantastical](https://flexibits.com/fantastical). Captured 2026-11-22. Desktop screenshots are 1440×900 CSS pixels at device pixel ratio 2. The phone homepage is 390×844 CSS pixels at device pixel ratio 2. The site stayed light when `prefers-color-scheme` was dark.

This package is the public web site. It does not replace a native package. `systems/fantastical-ios/` was not present on this branch and was not created.

Public marketing pages, the header, the footer, pricing, the phone homepage and its menu, the 404 page, and the signed-out login and signup walls only. No account was created. No email or password was typed. No identity provider was clicked. No form was submitted. No checkout was entered. No download was kept. `login-extracted` stays not-started.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [icon.png](icon.png) | The site icon, 128px, resized from `/favicon.ico`. |
| [tokens.json](tokens.json) | DTCG tokens. `core` holds type, radius, and space. `light` holds the semantic roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. The catalog generator was not run. |
| [style-guide.html](style-guide.html) | Renders the token roles. Effra is not loaded. |
| [components.md](components.md) | Measured controls, and the gaps. |
| [patterns.md](patterns.md) | How the public pages are built, and where they stop. |
| [site-tree.md](site-tree.md) | Which header and footer controls open which pages and walls. |
| [components/](components/) | Crop folder. Element crops were not cut. The page screenshots hold the controls. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. |
| [raw/](raw/) | Computed styles from the homepage. |
| [tools/](tools/) | `test_tokens.py`. |

<!-- brief:start -->
<!-- brief:end -->

<!-- health:start -->
<!-- health:end -->

## How the values were read

Computed styles were read with `getComputedStyle` on `https://flexibits.com/fantastical` on 2026-11-22: the body, the header, the first `h1`, the hero `h2`, the Pricing link, Sign In, Try for Free, and Start for Free. `:root` exposed Bootstrap breakpoint variables only. Colour roles come from those computed colours.

## What to distrust

The marketing sans is Effra, with Helvetica Neue, Arial, and Helvetica behind it. The file is not in this package. The capture browser resolved Effra on the homepage.

The header background is `#ffffff` at alpha 0.8. The token records the opaque hex. The alpha is in [raw/home-tokens.json](raw/home-tokens.json).

A later homepage heading, "See Everything. Miss Nothing.", computed at 64px. The hero `h1` computed at 40px. The display token is the hero.

Screenshots are 256-colour PNGs. Long pages were cropped to the first 900 CSS pixels after the page had loaded. Read colours from `tokens.json`, not from the images.

Setting `prefers-color-scheme: dark` did not switch the page. Body background stayed `#ffffff`.

## Fonts

The computed family is Effra, Helvetica Neue, Arial, Helvetica, sans-serif. Effra is not in this package. The tokens fall back to the system sans.

## Coverage

| Item | Status |
|---|---|
| Colour, type, space, radius | Captured from computed styles. [tokens.json](tokens.json) |
| Light theme | Captured. Page background `#ffffff`. |
| Dark theme | Not present on the public marketing pages. `prefers-color-scheme: dark` left the page light. |
| Desktop 1440 | Captured for home, company home, pricing, support, blog, scheduling, about, jobs, affiliate, privacy, privacy FAQ, terms, California notice, legal, trust, Android coming soon, the 404 page, and both auth walls. |
| Phone 390 | Captured for the homepage, closed and with the menu open. [screenshots/home-light-phone.png](screenshots/home-light-phone.png) |
| Button, link, text field | Observed on public pages and the empty auth walls. See [components.md](components.md). |
| Checkbox, radio, switch, tabs, toast, table, select, dialog | Not present on the pages that were opened. Pricing uses in-page Annually and Monthly links. |
| Pricing | Captured. Free $0.00, Individual and Team $4.75, Family $7.50, read as annual monthly equivalents. [screenshots/pricing-light-desktop.png](screenshots/pricing-light-desktop.png) |
| Download page | Not present as a page. `/fantastical/download` starts a zip. The file was not kept. |
| Empty state | Captured. A missing path shows "404" and "Page not found." [screenshots/not-found-light-desktop.png](screenshots/not-found-light-desktop.png) |
| Signed-in app | Not entered. `login-extracted` is not-started. |
| Loading, error on a form | Not shown. Forms were not submitted. |

## Do and don't

- **Do paint the page `#ffffff`.** The headline is `#1d1e1f` in Effra at 40px, weight 500. [screenshots/home-light-desktop.png](screenshots/home-light-desktop.png)
- **Do paint Try for Free and Start for Free as `#408fff` pills.** The radius is 24px. The label is white. [screenshots/home-light-desktop.png](screenshots/home-light-desktop.png)
- **Do keep Sign In as a quiet `#408fff` label.** It is not a filled pill in the desktop bar. [screenshots/home-light-desktop.png](screenshots/home-light-desktop.png)
- **Don't invent a dark marketing theme.** A dark colour-scheme preference left the body at `#ffffff`.
- **Don't treat the homepage calendar mock as the signed-in app.** It is a marketing demo. [screenshots/home-light-desktop.png](screenshots/home-light-desktop.png)
- **Don't click through the login wall.** It offers Continue with Apple. That button was not opened. [screenshots/login-wall-light-desktop.png](screenshots/login-wall-light-desktop.png)
- **Don't follow Download into a file.** `/fantastical/download` starts a zip. The file was not kept.
- **Don't ship the Effra file.** It is licensed to the product.

## Rebuild

```bash
python3 tools/test_tokens.py
```

`tokens.json` and `DESIGN.md` were written from the readings in [raw/](raw/). `catalog.json` was left alone, so `make design-md` was not run for this package.
