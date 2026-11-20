# Allbirds components

The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from www.allbirds.com on 2026-11-08, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was bought, checked out, signed into, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (48 components, 92 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Geograph 12/15 500, #212121`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (92 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (Allbirds serves one light theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home. Promo strip, nav bar, hero card, category cards, carousels, subscribe row, footer. Mega-menu, search overlay and full page captured. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png), [search](screenshots/home-light-search.png) |
| Collection, Men's. Title, filter button, the filter sheet open, product cards; full page. | `/collections/mens` | [default](screenshots/collection-light-default.png), [filter](screenshots/collection-light-filter.png), [full](screenshots/collection-light-full.png) |
| Product, Men's Tree Runner NZ. Buy box, size picked, accordion open, cart drawer; full page. | `/products/mens-tree-runner-nz-medium-grey` | [accordion](screenshots/product-light-accordion.png), [cart-drawer](screenshots/product-light-cart-drawer.png), [default](screenshots/product-light-default.png), [full](screenshots/product-light-full.png), [options](screenshots/product-light-options.png) |
| Cart page, empty session cart. | `/cart` | [default](screenshots/cart-light-default.png) |
| Search page. | `/search` | [default](screenshots/searchpage-light-default.png) |
| Account login (Shopify-hosted). Email field focused. | `/account/login` | [default](screenshots/account-light-default.png), [focus](screenshots/account-light-focus.png) |
| Our Story page. | `/pages/our-story` | [default](screenshots/story-light-default.png), [full](screenshots/story-light-full.png) |
| Materials page. | `/pages/materials` | [default](screenshots/materials-light-default.png), [full](screenshots/materials-light-full.png) |
| Help page. | `/pages/help` | [default](screenshots/help-light-default.png), [full](screenshots/help-light-full.png) |
| Blog index. | `/blogs/stories` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Home at 390: ink header bar, menu drawer open, full page. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Collection at 390; full page. | `/collections/mens` | [default](screenshots/mobile-collection-light-default.png), [full](screenshots/mobile-collection-light-full.png) |
| Product at 390: buy box, size picked, cart drawer. | `/products/mens-tree-runner-nz-medium-grey` | [cart-drawer](screenshots/mobile-product-light-cart-drawer.png), [default](screenshots/mobile-product-light-default.png), [options](screenshots/mobile-product-light-options.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Geofencing dialog ("Where are we shipping to?") | first visit, any page | US chosen once to set the region; the section is then removed so it cannot remount over other shots | dismissed before every capture |
| Mega-menu flyout | desktop nav | hover on the MEN button | [menu](screenshots/home-light-menu.png), [mega-menu](#mega-menu-flyout) |
| Search overlay | desktop nav | the Search nav item | [search](screenshots/home-light-search.png) |
| Filter sheet | collection | the Filter button; Escape after capture | [filter](screenshots/collection-light-filter.png), [filter-sheet](#filter-sheet) |
| Cart drawer | product page | a size picked, then Add to Cart (a session cart; checkout never pressed) | [cart-drawer](screenshots/mobile-product-light-cart-drawer.png), [cart-drawer](#cart-drawer) |
| Mobile menu drawer | mobile home | the hamburger button | [menu](screenshots/mobile-home-light-menu.png), [m-menu-drawer](#mobile-menu-drawer) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 7 components were given a real keyboard focus. 7 draw a ring: `nav-link` (1px auto #005fcc, offset 1px), `filter-button` (1px auto #005fcc, offset 0px), `swatch` (1px auto #005fcc, offset 0px), `atc-button` (1px auto oklch(0.546 0.245 262.881), offset 0px), `cart-button` (1px auto #005fcc, offset 0px), `search-link` (1px auto #005fcc, offset 1px), `cta-primary` (1px auto oklch(0.546 0.245 262.881), offset 1px). The other 0 draw none, so a keyboard user sees no change: .

**Pressed.** Allbirds' pill buttons invert or stay flat when pressed; the size chips take a `light-charcoal-0.3` (19% grey) wash — see the per-component state rows.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, color, fill, opacity, outline-color, stroke, text-decoration-color | card-image, email-input, login-submit, signup-button, tooltip-pill |
| 0.2s | `cubic-bezier(0.37, 0, 0.63, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, opacity, outline-color, stroke, text-decoration-color | atc-button, cta-outline-white, cta-primary, nav-link, nav-menu-button, size-button, size-button-disabled |
| 0.2s | `cubic-bezier(0.61, 1, 0.88, 1)` | opacity | atc-button, cta-outline-white, cta-primary |
| 0.2s | `ease-in-out` | all | login-input |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | size-tab |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Header](#header) | 1400 x 48 | - | 12px | #ffffff `white` | rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px | 0px 20px |
| [Announcement bar](#announcement-bar) | 1440 x 32 | - | - | transparent | none | 0 |
| [Mega-menu flyout](#mega-menu-flyout) | 155.72 x 202 | - | - | transparent | none | 0 |
| [Cart drawer](#cart-drawer) | 531 x 900 | - | - | #ffffff `white` | rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px | 0 |
| [Filter sheet](#filter-sheet) | 1280 x 628 | - | 20px | #ffffff `white` | rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px | 68px 24px 24px 24px |
| [Mobile header](#mobile-header) | 390 x 46 | - | - | #212121 `ink.DEFAULT` | none | 0 |
| [Mobile menu drawer](#mobile-menu-drawer) | 390 x 798 | - | - | #ece9e2 `natural-white.60` (on `span.bg-natural-white-60.fixed`) | none | 0 |
| [Product card](#product-card) | 280.5 x 65 | - | - | transparent | none | 0 |
| [Upsell card](#upsell-card) | 338 x 116 | 1px solid oklch(0.928 0.006 264.531) | 10px | #ffffff `white` | none | 10px |
| [Tooltip pill](#tooltip-pill) | 273.73 x 40 | - | 3.35544e+07px | #242424 | rgba(0, 0, 0, 0.12) 0px 2px 20px 0px | 10px 12px |
| [Shop with AI chip](#shop-with-ai-chip) | 199.73 x 64 | 2px solid oklab(0.260318 0.0000118539 0.00000520051 / 0.2) | 3.35544e+07px | transparent | rgba(0, 0, 0, 0.25) 0px 2px 20px 0px, rgba(0, 0, 0, 0.25) 0px 0px 1px 0px | 0 |
| [Size button](#size-button) | 62.17 x 42 | 1px solid #cdcdcd `stroke` | 2px | transparent | none | 12px 0px |
| [Swatch](#swatch) | 36 x 36 | 3px solid #ffffff `white` | 3.35544e+07px | - (on `span.inset-ring-light-charcoal-0.7.pointer-events-none`) | transparent 0px 0px 0px 0px, rgba(87, 87, 87, 0.7) 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #212121 0px 0px 0px 1px | 0 |

## Components

### Shell and navigation

The storefront chrome on every page: the black announcement strip, then the rounded white nav bar (serif wordmark, uppercase xs links, MEN/WOMEN mega-menu buttons, search and bag) floating over the warm natural-white page.

#### Announcement bar
The rotating strip above the header ("Free ground shipping on orders over $100", shipping-delay notices): black fill, centred xs copy, prev/next chevrons at the ends (a Swiper carousel). Read as `promo-bar` on the home page.

**Values (default).** size 1440 x 32; background transparent; text Geograph 12/16 400, #ffffff `white`; icon 24 x 24, #ffffff `white`.

![Announcement bar default](components/crops/promo-bar-default.png)

#### Announcement bar arrow
Read as `promo-bar-next` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 24 x 24; background transparent; text Geograph 16/24 400, #ffffff `white`; icon 24 x 24, #ffffff `white` |

![Announcement bar arrow default](components/crops/promo-bar-next-default.png) ![Announcement bar arrow hover](components/crops/promo-bar-next-hover.png)

#### Header
The sticky rounded bar: wordmark centre-left, text links NEW ARRIVALS and SHOP ALL, the MEN and WOMEN mega-menu buttons, a Search link and the cart button with its count badge. Read as `header` on the home page.

**Values (default).** size 1400 x 48; padding 0px 20px; radius 12px; background #ffffff `white`; shadow rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px; text Geograph 12/16 500, #212121 `ink.DEFAULT`.

![Header default](components/crops/header-default.png)

#### Nav link
A text nav item: xs, medium, tracking-wider, uppercase. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 61.73 x 16; background transparent; text Geograph 12/16 500, #212121 `ink.DEFAULT`; transition opacity 0.2s cubic-bezier(0.37, 0, 0.63, 1) |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Mega-menu button
MEN/WOMEN open the mega-menu flyout on hover; measured, also hovered once for the flyout crop. Read as `nav-menu-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 30.42 x 16; background transparent; text Geograph 12/16 500, #212121 `ink.DEFAULT`; transition opacity 0.2s cubic-bezier(0.37, 0, 0.63, 1) |

![Mega-menu button default](components/crops/nav-menu-button-default.png) ![Mega-menu button hover](components/crops/nav-menu-button-hover.png) ![Mega-menu button pressed](components/crops/nav-menu-button-pressed.png)

#### Mega-menu flyout
The panel under MEN: category links and colour/material rows of circular swatches. Read as `mega-menu` on the home page.

**Values (default).** size 155.72 x 202; background transparent; text Geograph 12/16 500, #212121 `ink.DEFAULT`.

![Mega-menu flyout default](components/crops/mega-menu-default.png)

#### Cart button
The bag icon with the count badge on top; opens the cart drawer. Read as `cart-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 24; background transparent; text Geograph 9/13.5 500, #ffffff `white`; icon 24 x 24, #000000 |
| focus-visible | outline 1px auto #005fcc, offset 0px |

Child layers that carry the look: span 14x14 background #212121 `ink.DEFAULT` radius 3.35544e+07px.

![Cart button default](components/crops/cart-button-default.png) ![Cart button hover](components/crops/cart-button-hover.png) ![Cart button focus-visible](components/crops/cart-button-focus-visible.png) ![Cart button pressed](components/crops/cart-button-pressed.png)

#### Search link
The magnifier nav item; navigates to /search. Read as `search-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 24; background transparent; text Geograph 16/24 400, #000000; icon 24 x 24, #000000 |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Search link default](components/crops/search-link-default.png) ![Search link hover](components/crops/search-link-hover.png) ![Search link focus-visible](components/crops/search-link-focus-visible.png) ![Search link pressed](components/crops/search-link-pressed.png)

#### Footer
The black footer: subscribe row, HELP/SHOP/COMPANY link columns, legal links, the OneTrust "Do Not Sell" settings button. Read as `footer` on the home page.

**Values (default).** size 1440 x 763; padding 80px 40px 20px 40px; background #212121 `ink.DEFAULT`; text Akkurat Mono 12/16 400, #ffffff `white`; icon 24 x 24, #ffffff `white`.

![Footer default](components/crops/footer-default.png)

### Home

The marketing home page: rounded photo cards, serif headlines, pill CTAs and product carousels.

#### Hero
The first band: a rounded-corner photo card carrying the "Wildly Comfortable. Super Natural." headline and the two pill CTAs. Read as `hero` on the home page.

**Values (default).** size 1420 x 784; radius 20px; background transparent; text Akkurat Mono 12/20 500, #ffffff `white`.

Child layers that carry the look: a 122.3x33 background #ffffff `white` border 1px solid #ffffff `white` radius 3.35544e+07px; a 122.3x33 background #ffffff `white` border 1px solid #ffffff `white` radius 3.35544e+07px.

![Hero default](components/crops/hero-default.png)

#### Hero title
The home hero headline: it renders in Geograph (24px/32px, 0.6px tracking), not the brand serif. Read as `hero-title` on the home page.

**Values (default).** size 414.53 x 32; background transparent; text Geograph 24/32 400, #ffffff `white`.

![Hero title default](components/crops/hero-title-default.png)

#### Primary button
.btn.btn-primary: the white pill CTA ("SHOP MEN"), xs medium uppercase tracking-wider. Read as `cta-primary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 122.25 x 33; padding 8px 16px; border 1px solid #ffffff `white`; radius 3.35544e+07px; background #ffffff `white`; text Geograph 12/15 500, #212121 `ink.DEFAULT`; transition background-color 0.2s cubic-bezier(0.37, 0, 0.63, 1), color 0.2s cubic-bezier(0.37, 0, 0.63, 1), border-color 0.2s cubic-bezier(0.37, 0, 0.63, 1), opacity 0.2s cubic-bezier(0.61, 1, 0.88, 1) |
| hover | border 1px solid #212121 `ink.DEFAULT`; background #212121 `ink.DEFAULT`; text Geograph 12/15 500, #ffffff `white` |
| focus-visible | outline 1px auto oklch(0.546 0.245 262.881), offset 1px |
| pressed | border 1px solid #212121 `ink.DEFAULT`; background #212121 `ink.DEFAULT`; text Geograph 12/15 500, #ffffff `white` |

![Primary button default](components/crops/cta-primary-default.png) ![Primary button hover](components/crops/cta-primary-hover.png) ![Primary button focus-visible](components/crops/cta-primary-focus-visible.png) ![Primary button pressed](components/crops/cta-primary-pressed.png)

#### Outline button
.btn.btn-outline-white: the bordered pill used on category cards. Read as `cta-outline-white` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 122.25 x 33; padding 8px 16px; border 1px solid #ffffff `white`; radius 3.35544e+07px; background transparent; text Geograph 12/15 500, #ffffff `white`; transition background-color 0.2s cubic-bezier(0.37, 0, 0.63, 1), color 0.2s cubic-bezier(0.37, 0, 0.63, 1), border-color 0.2s cubic-bezier(0.37, 0, 0.63, 1), opacity 0.2s cubic-bezier(0.61, 1, 0.88, 1) |

![Outline button default](components/crops/cta-outline-white-default.png) ![Outline button hover](components/crops/cta-outline-white-hover.png)

#### Section title
Marketing section headline in the brand serif, fluid 30-40px. Read as `section-title` on the home page.

**Values (default).** size 407.92 x 60; background transparent; text Self Modern 40/60 400, #ffffff `white`.

![Section title default](components/crops/section-title-default.png)

#### Carousel arrow
A 24-40px round icon button at the edge of a product/media carousel. Read as `carousel-nav` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 24 x 24; background transparent; text Geograph 16/24 400, #ffffff `white`; icon 24 x 24, #ffffff `white` |

![Carousel arrow default](components/crops/carousel-nav-default.png) ![Carousel arrow hover](components/crops/carousel-nav-hover.png)

### Collection grid

The collection page: title, the Filter button and its sheet, then product cards in a grid.

#### Collection title
The collection page heading. Read as `collection-title` on the collection page.

**Values (default).** size 139.19 x 32; background transparent; text Geograph 24/32 400, #ffffff `white`.

![Collection title default](components/crops/collection-title-default.png)

#### Filter button
Opens the filter/sort sheet; labelled with the product count. The sheet itself is the filter-sheet component. Read as `filter-button` on the collection page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 183.48 x 34; background transparent; text Geograph 14/20 500, oklch(0.446 0.03 256.802); icon 24 x 24, #000000 |
| focus-visible | outline 1px auto #005fcc, offset 0px |

Child layers that carry the look: span 34x34 border 1px solid #212121 `ink.DEFAULT` radius 3.35544e+07px.

![Filter button default](components/crops/filter-button-default.png) ![Filter button hover](components/crops/filter-button-hover.png) ![Filter button focus-visible](components/crops/filter-button-focus-visible.png) ![Filter button pressed](components/crops/filter-button-pressed.png)

#### Filter sheet
The panel the Filter button opens: size/price/colour groups with checkboxes. Read as `filter-sheet` on the collection page.

**Values (open).** size 1280 x 628; padding 68px 24px 24px 24px; radius 20px; background #ffffff `white`; shadow rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px; text Geograph 16/24 500, #000000; icon 32 x 32, #000000.

![Filter sheet open](components/crops/filter-sheet-open.png)

#### Product card
A grid card: rounded-2xl photo, name, colour name, price; hover swaps in the second photo (opacity fade on a z-[1] image). Read as `product-card` on the collection page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 280.5 x 65; background transparent; text Geograph 14/20 500, #000000 |

![Product card default](components/crops/product-card-default.png) ![Product card hover](components/crops/product-card-hover.png)

#### Card photo
Read as `card-image` on the collection page.

**Values (default).** size 312.5 x 312.5; background transparent; text Geograph 16/24 400, #000000; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Card photo default](components/crops/card-image-default.png)

#### More colours link
The "+6" under a card: xs medium underline, points at the product page. Read as `more-colors` on the collection page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 16.7 x 14; background transparent; text Geograph 14/14 500, #000000; decoration underline |

![More colours link default](components/crops/more-colors-default.png) ![More colours link hover](components/crops/more-colors-hover.png)

### Product page

The PDP buy box: serif title, uppercase price, colour swatches, the men/women size tab, the 62x42 size grid (sold-out chips struck through), Fit Guide, the black Add to Cart pill and the detail accordions.

#### Product title
"Men's Tree Runner NZ" in the brand serif. Read as `pdp-title` on the product page.

**Values (default).** size 483.19 x 36; background transparent; text Self Modern 30/36 400, #000000.

![Product title default](components/crops/pdp-title-default.png)

#### Price
Read as `pdp-price` on the product page.

**Values (default).** size 44.86 x 28; background transparent; text Geograph 18/28 500, #212121 `ink.DEFAULT`.

![Price default](components/crops/pdp-price-default.png)

#### Swatch group
The colour picker: rows of circular swatches (uppercase group labels like "JERSEY", "STRIPE"). Read as `swatch-group` on the product page.

**Values (default).** size 483.19 x 76; background transparent; text Geograph 16/24 400, #000000.

Child layers that carry the look: span 36x36 image linear-gradient(135deg, #8b8a8f 50%, #e0e2dc 50%) border 3px solid #ffffff `white` radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, rgba(87, 87, 87, 0.7) `ink.light-charcoal-07` 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #212121 `ink.DEFAULT` 0px 0px 0px 1px; span 36x36 image linear-gradient(135deg, #242729 50%, #e0e2dc 50%) border 3px solid #ffffff `white` radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, rgba(87, 87, 87, 0.7) `ink.light-charcoal-07` 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px; span 36x36 background #242729 border 3px solid #ffffff `white` radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, rgba(87, 87, 87, 0.7) `ink.light-charcoal-07` 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px.

![Swatch group default](components/crops/swatch-group-default.png)

#### Swatch
One colour circle; the selected one carries a ring. Read as `swatch` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 36 x 36; radius 3.35544e+07px; background transparent; text Geograph 16/24 400, #000000 |
| focus-visible | outline 1px auto #005fcc, offset 0px |

Child layers that carry the look: span 36x36 image linear-gradient(135deg, #8b8a8f 50%, #e0e2dc 50%) border 3px solid #ffffff `white` radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, rgba(87, 87, 87, 0.7) `ink.light-charcoal-07` 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #212121 `ink.DEFAULT` 0px 0px 0px 1px.

![Swatch default](components/crops/swatch-default.png) ![Swatch hover](components/crops/swatch-hover.png) ![Swatch focus-visible](components/crops/swatch-focus-visible.png) ![Swatch pressed](components/crops/swatch-pressed.png)

#### Size tab, active
The underlined "MEN'S SIZES" tab of the men/women size-grid switch. Read as `size-tab-active` on the product page.

**Values (default).** size 121.95 x 17; background transparent; text Akkurat Mono 14/20 400, #575757 `ink.light-charcoal`; decoration underline.

![Size tab, active default](components/crops/size-tab-active-default.png)

#### Size tab
The inactive tab: light-charcoal, transparent border. Read as `size-tab` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 121.95 x 21; border B: 1px solid transparent; background transparent; text Akkurat Mono 14/20 400, #575757 `ink.light-charcoal`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border B: 1px solid #212121 `ink.DEFAULT` |

Child layers that carry the look: a 122x21 border 1px solid transparent.

![Size tab default](components/crops/size-tab-default.png) ![Size tab hover](components/crops/size-tab-hover.png)

#### Size button
.btn-size: the bordered size chip; selected state fills black with white text (measured after one was clicked). Read as `size-button` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 62.17 x 42; padding 12px 0px; border 1px solid #cdcdcd `stroke`; radius 2px; background transparent; text Geograph 12/16 500, #000000; transition color 0.2s cubic-bezier(0.37, 0, 0.63, 1), background-color 0.2s cubic-bezier(0.37, 0, 0.63, 1), border-color 0.2s cubic-bezier(0.37, 0, 0.63, 1), outline-color 0.2s cubic-bezier(0.37, 0, 0.63, 1), text-decoration-color 0.2s cubic-bezier(0.37, 0, 0.63, 1), fill 0.2s cubic-bezier(0.37, 0, 0.63, 1), stroke 0.2s cubic-bezier(0.37, 0, 0.63, 1), --tw-gradient-from 0.2s cubic-bezier(0.37, 0, 0.63, 1), --tw-gradient-via 0.2s cubic-bezier(0.37, 0, 0.63, 1), --tw-gradient-to 0.2s cubic-bezier(0.37, 0, 0.63, 1) |
| hover, pressed | background rgba(87, 87, 87, 0.19) `ink.light-charcoal-03` |

![Size button default](components/crops/size-button-default.png) ![Size button hover](components/crops/size-button-hover.png) ![Size button pressed](components/crops/size-button-pressed.png)

#### Size button, sold out
.btn-size.disabled: the struck-through greyed chip. Read as `size-button-disabled` on the product page.

**Values (default).** size 62.16 x 42; padding 12px 0px; border 1px solid #cdcdcd `stroke`; radius 2px; background transparent; text Geograph 12/16 500, oklch(0.707 0.022 261.325); transition color 0.2s cubic-bezier(0.37, 0, 0.63, 1), background-color 0.2s cubic-bezier(0.37, 0, 0.63, 1), border-color 0.2s cubic-bezier(0.37, 0, 0.63, 1), outline-color 0.2s cubic-bezier(0.37, 0, 0.63, 1), text-decoration-color 0.2s cubic-bezier(0.37, 0, 0.63, 1), fill 0.2s cubic-bezier(0.37, 0, 0.63, 1), stroke 0.2s cubic-bezier(0.37, 0, 0.63, 1), --tw-gradient-from 0.2s cubic-bezier(0.37, 0, 0.63, 1), --tw-gradient-via 0.2s cubic-bezier(0.37, 0, 0.63, 1), --tw-gradient-to 0.2s cubic-bezier(0.37, 0, 0.63, 1); opacity 0.7; icon 60.16 x 40, oklch(0.707 0.022 261.325).

![Size button, sold out default](components/crops/size-button-disabled-default.png)

#### Fit Guide link
The underlined text button under the size grid. Read as `fit-guide` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 51.63 x 16; background transparent; text Geograph 12/16 400, #575757 `ink.light-charcoal`; decoration underline |

![Fit Guide link default](components/crops/fit-guide-default.png) ![Fit Guide link hover](components/crops/fit-guide-hover.png)

#### Add to Cart button
.btn.btn-secondary: the full-width black pill under the buy box ("ADD TO CART - $100"). Mounted once a size is picked; clicked once for the cart drawer, checkout never pressed. Read as `atc-button` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 483.19 x 49; padding 16px; border 1px solid #212121 `ink.DEFAULT`; radius 3.35544e+07px; background #212121 `ink.DEFAULT`; text Geograph 12/15 500, #ffffff `white`; transition background-color 0.2s cubic-bezier(0.37, 0, 0.63, 1), color 0.2s cubic-bezier(0.37, 0, 0.63, 1), border-color 0.2s cubic-bezier(0.37, 0, 0.63, 1), opacity 0.2s cubic-bezier(0.61, 1, 0.88, 1) |
| hover | background #575757 `ink.light-charcoal` |
| focus-visible | outline 1px auto oklch(0.546 0.245 262.881), offset 0px |
| pressed | background #575757 `ink.light-charcoal` |

![Add to Cart button default](components/crops/atc-button-default.png) ![Add to Cart button hover](components/crops/atc-button-hover.png) ![Add to Cart button focus-visible](components/crops/atc-button-focus-visible.png) ![Add to Cart button pressed](components/crops/atc-button-pressed.png)

#### Accordion row
A PDP details row (WHY WE LOVE THIS, MATERIALS & SUSTAINABILITY, CARE INSTRUCTIONS): full-width, py-6, plus/minus on the right. Read as `accordion` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: open, hover) | size 1364 x 72; padding 24px 0px; background transparent; text Akkurat Mono 16/24 400, #000000 |

Child layers that carry the look: span 16x1 background #000000; span 16x1 background #000000.

![Accordion row default](components/crops/accordion-default.png) ![Accordion row open](components/crops/accordion-open.png) ![Accordion row hover](components/crops/accordion-hover.png)

#### Tooltip pill
The black pill over the gallery (e.g. "Tree-based upper for lightweight comfort") that opens a material tooltip. Read as `tooltip-pill` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 273.73 x 40; padding 10px 12px; radius 3.35544e+07px; background #242424; shadow rgba(0, 0, 0, 0.12) 0px 2px 20px 0px; text Barlow 14/20 400, #ffffff `white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

![Tooltip pill default](components/crops/tooltip-pill-default.png) ![Tooltip pill hover](components/crops/tooltip-pill-hover.png)

### Cart drawer

The right-hand takeover after Add to Cart: free-shipping meter, item rows with a qty stepper, a natural-white-60 upsell band, subtotal and checkout. Never checked out.

#### Cart drawer
The right-hand .z-takeover drawer after Add to Cart: CART heading, free-shipping meter, item rows, upsell carousel, subtotal and the checkout buttons. Never checked out. Read as `cart-drawer` on the product page.

**Values (open).** size 531 x 900; background #ffffff `white`; shadow rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px; text Geograph 12/16 500, #000000; icon 32 x 32, #000000.

![Cart drawer open](components/crops/cart-drawer-open.png)

#### Quantity stepper
The +/- stepper on a cart row. Read as `cart-qty` on the product page.

**Values (default).** size 7.2 x 16; background transparent; text Geograph 12/16 500, #212121 `ink.DEFAULT`.

![Quantity stepper default](components/crops/cart-qty-default.png)

#### Upsell card
RECOMMENDED FOR YOU carousel cards with a size select and an "Add+" link. Read as `cart-upsell-card` on the product page.

**Values (default).** size 338 x 116; padding 10px; border 1px solid oklch(0.928 0.006 264.531); radius 10px; background #ffffff `white`; text Geograph 14/20 400, #575757 `ink.light-charcoal`; icon 16 x 16, #000000.

![Upsell card default](components/crops/cart-upsell-card-default.png)

#### Checkout button
The black "Checkout+ | $104.98" pill in the cart drawer footer. Rendered by Shopify's checkout surface (shadow DOM / iframe): visible in the drawer crop but not introspectable from the page DOM, so no computed style was recorded. Never pressed. Read as `checkout-button` on the product page.

Not on the page when it was captured.

#### Express pay buttons
The Amazon Pay / G Pay / PayPal / Shop Pay wallet row under checkout. Shopify-hosted (iframes/shadow): visible in the drawer crop, not introspectable from the page DOM, so no computed style was recorded. Read as `express-button` on the product page.

Not on the page when it was captured.

### Forms

Fields reachable signed out: the footer subscribe row, the search page and the Shopify-hosted account login.

#### Search field
The /search page field. Text was typed and deleted; never submitted. Read as `search-input` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 676 x 40; padding 8px 32px 8px 8px; radius 6px; background transparent; text Geograph 16/24 400, #000000; placeholder oklab(0 0 0 / 0.5) |

![Search field default](components/crops/search-input-default.png) ![Search field focused](components/crops/search-input-focused.png) ![Search field filled](components/crops/search-input-filled.png)

#### Search submit
Measured, never pressed. Read as `search-submit` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 24 x 40; background transparent; text Geograph 16/24 400, #000000; icon 24 x 24, #000000 |

![Search submit default](components/crops/search-submit-default.png) ![Search submit hover](components/crops/search-submit-hover.png)

#### Login email field
The account sign-in field on the public login page. Text was typed and deleted; never submitted. Read as `login-input` on the account page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 337 x 47; padding 13.55px 10px; background transparent; text lBKuE1Nf 14/18.9 400, #000000; transition all 0.2s ease-in-out; placeholder #707070 |
| filled | padding 21.05px 10px 6.05px 10px |

![Login email field default](components/crops/login-input-default.png) ![Login email field focused](components/crops/login-input-focused.png) ![Login email field filled](components/crops/login-input-filled.png)

#### Sign-in button
Measured, never pressed; signing in was out of scope. The account page is Shopify-hosted (Shop account UI). Read as `login-submit` on the account page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 345 x 50; radius 8px; background #5433eb; text GTStandard-M 16/22 500, #ffffff `white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 38.39 x 16, #ffffff `white` |
| hover | background #4524db |

![Sign-in button default](components/crops/login-submit-default.png) ![Sign-in button hover](components/crops/login-submit-hover.png)

#### Email field
The footer subscribe field. Text was typed and deleted; never submitted. Read as `email-input` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 42; padding 10px 80px 10px 12px; border 1px solid #212121 `ink.DEFAULT`; radius 3.35544e+07px; background #ffffff `white`; text Geograph 16/24 400, #212121 `ink.DEFAULT`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder oklch(0.551 0.027 264.364) |
| focused, filled | outline 1px auto #005fcc, offset 0px |

![Email field default](components/crops/email-input-default.png) ![Email field focused](components/crops/email-input-focused.png) ![Email field filled](components/crops/email-input-filled.png)

#### Sign Up button
.btn.btn-outline on the subscribe row. Measured, never submitted. Read as `signup-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 81.58 x 31; padding 8px 16px; radius 3.35544e+07px; background transparent; text Geograph 12/15 700, #212121 `ink.DEFAULT`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| pressed | opacity 0.85 |

![Sign Up button default](components/crops/signup-button-default.png) ![Sign Up button hover](components/crops/signup-button-hover.png) ![Sign Up button pressed](components/crops/signup-button-pressed.png)

### Mobile (390 wide)

The same components as a phone draws them, at 390 x 844 with an iPhone user agent.

#### Mobile header
The rounded pill bar: hamburger, wordmark, search and bag icons. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 46; background #212121 `ink.DEFAULT`; text Geograph 10/15 400, #ffffff `white`; icon 24 x 24, #ffffff `white`.

![Mobile header default](components/crops/m-header-default.png)

#### Hamburger button
Opens the mobile menu drawer. Read as `m-hamburger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 24 x 24; radius 6px; background transparent; text Geograph 16/24 400, #000000 |

![Hamburger button default](components/crops/m-hamburger-default.png) ![Hamburger button pressed](components/crops/m-hamburger-pressed.png)

#### Mobile menu drawer
The sheet the hamburger opens: NEW ARRIVALS / SHOP ALL text rows, MEN and WOMEN with chevrons, and a footer of category links. Read as `m-menu-drawer` on the home page at 390 wide.

**Values (open).** size 390 x 798; background transparent; text Geograph 14/21 500, #000000; icon 24 x 24, #000000.

Child layers that carry the look: span 390x844 background #ece9e2 `natural-white.60`; ul 350x131 background #ffffff `white` radius 4px; div 0x0 background #e0dacf `natural-white.DEFAULT` radius 20px.

![Mobile menu drawer open](components/crops/m-menu-drawer-open.png)

#### Shop with AI chip
The floating pill bottom-right: spark icon, label, close X. Never opened. Read as `m-ai-chip` on the home page at 390 wide.

**Values (default).** size 199.73 x 64; border 2px solid oklab(0.260318 0.0000118539 0.00000520051 / 0.2); radius 3.35544e+07px; background transparent; shadow rgba(0, 0, 0, 0.25) 0px 2px 20px 0px, rgba(0, 0, 0, 0.25) 0px 0px 1px 0px; text Barlow 16/22 400, transparent; icon 24 x 24, #ffffff `white`.

![Shop with AI chip default](components/crops/m-ai-chip-default.png)
## Gaps

### Pages

- **Signed-in pages.** Nothing behind sign-in was captured: account details, order history, saved addresses/payments and the checkout flow itself. The account page is Shopify-hosted and was only measured at the login card.
- **Anything that buys or sends.** Checkout was never pressed, no order placed, no search submitted, no subscribe or login form sent; the cart stays a session cart.
- **The geofencing dialog** ("Where are we shipping to?", US/SG choices over a `bg-black/50` dim) mounts on first visits only and did not mount during the measurement runs, so it has no entry. Its layer is `z-takeover` like every other takeover.
- **Reviews, wishlist and recommendation widgets** below the PDP buy box were not reached (the tour stops at the details accordions).

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover), so a state a script adds on mousedown (if any) is missing.
- **The gallery tooltip pill and the mobile "Shop with AI" chip** mount intermittently (media-load dependent); their measurements come from runs where they rendered, and may be flagged absent on a given run.
- **Checkout and express-pay buttons** in the cart drawer are Shopify-hosted surfaces (iframes/shadow DOM): visible in [cart-drawer-open](components/crops/cart-drawer-open.png) but not introspectable from the page DOM, so they carry no computed styles.

### Themes

Allbirds serves one light theme: no dark attribute is set anywhere, the Tailwind v4 theme layer declares no dark variant, and nothing in the capture hints at a toggle. The token file therefore ships no dark set.

### Fonts

- **Geograph**, **Self Modern** and **Akkurat Mono** are Allbirds' own faces, served as woff2 from theme assets (`fonts` in [raw/css-vars.json](raw/css-vars.json), 10 `@font-face` rules). The style guide falls back to the system serif/sans/mono for them.
- The **Shopify-hosted login** uses Shop's own faces (GTStandard, lBKuE1Nf) which are not part of the theme's tokens.

### Screenshots

- Product photography is Allbirds' content and appears only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- No personal data was captured: every page was read signed out with an empty session, and the only form text typed was sample text, deleted before capture ended.
