# adidas components

The discovery list of every page and state captured, then one entry per component with crops of the real site, the shared values and the Gaps. Captured from adidas.com.cn on 2026-11-10 — the China flagship storefront (prices in CNY ¥) — as static pages rendered at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the live DOM. Nothing was submitted, bought or signed into; the only presses were local UI toggles (the Search disclosure, the nav flyout, the filter rail). No consent SDK mounts on these routes.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (21 components, 38 states).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) whose value is the same, when there is one. Text is written family size/line-height weight, then its colour, for example `AdihausDIN 15/20 700, #000000`, and is read from the first text node inside the component.
- The first state of each entry lists every value; later states list only what changed. A state identical to the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do; a state that only repaints a child layer is listed as "child paint".
- Crops are images of the component in [components/crops/](components/crops) (38 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`. Desktop viewport shots are 1440 x 900. Phone viewport shots are 390 x 844 at 2x (780 x 1688). `-full` shots tile the inner scroll shell, so they are taller than the viewport. Only light exists. The storefront has no dark theme. Which control opens which page is in [site-tree.md](site-tree.md).

| Surface | URL | Screenshots |
|---|---|---|
| Home. The campaign band, tag strip, product rows and footer. Captured at rest, search open, and full-page. | `/` | [default (light)](screenshots/home-light-default.png), [full (light)](screenshots/home-light-full.png), [search (light)](screenshots/home-light-search.png) |
| A catalogue page (跑步 running, men's). Captured at rest, filter open, and full-page. | `/plp/sp_run_app_male` | [default (light)](screenshots/plp-light-default.png), [filter (light)](screenshots/plp-light-filter.png), [full (light)](screenshots/plp-light-full.png) |
| A product page (articleId JP1477 — pinned so the screenshots and the measurements describe the same product). Captured at rest and full-page. | `/pdp?articleId=JP1477` | [default (light)](screenshots/pdp-light-default.png), [full (light)](screenshots/pdp-light-full.png) |
| The empty bag. | `/cart` | [default (light)](screenshots/cart-light-default.png), [full (light)](screenshots/cart-light-full.png) |
| The public site map: the catalog tree as a page. | `/siteMap` | [default (light)](screenshots/sitemap-light-default.png), [full (light)](screenshots/sitemap-light-full.png) |
| A campaign listing (one /splp tile from home). | `/splp?contentId=SPLP_NGuAJiSc` | [default (light)](screenshots/campaign-light-default.png), [full (light)](screenshots/campaign-light-full.png) |
| A brand content page linked from the home brand tiles. | `/clp?contentId=904` | [default (light)](screenshots/clp-light-default.png), [full (light)](screenshots/clp-light-full.png) |
| The published privacy statement. The registered-address span is painted out. | `/my-account/privacy-statement` | [default (light)](screenshots/privacy-light-default.png), [full (light)](screenshots/privacy-light-full.png) |
| Home at 390, at rest, search open, and full-page. No burger is mounted. | `/` | [default (light)](screenshots/mobile-home-light-default.png), [full (light)](screenshots/mobile-home-light-full.png), [search (light)](screenshots/mobile-home-light-search.png) |
| The catalogue page at 390. | `/plp/sp_run_app_male` | [default (light)](screenshots/mobile-plp-light-default.png), [full (light)](screenshots/mobile-plp-light-full.png) |
| The product page at 390. | `/pdp?articleId=JP1477` | [default (light)](screenshots/mobile-pdp-light-default.png), [full (light)](screenshots/mobile-pdp-light-full.png) |
| The empty bag at 390. | `/cart` | [default (light)](screenshots/mobile-cart-light-default.png), [full (light)](screenshots/mobile-cart-light-full.png) |
| The category tab: the catalog tree, already open. | `/category` | [default (light)](screenshots/mobile-category-light-default.png), [full (light)](screenshots/mobile-category-light-full.png) |
| The account tab. Login wall. The register control was not clicked. | `/my-account` | [default (light)](screenshots/mobile-account-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Search disclosure | home | the search pill | [home-light-search](screenshots/home-light-search.png), [mobile-home-light-search](screenshots/mobile-home-light-search.png) |
| Filter rail | PLP | the filter/sort control | [plp-light-filter](screenshots/plp-light-filter.png), [filter-row](#filter-row) |
| Login drawer | home | 请登录 and the profile icon. Branch stopped. Not screenshotted. | not captured: login wall |
| Catalog mega-menu | home | a category label. Parent stayed hidden in this headless session. | [sitemap](screenshots/sitemap-light-default.png) and [mobile category](screenshots/mobile-category-light-default.png) show the same links |
| Staff password dialog | every desktop load | mounted with no close control. Not clicked. Hidden before shots. | not captured: password change |

## Shared values

Values that apply across entries, tallied from the measurement file.

**Radius.** none — every corner measured on the storefront is 0px — buttons, fields, tiles, drawers and cells are all square.

**Hover.** no change on the element (6), #ffffff `action.primaryText` to #eceff1 `background.inset` (1), a child layer repaints (the entry's child paint row has the detail) (1). The one measured hover effect is painted by a child: the product card's border steps from #eceff1 to black while its fill stays grey. Buttons and links show no hover change on the element itself.

**Focus.** Of 3 elements given a real keyboard focus: focus could not be driven (4), no ring on the element (2), 1px auto #005fcc offset 1px (1). The only ring measured is the browser's own (footer-link takes Chromium's 1px auto #005fcc outline); buttons and nav items paint no focus style at all, and several controls (div nav items, the promo tag) are not keyboard-focusable — 4 focus attempts could not land.

**Motion.** 0.3s ease-in (1). The header bar itself carries `all 0.3s ease-in`; the readable stylesheets' declared transitions are listed in [raw/measurements.md](raw/measurements.md).

**Layout.** The header is a 124px rail (a 40px black utility strip over an 84px nav bar); the campaign band under it runs 540px tall at 1440. Buttons share one 48px height with 16px side padding; the PLP grid runs 338.5px product cards at 454.5px tall; the PDP purchase column is ~400px; the footer is a 360px block. Edges, where they exist, are 1px hairlines in #eceff1, #c8cbcc or black.

**Accent.** None — the storefront is strict monochrome: black text and keylines on white, grey steps (#9a9b9b muted, #c8cbcc disabled/hairline, #eceff1 and #f9f9f9 surfaces). No accent colour was measured on the public surface.

## Components

### Shell and navigation

The 124px two-strip header every page shares: a 40px black utility strip (在线客服 online service, 请登录 sign in), then an 84px nav bar — the adidas mark, the category nav (男装, 男鞋, 女装…), search, help, account, bag — over a #eceff1 hairline, plus the off-white campaign tag strip.

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
| default (same: hover, focus-visible, pressed) | size 261.33 x 32; background #f9f9f9 `background.surface`; text AdihausDIN 13/18 400, #9a9b9b `text.muted` |

#### Wordmark

<a id="logo"></a>`logo`, on home. The adidas wordmark linking home.

<img src="components/crops/logo-default.png" alt="Wordmark, default" height="84"> 

| State | Values |
|---|---|
| default | size 84 x 84; background transparent |

### Home

The home canvas: the 540px full-bleed campaign band (.feed-com-carousel) under the header — photography, a banner headline and a lib-button 立即选购 CTA — then product rows and the footer.

#### Hero

<a id="hero"></a>`hero`, on home. The campaign band under the header: photography, a headline and a 立即选购 CTA.

<img src="components/crops/hero-default.png" alt="Hero, default" height="120"> 

| State | Values |
|---|---|
| default | size 1440 x 540; background transparent; text adineuePRO 20/34 700, #000000 `text.primary` |

Child layers: div 185x34 background #ffffff `action.primaryText`; div 0x0 background #ffffff `action.primaryText`; button 200x48 background #ffffff `action.primaryText`

#### Primary CTA

<a id="hero-cta"></a>`hero-cta`, on home. A lib-button campaign CTA (立即选购 "Shop now").

<img src="components/crops/hero-cta-default.png" alt="Primary CTA, default" height="48"> <img src="components/crops/hero-cta-hover.png" alt="Primary CTA, hover" height="48"> <img src="components/crops/hero-cta-focus-visible.png" alt="Primary CTA, focus-visible" height="48"> <img src="components/crops/hero-cta-pressed.png" alt="Primary CTA, pressed" height="48"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 200 x 48; padding 0px 16px; background #ffffff `action.primaryText`; text AdihausDIN 14/20 700, #000000 `text.primary` |
| hover, pressed | background #eceff1 `background.inset`; child paint button.btn.mt-16: background #ffffff → #eceff1 |

### Footer

The page foot (360px): bold 15/20 column titles (帮助中心…) over 11/16 link columns and the service line.

#### Footer

<a id="footer"></a>`footer`, on home. The page foot: link columns and the published service line service line.

<img src="components/crops/footer-default.png" alt="Footer, default" height="120"> 

| State | Values |
|---|---|
| default | size 1440 x 360; background transparent; text AdihausDIN 15/20 700, #000000 `text.primary` |

Child layers: div 1440x360 background #f9f9f9 `background.surface`; div 108x122 background #ffffff `action.primaryText`; div 8x8 background #ffffff `action.primaryText`

#### Footer link

<a id="footer-link"></a>`footer-link`, on home. A footer link entry.

<img src="components/crops/footer-link-default.png" alt="Footer link, default" height="32"> <img src="components/crops/footer-link-hover.png" alt="Footer link, hover" height="32"> <img src="components/crops/footer-link-focus-visible.png" alt="Footer link, focus-visible" height="32"> <img src="components/crops/footer-link-pressed.png" alt="Footer link, pressed" height="32"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 57.8 x 32; padding 8px 0px; background transparent; text AdihausDIN 11/16 400, #000000 `text.primary` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

### Catalogue page (PLP)

A catalogue page (/plp/sp_run_app_male): grey filter/sort labels, then the product grid — a bordered photo tile, bold 13/18 name and ¥ price per card.

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
| default | size 338.5 x 454.5; background transparent; text AdihausDIN 11/16 400, #000000 `text.primary` |
| hover | child paint div.product-card-whole.fill-bg-light-gray: border T:1px solid #eceff1 / R:1px solid #eceff1 / B:1px solid #eceff1 / L:1px solid #eceff1 → T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |

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

A product page (/pdp?articleId=JP1477): a two-column canvas — gallery left, purchase column right — adineuePRO title and ¥ price, the white disabled add-to-cart bar, size cells and accordion rows.

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

The same storefront at 390: the top bar collapses to a search-field pill — no nav row and no burger menu.

#### Mobile header

<a id="m-header"></a>`m-header`, on home. The top bar at 390 wide: a search-field pill, no nav row.

<img src="components/crops/m-header-default.png" alt="Mobile header, default" height="48"> 

| State | Values |
|---|---|
| default | size 390 x 48; padding 4px 16px; background transparent; text AdihausDIN 13/18 400, #9a9b9b `text.muted` |

Child layers: div 310x32 background #f9f9f9 `background.surface`

#### Burger button

<a id="m-burger"></a>`m-burger`, on home. The menu button on mobile. None is mounted at 390 — the top bar is the search field, so this records a miss rather than an icon glyph.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

## Gaps

- States that submit were never pressed: 加入购物袋 (add to cart) and the checkout controls. Hover, focus and pressed styles come from CDP-forced pseudo-classes and keyboard focus, not real clicks.
- The captured PDP showed add-to-cart in its disabled state (white fill, #c8cbcc text and border); an in-stock enabled bar was not measured.
- The nav flyout did not open on hover in headless (some items open on click); the search disclosure is in the screenshots, its panel is not measured.
- `plp-title`, `product-card-price`, `size-cell`, `accordion` and `m-burger` are recorded misses — the selectors found nothing, so nothing is reported; `size-cell`/`accordion` may not exist on this PDP variant, and no burger menu mounts at 390 (the top bar is the search pill).
- Pages are fixed-height app shells with inner scroll containers, so the `-full` screenshots capture the viewport-height shell, not a tall page — a boundary of the front end, not a truncation.
- The global adidas.com storefront is Akamai-blocked from the capture environment (every regional domain answers HTTP 403), so this package covers adidas.com.cn, a related but different zh-CN front end.
- Hover/focus on the 390 capture is not meaningful (a phone has neither); the mobile entries cover layout.

