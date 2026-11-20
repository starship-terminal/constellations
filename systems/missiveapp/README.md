# Missive design reference

A token set and component reference for Missive's public marketing site (https://missiveapp.com), a Webflow site for a team inbox product. Use it to build a marketing surface that borrows its look: a white page, ink `#34363a`, muted `#646c76`, hairline `#e4e6e9`, surface `#f5f6f6`, a blue `#2266ed` primary action that darkens to `#1c42b1`, Inter for UI, and Tiempos Headline for the display line. The site ships its own token layer as CSS custom properties: `--swatch--*` ramps, `--color--*` roles, and a 4px-base `--spacing--*` scale. It was captured signed out, in headless Chromium at 1440 x 900 (phone at 390 x 844) on 2026-11-21.

It holds 61 screenshots across the public templates the nav and footer open, plus transient states (Product menu, Resources menu, Watch demo lightbox, pricing FAQ, phone menu), and 26 measured components with 57 crops. The product itself (https://mail.missiveapp.com/#login) asks for a work email and password, or Google, Apple, or SSO, and that branch was not entered. One painted theme: light. No dark theme switch and no dark custom-property set were found.

This package contains no Missive code, and none of its artwork has been redrawn. The screenshots, product imagery and visual system they show belong to Missive ([docs/RIGHTS.md](../../docs/RIGHTS.md)). Borrow structure and proportions, not the logo, artwork or brand assets.

| File | What it is |
|---|---|
| [icon.png](icon.png) | The site apple-touch icon, resized to 128 px, fetched from the Webflow CDN the homepage declares |
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout: `core` (swatches, spacing, font families) and `light` (semantic roles plus measured component sizes). Every token has `$extensions.source`. No dark set |
| [DESIGN.md](DESIGN.md) | A DESIGN.md export of the light tokens and this README, written in the catalog format. `make design-md` was not run, because that command needs a catalog entry and this capture does not edit [catalog.json](../../catalog.json) |
| [style-guide.html](style-guide.html) | Every token rendered, with site mockups built only from the tokens (nav, hero, three plan columns). Open it from disk. The theme toggle is hidden: there is one theme |
| [components.md](components.md) | 26 measured components, each with its values per state and crops of the real page, then a Gaps section |
| [patterns.md](patterns.md) | How the nav, hero, menus, pricing, docs and footer compose |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, dialog or interaction, mapped before the screenshot pass |
| [components/crops/](components/crops) | 57 element crops, `{component}-{state}.png`, cut from the live page at 2x |
| [screenshots/](screenshots) | 61 captures, `{page}-light-{state}.png` at 1440 x 900 and `mobile-*` at 780 wide (390 at 2x), quantised to 256 colours |
| [raw/](raw) | `css-vars.json`, `component-tokens.json`, `components-computed.json`, `measurements.md` |
| [tools/](tools) | The capture kit and the builders that regenerate the package |

## Brief

<!-- brief:start -->

Not generated. `make brief` reads [catalog.json](../../catalog.json), and this capture does not edit that file. Read [tokens.json](tokens.json) and the Do and don't list below before designing in this style.

<!-- brief:end -->

## Health

<!-- health:start -->

Not generated. `make grade` writes this section from the scorecard and a catalog entry. This capture does not edit [catalog.json](../../catalog.json), so no grades were written.

Layout ([docs/PACKAGE.md](../../docs/PACKAGE.md)): no `icons/` folder. The icon extraction pass was not run. The wordmark and icons stay in the screenshots and in [icon.png](icon.png). That gap is recorded here because the catalog was not edited.

<!-- health:end -->

## How the values were read

- CSS custom properties were read from the live stylesheets by [tools/capture/vars.mjs](tools/capture/vars.mjs) into [raw/css-vars.json](raw/css-vars.json). The product layer is `--swatch--*`, `--color--*` and `--spacing--*` on `:root`. Ketch consent variables (`--k-*`) were treated as vendor and are not tokens.
- Every component was located on the live page by [tools/capture/public/measure.mjs](tools/capture/public/measure.mjs) in headless Chromium. Computed styles were read per state: default, hover, focus-visible, pressed (forced via `CSS.forcePseudoState`), focused on the docs search field, opened on the Product menu, pricing FAQ and phone menu. One 2x crop was saved per state.
- Screenshots were taken by [tools/capture/public/public.mjs](tools/capture/public/public.mjs) and quantised to 256 colours by [tools/capture/quantize.py](tools/capture/quantize.py). The Ketch banner (`#ketch-banner`, `#lanyard_root`) was hidden with CSS. It was not clicked.
- The site tree in [site-tree.md](site-tree.md) was mapped from the homepage DOM before the screenshot pass.

## What to distrust

- **The product is absent.** https://mail.missiveapp.com/#login and `#signup` were recorded and not entered. Download installers on that host and on `downloads.missiveapp.com` were not opened. Nothing here describes the signed-in app.
- **There is no dark theme.** Do not invent one from the light swatches. `resolved.dark` in the raw CSS dump is the same light values, because a `.dark` class is unbound.
- **`flyout-open` and `m-menu-open` measured the trigger, not the panel.** The open panels are in [home-light-product-menu](screenshots/home-light-product-menu.png) and [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).
- **`card` matched a small chip, not a story card.** Story cards are in the home and customers screenshots.
- **The docs chat field was not measured.** The docs search field was. Neither was submitted.
- **Status colours are swatches, not roles.** `light.status.success` and `light.status.warning` are `--swatch--green-600` and `--swatch--cumin-600`. The site does not declare success, warning, danger or info roles.
- **Screenshots are 256-colour PNGs.** Read exact colours from [tokens.json](tokens.json) or the raw JSON, never from a screenshot pixel.
- **Five full-page shots were capped at 12000 px** after the stitch: changelog, compare, features, mobile-features, and mobile-home. The viewport shots of those pages are complete.
- **DESIGN.md was written for this capture without a catalog entry.** After a catalog entry exists, regenerate it with `make design-md` and treat that output as the copy of record.

## Fonts

- **Inter** is the painted UI face, loaded as a webfont. The file is not committed. The token stack is Inter, then ui-sans-serif, system-ui, sans-serif.
- **Tiempos Headline** is the painted display face, loaded as a webfont. The file is not committed. The token stack falls back to Georgia, then serif.
- No mono or print family was declared in the product token layer.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Page, surface, text, muted, accent, border | captured | `light.page`, `light.surface`, `light.text`, `light.muted`, `light.accent`, `light.border` |
| Accent hover and soft | captured | `light.color.accent-hover` `#1c42b1`, `light.color.accent-soft` `#dbebfe` |
| Dark theme | not present | no theme switch, no dark custom-property set |
| Type families | captured | `core.font.family.ui` Inter, `core.font.family.display` Tiempos Headline. No composite type styles |
| Spacing | captured | `core.spacing.1` 4px through `core.spacing.28` 112px |
| Radius, shadow, motion tokens | not captured | not declared as custom properties. Computed radii and the FAQ padding transition are in [raw/measurements.md](raw/measurements.md) |
| Component sizes | captured | `light.component`: button 44px, nav link 44px, hero 56px, field 37px, header 61px |
| Nav, CTA, hero, plan card, FAQ, docs search, footer, phone menu | captured | [components.md](components.md) |
| Checkbox, radio, switch, toast, table, destructive confirm | not present | none on the public marketing surface |
| Disabled, error, loading, selected | not present | none on the public marketing surface |
| Login and signup | not captured | https://mail.missiveapp.com/#login and `#signup` recorded, not entered |
| Icons | not captured | no `icons/` folder. Wordmark is in the screenshots and [icon.png](icon.png) |
| Sitemap copies | sampled | one template each for blog, changelog, story, integration, partner, compare, use case, solution, French home |

## Do and don't

- **Do keep the page white and the ink `#34363a`.** Surface is `#f5f6f6`, muted is `#646c76`, hairline is `#e4e6e9`. ([header](components/crops/header-default.png), [hero-title](components/crops/hero-title-default.png))
- **Do use `#2266ed` for the primary action.** The nav and hero CTAs are that blue, with white label text. Hover darkens toward `#1c42b1`. ([nav-cta](components/crops/nav-cta-default.png), [hero-cta](components/crops/hero-cta-default.png))
- **Do set display lines in Tiempos Headline and UI in Inter.** The hero is a 56px serif line. Nav and body are Inter. ([hero-title](components/crops/hero-title-default.png), [nav-link](components/crops/nav-link-default.png))
- **Do space on the 4px base.** `--spacing--1` is 4px and `--spacing--28` is 112px. ([pricing](screenshots/pricing-light-default.png))
- **Do open the Product menu on hover.** It is a mega menu, not a new page. ([home-light-product-menu](screenshots/home-light-product-menu.png))
- **Don't ship this as the app.** The signed-in product was not entered. A screen that claims the Missive inbox from these tokens would be invented.
- **Don't invent a dark theme.** The public site paints light only.
- **Don't submit the public forms.** Docs search, docs chat, newsletter and plan CTAs were left unsent.

## Rebuild

```bash
cd systems/missiveapp
node tools/capture/public/build-measurements.mjs
python3 tools/build_component_tokens.py
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/build_components_md.py
```

Capture (already run for this package, headless Chromium, Ketch banner hidden, login wall not entered):

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/public.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/measure.mjs
```

`make brief`, `make design-md`, `make grade` and `make check` need a catalog entry. This capture does not add one.
