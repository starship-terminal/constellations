# Busuu components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from busuu.com on 2026-11-11, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the register flow's language picker was measured, never chosen; the login form was never filled.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (28 components, 63 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (61 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme (the footer is a pale-blue section). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Premium (upsell) | `/en/premium` | [default](screenshots/premium-light-default.png), [full](screenshots/premium-light-full.png), [monthly](screenshots/premium-light-monthly.png) |
| Learn Spanish | `/en/course/learn-spanish-online` | [default](screenshots/course-light-default.png), [full](screenshots/course-light-full.png) |
| Choose your language | `/en/choose-your-language` | [default](screenshots/languages-light-default.png), [full](screenshots/languages-light-full.png) |
| Register (step 1: pick a language) | `/en/register` | [default](screenshots/register-light-default.png) |
| Log in | `/en/login` | [default](screenshots/login-light-default.png) |
| About | `/en/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Learn Spanish, phone | `/en/course/learn-spanish-online` | [default](screenshots/mobile-course-light-default.png), [full](screenshots/mobile-course-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | every page, phone width | the kebab's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-nav-item](#mobile-nav-item) |
| Desktop menu overlay | home page | the kebab's own toggle (an empty <a> wrapping span.responsive-nav__icon) | [home-light-menu](screenshots/home-light-menu.png) |
| OneTrust consent stack | every page | hidden, never answered (no consent button was ever clicked) | hidden before every shot and reading |
| Billing-period toggle | /en/premium | the 1 month tab's own toggle | [premium-light-monthly](screenshots/premium-light-monthly.png), [period-toggle](#period-toggle) |
| Register flow | /en/register | the language picker is step 1; options measured, never chosen | [register-light-default](screenshots/register-light-default.png), [language-item](#language-option) |
| Signed-in app | app.busuu.com | the product lives behind login on another host | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 9 components were given a real keyboard focus. 3 draw an outline ring: `flag-card` (1px auto #005fcc `measured.focus-outline`, offset 1px), `plan-cta` (1px auto #005fcc `measured.focus-outline`, offset 0px), `footer-link` (1px auto #005fcc `measured.focus-outline`, offset 1px). 2 change only their border: `cta-signup`, `hero-cta`. The other 4 show no measured change: `course-cta`, `social-icon`, `m-nav-item`, `nav-link`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `ease-out` | background-color, border-color | flag-card, language-item |
| 0.2s | `ease` | all | cta-signup, hero-cta, nav-link |
| 0.2s | `ease-in-out` | all | plan-cta |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Language card](#language-card) | 152 x 114 | - | 16px | transparent | none | 15px 0px |
| [Plan card](#plan-card) | 356 x 812 | 2px solid #ffffff `color.neutral.paper` | 8px | #221658 `color.brand.indigo` | none | 24px |
| [Language option](#language-option) | 182 x 147 | 1px solid #dae1ea | 16px | transparent | none | 0 |
| [Mobile nav item](#mobile-nav-item) | 250 x 55.19 | - | - | transparent | none | 14px 20px |

## Components

### Shell and navigation

The simplified header: wordmark, the green Learn-for-free pill, the Log-in outline and the kebab dropdown.

#### Header
The marketing header: logo, Learn for free, Log in, For Educators/Businesses. Read as `header` on the home page.

**Values (default).** size 1440 x 557; background transparent; text Nista 40/52 800, #ffffff `color.neutral.paper`; layers ::before rgba(0, 0, 0, 0) 0px none 1; header::before.main-header-simplified 1440pxx557px; a.header-simplified__cta.btn 290.0x48.0 rgb(17, 238, 146) T:2px solid rgb(17, 238, 146) / R:2px solid rgb(17, 238, 146) / B:2px solid rgb(17, 238, 146) / L:2px solid rgb(17, 238, 146) rgba(0, 0, 0, 0.3) 0px 2px 4px 0px 45.04px.

Child layers that carry the look: header::before 1440pxx557px image linear-gradient(20.78deg, #6e00f8 3.3%, #563ce9 27.67%, #116eee `color.brand.blue` 93.23%); a 290x48 background #11ee92 `color.brand.green` border 2px solid #11ee92 `color.brand.green` radius 45.04px shadow rgba(0, 0, 0, 0.3) 0px 2px 4px 0px.

![Header default](components/crops/header-default.png)

#### Logo
The wordmark anchor (a.nav-dropdown__logo, a labelled svg), top-left of the nav bar. Read as `logo` on the home page.

**Values (default).** size 127 x 40; background transparent; text Nista 16/27.2 400, #0000ee; decoration underline auto, #0000ee.

![Logo default](components/crops/logo-default.png)

#### Signup CTA
The header CTA; links to signup, measured never followed. Read as `cta-signup` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 290 x 48; padding 12px 40px; border 2px solid #11ee92 `color.brand.green`; radius 45.04px; background #11ee92 `color.brand.green`; shadow rgba(0, 0, 0, 0.3) 0px 2px 4px 0px; text Nista 16/normal 700, #252b2f `color.neutral.ink`; transition all 0.2s ease |
| hover, focus-visible, pressed | border 2px solid #41f1a8 `color.brand.green-hover`; background #41f1a8 `color.brand.green-hover` |

![Signup CTA default](components/crops/cta-signup-default.png) ![Signup CTA hover](components/crops/cta-signup-hover.png) ![Signup CTA focus-visible](components/crops/cta-signup-focus-visible.png) ![Signup CTA pressed](components/crops/cta-signup-pressed.png)

#### Nav dropdown
The language/product dropdown in the header. Read as `nav-dropdown` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1400 x 40; background transparent; text Nista 14/normal 700, #116eee `color.brand.blue`; layers a.btn.btn--s 155.8x33.0 rgb(255, 255, 255) T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) 45.04px; a.btn.btn--s 101.0x33.0 T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) 45.04px; span::before.responsive-nav__icon.icon 100%x3px rgb(17, |

**Focus.** A real keyboard focus could not be held on this element at capture (focus-visible failed), so its focus look is uncaptured.

Child layers that carry the look: a 155.8x33 background #ffffff `color.neutral.paper` border 2px solid #ffffff `color.neutral.paper` radius 45.04px; a 101x33 border 2px solid #ffffff `color.neutral.paper` radius 45.04px; span::before 100%x3px background #116eee `color.brand.blue`.

![Nav dropdown default](components/crops/nav-dropdown-default.png) ![Nav dropdown hover](components/crops/nav-dropdown-hover.png) ![Nav dropdown pressed](components/crops/nav-dropdown-pressed.png)

#### Nav link
The nav's Log-in outline button (a.nav-dropdown__btn.btn--outline-default); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 101 x 33; padding 6px 28px; border 2px solid #ffffff `color.neutral.paper`; radius 45.04px; background transparent; text Nista 14/normal 700, #ffffff `color.neutral.paper`; transition all 0.2s ease |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

### Home

The gradient hero and the language flag module.

#### Hero headline
Read as `hero-title` on the home page.

**Values (default).** size 504 x 156; background transparent; text Nista 40/52 800, #ffffff `color.neutral.paper`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero CTA
The hero action; measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 290 x 48; padding 12px 40px; border 2px solid #11ee92 `color.brand.green`; radius 45.04px; background #11ee92 `color.brand.green`; text Nista 16/normal 700, #252b2f `color.neutral.ink`; transition all 0.2s ease |
| hover, focus-visible, pressed | border 2px solid #41f1a8 `color.brand.green-hover`; background #41f1a8 `color.brand.green-hover` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero copy
The lede under the headline. Read as `hero-sub` on the home page.

**Values (default).** size 540 x 81.56; background transparent; text Nista 16/27.2 400, #252b2f `color.neutral.ink`.

![Hero copy default](components/crops/hero-sub-default.png)

#### Language card
A language entry in the flag module. Read as `flag-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 152 x 114; padding 15px 0px; radius 16px; background transparent; text Nista 16/24 800, #666e7e `color.neutral.muted`; transition background-color 0.15s ease-out; layers span.icon.icon--circle 56.0x56.0 rgba(0, 0, 0, 0.1) 0px 1px 2px 0px 100% |
| hover | text Nista 16/24 800, #116eee `color.brand.blue` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a.flag-text.js-flag 152.0x114.0 1px auto rgb(0, 95, 204) offset 1px 16px; span.icon.icon--circle 56.0x56.0 rgba(0, 0, 0, 0.1) 0px 1px 2px 0px 100% |
| pressed | text Nista 16/24 800, #116eee `color.brand.blue` |

