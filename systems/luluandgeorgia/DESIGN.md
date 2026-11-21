---
# Hand-written from tokens.json on 2026-11-21. Not regenerated: make design-md rewrites catalog.json.
# Source of truth: tokens.json. DESIGN.md spec version alpha.
version: "alpha"
name: "Lulu and Georgia"
description: "furniture storefront design: a white page, near-black ink #1a1713, a red announcement bar and Sale link #b11515, square corners, Soehne UI type and Iskry headings, a wide grey search field, and a black add-to-cart"
omitted:
  - section: "components"
    reason: "tokens.json has no components tokens under the colour set's `component` group"
colors:
  primary: "#b11515"
  neutral: "#ffffff"
  surface: "#ebebeb"
  on-surface: "#1a1713"
  on-surface-variant: "#747474"
  outline: "#e5e5e5"
  color-page: "#ffffff"
  color-surface: "#ebebeb"
  color-text-primary: "#1a1713"
  color-text-secondary: "#747474"
  color-text-on-accent: "#ffffff"
  color-text-link: "#1a1713"
  color-text-sale: "#b11515"
  color-border-default: "#e5e5e5"
  color-border-strong: "#1a1713"
  color-action: "#1a1713"
  color-action-hover: "#1a1713"
  color-promo: "#b11515"
  color-sale: "#b11515"
  color-cream: "#f3eee8"
  color-info: "#108474"
typography:
  heading:
    fontFamily: "Iskry"
    fontSize: "26px"
    fontWeight: 400
    lineHeight: "40px"
    letterSpacing: "1.2px"
  product:
    fontFamily: "Soehne Leicht"
    fontSize: "20px"
    fontWeight: 400
    lineHeight: "28px"
    letterSpacing: "0px"
  body:
    fontFamily: "Soehne Leicht"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "24px"
    letterSpacing: "0px"
  nav:
    fontFamily: "Soehne Leicht"
    fontSize: "11px"
    fontWeight: 400
    lineHeight: "24px"
    letterSpacing: "1.2px"
  button:
    fontFamily: "Soehne Leicht"
    fontSize: "13px"
    fontWeight: 800
    lineHeight: "24px"
    letterSpacing: "2px"
  caption:
    fontFamily: "Soehne Leicht"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: "16px"
    letterSpacing: "0px"
rounded:
  none: "0px"
spacing:
  "8": "8px"
  "12": "12px"
  "16": "16px"
  "40": "40px"
---

# Lulu and Georgia

Hand-written from [tokens.json](tokens.json) and [README.md](README.md) on 2026-11-21. `make design-md` was not run, because that command rewrites catalog.json. Change the tokens through the package's builders, then update this file from those tokens.

It follows the DESIGN.md spec, version alpha. That format has no themes, no per-value provenance and only px, em and rem units, so this file holds the `light` theme alone with every alias resolved. [tokens.json](tokens.json) is the source of truth: it records where each value was read, and keeps the 0 tokens from these groups that DESIGN.md cannot hold (gradients, shadows, percentages, durations and other non-colour or non-px values).

## Overview

Good for: furniture storefront design: a white page, near-black ink #1a1713, a red announcement bar and Sale link #b11515, square corners, Soehne UI type and Iskry headings, a wide grey search field, and a black add-to-cart.

Refreshed 2026-11-21, signed out. Account, checkout, add to cart, wishlist, and Continue with shop were not entered. The search field and the login email were left empty. Themes: light.

A token set and component reference for the Lulu and Georgia public storefront. Refreshed from luluandgeorgia.com on 2026-11-21, signed out, in headless Chromium at 1440 x 900 and 390 x 844. Surfaces: home, the furniture mega-menu, the furniture collection, the Sachs dining table product page, search for "rug", the about page, the account drawer, the empty bag drawer, the filter drawer, the footer, and the Shop sign-in page that `/account/login` and `/account/register` both redirect to.

The storefront is Shopify. It does not publish a design-token layer for colour and type. Values are computed styles. The page is white, the ink is `#1a1713`, and the announcement bar and Sale are both `#b11515`. Type is Soehne for UI and Iskry for headings. Corners are square.

`icons/` is declared absent in the catalog `layoutGaps`: header icons are inline SVGs and were not extracted.

## Colors

The roles below are the catalog's swatches for the `light` theme. The front matter then lists every colour token under `light`, named by its path with dots turned into hyphens.

