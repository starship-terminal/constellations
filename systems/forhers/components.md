# forhers components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from forhers.com on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. www.forhers.com answers a Cloudflare managed challenge to this network, so the DOM is Wayback Machine SSR snapshots (2025-12-23 to 2026-11-11, per page) served locally and painted by their archived styled-components and bundled CSS with scripts removed — nothing was signed into, submitted or bought; hover/focus/pressed states were forced, and the controls hydration owns (the slide menu, the Log-in menu, accordion panels, quiz starts) stay closed rather than faked. Nav, card, footer and drug-index links were measured, never followed; the form fields were typed into and cleared, never submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (64 components, 129 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (124 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every page paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at CSS scale (one CSS pixel per image pixel — mobile fulls are 390 wide); mobile viewport shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Weight loss | `/weight-loss` | [default](screenshots/weight-loss-light-default.png), [full](screenshots/weight-loss-light-full.png) |
| Hair loss | `/hair-loss` | [default](screenshots/hair-loss-light-default.png), [full](screenshots/hair-loss-light-full.png) |
| Skin care | `/skin-care` | [default](screenshots/skin-care-light-default.png), [full](screenshots/skin-care-light-full.png) |
| Mental health | `/mental-health` | [default](screenshots/mental-health-light-default.png), [full](screenshots/mental-health-light-full.png) |
| Birth control | `/birth-control` | [default](screenshots/birth-control-light-default.png), [full](screenshots/birth-control-light-full.png) |
| Product: minoxidil + biotin chew | `/hair-loss/minoxidil-biotin-chew` | [default](screenshots/product-light-default.png), [full](screenshots/product-light-full.png) |
| Product: anti-aging | `/skin-care/anti-aging` | [default](screenshots/anti-aging-light-default.png), [full](screenshots/anti-aging-light-full.png) |
| Product: Wegovy pill | `/weight-loss/wegovy-pill` | [default](screenshots/wegovy-pill-light-default.png), [full](screenshots/wegovy-pill-light-full.png) |
| Labs | `/labs` | [default](screenshots/labs-light-default.png), [full](screenshots/labs-light-full.png) |
| Benefits | `/benefits` | [default](screenshots/benefits-light-default.png), [full](screenshots/benefits-light-full.png) |
| Quality and safety | `/quality-and-safety` | [default](screenshots/quality-light-default.png), [full](screenshots/quality-light-full.png) |
| Blog index | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Blog article | `/blog/zoloft-weight-loss` | [default](screenshots/blog-post-light-default.png), [full](screenshots/blog-post-light-full.png) |
| BMI calculator | `/tools/bmi-calculator` | [default](screenshots/bmi-calculator-light-default.png), [full](screenshots/bmi-calculator-light-full.png) |
| Drug information index | `/drugs/info` | [default](screenshots/drugs-info-light-default.png), [full](screenshots/drugs-info-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Weight loss, phone | `/weight-loss` | [default](screenshots/mobile-weight-loss-light-default.png), [full](screenshots/mobile-weight-loss-light-full.png) |
| Product, phone | `/hair-loss/minoxidil-biotin-chew` | [default](screenshots/mobile-product-light-default.png), [full](screenshots/mobile-product-light-full.png) |
| BMI calculator, phone | `/tools/bmi-calculator` | [default](screenshots/mobile-bmi-calculator-light-default.png), [full](screenshots/mobile-bmi-calculator-light-full.png) |
| Blog article, phone | `/blog/zoloft-weight-loss` | [default](screenshots/mobile-blog-post-light-default.png), [full](screenshots/mobile-blog-post-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Slide navigation menu | every page | hydration-only — the menu toggle's drawer renders client-side | the 48px toggle measured; [menu-toggle](#menu-toggle) |
| Log-in menu | every page | hydration-only — the Log in menu renders client-side; sign-in is a boundary anyway | [login-button](#log-in-control) |
| Accordion panels | drug index, shop pages | hydration-only — the toggle rows were measured; the panels never open | [accordion-toggle](#accordion-toggle) |
| Continuity / promo modal | home | a fixed z-900 dialog the SSR ships; hidden for capture, never answered | recorded under chrome in raw/components-computed.json; see Gaps |
| Regional redirect card | several pages | measured as the dialog it is ([region-dialog](#regional-redirect-card)), then hidden — never accepted | captured |
| Promo strip | every page | the lime banner; hidden on some captures to keep the header in frame, never clicked | [promo-bar](#promo-bar) |
| Quiz / consultation start | home and category CTAs | the quiz is a client-rendered flow; starting it crosses a hydration boundary and begins intake | not captured — see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 17 components were given a real keyboard focus. 6 draw an outline ring: `cta-primary` (1px auto #101010 `light.focus.ring`, offset 1px), `cta-underlined` (1px auto #101010 `light.focus.ring`, offset 1px), `read-more` (1px auto #101010 `light.focus.ring`, offset 0px), `region-cta` (1px auto #101010 `light.focus.ring`, offset 1px), `drug-link` (1px auto #101010 `light.focus.ring`, offset 1px), `topic-tab` (1px auto #101010 `light.focus.ring`, offset 1px). 4 change only their border: `nav-link`, `cta-secondary`, `footer-social`, `blog-topic`. The other 7 show no measured change: `logo`, `menu-toggle`, `app-cta`, `cta-tertiary`, `footer-link`, `footer-fineprint`, `form-submit`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease-in` | all | topic-tab |
| 0.2s | `cubic-bezier(0.28, 0.13, 0.38, 1)` | background, box-shadow, transform | disabled-button |
| 0.2s | `cubic-bezier(0.33, 0, 0, 1)` | background-color, color | email-field, m-text-field, text-field |
| 0.2s | `ease-in-out` | background, background-color, border-color, box-shadow, color, outline-color, outline-offset, text-decoration-color, transform | blog-topic, cta-secondary, cta-tertiary, m-cta-primary |
| 0.2s | `linear` | opacity | product-card, treatment-card |
| 0.3s | `ease` | backdrop-filter, background-color, border-color, box-shadow, color, fill, stroke, transform | form-submit, m-header, slide-dot |
| 0.3s | `ease-in-out` | background-color, border-color, color, text-decoration-color | carousel-arrow, footer-social, nav-link |
| 0.3s | `ease-out` | background-color, box-shadow, color, fill, stroke | m-menu-toggle, menu-toggle |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Product card](#product-card) | 320 x 389 | - | - | transparent | none | 0 |
| [Treatment card](#treatment-card) | 320 x 389 | - | - | transparent | none | 0 |
| [Category tile](#category-tile) | 337 x 100 | - | 24px | transparent | none | 0px 8px 0px 16px |
| [Content card](#content-card) | 438 x 584 | - | 16px | transparent | none | 25px |
| [Article card](#article-card) | 691.89 x 389.19 | - | - | transparent | none | 0 |
| [Testimonial card](#testimonial-card) | 546 x 745.25 | - | - | transparent | none | 0px 36px |
| [Mobile bento card](#mobile-bento-card) | 374 x 400 | - | - | transparent | none | 20px |
| [Mobile content card](#mobile-content-card) | 346 x 63.48 | - | - | transparent | none | 0 |

## Components

### Header and site chrome

The sticky top chrome shared by the marketing pages: the lime promo strip, the 56px header (the 'hers' wordmark, category nav links, the circular Log in and menu icon buttons). Measured on the drug index page, where the chrome paints identically.

#### Header
The top chrome: promo bar over the nav row (wordmark, category links, Log in, hamburger). Read as `header` on the mental health page.

**Values (default).** size 1440 x 57; background transparent; text CareSans 16/24 400, #000000 `core.palette.ink.base`; icon 57.59 x 24, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; layers div._exterior_152ff_19 1440.0x57.0 rgb(255, 255, 255); button._reset_5zh37_19._base_5zh37_28 304.0x304.0 rgb(239, 239, 239) T:2px outset rgb(0, 0, 0) / R:2px outset rgb(0, 0, 0) / B:2px outset rgb(0, 0, 0) / L:2px outset rgb(0, 0, 0).

Child layers that carry the look: div 1440x57 background #ffffff `core.palette.paper.white`; button 304x304 background #efefef `core.palette.paper.grey` border 2px outset #000000 `core.palette.ink.base`.

![Header default](components/crops/header-default.png)

#### Promo bar
The lime announcement strip ("Peptides+ is coming soon" / "The GLP-1 pill is here") with a tertiary CTA link. Read as `promo-bar` on the hair loss page.

**Values (default).** size 1440 x 44; padding 0px 20px 5px 20px; background #bff8b1 `core.palette.lime.200`; text CareSans 15.66/20.02 600, rgba(0, 0, 0, 0.81); layers ::before rgba(0, 0, 0, 0) 0px rgb(191, 248, 177) 0px -16px 0px 0px 1; ::after rgba(0, 0, 0, 0) 0px rgb(191, 248, 177) 0px -16px 0px 0px 1.

![Promo bar default](components/crops/promo-bar-default.png)

#### Wordmark
The "hers" serif wordmark linking home; measured, never followed. Read as `logo` on the mental health page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 57.59 x 24; background transparent; text CareSans 16/24 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; decoration underline rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; icon 57.59 x 24, rgba(0, 0, 0, 0.89) `core.palette.ink.a89` |

![Wordmark default](components/crops/logo-default.png) ![Wordmark hover](components/crops/logo-hover.png) ![Wordmark focus-visible](components/crops/logo-focus-visible.png) ![Wordmark pressed](components/crops/logo-pressed.png)

#### Nav link
A category link in the nav row; measured, never followed. Read as `nav-link` on the skin care page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36.03 x 18; padding 0px 5px; background transparent; text CareSans 12/18 500, rgba(0, 0, 0, 0.65) `core.palette.ink.a65`; decoration underline transparent; transition text-decoration-color 0.3s ease-in-out, color 0.3s ease-in-out |
| hover, focus-visible, pressed | text CareSans 12/18 500, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; decoration underline rgba(0, 0, 0, 0.89) `core.palette.ink.a89` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log in control
The "Log in" button/link; measured, never pressed — its menu and the account are hydration- and auth-gated. Read as `login-button` on the mental health page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 43.59 x 24; background transparent; text CareSans 16/24 400, #0000ee; decoration underline #0000ee |
| pressed | text CareSans 16/24 400, #ff0000; decoration underline #ff0000 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Log in control default](components/crops/login-button-default.png) ![Log in control hover](components/crops/login-button-hover.png) ![Log in control pressed](components/crops/login-button-pressed.png)

#### Menu toggle
The hamburger that opens the slide menu; measured, never toggled (the drawer needs hydration). Read as `menu-toggle` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 42 x 42; border B: 2px solid transparent; radius 48px; background transparent; text CareSans 12/12 600, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; transition color 0.3s ease-out, background-color 0.3s ease-out, box-shadow 0.3s ease-out, fill 0.3s ease-out, stroke 0.3s ease-out; icon 24 x 24, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; layers ::before rgba(0, 0, 0, 0) 1px none 1; button.elements-style__ButtonReset-sc-82b26c75-0.link-style__ButtonLink-sc-67ab2a15-1 42.0x42.0 B:2px solid rgba(0, 0, 0, 0) 48px; button::before.elements-style__ButtonReset-sc-82b26c75-0.link-style__ButtonLink-sc-67ab2a15-1 autoxcalc(100% + 2px) T:1px solid rgba(0, 0, 0, 0.03) / R:1px solid rgba(0, 0, 0, 0.03) / B:1px solid rgba(0, 0, 0, 0.03) / L:1px solid r |
| hover, pressed | background rgba(0, 0, 0, 0.06) `core.palette.ink.a06`; layers ::before rgba(0, 0, 0, 0) 1px none 1 |

Child layers that carry the look: button 42x42 border 2px solid transparent radius 48px; button::before autoxcalc(100% + 2px) border 1px solid rgba(0, 0, 0, 0.03) `core.palette.ink.a03` radius 48px.

![Menu toggle default](components/crops/menu-toggle-default.png) ![Menu toggle hover](components/crops/menu-toggle-hover.png) ![Menu toggle focus-visible](components/crops/menu-toggle-focus-visible.png) ![Menu toggle pressed](components/crops/menu-toggle-pressed.png)

### Home page (marketing stack)

The signed-out landing (/): the CareSans hero headline over wide category tiles, the bento/product cards, the FDA badge, the testimonial card and the section CTA. The quiz entry tile and slide indicator paint only after hydration.

#### Hero headline
"The care you’ve always deserved" — the IvarSoft serif hero. Read as `hero-heading` on the home page.

**Values (default).** size 1392 x 114; padding 0px 16px; background transparent; text CareSans 57/57 410, rgba(0, 0, 0, 0.88).

![Hero headline default](components/crops/hero-heading-default.png)

#### Bento card
A hero bento tile (category card: headline, image, arrow); measured, never followed. Read as `bento-card` on the home page.

Selector matched the wrong element (see measure.mjs). Not republished as this component until a recapture with the scoped selector.

#### Category tile
A category entry tile ("Grow fuller hair" / "Treat menopause"); measured, never followed. Read as `tile-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 337 x 100; padding 0px 8px 0px 16px; radius 24px; background transparent; image linear-gradient(167deg, #e4eee6 `core.palette.surface.sage-300` 0%, #f2f9f4 `core.palette.surface.sage-100` 38%, #f2f9f4 `core.palette.surface.sage-100` 84%, #e4eee6 `core.palette.surface.sage-300` 10; text CareSans 19/23.69 400, #3e4f49 `core.palette.forest.500`; icon 6.45 x 12, #0000ee; layers ::before rgba(0, 0, 0, 0) 0px none 0 |
| hover | text CareSans 19/23.69 400, rgba(252, 252, 252, 0.514); layers ::before rgba(0, 0, 0, 0) 0px none 0.990969 |

![Category tile default](components/crops/tile-card-default.png) ![Category tile hover](components/crops/tile-card-hover.png)

#### Quiz entry tile
The "Unsure where to begin? Start here" quiz entry tile; measured, never followed (the quiz is a client app). Read as `quiz-tile` on the home page.

Not on the page when it was captured.

#### Product card
A GLP-1 product card in the lineup rail (image, name, drug, price, CTA). Read as `product-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 389; background transparent; text CareSans 28/31.5 460, #ffffff `core.palette.paper.white`; transition opacity 0.2s linear; opacity 0; layers a.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 320.0x389.0 24px; a::after.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 320pxx389px; div::after.wl-sidekick-style__ProductImageWrapper-sc-6d946ce3-2.iA-DSMA 64pxx8px 50% |
| hover | layers a.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 329.6x400.7 24px; a::after.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 320pxx389px; div::after.wl-sidekick-style__ProductImageWrapper-sc-6d946ce3-2.iA-DSMA 64pxx8px 50% |

Child layers that carry the look: a 320x389 image linear-gradient(#9fb089 `core.palette.sage-green.550`, #7b8967 `core.palette.sage-green.65 radius 24px; a::after 320pxx389px image linear-gradient(#7d8f66 `core.palette.sage-green.700`, #536240 `core.palette.forest.350`); div::after 64pxx8px image radial-gradient(rgba(0, 0, 0, 0.3), transparent 80%) radius 50%.

![Product card hover](components/crops/product-card-hover.png)

#### FDA badge
The "FDA-approved" badge on a product card. Read as `fda-badge` on the home page.

**Values (default).** size 56 x 56; background transparent; text CareSans 16/22.4 400, #ffffff `core.palette.paper.white`.

![FDA badge default](components/crops/fda-badge-default.png)

#### Testimonial card
A testimonial slide (quote, user photo, name) in the carousel. Read as `testimonial` on the home page.

**Values (default).** size 546 x 745.25; padding 0px 36px; background transparent; text CareSans 25/24.85 400, #b4cdc4 `core.palette.teal.200`.

![Testimonial card default](components/crops/testimonial-default.png)

#### Section CTA
A mid-page secondary CTA ("Meet the app" / "Learn more"); measured, never followed. Read as `app-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 151.48 x 48; background transparent; text CareSans 16/19.2 500, #343c2b `core.palette.forest.600`; layers button.elements-style__ButtonReset-sc-82b26c75-0.button-style__ButtonVariant-sc-de21aabe-5 151.5x48.0 rgb(197, 237, 130) T:2px solid rgba(0, 0, 0, 0) / R:2px solid rgba(0, 0, 0, 0) / B:2px solid rgba(0, 0, 0, 0) / L:2px solid rgba(0, 0, 0, 0) 48px; button::before.elements-style__ButtonReset-sc-82b26c75-0.button-style__ButtonVariant-sc-de21aabe-5 155.484pxx52px T:2px solid rgba(255, 255, 255, 0) /  |
| hover | layers button.elements-style__ButtonReset-sc-82b26c75-0.button-style__ButtonVariant-sc-de21aabe-5 151.5x48.0 rgb(157, 189, 103) T:2px solid rgba(0, 0, 0, 0) / R:2px solid rgba(0, 0, 0, 0) / B:2px solid rgba(0, 0, 0, 0) / L:2px solid rgba(0, 0, 0, 0) 48px; button::before.elements-style__ButtonReset-sc-82b26c75-0.button-style__ButtonVariant-sc-de21aabe-5 155.484pxx52px T:2px solid rgba(255, 255, 255, 0) /  |

Child layers that carry the look: button 151.5x48 background #c5ed82 `core.palette.lime.450` border 2px solid transparent radius 48px; button::before 155.484pxx52px border 2px solid rgba(255, 255, 255, 0) radius 48px.

![Section CTA hover](components/crops/app-cta-hover.png) ![Section CTA focus-visible](components/crops/app-cta-focus-visible.png) ![Section CTA pressed](components/crops/app-cta-pressed.png)

### Shop pages (weight-loss, hair, skin, mental-health, birth-control, product, labs, benefits)

The category storefronts and product detail pages (/weight-loss, /hair-loss, /skin-care, /mental-health, /birth-control, /hair-loss/minoxidil-biotin-chew, /skin-care/anti-aging, /weight-loss/wegovy-pill, /labs, /benefits): the CareSans page heading (about 53px at 1440), treatment/product cards with prices, the CTA trio, content cards, the accordion, carousel controls, disclaimers and 'Read more' toggles.

#### Page heading
The serif section heading ("Weight loss that works" / "Lose weight the way you want"). Read as `page-heading` on the mental health page.

**Values (default).** size 781.08 x 52.83; background transparent; text CareSans 52.83/52.83 410, rgba(0, 0, 0, 0.81).

![Page heading default](components/crops/page-heading-default.png)

#### Section dek
The body copy beside the section heading. Read as `page-dek` on the mental health page.

**Values (default).** size 557.92 x 46.31; background transparent; text CareSans 18.5/23.15 400, rgba(0, 0, 0, 0.5) `core.palette.ink.a50`; layers em.options_marks_with-gradient__yWDlC.options_marks_reset__pynUw 516.3x44.2.

Child layers that carry the look: em 516.3x44.2 image linear-gradient(135deg, #5d62c8 `core.palette.accent.violet` -0.03%, #5e91d6 `core.palette.

![Section dek default](components/crops/page-dek-default.png)

#### Primary CTA
The dark-green pill primary action ("Start losing weight" / "Go to membership"); measured, never followed. Read as `cta-primary` on the mental health page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 173.41 x 17; background transparent; text CareSans 16/24 400, #0000ee; decoration underline #0000ee |
| focus-visible | outline 1px auto #101010 `light.focus.ring`, offset 1px; layers a._reset_5zh37_19._base_5zh37_28 173.4x17.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text CareSans 16/24 400, #ff0000; decoration underline #ff0000 |

![Primary CTA default](components/crops/cta-primary-default.png) ![Primary CTA hover](components/crops/cta-primary-hover.png) ![Primary CTA focus-visible](components/crops/cta-primary-focus-visible.png) ![Primary CTA pressed](components/crops/cta-primary-pressed.png)

#### Secondary CTA
The outlined secondary action ("Get started"); measured, never followed. Read as `cta-secondary` on the skin care page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 388 x 48; padding 8px 24px; border 1px solid rgba(0, 0, 0, 0.19); radius 9999px; background rgba(255, 255, 255, 0.01); outline 1px solid transparent, offset 0px; text CareSans 16/24 600, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; transition border-color 0.2s ease-in-out, color 0.2s ease-in-out, background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, outline-offset 0.2s ease-in-out, outline-color 0.2s ease-in-out, text-decoration-color 0.2s ease-in-out |
| hover | border 1px solid transparent; background rgba(0, 0, 0, 0.65) `core.palette.ink.a65`; text CareSans 16/24 600, #ffffff `core.palette.paper.white` |
| focus-visible | border 1px solid transparent; background rgba(0, 0, 0, 0.65) `core.palette.ink.a65`; outline 1px solid transparent, offset 3px; text CareSans 16/24 600, #ffffff `core.palette.paper.white` |
| pressed | border 1px solid transparent; background rgba(0, 0, 0, 0.74) `core.palette.ink.a74`; text CareSans 16/24 600, #ffffff `core.palette.paper.white` |

![Secondary CTA default](components/crops/cta-secondary-default.png) ![Secondary CTA hover](components/crops/cta-secondary-hover.png) ![Secondary CTA focus-visible](components/crops/cta-secondary-focus-visible.png)

#### Tertiary CTA
The quiet tertiary action ("View details"); measured, never followed. Read as `cta-tertiary` on the skin care page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 188.67 x 48; padding 8px 24px; border 1px solid transparent; radius 9999px; background rgba(0, 0, 0, 0.06) `core.palette.ink.a06`; outline 1px solid transparent, offset 0px; text CareSans 16/24 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; transition border-color 0.2s ease-in-out, color 0.2s ease-in-out, background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, outline-offset 0.2s ease-in-out, outline-color 0.2s ease-in-out, text-decoration-color 0.2s ease-in-out |
| hover | background rgba(0, 0, 0, 0.65) `core.palette.ink.a65`; text CareSans 16/24 400, #ffffff `core.palette.paper.white` |
| focus-visible | background rgba(0, 0, 0, 0.65) `core.palette.ink.a65`; outline 1px solid transparent, offset 3px; text CareSans 16/24 400, #ffffff `core.palette.paper.white` |
| pressed | background rgba(0, 0, 0, 0.74) `core.palette.ink.a74`; text CareSans 16/24 400, #ffffff `core.palette.paper.white` |

![Tertiary CTA hover](components/crops/cta-tertiary-hover.png) ![Tertiary CTA focus-visible](components/crops/cta-tertiary-focus-visible.png) ![Tertiary CTA pressed](components/crops/cta-tertiary-pressed.png)

#### Underlined link
The underlined "Important safety information" action; measured, never followed. Read as `cta-underlined` on the mental health page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 198.31 x 17; background transparent; text CareSans 16/24 400, #0000ee; decoration underline #0000ee |
| focus-visible | outline 1px auto #101010 `light.focus.ring`, offset 1px; layers a._reset_5zh37_19._base_5zh37_28 198.3x17.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text CareSans 16/24 400, #ff0000; decoration underline #ff0000 |

![Underlined link default](components/crops/cta-underlined-default.png) ![Underlined link hover](components/crops/cta-underlined-hover.png) ![Underlined link focus-visible](components/crops/cta-underlined-focus-visible.png) ![Underlined link pressed](components/crops/cta-underlined-pressed.png)

#### Content card
A rounded media-first content card in the rails (gradient surface, image, heading, CTA stack). Read as `content-card` on the mental health page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 438 x 584; padding 25px; radius 16px; background transparent; text CareSans 26.66/30.22 500, rgba(0, 0, 0, 0.81) |

![Content card default](components/crops/content-card-default.png) ![Content card hover](components/crops/content-card-hover.png)

#### Treatment card
A medication treatment card (name, drug, price "From $149/mo", CTA stack). Read as `treatment-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 389; background transparent; text CareSans 28/31.5 460, #ffffff `core.palette.paper.white`; transition opacity 0.2s linear; opacity 0; layers a.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 320.0x389.0 24px; a::after.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 320pxx389px; div::after.wl-sidekick-style__ProductImageWrapper-sc-6d946ce3-2.iA-DSMA 64pxx8px 50% |
| hover | layers a.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 329.6x400.7 24px; a::after.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 320pxx389px; div::after.wl-sidekick-style__ProductImageWrapper-sc-6d946ce3-2.iA-DSMA 64pxx8px 50% |

Child layers that carry the look: a 320x389 image linear-gradient(#9fb089 `core.palette.sage-green.550`, #7b8967 `core.palette.sage-green.65 radius 24px; a::after 320pxx389px image linear-gradient(#7d8f66 `core.palette.sage-green.700`, #536240 `core.palette.forest.350`); div::after 64pxx8px image radial-gradient(rgba(0, 0, 0, 0.3), transparent 80%) radius 50%.

![Treatment card default](components/crops/treatment-card-default.png) ![Treatment card hover](components/crops/treatment-card-hover.png)

#### Price line
The "From $149/mo †" price line on a treatment/product card. Read as `card-price` on the home page.

Selector matched the wrong element (see measure.mjs). Not republished as this component until a recapture with the scoped selector.

#### Accordion
The FAQ accordion block; the first panel ships open in SSR, toggles need hydration. Read as `accordion` on the mental health page.

**Values (default).** size 616 x 325; background transparent; text CareSans 15.66/18.83 500, rgba(0, 0, 0, 0.81); layers div::before._accordion-icon_1wnp5_28 10.5pxx2px rgba(0, 0, 0, 0.88) 4px 0px 0px 4px; div::after._accordion-icon_1wnp5_28 10.5pxx2px rgba(0, 0, 0, 0.88) 0px 4px 4px 0px; div._visibility-precluded_1wnp5_147._content_1wnp5_94 616.0x1.0 B:1px solid rgba(0, 0, 0, 0.12); div::before._accordion-icon_1wnp5_28 10.5pxx2px rgba(0, 0, 0, 0.88) 4px 0px 0px 4px; div::after._accordion-icon_1wnp5_28 10.5pxx2px rg.

Child layers that carry the look: div::before 10.5pxx2px background rgba(0, 0, 0, 0.88) radius 4px 0px 0px 4px; div::after 10.5pxx2px background rgba(0, 0, 0, 0.88) radius 0px 4px 4px 0px; div 616x1 border 1px solid rgba(0, 0, 0, 0.12) `core.palette.ink.a12`.

![Accordion default](components/crops/accordion-default.png)

#### Accordion toggle
An accordion row toggle (title + icon); measured, never toggled. Read as `accordion-toggle` on the mental health page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 575 x 18.83; background transparent; text CareSans 15.66/18.83 500, rgba(0, 0, 0, 0.81) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Accordion toggle default](components/crops/accordion-toggle-default.png) ![Accordion toggle hover](components/crops/accordion-toggle-hover.png) ![Accordion toggle pressed](components/crops/accordion-toggle-pressed.png)

#### Disclaimer
The collapsed legal disclaimer block (grey text, expandable). Read as `disclaimer` on the mental health page.

**Values (default).** size 800.86 x 40.06; background transparent; text CareSans 15.66/20.02 600, rgba(0, 0, 0, 0.81).

![Disclaimer default](components/crops/disclaimer-default.png)

#### Read more toggle
The "Read more" disclaimer toggle; measured, never toggled. Read as `read-more` on the weight loss page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 66.72 x 15.66; background transparent; text CareSans 12.83/15.65 600, rgba(0, 0, 0, 0.37) `core.palette.ink.a37` |
| hover | decoration underline rgba(0, 0, 0, 0.37) `core.palette.ink.a37` |
| focus-visible | outline 1px auto #101010 `light.focus.ring`, offset 0px; decoration underline rgba(0, 0, 0, 0.37) `core.palette.ink.a37`; layers button.ReadMore_button__B36Ye 66.7x15.7 1px auto rgb(16, 16, 16) offset 0px |
| pressed | decoration underline rgba(0, 0, 0, 0.37) `core.palette.ink.a37` |

![Read more toggle hover](components/crops/read-more-hover.png) ![Read more toggle focus-visible](components/crops/read-more-focus-visible.png) ![Read more toggle pressed](components/crops/read-more-pressed.png)

#### Carousel arrow
A carousel next/previous control; measured, never pressed. Read as `carousel-arrow` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 48 x 48; padding 1px 6px; border 2px solid rgba(255, 255, 255, 0.11); radius 100%; background transparent; text CareSans 16/18.4 400, rgba(255, 255, 255, 0.11); transition color 0.3s ease-in-out, border-color 0.3s ease-in-out; transform translate(0px, -24px); icon 24 x 24, rgba(255, 255, 255, 0.11) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Carousel arrow default](components/crops/carousel-arrow-default.png) ![Carousel arrow hover](components/crops/carousel-arrow-hover.png) ![Carousel arrow pressed](components/crops/carousel-arrow-pressed.png)

#### Slide indicator
A carousel position dot; measured, never pressed. Read as `slide-dot` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 60 x 12; background transparent; text CareSans 16/22.4 400, #ffffff `core.palette.paper.white`; transition transform 0.3s ease; layers span.testimonial-card-style__SlideIndicatorDot-sc-179bb82b-15.dDiWwq 12.0x12.0 rgb(255, 255, 255) 100%; span.testimonial-card-style__SlideIndicatorDot-sc-179bb82b-15.dDiWwq 10.0x10.0 rgba(255, 255, 255, 0.1) 100%; span.testimonial-card-style__SlideIndicatorDot-sc-179bb82b-15.dDiWwq 10.0x10.0 rgba(255, 255, 255, 0.1) 100%; span.testimonial-card-style__SlideIndicatorDot-sc-179bb82b-15.dDiWwq 8.0x8.0 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: span 12x12 background #ffffff `core.palette.paper.white` radius 100%; span 10x10 background rgba(255, 255, 255, 0.1) radius 100%; span 10x10 background rgba(255, 255, 255, 0.1) radius 100%.

![Slide indicator default](components/crops/slide-dot-default.png) ![Slide indicator hover](components/crops/slide-dot-hover.png) ![Slide indicator pressed](components/crops/slide-dot-pressed.png)

### Content pages (blog, article, quality, drugs-info)

The editorial surfaces (/blog, a blog article, /quality-and-safety, /drugs/info): article cards and topic chips on the index, the article title/byline/prose roles, the A-Z chips and drug index links, and the regional-redirect card measured as the dialog it is (then hidden).

#### Article card
An article card on the blog index; measured, never followed. Read as `article-card` on the blog index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 691.89 x 389.19; background transparent; text sofia-pro 16/22.4 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; layers div.sc-46d8ac7e-2.emlLAx 691.9x389.2 rgba(0, 0, 0, 0.06) |
| hover | layers div.sc-46d8ac7e-2.emlLAx 705.7x397.0 rgba(0, 0, 0, 0.06) |

Child layers that carry the look: div 691.9x389.2 background rgba(0, 0, 0, 0.06) `core.palette.ink.a06`.

![Article card default](components/crops/article-card-default.png) ![Article card hover](components/crops/article-card-hover.png)

#### Topic link
A blog topic/category link; measured, never followed. Read as `blog-topic` on the blog index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 139 x 64; padding 0px 32px; radius 100px; background rgba(0, 0, 0, 0.06) `core.palette.ink.a06`; text sofia-pro 14/19.6 500, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; transition background 0.2s ease-in-out, color 0.2s ease-in-out, transform 0.2s ease-in-out |
| hover, focus-visible | background rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; text sofia-pro 14/19.6 500, #ffffff `core.palette.paper.white` |
| pressed | size 132.05 x 60.8; background rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; text sofia-pro 14/19.6 500, #ffffff `core.palette.paper.white`; transform scale(0.95) |

![Topic link default](components/crops/blog-topic-default.png) ![Topic link hover](components/crops/blog-topic-hover.png) ![Topic link focus-visible](components/crops/blog-topic-focus-visible.png) ![Topic link pressed](components/crops/blog-topic-pressed.png)

#### Regional redirect card
The "It looks like you’re visiting from Canada" redirect card, the one dialog the signed-out SSR paints. Its CTA was measured, never followed; the card was hidden, never answered. Read as `region-dialog` on the drug information index page.

**Values (default).** size 388 x 234.39; border 1px solid rgba(0, 0, 0, 0.06) `core.palette.ink.a06`; radius 16px; background #ffffff `core.palette.paper.white`; shadow rgba(0, 0, 0, 0.08) 0px 20px 40px 0px; text sofia-pro 24/32 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; icon 16 x 16, #000000 `core.palette.ink.base`.

![Regional redirect card default](components/crops/region-dialog-default.png)

#### Redirect CTA
The "Go to forhers.ca" pill button inside the redirect card; measured, never followed. Read as `region-cta` on the drug information index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 338 x 48.39; padding 12px 24px; border 1px solid rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; radius 9999px; background transparent; text sofia-pro 16/22.4 500, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; icon 16 x 16, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; ancestors div.regional-redirect-popupstyle__RegionalRedirectPopupWrapper-web-components__sc-o05fs-0.dVvNUF bg #ffffff `core.palette.paper.white` shadow rgba(0, 0, 0, 0.08) 0px 20px 40px 0px |
| hover | opacity 0.85 |
| focus-visible | outline 1px auto #101010 `light.focus.ring`, offset 1px; opacity 0.85 |
| pressed | opacity 0.85 |

![Redirect CTA default](components/crops/region-cta-default.png) ![Redirect CTA hover](components/crops/region-cta-hover.png) ![Redirect CTA focus-visible](components/crops/region-cta-focus-visible.png) ![Redirect CTA pressed](components/crops/region-cta-pressed.png)

#### Article title
The article H1. Read as `article-title` on the blog article page.

**Values (default).** size 648.5 x 130.19; background transparent; text sofia-pro 62/65.1 500, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`.

![Article title default](components/crops/article-title-default.png)

#### Body paragraph
A body paragraph in the article prose. Read as `prose-p` on the blog article page.

Selector matched the wrong element (see measure.mjs). Not republished as this component until a recapture with the scoped selector.

#### Section heading
An in-article section heading. Read as `prose-h2` on the blog article page.

Not on the page when it was captured.

#### Inline link
An inline link inside the article body; measured, never followed. Read as `prose-link` on the blog article page.

Not on the page when it was captured.

#### List item
A list item in the article body. Read as `prose-list` on the blog article page.

**Values (default).** size 0 x 0; background transparent; text sofia-pro 16/24.88 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Byline block
The author/reviewer byline under the title. Read as `byline` on the blog article page.

**Values (default).** size 648.5 x 60; background transparent; text sofia-pro 12/20 500, rgba(0, 0, 0, 0.44) `core.palette.ink.a44`.

![Byline block default](components/crops/byline-default.png)

#### Heading
A heading on the quality/safety page. Read as `prose-h` on the quality and safety page.

**Values (default).** size 694 x 69.44; background transparent; text sofia-pro 12/12 500, #ffffff `core.palette.paper.white`; layers span.cactus-typography-component__TypographyBase-sc-22492af4-0.bgiBTD 147.8x24.0 rgb(51, 133, 133) 46px.

Child layers that carry the look: span 147.8x24 background #338585 `core.palette.teal.700` radius 46px.

![Heading default](components/crops/prose-h-default.png)

#### Body text
A body paragraph. Read as `prose-body` on the quality and safety page.

**Values (default).** size 752 x 168; background transparent; text sofia-pro 20/28 400, rgba(0, 0, 0, 0.65) `core.palette.ink.a65`.

![Body text default](components/crops/prose-body-default.png)

#### A-Z chip
A grey circular letter chip in "Browse A-Z"; measured, never followed. Read as `az-chip` on the drug information index page.

Not on the page when it was captured.

#### Drug link
A medication link in the "Popular Medications" list; measured, never followed. Read as `drug-link` on the drug information index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 455 x 37.34; background transparent; text sofia-pro 29/37.35 400, #0077ab `core.palette.accent.link` |
| hover | decoration underline #0077ab `core.palette.accent.link` 2px |
| focus-visible | outline 1px auto #101010 `light.focus.ring`, offset 1px; layers a.sc-7735162f-0.hbdJaM 455.0x37.3 1px auto rgb(16, 16, 16) offset 1px |
| pressed | decoration underline #0077ab `core.palette.accent.link` 2px |

![Drug link default](components/crops/drug-link-default.png) ![Drug link hover](components/crops/drug-link-hover.png) ![Drug link focus-visible](components/crops/drug-link-focus-visible.png) ![Drug link pressed](components/crops/drug-link-pressed.png)

#### Page lede
The page heading/dek block. Read as `page-lede` on the drug information index page.

**Values (default).** size 964 x 83.75; background transparent; text sofia-pro 87/83.75 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; layers span 422.5x112.0.

Child layers that carry the look: span 422.5x112 image linear-gradient(135deg, #5d62c8 `core.palette.accent.violet` -0.03%, #5e91d6 `core.palette.

![Page lede default](components/crops/page-lede-default.png)

#### Topic link
A topic link in the drugs index sub-nav (All / Weight Loss / …). Read as `topic-tab` on the drug information index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85 x 18; border B: 2px solid transparent; background transparent; text sofia-pro 16/16 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; transition all 0.1s ease-in; layers a.sc-4263aab9-2.dUetuz 85.0x18.0 B:2px solid rgba(0, 0, 0, 0) |
| hover | border B: 2px solid rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; layers a.sc-4263aab9-2.dUetuz 85.0x18.0 B:2px solid rgba(0, 0, 0, 0.89) |
| focus-visible | border B: 2px solid #000000 `core.palette.ink.base`; outline 1px auto #101010 `light.focus.ring`, offset 1px; layers a.sc-4263aab9-2.dUetuz 85.0x18.0 B:2px solid rgb(0, 0, 0) 1px auto rgb(16, 16, 16) offset 1px |
| pressed | border B: 2px solid rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; layers a.sc-4263aab9-2.dUetuz 85.0x18.0 B:2px solid rgba(0, 0, 0, 0.89) |

Child layers that carry the look: a 85x18 border 2px solid transparent.

![Topic link default](components/crops/topic-tab-default.png) ![Topic link hover](components/crops/topic-tab-hover.png) ![Topic link focus-visible](components/crops/topic-tab-focus-visible.png) ![Topic link pressed](components/crops/topic-tab-pressed.png)

### Forms and tools (bmi-calculator, lead capture)

The BMI calculator (/tools/bmi-calculator): the number fields, the email field, the #b6dd64 lime Calculate submit, the painted disabled button, the result dial, the lead-capture block and the privacy disclosure. Fields were typed into and cleared; nothing was submitted.

#### BMI form
The calculator form: height feet/inches and weight number fields plus the submit. Read as `bmi-form` on the BMI calculator page.

**Values (default).** size 652.5 x 273.19; background transparent; text sofia-pro 14/19.6 500, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; layers div.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy 318.3x56.0 rgb(255, 255, 255) T:1px solid rgba(0, 0, 0, 0.19) / R:1px solid rgba(0, 0, 0, 0.19) / B:1px solid rgba(0, 0, 0, 0.19) / L:1px solid rgba(0, 0, 0, 0.19) 12px; div::before.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy 316.25pxx54px T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / .

Child layers that carry the look: div 318.3x56 background #ffffff `core.palette.paper.white` border 1px solid rgba(0, 0, 0, 0.19) radius 12px; div::before 316.25pxx54px border 1px solid transparent radius 11px; div 318.3x56 background #ffffff `core.palette.paper.white` border 1px solid rgba(0, 0, 0, 0.19) radius 12px.

![BMI form default](components/crops/bmi-form-default.png)

#### Number field
A labelled number input ("feet"/"inches"/"pounds"); focused and typed into then cleared — never submitted. Read as `text-field` on the BMI calculator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 316.25 x 54; padding 18px 15px 0px 15px; radius 11px; background transparent; text sofia-pro 14/16.1 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; transition color 0.2s cubic-bezier(0.33, 0, 0, 1), background-color 0.2s cubic-bezier(0.33, 0, 0, 1); placeholder rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; ancestors div.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy bg #ffffff `core.palette.paper.white` |

![Number field default](components/crops/text-field-default.png) ![Number field focused](components/crops/text-field-focused.png) ![Number field filled](components/crops/text-field-filled.png)

#### Email field
The lead-capture email input; focused and typed into then cleared — never submitted. Read as `email-field` on the BMI calculator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 358 x 62; padding 18px 15px 0px 15px; radius 11px; background transparent; text sofia-pro 16/18.4 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; transition color 0.2s cubic-bezier(0.33, 0, 0, 1), background-color 0.2s cubic-bezier(0.33, 0, 0, 1); placeholder rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; ancestors div.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy bg #ffffff `core.palette.paper.white` |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png) ![Email field filled](components/crops/email-field-filled.png)

#### Form submit
The form's dark pill submit; measured, never pressed. Read as `form-submit` on the BMI calculator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 652.5 x 48; padding 0px 24px; border 2px solid rgba(255, 255, 255, 0); radius 48px; background #b6dd64 `core.palette.lime.550`; text sofia-pro 14/normal 500, #000000 `core.palette.ink.base`; transition color 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease, fill 0.3s ease, stroke 0.3s ease, backdrop-filter 0.3s ease, border-color 0.3s ease; layers ::before rgba(0, 0, 0, 0) 2px none 1 |
| hover | background #d5ff5d `core.palette.lime.400` |
| focus-visible | background rgba(0, 0, 0, 0.54) `core.palette.ink.a54` |
| pressed | background #d5ff5d `core.palette.lime.400` |

![Form submit default](components/crops/form-submit-default.png) ![Form submit hover](components/crops/form-submit-hover.png) ![Form submit focus-visible](components/crops/form-submit-focus-visible.png) ![Form submit pressed](components/crops/form-submit-pressed.png)

#### Disabled button
A disabled pagination/option button in the tool (resting disabled state, SSR). Read as `disabled-button` on the BMI calculator page.

**Values (default).** size 48 x 48; padding 1px 6px; radius 100%; background rgba(0, 0, 0, 0.06) `core.palette.ink.a06`; text sofia-pro 16/18.4 400, rgba(16, 16, 16, 0.3) `core.palette.ink.a30`; transition background 0.2s cubic-bezier(0.28, 0.13, 0.38, 1), box-shadow 0.2s cubic-bezier(0.28, 0.13, 0.38, 1), transform 0.2s cubic-bezier(0.28, 0.13, 0.38, 1); icon 24 x 24, rgba(16, 16, 16, 0.3) `core.palette.ink.a30`.

![Disabled button default](components/crops/disabled-button-default.png)

#### BMI dial
The result dial gauge beside the form. Read as `bmi-dial` on the BMI calculator page.

**Values (default).** size 652.5 x 615.56; background transparent; text sofia-pro 16/22.4 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; layers div.bmi-dialstyle__BmiDialWrapper-web-components__sc-19w4ur4-1.exnzvJ 652.5x615.6 rgb(49, 54, 49) T:4px solid rgb(176, 213, 99) / R:4px solid rgb(176, 213, 99) / B:4px solid rgb(176, 213, 99) / L:4px solid rgb(176, 213, 99) 32px; div.bmi-tablestyle__RowContainer-web-components__sc-1xbn2ud-3.gFWFul 380.0x55.4 B:1px solid rgb(255, 255, 255); div.bmi-tablestyle__RowContainer-web-components__sc-1xbn2u; ancestors div.bmi-calculatorstyle__BmiCalculatorWrapper-web-components__sc-1s5qk2f-1.dZpUFx bg #ffffff `core.palette.paper.white`.

Child layers that carry the look: div 652.5x615.6 background #313631 `core.palette.forest.650` border 4px solid #b0d563 `core.palette.lime.600` radius 32px; div 380x55.4 border 1px solid #ffffff `core.palette.paper.white`; div 380x55.4 border 1px solid #ffffff `core.palette.paper.white`.

![BMI dial default](components/crops/bmi-dial-default.png)

#### Lead capture block
The email sign-up block (input + submit + privacy disclosure). Read as `lead-capture` on the BMI calculator page.

**Values (default).** size 480 x 466.39; background transparent; text sofia-pro 62/65.1 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; layers div.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy 360.0x64.0 rgb(255, 255, 255) T:1px solid rgba(0, 0, 0, 0.19) / R:1px solid rgba(0, 0, 0, 0.19) / B:1px solid rgba(0, 0, 0, 0.19) / L:1px solid rgba(0, 0, 0, 0.19) 12px; div::before.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy 358pxx62px T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1.

Child layers that carry the look: div 360x64 background #ffffff `core.palette.paper.white` border 1px solid rgba(0, 0, 0, 0.19) radius 12px; div::before 358pxx62px border 1px solid transparent radius 11px; button 100x48 background #000000 `core.palette.ink.base` border 2px solid rgba(255, 255, 255, 0) radius 48px.

![Lead capture block default](components/crops/lead-capture-default.png)

#### Privacy disclosure
The fine-print privacy disclosure under the lead capture. Read as `privacy-note` on the BMI calculator page.

**Values (default).** size 480 x 31.91; background transparent; text sofia-pro 12/15.96 400, rgba(0, 0, 0, 0.65) `core.palette.ink.a65`; layers a.linkstyle__BlogLink-web-components__sc-kz1v8b-3.linkstyle__UnderlinedBlogLink-web-components__sc-kz1v8b-4 106.0x17.0 B:2px solid rgba(0, 0, 0, 0); a.linkstyle__BlogLink-web-components__sc-kz1v8b-3.linkstyle__UnderlinedBlogLink-web-components__sc-kz1v8b-4 74.0x17.0 B:2px solid rgba(0, 0, 0, 0).

Child layers that carry the look: a 106x17 border 2px solid transparent; a 74x17 border 2px solid transparent.

![Privacy disclosure default](components/crops/privacy-note-default.png)

### Footer

The site footer: the 'visit hims.com' cross-promo, section columns of links, the social icon wells and the fineprint/legal line.

#### Footer
The site footer: link columns, social icons, legal fineprint row. Read as `footer` on the mental health page.

**Values (default).** size 1440 x 1774.95; padding 90px 60px 60px 60px; background #f0f0f0 `core.palette.paper.wash`; text CareSans 12.83/15.65 490.75, rgba(0, 0, 0, 0.65) `core.palette.ink.a65`; icon 10 x 12, rgba(0, 0, 0, 0.65) `core.palette.ink.a65`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer column link; measured, never followed. Read as `footer-link` on the mental health page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 113.8 x 15; background transparent; text CareSans 12.83/16.74 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89` |
| hover, focus-visible, pressed | decoration underline rgba(0, 0, 0, 0.89) `core.palette.ink.a89` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Fineprint link
A legal fineprint link in the footer's last row; measured, never followed. Read as `footer-fineprint` on the mental health page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 227.75 x 15; background transparent; text CareSans 12.83/16.74 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89` |
| hover, focus-visible, pressed | decoration underline rgba(0, 0, 0, 0.89) `core.palette.ink.a89` |

![Fineprint link default](components/crops/footer-fineprint-default.png) ![Fineprint link hover](components/crops/footer-fineprint-hover.png) ![Fineprint link focus-visible](components/crops/footer-fineprint-focus-visible.png) ![Fineprint link pressed](components/crops/footer-fineprint-pressed.png)

#### Social icon link
A social icon link in the footer; measured, never followed. Read as `footer-social` on the mental health page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 20 x 20; padding 0px 5px; radius 100%; background transparent; text CareSans 12/18 500, rgba(0, 0, 0, 0.65) `core.palette.ink.a65`; decoration underline transparent; transition background-color 0.3s ease-in-out; icon 10 x 12, rgba(0, 0, 0, 0.65) `core.palette.ink.a65` |
| hover, focus-visible, pressed | background rgba(0, 0, 0, 0.06) `core.palette.ink.a06`; text CareSans 12/18 500, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; decoration underline rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; icon 10 x 12, rgba(0, 0, 0, 0.89) `core.palette.ink.a89` |

![Social icon link default](components/crops/footer-social-default.png) ![Social icon link hover](components/crops/footer-social-hover.png) ![Social icon link focus-visible](components/crops/footer-social-focus-visible.png) ![Social icon link pressed](components/crops/footer-social-pressed.png)

### Mobile (390 wide)

The pages at phone width (390 x 844 at 2x): the mobile header and wordmark, the bento and content cards re-stacked, the black 9999px pill primary CTA and the mobile field.

#### Mobile header
The top chrome at 390: promo bar, wordmark, hamburger (the slide menu needs hydration). Read as `m-header` on the blog article page at 390 wide.

**Values (default).** size 390 x 785; background transparent; text sofia-pro 16/16 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; transition transform 0.3s ease; icon 51 x 20, #0000ee; layers div.global-navigation-headerstyle__GlobalNavigationBackground-navigation__sc-o5ejvm-1.dDoiyQ 390.0x98.0 rgb(255, 255, 255) 16px 16px 0px 0px; a.sc-4263aab9-2.dUetuz 18.0x18.0 B:2px solid rgba(0, 0, 0, 0); a.sc-4263aab9-2.dUetuz 85.0x18.0 B:2px solid rgba(0, 0, 0, 0); a.sc-4263aab9-2.dUetuz 87.0x18.0 B:2px solid rgba(0, 0, 0, 0); a.sc-4263aab9-2.dUetuz 104.0x18.0 B:2px solid rgba(0, 0, 0, 0); a.sc-.

Child layers that carry the look: div 390x98 background #ffffff `core.palette.paper.white` radius 16px 16px 0px 0px; a 18x18 border 2px solid transparent; a 85x18 border 2px solid transparent.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu toggle
The hamburger at phone width; measured, never toggled. Read as `m-menu-toggle` on the blog article page at 390 wide.

**Values (default).** size 48 x 48; border B: 2px solid transparent; radius 48px; background transparent; text sofia-pro 10/10 600, #000000 `core.palette.ink.base`; transition color 0.3s ease-out, background-color 0.3s ease-out, box-shadow 0.3s ease-out, fill 0.3s ease-out, stroke 0.3s ease-out; icon 24 x 24, #000000 `core.palette.ink.base`; layers ::before rgba(0, 0, 0, 0) 1px none 1; button.elementsstyle__ButtonReset-web-components__sc-u730hl-0.linkstyle__ButtonLink-web-components__sc-kz1v8b-1 48.0x48.0 B:2px solid rgba(0, 0, 0, 0) 48px; button::before.elementsstyle__ButtonReset-web-components__sc-u730hl-0.linkstyle__ButtonLink-web-components__sc-kz1v8b-1 autoxcalc(100% + 2px) T:1px solid rgba(0, 0, 0, 0.03) / R:1px solid rgba(0, 0, 0, 0.0.

Child layers that carry the look: button 48x48 border 2px solid transparent radius 48px; button::before autoxcalc(100% + 2px) border 1px solid rgba(0, 0, 0, 0.03) `core.palette.ink.a03` radius 48px.

![Mobile menu toggle default](components/crops/m-menu-toggle-default.png)

#### Mobile wordmark
The "hers" wordmark at phone width. Read as `m-logo` on the product detail page at 390 wide.

**Values (default).** size 57.59 x 24; background transparent; text CareSans 16/24 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; decoration underline rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; icon 57.59 x 24, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`.

![Mobile wordmark default](components/crops/m-logo-default.png)

#### Mobile bento card
A bento tile at phone width. Read as `m-bento-card` on the home page at 390 wide.

**Values (default).** size 374 x 400; padding 20px; background transparent; text CareSans 20/23.5 480, #ffffff `core.palette.paper.white`; layers button.elements-style__ButtonReset-sc-82b26c75-0.button-style__ButtonVariant-sc-de21aabe-5 128.5x44.0 rgba(255, 255, 255, 0.17) T:2px solid rgba(255, 255, 255, 0) / R:2px solid rgba(255, 255, 255, 0) / B:2px solid rgba(255, 255, 255, 0) / L:2px solid rgba(255, 255, 255, 0) 48px; button::before.elements-style__ButtonReset-sc-82b26c75-0.button-style__ButtonVariant-sc-de21aabe-5 132.484pxx48px T:2px ; ancestors div.stacked-cta-card-style__Frame-sc-142aa7a5-0.kOucQG bg rgba(0, 0, 0, 0.12) `core.palette.ink.a12`.

Child layers that carry the look: button 128.5x44 background rgba(255, 255, 255, 0.17) border 2px solid rgba(255, 255, 255, 0) radius 48px; button::before 132.484pxx48px border 2px solid transparent radius 48px.

![Mobile bento card default](components/crops/m-bento-card-default.png)

#### Mobile primary CTA
The primary pill action at phone width. Read as `m-cta-primary` on the product detail page at 390 wide.

**Values (default).** size 346 x 48; padding 8px 24px; border 1px solid transparent; radius 9999px; background #000000 `core.palette.ink.base`; outline 1px solid transparent, offset 0px; text CareSans 16/24 400, #ffffff `core.palette.paper.white`; transition border-color 0.2s ease-in-out, color 0.2s ease-in-out, background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, outline-offset 0.2s ease-in-out, outline-color 0.2s ease-in-out, text-decoration-color 0.2s ease-in-out.

![Mobile primary CTA default](components/crops/m-cta-primary-default.png)

#### Mobile content card
A content card at phone width. Read as `m-content-card` on the product detail page at 390 wide.

**Values (default).** size 346 x 63.48; background transparent; text CareSans 18/21.37 500, rgba(0, 0, 0, 0.81).

![Mobile content card default](components/crops/m-content-card-default.png)

#### Mobile number field
The number input at phone width. Read as `m-text-field` on the BMI calculator page at 390 wide.

**Values (default).** size 161.5 x 54; padding 18px 15px 0px 15px; radius 11px; background transparent; text sofia-pro 16/18.4 400, rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; transition color 0.2s cubic-bezier(0.33, 0, 0, 1), background-color 0.2s cubic-bezier(0.33, 0, 0, 1); placeholder rgba(0, 0, 0, 0.89) `core.palette.ink.a89`; ancestors div.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy bg #ffffff `core.palette.paper.white`.

![Mobile number field default](components/crops/m-text-field-default.png)

## Icons

46 distinct SVGs were lifted from the archived pages (the wordmark, social glyphs, chevrons, the carousel arrow, the close glyph and the 'visit hims.com' lockups), deduplicated by content hash into [icons/](icons) and indexed in [icons/INDEX.tsv](icons/INDEX.tsv). Names are inferred from the element's accessible label or class; the 'hims-on-*' social glyphs live in the footer's 'visit hims.com' cross-promo, the 'hers-on-*' glyphs are the hers socials.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [visit-hims-com](icons/visit-hims-com-1a3c65a1.svg) | 20x24 21x24 | 0 0 19 22 | stroke | weight-loss; hair-loss; skin-care; mental-health; birth-control; product; wegovy-pill; labs; benefits | visit hims.com |
| [hims-on-facebook](icons/hims-on-facebook.svg) | 20x48 | 0 0 155 155 | fill | weight-loss; hair-loss; skin-care; mental-health; product; wegovy-pill; labs; benefits | Hims on Facebook |
| [hims-on-tiktok](icons/hims-on-tiktok.svg) | 20x48 | 0 0 24 24 | fill | weight-loss; hair-loss; skin-care; mental-health; product; wegovy-pill; labs; benefits | Hims on TikTok |
| [hims-on-twitter](icons/hims-on-twitter.svg) | 20x48 | 0 0 20 20 | fill | weight-loss; hair-loss; skin-care; mental-health; product; wegovy-pill; labs; benefits | Hims on Twitter |
| [hims-on-instagram](icons/hims-on-instagram.svg) | 20x48 | 0 0 20 20 | fill | weight-loss; hair-loss; skin-care; mental-health; product; wegovy-pill; labs; benefits | Hims on Instagram |
| [visit-hims-com](icons/visit-hims-com-c0feeb4a.svg) | 50x17 | 0 0 404 139 | fill | weight-loss; hair-loss; skin-care; mental-health; product; wegovy-pill; labs; benefits | visit hims.com |
| [icon-cc05887b](icons/icon-cc05887b.svg) | 12x12 | 0 0 12 12 | stroke | weight-loss; hair-loss; skin-care; mental-health; birth-control; product; wegovy-pill; labs | Birth Control Online / Try a Birth Contr / Labs / Labs by He |
| [navigate-to-homepage](icons/navigate-to-homepage.svg) | 58x24 | 0 0 204 85 | fill | weight-loss; hair-loss; skin-care; mental-health; product; wegovy-pill; labs; benefits | Navigate to homepage |
| [icon-ec2e0c37](icons/icon-ec2e0c37.svg) | 10x12 | 0 0 12 12 | stroke | weight-loss; hair-loss; skin-care; mental-health; birth-control; product; wegovy-pill; labs |  |
| [reset-5zh37-19](icons/reset-5zh37-19.svg) | 24x24 | 0 0 24 24 | fill | weight-loss; hair-loss; skin-care; birth-control; product; labs | Open drawer for more navigation |
| [home](icons/home-b6ad9f8c.svg) | 61x24 | 0 0 204 80 | fill | home; quality; blog; blog-post; bmi-calculator; drugs-info | Home |
| [slide-menu-toggle](icons/slide-menu-toggle.svg) | 24x24 | 0 0 24 24 | fill | home; blog; blog-post; bmi-calculator; drugs-info | Slide Menu Toggle |
| [login-button](icons/login-button.svg) | 18x18 | 0 0 18 18 | fill | blog; blog-post; bmi-calculator; drugs-info | Login Button |
| [hers-on-facebook](icons/hers-on-facebook.svg) | 20x20 | 0 0 155 155 | fill | home; anti-aging; quality | hers on Facebook |
| [hers-on-twitter](icons/hers-on-twitter.svg) | 20x20 | 0 0 20 20 | fill | home; anti-aging; quality | hers on Twitter |
| [verified-review](icons/verified-review.svg) | 16x15 | 0 0 17 16 | fill | hair-loss; mental-health; product | Verified review |
| [visit-hims-com](icons/visit-hims-com-bde8715a.svg) | 58x20 | 0 0 404 139 | fill | home; anti-aging; quality | visit hims.com |
| [hers-on-tiktok](icons/hers-on-tiktok.svg) | 20x20 | 0 0 24 24 | fill | home; anti-aging; quality | hers on TikTok |
| [visit-hims-com](icons/visit-hims-com-e3febb23.svg) | 19x22 | 0 0 19 22 | stroke | home; anti-aging; quality | visit hims.com |
| [hers-on-instagram](icons/hers-on-instagram.svg) | 20x20 | 0 0 504 504 | fill | home; anti-aging; quality | hers on Instagram |
| [buttonreset-web-components-sc-u7](icons/buttonreset-web-components-sc-u7.svg) | 16x16 | 0 0 24 24 | fill | blog-post; bmi-calculator |  |
| [icon](icons/icon-2d169100.svg) | 18x18 | 0 0 40 40 | fill | hair-loss; product | Free assessment by a medical professiona / 100% online proce |
| [icon](icons/icon-8e6b17bd.svg) | 18x18 25x25 | 0 0 40 40 | fill | skin-care; labs | Customized prescription gel creams / Quality over-the-counte |
| [rotationwrapper-sc-30ced069-0](icons/rotationwrapper-sc-30ced069-0.svg) | 20x20 | 0 0 20 20 | fill | home; anti-aging | Peptides+ is coming soon Get early acces / Read now |
| [icon-e2a6f4eb](icons/icon-e2a6f4eb.svg) | 14x14 | 0 0 12 12 | fill | blog; blog-post | Estrogen and Collagen: How Menopause Aff / Menopause and Alc |
| [wrapper-sc-4a3fbd7a-0](icons/wrapper-sc-4a3fbd7a-0-08aceab4.svg) | 18x18 | 0 0 18 18 | fill | anti-aging |  |
| [thumbnail-sc-9df93707-1](icons/thumbnail-sc-9df93707-1-117e3253.svg) | 60x60 | -3 -3 60 60 | stroke | anti-aging |  |
| [thumbnail-sc-9df93707-1](icons/thumbnail-sc-9df93707-1-36906889.svg) | 60x60 | -3 -3 60 60 | stroke | anti-aging |  |
| [carousel-controls-arrow](icons/carousel-controls-arrow.svg) | 32x32 | 0 0 24 24 | fill | wegovy-pill | Weight loss treatment comparison: previo / Weight loss treat |
| [home](icons/home-57af79c4.svg) | 61x24 | 0 0 204 80 | fill | anti-aging | Home |
| [quiztileicon-sc-ecd885f-2](icons/quiztileicon-sc-ecd885f-2.svg) | 10x10 | 0 0 10 10 | fill | home | Unsure where to begin? Start here |
| [icon-626f99e9](icons/icon-626f99e9.svg) | 12x12 | 0 0 12 12 | stroke | benefits |  |
| [benefits-hers](icons/benefits-hers.svg) | 12x12 | 0 0 12 12 | stroke | benefits | Benefits / Hers |
| [close](icons/close.svg) | 14x14 21x21 | 0 0 16 16 | fill | anti-aging | Close |
| [icon](icons/icon-713c499d.svg) | 18x18 | 0 0 40 40 | fill | weight-loss | Access to GLP-1 medications / 24/7 Care Team access / Nutrit |
| [previous-testimonial](icons/previous-testimonial.svg) | 24x24 | 0 0 24 24 | fill | home | Previous testimonial / Next testimonial |
| [icon-9d375d46](icons/icon-9d375d46.svg) | 24x24 | 0 0 24 24 | fill | bmi-calculator |  |
| [labs-by](icons/labs-by.svg) | 31x12 | 0 0 204 80 | fill | home | labs by |
| [icon](icons/icon-b30ab044.svg) | 18x18 | 0 0 40 40 | fill | mental-health | Anxiety and depression treatment plans d / Combining a presc |
| [icon-ba862dc9](icons/icon-ba862dc9.svg) | 60x60 | 0 0 60 60 | stroke | product |  |
| [icon-c835a778](icons/icon-c835a778.svg) | 64x64 | 0 0 60 60 | stroke | wegovy-pill |  |
| [rotationwrapper-sc-7c42cb01-0](icons/rotationwrapper-sc-7c42cb01-0.svg) | 32x32 | 0 0 24 24 | fill | anti-aging |  |
| [36-sources](icons/36-sources.svg) | 24x24 | 0 0 24 24 | fill | bmi-calculator | 36 Sources |
| [download-now](icons/download-now.svg) | 16x16 | 0 0 16 16 | fill | birth-control | Download now |
| [32-lbs](icons/32-lbs.svg) | 12x16 | 0 0 12 16 | fill | weight-loss | 32 lbs * |
| [wrapper-sc-4a3fbd7a-0](icons/wrapper-sc-4a3fbd7a-0-f0f04a7c.svg) | 18x18 | 0 0 18 18 | fill | quality |  |

## Gaps

### Members and external destinations

forhers has a signed-in product — the patient account, the consultation/intake flow, prescriptions, orders, the app and checkout — that lives behind the Log in control and the 'Get started' quiz and was never opened. The nav, card, footer and drug-index links and the social icons were measured, never followed; nothing was bought, no quiz was started and no form was submitted.

### Pages

- **Live forhers.com is unreachable to automation** — www.forhers.com answers a Cloudflare managed challenge (HTTP 403) to this network, headless and headed alike. The DOM evidence is Wayback Machine SSR snapshots (one per page, 2025-12-23 to 2026-11-11) served locally; the CSS, fonts and imagery are their own archived assets fetched through web.archive.org and mirrored under scratch. The markup is archived, not current live markup.
- **Scripts were stripped** from the archived pages, so everything hydration owns — the slide menu, the Log-in menu, accordion panels, carousel scrolling, quiz starts, the 'Read more' expansion — stays closed. Those resting controls were measured; their opened states are recorded as a boundary, not faked.
- **Some archived assets are missing** — Wayback never captured a share of the Cloudinary image URLs and a few page stylesheets, so some screenshots show image gaps or partially styled sections. 79 asset URLs had no usable archived copy when the mirror was built; the gaps are visible in the screenshots rather than filled with placeholders.
- **The quiz/consultation flow is client-rendered** — its SSR shell paints nothing measurable, and starting it would cross into intake. Not captured.
- **Sign-in, checkout, patient account, the app** — all gated; the controls that lead there were measured at rest and the destinations are boundaries.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover) on every control, so a state a script adds on mousedown (if any) is missing.
- **Opened, expanded and selected states** that hydration renders (menus, accordion panels, topic-tab selection, the quiz) are absent — the archived copy cannot paint them.
- **Error and loading action states** were not seen painted on the public surface; the painted disabled button was measured (forms group).

### Themes

One painted theme, no toggle: white and sage/cream surfaces with the rgba(0,0,0,.89) ink, the #338585 Hers teal, the #d5ff5d promo lime and the black action pill, over 'CareSans' display type and 'sofia-pro/SofiaProWeb' UI type. The `data-theme="light"`/`"hers"` attributes in the markup are per-component variants, not a page-level switch; tokens.json emits light only.

### Fonts

- **'sofia-pro/SofiaProWeb'** (UI) and **'CareSans'** (display) are proprietary webfonts; the woff2 files paint the captures (fetched through the archive) but are not shipped in this package. 'IvarSoft' faces are @font-face-declared on every page but no SSR rule applies them. Samples fall back to Helvetica/Arial where a face is absent.

### Screenshots

- Product photography, campaign imagery, drug names and prices shown on cards are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Product names, prices, campaign copy, article text and photography are the product's content; only frames and components were measured.