Child layers that carry the look: span 56x56 radius 100% shadow rgba(0, 0, 0, 0.1) 0px 1px 2px 0px.

![Language card default](components/crops/flag-card-default.png) ![Language card hover](components/crops/flag-card-hover.png) ![Language card focus-visible](components/crops/flag-card-focus-visible.png) ![Language card pressed](components/crops/flag-card-pressed.png)

### Premium

The upsell paywall: billing-period toggle, plan cards and the Get-Premium actions.

#### Premium title
Read as `premium-title` on the Premium page.

**Values (default).** size 585.42 x 44.8; background transparent; text Nista 32/44.8 800, #ffffff `color.neutral.paper`.

![Premium title default](components/crops/premium-title-default.png)

#### Period toggle
A billing-period option (12 months/1 month). Read as `period-toggle` on the Premium page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 78.48 x 22; background transparent; text Nista 16/22 400, #ffffff `color.neutral.paper` |

**Focus.** A real keyboard focus could not be held on this element at capture (focus-visible failed), so its focus look is uncaptured.

![Period toggle default](components/crops/period-toggle-default.png) ![Period toggle hover](components/crops/period-toggle-hover.png) ![Period toggle pressed](components/crops/period-toggle-pressed.png)

#### Plan price
A monthly price figure inside a tier card. Read as `plan-price` on the Premium page.

