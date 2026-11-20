# Craftwork components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from craftwork.design on 2026-11-12, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, submitted or paid for; the nav theme toggle was flipped to dark and back for one shot, the OTP email field was filled and cleared but Send code was never pressed, and Connect agent, Get full access, every plan CTA and the Google button were never followed. The fixed cookie notice was hidden, never answered.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (36 components, 96 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (92 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-dark-default.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Components | `/components` | [default](screenshots/components-light-default.png), [full](screenshots/components-light-full.png) |
| Catalog | `/catalog` | [default](screenshots/catalog-light-default.png), [full](screenshots/catalog-light-full.png) |
| Black Friday deal | `/black-friday` | [default](screenshots/deal-light-default.png), [full](screenshots/deal-light-full.png) |
| Login | `/login` | [default](screenshots/login-light-default.png), [filled](screenshots/login-light-filled.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-menu-row) |
| Dark theme | home | the nav theme toggle (aria-label Dark theme) — flipped for the shot, flipped back | [home-dark-default](screenshots/home-dark-default.png), [theme-toggle](#theme-toggle) |
| OTP form, filled | /login | the email field filled with a placeholder and cleared — Send code never pressed | [login-light-filled](screenshots/login-light-filled.png), [login-field](#email-field) |
| Cookie notice | every page | hidden via the generic overlay hider, never answered | not captured |
| The signed-in library | accounts, purchases | Sign in leads to the OTP card; Pro purchase and every download were never used | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 19 components were given a real keyboard focus. 16 draw an outline ring: `nav-link` (2px solid #606060, offset 2px), `search-field` (2px solid #606060, offset 2px), `theme-toggle` (2px solid #606060, offset 2px), `signin-link` (2px solid #606060, offset 2px), `connect-cta` (2px solid #606060, offset 2px), `hero-cta` (2px solid #606060, offset 2px), `hero-cta-2` (2px solid #606060, offset 2px), `product-card` (2px solid #606060, offset 2px), `faq-row` (2px solid #000000 `color.brand.logo`, offset 2px), `catalog-card` (on a child: 1px auto rgb(0, 95, 204) offset 1px), `google-btn` (1px auto #005fcc, offset 0px), `footer-link` (2px solid #606060, offset 2px), `social-icon` (2px solid #606060, offset 2px), `m-menu-button` (2px solid #606060, offset 2px), `m-nav-item` (2px solid #606060, offset 2px), `library-row` (1px auto #005fcc, offset 1px). The other 3 show no measured change: `components-filter`, `catalog-filter`, `login-field`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color, transform | footer-link, m-nav-item, nav-link, search-field, social-icon |
| 0.18s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, color, transform | m-menu-button, signin-link, theme-toggle |
| 0.18s | `ease` | background-color, color | library-row |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | promo-banner |
| 0.3s | `cubic-bezier(0, 0, 0.2, 1)` | all, transform | connect-cta, hero-cta, hero-cta-2 |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | google-btn, send-code |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 547.19 x 340 | - | - | transparent | none | 24px 0px 0px 0px |

## Components

### Shell and navigation

The #161616 Black Friday countdown bar (36px) sits above the 60px nav: the craftwork wordmark, Assets / Templates / Inspiration dropdowns, the 350px #fafafa search pill with the CMD-K hint, Pricing, the 32px theme toggle, Sign in and the 30px #1e1e1e Connect agent pill.

#### Promo banner
The Black Friday countdown bar above the nav ("Lifetime Pro for $224 instead of $449 · Ends in · See the deal"). Read as `promo-banner` on the home page.

**Values (default).** size 1440 x 36; padding 0px 16px; background #161616; text euclidCircularALightWebS 13/19.5 500, #f2f2f2; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, #f2f2f2.

![Promo banner default](components/crops/promo-banner-default.png)

#### Nav bar
The top bar: craftwork logo, Assets/Templates/Inspiration dropdowns, search, Pricing, theme toggle, Sign in and the black Connect agent pill. Read as `nav` on the home page.

**Values (default).** size 1440 x 60; background transparent; text euclidCircularALightWebS 20/20 600, #000000 `color.brand.logo`; icon 26 x 26, #000000 `color.brand.logo`; layers span.pointer-events-none.absolute 0.0x36.0 rgba(0, 0, 0, 0.07) 8px; div.absolute.left-0 892.4x502.5 rgba(255, 255, 255, 0.9) rgba(0, 0, 0, 0.14) 0px 12px 28px -8px, rgba(0, 0, 0, 0.22) 0px 30px 70px -24px 24px; a.flex.items-center 201.8x34.9 rgba(127, 127, 127, 0.14) 12px; div.border-t.border-other-stroke 201.8x47.5 T:1px solid rgba(0, 0, 0, 0.098); span.relative.block 206.9x155.2 rgba(127, 127, 1.

Child layers that carry the look: span 0x36 background rgba(0, 0, 0, 0.07) radius 8px; div 892.4x502.5 background rgba(255, 255, 255, 0.9) radius 24px shadow rgba(0, 0, 0, 0.14) 0px 12px 28px -8px, rgba(0, 0, 0, 0.22) 0px 30px 70px -24px; a 201.8x34.9 background rgba(127, 127, 127, 0.14) radius 12px.

![Nav bar default](components/crops/nav-default.png)

#### Logo
The craftwork wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 128.78 x 34; padding 4px; radius 6px; background transparent; text euclidCircularALightWebS 20/20 600, #000000 `color.brand.logo`; icon 26 x 26, #000000 `color.brand.logo`.

![Logo default](components/crops/logo-default.png)

#### Nav link
A nav item (36px h-9 row); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 83.2 x 36; padding 0px 6px 0px 10px; radius 8px; background transparent; text euclidCircularALightWebS 16/22 400, #606060; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #606060 |
| hover | text euclidCircularALightWebS 16/22 400, #000000 `color.brand.logo`; icon 16 x 16, #000000 `color.brand.logo` |
| focus-visible | outline 2px solid #606060, offset 2px; layers button.relative.z-10 83.2x36.0 2px solid rgb(96, 96, 96) offset 2px 8px |
| pressed | size 80.71 x 34.92; text euclidCircularALightWebS 16/22 400, #000000 `color.brand.logo`; transform scale(0.97); icon 15.52 x 15.52, #000000 `color.brand.logo` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Search field
The nav search field with the CMD-K hint; opens a search overlay, never typed into. Read as `search-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 350 x 38; padding 0px 8px 0px 12px; radius 9999px; background #fafafa; text euclidCircularALightWebS 16/22 400, #999999; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 18 x 18, #999999 |
| hover | background rgba(237, 237, 237, 0.698) |
| focus-visible | outline 2px solid #606060, offset 2px |
| pressed | background rgba(237, 237, 237, 0.698) |

![Search field default](components/crops/search-field-default.png) ![Search field hover](components/crops/search-field-hover.png) ![Search field focus-visible](components/crops/search-field-focus-visible.png) ![Search field pressed](components/crops/search-field-pressed.png)

#### Theme toggle
The nav theme switch (aria-label "Dark theme"): flips data-theme between the painted light and dark surfaces. Read as `theme-toggle` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 8px; background transparent; text euclidCircularALightWebS 16/24 400, #000000 `color.brand.logo`; transition background-color 0.18s cubic-bezier(0.4, 0, 0.2, 1), color 0.18s cubic-bezier(0.4, 0, 0.2, 1), transform 0.18s cubic-bezier(0.4, 0, 0.2, 1); icon 18 x 18, #000000 `color.brand.logo` |
| hover | background rgba(0, 0, 0, 0.07) |
| focus-visible | outline 2px solid #606060, offset 2px; layers button.flex.size-11 32.0x32.0 2px solid rgb(96, 96, 96) offset 2px 8px |
| pressed | size 31.04 x 31.04; background rgba(0, 0, 0, 0.1); transform scale(0.97); icon 17.46 x 17.46, #000000 `color.brand.logo` |

![Theme toggle default](components/crops/theme-toggle-default.png) ![Theme toggle hover](components/crops/theme-toggle-hover.png) ![Theme toggle focus-visible](components/crops/theme-toggle-focus-visible.png) ![Theme toggle pressed](components/crops/theme-toggle-pressed.png)

#### Sign-in link
The "Sign in" nav link (leads to /login); measured, never followed. Read as `signin-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 71.39 x 36; padding 0px 12px; radius 8px; background transparent; text euclidCircularALightWebS 16/22 400, #606060; transition background-color 0.18s cubic-bezier(0.4, 0, 0.2, 1), color 0.18s cubic-bezier(0.4, 0, 0.2, 1), transform 0.18s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(0, 0, 0, 0.07); text euclidCircularALightWebS 16/22 400, #000000 `color.brand.logo` |
| focus-visible | outline 2px solid #606060, offset 2px; layers button.inline-flex.h-11 71.4x36.0 2px solid rgb(96, 96, 96) offset 2px 8px |
| pressed | size 69.25 x 34.92; background rgba(0, 0, 0, 0.1); text euclidCircularALightWebS 16/22 400, #000000 `color.brand.logo`; transform scale(0.97) |

![Sign-in link default](components/crops/signin-link-default.png) ![Sign-in link hover](components/crops/signin-link-hover.png) ![Sign-in link focus-visible](components/crops/signin-link-focus-visible.png) ![Sign-in link pressed](components/crops/signin-link-pressed.png)

#### Connect agent pill
The black "Connect agent" nav pill; measured, never followed. Read as `connect-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 126.98 x 30; padding 0px 8px; radius 8px; background #1e1e1e `color.toast.default-bg`; text euclidCircularALightWebS 16/22 500, #ffffff `color.toast.default-fg`; transition transform 0.3s cubic-bezier(0, 0, 0.2, 1) |
| hover | background #383838; transform translate(0px, -1px) |
| focus-visible | outline 2px solid #606060, offset 2px |
| pressed | background #000000 `color.brand.logo`; transform translate(0px, -1px) |

![Connect agent pill default](components/crops/connect-cta-default.png) ![Connect agent pill hover](components/crops/connect-cta-hover.png) ![Connect agent pill focus-visible](components/crops/connect-cta-focus-visible.png) ![Connect agent pill pressed](components/crops/connect-cta-pressed.png)

### Home

The 68px Euclid hero ("UI kits, templates and fonts made by real designers"), the 46px #1e1e1e Get full access and #efefef Browse the catalog buttons, and the product-card rail with "from $N" prices.

#### Hero headline
The 68px Euclid Circular hero ("UI kits, templates and fonts made by real designers"). Read as `hero-h1` on the home page.

**Values (default).** size 835.84 x 141.44; background transparent; text euclidCircularALightWebS 68/70.72 600, #000000 `color.brand.logo`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero subline
"4,000+ packs for Figma, Framer, Webflow and code by 570+ independent designers." Read as `hero-sub` on the home page.

**Values (default).** size 544 x 60; background transparent; text euclidCircularALightWebS 20/30 400, #606060.

![Hero subline default](components/crops/hero-sub-default.png)

#### Hero CTA
The black "Get full access" hero button (leads to pricing); measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 178.52 x 46; padding 0px 20px; radius 10px; background #1e1e1e `color.toast.default-bg`; text euclidCircularALightWebS 16/22 500, #ffffff `color.toast.default-fg`; transition all 0.3s cubic-bezier(0, 0, 0.2, 1); icon 24 x 24, #ffffff `color.toast.default-fg` |
| hover | background #383838; shadow rgba(0, 0, 0, 0.45) 0px 10px 24px -12px; transform translate(0px, -2px) |
| focus-visible | outline 2px solid #606060, offset 2px |
| pressed | size 174.95 x 45.08; background #000000 `color.brand.logo`; shadow rgba(0, 0, 0, 0.45) 0px 10px 24px -12px; transform matrix(0.98, 0, 0, 0.98, 0, -2); icon 23.52 x 23.52, #ffffff `color.toast.default-fg` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero secondary
The light "Browse the catalog" hero button; measured, never followed. Read as `hero-cta-2` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 181.02 x 46; padding 0px 20px; radius 10px; background #efefef; text euclidCircularALightWebS 16/22 500, #000000 `color.brand.logo`; transition all 0.3s cubic-bezier(0, 0, 0.2, 1) |
| hover | background #e1e1e1; shadow rgba(255, 255, 255, 0.08) 0px 1px 0px 0px inset |
| focus-visible | outline 2px solid #606060, offset 2px |
| pressed | size 177.4 x 45.08; background #e1e1e1; shadow rgba(255, 255, 255, 0.08) 0px 1px 0px 0px inset; transform scale(0.98) |

![Hero secondary default](components/crops/hero-cta-2-default.png) ![Hero secondary hover](components/crops/hero-cta-2-hover.png) ![Hero secondary focus-visible](components/crops/hero-cta-2-focus-visible.png) ![Hero secondary pressed](components/crops/hero-cta-2-pressed.png)

#### Product card
A catalog product card in the home rail (artwork, name, "from $N" price); measured, never followed. Read as `product-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 362.67 x 311; background transparent; outline 2px solid transparent, offset 2px; text euclidCircularALightWebS 18/22 500, #000000 `color.brand.logo`; layers a.group.block 362.7x311.0 2px solid rgba(0, 0, 0, 0) offset 2px; div.absolute.w-full 362.7x272.0 T:1px solid rgba(0, 0, 0, 0.1) / R:1px solid rgba(0, 0, 0, 0.1) / B:1px solid rgba(0, 0, 0, 0.1) / L:1px solid rgba(0, 0, 0, 0.1) 10px |
| focus-visible | outline 2px solid #606060, offset 2px; layers a.group.block 362.7x311.0 2px solid rgb(96, 96, 96) offset 2px; span.block.group-focus-visible:rounded-[10px] 362.7x272.0 2px solid rgb(96, 96, 96) offset 2px 10px; div.absolute.w-full 362.7x272.0 T:1px solid rgba(0, 0, 0, 0.1) / R:1px solid rgba(0, 0, 0, 0.1) / B:1px solid rgba(0, 0, 0, 0.1) / L:1px solid rgba(0, 0, 0, 0.1) 10px |

Child layers that carry the look: a 362.7x311; div 362.7x272 border 1px solid rgba(0, 0, 0, 0.1) radius 10px.

![Product card default](components/crops/product-card-default.png) ![Product card hover](components/crops/product-card-hover.png) ![Product card focus-visible](components/crops/product-card-focus-visible.png) ![Product card pressed](components/crops/product-card-pressed.png)

### Pricing

The /pricing surface: "Browse for free. Go Pro to use it all.", the plan cards with 40px price figures and the 68px FAQ accordion rows.

#### Pricing headline
"Browse for free. Go Pro to use it all." Read as `price-h1` on the pricing page.

**Values (default).** size 500.97 x 132; background transparent; text euclidCircularALightWebS 62/66 600, #000000 `color.brand.logo`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Plan card
A pricing plan card (name, price, feature list, CTA); measured, never purchased. Read as `plan-card` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 547.19 x 340; padding 24px 0px 0px 0px; background transparent; text euclidCircularALightWebS 14/21 400, #606060; icon 16 x 16, #ffffff `color.toast.default-fg`; layers span.pointer-events-none.absolute 437.8x192.0 rgba(0, 0, 0, 0.03) 9999px; span.absolute.inset-0 419.2x224.3 rgb(244, 244, 244) T:1px solid rgba(0, 0, 0, 0.1) / R:1px solid rgba(0, 0, 0, 0.1) / B:1px solid rgba(0, 0, 0, 0.1) / L:1px solid rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.45) 0px 24px 48px -16px 14px; span.absolute.inset-0 455.9x2 |
| hover | layers span.pointer-events-none.absolute 437.8x192.0 rgba(0, 0, 0, 0.03) 9999px; span.absolute.inset-0 416.5x230.0 rgb(244, 244, 244) T:1px solid rgba(0, 0, 0, 0.1) / R:1px solid rgba(0, 0, 0, 0.1) / B:1px solid rgba(0, 0, 0, 0.1) / L:1px solid rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.45) 0px 24px 48px -16px 14px; span.absolute.inset-0 451.6x2 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: span 437.8x192 background rgba(0, 0, 0, 0.03) radius 9999px; span 419.2x224.3 background #f4f4f4 border 1px solid rgba(0, 0, 0, 0.1) radius 14px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.45) 0px 24px 48px -16px; span 455.9x244.5 background #f4f4f4 border 1px solid rgba(0, 0, 0, 0.1) radius 14px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.45) 0px 24px 48px -16px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Plan price
A plan price figure. Read as `plan-price` on the pricing page.

**Values (default).** size 388 x 44; background transparent; text euclidCircularALightWebS 40/44 600, #000000 `color.brand.logo`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### FAQ row
A pricing FAQ accordion row; toggled locally, never submitted. Read as `faq-row` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 572 x 68; padding 20px 0px; background transparent; text euclidCircularALightWebS 17/24 500, #000000 `color.brand.logo`; icon 22.63 x 22.63, #ffffff `color.toast.default-fg`; layers span.flex.size-7 39.6x39.6 rgb(30, 30, 30) 9999px |
| focus-visible | outline 2px solid #000000 `color.brand.logo`, offset 2px; layers button.group.flex 572.0x68.0 2px solid rgb(0, 0, 0) offset 2px; span.flex.size-7 39.6x39.6 rgb(30, 30, 30) 9999px |

Child layers that carry the look: span 39.6x39.6 background #1e1e1e `color.toast.default-bg` radius 9999px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Catalog

The /components and /catalog surfaces: the 157/193px filter fields, the 34px library rows with live counts and the asset grid. /components' h1 ("Components, 1,224") is a 1x1 accessibility heading.

#### Components headline
"Components, 1,224" — the catalog count heading. Read as `components-h1` on the components page.

**Values (default).** size 1 x 1; background transparent; text euclidCircularALightWebS 16/24 400, #000000 `color.brand.logo`.

![Components headline default](components/crops/components-h1-default.png)

#### Filter field
A catalog filter/search input; measured in place, never submitted. Read as `components-filter` on the components page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 157 x 30; padding 0px 8px; background transparent; outline 2px solid transparent, offset 2px; text euclidCircularALightWebS 14/20 400, #000000 `color.brand.logo`; placeholder #999999; layers input.h-full.w-full 157.0x30.0 2px solid rgba(0, 0, 0, 0) offset 2px |
| focus-visible | placeholder transparent |
| filled | size 135 x 30; placeholder transparent; layers input.h-full.w-full 135.0x30.0 2px solid rgba(0, 0, 0, 0) offset 2px |

Child layers that carry the look: input 157x30.

![Filter field default](components/crops/components-filter-default.png) ![Filter field focus-visible](components/crops/components-filter-focus-visible.png) ![Filter field filled](components/crops/components-filter-filled.png)

#### Catalog card
An asset card in the catalog grid; measured, never followed. Read as `components-card` on the components page.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Catalog headline
"Assets" — the catalog heading. Read as `catalog-h1` on the catalog page.

**Values (default).** size 472.38 x 47.52; background transparent; text euclidCircularALightWebS 44/47.52 600, #000000 `color.brand.logo`.

![Catalog headline default](components/crops/catalog-h1-default.png)

#### Filter field
A catalog filter/search input; measured in place, never submitted. Read as `catalog-filter` on the catalog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 193 x 30; padding 0px 8px; background transparent; outline 2px solid transparent, offset 2px; text euclidCircularALightWebS 14/20 400, #000000 `color.brand.logo`; placeholder #999999; layers input.h-full.w-full 193.0x30.0 2px solid rgba(0, 0, 0, 0) offset 2px |
| focus-visible | placeholder transparent |
| filled | size 171 x 30; placeholder transparent; layers input.h-full.w-full 171.0x30.0 2px solid rgba(0, 0, 0, 0) offset 2px |

Child layers that carry the look: input 193x30.

![Filter field default](components/crops/catalog-filter-default.png) ![Filter field focus-visible](components/crops/catalog-filter-focus-visible.png) ![Filter field filled](components/crops/catalog-filter-filled.png)

#### Catalog card
An asset card in the catalog grid; measured, never followed. Read as `catalog-card` on the catalog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1050 x 550.59; padding 60px 0px 100px 0px; background transparent; text euclidCircularALightWebS 22/28 600, #000000 `color.brand.logo`; layers a.flex.flex-row 167.0x38.0 rgb(255, 255, 255) T:1px solid rgba(0, 0, 0, 0.1) / R:1px solid rgba(0, 0, 0, 0.1) / B:1px solid rgba(0, 0, 0, 0.1) / L:1px solid rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(47, 43, 67, 0.1) 0px -1px 0px 0px inset, rgba(47, 43, 67, 0.1) 0px 1px 3px 0px 10px |
| focus-visible | layers a.flex.flex-row 167.0x38.0 rgb(255, 255, 255) T:1px solid rgba(0, 0, 0, 0.1) / R:1px solid rgba(0, 0, 0, 0.1) / B:1px solid rgba(0, 0, 0, 0.1) / L:1px solid rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(47, 43, 67, 0.1) 0px -1px 0px 0px inset, rgba(47, 43, 67, 0.1) 0px 1px 3px 0px 1px auto rgb(0, 95, 204) offset 1px 10px |

Child layers that carry the look: a 167x38 background #ffffff `color.toast.default-fg` border 1px solid rgba(0, 0, 0, 0.1) radius 10px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(47, 43, 67, 0.1) 0px -1px 0px 0px inset, rgba(47, 43, 67, 0.1) 0px 1px 3px 0px.

![Catalog card default](components/crops/catalog-card-default.png) ![Catalog card hover](components/crops/catalog-card-hover.png) ![Catalog card focus-visible](components/crops/catalog-card-focus-visible.png) ![Catalog card pressed](components/crops/catalog-card-pressed.png)

#### Library row
A component-library row in the left list ("Smooth UI | 231"). The page's only h1 ("Components, 1,224") is a 1x1 accessibility heading. Read as `library-row` on the components page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 259 x 34; padding 2px 8px 2px 2px; radius 10px; background rgba(0, 0, 0, 0.07); text euclidCircularALightWebS 14/20 400, #000000 `color.brand.logo`; transition background-color 0.18s ease, color 0.18s ease; icon 20 x 20, #525252 `color.catalog-tint.gray` |
| hover | background rgba(0, 0, 0, 0.04) |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background rgba(0, 0, 0, 0.04) |

![Library row default](components/crops/library-row-default.png) ![Library row hover](components/crops/library-row-hover.png) ![Library row focus-visible](components/crops/library-row-focus-visible.png) ![Library row pressed](components/crops/library-row-pressed.png)

### Login

The OTP auth card at /login: "Log in or sign up to craftwork", the 46px email field, Send code and the black Log in with Google button — Send code was never pressed.

#### Login headline
"Log in or sign up to ..." on the OTP auth card. Read as `login-h1` on the login page.

**Values (default).** size 122.08 x 20; background transparent; text euclidCircularALightWebS 14/20 400, #606060.

![Login headline default](components/crops/login-h1-default.png)

#### Email field
The "Your Email" OTP field (390 wide); filled with a placeholder for the shot, never submitted. Read as `login-field` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, filled) | size 338 x 46; background transparent; outline 2px solid transparent, offset 2px; text euclidCircularALightWebS 16/22 400, #000000 `color.brand.logo`; placeholder #999999; layers input.px-3.h-[46px] 338.0x46.0 2px solid rgba(0, 0, 0, 0) offset 2px |

Child layers that carry the look: input 338x46.

![Email field default](components/crops/login-field-default.png) ![Email field focus-visible](components/crops/login-field-focus-visible.png) ![Email field filled](components/crops/login-field-filled.png)

#### Send code button
The "Send code" submit (390x46); measured only — pressing it would send a one-time code, so it is never pressed. Read as `send-code` on the login page.

**Values (default).** size 390 x 46; padding 0px 12px; border 1px solid rgba(0, 0, 0, 0.1); radius 10px; background #efefef; shadow rgba(47, 43, 67, 0.1) 0px -1px 0px 0px inset, rgba(47, 43, 67, 0.1) 0px 1px 3px 0px; text euclidCircularALightWebS 16/22 500, #000000 `color.brand.logo`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1).

![Send code button default](components/crops/send-code-default.png)

#### Google SSO
The "Log in with Google" button; measured, OAuth never followed. Read as `google-btn` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 390 x 46; padding 0px 12px; radius 10px; background #1e1e1e `color.toast.default-bg`; text euclidCircularALightWebS 16/22 400, #ffffff `color.toast.default-fg`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #ffffff `color.toast.default-fg` |
| hover | background #383838 |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #000000 `color.brand.logo` |

![Google SSO default](components/crops/google-btn-default.png) ![Google SSO hover](components/crops/google-btn-hover.png) ![Google SSO focus-visible](components/crops/google-btn-focus-visible.png) ![Google SSO pressed](components/crops/google-btn-pressed.png)

### Footer

The footer: category link columns, socials and the legal row.

#### Footer
The footer: category link columns and the legal row. Read as `footer` on the home page.

**Values (default).** size 1400 x 938; background transparent; text euclidCircularALightWebS 14/20 500, #999999; icon 20 x 20, #999999; layers div.mx-auto.max-w-[1110px] 1110.0x938.0 rgb(244, 244, 244) 24px; a.flex.items-center 157.2x32.0 rgb(249, 249, 249) 10px; a.flex.items-center 121.9x32.0 rgb(249, 249, 249) 10px; a.flex.items-center 97.6x32.0 rgb(249, 249, 249) 10px; button.cursor-default.flex 30.0x30.0 rgba(237, 237, 237, 0.698) 8px; nav.mt-10.flex 1020.0x101.0 T:1px solid rgba(0, 0, 0, 0.1).

Child layers that carry the look: div 1110x938 background #f4f4f4 radius 24px; a 157.2x32 background #f9f9f9 radius 10px; a 121.9x32 background #f9f9f9 radius 10px.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 42.48 x 20; background transparent; text euclidCircularALightWebS 14/20 500, #999999; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text euclidCircularALightWebS 14/20 500, #000000 `color.brand.logo` |
| focus-visible | outline 2px solid #606060, offset 2px; layers a.foot-note-medium.text-text-icons-tertiary 42.5x20.0 2px solid rgb(96, 96, 96) offset 2px |
| pressed | text euclidCircularALightWebS 14/20 500, #000000 `color.brand.logo` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A social link in the footer. Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 30 x 30; radius 8px; background transparent; text euclidCircularALightWebS 16/24 400, #999999; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #999999 |
| hover | background #f9f9f9; text euclidCircularALightWebS 16/24 400, #000000 `color.brand.logo`; icon 20 x 20, #000000 `color.brand.logo` |
| focus-visible | outline 2px solid #606060, offset 2px; layers a.cursor-default.flex 30.0x30.0 2px solid rgb(96, 96, 96) offset 2px 8px |
| pressed | background #f9f9f9; text euclidCircularALightWebS 16/24 400, #000000 `color.brand.logo`; icon 20 x 20, #000000 `color.brand.logo` |

![Social link default](components/crops/social-icon-default.png) ![Social link hover](components/crops/social-icon-hover.png) ![Social link focus-visible](components/crops/social-icon-focus-visible.png) ![Social link pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The same surface at phone width: the 60px header keeps the wordmark and opens a 300px menu sheet; the hero sets at 38px.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 60; background transparent; text euclidCircularALightWebS 16/22 400, #606060; icon 26 x 26, #000000 `color.brand.logo`; layers span.pointer-events-none.absolute 0.0x0.0 rgba(0, 0, 0, 0.07) 8px; div.absolute.left-0 0.0x0.0 rgba(255, 255, 255, 0.9) rgba(0, 0, 0, 0.14) 0px 12px 28px -8px, rgba(0, 0, 0, 0.22) 0px 30px 70px -24px 24px; a.flex.items-center 0.0x0.0 rgba(127, 127, 127, 0.14) 12px; div.border-t.border-other-stroke 0.0x0.0 T:1px solid rgba(0, 0, 0, 0.098); span.relative.block 0.0x0.0 rgba(127, 127, 127, 0.1) rgba(0.

Child layers that carry the look: span 0x0 background rgba(0, 0, 0, 0.07) radius 8px; div 0x0 background rgba(255, 255, 255, 0.9) radius 24px shadow rgba(0, 0, 0, 0.14) 0px 12px 28px -8px, rgba(0, 0, 0, 0.22) 0px 30px 70px -24px; a 0x0 background rgba(127, 127, 127, 0.14) radius 12px.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The header menu button that opens the nav overlay. Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 44 x 44; radius 8px; background transparent; text euclidCircularALightWebS 16/24 400, #000000 `color.brand.logo`; transition background-color 0.18s cubic-bezier(0.4, 0, 0.2, 1), color 0.18s cubic-bezier(0.4, 0, 0.2, 1), transform 0.18s cubic-bezier(0.4, 0, 0.2, 1); icon 18 x 18, #000000 `color.brand.logo` |
| focus-visible | outline 2px solid #606060, offset 2px; layers button.flex.size-11 44.0x44.0 2px solid rgb(96, 96, 96) offset 2px 8px |
| pressed | size 42.68 x 42.68; background rgba(0, 0, 0, 0.1); transform scale(0.97); icon 17.46 x 17.46, #000000 `color.brand.logo` |

![Menu button default](components/crops/m-menu-button-default.png) ![Menu button hover](components/crops/m-menu-button-hover.png) ![Menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The opened nav overlay. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 300 x 1186; background transparent; text euclidCircularALightWebS 14/20 500, #999999; icon 20 x 20, #999999.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile menu row
A row inside the opened nav overlay. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 42.48 x 20; background transparent; text euclidCircularALightWebS 14/20 500, #999999; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 2px solid #606060, offset 2px; layers a.foot-note-medium.text-text-icons-tertiary 42.5x20.0 2px solid rgb(96, 96, 96) offset 2px |

![Mobile menu row default](components/crops/m-nav-item-default.png) ![Mobile menu row hover](components/crops/m-nav-item-hover.png) ![Mobile menu row focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile menu row pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 358 x 123.09; background transparent; text euclidCircularALightWebS 38/41.04 600, #000000 `color.brand.logo`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the craftwork wordmark, the menu glyph, the theme toggle, the social glyphs and the product artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The signed-in library — the account, the asset downloads, the cart and checkout, the Pro purchase and the sell/author dashboard — was never reached. /login is an OTP card whose Send code was never pressed; every purchase CTA was measured, never followed. What the product looks like past the public catalogue is not documented here.

### Pages

- **Purchases and CTAs.** Get full access, Connect agent, every plan CTA and the deal's Get the deal were measured or screenshotted, never followed; no purchase was made and no file fetched.
- **Sign in.** The OTP card's email field was filled with a placeholder and cleared; Send code and Log in with Google were never pressed, so the one-time-code step is undocumented.
- **External surfaces** (social profiles, author pages, the shader studio) are linked from the site but were never opened.
- **The /components h1.** "Components, 1,224" is a 1x1 accessibility heading; the library row was measured instead.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **The Assets/Templates/Inspiration dropdowns** were never opened — they are flyout menus captured only as nav rows.

### Themes

The nav theme toggle paints both themes live (data-theme on <html>): the css-vars harvest resolved every var under both passes, and the home dark shot is captured. Dark measurements are var-resolved, not component-measured — the toggle was flipped only for the home screenshot.

### Fonts

- **Euclid Circular A** (600 on every heading, 400/500 UI) is Craftwork's own face served same-origin as euclidCircularA*WebS webfonts (harvested src list in raw/css-vars.json). The style guide falls back to system sans — the webfonts are licensed, not shipped.

### Screenshots

- The product artwork, UI-kit previews and the craftwork wordmark in the screenshots are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The kit/template artwork, product previews, plan feature lists and marketing copy are the product's content; only frames and components were measured.
