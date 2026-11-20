# Equals components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from equals.com, go.equals.com and docs.equals.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the sign-in and demo e-mail fields were focused and filled for measurement, then cleared, and never sent; the Get-a-demo and plan actions were never followed. The spreadsheet workspace behind login was never reached — the 'workbook' entries below are the marketing page's own demo mockup.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (60 components, 140 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (136 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`: marketing and sign-in surfaces paint `light`; the docs' dark-mode pages are the `*-dark-dark-*` files. Desktop shots are 1440 x 900 at DPR 2 (256-colour PNGs); `-full` shots are whole pages, chunked and stitched; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home (marketing) | `equals.com/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Pricing | `equals.com/pricing/` | [default](screenshots/pricing-light-default.png), [faq-open](screenshots/pricing-light-faq-open.png), [full](screenshots/pricing-light-full.png) |
| About | `equals.com/about/` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Customers | `equals.com/customers/` | [default](screenshots/customers-light-default.png), [full](screenshots/customers-light-full.png) |
| Launches | `equals.com/launches/` | [default](screenshots/launches-light-default.png), [full](screenshots/launches-light-full.png) |
| Use cases index | `equals.com/use-cases/` | [default](screenshots/usecases-light-default.png), [full](screenshots/usecases-light-full.png) |
| ARR dashboard use-case | `equals.com/use-cases/arr-dashboard/` | [default](screenshots/usecase-light-default.png), [full](screenshots/usecase-light-full.png) |
| ARR guide | `equals.com/guides/arr/` | [default](screenshots/guide-light-default.png), [full](screenshots/guide-light-full.png), [splash](screenshots/guide-light-splash.png) |
| Sign in | `go.equals.com/` | [default](screenshots/signin-light-default.png) |
| Docs (light) | `docs.equals.com/docs/getting-started` | [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png) |
| Docs: charts | `docs.equals.com/docs/charts` | [default](screenshots/docs-charts-light-default.png), [full](screenshots/docs-charts-light-full.png) |
| Docs: spreadsheet (light) | `docs.equals.com/docs/how-to-spreadsheet` | [default](screenshots/docs-spreadsheet-light-default.png), [full](screenshots/docs-spreadsheet-light-full.png) |
| Docs: spreadsheet (dark) | `docs.equals.com/docs/how-to-spreadsheet, dark` | [default](screenshots/docs-spreadsheet-dark-dark-default.png), [full](screenshots/docs-spreadsheet-dark-dark-full.png) |
| Docs (dark) | `docs.equals.com/docs/getting-started, dark` | [default](screenshots/docs-dark-dark-default.png), [full](screenshots/docs-dark-dark-full.png) |
| Home, phone | `equals.com/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `equals.com/pricing/` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Use-case, phone | `equals.com/use-cases/arr-dashboard/` | [default](screenshots/mobile-usecase-light-default.png), [full](screenshots/mobile-usecase-light-full.png) |
| Sign-in, phone | `go.equals.com/` | [default](screenshots/mobile-signin-light-default.png) |
| Docs dark, phone | `docs.equals.com/, dark` | [default](screenshots/mobile-docs-dark-dark-default.png), [full](screenshots/mobile-docs-dark-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Use-cases mega-menu | equals.com header | the menu trigger's own toggle | [home-light-menu](screenshots/home-light-menu.png), [mkt-menu](#use-cases-mega-menu), [mkt-menu-item](#mega-menu-link) |
| Pricing FAQ accordion | /pricing/ | the question row's own toggle | [pricing-light-faq-open](screenshots/pricing-light-faq-open.png), [faq](#faq-item) |
| Guide splash gate | /guides/arr/ | the 'Start reading' button's own toggle | [guide-light-splash](screenshots/guide-light-splash.png) |
| Mobile nav drawer | home, phone width | the hamburger's own toggle | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-drawer](#mobile-nav-drawer) |
| E-mail fields | home, use-case, sign-in and phone | focused and filled with a test address, then cleared — never submitted | [hero-email](#demo-email-field), [signin-email](#sign-in-email-field), [m-email](#demo-email-field-mobile) |
| Docs theme | docs.equals.com | html.dark applied by the capture context, not a menu click | the `d-docs-*` entries and `docs-dark`/`docs-spreadsheet-dark` shots |
| Signed-in product | app.equals.com / post-login | every post-login surface needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 19 components were given a real keyboard focus. 16 draw an outline ring: `mkt-nav-link` (1px auto #101010, offset 1px), `mkt-menu-trigger` (1px auto #101010, offset 0px), `mkt-menu-item` (1px auto #101010, offset 1px), `mkt-signin` (1px auto #101010, offset 1px), `build-tab` (1px auto #101010, offset 0px), `signin-continue` (1px auto #101010, offset 0px), `docs-search` (1px auto #7839e5 `color.app.primary`, offset 0px), `docs-theme-btn` (1px auto #7839e5 `color.app.primary`, offset 0px), `docs-nav-item` (1px auto #7839e5 `color.app.primary`, offset -2px), `docs-assistant` (1px auto #7839e5 `color.app.primary`, offset 0px), `docs-link` (1px auto #7839e5 `color.app.primary`, offset -2px), `d-docs-search` (1px auto #7839e5 `color.app.primary`, offset 0px), `d-docs-theme-btn` (1px auto #7839e5 `color.app.primary`, offset 0px), `d-docs-nav-item` (1px auto #7839e5 `color.app.primary`, offset -2px), `d-docs-assistant` (1px auto #7839e5 `color.app.primary`, offset 0px), `d-docs-link` (1px auto #7839e5 `color.app.primary`, offset -2px). The other 3 show no measured change: `hero-cta`, `plan-cta`, `plan-cta-orchid`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.4, 0, 0.2, 1)` | rotate, scale, transform, translate | d-docs-sidebar, docs-sidebar |
| 0.1s | `ease-out` | text-decoration | mkt-menu-trigger, mkt-nav-link, mkt-signin |
| 0.15s | `ease-out` | background-color | hero-cta, signin-continue |
| 0.16s | `cubic-bezier(0.16, 1, 0.3, 1)` | opacity, transform | mkt-menu |
| 0.2s | `ease-out` | opacity | build-tab |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 421.33 x 568.8 | - | - | #faf9f5 `color.brand.grey-1` | none | 32px |
| [Use-cases mega-menu](#use-cases-mega-menu) | 633.76 x 360.31 | - | 12px | #ffffff `color.brand.white` | rgba(0, 0, 0, 0.1) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.05) 0px 2px 8px -2px, rgba(0, 0, 0, 0.15) 0px 8px 24px -4px | 14px 10px |
| [Sign-in card](#sign-in-card) | 300 x 226 | - | - | transparent | none | 0 |
| [Workbook mockup](#workbook-mockup) | 980 x 640 | - | 12px | #fcfcfc `color.app.background` | rgba(38, 38, 38, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.2) 0px 2px 8px -4px | 0 |
| [Mobile nav drawer](#mobile-nav-drawer) | 390 x 52 | - | - | transparent | none | 0px 16px |
| [Docs sidebar](#docs-sidebar) | 288 x 804 | R: 1px solid #f1eff5 `color.docs.gray.100` | - | transparent | none | 0 |

## Components

### Marketing chrome

The equals.com header: the 52px cream bar with the Equals wordmark, nav links, the Use-cases mega-menu trigger and the Sign-in link.

#### Marketing header
The top bar: wordmark, Home / Use cases / Pricing / About, "Get a demo" capture and the "Sign in" link. Read as `mkt-header` on the marketing home page.

**Values (default).** size 1440 x 52; background #faf9f5 `color.brand.grey-1`; text Unica77 14/20 400, #000000 `color.brand.black`; icon 108 x 22, #0000ee.

![Marketing header default](components/crops/mkt-header-default.png)

#### Logo
The Equals wordmark at the left of the header. Read as `mkt-logo` on the marketing home page.

**Values (default).** size 108 x 21; background transparent; text Unica77 18/24 400, #0000ee; icon 108 x 22, #0000ee.

![Logo default](components/crops/mkt-logo-default.png)

#### Nav link
A marketing header link (Pricing/About); measured, never followed. Read as `mkt-nav-link` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 42.38 x 16; background transparent; text Unica77 14/20 400, #000000 `color.brand.black`; transition text-decoration 0.1s ease-out |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.header__nav-link 42.4x16.0 1px auto rgb(16, 16, 16) offset 1px |

![Nav link default](components/crops/mkt-nav-link-default.png) ![Nav link hover](components/crops/mkt-nav-link-hover.png) ![Nav link focus-visible](components/crops/mkt-nav-link-focus-visible.png) ![Nav link pressed](components/crops/mkt-nav-link-pressed.png)

#### Use-cases menu trigger
The header "Use cases" button; opened to reveal the mega-menu of use-case links (a local toggle, its links never followed). Read as `mkt-menu-trigger` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 65 x 20; background transparent; text Unica77 14/20 400, #000000 `color.brand.black`; transition text-decoration 0.1s ease-out |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.header__menu-trigger 65.0x20.0 1px auto rgb(16, 16, 16) offset 0px |

![Use-cases menu trigger default](components/crops/mkt-menu-trigger-default.png) ![Use-cases menu trigger hover](components/crops/mkt-menu-trigger-hover.png) ![Use-cases menu trigger focus-visible](components/crops/mkt-menu-trigger-focus-visible.png) ![Use-cases menu trigger pressed](components/crops/mkt-menu-trigger-pressed.png) ![Use-cases menu trigger opened](components/crops/mkt-menu-trigger-opened.png)

#### Use-cases mega-menu
The dropdown the "Use cases" trigger opens: category labels and use-case links. Read as `mkt-menu` on the marketing home page.

**Values (default).** size 633.76 x 360.31; padding 14px 10px; radius 12px; background #ffffff `color.brand.white`; shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.05) 0px 2px 8px -2px, rgba(0, 0, 0, 0.15) 0px 8px 24px -4px; text Unica77 14/20 400, rgba(0, 0, 0, 0.6) `color.brand.grey-5`; transition opacity 0.16s cubic-bezier(0.16, 1, 0.3, 1), transform 0.16s cubic-bezier(0.16, 1, 0.3, 1); transform matrix(0.995323, 0, 0, 0.995323, 0, -0.935443); opacity 0.766139.

![Use-cases mega-menu default](components/crops/mkt-menu-default.png)

#### Mega-menu link
One use-case link inside the open mega-menu; measured, never followed. Read as `mkt-menu-item` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 204.62 x 27.87; padding 4px 12px; radius 6px; background transparent; text Unica77 14/20 400, #000000 `color.brand.black` |
| hover | size 205.58 x 28; background rgba(0, 0, 0, 0.05) `color.brand.grey-2` |
| focus-visible, pressed | size 205.58 x 28; background rgba(0, 0, 0, 0.05) `color.brand.grey-2`; outline 1px auto #101010, offset 1px |

![Mega-menu link default](components/crops/mkt-menu-item-default.png) ![Mega-menu link hover](components/crops/mkt-menu-item-hover.png) ![Mega-menu link focus-visible](components/crops/mkt-menu-item-focus-visible.png) ![Mega-menu link pressed](components/crops/mkt-menu-item-pressed.png)

#### Sign-in link
The header "Sign in" link to go.equals.com; measured, never followed. Read as `mkt-signin` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 41.38 x 20; background transparent; text Unica77 14/20 400, #000000 `color.brand.black`; transition text-decoration 0.1s ease-out |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.header__nav-link 41.4x20.0 1px auto rgb(16, 16, 16) offset 1px |

![Sign-in link default](components/crops/mkt-signin-default.png) ![Sign-in link hover](components/crops/mkt-signin-hover.png) ![Sign-in link focus-visible](components/crops/mkt-signin-focus-visible.png) ![Sign-in link pressed](components/crops/mkt-signin-pressed.png)

### Home hero and sections

The 'What's after Excel?' hero and the sections below it: the Serrif Condensed display, the demo email capture with its orchid CTA, the amber eyebrow labels, the persona tabs, and the use-case page's own hero.

#### Hero headline
"What’s after Excel?" — the Serrif Condensed display on the hero. Read as `hero-h1` on the marketing home page.

**Values (default).** size 1050 x 110; background transparent; text Serrif Condensed 110/110 400, #000000 `color.brand.black`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero sub
The lede under the headline. Read as `hero-sub` on the marketing home page.

**Values (default).** size 618 x 64; background transparent; text Unica77 24/32 400, #000000 `color.brand.black`.

![Hero sub default](components/crops/hero-sub-default.png)

#### Demo email field
The "Enter your work email" capture under the hero copy; focused and typed into then cleared — never submitted. Read as `hero-email` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 380 x 56; padding 18px 150px 18px 28px; background transparent; text Unica77 16/20 400, #000000 `color.brand.black`; placeholder rgba(0, 0, 0, 0.6) `color.brand.grey-5` |

![Demo email field default](components/crops/hero-email-default.png) ![Demo email field focused](components/crops/hero-email-focused.png) ![Demo email field filled](components/crops/hero-email-filled.png)

#### Get-a-demo button
The black "Get a demo" pill on the email capture; measured never pressed (it submits the capture). Read as `hero-cta` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 118 x 44; padding 12px 18px; radius 60px; background #b074ce `color.brand.orchid`; image linear-gradient(transparent 75%, rgba(0, 0, 0, 0.04) 100%); text Unica77 16/20 400, #ffffff `color.brand.white`; transition background-color 0.15s ease-out; transform translate(0px, -22px) |
| hover | background #9b66b5 |
| pressed | background #9b66b5; shadow rgba(0, 0, 0, 0.17) 0px 1px 3px 0px inset |

![Get-a-demo button default](components/crops/hero-cta-default.png) ![Get-a-demo button hover](components/crops/hero-cta-hover.png) ![Get-a-demo button focus-visible](components/crops/hero-cta-focus-visible.png) ![Get-a-demo button pressed](components/crops/hero-cta-pressed.png)

#### Section label
The numbered eyebrow label over a marketing section ("1. TRUST"), coloured by the page’s label-- theme. Read as `section-label` on the marketing home page.

**Values (default).** size 1266 x 24; background transparent; text Aeonik Fono 14/24 400, #ff3716 `color.brand.amber`.

![Section label default](components/crops/section-label-default.png)

#### Section heading
A marketing section heading ("A single source of truth…"). Read as `section-h2` on the marketing home page.

**Values (default).** size 1266 x 100; background transparent; text Serrif Condensed 48/50 400, #000000 `color.brand.black`.

![Section heading default](components/crops/section-h2-default.png)

#### Persona tab
A "Build …" persona tab in the AI-demo section (the active one carries build-tab--active); measured, never pressed. Read as `build-tab` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 402 x 129; padding 16px 0px 32px 0px; border B: 1px solid rgba(0, 0, 0, 0.1); background transparent; text Unica77 14/16 400, rgba(0, 0, 0, 0.6) `color.brand.grey-5`; transition opacity 0.2s ease-out; opacity 0.55; layers button.build-tab 402.0x129.0 B:1px solid rgba(0, 0, 0, 0.1); span.build-tab__progress 0.0x1.0 rgb(0, 0, 0) |
| hover | opacity 0.85 |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.build-tab 402.0x129.0 B:1px solid rgba(0, 0, 0, 0.1) 1px auto rgb(16, 16, 16) offset 0px; span.build-tab__progress 0.0x1.0 rgb(0, 0, 0) |
| pressed | opacity 0.85 |

Child layers that carry the look: button 402x129 border 1px solid rgba(0, 0, 0, 0.1); span 0x1 background #000000 `color.brand.black`.

![Persona tab default](components/crops/build-tab-default.png) ![Persona tab hover](components/crops/build-tab-hover.png) ![Persona tab focus-visible](components/crops/build-tab-focus-visible.png) ![Persona tab pressed](components/crops/build-tab-pressed.png)

#### Use-case headline
"ARR Dashboard" — the use-case page’s display heading. Read as `uc-h1` on the use-cases page.

**Values (default).** size 1266 x 110; background transparent; text Serrif Condensed 110/110 400, #000000 `color.brand.black`.

![Use-case headline default](components/crops/uc-h1-default.png)

#### Use-case lede
The first paragraph under the use-case hero. Read as `uc-lede` on the use-cases page.

**Values (default).** size 633 x 96; background transparent; text Unica77 24/32 400, #000000 `color.brand.black`.

![Use-case lede default](components/crops/uc-lede-default.png)

#### Demo email field (use-case)
The same email capture on a use-case page; focused and typed into then cleared — never submitted. Read as `uc-email` on the use-cases page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 380 x 56; padding 18px 150px 18px 28px; background transparent; text Unica77 16/20 400, #000000 `color.brand.black`; placeholder rgba(0, 0, 0, 0.6) `color.brand.grey-5` |

![Demo email field (use-case) default](components/crops/uc-email-default.png) ![Demo email field (use-case) focused](components/crops/uc-email-focused.png) ![Demo email field (use-case) filled](components/crops/uc-email-filled.png)

### Workbook mockup

The animated workbook demo embedded in the marketing page — a marketing mockup of the spreadsheet, not the authenticated app: its toolbar buttons, sheet tabs and a painted cell.

#### Workbook mockup
The in-page spreadsheet demo: toolbar, formula bar, sheet tabs and cells — a public demo, not the app. Read as `wb-mockup` on the marketing home page.

**Values (default).** size 980 x 640; radius 12px; background #fcfcfc `color.app.background`; shadow rgba(38, 38, 38, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.2) 0px 2px 8px -4px; text Unica77 12/24 400, #575757; icon 12 x 12, #8d8d8d.

![Workbook mockup default](components/crops/wb-mockup-default.png)

#### Mock toolbar button
A toolbar icon button inside the workbook mockup; measured, never pressed. Read as `wb-toolbar-button` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 24; radius 4px; background transparent; text Unica77 18/24 400, #262626 `color.app.grey.800`; icon 16 x 16, #262626 `color.app.grey.800` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Mock toolbar button default](components/crops/wb-toolbar-button-default.png) ![Mock toolbar button hover](components/crops/wb-toolbar-button-hover.png) ![Mock toolbar button pressed](components/crops/wb-toolbar-button-pressed.png)

#### Sheet tab
A workbook sheet tab inside the mockup; measured, never pressed. Read as `wb-sheet-tab` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 92.63 x 32; padding 0px 8px; border T: 1px solid #d4d4d4 `color.app.grey.300`; L: 1px solid #d4d4d4 `color.app.grey.300`; background #fafafa `color.app.grey.50`; text Unica77 11/14 400, #737373 `color.app.grey.500`; icon 11 x 11, #737373 `color.app.grey.500` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Sheet tab default](components/crops/wb-sheet-tab-default.png) ![Sheet tab hover](components/crops/wb-sheet-tab-hover.png) ![Sheet tab pressed](components/crops/wb-sheet-tab-pressed.png)

#### Workbook cell
A label cell in the workbook mockup ("Build Summary"); the mockup cycles demo slides, so the reading is whichever cell is painted — its value cells animate as the demo types. Read as `wb-cell` on the marketing home page.

**Values (default).** size 131 x 21; padding 0px 4px; border R: 1px solid #ededed `color.app.grey.150`; B: 1px solid #ededed `color.app.grey.150`; background #ffffff `color.brand.white`; text Unica77 12/20 500, #262626 `color.app.grey.800`.

![Workbook cell default](components/crops/wb-cell-default.png)

### Pricing

The /pricing page: the plan cards, price, per-plan CTAs and the FAQ accordion.

#### Plan card
An Essential pricing card: plan name, price, "Get a demo" CTA and feature list on the cream page. Read as `plan-card` on the pricing page.

**Values (default).** size 421.33 x 568.8; padding 32px; background #faf9f5 `color.brand.grey-1`; text Unica77 18/22 400, #ff3716 `color.brand.amber`; icon 16 x 16, #000000 `color.brand.black`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan name
The "Essential" plan label. Read as `plan-name` on the pricing page.

**Values (default).** size 357.33 x 22; background transparent; text Unica77 18/22 400, #ff3716 `color.brand.amber`.

![Plan name default](components/crops/plan-name-default.png)

#### Plan price
The "$24k /year" price line — the suffix is a smaller muted span. Read as `plan-price` on the pricing page.

**Values (default).** size 357.33 x 52.8; background transparent; text Serrif Condensed 48/52.8 400, #000000 `color.brand.black`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
The card’s "Get a demo" action on its accent--amber background; measured never pressed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 357.33 x 42; background transparent; text Unica77 14/18 400, #ffffff `color.brand.white`; layers form.email-capture-group.get-a-demo 357.3x42.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.15) 0px 0px 0px 0.5px 50px; button.email-capture-group__button.button 97.0x30.0 rgb(255, 55, 22) 60px |
| hover | layers form.email-capture-group.get-a-demo 357.3x42.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.18) 0px 0px 0px 0.5px 50px; button.email-capture-group__button.button 97.0x30.0 rgb(255, 55, 22) 60px |
| focus-visible | layers form.email-capture-group.get-a-demo 357.3x42.0 rgb(255, 255, 255) rgb(255, 55, 22) 0px 0px 0px 1px, color(srgb 1 0.215686 0.0862745 / 0.1) 0px 0px 0px 3px 50px; button.email-capture-group__button.button 97.0x30.0 rgb(255, 55, 22) 60px |

Child layers that carry the look: form 357.3x42 background #ffffff `color.brand.white` radius 50px shadow rgba(0, 0, 0, 0.15) `color.brand.grey-4` 0px 0px 0px 0.5px; button 97x30 background #ff3716 `color.brand.amber` image linear-gradient(transparent 75%, rgba(0, 0, 0, 0.04) 100%) radius 60px.

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan CTA (orchid)
The Business card’s CTA on the accent--orchid background; each plan carries its own accent colour. Read as `plan-cta-orchid` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 356.33 x 42; background transparent; text Unica77 14/18 400, #ffffff `color.brand.white`; layers form.email-capture-group.get-a-demo 356.3x42.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.15) 0px 0px 0px 0.5px 50px; button.email-capture-group__button.button 97.0x30.0 rgb(176, 116, 206) 60px |
| hover | layers form.email-capture-group.get-a-demo 356.3x42.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.18) 0px 0px 0px 0.5px 50px; button.email-capture-group__button.button 97.0x30.0 rgb(176, 116, 206) 60px |
| focus-visible | layers form.email-capture-group.get-a-demo 356.3x42.0 rgb(255, 255, 255) rgb(176, 116, 206) 0px 0px 0px 1px, color(srgb 0.690196 0.454902 0.807843 / 0.1) 0px 0px 0px 3px 50px; button.email-capture-group__button.button 97.0x30.0 rgb(176, 116, 206) 60px |

Child layers that carry the look: form 356.3x42 background #ffffff `color.brand.white` radius 50px shadow rgba(0, 0, 0, 0.15) `color.brand.grey-4` 0px 0px 0px 0.5px; button 97x30 background #b074ce `color.brand.orchid` image linear-gradient(transparent 75%, rgba(0, 0, 0, 0.04) 100%) radius 60px.

![Plan CTA (orchid) default](components/crops/plan-cta-orchid-default.png) ![Plan CTA (orchid) hover](components/crops/plan-cta-orchid-hover.png) ![Plan CTA (orchid) focus-visible](components/crops/plan-cta-orchid-focus-visible.png) ![Plan CTA (orchid) pressed](components/crops/plan-cta-orchid-pressed.png)

#### Plan feature row
A feature line inside the plan card ("Unlimited seats"). Read as `plan-feature` on the pricing page.

**Values (default).** size 357.33 x 38; padding 8px 0px; background transparent; text Unica77 16/22 400, #000000 `color.brand.black`; icon 16 x 16, #000000 `color.brand.black`.

![Plan feature row default](components/crops/plan-feature-default.png)

#### FAQ item
A pricing FAQ row (a checkbox accordion); opened by clicking its label — a local toggle, never a form post. Read as `faq` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 1266 x 230; border T: 1px solid rgba(0, 0, 0, 0.1); B: 1px solid rgba(0, 0, 0, 0.1); background transparent; text Unica77 24/32 400, #000000 `color.brand.black` |

![FAQ item default](components/crops/faq-default.png) ![FAQ item opened](components/crops/faq-opened.png)

#### FAQ question
The question label of the first FAQ item. Read as `faq-question` on the pricing page.

**Values (default).** size 1266 x 72; padding 24px 0px 16px 0px; background transparent; text Unica77 24/32 400, #000000 `color.brand.black`.

![FAQ question default](components/crops/faq-question-default.png)

### Sign in (go.equals.com)

The signed-out Equals app card on go.equals.com: heading, email field, Continue submit and the footer links — measured, never submitted.

#### Sign-in card
The whole "Sign in to Equals" card — heading, subheading, the email form and the footer line. Read as `signin-card` on the go.equals.com sign-in page.

**Values (default).** size 300 x 226; background transparent; text Serrif Condensed 30/39 400, #000000 `color.brand.black`; transform translate(0px, -20px); layers input.SignIn__Input 300.0x30.0 rgb(245, 245, 245) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 8px; input.SignIn__Button 300.0x27.0 rgb(124, 58, 237) 8px.

Child layers that carry the look: input 300x30 background #f5f5f5 `color.app.grey.100` border 1px solid transparent radius 8px; input 300x27 background #7c3aed `color.app.purple.600` radius 8px.

![Sign-in card default](components/crops/signin-card-default.png)

#### Sign-in heading
"Sign in to Equals". Read as `signin-heading` on the go.equals.com sign-in page.

**Values (default).** size 300 x 39; background transparent; text Serrif Condensed 30/39 400, #000000 `color.brand.black`.

![Sign-in heading default](components/crops/signin-heading-default.png)

#### Sign-in subheading
"Enter your email below to login to your account". Read as `signin-sub` on the go.equals.com sign-in page.

**Values (default).** size 300 x 16; background transparent; text neue-haas-unica 12/16 400, #000000 `color.brand.black`.

![Sign-in subheading default](components/crops/signin-sub-default.png)

#### Sign-in email field
The "Enter your email" input; focused and typed into then cleared — never submitted. Read as `signin-email` on the go.equals.com sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 300 x 30; padding 6px 8px; border 1px solid transparent; radius 8px; background #f5f5f5 `color.app.grey.100`; text neue-haas-unica 12/16 400, #262626 `color.app.grey.800`; placeholder #a3a3a3 `color.app.grey.400` |
| focused, filled | border 1px solid #7c3aed `color.app.purple.600` |

![Sign-in email field default](components/crops/signin-email-default.png) ![Sign-in email field focused](components/crops/signin-email-focused.png) ![Sign-in email field filled](components/crops/signin-email-filled.png)

#### Continue button
The form’s "Continue" submit; its states were measured but it was never clicked — nothing was submitted. Read as `signin-continue` on the go.equals.com sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 300 x 27; padding 6px 8px; radius 8px; background #7c3aed `color.app.purple.600`; text neue-haas-unica 12/15 400, #ffffff `color.brand.white`; transition background-color 0.15s ease-out; placeholder #ffffff `color.brand.white` |
| hover | background #6d28d9 `color.app.purple.700` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background #6d28d9 `color.app.purple.700` |

![Continue button default](components/crops/signin-continue-default.png) ![Continue button hover](components/crops/signin-continue-hover.png) ![Continue button focus-visible](components/crops/signin-continue-focus-visible.png) ![Continue button pressed](components/crops/signin-continue-pressed.png)

#### Sign-in footer link
"Don’t have an account? Request a demo" — the footer copy and link; measured, never followed. Read as `signin-footer` on the go.equals.com sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 300 x 16; background transparent; text neue-haas-unica 12/16 400, #737373 `color.app.grey.500` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Sign-in footer link default](components/crops/signin-footer-default.png) ![Sign-in footer link hover](components/crops/signin-footer-hover.png) ![Sign-in footer link pressed](components/crops/signin-footer-pressed.png)

### Docs (docs.equals.com) (light)

The Mintlify docs shell in light mode: the 288px sidebar, search pill, theme button, nav items, assistant pill, page heading, body copy, links and code blocks.

#### Docs sidebar
The docs left rail: logo, search, theme menu and the nav tree. Read as `docs-sidebar` on the docs page.

**Values (default).** size 288 x 804; border R: 1px solid #f1eff5 `color.docs.gray.100`; background transparent; text Inter 12/16 600, #1a181d `color.docs.gray.900`; transition transform 0.1s cubic-bezier(0.4, 0, 0.2, 1), translate 0.1s cubic-bezier(0.4, 0, 0.2, 1), scale 0.1s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 8, #a2a0a5 `color.docs.gray.400`; layers nav.hidden.sticky 288.0x804.0 R:1px solid rgb(241, 239, 245); a.group.flex 267.0x32.0 oklab(0.529224 0.0935356 -0.219964 / 0.1) 12px; div.sidebar-nav-group-divider.h-px 259.0x1.0 rgb(241, 239, 245); div.sidebar-nav-group-divider.h-px 259.0x1.0 rgb(241, 239, 245); div.sidebar-nav-group-divider.h-px 259.0x1.0 rgb(241, 239, 245); div.sidebar-nav-group-divider.h-px 259.0x1.0 rgb(241, 239, 245).

Child layers that carry the look: nav 288x804 border 1px solid #f1eff5 `color.docs.gray.100`; a 267x32 background oklab(0.529224 0.0935356 -0.219964 / 0.1) radius 12px; div 259x1 background #f1eff5 `color.docs.gray.100`.

![Docs sidebar default](components/crops/docs-sidebar-default.png)

#### Docs logo
The Equals wordmark at the top of the docs rail. Read as `docs-logo` on the docs page.

**Values (default).** size 117.89 x 24; background transparent; text Inter 16/24 400, #737176 `color.docs.gray.500`.

![Docs logo default](components/crops/docs-logo-default.png)

#### Search button
The "Search…" field-styled button in the docs rail; measured, never opened. Read as `docs-search` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 264.33 x 36; padding 0px 12px 0px 14px; radius 9999px; background oklab(0.155089 0.0065295 -0.0112347 / 0.03); shadow oklab(0.708939 0.00425118 -0.00619447 / 0.3) 0px 0px 0px 0px; text Inter 14/24 400, #737176 `color.docs.gray.500`; icon 16 x 16, #424045 `color.docs.gray.700` |
| hover | background oklab(0.155089 0.0065295 -0.0112347 / 0.1); shadow oklab(0.438582 0.00476192 -0.00700194 / 0.3) 0px 0px 0px 0px; icon 16 x 16, #29272c `color.docs.gray.800` |
| focus-visible | outline 1px auto #7839e5 `color.app.primary`, offset 0px |
| pressed | background oklab(0.155089 0.0065295 -0.0112347 / 0.1); shadow oklab(0.438582 0.00476192 -0.00700194 / 0.3) 0px 0px 0px 0px; icon 16 x 16, #29272c `color.docs.gray.800` |

![Search button default](components/crops/docs-search-default.png) ![Search button hover](components/crops/docs-search-hover.png) ![Search button focus-visible](components/crops/docs-search-focus-visible.png) ![Search button pressed](components/crops/docs-search-pressed.png)

#### Theme menu button
The docs theme menu button; measured, never opened (the dark capture used a prefers-color-scheme context instead). Read as `docs-theme-btn` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 30 x 30; padding 8px; radius 9999px; background oklab(0.27687 0.00530203 -0.00787868 / 0.04); text Inter 14/20 400, oklab(0.155089 0.0065295 -0.0112347 / 0.5); icon 14 x 16, #535156 `color.docs.gray.600` |
| hover | icon 14 x 16, #29272c `color.docs.gray.800` |
| focus-visible | outline 1px auto #7839e5 `color.app.primary`, offset 0px |
| pressed | icon 14 x 16, #29272c `color.docs.gray.800` |

![Theme menu button default](components/crops/docs-theme-btn-default.png) ![Theme menu button hover](components/crops/docs-theme-btn-hover.png) ![Theme menu button focus-visible](components/crops/docs-theme-btn-focus-visible.png) ![Theme menu button pressed](components/crops/docs-theme-btn-pressed.png)

#### Nav item
A docs sidebar link; measured, never followed. Read as `docs-nav-item` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 267 x 32; padding 6px 12px 6px 28px; radius 12px; background oklab(0.529224 0.0935356 -0.219964 / 0.1); text Inter 14/20 400, #7839e5 `color.app.primary` |
| focus-visible | outline 1px auto #7839e5 `color.app.primary`, offset -2px |

![Nav item default](components/crops/docs-nav-item-default.png) ![Nav item hover](components/crops/docs-nav-item-hover.png) ![Nav item focus-visible](components/crops/docs-nav-item-focus-visible.png) ![Nav item pressed](components/crops/docs-nav-item-pressed.png)

#### Assistant button
The "Ask AI" assistant entry in the docs chrome; measured at rest, never opened — nothing was sent. Read as `docs-assistant` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 171 x 36; padding 0px 14px 0px 12px; radius 9999px; background oklab(0.155089 0.0065295 -0.0112347 / 0.03); shadow oklab(0.708939 0.00425118 -0.00619447 / 0.3) 0px 0px 0px 0px; text Inter 14/20 400, #737176 `color.docs.gray.500`; icon 16 x 16, #424045 `color.docs.gray.700` |
| hover | background oklab(0.155089 0.0065295 -0.0112347 / 0.1); shadow oklab(0.438582 0.00476192 -0.00700194 / 0.3) 0px 0px 0px 0px; icon 16 x 16, #29272c `color.docs.gray.800` |
| focus-visible | outline 1px auto #7839e5 `color.app.primary`, offset 0px |
| pressed | background oklab(0.155089 0.0065295 -0.0112347 / 0.1); shadow oklab(0.438582 0.00476192 -0.00700194 / 0.3) 0px 0px 0px 0px; icon 16 x 16, #29272c `color.docs.gray.800` |

![Assistant button default](components/crops/docs-assistant-default.png) ![Assistant button hover](components/crops/docs-assistant-hover.png) ![Assistant button focus-visible](components/crops/docs-assistant-focus-visible.png) ![Assistant button pressed](components/crops/docs-assistant-pressed.png)

#### Page heading
The doc page’s h1. Read as `docs-h1` on the docs page.

**Values (default).** size 168.89 x 40; background transparent; text Inter 36/40 600, #1a181d `color.docs.gray.900`.

![Page heading default](components/crops/docs-h1-default.png)

#### Body paragraph
A body paragraph in the doc. Read as `docs-para` on the docs page.

**Values (default).** size 632 x 28; background transparent; text Inter 18/28 400, #424045 `color.docs.gray.700`.

![Body paragraph default](components/crops/docs-para-default.png)

#### Body link
A link inside the doc body; measured, never followed. Read as `docs-link` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 264 x 32; padding 4px 0px 4px 16px; border L: 1px solid #7839e5 `color.app.primary`; background transparent; text Inter 14/24 400, #7839e5 `color.app.primary`; layers a.text-primary.dark:text-primary-light 264.0x32.0 L:1px solid rgb(120, 57, 229) |
| focus-visible | size 268 x 32; padding 4px 0px 4px 20px; outline 1px auto #7839e5 `color.app.primary`, offset -2px; layers a.text-primary.dark:text-primary-light 268.0x32.0 L:1px solid rgb(120, 57, 229) 1px auto rgb(120, 57, 229) offset -2px |

Child layers that carry the look: a 264x32 border 1px solid #7839e5 `color.app.primary`.

![Body link default](components/crops/docs-link-default.png) ![Body link hover](components/crops/docs-link-hover.png) ![Body link focus-visible](components/crops/docs-link-focus-visible.png) ![Body link pressed](components/crops/docs-link-pressed.png)

#### Code block
A code block or inline code span in the doc. Read as `docs-code` on the docs page.

**Values (default).** size 128 x 20; padding 2px 8px; radius 6px; background oklab(0.955295 0.00433394 -0.00702435 / 0.5); text Paper Mono 14/21 500, oklch(0.21 0.034 264.665).

![Code block default](components/crops/docs-code-default.png)

### Docs (docs.equals.com) (dark)

The same docs shell under html.dark: dark canvas, grey-400 body copy, white-wash chips and the same purple primary.

#### Docs sidebar
The docs left rail: logo, search, theme menu and the nav tree. Read as `d-docs-sidebar` on the docs dark page.

**Values (default).** size 288 x 804; border R: 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1); background transparent; text Inter 12/16 600, #e2e0e5 `color.docs.gray.200`; transition transform 0.1s cubic-bezier(0.4, 0, 0.2, 1), translate 0.1s cubic-bezier(0.4, 0, 0.2, 1), scale 0.1s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 8, #535156 `color.docs.gray.600`; layers nav.hidden.sticky 288.0x804.0 R:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1); a.group.flex 267.0x32.0 oklab(0.529224 0.0935356 -0.219964 / 0.1) 12px; div.sidebar-nav-group-divider.h-px 259.0x1.0 oklab(0.999994 0.0000455678 0.0000200868 / 0.1); div.sidebar-nav-group-divider.h-px 259.0x1.0 oklab(0.999994 0.0000455678 0.0000200868 / 0.1); div.sidebar-nav-group-divider.h-px 259.0x1.0 okla.

Child layers that carry the look: nav 288x804 border 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1); a 267x32 background oklab(0.529224 0.0935356 -0.219964 / 0.1) radius 12px; div 259x1 background oklab(0.999994 0.0000455678 0.0000200868 / 0.1).

![Docs sidebar default](components/crops/d-docs-sidebar-default.png)

#### Docs logo
The Equals wordmark at the top of the docs rail. Read as `d-docs-logo` on the docs dark page.

**Values (default).** size 117.89 x 24; background transparent; text Inter 16/24 400, #a2a0a5 `color.docs.gray.400`.

![Docs logo default](components/crops/d-docs-logo-default.png)

#### Search button
The "Search…" field-styled button in the docs rail; measured, never opened. Read as `d-docs-search` on the docs dark page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 264.33 x 36; padding 0px 12px 0px 14px; radius 9999px; background oklab(0.999994 0.0000455678 0.0000200868 / 0.03); shadow oklab(0.438582 0.00476192 -0.00700194 / 0.3) 0px 0px 0px 0px; text Inter 14/24 400, oklab(0.999994 0.0000455678 0.0000200868 / 0.5); icon 16 x 16, #a2a0a5 `color.docs.gray.400` |
| hover | background oklab(0.999994 0.0000455678 0.0000200868 / 0.1); shadow oklab(0.552007 0.00451359 -0.00660944 / 0.3) 0px 0px 0px 0px; icon 16 x 16, #e2e0e5 `color.docs.gray.200` |
| focus-visible | outline 1px auto #7839e5 `color.app.primary`, offset 0px |
| pressed | background oklab(0.999994 0.0000455678 0.0000200868 / 0.1); shadow oklab(0.552007 0.00451359 -0.00660944 / 0.3) 0px 0px 0px 0px; icon 16 x 16, #e2e0e5 `color.docs.gray.200` |

![Search button default](components/crops/d-docs-search-default.png) ![Search button hover](components/crops/d-docs-search-hover.png) ![Search button focus-visible](components/crops/d-docs-search-focus-visible.png) ![Search button pressed](components/crops/d-docs-search-pressed.png)

#### Theme menu button
The docs theme menu button; measured, never opened (the dark capture used a prefers-color-scheme context instead). Read as `d-docs-theme-btn` on the docs dark page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 30 x 30; padding 8px; radius 9999px; background oklab(0.999994 0.0000455678 0.0000200868 / 0.1); text Inter 14/20 400, oklab(0.999994 0.0000455678 0.0000200868 / 0.5); icon 14 x 16, #d1cfd5 `color.docs.gray.300` |
| hover | icon 14 x 16, #f1eff5 `color.docs.gray.100` |
| focus-visible | outline 1px auto #7839e5 `color.app.primary`, offset 0px |
| pressed | icon 14 x 16, #f1eff5 `color.docs.gray.100` |

![Theme menu button default](components/crops/d-docs-theme-btn-default.png) ![Theme menu button hover](components/crops/d-docs-theme-btn-hover.png) ![Theme menu button focus-visible](components/crops/d-docs-theme-btn-focus-visible.png) ![Theme menu button pressed](components/crops/d-docs-theme-btn-pressed.png)

#### Nav item
A docs sidebar link; measured, never followed. Read as `d-docs-nav-item` on the docs dark page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 267 x 32; padding 6px 12px 6px 28px; radius 12px; background oklab(0.529224 0.0935356 -0.219964 / 0.1); text Inter 14/20 400, #7839e5 `color.app.primary` |
| focus-visible | outline 1px auto #7839e5 `color.app.primary`, offset -2px |

![Nav item default](components/crops/d-docs-nav-item-default.png) ![Nav item hover](components/crops/d-docs-nav-item-hover.png) ![Nav item focus-visible](components/crops/d-docs-nav-item-focus-visible.png) ![Nav item pressed](components/crops/d-docs-nav-item-pressed.png)

#### Assistant button
The "Ask AI" assistant entry in the docs chrome; measured at rest, never opened — nothing was sent. Read as `d-docs-assistant` on the docs dark page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 171 x 36; padding 0px 14px 0px 12px; radius 9999px; background oklab(0.999994 0.0000455678 0.0000200868 / 0.03); shadow oklab(0.438582 0.00476192 -0.00700194 / 0.3) 0px 0px 0px 0px; text Inter 14/20 400, oklab(0.999994 0.0000455678 0.0000200868 / 0.5); icon 16 x 16, #a2a0a5 `color.docs.gray.400` |
| hover | background oklab(0.999994 0.0000455678 0.0000200868 / 0.1); shadow oklab(0.552007 0.00451359 -0.00660944 / 0.3) 0px 0px 0px 0px; icon 16 x 16, #e2e0e5 `color.docs.gray.200` |
| focus-visible | outline 1px auto #7839e5 `color.app.primary`, offset 0px |
| pressed | background oklab(0.999994 0.0000455678 0.0000200868 / 0.1); shadow oklab(0.552007 0.00451359 -0.00660944 / 0.3) 0px 0px 0px 0px; icon 16 x 16, #e2e0e5 `color.docs.gray.200` |

![Assistant button default](components/crops/d-docs-assistant-default.png) ![Assistant button hover](components/crops/d-docs-assistant-hover.png) ![Assistant button focus-visible](components/crops/d-docs-assistant-focus-visible.png) ![Assistant button pressed](components/crops/d-docs-assistant-pressed.png)

#### Page heading
The doc page’s h1. Read as `d-docs-h1` on the docs dark page.

**Values (default).** size 168.89 x 40; background transparent; text Inter 36/40 600, #e2e0e5 `color.docs.gray.200`.

![Page heading default](components/crops/d-docs-h1-default.png)

#### Body paragraph
A body paragraph in the doc. Read as `d-docs-para` on the docs dark page.

**Values (default).** size 632 x 28; background transparent; text Inter 18/28 400, #a2a0a5 `color.docs.gray.400`.

![Body paragraph default](components/crops/d-docs-para-default.png)

#### Body link
A link inside the doc body; measured, never followed. Read as `d-docs-link` on the docs dark page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 264 x 32; padding 4px 0px 4px 16px; border L: 1px solid #7839e5 `color.app.primary`; background transparent; text Inter 14/24 400, #7839e5 `color.app.primary`; layers a.text-primary.dark:text-primary-light 264.0x32.0 L:1px solid rgb(120, 57, 229) |
| focus-visible | size 268 x 32; padding 4px 0px 4px 20px; outline 1px auto #7839e5 `color.app.primary`, offset -2px; layers a.text-primary.dark:text-primary-light 268.0x32.0 L:1px solid rgb(120, 57, 229) 1px auto rgb(120, 57, 229) offset -2px |

Child layers that carry the look: a 264x32 border 1px solid #7839e5 `color.app.primary`.

![Body link default](components/crops/d-docs-link-default.png) ![Body link hover](components/crops/d-docs-link-hover.png) ![Body link focus-visible](components/crops/d-docs-link-focus-visible.png) ![Body link pressed](components/crops/d-docs-link-pressed.png)

#### Code block
A code block or inline code span in the doc. Read as `d-docs-code` on the docs dark page.

**Values (default).** size 128 x 20; padding 2px 8px; radius 6px; background oklab(0.999994 0.0000455678 0.0000200868 / 0.05); text Paper Mono 14/21 500, #e2e0e5 `color.docs.gray.200`.

![Code block default](components/crops/d-docs-code-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the 53px header, the hamburger and its drawer, the stacked hero and the email capture.

#### Mobile header
The top bar at 390: wordmark, hamburger and "Get a demo". Read as `m-header` on the marketing home page at 390 wide.

**Values (default).** size 390 x 53; border B: 1px solid rgba(0, 0, 0, 0.15) `color.brand.grey-4`; background #faf9f5 `color.brand.grey-1`; text Unica77 18/24 400, #000000 `color.brand.black`; icon 108 x 22, #0000ee.

![Mobile header default](components/crops/m-header-default.png)

#### Hamburger
The mobile nav toggle (a label over a hidden checkbox); opened to reveal the drawer — a local toggle, its links never followed. Read as `m-hamburger` on the marketing home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40 x 40; background transparent; text Unica77 18/24 400, #000000 `color.brand.black`; layers span.header__hamburger-line 16.0x1.5 rgb(0, 0, 0); span.header__hamburger-line 16.0x1.5 rgb(0, 0, 0) |
| opened | layers span.header__hamburger-line 12.4x12.4 rgb(0, 0, 0); span.header__hamburger-line 12.4x12.4 rgb(0, 0, 0) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: span 16x1.5 background #000000 `color.brand.black`; span 16x1.5 background #000000 `color.brand.black`.

![Hamburger default](components/crops/m-hamburger-default.png) ![Hamburger hover](components/crops/m-hamburger-hover.png) ![Hamburger pressed](components/crops/m-hamburger-pressed.png) ![Hamburger opened](components/crops/m-hamburger-opened.png)

#### Mobile nav drawer
The nav the hamburger opens. Read as `m-drawer` on the marketing home page at 390 wide.

**Values (default).** size 390 x 52; padding 0px 16px; background transparent; text Unica77 24/30 400, #000000 `color.brand.black`; icon 108 x 22, #0000ee; layers span.header__hamburger-line 12.4x12.4 rgb(0, 0, 0); span.header__hamburger-line 12.4x12.4 rgb(0, 0, 0); ul.header__nav 390.0x792.0 rgb(250, 249, 245); form.email-capture-group.get-a-demo 358.0x52.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.1) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.05) 0px 2px 8px -2px, rgba(0, 0, 0, 0.14) 0px 2px 10px -4px 50px; button.email-capture-group__button.button 118.0x40.0 rgb(176, 1.

Child layers that carry the look: span 12.4x12.4 background #000000 `color.brand.black`; span 12.4x12.4 background #000000 `color.brand.black`; ul 390x792 background #faf9f5 `color.brand.grey-1`.

![Mobile nav drawer default](components/crops/m-drawer-default.png)

#### Hero headline (mobile)
"What’s after Excel?" at 390 wide. Read as `m-hero-h1` on the marketing home page at 390 wide.

**Values (default).** size 980 x 48; background transparent; text Serrif Condensed 48/48 400, #000000 `color.brand.black`.

![Hero headline (mobile) default](components/crops/m-hero-h1-default.png)

#### Demo email field (mobile)
The email capture at 390; focused and typed into then cleared — never submitted. Read as `m-email` on the marketing home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 358 x 52; padding 16px 28px; background transparent; text Unica77 16/20 400, #000000 `color.brand.black`; placeholder rgba(0, 0, 0, 0.6) `color.brand.grey-5` |

![Demo email field (mobile) default](components/crops/m-email-default.png) ![Demo email field (mobile) focused](components/crops/m-email-focused.png) ![Demo email field (mobile) filled](components/crops/m-email-filled.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Equals wordmark, the chevrons and hamburger strokes, the mock-toolbar glyphs, social and integration logos) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The real Equals spreadsheet lives behind login — workbook, dashboards, datasources, settings and AI features all need an account and were never reached. `go.equals.com` was measured only as the signed-out card it serves; the form was never submitted. `app.equals.com` did not answer at all during the capture. The 'workbook' components above are the marketing page's own animated mockup of the product, not the app — they show what Equals wants the product to look like, which is still real public evidence, but they must not be read as the authenticated spreadsheet.

### Pages

- **The account and trial flow.** Every post-login surface was never reached; the sign-in form and the demo e-mail captures were measured as fields and never submitted, and the Get-a-demo / Start-free actions were never followed.
- **mobile-usecase.** The phone capture of `/use-cases/arr-dashboard/` hit a security challenge; the phone screenshots that exist are real, and component readings fell back to the desktop measurement rather than being invented.
- **status.equals.com** was reachable but not part of the measured pass.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active), so a state a script adds on real mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **The workbook mockup animates** on a loop; `wb-cell` was read on whichever cell frame was painted, so its geometry is real but the demo's cell contents cycle.
- **Two full-page shots** (docs-dark, docs-charts) timed out mid-capture on the docs' long pages; the `-full` files for them are the chunks that completed, and their `-default` shots are complete.

### Themes

Three distinct public surfaces were captured: the marketing site (light only — the per-page accent comes from `.accent--*`/`.label--*` body classes, not a user toggle), the go.equals.com sign-in card (light only), and the Mintlify docs, which genuinely switch on `html.dark`. tokens.json keeps real light and dark sets; the dark set holds docs roles only, since marketing and sign-in paint no dark theme.

### Fonts

- **Unica77** (marketing body/UI), **Serrif Condensed** (marketing display), **Aeonik Fono** (eyebrow labels), **Aeonik Pro** (declared sans stack) and **Lato** are the served marketing faces; **neue-haas-unica** and **JetBrains Mono** serve the app card; **Inter** and **Paper Mono** serve the docs. They are served from the sites' CDNs; the style guide falls back to system sans.

### Screenshots

- The Equals wordmark, integration logos, photography and workbook artwork in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files, never off a screenshot.

### Content left out

- Customer names, quotes, guide copy and doc page content are the product's published text; only frames and components were measured.