**Values (default).** size 67.97 x 27; background transparent; text Nista 18/27 400, #ffffff `color.neutral.paper`; decoration line-through auto, #ffffff `color.neutral.paper`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A Get Premium action; measured never followed. Read as `plan-cta` on the Premium page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 304 x 48; padding 12px 24px; border 2px solid #ffffff `color.neutral.paper`; radius 26px; background #ffffff `color.neutral.paper`; text Nista 16/24 700, #5438dc `color.brand.purple`; transition all 0.2s ease-in-out |
| hover | border 2px solid #5438dc `color.brand.purple` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |
| pressed | border 2px solid #432db0; text Nista 16/24 700, #432db0 |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan card
A Premium plan tier card (the Get Premium column). Read as `plan-card` on the Premium page.

**Values (default).** size 356 x 812; padding 24px; border 2px solid #ffffff `color.neutral.paper`; radius 8px; background #221658 `color.brand.indigo`; text Nista 16/24 700, #1e2d40; icon 24 x 24, #ffffff `color.neutral.paper`.

![Plan card default](components/crops/plan-card-default.png)

#### Save badge
A SAVE n% label on the plan cards. Read as `save-badge` on the Premium page.

Not on the page when it was captured.

### Course pages

The course landing pages (Spanish captured).

#### Course CTA
Read as `course-cta` on the course page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 161.44 x 48; background transparent; text NistaFonts 16/24 700, #1e2d40; layers button.sc-gEvEer.dUizwn 161.4x48.0 rgb(17, 238, 146) T:2px solid rgb(17, 238, 146) / R:2px solid rgb(17, 238, 146) / B:2px solid rgb(17, 238, 146) / L:2px solid rgb(17, 238, 146) 100px |
| hover | layers button.sc-gEvEer.dUizwn 161.4x48.0 rgb(136, 247, 200) T:2px solid rgb(136, 247, 200) / R:2px solid rgb(136, 247, 200) / B:2px solid rgb(136, 247, 200) / L:2px solid rgb(136, 247, 200) 100px |

