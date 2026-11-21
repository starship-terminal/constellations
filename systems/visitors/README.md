# Visitors design reference

A token set for Visitors (visitors.now), a privacy-friendly web analytics product. Read on 2026-11-21 from the public site, signed out. The session had no account. `/login` is an email, Google, or GitHub wall, and `/dashboard` returns to it. Google was not clicked. No password, code, or onboarding field was filled.

Themes: light is what the public pages rendered. Dark is the `.dark` block in the same stylesheet (`styles-pNqCiRay.css`). It was not applied on any page visited, so dark values are stylesheet evidence. Widths: the preview viewport measured 1920×1080 CSS at devicePixelRatio 2, not 1440. A 390 phone width was not captured. The preview stopped producing screenshot frames after the homepage scroll, and a second open did not restore frames.

| File | What it is |
|---|---|
| [icon.png](icon.png) | 128 px PNG from `/favicon-black.png` (source was 96 px) |
| [tokens.json](tokens.json) | DTCG tokens. `core` holds the font, the `:root` ramps, radii, type sizes, shadows, blur, and easing. `light` and `dark` hold background, text, and alpha roles. Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Not generated. `catalog.json` was left for the batch merge, and `make design-md` writes this from a catalog entry |
| [style-guide.html](style-guide.html) | Swatches and three controls painted from the measured values |
| [components.md](components.md) | Controls that rendered, with computed styles where they were read |
| [patterns.md](patterns.md) | Homepage, login split, feature menu. App patterns were behind the wall |
| [site-tree.md](site-tree.md) | Which homepage control opens which page or interaction |
| [login-review.json](login-review.json) | Post-auth screens: none reached. One gap per screen |
| [screenshots/](screenshots) | Four light captures at 3840×2160 (1920 CSS, dpr 2) |
| [raw/css-vars.json](raw/css-vars.json) | The declared custom properties from the live stylesheet |
| [tools/](tools) | `build_tokens.py` and `build_style_guide.py`, plus the copied capture kit |

## Brief

<!-- brief:start -->

Brief is written by `make brief` after the catalog entry exists. This package left `catalog.json` for the batch merge, so the section is a placeholder.

<!-- brief:end -->

## Health

<!-- health:start -->

Health is written by `make grade` after a catalog entry and a scorecard snapshot exist. Neither was written here.

<!-- health:end -->

## How the values were read

Custom properties were read from the CSSOM on `https://visitors.now/` and confirmed against `https://visitors.now/assets/styles-pNqCiRay.css`. `:root` matches what the pages computed. `.dark` is in that file and was not on `documentElement`. Component colours and sizes on the homepage hero and the login form were `getComputedStyle` readings. Screenshots were saved from the T3 preview with `save: true`.

## What to distrust

- Dark tokens were not rendered. Do not treat them as a measured theme.
- The nav Register pill computed to `#9580ff`. The hero trial button computed to `#918df6`, which is `:root --purple-4`. `.dark --purple-4` is `#9580ff`. The core ramp keeps the `:root` value.
- Homepage tiles after the first have the Features menu open over the page. They are not clean full-page evidence. The stitched full page was deleted for that reason.
- No 1440 or 390 screenshot exists. The measured CSS viewport was 1920×1080.
- Screenshots are full colour. Read colours from `tokens.json`.

## Fonts

Open Runde, self-hosted as `OpenRunde` at weights 400, 500, and 600 (`/assets/OpenRunde-*.woff2`). The stack falls back to Inter, then sans-serif. Mono is SF Mono, then Menlo, then Open Runde. Licence of Open Runde was not read.

## Coverage

| Item | Status |
|---|---|
| Colour roles, light | Captured. `tokens.json` `light`, from `:root` |
| Colour roles, dark | Stylesheet only. `.dark` was not applied |
| Type | Family, sizes, and weights from CSS. Roles (display, body, label) were computed on h1, h2, and the login field, not as a full scale specimen |
| Spacing | Unit only (`--spacing: .25rem`). Component padding was computed on a few controls |
| Radii, shadows, blur, easing, duration | Captured from declared tokens |
| Button, link, text field, menu, badge, nav | Captured, default (and disabled, and email focus) |
| Text area, select, checkbox, radio, switch, tooltip, dialog, toast, table, avatar | Not present on the pages that rendered |
| Hover, pressed, loading, error | Not captured. The preview stopped before those passes |
| App shell, empty, loading, error, destructive confirm, search | Not captured. Behind `/login` |
| Onboarding / project setup | Not captured. See [login-review.json](login-review.json) |
| Phone 390 | Not captured. Frames stopped |
| Desktop 1440 | Not captured. Measured viewport was 1920 |

## Do and don't

- **Do use one purple pill for the primary action.** The trial button and the nav Register pill are the only filled actions on the homepage. See [screenshots/home-light-viewport.png](screenshots/home-light-viewport.png).
- **Do keep secondary actions as quiet pills.** See demo, Google, and GitHub share the 3% black fill. See [screenshots/login-light.png](screenshots/login-light.png).
- **Do set the page in Open Runde with tight tracking.** Body tracking computed to -0.32px. The h1 computed to 60px, weight 600, tracking -3px.
- **Don't invent a rendered dark theme.** The public pages stayed on `:root`.
- **Don't treat the hero chart as the product.** It is a marketing image. The signed-in app was not opened.

## Rebuild

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

`DESIGN.md`, Brief, and Health wait on the catalog entry, which this branch does not add.
