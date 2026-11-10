# adidas components

The discovery list of every page and state captured, then one entry per component with crops of the real site, the shared values and the Gaps. Captured from adidas.com.cn on 2026-11-10 — the China flagship storefront (prices in CNY ¥) — as static pages rendered at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the live DOM. Nothing was submitted, bought or signed into; the only presses were local UI toggles (the Search disclosure, Email sign up modal, My cart drawer, All filters rail, burger menu). The OneTrust consent SDK was blocked at the network layer — its banner was never mounted, and no consent button was ever pressed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (21 components, 41 states).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) whose value is the same, when there is one. Text is written family size/line-height weight, then its colour, for example `Chinese UI sans 12/20 400, #000000`, and is read from the first text node inside the component.
- The first state of each entry lists every value; later states list only what changed. A state identical to the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component in [components/crops/](components/crops) (41 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`. Desktop shots are 1440 x 900 at 2x; `-full` shots are whole pages; mobile shots are `mobile-{page}-light-{state}.png`, 390 x 844 at 2x. Only light exists — the storefront has no dark theme.

| Surface | URL | Screenshots |
|---|---|---|
| Home. The hero, product rows and footer. Captured at rest, search open, sign-up modal, cart drawer, nav hover, and full-page. | `/` | [default (light)](screenshots/home-light-default.png), [full (light)](screenshots/home-light-full.png), [search (light)](screenshots/home-light-search.png) |
| Shop all, the catalogue page. Captured at rest, filters rail open, and full-page. | `/shop-all/` |  |
| The Skin Care category landing. | `/skin-care/` |  |
| A product page (The adidas Valise, APB399). Captured at rest, an accordion open, and full-page. | `/gifts/seasonal-gift-kits/the-aesop-valise/APB399.html` | [default (light)](screenshots/pdp-light-default.png), [full (light)](screenshots/pdp-light-full.png) |
| The store locator. | `/stores` |  |
| The cart route, empty. | `/cart` | [default (light)](screenshots/cart-light-default.png), [full (light)](screenshots/cart-light-full.png) |
| The Demandware sign-in page. | `/on/demandware.store/Sites-aesop-us-Site/en_US/Login-Show` |  |
| The styled 404 / unexpected-error page. | `/account` |  |
| Home at 390, at rest, the burger drawer open, and full-page. | `/` | [default (light)](screenshots/mobile-home-light-default.png), [full (light)](screenshots/mobile-home-light-full.png), [menu (light)](screenshots/mobile-home-light-menu.png) |
| The catalogue page at 390. | `/shop-all/` |  |
| The product page at 390. | `/gifts/seasonal-gift-kits/the-aesop-valise/APB399.html` | [default (light)](screenshots/mobile-pdp-light-default.png), [full (light)](screenshots/mobile-pdp-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Search disclosure | home | the Search header button | [home-light-search](screenshots/home-light-search.png), [search-field](#search-field) |
| Email sign up modal | home | the Email sign up button | [home-light-signup](screenshots/home-light-signup.png), [signup-dialog](#signup-dialog) |
| My cart drawer | home | the My cart button | [home-light-cart](screenshots/home-light-cart.png), [cart-panel](#cart-panel) |
| Filter rail | PLP | the All filters button | [shopall-light-sort](screenshots/shopall-light-sort.png), [filter-panel](#filter-panel) |
| Accordion opened | PDP | a PDP accordion row | [pdp-light-accordion](screenshots/pdp-light-accordion.png) |
| Mobile burger drawer | home at 390 | the burger button | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-drawer](#m-menu-drawer) |

## Shared values

Values that apply across entries, tallied from the measurement file.

**Radius.** none — every corner on the site is 0px. The single curve is the filter rail's 10px radio dot (`border-radius:100%` on a `::before`).

**Hover.** Acne hovers with colour, never fills or shadows: no change on the element (8), #ffffff `action.primaryText` to #eceff1 `background.inset` (1). Black fills (LOAD MORE, CONTINUE, SHOW N ITEMS) flip to Acne blue; blue fills (ADD TO BAG) deepen to #051574; blue links deepen the same way; black labels (nav, FILTER, Menu) grey to #6b6b6b.

**Focus.** Of 3 elements given a real keyboard focus: focus could not be driven (5), no ring on the element (2), 1px auto #005fcc offset 1px (1). The ring Acne does draw is a 1px solid keyline 3px inside the control — white on the black/blue buttons, deep blue on the white wishlist button, black on the size cells. Text links show no ring.

**Motion.** 0.3s ease-in (1). The only transitions the stylesheet carries are the drawers' 150ms padding-bottom safe-area slide, the accordions' 200ms max-height reveal and a 500ms fade on campaign layers, none on the controls themselves.

**Layout.** The header is a 60px rail (45px at 390); every page is a 1440-wide fluid grid of 4-px-base cells (`as-cell`). Primary buttons and the email fields share one 60px height; the small search field, menu links, suggestions and gift-guide bars are 30px rows; size cells are 77 x 45; every right-side drawer is 360 wide with a 45px head. Hairline 1px rules in #f2f2f2 (or black on drawers and the mega-menu's top edge) separate everything — several are painted as 1px background gradients rather than borders.

**Accent.** Acne blue (#0018a8) is the only accent: every text link, the ADD TO BAG fill, the wishlist border, the picked size cell's border and fill, the geo selector, and the hover step of every black button. Its deeper step #051574 is hover-only. Everything else is black, white or one of four warm greys.

## Components

### Shell and navigation

The two-tier header every page shares: a thin utility row (Stores, Customer service / Email sign up, Account, My cart), the centred Aēsop wordmark and the main-nav row ending in a Search disclosure trigger. Cream-on-ink, transparent over the hero.

#### Header

<a id="header"></a>`header`, on home. The sticky top bar every page shares: a utility strip (在线客服, 请登录), the adidas wordmark, the category nav and the campaign tag strip.

<img src="components/crops/header-default.png" alt="Header, default" height="120"> 

| State | Values |
|---|---|
| default | size 1440 x 124; background #ffffff `action.primaryText`; text AdihausDIN 13/18 400, #ffffff `text.onDark`; transition all 0.3s ease-in |

#### Nav item

<a id="nav-item"></a>`nav-item`, on home. A top-level category item (男装, 男鞋, 女装, 女鞋, 儿童, 配件).

<img src="components/crops/nav-item-default.png" alt="Nav item, default" height="84"> <img src="components/crops/nav-item-hover.png" alt="Nav item, hover" height="84"> <img src="components/crops/nav-item-focus-visible.png" alt="Nav item, focus-visible" height="84"> <img src="components/crops/nav-item-pressed.png" alt="Nav item, pressed" height="84"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 47 x 84; background transparent; text AdihausDIN 15/20 700, #000000 `text.primary` |

#### Utility link

<a id="utility-link"></a>`utility-link`, on home. A utility-strip entry (在线客服 online service, 请登录 sign in).

<img src="components/crops/utility-link-default.png" alt="Utility link, default" height="38"> <img src="components/crops/utility-link-hover.png" alt="Utility link, hover" height="38"> <img src="components/crops/utility-link-focus-visible.png" alt="Utility link, focus-visible" height="38"> <img src="components/crops/utility-link-pressed.png" alt="Utility link, pressed" height="38"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 74 x 38; background transparent; text AdihausDIN 13/18 400, #ffffff `text.onDark` |

#### Promo tag

<a id="promo-tag"></a>`promo-tag`, on home. A campaign tag in the strip under the nav (11.11 不止5折, 雪境漫游, 降温毛衣精选).

<img src="components/crops/promo-tag-default.png" alt="Promo tag, default" height="32"> <img src="components/crops/promo-tag-hover.png" alt="Promo tag, hover" height="32"> <img src="components/crops/promo-tag-focus-visible.png" alt="Promo tag, focus-visible" height="32"> <img src="components/crops/promo-tag-pressed.png" alt="Promo tag, pressed" height="32"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 261.33 x 32; background #f9f9f9 `background.surface`; text AdihausDIN-Woff 13/18 400, #9a9b9b `text.muted` |

#### Wordmark

<a id="logo"></a>`logo`, on home. The adidas wordmark linking home.

<img src="components/crops/logo-default.png" alt="Wordmark, default" height="84"> 

| State | Values |
|---|---|
| default | size 84 x 84; background transparent |

### Home

The home canvas: a full-bleed campaign band under the transparent header (photography or film, an overlaid line and a bordered CTA card), then product rows and the dark footer.

#### Hero

<a id="hero"></a>`hero`, on home. The campaign band under the header: photography, a headline and a 立即选购 CTA.

<img src="components/crops/hero-default.png" alt="Hero, default" height="40"> 

| State | Values |
|---|---|
| default | size 1143 x 40; background transparent |

#### Primary CTA

<a id="hero-cta"></a>`hero-cta`, on home. A lib-button campaign CTA (立即选购 "Shop now").

<img src="components/crops/hero-cta-default.png" alt="Primary CTA, default" height="48"> <img src="components/crops/hero-cta-hover.png" alt="Primary CTA, hover" height="48"> <img src="components/crops/hero-cta-focus-visible.png" alt="Primary CTA, focus-visible" height="48"> <img src="components/crops/hero-cta-pressed.png" alt="Primary CTA, pressed" height="48"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 200 x 48; padding 0px 16px; background #ffffff `action.primaryText`; text AdihausDIN 14/20 700, #000000 `text.primary` |
| hover, pressed | background #eceff1 `background.inset` |

### Footer

The dark page foot (ink #252525): secure-checkout and complimentary-samples lines, the Orders and support / About / Sustainability link columns in cream, and the Online Preferences OneTrust trigger.

#### Footer

<a id="footer"></a>`footer`, on pdp. The page foot: link columns and the tel:400-999-5999 service line.

<img src="components/crops/footer-default.png" alt="Footer, default" height="120"> 

| State | Values |
|---|---|
| default | size 1440 x 360; background transparent; text AdihausDIN 15/20 700, #000000 `text.primary` |

Child layers: div 1440x360 background #f9f9f9 `background.surface`; div 108x122 background #ffffff `action.primaryText`; div 8x8 background #ffffff `action.primaryText`

#### Footer link

<a id="footer-link"></a>`footer-link`, on pdp. A footer link entry.

<img src="components/crops/footer-link-default.png" alt="Footer link, default" height="32"> <img src="components/crops/footer-link-hover.png" alt="Footer link, hover" height="32"> <img src="components/crops/footer-link-focus-visible.png" alt="Footer link, focus-visible" height="32"> <img src="components/crops/footer-link-pressed.png" alt="Footer link, pressed" height="32"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 57.8 x 32; padding 8px 0px; background transparent; text AdihausDIN 11/16 400, #000000 `text.primary` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

### Catalogue page (PLP)

A catalogue page such as Shop all: the category title and product count, an All filters toggle opening a 400px left rail of accordion groups (Price, Skin type, Skin concern, Form, Ingredients, Aroma), a Sort select, then the tile grid — photograph, bold name, descriptor, size select, price, ink add-to-cart.

#### Page title

<a id="plp-title"></a>`plp-title`, on plp. The catalogue page heading.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

#### Filter row

<a id="filter-row"></a>`filter-row`, on plp. A refinement row in the left filter column (性别 gender, category, price).

<img src="components/crops/filter-row-default.png" alt="Filter row, default" height="56"> <img src="components/crops/filter-row-hover.png" alt="Filter row, hover" height="56"> <img src="components/crops/filter-row-focus-visible.png" alt="Filter row, focus-visible" height="56"> <img src="components/crops/filter-row-pressed.png" alt="Filter row, pressed" height="56"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 51 x 56; padding 19px 24px 19px 0px; background transparent; text AdihausDIN 13/18 400, #9a9b9b `text.muted` |

#### Product tile

<a id="product-card"></a>`product-card`, on plp. A product card linking /pdp?articleId=… : image, name, price.

<img src="components/crops/product-card-default.png" alt="Product tile, default" height="120"> <img src="components/crops/product-card-hover.png" alt="Product tile, hover" height="120"> 

| State | Values |
|---|---|
| default (same: hover) | size 338.5 x 454.5; background transparent; text AdihausDIN 11/16 400, #000000 `text.primary` |

Child layers: div 338.5x454.5 background #eceff1 `background.inset` border 1px solid #eceff1 `background.inset`; li 40.3x24 background #ffffff `action.primaryText`; div 2x2 background #9a9b9b `text.muted`

#### Tile name

<a id="product-card-name"></a>`product-card-name`, on plp. The product name inside a tile.

<img src="components/crops/product-card-name-default.png" alt="Tile name, default" height="30"> 

| State | Values |
|---|---|
| default | size 312.5 x 30; background transparent; text AdihausDIN 13/18 700, #000000 `text.primary` |

#### Tile price

<a id="product-card-price"></a>`product-card-price`, on plp. The ¥ price inside a tile.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

### Product page (PDP)

A product detail page: breadcrumbs over a two-column canvas (gallery left, purchase column right) — badge line, product title, price, descriptor, the bordered variant/size box, the ink Add to cart bar, then expandable rows and a suggested-partners rail.

#### Product title

<a id="pdp-title"></a>`pdp-title`, on pdp. The product name heading.

<img src="components/crops/pdp-title-default.png" alt="Product title, default" height="30"> 

| State | Values |
|---|---|
| default | size 399.94 x 30; background transparent; text adineuePRO 24/30 700, #000000 `text.primary` |

#### Product price

<a id="pdp-price"></a>`pdp-price`, on pdp. The ¥ price beside the title.

<img src="components/crops/pdp-price-default.png" alt="Product price, default" height="24"> 

| State | Values |
|---|---|
| default | size 41.67 x 22; background transparent; text adineuePRO 18/22 700, #000000 `text.primary` |

#### Add-to-cart button

<a id="add-to-cart"></a>`add-to-cart`, on pdp. The primary purchase bar (加入购物袋). Measured, never pressed.

<img src="components/crops/add-to-cart-default.png" alt="Add-to-cart button, default" height="48"> <img src="components/crops/add-to-cart-hover.png" alt="Add-to-cart button, hover" height="48"> <img src="components/crops/add-to-cart-focus-visible.png" alt="Add-to-cart button, focus-visible" height="48"> <img src="components/crops/add-to-cart-pressed.png" alt="Add-to-cart button, pressed" height="48"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 399.94 x 48; padding 0px 16px; background #ffffff `action.primaryText`; text AdihausDIN 14/20 700, #c8cbcc `text.disabled` |

#### Size cell

<a id="size-cell"></a>`size-cell`, on pdp. A size/spec cell on the PDP.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

#### Accordion row

<a id="accordion"></a>`accordion`, on pdp. An expandable detail row on the PDP.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

### Mobile (390 wide)

The same storefront at 390: the header collapses to Stores, wordmark and My cart; the burger button opens a flat accordion drawer of 48px rows.

#### Mobile header

<a id="m-header"></a>`m-header`, on home. The header at 390 wide.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

#### Burger button

<a id="m-burger"></a>`m-burger`, on home. The menu button on mobile, if visible.

<img src="components/crops/m-burger-default.png" alt="Burger button, default" height="60"> <img src="components/crops/m-burger-hover.png" alt="Burger button, hover" height="60"> <img src="components/crops/m-burger-focus-visible.png" alt="Burger button, focus-visible" height="60"> <img src="components/crops/m-burger-pressed.png" alt="Burger button, pressed" height="60"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 40 x 60; background transparent |

## Gaps

- The Email sign up modal mounts as a cream shell (970 x 450 measured); its remote Demandware Newsletter-SignUp fragment did not render in headless Chromium, so the dialog's fields, checkboxes and submit were never measurable — `signup-field`, `signup-checkbox` and `signup-submit` are honest misses.
- States that submit were never pressed: ADD TO CART, APPLY, the sign-in Submit, the store OK. Their hover, focus and pressed styles come from CDP-forced pseudo-classes and keyboard focus, not real clicks.
- `search-panel`'s container eluded marking (the disclosure mounts under a different id), but `search-field` and `search-close` inside it are measured, and the open state is in screenshots. `cart-close` has no measurable button: the drawer closes on backdrop/Escape.
- `qty-select` is absent on this PDP (a one-variant kit); the variant/size box is measured instead. `no-result-dialog` was measured at 415 x 211.
- Cloudflare Turnstile gates second document loads per context and some system routes: PDPs are reached as a first load in a fresh context (see tools/capture/public/lib.mjs note), and a still-blocked route would be recorded, not fought.
- Hover/focus on the 390 capture is not meaningful (a phone has neither); mobile entries cover layout and the burger drawer.

