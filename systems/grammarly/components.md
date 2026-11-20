# Grammarly components

The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from www.grammarly.com on 2026-11-16, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (57 components, 141 states). The page layouts are described in [raw/layout.json](raw/layout.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Matter 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (135 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (grammarly.com paints one light theme on its public pages; the dark values the stylesheets declare are in tokens.json but were never painted). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home. Matter hero, capability carousel, the dark enterprise strip, customer stats, the footer. The Product flyout captured open. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [nav-product-open](screenshots/home-light-nav-product-open.png) |
| Features. The pill tabs and the feature panels; the Proofreading tab selected. | `/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png), [tab-proofreading](screenshots/features-light-tab-proofreading.png) |
| Plans. Three plan columns, the Pro card marked Most popular, the comparison table and FAQ. | `/plans` | [default](screenshots/plans-light-default.png), [full](screenshots/plans-light-full.png) |
| Enterprise landing. | `/business/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| Grammarly Business landing. | `/business` | [default](screenshots/business-light-default.png), [full](screenshots/business-light-full.png) |
| The professionals page. | `/professionals` | [default](screenshots/professionals-light-default.png), [full](screenshots/professionals-light-full.png) |
| The students page. | `/students` | [default](screenshots/students-light-default.png), [full](screenshots/students-light-full.png) |
| Grammarly for Education. | `/edu` | [default](screenshots/edu-light-default.png), [full](screenshots/edu-light-full.png) |
| The AI product page. | `/ai` | [default](screenshots/ai-light-default.png), [full](screenshots/ai-light-full.png) |
| The AI agents page. | `/ai-agents` | [default](screenshots/ai-agents-light-default.png), [full](screenshots/ai-agents-light-full.png) |
| The free grammar checker: editor and Suggestions rail, empty and with a sample sentence analysed (deleted after). | `/grammar-check` | [default](screenshots/grammar-check-light-default.png), [filled](screenshots/grammar-check-light-filled.png), [full](screenshots/grammar-check-light-full.png) |
| The plagiarism checker tool. | `/plagiarism-checker` | [default](screenshots/plagiarism-checker-light-default.png), [full](screenshots/plagiarism-checker-light-full.png) |
| The paraphrasing tool, empty and with a sample sentence (deleted after). | `/paraphrasing-tool` | [default](screenshots/paraphrasing-tool-light-default.png), [filled](screenshots/paraphrasing-tool-light-filled.png), [full](screenshots/paraphrasing-tool-light-full.png) |
| The AI detector tool. | `/ai-detector` | [default](screenshots/ai-detector-light-default.png), [full](screenshots/ai-detector-light-full.png) |
| The word counter tool. | `/word-counter` | [default](screenshots/word-counter-light-default.png), [full](screenshots/word-counter-light-full.png) |
| The desktop apps page. | `/desktop` | [default](screenshots/desktop-light-default.png), [full](screenshots/desktop-light-full.png) |
| The browser extensions page. | `/browser` | [default](screenshots/browser-light-default.png), [full](screenshots/browser-light-full.png) |
| The trust and security page. | `/trust` | [default](screenshots/trust-light-default.png), [full](screenshots/trust-light-full.png) |
| The contact-sales form; a field focused. | `/contact/sales` | [default](screenshots/contact-sales-light-default.png), [field-focused](screenshots/contact-sales-light-field-focused.png), [full](screenshots/contact-sales-light-full.png) |
| The sign-in dialog over the dimmed home page, empty and with a placeholder email typed and deleted. Never submitted. | `/signin` | [default](screenshots/signin-light-default.png), [email-filled](screenshots/signin-light-email-filled.png), [full](screenshots/signin-light-full.png) |
| The sign-up page. | `/signup` | [default](screenshots/signup-light-default.png), [full](screenshots/signup-light-full.png) |
| The blog index. | `/blog/` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Home at 390: header, hero, the open navigation sheet and the full page. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Plans at 390. | `/plans` | [default](screenshots/mobile-plans-light-default.png), [full](screenshots/mobile-plans-light-full.png) |
| The grammar checker at 390. | `/grammar-check` | [default](screenshots/mobile-grammar-check-light-default.png), [full](screenshots/mobile-grammar-check-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Product flyout | the nav, every page | the Product menu button (a UI toggle); closed with Escape afterwards | [home-light-nav-product-open](screenshots/home-light-nav-product-open.png), [nav-panel](#nav-panel) |
| Feature tab, selected | features | the tab itself pressed (a UI toggle) | [features-light-tab-proofreading](screenshots/features-light-tab-proofreading.png), [tab-selected](#tab-selected) |
| Checker, filled | grammar checker | a sample sentence typed into the free editor, analysed, then deleted; never submitted | [grammar-check-light-filled](screenshots/grammar-check-light-filled.png), [checker-filled](#checker-filled) |
| Paraphraser, filled | paraphrasing tool | a sample sentence typed, then deleted; never submitted | [paraphrasing-tool-light-filled](screenshots/paraphrasing-tool-light-filled.png) |
| Form field, focused | contact sales | a field clicked into; nothing typed or sent | [contact-sales-light-field-focused](screenshots/contact-sales-light-field-focused.png) |
| Email field, filled | sign-in | the placeholder name@example.com typed, shot, deleted; never submitted | [signin-light-email-filled](screenshots/signin-light-email-filled.png), [signin-email](#signin-email) |
| Mobile navigation sheet | home at 390 | the menu's own Open button; closed with its Close button | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu](#m-menu) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 24 components were given a real keyboard focus. 20 draw a ring: `nav-menu-button` (2px solid #027e6f `green.60`, offset 0px), `nav-link` (2px solid #027e6f `green.60`, offset 1px), `nav-demo` (2px solid #027e6f `green.60`, offset 1px), `nav-login` (2px solid #027e6f `green.60`, offset 1px), `nav-signup` (2px solid #027e6f `green.60`, offset 2px), `btn-hero` (2px solid #027e6f `green.60`, offset 2px), `btn-google` (2px solid #027e6f `green.60`, offset 2px), `btn-carousel` (3px solid #027e6f `green.60`, offset 2px), `feature-card` (3px solid #027e6f `green.60`, offset 3px), `stat-card` (2px solid #11a683, offset -4px), `link-legal` (2px solid #027e6f `green.60`, offset 1px), `footer-link` (1px auto #101010, offset 1px), `plan-cta-primary` (2px solid #027e6f `green.60`, offset 2px), `plan-cta-secondary` (2px solid #027e6f `green.60`, offset 2px), `info-icon-button` (2px solid #027e6f `green.60`, offset 2px), `tools-nav-item` (2px solid #027e6f `green.60`, offset 2px), `form-select` (1px auto #101010, offset 0px), `signin-help-link` (2px solid #027e6f `green.60`, offset 2px), `m-menu-button` (2px solid #027e6f `green.60`, offset 0px), `m-hero-btn` (2px solid #027e6f `green.60`, offset 2px). The other 4 draw none, so a keyboard user sees no change: `tab`, `checker-cta`, `signin-continue`, `signin-provider`. Focus could not be held on 3 more (`nav-panel-item`, `copy-button`, `form-submit`), so their focus look is uncaptured, not absent.

**Pressed.** Pressed was forced with DevTools (`:active` + `:hover` forced on the node), so no link, submit or sign-in control could fire. The `--button-*-background-active` tokens say the buttons change fill on press rather than transform; the state rows below record what was actually painted.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease` | background-color | info-icon-button |
| 0.2s | `ease` | background-color, box-shadow, transform | btn-carousel, feature-card |
| 0.2s | `ease-out` | transform | stat-card |
| 0.3s | `ease` | all, inset-block-start, visibility | checker-cta, m-menu, tools-nav |
| 0.3s | `ease-in` | transform | m-menu |
| 0.4s | `ease` | color | tab, tab-selected |

**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).

| Page | 1440 | 1920 | 1024 | 390 |
|---|---|---|---|---|
| home | content x 0, 1440 wide; grid 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 gap 32px | content x 0, 1920 wide; grid 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 gap 32px | content x 0, 1024 wide; grid 45.3 45.3 45.3 45.3 45.3 45.3 45.3 45.3 45.3 45.3 45.3 45.3 gap 32px | content x 0, 390 wide; grid 65.5 65.5 65.5 65.5 gap 32px |
| plans | content x 0, 1440 wide | content x 0, 1920 wide | content x 0, 1024 wide | content x 0, 390 wide |
| features | content x 0, 1440 wide; grid 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 gap 32px | content x 0, 1920 wide; grid 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 gap 32px | content x 0, 1024 wide; grid 200 200 200 200 gap 32px | content x 0, 390 wide; grid 65.5 65.5 65.5 65.5 gap 32px |
| grammar-check | content x 0, 1440 wide; grid 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 gap 32px | content x 0, 1920 wide; grid 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 77.3 gap 32px | content x 0, 1024 wide; grid 45.3 45.3 45.3 45.3 45.3 45.3 45.3 45.3 45.3 45.3 45.3 45.3 gap 32px | content x 0, 390 wide; grid 65.5 65.5 65.5 65.5 gap 32px |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Feature card](#feature-card) | 417.33 x 382.78 | 1px solid #ebebeb `neutral.10` | 8px | #ffffff `white` | none | 0 |
| [Customer stat card](#customer-stat-card) | 390 x 500 | - | 8px | #ffffff `white` | none | 0 |
| [Plan card (featured)](#plan-card-featured) | 386.67 x 786 | 1px #0d8065 | - | #eafaf9 `green.0` | none | 0 |
| [Plan card (plain)](#plan-card-plain) | 386.67 x 786 | 1px #cdd1dc `gds.blue-gray.10` | 8px 0px 0px 8px | transparent | none | 0 |
| [Promo banner](#promo-banner) | 1440 x 51.19 | - | - | #00231f `green.100` | none | 0px 14px |
| [Dark section](#dark-section) | 1440 x 469 | - | - | transparent | none | 96px 80px 0px 80px |
| [Sign-in card](#sign-in-card) | 396 x 202 | - | - | transparent | none | 0 |
| [Checker frame](#checker-frame) | 1280 x 666 | - | - | transparent | none | 32px 0px |
| [Suggestions rail (onboarding)](#suggestions-rail-onboarding) | 267 x 215 | - | - | transparent | none | 0 |
| [Mobile menu](#mobile-menu) | 390 x 844 | - | - | #ffffff `white` | none | 0 |

## Components

### Shell and navigation

The marketing shell shared by every public page: a 65px sticky header with the Grammarly lockup, the Product/Work/Education/Resources menu buttons, the Pricing link and the Request a demo / Log in / Sign Up cluster. The Product menu opens a flyout panel (a UI toggle, no navigation).

#### Top nav
The fixed bar over every page: the Grammarly lockup, the Product/Work/Education/Resources menu buttons, the Pricing link, then Request a demo, Log in and the Sign Up pill. Read as `header` on the home page.

**Values (default).** size 1440 x 65; background transparent; text Glyph 14/20 400, #1c1c1c `neutral.100`.

Child layers that carry the look: header 1440x65 background #ffffff `white` border 1px #d9d9d9 `neutral.20`; button 98x32 background rgba(255, 255, 255, 0) `transparent` border 1px transparent radius 4px; div 0x0 background #ffffff `white` shadow rgba(135, 141, 162, 0.25) 0px 2px 12px 0.5px, rgba(135, 141, 162, 0.1) 0px 1px 8px 0.5px, rgba(135, 141, 162, 0.5) 0px 0px 2px 0.5px, #878da2 `gds.blue-gray.40` 0px 0px 0px 0.5px.

![Top nav default](components/crops/header-default.png)

#### Brand lockup
The Grammarly mark + wordmark link in the nav start. Read as `brand` on the home page.

**Values (default).** size 158 x 34; background transparent; text Glyph 16/normal 400, #0000ee.

![Brand lockup default](components/crops/brand-default.png)

#### Nav menu button
A top-level menu trigger (Product): nav text with a chevron; opens the flyout panel. Read as `nav-menu-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 98 x 32; padding 0px 12px; border 1px solid transparent; radius 4px; background rgba(255, 255, 255, 0) `transparent`; text Glyph 14/20 400, #1c1c1c `neutral.100`; icon 10 x 6, #1c1c1c `neutral.100` |
| hover | background transparent |
| focus-visible | outline 2px solid #027e6f `green.60`, offset 0px |
| pressed | background transparent |

![Nav menu button default](components/crops/nav-menu-button-default.png) ![Nav menu button hover](components/crops/nav-menu-button-hover.png) ![Nav menu button focus-visible](components/crops/nav-menu-button-focus-visible.png) ![Nav menu button pressed](components/crops/nav-menu-button-pressed.png)

#### Nav dropdown panel
The Product flyout: a floating panel with Learn and Use Grammarly columns of item rows. Read as `nav-panel` on the home page.

**Values (default).** size 667 x 463; background #ffffff `white`; shadow rgba(135, 141, 162, 0.25) 0px 2px 12px 0.5px, rgba(135, 141, 162, 0.1) 0px 1px 8px 0.5px, rgba(135, 141, 162, 0.5) 0px 0px 2px 0.5px, #878da2 0px 0px 0px 0.5px; text glyph 14/21 700, #1c1c1c `neutral.100`; icon 20 x 20, #0000ee.

![Nav dropdown panel default](components/crops/nav-panel-default.png)

#### Nav dropdown item
Read as `nav-panel-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 253 x 38; padding 8px 16px; radius 4px; background transparent; text Glyph 14/22 400, #1c1c1c `neutral.100` |
| hover, pressed | outline 1px solid #027e6f `green.60`, offset 0px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible`), so its focus look is uncaptured, not measured as absent.

![Nav dropdown item default](components/crops/nav-panel-item-default.png) ![Nav dropdown item hover](components/crops/nav-panel-item-hover.png) ![Nav dropdown item pressed](components/crops/nav-panel-item-pressed.png)

#### Nav link
The plain text link in the bar (Pricing). Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 69 x 32; padding 0px 12px; border 1px solid transparent; radius 4px; background transparent; text Glyph 14/20 400, #1c1c1c `neutral.100` |
| focus-visible | outline 2px solid #027e6f `green.60`, offset 1px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Request a demo link
The secondary text link in the nav end. Measured, never followed. Read as `nav-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 132 x 32; padding 0px 12px; border 1px solid transparent; radius 4px; background transparent; text Glyph 14/20 700, #1c1c1c `neutral.100` |
| focus-visible | outline 2px solid #027e6f `green.60`, offset 1px |

![Request a demo link default](components/crops/nav-demo-default.png) ![Request a demo link hover](components/crops/nav-demo-hover.png) ![Request a demo link focus-visible](components/crops/nav-demo-focus-visible.png) ![Request a demo link pressed](components/crops/nav-demo-pressed.png)

#### Log in link
The plain sign-in link in the nav end. Measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 66 x 32; padding 0px 12px; border 1px solid transparent; radius 4px; background transparent; text Glyph 14/20 700, #1c1c1c `neutral.100` |
| focus-visible | outline 2px solid #027e6f `green.60`, offset 1px |

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Sign Up (nav)
The green pill in the nav end. Measured, never followed. Read as `nav-signup` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 121 x 34; padding 0px 8px; border 1px solid transparent; radius 6px; background #027e6f `green.60`; text Glyph 14/32 700, #ffffff `white` |
| hover | background #014c43 `green.90` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px; outline 2px solid #027e6f `green.60`, offset 2px |
| pressed | background #014c43 `green.90` |

![Sign Up (nav) default](components/crops/nav-signup-default.png) ![Sign Up (nav) hover](components/crops/nav-signup-hover.png) ![Sign Up (nav) focus-visible](components/crops/nav-signup-focus-visible.png) ![Sign Up (nav) pressed](components/crops/nav-signup-pressed.png)

### Buttons

The site's rounded-rectangle buttons (the `base-module_basic__*` family): the green primary, the bordered secondary and the ghost variants, plus the round carousel arrows.

#### Primary button (hero)
The large green button under the hero ("Sign up It's free"): the brand fill, radius 6-ish, trailing arrow. Measured, never followed. Read as `btn-hero` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 60; padding 16px 24px; border 1px solid transparent; radius 6px; background #027e6f `green.60`; text Glyph 14/24 700, #ffffff `white`; icon 11 x 10, #ffffff `white` |
| hover | background #014c43 `green.90` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px; outline 2px solid #027e6f `green.60`, offset 2px |
| pressed | background #014c43 `green.90` |

![Primary button (hero) default](components/crops/btn-hero-default.png) ![Primary button (hero) hover](components/crops/btn-hero-hover.png) ![Primary button (hero) focus-visible](components/crops/btn-hero-focus-visible.png) ![Primary button (hero) pressed](components/crops/btn-hero-pressed.png)

#### Secondary button (Google)
The bordered white button beside the primary CTA ("Sign up with Google"): hairline border, the G mark, same radius. Measured, never followed. Read as `btn-google` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 60; padding 8px 16px; border 1px solid #6d758d; radius 6px; background #ffffff `white`; text Glyph 14/32 400, #4d536e; icon 16 x 16, #4d536e |
| hover | border 1px solid #027e6f `green.60`; shadow #027e6f 0px 0px 0px 1px |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #005fcc 0px 0px 0px 4px; outline 2px solid #027e6f `green.60`, offset 2px |
| pressed | border 1px solid #027e6f `green.60`; shadow #027e6f 0px 0px 0px 1px |

![Secondary button (Google) default](components/crops/btn-google-default.png) ![Secondary button (Google) hover](components/crops/btn-google-hover.png) ![Secondary button (Google) focus-visible](components/crops/btn-google-focus-visible.png) ![Secondary button (Google) pressed](components/crops/btn-google-pressed.png)

#### Carousel arrow button
The round Next arrow on the feature carousel (the Previous arrow sits collapsed at the start of the strip). Read as `btn-carousel` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 48; border 1px solid #545454 `neutral.80`; radius 50%; background #f5f5f5 `neutral.0`; text Glyph 14/normal 400, #545454 `neutral.80`; transition background-color 0.2s ease, transform 0.2s ease; icon 20 x 20, #545454 `neutral.80` |
| hover | background #d9d9d9 `neutral.20` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px; outline 3px solid #027e6f `green.60`, offset 2px |
| pressed | background #d9d9d9 `neutral.20` |

![Carousel arrow button default](components/crops/btn-carousel-default.png) ![Carousel arrow button hover](components/crops/btn-carousel-hover.png) ![Carousel arrow button focus-visible](components/crops/btn-carousel-focus-visible.png) ![Carousel arrow button pressed](components/crops/btn-carousel-pressed.png)

### Pricing

The plans page: a three-column plan grid (Free, Pro, Enterprise), the featured Pro card with its Most-popular header and Try-for-free tag, the per-plan CTAs, the Compare Plans table with its info icon buttons and the FAQ accordion. The captured page paints no billing-period switch.

#### Billing period switch
The Monthly/Yearly toggle that used to sit above the plan cards. Not present in the captured /plans markup — recorded as a gap. Read as `billing-switch` on the plans page.

Not on the page when it was captured.

#### Plan grid
The three-column plans list: Free, Pro (marked Most popular), Enterprise. Read as `plan-grid` on the plans page.

**Values (default).** size 1160 x 786; background transparent; text glyph 14/21 700, #ffffff `white`; icon 18 x 21, #ffffff `white`.

Child layers that carry the look: div 386.7x36 background #027e6f `green.60` radius 8px 8px 0px 0px; div 386.7x750 border 1px #cdd1dc `gds.blue-gray.10` radius 8px 0px 0px 8px; button 305.7x48 background rgba(255, 255, 255, 0) `transparent` border 1px #027e6f `green.60` radius 6px.

![Plan grid default](components/crops/plan-grid-default.png)

#### Plan card (featured)
The Pro column ($12 USD/month as captured): the "Most popular" green header bar, the price, the Try-for-free tag and its CTAs. Read as `plan-card` on the plans page.

**Values (default).** size 386.67 x 786; background transparent; text glyph 14/21 700, #ffffff `white`; icon 18 x 21, #ffffff `white`.

Child layers that carry the look: div 386.7x36 background #027e6f `green.60` radius 8px 8px 0px 0px; div 386.7x750 background #eafaf9 `green.0` border 1px #0d8065; div 70x20 background #eafaf9 `green.0` border 1px #73e1d4 `green.20` radius 4px.

![Plan card (featured) default](components/crops/plan-card-default.png)

#### Plan card (plain)
The Free column: quiet card next to the featured one. Read as `plan-card-plain` on the plans page.

**Values (default).** size 386.67 x 786; background transparent; text glyph 14/21 700, #ffffff `white`; icon 18 x 21, #ffffff `white`.

Child layers that carry the look: div 386.7x36 background #027e6f `green.60` radius 8px 8px 0px 0px; div 386.7x750 border 1px #cdd1dc `gds.blue-gray.10` radius 8px 0px 0px 8px; button 305.7x48 background rgba(255, 255, 255, 0) `transparent` border 1px #027e6f `green.60` radius 6px.

![Plan card (plain) default](components/crops/plan-card-plain-default.png)

#### Try-for-free tag
The small tag beside the Pro price ("Try for free"): a pill tag with its own fill. Read as `sticker-tag` on the plans page.

**Values (default).** size 60 x 18.02; background transparent; text Glyph 12.04/18.01 400, #016a5e `green.80`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Plan CTA (primary)
The green CTA inside the Pro card. Measured, never followed. Read as `plan-cta-primary` on the plans page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 304.67 x 48; padding 0px 8px; border 1px solid transparent; radius 6px; background #027e6f `green.60`; text Glyph 16/25 500, #ffffff `white` |
| hover | background #014c43 `green.90` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px; outline 2px solid #027e6f `green.60`, offset 2px |
| pressed | background #014c43 `green.90` |

![Plan CTA (primary) default](components/crops/plan-cta-primary-default.png) ![Plan CTA (primary) hover](components/crops/plan-cta-primary-hover.png) ![Plan CTA (primary) focus-visible](components/crops/plan-cta-primary-focus-visible.png) ![Plan CTA (primary) pressed](components/crops/plan-cta-primary-pressed.png)

#### Plan CTA (secondary)
The bordered CTA in a plan card (Create account / Contact Sales). Measured, never followed. Read as `plan-cta-secondary` on the plans page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 305.67 x 48; padding 0px 8px; border 1px solid #027e6f `green.60`; radius 6px; background rgba(255, 255, 255, 0) `transparent`; text Glyph 16/25 500, #027e6f `green.60` |
| hover | shadow #027e6f 0px 0px 0px 1px |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px; outline 2px solid #027e6f `green.60`, offset 2px |
| pressed | shadow #027e6f 0px 0px 0px 1px |

![Plan CTA (secondary) default](components/crops/plan-cta-secondary-default.png) ![Plan CTA (secondary) hover](components/crops/plan-cta-secondary-hover.png) ![Plan CTA (secondary) focus-visible](components/crops/plan-cta-secondary-focus-visible.png) ![Plan CTA (secondary) pressed](components/crops/plan-cta-secondary-pressed.png)

#### Info icon button
The round "More information" icon button beside a row in the Compare Plans table. Read as `info-icon-button` on the plans page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 6px; background transparent; text Glyph 14/normal 400, #707070 `neutral.60`; transition background-color 0.1s ease; icon 20 x 20, #707070 `neutral.60` |
| hover | background #ebebeb `neutral.10`; text Glyph 14/normal 400, #545454 `neutral.80`; icon 20 x 20, #545454 `neutral.80` |
| focus-visible | outline 2px solid #027e6f `green.60`, offset 2px |
| pressed | background #ebebeb `neutral.10`; text Glyph 14/normal 400, #545454 `neutral.80`; icon 20 x 20, #545454 `neutral.80` |

![Info icon button default](components/crops/info-icon-button-default.png) ![Info icon button hover](components/crops/info-icon-button-hover.png) ![Info icon button focus-visible](components/crops/info-icon-button-focus-visible.png) ![Info icon button pressed](components/crops/info-icon-button-pressed.png)

#### FAQ accordion item
A question row in the plans FAQ ("What will happen to my Premium subscription if I switch to Pro?"): a labelled row with a chevron that opens the answer. Never opened. Read as `faq-item` on the plans page.

**Values (default).** size 700 x 60; padding 16px; border 1px solid #e7e9f5; radius 8px; background #ffffff `white`; text glyph 18/26 400, #0e101a.

![FAQ accordion item default](components/crops/faq-item-default.png)

### Feature pages

The features page's pill tabs (Paragraph rewrites, Proofreading, Clarity, ...) that swap the demo panel.

#### Feature tab list
The pill tabs over the feature demos (Paragraph rewrites, Proofreading, ...): a row of labelled tabs. Read as `tab-list` on the features page.

**Values (default).** size 1280 x 48; border B: 1px solid #545454 `neutral.80`; background transparent; text glyph 20/30 700, #2e2e2e `neutral.90`.

Child layers that carry the look: div 1280x48 border 1px #545454 `neutral.80`; button 320x48 border 2px #2e2e2e `neutral.90`; button 320x48 border 2px transparent.

![Feature tab list default](components/crops/tab-list-default.png)

#### Feature tab
One tab in the feature list. Measured and selected only through the tab itself. Read as `tab` on the features page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 48; padding 0px 0px 16px 0px; border B: 2px solid #2e2e2e `neutral.90`; background transparent; text glyph 20/30 700, #2e2e2e `neutral.90`; transition color 0.4s ease |
| hover | text glyph 20/30 700, #0e101a |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px |
| pressed | text glyph 20/30 700, #0e101a |

Child layers that carry the look: button 320x48 border 2px #2e2e2e `neutral.90`.

![Feature tab default](components/crops/tab-default.png) ![Feature tab hover](components/crops/tab-hover.png) ![Feature tab focus-visible](components/crops/tab-focus-visible.png) ![Feature tab pressed](components/crops/tab-pressed.png)

#### Feature tab, selected
The same tab measured after the page's own tab was pressed: the selected pill. Read as `tab-selected` on the features page.

**Values (default).** size 320 x 48; padding 0px 0px 16px 0px; border B: 2px solid #2e2e2e `neutral.90`; background transparent; text glyph 20/30 700, #0e101a; transition color 0.4s ease.

Child layers that carry the look: button 320x48 border 2px #2e2e2e `neutral.90`.

![Feature tab, selected default](components/crops/tab-selected-default.png)

### Writing tools

The sticky secondary nav strip the free tools share (Grammar Check, Plagiarism Checker, Paraphrasing Tool, ...), each item an icon plus a label, the current tool marked.

#### Tools secondary nav
The sticky strip under the header on the free tools (Grammar Check, Plagiarism Checker, Paraphrasing Tool, ...): icon + label links, the current tool underlined. Read as `tools-nav` on the grammar checker page.

**Values (default).** size 1440 x 46; padding 0px 8px; border B: 1px solid #d9d9d9 `neutral.20`; background #ffffff `white`; text Inter 14/21 500, #1c1c1c `neutral.100`; transition inset-block-start 0.3s ease; icon 20 x 20, #1c1c1c `neutral.100`.

![Tools secondary nav default](components/crops/tools-nav-default.png)

#### Tools nav item
One item in the tools strip; the first is the current page. Read as `tools-nav-item` on the grammar checker page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 148 x 29; padding 4px 8px; radius 4px; background transparent; text Inter 14/21 500, #1c1c1c `neutral.100`; icon 20 x 20, #1c1c1c `neutral.100` |
| focus-visible | outline 2px solid #027e6f `green.60`, offset 2px |

Child layers that carry the look: a::after 148pxx1px background #1c1c1c `neutral.100`.

![Tools nav item default](components/crops/tools-nav-item-default.png) ![Tools nav item hover](components/crops/tools-nav-item-hover.png) ![Tools nav item focus-visible](components/crops/tools-nav-item-focus-visible.png) ![Tools nav item pressed](components/crops/tools-nav-item-pressed.png)

### Grammar checker

The free grammar checker at /grammar-check: a two-column panel — the contenteditable writing area at the left, the Suggestions rail at the right. A sample sentence was typed to watch the checker underline issues and fill the rail, then deleted; nothing was submitted.

#### Checker frame
The free grammar checker: a two-column panel — the editor on the left, the Suggestions rail on the right. Read as `checker` on the grammar checker page.

**Values (default).** size 1280 x 666; padding 32px 0px; background transparent; text matter 46/50 670, #0e101a.

Child layers that carry the look: div 1000x384 background #ffffff `white` border 1px #c6cbde radius 12px shadow rgba(26, 33, 52, 0.11) 0px 12px 48px 0px; div 0x0 border 1px #c6cbde; button 0x0 background rgba(255, 255, 255, 0) `transparent` border 1px #027e6f `green.60` radius 6px.

![Checker frame default](components/crops/checker-default.png)

#### Editor area
The writing area with the "Start writing here" placeholder: a large bordered field. Read as `checker-editor` on the grammar checker page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 670 x 334; padding 12px 15px; background transparent; text inter 16/28 400, #0e101a |

![Editor area default](components/crops/checker-editor-default.png) ![Editor area focused](components/crops/checker-editor-focused.png)

#### Suggestions rail (onboarding)
The right rail of the free checker: the Suggestions header and the three-step "Let's get started" card shown to signed-out visitors. Read as `suggestions-panel` on the grammar checker page.

**Values (default).** size 267 x 215; background transparent; text glyph 20/30 700, #0e101a.

![Suggestions rail (onboarding) default](components/crops/suggestions-panel-default.png)

#### Editor, filled
The editor after a sample sentence was typed (then deleted): text in the field, issue underlines painted by the checker. Read as `checker-filled` on the grammar checker page.

**Values (default).** size 670 x 334; padding 12px 15px; background transparent; text inter 16/28 400, #0e101a.

![Editor, filled default](components/crops/checker-filled-default.png)

#### Suggestion card
A suggestion card in the rail (issue type, fix, Accept/Dismiss). The checker's issue underlines and cards are painted by a product overlay outside the page's light DOM; nothing matched in the signed-out run — recorded as a gap. Read as `suggestion-card` on the grammar checker page.

Not on the page when it was captured.

#### Get Grammarly CTA
The green CTA in the Suggestions rail. Measured, never followed. Read as `checker-cta` on the grammar checker page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 267 x 50; padding 8px; border 1px solid transparent; radius 6px; background #0d8065; text Glyph 14/32 700, #ffffff `white`; transition all 0.3s ease |
| hover | background #006c51 |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #0d8065 0px 0px 0px 4px |
| pressed | background #006c51 |

![Get Grammarly CTA default](components/crops/checker-cta-default.png) ![Get Grammarly CTA hover](components/crops/checker-cta-hover.png) ![Get Grammarly CTA focus-visible](components/crops/checker-cta-focus-visible.png) ![Get Grammarly CTA pressed](components/crops/checker-cta-pressed.png)

#### Copy text button
The quiet button over the editor that copies the field's text (present in the DOM but collapsed when the editor's helper footer is hidden). Measured, never pressed. Read as `copy-button` on the grammar checker page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 0 x 0; padding 0px 8px; border 1px solid #027e6f `green.60`; radius 6px; background rgba(255, 255, 255, 0) `transparent`; text Glyph 14/32 400, #027e6f `green.60` |
| pressed | shadow #027e6f 0px 0px 0px 1px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible`), so its focus look is uncaptured, not measured as absent.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Get-started steps
The numbered steps inside the rail's onboarding card ("Add your text...", "Hover over the underlines...", "Click a suggestion..."). Read as `getting-started` on the grammar checker page.

**Values (default).** size 267 x 105; background transparent; text glyph 14/21 700, #0e101a.

![Get-started steps default](components/crops/getting-started-default.png)

### Forms

The contact-sales lead form: labelled required fields, selects and the Submit button. Fields were clicked and sample text typed and deleted; nothing was submitted.

#### Contact sales form
The lead form ("Contact our Sales team"): labelled required fields, selects and the Submit button. Read as `form` on the contact sales page.

**Values (default).** size 653.33 x 1142; padding 32px 40px 40px 40px; background transparent; text inter 14/22 400, #1f243c; icon 12 x 12, #6d758d.

Child layers that carry the look: input 573.3x42 background #ffffff `white` border 1px #646b81 `gds.blue-gray.60` radius 4px; input 573.3x42 background #ffffff `white` border 1px #646b81 `gds.blue-gray.60` radius 4px; input 573.3x42 background #ffffff `white` border 1px #646b81 `gds.blue-gray.60` radius 4px.

![Contact sales form default](components/crops/form-default.png)

#### Field label
A field caption ("Work email*"): small text over the input. Read as `form-label` on the contact sales page.

**Values (default).** size 573.33 x 22; background transparent; text inter 14/22 400, #1f243c.

![Field label default](components/crops/form-label-default.png)

#### Text field
A single-line input in the sales form: hairline border, placeholder only via the label. Text was typed and deleted; nothing sent. Read as `form-input` on the contact sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 573.33 x 42; padding 8px 10px; border 1px solid #646b81 `gds.blue-gray.60`; radius 4px; background #ffffff `white`; text Arial 16/24 400, #000000; placeholder #000000 |
| focused | border 1px solid #2551da `blue.60`; outline 1px auto #101010, offset 0px |
| filled | border 1px solid #d31332; outline 1px auto #101010, offset 0px |

![Text field default](components/crops/form-input-default.png) ![Text field focused](components/crops/form-input-focused.png) ![Text field filled](components/crops/form-input-filled.png)

#### Select
A dropdown in the sales form (institution type, product, country): same field skin with a chevron. Never opened. Read as `form-select` on the contact sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 573.33 x 42; padding 8px 10px; border 1px solid #646b81 `gds.blue-gray.60`; radius 4px; background #ffffff `white`; text Arial 16/24 400, #000000 |
| focus-visible | border 1px solid #2551da `blue.60`; outline 1px auto #101010, offset 0px |
| pressed | border 1px solid #2551da `blue.60` |

![Select default](components/crops/form-select-default.png) ![Select hover](components/crops/form-select-hover.png) ![Select focus-visible](components/crops/form-select-focus-visible.png) ![Select pressed](components/crops/form-select-pressed.png)

#### Submit button
The form's green Submit. Measured, never pressed. Read as `form-submit` on the contact sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 93 x 60; padding 16px 24px; border 1px solid transparent; radius 6px; background #f0f2fc; text Glyph 14/24 400, #c6cbde |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible`), so its focus look is uncaptured, not measured as absent.

![Submit button default](components/crops/form-submit-default.png) ![Submit button hover](components/crops/form-submit-hover.png) ![Submit button pressed](components/crops/form-submit-pressed.png)

### Footer

The site foot: link columns, the legal bar and the social icons.

#### Footer
The site foot: link columns, the legal bar and the social icons. Read as `footer` on the home page.

**Values (default).** size 1440 x 1188; padding 16px 80px; background transparent; text Glyph 14/normal 700, #1f243c; icon 20 x 20, #1f243c.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 192 x 17.5; background transparent; text Glyph 14/17.5 400, #1f243c |
| focus-visible | outline 1px auto #101010, offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Dialogs and overlays

The sign-in page's dialog over the dimmed home page — the email field, the provider rows and the Continue button. Shot and measured, never submitted.

#### Sign-in card
The account card on /signin ("Sign in" with the email field and the provider buttons). Shot and measured, never submitted. Read as `signin-dialog` on the sign-in page.

**Values (default).** size 396 x 202; background transparent; text Matter 24/32 400, #0e101a; icon 16 x 11, #000000.

Child layers that carry the look: div 396x48 border 1px #6d758d radius 4px; input 394x46 background #ffffff `white` radius 4px; div 396x48 border 1px #6d758d radius 4px.

![Sign-in card default](components/crops/signin-dialog-default.png)

#### Email field
The sign-in email input: hairline border with the Email label inside. Text was typed and deleted; nothing sent. Read as `signin-email` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 394 x 46; padding 12px 12px 0px 12px; radius 4px; background #ffffff `white`; text Glyph 16/21 400, #000000; placeholder #000000 |
| focused, filled | outline 2px solid #0b6a54, offset 2px |

![Email field default](components/crops/signin-email-default.png) ![Email field focused](components/crops/signin-email-focused.png) ![Email field filled](components/crops/signin-email-filled.png)

#### Continue button
The dialog's green primary. Measured, never pressed. Read as `signin-continue` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 396 x 48; padding 8px 16px; border 1px solid transparent; radius 6px; background #027e6f `green.60`; text Glyph 14/32 700, #ffffff `white` |
| hover | background #014c43 `green.90` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #027e6f 0px 0px 0px 4px |
| pressed | background #014c43 `green.90` |

![Continue button default](components/crops/signin-continue-default.png) ![Continue button hover](components/crops/signin-continue-hover.png) ![Continue button focus-visible](components/crops/signin-continue-focus-visible.png) ![Continue button pressed](components/crops/signin-continue-pressed.png)

#### Provider button
A social sign-in row (Google, Facebook, Apple, SSO): bordered, icon left, chevron right. Measured, never followed. Read as `signin-provider` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 396 x 48; padding 8px 16px; border 1px solid #6d758d; radius 4px; background #ffffff `white`; text Glyph 14/32 400, #4d536e; icon 16 x 16, #4d536e |
| hover | background #f9faff |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #005fcc 0px 0px 0px 4px |
| pressed | background #f9faff |

![Provider button default](components/crops/signin-provider-default.png) ![Provider button hover](components/crops/signin-provider-hover.png) ![Provider button focus-visible](components/crops/signin-provider-focus-visible.png) ![Provider button pressed](components/crops/signin-provider-pressed.png)

#### Troubleshoot link
The quiet link under the primary ("Can't sign in?") and the "I don't have an account" link. Measured, never followed. Read as `signin-help-link` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 144 x 17; background transparent; text Glyph 14/22 400, #027e6f `green.60` |
| focus-visible | radius 2px; outline 2px solid #027e6f `green.60`, offset 2px |

![Troubleshoot link default](components/crops/signin-help-link-default.png) ![Troubleshoot link hover](components/crops/signin-help-link-hover.png) ![Troubleshoot link focus-visible](components/crops/signin-help-link-focus-visible.png) ![Troubleshoot link pressed](components/crops/signin-help-link-pressed.png)

### Content and cards

The home page's content furniture: the Matter hero, the capability cards in the carousel, the dark enterprise strip's stat cards, the promo banner and the dark marketing sections.

#### Hero title
The page's display line ("Think big. We'll take care of the details."): Matter, large size, tight tracking. Read as `hero` on the home page.

**Values (default).** size 890 x 50; background transparent; text matter 46/50 670, #0e101a.

![Hero title default](components/crops/hero-default.png)

#### Hero lede
The supporting line under the hero title. Read as `hero-lede` on the home page.

**Values (default).** size 890 x 26; background transparent; text glyph 18/26 400, #0e101a.

![Hero lede default](components/crops/hero-lede-default.png)

#### Feature card
A card in the capability carousel ("Paragraph rewrites", "Tone suggestions"): a screenshot tile over a title and a lede, on the page ground. Read as `feature-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 417.33 x 382.78; border 1px solid #ebebeb `neutral.10`; radius 8px; background #ffffff `white`; text Matter 20.00/24.00 600, #000000; transition transform 0.2s ease, box-shadow 0.2s ease |
| hover | size 429.85 x 394.26; shadow rgba(0, 0, 0, 0.16) 0px 12px 32px 0px; transform scale(1.03) |
| focus-visible | size 429.85 x 394.26; outline 3px solid #027e6f `green.60`, offset 3px; transform scale(1.03) |
| pressed | size 408.98 x 375.13; shadow rgba(0, 0, 0, 0.16) 0px 12px 32px 0px; transform scale(0.98) |

![Feature card default](components/crops/feature-card-default.png) ![Feature card hover](components/crops/feature-card-hover.png) ![Feature card focus-visible](components/crops/feature-card-focus-visible.png) ![Feature card pressed](components/crops/feature-card-pressed.png)

#### Customer stat card
A linked card in the dark enterprise strip ("20 days saved annually per user"): dark fill, a stat, a name. Measured, never followed. Read as `stat-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 390 x 500; radius 8px; background #ffffff `white`; text matter 52/58 670, #0e101a; icon 11 x 10, #0d8065 |
| hover | shadow rgba(84, 84, 84, 0.08) 0px 8px 20px 0px; transition transform 0.2s ease-out; transform translate(0px, -5px) |
| focus-visible | outline 2px solid #11a683, offset -4px |
| pressed | shadow rgba(84, 84, 84, 0.08) 0px 8px 20px 0px; transition transform 0.2s ease-out; transform translate(0px, -5px) |

![Customer stat card default](components/crops/stat-card-default.png) ![Customer stat card hover](components/crops/stat-card-hover.png) ![Customer stat card focus-visible](components/crops/stat-card-focus-visible.png) ![Customer stat card pressed](components/crops/stat-card-pressed.png)

#### Promo banner
The dark banner aside ("Try Grammarly Pro for free"): dark fill, white text and a pale CTA. Read as `banner` on the home page.

**Values (default).** size 1440 x 51.19; padding 0px 14px; background #00231f `green.100`; text Matter 20/normal 570, #ffffff `white`; icon 14 x 12.72, #d5ff00 `yellowgreen.0`.

![Promo banner default](components/crops/banner-default.png)

#### Dark section
A marketing section painted dark (bg-colors_darkThemeTextColor_*): ink ground with light text, reached without a theme switch. Read as `section-dark` on the home page.

**Values (default).** size 1440 x 469; padding 96px 80px 0px 80px; background transparent; text glyph 14/21 400, #ffffff `white`; icon 11 x 10, #1c1c1c `neutral.100`.

Child layers that carry the look: a 193x60 background #ffffff `white` border 1px transparent radius 6px; a 161x60 background rgba(255, 255, 255, 0) `transparent` border 1px #ffffff `white` radius 6px.

![Dark section default](components/crops/section-dark-default.png)

#### Inline link
A text link inside body copy ("Terms and Conditions" under the hero buttons). Read as `link-legal` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 133 x 17; background transparent; text glyph 14/21 400, #027e6f `green.60` |
| hover | text glyph 14/21 400, #016a5e `green.80` |
| focus-visible | radius 6px; outline 2px solid #027e6f `green.60`, offset 1px |
| pressed | text glyph 14/21 400, #014c43 `green.90` |

![Inline link default](components/crops/link-legal-default.png) ![Inline link hover](components/crops/link-legal-hover.png) ![Inline link focus-visible](components/crops/link-legal-focus-visible.png) ![Inline link pressed](components/crops/link-legal-pressed.png)

### Mobile (390 wide)

A few components as a phone draws them, at 390 x 844 with a mobile user agent.

#### Top nav (mobile)
The 390-wide header: lockup and the menu button. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 65; background transparent; text Glyph 16/normal 400, #1f243c.

Child layers that carry the look: header 390x65 background #ffffff `white` border 1px #d9d9d9 `neutral.20`; button 0x0 background rgba(255, 255, 255, 0) `transparent` border 1px transparent radius 4px; div 0x0 background #ffffff `white` shadow rgba(135, 141, 162, 0.25) 0px 2px 12px 0.5px, rgba(135, 141, 162, 0.1) 0px 1px 8px 0.5px, rgba(135, 141, 162, 0.5) 0px 0px 2px 0.5px, #878da2 `gds.blue-gray.40` 0px 0px 0px 0.5px.

![Top nav (mobile) default](components/crops/m-header-default.png)

#### Menu button
The icon button that opens the mobile navigation sheet. Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 38 x 32; padding 0px 8px; radius 6px; background rgba(255, 255, 255, 0) `transparent`; text Glyph 14/32 400, #000000; icon 22 x 13, #000000 |
| hover | background transparent; outline 1px solid #027e6f `green.60`, offset 0px |
| focus-visible | outline 2px solid #027e6f `green.60`, offset 0px |
| pressed | background transparent; outline 1px solid #027e6f `green.60`, offset 0px |

![Menu button default](components/crops/m-menu-button-default.png) ![Menu button hover](components/crops/m-menu-button-hover.png) ![Menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu
The open navigation sheet at 390: the link list and the sign-in row. Read as `m-menu` on the home page at 390 wide.

**Values (default).** size 390 x 844; background #ffffff `white`; text Glyph 14/20 400, #1c1c1c `neutral.100`; transition visibility 0.3s ease, transform 0.3s ease-in.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Primary button (mobile)
The hero CTA at 390. Read as `m-hero-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 358 x 60; padding 16px 24px; border 1px solid transparent; radius 6px; background #027e6f `green.60`; text Glyph 14/24 700, #ffffff `white`; icon 11 x 10, #ffffff `white` |
| hover | background #014c43 `green.90` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #638eeb 0px 0px 0px 4px; outline 2px solid #027e6f `green.60`, offset 2px |
| pressed | background #014c43 `green.90` |

![Primary button (mobile) default](components/crops/m-hero-btn-default.png) ![Primary button (mobile) hover](components/crops/m-hero-btn-hover.png) ![Primary button (mobile) focus-visible](components/crops/m-hero-btn-focus-visible.png) ![Primary button (mobile) pressed](components/crops/m-hero-btn-pressed.png)

## Icons

38 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. The marketing illustrations and logo walls were left out; these are the interface icons. The SVGs are Grammarly's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [x](icons/x.svg) | 16x12 | 0 0 13 12 | fill | home; features; plans; enterprise; business; professionals; students; edu; ai; ai-agents; grammar-check; plagiarism-checker; paraphrasing-tool; ai-detector; word-counter; desktop; browser; trust; contact-sales; blog; nav | X |
| [facebook](icons/facebook.svg) | 16x14 | 0 0 7 14 | fill | home; features; plans; enterprise; business; professionals; students; edu; ai; ai-agents; grammar-check; plagiarism-checker; paraphrasing-tool; ai-detector; word-counter; desktop; browser; trust; contact-sales; blog; nav | Facebook |
| [instagram](icons/instagram.svg) | 16x13 | 0 0 13 13 | fill | home; features; plans; enterprise; business; professionals; students; edu; ai; ai-agents; grammar-check; plagiarism-checker; paraphrasing-tool; ai-detector; word-counter; desktop; browser; trust; contact-sales; blog; nav | Instagram |
| [linkedin](icons/linkedin.svg) | 16x12 | 0 0 13 12 | fill | home; features; plans; enterprise; business; professionals; students; edu; ai; ai-agents; grammar-check; plagiarism-checker; paraphrasing-tool; ai-detector; word-counter; desktop; browser; trust; contact-sales; blog; nav | LinkedIn |
| [sign-up-it-s-free](icons/sign-up-it-s-free.svg) | 11x10 14x13 | 0 0 11 10 | fill | home; features; enterprise; business; professionals; students; edu; ai; ai-agents; grammar-check; plagiarism-checker; paraphrasing-tool; ai-detector; word-counter; desktop; browser; trust; contact-sales; nav | Sign up It’s free / Learn more / Create Account |
| [superhuman](icons/superhuman-e4ef864c.svg) | 20x20 | 0 0 50 50 | fill | features; enterprise; business; professionals; students; edu; ai; ai-agents; grammar-check; plagiarism-checker; paraphrasing-tool; ai-detector; word-counter; desktop; browser; trust | Superhuman |
| [sign-up-with-google](icons/sign-up-with-google.svg) | 16x16 | 0 0 16 16 | fill | home; features; professionals; students; ai-agents; paraphrasing-tool; ai-detector; desktop; browser; signin; nav | Sign up with Google / Sign in with Google |
| [pause](icons/pause.svg) | 32x32 | 0 0 32 32 | fill | home; enterprise; business; edu; plagiarism-checker; trust; nav | Pause |
| [superhuman](icons/superhuman-941f318f.svg) | 20x20 | 0 0 50 50 | fill | home; plans; contact-sales; blog; nav | Superhuman |
| [statstestimonialcta](icons/statstestimonialcta.svg) | 11x10 | 0 0 11 10 | fill | home; edu; nav | 20 days saved annually per user Mihai Fo / 50% fewer writing |
| [previous](icons/previous.svg) | 20x20 | 0 0 11 11 | stroke | home; edu; nav | Previous |
| [write-without-mistakes](icons/write-without-mistakes.svg) | 24x24 | 0 0 24 24 | stroke | home; plans; nav | Write without mistakes / See your writing tone / Generate te |
| [ai-detector](icons/ai-detector.svg) | 20x20 24x24 | 0 0 20 20 | fill | grammar-check; plagiarism-checker; paraphrasing-tool; ai-detector | AI Detector / AI Detection results |
| [ai-chat](icons/ai-chat.svg) | 20x20 | 0 0 20 20 | fill | grammar-check; plagiarism-checker; paraphrasing-tool; ai-detector | AI Chat |
| [most-popular](icons/most-popular-33624d38.svg) | 18x21 |  | fill | home; nav | Most popular |
| [ai-humanizer](icons/ai-humanizer.svg) | 20x20 | 0 0 20 20 | fill | grammar-check; plagiarism-checker; paraphrasing-tool; ai-detector | AI Humanizer |
| [grammar-check](icons/grammar-check.svg) | 20x20 | 0 0 20 20 | fill | grammar-check; plagiarism-checker; paraphrasing-tool; ai-detector | Grammar Check |
| [paraphrasing-tool](icons/paraphrasing-tool.svg) | 20x20 24x24 | 0 0 20 20 | fill | grammar-check; plagiarism-checker; paraphrasing-tool; ai-detector | Paraphrasing Tool / Paraphrased Text |
| [plagiarism-checker](icons/plagiarism-checker.svg) | 20x20 24x24 | 0 0 20 20 | fill | grammar-check; plagiarism-checker; paraphrasing-tool; ai-detector | Plagiarism Checker / Plagiarism Checker results |
| [next](icons/next-b2961db3.svg) | 20x20 | 0 0 11 11 | stroke | home; nav | Next |
| [upload-file](icons/upload-file.svg) | 20x20 | 0 0 16 16 | fill | plagiarism-checker; paraphrasing-tool; ai-detector | Upload file |
| [next](icons/next-c934f98a.svg) | 20x20 | 0 0 11 11 | stroke | home; nav | Next |
| [more-information](icons/more-information.svg) | 20x20 | 0 0 16 16 | fill | plans; ai-detector | More information / How it works |
| [next](icons/next-08137f98.svg) | 20x20 | 0 0 11 11 | stroke | edu | Next |
| [resembles-ai-text](icons/resembles-ai-text.svg) | 16x16 | 0 0 16 16 | fill | ai-detector | Resembles AI text —% |
| [1pkeu-logo](icons/1pkeu-logo.svg) | 38x18 | 0 0 42 20 | fill | blog |  |
| [icon-2f1fffbc](icons/icon-2f1fffbc.svg) | 56x56 | 0 0 80 80 | fill | paraphrasing-tool |  |
| [hoaur34r](icons/hoaur34r.svg) | 24x24 | 0 0 24 24 | stroke | plans |  |
| [business-education](icons/business-education.svg) | 12x12 | 0 0 8 5 | stroke | contact-sales | Business Education / Superhuman Suite Docs Go Grammarly Mail |
| [open-navigation-menu](icons/open-navigation-menu.svg) | 22x13 | 0 0 22 13 | fill | nav | Open navigation menu |
| [sign-in-with-facebook](icons/sign-in-with-facebook.svg) | 16x16 | 0 0 16 16 | fill | signin | Sign in with Facebook |
| [close-navigation-menu](icons/close-navigation-menu.svg) | 14x14 | 0 0 14 14 | fill | nav | Close navigation menu |
| [scorecircle](icons/scorecircle.svg) | 16x16 | 0 0 16 16 | fill | ai-detector | No AI text patterns found —% |
| [most-popular](icons/most-popular-b32aca25.svg) | 18x21 |  | fill | plans | Most popular |
| [zjuftatq](icons/zjuftatq.svg) | 28x28 | 0 0 28 28 | fill | grammar-check |  |
| [lefticonwrapper](icons/lefticonwrapper.svg) | 16x16 | 0 0 16 16 | fill | signin | Sign in with Single Sign-On |
| [superhuman-logo](icons/superhuman-logo.svg) | 20x20 | 0 0 50 50 | fill | nav | Superhuman Logo |
| [sign-in-with-apple](icons/sign-in-with-apple.svg) | 16x16 | 0 0 14 15 | fill | signin | Sign in with Apple |

## Gaps

### Pages

- **Signed-in pages.** Nothing behind sign-in was captured: the Grammarly editor and dashboard, documents, account and subscription settings, the workspace and admin consoles, and any app.grammarly.com surface. The kit never signs in.
- **Anything that sends or creates.** No form was submitted (contact sales, sign-in, newsletter), no checkout or trial was started, and no tool's output was generated — the free checker's analysis of the typed sample was captured, but the plagiarism checker, AI detector, paraphraser and word counter only produce their result views after a submit action the kit never performs.
- **Blog articles.** Only the blog index was captured; article pages were not traversed.
- **Support and community.** The help centre, community forum and status pages sit on other subdomains and were not captured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled states** were not seen on any public control.
- **Live suggestion cards** never painted: the free checker's issue underlines and Accept/Dismiss cards are rendered by a product overlay outside the page's light DOM, and no public selector matches them (`suggestion-card` is recorded missing). What a signed-out visitor does see — the '3 Suggestions' header and the get-started steps — was captured instead.

### Themes

grammarly.com shows one light theme on its public pages, but its stylesheets declare a full dark theme: the GDS layer under `[data-gds-theme="dark"]` and the Origin layer under `[data-origin-theme="grammarly"][data-origin-mode="dark"]`. No public page mounts those attributes, there is no theme switch anywhere, and `prefers-color-scheme: dark` changes nothing (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). The token file ships the dark set anyway — every value is labelled as declared evidence, resolved synthetically, never painted. The same stylesheets also carry Superhuman and Coda themes (sibling Grammarly Inc. products sharing the Origin system); only the grammarly theme was resolved.

### Fonts

- **Matter** is Grammarly's self-hosted display face; it is served from Grammarly's CDN and is not in the style guide, which falls back to Inter — the same fallback the token stacks name.
- **Super Sans Mono VF** and **Super Serif VF** are Superhuman's brand faces in the Origin stacks; they resolve to the platform fallbacks here.

### Screenshots

- Illustrations, customer logos, product imagery and video frames are Grammarly's content and appear only inside screenshots and crops. Hero and feature sections animate, so two captures of the same view can differ in the frame drawn.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy inside screenshots and crops is Grammarly's content, kept as captured for layout and proportion reference only.
- No personal data was captured: the pages were read signed out, and the only text ever typed was throwaway sample text, deleted in place.
