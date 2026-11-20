# Faire components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from faire.com on 2026-11-14, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, registered, bought or submitted; the application and auth forms were measured and typed into then cleared, never sent; every link and CTA was measured, never followed — product tiles open the sign-up dialog, which is the deepest public surface.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (95 components, 245 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Graphik_fix 14/20 400, #333333`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (255 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture — `light` on every surface here: faire.com paints a single light theme signed out (no theme attribute, no user toggle, and the probe's .dark pass resolves identically to :root). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [categories-menu](screenshots/home-light-categories-menu.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Category teaser (Home decor) | `/category/Home Decor` | [default](screenshots/category-home-decor-light-default.png), [full](screenshots/category-home-decor-light-full.png) |
| Category teaser (New products) | `/category/New Products` | [default](screenshots/category-new-products-light-default.png), [full](screenshots/category-new-products-light-full.png) |
| Brand storefront (54 Celsius) | `/brand/b_d72c56fe` | [default](screenshots/brand-light-default.png), [full](screenshots/brand-light-full.png) |
| Suppliers listing (Candles) | `/suppliers/Home Decor/subcategory/Candles & Holders/Candles` | [default](screenshots/suppliers-candles-light-default.png), [full](screenshots/suppliers-candles-light-full.png) |
| Suppliers A-Z | `/suppliers/All Brands/brand-value/women-owned` | [default](screenshots/suppliers-all-light-default.png), [full](screenshots/suppliers-all-light-full.png) |
| How Faire works | `/how-faire-works` | [default](screenshots/how-faire-works-light-default.png), [full](screenshots/how-faire-works-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Newsroom | `/news` | [default](screenshots/news-light-default.png), [full](screenshots/news-light-full.png) |
| Careers | `/careers` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| Large retailers | `/large-retailers` | [default](screenshots/large-retailers-light-default.png), [full](screenshots/large-retailers-light-full.png) |
| Point of sale | `/point-of-sale/about` | [default](screenshots/point-of-sale-light-default.png), [full](screenshots/point-of-sale-light-full.png) |
| Faire Markets | `/markets` | [default](screenshots/markets-light-default.png), [full](screenshots/markets-light-full.png) |
| Help center | `/support` | [default](screenshots/support-light-default.png), [full](screenshots/support-light-full.png) |
| Affiliates | `/affiliates` | [default](screenshots/affiliates-light-default.png), [full](screenshots/affiliates-light-full.png) |
| Brand application | `/apply` | [default](screenshots/apply-light-default.png), [full](screenshots/apply-light-full.png) |
| Sign-in dialog | `/?signIn=1` | [default](screenshots/signin-light-default.png) |
| Sign-up dialog | `/?signUp=1` | [default](screenshots/signup-light-default.png) |
| 404 | `/pagenotfound` | [default](screenshots/notfound-light-default.png), [full](screenshots/notfound-light-full.png) |
| Terms of service | `/tos` | [default](screenshots/tos-light-default.png), [full](screenshots/tos-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Category teaser, phone | `/category/Home Decor` | [default](screenshots/mobile-category-home-decor-light-default.png), [full](screenshots/mobile-category-home-decor-light-full.png) |
| Brand application, phone | `/apply` | [default](screenshots/mobile-apply-light-default.png), [full](screenshots/mobile-apply-light-full.png) |
| Sign-in dialog, phone | `/?signIn=1` | [default](screenshots/mobile-signin-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| OneTrust consent layer | every page | the consent SDK mounts a banner or the Privacy Preference Center; it is hidden with display:none, never answered — no accept/reject was clicked | hidden before every shot and reading |
| Cloudflare edge challenge | fresh clients, some routes | an intermittent Turnstile 'Just a moment…' interstitial; waited out and retried on a fresh context, never solved or clicked | category/suppliers/brand routes intermittently degrade; the states it ate are listed in Gaps |
| All categories menu | home page header | the 'All categories' button's own toggle — pointer click, keyboard Enter as fallback | [home-light-categories-menu](screenshots/home-light-categories-menu.png), [all-categories-btn](#all-categories-button), [categories-panel](#categories-menu-panel) |
| Mobile nav drawer | home page, phone width | the Menu button's own toggle | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-drawer](#mobile-nav-drawer) |
| Mobile search overlay | home page, phone width | the unlabelled magnifier button's own toggle | [m-search](#mobile-search-field) |
| Sign-in dialog | /?signIn=1 | mounted by the query parameter; fields typed into then cleared — nothing sent | [signin-light-default](screenshots/signin-light-default.png), [signin-dialog](#sign-in-dialog), [signin-email](#email-field-sign-in) |
| Sign-up dialog | /?signUp=1 (also every product tile) | mounted by the query parameter; fields typed into then cleared — nothing sent | [signup-light-default](screenshots/signup-light-default.png), [signup-dialog](#sign-up-dialog), [signup-email](#business-email-field) |
| Application fields | /apply | typed into then cleared — nothing sent | [field-firstname](#first-name-field), [field-email](#email-field), [field-phone](#phone-field), [field-password](#password-field) |
| Signed-in marketplace | a Faire account | every post-dialog surface — search results, product detail, cart, checkout, account — needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 40 components were given a real keyboard focus. 36 draw an outline ring: `all-categories-btn` (2px solid #101010, offset 2px), `nav-sell` (1px solid #101010, offset 1px), `nav-signup-buy` (2px solid #275ec5 `color.blue.700`, offset 1px), `nav-link` (1px auto #101010, offset 1px), `cta-secondary` (2px solid #275ec5 `color.blue.700`, offset 1px), `brand-tab` (5px auto #101010, offset 0px), `back-btn` (1px auto #101010, offset 0px), `phone-code-btn` (2px solid #101010, offset 0px), `show-password` (2px solid #275ec5 `color.blue.700`, offset 8px), `checkbox-terms` (2px solid #275ec5 `color.blue.700`, offset 2px), `next-btn` (2px solid #275ec5 `color.blue.700`, offset 1px), `signin-submit` (2px solid #275ec5 `color.blue.700`, offset 1px), `hw-cta` (2px solid #275ec5 `color.blue.700`, offset 1px), `about-cta` (2px solid #275ec5 `color.blue.700`, offset 1px), `lr-cta` (2px solid #275ec5 `color.blue.700`, offset 1px), `pos-cta` (2px solid #275ec5 `color.blue.700`, offset 1px), `markets-cta` (2px solid #275ec5 `color.blue.700`, offset 1px), `aff-cta` (2px solid #275ec5 `color.blue.700`, offset 1px), `m-menu-btn` (1px auto #e59700, offset 0px), `signin-google` (2px solid #101010, offset 2px), `signin-apple` (2px solid #101010, offset 2px), `signin-signup-link` (2px solid #275ec5 `color.blue.700`, offset 1px), `signin-close` (2px solid #275ec5 `color.blue.700`, offset 1px), `signin-show-password` (2px solid #275ec5 `color.blue.700`, offset 8px), `nav-signin` (1px auto #101010, offset 0px), `cta-plain` (2px solid #275ec5 `color.blue.700`, offset 1px), `cta-primary` (2px solid #275ec5 `color.blue.700`, offset 1px), `cat-nav-link` (2px solid #101010, offset 2px), `pill-tab` (on a child: 1px auto rgb(16, 16, 16) offset 0px), `signup-submit` (2px solid #275ec5 `color.blue.700`, offset 1px), `signup-google` (2px solid #101010, offset 2px), `signup-signin-link` (2px solid #275ec5 `color.blue.700`, offset 1px), `signup-close` (2px solid #275ec5 `color.blue.700`, offset 1px), `m-search-btn` (2px solid #275ec5 `color.blue.700`, offset 1px), `cat-filter-btn` (2px solid #275ec5 `color.blue.700`, offset 1px), `subcat-card` (2px solid #275ec5 `color.blue.700`, offset 1px). The other 4 show no measured change: `footer-link`, `help-link`, `news-cta`, `careers-cta`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `linear` | background, color | m-topbar, mkt-header, nav-link, nav-sell |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | back-btn |
| 0.252s | `cubic-bezier(0.33, 1, 0.68, 1)` | opacity, width | m-search, search-field |
| 0.3s | `ease-out` | background-color | all-categories-btn |
| 1s | `cubic-bezier(0.4, 0, 0.2, 1)` | rotate, scale, transform, translate | category-card |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Categories menu panel](#categories-menu-panel) | 1440 x 712 | - | - | #ffffff `color.bsr.grey.100` | none | 48px |
| [Subcategory card](#subcategory-card) | 324 x 96 | - | 4px | #fbf8f6 `color.neutral.100` | none | 16px |
| [Brand card](#brand-card) | 217.33 x 273.34 | - | - | transparent | none | 0 |
| [Newsroom headline card](#newsroom-headline-card) | 86.81 x 38 | - | 4px | transparent | none | 0 |
| [Sign-in dialog](#sign-in-dialog) | 420 x 649 | - | - | #ffffff `color.bsr.grey.100` | none | 0 |
| [Sign-up dialog](#sign-up-dialog) | 500 x 523 | - | - | #ffffff `color.bsr.grey.100` | none | 0 |
| [Mobile nav drawer](#mobile-nav-drawer) | 312 x 844 | - | 0px 4px 4px 0px | #ffffff `color.bsr.grey.100` | none | 0 |

## Components

### Site chrome

The fixed header on every page: the Faire wordmark, the 'All categories' dropdown (its panel is a full-width white sheet), the search field, the EN-US locale control, Blog, 'Sign up to sell', 'Sign in' and the dark 'Sign up to buy' fs-button--primary — plus the sub-header category strip and the promo line above.

#### Site header
The white top bar: Faire wordmark, "All categories" dropdown, search field, locale button, Blog, "Sign up to sell", "Sign in" and the dark "Sign up to buy" button. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 108; border B: 1px solid #dadada `color.grey.400`; background #ffffff `color.bsr.grey.100`; text graphik 14/20 200, #333333 `color.grey.900`; transition background 0.1s linear; icon 8 x 8, #333333 `color.grey.900`.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Faire wordmark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 136 x 29; padding 8px 16px; background transparent; text Graphik 16/24 400, #000000 `color.bsr.grey.1000`.

![Logo default](components/crops/mkt-logo-default.png)

#### Header search field
The "Search wholesale products or brands" field; focused and typed into then cleared — nothing searched. Read as `search-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 579.11 x 20; padding 0px 0px 0px 40px; background transparent; text Graphik_fix 14/20 400, #333333 `color.grey.900`; transition width 0.252s cubic-bezier(0.33, 1, 0.68, 1), opacity 0.252s cubic-bezier(0.33, 1, 0.68, 1); placeholder oklab(0.321069 0.0000146478 0.0000064373 / 0.5) |
| focused, filled | text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000`; placeholder oklab(0 0 0 / 0.5) |

![Header search field default](components/crops/search-field-default.png) ![Header search field focused](components/crops/search-field-focused.png)

#### All categories button
The rounded header dropdown trigger (rounded-[32px]); the opened state was measured after activating it — a local UI toggle, its links never followed. Read as `all-categories-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 141.11 x 40; padding 10px 16px; radius 32px; background transparent; text graphik 14/20 200, #333333 `color.grey.900`; transition background-color 0.3s ease-out; icon 8 x 8, #333333 `color.grey.900` |
| hover | size 133 x 40; background #f1f1f1 `color.grey.300`; text GT Standard 14/20 400, #000000 `color.bsr.grey.1000`; icon 8 x 8, #000000 `color.bsr.grey.1000` |
| focus-visible | background #f1f1f1 `color.grey.300`; outline 2px solid #101010, offset 2px |
| pressed | background #f1f1f1 `color.grey.300`; text graphik 14/20 200, #000000 `color.bsr.grey.1000`; icon 8 x 8, #000000 `color.bsr.grey.1000` |
| opened | size 133 x 40; background #f1f1f1 `color.grey.300`; text GT Standard 14/20 400, #000000 `color.bsr.grey.1000`; icon 8 x 8, #000000 `color.bsr.grey.1000` |

![All categories button default](components/crops/all-categories-btn-default.png) ![All categories button hover](components/crops/all-categories-btn-hover.png) ![All categories button focus-visible](components/crops/all-categories-btn-focus-visible.png) ![All categories button pressed](components/crops/all-categories-btn-pressed.png) ![All categories button opened](components/crops/all-categories-btn-opened.png)

#### Categories menu panel
The panel opened by "All categories"; its links were never followed. Read as `categories-panel` on the home page.

**Values (default).** size 1440 x 712; padding 48px; background #ffffff `color.bsr.grey.100`; text graphik 12/16 200, #6c6a6a `color.bsr.neutral.1000`.

![Categories menu panel default](components/crops/categories-panel-default.png)

#### Sign up to sell link
The header link to the brand application; measured, never followed. Read as `nav-sell` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 121.25 x 60; padding 0px 12px; background transparent; text graphik 14/20 200, #333333 `color.grey.900`; transition color 0.1s linear |
| hover | text graphik 14/20 200, #000000 `color.bsr.grey.1000` |
| focus-visible | outline 1px solid #101010, offset 1px; layers a.focus-visible:outline.text-fs-text-primary 121.3x60.0 1px solid rgb(16, 16, 16) offset 1px |
| pressed | text graphik 14/20 200, #000000 `color.bsr.grey.1000` |

![Sign up to sell link default](components/crops/nav-sell-default.png) ![Sign up to sell link hover](components/crops/nav-sell-hover.png) ![Sign up to sell link focus-visible](components/crops/nav-sell-focus-visible.png) ![Sign up to sell link pressed](components/crops/nav-sell-pressed.png)

#### Sign up to buy button
The dark "Sign up to buy" fs-button--primary in the header; measured, never pressed. Read as `nav-signup-buy` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 132.11 x 40; padding 0px 16px; border 1px solid transparent; radius 4px; background #333333 `color.grey.900`; text Graphik_fix 14/20 400, #ffffff `color.bsr.grey.100` |
| hover | background #000000 `color.bsr.grey.1000` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px |
| pressed | background #000000 `color.bsr.grey.1000` |

![Sign up to buy button default](components/crops/nav-signup-buy-default.png) ![Sign up to buy button hover](components/crops/nav-signup-buy-hover.png) ![Sign up to buy button focus-visible](components/crops/nav-signup-buy-focus-visible.png) ![Sign up to buy button pressed](components/crops/nav-signup-buy-pressed.png)

#### Nav link
The header Blog link; measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 54.61 x 60; padding 0px 12px; background transparent; text graphik 14/20 200, #333333 `color.grey.900`; transition color 0.1s linear |
| hover | text graphik 14/20 200, #000000 `color.bsr.grey.1000` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.text-fs-text-primary.hover:text-fs-action-text-hover 54.6x60.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text graphik 14/20 200, #000000 `color.bsr.grey.1000` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Locale button
The EN-US locale selector (globe + "EN-US") in the header — a div control, not a button; measured, never opened. Read as `locale-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 90.75 x 60; background transparent; text graphik 14/20 200, #333333 `color.grey.900`; icon 16 x 16, #000000 `color.bsr.grey.1000`; layers div.[&&]:border-fs-border-muted.[&&]:absolute 0.0x0.0 rgb(255, 255, 255) T:1px solid rgb(218, 218, 218) / R:1px solid rgb(218, 218, 218) / B:1px solid rgb(218, 218, 218) / L:1px solid rgb(218, 218, 218) rgb(247, 247, 247) 0px 1px 1px 0px |
| hover, pressed | layers div.[&&]:border-fs-border-muted.[&&]:absolute 170.0x506.0 rgb(255, 255, 255) T:1px solid rgb(218, 218, 218) / R:1px solid rgb(218, 218, 218) / B:1px solid rgb(218, 218, 218) / L:1px solid rgb(218, 218, 218) rgb(247, 247, 247) 0px 1px 1px 0px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 0x0 background #ffffff `color.bsr.grey.100` border 1px solid #dadada `color.grey.400` shadow #f7f7f7 `color.grey.200` 0px 1px 1px 0px.

![Locale button default](components/crops/locale-btn-default.png) ![Locale button hover](components/crops/locale-btn-hover.png) ![Locale button pressed](components/crops/locale-btn-pressed.png)

#### Sign in button
The header "Sign in" — it mounts the sign-in dialog; measured, never pressed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 79.06 x 60; padding 0px 16px; background transparent; text Graphik_fix 14/20 400, #333333 `color.grey.900` |
| hover | text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.type-fs-paragraph.whitespace-nowrap 79.1x60.0 1px auto rgb(16, 16, 16) offset 0px |
| pressed | text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000` |

![Sign in button default](components/crops/nav-signin-default.png) ![Sign in button hover](components/crops/nav-signin-hover.png) ![Sign in button focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign in button pressed](components/crops/nav-signin-pressed.png)

#### Promo banner
The top strip above the header ("Shop wholesale online from over 100,000 brands. Sign up"). Read as `promo-banner` on the home page.

**Values (default).** size 394.27 x 17; background transparent; text Graphik_fix 14/20 400, #333333 `color.grey.900`.

![Promo banner default](components/crops/promo-banner-default.png)

#### Category nav link
A link in the sub-header category strip ("New products", "Home decor"…); measured, never followed. Read as `cat-nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 105.5 x 30; padding 4px 0px 0px 0px; radius 4px; background transparent; text graphik 18/26 200, #333333 `color.grey.900` |
| focus-visible | outline 2px solid #101010, offset 2px; layers a.sc-da430d62-1.llTVOz 105.5x30.0 2px solid rgb(16, 16, 16) offset 2px 4px |

![Category nav link default](components/crops/cat-nav-link-default.png) ![Category nav link hover](components/crops/cat-nav-link-hover.png) ![Category nav link focus-visible](components/crops/cat-nav-link-focus-visible.png) ![Category nav link pressed](components/crops/cat-nav-link-pressed.png)

### Home

The home page: the 'Find your next bestseller' serif display hero over lifestyle media, the featured-brands pill tabs, brand and category tiles and the sign-up CTAs.

#### Hero headline
"Find your next bestseller" — the type-fs-display display heading in inverse ink over the hero media. Read as `hero-h1` on the home page.

**Values (default).** size 546 x 64; background transparent; text Nantes_fix 52/64 400, #ffffff `color.bsr.grey.100`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero panel
The hero block behind the display heading. Read as `hero-panel` on the home page.

**Values (default).** size 1392 x 224; background transparent; text GT Canon 52/64 400, #ffffff `color.bsr.grey.100`; layers button.interactive.focusable 131.0x48.0 rgb(255, 255, 255) T:1px solid rgb(218, 218, 218) / R:1px solid rgb(218, 218, 218) / B:1px solid rgb(218, 218, 218) / L:1px solid rgb(218, 218, 218) 4px; a.interactive.focusable 87.0x20.0 rgba(51, 51, 51, 0) 4px.

Child layers that carry the look: button 131x48 background #ffffff `color.bsr.grey.100` border 1px solid #dadada `color.grey.400` radius 4px; a 87x20 background rgba(51, 51, 51, 0) `color.transparent.grey.0` radius 4px.

![Hero panel default](components/crops/hero-panel-default.png)

#### Secondary button
An outlined "Sign up to buy" fs-button--secondary; measured, never pressed. Read as `cta-secondary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 140.11 x 48; padding 0px 20px; border 1px solid #dadada `color.grey.400`; radius 4px; background #ffffff `color.bsr.grey.100`; text Graphik_fix 14/20 400, #333333 `color.grey.900` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px |
| pressed | border 1px solid #000000 `color.bsr.grey.1000`; background #f1f1f1 `color.grey.300`; text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000` |

![Secondary button default](components/crops/cta-secondary-default.png) ![Secondary button hover](components/crops/cta-secondary-hover.png) ![Secondary button focus-visible](components/crops/cta-secondary-focus-visible.png) ![Secondary button pressed](components/crops/cta-secondary-pressed.png)

#### Section heading
A marketing section heading further down the home page. Read as `section-h2` on the home page.

**Values (default).** size 627 x 128; background transparent; text nantes 52/64 400, #333333 `color.grey.900`.

![Section heading default](components/crops/section-h2-default.png)

#### Brand card
A brand tile on the home page (image, name); measured, never followed. Read as `brand-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 217.33 x 273.34; background transparent; text graphik 14/20 500, #333333 `color.grey.900`; layers p.f_t_base.f_t_maxLines 127.7x20.0 |
| hover | layers p.f_t_base.f_t_maxLines 104.0x20.0 |

Child layers that carry the look: p 127.7x20 image linear-gradient(to right in oklab, #333333 `color.grey.900` 0px, #333333 `color.grey.900` .

![Brand card default](components/crops/brand-card-default.png) ![Brand card hover](components/crops/brand-card-hover.png)

#### Plain button
A "Sign up for free" fs-button--plain text button; measured, never pressed. Read as `cta-plain` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 105.41 x 20; radius 4px; background rgba(51, 51, 51, 0) `color.transparent.grey.0`; text Graphik_fix 14/20 400, #333333 `color.grey.900` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px |
| pressed | text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000` |

![Plain button default](components/crops/cta-plain-default.png) ![Plain button hover](components/crops/cta-plain-hover.png) ![Plain button focus-visible](components/crops/cta-plain-focus-visible.png) ![Plain button pressed](components/crops/cta-plain-pressed.png)

#### Primary button
A dark "Sign up to buy" fs-button--primary (medium); measured, never pressed. Read as `cta-primary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 131 x 48; padding 0px 20px; border 1px solid transparent; radius 4px; background #ffffff `color.bsr.grey.100`; text GT Standard 14/20 400, #161616 `color.bsr.grey.900` |
| hover | size 140.11 x 48; text Graphik_fix 14/20 400, #333333 `color.grey.900` |
| focus-visible | size 140.11 x 48; outline 2px solid #275ec5 `color.blue.700`, offset 1px; text Graphik_fix 14/20 400, #333333 `color.grey.900` |
| pressed | size 140.11 x 48; background #f7f7f7 `color.grey.200`; text Graphik_fix 14/20 400, #333333 `color.grey.900` |

![Primary button default](components/crops/cta-primary-default.png) ![Primary button hover](components/crops/cta-primary-hover.png) ![Primary button focus-visible](components/crops/cta-primary-focus-visible.png) ![Primary button pressed](components/crops/cta-primary-pressed.png)

#### Featured-brands pill tab
A rounded pill filter tab under "Featured brands" (the selected one paints dark); measured, never toggled. Read as `pill-tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 116.5 x 40; background transparent; text graphik 14/20 200, #333333 `color.grey.900`; layers p.f_t_base.f_t_color 116.5x40.0 T:1px solid rgb(218, 218, 218) / R:1px solid rgb(218, 218, 218) / B:1px solid rgb(218, 218, 218) / L:1px solid rgb(218, 218, 218) 40px |
| focus-visible | layers p.f_t_base.f_t_color 116.5x40.0 T:1px solid rgb(51, 51, 51) / R:1px solid rgb(51, 51, 51) / B:1px solid rgb(51, 51, 51) / L:1px solid rgb(51, 51, 51) 1px auto rgb(16, 16, 16) offset 0px 40px |

Child layers that carry the look: p 116.5x40 border 1px solid #dadada `color.grey.400` radius 40px.

![Featured-brands pill tab default](components/crops/pill-tab-default.png) ![Featured-brands pill tab hover](components/crops/pill-tab-hover.png) ![Featured-brands pill tab focus-visible](components/crops/pill-tab-focus-visible.png) ![Featured-brands pill tab pressed](components/crops/pill-tab-pressed.png)

#### Category card
A category tile (image, label); measured, never followed. Read as `category-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 437.33 x 312.38; background transparent; text nantes 22/32 400, #ffffff `color.bsr.grey.100`; transition transform 1s cubic-bezier(0.4, 0, 0.2, 1), translate 1s cubic-bezier(0.4, 0, 0.2, 1), scale 1s cubic-bezier(0.4, 0, 0.2, 1), rotate 1s cubic-bezier(0.4, 0, 0.2, 1); layers div.absolute.inset-0 437.3x312.4 |

Child layers that carry the look: div 437.3x312.4 image linear-gradient(22.18deg, rgba(0, 0, 0, 0.5) 1.86%, transparent 31.23%).

![Category card default](components/crops/category-card-default.png) ![Category card hover](components/crops/category-card-hover.png)

### Category teaser

/category/Home Decor — the public teaser grid: a 'Wholesale home decor' serif masthead over media, the 'All filters' pill, subcategory cards, product tiles that all link to the sign-up dialog and a sign-up wall at the bottom.

#### Category headline
The category page masthead ("Wholesale home decor for your store"). Read as `cat-h1` on the category teaser page.

**Values (default).** size 1248 x 50; background transparent; text GT Canon 38/50 400, #ffffff `color.bsr.grey.100`.

![Category headline default](components/crops/cat-h1-default.png)

#### All filters button
The filters trigger on the category teaser grid; measured, never opened. Read as `cat-filter-btn` on the category teaser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 112 x 40; padding 0px 16px; border 1px solid #dadada `color.grey.400`; radius 999px; background #ffffff `color.bsr.grey.100`; text GT Standard 14/20 400, #161616 `color.bsr.grey.900`; icon 16 x 16, #161616 `color.bsr.grey.900` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px |
| pressed | border 1px solid #000000 `color.bsr.grey.1000`; text GT Standard 14/20 400, #000000 `color.bsr.grey.1000`; icon 16 x 16, #000000 `color.bsr.grey.1000` |

![All filters button default](components/crops/cat-filter-btn-default.png) ![All filters button hover](components/crops/cat-filter-btn-hover.png) ![All filters button focus-visible](components/crops/cat-filter-btn-focus-visible.png) ![All filters button pressed](components/crops/cat-filter-btn-pressed.png)

#### Product tile
A product card in the teaser grid (photo, name, price); clicking it mounts the sign-up dialog, so it was measured, never followed. Read as `product-tile` on the category teaser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 217.33 x 217.33; radius 4px; background transparent; text Graphik 16/24 400, #000000 `color.bsr.grey.1000` |

![Product tile default](components/crops/product-tile-default.png) ![Product tile hover](components/crops/product-tile-hover.png)

#### Subcategory card
A card in the "Explore diverse styles" subcategory grid (thumbnail + label); measured, never followed. Read as `subcat-card` on the category teaser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 324 x 96; padding 16px; radius 4px; background #fbf8f6 `color.neutral.100`; text GT Standard 14/20 500, #161616 `color.bsr.grey.900` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px |

![Subcategory card default](components/crops/subcat-card-default.png) ![Subcategory card hover](components/crops/subcat-card-hover.png) ![Subcategory card focus-visible](components/crops/subcat-card-focus-visible.png) ![Subcategory card pressed](components/crops/subcat-card-pressed.png)

#### Sign-up wall email field
The "Business email address" field in the page's sign-up section; focused and typed into then cleared — never submitted. Read as `wall-field` on the category teaser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 322 x 20; background transparent; text GT Standard 14/20 400, #161616 `color.bsr.grey.900`; placeholder oklab(0.200175 0.00000910461 0.00000399351 / 0.5) |
| focused, filled | text GT Standard 14/20 400, #000000 `color.bsr.grey.1000`; placeholder oklab(0 0 0 / 0.5) |

![Sign-up wall email field default](components/crops/wall-field-default.png) ![Sign-up wall email field focused](components/crops/wall-field-focused.png) ![Sign-up wall email field filled](components/crops/wall-field-filled.png)

#### Brand link on card
A brand name link inside a product card on the category page; measured, never followed. Read as `brand-tile` on the category teaser page.

Not on the page when it was captured.

### Brand storefront

/brand/b_d72c56fe — a public brand page (54 Celsius): cover photo, circular fs-avatar, 'Top Shop' and rating badges, the section tab row, product tiles and an 'About' card; every buy path leads to the sign-up wall.

#### Brand headline
"54 Celsius wholesale" — the brand storefront masthead. Read as `brand-h1` on the brand storefront page.

**Values (default).** size 215 x 32; background transparent; text GT Standard 22/32 500, #161616 `color.bsr.grey.900`.

![Brand headline default](components/crops/brand-h1-default.png)

#### Minimum order badge
The "US$100 min" order-minimum label on brand tiles. Read as `min-order-badge` on the brand storefront page.

**Values (default).** size 75 x 20; background transparent; text GT Standard 14/20 400, #161616 `color.bsr.grey.900`.

![Minimum order badge default](components/crops/min-order-badge-default.png)

#### Section tab
A storefront section nav item ("All products"/"New"); measured, never followed. Read as `brand-tab` on the brand storefront page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 78 x 51; border B: 1px solid #95948f `color.bsr.neutral.800`; background transparent; text GT Standard 14/20 500, #161616 `color.bsr.grey.900`; layers button.flex.h-full 78.0x51.0 B:1px solid rgb(149, 148, 143) |
| focus-visible | outline 5px auto #101010, offset 0px; layers button.flex.h-full 78.0x51.0 B:1px solid rgb(149, 148, 143) 5px auto rgb(16, 16, 16) offset 0px |

Child layers that carry the look: button 78x51 border 1px solid #95948f `color.bsr.neutral.800`.

![Section tab default](components/crops/brand-tab-default.png) ![Section tab hover](components/crops/brand-tab-hover.png) ![Section tab focus-visible](components/crops/brand-tab-focus-visible.png) ![Section tab pressed](components/crops/brand-tab-pressed.png)

#### Brand product tile
A product card on the brand page (photo, name, price, order minimum); it links to the sign-up dialog — measured, never followed. Read as `brand-product-tile` on the brand storefront page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 259.19 x 259.19; radius 4px; background transparent; text Graphik 16/24 400, #000000 `color.bsr.grey.1000` |

![Brand product tile default](components/crops/brand-product-tile-default.png) ![Brand product tile hover](components/crops/brand-product-tile-hover.png)

#### About heading
The "About <brand>" section heading. Read as `about-h2` on the brand storefront page.

**Values (default).** size 616 x 20; background transparent; text GT Standard 14/20 500, #161616 `color.bsr.grey.900`.

![About heading default](components/crops/about-h2-default.png)

#### Wall email field
The "Business email address" field in the brand page's sign-up wall; focused and typed into then cleared — never submitted. Read as `wall-email` on the brand storefront page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 322 x 20; background transparent; text GT Standard 14/20 400, #161616 `color.bsr.grey.900`; placeholder oklab(0.200175 0.00000910461 0.00000399351 / 0.5) |
| focused, filled | text GT Standard 14/20 400, #000000 `color.bsr.grey.1000`; placeholder oklab(0 0 0 / 0.5) |

![Wall email field default](components/crops/wall-email-default.png) ![Wall email field focused](components/crops/wall-email-focused.png)

#### Brand avatar
The brand's circular fs-avatar logo by the masthead. Read as `brand-avatar` on the brand storefront page.

**Values (default).** size 96 x 96; radius 999px; background #ffffff `color.bsr.grey.100`; outline 2px solid transparent, offset 2px; text GT Standard 30/38 500, #ffffff `color.bsr.grey.100`.

![Brand avatar default](components/crops/brand-avatar-default.png)

### Suppliers listings

The SEO /suppliers/* listings (the candles subcategory and the /suppliers/All Brands A-Z): breadcrumb, 'Wholesale … suppliers' masthead and rows of brand cards — intermittently gated by the Cloudflare edge challenge.

#### Supplier row
A brand row/card in the suppliers listing; measured, never followed. Read as `supplier-row` on the suppliers listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 220 x 220; background transparent; text Graphik 16/24 400, #000000 `color.bsr.grey.1000`; layers div.bg-fs-surface-secondary.relative 220.0x220.0 rgb(247, 247, 247); div.bg-fs-action-surface-active/2.rounded-fs-component-default 220.0x220.0 oklab(0 0 0 / 0.02) 4px |

Child layers that carry the look: div 220x220 background #f7f7f7 `color.grey.200`; div 220x220 background oklab(0 0 0 / 0.02) radius 4px.

![Supplier row default](components/crops/supplier-row-default.png) ![Supplier row hover](components/crops/supplier-row-hover.png)

#### All brands headline
The /suppliers/All Brands masthead. Read as `supall-h1` on the suppliers A-Z page.

**Values (default).** size 672 x 38; background transparent; text GT Canon 30/38 400, #161616 `color.bsr.grey.900`.

![All brands headline default](components/crops/supall-h1-default.png)

#### All brands row
A brand row in the A-Z listing; measured, never followed. Read as `supall-row` on the suppliers A-Z page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 220 x 220; background transparent; text Graphik 16/24 400, #000000 `color.bsr.grey.1000`; layers div.bg-fs-surface-secondary.relative 220.0x220.0 rgb(247, 247, 247); div.bg-fs-action-surface-active/2.rounded-fs-component-default 220.0x220.0 oklab(0 0 0 / 0.02) 4px |

Child layers that carry the look: div 220x220 background #f7f7f7 `color.grey.200`; div 220x220 background oklab(0 0 0 / 0.02) radius 4px.

![All brands row default](components/crops/supall-row-default.png) ![All brands row hover](components/crops/supall-row-hover.png)

#### Suppliers headline
The SEO suppliers listing masthead. Read as `sup-h1` on the suppliers listing page.

Not on the page when it was captured.

#### Subcategory link
A related-subcategory link; measured, never followed. Read as `sup-filter-link` on the suppliers listing page.

Not on the page when it was captured.

### Marketing pages

The signed-out marketing surface — /how-faire-works, /about, /news, /careers, /large-retailers, /point-of-sale/about, /markets, /affiliates: serif mastheads, CTAs and content cards.

#### How Faire works headline
The /how-faire-works masthead. Read as `hw-h1` on the how-faire-works page.

**Values (default).** size 647 x 26; background transparent; text graphik 18/26 500, #333333 `color.grey.900`.

![How Faire works headline default](components/crops/hw-h1-default.png)

#### How Faire works headline CTA
The page's main call to action; measured, never followed or pressed. Read as `hw-cta` on the how-faire-works page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 52.06 x 17; background transparent; text Graphik_fix 14/normal 400, #333333 `color.grey.900` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px; layers button.focusable.interactive 52.1x17.0 2px solid rgb(39, 94, 197) offset 1px |

![How Faire works headline CTA default](components/crops/hw-cta-default.png) ![How Faire works headline CTA hover](components/crops/hw-cta-hover.png) ![How Faire works headline CTA focus-visible](components/crops/hw-cta-focus-visible.png) ![How Faire works headline CTA pressed](components/crops/hw-cta-pressed.png)

#### About headline
The /about masthead. Read as `about-h1` on the about page.

**Values (default).** size 74 x 26; background transparent; text GT Standard 18/26 500, #ffffff `color.bsr.grey.100`.

![About headline default](components/crops/about-h1-default.png)

#### About headline CTA
The page's main call to action; measured, never followed or pressed. Read as `about-cta` on the about page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 47 x 16; background transparent; text GT Standard 14/normal 400, #161616 `color.bsr.grey.900` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px; layers button.focusable.interactive 47.0x16.0 2px solid rgb(39, 94, 197) offset 1px |

![About headline CTA default](components/crops/about-cta-default.png) ![About headline CTA hover](components/crops/about-cta-hover.png) ![About headline CTA focus-visible](components/crops/about-cta-focus-visible.png) ![About headline CTA pressed](components/crops/about-cta-pressed.png)

#### Newsroom headline CTA
The page's main call to action; measured, never followed or pressed. Read as `news-cta` on the newsroom page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 123.36 x 50; padding 15px 25px; background #333333 `color.grey.900`; text graphik 14/20 200, #ffffff `color.bsr.grey.100` |

![Newsroom headline CTA default](components/crops/news-cta-default.png) ![Newsroom headline CTA hover](components/crops/news-cta-hover.png) ![Newsroom headline CTA focus-visible](components/crops/news-cta-focus-visible.png) ![Newsroom headline CTA pressed](components/crops/news-cta-pressed.png)

#### Newsroom headline card
A content card on the page; measured, never followed. Read as `news-card` on the newsroom page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 86.81 x 38; radius 4px; background transparent; text graphik 14/20 200, #333333 `color.grey.900` |
| hover | text graphik 14/20 200, #000000 `color.bsr.grey.1000` |

![Newsroom headline card default](components/crops/news-card-default.png) ![Newsroom headline card hover](components/crops/news-card-hover.png)

#### Careers headline CTA
The page's main call to action; measured, never followed or pressed. Read as `careers-cta` on the careers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 97.25 x 17; background transparent; text Graphik_fix 14/20 400, #333333 `color.grey.900` |

![Careers headline CTA default](components/crops/careers-cta-default.png) ![Careers headline CTA hover](components/crops/careers-cta-hover.png) ![Careers headline CTA focus-visible](components/crops/careers-cta-focus-visible.png) ![Careers headline CTA pressed](components/crops/careers-cta-pressed.png)

#### Large retailers headline
The /large-retailers masthead. Read as `lr-h1` on the large-retailers page.

**Values (default).** size 137.75 x 16; background transparent; text graphik 12/16 200, #ffffff `color.bsr.grey.100`.

![Large retailers headline default](components/crops/lr-h1-default.png)

#### Large retailers headline CTA
The page's main call to action; measured, never followed or pressed. Read as `lr-cta` on the large-retailers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 140.11 x 48; padding 0px 20px; border 1px solid #dadada `color.grey.400`; radius 4px; background #ffffff `color.bsr.grey.100`; text Graphik_fix 14/20 400, #333333 `color.grey.900` |
| hover | border 1px solid #000000 `color.bsr.grey.1000`; background #f1f1f1 `color.grey.300`; text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px |
| pressed | border 1px solid #000000 `color.bsr.grey.1000`; background #f1f1f1 `color.grey.300`; text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000` |

![Large retailers headline CTA default](components/crops/lr-cta-default.png) ![Large retailers headline CTA hover](components/crops/lr-cta-hover.png) ![Large retailers headline CTA focus-visible](components/crops/lr-cta-focus-visible.png) ![Large retailers headline CTA pressed](components/crops/lr-cta-pressed.png)

#### Point of sale headline CTA
The page's main call to action; measured, never followed or pressed. Read as `pos-cta` on the point-of-sale page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 52.06 x 17; background transparent; text Graphik_fix 14/normal 400, #333333 `color.grey.900` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px; layers button.focusable.interactive 52.1x17.0 2px solid rgb(39, 94, 197) offset 1px |

![Point of sale headline CTA default](components/crops/pos-cta-default.png) ![Point of sale headline CTA hover](components/crops/pos-cta-hover.png) ![Point of sale headline CTA focus-visible](components/crops/pos-cta-focus-visible.png) ![Point of sale headline CTA pressed](components/crops/pos-cta-pressed.png)

#### Faire Markets headline
The /markets masthead. Read as `markets-h1` on the markets page.

**Values (default).** size 656 x 192; background transparent; text GT Canon 52/64 400, #ffffff `color.bsr.grey.100`.

![Faire Markets headline default](components/crops/markets-h1-default.png)

#### Faire Markets headline CTA
The page's main call to action; measured, never followed or pressed. Read as `markets-cta` on the markets page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 47 x 16; background transparent; text GT Standard 14/normal 400, #161616 `color.bsr.grey.900` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px; layers button.focusable.interactive 47.0x16.0 2px solid rgb(39, 94, 197) offset 1px |

![Faire Markets headline CTA default](components/crops/markets-cta-default.png) ![Faire Markets headline CTA hover](components/crops/markets-cta-hover.png) ![Faire Markets headline CTA focus-visible](components/crops/markets-cta-focus-visible.png) ![Faire Markets headline CTA pressed](components/crops/markets-cta-pressed.png)

#### Affiliates headline
The /affiliates masthead. Read as `aff-h1` on the affiliates page.

**Values (default).** size 553 x 64; background transparent; text GT Canon 52/64 400, #ffffff `color.bsr.grey.100`.

![Affiliates headline default](components/crops/aff-h1-default.png)

#### Affiliates headline CTA
The page's main call to action; measured, never followed or pressed. Read as `aff-cta` on the affiliates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 47 x 16; background transparent; text GT Standard 14/normal 400, #161616 `color.bsr.grey.900` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px; layers button.focusable.interactive 47.0x16.0 2px solid rgb(39, 94, 197) offset 1px |

![Affiliates headline CTA default](components/crops/aff-cta-default.png) ![Affiliates headline CTA hover](components/crops/aff-cta-hover.png) ![Affiliates headline CTA focus-visible](components/crops/aff-cta-focus-visible.png) ![Affiliates headline CTA pressed](components/crops/aff-cta-pressed.png)

#### Newsroom headline
The /news masthead. Read as `news-h1` on the newsroom page.

**Values (default).** size 670 x 100; background transparent; text nantes 38/50 400, #333333 `color.grey.900`.

![Newsroom headline default](components/crops/news-h1-default.png)

#### Careers headline
The /careers masthead. Read as `careers-h1` on the careers page.

**Values (default).** size 450 x 150; background transparent; text nantes 38/50 400, #ffffff `color.bsr.grey.100`.

![Careers headline default](components/crops/careers-h1-default.png)

#### Point of sale headline
The /point-of-sale/about masthead. Read as `pos-h1` on the point-of-sale page.

**Values (default).** size 456 x 128; background transparent; text nantes 52/64 400, #333333 `color.grey.900`.

![Point of sale headline default](components/crops/pos-h1-default.png)

### Brand application (/apply)

The /apply brand-onboarding form measured at rest: name/e-mail/phone/password fields, the +1 country-code prefix, show-password icon, terms and marketing fs-checkbox inputs and the 'Next' submit — focused and typed into then cleared, never submitted.

#### Back button
The "Go back" chevron icon button in the top bar; measured, never pressed. Read as `back-btn` on the brand application page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40 x 40; radius 3.35544e+07px; background transparent; text Graphik 16/normal 400, #000000 `color.bsr.grey.1000`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #000000 `color.bsr.grey.1000` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.absolute.left-4 40.0x40.0 1px auto rgb(16, 16, 16) offset 0px 3.35544e+07px |

![Back button default](components/crops/back-btn-default.png) ![Back button hover](components/crops/back-btn-hover.png) ![Back button focus-visible](components/crops/back-btn-focus-visible.png) ![Back button pressed](components/crops/back-btn-pressed.png)

#### First name field
The firstName input; focused and typed into then cleared — never submitted. Read as `field-firstname` on the brand application page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 186 x 20; background transparent; text Graphik_fix 14/20 400, #333333 `color.grey.900`; placeholder #333333 `color.grey.900` |
| focused, filled | text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000`; placeholder #000000 `color.bsr.grey.1000` |

![First name field default](components/crops/field-firstname-default.png) ![First name field focused](components/crops/field-firstname-focused.png) ![First name field filled](components/crops/field-firstname-filled.png)

#### Last name field
The lastName input; focused and typed into then cleared — never submitted. Read as `field-lastname` on the brand application page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 186 x 20; background transparent; text Graphik_fix 14/20 400, #333333 `color.grey.900`; placeholder #333333 `color.grey.900` |
| focused, filled | text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000`; placeholder #000000 `color.bsr.grey.1000` |

![Last name field default](components/crops/field-lastname-default.png) ![Last name field focused](components/crops/field-lastname-focused.png) ![Last name field filled](components/crops/field-lastname-filled.png)

#### Email field
The work-email input; focused and typed into then cleared — never submitted. Read as `field-email` on the brand application page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 430 x 20; background transparent; text Graphik_fix 14/20 400, #333333 `color.grey.900`; placeholder #333333 `color.grey.900` |
| focused, filled | text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000`; placeholder #000000 `color.bsr.grey.1000` |

![Email field default](components/crops/field-email-default.png) ![Email field focused](components/crops/field-email-focused.png) ![Email field filled](components/crops/field-email-filled.png)

#### Phone field
The phoneNumber input with its +1 country-code prefix button; focused and typed into then cleared — never submitted. Read as `field-phone` on the brand application page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 406 x 40; padding 0px 16px; background transparent; text graphik 14/20 200, #333333 `color.grey.900`; placeholder #333333 `color.grey.900` |

![Phone field default](components/crops/field-phone-default.png) ![Phone field focused](components/crops/field-phone-focused.png) ![Phone field filled](components/crops/field-phone-filled.png)

#### Country code button
The +1 country-code prefix button inside the phone field; measured, never opened. Read as `phone-code-btn` on the brand application page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 64 x 40; padding 0px 10px; border R: 1px solid #dadada `color.grey.400`; radius 4px 0px 0px 4px; background #ffffff `color.bsr.grey.100`; text graphik 14/20 200, #333333 `color.grey.900`; icon 8 x 8, #333333 `color.grey.900` |
| focus-visible | border R: 1px solid #8e8c8c `color.grey.600`; outline 2px solid #101010, offset 0px |

![Country code button default](components/crops/phone-code-btn-default.png) ![Country code button hover](components/crops/phone-code-btn-hover.png) ![Country code button focus-visible](components/crops/phone-code-btn-focus-visible.png) ![Country code button pressed](components/crops/phone-code-btn-pressed.png)

#### Password field
The password input (with a show-password icon); focused only — nothing was typed or submitted. Read as `field-password` on the brand application page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 414 x 20; background transparent; text Graphik_fix 14/20 400, #333333 `color.grey.900`; placeholder #333333 `color.grey.900` |
| focused | text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000`; placeholder #000000 `color.bsr.grey.1000` |

![Password field default](components/crops/field-password-default.png) ![Password field focused](components/crops/field-password-focused.png)

#### Show password icon button
The fs-icon-button--plain show/hide toggle inside the password field; measured, never pressed. Read as `show-password` on the brand application page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 16 x 16; border 1px solid transparent; radius 4px; background rgba(51, 51, 51, 0) `color.transparent.grey.0`; text Graphik_fix 14/20 400, #333333 `color.grey.900`; icon 16 x 16, #333333 `color.grey.900` |
| hover | text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000`; icon 16 x 16, #000000 `color.bsr.grey.1000` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 8px |
| pressed | text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000`; icon 16 x 16, #000000 `color.bsr.grey.1000` |

![Show password icon button default](components/crops/show-password-default.png) ![Show password icon button hover](components/crops/show-password-hover.png) ![Show password icon button focus-visible](components/crops/show-password-focus-visible.png) ![Show password icon button pressed](components/crops/show-password-pressed.png)

#### Terms checkbox
The fs-checkbox for the terms consent; measured, never toggled. Read as `checkbox-terms` on the brand application page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 14 x 14; background transparent; text Graphik_fix 14/20 400, #333333 `color.grey.900`; placeholder #333333 `color.grey.900` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 2px; layers input.fs-checkbox__input.focusable 14.0x14.0 2px solid rgb(39, 94, 197) offset 2px |

![Terms checkbox default](components/crops/checkbox-terms-default.png) ![Terms checkbox focus-visible](components/crops/checkbox-terms-focus-visible.png)

#### Marketing checkbox
The opt-in fs-checkbox; measured, never toggled. Read as `checkbox-marketing` on the brand application page.

**Values (default).** size 14 x 14; background transparent; text Graphik_fix 14/20 400, #333333 `color.grey.900`; placeholder #333333 `color.grey.900`.

![Marketing checkbox default](components/crops/checkbox-marketing-default.png)

#### Next button
The form's dark fs-button--primary "Next" submit; its states were measured but the button was never clicked — nothing was submitted. Read as `next-btn` on the brand application page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 472 x 48; padding 0px 20px; border 1px solid transparent; radius 4px; background #333333 `color.grey.900`; text Graphik_fix 14/20 400, #ffffff `color.bsr.grey.100` |
| hover | background #000000 `color.bsr.grey.1000` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px |
| pressed | background #000000 `color.bsr.grey.1000` |

![Next button default](components/crops/next-btn-default.png) ![Next button hover](components/crops/next-btn-hover.png) ![Next button focus-visible](components/crops/next-btn-focus-visible.png) ![Next button pressed](components/crops/next-btn-pressed.png)

#### Application heading
The /apply step heading ("Welcome! Sign up to sell on Faire." — an h4 in the f_t_displaySSerifRegular serif role). Read as `apply-heading` on the brand application page.

**Values (default).** size 472 x 38; background transparent; text nantes 30/38 400, #333333 `color.grey.900`.

![Application heading default](components/crops/apply-heading-default.png)

### Sign-in dialog

The 'Sign in to Faire' fs-modal mounted by ?signIn=1 over the home page — e-mail and password fields, the dark Sign in submit, Google/Apple SSO buttons, a sign-up link and the close icon; measured at rest, never submitted.

#### Sign-in dialog
The "Sign in to Faire" fs-modal mounted by ?signIn=1 over the home page: email + password fields, dark submit, Google and Apple SSO, a sign-up link and the close icon. Read as `signin-dialog` on the sign-in dialog page.

**Values (default).** size 420 x 649; background #ffffff `color.bsr.grey.100`; text GT Canon 30/38 400, #161616 `color.bsr.grey.900`; icon 16 x 16, #161616 `color.bsr.grey.900`.

![Sign-in dialog default](components/crops/signin-dialog-default.png)

#### Sign in submit
The dialog's Sign in submit button; its states were measured but the button was never clicked — nothing was submitted. Read as `signin-submit` on the sign-in dialog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 340 x 48; padding 0px 20px; border 1px solid transparent; radius 4px; background #161616 `color.bsr.grey.900`; text GT Standard 14/20 400, #ffffff `color.bsr.grey.100` |
| hover | background #474747 `color.bsr.grey.800` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px |
| pressed | background #000000 `color.bsr.grey.1000` |

![Sign in submit default](components/crops/signin-submit-default.png) ![Sign in submit hover](components/crops/signin-submit-hover.png) ![Sign in submit focus-visible](components/crops/signin-submit-focus-visible.png) ![Sign in submit pressed](components/crops/signin-submit-pressed.png)

#### Email field (sign-in)
The email input in the sign-in dialog; focused and typed into then cleared — never submitted. Read as `signin-email` on the sign-in dialog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 298 x 20; background transparent; text GT Standard 14/20 400, #161616 `color.bsr.grey.900`; placeholder oklab(0.200175 0.00000910461 0.00000399351 / 0.5) |
| focused, filled | text GT Standard 14/20 400, #000000 `color.bsr.grey.1000`; placeholder oklab(0 0 0 / 0.5) |

![Email field (sign-in) default](components/crops/signin-email-default.png) ![Email field (sign-in) focused](components/crops/signin-email-focused.png) ![Email field (sign-in) filled](components/crops/signin-email-filled.png)

#### Password field (sign-in)
The password input in the sign-in dialog; focused only — nothing was typed or submitted. Read as `signin-password` on the sign-in dialog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 282 x 20; background transparent; text GT Standard 14/20 400, #161616 `color.bsr.grey.900`; placeholder oklab(0.200175 0.00000910461 0.00000399351 / 0.5) |
| focused | text GT Standard 14/20 400, #000000 `color.bsr.grey.1000`; placeholder oklab(0 0 0 / 0.5) |

![Password field (sign-in) default](components/crops/signin-password-default.png) ![Password field (sign-in) focused](components/crops/signin-password-focused.png)

#### Google SSO button
"Sign in with Google"; measured, never followed. Read as `signin-google` on the sign-in dialog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 340 x 48; padding 0px 24px; border 1px solid #e4e1de `color.bsr.neutral.500`; radius 4px; background #ffffff `color.bsr.grey.100`; text GT Standard 14/20 400, #161616 `color.bsr.grey.900`; icon 20 x 20, #161616 `color.bsr.grey.900` |
| hover | background #474747 `color.bsr.grey.800`; text GT Standard 14/20 400, #ffffff `color.bsr.grey.100`; icon 20 x 20, #ffffff `color.bsr.grey.100` |
| focus-visible | outline 2px solid #101010, offset 2px |
| pressed | background #474747 `color.bsr.grey.800`; text GT Standard 14/20 400, #ffffff `color.bsr.grey.100`; icon 20 x 20, #ffffff `color.bsr.grey.100` |

![Google SSO button default](components/crops/signin-google-default.png) ![Google SSO button hover](components/crops/signin-google-hover.png) ![Google SSO button focus-visible](components/crops/signin-google-focus-visible.png) ![Google SSO button pressed](components/crops/signin-google-pressed.png)

#### Apple SSO button
"Sign in with Apple"; measured, never followed. Read as `signin-apple` on the sign-in dialog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 340 x 48; padding 0px 24px; border 1px solid #e4e1de `color.bsr.neutral.500`; radius 4px; background #ffffff `color.bsr.grey.100`; text GT Standard 14/20 400, #161616 `color.bsr.grey.900`; icon 20 x 20, #161616 `color.bsr.grey.900` |
| hover | background #474747 `color.bsr.grey.800`; text GT Standard 14/20 400, #ffffff `color.bsr.grey.100`; icon 20 x 20, #ffffff `color.bsr.grey.100` |
| focus-visible | outline 2px solid #101010, offset 2px |
| pressed | background #474747 `color.bsr.grey.800`; text GT Standard 14/20 400, #ffffff `color.bsr.grey.100`; icon 20 x 20, #ffffff `color.bsr.grey.100` |

![Apple SSO button default](components/crops/signin-apple-default.png) ![Apple SSO button hover](components/crops/signin-apple-hover.png) ![Apple SSO button focus-visible](components/crops/signin-apple-focus-visible.png) ![Apple SSO button pressed](components/crops/signin-apple-pressed.png)

#### Sign up link (sign-in)
The "Sign up" action inside the sign-in dialog; measured, never followed. Read as `signin-signup-link` on the sign-in dialog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 340 x 48; padding 0px 20px; border 1px solid #dadada `color.grey.400`; radius 4px; background #ffffff `color.bsr.grey.100`; text GT Standard 14/20 400, #161616 `color.bsr.grey.900` |
| hover | border 1px solid #000000 `color.bsr.grey.1000`; background #f1f1f1 `color.grey.300`; text GT Standard 14/20 400, #000000 `color.bsr.grey.1000` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px |
| pressed | border 1px solid #000000 `color.bsr.grey.1000`; background #f1f1f1 `color.grey.300`; text GT Standard 14/20 400, #000000 `color.bsr.grey.1000` |

![Sign up link (sign-in) default](components/crops/signin-signup-link-default.png) ![Sign up link (sign-in) hover](components/crops/signin-signup-link-hover.png) ![Sign up link (sign-in) focus-visible](components/crops/signin-signup-link-focus-visible.png) ![Sign up link (sign-in) pressed](components/crops/signin-signup-link-pressed.png)

#### Dialog close button
The dialog's "Close modal" icon button; measured, never pressed. Read as `signin-close` on the sign-in dialog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; radius 4px; background rgba(51, 51, 51, 0) `color.transparent.grey.0`; text GT Standard 16/normal 400, #161616 `color.bsr.grey.900`; icon 16 x 16, #161616 `color.bsr.grey.900` |
| hover | background #f1f1f1 `color.grey.300`; text GT Standard 16/normal 400, #000000 `color.bsr.grey.1000` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px |
| pressed | background #f1f1f1 `color.grey.300`; text GT Standard 16/normal 400, #000000 `color.bsr.grey.1000` |

![Dialog close button default](components/crops/signin-close-default.png) ![Dialog close button hover](components/crops/signin-close-hover.png) ![Dialog close button focus-visible](components/crops/signin-close-focus-visible.png) ![Dialog close button pressed](components/crops/signin-close-pressed.png)

#### Show password icon (sign-in)
The eye icon inside the password field; measured, never pressed. Read as `signin-show-password` on the sign-in dialog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 16 x 16; border 1px solid transparent; radius 4px; background rgba(51, 51, 51, 0) `color.transparent.grey.0`; text GT Standard 14/20 400, #161616 `color.bsr.grey.900`; icon 16 x 16, #161616 `color.bsr.grey.900` |
| hover | text GT Standard 14/20 400, #000000 `color.bsr.grey.1000`; icon 16 x 16, #000000 `color.bsr.grey.1000` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 8px |
| pressed | text GT Standard 14/20 400, #000000 `color.bsr.grey.1000`; icon 16 x 16, #000000 `color.bsr.grey.1000` |

![Show password icon (sign-in) default](components/crops/signin-show-password-default.png) ![Show password icon (sign-in) hover](components/crops/signin-show-password-hover.png) ![Show password icon (sign-in) focus-visible](components/crops/signin-show-password-focus-visible.png) ![Show password icon (sign-in) pressed](components/crops/signin-show-password-pressed.png)

### Sign-up dialog

The 'Unlock wholesale pricing' fs-modal mounted by ?signUp=1 — the business-e-mail field, 'Sign up for free' submit, Google/Apple SSO and a sign-in link; measured at rest, never submitted. The same dialog mounts when a product tile is clicked.

#### Sign-up dialog
The "Unlock wholesale pricing" fs-modal mounted by ?signUp=1: business-email field, "Sign up for free" submit, Google and Apple SSO and a sign-in link. Read as `signup-dialog` on the sign-up dialog page.

**Values (default).** size 500 x 523; background #ffffff `color.bsr.grey.100`; text GT Canon 30/38 400, #161616 `color.bsr.grey.900`; icon 16 x 16, #161616 `color.bsr.grey.900`.

![Sign-up dialog default](components/crops/signup-dialog-default.png)

#### Business email field
The business-email input in the sign-up dialog; focused and typed into then cleared — never submitted. Read as `signup-email` on the sign-up dialog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 394 x 20; background transparent; text GT Standard 14/20 400, #161616 `color.bsr.grey.900`; placeholder #161616 `color.bsr.grey.900` |
| focused, filled | text GT Standard 14/20 400, #000000 `color.bsr.grey.1000`; placeholder #000000 `color.bsr.grey.1000` |

![Business email field default](components/crops/signup-email-default.png) ![Business email field focused](components/crops/signup-email-focused.png) ![Business email field filled](components/crops/signup-email-filled.png)

#### Sign up submit
The dialog's "Sign up for free" submit button; its states were measured but the button was never clicked — nothing was submitted. Read as `signup-submit` on the sign-up dialog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 436 x 48; padding 0px 20px; border 1px solid transparent; radius 4px; background #161616 `color.bsr.grey.900`; text GT Standard 14/20 400, #ffffff `color.bsr.grey.100` |
| hover | background #474747 `color.bsr.grey.800` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px |
| pressed | background #000000 `color.bsr.grey.1000` |

![Sign up submit default](components/crops/signup-submit-default.png) ![Sign up submit hover](components/crops/signup-submit-hover.png) ![Sign up submit focus-visible](components/crops/signup-submit-focus-visible.png) ![Sign up submit pressed](components/crops/signup-submit-pressed.png)

#### Google SSO button (sign-up)
"Sign up with Google"; measured, never followed. Read as `signup-google` on the sign-up dialog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 436 x 48; padding 0px 24px; border 1px solid #e4e1de `color.bsr.neutral.500`; radius 4px; background #ffffff `color.bsr.grey.100`; text GT Standard 14/20 400, #161616 `color.bsr.grey.900`; icon 20 x 20, #161616 `color.bsr.grey.900` |
| hover | background #474747 `color.bsr.grey.800`; text GT Standard 14/20 400, #ffffff `color.bsr.grey.100`; icon 20 x 20, #ffffff `color.bsr.grey.100` |
| focus-visible | outline 2px solid #101010, offset 2px |
| pressed | background #474747 `color.bsr.grey.800`; text GT Standard 14/20 400, #ffffff `color.bsr.grey.100`; icon 20 x 20, #ffffff `color.bsr.grey.100` |

![Google SSO button (sign-up) default](components/crops/signup-google-default.png) ![Google SSO button (sign-up) hover](components/crops/signup-google-hover.png) ![Google SSO button (sign-up) focus-visible](components/crops/signup-google-focus-visible.png) ![Google SSO button (sign-up) pressed](components/crops/signup-google-pressed.png)

#### Apple SSO button (sign-up)
"Sign up with Apple"; measured, never followed. Read as `signup-apple` on the sign-up dialog page.

Not on the page when it was captured.

#### Sign in link (sign-up)
The "Sign in" action inside the sign-up dialog; measured, never followed. Read as `signup-signin-link` on the sign-up dialog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 36 x 14; background transparent; text GT Standard M 12/16 400, #161616 `color.bsr.grey.900` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px; layers a.focusable.interactive 36.0x14.0 2px solid rgb(39, 94, 197) offset 1px |

![Sign in link (sign-up) default](components/crops/signup-signin-link-default.png) ![Sign in link (sign-up) hover](components/crops/signup-signin-link-hover.png) ![Sign in link (sign-up) focus-visible](components/crops/signup-signin-link-focus-visible.png) ![Sign in link (sign-up) pressed](components/crops/signup-signin-link-pressed.png)

#### Dialog close button (sign-up)
The dialog's "Close modal" icon button; measured, never pressed. Read as `signup-close` on the sign-up dialog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; radius 4px; background rgba(51, 51, 51, 0) `color.transparent.grey.0`; text GT Standard 16/normal 400, #161616 `color.bsr.grey.900`; icon 16 x 16, #161616 `color.bsr.grey.900` |
| hover | background #f1f1f1 `color.grey.300`; text GT Standard 16/normal 400, #000000 `color.bsr.grey.1000` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px |
| pressed | background #f1f1f1 `color.grey.300`; text GT Standard 16/normal 400, #000000 `color.bsr.grey.1000` |

![Dialog close button (sign-up) default](components/crops/signup-close-default.png) ![Dialog close button (sign-up) hover](components/crops/signup-close-hover.png) ![Dialog close button (sign-up) focus-visible](components/crops/signup-close-focus-visible.png) ![Dialog close button (sign-up) pressed](components/crops/signup-close-pressed.png)

### Help center

/support — the help-center masthead, the 'Search retailer guides' field and topic links.

#### Help search field
The "Search retailer guides" field; focused and typed into then cleared — nothing searched. Read as `help-search` on the help center page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 564 x 40; background transparent; text graphik 14/20 200, #333333 `color.grey.900`; placeholder oklab(0.321069 0.0000146478 0.0000064373 / 0.5) |

![Help search field default](components/crops/help-search-default.png) ![Help search field focused](components/crops/help-search-focused.png) ![Help search field filled](components/crops/help-search-filled.png)

#### Help topic link
A help topic link; measured, never followed. Read as `help-link` on the help center page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 471.98 x 162; padding 0px 0px 40px 56px; background transparent; text Graphik_fix 12/16 400, #333333 `color.grey.900`; layers div.fs-tag.fs-component 120.6x24.0 rgb(241, 241, 241) 2px |

Child layers that carry the look: div 120.6x24 background #f1f1f1 `color.grey.300` radius 2px.

![Help topic link default](components/crops/help-link-default.png) ![Help topic link hover](components/crops/help-link-hover.png) ![Help topic link focus-visible](components/crops/help-link-focus-visible.png) ![Help topic link pressed](components/crops/help-link-pressed.png)

#### Help center headline
The /support help-center masthead. Read as `help-h1` on the help center page.

**Values (default).** size 398 x 64; background transparent; text nantes 52/64 400, #333333 `color.grey.900`.

![Help center headline default](components/crops/help-h1-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the top bar with Menu button and search icon, the nav drawer the Menu button opens, the search overlay the magnifier opens and the hero.

#### Mobile top bar
The phone header: Faire mark, Menu button, Sign in. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 390 x 51; border B: 1px solid #dadada `color.grey.400`; background #ffffff `color.bsr.grey.100`; text Graphik_fix 14/20 400, #333333 `color.grey.900`; transition background 0.1s linear; icon 20 x 20, #333333 `color.grey.900`.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile menu button
The header Menu button that opens the nav drawer — a local UI toggle; the opened state was measured after activating it. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 52 x 50; padding 0px 16px; background transparent; text Graphik 16/normal 400, #333333 `color.grey.900`; icon 20 x 20, #333333 `color.grey.900` |
| focus-visible | outline 1px auto #e59700, offset 0px; layers button.relative.flex 52.0x50.0 1px auto rgb(229, 151, 0) offset 0px |

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png) ![Mobile menu button opened](components/crops/m-menu-btn-opened.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 317 x 38; background transparent; text Nantes_fix 30/38 400, #ffffff `color.bsr.grey.100`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile nav drawer
The nav drawer opened by the Menu button; its links were never followed. Read as `m-drawer` on the home page at 390 wide.

**Values (default).** size 312 x 844; radius 0px 4px 4px 0px; background #ffffff `color.bsr.grey.100`; text graphik 14/20 200, #ffffff `color.bsr.grey.100`; icon 16 x 16, #ffffff `color.bsr.grey.100`.

![Mobile nav drawer default](components/crops/m-drawer-default.png)

#### Mobile search button
The unlabelled magnifier icon button in the phone header; measured at rest (opening the search overlay is covered by m-search). Read as `m-search-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 40 x 21.34; radius 4px; background rgba(51, 51, 51, 0) `color.transparent.grey.0`; text Graphik_fix 14/20 400, #333333 `color.grey.900`; icon 20 x 20, #333333 `color.grey.900` |
| focus-visible | outline 2px solid #275ec5 `color.blue.700`, offset 1px |
| pressed | text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000` |

![Mobile search button default](components/crops/m-search-btn-default.png) ![Mobile search button hover](components/crops/m-search-btn-hover.png) ![Mobile search button focus-visible](components/crops/m-search-btn-focus-visible.png) ![Mobile search button pressed](components/crops/m-search-btn-pressed.png)

#### Mobile search field
The search field inside the overlay the magnifier button opens (a local UI toggle); focused and typed into then cleared — nothing searched. Read as `m-search` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 285.09 x 20; padding 0px 0px 0px 40px; background transparent; text Graphik_fix 14/20 400, #333333 `color.grey.900`; transition width 0.252s cubic-bezier(0.33, 1, 0.68, 1), opacity 0.252s cubic-bezier(0.33, 1, 0.68, 1); placeholder oklab(0.321069 0.0000146478 0.0000064373 / 0.5) |
| focused, filled | text Graphik_fix 14/20 400, #000000 `color.bsr.grey.1000`; placeholder oklab(0 0 0 / 0.5) |

![Mobile search field default](components/crops/m-search-default.png) ![Mobile search field focused](components/crops/m-search-focused.png) ![Mobile search field filled](components/crops/m-search-filled.png)

### Footer

The page footer: the brand promise line in the serif face, sitemap columns, locale/social links and the legal row.

#### Footer
The page footer: brand promise line, sitemap columns, locale and social links, legal row. Read as `footer` on the home page.

**Values (default).** size 1440 x 448; background transparent; text nantes 38/50 400, #333333 `color.grey.900`; icon 16 x 16, #333333 `color.grey.900`; layers button.interactive.focusable 140.1x48.0 rgb(255, 255, 255) T:1px solid rgb(218, 218, 218) / R:1px solid rgb(218, 218, 218) / B:1px solid rgb(218, 218, 218) / L:1px solid rgb(218, 218, 218) 4px; a.interactive.focusable 139.3x48.0 rgb(255, 255, 255) T:1px solid rgb(218, 218, 218) / R:1px solid rgb(218, 218, 218) / B:1px solid rgb(218, 218, 218) / L:1px solid rgb(218, 218, 218) 4px.

Child layers that carry the look: button 140.1x48 background #ffffff `color.bsr.grey.100` border 1px solid #dadada `color.grey.400` radius 4px; a 139.3x48 background #ffffff `color.bsr.grey.100` border 1px solid #dadada `color.grey.400` radius 4px.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 59.2 x 17; background transparent; text Graphik_fix 14/20 400, #333333 `color.grey.900` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Faire wordmark, the header glyphs, social icons, the product badges) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in marketplace

Faire's product is the marketplace: every surface past the sign-up/sign-in dialogs — search results, product detail, cart, checkout, orders, the retailer and brand dashboards — needs an account and was never reached. Product tiles link to `?signUp=product`, which mounts the sign-up dialog: the deepest public surface, and it was measured as a form, never submitted. The /brand-portal route redirects to sign-in.

### Pages

- **The account.** Every post-sign-in surface was never reached; both auth dialogs were measured at rest and never submitted; Google/Apple SSO was never followed.
- **Forms.** The /apply brand application was measured at rest and typed into then cleared — 'Next' was never pressed; what the second step or a submission returns is unverified.
- **Cloudflare.** The edge intermittently serves a Turnstile interstitial, worst on the category/suppliers/brand routes; those components were captured across several passes and a few entries below are marked missing or carry `recaptureMissed` runs — the routes it ate during a pass are documented, not patched over.
- **Blog.** The header's Blog link leaves faire.com for the blog subdomain; not captured.
- **Newsroom articles** are not followed; /news is covered by the index and its cards.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **Dialog fields' validation states** are unseen — validation needs a submit, which was never performed.
- **signup-apple** is absent from the sign-up dialog as rendered to this client (Google only); `brand-tile`, `sup-h1` and `wall-submit` stayed missing/unmeasured because the routes degraded during every later pass.

### Themes

faire.com has no user theme toggle, no theme attribute and no `prefers-color-scheme` switch: one light theme signed out. The vars probe resolved every custom property a second time under a `dark` class nothing on the site sets and the values are identical — the only "dark" contexts are inverse surfaces inside the light page (the dark marketing band, controls over hero media), which the declared `.fs-mode-on-surface` scope re-themes; its resolved values sit under `light.color.onSurface.*`.

### Fonts

- **Graphik_fix** (the UI sans — body, controls, fields), **Nantes_fix** (the marketing display serif — mastheads, the footer promise line) are the declared faces; **GT Canon** (category mastheads, dialog titles), **GT Standard** (large CTAs) and **GT Standard M** (mono accents) appear in measured styles. All are served woff2 faces from cdn.faire.com; the style guide falls back to system sans.

### Screenshots

- The product photography, brand imagery and video frames in the screenshots are the site's published content.
- The suppliers-candles default screenshot caught the skeleton loader; the full shot and the measurements show the real listing.
- Full-page shots are bounded at eight chunks; the bounds each page hit are in the `.png.capture.json` sidecars.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article copy, product names, brand names and prices are the site's content; only frames and components were measured.
