# Douze

A token set and component reference for Douze, the non-alcoholic spritz storefront at drinkdouze.com. Captured 2026-11-21, signed out, in headless Chromium at 1440 and 390. English `/en` is the captured surface. A fr-FR context was used once for the French home. One light theme. Shopify storefront. The control map is [site-tree.md](site-tree.md).

Dusk ink `#301816` does text, nav, and the primary button. Sable `#f6f2e9` is the header bubble, footer, and login card. Paper is white. Display type is Boogy at weight 300. UI labels are Robin Semibold, 12px, uppercase, tracked. Buttons are square. Filter tabs and login fields are pills. Section cards use a 45px radius.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px PNG, resized from the public 96 px favicon |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` (42 leaves) and `light` (21 aliases). One theme. Every leaf has `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Hand-written stand-in. `make design-md` needs a catalog.json entry, and this capture must not add one. Tokens stay the source of truth. |
| [style-guide.html](style-guide.html) | One page of the measured colours, type, and controls. Brand fonts are not loaded. |
| [components.md](components.md) | Component inventory with crops and token names |
| [patterns.md](patterns.md) | How the components combine on the public pages |
| [site-tree.md](site-tree.md) | Which control opens which page or in-page interaction |
| [components/crops/](components/crops) | 23 element crops, `{component}-{state}.png` at 1x |
| [screenshots/](screenshots) | 58 page shots, `{page}-light-{state}.png`, desktop 1440 and `mobile-*` at 390, quantized to 256 colours |
| [raw/](raw) | `root-vars.json`, `css-vars.json`, `measurements.json`, `component-tokens.json` |
| [tools/](tools) | `build_tokens.py`, `build_style_guide.py`, `style-guide.template.html`, `capture/quantize.py` |

## Brief

<!-- brief:start -->

Not generated. `make brief` reads catalog.json, and this package is not registered there. Read [tokens.json](tokens.json) and the Do and don't list below.

<!-- brief:end -->

## Health

<!-- health:start -->

No scorecard snapshot. This package is not in catalog.json, so `make grade` cannot write a Health section for it.

<!-- health:end -->

## How the values were read

Playwright (headless Chromium) opened the public storefront signed out. Viewport 1440x900 for desktop and 390x844 for phone. `window.innerWidth` was checked on each shot.

`:root` custom properties were read from CSSStyleSheet rules into [raw/root-vars.json](raw/root-vars.json). `getComputedStyle(documentElement)` did not enumerate custom properties (resolved count 0), so declared tokens come from the stylesheet, and painted values come from computed styles on the elements in [raw/measurements.json](raw/measurements.json).

[tools/build_tokens.py](tools/build_tokens.py) turns [raw/component-tokens.json](raw/component-tokens.json) into [tokens.json](tokens.json). Colour triplets were converted to hex. An alias that does not resolve fails the build.

Screenshots were quantized to 256 colours with no dither by [tools/capture/quantize.py](tools/capture/quantize.py). Full-colour captures stay outside the repo.

The icon is the public favicon, resized with Pillow LANCZOS from 96 px to 128 px. `tools/fetch_icon.py` could not fetch it because the slug is not in catalog.json.

## What to distrust

Crop boxes in [components/crops/](components/crops) were estimated from the page screenshots. They were not visually re-checked after the crop. Treat a crop as a pointer to the page shot, not as a tight measurement.

`radius.pill` (999px) was measured on `.tabs-nav__item` only. Login fields computed to 16px (`radius.blockReduced`), with a 1px dusk border and 52px height. A 256-colour screenshot can make those ends look rounder than the computed radius.

`--error-color` is the same triplet as `--success-color`. There is no distinct danger colour in the declared tokens. Do not invent one.

Add-to-cart focus paints no outline (`none 0px`). A shadow `rgba(0, 0, 0, 0.15) 0px 4px 8px 0px` was computed on focus. That is a shadow, not a focus ring.

