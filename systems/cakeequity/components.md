# Cake Equity components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from cakeequity.com on 2026-11-11, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844 visual, over the ~745px layout the page forces), with computed styles read from the running page. Nothing was signed into, bought or submitted; the login card was never filled; the plan and demo actions were never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (44 components, 97 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (96 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every surface paints `light` — the dark looks are regions on the page (the footer, the Cake-MCP band), not a theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [faq-open](screenshots/home-light-faq-open.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [quarterly](screenshots/pricing-light-quarterly.png) |
| Feature (cap table) | `/features/cap-table` | [default](screenshots/feature-light-default.png), [full](screenshots/feature-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Demo request | `/demo-request` | [default](screenshots/demo-light-default.png), [full](screenshots/demo-light-full.png) |
| Product tour | `/product-tour` | [default](screenshots/tour-light-default.png), [full](screenshots/tour-light-full.png) |
| Log in (hosted auth) | `app.cakeequity.com/login` | [default](screenshots/login-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the menu button's own toggle (a programmatic click — a pointer tap pans the widened page) | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-button](#mobile-menu-button) |
| Desktop mega-nav | every marketing page | the Product trigger's own hover toggle | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#mega-nav-panel), [menu-link](#menu-link) |
| Billing-period toggle | /pricing | the Yearly/Quarterly switch's own toggle | [pricing-light-quarterly](screenshots/pricing-light-quarterly.png), [billing-toggle](#billing-toggle) |
| FAQ accordion | home | the question's own click toggle | [home-light-faq-open](screenshots/home-light-faq-open.png), [faq-item](#faq-item) |
| Chatbase chat widget | every page | hidden, never opened (a third-party widget, not Cake chrome) | hidden before every shot and reading |
| HubSpot demo form | /demo-request | a cross-origin iframe embed | [demo-form](#demo-form-embed) measured as a region; its inner fields are third-party paint, never filled |
| Signed-in product | app.cakeequity.com workspace | the equity-management app lives behind the hosted login | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 16 components were given a real keyboard focus. 14 draw an outline ring: `nav-link` (1px auto #005fcc `color.measured.focus`, offset 1px), `nav-login` (1px auto #005fcc `color.measured.focus`, offset 1px), `nav-demo` (1px auto #005fcc `color.measured.focus`, offset 1px), `nav-cta` (1px auto #005fcc `color.measured.focus`, offset 1px), `announce-pill` (1px auto #005fcc `color.measured.focus`, offset 1px), `hero-cta` (1px auto #005fcc `color.measured.focus`, offset 1px), `hero-demo` (1px auto #015ecc, offset 0.984375px), `plan-cta` (1px auto #005fcc `color.measured.focus`, offset 1px), `collection-card` (on a child: 1px auto rgb(0, 95, 204) offset 1px), `login-cta` (2px solid #0054f0 `color.auth.focus`, offset 2px), `login-oauth` (2px solid #0054f0 `color.auth.focus`, offset 2px), `login-link` (2px solid #0054f0 `color.auth.focus`, offset 2px), `footer-link` (1px auto #005fcc `color.measured.focus`, offset 1px), `social-icon` (1px auto #005fcc `color.measured.focus`, offset 1px). 1 change only their border: `menu-link`. The other 1 show no measured change: `nav-trigger`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.25, 0, 0.1, 1)` | border-color, outline-offset | login-cta, login-field, login-link, login-oauth |
| 0.15s | `cubic-bezier(0.25, 0, 1, 1)` | background-color | login-cta, login-oauth |
| 0.15s | `cubic-bezier(0.9, 0, 0.1, 1)` | color | login-link |
| 0.2s | `ease` | all, opacity | footer-link, hero-cta, nav-cta, nav-demo, nav-link, nav-login, plan-cta, social-icon and more |
| 0.3s | `ease` | transform | faq-item |
| 0.4s | `ease` | all | hero-demo |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 312 x 741.2 | 1px solid rgba(126, 120, 255, 0.25) `color.plum.25` | 0px 0px 20px 20px | #ffffff `color.neutral.white` | none | 0 |
| [Story card](#story-card) | 420 x 102.73 | - | 16px | #ffffff `color.neutral.white` | rgba(0, 0, 0, 0.2) 0px 2px 5px 0px | 16px |
| [Announcement pill](#announcement-pill) | 334.83 x 37 | 1px solid #ebe8f2 `color.measured.chip-border` | 100px | #ffffff `color.neutral.white` | none | 5px 16px 5px 5px |
| [FAQ item](#faq-item) | 907.19 x 79.88 | B: 1px solid rgba(24, 22, 26, 0.1) `color.ink.10` | - | transparent | none | 16px 0px |
| [Demo form embed](#demo-form-embed) | 599.59 x 1122.13 | - | 20px | #ffffff `color.neutral.white` | none | 20px |
| [Login card](#login-card) | 496 x 608.53 | - | 16px | #ffffff `color.neutral.white` | none | 48px |
| [Country select](#country-select) | 200 x 48 | 1px solid #d9d9e0 `color.measured.field-border` | 100px | #ffffff `color.neutral.white` | none | 8px 18px |
| [Billing toggle](#billing-toggle) | 236 x 48 | - | - | transparent | none | 0px 0px 0px 20px |

## Components

### Shell and navigation

The fixed marketing navbar: the cake. wordmark, the Product/Solutions mega-nav, the Pricing link, Login, Book-a-demo and the violet Get-started-free pill.

#### Header
The fixed marketing navbar: wordmark, Product/Solutions/Resources/Customers mega-nav, Pricing link, Login, Book-a-demo and Get-started-free. Read as `header` on the home page.

**Values (default).** size 1440 x 74.19; background transparent; shadow rgba(0, 0, 0, 0.2) 0px 2px 20px -19px; text Inter 14/18.2 400, #222222 `color.measured.nav-text`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1; div.navbar.w-nav 1440.0x74.2 rgba(0, 0, 0, 0.2) 0px 2px 20px -19px; div.navbar-bg-shadow 1440.0x0.0 rgba(0, 0, 0, 0.1) 0px 1px 30px 0px; div.absolute-border 0.0x2.0 rgb(126, 120, 255); div.nav-container.for-dropdown 0.0x0.0 rgb(255, 255, 255) rgba(24, 22, 26, 0.25) 0px 0px 20px -5px 20px; div.nav-grid-column-item 0.0x0.0 T:.

![Header default](components/crops/header-default.png)

#### Logo
The cake. wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 100 x 31.7; background transparent; text Inter 14/0 400, #333333.

![Logo default](components/crops/logo-default.png)

#### Nav trigger
The Product mega-nav toggle; opens its panel on hover (Webflow w-dropdown), never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 95.95 x 58.19; padding 20px 10px; background transparent; text Inter 14/18.2 400, #222222 `color.measured.nav-text`; layers div.absolute-border 0.0x2.0 rgb(126, 120, 255) |
| hover | text Inter 14/18.2 400, #4823ff `color.plum.bright`; layers div.absolute-border 96.0x2.0 rgb(126, 120, 255) |
| pressed | text Inter 14/18.2 400, #4823ff `color.plum.bright` |

Child layers that carry the look: div 0x2 background #7e78ff `color.plum.100`.

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav link
The plain Pricing header link. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 45.28 x 18.19; background transparent; text Inter 14/18.2 400, #222222 `color.measured.nav-text`; transition all 0.2s ease |
| hover | text Inter 14/18.2 400, #4823ff `color.plum.bright` |
| focus-visible | outline 1px auto #005fcc `color.measured.focus`, offset 1px; layers a.nav-link.w-nav-link 45.3x18.2 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text Inter 14/18.2 400, #4823ff `color.plum.bright` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Login link
The Login header action (links to app.cakeequity.com); measured never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 88.19 x 44.19; padding 12px 25px 10px 25px; border 1px solid transparent; radius 50px; background transparent; text Inter 14/18.2 400, #18161a `color.ink.100`; transition all 0.2s ease |
| hover | border 1px solid rgba(126, 120, 255, 0.25) `color.plum.25`; background rgba(126, 120, 255, 0.25) `color.plum.25` |
| focus-visible | outline 1px auto #005fcc `color.measured.focus`, offset 1px |
| pressed | border 1px solid rgba(126, 120, 255, 0.25) `color.plum.25`; background rgba(126, 120, 255, 0.25) `color.plum.25` |

![Login link default](components/crops/nav-login-default.png) ![Login link hover](components/crops/nav-login-hover.png) ![Login link focus-visible](components/crops/nav-login-focus-visible.png) ![Login link pressed](components/crops/nav-login-pressed.png)

#### Book-a-demo button
The secondary header action (primary-button-nav light-grey). Read as `nav-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 124.36 x 44.19; padding 12px 18px; border 1px solid #4823ff `color.plum.bright`; radius 100px; background rgba(255, 255, 255, 0); text Inter 14/18.2 400, #4823ff `color.plum.bright`; transition all 0.2s ease |
| hover | border 1px solid #2b1599 `color.plum.dark`; background #2b1599 `color.plum.dark`; text Inter 14/18.2 400, #ffffff `color.neutral.white` |
| focus-visible | outline 1px auto #005fcc `color.measured.focus`, offset 1px |
| pressed | border 1px solid #2b1599 `color.plum.dark`; background #2b1599 `color.plum.dark`; text Inter 14/18.2 400, #ffffff `color.neutral.white` |

![Book-a-demo button default](components/crops/nav-demo-default.png) ![Book-a-demo button hover](components/crops/nav-demo-hover.png) ![Book-a-demo button focus-visible](components/crops/nav-demo-focus-visible.png) ![Book-a-demo button pressed](components/crops/nav-demo-pressed.png)

#### Nav CTA
The Get-started-free header action; links to the app signup, measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 143.39 x 44.19; padding 12px 18px; border 1px solid #4823ff `color.plum.bright`; radius 100px; background #4823ff `color.plum.bright`; text Inter 14/18.2 400, #ffffff `color.neutral.white`; transition all 0.2s ease |
| hover | border 1px solid #2b1599 `color.plum.dark`; background #2b1599 `color.plum.dark` |
| focus-visible | outline 1px auto #005fcc `color.measured.focus`, offset 1px |
| pressed | border 1px solid #2b1599 `color.plum.dark`; background #2b1599 `color.plum.dark` |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Mega-nav panel
The Product mega-menu panel, opened by hovering its own trigger. Read as `nav-dropdown` on the home page.

**Values (default).** size 1008 x 459.38; padding 0px 8px 40px 8px; background transparent; text Inter 12.6/16.38 400, #333333; layers div.nav-container.for-dropdown 992.0x407.4 rgb(255, 255, 255) rgba(24, 22, 26, 0.25) 0px 0px 20px -5px 20px; div.nav-grid-column-item 213.2x299.0 T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255); div.spacer-with-line 211.2x1.0 rgba(24, 22, 26, 0.1); div.product-shipped.now-live 63.5x22.0 rgb(235, 255, 233) 50px; div.n.

Child layers that carry the look: div 992x407.4 background #ffffff `color.neutral.white` radius 20px shadow rgba(24, 22, 26, 0.25) `color.ink.25` 0px 0px 20px -5px; div 213.2x299 border 1px solid #ffffff `color.neutral.white`; div 211.2x1 background rgba(24, 22, 26, 0.1) `color.ink.10`.

![Mega-nav panel default](components/crops/nav-dropdown-default.png)

#### Menu link
A feature link inside the opened mega-nav. Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 211.16 x 46.88; padding 10px 0px 10px 45px; background transparent; text Inter 16.8/26.88 600, #18161a `color.ink.100` |
| hover, focus-visible, pressed | background rgba(126, 120, 255, 0.1) `color.plum.10`; image url(…); text Inter 16.8/26.88 600, #4823ff `color.plum.bright` |

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link focus-visible](components/crops/menu-link-focus-visible.png) ![Menu link pressed](components/crops/menu-link-pressed.png)

### Home

The 60px Exposure hero over the announcement chip, the violet and ghost CTAs, the section eyebrows, the #0e0d12 Cake-MCP band, the story quote cards and the FAQ accordion.

#### Announcement pill
The Pulley announcement chip above the hero (links to the managed-migration section anchor). Read as `announce-pill` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 334.83 x 37; padding 5px 16px 5px 5px; border 1px solid #ebe8f2 `color.measured.chip-border`; radius 100px; background #ffffff `color.neutral.white`; text Inter 15/16.8 500, #18161a `color.ink.100` |
| hover | text Inter 15/16.8 500, #4823ff `color.plum.bright` |
| focus-visible | outline 1px auto #005fcc `color.measured.focus`, offset 1px |
| pressed | text Inter 15/16.8 500, #4823ff `color.plum.bright` |

![Announcement pill default](components/crops/announce-pill-default.png) ![Announcement pill hover](components/crops/announce-pill-hover.png) ![Announcement pill focus-visible](components/crops/announce-pill-focus-visible.png) ![Announcement pill pressed](components/crops/announce-pill-pressed.png)

#### Hero headline
The "The equity platform for growing startups" display headline in Exposure. Read as `hero-title` on the home page.

**Values (default).** size 579.69 x 132; background transparent; text Exposure Light 60/66 400, #18161a `color.ink.100`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede under the headline (body-medium). Read as `hero-sub` on the home page.

**Values (default).** size 579.69 x 96; background transparent; text Inter 20/32 600, #18161a `color.ink.100`.

![Hero copy default](components/crops/hero-sub-default.png)

#### Hero CTA
The hero Get-started action (primary-button-v2); links to the app signup, measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 188.5 x 58.8; padding 20px 36px; border 1px solid #4823ff `color.plum.bright`; radius 100px; background #4823ff `color.plum.bright`; text Inter 19.2/16.8 400, #ffffff `color.neutral.white`; transition all 0.2s ease |
| hover | border 1px solid #2b1599 `color.plum.dark`; background #2b1599 `color.plum.dark` |
| focus-visible | outline 1px auto #005fcc `color.measured.focus`, offset 1px |
| pressed | border 1px solid #2b1599 `color.plum.dark`; background #2b1599 `color.plum.dark` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero secondary
The hero Book-a-demo ghost button (transparent-button-v2). Read as `hero-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 188.5 x 58.8; padding 20px 36px; border 1px solid #4823ff `color.plum.bright`; radius 100px; background rgba(255, 255, 255, 0); text Inter 19.2/16.8 400, #4823ff `color.plum.bright`; transition all 0.4s ease |
| hover | border 1px solid #2b1599 `color.plum.dark`; background #2b1599 `color.plum.dark`; text Inter 19.2/16.8 400, #ffffff `color.neutral.white` |
| focus-visible | outline 1px auto #015ecc, offset 0.984375px |
| pressed | border 1px solid #2b1599 `color.plum.dark`; background #2b1599 `color.plum.dark`; text Inter 19.2/16.8 400, #ffffff `color.neutral.white` |

![Hero secondary default](components/crops/hero-demo-default.png) ![Hero secondary hover](components/crops/hero-demo-hover.png) ![Hero secondary focus-visible](components/crops/hero-demo-focus-visible.png) ![Hero secondary pressed](components/crops/hero-demo-pressed.png)

#### Section eyebrow
A small-caps section label (eyebrow-2 plum). Read as `eyebrow` on the home page.

**Values (default).** size 152 x 29.2; padding 5px 0px; background transparent; text Inter 16/19.2 600, rgba(24, 22, 26, 0.5) `color.ink.50`.

![Section eyebrow default](components/crops/eyebrow-default.png)

#### Section heading
A 44px section heading. Read as `section-h2` on the home page.

**Values (default).** size 565.33 x 44; background transparent; text Exposure Light 44/44 300, #18161a `color.ink.100`; layers span.hp26-mark 349.3x53.0.

Child layers that carry the look: span 349.3x53 image linear-gradient(transparent 64%, #e7ff6e `color.lemon.100` 64%, #e7ff6e `color.lemon.100` .

![Section heading default](components/crops/section-h2-default.png)

#### Dark band
The Cake-MCP section: the one dark surface on the page (hp26-aidark-2). Read as `dark-section` on the home page.

**Values (default).** size 1296 x 635; radius 28px; background #0e0d12 `color.measured.dark-band`; image url(…); text Inter 14/16.8 600, #e7ff6e `color.lemon.100`.

![Dark band default](components/crops/dark-section-default.png)

#### Story card
A customer-quote card in the stories section. Read as `story-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 420 x 102.73; padding 16px; radius 16px; background #ffffff `color.neutral.white`; shadow rgba(0, 0, 0, 0.2) 0px 2px 5px 0px; text Exposure Light 18/23.4 300, #18161a `color.ink.100`; transition opacity 0.2s ease; transform translate(-210px, -6px); opacity 0 |
| hover | transform translate(-210px, -12px); opacity none |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Story card default](components/crops/story-card-default.png) ![Story card hover](components/crops/story-card-hover.png) ![Story card pressed](components/crops/story-card-pressed.png)

#### FAQ item
A Frequently-Asked accordion card; toggled open by clicking its question wrap (a local UI toggle revealing the answer). Read as `faq-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 907.19 x 79.88; padding 16px 0px; border B: 1px solid rgba(24, 22, 26, 0.1) `color.ink.10`; background transparent; text Inter 22.4/26.88 300, #18161a `color.ink.100`; transition transform 0.3s ease; layers div.faq-item-card 907.2x79.9 B:1px solid rgba(24, 22, 26, 0.1); div.faq-open-icon-vertical 1.0x12.0 rgb(126, 120, 255) 20px; div.faq-open-icon-horizontal 12.0x1.0 rgb(126, 120, 255) 20px |
| opened | size 907.19 x 301.64; shadow rgba(0, 0, 0, 0.2) 0px 2px 10px -8px; transform translate(0px, -2px); layers div.faq-item-card 907.2x301.6 B:1px solid rgba(24, 22, 26, 0.1) rgba(0, 0, 0, 0.2) 0px 2px 10px -8px; div.faq-open-icon-vertical 12.0x1.0 rgb(126, 120, 255) 20px; div.faq-open-icon-horizontal 12.0x1.0 rgb(126, 120, 255) 20px |

Child layers that carry the look: div 907.2x79.9 border 1px solid rgba(24, 22, 26, 0.1) `color.ink.10`; div 1x12 background #7e78ff `color.plum.100` radius 20px; div 12x1 background #7e78ff `color.plum.100` radius 20px.

![FAQ item default](components/crops/faq-item-default.png) ![FAQ item opened](components/crops/faq-item-opened.png)

### Pricing

The pricing surface: the region select that re-prices the plans, the Yearly/Quarterly save switch, the white plan cards (Growth featured, plum-bordered) and their violet Start-free actions.

#### Pricing title
The "Growth-friendly pricing, no complexity" display heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 1043.23 x 66; background transparent; text Exposure Light 60/66 400, #18161a `color.ink.100`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Country select
The region <select> (United States/Canada/Australia/UK/Singapore/New Zealand) that re-prices the plans; geo-defaulted to Singapore in this capture. Tapped into focus, never changed. Read as `country-select` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 200 x 48; padding 8px 18px; border 1px solid #d9d9e0 `color.measured.field-border`; radius 100px; background #ffffff `color.neutral.white`; text Inter 14/normal 500, #18161a `color.ink.100` |
| focused | border 1px solid #3898ec `color.measured.field-focus` |

![Country select default](components/crops/country-select-default.png) ![Country select focused](components/crops/country-select-focused.png)

#### Billing toggle
The Yearly/Quarterly save switch (label.w-checkbox over #cycleCheckbox); a local UI toggle measured at rest — clicking it re-prices client-side, captured in screenshots only. Read as `billing-toggle` on the pricing page.

**Values (default).** size 236 x 48; padding 0px 0px 0px 20px; background transparent; text Inter 14/16.8 500, #ffffff `color.neutral.white`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1; div.ms-switch-select.yearly 114.0x40.0 rgb(24, 22, 26) 999px; div.save-pill-div 43.6x20.8 rgb(198, 240, 220) 30px; div.ms-switch-bg 236.0x48.0 rgb(255, 255, 255) T:1px solid rgb(217, 217, 224) / R:1px solid rgb(217, 217, 224) / B:1px solid rgb(217, 217, 224) / L:1px solid rgb(217, 217, 224) 999px.

Child layers that carry the look: div 114x40 background #18161a `color.ink.100` radius 999px; div 43.6x20.8 background #c6f0dc `color.measured.save-pill` radius 30px; div 236x48 background #ffffff `color.neutral.white` border 1px solid #d9d9e0 `color.measured.field-border` radius 999px.

![Billing toggle default](components/crops/billing-toggle-default.png)

#### Calculator field
The estimate inputs of the pricing form — they all sit in .pp-hidden-fields (display:none) behind the country select, so nothing paints; recorded missing. Read as `calc-field` on the pricing page.

Not on the page when it was captured.

#### Plan card
The Growth plan card (.pricing-cards.pop, the featured tier). Read as `plan-card` on the pricing page.

**Values (default).** size 312 x 741.2; border 1px solid rgba(126, 120, 255, 0.25) `color.plum.25`; radius 0px 0px 20px 20px; background #ffffff `color.neutral.white`; text Inter 20/24 500, #18161a `color.ink.100`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan price
A plan card's price figure (S$1,128 annually for the detected region). Read as `plan-price` on the pricing page.

**Values (default).** size 262 x 40; background transparent; text Inter 40/40 400, #18161a `color.ink.100`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan badge
The "Most popular" pill on the featured plan card. Read as `plan-badge` on the pricing page.

**Values (default).** size 80.91 x 13; background transparent; text Inter 13/13 500, #4823ff `color.plum.bright`.

![Plan badge default](components/crops/plan-badge-default.png)

#### Plan CTA
A plan Start-free action; links to the app signup, measured never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 270 x 49; padding 13px 20px; border 1px solid #4823ff `color.plum.bright`; radius 100px; background #4823ff `color.plum.bright`; text Inter 15/21 400, #ffffff `color.neutral.white`; transition all 0.2s ease |
| hover | border 1px solid #2b1599 `color.plum.dark`; background #2b1599 `color.plum.dark` |
| focus-visible | outline 1px auto #005fcc `color.measured.focus`, offset 1px |
| pressed | border 1px solid #2b1599 `color.plum.dark`; background #2b1599 `color.plum.dark` |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

### Blog and demo

The /features/cap-table head, the Cake-blog collection cards, and the /demo-request page with its HubSpot embed — measured as a region, never filled.

#### Feature headline
The /features/cap-table display heading; one of ~25 sibling feature pages on the same template. Read as `feature-h1` on the feature page.

**Values (default).** size 478.39 x 132; background transparent; text Exposure Light 60/66 400, #18161a `color.ink.100`.

![Feature headline default](components/crops/feature-h1-default.png)

#### Blog title
The "Cake blog" heading. Read as `blog-h1` on the blog page.

**Values (default).** size 265.36 x 66; background transparent; text Exposure Light 60/66 400, #18161a `color.ink.100`.

![Blog title default](components/crops/blog-h1-default.png)

#### Article card
A blog collection card (the featured post). Read as `collection-card` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 693.36 x 695.92; background transparent; text Exposure Light 44/44 300, #18161a `color.ink.100`; layers a.resource-cta-text.link-right-chev 94.0x29.2 rgba(255, 255, 255, 0) |
| focus-visible | layers a.card-link-overlay.w-inline-block 693.4x695.9 1px auto rgb(0, 95, 204) offset 1px; a.resource-cta-text.link-right-chev 94.0x29.2 rgba(255, 255, 255, 0) |

Child layers that carry the look: a 94x29.2 background rgba(255, 255, 255, 0).

![Article card default](components/crops/collection-card-default.png) ![Article card hover](components/crops/collection-card-hover.png) ![Article card focus-visible](components/crops/collection-card-focus-visible.png) ![Article card pressed](components/crops/collection-card-pressed.png)

#### Demo title
The /demo-request heading. Read as `demo-h1` on the demo page.

**Values (default).** size 536.77 x 198; background transparent; text Exposure Light 60/66 400, #18161a `color.ink.100`.

![Demo title default](components/crops/demo-h1-default.png)

#### Demo form embed
The HubSpot form region (a cross-origin hsforms.net iframe; its inner fields are third-party paint, documented as a boundary). Read as `demo-form` on the demo page.

**Values (default).** size 599.59 x 1122.13; padding 20px; radius 20px; background #ffffff `color.neutral.white`; text Inter 15.4/21.56 300, #18161a `color.ink.100`.

![Demo form embed default](components/crops/demo-form-default.png)

### Login (Kinde hosted auth)

The hosted-auth card app.cakeequity.com redirects to: email, Continue and the Google/LinkedIn OAuth buttons — Kinde's own violet scale, not the marketing plum.

#### Login card
The Kinde hosted-auth card (Welcome back): email field, Continue, Google and LinkedIn OAuth. Read as `login-card` on the login page.

**Values (default).** size 496 x 608.53; padding 48px; radius 16px; background #ffffff `color.neutral.white`; text Inter 24/31.99 500, #0f0f0f `color.auth.text`; icon 24 x 24, #0f0f0f `color.auth.text`.

![Login card default](components/crops/login-card-default.png)

#### Login title
The "Welcome back" auth heading. Read as `login-title` on the login page.

**Values (default).** size 400 x 31.98; background transparent; text Inter 24/31.99 500, #0f0f0f `color.auth.text`.

![Login title default](components/crops/login-title-default.png)

#### Email field
The auth email input; tapped into focus, never typed into or submitted. Read as `login-field` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 48; padding 12px; border 1px solid #ababab `color.auth.field-border`; radius 8px; background transparent; text Inter 16/24 400, #2b2b2b `color.auth.muted`; transition outline-offset 0.15s cubic-bezier(0.25, 0, 0.1, 1), border-color 0.15s cubic-bezier(0.25, 0, 0.1, 1); placeholder #2b2b2b `color.auth.muted` |
| focused | outline 2px solid #0054f0 `color.auth.focus`, offset 2px |

![Email field default](components/crops/login-field-default.png) ![Email field focused](components/crops/login-field-focused.png)

#### Continue button
The primary Continue action (a submit button — measured, never pressed for real). Read as `login-cta` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 400 x 48; padding 0px 16px; border 1px solid transparent; radius 8px; background #5a38fd `color.auth.primary`; text Inter 16/24 500, #ffffff `color.neutral.white`; transition outline-offset 0.15s cubic-bezier(0.25, 0, 0.1, 1), background-color 0.15s cubic-bezier(0.25, 0, 1, 1) |
| focus-visible | outline 2px solid #0054f0 `color.auth.focus`, offset 2px |

![Continue button default](components/crops/login-cta-default.png) ![Continue button hover](components/crops/login-cta-hover.png) ![Continue button focus-visible](components/crops/login-cta-focus-visible.png) ![Continue button pressed](components/crops/login-cta-pressed.png)

#### OAuth button
A secondary Continue-with provider button (Google/LinkedIn). Read as `login-oauth` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 48; padding 0px 16px; border 1px solid transparent; radius 8px; background #f5f5f5 `color.auth.oauth`; text Inter 16/24 500, #0f0f0f `color.auth.text`; transition outline-offset 0.15s cubic-bezier(0.25, 0, 0.1, 1), background-color 0.15s cubic-bezier(0.25, 0, 1, 1); icon 24 x 24, #0f0f0f `color.auth.text` |
| hover | background #ebebeb `color.auth.oauth-hover` |
| focus-visible | outline 2px solid #0054f0 `color.auth.focus`, offset 2px |
| pressed | background #dbdbdb `color.auth.oauth-pressed` |

![OAuth button default](components/crops/login-oauth-default.png) ![OAuth button hover](components/crops/login-oauth-hover.png) ![OAuth button focus-visible](components/crops/login-oauth-focus-visible.png) ![OAuth button pressed](components/crops/login-oauth-pressed.png)

#### Create-one link
The "Create one" signup link under the OAuth buttons. Read as `login-link` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 83.11 x 20; background transparent; text Inter 16/24 500, #1c029d `color.auth.link`; transition outline-offset 0.15s cubic-bezier(0.25, 0, 0.1, 1), color 0.15s cubic-bezier(0.9, 0, 0.1, 1) |
| focus-visible | radius 2px; outline 2px solid #0054f0 `color.auth.focus`, offset 2px; layers a.kinde-text-link.kinde-text-link-is-inline 83.1x20.0 2px solid rgb(0, 84, 240) offset 2px 2px |

![Create-one link default](components/crops/login-link-default.png) ![Create-one link hover](components/crops/login-link-hover.png) ![Create-one link focus-visible](components/crops/login-link-focus-visible.png) ![Create-one link pressed](components/crops/login-link-pressed.png)

### Footer

The #18161a footer: office lines, link columns, socials and legal — white text, plum hover.

#### Footer
The footer-section: office address, link columns, socials, legal. Read as `footer` on the home page.

**Values (default).** size 1440 x 659.08; background #18161a `color.ink.100`; text Inter 15.4/21.56 300, #ffffff `color.neutral.white`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85.48 x 20; background transparent; text Inter 16/16 300, #ffffff `color.neutral.white`; transition all 0.2s ease |
| hover | text Inter 16/16 300, #7e78ff `color.plum.100` |
| focus-visible | outline 1px auto #005fcc `color.measured.focus`, offset 1px; layers a.footer-link-16px 85.5x20.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text Inter 16/16 300, #7e78ff `color.plum.100` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A social link in the footer. Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 25 x 25; background transparent; text Inter 14/16.8 400, #0000ee; transition all 0.2s ease |
| hover | text Inter 14/16.8 400, #4823ff `color.plum.bright`; transform translate(0px, -5px) |
| focus-visible | outline 1px auto #005fcc `color.measured.focus`, offset 1px; layers a.social-profile-wrapper.w-inline-block 25.0x25.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text Inter 14/16.8 400, #4823ff `color.plum.bright`; transform translate(0px, -5px) |

![Social link default](components/crops/social-icon-default.png) ![Social link hover](components/crops/social-icon-hover.png) ![Social link focus-visible](components/crops/social-icon-focus-visible.png) ![Social link pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The home page at phone width: the page forces a ~745px layout viewport (.comparison-grid min-width:700px), so the hamburger sits outside the 390 visual viewport and the page pans — what a phone actually paints.

#### Mobile header
The navbar at 390 — the page forces a ~745px layout viewport (a .comparison-grid min-width:700px plus navbar chrome), so the hamburger sits outside the 390 visual viewport: the shots record what a phone actually paints. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 745 x 68; background transparent; shadow rgba(0, 0, 0, 0.2) 0px 2px 20px -19px; text Inter 14/16.8 400, #333333; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1; div.navbar.w-nav 745.0x68.0 rgba(0, 0, 0, 0.2) 0px 2px 20px -19px; div.navbar-bg-shadow 745.0x0.0 rgba(0, 0, 0, 0.1) 0px 1px 30px 0px; nav.navbar-menu.w-nav-menu 0.0x0.0 rgb(255, 255, 255); div.nav-menu_link-wrap.w-dropdown-toggle 0.0x0.0 B:1px solid rgb(207, 219, 222); div.absolute-border 0.0x0.0 rgb(126, 120, 255); div.na.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The hamburger (menu-button w-nav-button); painted at x~660 of the forced 745 layout, off the 390 visual viewport. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 48 x 48; padding 8px; radius 4px; background transparent; text Inter 24/16.8 400, #333333.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 351 x 228.81; background transparent; text Exposure Light 52/57.2 400, #18161a `color.ink.100`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the cake. wordmark, the arrow chevrons, the +/- accordion glyph, social glyphs, and the product-UI artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The Cake equity-management app itself lives behind app.cakeequity.com — the cap table, option grants, scenario models, documents, stakeholders, reports and settings all need an account and were never reached. app.cakeequity.com/login redirects to a Kinde-hosted auth page (authentication.cakeequity.com); the card was captured as a form and never filled or submitted. Nothing here describes what sits behind it.

### Pages

- **The app.** Every post-login surface was never reached; the login card was measured as a form, never used.
- **Signup and checkout.** Every Get-started-free, Start-free and Book-a-demo action was measured, never followed. The demo form itself is a HubSpot cross-origin iframe — captured as a region, never filled.
- **The ~25 sibling feature pages.** Only /features/cap-table was measured; the other feature, stage, comparison, stories, guides, tools and template pages share the template but were not read individually.
- **Article pages.** The blog index was captured; no post was opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **calc-field** is recorded missing: the pricing calculator's estimate inputs sit in .pp-hidden-fields (display:none) behind the region select — nothing paints signed out, so it is honestly a miss, not an absent field.
- **The Kinde Continue button** does not change its fill on hover in the captured reading (the hover state measured identical); only its focus ring differs.

### Themes

The site is light-only — no stylesheet binds a dark theme — but two dark surfaces are painted on the page: the #18161a footer and the #0e0d12 Cake-MCP band. tokens.json keeps their roles in the dark set.

### Fonts

- **Exposure Light** (display headlines), **Inter** (everything else on the marketing pages) and the **Kinde Inter/system stack** (the auth card) are the painted faces. Exposure Bold, Youth, Cabinetgrotesk, Inconsolata and Plus Jakarta Sans are served @font-faces nothing measured painted — recorded as declared, not observed.

### Screenshots

- The product-UI artwork inside heroes and cards, customer logos and story portraits are the product's published content.
- The mobile page forces a ~745px layout viewport (.comparison-grid{min-width:700px}): at 390 visual width the hamburger sits at x~660 and the page pans horizontally. The mobile shots record what a phone actually paints, not a re-render at 390.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Blog posts, stories, guides, template copy and the HubSpot form's inner fields are the product's content; only frames and components were measured.
