# Elementor components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from elementor.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, bought or sent.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (45 components, 100 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Roobert 88/96.8 700, #ffffff`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (102 files, named `{component}-{state}.png`). Crop scale: the capture context runs at a device scale of 2, and a crop larger than ~1.2 megapixels is saved halved (effectively 1x) to keep the folder small — the wide panels (`nav-dropdown`, `footer`, `form-popup`, `plan-card`, `m-menu-open`) are the 1x ones. Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (the site paints light with `.dark-mode` islands on the same vars). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at the context's device scale — 1x on desktop, 2x on mobile — capped at eight chunks of 14000 device px each; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home. Photo hero with the white headline and Get-started pill, marketing sections, footer. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Website builder. The marketing page for the editor itself. | `/products/website-builder/` | [default](screenshots/builder-light-default.png), [full](screenshots/builder-light-full.png) |
| Pricing. Plan cards, billing toggles, feature rows. | `/pricing/` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [plans](screenshots/pricing-light-plans.png) |
| Enterprise. The solutions pitch for large organisations. | `/solutions/enterprise/` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| About. The company page. | `/about/` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Contact. The Elementor form (name, email, message, acceptance, submit); nothing filled or sent. | `/contact/` | [default](screenshots/contact-light-default.png), [form](screenshots/contact-light-form.png), [full](screenshots/contact-light-full.png) |
| FAQ. The accordion of questions. | `/faq/` | [default](screenshots/faq-light-default.png), [full](screenshots/faq-light-full.png), [open](screenshots/faq-light-open.png) |
| Home at 390, and the header menu opened by its own toggle. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing at 390. | `/pricing/` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Products mega-menu | every page, header | the Products trigger opened (hover + click); closed with Escape | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-dropdown) |
| Mobile menu | Home at 390 | the `e-n-menu-toggle` hamburger; closed with Escape | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |
| FAQ item, open | FAQ | the question row's own toggle (aria-expanded) | [faq-light-open](screenshots/faq-light-open.png), [faq-item-open](#faq-item-open) |
| Form field, filled | Contact | sample text typed into the name field and deleted; nothing sent | [field-name](#name-field) |
| Cookiebot consent dialog | every page, on load | hidden with CSS; the consent buttons were never pressed (a press POSTs) | [home-light-default](screenshots/home-light-default.png) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 16 components were given a real keyboard focus. 16 draw a ring: `nav-link` (2px auto #005fcc, offset 2px), `nav-login` (2px auto #005fcc, offset 2px), `nav-cta` (2px auto #005fcc, offset 2px), `menu-link` (2px auto #005fcc, offset 2px), `hero-cta` (2px auto #005fcc, offset 2px), `plan-cta` (2px auto #005fcc, offset 2px), `plan-toggle` (2px auto #005fcc, offset 2px), `contact-card` (2px auto #005fcc, offset 2px), `checkbox` (1px auto #005fcc, offset 2px), `submit-btn` (2px auto #005fcc, offset 2px), `faq-item` (1px auto #005fcc, offset 0px), `footer-link` (2px auto #005fcc, offset 2px), `social-icon` (2px auto #005fcc, offset 2px), `m-nav-item` (2px auto #005fcc offset 2px (on button.e-n-menu-dropdown-icon.e-focus)), `menu-feature` (2px auto #005fcc, offset 2px), `cta-dark` (2px auto #005fcc, offset 2px). The other 0 draw none, so a keyboard user sees no change: none. On 1 more, keyboard focus could not be landed at all (`nav-trigger`) — recorded as a failed state, not as a no-ring reading.

**Pressed.** Read with DevTools `forcePseudoState` (`:active` + `:hover`), so no control was really pressed; a state a script adds on mousedown (if any) is missing.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease` | background-color | cta-dark, footer-link, hero-cta |
| 0.3s | `ease` | all, background, border, box-shadow, max-height | faq-item, faq-item-open, m-menu-open, plan-cta, social-icon, submit-btn |
| 0.3s | `ease-in-out` | opacity | logo, nav-cta, nav-login |
| 0.4s | `ease` | transform | faq-item, faq-item-open |
| 0.5s | `ease` | grid-template-rows | faq-answer |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Nav dropdown](#nav-dropdown) | 1440 x 693.2 | - | 24px | #ffffff `blank-canvas-white` | rgba(0, 0, 0, 0.05) 0px 0px 15.008px 3.008px | 0 |
| [Card](#card) | 400 x 183.67 | - | 16px | #000000 `kernel-black` | none | 24px |
| [Plan card](#plan-card) | 297 x 1024.33 | - | 8px | #ffffff `blank-canvas-white` | none | 0 |
| [FAQ item (closed)](#faq-item-closed) | 1024 x 28 | - | - | transparent | none | 0px 80px 0px 0px |
| [FAQ answer](#faq-answer) | 1024 x 160.03 | - | - | transparent | none | 0 |
| [Name field](#name-field) | 249 x 40.41 | 1px solid #d1d1d1 `grey-500` | 4px | #ffffff `blank-canvas-white` | none | 8px |
| [Message area](#message-area) | 522 x 107.63 | 1px solid #d1d1d1 `grey-500` | 4px | #ffffff `blank-canvas-white` | none | 8px |
| [Mobile menu, open](#mobile-menu-open) | 390 x 844 | - | - | #ffffff `blank-canvas-white` | none | 88px 0px 128px 0px |

## Components

### Shell and navigation

The floating pill header shared by every page: the Elementor wordmark, the Products mega-menu trigger, plain links, the En language selector, Log in and the black Get-started pill. The header is an Elementor `header` location template (`data-elementor-type="header"`) over an `e-n-menu` widget; the dropdown is the mega-menu content panel.

#### Header
The floating pill header: Elementor logo, the Products mega-menu trigger, Agency/Enterprise/Pricing/App-Builder links, the En language selector, Log in and the black Get-started pill. Read as `header` on the Home page.

**Values (default).** size 1248 x 72; padding 0px 12px 0px 20px; radius 24px; background #ffffff `blank-canvas-white`; shadow rgba(0, 0, 0, 0.05) 0px 0px 15.008px 3.008px; text Roobert 16/22.4 400, #212121 `grey-800`.

![Header default](components/crops/header-default.png)

#### Logo
The Elementor wordmark anchor. Read as `logo` on the Home page.

**Values (default).** size 184 x 32; background transparent; text Times 16/normal 400, #0000ee; transition opacity 0.3s ease-in-out.

![Logo default](components/crops/logo-default.png)

#### Nav trigger
The Products menu trigger that opens the mega-menu; toggled, never followed. Read as `nav-trigger` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 97.97 x 40.3; padding 8.96px 16px; radius 8px; background transparent; text Roobert 16/22.4 400, #212121 `grey-800` |
| hover, pressed | background #fae4fa `syntax-glow`; text Roobert 16/22.4 400, #1f2124 |

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav link
The plain Pricing header link. Read as `nav-link` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 50.81 x 22.39; background transparent; text Roobert 16/22.4 400, #212121 `grey-800` |
| hover | text Roobert 16/22.4 400, #1f2124 |
| focus-visible | outline 2px auto #005fcc, offset 2px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Login link
The Log-in header action; measured never followed (it points at my.elementor.com). Read as `nav-login` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 44.3 x 24; background transparent; text Roobert 16/24 500, #000000 `kernel-black`; transition opacity 0.3s ease-in-out |
| focus-visible | outline 2px auto #005fcc, offset 2px |

![Login link default](components/crops/nav-login-default.png) ![Login link hover](components/crops/nav-login-hover.png) ![Login link focus-visible](components/crops/nav-login-focus-visible.png) ![Login link pressed](components/crops/nav-login-pressed.png)

#### Nav CTA
The black Get-started pill (dsm-button-primary-st); measured never followed (points at my.elementor.com/signup). Read as `nav-cta` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 144 x 48; padding 0px 24px; radius 8px; background #000000 `kernel-black`; text Roobert 18/25.2 500, #ffffff `blank-canvas-white`; transition opacity 0.3s ease-in-out |
| hover | background #ed01ee `neon-loop` |
| focus-visible | background #ed01ee `neon-loop`; outline 2px auto #005fcc, offset 2px |
| pressed | background #ed01ee `neon-loop` |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Nav dropdown
The Products mega-menu panel, opened by its own trigger. Read as `nav-dropdown` on the Home page.

**Values (default).** size 1440 x 693.2; background transparent; text Roobert 14/22.4 400, #ffffff `blank-canvas-white`; icon 84.3 x 30.39, rgba(110, 193, 228, 0).

Child layers that carry the look: div 1248x693.2 background #ffffff `blank-canvas-white` radius 24px shadow rgba(0, 0, 0, 0.05) 0px 0px 15.008px 3.008px; div::before 1248pxx1px background #d1d1d1 `grey-500`; div 368x557.2 border 1px solid #d1d1d1 `grey-500`.

![Nav dropdown default](components/crops/nav-dropdown-default.png)

#### Menu link
A product link inside the opened mega-menu columns. Read as `menu-link` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 250.66 x 84.81; padding 16px; radius 8px; background transparent; text Roobert 14/22.4 600, #000000 `kernel-black` |
| hover | background #fae4fa `syntax-glow` |
| focus-visible | background #fae4fa `syntax-glow`; outline 2px auto #005fcc, offset 2px |
| pressed | background #fae4fa `syntax-glow` |

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link focus-visible](components/crops/menu-link-focus-visible.png) ![Menu link pressed](components/crops/menu-link-pressed.png)

#### Menu feature tile
The large featured tile inside the mega-menu (the Agent Ready Scanner promo). Read as `menu-feature` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 343 x 204.22; padding 40px 24px; radius 8px; background transparent; image linear-gradient(297deg, #620856 `codeberry` 9.99%, #1b0317 60.15%); text Roobert 14/22.4 400, #ffffff `blank-canvas-white` |
| focus-visible | outline 2px auto #005fcc, offset 2px |

![Menu feature tile default](components/crops/menu-feature-default.png) ![Menu feature tile hover](components/crops/menu-feature-hover.png) ![Menu feature tile focus-visible](components/crops/menu-feature-focus-visible.png) ![Menu feature tile pressed](components/crops/menu-feature-pressed.png)

### Home hero

The full-viewport photo hero: a `.dark-mode` island that re-binds the same named vars (`--Blank-Canvas-White` -> black, `--Kernel-Black` -> white), so the headline and the white Get-started pill read inverted against the dark media.

#### Hero headline
The 88px Roobert white display headline over the photo hero (a .dark-mode island). Read as `hero-title` on the Home page.

**Values (default).** size 880 x 193.59; background transparent; text Roobert 88/96.8 600, #ffffff `blank-canvas-white`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede under the hero headline. Read as `hero-lede` on the Home page.

**Values (default).** size 352 x 56; background transparent; text Roobert 20/28 400, #f6f6f6 `grey-200`.

![Hero copy default](components/crops/hero-lede-default.png)

#### Hero CTA
The white Get-started pill in the dark hero (dsm-button-primary inverted by the .dark-mode scope); measured never followed. Read as `hero-cta` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 140.36 x 48; padding 0px 24px; radius 8px; background #ffffff `blank-canvas-white`; text Roobert 18/25.2 500, #000000 `kernel-black`; transition background-color 0.2s ease |
| hover | background #ed01ee `neon-loop`; text Roobert 18/25.2 500, #ffffff `blank-canvas-white` |
| focus-visible | background #ed01ee `neon-loop`; outline 2px auto #005fcc, offset 2px; text Roobert 18/25.2 500, #ffffff `blank-canvas-white` |
| pressed | background #ed01ee `neon-loop`; text Roobert 18/25.2 500, #ffffff `blank-canvas-white` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero stage
The full-viewport video hero (the first .dark-mode island) behind the headline; its paint is the hosted <video> plus the swap overlay, not a background. Read as `hero-stage` on the Home page.

**Values (default).** size 1440 x 900; padding 88px 96px; background #000000 `kernel-black`; image url(…); text Roobert 56/61.6 600, rgba(255, 255, 255, 0.3); transform translate(0px, 2700px); icon 48 x 48, #000000 `kernel-black`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Home

Body sections of the home page: section headings in Roobert, white `dsm-card` tiles and icon-list rows on the light ground.

#### Section heading
A Roobert section heading in the page body. Read as `h2-section` on the Home page.

**Values (default).** size 576 x 62.41; background transparent; text Roobert 24/31.2 400, #ffffff `blank-canvas-white`.

![Section heading default](components/crops/h2-section-default.png)

#### Card
A dsm card tile (1rem radius, white fill). Read as `card` on the Home page.

**Values (default).** size 400 x 183.67; padding 24px; radius 16px; background #000000 `kernel-black`; text Roobert 32/35.2 600, #f6f6f6 `grey-200`.

![Card default](components/crops/card-default.png)

#### Icon list item
A dsm icon-list row (glyph + label). Read as `icon-item` on the Home page.

**Values (default).** size 228.8 x 27.59; padding 0px 0px 8px 0px; background transparent; text Roobert 14/19.6 400, #f6f6f6 `grey-200`.

![Icon list item default](components/crops/icon-item-default.png)

#### Dark CTA
A black dsm-button-primary pill on a light section; measured never followed. Read as `cta-dark` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 141.72 x 48; padding 0px 24px; radius 8px; background #000000 `kernel-black`; text Roobert 18/25.2 500, #ffffff `blank-canvas-white`; transition background-color 0.2s ease |
| hover | background #ed01ee `neon-loop` |
| focus-visible | background #ed01ee `neon-loop`; outline 2px auto #005fcc, offset 2px |
| pressed | background #ed01ee `neon-loop` |

![Dark CTA default](components/crops/cta-dark-default.png) ![Dark CTA hover](components/crops/cta-dark-hover.png) ![Dark CTA focus-visible](components/crops/cta-dark-focus-visible.png) ![Dark CTA pressed](components/crops/cta-dark-pressed.png)

### Pricing

The pricing page: plan cards (`e-loop-item` in a carousel), the billing-period toggles, Buy-now actions and feature rows. Nothing was bought; the toggles were measured as controls, not switched into checkout.

#### Pricing title
The pricing page heading. Read as `pricing-h1` on the Pricing page.

**Values (default).** size 306.75 x 26; background transparent; text Roobert 20/26 500, #000000 `kernel-black`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Plan name
A plan card name (Essential/Advanced Solo/Advanced). Read as `plan-name` on the Pricing page.

**Values (default).** size 247 x 32; background transparent; text Roobert 20/32 600, #000000 `kernel-black`.

![Plan name default](components/crops/plan-name-default.png)

#### Plan price
A plan card price figure. Read as `plan-price` on the Pricing page.

**Values (default).** size 73.08 x 40; background transparent; text Roobert 40/40 600, #000000 `kernel-black`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan card Buy-now action; measured never followed (it would open checkout). Read as `plan-cta` on the Pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 247 x 56; border 2px solid #000000 `kernel-black`; radius 8px; background transparent; text Roobert 18/52 500, #000000 `kernel-black`; transition all 0.3s ease |
| hover | border 2px solid #ed01ee `neon-loop`; background #ed01ee `neon-loop`; text Roobert 18/52 500, #ffffff `blank-canvas-white` |
| focus-visible | border 2px solid #ed01ee `neon-loop`; background #ed01ee `neon-loop`; outline 2px auto #005fcc, offset 2px; text Roobert 18/52 500, #ffffff `blank-canvas-white` |
| pressed | border 2px solid #ed01ee `neon-loop`; background #ed01ee `neon-loop`; text Roobert 18/52 500, #ffffff `blank-canvas-white` |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan card
A pricing plan card: white 8px-radius tile holding the plan name, price, Buy-now action, the variant toggle and the feature list. Read as `plan-card` on the Pricing page.

**Values (default).** size 297 x 1024.33; radius 8px; background #ffffff `blank-canvas-white`; text Roobert 20/32 600, #000000 `kernel-black`; icon 16 x 16, #000000 `kernel-black`.

![Plan card default](components/crops/plan-card-default.png)

#### Billing toggle
A plan variant toggle inside a plan card (Advanced/Expert, One/One Agency); measured, never switched into a purchase. Read as `plan-toggle` on the Pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 119.5 x 34; radius 8px; background #ffffff `blank-canvas-white`; text Roobert 16/34 700, #212121 `grey-800` |
| focus-visible | outline 2px auto #005fcc, offset 2px |

![Billing toggle default](components/crops/plan-toggle-default.png) ![Billing toggle hover](components/crops/plan-toggle-hover.png) ![Billing toggle focus-visible](components/crops/plan-toggle-focus-visible.png) ![Billing toggle pressed](components/crops/plan-toggle-pressed.png)

#### Feature row
A plan feature row with its included/not-included marker. Read as `feature-row` on the Pricing page.

**Values (default).** size 247 x 19.59; padding 0px 0px 0px 24px; background transparent; text Roobert 14/19.6 700, #212121 `grey-800`.

Child layers that carry the look: li::before 16pxx21px image url(data:…).

![Feature row default](components/crops/feature-row-default.png)

### Contact form

The Elementor form widget on /contact: text inputs, textarea, select, the acceptance checkbox and the submit. Fields were focused and filled with sample text only; nothing was sent.

#### Contact title
The Contact-us page heading. Read as `contact-h1` on the Contact page.

**Values (default).** size 100.69 x 26; background transparent; text Roobert 20/26 500, #000000 `kernel-black`.

![Contact title default](components/crops/contact-h1-default.png)

#### Contact card
A contact-option card (Legal department inquiries form): its own toggle opens the Elementor popup holding the form. Read as `contact-card` on the Contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 280.02; padding 32px 24px; radius 16px; background #f6f6f6 `grey-200`; text Roobert 24/31.2 600, #000000 `kernel-black`; icon 32 x 32, #000000 `kernel-black` |
| hover | background transparent; shadow #000000 0px 0px 0px 1px |
| focus-visible | background transparent; shadow #000000 0px 0px 0px 1px; outline 2px auto #005fcc, offset 2px |
| pressed | background transparent; shadow #000000 0px 0px 0px 1px |

![Contact card default](components/crops/contact-card-default.png) ![Contact card hover](components/crops/contact-card-hover.png) ![Contact card focus-visible](components/crops/contact-card-focus-visible.png) ![Contact card pressed](components/crops/contact-card-pressed.png)

#### Form popup
The Elementor popup dialog holding the contact form, opened by its card. Read as `form-popup` on the Contact page.

**Values (default).** size 602 x 720.66; background transparent; text Roobert 40/52 900, #000000 `kernel-black`; icon 48 x 48, #000000 `kernel-black`.

Child layers that carry the look: a 48x48 background #f6f6f6 `grey-200` radius 50%; input 249x40.4 background #ffffff `blank-canvas-white` border 1px solid #d1d1d1 `grey-500` radius 4px; input 249x40.4 background #ffffff `blank-canvas-white` border 1px solid #d1d1d1 `grey-500` radius 4px.

![Form popup default](components/crops/form-popup-default.png)

#### Name field
The full-name text input; sample text typed and deleted, nothing sent. Read as `field-name` on the Contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 249 x 40.41; padding 8px; border 1px solid #d1d1d1 `grey-500`; radius 4px; background #ffffff `blank-canvas-white`; text Roobert 16/22.4 400, #000000 `kernel-black`; placeholder #000000 `kernel-black` |
| focused, filled | border 1px solid #000000 `kernel-black`; shadow #e2e2e2 0px 0px 6px 0px |

![Name field default](components/crops/field-name-default.png) ![Name field focused](components/crops/field-name-focused.png) ![Name field filled](components/crops/field-name-filled.png)

#### Email field
The email input; focused only, never filled or sent. Read as `field-email` on the Contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 249 x 40.41; padding 8px; border 1px solid #d1d1d1 `grey-500`; radius 4px; background #ffffff `blank-canvas-white`; text Roobert 16/22.4 400, #000000 `kernel-black`; placeholder #000000 `kernel-black` |
| focused | border 1px solid #000000 `kernel-black`; shadow #e2e2e2 0px 0px 6px 0px |

![Email field default](components/crops/field-email-default.png) ![Email field focused](components/crops/field-email-focused.png)

#### Message area
The message textarea; focused only. Read as `field-message` on the Contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 522 x 107.63; padding 8px; border 1px solid #d1d1d1 `grey-500`; radius 4px; background #ffffff `blank-canvas-white`; text Roobert 16/22.4 400, #000000 `kernel-black`; placeholder #000000 `kernel-black` |
| focused | border 1px solid #000000 `kernel-black`; shadow #e2e2e2 0px 0px 6px 0px |

![Message area default](components/crops/field-message-default.png) ![Message area focused](components/crops/field-message-focused.png)

#### Department select
The department select; measured, never changed. Read as `field-select` on the Contact page.

Not on the page when it was captured.

#### Acceptance checkbox
The acceptance checkbox; checked and unchecked as local UI state — the form was never submitted. Read as `checkbox` on the Contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 16 x 16; background #ffffff `blank-canvas-white`; visible box 16px x 16px; background #ffffff `blank-canvas-white`; border 1px solid #b5b5b5 `grey-600`; radius 2.08px; text Roobert 16/22.4 400, #000000 `kernel-black`; opacity 0; placeholder #000000 `kernel-black` |
| hover | visible box 16px x 16px; background #ffffff `blank-canvas-white`; border 1px solid #000000 `kernel-black`; radius 2.08px |
| focus-visible | outline 1px auto #005fcc, offset 2px; visible box 16px x 16px; background #ffffff `blank-canvas-white`; border 1px solid #000000 `kernel-black`; radius 2.08px |
| selected | visible box 16px x 16px; background #000000 `kernel-black`; image check glyph (data-URI svg); border 1px solid #000000 `kernel-black`; radius 2.08px; checked true on the input |

![Acceptance checkbox default](components/crops/checkbox-default.png) ![Acceptance checkbox hover](components/crops/checkbox-hover.png) ![Acceptance checkbox focus-visible](components/crops/checkbox-focus-visible.png) ![Acceptance checkbox pressed](components/crops/checkbox-pressed.png) ![Acceptance checkbox selected](components/crops/checkbox-selected.png)

#### Submit button
The form submit; measured, never pressed (a real press would send the form). Read as `submit-btn` on the Contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 105.22 x 48; padding 0px 24px; radius 8px; background #000000 `kernel-black`; text Roobert 18/48 500, #ffffff `blank-canvas-white`; transition all 0.3s ease |
| hover | background #ed01ee `neon-loop` |
| focus-visible | outline 2px auto #005fcc, offset 2px |
| pressed | background #ed01ee `neon-loop` |

![Submit button default](components/crops/submit-btn-default.png) ![Submit button hover](components/crops/submit-btn-hover.png) ![Submit button focus-visible](components/crops/submit-btn-focus-visible.png) ![Submit button pressed](components/crops/submit-btn-pressed.png)

### FAQ

The FAQ accordion on /faq: `dsm-faq--title` question rows (aria-expanded triggers) and their `dsm-faq--faq-content` answer panels.

#### FAQ title
The Frequently-Asked-Questions heading. Read as `faq-h1` on the FAQ page.

**Values (default).** size 901.38 x 79.2; background transparent; text Roobert 72/79.2 600, #000000 `kernel-black`.

![FAQ title default](components/crops/faq-h1-default.png)

#### FAQ item (closed)
A question row of the FAQ accordion (aria-expanded toggle). Read as `faq-item` on the FAQ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1024 x 28; padding 0px 80px 0px 0px; background transparent; text Roobert 20/28 700, #212121 `grey-800`; transition background 0.3s ease, border 0.3s ease, box-shadow 0.3s ease, transform 0.4s ease |
| focus-visible | outline 1px auto #005fcc, offset 0px |

Child layers that carry the look: div::after 16pxx16px image linear-gradient(#000000 `kernel-black`, #000000 `kernel-black`), linear-gradient(#000000 `.

![FAQ item (closed) default](components/crops/faq-item-default.png) ![FAQ item (closed) hover](components/crops/faq-item-hover.png) ![FAQ item (closed) focus-visible](components/crops/faq-item-focus-visible.png) ![FAQ item (closed) pressed](components/crops/faq-item-pressed.png)

#### FAQ item (open)
The same question row after its own toggle opened it. Read as `faq-item-open` on the FAQ page.

**Values (default).** size 1024 x 28; padding 0px 80px 0px 0px; background transparent; text Roobert 20/28 700, #212121 `grey-800`; transition background 0.3s ease, border 0.3s ease, box-shadow 0.3s ease, transform 0.4s ease.

Child layers that carry the look: div::after 16pxx16px image linear-gradient(#000000 `kernel-black`, #000000 `kernel-black`), linear-gradient(#000000 `.

![FAQ item (open) default](components/crops/faq-item-open-default.png)

#### FAQ answer
The revealed answer panel. Read as `faq-answer` on the FAQ page.

**Values (default).** size 1024 x 160.03; background transparent; text Roobert 16/22.4 400, #212121 `grey-800`; transition grid-template-rows 0.5s ease.

![FAQ answer default](components/crops/faq-answer-default.png)

### Footer

The `dsm-footer`, another `.dark-mode` island: link columns, social icons and legal on black.

#### Footer
The dsm-footer (a .dark-mode island): link columns, social icons and legal on black. Read as `footer` on the Home page.

**Values (default).** size 1440 x 671.53; padding 0px 96px; background #000000 `kernel-black`; text Roobert 14/19.6 700, #ffffff `blank-canvas-white`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 140.36 x 48; padding 0px 24px; radius 8px; background #ffffff `blank-canvas-white`; text Roobert 18/25.2 500, #000000 `kernel-black`; transition background-color 0.2s ease |
| hover | background #ed01ee `neon-loop`; text Roobert 18/25.2 500, #ffffff `blank-canvas-white` |
| focus-visible | background #ed01ee `neon-loop`; outline 2px auto #005fcc, offset 2px; text Roobert 18/25.2 500, #ffffff `blank-canvas-white` |
| pressed | background #ed01ee `neon-loop`; text Roobert 18/25.2 500, #ffffff `blank-canvas-white` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social icon
A footer social-icon link (icon button). Read as `social-icon` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; radius 10%; background transparent; text Times 24/24 400, #69727d; transition all 0.3s ease; icon 24 x 24, #69727d |
| hover | text Times 24/24 400, #ffffff `blank-canvas-white`; opacity 0.9; icon 24 x 24, #ffffff `blank-canvas-white` |
| focus-visible | outline 2px auto #005fcc, offset 2px |
| pressed | text Times 24/24 400, #ffffff `blank-canvas-white`; opacity 0.9; icon 24 x 24, #ffffff `blank-canvas-white` |

![Social icon default](components/crops/social-icon-default.png) ![Social icon hover](components/crops/social-icon-hover.png) ![Social icon focus-visible](components/crops/social-icon-focus-visible.png) ![Social icon pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

A few components as a phone draws them, at 390 x 844 with a mobile user agent, including the `e-n-menu-toggle` hamburger and the opened header menu.

#### Mobile header
Read as `m-header` on the Home page at 390 wide.

**Values (default).** size 358 x 64; padding 0px 16px; radius 24px; background #ffffff `blank-canvas-white`; shadow rgba(0, 0, 0, 0.05) 0px 0px 15.008px 3.008px; text Times 16/normal 400, #000000 `kernel-black`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The header hamburger toggle (e-n-menu-toggle). Read as `m-menu-button` on the Home page at 390 wide.

**Values (default).** size 32 x 32; background transparent; text Roobert 16/25.2 500, #000000 `kernel-black`; icon 32 x 32, #000000 `kernel-black`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The header menu panel opened by its own toggle. Read as `m-menu-open` on the Home page at 390 wide.

**Values (default).** size 390 x 844; padding 88px 0px 128px 0px; background #ffffff `blank-canvas-white`; text Roobert 14/19.6 400, #212121 `grey-800`; transition max-height 0.3s ease; icon 20 x 20, #212121 `grey-800`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
An item inside the opened header menu. Read as `m-nav-item` on the Home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 390 x 52.59; padding 16px 32px 16px 36px; border B: 1px solid #d1d1d1 `grey-500`; background #ffffff `blank-canvas-white`; text Roobert 14/19.6 400, #212121 `grey-800`; icon 20 x 20, #212121 `grey-800` |
| hover | icon 20 x 20, #1f2124 |
| focus-visible | outline 2px auto #005fcc offset 2px (on button.e-n-menu-dropdown-icon.e-focus) |
| pressed | icon 20 x 20, #1f2124 |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the Home page at 390 wide.

**Values (default).** size 326 x 116.16; background transparent; text Roobert 35.2/38.72 600, #ffffff `blank-canvas-white`.

![Mobile headline default](components/crops/m-hero-default.png)

## Gaps

### Pages

- **Signed-in pages.** Nothing behind sign-in was captured: the Elementor editor, the my.elementor.com dashboard, hosting/site management, and the account flows the header's Log-in and Get-started actions point at. The kit never signs in.
- **Anything that sends, buys or creates.** No contact form was submitted, no plan was bought (Buy now was measured, never pressed — it would open checkout), no account was created, no OAuth was completed, and the Cookiebot consent buttons were never pressed (the dialog was hidden with CSS instead).
- **Editor and product surfaces.** The Elementor editor, the Angi/AI copilot chat (`#elementor-angie-root` was hidden), the site-builder canvas and the hosting admin are product surfaces behind auth — documented as boundaries, not attempted.

### States

- **Pressed** was forced with DevTools on every control except toggles, so a state a script adds on mousedown (if any) is missing.
- **Billing toggles** on Pricing were measured as controls; switching them re-renders prices client-side and was not exercised into checkout.
- **Disabled states** were not seen on any public control.

### Themes

Elementor paints one light page with `.dark-mode` islands: the photo hero, dark sections and the footer carry `class="dark-mode"`, under which `.dark-mode *` re-binds `--Kernel-Black` to `#fff`, `--Blank-Canvas-White` to `#000` and `--Grey-800` to `--Grey-200`. There is no theme switch; the re-binding is scoped to those islands, so the same named vars produce the light and dark readings the token file ships (`darkscope` rules and the `dark` pass in [raw/css-vars.json](raw/css-vars.json)).

### Fonts

- **Roobert** (`--Roobert: 'Roobert'`) is the site face, self-hosted under wp-content/fonts; it renders in captures because the page loads it.
- **Roboto** is pulled from Google Fonts (`fonts.googleapis.com/css2?family=Roboto`) for the editor-side/chrome text.

### Screenshots

- Photography, product renders and brand art are Elementor's content and appear only inside screenshots and crops. The hero media and carousels keep moving, so two captures of the same view can differ.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Page prose was not transcribed; only the frames, controls and states around it were measured.
- No personal data was captured: the pages were read signed out, and no form was submitted.
