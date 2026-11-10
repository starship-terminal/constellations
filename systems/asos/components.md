# ASOS components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from asos.com on 2026-11-10, signed out, in headed Chrome at 1440 x 900 (the Mobile group at 390 x 844) — Akamai serves a 403 to headless browsers, so the capture ran headed — with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (72 components, 180 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (176 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the shop paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [consent](screenshots/home-light-consent.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Women's hub | `/women/` | [default](screenshots/women-light-default.png), [full](screenshots/women-light-full.png) |
| Men's hub | `/men/` | [default](screenshots/men-light-default.png), [full](screenshots/men-light-full.png) |
| Shop: women new-in | `/women/new-in/new-in-clothing/cat/?cid=2623` | [default](screenshots/shop-women-light-default.png), [full](screenshots/shop-women-light-full.png) |
| Shop: men new-in | `/men/new-in/new-in-clothing/cat/?cid=27110` | [default](screenshots/shop-men-light-default.png), [full](screenshots/shop-men-light-full.png) |
| Product page | `first product on the shop grid` | [default](screenshots/pdp-light-default.png), [full](screenshots/pdp-light-full.png), [size-picked](screenshots/pdp-light-size-picked.png) |
| Bag | `/bag` | [default](screenshots/bag-light-default.png), [full](screenshots/bag-light-full.png) |
| Saved lists | `/saved-lists/` | [default](screenshots/saved-lists-light-default.png), [full](screenshots/saved-lists-light-full.png) |
| Account gate | `https://my.asos.com/my-account` | [default](screenshots/account-light-default.png), [full](screenshots/account-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Shop grid, phone | `/women/new-in/new-in-clothing/cat/?cid=2623` | [default](screenshots/mobile-shop-women-light-default.png), [full](screenshots/mobile-shop-women-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| OneTrust consent dialog | every page, on load | captured as it arrives, then hidden (never answered: no Accept/Reject/Save is ever clicked) | [home-light-consent](screenshots/home-light-consent.png) |
| Category mega-menu | category nav, shop grid | the first nav button hovered; the flyout shows in the crop | [nav-flyout](#category-flyout-panel), [nav-mega](#category-flyout-open) |
| PDP size select | product page | a size option picked then restored; never added to bag | [size-select-picked](components/crops/size-select-picked.png), [size-select](#size-select) |
| PDP accordion | product page | a disclosure row's own toggle | [pdp-accordion-open-opened](components/crops/pdp-accordion-open-opened.png), [pdp-accordion](#pdp-accordion) |
| Mobile side-panel menu | home, phone | the menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 31 components were given a real keyboard focus. 30 draw an outline ring: `nav-tab` (5px auto #005fcc `measured.focus-outline`, offset -2px), `nav-item` (5px auto #005fcc `measured.focus-outline`, offset -2px), `account-icon` (5px auto #005fcc `measured.focus-outline`, offset -2px), `saved-icon` (5px auto #005fcc `measured.focus-outline`, offset -2px), `bag-icon` (5px auto #005fcc `measured.focus-outline`, offset -2px), `promo-tab` (1px auto #005fcc `measured.focus-outline`, offset 1px), `country-link` (5px auto #005fcc `measured.focus-outline`, offset -2px), `hero-cta` (1px auto #005fcc `measured.focus-outline`, offset 1px), `hero-cta-alt` (1px auto #005fcc `measured.focus-outline`, offset 1px), `cat-pill` (1px auto #005fcc `measured.focus-outline`, offset 1px), `sort-button` (1px auto #005fcc `measured.focus-outline`, offset 0px), `filter-button` (1px auto #005fcc `measured.focus-outline`, offset 0px), `tile-name` (1px auto #005fcc `measured.focus-outline`, offset 1px), `load-more` (1px auto #005fcc `measured.focus-outline`, offset 1px), `help-link` (5px auto #005fcc `measured.focus-outline`, offset -2px), `fit-link` (1px auto #005fcc `measured.focus-outline`, offset 0px), `add-to-bag` (3px auto #005fcc `measured.focus-outline`, offset 0px), `save-button` (1px auto #005fcc `measured.focus-outline`, offset 0px), `delivery-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `pdp-accordion` (3px auto #005fcc `measured.focus-outline`, offset 0px), `gallery-chevron` (1px auto #005fcc `measured.focus-outline`, offset 0px), `reviews-cta` (1px auto #005fcc `measured.focus-outline`, offset 0px), `bag-cta` (1px auto #005fcc `measured.focus-outline`, offset 0px), `saved-cta` (1px auto #005fcc `measured.focus-outline`, offset 0px), `continue-button` (1px solid #0770cf `color.blue.default`, offset 3px), `social-button` (1px solid #0770cf `color.blue.default`, offset 3px), `footer-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `footer-social` (1px auto #005fcc `measured.focus-outline`, offset 1px), `m-menu-button` (1px auto #005fcc `measured.focus-outline`, offset 0px), `m-search-icon` (5px auto #005fcc `measured.focus-outline`, offset -2px). The other 1 show no measured change: `save-heart`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): controls keep their shape — ASOS answers hover with fill swaps (navy on nav buttons, darker green on buy) rather than scale or shadow. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease-in-out` | min-height | nav-flyout |
| 0.3s | `ease` | background-color | search-button |
| 0.4s | `ease` | background-color, border-color | hero-cta, hero-cta-alt |
| 0.4s | `ease-in-out` | color | hero-cta, hero-cta-alt |
| 0.8s | `ease` | opacity | promo-tab |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Product tile](#product-tile) | 335 x 559.41 | - | - | transparent | none | 0 |
| [Content tile](#content-tile) | 345 x 213.73 | - | - | transparent | none | 0 |
| [Hub hero tile](#hub-hero-tile) | 1440 x 640 | - | - | transparent | none | 0 |
| [Hub rail card](#hub-rail-card) | 446.69 x 152.78 | - | - | transparent | none | 0 |
| [Mobile content tile](#mobile-content-tile) | 187 x 115.85 | - | - | transparent | none | 0 |
| [Bag body](#bag-body) | 1440 x 455 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The top app strip, the black header (logo, WOMEN/MEN tabs, search, account, saved, bag) and the category nav with its flyout.

#### App strip
The dark link at the very top right of the page, above the header. Read as `app-strip` on the home page.

**Values (default).** size 194.45 x 30; padding 0px 16px; background #051a6e `measured.nav-hover`; text futura-pt 14/30 600, #ffffff `color.neutral.white`.

![App strip default](components/crops/app-strip-default.png)

#### Header
The black bar: white wordmark, WOMEN/MEN tabs, search field, account, saved and bag icons. Read as `header` on the home page.

**Values (default).** size 1440 x 140; background transparent; text futura-pt 14/30 600, #ffffff `color.neutral.white`; icon 16 x 16, #2d2d2d `color.neutral.ink.900`; layers div.Fmy9ifd 0.0x0.0 rgb(255, 235, 204); div::before.AIkY9uF 18pxx18px; div.vcXJfPO.fVdHxMU 1440.0x30.0 rgb(248, 248, 248); a.eWFSkWC.ZHWKoMf 194.4x30.0 rgb(5, 26, 110); li 51.0x30.0 R:1px solid rgb(221, 221, 221) / L:1px solid rgb(221, 221, 221); div.R9mnQSo 1440.0x60.0 rgb(0, 0, 0).

Child layers that carry the look: div 0x0 background #ffebcc `color.orange.wash`; div::before 18pxx18px image url(data:…)'%3E %3Ctspan x='7.332' y='12'%3E!%3C/tspan%3E %3C/text%3E%3C/g%3E%3C/svg%3E"); div 1440x30 background #f8f8f8 `color.neutral.grey.100`.

![Header default](components/crops/header-default.png)

#### Logo
Read as `logo` on the home page.

**Values (default).** size 113 x 60; padding 0px 20px 0px 0px; background transparent; text futura-pt 14/14 400, #000000 `color.neutral.black`.

![Logo default](components/crops/logo-default.png)

#### Gender tab
WOMEN/MEN — the audience switch in the header. Read as `nav-tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 115 x 60; background #000000 `color.neutral.black`; text futura-pt 14/60 900, #ffffff `color.neutral.white` |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset -2px |

![Gender tab default](components/crops/nav-tab-default.png) ![Gender tab hover](components/crops/nav-tab-hover.png) ![Gender tab focus-visible](components/crops/nav-tab-focus-visible.png) ![Gender tab pressed](components/crops/nav-tab-pressed.png)

#### Category button
A button in the category nav row (New in, Clothing, Dresses…); each opens a flyout. Read as `nav-item` on the new-in shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 64.56 x 50; padding 0px 10px; background #000000 `color.neutral.black`; text futura-pt 14/50 400, #ffffff `color.neutral.white` |
| hover | background #051a6e `measured.nav-hover` |
| focus-visible | background #051a6e `measured.nav-hover`; outline 5px auto #005fcc `measured.focus-outline`, offset -2px |
| pressed | background #051a6e `measured.nav-hover` |

![Category button default](components/crops/nav-item-default.png) ![Category button hover](components/crops/nav-item-hover.png) ![Category button focus-visible](components/crops/nav-item-focus-visible.png) ![Category button pressed](components/crops/nav-item-pressed.png)

#### Category flyout, open
The nav button while its flyout is open. Read as `nav-mega` on the new-in shop grid page.

**Values (opened).** size 64.56 x 50; padding 0px 10px; background #051a6e `measured.nav-hover`; text futura-pt 14/50 400, #ffffff `color.neutral.white`.

![Category flyout, open opened](components/crops/nav-mega-opened.png)

#### Search field
The header search input; focused only, nothing typed. Read as `search-input` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 764 x 38; padding 0px 70px 0px 16px; radius 19px 50%; background #ffffff `color.neutral.white`; text futura-pt 16/16 400, #2d2d2d `color.neutral.ink.900`; placeholder #757575 |
| focused | outline 5px auto #005fcc `measured.focus-outline`, offset -2px |

![Search field default](components/crops/search-input-default.png) ![Search field focused](components/crops/search-input-focused.png)

#### Search button
The magnifier at the end of the search field. Measured, never pressed. Read as `search-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 38 x 38; padding 10px; border 1px solid transparent; radius 50%; background transparent; text futura-pt 14/14 400, #2d2d2d `color.neutral.ink.900`; transition background-color 0.3s ease; icon 16 x 16, #2d2d2d `color.neutral.ink.900` |

![Search button default](components/crops/search-button-default.png) ![Search button hover](components/crops/search-button-hover.png) ![Search button pressed](components/crops/search-button-pressed.png)

#### Account icon
Opens the My Account dropdown (Sign In / Join); measured, never opened. Read as `account-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 50 x 60; padding 12px 15px; background transparent; text futura-pt 0/60 400, #ffffff `color.neutral.white`; layers span.dejKRrj.c_IO2I_ 20.0x20.0 rgb(255, 255, 255) |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset -2px; layers button.KH34gk4.TYb4J9A 50.0x60.0; span.dejKRrj.c_IO2I_ 20.0x20.0 rgb(255, 255, 255) |

Child layers that carry the look: span 20x20 background #ffffff `color.neutral.white`.

![Account icon default](components/crops/account-icon-default.png) ![Account icon hover](components/crops/account-icon-hover.png) ![Account icon focus-visible](components/crops/account-icon-focus-visible.png) ![Account icon pressed](components/crops/account-icon-pressed.png)

#### Saved-lists icon
The heart. Measured, never followed. Read as `saved-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 50 x 60; padding 12px 15px; background transparent; text futura-pt 0/60 400, #ffffff `color.neutral.white`; layers span.vQeUV7s.c_IO2I_ 20.0x20.0 rgb(255, 255, 255) |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset -2px; layers a.KH34gk4.TYb4J9A 50.0x60.0; span.vQeUV7s.c_IO2I_ 20.0x20.0 rgb(255, 255, 255) |

Child layers that carry the look: span 20x20 background #ffffff `color.neutral.white`.

![Saved-lists icon default](components/crops/saved-icon-default.png) ![Saved-lists icon hover](components/crops/saved-icon-hover.png) ![Saved-lists icon focus-visible](components/crops/saved-icon-focus-visible.png) ![Saved-lists icon pressed](components/crops/saved-icon-pressed.png)

#### Bag icon
"Bag 0 items". Measured, never followed. Read as `bag-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 50 x 60; padding 12px 15px; background transparent; text futura-pt 0/60 400, #ffffff `color.neutral.white`; layers span.LpoEdV8.c_IO2I_ 20.0x20.0 rgb(255, 255, 255) |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset -2px; layers a.KH34gk4.TYb4J9A 50.0x60.0; span.LpoEdV8.c_IO2I_ 20.0x20.0 rgb(255, 255, 255) |

Child layers that carry the look: span 20x20 background #ffffff `color.neutral.white`.

![Bag icon default](components/crops/bag-icon-default.png) ![Bag icon hover](components/crops/bag-icon-hover.png) ![Bag icon focus-visible](components/crops/bag-icon-focus-visible.png) ![Bag icon pressed](components/crops/bag-icon-pressed.png)

#### Promo strip
The dark panel under the header carrying the new-customer offer and WOMEN/MEN toggle buttons. Read as `promo-strip` on the home page.

**Values (default).** size 1351 x 48; padding 0px 32px; background transparent; text Futura-pt 10.56/26 700, #ffffff `color.neutral.white`; layers a.Button-module_button__0sgpT 100.0x30.0 T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255); div.Tooltip-module_tooltip__f9BC8 720.0x72.0 rgb(242, 242, 242) rgba(105, 105, 105, 0.5) 3px 3px 0px 0px; div::before.Tooltip-module_tooltip__f9BC8 0pxx0px R:5px solid rgba(0, 0, 0, 0) / B:5px solid rgb(242, 242, 242) / L:5px so.

Child layers that carry the look: a 100x30 border 2px solid #ffffff `color.neutral.white`; div 720x72 background #f2f2f2 shadow rgba(105, 105, 105, 0.5) 3px 3px 0px 0px; div::before 0pxx0px border 5px solid transparent.

![Promo strip default](components/crops/promo-strip-default.png)

#### Promo strip tab
The bordered WOMEN/MEN buttons inside the promo strip. Read as `promo-tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 100 x 30; border 2px solid #ffffff `color.neutral.white`; background transparent; text Futura-pt 10.56/26 700, #ffffff `color.neutral.white`; transition opacity 0.8s ease |
| hover | opacity 0.563477 |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; opacity 0.992271 |
| pressed | opacity 0.593706 |

![Promo strip tab default](components/crops/promo-tab-default.png) ![Promo strip tab hover](components/crops/promo-tab-hover.png) ![Promo strip tab focus-visible](components/crops/promo-tab-focus-visible.png) ![Promo strip tab pressed](components/crops/promo-tab-pressed.png)

#### Country selector
"You're in Singapore Change" — a flag button in the top bar; opens the country picker, never pressed. Read as `country-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 49 x 30; padding 0px 17px; background transparent; text futura-pt 14/14 400, #000000 `color.neutral.black` |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset -2px; layers button.breiRmE.TYb4J9A 49.0x30.0 |

![Country selector default](components/crops/country-link-default.png) ![Country selector hover](components/crops/country-link-hover.png) ![Country selector focus-visible](components/crops/country-link-focus-visible.png) ![Country selector pressed](components/crops/country-link-pressed.png)

#### Help link
"Help & FAQs" in the top bar. Read as `help-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 114.2 x 30; padding 0px 19px; background transparent; text futura-pt 14/30 400, #666666 `color.neutral.grey.600` |
| hover | text futura-pt 14/30 400, #0770cf `color.blue.default` |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset -2px; text futura-pt 14/30 400, #0770cf `color.blue.default`; layers a.R2BDZ6J.TYb4J9A 114.2x30.0 |
| pressed | text futura-pt 14/30 400, #0770cf `color.blue.default` |

![Help link default](components/crops/help-link-default.png) ![Help link hover](components/crops/help-link-hover.png) ![Help link focus-visible](components/crops/help-link-focus-visible.png) ![Help link pressed](components/crops/help-link-pressed.png)

#### Category flyout panel
The open mega-menu panel itself, while the button is hovered. Read as `nav-flyout` on the new-in shop grid page.

**Values (default).** size 1302 x 399.1; padding 24px 10px; background #ffffff `color.neutral.white`; text futura-pt 14/20 700, #000000 `color.neutral.black`; transition min-height 0.2s ease-in-out.

![Category flyout panel default](components/crops/nav-flyout-default.png)

#### Flyout link
A link inside the open mega-menu ("View all", "New In: Today"…). Measured, never followed. Read as `flyout-link` on the new-in shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 68.38 x 28; padding 8px 5px 0px 5px; background transparent; text futura-pt 14/29.96 700, #666666 `color.neutral.grey.600` |
| hover | text futura-pt 14/29.96 700, #0770cf `color.blue.default` |

![Flyout link default](components/crops/flyout-link-default.png) ![Flyout link hover](components/crops/flyout-link-hover.png)

### Home

The hero, its SHOP WOMENS/MENS buttons and the marketing tiles below.

#### Hero CTA
The filled hero button ("SHOP WOMENS"). Measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 184 x 44; padding 9px 14px; border 2px solid #ffffff `color.neutral.white`; background #ffffff `color.neutral.white`; text futura-pt 16/21 700, #000000 `color.neutral.black`; transition background-color 0.4s ease, border-color 0.4s ease, color 0.4s ease-in-out |
| hover | border 2px solid #000000 `color.neutral.black`; background #000000 `color.neutral.black`; text futura-pt 16/21 700, #ffffff `color.neutral.white` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero CTA, alternate
Read as `hero-cta-alt` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 184 x 44; padding 9px 14px; border 2px solid #ffffff `color.neutral.white`; background #ffffff `color.neutral.white`; text futura-pt 16/21 700, #000000 `color.neutral.black`; transition background-color 0.4s ease, border-color 0.4s ease, color 0.4s ease-in-out |
| hover | border 2px solid #000000 `color.neutral.black`; background #000000 `color.neutral.black`; text futura-pt 16/21 700, #ffffff `color.neutral.white` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |

![Hero CTA, alternate default](components/crops/hero-cta-alt-default.png) ![Hero CTA, alternate hover](components/crops/hero-cta-alt-hover.png) ![Hero CTA, alternate focus-visible](components/crops/hero-cta-alt-focus-visible.png) ![Hero CTA, alternate pressed](components/crops/hero-cta-alt-pressed.png)

#### Content tile
A dark marketing tile lower on the home page ("NEW HERE?"…). Read as `grid-tile` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 345 x 213.73; background transparent; text futura-pt 0/0 400, #000000 `color.neutral.black` |

![Content tile default](components/crops/grid-tile-default.png) ![Content tile hover](components/crops/grid-tile-hover.png)

### Hub pages

The women's hub: promo banner, campaign hero and product rail.

#### Hub section title
"The latest drops" — the hub's visible section heading (the h1 is screen-reader only). Read as `hub-title` on the women's hub page.

**Values (default).** size 215.98 x 36; background transparent; text futura-pt 28/36 700, #000000 `color.neutral.black`.

![Hub section title default](components/crops/hub-title-default.png)

#### Hub hero tile
The "THE PARTY EDIT / SHOP NOW" campaign tile. Read as `hub-tile` on the women's hub page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1440 x 640; background transparent; text futura-pt 0/0 400, #000000 `color.neutral.black`; layers h2.hero-title__text.js-dynamicText 0.0x0.0 rgb(255, 255, 255) rgb(255, 255, 255) 10px 0px 0px 0px, rgb(255, 255, 255) -10px 0px 0px 0px, rgb(255, 255, 255) 10px 0px 0px 0px, rgb(255, 255, 255) -10px 0px 0px 0px, rgb(255, 255, 255) 10px 0px 0px 0px, rgb(255, 255, 255) -10px 0px 0px 0px, rgb(255, 255, 255) 10px 0px 0px 0px, rgb(255, 255, 255) -10px 0px 0px 0px; h2.hero-title__text 0.0x0.0 rgb(255, 2 |

Child layers that carry the look: h2 0x0 background #ffffff `color.neutral.white` shadow #ffffff `color.neutral.white` 10px 0px 0px 0px, #ffffff `color.neutral.white` -10px 0px 0px 0px, #ffffff `color.neutral.white` 10px 0px 0px 0px, #ffffff `color.neutral.white` -10px 0px 0px 0px, #ffffff `color.neutral.white` 10px 0px 0px 0px, #ffffff `color.neutral.white` -10px 0px 0px 0px, #ffffff `color.neutral.white` 10px 0px 0px 0px, #ffffff `color.neutral.white` -10px 0px 0px 0px; h2 0x0 background #ffffff `color.neutral.white` shadow #ffffff `color.neutral.white` 10px 0px 0px 0px, #ffffff `color.neutral.white` -10px 0px 0px 0px, #ffffff `color.neutral.white` 10px 0px 0px 0px, #ffffff `color.neutral.white` -10px 0px 0px 0px, #ffffff `color.neutral.white` 10px 0px 0px 0px, #ffffff `color.neutral.white` -10px 0px 0px 0px, #ffffff `color.neutral.white` 10px 0px 0px 0px, #ffffff `color.neutral.white` -10px 0px 0px 0px.

![Hub hero tile default](components/crops/hub-tile-default.png) ![Hub hero tile hover](components/crops/hub-tile-hover.png)

#### Hub promo banner
The dark "SINGLES' DAY — UP TO 40% OFF" banner under the header. Read as `hub-banner` on the women's hub page.

**Values (default).** size 446.69 x 152.78; padding 0px 16px; background transparent; text futura-pt 16/16 400, #ffffff `color.neutral.white`; layers mark 92.2x39.3 T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255).

Child layers that carry the look: mark 92.2x39.3 border 2px solid #ffffff `color.neutral.white`.

![Hub promo banner default](components/crops/hub-banner-default.png)

#### Hub rail card
A product card in the "latest drops" rail. Read as `hub-card` on the women's hub page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 446.69 x 152.78; background transparent; text futura-pt 16/16 400, #ffffff `color.neutral.white`; layers div.flexible-banner__background 1440.0x200.8 rgb(45, 45, 45); mark 92.2x39.3 T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) |

Child layers that carry the look: div 1440x200.8 background #2d2d2d `color.neutral.ink.900`; mark 92.2x39.3 border 2px solid #ffffff `color.neutral.white`.

![Hub rail card default](components/crops/hub-card-default.png) ![Hub rail card hover](components/crops/hub-card-hover.png)

### Shop grid

The new-in grid: breadcrumb, category pills, sort/filter, product tiles and load-more.

#### Breadcrumb
Home / Women / New In / New In: Clothing. Read as `breadcrumb` on the new-in shop grid page.

**Values (default).** size 1440 x 50; background transparent; text futura-pt 14/20 400, #2d2d2d `color.neutral.ink.900`.

![Breadcrumb default](components/crops/breadcrumb-default.png)

#### Collection title
"New In Clothing for Women" in Futura bold. Read as `plp-title` on the new-in shop grid page.

**Values (default).** size 344.69 x 30; background transparent; text futura-pt 24/30 700, #000000 `color.neutral.black`.

![Collection title default](components/crops/plp-title-default.png)

#### Category pill
A chip in the sub-category carousel ("New in: Today"…). Read as `cat-pill` on the new-in shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 125.87 x 36; padding 10px; border 1px solid #dddddd `color.neutral.grey.300`; background #ffffff `color.neutral.white`; text futura-pt 16/14 400, #2d2d2d `color.neutral.ink.900` |
| hover | border 1px solid #999999; background #f5f5f5 `measured.hover-wash` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | border 1px solid #999999; background #f5f5f5 `measured.hover-wash` |

![Category pill default](components/crops/cat-pill-default.png) ![Category pill hover](components/crops/cat-pill-hover.png) ![Category pill focus-visible](components/crops/cat-pill-focus-visible.png) ![Category pill pressed](components/crops/cat-pill-pressed.png)

#### Sort control
The grid sort trigger. Measured, never opened. Read as `sort-button` on the new-in shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 92 x 43; padding 7px; border 1px solid #dddddd `color.neutral.grey.300`; background transparent; text futura-pt 16/16 400, #000000 `color.neutral.black` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |

![Sort control default](components/crops/sort-button-default.png) ![Sort control hover](components/crops/sort-button-hover.png) ![Sort control focus-visible](components/crops/sort-button-focus-visible.png) ![Sort control pressed](components/crops/sort-button-pressed.png)

#### Filter button
Opens the filter panel; measured, never opened. Read as `filter-button` on the new-in shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 92 x 43; padding 7px; border 1px solid #dddddd `color.neutral.grey.300`; background transparent; text futura-pt 16/16 400, #000000 `color.neutral.black` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |

![Filter button default](components/crops/filter-button-default.png) ![Filter button hover](components/crops/filter-button-hover.png) ![Filter button focus-visible](components/crops/filter-button-focus-visible.png) ![Filter button pressed](components/crops/filter-button-pressed.png)

#### Styles count
"2,697 styles found". Read as `styles-count` on the new-in shop grid page.

**Values (default).** size 110.52 x 20; background transparent; text futura-pt 14/20 400, #666666 `color.neutral.grey.600`.

![Styles count default](components/crops/styles-count-default.png)

#### Product tile
A grid card: image, save heart, name, price, MORE COLOURS / SELLING FAST badges. Read as `product-tile` on the new-in shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 335 x 559.41; background transparent; text futura-pt 14/22 400, #2d2d2d `color.neutral.ink.900`; icon 19.99 x 17.77, #2d2d2d `color.neutral.ink.900`; layers div.badge_juy1n.productBadge_yGKk_ 106.0x20.0 rgba(255, 255, 255, 0.8) T:1px solid rgb(221, 221, 221) / R:1px solid rgb(221, 221, 221) / B:1px solid rgb(221, 221, 221) / L:1px solid rgb(221, 221, 221); div.badge_juy1n.sellingFastBadge_AHx_Z 91.9x20.0 rgb(102, 102, 102); span.container_p0yFn.icon_xgNGS 38.0x37.0 rgba(255, 255, 255, 0.8) T:4px solid rgba(0, 0, 0, 0) / R:4px solid rgba(0, 0, 0, 0) /  |

Child layers that carry the look: div 106x20 background rgba(255, 255, 255, 0.8) border 1px solid #dddddd `color.neutral.grey.300`; div 91.9x20 background #666666 `color.neutral.grey.600`; span 38x37 background rgba(255, 255, 255, 0.8) border 4px solid transparent radius 50%.

![Product tile default](components/crops/product-tile-default.png) ![Product tile hover](components/crops/product-tile-hover.png)

#### Product link
The whole-card link inside the tile: image, name and price. Read as `tile-name` on the new-in shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 335 x 559.41; background transparent; text futura-pt 14/22 400, #2d2d2d `color.neutral.ink.900`; layers div.badge_juy1n.productBadge_yGKk_ 106.0x20.0 rgba(255, 255, 255, 0.8) T:1px solid rgb(221, 221, 221) / R:1px solid rgb(221, 221, 221) / B:1px solid rgb(221, 221, 221) / L:1px solid rgb(221, 221, 221); div.badge_juy1n.sellingFastBadge_AHx_Z 91.9x20.0 rgb(102, 102, 102) |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a.productLink_KM4PI 335.0x559.4; div.badge_juy1n.productBadge_yGKk_ 106.0x20.0 rgba(255, 255, 255, 0.8) T:1px solid rgb(221, 221, 221) / R:1px solid rgb(221, 221, 221) / B:1px solid rgb(221, 221, 221) / L:1px solid rgb(221, 221, 221); div.badge_juy1n.sellingFastBadge_AHx_Z 91.9x20.0 rgb(102, 102, 102) |

Child layers that carry the look: div 106x20 background rgba(255, 255, 255, 0.8) border 1px solid #dddddd `color.neutral.grey.300`; div 91.9x20 background #666666 `color.neutral.grey.600`.

![Product link default](components/crops/tile-name-default.png) ![Product link hover](components/crops/tile-name-hover.png) ![Product link focus-visible](components/crops/tile-name-focus-visible.png) ![Product link pressed](components/crops/tile-name-pressed.png)

#### Tile price
SGD pricing on the geo-served surface. Read as `tile-price` on the new-in shop grid page.

**Values (default).** size 335 x 20; background transparent; text futura-pt 14/20 700, #2d2d2d `color.neutral.ink.900`.

![Tile price default](components/crops/tile-price-default.png)

#### Save heart
The heart on a product tile; a local save toggle, never pressed. Read as `save-heart` on the new-in shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 46 x 45; padding 4px; background transparent; text futura-pt 16/0 400, #000000 `color.neutral.black`; icon 19.99 x 17.77, #2d2d2d `color.neutral.ink.900`; layers span.container_p0yFn.icon_xgNGS 38.0x37.0 rgba(255, 255, 255, 0.8) T:4px solid rgba(0, 0, 0, 0) / R:4px solid rgba(0, 0, 0, 0) / B:4px solid rgba(0, 0, 0, 0) / L:4px solid rgba(0, 0, 0, 0) 50% |
| hover | layers span.container_p0yFn.icon_xgNGS 38.0x37.0 rgba(255, 255, 255, 0.8) T:4px solid rgba(0, 0, 0, 0) / R:4px solid rgba(0, 0, 0, 0) / B:4px solid rgba(0, 0, 0, 0) / L:4px solid rgba(0, 0, 0, 0) rgba(45, 45, 45, 0.14) 0px 2px 4px 0px 50% |
| focus-visible | layers span.container_p0yFn.icon_xgNGS 38.0x37.0 rgba(255, 255, 255, 0.8) T:4px solid rgb(45, 45, 45) / R:4px solid rgb(45, 45, 45) / B:4px solid rgb(45, 45, 45) / L:4px solid rgb(45, 45, 45) 50% |

Child layers that carry the look: span 38x37 background rgba(255, 255, 255, 0.8) border 4px solid transparent radius 50%.

![Save heart default](components/crops/save-heart-default.png) ![Save heart hover](components/crops/save-heart-hover.png) ![Save heart focus-visible](components/crops/save-heart-focus-visible.png) ![Save heart pressed](components/crops/save-heart-pressed.png)

#### Tile badge
SELLING FAST or MORE COLOURS — the small status text under a tile. Read as `tile-badge` on the new-in shop grid page.

**Values (default).** size 335 x 100; background transparent; text futura-pt 14/22 400, #2d2d2d `color.neutral.ink.900`; layers div.badge_juy1n.productBadge_yGKk_ 106.0x20.0 rgba(255, 255, 255, 0.8) T:1px solid rgb(221, 221, 221) / R:1px solid rgb(221, 221, 221) / B:1px solid rgb(221, 221, 221) / L:1px solid rgb(221, 221, 221); div.badge_juy1n.sellingFastBadge_AHx_Z 91.9x20.0 rgb(102, 102, 102).

Child layers that carry the look: div 106x20 background rgba(255, 255, 255, 0.8) border 1px solid #dddddd `color.neutral.grey.300`; div 91.9x20 background #666666 `color.neutral.grey.600`.

![Tile badge default](components/crops/tile-badge-default.png)

#### Load more
The grid pagination button. Measured, never pressed. Read as `load-more` on the new-in shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 300 x 54.5; padding 15px; border 2px solid #dddddd `color.neutral.grey.300`; background #ffffff `color.neutral.white`; text futura-pt 16/normal 900, #2d2d2d `color.neutral.ink.900` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | background #eeeeee `color.neutral.grey.200` |

![Load more default](components/crops/load-more-default.png) ![Load more hover](components/crops/load-more-hover.png) ![Load more focus-visible](components/crops/load-more-focus-visible.png) ![Load more pressed](components/crops/load-more-pressed.png)

### Product page

Title, price, rating, colour/size, the green buy button, accordions and reviews.

#### Product title
Read as `pdp-title` on the product page page.

**Values (default).** size 275.98 x 72; background transparent; text futura-pt 18/24 400, #2d2d2d `color.neutral.ink.900`.

![Product title default](components/crops/pdp-title-default.png)

#### Product price
Read as `pdp-price` on the product page page.

**Values (default).** size 299.98 x 28; background transparent; text futura-pt 16/16 400, #000000 `color.neutral.black`.

![Product price default](components/crops/pdp-price-default.png)

#### Star rating
The 3.8 (30) review stars under the price. Read as `rating` on the product page page.

**Values (default).** size 156.89 x 22.5; background transparent; text futura-pt 14/20 400, #2d2d2d `color.neutral.ink.900`.

![Star rating default](components/crops/rating-default.png)

#### Promo banner
The light-blue strip "Get 20% off! With code: WOW" between price and colour. Read as `promo-banner` on the product page page.

**Values (default).** size 299.98 x 44; background #cde2f5 `color.blue.wash`; text futura-pt 14/20 400, #2d2d2d `color.neutral.ink.900`.

![Promo banner default](components/crops/promo-banner-default.png)

#### Colour label
Read as `colour-label` on the product page page.

**Values (default).** size 299.98 x 22; background transparent; text futura-pt 12/16 700, #2d2d2d `color.neutral.ink.900`.

![Colour label default](components/crops/colour-label-default.png)

#### Fit Assistant link
"Find your Fit Assistant size" beside SIZE:. Measured, never pressed. Read as `fit-link` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 182.42 x 20; background transparent; text futura-pt 14/20 400, #2d2d2d `color.neutral.ink.900`; layers span.agHJy 18.0x18.0 rgb(6, 14, 137) 9px |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px; layers button.eJWsf 182.4x20.0; span.agHJy 18.0x18.0 rgb(6, 14, 137) 9px |

Child layers that carry the look: span 18x18 background #060e89 radius 9px.

![Fit Assistant link default](components/crops/fit-link-default.png) ![Fit Assistant link hover](components/crops/fit-link-hover.png) ![Fit Assistant link focus-visible](components/crops/fit-link-focus-visible.png) ![Fit Assistant link pressed](components/crops/fit-link-pressed.png)

#### Size select
The native "Please select" dropdown; a size was picked then restored, never submitted. Read as `size-select` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: picked) | size 299.98 x 38; padding 7px 29.9922px 7px 8px; border 1px solid #555555; background #ffffff `color.neutral.white`; image url(…); text futura-pt 16/22 400, #2d2d2d `color.neutral.ink.900` |
| focused | outline 3px auto #005fcc `measured.focus-outline`, offset 0px |

![Size select default](components/crops/size-select-default.png) ![Size select focused](components/crops/size-select-focused.png) ![Size select picked](components/crops/size-select-picked.png)

#### Add to bag
The green buy button; measured in every state except a real press. Read as `add-to-bag` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 243.98 x 44; padding 4px 0px; background #018849 `color.green.default`; text futura-pt 16/22 700, #ffffff `color.neutral.white` |
| hover | background #006637 `color.green.dark` |
| focus-visible | outline 3px auto #005fcc `measured.focus-outline`, offset 0px |
| pressed | background #006637 `color.green.dark` |

![Add to bag default](components/crops/add-to-bag-default.png) ![Add to bag hover](components/crops/add-to-bag-hover.png) ![Add to bag focus-visible](components/crops/add-to-bag-focus-visible.png) ![Add to bag pressed](components/crops/add-to-bag-pressed.png)

#### Save for later
The heart button beside Add to bag; a local save toggle, never pressed. Read as `save-button` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 44 x 44; padding 4px; radius 100px; background #eeeeee `color.neutral.grey.200`; text futura-pt 16/16 400, #000000 `color.neutral.black` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |

![Save for later default](components/crops/save-button-default.png) ![Save for later hover](components/crops/save-button-hover.png) ![Save for later focus-visible](components/crops/save-button-focus-visible.png) ![Save for later pressed](components/crops/save-button-pressed.png)

#### Delivery link
Read as `delivery-link` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 220.37 x 17.5; background transparent; text futura-pt 14/20 400, #2d2d2d `color.neutral.ink.900` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a 220.4x17.5 |

![Delivery link default](components/crops/delivery-link-default.png) ![Delivery link hover](components/crops/delivery-link-hover.png) ![Delivery link focus-visible](components/crops/delivery-link-focus-visible.png) ![Delivery link pressed](components/crops/delivery-link-pressed.png)

#### PDP accordion
A disclosure row (Size & Fit / Product Details / Brand). Read as `pdp-accordion` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 299.98 x 44; padding 14px 0px; background transparent; text futura-pt 14/16 700, #2d2d2d `color.neutral.ink.900` |
| focus-visible | outline 3px auto #005fcc `measured.focus-outline`, offset 0px; layers button.accordion-item-module_titleBtn__wIijl 300.0x44.0 |

![PDP accordion default](components/crops/pdp-accordion-default.png) ![PDP accordion hover](components/crops/pdp-accordion-hover.png) ![PDP accordion focus-visible](components/crops/pdp-accordion-focus-visible.png) ![PDP accordion pressed](components/crops/pdp-accordion-pressed.png)

#### PDP accordion, open
Read as `pdp-accordion-open` on the product page page.

**Values (opened).** size 299.98 x 44; padding 14px 0px; background transparent; outline 3px auto #005fcc `measured.focus-outline`, offset 0px; text futura-pt 14/16 700, #2d2d2d `color.neutral.ink.900`; layers button.accordion-item-module_titleBtn__wIijl 300.0x44.0.

Child layers that carry the look: button 300x44.

![PDP accordion, open opened](components/crops/pdp-accordion-open-opened.png)

#### Gallery chevron
The prev/next control on the product gallery. Measured, never pressed. Read as `gallery-chevron` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 66 x 65; padding 15px 16px 15px 29px; background transparent; text futura-pt 16/16 400, #000000 `color.neutral.black`; transform translate(0px, -32.5px) |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px; layers button.sKOc0.fQCRy 66.0x65.0 |

![Gallery chevron default](components/crops/gallery-chevron-default.png) ![Gallery chevron hover](components/crops/gallery-chevron-hover.png) ![Gallery chevron focus-visible](components/crops/gallery-chevron-focus-visible.png) ![Gallery chevron pressed](components/crops/gallery-chevron-pressed.png)

#### Reviews CTA
"VIEW ALL REVIEWS" — measured, never pressed. Read as `reviews-cta` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 359 x 44; padding 0px 16px; border 2px solid #dddddd `color.neutral.grey.300`; background #ffffff `color.neutral.white`; text futura-pt 16/18 700, #2d2d2d `color.neutral.ink.900` |
| hover | background #eeeeee `color.neutral.grey.200` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |
| pressed | background #eeeeee `color.neutral.grey.200` |

![Reviews CTA default](components/crops/reviews-cta-default.png) ![Reviews CTA hover](components/crops/reviews-cta-hover.png) ![Reviews CTA focus-visible](components/crops/reviews-cta-focus-visible.png) ![Reviews CTA pressed](components/crops/reviews-cta-pressed.png)

### Bag

The signed-out bag.

#### Bag title
"MY BAG". Read as `bag-title` on the bag page.

**Values (default).** size 362 x 66; padding 44px 0px 0px 0px; background transparent; image an image (data URI)%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cg%20id%3D%22M02B_empty_bag_signed_in%22%20transform%3D%22translate(0.000000%2C%20131.000000)%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%2; text futura-pt-n7 17.6/22 700, #2d2d2d `color.neutral.ink.900`.

![Bag title default](components/crops/bag-title-default.png)

#### Bag body
The signed-out bag with nothing in it. Read as `bag-empty` on the bag page.

**Values (default).** size 1440 x 455; background transparent; text futura-pt-n7 17.6/22 700, #2d2d2d `color.neutral.ink.900`; layers div.bag-contents-holder.bag-contents-holder-panel 1420.0x434.0 rgb(255, 255, 255); h1.empty-bag-title 362.0x66.0; button.main-button 288.0x44.0 rgb(1, 136, 73).

Child layers that carry the look: div 1420x434 background #ffffff `color.neutral.white`; h1 362x66 image url(data:…)%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cg%20id%3D%22M02B_empty_bag_signed_; button 288x44 background #018849 `color.green.default`.

![Bag body default](components/crops/bag-empty-default.png)

#### Bag CTA
Measured, never followed. Read as `bag-cta` on the bag page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 288 x 44; padding 15px; background #018849 `color.green.default`; text futura-pt-n7 14/14 700, #ffffff `color.neutral.white` |
| hover | background #006637 `color.green.dark` |
| focus-visible | background #006637 `color.green.dark`; outline 1px auto #005fcc `measured.focus-outline`, offset 0px |
| pressed | background #006637 `color.green.dark` |

![Bag CTA default](components/crops/bag-cta-default.png) ![Bag CTA hover](components/crops/bag-cta-hover.png) ![Bag CTA focus-visible](components/crops/bag-cta-focus-visible.png) ![Bag CTA pressed](components/crops/bag-cta-pressed.png)

### Saved lists

The signed-out saved-lists page.

#### Saved title
Read as `saved-title` on the saved lists page.

**Values (default).** size 221.35 x 24; background transparent; text futura-pt 18/24 700, #2d2d2d `color.neutral.ink.900`.

![Saved title default](components/crops/saved-title-default.png)

#### Saved body
Saved items is signed-out empty. Read as `saved-empty` on the saved lists page.

**Values (default).** size 1440 x 444; background transparent; text futura-pt 18/24 700, #2d2d2d `color.neutral.ink.900`; icon 24 x 24, #2d2d2d `color.neutral.ink.900`; layers button.button_g2MO4.noItemsButton_DY_8I 288.0x44.0 rgb(45, 45, 45).

Child layers that carry the look: button 288x44 background #2d2d2d `color.neutral.ink.900`.

![Saved body default](components/crops/saved-empty-default.png)

#### Saved CTA
Measured, never followed. Read as `saved-cta` on the saved lists page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 288 x 44; background #2d2d2d `color.neutral.ink.900`; text futura-pt 16/22 700, #ffffff `color.neutral.white` |
| hover | background #000000 `color.neutral.black` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |
| pressed | background #000000 `color.neutral.black` |

![Saved CTA default](components/crops/saved-cta-default.png) ![Saved CTA hover](components/crops/saved-cta-hover.png) ![Saved CTA focus-visible](components/crops/saved-cta-focus-visible.png) ![Saved CTA pressed](components/crops/saved-cta-pressed.png)

### Account gate

The my.asos.com identity gate; nothing was submitted.

#### Login title
"Hi friend!" Read as `login-title` on the account gate page.

**Values (default).** size 343 x 30; background transparent; text futura-pt 24/30 600, #2d2d2d `color.neutral.ink.900`.

![Login title default](components/crops/login-title-default.png)

#### Email field
Text was typed and deleted; the form was never submitted. Read as `email-input` on the account gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 343 x 44; padding 10px 8px 10px 16px; border 1px solid #767676 `color.neutral.grey.500`; background transparent; text futura-pt 16/22 400, #2d2d2d `color.neutral.ink.900`; placeholder #2d2d2d `color.neutral.ink.900` |
| focused, filled | outline 2px solid #0770cf `color.blue.default`, offset -2px |

![Email field default](components/crops/email-input-default.png) ![Email field focused](components/crops/email-input-focused.png) ![Email field filled](components/crops/email-input-filled.png)

#### Continue button
The submit; measured except a real press — the form was never submitted. Read as `continue-button` on the account gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 343 x 48; padding 8px 16px; background #2d2d2d `color.neutral.ink.900`; text futura-pt 16/18 600, #ffffff `color.neutral.white` |
| hover | background #000000 `color.neutral.black` |
| focus-visible | background #000000 `color.neutral.black`; outline 1px solid #0770cf `color.blue.default`, offset 3px |

![Continue button default](components/crops/continue-button-default.png) ![Continue button hover](components/crops/continue-button-hover.png) ![Continue button focus-visible](components/crops/continue-button-focus-visible.png)

#### Social sign-in button
Measured, never pressed. Read as `social-button` on the account gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 52 x 52; padding 8px 16px; border 2px solid #dddddd `color.neutral.grey.300`; background transparent; image url(…); text futura-pt 16/normal 400, #2d2d2d `color.neutral.ink.900` |
| focus-visible | outline 1px solid #0770cf `color.blue.default`, offset 3px |

![Social sign-in button default](components/crops/social-button-default.png) ![Social sign-in button hover](components/crops/social-button-hover.png) ![Social sign-in button focus-visible](components/crops/social-button-focus-visible.png) ![Social sign-in button pressed](components/crops/social-button-pressed.png)

### Footer

The page footer, social icons and newsletter field.

#### Footer
Read as `footer` on the home page.

**Values (default).** size 1440 x 723.5; background #000000 `color.neutral.black`; text futura-pt 14/16 700, #ffffff `color.neutral.white`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1440 x 48; padding 16px; background #051a6e `measured.nav-hover`; text futura-pt 14/16 700, #ffffff `color.neutral.white` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer social icon
Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 30 x 30; background transparent; text futura-pt 16/16 400, #000000 `color.neutral.black` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a.cYGKXSQ 30.0x30.0 |

![Footer social icon default](components/crops/footer-social-default.png) ![Footer social icon hover](components/crops/footer-social-hover.png) ![Footer social icon focus-visible](components/crops/footer-social-focus-visible.png) ![Footer social icon pressed](components/crops/footer-social-pressed.png)

#### Newsletter field
Focused only; never subscribed. Read as `newsletter-input` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 566.55 x 38.5; padding 9px 12px; background #ffffff `color.neutral.white`; text futura-pt 16/16 400, #2d2d2d `color.neutral.ink.900`; placeholder #757575 |
| focused | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |

![Newsletter field default](components/crops/newsletter-input-default.png) ![Newsletter field focused](components/crops/newsletter-input-focused.png)

### Mobile (390 wide)

The same surface at phone width, with the side-panel menu open.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 50; background transparent; text futura-pt 14/20 700, #ffffff `color.neutral.white`; layers div.Fmy9ifd 0.0x0.0 rgb(255, 235, 204); div::before.AIkY9uF 18pxx18px; div.R9mnQSo 390.0x50.0 rgb(0, 0, 0); span.BKBoO9a.TYb4J9A 20.0x20.0 rgb(255, 255, 255); div.jgxJaMT 390.0x884.0 rgba(45, 45, 45, 0.65); form.zel29Kx 0.0x0.0 rgb(238, 238, 238).

Child layers that carry the look: div 0x0 background #ffebcc `color.orange.wash`; div::before 18pxx18px image url(data:…)'%3E %3Ctspan x='7.332' y='12'%3E!%3C/tspan%3E %3C/text%3E%3C/g%3E%3C/svg%3E"); div 390x50 background #000000 `color.neutral.black`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 58 x 50; padding 0px 18px; background transparent; text futura-pt 14/14 400, #000000 `color.neutral.black`; layers span.BKBoO9a.TYb4J9A 20.0x20.0 rgb(255, 255, 255) |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px; layers button.btUA6FL 58.0x50.0; span.BKBoO9a.TYb4J9A 20.0x20.0 rgb(255, 255, 255) |

Child layers that carry the look: span 20x20 background #ffffff `color.neutral.white`.

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button hover](components/crops/m-menu-button-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The button after its own toggle; the open drawer shows in the crop. Read as `m-menu-open` on the home page at 390 wide.

**Values (opened).** size 58 x 50; padding 0px 18px; background transparent; text futura-pt 14/14 400, #000000 `color.neutral.black`; layers span.BKBoO9a.TYb4J9A 20.0x20.0 rgb(255, 255, 255).

Child layers that carry the look: span 20x20 background #ffffff `color.neutral.white`.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav link
A category row inside the opened side panel (NEW IN, CLOTHING…). Read as `m-nav-link` on the home page at 390 wide.

**Values (default).** size 288 x 96; background #eeeeee `color.neutral.grey.200`; image url(…); text futura-pt 16/18 900, #2d2d2d `color.neutral.ink.900`.

![Mobile nav link default](components/crops/m-nav-link-default.png)

#### Mobile floor tab
The WOMEN tab at the top of the open side panel. Read as `m-floor-tab` on the home page at 390 wide.

**Values (default).** size 160 x 49; background #000000 `color.neutral.black`; text futura-pt 14/50 900, #ffffff `color.neutral.white`.

![Mobile floor tab default](components/crops/m-floor-tab-default.png)

#### Mobile search icon
The magnifier that opens the search overlay (there is no inline field on mobile). Read as `m-search-icon` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 50 x 50; padding 12px 15px; background transparent; text futura-pt 0/50 400, #ffffff `color.neutral.white`; layers span.uszE8X4.c_IO2I_ 20.0x20.0 rgb(255, 255, 255) |
| focus-visible | outline 5px auto #005fcc `measured.focus-outline`, offset -2px; layers button.KH34gk4.TYb4J9A 50.0x50.0; span.uszE8X4.c_IO2I_ 20.0x20.0 rgb(255, 255, 255) |

Child layers that carry the look: span 20x20 background #ffffff `color.neutral.white`.

![Mobile search icon default](components/crops/m-search-icon-default.png) ![Mobile search icon hover](components/crops/m-search-icon-hover.png) ![Mobile search icon focus-visible](components/crops/m-search-icon-focus-visible.png) ![Mobile search icon pressed](components/crops/m-search-icon-pressed.png)

#### Mobile content tile
A dark marketing tile under the hero. Read as `m-feature-tile` on the home page at 390 wide.

**Values (default).** size 187 x 115.85; background transparent; text futura-pt 0/0 400, #000000 `color.neutral.black`.

![Mobile content tile default](components/crops/m-feature-tile-default.png)

### Other



## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are ASOS's artwork (inline SVG and Font Awesome). Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **Checkout and anything behind sign-in.** No item was added to the bag, so checkout, delivery options, payment and account pages were never reached. The `my.asos.com` identity gate itself is public and is measured; it was never submitted. The bag and saved-lists pages are public but empty for a signed-out visitor, and are recorded that way.
- **Anything that buys, sends or joins.** No product was added to the bag, no form was submitted (the login email was typed into and cleared), no search was run, no account was created, no consent choice was made.
- **The mega-menu columns, the account dropdown and the filter/sort panels** were opened or hovered but their innards were not measured beyond the first link.
- **The home page's category nav** stays `display:none` on `/` — it is measured on the shop grid, where the row is visible, and the home screenshot records the nav-less layout as served.
- **Headless access.** Akamai answers headless Chromium and headless Chrome with `403 Access Denied`; the whole capture ran in headed Chrome (channel `chrome`). That is a transport boundary, not a page one.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Keyboard focus on the header search button** did not land (recorded as an error state on `search-button`, not as evidence). Focus states on flyout links do not exist: the flyout closes the moment focus leaves the nav button.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The site paints one light theme on every captured route; a `.dark` probe resolves every custom property identically. The only themed sheets are vendor — OneTrust's `--ot-*` (consent UI) and Swiper's `--swiper-*` — recorded in [raw/css-vars.json](raw/css-vars.json) and never tokenised. No dark or reduced-contrast mode is offered.

### Fonts

- **Futura PT** (book 400, demi 500, bold 700, all italic) is ASOS's licensed face — every headline, nav item and button; the older **FuturaStd** (400/700) still loads on promo furniture. Neither is distributed; the style guide falls back to a system sans.
- Font Awesome and VideoJS faces ship inside widgets only.

### Screenshots

- Product photography, campaign imagery and the ASOS wordmark in the screenshots are ASOS's content. The PDP captured is whichever product the shop grid listed first at run time (recorded as `pdp_url` in components-computed.json); another run may land on a different product. Prices and the country banner are geo-served in Singapore (SGD).
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Product photography and campaign imagery are the product's content; only the frames and components were measured.
