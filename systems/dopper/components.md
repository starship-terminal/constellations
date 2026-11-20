# Dopper components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from www.dopper.com and shop.dopper.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running pages. Prices render in EUR. Nothing was signed into, created, submitted or paid for: the login fields were focused and typed into then cleared, never sent, and Add to cart / Sign in / checkout were never pressed for real.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (59 components, 126 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (114 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Marketing home (www.dopper.com) | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Mission story | `/en/mission/story` | [default](screenshots/mission-light-default.png), [full](screenshots/mission-light-full.png) |
| Insulated product page | `/en/products/insulated` | [default](screenshots/product-insulated-light-default.png), [full](screenshots/product-insulated-light-full.png) |
| Blog | `/en/blog/just-refill` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Shop home (shop.dopper.com) | `shop.dopper.com/` | [default](screenshots/shop-light-default.png), [full](screenshots/shop-light-full.png) |
| Bottles PLP | `shop.dopper.com/bottles` | [default](screenshots/category-light-default.png), [full](screenshots/category-light-full.png) |
| Product detail | `shop.dopper.com/dopper-original-pacific-blue` | [default](screenshots/pdp-light-default.png), [full](screenshots/pdp-light-full.png) |
| Cart (empty) | `shop.dopper.com/checkout/cart/` | [default](screenshots/cart-light-default.png), [full](screenshots/cart-light-full.png) |
| Customer login | `shop.dopper.com/customer/account/login/` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Shop home, phone | `shop.dopper.com/` | [default](screenshots/mobile-shop-light-default.png), [full](screenshots/mobile-shop-light-full.png) |
| Bottles PLP, phone | `shop.dopper.com/bottles` | [default](screenshots/mobile-category-light-default.png), [filter](screenshots/mobile-category-light-filter.png), [full](screenshots/mobile-category-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Bottle mega-menu | home | the Bottle nav trigger's own hover/click | [home-light-menu](screenshots/home-light-menu.png), [flyout](#mega-menu), [flyout-tab](#flyout-tab), [flyout-card](#flyout-card) |
| Mobile menu overlay | home, phone width | the burger button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item), [m-menu-pill](#mobile-menu-pill) |
| Collections tab | home | a collection tab's own click (local swap) | [collection-tab](#collection-tab) |
| PLP filter sheet | the Bottles list | open by default on desktop; the + Filters pill's own toggle on mobile | [category-light-default](screenshots/category-light-default.png), [mobile-category-light-filter](screenshots/mobile-category-light-filter.png), [filter-panel](#filter-panel), [filter-radio](#filter-radio), [m-filter-sheet](#filter-sheet-mobile) |
| Cookiebot consent dialog | every page on both hosts | hidden, never answered (Allow all / Allow selection / Deny were never clicked) | hidden before every shot and reading |
| Login fields | customer login | focused and typed into, then cleared — Sign in was never pressed | [login-email](#email-field), [login-password](#password-field) |
| Checkout and account | shop.dopper.com checkout, customer area | behind checkout/sign-in; the empty cart and the login card were measured, never used | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 14 components were given a real keyboard focus. 14 draw an outline ring: `bag-button` (1px auto #005fcc `measured.focus-ring`, offset 1px), `btn-dark` (1px auto #005fcc `measured.focus-ring`, offset 1px), `btn-outline` (1px auto #005fcc `measured.focus-ring`, offset 1px), `collection-tab` (1px auto #005fcc `measured.focus-ring`, offset 0px), `shop-nav-link` (2px solid #000f2e `color.deep_sea.default`, offset 4px), `shop-hero-button` (2px solid #000f2e `color.deep_sea.default`, offset 4px), `filters-button` (2px solid #000f2e `color.deep_sea.default`, offset 4px), `filter-swatch` (on a child: 2px solid rgb(0, 15, 46) offset 4px), `filter-close` (2px solid #000f2e `color.deep_sea.default`, offset 4px), `add-to-cart` (2px solid #000f2e `color.deep_sea.default`, offset 4px), `cart-cta` (2px solid #000f2e `color.deep_sea.default`, offset 4px), `login-button` (2px solid #000f2e `color.deep_sea.default`, offset 4px), `login-link` (2px solid #000f2e `color.deep_sea.default`, offset 4px), `create-button` (2px solid #000f2e `color.deep_sea.default`, offset 4px). Focus could not be captured on 5 more (keyboard focus never landed on them, so their readings are left out): `nav-trigger`, `nav-link`, `m-burger`, `m-nav-item`, `m-menu-pill`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease-in-out` | all | login-checkbox |
| 0.25s | `linear` | background | btn-outline |
| 0.3s | `ease` | color, opacity | m-nav-item, nav-link, nav-trigger |
| 0.3s | `linear` | opacity | newsletter-input |
| 0.4s | `cubic-bezier(0.83, 0, 0.17, 1)` | opacity | collection-tab |
| 0.4s | `ease` | opacity | m-menu-pill |
| 0.7s | `ease` | transform | m-menu-pill, m-nav-item |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Content card](#content-card) | 786 x 596.94 | - | - | transparent | none | 0px 16px 0px 70px |
| [Product card](#product-card) | 340 x 655.52 | - | - | transparent | none | 0px 16px |
| [Login card](#login-card) | 534.09 x 489 | - | 20px | #0067e5 `color.darkBlue.default` | none | 40px 44px 53px 44px |
| [New customers card](#new-customers-card) | 534.09 x 489 | - | 20px | #cce2ff `color.darkBlue.-3` | none | 40px 44px 53px 44px |
| [Filter panel](#filter-panel) | 1360 x 347.56 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The DOPPER-NAVIGATION custom element on both hosts: the dopper. wordmark, the Bottle / Travel Mug / Tap / Mission / Get Involved flyout triggers, right links (Impact report / Find a Store / For Businesses / EN) and the bag button. The Bottle trigger opens a yellow mega-menu; its shadow DOM carries the nav content.

#### Header
The transparent-then-solid top bar (the DOPPER-NAVIGATION custom element): flyout triggers (Bottle / Travel Mug / Tap / Mission / Get Involved), the dopper. wordmark, right links (Impact report / Find a Store / For Businesses / EN) and the bag button. Read as `header` on the home page.

**Values (default).** size 1440 x 110; padding 0px 70px; background transparent; text Gilroy 16/20.8 700, #0c1a37; icon 12 x 8, #0c1a37; layers ul.languagePopup.hidden 0.0x0.0 rgb(252, 250, 242) rgba(0, 0, 0, 0.1) 0px 4px 20px 0px 20px; button.menuToggle 0.0x0.0 rgb(239, 239, 239) 50%.

Child layers that carry the look: ul 0x0 background #fcfaf2 `color.sand.-3` radius 20px shadow rgba(0, 0, 0, 0.1) 0px 4px 20px 0px; button 0x0 background #efefef radius 50%.

![Header default](components/crops/header-default.png)

#### Logo
The dopper. wordmark anchor (svg, centred in the bar). Read as `logo` on the home page.

**Values (default).** size 200 x 47; background transparent; text -apple-system 16/16 400, #0000ee.

![Logo default](components/crops/logo-default.png)

#### Nav trigger
The Bottle flyout trigger in the header; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 64.16 x 20.8; background transparent; text Gilroy 16/20.8 700, #000f2e `color.deep_sea.default`; transition color 0.3s ease; icon 12 x 8, #000f2e `color.deep_sea.default` |
| hover | text Gilroy 16/20.8 700, #0067e5 `color.darkBlue.default`; icon 12.9 x 9.43, #0067e5 `color.darkBlue.default` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png)

#### Nav link
A right-side header link (Impact report). Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101.91 x 20.8; background transparent; text Gilroy 16/20.8 500, #000f2e `color.deep_sea.default`; transition color 0.3s ease |
| hover | text Gilroy 16/20.8 500, #0067e5 `color.darkBlue.default` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`; the via was later rewritten by hand, not re-measured), so its focus look is uncaptured — not measured as absent.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png)

#### Bag button
The shopping-bag icon button, right end of the header (light-blue circle); links to the cart, never followed. Read as `bag-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 60 x 62; background transparent; text -apple-system 16/16 400, #000000 `color.neutral.ink` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring`, offset 1px; layers a 60.0x62.0 1px auto rgb(0, 95, 204) offset 1px |

![Bag button default](components/crops/bag-button-default.png) ![Bag button hover](components/crops/bag-button-hover.png) ![Bag button focus-visible](components/crops/bag-button-focus-visible.png) ![Bag button pressed](components/crops/bag-button-pressed.png)

#### Mega-menu
The yellow Bottle flyout (tab pills across the top, feature columns, CTAs and a product photo). Read as `flyout` on the home page.

**Note:** Misidentified: the stored states are the static 'Explore our solutions' section (the tabsVariation cards carry the same copy as the menu). The opened Bottle mega-menu was screenshotted (screenshots/home-light-menu.png) but not measured; the selector is now scoped to the opened panel and a re-measure is queued.

Not on the page when it was captured.

#### Flyout tab
A pill tab across the top of the opened menu (Bottle active on yellow). Read as `flyout-tab` on the home page.

**Note:** Misidentified: the stored states are the static 'Explore our solutions' section (the tabsVariation cards carry the same copy as the menu). The opened Bottle mega-menu was screenshotted (screenshots/home-light-menu.png) but not measured; the selector is now scoped to the opened panel and a re-measure is queued.

Not on the page when it was captured.

#### Flyout card
An option card inside the flyout carousel ("Bottle — A range of reusable bottles…"). Read as `flyout-card` on the home page.

**Note:** Misidentified: the stored states are the static 'Explore our solutions' section (the tabsVariation cards carry the same copy as the menu). The opened Bottle mega-menu was screenshotted (screenshots/home-light-menu.png) but not measured; the selector is now scoped to the opened panel and a re-measure is queued.

Not on the page when it was captured.

### Home (www)

The video hero with the "Whatever the season" display and Watch now / Shop our collection pills, the yellow Bottle flyout, the collections tab showcase, the impact calculator, content cards and the newsletter band.

#### Hero display
The h1 over the full-bleed video hero ("Whatever the season") — Dopper display type on media. Read as `hero-display` on the home page.

**Values (default).** size 425.36 x 144; background transparent; text Dopper 72/72 400, #f6ecc8 `color.sand.default`.

![Hero display default](components/crops/hero-display-default.png)

#### Button, dark
The deep-sea filled pill CTA ("Watch now") on the video hero. Read as `btn-dark` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 173.73 x 51.39; background transparent; text Gilroy 18/23.4 600, #f6ecc8 `color.sand.default`; layers div.burstButton_fakeButton__B8btS 165.0x38.5 rgb(0, 15, 46) 20px; div.link_link__JtDHX.link_background__vwwg3 173.7x51.4 rgb(0, 15, 46) 20px |
| hover | layers div.burstButton_fakeButton__B8btS 165.0x38.5 rgb(0, 15, 46) 20px; div.burstButton_bubble__N2Lo3 24.2x24.2 rgb(0, 15, 46) 9999px; div.burstButton_bubble__N2Lo3 13.1x13.1 rgb(0, 15, 46) 9999px; div.burstButton_bubble__N2Lo3 20.4x20.4 rgb(0, 15, 46) 9999px; div.burstButton_bubble__N2Lo3 21.6x21.6 rgb(0, 15, 46) 9999px; div.burstButton_bubble__N2Lo3 13.0x13.0 rgb(0, 15, 46) 9999px |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring`, offset 1px; layers a.burstButton_wrapper__JRFOg 173.7x51.4 1px auto rgb(0, 95, 204) offset 1px; div.burstButton_fakeButton__B8btS 165.0x38.5 rgb(0, 15, 46) 20px; div.link_link__JtDHX.link_background__vwwg3 173.7x51.4 rgb(0, 15, 46) 20px |

Child layers that carry the look: div 165x38.5 background #000f2e `color.deep_sea.default` radius 20px; div 173.7x51.4 background #000f2e `color.deep_sea.default` radius 20px.

![Button, dark default](components/crops/btn-dark-default.png) ![Button, dark hover](components/crops/btn-dark-hover.png) ![Button, dark focus-visible](components/crops/btn-dark-focus-visible.png) ![Button, dark pressed](components/crops/btn-dark-pressed.png)

#### Button, outline
The outline pill CTA ("Shop our collection") on the video hero. Read as `btn-outline` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 244.63 x 51.39; padding 12px 40px; border 2px solid #f6ecc8 `color.sand.default`; radius 20px; background transparent; text Gilroy 18/23.4 600, #f6ecc8 `color.sand.default`; transition background 0.25s linear |
| hover | background #f6ecc8 `color.sand.default`; text Gilroy 18/23.4 600, #0067e5 `color.darkBlue.default` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring`, offset 1px |
| pressed | background #f6ecc8 `color.sand.default`; text Gilroy 18/23.4 600, #0067e5 `color.darkBlue.default` |

![Button, outline default](components/crops/btn-outline-default.png) ![Button, outline hover](components/crops/btn-outline-hover.png) ![Button, outline focus-visible](components/crops/btn-outline-focus-visible.png) ![Button, outline pressed](components/crops/btn-outline-pressed.png)

#### Collection tab
A product tab inside "The collections" showcase; toggled to swap the card below. Read as `collection-tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 250 x 445; radius 20px; background transparent; text Gilroy 27/32.4 400, #000f2e `color.deep_sea.default`; transition opacity 0.4s cubic-bezier(0.83, 0, 0.17, 1); transform translate(20px, 0px); opacity 0; layers article.tabsVariation_card__lZivw 267.5x476.2 rgb(138, 177, 230) 20px |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring`, offset 0px; layers button.keen-slider__slide.tabsVariation_cardItem__G2SQa 250.0x445.0 1px auto rgb(0, 95, 204) offset 0px 20px; article.tabsVariation_card__lZivw 267.5x476.2 rgb(138, 177, 230) 20px |

Child layers that carry the look: article 267.5x476.2 background #8ab1e6 `color.darkBlue.-2` radius 20px.

![Collection tab default](components/crops/collection-tab-default.png) ![Collection tab hover](components/crops/collection-tab-hover.png) ![Collection tab focus-visible](components/crops/collection-tab-focus-visible.png) ![Collection tab pressed](components/crops/collection-tab-pressed.png)

#### Section heading
A section heading ("The collections") — Gilroy bold, deep-sea. Read as `collections-heading` on the home page.

**Values (default).** size 1324 x 58; background transparent; text Dopper 58/58 400, #000000 `color.neutral.ink`.

![Section heading default](components/crops/collections-heading-default.png)

#### Content card
A home split card (copy + CTA beside a photo tile). Read as `content-card` on the home page.

**Values (default).** size 786 x 596.94; padding 0px 16px 0px 70px; background transparent; text Gilroy 43/47.3 600, #000f2e `color.deep_sea.default`; layers span.RangeSlider_track__Ma03Q 700.0x16.0 rgb(204, 226, 255) 9999px; span.RangeSlider_progress__KeNcI 20.0x16.0 20px; span.RangeSlider_thumb__cji3q 40.0x40.0 rgb(0, 103, 229) rgba(0, 103, 229, 0.2) 0px 2px 8px 0px 50%; span::before.RangeSlider_thumb__cji3q 8pxx8px rgb(0, 15, 46) T:4px solid rgb(252, 250, 242) / R:4px solid rgb(252, 250, 242) / B:4px solid rgb(252, 250, 242) / L:4px solid rgb(252, 2.

Child layers that carry the look: span 700x16 background #cce2ff `color.darkBlue.-3` radius 9999px; span 20x16 image linear-gradient(90deg, #0067e5 `color.darkBlue.default` 0px, #4183d9 `color.darkBlue.-1` 1 radius 20px; span 40x40 background #0067e5 `color.darkBlue.default` radius 50% shadow rgba(0, 103, 229, 0.2) 0px 2px 8px 0px.

![Content card default](components/crops/content-card-default.png)

### Shop

The Magento storefront (shop.dopper.com): the same header plus the catalog nav row (All products / Mugs / Bottles / …) and hero tiles with darkBlue CTAs.

#### Shop header
The same dopper header on the Magento storefront, plus the catalog nav row below it. Read as `shop-header` on the shop home page.

**Values (default).** size 1440 x 110; background #fcfaf2 `color.sand.-3`; text Gilroy 20/26 400, #000f2e `color.deep_sea.default`.

![Shop header default](components/crops/shop-header-default.png)

#### Shop nav
The catalog nav row (All products / Mugs / Bottles / Accessories / Spare parts / E-Gift Card / Last chance). Read as `shop-nav` on the shop home page.

**Values (default).** size 1360 x 27; background transparent; text Gilroy 20/25 600, #0067e5 `color.darkBlue.default`; layers ul.level0.submenu 0.0x0.0 rgb(252, 250, 242) T:1px solid rgb(204, 204, 204) / R:1px solid rgb(204, 204, 204) / B:1px solid rgb(204, 204, 204) / L:1px solid rgb(204, 204, 204) rgba(0, 0, 0, 0.19) 0px 5px 5px 0px; ul.level0.submenu 0.0x0.0 rgb(252, 250, 242) T:1px solid rgb(204, 204, 204) / R:1px solid rgb(204, 204, 204) / B:1px solid rgb(204, 204, 204) / L:1px solid rgb(204, 204, 204) rgba(0, 0, 0,.

Child layers that carry the look: ul 0x0 background #fcfaf2 `color.sand.-3` border 1px solid #cccccc shadow rgba(0, 0, 0, 0.19) 0px 5px 5px 0px; ul 0x0 background #fcfaf2 `color.sand.-3` border 1px solid #cccccc shadow rgba(0, 0, 0, 0.19) 0px 5px 5px 0px; ul 0x0 background #fcfaf2 `color.sand.-3` border 1px solid #cccccc shadow rgba(0, 0, 0, 0.19) 0px 5px 5px 0px.

![Shop nav default](components/crops/shop-nav-default.png)

#### Shop nav link
A catalog nav item; "All products" paints the active darkBlue. Read as `shop-nav-link` on the shop home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 109.56 x 25; background transparent; text Gilroy 20/25 600, #0067e5 `color.darkBlue.default` |
| focus-visible | radius 20px; outline 2px solid #000f2e `color.deep_sea.default`, offset 4px; layers a.level-top 109.6x25.0 2px solid rgb(0, 15, 46) offset 4px 20px |

![Shop nav link default](components/crops/shop-nav-link-default.png) ![Shop nav link hover](components/crops/shop-nav-link-hover.png) ![Shop nav link focus-visible](components/crops/shop-nav-link-focus-visible.png) ![Shop nav link pressed](components/crops/shop-nav-link-pressed.png)

#### Shop CTA
The darkBlue pill CTA on a shop hero tile ("Shop now"). Read as `shop-hero-button` on the shop home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 172.98 x 54; padding 13px 40px; border 1px solid transparent; radius 20px; background transparent; text Gilroy 20/26 600, #f6ecc8 `color.sand.default`; layers ::before rgb(0, 103, 229) 0px none 1 |
| focus-visible | outline 2px solid #000f2e `color.deep_sea.default`, offset 4px |
| pressed | shadow rgba(204, 204, 204, 0.8) 0px 1px 0px 0px inset, rgba(204, 204, 204, 0.3) 0px -1px 0px 0px inset |

![Shop CTA default](components/crops/shop-hero-button-default.png) ![Shop CTA hover](components/crops/shop-hero-button-hover.png) ![Shop CTA focus-visible](components/crops/shop-hero-button-focus-visible.png) ![Shop CTA pressed](components/crops/shop-hero-button-pressed.png)

### Product list (PLP)

The /bottles list: centred display title, the teal + Filters pill, the light-blue filter sheet (open on desktop), product cards with badge chips and EUR prices.

#### PLP title
"Bottles" — Dopper display type, deep-sea, centred over the sand field. Read as `plp-h1` on the category (PLP) page.

**Values (default).** size 259.36 x 80; background transparent; text Dopper 72/72 400, #000f2e `color.deep_sea.default`.

![PLP title default](components/crops/plp-h1-default.png)

#### PLP subtitle
The one-line lede under the title ("End packaged water. Just refill your Dopper bottle."). Read as `plp-sub` on the category (PLP) page.

**Values (default).** size 1440 x 24; padding 0px 40px; background transparent; text Dopper 20/24 400, #000f2e `color.deep_sea.default`.

![PLP subtitle default](components/crops/plp-sub-default.png)

#### Filters button
The teal "+ Filters" pill that opens the filter sheet (open by default on desktop). Read as `filters-button` on the category (PLP) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 156.23 x 52; padding 12px 40px 12px 60px; radius 20px; background transparent; text Gilroy 20/26 700, #ffffff; layers ::before rgb(10, 190, 170) 0px none 1; button::before.action.cta 156.234pxx54px rgb(10, 190, 170) 20px |
| focus-visible | outline 2px solid #000f2e `color.deep_sea.default`, offset 4px; layers ::before rgb(10, 190, 170) 0px none 1; button.action.cta 156.2x52.0 2px solid rgb(0, 15, 46) offset 4px 20px; button::before.action.cta 156.234pxx54px rgb(10, 190, 170) 20px |
| pressed | shadow rgba(204, 204, 204, 0.8) 0px 1px 0px 0px inset, rgba(204, 204, 204, 0.3) 0px -1px 0px 0px inset; layers ::before rgb(10, 190, 170) 0px none 1; button.action.cta 156.2x52.0 rgba(204, 204, 204, 0.8) 0px 1px 0px 0px inset, rgba(204, 204, 204, 0.3) 0px -1px 0px 0px inset 20px; button::before.action.cta 156.234pxx54px rgb(10, 190, 170) 20px |

Child layers that carry the look: button::before 156.234pxx54px background #0abeaa `color.carribean.default` radius 20px.

![Filters button default](components/crops/filters-button-default.png) ![Filters button hover](components/crops/filters-button-hover.png) ![Filters button focus-visible](components/crops/filters-button-focus-visible.png) ![Filters button pressed](components/crops/filters-button-pressed.png)

#### Filter panel
The light-blue (darkBlue-3) filter sheet: Collection/Size radio groups, Colour swatches, Bundle checkbox. Read as `filter-panel` on the category (PLP) page.

**Values (default).** size 1360 x 347.56; background transparent; text Gilroy 24/28.56 700, #000f2e `color.deep_sea.default`; layers div.swatch-option.color 24.0x24.0 rgb(240, 240, 240) 100%; div.swatch-option.color 24.0x24.0 rgb(148, 148, 148) 100%; div.swatch-option.color 24.0x24.0 rgb(0, 0, 0) 100%; div.swatch-option.color 24.0x24.0 rgb(53, 98, 161) 100%; div.swatch-option.color 24.0x24.0 rgb(98, 148, 49) 100%; div.swatch-option.color 24.0x24.0 rgb(243, 213, 78) 100%.

Child layers that carry the look: div 24x24 background #f0f0f0 image linear-gradient(to left, rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 50%, rgba(0, 0, 0, 0.1)  radius 100%; div 24x24 background #949494 image linear-gradient(to left, rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 50%, rgba(0, 0, 0, 0.1)  radius 100%; div 24x24 background #000000 `color.neutral.ink` image linear-gradient(to left, rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 50%, rgba(0, 0, 0, 0.1)  radius 100%.

![Filter panel default](components/crops/filter-panel-default.png)

#### Filter radio
A Collection/Size option row: ring + name + muted item count. Read as `filter-radio` on the category (PLP) page.

**Values (default).** size 184.14 x 26; padding 0px 0px 0px 30px; background transparent; text Gilroy 20/26 700, #000f2e `color.deep_sea.default`.

![Filter radio default](components/crops/filter-radio-default.png)

#### Colour swatch
A colour-dot swatch filter option. Read as `filter-swatch` on the category (PLP) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 155 x 129; background transparent; text Gilroy 20/26 400, #000f2e `color.deep_sea.default`; layers div.swatch-option.color 24.0x24.0 rgb(240, 240, 240) 100%; div.swatch-option.color 24.0x24.0 rgb(148, 148, 148) 100%; div.swatch-option.color 24.0x24.0 rgb(0, 0, 0) 100%; div.swatch-option.color 24.0x24.0 rgb(53, 98, 161) 100%; div.swatch-option.color 24.0x24.0 rgb(98, 148, 49) 100%; div.swatch-option.color 24.0x24.0 rgb(243, 213, 78) 100% |
| focus-visible | layers div.swatch-option.color 24.0x24.0 rgb(240, 240, 240) 2px solid rgb(0, 15, 46) offset 4px 100%; div.swatch-option.color 24.0x24.0 rgb(148, 148, 148) 100%; div.swatch-option.color 24.0x24.0 rgb(0, 0, 0) 100%; div.swatch-option.color 24.0x24.0 rgb(53, 98, 161) 100%; div.swatch-option.color 24.0x24.0 rgb(98, 148, 49) 100%; div.swatch-option.color 24.0x24.0 rgb(243, 213, 78) 100% |

Child layers that carry the look: div 24x24 background #f0f0f0 image linear-gradient(to left, rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 50%, rgba(0, 0, 0, 0.1)  radius 100%; div 24x24 background #949494 image linear-gradient(to left, rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 50%, rgba(0, 0, 0, 0.1)  radius 100%; div 24x24 background #000000 `color.neutral.ink` image linear-gradient(to left, rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 50%, rgba(0, 0, 0, 0.1)  radius 100%.

![Colour swatch default](components/crops/filter-swatch-default.png) ![Colour swatch hover](components/crops/filter-swatch-hover.png) ![Colour swatch focus-visible](components/crops/filter-swatch-focus-visible.png) ![Colour swatch pressed](components/crops/filter-swatch-pressed.png)

#### Filter checkbox
The Bundle option: box checkbox + "Flip Straw Bundle" + count. Read as `filter-checkbox` on the category (PLP) page.

**Values (default).** size 291.38 x 28.56; background transparent; text Gilroy 24/28.56 700, #000f2e `color.deep_sea.default`.

![Filter checkbox default](components/crops/filter-checkbox-default.png)

#### Filter close
The deep-sea circle × button closing the filter sheet. Read as `filter-close` on the category (PLP) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 54 x 54; radius 20px; background transparent; text Gilroy 20/26 700, #0067e5 `color.darkBlue.default`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 2px solid #000f2e `color.deep_sea.default`, offset 4px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.filter-close 54.0x54.0 2px solid rgb(0, 15, 46) offset 4px 20px |

![Filter close default](components/crops/filter-close-default.png) ![Filter close hover](components/crops/filter-close-hover.png) ![Filter close focus-visible](components/crops/filter-close-focus-visible.png) ![Filter close pressed](components/crops/filter-close-pressed.png)

#### Product card
A PLP card: product photo, optional badge chip, name, price in EUR. Read as `product-card` on the category (PLP) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 340 x 655.52; padding 0px 16px; background transparent; text Gilroy 20/26 400, #999cba `color.deep_sea.-2`; layers div.drop.drop-hover 0.0x0.0 rgb(167, 191, 183) 63% 37% 54% 46% / 55% 48% 52% 45%; div.product-item-inner 308.0x40.0 rgb(255, 255, 255); div.product.actions 308.0x40.0 rgb(253, 250, 243); button.action.tocart 105.6x40.0 rgb(4, 92, 220) 10px; a.action.personalize 139.0x40.0 T:2px solid rgb(1, 17, 40) / R:2px solid rgb(1, 17, 40) / B:2px solid rgb(1, 17, 40) / L:2px solid rgb(1, 17, 40) 10px |
| hover | text Gilroy 20/26 400, #000f2e `color.deep_sea.default`; layers div.drop.drop-hover 246.4x246.4 rgb(167, 191, 183) 62.8153% 37.1847% 54% 46% / 54.9518% 48.0964% 51.9036% 45.0482%; div.product-item-inner 308.0x40.0 rgb(255, 255, 255); div.product.actions 308.0x40.0 rgb(253, 250, 243); button.action.tocart 105.6x40.0 rgb(4, 92, 220) 10px; a.action.personalize 139.0x40.0 T:2px solid rgb(1, 17, 40) / R:2px solid rgb(1, 17, 40) / B:2px solid rgb(1, 17, 40) / L:2px  |

Child layers that carry the look: div 0x0 background #a7bfb7 radius 63% 37% 54% 46% / 55% 48% 52% 45%; div 308x40 background #ffffff; div 308x40 background #fdfaf3.

![Product card default](components/crops/product-card-default.png) ![Product card hover](components/crops/product-card-hover.png)

#### Price
The EUR price on a product card. Read as `product-price` on the category (PLP) page.

**Values (default).** size 308 x 24; background transparent; text Gilroy 16/24 600, #999cba `color.deep_sea.-2`.

![Price default](components/crops/product-price-default.png)

#### Badge chip
The outlined "New" chip on a product card. Read as `product-badge` on the category (PLP) page.

Not on the page when it was captured.

### Product page (PDP)

The /dopper-original-pacific-blue detail: breadcrumb, gallery, price, the colour/collection/pattern configurator rows, the darkBlue Add to cart and the icon feature list.

#### Breadcrumb
Home > Original - Pacific Blue trail above the gallery. Read as `breadcrumb` on the product page page.

**Values (default).** size 1394 x 26; padding 0px 40px; background transparent; text Gilroy 16/26 400, #000f2e `color.deep_sea.default`; transform translate(-697px, 0px).

![Breadcrumb default](components/crops/breadcrumb-default.png)

#### PDP title
The product name ("Original - Pacific Blue"). Read as `pdp-title` on the product page page.

**Values (default).** size 415 x 83; background transparent; text Dopper 30/46 400, #000f2e `color.deep_sea.default`.

![PDP title default](components/crops/pdp-title-default.png)

#### PDP price
€14.95 under the title. Read as `pdp-price` on the product page page.

**Values (default).** size 44.69 x 16; background transparent; text Gilroy 16/16 600, #000f2e `color.deep_sea.default`.

![PDP price default](components/crops/pdp-price-default.png)

#### Add to cart
The darkBlue pill buy button; measured, never pressed for real (pressed state is CDP-forced). Read as `add-to-cart` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 203.34 x 54; padding 13px 25px; border 1px solid #0067e5 `color.darkBlue.default`; radius 20px; background #0067e5 `color.darkBlue.default`; text Gilroy 20/26 600, #f9f3df `color.sand.-2` |
| focus-visible | shadow #fcfaf2 0px 0px 0px 4px; outline 2px solid #000f2e `color.deep_sea.default`, offset 4px |

![Add to cart default](components/crops/add-to-cart-default.png) ![Add to cart hover](components/crops/add-to-cart-hover.png) ![Add to cart focus-visible](components/crops/add-to-cart-focus-visible.png) ![Add to cart pressed](components/crops/add-to-cart-pressed.png)

#### Configurator row
A collapsed configurator row in the buy box; the "opened" state presses its own toggle (a local expand). Read as `pdp-option` on the product page page.

**Values (default).** size 106.83 x 25; background transparent; text Gilroy 20/25 600, #000f2e `color.deep_sea.default`.

![Configurator row default](components/crops/pdp-option-default.png)

#### PDP swatch
A colour dot in "Choose your colour" (the selected ring vs the rest). Read as `pdp-swatch` on the product page page.

Not on the page when it was captured.

#### Feature line
An icon + claim row in the buy box (Lightweight and extremely tough). Read as `pdp-feature` on the product page page.

**Values (default).** size 415 x 26; background transparent; text Gilroy 20/26 400, #000f2e `color.deep_sea.default`.

![Feature line default](components/crops/pdp-feature-default.png)

### Cart

The /checkout/cart empty state: "Your cart" display, the darkBlue-3 continue-shopping strip, the basket illustration and Back to shop CTA. A filled cart was not exercised.

#### Cart title
"Your cart" — darkBlue Dopper display on sand. Read as `cart-title` on the cart page.

**Values (default).** size 1440 x 80; background transparent; text Dopper 80/80 400, #0067e5 `color.darkBlue.default`.

![Cart title default](components/crops/cart-title-default.png)

#### Empty cart
The empty-basket block: "Be my hero" illustration, copy and a Back to shop CTA. A filled cart was not exercised (nothing is added). Read as `cart-empty` on the cart page.

**Known wrong; recapture needed.** The reading is the 1440 x 80 "Your cart" h1, not the empty-basket block; the 2026-11-13 run did not find the block and kept these states (recaptureMissed).

**Values (default).** size 1440 x 80; background transparent; text Dopper 80/80 400, #0067e5 `color.darkBlue.default`.

![Empty cart default](components/crops/cart-empty-default.png)

#### Cart CTA
The darkBlue pill "Back to shop" in the empty state. Read as `cart-cta` on the cart page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 202.17 x 54; padding 13px 40px; border 1px solid #0067e5 `color.darkBlue.default`; radius 20px; background #0067e5 `color.darkBlue.default`; text Gilroy 20/26 600, #f9f3df `color.sand.-2` |
| focus-visible | outline 2px solid #000f2e `color.deep_sea.default`, offset 4px |

![Cart CTA default](components/crops/cart-cta-default.png) ![Cart CTA hover](components/crops/cart-cta-hover.png) ![Cart CTA focus-visible](components/crops/cart-cta-focus-visible.png) ![Cart CTA pressed](components/crops/cart-cta-pressed.png)

#### Cart strip
The darkBlue-3 band under the header: ← Continue shopping left, Customer Service right. Read as `cart-strip` on the cart page.

**Values (default).** size 1440 x 93; background #cce2ff `color.darkBlue.-3`; text Gilroy 16/20 400, #000f2e `color.deep_sea.default`.

![Cart strip default](components/crops/cart-strip-default.png)

### Login and signup

The Magento /customer/account/login surface: the darkBlue "Registered Customers" card (Email + Password fields, Sign in, Show password, Remember Me, Forgot link) beside the light-blue "New Customers" card with Create an Account. Fields were focused and typed into, then cleared — nothing sent; Sign in was never pressed.

#### Login card
The darkBlue "Registered Customers" card: Email + Password fields, Sign in, Show password, Remember Me, Forgot link. Read as `login-card` on the login page.

**Values (default).** size 534.09 x 489; padding 40px 44px 53px 44px; radius 20px; background #0067e5 `color.darkBlue.default`; text Gilroy 40/42 500, #fcfaf2 `color.sand.-3`.

![Login card default](components/crops/login-card-default.png)

#### Email field
The white rounded Email field on the blue card; focused and typed into, then cleared — nothing sent. Read as `login-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 357 x 54; padding 0px 20px; border 2px solid #fcfaf2 `color.sand.-3`; radius 20px; background #fcfaf2 `color.sand.-3`; text Gilroy 20/28.57 400, #000f2e `color.deep_sea.default`; placeholder #000f2e `color.deep_sea.default` |
| focused, filled | border 2px solid #000f2e `color.deep_sea.default`; outline 2px solid #000f2e `color.deep_sea.default`, offset 4px |

![Email field default](components/crops/login-email-default.png) ![Email field focused](components/crops/login-email-focused.png) ![Email field filled](components/crops/login-email-filled.png)

#### Password field
The Password field beside the Sign in button. Read as `login-password` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 197.61 x 54; padding 0px 20px; border 2px solid #fcfaf2 `color.sand.-3`; radius 20px; background #fcfaf2 `color.sand.-3`; text Gilroy 20/28.57 400, #000f2e `color.deep_sea.default`; placeholder #000f2e `color.deep_sea.default` |
| focused | border 2px solid #000f2e `color.deep_sea.default`; outline 2px solid #000f2e `color.deep_sea.default`, offset 4px |

![Password field default](components/crops/login-password-default.png) ![Password field focused](components/crops/login-password-focused.png)

#### Sign in button
The deep-sea pill Sign in inside the blue card; never pressed (pressed state is CDP-forced). Read as `login-button` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 143.39 x 56; padding 14px 40px; border 1px solid transparent; radius 20px; background transparent; text Gilroy 20/26 600, #f6ecc8 `color.sand.default`; layers ::before rgb(0, 15, 46) 1px none 1 |
| focus-visible | outline 2px solid #000f2e `color.deep_sea.default`, offset 4px |
| pressed | shadow rgba(204, 204, 204, 0.8) 0px 1px 0px 0px inset, rgba(204, 204, 204, 0.3) 0px -1px 0px 0px inset |

![Sign in button default](components/crops/login-button-default.png) ![Sign in button hover](components/crops/login-button-hover.png) ![Sign in button focus-visible](components/crops/login-button-focus-visible.png) ![Sign in button pressed](components/crops/login-button-pressed.png)

#### Field label
The small sand label above a field on the blue card. Read as `login-label` on the login page.

**Values (default).** size 56.94 x 26; background transparent; text Gilroy 20/26 400, #fcfaf2 `color.sand.-3`; layers ::after rgba(0, 0, 0, 0) 0px none 1.

![Field label default](components/crops/login-label-default.png)

#### Checkbox row
The Remember Me / Show password checkbox rows under the password field. Read as `login-checkbox` on the login page.

**Values (default).** size 197.61 x 27; padding 0px 0px 0px 30px; background transparent; text Gilroy 20/26 600, #fcfaf2 `color.sand.-3`; transition all 0.2s ease-in-out; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Checkbox row default](components/crops/login-checkbox-default.png)

#### Form link
"Forgot Your Password?" — sand text link on the blue card. Read as `login-link` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 187.03 x 24.13; background transparent; text Gilroy 18/24.12 400, #f6ecc8 `color.sand.default` |
| focus-visible | radius 20px; outline 2px solid #000f2e `color.deep_sea.default`, offset 4px; layers a.action.remind 187.0x24.1 2px solid rgb(0, 15, 46) offset 4px 20px |

![Form link default](components/crops/login-link-default.png) ![Form link hover](components/crops/login-link-hover.png) ![Form link focus-visible](components/crops/login-link-focus-visible.png) ![Form link pressed](components/crops/login-link-pressed.png)

#### New customers card
The darkBlue-3 "New Customers" card with benefits copy and a Create an Account CTA. Read as `new-card` on the login page.

**Values (default).** size 534.09 x 489; padding 40px 44px 53px 44px; radius 20px; background #cce2ff `color.darkBlue.-3`; text Gilroy 40/42 500, #000f2e `color.deep_sea.default`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![New customers card default](components/crops/new-card-default.png)

#### Create account
The darkBlue pill in the New Customers card; a link, never followed. Read as `create-button` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 256.53 x 56; padding 14px 40px; border 1px solid transparent; radius 20px; background transparent; text Gilroy 20/26 600, #f6ecc8 `color.sand.default`; layers ::before rgb(0, 103, 229) 1px none 1 |
| focus-visible | outline 2px solid #000f2e `color.deep_sea.default`, offset 4px |

![Create account default](components/crops/create-button-default.png) ![Create account hover](components/crops/create-button-hover.png) ![Create account focus-visible](components/crops/create-button-focus-visible.png) ![Create account pressed](components/crops/create-button-pressed.png)

### Footer

The sand footer: newsletter band (name + email fields), "Just refill" columns, social icons, certification and payment logos.

#### Footer
The sand footer: newsletter band, "Just refill" columns, social icons, certification and payment logos. Read as `footer` on the home page.

**Values (default).** size 1440 x 736.63; background transparent; text Gilroy 22/26.18 600, #000000 `color.neutral.ink`; icon 60 x 60, #000000 `color.neutral.ink`; layers div.main-section 1440.0x630.6 rgb(246, 236, 200); a.link.social 0.0x0.0 rgb(249, 243, 223) 42px; a.link.social 0.0x0.0 rgb(249, 243, 223) 42px; a.link.social 0.0x0.0 rgb(249, 243, 223) 42px; a.link.social 0.0x0.0 rgb(249, 243, 223) 42px; input 245.0x54.0 rgb(252, 250, 242) 20px.

Child layers that carry the look: div 1440x630.6 background #f6ecc8 `color.sand.default`; a 0x0 background #f9f3df `color.sand.-2` radius 42px; a 0x0 background #f9f3df `color.sand.-2` radius 42px.

![Footer default](components/crops/footer-default.png)

#### Newsletter input
The email field in the footer newsletter band; focused, never submitted. Read as `newsletter-input` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 54; padding 12px 20px; radius 20px; background #fcfaf2 `color.sand.-3`; text Gilroy 18/23.4 400, #000f2e `color.deep_sea.default`; transition opacity 0.3s linear; placeholder #757575 |
| focused | outline 1px auto #005fcc `measured.focus-ring`, offset 0px |

![Newsletter input default](components/crops/newsletter-input-default.png) ![Newsletter input focused](components/crops/newsletter-input-focused.png)

### Mobile (390 wide)

The same surfaces at phone width: the header shrinks to wordmark + sand burger, the menu opens as a darkBlue full-screen panel, and the PLP filters open as a full sheet.

#### Mobile header
The 390 bar: dopper. wordmark left-centre and the sand burger circle. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 125; background transparent; text -apple-system 16/16 400, #000000 `color.neutral.ink`; layers ul.languagePopup.hidden 0.0x0.0 rgb(252, 250, 242) rgba(0, 0, 0, 0.1) 0px 4px 20px 0px 20px.

Child layers that carry the look: ul 0x0 background #fcfaf2 `color.sand.-3` radius 20px shadow rgba(0, 0, 0, 0.1) 0px 4px 20px 0px.

![Mobile header default](components/crops/m-header-default.png)

#### Burger button
The sand-circle hamburger opening the full-screen menu. Read as `m-burger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 45 x 45; padding 15px; background transparent; text Arial 13.33/normal 400, #000000 `color.neutral.ink`; icon 51 x 51, #000000 `color.neutral.ink` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`; the via was later rewritten by hand, not re-measured), so its focus look is uncaptured — not measured as absent.

![Burger button default](components/crops/m-burger-default.png) ![Burger button hover](components/crops/m-burger-hover.png)

#### Mobile display
The hero h1 at 390. Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 390 x 105.59; background transparent; text Dopper 44/52.8 400, #f6ecc8 `color.sand.default`.

![Mobile display default](components/crops/m-hero-default.png)

#### Mobile menu, open
The darkBlue full-screen menu: large white rows, outline pills, bag and × controls. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; padding 0px 20px 20px 20px; background transparent; text Gilroy 34/37.4 700, #fcfaf2 `color.sand.-3`; icon 12 x 8, #fcfaf2 `color.sand.-3`; layers div.dialog__background 390.0x844.0 rgb(0, 103, 229) 0px 0px 0% 0%; span.underline 0.0x0.0; span.underline 0.0x0.0; span.underline 0.0x0.0; span.underline 0.0x0.0; span.underline 0.0x0.0.

Child layers that carry the look: div 390x844 background #0067e5 `color.darkBlue.default` radius 0px 0px 0% 0%; span 0x0 image linear-gradient(transparent calc(100% - 1px), #fcfaf2 `color.sand.-3` 1px); span 0x0 image linear-gradient(transparent calc(100% - 1px), #fcfaf2 `color.sand.-3` 1px).

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
A large row inside the opened menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 120.81 x 37.41; background transparent; text Gilroy 34/37.4 700, #fcfaf2 `color.sand.-3`; transition opacity 0.3s ease, transform 0.7s ease; icon 12 x 8, #fcfaf2 `color.sand.-3` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png)

#### Mobile menu pill
An outline pill inside the menu (Impact report / Find a Store). Read as `m-menu-pill` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 194.64 x 54; padding 14px 31px; border 2px solid #f6ecc8 `color.sand.default`; radius 20px; background transparent; text Gilroy 20/22 700, #f6ecc8 `color.sand.default`; transition opacity 0.4s ease, transform 0.7s ease |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`; the via was later rewritten by hand, not re-measured), so its focus look is uncaptured — not measured as absent.

![Mobile menu pill default](components/crops/m-menu-pill-default.png) ![Mobile menu pill hover](components/crops/m-menu-pill-hover.png)

#### Filter sheet (mobile)
The opened filter overlay at 390: Collection/Size radios, Colour swatches, × close. Read as `m-filter-sheet` on the category (PLP) page at 390 wide.

**Values (default).** size 326 x 1063.63; background transparent; text Gilroy 22/26.4 700, #000f2e `color.deep_sea.default`; layers div.swatch-option.color 32.0x32.0 rgb(240, 240, 240) 100%; div.swatch-option.color 32.0x32.0 rgb(148, 148, 148) 100%; div.swatch-option.color 32.0x32.0 rgb(0, 0, 0) 100%; div.swatch-option.color 32.0x32.0 rgb(53, 98, 161) 100%; div.swatch-option.color 32.0x32.0 rgb(98, 148, 49) 100%; div.swatch-option.color 32.0x32.0 rgb(243, 213, 78) 100%.

Child layers that carry the look: div 32x32 background #f0f0f0 image linear-gradient(to left, rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 50%, rgba(0, 0, 0, 0.1)  radius 100%; div 32x32 background #949494 image linear-gradient(to left, rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 50%, rgba(0, 0, 0, 0.1)  radius 100%; div 32x32 background #000000 `color.neutral.ink` image linear-gradient(to left, rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 50%, rgba(0, 0, 0, 0.1)  radius 100%.

![Filter sheet (mobile) default](components/crops/m-filter-sheet-default.png)

#### Mobile filter row
A radio row in the mobile filter sheet. Read as `m-filter-radio` on the category (PLP) page at 390 wide.

**Note:** Misidentified: the stored state is the product link 'Insulated (350 ml) - Pine Green', not a filter option row. The row search is now scoped to the marked sheet and a re-measure is queued.

Not on the page when it was captured.

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the dopper. wordmark, the nav chevrons and bag glyph, the feature-line iconography, the 'Be my hero' basket illustration, the social and payment marks) are the product's artwork. The shop serves a Dopper-Icons icon font (raw/css-vars.json fonts). Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Everything behind the login card — the customer account, order history, addresses and the whole checkout flow — was never reached. The Magento checkout begins at /checkout/ past the cart and was never opened; Add to cart was measured and its pressed state CDP-forced, never really clicked, so a filled cart, the cart drawer, shipping, payment and any logged-in surface are undocumented. The marketing site's "For Businesses" B2B portal, the Digital Product Passport and the Tap/Map/community apps are linked surfaces that were not captured.

### Pages

- **Two hosts.** www.dopper.com is the Next.js/Storyblok marketing site; shop.dopper.com is Magento 2 (theme Dopper/dopper_b2c). The header and brand palette are shared; shop values are compiled literals (measured, not declared). Other locales (/nl/, /de/, /fr/) were not captured — English only.
- **Add to cart was never really clicked** (its pressed state is CDP-forced): the filled cart, mini-cart and every step past it are uncaptured by design.
- **Configurator rows** ('Choose collection', 'Select your pattern', 'Own text or image', 'Accessories') are links to filtered/option views, not in-page toggles — the kit's toggle refused them; measured at rest only.
- **The flyout card's inner CTAs** ('Buy a bottle', 'Customise 60+ bottles') sit inside the card's own markup — probably a closed shadow root — no standalone leaf exposed them. The same deep-sea pill is measured as btn-dark.
- **External surfaces** (Dopper app stores, social profiles, Cradle to Cradle, the Digital Product Passport) are linked but were never opened.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover); on elements inside DOPPER-NAVIGATION's shadow root the CDP node lookup could not reach them, so nav-trigger/nav-link/m-burger/m-nav-item/m-menu-pill have no pressed reading (recorded as errors, not absence).
- **Disabled, error and loading states** were not seen on the public surface (the PDP buy box's skeleton shimmer was caught mid-load in the default shot).
- **The mega-menu closes on blur**; each flyout-child measurement re-opened it via the Bottle trigger before reading.

### Themes

Light-only. Neither host has a dark theme mechanism — no theme class, attribute or prefers-color-scheme retheme was found, and vars.mjs resolved only a light set. The darkBlue mobile menu and the deep-sea/darkBlue bands are brand-painted surfaces of the light page, not a theme — the export holds no invented dark set.

### Fonts

- **Dopper** (regular — the display face and wordmark) and **Gilroy** (Medium/400, Bold/600) are served from www.dopper.com's Next.js media; the shop also serves Gilroy 400/600/800 and a Dopper-Icons icon font. The @font-face blocks are harvested in raw/css-vars.json. The style guide falls back to system sans — the faces are licensed, not shipped.

### Screenshots

- The hero is a full-bleed video ('Whatever the season'): screenshots freeze one frame; its motion is not a token.
- Full-page captures were bounded at the kit's 8-chunk cap: home is ~10k px (9999 captured), shop ~13k px, category ~11.9k px; mobile pages exceed 15k px and were stitched from tiles. Everything below the cap is documented but the longest tails were truncated.
- The Cookiebot dialog and the chat widget were hidden before every shot, never answered; where a page reserves their layer the shots show the page as a consenting visitor sees it.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Product photography, the bottle artwork, marketing copy and article content are the product's; only frames and components were measured.
