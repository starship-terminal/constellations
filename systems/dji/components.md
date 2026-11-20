# DJI components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from dji.com's geo-locale /sg site on 2026-11-15, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought, booked or submitted; nav links, store CTAs, search fields and cards were measured, never followed or pressed. The product paints both section themes signed out — .light-theme on nav/listings/support and .dark-theme on hero, product and footer sections — so both themes are real painted evidence.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (32 components, 79 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (79 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{state}.png`; dark paint needs no forcing — the product scopes it to `.dark-theme` sections on the live pages. Desktop shots are 1440 x 900 at 1x; the phone surfaces are `mobile-{page}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/sg` | [default](screenshots/home-default.png), [full](screenshots/home-full.png) |
| Camera Drones | `/sg/camera-drones` | [default](screenshots/drones-default.png), [full](screenshots/drones-full.png) |
| Handheld | `/sg/handheld` | [default](screenshots/handheld-default.png), [full](screenshots/handheld-full.png) |
| Mavic 4 Pro | `/sg/mavic-4-pro` | [default](screenshots/product-default.png), [full](screenshots/product-full.png) |
| Support | `/sg/support` | [default](screenshots/support-default.png), [full](screenshots/support-full.png) |
| Company | `/sg/company` | [default](screenshots/company-default.png), [full](screenshots/company-full.png) |
| Where to Buy | `/sg/where-to-buy/online-stores` | [default](screenshots/stores-default.png), [full](screenshots/stores-full.png) |
| Home, phone | `/sg/mobile` | [default](screenshots/mobile-home-default.png), [full](screenshots/mobile-home-full.png) |
| Mavic 4 Pro, phone | `/sg/mavic-4-pro` | [default](screenshots/mobile-product-default.png), [full](screenshots/mobile-product-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Dark theme | hero, product, footer sections | the product scopes dark paint to sections carrying its own .dark-theme class — measured on the live surfaces, no forcing needed | [pd-buy](#atom-buy-button), [ft-link](#footer-link) |
| Store / checkout | Store buttons, Buy Now CTAs | measured at every paintable state, never followed — the store gates on a DJI account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 14 components were given a real keyboard focus. 11 draw an outline ring: `nv-mark` (1px auto #101010, offset 1px), `nv-item` (1px auto #101010, offset 1px), `nv-store` (2px dotted #ff0000, offset 1px), `nv-login` (1px auto #101010, offset 1px), `hm-learn` (1px auto #101010, offset 0.984375px), `hm-buy` (1px auto #101010, offset 1px), `ft-link` (1px auto #101010, offset 1px), `ct-subnav` (1px auto #101010, offset 1px), `m-cta` (1px auto #e59700, offset 1px), `m-tab` (1px auto #e59700, offset 1px), `m-menu` (1px auto #e59700, offset 1px). 2 change their fill: `pd-buy`, `pd-watch`. 1 change only their text colour: `st-link`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.3s | `ease` | all, background-color | ct-subnav, hm-buy, hm-learn, m-cta, m-tab, nv-item, nv-store, pd-buy and more |
| 0.6s | `ease-in-out` | all | ct-h1, hh-h1, pd-eyebrow, pd-h |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Product card](#product-card) | 696 x 600 | - | - | #f5f5f5 `color.background.1` | none | 0 |
| [Handheld card](#handheld-card) | 696 x 600 | - | - | #f5f5f5 `color.background.1` | none | 0 |
| [Support tile](#support-tile) | 325.33 x 120 | - | - | transparent | none | 0 |

## Components

### Site chrome

The top nav and footer: the DJI mark, the Camera Drones / Handheld / Lifestyle Tech / Specialized / Explore / Support / Where to Buy menus, the locale picker, Login/Register and the Store button. The home page paints the legacy dui-navbar; category and product pages paint the newer siteHeader module.

#### Site header
The top nav — DJI mark, product menus, ecosystem links, Login/Register, Store (the home page paints the legacy dui-navbar; category and product pages paint the newer siteHeader module). Read as `nv-bar` on the home page.

**Values (default).** size 1440 x 64; background transparent; text Open Sans 14/14 400, #ffffff `color.background.0`; layers span.navbar-brand-logo 45.0x26.0; div.dui-dropdown-menu 1230.0x0.0 #ffffff `color.background.0` rgba(0, 0, 0, 0.1) 0px 16px 16px 0px; div.dui-dropdown-menu 1230.0x0.0 #ffffff `color.background.0` rgba(0, 0, 0, 0.1) 0px 16px 16px 0px; div.dui-dropdown-menu 1230.0x0.0 #ffffff `color.background.0` rgba(0, 0, 0, 0.1) 0px 16px 16px 0px; ul 132.4x96.0 #ffffff `color.background.0` rgba(0, 0, 0, 0.1) 0px .

Child layers that carry the look: span 45x26 image url(data:…); div 1230x0 background #ffffff `color.background.0` shadow rgba(0, 0, 0, 0.1) 0px 16px 16px 0px; div 1230x0 background #ffffff `color.background.0` shadow rgba(0, 0, 0, 0.1) 0px 16px 16px 0px.

![Site header default](components/crops/nv-bar-default.png)

#### DJI mark
The DJI logo link in the header; measured, never followed. Read as `nv-mark` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 93 x 64; padding 19px 48px 19px 0px; background transparent; text Open Sans 16/normal 400, #0000ee; layers span.navbar-brand-logo 45.0x26.0 |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.navbar-brand.ga-data 93.0x64.0 1px auto #101010 offset 1px; span.navbar-brand-logo 45.0x26.0 |
| pressed | text Open Sans 16/normal 400, #ff0000 |

Child layers that carry the look: span 45x26 image url(data:…).

![DJI mark default](components/crops/nv-mark-default.png) ![DJI mark hover](components/crops/nv-mark-hover.png) ![DJI mark focus-visible](components/crops/nv-mark-focus-visible.png) ![DJI mark pressed](components/crops/nv-mark-pressed.png)

#### Nav menu item
A product menu link (Camera Drones) that opens the mega-menu; hover measured, menu opened via toggle below. Read as `nv-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 100.38 x 64; background transparent; text Open Sans 14/14 400, #ffffff `color.bg.7`; transition all 0.3s ease; layers ::after transparent 0px none 0 |
| hover | text Open Sans 14/14 400, rgba(255, 255, 255, 0.65) `color.white.7`; layers ::after transparent 0px none 1 |
| focus-visible | outline 1px auto #101010, offset 1px; layers ::after transparent 0px none 0; a.nav-item-title.ga-data 100.4x64.0 1px auto #101010 offset 1px |
| pressed | text Open Sans 14/14 400, rgba(255, 255, 255, 0.65) `color.white.7` |

![Nav menu item default](components/crops/nv-item-default.png) ![Nav menu item hover](components/crops/nv-item-hover.png) ![Nav menu item focus-visible](components/crops/nv-item-focus-visible.png) ![Nav menu item pressed](components/crops/nv-item-pressed.png)

#### Store button
The "Store" nav button linking to store.dji.com; measured, never followed — the store gates on a DJI account. Read as `nv-store` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 83.61 x 32; padding 8px 16px 8px 34px; radius 1408px; background #0070d5 `color.brand.6`; image an image (data URI); text Open Sans 14/14 400, #ffffff `color.background.0`; transition background-color 0.3s ease |
| hover | background #2490e3 `action.primary-hover` |
| focus-visible | shadow #1890ff 0px 0px 0px 3px; outline 2px dotted #ff0000, offset 1px |
| pressed | background #0058b0 `action.primary-pressed` |

![Store button default](components/crops/nv-store-default.png) ![Store button hover](components/crops/nv-store-hover.png) ![Store button focus-visible](components/crops/nv-store-focus-visible.png) ![Store button pressed](components/crops/nv-store-pressed.png)

#### Login link
The Login link in the header; measured, never followed — it redirects to the DJI account. Read as `nv-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 110 x 44; padding 16px 32px; background transparent; text Open Sans 12/12 400, #303233 `text.nav-ink` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.login-link.ga-data 110.0x44.0 1px auto #101010 offset 1px |

![Login link default](components/crops/nv-login-default.png) ![Login link hover](components/crops/nv-login-hover.png) ![Login link focus-visible](components/crops/nv-login-focus-visible.png) ![Login link pressed](components/crops/nv-login-pressed.png)

#### Site footer
The DJI sitemap footer — product/support/company columns and locale links. Read as `ft-bar` on the home page.

**Values (default).** size 1440 x 833; padding 32px 0px; background #272727 `surface.footer`; text Open Sans 18/24 600, #ffffff `color.bg.7`.

![Site footer default](components/crops/ft-bar-default.png)

#### Footer link
A footer column link; hover measured, never followed. Read as `ft-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 161 x 17; background transparent; text Open Sans 12/16 400, rgba(255, 255, 255, 0.85) `text.muted` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.ga-data 161.0x17.0 1px auto #101010 offset 1px |
| pressed | text Open Sans 12/16 400, #ffffff `color.bg.7` |

![Footer link default](components/crops/ft-link-default.png) ![Footer link hover](components/crops/ft-link-hover.png) ![Footer link focus-visible](components/crops/ft-link-focus-visible.png) ![Footer link pressed](components/crops/ft-link-pressed.png)

### Home hero

The 800px hero panels: product art over a .dark-theme section with the Learn More / Buy Now ghost CTAs.

#### Hero panel
A home hero panel — product art over a dark or light backdrop with the CTA row. Read as `hm-slide` on the home page.

**Values (default).** size 1440 x 800; padding 112px 0px 0px 0px; background #ededed; image image-set(url(…) 1dppx, url(…) 2dppx); text Open Sans 16/20 400, rgba(255, 255, 255, 0.65) `color.white.7`.

![Hero panel default](components/crops/hm-slide-default.png)

#### Learn More CTA
The hero "Learn More" link to the product page; measured, never followed. Read as `hm-learn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 133 x 32; padding 5px 16px; border 1px solid #ffffff `color.background.0`; radius 64px; background transparent; text Open Sans 14/20 400, #ffffff `color.background.0`; transition all 0.3s ease |
| focus-visible | outline 1px auto #101010, offset 0.984375px |
| pressed | background rgba(255, 255, 255, 0.09) |

![Learn More CTA default](components/crops/hm-learn-default.png) ![Learn More CTA hover](components/crops/hm-learn-hover.png) ![Learn More CTA focus-visible](components/crops/hm-learn-focus-visible.png) ![Learn More CTA pressed](components/crops/hm-learn-pressed.png)

#### Buy Now CTA
The hero "Buy Now" CTA linking to the store; measured, never followed — checkout gates on a DJI account. Read as `hm-buy` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 115 x 32; padding 5px 16px; border 1px solid #ffffff `color.background.0`; radius 64px; background transparent; text Open Sans 14/20 400, #ffffff `color.background.0`; transition all 0.3s ease |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background rgba(255, 255, 255, 0.09) |

![Buy Now CTA default](components/crops/hm-buy-default.png) ![Buy Now CTA focus-visible](components/crops/hm-buy-focus-visible.png) ![Buy Now CTA pressed](components/crops/hm-buy-pressed.png)

### Product cards

The atom-design hero-vertical-cards on the category grids: product art, tagline and model name.

#### Product card
A 2-up atom-design hero-vertical-card on the category grid — product art, tagline and name (the page's H1 banner and full-width series intro share the class, so the filter anchors on a DJI product name); hover measured, never followed. Read as `ct-card` on the camera drones page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 696 x 600; background #f5f5f5 `color.background.1`; image url(…); text Open Sans 12/16 400, #be4e04 `color.orange.6` |

![Product card default](components/crops/ct-card-default.png) ![Product card hover](components/crops/ct-card-hover.png)

#### Handheld card
A 2-up handheld product card (atom hero-vertical-card; the full-width Osmo Pocket hero shares the class, so the filter anchors on a grid product name); hover measured, never followed. Read as `hh-card` on the handheld page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 696 x 600; background #f5f5f5 `color.background.1`; image url(…); text Open Sans 12/16 400, #be4e04 `color.orange.6` |

![Handheld card default](components/crops/hh-card-default.png) ![Handheld card hover](components/crops/hh-card-hover.png)

### Category page

The category listings (/camera-drones, /handheld): display headings, sub-nav and product-card rows.

#### Category heading
The "Camera Drones" listing heading. Read as `ct-h1` on the camera drones page.

**Values (default).** size 693 x 52; background transparent; text Open Sans 48/52 600, rgba(0, 0, 0, 0.85) `color.black.8`; transition all 0.6s ease-in-out.

![Category heading default](components/crops/ct-h1-default.png)

#### Sub-nav Store button
The "Store"/"Buy Now" button pinned in the page sub-nav; measured, never followed. Read as `ct-subnav` on the camera drones page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 83.61 x 32; padding 8px 16px 8px 34px; radius 1408px; background #0070d5 `color.brand.6`; image an image (data URI); text Open Sans 14/14 400, #ffffff `color.background.0`; transition background-color 0.3s ease |
| hover | background #2490e3 `action.primary-hover` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #0058b0 `action.primary-pressed` |

![Sub-nav Store button default](components/crops/ct-subnav-default.png) ![Sub-nav Store button hover](components/crops/ct-subnav-hover.png) ![Sub-nav Store button focus-visible](components/crops/ct-subnav-focus-visible.png) ![Sub-nav Store button pressed](components/crops/ct-subnav-pressed.png)

#### Handheld heading
The handheld category heading (Osmo action cameras, gimbals, mics). Read as `hh-h1` on the handheld page.

**Values (default).** size 693 x 48; background transparent; text Open Sans 40/48 600, rgba(0, 0, 0, 0.85) `color.black.8`; transition all 0.6s ease-in-out.

![Handheld heading default](components/crops/hh-h1-default.png)

### Product page

The /mavic-4-pro surface: the sticky sub-nav, atom-design Buy Now and Watch Video buttons, eyebrow headings and spec lines — measured, never pressed (purchase gates on the store account).

#### Product sub-nav
The product page sticky sub-nav — section links and the Buy Now button. Read as `pd-subnav` on the product page page.

**Values (default).** size 1440 x 64; background transparent; text Open Sans 14/64 400, #ffffff `color.background.0`; layers nav.style__sub-nav___AjIC_ 1440.0x64.0 rgba(35, 37, 38, 0.9); a.style__sub-nav-btn___fguHS 91.0x30.0 #0070d5 `color.brand.6` 2px; div.popover__flex-box___14szQ 320.0x88.0 #ffffff `color.background.0` 4px; div.popover__cover-image___1yWkS 40.0x40.0 #f5f5f5 `color.background.1` 99px; div.popover__close___1jBk4 32.0x32.0 99px; div.popover__arrow___29rRa 22.0x12.0 R:11px solid transparent / B:12px sol.

Child layers that carry the look: nav 1440x64 background rgba(35, 37, 38, 0.9); a 91x30 background #0070d5 `color.brand.6` radius 2px; div 320x88 background #ffffff `color.background.0` radius 4px.

![Product sub-nav default](components/crops/pd-subnav-default.png)

#### Atom Buy button
The atom-design-v1 primary "Buy Now" button (dji-btn-lg); states measured, never pressed — purchase gates on the store account. Read as `pd-buy` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 144 x 40; padding 0px 16px; radius 60px; background #ffffff `color.bg.7`; text Open Sans 16/20 400, rgba(0, 0, 0, 0.85) `color.black.8`; transition all 0.3s ease |
| hover, focus-visible | background rgba(255, 255, 255, 0.9) `action.cta-hover` |
| pressed | background rgba(255, 255, 255, 0.8) `action.cta-pressed` |

![Atom Buy button default](components/crops/pd-buy-default.png) ![Atom Buy button hover](components/crops/pd-buy-hover.png) ![Atom Buy button focus-visible](components/crops/pd-buy-focus-visible.png) ![Atom Buy button pressed](components/crops/pd-buy-pressed.png)

#### Atom ghost button
The secondary "Watch Video" atom button; states measured, never pressed. Read as `pd-watch` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 147.48 x 40; padding 0px 15px; border 1px solid #ffffff `color.bg.7`; radius 60px; background transparent; text Open Sans 16/20 400, #ffffff `color.bg.7`; transition all 0.3s ease |
| hover, focus-visible | background rgba(255, 255, 255, 0.09) `action.ghost-hover` |
| pressed | background rgba(255, 255, 255, 0.15) `action.ghost-pressed` |

![Atom ghost button default](components/crops/pd-watch-default.png) ![Atom ghost button hover](components/crops/pd-watch-hover.png) ![Atom ghost button focus-visible](components/crops/pd-watch-focus-visible.png) ![Atom ghost button pressed](components/crops/pd-watch-pressed.png)

#### Eyebrow heading
A section eyebrow line (e.g. "Triple-Camera Imaging System") using the text-ms-24 size utility. Read as `pd-eyebrow` on the product page page.

**Values (default).** size 693 x 52; background transparent; text Open Sans 20/52 600, rgba(255, 255, 255, 0.85); transition all 0.6s ease-in-out.

![Eyebrow heading default](components/crops/pd-eyebrow-default.png)

#### Product heading
A product page display heading. Read as `pd-h` on the product page page.

**Values (default).** size 693 x 32; background transparent; text Open Sans 24/32 600, #ffffff `color.bg.7`; transition all 0.6s ease-in-out.

![Product heading default](components/crops/pd-h-default.png)

#### Spec line
A spec value line on the product page. Read as `pd-spec` on the product page page.

**Values (default).** size 895.02 x 55; background transparent; image linear-gradient(90deg, #f68128 0%, #ffae66 52%, #f68128 100%); text Open Sans 20/28 600, transparent.

![Spec line default](components/crops/pd-spec-default.png)

### Support / company

The /support portal (search field, category tiles), /company and /where-to-buy/online-stores (store-type links).

#### Support heading
The support portal heading. Read as `sp-h1` on the support page.

**Values (default).** size 1200 x 56; background transparent; text Open Sans 48/56 500, #ffffff `color.background.0`.

![Support heading default](components/crops/sp-h1-default.png)

#### Support tile
A support category tile (repairs, service, downloads); hover measured, never followed. Read as `sp-card` on the support page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 325.33 x 120; background transparent; text Open Sans 20/24 600, rgba(0, 0, 0, 0.85) `color.black.8` |

![Support tile default](components/crops/sp-card-default.png) ![Support tile hover](components/crops/sp-card-hover.png)

#### Support search
The support search field; focus/fill measured, never submitted. Read as `sp-search` on the support page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 640 x 32; padding 4px 8px; background #ffffff `color.background.0`; text Open Sans 16/normal 400, #303233 `text.nav-ink`; placeholder #757575 |

![Support search default](components/crops/sp-search-default.png) ![Support search focused](components/crops/sp-search-focused.png) ![Support search filled](components/crops/sp-search-filled.png)

#### About DJI nav heading
The "About DJI" section heading in the company sidebar nav — the page paints its hero as image, so this named link is its display text. Read as `co-h1` on the company page.

**Values (default).** size 61 x 19; background transparent; text Open Sans 14/20 400, #707473.

![About DJI nav heading default](components/crops/co-h1-default.png)

#### Company lede
The first body paragraph on the company page. Read as `co-lede` on the company page.

**Values (default).** size 395 x 48; background transparent; text Open Sans 16/24 400, rgba(0, 0, 0, 0.65) `color.black.7`.

![Company lede default](components/crops/co-lede-default.png)

#### Where to Buy heading
The where-to-buy page heading. Read as `st-h1` on the where to buy page.

**Values (default).** size 1200 x 76.19; padding 24px 0px 16px 0px; border B: 1px solid #f0f1f2; background transparent; text Open Sans 32/35.2 600, #3b3e40; layers h1.bread-title 1200.0x76.2 B:1px solid #f0f1f2.

Child layers that carry the look: h1 1200x76.2 border 1px solid #f0f1f2.

![Where to Buy heading default](components/crops/st-h1-default.png)

#### Store-type link
A store-type link (Flagship Stores); measured, never followed. Read as `st-link` on the where to buy page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 126 x 40; padding 8px 16px; background transparent; text Open Sans 16/24 400, rgba(0, 0, 0, 0.65) `color.black.7` |
| hover, focus-visible, pressed | text Open Sans 16/24 400, rgba(0, 0, 0, 0.85) `color.black.8` |

![Store-type link default](components/crops/st-link-default.png) ![Store-type link hover](components/crops/st-link-hover.png) ![Store-type link focus-visible](components/crops/st-link-focus-visible.png) ![Store-type link pressed](components/crops/st-link-pressed.png)

### Mobile (390 wide)

The phone surface at 390 wide — the separate /sg/mobile site: dui-navbar-m nav, category tabs and hero CTAs.

#### Mobile header
The phone header at 390px — mark and menu affordance. Read as `m-bar` on the mobile home page at 390 wide.

**Values (default).** size 390 x 50; background transparent; text Open Sans 14/20 400, rgba(0, 0, 0, 0.85) `color.black.8`; layers span::before.control-icon 22pxx2px #ffffff `color.background.0` 0px 2px; span::before.control-icon 22pxx2px #ffffff `color.background.0` 0px 2px; span::before.control-icon 22pxx2px #ffffff `color.background.0` 0px 2px; i.search-trigger 28.0x28.0; a.navbar-shopingbag.ga-data 32.0x32.0 1408px; a.navbar-shopingbag.active 0.0x0.0 1408px.

Child layers that carry the look: span::before 22pxx2px background #ffffff `color.background.0` radius 0px 2px; span::before 22pxx2px background #ffffff `color.background.0` radius 0px 2px; span::before 22pxx2px background #ffffff `color.background.0` radius 0px 2px.

![Mobile header default](components/crops/m-bar-default.png)

#### Mobile CTA
A hero CTA at 390px; measured, never followed. Read as `m-cta` on the mobile home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 133 x 32; padding 5px 16px; border 1px solid #ffffff `color.background.0`; radius 60px; background transparent; text Open Sans 14/20 400, #ffffff `color.background.0`; transition all 0.3s ease |
| focus-visible | outline 1px auto #e59700, offset 1px |
| pressed | background rgba(255, 255, 255, 0.15) |

![Mobile CTA default](components/crops/m-cta-default.png) ![Mobile CTA hover](components/crops/m-cta-hover.png) ![Mobile CTA focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile CTA pressed](components/crops/m-cta-pressed.png)

#### Mobile nav tab
A category tab in the mobile nav row (the phone UA is redirected to the separate /sg/mobile site); measured, never followed. Read as `m-tab` on the mobile home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 354 x 20; padding 0px 32px 0px 0px; background transparent; text Open Sans 14/20 400, rgba(0, 0, 0, 0.85) `color.black.8`; transition all 0.3s ease |
| focus-visible | outline 1px auto #e59700, offset 1px; layers a.ga-data.title 354.0x20.0 1px auto #e59700 offset 1px |

![Mobile nav tab hover](components/crops/m-tab-hover.png) ![Mobile nav tab focus-visible](components/crops/m-tab-focus-visible.png) ![Mobile nav tab pressed](components/crops/m-tab-pressed.png)

#### Mobile menu button
The hamburger control in the /sg/mobile navbar; measured, never toggled open. Read as `m-menu` on the mobile home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 54 x 50; padding 13px 16px; background transparent; text Open Sans 16/normal 400, #0000ee; layers span::before.control-icon 22pxx2px #ffffff `color.background.0` 0px 2px; span::before.control-icon 22pxx2px #ffffff `color.background.0` 0px 2px; span::before.control-icon 22pxx2px #ffffff `color.background.0` 0px 2px |
| focus-visible | outline 1px auto #e59700, offset 1px; layers a.navbar-control 54.0x50.0 1px auto #e59700 offset 1px; span::before.control-icon 22pxx2px #ffffff `color.background.0` 0px 2px; span::before.control-icon 22pxx2px #ffffff `color.background.0` 0px 2px; span::before.control-icon 22pxx2px #ffffff `color.background.0` 0px 2px |
| pressed | text Open Sans 16/normal 400, #ff0000 |

Child layers that carry the look: span::before 22pxx2px background #ffffff `color.background.0` radius 0px 2px; span::before 22pxx2px background #ffffff `color.background.0` radius 0px 2px; span::before 22pxx2px background #ffffff `color.background.0` radius 0px 2px.

![Mobile menu button default](components/crops/m-menu-default.png) ![Mobile menu button hover](components/crops/m-menu-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the DJI wordmark, menu glyphs, search/account icons and footer marks) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Purchase and account need the DJI account — the Store and Buy Now CTAs lead to store.dji.com sign-in and checkout, which were never opened; Login/Register redirect to the member service. What is genuinely public signed out: the home hero (/sg), the category pages (/camera-drones, /handheld), product pages (/mavic-4-pro) with specs and CTAs, /support, /company and /where-to-buy/*. The Buy/Store buttons were measured, never pressed.

### Pages

- **Store, Login and Register actions.** The Store/Buy Now CTAs and the member-service redirects gate on a DJI account; they were measured at default/hover/focus-visible/pressed, never followed.
- **Mega-menu panels.** The nav product menus open hover panels that were hovered but not walked item-by-item; the panel links' own states are unmeasured.
- **App-download banner.** A top banner painted on load; it was left in the captures.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

There is no theme toggle and no root-level dark sheet: the product scopes themes to sections — :root .light-theme and :root .dark-theme re-declare the semantic roles, and sections opt in by class. Both paint signed out (nav/listings/support light; hero/product/footer dark), so light.* and dark.* are both measured paint. A full-page dark repaint does not exist — dark is per-section by design.

### Fonts

- **Open Sans** (the UI face — every UI string) with PingFang SC / Microsoft YaHei CJK fallbacks, and **Dji** (the icon face) are the served families, read from the @font-face declarations in the served sheets; the style guide falls back to system fonts.

### Screenshots

- Full-page shots are single document captures; the marketing pages' animated hero fields are motion media, frozen at capture time.
- Product names, taglines, imagery and prices are the site's published content; screenshots are 256-colour PNGs, read exact colours from the tokens or the raw files.

### Content left out

- Product names, taglines, imagery and prices are the site's published content; only frames and components were measured.