The search drawer shot was taken by setting the `open` attribute. No visible search trigger was found at 1440 or at 1000. The desktop SHOP item points `aria-controls` at `desktop-menu-1`, which is not in the DOM.

Screenshots are 256-colour. Do not sample hex from them.

`size.logo` is the logo link width (70px). The height was 23px and is not a separate token.

## Fonts

Boogy (display) and Boogy Italic are declared as `--heading-font-family` and `--heading-font-family-italic`, `font-display: swap`. Robin Regular and Robin Semibold are the text and label faces. They are proprietary. The tokens name them and fall back to `sans-serif`. The style guide does not load the files.

Vendor faces also appear in the stylesheet (Jost, Barlow, Klaviyo, Okendo). They are not the storefront's type system and are not tokenised.

## Coverage

Signed-out public pages at 1440 and a phone subset at 390. The map is [site-tree.md](site-tree.md).

Captured: home (default, cart drawer, locale click, forced search drawer, full page, French home), shop and its Cans tab, one PDP with pack and subscription option selected, story, why, recipes, one recipe, general blog, store locator, find-us, subscription, contact, both stockist forms, referral, terms, privacy, campaign page, gift card product, search, empty cart, login, register, 404, collection index and four collections, FAQ closed and one item open, mobile home (default, full, menu), shop, PDP, login, cart, recipes, locator, FAQ, subscription, search.

Not captured: a filled cart, checkout, a submitted search, the newsletter popup (the node is absent), a visible header search button, the desktop SHOP mega-menu (the panel is absent), dark theme (none), every product page, every recipe article, the French tree beyond the home shot, account interiors past the login wall.

## Do and don't

**Do set dusk on paper.** Body, nav, and the primary button share `#301816`. The page is white. See [screenshots/home-light-default.png](screenshots/home-light-default.png).

**Do use sable for the quiet surfaces.** Header bubble, footer, and the login card are `#f6f2e9`. See [components/crops/login-card-default.png](components/crops/login-card-default.png).

**Do set display type in Boogy at weight 300.** The home hero heading is 72px, line-height 64.8px, tracking -0.72px, sable ink over the photograph. See [screenshots/home-light-default.png](screenshots/home-light-default.png).

**Do set labels in Robin Semibold, 12px, uppercase, tracked.** Nav tracking is 1.2px. Button tracking is 0.96px. See [components/crops/nav-link-default.png](components/crops/nav-link-default.png).

**Do keep buttons square and filters pill.** `--button-border-radius` is 0px. Selected filter tabs are 999px, dusk fill, white label. See [components/crops/filter-tabs-selected.png](components/crops/filter-tabs-selected.png).

**Do keep the three flavour colours for flavour, not for chrome.** Apricot `#f4a765`, pear `#f3eea7`, orange `#f26554` are declared flavour tokens.

**Don't invent a focus ring.** Focus on add-to-cart computed `outline: none 0px`. See [raw/measurements.json](raw/measurements.json) `addFocus`.

**Don't invent a danger red from the error token.** `--error-color` matches `--success-color`. Low-stock text `#df6464` is a stock role, not a form error.

**Don't fill login, newsletter, contact, stockist, referral, or checkout forms to capture more.** Those branches stop at the wall. See [site-tree.md](site-tree.md).

**Don't sample colour from the screenshots.** They are 256-colour PNGs. Read [tokens.json](tokens.json).

## Rebuild

```bash
cd systems/drinkdouze && python3 tools/build_tokens.py && python3 tools/build_style_guide.py
```

`build_components_md.py` is the shared kit builder. It expects another package's `components-computed.json` and is not the writer for [components.md](components.md). That file is written from [raw/measurements.json](raw/measurements.json).

`make design-md` and `make check` need a catalog.json entry. This capture does not add one. Register the package in a later change if the catalog should list Douze.

## Catalog

This folder is the package. [catalog.json](../../catalog.json) and [webapps-manifest.json](../../webapps-manifest.json) are unchanged. The catalog name, when registered, is Douze.