Child layers that carry the look: button 161.4x48 background #11ee92 `color.brand.green` border 2px solid #11ee92 `color.brand.green` radius 100px.

![Course CTA default](components/crops/course-cta-default.png) ![Course CTA hover](components/crops/course-cta-hover.png) ![Course CTA focus-visible](components/crops/course-cta-focus-visible.png) ![Course CTA pressed](components/crops/course-cta-pressed.png)

#### Section heading
Read as `course-section` on the course page.

**Values (default).** size 840.53 x 62; background transparent; text NistaFonts 48/62 900, #252b2f `color.neutral.ink`.

![Section heading default](components/crops/course-section-default.png)

#### Course page title
The visible display heading (the semantic h1 is clipped for accessibility). Read as `course-title` on the course page.

**Values (default).** size 560 x 195; background transparent; text NistaFonts 48/65 900, #ffffff `color.neutral.paper`.

![Course page title default](components/crops/course-title-default.png)

### Signup and login

The register flow's language picker and the login form.

#### Signup heading
Read as `register-title` on the register page.

**Values (default).** size 595.13 x 52; background transparent; text NistaFonts 40/52 800, #252b2f `color.neutral.ink`.

![Signup heading default](components/crops/register-title-default.png)

#### Language option
A language choice in the signup flow; measured never chosen. Read as `language-item` on the register page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 182 x 147; border 1px solid #dae1ea; radius 16px; background transparent; text NistaFonts 16/24 700, #1e2d40; transition border-color 0.15s ease-out; icon 60 x 60, #116eee `color.brand.blue` |
| hover, pressed | border 1px solid #116eee `color.brand.blue`; text NistaFonts 16/24 700, #116eee `color.brand.blue` |

**Focus.** A real keyboard focus could not be held on this element at capture (focus-visible failed), so its focus look is uncaptured.

![Language option default](components/crops/language-item-default.png) ![Language option hover](components/crops/language-item-hover.png) ![Language option pressed](components/crops/language-item-pressed.png)

### Footer

The pale-blue footer: link columns, social icons, the language select, legal.

#### Footer
The main-footer: link columns, social, legal. Read as `footer` on the home page.

**Values (default).** size 1280 x 640.91; padding 30px 0px 0px 0px; background transparent; text Nista 16/27.2 800, #252b2f `color.neutral.ink`; icon 20 x 20, #000000; layers div::before.form__select-wrap 8pxx6px R:4px solid rgba(0, 0, 0, 0) / B:6px solid rgb(102, 110, 126) / L:4px solid rgba(0, 0, 0, 0); div::after.form__select-wrap 8pxx6px T:6px solid rgb(102, 110, 126) / R:4px solid rgba(0, 0, 0, 0) / L:4px solid rgba(0, 0, 0, 0); select.form__select.js-interface-switcher 220.0x41.2 T:1px solid rgb(214, 222, 230) / R:1px solid rgb(214, 222, 230) / B:1px solid rgb(21.

Child layers that carry the look: div::before 8pxx6px border 4px solid transparent; div::after 8pxx6px border 6px solid #666e7e `color.neutral.muted`; select 220x41.2 border 1px solid #d6dee6 `color.neutral.line` radius 5px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 145.61 x 17; background transparent; text Nista 14/23.8 700, #252b2f `color.neutral.ink` |
| hover | decoration underline auto, #252b2f `color.neutral.ink` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a 145.6x17.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | decoration underline auto, #252b2f `color.neutral.ink` |

