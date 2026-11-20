# DoorDash components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from www.doordash.com pages rendered from Internet Archive snapshots on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page — archival evidence: every live *.doordash.com route Cloudflare-blocked this client, so each page is the product's own SSR HTML and CSS proxied by the Wayback Machine (routes and snapshot ids in [raw/archive-urls.json](raw/archive-urls.json)). The consumer stack is consumer-web-next (Next.js SSR, styled-components) over the prism design-token system (:where(.prism-theme): --base-*, --usage-*, --comp-*); careers is a separate WordPress/Tailwind stack. Nothing was signed into, ordered, address-entered or submitted; the address-gate field was focused once for measurement and never filled; consent and Turnstile elements were hidden, never answered.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (74 components, 171 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (165 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-state.png`: every captured surface paints `light` — no dark theme is published on these pages. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). The Wayback Machine's replay toolbar is hidden in every shot.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/ (wayback 2026-11-12)` | [cuisines](screenshots/home-light-cuisines.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Food delivery directory | `/food-delivery/ (wayback 2026-10-04)` | [default](screenshots/food-delivery-light-default.png), [full](screenshots/food-delivery-light-full.png) |
| DoorDash for Business | `/en-US/business/ (wayback 2026-10-12)` | [default](screenshots/business-light-default.png), [full](screenshots/business-light-full.png) |
| DashPass student | `/en-US/dashpass/student (wayback 2026-10-12)` | [default](screenshots/dashpass-light-default.png), [full](screenshots/dashpass-light-full.png) |
| Restaurants near me | `/en-US/restaurants-near-me/ (wayback 2026-10-05)` | [default](screenshots/restaurants-light-default.png), [full](screenshots/restaurants-light-full.png) |
| Restaurant storefront | `/en-US/store/the-sweet-tooth-north-miami-beach-33434247/ (wayback 2026-10-24)` | [default](screenshots/store-light-default.png), [full](screenshots/store-light-full.png), [pickup](screenshots/store-light-pickup.png) |
| HSA/FSA store | `/en-US/p/hsa-fsa-store (wayback 2026-09-30)` | [default](screenshots/hsa-light-default.png), [full](screenshots/hsa-light-full.png) |
| Seasonal campaign | `/en-US/p/seasonal-holidays/ (wayback 2026-10-25)` | [default](screenshots/seasonal-light-default.png), [full](screenshots/seasonal-light-full.png) |
| Promo codes | `/en-US/promos/ (wayback 2026-10-08)` | [default](screenshots/promos-light-default.png), [full](screenshots/promos-light-full.png) |
| Careers | `careersatdoordash.com (wayback 2026-10-09)` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| Home, phone | `/ (wayback 2026-11-12)` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Storefront, phone | `/en-US/store/… (wayback 2026-10-24)` | [default](screenshots/mobile-store-light-default.png), [full](screenshots/mobile-store-light-full.png), [menu](screenshots/mobile-store-light-menu.png) |
| Food delivery, phone | `/food-delivery/ (wayback 2026-10-04)` | [default](screenshots/mobile-food-delivery-light-default.png), [full](screenshots/mobile-food-delivery-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Wayback Machine toolbar | every page | hidden on every shot — archive chrome is not the product | never visible in committed evidence |
| Cookie banner | storefront + directory pages | un-hidden for one computed-style reading, then re-hidden — never answered | [cookie-banner](#cookie-banner) values only |
| Cloudflare Turnstile nodes | every consumer page | dormant testids hidden, never answered | hidden before every shot and reading |
| Directory tabs | home | the Top Cuisines tab's own toggle — a local reveal | [home-light-cuisines](screenshots/home-light-cuisines.png) |
| Delivery/Pickup toggle | storefront | the Pickup option's own toggle — local UI state | [store-light-pickup](screenshots/store-light-pickup.png) |
| Address gate | home, promos, storefront | the field was focused for measurement; nothing typed, never submitted — the gate stays closed | boundary; see Gaps |
| Signed-in product | consumer app, ordering, cart, checkout | every Sign-in / Sign-up / cart / quick-add action measured, never followed | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 27 components were given a real keyboard focus. 25 draw an outline ring: `signin-btn` (1px auto #005fcc, offset 1px), `signup-btn` (1px auto #005fcc, offset 1px), `address-pill` (1px auto #005fcc, offset 0px), `location-pill` (1px auto #005fcc, offset 0px), `cta-btn` (1px auto #005fcc, offset 1px), `dir-link` (1px auto #005fcc, offset 1px), `show-more` (on a child: 1px auto rgb(0, 95, 204) offset 0px), `cross-link` (1px auto #005fcc, offset 1px), `address-btn` (1px auto #005fcc, offset 0px), `cart-btn` (1px auto #005fcc, offset 0px), `dp-cta` (1px auto #005fcc, offset 0px), `popular-btn` (1px auto #005fcc, offset 0px), `nearby-cta` (1px auto #005fcc, offset 0px), `pagination` (on a child: 1px auto rgb(0, 95, 204) offset 0px), `internal-link` (1px auto #005fcc, offset 1px), `fulfil-toggle` (1px auto #005fcc, offset 0px), `quick-add` (1px auto #005fcc, offset 0px), `hsa-toggle` (on a child: 1px auto rgb(0, 95, 204) offset 0px), `identity-btn` (1px auto #005fcc, offset 0px), `landing-link` (on a child: 1px auto rgb(0, 95, 204) offset 1px), `car-btn` (1px auto #005fcc, offset 1px), `car-nav-link` (1px auto #005fcc, offset 1px), `footer-link` (1px auto #005fcc, offset 1px), `appstore-badge` (1px auto #005fcc, offset 1px), `social-btn` (1px auto #005fcc, offset 1px). The other 2 show no measured change: `value-prop-card`, `card-cta`. Focus could not be captured on 6 more (keyboard focus never landed on them, so their readings are left out): `tab-selected`, `tab-idle`, `city-link`, `bell-btn`, `group-order`, `m-identity-btn`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `ease-in-out` | background-color, box-shadow | tab-idle, tab-selected |
| 0.2s | `cubic-bezier(0.4, 0.4, 0, 1)` | background-color, box-shadow | address-btn, address-pill, cart-btn, cta-btn, fulfil-toggle, identity-btn, location-pill, nearby-cta and more |
| 0.2s | `ease` | filter, opacity | appstore-badge, footer-link, logo, social-btn |
| 0.225s | `cubic-bezier(0.83, 0, 0.17, 1)` | box-shadow | sidenav-toggle |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | car-btn, car-nav-link |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [CTA band](#cta-band) | 1440 x 600 | - | - | transparent | none | 0 |
| [Value-prop card](#value-prop-card) | 360 x 410 | - | - | transparent | none | 16px |
| [Restaurant card](#restaurant-card) | 447.98 x 274 | - | - | transparent | none | 0 |
| [Menu item card](#menu-item-card) | 944 x 450 | - | 16px | #f7f7f7 `color.neutral.0` | none | 0 |
| [Cookie banner](#cookie-banner) | 1440 x 98 | - | - | #f7f7f7 `color.neutral.0` | none | 0 |
| [Hero band](#hero-band) | 1440 x 650 | - | - | transparent | none | 0px 8px |

## Components

### App shell and navigation

The consumer app chrome that ships signed out: the marketing top bar with Sign in / Sign Up and the storefront Header (logo, address gate, side-nav, cart, bell).

#### Wordmark
The DoorDash wordmark anchor (svg + visually-hidden label). Read as `logo` on the home page.

**Values (default).** size 170.7 x 20; background transparent; text DD Norms 14/20 500, #c4c4c4 `color.neutral.20`; transition filter 0.2s ease.

![Wordmark default](components/crops/logo-default.png)

#### Sign-in button
kind="BUTTON/PRIMARY" anchor to identity.doordash.com; measured, never followed. Read as `signin-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 82.44 x 40; radius 9999px; background #eb1700 `color.brand.doordash.60`; shadow rgba(25, 25, 25, 0) 0px 0px 0px 1px inset; text DD Norms 18/22 800, #ffffff `color.white`; transition background-color 0.2s cubic-bezier(0.4, 0.4, 0, 1), box-shadow 0.2s cubic-bezier(0.4, 0.4, 0, 1) |
| hover | background #d91400 `color.brand.doordash.70`; transition background-color 0.05s linear, box-shadow 0.05s linear |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #b71000 `color.brand.doordash.80`; transition background-color 0.05s linear, box-shadow 0.05s linear |

![Sign-in button default](components/crops/signin-btn-default.png) ![Sign-in button hover](components/crops/signin-btn-hover.png) ![Sign-in button focus-visible](components/crops/signin-btn-focus-visible.png) ![Sign-in button pressed](components/crops/signin-btn-pressed.png)

#### Sign-up button
kind="BUTTON/PLAIN" red pill to the signup URL; measured, never followed. Read as `signup-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 90.55 x 40; radius 9999px; background #ffffff `color.white`; shadow rgba(25, 25, 25, 0) 0px 0px 0px 1px inset; text DD Norms 18/22 800, #606060 `color.neutral.70`; transition background-color 0.2s cubic-bezier(0.4, 0.4, 0, 1), box-shadow 0.2s cubic-bezier(0.4, 0.4, 0, 1) |
| hover | transition background-color 0.05s linear, box-shadow 0.05s linear |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | transition background-color 0.05s linear, box-shadow 0.05s linear |

![Sign-up button default](components/crops/signup-btn-default.png) ![Sign-up button hover](components/crops/signup-btn-hover.png) ![Sign-up button focus-visible](components/crops/signup-btn-focus-visible.png) ![Sign-up button pressed](components/crops/signup-btn-pressed.png)

#### Language select
The footer/top-bar native <select> of locales (data-size="small"). Read as `language-select` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 94 x 20; padding 0px 24px 0px 0px; background #f1f1f1 `color.neutral.5`; text DD Norms 14/20 500, #191919 `color.neutral.100` |

![Language select default](components/crops/language-select-default.png) ![Language select focused](components/crops/language-select-focused.png)

#### App header
The consumer app shell header — HomeLogo, address button, side-nav toggle, cart and bell. Read as `app-header` on the DashPass student page.

**Values (default).** size 1440 x 64; padding 64px 0px 0px 0px; background transparent; text DD Norms 14/20 700, #191919 `color.neutral.100`; icon 32 x 18, #0000ee (the browser's default link colour, inherited in the replay); layers div.sc-51f7ae22-5.CiCuB 1440.0x0.0 rgb(255, 255, 255); div.sc-51f7ae22-6.jtIgLU 1440.0x64.0 rgb(255, 255, 255) B:1px solid rgb(228, 228, 228); div.sc-51f7ae22-8.icwqCe 152.0x18.0; button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 150.3x32.0 rgb(241, 241, 241) rgb(241, 241, 241) 0px 0px 0px 1px inset 9999px; button.ButtonRootInternal-sc-j2wkqj-0.dxDIIR 32.0x32.0 rgb(241, 241, 241) rgb(241, 241, 241) 0px.

Child layers that carry the look: div 1440x0 background #ffffff `color.white`; div 1440x64 background #ffffff `color.white` border 1px solid #e4e4e4; div 152x18 image linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, #ffffff `color.white` 5%, #ffffff `color.

![App header default](components/crops/app-header-default.png)

#### App wordmark
Read as `app-logo` on the DashPass student page.

**Values (default).** size 152 x 18; background transparent; image linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, #ffffff `color.white` 5%, #ffffff `color.white` 50%, #ffffff `color.white` 95%, rgba(255, 255, 255, 0) 100%); text browser default (Times 16/normal 400, #000000); icon 32 x 18, #0000ee (the browser's default link colour, inherited in the replay).

![App wordmark default](components/crops/app-logo-default.png)

#### Address button
The header address/destination control — an address gate, never pressed. Read as `address-btn` on the DashPass student page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 150.27 x 32; radius 9999px; background #f1f1f1 `color.neutral.5`; shadow #f1f1f1 0px 0px 0px 1px inset; text DD Norms 14/20 700, #191919 `color.neutral.100`; transition background-color 0.2s cubic-bezier(0.4, 0.4, 0, 1), box-shadow 0.2s cubic-bezier(0.4, 0.4, 0, 1); icon 16 x 24, #191919 `color.neutral.100` |
| hover | background #d6d6d6 `color.neutral.10`; shadow #d6d6d6 0px 0px 0px 1px inset; transition background-color 0.05s linear, box-shadow 0.05s linear; icon 16 x 24, #242424 `color.neutral.95` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #c4c4c4 `color.neutral.20`; shadow #c4c4c4 0px 0px 0px 1px inset; transition background-color 0.05s linear, box-shadow 0.05s linear; icon 16 x 24, #313131 `color.neutral.90` |

![Address button default](components/crops/address-btn-default.png) ![Address button hover](components/crops/address-btn-hover.png) ![Address button focus-visible](components/crops/address-btn-focus-visible.png) ![Address button pressed](components/crops/address-btn-pressed.png)

#### Side-nav toggle
The hamburger that opens the side navigation; toggled on mobile only. Read as `sidenav-toggle` on the DashPass student page.

**Values (default).** size 221 x 836; border R: 1px solid #e4e4e4; background #ffffff `color.white`; text DD Norms 14/20 500, #191919 `color.neutral.100`; transition box-shadow 0.225s cubic-bezier(0.83, 0, 0.17, 1); icon 24 x 24, #0000ee (the browser's default link colour, inherited in the replay).

![Side-nav toggle default](components/crops/sidenav-toggle-default.png)

#### Cart button
The header cart (icon button with badge); measured, never pressed. Read as `cart-btn` on the DashPass student page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 57.66 x 32; radius 9999px; background #eb1700 `color.brand.doordash.60`; shadow rgba(25, 25, 25, 0) 0px 0px 0px 1px inset; text DD Norms 14/20 700, #ffffff `color.white`; transition background-color 0.2s cubic-bezier(0.4, 0.4, 0, 1), box-shadow 0.2s cubic-bezier(0.4, 0.4, 0, 1); icon 20 x 20, #ffffff `color.white` |
| hover | background #d91400 `color.brand.doordash.70`; transition background-color 0.05s linear, box-shadow 0.05s linear |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #b71000 `color.brand.doordash.80`; transition background-color 0.05s linear, box-shadow 0.05s linear |

![Cart button default](components/crops/cart-btn-default.png) ![Cart button hover](components/crops/cart-btn-hover.png) ![Cart button focus-visible](components/crops/cart-btn-focus-visible.png) ![Cart button pressed](components/crops/cart-btn-pressed.png)

#### Bell button
The header notifications bell; measured, never pressed. Read as `bell-btn` on the DashPass student page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 24 x 32; background transparent; text browser default (Times 16/normal 400, #000000); icon 24 x 24, #191919 `color.neutral.100`; layers button.ButtonRootInternal-sc-j2wkqj-0.dxDIIR 32.0x32.0 rgb(241, 241, 241) rgb(241, 241, 241) 0px 0px 0px 1px inset 9999px |
| hover | icon 24 x 24, #242424 `color.neutral.95`; layers button.ButtonRootInternal-sc-j2wkqj-0.dxDIIR 32.0x32.0 rgb(214, 214, 214) rgb(214, 214, 214) 0px 0px 0px 1px inset 9999px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: button 32x32 background #f1f1f1 `color.neutral.5` radius 9999px shadow #f1f1f1 `color.neutral.5` 0px 0px 0px 1px inset.

![Bell button default](components/crops/bell-btn-default.png) ![Bell button hover](components/crops/bell-btn-hover.png) ![Bell button pressed](components/crops/bell-btn-pressed.png)

#### Hero band
The marketing hero region the top bar floats on: wordmark, Sign in and Sign Up over the campaign field (the bar has no separate paint). Read as `hero-band` on the home page.

**Values (default).** size 1440 x 650; padding 0px 8px; background transparent; image url(…); text TTNormsProCond-Blk 40/40 900, #ffffff `color.white`; icon 42 x 24, #000000 `color.black`.

![Hero band default](components/crops/hero-band-default.png)

### Marketing hero

The red campaign hero — TTNormsProCond-Blk display headline, the DoorDash wordmark, and the two address-gate pills, measured but never pressed.

#### Hero headline
The campaign h1 — TTNormsProCond-Blk 900, uppercase. Read as `hero-title` on the home page.

**Values (default).** size 646.88 x 40; background transparent; text TTNormsProCond-Blk 40/40 900, #ffffff `color.white`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero subcopy
The line under the hero headline ("Other fees apply"). Read as `hero-sub` on the home page.

**Values (default).** size 92.69 x 22; background transparent; text DD Norms 12/22 600, #ffffff `color.white`.

![Hero subcopy default](components/crops/hero-sub-default.png)

#### Address pill (sign-in gate)
The "Sign in for saved address" hero pill — an authentication gate, never pressed. Read as `address-pill` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 204.55 x 32; radius 9999px; background #ffffff `color.white`; shadow rgba(25, 25, 25, 0) 0px 0px 0px 1px inset, rgba(25, 25, 25, 0.2) 0px 2px 8px 0px; text DD Norms 14/20 700, #191919 `color.neutral.100`; transition background-color 0.2s cubic-bezier(0.4, 0.4, 0, 1), box-shadow 0.2s cubic-bezier(0.4, 0.4, 0, 1); icon 16 x 24, #191919 `color.neutral.100` |
| hover | text DD Norms 14/20 700, #242424 `color.neutral.95`; transition background-color 0.05s linear, box-shadow 0.05s linear; icon 16 x 24, #242424 `color.neutral.95` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | text DD Norms 14/20 700, #313131 `color.neutral.90`; transition background-color 0.05s linear, box-shadow 0.05s linear; icon 16 x 24, #313131 `color.neutral.90` |

![Address pill (sign-in gate) default](components/crops/address-pill-default.png) ![Address pill (sign-in gate) hover](components/crops/address-pill-hover.png) ![Address pill (sign-in gate) focus-visible](components/crops/address-pill-focus-visible.png) ![Address pill (sign-in gate) pressed](components/crops/address-pill-pressed.png)

#### Location pill
The "Use current Location" hero pill — a geolocation prompt, never pressed. Read as `location-pill` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 179.81 x 32; radius 9999px; background #ffffff `color.white`; shadow rgba(25, 25, 25, 0) 0px 0px 0px 1px inset, rgba(25, 25, 25, 0.2) 0px 2px 8px 0px; text DD Norms 14/20 700, #191919 `color.neutral.100`; transition background-color 0.2s cubic-bezier(0.4, 0.4, 0, 1), box-shadow 0.2s cubic-bezier(0.4, 0.4, 0, 1); icon 16 x 24, #191919 `color.neutral.100` |
| hover | text DD Norms 14/20 700, #242424 `color.neutral.95`; transition background-color 0.05s linear, box-shadow 0.05s linear; icon 16 x 24, #242424 `color.neutral.95` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | text DD Norms 14/20 700, #313131 `color.neutral.90`; transition background-color 0.05s linear, box-shadow 0.05s linear; icon 16 x 24, #313131 `color.neutral.90` |

![Location pill default](components/crops/location-pill-default.png) ![Location pill hover](components/crops/location-pill-hover.png) ![Location pill focus-visible](components/crops/location-pill-focus-visible.png) ![Location pill pressed](components/crops/location-pill-pressed.png)

### CTA bands and cards

The mid-page call-to-action sections (CTASplash bands, business and DashPass CTAs) and the Become-a-Dasher-style value-prop cards.

#### CTA band
A mid-page CTA section (CTASplash) — tinted band with headline, copy and a primary action. Read as `cta-band` on the home page.

**Values (default).** size 1440 x 600; background transparent; image url(…); text DD Norms 40/40 800, #ffffff `color.white`.

![CTA band default](components/crops/cta-band-default.png)

#### CTA band headline
Read as `cta-band-title` on the home page.

**Values (default).** size 240.97 x 120; background transparent; text DD Norms 40/40 800, #191919 `color.neutral.100`.

![CTA band headline default](components/crops/cta-band-title-default.png)

#### CTA band copy
Read as `cta-band-copy` on the home page.

**Values (default).** size 267.75 x 88; background transparent; text DD Norms 16/22 500, #191919 `color.neutral.100`.

![CTA band copy default](components/crops/cta-band-copy-default.png)

#### CTA button
kind="BUTTON/PRIMARY" red pill in the CTA band; measured, never followed. Read as `cta-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 145.42 x 40; radius 9999px; background #eb1700 `color.brand.doordash.60`; shadow rgba(25, 25, 25, 0) 0px 0px 0px 1px inset; text DD Norms 16/22 700, #ffffff `color.white`; transition background-color 0.2s cubic-bezier(0.4, 0.4, 0, 1), box-shadow 0.2s cubic-bezier(0.4, 0.4, 0, 1) |
| hover | background #d91400 `color.brand.doordash.70`; transition background-color 0.05s linear, box-shadow 0.05s linear |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #b71000 `color.brand.doordash.80`; transition background-color 0.05s linear, box-shadow 0.05s linear |

![CTA button default](components/crops/cta-btn-default.png) ![CTA button hover](components/crops/cta-btn-hover.png) ![CTA button focus-visible](components/crops/cta-btn-focus-visible.png) ![CTA button pressed](components/crops/cta-btn-pressed.png)

#### Value-prop card
A "Become a Dasher"-style card: illustration, heading, copy and a link. Read as `value-prop-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 360 x 410; padding 16px; background transparent; text DD Norms 32/40 800, #191919 `color.neutral.100`; icon 16 x 16, #000000 `color.black` |

![Value-prop card default](components/crops/value-prop-card-default.png) ![Value-prop card hover](components/crops/value-prop-card-hover.png) ![Value-prop card focus-visible](components/crops/value-prop-card-focus-visible.png) ![Value-prop card pressed](components/crops/value-prop-card-pressed.png)

#### Card CTA
The arrow/action inside a value-prop card. Read as `card-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 250 x 20; background transparent; text DD Norms 14/20 700, #eb1700 `color.brand.doordash.60`; icon 16 x 16, #000000 `color.black` |

![Card CTA default](components/crops/card-cta-default.png) ![Card CTA hover](components/crops/card-cta-hover.png) ![Card CTA focus-visible](components/crops/card-cta-focus-visible.png) ![Card CTA pressed](components/crops/card-cta-pressed.png)

#### Business hero
The DoorDash for Business headline. Read as `biz-h1` on the DoorDash for Business page.

**Values (default).** size 600 x 94; background transparent; text DD-TTNorms 40/normal 700, #000000 `color.black`.

![Business hero default](components/crops/biz-h1-default.png)

#### Business CTA
The business page primary action; measured, never followed. Read as `biz-cta` on the DoorDash for Business page.

Not on the page when it was captured.

#### Merchant link
A merchant-name entry in the business directory lists. Read as `biz-merchant` on the DoorDash for Business page.

**Values (default).** size 211.41 x 40; background transparent; text DD Norms 16/40 500, #191919 `color.neutral.100`.

![Merchant link default](components/crops/biz-merchant-default.png)

#### DashPass headline
The DashPass student page headline. Read as `dp-h1` on the DashPass student page.

Not on the page when it was captured.

#### DashPass CTA
A DashPass signup action; measured, never followed (signup gated). Read as `dp-cta` on the DashPass student page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 196 x 40; radius 8px; background #ffffff `color.white`; text DD Norms 14/20 500, #191919 `color.neutral.100`; icon 24 x 24, #000000 `color.black` |
| hover | background #f7f7f7 `color.neutral.0` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #f1f1f1 `color.neutral.5` |

![DashPass CTA default](components/crops/dp-cta-default.png) ![DashPass CTA hover](components/crops/dp-cta-hover.png) ![DashPass CTA focus-visible](components/crops/dp-cta-focus-visible.png) ![DashPass CTA pressed](components/crops/dp-cta-pressed.png)

### Directory lists and tabs

The SEO directory surfaces: the Top Cities / Top Cuisines / Top Chains tabs, city/cuisine link lists and the Show-more toggles.

#### Section title
A "Get more from your neighborhood" h2. Read as `section-title` on the home page.

**Values (default).** size 1130 x 40; background transparent; text DD Norms 32/40 800, #191919 `color.neutral.100`.

![Section title default](components/crops/section-title-default.png)

#### Directory tab, selected
The selected tab (Top Cities) — 3px bottom border in the selected colour. Read as `tab-selected` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 376.63 x 40; border B: 3px solid #191919 `color.neutral.100`; background #ffffff `color.white`; text DD Norms 16/22 700, #191919 `color.neutral.100`; transition background-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out |
| hover, pressed | background #f7f7f7 `color.neutral.0` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Directory tab, selected default](components/crops/tab-selected-default.png) ![Directory tab, selected hover](components/crops/tab-selected-hover.png) ![Directory tab, selected pressed](components/crops/tab-selected-pressed.png)

#### Directory tab, idle
An idle tab (Top Cuisines / Top Chains). Read as `tab-idle` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 376.63 x 40; border B: 2px solid #e4e4e4; background #ffffff `color.white`; text DD Norms 16/22 500, #606060 `color.neutral.70`; transition background-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out |
| hover, pressed | background #f7f7f7 `color.neutral.0` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Directory tab, idle default](components/crops/tab-idle-default.png) ![Directory tab, idle hover](components/crops/tab-idle-hover.png) ![Directory tab, idle pressed](components/crops/tab-idle-pressed.png)

#### Directory link
A city/cuisine/chain link in the tabbed directory lists. Read as `dir-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 90.16 x 22; background transparent; text DD Norms 16/22 500, #191919 `color.neutral.100` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.c1gxzxj 90.2x22.0 1px auto rgb(0, 95, 204) offset 1px |

![Directory link default](components/crops/dir-link-default.png) ![Directory link hover](components/crops/dir-link-hover.png) ![Directory link focus-visible](components/crops/dir-link-focus-visible.png) ![Directory link pressed](components/crops/dir-link-pressed.png)

#### Show-more toggle
The expand/collapse control on a directory list; measured, not pressed here (toggled in the shot pass). Read as `show-more` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1130 x 60; padding 10px 0px; background transparent; text DD Norms 20/24 800, #191919 `color.neutral.100`; icon 24 x 24, #191919 `color.neutral.100`; layers button.b11usoxu 40.0x40.0 rgb(241, 241, 241) rgb(241, 241, 241) 0px 0px 0px 1px inset 9999px |
| focus-visible | layers button.b11usoxu 40.0x40.0 rgb(241, 241, 241) rgb(241, 241, 241) 0px 0px 0px 1px inset 1px auto rgb(0, 95, 204) offset 0px 9999px |

Child layers that carry the look: button 40x40 background #f1f1f1 `color.neutral.5` radius 9999px shadow #f1f1f1 `color.neutral.5` 0px 0px 0px 1px inset.

![Show-more toggle default](components/crops/show-more-default.png) ![Show-more toggle hover](components/crops/show-more-hover.png) ![Show-more toggle focus-visible](components/crops/show-more-focus-visible.png) ![Show-more toggle pressed](components/crops/show-more-pressed.png)

#### Cross link
A cross-category link tile (e.g. grocery → convenience). Read as `cross-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 90.16 x 22; background transparent; text DD Norms 16/22 500, #191919 `color.neutral.100` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.c1gxzxj 90.2x22.0 1px auto rgb(0, 95, 204) offset 1px |

![Cross link default](components/crops/cross-link-default.png) ![Cross link hover](components/crops/cross-link-hover.png) ![Cross link focus-visible](components/crops/cross-link-focus-visible.png) ![Cross link pressed](components/crops/cross-link-pressed.png)

#### Page title
The food-delivery page headline. Read as `fd-h1` on the food delivery page.

**Values (default).** size 460 x 40; background transparent; text DD-TTNorms 32/40 700, #000000 `color.black`.

![Page title default](components/crops/fd-h1-default.png)

#### City link
A city directory entry (per-city data-testid); measured, never followed. Read as `city-link` on the food delivery page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 211.39 x 40; background transparent; text DD Norms 16/40 500, #191919 `color.neutral.100` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![City link default](components/crops/city-link-default.png) ![City link hover](components/crops/city-link-hover.png) ![City link pressed](components/crops/city-link-pressed.png)

#### FAQ block
The SEO FAQ accordion block, if published on this route. Read as `fd-faq` on the food delivery page.

Not on the page when it was captured.

### Storefront (menu page)

A real public restaurant page (/en-US/store/…): store header, Delivery/Pickup toggle, the menu grid, quick-add circles and the recommended carousel — all read-only.

#### Store header
The storefront header: hero image, name, rating and delivery info. Read as `store-head` on the restaurant storefront page.

**Values (default).** size 1200 x 210; background transparent; text browser default (Times 16/normal 400, #000000); layers div.sc-9c44606c-5.eznBjt 0.0x0.0 T:60px solid rgba(0, 0, 0, 0) / L:480px solid rgb(255, 255, 255); div.sc-9c44606c-6.joKFnE 80.0x80.0 rgb(255, 255, 255) T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) rgba(0, 0, 0, 0.2) 0px 2px 8px 0px 50%; div.sc-9c44606c-7.dgRYDA 1200.0x110.0 0px 0px 12px 12px.

Child layers that carry the look: div 0x0 border 60px solid transparent; div 80x80 background #ffffff `color.white` border 2px solid #ffffff `color.white` radius 50% shadow rgba(0, 0, 0, 0.2) 0px 2px 8px 0px; div 1200x110 image linear-gradient(transparent 0%, rgba(0, 0, 0, 0.6) 75%) radius 0px 0px 12px 12px.

![Store header default](components/crops/store-head-default.png)

#### Store name
Read as `store-name` on the restaurant storefront page.

**Values (default).** size 836 x 28; background transparent; text DD Norms 24/28 800, #191919 `color.neutral.100`.

![Store name default](components/crops/store-name-default.png)

#### Store meta
The rating/distance/delivery-fee detail line under the store name. Read as `store-meta` on the restaurant storefront page.

**Values (default).** size 222.5 x 52; radius 8px; background transparent; text DD Norms 14/20 700, #191919 `color.neutral.100`; icon 12 x 12, #191919 `color.neutral.100`; layers button.ButtonRoot-sc-j2wkqj-0.iLCINK 12.0x22.0 rgba(25, 25, 25, 0) rgba(25, 25, 25, 0) 0px 0px 0px 1px inset 9999px.

Child layers that carry the look: button 12x22 background rgba(25, 25, 25, 0) radius 9999px shadow rgba(25, 25, 25, 0) 0px 0px 0px 1px inset.

![Store meta default](components/crops/store-meta-default.png)

#### Fulfilment toggle
The Delivery/Pickup segmented toggle in the menu header; measured, not pressed (a press re-queries the menu). Read as `fulfil-toggle` on the restaurant storefront page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 94.45 x 32; radius 9999px; background #ffffff `color.white`; shadow #e4e4e4 0px 0px 0px 2px inset, rgba(25, 25, 25, 0) 0px 0px 0px 0px; text DD Norms 14/20 700, #191919 `color.neutral.100`; transition background-color 0.2s cubic-bezier(0.4, 0.4, 0, 1), box-shadow 0.2s cubic-bezier(0.4, 0.4, 0, 1) |
| hover | background #f1f1f1 `color.neutral.5`; shadow #d6d6d6 0px 0px 0px 2px inset, rgba(25, 25, 25, 0) 0px 0px 0px 0px; text DD Norms 14/20 700, #242424 `color.neutral.95`; transition background-color 0.05s linear, box-shadow 0.05s linear |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #d6d6d6 `color.neutral.10`; shadow #c4c4c4 0px 0px 0px 2px inset, rgba(25, 25, 25, 0) 0px 0px 0px 0px; text DD Norms 14/20 700, #313131 `color.neutral.90`; transition background-color 0.05s linear, box-shadow 0.05s linear |

![Fulfilment toggle default](components/crops/fulfil-toggle-default.png) ![Fulfilment toggle hover](components/crops/fulfil-toggle-hover.png) ![Fulfilment toggle focus-visible](components/crops/fulfil-toggle-focus-visible.png) ![Fulfilment toggle pressed](components/crops/fulfil-toggle-pressed.png)

#### Group-order button
The group-cart action; measured, never pressed. Read as `group-order` on the restaurant storefront page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 107.63 x 38; background transparent; text DD Norms 14/20 700, #191919 `color.neutral.100`; layers button.ButtonRoot-sc-j2wkqj-0.jcvtZg 107.6x38.0 rgb(241, 241, 241) rgb(241, 241, 241) 0px 0px 0px 1px inset 9999px |
| hover | text DD Norms 14/20 700, #242424 `color.neutral.95`; layers button.ButtonRoot-sc-j2wkqj-0.jcvtZg 107.6x38.0 rgb(214, 214, 214) rgb(214, 214, 214) 0px 0px 0px 1px inset 9999px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: button 107.6x38 background #f1f1f1 `color.neutral.5` radius 9999px shadow #f1f1f1 `color.neutral.5` 0px 0px 0px 1px inset.

![Group-order button default](components/crops/group-order-default.png) ![Group-order button hover](components/crops/group-order-hover.png) ![Group-order button pressed](components/crops/group-order-pressed.png)

#### Store search field
The in-store menu search input; focused only, never submitted. Read as `search-input` on the restaurant storefront page.

Not on the page when it was captured.

#### Menu item card
A menu item in the virtualised grid: image, name, price. Read as `menu-item` on the restaurant storefront page.

**Values (default).** size 944 x 450; radius 16px; background #f7f7f7 `color.neutral.0`; text browser default (Times 16/normal 400, #000000).

![Menu item card default](components/crops/menu-item-default.png)

#### Quick-add button
The + quick-add circle on a menu item; measured, NEVER pressed — a press starts a cart. Read as `quick-add` on the restaurant storefront page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 9999px; background #ffffff `color.white`; shadow rgba(25, 25, 25, 0) 0px 0px 0px 1px inset, rgba(25, 25, 25, 0.2) 0px 2px 8px 0px; text Arial 13.33/normal 400, #191919 `color.neutral.100`; transition background-color 0.2s cubic-bezier(0.4, 0.4, 0, 1), box-shadow 0.2s cubic-bezier(0.4, 0.4, 0, 1); icon 24 x 24, #191919 `color.neutral.100` |
| hover | text Arial 13.33/normal 400, #242424 `color.neutral.95`; transition background-color 0.05s linear, box-shadow 0.05s linear; icon 24 x 24, #242424 `color.neutral.95` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | text Arial 13.33/normal 400, #313131 `color.neutral.90`; transition background-color 0.05s linear, box-shadow 0.05s linear; icon 24 x 24, #313131 `color.neutral.90` |

![Quick-add button default](components/crops/quick-add-default.png) ![Quick-add button hover](components/crops/quick-add-hover.png) ![Quick-add button focus-visible](components/crops/quick-add-focus-visible.png) ![Quick-add button pressed](components/crops/quick-add-pressed.png)

#### Recommended carousel
The "Recommended items for you" carousel rail. Read as `rec-section` on the restaurant storefront page.

**Values (default).** size 944 x 302; padding 20px 0px 0px 0px; background transparent; text DD Norms 20/24 800, #191919 `color.neutral.100`; icon 24 x 24, #191919 `color.neutral.100`; layers div.sc-6d5ee6a2-0.kQKwOO 177.0x168.0 rgb(247, 247, 247); button.ButtonRoot-sc-j2wkqj-0.kLnbCu 32.0x32.0 rgb(255, 255, 255) rgba(25, 25, 25, 0) 0px 0px 0px 1px inset, rgba(25, 25, 25, 0.2) 0px 2px 8px 0px 9999px; div.sc-6d5ee6a2-0.kQKwOO 177.0x168.0 rgb(247, 247, 247); button.ButtonRoot-sc-j2wkqj-0.kLnbCu 32.0x32.0 rgb(255, 255, 255) rgba(25, 25, 25, 0) 0px 0px 0px 1px inset, rgba(25, 25, 25, 0.2) .

Child layers that carry the look: div 177x168 background #f7f7f7 `color.neutral.0`; button 32x32 background #ffffff `color.white` radius 9999px shadow rgba(25, 25, 25, 0) 0px 0px 0px 1px inset, rgba(25, 25, 25, 0.2) 0px 2px 8px 0px; div 177x168 background #f7f7f7 `color.neutral.0`.

![Recommended carousel default](components/crops/rec-section-default.png)

#### Breadcrumb
The SEO breadcrumb trail at the foot of the store page. Read as `breadcrumb` on the restaurant storefront page.

**Values (default).** size 1200 x 20; background transparent; text DD Norms 12/12 700, #606060 `color.neutral.70`.

![Breadcrumb default](components/crops/breadcrumb-default.png)

#### Missing-address nux
The new-user "add an address" prompt shown without a saved address — the documented address gate, never answered. Read as `address-nux` on the restaurant storefront page.

**Values (default).** size 222.5 x 52; radius 8px; background #ffffff `color.white`; text DD Norms 16/22 700, #191919 `color.neutral.100`.

![Missing-address nux default](components/crops/address-nux-default.png)

### Restaurant directory

The /en-US/restaurants-near-me/ listings: compact cards with offer and leaderboard badges, FAQ accordions and pagination.

#### Restaurant card
A restaurant tile: image, name, rating/ETA and an offer badge. Read as `rest-card` on the restaurants-near-me page.

**Values (default).** size 447.98 x 274; background transparent; text DD Norms 16/22 700, #191919 `color.neutral.100`; icon 12 x 12, #606060 `color.neutral.70`; layers div.sc-ab0469c2-0.QkeXV 448.0x172.0 rgb(247, 247, 247) 12px; div.TagWrapperInternal-sc-1l2oqbc-2.eYQCgy 118.3x20.0 rgb(241, 241, 241) rgba(247, 247, 247, 0) 0px 0px 0px 0px inset 9999px.

Child layers that carry the look: div 448x172 background #f7f7f7 `color.neutral.0` radius 12px; div 118.3x20 background #f1f1f1 `color.neutral.5` radius 9999px shadow rgba(247, 247, 247, 0) 0px 0px 0px 0px inset.

![Restaurant card default](components/crops/rest-card-default.png)

#### Card title
Read as `rest-card-title` on the restaurants-near-me page.

**Values (default).** size 447.98 x 94; background transparent; text DD Norms 16/22 700, #191919 `color.neutral.100`; icon 12 x 12, #606060 `color.neutral.70`; layers div.TagWrapperInternal-sc-1l2oqbc-2.eYQCgy 118.3x20.0 rgb(241, 241, 241) rgba(247, 247, 247, 0) 0px 0px 0px 0px inset 9999px.

Child layers that carry the look: div 118.3x20 background #f1f1f1 `color.neutral.5` radius 9999px shadow rgba(247, 247, 247, 0) 0px 0px 0px 0px inset.

![Card title default](components/crops/rest-card-title-default.png)

#### Card subtitle
The rating · ETA · fee line under the restaurant name (a single styled leaf of the row). Read as `rest-card-sub` on the restaurants-near-me page.

**Values (default).** size 38.38 x 20; background transparent; text DD Norms 14/20 500, #606060 `color.neutral.70`.

![Card subtitle default](components/crops/rest-card-sub-default.png)

#### Offer badge
A promo chip on a restaurant card ("20% off on $40+"). Read as `offer-badge` on the restaurants-near-me page.

**Values (default).** size 109.17 x 20; padding 0px 8px; radius 9999px; background #fff0ed `color.brand.doordash.5`; shadow rgba(247, 247, 247, 0) 0px 0px 0px 0px inset; text DD Norms 12/18 700, #d91400 `color.brand.doordash.70`.

![Offer badge default](components/crops/offer-badge-default.png)

#### Leaderboard badge
A "Top 10%"-style tag on a restaurant card. Read as `leaderboard-badge` on the restaurants-near-me page.

**Values (default).** size 118.33 x 20; padding 0px 8px; radius 9999px; background #f1f1f1 `color.neutral.5`; shadow rgba(247, 247, 247, 0) 0px 0px 0px 0px inset; text DD Norms 12/18 700, #191919 `color.neutral.100`; icon 24 x 24, #0000ee (the browser's default link colour, inherited in the replay).

![Leaderboard badge default](components/crops/leaderboard-badge-default.png)

#### Popular-items button
Read as `popular-btn` on the restaurants-near-me page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 90.14 x 32; radius 9999px; background rgba(25, 25, 25, 0); shadow rgba(25, 25, 25, 0) 0px 0px 0px 1px inset; text DD Norms 14/20 700, #191919 `color.neutral.100`; transition background-color 0.2s cubic-bezier(0.4, 0.4, 0, 1), box-shadow 0.2s cubic-bezier(0.4, 0.4, 0, 1) |
| hover | text DD Norms 14/20 700, #242424 `color.neutral.95`; transition background-color 0.05s linear, box-shadow 0.05s linear |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | text DD Norms 14/20 700, #313131 `color.neutral.90`; transition background-color 0.05s linear, box-shadow 0.05s linear |

![Popular-items button default](components/crops/popular-btn-default.png) ![Popular-items button hover](components/crops/popular-btn-hover.png) ![Popular-items button focus-visible](components/crops/popular-btn-focus-visible.png) ![Popular-items button pressed](components/crops/popular-btn-pressed.png)

#### Location CTA
The "search nearby"/sign-in call at the end of the directory; measured, never pressed (address/sign-in gate). Read as `nearby-cta` on the restaurants-near-me page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 758.56 x 40; radius 9999px; background #eb1700 `color.brand.doordash.60`; shadow rgba(25, 25, 25, 0) 0px 0px 0px 1px inset; text DD Norms 16/22 700, #ffffff `color.white`; transition background-color 0.2s cubic-bezier(0.4, 0.4, 0, 1), box-shadow 0.2s cubic-bezier(0.4, 0.4, 0, 1) |
| hover | background #d91400 `color.brand.doordash.70`; transition background-color 0.05s linear, box-shadow 0.05s linear |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #b71000 `color.brand.doordash.80`; transition background-color 0.05s linear, box-shadow 0.05s linear |

![Location CTA default](components/crops/nearby-cta-default.png) ![Location CTA hover](components/crops/nearby-cta-hover.png) ![Location CTA focus-visible](components/crops/nearby-cta-focus-visible.png) ![Location CTA pressed](components/crops/nearby-cta-pressed.png)

#### Pagination loader
Read as `pagination` on the restaurants-near-me page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1440 x 584; background transparent; text browser default (Times 16/normal 400, #000000); layers div.sc-f98a4c4c-0.gTFInR 240.0x20.0 rgb(241, 241, 241) 8px; div.sc-f98a4c4c-0.foUEsd 28.0x28.0 rgb(241, 241, 241) 50%; div.sc-f98a4c4c-0.foUEsd 28.0x28.0 rgb(241, 241, 241) 50%; div.sc-f98a4c4c-0.hoBkdx 448.0x172.0 rgb(241, 241, 241) 8px; div.sc-f98a4c4c-0.gXJfPn 96.0x14.0 rgb(241, 241, 241) 8px; div.sc-f98a4c4c-0.gEHuWJ 184.0x14.0 rgb(241, 241, 241) 8px |
| focus-visible | layers div.sc-f98a4c4c-0.gTFInR 240.0x20.0 rgb(241, 241, 241) 8px; div.sc-f98a4c4c-0.foUEsd 28.0x28.0 rgb(241, 241, 241) 50%; div.sc-f98a4c4c-0.foUEsd 28.0x28.0 rgb(241, 241, 241) 50%; div.sc-297d2f35-0.sc-e4dee18e-0 1376.0x228.0 1px auto rgb(0, 95, 204) offset 0px; div.sc-f98a4c4c-0.hoBkdx 448.0x172.0 rgb(241, 241, 241) 8px; div.sc-f98a4c4c-0.gXJfPn 96.0x14.0 rgb(241, 241, 241) 8px |

Child layers that carry the look: div 240x20 background #f1f1f1 `color.neutral.5` image linear-gradient(90deg, #f1f1f1 `color.neutral.5`, #f7f7f7 `color.neutral.0`, #f1f1f1 `colo radius 8px; div 28x28 background #f1f1f1 `color.neutral.5` image linear-gradient(90deg, #f1f1f1 `color.neutral.5`, #f7f7f7 `color.neutral.0`, #f1f1f1 `colo radius 50%; div 28x28 background #f1f1f1 `color.neutral.5` image linear-gradient(90deg, #f1f1f1 `color.neutral.5`, #f7f7f7 `color.neutral.0`, #f1f1f1 `colo radius 50%.

![Pagination loader default](components/crops/pagination-default.png) ![Pagination loader hover](components/crops/pagination-hover.png) ![Pagination loader focus-visible](components/crops/pagination-focus-visible.png) ![Pagination loader pressed](components/crops/pagination-pressed.png)

#### FAQ block
The SEO FAQ accordion under the listings. Read as `faq-block` on the restaurants-near-me page.

**Values (default).** size 1152 x 610; padding 0px 0px 100px 0px; background transparent; text DD Norms 32/24 800, #191919 `color.neutral.100`; icon 24 x 24, #191919 `color.neutral.100`; layers hr.Border-sc-i9okij-1.hGZdZM 1152.0x1.0 rgb(228, 228, 228); div.sc-6edd2c8c-4.dIWIRl 1152.0x81.0 rgb(231, 231, 231) 0px -1px 0px 0px inset; div.sc-6edd2c8c-4.dIWIRl 1152.0x81.0 rgb(231, 231, 231) 0px -1px 0px 0px inset; div.sc-6edd2c8c-4.dIWIRl 1152.0x81.0 rgb(231, 231, 231) 0px -1px 0px 0px inset; div.sc-6edd2c8c-4.dIWIRl 1152.0x81.0 rgb(231, 231, 231) 0px -1px 0px 0px inset; div.sc-6edd2c8c-4.dI.

Child layers that carry the look: hr 1152x1 background #e4e4e4; div 1152x81 shadow #e7e7e7 0px -1px 0px 0px inset; div 1152x81 shadow #e7e7e7 0px -1px 0px 0px inset.

![FAQ block default](components/crops/faq-block-default.png)

#### Internal link
A related-cuisine link in the footer SEO block. Read as `internal-link` on the restaurants-near-me page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 91.98 x 22; background transparent; text DD Norms 16/22 500, #191919 `color.neutral.100` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.itninwi 92.0x22.0 1px auto rgb(0, 95, 204) offset 1px |

![Internal link default](components/crops/internal-link-default.png) ![Internal link hover](components/crops/internal-link-hover.png) ![Internal link focus-visible](components/crops/internal-link-focus-visible.png) ![Internal link pressed](components/crops/internal-link-pressed.png)

### Fields, search and gates

The native language select, the address-search gate (measured and focused, never submitted), catalog search fields and the cookie banner (measured then re-hidden, never answered).

#### Cookie banner
The consent strip, measured then re-hidden — never answered. Read as `cookie-banner` on the restaurant storefront page.

**Values (default).** size 1440 x 98; background #f7f7f7 `color.neutral.0`; text DD Norms 16/22 500, #191919 `color.neutral.100`; icon 24 x 24, #000000 `color.black`.

![Cookie banner default](components/crops/cookie-banner-default.png)

#### Search input
The catalog search field on the HSA/FSA store; focused only, nothing submitted. Read as `hsa-search` on the HSA/FSA store page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 788.78 x 32; background transparent; text browser default (Times 16/normal 400, #000000); icon 24 x 24, #191919 `color.neutral.100`; layers div::before.sc-b40f2357-2.fsoSKH calc(100% - 16px)x64px rgb(255, 255, 255) T:1px solid rgb(214, 214, 214) / R:1px solid rgb(214, 214, 214) / L:1px solid rgb(214, 214, 214) 20px 20px 0px 0px; div.InputContainer-sc-5yzsia-1.cIaZpF 756.8x32.0 rgb(247, 247, 247) rgb(247, 247, 247) 0px 0px 0px 1px inset 20px; div.InputContentContainerInternal-sc-5yzsia-2.gUKLGr 698.8x20.0 rgb(247, 247, 247); input.Inpu |
| focused | layers div::before.sc-b40f2357-2.fsoSKH calc(100% - 16px)x64px rgb(255, 255, 255) T:1px solid rgb(214, 214, 214) / R:1px solid rgb(214, 214, 214) / L:1px solid rgb(214, 214, 214) 20px 20px 0px 0px; div.InputContainer-sc-5yzsia-1.cIaZpF 756.8x32.0 rgb(247, 247, 247) rgb(25, 25, 25) 0px 0px 0px 2px inset 20px; div.InputContentContainerInternal-sc-5yzsia-2.gUKLGr 698.8x20.0 rgb(247, 247, 247); input.InputCo |

Child layers that carry the look: div::before calc(100% - 16px)x64px background #ffffff `color.white` border 1px solid #d6d6d6 `color.neutral.10` radius 20px 20px 0px 0px; div 756.8x32 background #f7f7f7 `color.neutral.0` radius 20px shadow #f7f7f7 `color.neutral.0` 0px 0px 0px 1px inset; div 698.8x20 background #f7f7f7 `color.neutral.0`.

![Search input default](components/crops/hsa-search-default.png) ![Search input focused](components/crops/hsa-search-focused.png)

#### Delivery/Pickup toggle
Read as `hsa-toggle` on the HSA/FSA store page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 155.3 x 38; background transparent; text DD Norms 14/20 700, #191919 `color.neutral.100`; layers div.SelectGroupContainer-sc-pcky6n-3.ia-DbeS 155.3x38.0 rgb(241, 241, 241) T:1px solid rgb(241, 241, 241) / R:1px solid rgb(241, 241, 241) / B:1px solid rgb(241, 241, 241) / L:1px solid rgb(241, 241, 241) 9999px; div.SelectGroupButtonIndicator-sc-pcky6n-1.VcJuC 78.5x32.0 rgb(255, 255, 255) rgb(228, 228, 228) 0px 0px 0px 2px inset, rgba(25, 25, 25, 0) 0px 0px 0px 0px 9999px |
| hover | layers div.SelectGroupContainer-sc-pcky6n-3.ia-DbeS 155.3x38.0 rgb(241, 241, 241) T:1px solid rgb(241, 241, 241) / R:1px solid rgb(241, 241, 241) / B:1px solid rgb(241, 241, 241) / L:1px solid rgb(241, 241, 241) 9999px; button.SelectGroupButton-sc-pcky6n-2.hnRBpa 78.5x32.0 rgb(241, 241, 241) 9999px; div.SelectGroupButtonIndicator-sc-pcky6n-1.VcJuC 78.5x32.0 rgb(241, 241, 241) rgb(214, 214, 214) 0px 0px 0 |
| focus-visible | layers div.SelectGroupContainer-sc-pcky6n-3.ia-DbeS 155.3x38.0 rgb(241, 241, 241) T:1px solid rgb(241, 241, 241) / R:1px solid rgb(241, 241, 241) / B:1px solid rgb(241, 241, 241) / L:1px solid rgb(241, 241, 241) 9999px; button.SelectGroupButton-sc-pcky6n-2.hnRBpa 78.5x32.0 1px auto rgb(0, 95, 204) offset 0px 9999px; div.SelectGroupButtonIndicator-sc-pcky6n-1.VcJuC 78.5x32.0 rgb(255, 255, 255) rgb(228, 22 |

Child layers that carry the look: div 155.3x38 background #f1f1f1 `color.neutral.5` border 1px solid #f1f1f1 `color.neutral.5` radius 9999px; div 78.5x32 background #ffffff `color.white` radius 9999px shadow #e4e4e4 0px 0px 0px 2px inset, rgba(25, 25, 25, 0) 0px 0px 0px 0px.

![Delivery/Pickup toggle default](components/crops/hsa-toggle-default.png) ![Delivery/Pickup toggle hover](components/crops/hsa-toggle-hover.png) ![Delivery/Pickup toggle focus-visible](components/crops/hsa-toggle-focus-visible.png) ![Delivery/Pickup toggle pressed](components/crops/hsa-toggle-pressed.png)

#### Promo page title
The HSA/FSA store headline. Read as `hsa-h1` on the HSA/FSA store page.

Not on the page when it was captured.

#### Address field (gate)
The landing-page address search — the entry point the whole consumer flow is gated behind. Focused only; nothing typed or submitted. Read as `address-field` on the promo codes page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 408 x 56; background transparent; text DD-TTNorms 16/normal 400, #000000 `color.black`; icon 24 x 24, #191919 `color.neutral.100`; layers div.InputContainer-sc-5yzsia-1.gBQgMf 408.0x56.0 rgb(247, 247, 247) rgb(247, 247, 247) 0px 0px 0px 1px inset 32px; div.InputContentContainer-sc-5yzsia-2.cKgGCJ 292.0x22.0 rgb(247, 247, 247); input.InputContent-sc-5yzsia-4.eLKfvL 292.0x22.0 rgb(247, 247, 247); button.ButtonRootInternal-sc-j2wkqj-0.bHBHib 40.0x40.0 rgb(235, 23, 0) rgba(25, 25, 25, 0) 0px 0px 0px 1px inset 9999px |
| focused | layers div.InputContainer-sc-5yzsia-1.gBQgMf 408.0x56.0 rgb(247, 247, 247) rgb(25, 25, 25) 0px 0px 0px 2px inset 32px; div.InputContentContainer-sc-5yzsia-2.cKgGCJ 292.0x22.0 rgb(247, 247, 247); input.InputContent-sc-5yzsia-4.eLKfvL 292.0x22.0 rgb(247, 247, 247); button.ButtonRootInternal-sc-j2wkqj-0.bHBHib 40.0x40.0 rgb(235, 23, 0) rgba(25, 25, 25, 0) 0px 0px 0px 1px inset 9999px |

Child layers that carry the look: div 408x56 background #f7f7f7 `color.neutral.0` radius 32px shadow #f7f7f7 `color.neutral.0` 0px 0px 0px 1px inset; div 292x22 background #f7f7f7 `color.neutral.0`; input 292x22 background #f7f7f7 `color.neutral.0`.

![Address field (gate) default](components/crops/address-field-default.png) ![Address field (gate) focused](components/crops/address-field-focused.png)

#### Identity button
The header Sign-in/sign-up identity control; measured, never followed. Read as `identity-btn` on the promo codes page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 204.55 x 32; radius 9999px; background #f1f1f1 `color.neutral.5`; shadow #f1f1f1 0px 0px 0px 1px inset; text DD Norms 14/20 700, #191919 `color.neutral.100`; transition background-color 0.2s cubic-bezier(0.4, 0.4, 0, 1), box-shadow 0.2s cubic-bezier(0.4, 0.4, 0, 1); icon 16 x 24, #191919 `color.neutral.100` |
| hover | background #d6d6d6 `color.neutral.10`; shadow #d6d6d6 0px 0px 0px 1px inset; text DD Norms 14/20 700, #242424 `color.neutral.95`; transition background-color 0.05s linear, box-shadow 0.05s linear; icon 16 x 24, #242424 `color.neutral.95` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #c4c4c4 `color.neutral.20`; shadow #c4c4c4 0px 0px 0px 1px inset; text DD Norms 14/20 700, #313131 `color.neutral.90`; transition background-color 0.05s linear, box-shadow 0.05s linear; icon 16 x 24, #313131 `color.neutral.90` |

![Identity button default](components/crops/identity-btn-default.png) ![Identity button hover](components/crops/identity-btn-hover.png) ![Identity button focus-visible](components/crops/identity-btn-focus-visible.png) ![Identity button pressed](components/crops/identity-btn-pressed.png)

#### Landing link
Read as `landing-link` on the promo codes page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1120 x 318; background transparent; text DD Norms 16/22 500, #ffffff `color.white` |
| focus-visible | layers a.sc-6c4a270f-12.hhhwiM 176.7x20.0 1px auto rgb(0, 95, 204) offset 1px |

![Landing link default](components/crops/landing-link-default.png) ![Landing link hover](components/crops/landing-link-hover.png) ![Landing link focus-visible](components/crops/landing-link-focus-visible.png) ![Landing link pressed](components/crops/landing-link-pressed.png)

### Footer

The marketing footer: link columns, app-store badges, language select and social links.

#### Footer
The footer: link columns, store badges, language select, socials, legal. Read as `footer` on the home page.

**Values (default).** size 1160 x 952; padding 0px 20px; background transparent; text DD Norms 16/22 500, #ffffff `color.white`; layers div.sc-6c4a270f-15.behXqC 160.0x52.0 rgb(73, 73, 73) 8px; div.sc-6c4a270f-15.behXqC 160.0x52.0 rgb(73, 73, 73) 8px; div.InputContainer-sc-5yzsia-1.futmdp 150.0x32.0 rgb(241, 241, 241) rgb(228, 228, 228) 0px 0px 0px 1px inset 16px; div.InputContentContainerInternal-sc-5yzsia-2.gUKLGr 94.0x20.0 rgb(241, 241, 241); div.SelectContainer-sc-1wilwzz-0.khtfio 94.0x20.0 rgb(241, 241, 241); select.SelectEle.

Child layers that carry the look: div 160x52 background #494949 `color.neutral.80` radius 8px; div 160x52 background #494949 `color.neutral.80` radius 8px; div 150x32 background #f1f1f1 `color.neutral.5` radius 16px shadow #e4e4e4 0px 0px 0px 1px inset.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 114.11 x 20; background transparent; text DD Norms 14/20 500, #c4c4c4 `color.neutral.20`; transition filter 0.2s ease |
| hover | text DD Norms 14/20 500, #ffffff `color.white` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.sc-6c4a270f-12.hhhwiM 114.1x20.0 1px auto rgb(0, 95, 204) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Store badge
The App Store / Google Play badge links. Read as `appstore-badge` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 160 x 52; background transparent; text browser default (Times 16/normal 400, #000000); transition opacity 0.2s ease; opacity 0.7; layers div.sc-6c4a270f-15.behXqC 160.0x52.0 rgb(73, 73, 73) 8px |
| hover | opacity none |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.sc-6c4a270f-14.fSugZ 160.0x52.0 1px auto rgb(0, 95, 204) offset 1px; div.sc-6c4a270f-15.behXqC 160.0x52.0 rgb(73, 73, 73) 8px |
| pressed | opacity none |

Child layers that carry the look: div 160x52 background #494949 `color.neutral.80` radius 8px.

![Store badge default](components/crops/appstore-badge-default.png) ![Store badge hover](components/crops/appstore-badge-hover.png) ![Store badge focus-visible](components/crops/appstore-badge-focus-visible.png) ![Store badge pressed](components/crops/appstore-badge-pressed.png)

#### Social button
A social-media icon link in the footer. Read as `social-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 32; background transparent; text browser default (Times 16/normal 400, #000000); transition opacity 0.2s ease; opacity 0.7; icon 24 x 24, #000000 `color.black` |
| hover | opacity none |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.sc-6c4a270f-14.fSugZ 24.0x32.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | opacity none |

![Social button default](components/crops/social-btn-default.png) ![Social button hover](components/crops/social-btn-hover.png) ![Social button focus-visible](components/crops/social-btn-focus-visible.png) ![Social button pressed](components/crops/social-btn-pressed.png)

### Careers site (WordPress stack)

careersatdoordash.com — a separate WordPress/Tailwind stack (bg-pinot-noir, .btn pills), not the prism consumer system; measured only for context.

#### Careers header
The careersatdoordash.com header — a separate WordPress/Tailwind stack (bg-pinot-noir, .btn), not the prism consumer system. Read as `car-header` on the careers page.

**Values (default).** size 1440 x 80; background #ffffff `color.white`; text Tt norms pro 14/21 700, #4c0c3a.

![Careers header default](components/crops/car-header-default.png)

#### Careers headline
Read as `car-h1` on the careers page.

**Values (default).** size 181 x 21.16; background transparent; text TT Norms Pro Cond 16/24 900, #4c0c3a.

![Careers headline default](components/crops/car-h1-default.png)

#### Careers button
A .btn pill on the WordPress careers theme. Read as `car-btn` on the careers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 127.27 x 42; padding 12px 20px; border 1px solid #ff3008; radius 3.35544e+07px; background #ff3008; text Tt norms pro 16/16 700, #ffffff `color.white`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #cc0000; background #cc0000 |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | border 1px solid #cc0000; background #cc0000 |

![Careers button default](components/crops/car-btn-default.png) ![Careers button hover](components/crops/car-btn-hover.png) ![Careers button focus-visible](components/crops/car-btn-focus-visible.png) ![Careers button pressed](components/crops/car-btn-pressed.png)

#### Careers nav link
Read as `car-nav-link` on the careers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 117.75 x 37; padding 8px 20px; radius 3.35544e+07px; background #ff3008; text Tt norms pro 14/21 700, #ffffff `color.white`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #cc0000 |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #cc0000 |

![Careers nav link default](components/crops/car-nav-link-default.png) ![Careers nav link hover](components/crops/car-nav-link-hover.png) ![Careers nav link focus-visible](components/crops/car-nav-link-focus-visible.png) ![Careers nav link pressed](components/crops/car-nav-link-pressed.png)

### Mobile (390 wide)

The marketing home at phone width: the compact top bar and stacked hero.

#### Mobile top bar
Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 390 x 600; padding 0px 8px; background transparent; image url(…); text TTNormsProCond-Blk 22/28 900, #ffffff `color.white`; icon 42 x 24, #000000 `color.black`.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile identity button
The combined sign-in/sign-up control at 390 wide. Read as `m-identity-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 390 x 40; padding 0px 24px 0px 16px; background transparent; text DD Norms 18/22 800, #ffffff `color.white`; layers a.ButtonRoot-sc-j2wkqj-0.iLCINK 82.4x40.0 rgb(235, 23, 0) rgba(25, 25, 25, 0) 0px 0px 0px 1px inset 9999px; a.ButtonRoot-sc-j2wkqj-0.iLCINK 90.5x40.0 rgb(255, 255, 255) rgba(25, 25, 25, 0) 0px 0px 0px 1px inset 9999px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: a 82.4x40 background #eb1700 `color.brand.doordash.60` radius 9999px shadow rgba(25, 25, 25, 0) 0px 0px 0px 1px inset; a 90.5x40 background #ffffff `color.white` radius 9999px shadow rgba(25, 25, 25, 0) 0px 0px 0px 1px inset.

![Mobile identity button default](components/crops/m-identity-btn-default.png) ![Mobile identity button hover](components/crops/m-identity-btn-hover.png) ![Mobile identity button pressed](components/crops/m-identity-btn-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 350 x 56; background transparent; text TTNormsProCond-Blk 22/28 900, #ffffff `color.white`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the DoorDash wordmark, social glyphs, store badges, product illustrations and the storefront imagery) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

DoorDash's product — the consumer ordering flow, restaurant browsing past the address gate, cart, checkout, DashPass membership, merchant dashboard and Dasher app — lives behind sign-in or the address search and was never reached. Every Sign-in, Sign-up, cart, quick-add, group-order and address action was measured, never followed. Identity anchors point at identity.doordash.com OAuth and were never clicked.

### Live access

- **Cloudflare gating.** Every live *.doordash.com surface tried on 2026-11-13 (home, /about/, /careers/, /merchant/, /dasher/, /en-US, /business/, merchants.doordash.com, dasher.doordash.com, help.doordash.com, plus robots.txt and the favicon) answered a 403 managed challenge — 'Performing security verification' — that never resolved in headless Chromium, new-headless or headed Chrome. The Wayback Machine holds the product's own SSR output, which is what this package captures; every page is labelled with its snapshot id in [raw/archive-urls.json](raw/archive-urls.json).
- **What 'archived' means here.** The DOM, stylesheets and token layer are the product's own; the Wayback Machine proxies them and injects its toolbar (hidden in every shot). Images served from img.cdn4dd.com render live because that CDN is not gated. Nothing is presented as a current live capture.

### Pages

- **Behind the address gate.** The consumer browsing experience past 'enter your address' — local restaurant lists, personalised carousels, delivery times and fees — requires a real address or sign-in and was never entered; a generic landmark was not tried either, because the gate's submit would place state on the session.
- **Ordering and checkout.** The menu item's quick-add, cart, group-cart and every checkout step were measured or left unpressed: a press would start a cart.
- **Merchant and Dasher onboarding.** merchants.doordash.com and dasher.doordash.com are Cloudflare-gated live and had no usable Wayback captures; the marketing links that reach them are present but their signup wizards are uncaptured.
- **Store directory pages.** /en-US/store/… pages are public once a store slug is known; one real storefront (The Sweet Tooth, North Miami Beach) was captured. Other stores' pages exist but were not enumerated.
- **Sign-in and sign-up.** The anchors point at identity.doordash.com/auth with signed state parameters; the OAuth flow was never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** exist richly in the --comp-* token layer (…-disabled, …-progressing) and were tokenised from the declarations; the public surface rarely paints them.
- **Browser defaults in the replay.** Elements the site styles only through their text children kept the browser's inherited defaults in the Wayback replay: Times 16px, #000000 text and the #0000ee link blue on anchors and the icons inside them. An entry whose text reads "browser default (...)" or whose icon is marked as the browser's link colour shows that, not a DoorDash value; the component tokens take their text colour from the first text node instead.
- **Hydration.** The archived pages are the SSR output; React hydration may not complete under Wayback, so lazy content that mounts after hydration (extra directory rows, some imagery) can be absent from a shot — the DOM and styles that did render are real.

### Themes

The prism consumer system publishes one light theme on this surface: no `.dark` scope, no `data-theme` attribute and no `prefers-color-scheme` bindings appear in the captured sheets, so there is no dark set — one is not inferred.

### Fonts

- **DD Norms** (proprietary; families `--base-font-family-default/brand/condensed`, weights 300-800, a 28-step px size scale) is the prism face, served from web-assets.cdn4dd.com; **TTNormsProCond-Blk** at weight 900 is the campaign display face set inline on hero headlines. The careers site's WordPress theme loads its own faces. The style guide falls back to system sans.

### Screenshots

- Product photography (the hero flat-lay, restaurant imagery), the DoorDash wordmark and merchant logos in the screenshots are the product's published content, rendered from the archive.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, restaurant names, menus and prices are the product's content; only frames and components were measured.