- **primary (#b11515):** `light.color.promo`
- **neutral (#ffffff):** `light.color.page`
- **surface (#ebebeb):** `light.color.surface`
- **on-surface (#1a1713):** `light.color.text.primary`
- **on-surface-variant (#747474):** `light.color.text.secondary`
- **outline (#e5e5e5):** `light.color.border.default`

## Typography

6 styles from `core.typography`. `fontFamily` is the first family of each stack; the full stacks, and properties DESIGN.md has no field for (text case, decoration), are in tokens.json. Families: Iskry, Soehne Leicht.

### Fonts (from README.md)

Soehne (Leicht, Buch) for UI, computed as `"Soehne Leicht"` and `"Soehne Buch"`. Iskry Bold for collection headings. The footer newsletter button also names Söhne and Helvetica Neue. Neither family is shipped here. Both are proprietary. The style guide falls back to the system sans and a serif. The Shop sign-in page loads Libre Franklin, which belongs to that widget.

## Layout

Spacing from `core.spacing`: `8` 8px, `12` 12px, `16` 16px, `40` 40px.

## Elevation & Depth

No shadow tokens were captured; depth comes from surface colours and borders. See [style-guide.html](style-guide.html).

## Shapes

Corner radii from `core.radius`: `none` 0px.

## Components

No component tokens map onto DESIGN.md's component properties.

Measured states, crops and the full inventory: [components.md](components.md), [components](components), [style-guide.html](style-guide.html).

## Do's and Don'ts

- Do take values from [tokens.json](tokens.json) when you need another theme, a value's source, or a token this file leaves out.
- Do read [README.md](README.md) before relying on a value; it says what is known to be wrong.
- Don't read colours off the screenshots; they are 256-colour PNGs.
- Don't copy the product's logo, icons, illustrations or brand colours into something that ships. Borrow structure and proportions.
- Don't edit this file; it is regenerated from the tokens.

### Do and don't (from README.md)

1. **Do keep the page white and the ink near-black.** Header, cards, and the product column sit on white. Text and Add to cart are `#1a1713`. See [home-light-default](screenshots/home-light-default.png) and [atc-default](components/crops/atc-default.png).
2. **Do put the only colour in the announcement bar and in Sale.** Both are `#b11515` with white or ink type. Everything else is ink, grey, or white. See [home-light-default](screenshots/home-light-default.png).
3. **Do keep corners square.** Search, buttons, cards, and the filter chips compute `border-radius: 0`. See [search-default](components/crops/search-default.png).
4. **Do set UI in Soehne and headings in Iskry.** Category links are 11px uppercase with 1.2px tracking. Collection headings are Iskry at 26px. See [collection-light-default](screenshots/collection-light-default.png).
5. **Don't treat the Shop sign-in button as a brand colour.** `/account/login` redirects to shopify.com and paints a purple "Continue with shop" pill. That purple is the Shop widget, not the storefront. See [login-light-default](screenshots/login-light-default.png).
6. **Don't press Add to cart, Apply, or Continue with shop.** Those controls were measured or shown and never activated. Checkout and the account sit behind sign-in. See [product-light-default](screenshots/product-light-default.png).

### What to distrust (from README.md)

- Spacing steps are the paddings that were measured (8, 12, 16, 40). There is no declared spacing scale.
- The display face on the home hero is painted over a photograph. The heading token is the collection h1, which was a real text node.
- Add to cart hover and pressed did not change the computed fill. That is the measurement, not a missing hover style that was filled in.
- Focus on Add to cart is a keyboard focus (Shift+Tab, then Tab) taken after the pointer was moved away. The 2026-11-21 reading says `:focus-visible` matched. The computed fill did not change. There is still no focus colour token.
- The `badge` reading and its crop are the whole product card: the badge selector matched the card, not the chip.
- `light.color.promo` is the announcement bar's computed fill, `#b11515`, the same red as Sale. `light.color.cream` and `light.color.info` still come from a colour probe that was not committed. `light.color.border.strong` comes from a wishlist button the measure pass did not find. Those three stay Reconstruction.
- The add-to-cart type role is the measured 13px / 24px, weight 800, 2px tracking. Before the 2026-11 audit it said 16px and 0px, which no reading holds.
- [components.md](components.md) is prose written at capture time; [tools/build_components_md.py](tools/build_components_md.py) fills every measured number in it from `raw/components-computed.json` and fails when one is missing.
- `light.color.info` is the reviews widget, not a storefront status colour. Success, warning, and danger were not painted as their own roles. Sale red is the only red.
- The Shop sign-in page uses Libre Franklin and a purple pill. Those values are not in `tokens.json`.
- Screenshots are 256-colour PNGs. Read colours from tokens, not from the images.
- The committed readings and screenshots were taken with `navigator.webdriver` hidden by `tools/capture/public/lib.mjs`. The mask has been removed from the script (2026-11 audit); a bot check is now a boundary, not something to get past.
- The chat bubble (Gladly) is still in some screenshots. It is a third-party widget.