![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social icon
Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 40 x 48.19; background transparent; text Nista 16/27.2 400, #000000; icon 20 x 20, #000000; layers span.icon.icon--light 40.0x40.0 rgb(167, 176, 183) 100% |
| hover | decoration underline auto, #000000; layers span.icon.icon--light 40.0x40.0 rgb(195, 201, 206) 100% |
| pressed | decoration underline auto, #000000 |

Child layers that carry the look: span 40x40 background #a7b0b7 radius 100%.

![Social icon default](components/crops/social-icon-default.png) ![Social icon hover](components/crops/social-icon-hover.png) ![Social icon focus-visible](components/crops/social-icon-focus-visible.png) ![Social icon pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The same surface at phone width.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 725.64; background transparent; text Nista 30/36 800, #ffffff `color.neutral.paper`; layers ::before rgba(0, 0, 0, 0) 0px none 1; a.header-simplified__cta.btn 193.4x43.2 rgb(17, 238, 146) T:2px solid rgb(17, 238, 146) / R:2px solid rgb(17, 238, 146) / B:2px solid rgb(17, 238, 146) / L:2px solid rgb(17, 238, 146) rgba(0, 0, 0, 0.3) 0px 2px 4px 0px 45.04px.

Child layers that carry the look: a 193.4x43.2 background #11ee92 `color.brand.green` border 2px solid #11ee92 `color.brand.green` radius 45.04px shadow rgba(0, 0, 0, 0.3) 0px 2px 4px 0px.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The kebab toggle: an empty anchor wrapping span.responsive-nav__icon. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 23 x 23; background transparent; text Nista 16/27.2 400, #0000ee; transform matrix(0, 1, -1, 0, 0, 0); icon 23 x 23, #0000ee; layers ::before rgb(17, 110, 238) 0px none 1; ::after rgb(17, 110, 238) 0px none 1; span::before.responsive-nav__icon.icon 100%x3px rgb(17, 110, 238); span::after.responsive-nav__icon.icon 65%x3px rgb(17, 110, 238).

Child layers that carry the look: span::before 100%x3px background #116eee `color.brand.blue`; span::after 65%x3px background #116eee `color.brand.blue`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The kebab dropdown, opened by its own toggle. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 250 x 165.56; radius 16px; background #ffffff `color.neutral.paper`; shadow rgba(0, 0, 0, 0.15) 1px 0px 10px 1px; text Nista 14/23.8 700, #252b2f `color.neutral.ink`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
A link inside the opened responsive nav dropdown. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 250 x 55.19; padding 14px 20px; background transparent; text Nista 14/23.8 700, #252b2f `color.neutral.ink` |
| hover, focus-visible, pressed | background #f2f7fd `color.brand.mist` |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 348 x 108; background transparent; text Nista 30/36 800, #ffffff `color.neutral.paper`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the flag artwork, social glyphs, the Busuu wordmark, the kebab) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The language-learning app itself lives on app.busuu.com behind login; the public site is the marketing shell, the register flow's first step, the login form and the /en/premium upsell. Everything past the language picker — the sign-up form, lessons, review, the profile — needs an account and was never reached.

### Pages

- **The app.** app.busuu.com and every signed-in surface were never reached.
- **Register past step 1.** The picker options were measured; choosing one (which creates a session) was never done, so later register steps are unmeasured.
- **Checkout.** Every Get Premium CTA was measured, never followed.
- **The paywall close.** The X on /en/premium was never pressed; where it lands is unrecorded.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **m-menu-button and m-menu-open** are recorded missing: the kebab is an empty <a> with no text, so the measurement specs could not label it; the opened menu shows in screenshots/mobile-home-light-menu.png and the m-nav-item measurements.
- **save-badge** is recorded missing: its selector found no SAVE n% badge on the captured premium load.
- **nav-dropdown, period-toggle and language-item** have no captured focus look: a real keyboard focus could not be held on them, so only default/hover/pressed are recorded.

### Themes

The site paints one light theme; the hero and the /en/premium upsell are gradient sections, not a theme. No dark mode is offered.

### Fonts

- **Nista** (marketing pages: home, premium, about, the nav and footer) and **NistaFonts** (the app-shell surfaces: course pages, register and the language picker) are the served faces for everything. They are served from the Busuu CDN; the style guide falls back to system sans.

### Screenshots

- Flag artwork, illustrations, the Busuu wordmark and reviewer photography in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Course syllabi, testimonials and about-page copy are the product's content; only frames and components were measured.
