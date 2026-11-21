# Alo Yoga components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from aloyoga.com on 2026-11-21, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (47 components, 105 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (110 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the shop paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/en-sg` | [consent](screenshots/home-light-consent.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [megamenu](screenshots/home-light-megamenu.png), [search](screenshots/home-light-search.png) |
| Shop: women | `/en-sg/collections/womens-shop-all` | [default](screenshots/shop-women-light-default.png), [filter](screenshots/shop-women-light-filter.png), [full](screenshots/shop-women-light-full.png), [sort](screenshots/shop-women-light-sort.png) |
| Shop: men | `/en-sg/collections/mens-shop-all` | [default](screenshots/shop-men-light-default.png), [full](screenshots/shop-men-light-full.png) |
| New arrivals | `/en-sg/collections/new-arrivals` | [default](screenshots/new-arrivals-light-default.png), [full](screenshots/new-arrivals-light-full.png) |
| Product page | `first product on the shop grid` | [default](screenshots/pdp-light-default.png), [full](screenshots/pdp-light-full.png) |
| New to Alo | `/en-sg/pages/new-to-alo` | [default](screenshots/new-to-alo-light-default.png), [full](screenshots/new-to-alo-light-full.png) |
| Cart | `/en-sg/cart` | [default](screenshots/cart-light-default.png), [full](screenshots/cart-light-full.png) |
| Account login | `/en-sg/account` | [default](screenshots/account-light-default.png), [full](screenshots/account-light-full.png) |
| Home, phone | `/en-sg` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png), [search](screenshots/mobile-home-light-search.png) |
| Shop grid, phone | `/en-sg/collections/womens-shop-all` | [default](screenshots/mobile-shop-women-light-default.png), [filter](screenshots/mobile-shop-women-light-filter.png), [full](screenshots/mobile-shop-women-light-full.png), [sort](screenshots/mobile-shop-women-light-sort.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Osano consent dialog | every page, on load | captured as it arrives, then hidden (never answered: no Accept/Reject/Save is ever clicked) | [home-light-consent](screenshots/home-light-consent.png) |
| WOMEN mega-menu | header, home | the nav item hovered; the flyout shows in the crop | [home-light-megamenu](screenshots/home-light-megamenu.png), [nav-mega](#mega-menu-open) |
| PDP colour tile | product page | a colour label toggled; never an add-to-bag | [pdp-swatch-picked-opened](components/crops/pdp-swatch-picked-opened.png), [pdp-swatch-picked](#pdp-swatch-picked) |
| Mobile menu drawer | home, phone | the menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 19 components were given a real keyboard focus. 18 draw an outline ring: `nav-item` (5px auto #005fcc `measured.focus-outline`, offset 1px), `account-icon` (5px auto #005fcc `measured.focus-outline`, offset 0px), `bag-icon` (5px auto #005fcc `measured.focus-outline`, offset 1px), `hero-button` (5px auto #005fcc `measured.focus-outline`, offset 0px), `carousel-cta` (5px auto #005fcc `measured.focus-outline`, offset 1px), `sort-button` (5px auto #005fcc `measured.focus-outline`, offset 0px), `swatch` (5px auto #005fcc `measured.focus-outline`, offset 0px), `product-name` (5px auto #005fcc `measured.focus-outline`, offset 1px), `pdp-swatch` (5px auto #005fcc `measured.focus-outline`, offset 0px), `size-button` (5px auto #005fcc `measured.focus-outline`, offset 0px), `add-to-bag` (5px auto #005fcc `measured.focus-outline`, offset 0px), `size-guide` (5px auto #005fcc `measured.focus-outline`, offset 0px), `cart-continue` (5px auto #005fcc `measured.focus-outline`, offset 1px), `m-menu-button` (5px auto #e59700, offset 0px), `m-hero-button` (5px auto #e59700, offset 0px), `wishlist-button` (5px auto #005fcc `measured.focus-outline`, offset 0px), `footer-link` (5px auto #005fcc `measured.focus-outline`, offset 1px), `footer-social` (5px auto #005fcc `measured.focus-outline`, offset 1px). 1 change only their border: `more-colors`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): controls deepen their fill or dim rather than scale; the nav flyout and framework icons keep their hover scale. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.3s | `ease` | color | bag-icon, carousel-cta, cart-continue, color-tile, footer-link, footer-social, logo, more-colors and more |
| 0.5s | `ease-in-out` | background-color, opacity | add-to-bag, to-top |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Product tile](#product-tile) | 324 x 645.8 | - | - | transparent | none | 0 |
| [Colour-story tile](#colour-story-tile) | 272 x 408 | - | - | transparent | none | 0 |
| [Mobile product tile](#mobile-product-tile) | 390 x 557.89 | - | - | transparent | none | 0 |
| [Empty cart](#empty-cart) | 1440 x 639.42 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The promo strip, the white header bar and the mega-menu flyout.

#### Promo strip
The thin bar above the header linking the current offer. Read as `promo-strip` on the shop home page.

Not on the page when it was captured.

#### Header
The white bar: wordmark, WOMEN/MEN/SHOES nav, search, account, bag. Read as `header` on the shop home page.

**Values (default).** size 1440 x 84; background transparent; text proxima-nova 18/normal 500, #000000 `measured.action-bg`; icon 71 x 48, #000000 `measured.action-bg`; layers div.desktop-nav.row 1440.0x84.0 B:1px solid rgb(222, 222, 222); div.container-fluid.main-navbar__sub-items 1440.0x15.0 rgb(255, 255, 255); div.row.no-gutters 1350.0x570.2 T:1px solid rgb(222, 222, 222) / B:1px solid rgb(222, 222, 222); div.container-fluid.main-navbar__sub-items 1440.0x15.0 rgb(255, 255, 255); div.row.no-gutters 1350.0x395.1 T:1px solid rgb(222, 222, 222) / B:1px solid rgb(222, 222.

Child layers that carry the look: div 1440x84 border 1px solid #dedede; div 1440x15 background #ffffff `color.neutral.white`; div 1350x570.2 border 1px solid #dedede.

![Header default](components/crops/header-default.png)

#### Logo
Read as `logo` on the shop home page.

**Values (default).** size 71 x 53; background transparent; text proxima-nova 16/normal 400, #000000 `measured.action-bg`; transition color 0.3s ease; icon 71 x 48, #000000 `measured.action-bg`.

![Logo default](components/crops/logo-default.png)

#### Nav item
A top-level shop category; hover opens the mega-menu. Read as `nav-item` on the shop home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 71.95 x 70; padding 24px 0px; background transparent; text proxima-nova 18/normal 500, #000000 `measured.action-bg`; transition color 0.3s ease; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | layers ::after rgb(0, 0, 0) 0px none 1; a::after.main-nav__item.hover-target 71.9531pxx3px rgb(0, 0, 0) |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset 1px; layers ::after rgb(0, 0, 0) 0px none 1; a.main-nav__item.hover-target 72.0x70.0; a::after.main-nav__item.hover-target 71.9531pxx3px rgb(0, 0, 0) |
| pressed | layers ::after rgb(0, 0, 0) 0px none 1; a::after.main-nav__item.hover-target 71.9531pxx3px rgb(0, 0, 0) |

![Nav item default](components/crops/nav-item-default.png) ![Nav item hover](components/crops/nav-item-hover.png) ![Nav item focus-visible](components/crops/nav-item-focus-visible.png) ![Nav item pressed](components/crops/nav-item-pressed.png)

#### Mega-menu, open
The nav item while its flyout is open; the panel shows in the crop. Read as `nav-mega` on the shop home page.

**Values (opened).** size 71.95 x 70; padding 24px 0px; background transparent; text proxima-nova 18/normal 500, #000000 `measured.action-bg`; transition color 0.3s ease; layers ::after rgb(0, 0, 0) 0px none 1; a::after.main-nav__item.hover-target 71.9531pxx3px rgb(0, 0, 0).

Child layers that carry the look: a::after 71.9531pxx3px background #000000 `measured.action-bg`.

![Mega-menu, open opened](components/crops/nav-mega-opened.png)

#### Search icon
Read as `search-icon` on the shop home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 20 x 25; background transparent; text proxima-nova 16/normal 400, #000000 `measured.action-bg`; transition color 0.3s ease; layers span.icon-search-static 20.0x20.0 |
| hover, pressed | text proxima-nova 16/normal 400, #595959 |

Child layers that carry the look: span 20x20 image url(data:…).

![Search icon default](components/crops/search-icon-default.png) ![Search icon hover](components/crops/search-icon-hover.png) ![Search icon pressed](components/crops/search-icon-pressed.png)

#### Account icon
Read as `account-icon` on the shop home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 18 x 20; background transparent; text proxima-nova 16/normal 400, #000000 `measured.action-bg`; layers span.icon-account-static 18.0x17.0 |
| hover | layers span.icon-account-solid 18.0x17.0 |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset 0px; layers button.account-icon 18.0x20.0; span.icon-account-static 18.0x17.0 |

Child layers that carry the look: span 18x17 image url(data:…).

![Account icon default](components/crops/account-icon-default.png) ![Account icon hover](components/crops/account-icon-hover.png) ![Account icon focus-visible](components/crops/account-icon-focus-visible.png) ![Account icon pressed](components/crops/account-icon-pressed.png)

#### Bag icon
Read as `bag-icon` on the shop home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 18 x 29; background transparent; text proxima-nova 16/normal 400, #000000 `measured.action-bg`; transition color 0.3s ease; layers span.icon-bag-static 18.0x24.0 |
| hover | text proxima-nova 16/normal 400, #595959 |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset 1px; text proxima-nova 16/normal 400, #595959; layers a.main-navbar__icon.main-navbar__icon--bag 18.0x29.0; span.icon-bag-static 18.0x24.0 |
| pressed | text proxima-nova 16/normal 400, #595959 |

Child layers that carry the look: span 18x24 image url(data:…).

![Bag icon default](components/crops/bag-icon-default.png) ![Bag icon hover](components/crops/bag-icon-hover.png) ![Bag icon focus-visible](components/crops/bag-icon-focus-visible.png) ![Bag icon pressed](components/crops/bag-icon-pressed.png)

#### Search field
The header search input; focused only, nothing typed. Read as `search-input` on the shop home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 175 x 26; padding 1px 2px; border 2px inset #767676; background #ffffff `color.neutral.white`; text proxima-nova 16/normal 400, #000000 `measured.action-bg`; placeholder #000000 `measured.action-bg` |
| focused | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |

![Search field default](components/crops/search-input-default.png) ![Search field focused](components/crops/search-input-focused.png)

### Home

Hero, category tiles, carousels and Builder.io colour stories.

#### Hero button
The filled hero CTA ("JOIN NOW"). Measured, never followed. Read as `hero-button` on the shop home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 192.88 x 48; padding 15px 30px; background #000000 `measured.action-bg`; text proxima-nova 18/18 900, #ffffff `color.neutral.white` |
| hover | background #ffffff `color.neutral.white`; text proxima-nova 18/18 900, #000000 `measured.action-bg` |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset 0px |
| pressed | background #ffffff `color.neutral.white`; text proxima-nova 18/18 900, #000000 `measured.action-bg` |

![Hero button default](components/crops/hero-button-default.png) ![Hero button hover](components/crops/hero-button-hover.png) ![Hero button focus-visible](components/crops/hero-button-focus-visible.png) ![Hero button pressed](components/crops/hero-button-pressed.png)

#### Category tile
A shop-category image tile (NEW ARRIVALS, PANTS, ...). Read as `grid-card` on the shop home page.

Not on the page when it was captured.

#### Tile label
Read as `grid-card-label` on the shop home page.

Not on the page when it was captured.

#### Carousel CTA link
"Shop Now" over a product carousel. Read as `carousel-cta` on the shop home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 129.31 x 22.39; background transparent; text proxima-nova 16/22.4 400, #000000 `measured.action-bg`; transition color 0.3s ease |
| hover | size 132.89 x 22.39; text proxima-nova 16/22.4 700, #000000 `measured.action-bg` |
| focus-visible | size 132.89 x 22.39; outline 5px auto #005fcc `measured.focus-outline`, offset 1px; text proxima-nova 16/22.4 700, #000000 `measured.action-bg`; layers a.carousel-header__cta.body-text-link 132.9x22.4 |
| pressed | size 132.89 x 22.39; text proxima-nova 16/22.4 700, #000000 `measured.action-bg` |

![Carousel CTA link default](components/crops/carousel-cta-default.png) ![Carousel CTA link hover](components/crops/carousel-cta-hover.png) ![Carousel CTA link focus-visible](components/crops/carousel-cta-focus-visible.png) ![Carousel CTA link pressed](components/crops/carousel-cta-pressed.png)

#### Colour-story tile
A Builder.io colourway block. Read as `color-tile` on the shop home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 272 x 408; background transparent; text proxima-nova 18/19.8 500, #ffffff `color.neutral.white`; transition color 0.3s ease; layers div.builder-block.builder-089145351202458b965b714f683813ac 260.0x110.6 rgb(127, 98, 74) |

Child layers that carry the look: div 260x110.6 background #7f624a.

![Colour-story tile default](components/crops/color-tile-default.png) ![Colour-story tile hover](components/crops/color-tile-hover.png)

#### Back-to-top button
The floating round return-to-top control. Read as `to-top` on the shop home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 98 x 98; background transparent; image url(…); text proxima-nova 16/normal 400, #000000 `measured.action-bg`; transition opacity 0.5s ease-in-out |
| hover, pressed | text proxima-nova 16/normal 400, #595959 |

![Back-to-top button default](components/crops/to-top-default.png) ![Back-to-top button hover](components/crops/to-top-hover.png) ![Back-to-top button pressed](components/crops/to-top-pressed.png)

### Shop grid

The collection grid: tiles, swatches, member-price hooks.

#### Collection title
Read as `plp-title` on the women's shop grid page.

**Values (default).** size 1382.41 x 44; background transparent; text proxima-nova 40/44 600, #000000 `measured.action-bg`.

![Collection title default](components/crops/plp-title-default.png)

#### Sort control
The grid sort/filter trigger. Measured, never opened. Read as `sort-button` on the women's shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 167.03 x 34; padding 0px 24px; border 1px solid #cccccc `color.neutral.alto`; radius 360px; background #ffffff `color.neutral.white`; text proxima-nova 14/normal 500, #000000 `measured.action-bg` |
| hover | border 1px solid #e1e1e1 `color.neutral.mercury`; background #e1e1e1 `color.neutral.mercury` |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset 0px |
| pressed | border 1px solid #e1e1e1 `color.neutral.mercury`; background #e1e1e1 `color.neutral.mercury` |

![Sort control default](components/crops/sort-button-default.png) ![Sort control hover](components/crops/sort-button-hover.png) ![Sort control focus-visible](components/crops/sort-button-focus-visible.png) ![Sort control pressed](components/crops/sort-button-pressed.png)

#### Product tile
A grid card: image, name, price, colour swatches, member-price link. Read as `product-tile` on the women's shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 324 x 645.8; background transparent; text proxima-nova 12/normal 400, #000000 `measured.action-bg`; layers span.icon-wishlist-static 20.0x20.0; div.product-card-badge 87.5x22.0 rgb(242, 242, 242); button.SwatchUI.swatch 26.0x26.0 rgb(0, 0, 0) T:1px solid rgb(236, 236, 236) / R:1px solid rgb(236, 236, 236) / B:1px solid rgb(236, 236, 236) / L:1px solid rgb(236, 236, 236) 50%; button::before.SwatchUI.swatch 32pxx32px T:1px solid rgb(127, 127, 127) / R:1px solid rgb(127, 127, 127) / B:1px solid rgb(127, 1 |
| hover | text proxima-nova 16/16 400, #ffffff `color.neutral.white`; layers span.icon-wishlist-static 20.0x20.0; div.quick-add.quick-add-dark-mode 304.0x58.0 rgb(59, 59, 59); button.quick-add-size-btn 42.3x25.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0); button.quick-add-size-btn 31.8x25.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid r |

Child layers that carry the look: span 20x20 image url(data:…); div 87.5x22 background #f2f2f2 `color.neutral.smoke`; button 26x26 background #000000 `measured.action-bg` border 1px solid #ececec radius 50%.

![Product tile default](components/crops/product-tile-default.png) ![Product tile hover](components/crops/product-tile-hover.png)

#### Colour swatch
A product colour dot; a local selection toggle. Read as `swatch` on the women's shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 26 x 26; border 1px solid #ececec; radius 50%; background #000000 `measured.action-bg`; text proxima-nova 16/normal 400, #000000 `measured.action-bg`; layers ::before rgba(0, 0, 0, 0) 1px none 1 |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset 0px |

![Colour swatch default](components/crops/swatch-default.png) ![Colour swatch hover](components/crops/swatch-hover.png) ![Colour swatch focus-visible](components/crops/swatch-focus-visible.png) ![Colour swatch pressed](components/crops/swatch-pressed.png)

#### Swatch, selected
Read as `swatch-selected` on the women's shop grid page.

**Values (default).** size 26 x 26; border 1px solid #ececec; radius 50%; background #000000 `measured.action-bg`; text proxima-nova 16/normal 400, #000000 `measured.action-bg`; layers ::before rgba(0, 0, 0, 0) 1px none 1.

![Swatch, selected default](components/crops/swatch-selected-default.png)

#### Product name link
Read as `product-name` on the women's shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 324 x 22.39; background transparent; text proxima-nova 16/22.4 600, #000000 `measured.action-bg`; transition color 0.3s ease |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset 1px; layers a 324.0x22.4 |

![Product name link default](components/crops/product-name-default.png) ![Product name link hover](components/crops/product-name-hover.png) ![Product name link focus-visible](components/crops/product-name-focus-visible.png) ![Product name link pressed](components/crops/product-name-pressed.png)

#### Member-price link
"Join Now" — the membership hook. Measured, never followed. Read as `member-link` on the women's shop grid page.

Not on the page when it was captured.

#### More colours chip
Read as `more-colors` on the women's shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 33 x 17; padding 0px 0px 0px 5px; background transparent; text proxima-nova 14/normal 400, #000000 `measured.action-bg`; transition color 0.3s ease; layers span.alo-add-thick-icon.icon__increment 9.0x9.0 |
| hover, focus-visible, pressed | text proxima-nova 14/normal 400, #595959 |

Child layers that carry the look: span 9x9 image url(data:…)' stroke='%23000' stroke-width='3.333' stroke-miterlimit='50'%3E%3Cpath d='M10 .

![More colours chip default](components/crops/more-colors-default.png) ![More colours chip hover](components/crops/more-colors-hover.png) ![More colours chip focus-visible](components/crops/more-colors-focus-visible.png) ![More colours chip pressed](components/crops/more-colors-pressed.png)

### Product page

Title, price, colour tiles, size chips and the buy button.

#### Product title
Read as `pdp-title` on the product page page.

**Values (default).** size 231.53 x 26.39; background transparent; text proxima-nova 24/26.4 500, #000000 `measured.action-bg`.

![Product title default](components/crops/pdp-title-default.png)

#### Product price
Read as `pdp-price` on the product page page.

**Values (default).** size 336.16 x 25.19; background transparent; text proxima-nova 18/25.2 400, #000000 `measured.action-bg`; layers div::before.review-star autoxauto.

Child layers that carry the look: div::before autoxauto image linear-gradient(90deg, #ceb18f calc(92.5532%), #ffffff `color.neutral.white` calc(92.5532%.

![Product price default](components/crops/pdp-price-default.png)

#### PDP swatch
Read as `pdp-swatch` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 46 x 78; background transparent; text proxima-nova 14/normal 400, #000000 `measured.action-bg`; layers span.swatch__wrapper 46.0x46.0 T:1px solid rgb(151, 151, 151) / R:1px solid rgb(151, 151, 151) / B:1px solid rgb(151, 151, 151) / L:1px solid rgb(151, 151, 151) 50%; span.swatch 35.0x35.0 rgb(0, 0, 0) 50%; span.swatch-disabled-ui 0.0x0.0 rgb(255, 255, 255); span.line 0.0x0.0 rgb(151, 151, 151) |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset 0px; layers label.UserSelection.square 46.0x78.0; span.swatch__wrapper 46.0x46.0 T:1px solid rgb(151, 151, 151) / R:1px solid rgb(151, 151, 151) / B:1px solid rgb(151, 151, 151) / L:1px solid rgb(151, 151, 151) 50%; span.swatch 35.0x35.0 rgb(0, 0, 0) 50%; span.swatch-disabled-ui 0.0x0.0 rgb(255, 255, 255); span.line 0.0x0.0 rgb(151, 151, 151) |

Child layers that carry the look: span 46x46 border 1px solid #979797 radius 50%; span 35x35 background #000000 `measured.action-bg` radius 50%; span 0x0 background #ffffff `color.neutral.white`.

![PDP swatch default](components/crops/pdp-swatch-default.png) ![PDP swatch hover](components/crops/pdp-swatch-hover.png) ![PDP swatch focus-visible](components/crops/pdp-swatch-focus-visible.png) ![PDP swatch pressed](components/crops/pdp-swatch-pressed.png)

#### PDP swatch, picked
A colour swatch after its own toggle; never an add-to-bag. Read as `pdp-swatch-picked` on the product page page.

**Values (opened).** size 46 x 78; background transparent; text proxima-nova 14/normal 400, #000000 `measured.action-bg`; layers span.swatch__wrapper 46.0x46.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 50%; span.swatch 35.0x35.0 rgb(0, 0, 0) 50%; span.swatch-disabled-ui 0.0x0.0 rgb(255, 255, 255); span.line 0.0x0.0 rgb(151, 151, 151).

Child layers that carry the look: span 46x46 border 1px solid transparent radius 50%; span 35x35 background #000000 `measured.action-bg` radius 50%; span 0x0 background #ffffff `color.neutral.white`.

![PDP swatch, picked opened](components/crops/pdp-swatch-picked-opened.png)

#### Size button
Read as `size-button` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 134 x 40; border 1px solid transparent; background #ffffff `color.neutral.white`; outline 1px solid #cccccc `color.neutral.alto`, offset 0px; text proxima-nova 16/normal 500, #000000 `measured.action-bg` |
| hover | border 1px solid #000000 `measured.action-bg`; outline 1px solid #000000 `measured.action-bg`, offset 0px |
| focus-visible | border 1px solid #000000 `measured.action-bg`; outline 5px auto #005fcc `measured.focus-outline`, offset 0px |
| pressed | border 1px solid #000000 `measured.action-bg`; background #000000 `measured.action-bg`; outline 1px solid #000000 `measured.action-bg`, offset 0px; text proxima-nova 16/normal 500, #ffffff `color.neutral.white` |

![Size button default](components/crops/size-button-default.png) ![Size button hover](components/crops/size-button-hover.png) ![Size button focus-visible](components/crops/size-button-focus-visible.png) ![Size button pressed](components/crops/size-button-pressed.png)

#### Add to bag
The purchase action; measured in every state except a real press. Read as `add-to-bag` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 52; padding 14px 16px; border 1px solid #000000 `measured.action-bg`; background #000000 `measured.action-bg`; text proxima-nova 18/normal 700, #ffffff `color.neutral.white`; transition background-color 0.5s ease-in-out |
| hover | border 1px solid #242424 `color.neutral.charcoal`; background #232323 `measured.action-bg-hover` |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset 0px |

![Add to bag default](components/crops/add-to-bag-default.png) ![Add to bag hover](components/crops/add-to-bag-hover.png) ![Add to bag focus-visible](components/crops/add-to-bag-focus-visible.png)

#### Size-guide link
Read as `size-guide` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 79.22 x 22.39; background transparent; text proxima-nova 16/22.4 400, #000000 `measured.action-bg` |
| hover | size 80.84 x 22.39; text proxima-nova 16/22.4 700, #000000 `measured.action-bg` |
| focus-visible | size 80.84 x 22.39; outline 5px auto #005fcc `measured.focus-outline`, offset 0px; text proxima-nova 16/22.4 700, #000000 `measured.action-bg`; layers span.label-add.size-guide-trigger 80.8x22.4 |
| pressed | size 80.84 x 22.39; text proxima-nova 16/22.4 700, #000000 `measured.action-bg` |

![Size-guide link default](components/crops/size-guide-default.png) ![Size-guide link hover](components/crops/size-guide-hover.png) ![Size-guide link focus-visible](components/crops/size-guide-focus-visible.png) ![Size-guide link pressed](components/crops/size-guide-pressed.png)

#### PDP accordion
Details/shipping disclosure row. Read as `pdp-accordion` on the product page page.

Not on the page when it was captured.

#### PDP accordion, open
Read as `pdp-accordion-open` on the product page page.

Not on the page when it was captured.

#### Size button, out of stock
The sold-out size state (a "notify me" affordance). Never pressed. Read as `size-oos` on the product page page.

Not on the page when it was captured.

#### Wishlist button
The ghost sibling of Add to bag. Measured, never pressed. Read as `wishlist-button` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 52; padding 14px 32px; border 1px solid #000000 `measured.action-bg`; background #ffffff `color.neutral.white`; text proxima-nova 18/normal 700, #000000 `measured.action-bg` |
| hover | border 1px solid #e1e1e1 `color.neutral.mercury`; background #e1e1e1 `color.neutral.mercury` |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset 0px |
| pressed | border 1px solid #e1e1e1 `color.neutral.mercury`; background #e1e1e1 `color.neutral.mercury` |

![Wishlist button default](components/crops/wishlist-button-default.png) ![Wishlist button hover](components/crops/wishlist-button-hover.png) ![Wishlist button focus-visible](components/crops/wishlist-button-focus-visible.png) ![Wishlist button pressed](components/crops/wishlist-button-pressed.png)

### Cart

The signed-out bag.

#### Empty cart
The signed-out bag with nothing in it. Read as `cart-empty` on the cart page.

**Values (default).** size 1440 x 639.42; background transparent; text proxima-nova 24/26.4 600, #000000 `measured.action-bg`; layers ::before rgba(0, 0, 0, 0.35) 0px none 1; main::before.main 1440pxx639.422px rgba(0, 0, 0, 0.35); div.builder-block.builder-c01ef5469a8242e5aff26dbecce4d263 1156.0x0.0 rgba(255, 255, 255, 0); div.full-width__line.d-block 0.0x0.0 B:1px solid rgb(223, 223, 223); div.shopping-bag-block.shopping-bag-block__new 770.0x99.0 T:1px solid rgb(207, 207, 207); a.btn.btn-primary 112.7x40.0 rgb(0, 0, 0) T:1px so.

Child layers that carry the look: main::before 1440pxx639.422px background rgba(0, 0, 0, 0.35); div 1156x0 background rgba(255, 255, 255, 0); div 0x0 border 1px solid #dfdfdf.

![Empty cart default](components/crops/cart-empty-default.png)

#### Continue shopping
Measured, never followed. Read as `cart-continue` on the cart page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 112.67 x 40; padding 10px 16px; border 1px solid transparent; background #000000 `measured.action-bg`; text proxima-nova 15/18 400, #fefefe; transition color 0.3s ease |
| hover | border 1px solid #404040; background #404040 |
| focus-visible | border 1px solid #404040; background #404040; outline 5px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | border 1px solid #000000 `measured.action-bg` |

![Continue shopping default](components/crops/cart-continue-default.png) ![Continue shopping hover](components/crops/cart-continue-hover.png) ![Continue shopping focus-visible](components/crops/cart-continue-focus-visible.png) ![Continue shopping pressed](components/crops/cart-continue-pressed.png)

### Footer

The page footer and newsletter field.

#### Footer
Read as `footer` on the shop home page.

**Values (default).** size 1440 x 643.27; padding 28px 0px 64px 0px; background #000000 `measured.action-bg`; text proxima-nova 16/22.4 600, #ffffff `color.neutral.white`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the shop home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 88.83 x 20; background transparent; text proxima-nova 16/22.4 400, #ffffff `color.neutral.white`; transition color 0.3s ease |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset 1px; layers a.body 88.8x20.0 |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer social icon
Read as `footer-social` on the shop home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 27 x 20; background transparent; text proxima-nova 16/normal 400, #ffffff `color.neutral.white`; transition color 0.3s ease |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset 1px; layers a.nav-link 27.0x20.0 |

![Footer social icon default](components/crops/footer-social-default.png) ![Footer social icon hover](components/crops/footer-social-hover.png) ![Footer social icon focus-visible](components/crops/footer-social-focus-visible.png) ![Footer social icon pressed](components/crops/footer-social-pressed.png)

#### Newsletter field
Focused only; never subscribed. Read as `newsletter-input` on the shop home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 293 x 48.39; padding 12px 16px; border 1px solid #a3a3a3 `color.neutral.dawn`; background transparent; text proxima-nova 16/22.4 400, #ffffff `color.neutral.white`; placeholder #636363 `color.neutral.chicago` |
| focused | border 1px solid #ffffff `color.neutral.white` |

![Newsletter field default](components/crops/newsletter-input-default.png) ![Newsletter field focused](components/crops/newsletter-input-focused.png)

### Mobile (390 wide)

The same surface at phone width, with the menu drawer open.

#### Mobile header
Read as `m-header` on the shop home page at 390 wide.

**Values (default).** size 390 x 57; background transparent; text proxima-nova 16/normal 400, #000000 `measured.action-bg`; layers div.desktop-nav.row 0.0x0.0 B:1px solid rgb(222, 222, 222); div.container-fluid.main-navbar__sub-items 0.0x0.0 rgb(255, 255, 255); div.row.no-gutters 0.0x0.0 T:1px solid rgb(222, 222, 222) / B:1px solid rgb(222, 222, 222); div.container-fluid.main-navbar__sub-items 0.0x0.0 rgb(255, 255, 255); div.row.no-gutters 0.0x0.0 T:1px solid rgb(222, 222, 222) / B:1px solid rgb(222, 222, 222); div.container-.

Child layers that carry the look: div 0x0 border 1px solid #dedede; div 0x0 background #ffffff `color.neutral.white`; div 0x0 border 1px solid #dedede.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the shop home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 30 x 30; padding 4px; border 1px solid transparent; background transparent; text proxima-nova 16/16 400, #000000 `measured.action-bg` |
| hover | opacity 0.7 |
| focus-visible | outline 5px auto #e59700, offset 0px; opacity 0.7 |
| pressed | opacity 0.7 |

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button hover](components/crops/m-menu-button-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The button after its own toggle; the open drawer shows in the crop. Read as `m-menu-open` on the shop home page at 390 wide.

**Values (opened).** size 29 x 29; padding 4px; border 1px solid transparent; background transparent; text proxima-nova 16/16 400, #000000 `measured.action-bg`; opacity 0.7.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav link
A row inside the opened menu drawer. Read as `m-nav-link` on the shop home page at 390 wide.

Not on the page when it was captured.

#### Mobile hero button
Read as `m-hero-button` on the shop home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 172.88 x 38; padding 10px 20px; background #ffffff `color.neutral.white`; text proxima-nova 18/18 900, #000000 `measured.action-bg` |
| focus-visible | outline 5px auto #e59700, offset 0px |
| pressed | background #000000 `measured.action-bg`; text proxima-nova 18/18 900, #ffffff `color.neutral.white` |

![Mobile hero button default](components/crops/m-hero-button-default.png) ![Mobile hero button hover](components/crops/m-hero-button-hover.png) ![Mobile hero button focus-visible](components/crops/m-hero-button-focus-visible.png) ![Mobile hero button pressed](components/crops/m-hero-button-pressed.png)

#### Mobile product tile
Read as `m-product-tile` on the shop home page at 390 wide.

**Values (default).** size 390 x 557.89; background transparent; text proxima-nova 24/26.4 600, #000000 `measured.action-bg`; layers span.icon-wishlist-static 20.0x20.0; span 40.0x40.0 rgba(255, 255, 255, 0.5) 50%; span.alo-quick-add-icon 20.0x20.0; div.product-card-badge 87.5x22.0 rgb(242, 242, 242); button.SwatchUI.swatch 28.0x28.0 rgb(81, 59, 44) T:1px solid rgb(236, 236, 236) / R:1px solid rgb(236, 236, 236) / B:1px solid rgb(236, 236, 236) / L:1px solid rgb(236, 236, 236) 50%; button::before.SwatchUI.swatch 32pxx32px T:1px.

Child layers that carry the look: span 20x20 image url(data:…); span 40x40 background rgba(255, 255, 255, 0.5) radius 50%; span 20x20 image url(data:…).

![Mobile product tile default](components/crops/m-product-tile-default.png)

### Other



## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Alo's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **Checkout, the bag drawer and anything behind sign-in.** No item was added to the bag. `https://www.aloyoga.com/en-sg/account/login` is a join and sign-in wall. The branch stops there. Nothing was typed.
- **Anything that buys, sends or joins.** No product was added to the bag, no form was submitted, no search query was typed, no membership was joined, no consent choice was made.
- **Login, password, phone, birthday and newsletter fields** were not filled. Search, the women mega-menu, the filter drawer and the sort menu were opened and screenshotted. Their inner controls were not measured as component states.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The shop paints one light theme on every captured route. The stylesheet does declare embedded-widget themes (the `.s-mode-*`/`.s-theme-*` blocks of a third-party app and Osano's own colours): recorded in [raw/css-vars.json](raw/css-vars.json) under the `vendor` bin, never applied to the storefront and not tokenised. No dark or reduced-contrast mode is offered.

### Fonts

- **Proxima Nova** (`--primary-font`) is Alo's licensed face — every headline, nav item and button. It is not distributed; the style guide falls back to Helvetica/system.
- A mono face is declared only inside widgets; the storefront itself is sans-only.

### Screenshots

- Product photography and the Alo wordmark in the screenshots are Alo's content. The PDP captured is whichever product the shop grid listed first at run time (recorded as `pdp_url` in components-computed.json); another run may land on a different product.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Product photography, campaign imagery and Builder.io colour stories are the product's content; only the frames and components were measured. `color-tile` and `to-top` missed their selectors on this pass (lazy Builder blocks) and are recorded as missing.
