# GlossGenius components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from glossgenius.com, app.glossgenius.com and bookings.glossgenius.com on 2026-11-21, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought, booked or submitted. The sign-in, sign-up, restore and demo forms were photographed empty. No field was typed into. No service was selected and no day was chosen.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (71 components, 172 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value in the component's own surface set (light / app / booking — the three hosts declare separate vocabularies), when there is one. Text is written family size/line-height weight, then its colour, for example `baselGrotesk 16/24 600, #17150e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (181 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the surface painted at capture: `light` for every page — glossgenius.com, app.glossgenius.com and the booking site are light-only on every signed-out route (no toggle; the app's .dark class and the marketing sheet's [data-theme="dark"] block are declared evidence nothing applies). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [biz-menu](screenshots/home-light-biz-menu.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [hiw-menu](screenshots/home-light-hiw-menu.png), [resources-menu](screenshots/home-light-resources-menu.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [faq-open](screenshots/pricing-light-faq-open.png), [full](screenshots/pricing-light-full.png), [monthly](screenshots/pricing-light-monthly.png), [tiers-menu](screenshots/pricing-light-tiers-menu.png) |
| Online booking feature | `/online-booking` | [default](screenshots/feature-booking-light-default.png), [full](screenshots/feature-booking-light-full.png) |
| Payments feature | `/payment-processing` | [default](screenshots/feature-payments-light-default.png), [full](screenshots/feature-payments-light-full.png) |
| AI business tools | `/ai-business-tools` | [default](screenshots/feature-ai-light-default.png), [full](screenshots/feature-ai-light-full.png) |
| Audience page | `/for-solo-professionals` | [default](screenshots/audience-light-default.png), [full](screenshots/audience-light-full.png) |
| Customer page | `/customers/hair-salon-software` | [default](screenshots/customer-light-default.png), [full](screenshots/customer-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Blog article | `/blog/salon-spa-front-desk-productivity` | [default](screenshots/blog-article-light-default.png), [full](screenshots/blog-article-light-full.png) |
| Contact | `/contact-us` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Get a demo | `/get-demo` | [default](screenshots/get-demo-light-default.png), [full](screenshots/get-demo-light-full.png) |
| Free trial | `/free-trial` | [default](screenshots/free-trial-light-default.png), [full](screenshots/free-trial-light-full.png) |
| Privacy | `/legal/privacy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| App sign-in | `app.glossgenius.com/login` | [default](screenshots/login-light-default.png) |
| App sign-up | `app.glossgenius.com/signup` | [default](screenshots/signup-light-default.png) |
| App password recovery | `app.glossgenius.com/forgot-password` | [default](screenshots/forgot-light-default.png) |
| Booking site home | `bookings.glossgenius.com/` | [default](screenshots/book-home-light-default.png), [full](screenshots/book-home-light-full.png) |
| Booking services | `bookings.glossgenius.com/services` | [default](screenshots/book-services-light-default.png), [full](screenshots/book-services-light-full.png), [pro-menu](screenshots/book-services-light-pro-menu.png) |
| Empty booking date-picker | `bookings.glossgenius.com/booking-flow` | [default](screenshots/book-flow-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| App sign-up, phone | `app.glossgenius.com/signup` | [default](screenshots/mobile-signup-light-default.png) |
| Booking services, phone | `bookings.glossgenius.com/services` | [default](screenshots/mobile-book-services-light-default.png), [full](screenshots/mobile-book-services-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Consent overlay | every page | no consent banner was observed on any host; any layer would be hidden, never answered | hidden before every shot and reading |
| How-it-works mega-menu | marketing header | hovered/clicked the 'How it works' w-dropdown trigger to open the mega-menu (Agents, Booking & Scheduling, Marketing & CRM, Payments & POS, Staff & Business, EMR rails) | [home-light-hiw-menu](screenshots/home-light-hiw-menu.png), [nav-hiw](#how-it-works-menu-trigger), [nav-drop-item](#mega-menu-item) |
| Businesses mega-menu | marketing header | opened the 'Businesses' w-dropdown (Beauty, Wellness, Medspa, Health, Fitness rails) | [home-light-biz-menu](screenshots/home-light-biz-menu.png) |
| Billing switch | pricing | clicked the Monthly/Annual .toggle_new — annual loads checked; the click selects Monthly, a local UI toggle repricing the cards | [pricing-light-monthly](screenshots/pricing-light-monthly.png), [ptoggle](#billing-toggle) |
| Plan tier picker | pricing | clicked the Beauty & Wellness / Medspa & Aesthetics .dropdown_new--pricing-tiers — options never activated | [pricing-light-tiers-menu](screenshots/pricing-light-tiers-menu.png), [ptier](#plan-tier-dropdown), [ptier-option](#tier-option) |
| Pricing FAQ | pricing | clicked an accordion-item summary row | [pricing-light-faq-open](screenshots/pricing-light-faq-open.png), [faq-item](#faq-accordion), [faq-answer](#accordion-content) |
| Mobile menu | home, phone width | tapped the nav burger | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-burger](#mobile-burger), [m-menu-link](#mobile-menu-link) |
| Professional select | booking services | clicked 'Any Professional' to open the react-select .gg-dropdown__menu — an option never chosen | [book-services-light-pro-menu](screenshots/book-services-light-pro-menu.png), [bk-pro-select](#professional-select), [bk-pro-option](#professional-option) |
| Empty date-picker | bookings.glossgenius.com/booking-flow | opened the public booking-flow URL directly. Both selects were left closed. No professional, category, or day was chosen. | [book-flow-light-default](screenshots/book-flow-light-default.png) |
| Auth walls | app.glossgenius.com | photographed the empty login, signup and forgot-password forms. Nothing was typed. Log in, Sign up and Send reset link were never pressed. | [login-light-default](screenshots/login-light-default.png), [signup-light-default](screenshots/signup-light-default.png), [forgot-light-default](screenshots/forgot-light-default.png) |
| Signed-in product | a GlossGenius account | every post-login surface (the calendar, clients, payments, marketing tools) needs an account — app.glossgenius.com/ redirects to /calendar behind sign-in | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 27 components were given a real keyboard focus. 23 draw an outline ring: `nav-link` (1px auto #005fcc `border.focus-ring`, offset 1px), `nav-login` (1px solid #17150e `color.primary.gloss.black`, offset 1.5px), `nav-demo` (1px solid #17150e `color.primary.gloss.black`, offset 1.5px), `hero-cta` (1px solid #17150e `color.primary.gloss.black`, offset 1.5px), `hero-demo` (1px solid #17150e `color.primary.gloss.black`, offset 1.5px), `gg-support` (1px auto #005fcc `border.focus-ring`, offset 0px), `ptoggle` (on a child: 1px auto rgb(0, 95, 204) offset 2px), `plan-cta` (1px solid #17150e `color.primary.gloss.black`, offset 1.5px), `ptab-nav` (on a child: 1px solid rgb(23, 21, 14) offset 1.5px), `feat-cta` (1px solid #17150e `color.primary.gloss.black`, offset 1.5px), `signup-promo` (1px auto #005fcc, offset 0px), `signup-submit` (1px auto #005fcc, offset 0px), `forgot-send` (1px auto #005fcc, offset 0px), `forgot-back` (1px auto #005fcc, offset 1px), `bk-nav-item` (1px auto #005fcc, offset 1px), `bk-book-cta` (1px auto #005fcc, offset 1px), `m-burger` (1px auto #e59700, offset 0px), `m-hero-cta` (1px solid #17150e `color.primary.gloss.black`, offset 1.5px), `demo-step-cta` (1px solid #17150e `color.primary.gloss.black`, offset 1.5px), `login-submit` (1px auto #005fcc, offset 0px), `login-forgot` (1px auto #005fcc, offset 1px), `login-signup` (1px auto #005fcc, offset 1px), `bk-service-select` (1px auto #101010, offset 0px). 2 draw a focus ring as a shadow instead: `bk-pro-select`, `bk-book-btn`. The other 2 show no measured change: `nav-hiw`, `ptier`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease` | -webkit-box-shadow, box-shadow, opacity | bk-pro-select, forgot-field, login-field, login-pass, signup-email, signup-name, signup-pass, signup-phone |
| 0.2s | `ease-in-out` | -webkit-box-shadow, box-shadow, opacity | bk-book-btn, forgot-field, login-field, login-pass, signup-email, signup-name, signup-pass, signup-phone |
| 0.25s | `cubic-bezier(0.165, 0.84, 0.44, 1)` | background-color | m-topbar, mkt-header |
| 0.3s | `cubic-bezier(0.165, 0.84, 0.44, 1)` | background-color, border-color, color | demo-select, feat-card, nav-hiw, nav-link, plan-card-popular |
| 0.3s | `ease` | background | bk-service-select |
| 0.5s | `cubic-bezier(0.165, 0.84, 0.44, 1)` | background-color, border-color, box-shadow, color | demo-step-cta, feat-cta, hero-cta, hero-demo, m-hero-cta, nav-demo, nav-login, plan-cta |
| 0.5s | `ease` | color | bk-book-cta |
| 0.75s | `cubic-bezier(0.165, 0.84, 0.44, 1)` | color, opacity | nav-drop-item, ptier-option |
| 0.75s | `cubic-bezier(0.23, 1, 0.32, 1)` | box-shadow, flex-grow | nav-drop-item |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Home card](#home-card) | 1243.63 x 659.88 | - | - | transparent | none | 0px 12px |
| [Plan card](#plan-card) | 357.33 x 404.75 | - | - | transparent | none | 0 |
| [Popular plan card](#popular-plan-card) | 389.33 x 629.16 | - | 16px | #ffffff `apps.colors.background.default` | none | 0 |
| [Feature card](#feature-card) | 386.66 x 302 | - | 8px | #f0f7f6 `color.primary.gloss.white` | none | 0 |
| [FAQ accordion](#faq-accordion) | 1352 x 211 | B: 1px solid rgba(160, 175, 176, 0.7) `color.primary.opacity.gray.2.70` | - | transparent | none | 0 |
| [Sign-in card](#sign-in-card) | 390 x 230 | - | - | transparent | none | 0 |
| [Service card](#service-card) | 1364 x 11241.14 | - | - | transparent | none | 0 |
| [Mobile menu link](#mobile-menu-link) | 156 x 27.8 | - | - | transparent | none | 8px |

## Components

### Site chrome

The header on every marketing page: the GlossGenius wordmark, the 'How it works' mega-menu, Businesses, Pricing, Resources, 'Log in' and the 'Book a demo' pill — plus the fixed support bubble.

#### Site header
The marketing top bar: the GlossGenius wordmark, the "How it works" / "Businesses" / "Resources" mega-menus, Pricing, "Log in" and the "Book a demo" pill. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 72; padding 0px 20px; background transparent; text Basel Grotesk Book 16/24 400, #ffffff `apps.colors.background.default`; transition background-color 0.25s cubic-bezier(0.165, 0.84, 0.44, 1); layers div.dropdown_new__list-content.dropdown_new__list-content--hiw 960.0x435.4 rgb(255, 255, 255) 16px; a.btn_new.w-variant-86ea12c4-a0f3-2df0-292c-65a8bd110cde 252.7x40.4 rgb(159, 166, 255) T:1px rgba(0, 0, 0, 0) / R:1px rgba(0, 0, 0, 0) / B:1px rgba(0, 0, 0, 0) / L:1px rgba(0, 0, 0, 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px inset 8px; div.card_new.u-bg-gloss-white 370.7x387.4 rgb(240, 247, 246) 16px; div..

Child layers that carry the look: div 960x435.4 background #ffffff `apps.colors.background.default` radius 16px; a 252.7x40.4 background #9fa6ff `color.super.sky` border 1px transparent radius 8px shadow transparent 0px 0px 0px 0px inset; div 370.7x387.4 background #f0f7f6 `color.primary.gloss.white` radius 16px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The GlossGenius wordmark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 164 x 28.47; padding 8px; background transparent; text Basel Grotesk Book 16/19.2 500, #ffffff `apps.colors.background.default`.

![Logo default](components/crops/mkt-logo-default.png)

#### Nav link
A marketing header nav link (Pricing); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 73.2 x 72; padding 24px 12px; background transparent; text Basel Grotesk Book 16/24 400, #ffffff `apps.colors.background.default`; transition color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) |
| focus-visible | outline 1px auto #005fcc `border.focus-ring`, offset 1px; layers a.nav-link.u-z-index-1 73.2x72.0 1px auto rgb(0, 95, 204) offset 1px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### How-it-works menu trigger
The "How it works" nav item that opens the feature mega-menu (Agents, Booking & Scheduling, Marketing & CRM, Payments & POS, Staff & Business, EMR rails). Read as `nav-hiw` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed, opened) | size 135.81 x 72; padding 24px 12px; background transparent; text Basel Grotesk Book 16/24 400, #ffffff `apps.colors.background.default`; transition color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) |

![How-it-works menu trigger default](components/crops/nav-hiw-default.png) ![How-it-works menu trigger hover](components/crops/nav-hiw-hover.png) ![How-it-works menu trigger focus-visible](components/crops/nav-hiw-focus-visible.png) ![How-it-works menu trigger pressed](components/crops/nav-hiw-pressed.png) ![How-it-works menu trigger opened](components/crops/nav-hiw-opened.png)

#### Mega-menu item
A feature link inside the opened "How it works" mega-menu; measured while the CSS-hover menu was held open by the parked pointer, never followed. Read as `nav-drop-item` on the home page.

**Values (default).** size 103.42 x 41.59; padding 8px; background transparent; text Basel Grotesk Book 20/24 500, #17150e `color.primary.gloss.black`; transition color 0.75s cubic-bezier(0.165, 0.84, 0.44, 1), opacity 0.75s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.75s cubic-bezier(0.23, 1, 0.32, 1), flex-grow 0.75s cubic-bezier(0.23, 1, 0.32, 1).

![Mega-menu item default](components/crops/nav-drop-item-default.png)

#### Log in button
The header "Log in" button to app.glossgenius.com; measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 92.94 x 48.41; border 1px solid transparent; radius 1440px; background transparent; text Basel Grotesk Book 16/22.4 400, #ffffff `apps.colors.background.default`; transition color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1) |
| focus-visible | outline 1px solid #17150e `color.primary.gloss.black`, offset 1.5px |

![Log in button default](components/crops/nav-login-default.png) ![Log in button hover](components/crops/nav-login-hover.png) ![Log in button focus-visible](components/crops/nav-login-focus-visible.png) ![Log in button pressed](components/crops/nav-login-pressed.png)

#### Book a demo pill
The header "Book a demo" pill to /get-demo; measured, never followed. Read as `nav-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 142.72 x 48.41; border 1px solid #f0f7f6 `color.primary.gloss.white`; radius 1440px; background transparent; text Basel Grotesk Book 16/22.4 400, #ffffff `apps.colors.background.default`; transition color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1) |
| hover | background oklab(0.195557 -0.000953875 0.0137073 / 0.0998077) |
| focus-visible | outline 1px solid #17150e `color.primary.gloss.black`, offset 1.5px |
| pressed | background oklab(0.195557 -0.000953875 0.0137073 / 0.0987439) |

![Book a demo pill default](components/crops/nav-demo-default.png) ![Book a demo pill hover](components/crops/nav-demo-hover.png) ![Book a demo pill focus-visible](components/crops/nav-demo-focus-visible.png) ![Book a demo pill pressed](components/crops/nav-demo-pressed.png)

#### Support bubble
The fixed support/chat launcher pinned to the corner of every marketing page; measured, never opened. Read as `gg-support` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 56 x 56; radius 1440px; background #17150e `color.primary.gloss.black`; text remixicon 20/20 400, #f0f7f6 `color.primary.gloss.white` |
| focus-visible | outline 1px auto #005fcc `border.focus-ring`, offset 0px |

![Support bubble default](components/crops/gg-support-default.png) ![Support bubble hover](components/crops/gg-support-hover.png) ![Support bubble focus-visible](components/crops/gg-support-focus-visible.png) ![Support bubble pressed](components/crops/gg-support-pressed.png)

### Home

The light home page: the 'Scheduling, payments, and admin. Handled.' masthead, the 'Start free trial'/'Get a demo' pills and the feature cards.

#### Hero eyebrow
The eyebrow line above the hero heading. Read as `hero-eyebrow` on the home page.

**Values (default).** size 94.39 x 22.39; background transparent; text Basel Grotesk Book 16/22.4 500, #17150e `color.primary.gloss.black`; transform translate(0px, 16px); opacity 0.

![Hero eyebrow default](components/crops/hero-eyebrow-default.png)

#### Hero headline
"Scheduling, payments, and admin. Handled." — the display heading. Read as `hero-h1` on the home page.

**Values (default).** size 926.66 x 139.66; background transparent; text Basel Classic Book 72/69.84 500, #f0f7f6 `color.primary.gloss.white`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero CTA
The hero "Start free trial" button to /free-trial (the u-sm-w-100 button group — the header and mobile-nav button groups are excluded); measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 153.64 x 48.41; border 1px solid transparent; radius 1440px; background #ffffff `apps.colors.background.default`; text remixicon 16/16 400, #17150e `color.primary.gloss.black`; transition color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1) |
| hover | background oklab(0.908203 -0.0000357544 0.00127722) |
| focus-visible | outline 1px solid #17150e `color.primary.gloss.black`, offset 1.5px |
| pressed | background oklab(0.909181 -0.0000348883 0.00126383) |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero demo link
The hero "Get a demo" action; measured, never followed. Read as `hero-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 142.72 x 48.41; border 1px solid #17150e `color.primary.gloss.black`; radius 1440px; background transparent; text Basel Grotesk Book 16/22.4 400, #17150e `color.primary.gloss.black`; transition color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1) |
| hover | border 1px solid oklab(0.195557 -0.000953875 0.0137073 / 0.700579); background oklab(0.195557 -0.000953875 0.0137073 / 0.0998069) |
| focus-visible | outline 1px solid #17150e `color.primary.gloss.black`, offset 1.5px |
| pressed | border 1px solid oklab(0.195557 -0.000953875 0.0137073 / 0.703768); background oklab(0.195557 -0.000953875 0.0137073 / 0.0987439) |

![Hero demo link default](components/crops/hero-demo-default.png) ![Hero demo link hover](components/crops/hero-demo-hover.png) ![Hero demo link focus-visible](components/crops/hero-demo-focus-visible.png) ![Hero demo link pressed](components/crops/hero-demo-pressed.png)

#### Section heading
A section heading on the marketing home. Read as `home-h2` on the home page.

**Values (default).** size 94.39 x 22.39; background transparent; text Basel Grotesk Book 16/22.4 500, #17150e `color.primary.gloss.black`.

![Section heading default](components/crops/home-h2-default.png)

#### Body paragraph
A body paragraph on the marketing home. Read as `home-prose` on the home page.

**Values (default).** size 532.2 x 38.38; background transparent; text Basel Grotesk Book 16/19.2 500, #f0f7f6 `color.primary.gloss.white`.

![Body paragraph default](components/crops/home-prose-default.png)

#### Home card
A feature/benefit card on the marketing home. Read as `home-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1243.63 x 659.88; padding 0px 12px; background transparent; text Basel Grotesk Book 32/35.2 500, #17150e `color.primary.gloss.black`; layers div.img-wrapper_new.img-wrapper_new--tabs 1219.6x659.9 24px; div.swiper-progress-wrap 1219.6x329.9; div.swiper-progress 1187.6x8.0 color(srgb 1 1 1 / 0.5) 1440px; div.swiper-progress__bar 1187.6x8.0 rgb(255, 255, 255) 1440px |
| hover | layers div.img-wrapper_new.img-wrapper_new--tabs 1219.6x659.9 24px; div.swiper-progress-wrap 1219.6x329.9; div.swiper-progress 1187.6x8.0 color(srgb 1 1 1 / 0.5) 1440px; div.swiper-progress__bar 39.2x8.0 rgb(255, 255, 255) 1440px |

Child layers that carry the look: div 1219.6x659.9 image linear-gradient(#f0f7f6 `color.primary.gloss.white`, #c7cfd1 `color.primary.gray.1`) radius 24px; div 1219.6x329.9 image linear-gradient(transparent, rgba(23, 21, 14, 0.1) `color.primary.opacity.gloss.black.10`); div 1187.6x8 background rgba(255, 255, 255, 0.5) `color.primary.opacity.white.50` radius 1440px.

![Home card default](components/crops/home-card-default.png) ![Home card hover](components/crops/home-card-hover.png)

### Pricing

The /pricing page: the Monthly/Annual billing switch ('save up to 14%'), the Beauty & Wellness / Medspa & Aesthetics tier picker, the plan cards — Gold inverted dark as 'Most popular' — the compare table and the FAQ disclosures.

#### Billing toggle
The Monthly/Annual ("save up to 14%") switch above the plan cards — a checkbox-backed .toggle_new that loads annual-checked; opened was measured after clicking its input to select Monthly (a local UI toggle). Read as `ptoggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 305.3 x 32; background transparent; text Basel Grotesk Book 16/19.2 500, #778280 `color.primary.gray.3`; layers input.toggle_new__checkbox 64.0x32.0 rgb(23, 21, 14) 1440px; input::before.toggle_new__checkbox 24pxx24px rgb(240, 247, 246) 50% |
| focus-visible | layers input.toggle_new__checkbox 64.0x32.0 rgb(23, 21, 14) 1px auto rgb(0, 95, 204) offset 2px 1440px; input::before.toggle_new__checkbox 24pxx24px rgb(240, 247, 246) 50% |
| opened | text Basel Grotesk Book 16/19.2 500, #17150e `color.primary.gloss.black`; layers input.toggle_new__checkbox 64.0x32.0 rgb(119, 130, 128) 1440px; input::before.toggle_new__checkbox 24pxx24px rgb(240, 247, 246) 50% |

Child layers that carry the look: input 64x32 background #17150e `color.primary.gloss.black` radius 1440px; input::before 24pxx24px background #f0f7f6 `color.primary.gloss.white` radius 50%.

![Billing toggle default](components/crops/ptoggle-default.png) ![Billing toggle hover](components/crops/ptoggle-hover.png) ![Billing toggle focus-visible](components/crops/ptoggle-focus-visible.png) ![Billing toggle pressed](components/crops/ptoggle-pressed.png) ![Billing toggle opened](components/crops/ptoggle-opened.png)

#### Plan tier dropdown
The "Beauty & Wellness / Medspa & Aesthetics" plan-tier picker; opened was measured after clicking it — a local UI toggle whose options were never activated. Read as `ptier` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed, opened) | size 315 x 41; padding 8px; radius 32px; background #ffffff `apps.colors.background.default`; text Basel Grotesk Book 16/19.2 500, #222222 `apps.charts.chart.5.default` |

![Plan tier dropdown default](components/crops/ptier-default.png) ![Plan tier dropdown hover](components/crops/ptier-hover.png) ![Plan tier dropdown focus-visible](components/crops/ptier-focus-visible.png) ![Plan tier dropdown pressed](components/crops/ptier-pressed.png) ![Plan tier dropdown opened](components/crops/ptier-opened.png)

#### Tier option
The "Medspa & Aesthetics" option row inside the opened tier dropdown (the current option, "Beauty & Wellness", is display:none); measured while the list was held open, never activated. Read as `ptier-option` on the pricing page.

**Values (default).** size 323 x 41.59; padding 12px 0px; background transparent; text Basel Grotesk Book 16/17.6 400, #17150e `color.primary.gloss.black`; transition opacity 0.75s cubic-bezier(0.165, 0.84, 0.44, 1).

![Tier option default](components/crops/ptier-option-default.png)

#### Plan card
A pricing plan card (Standard: $28/mo monthly, $24/mo annual — "Essential tools for businesses just starting out"). Read as `plan-card` on the pricing page.

**Values (default).** size 357.33 x 404.75; background transparent; text Basel Grotesk Book 40/40 500, #17150e `color.primary.gloss.black`; layers div.pricing-table-row 357.3x52.6 T:1px color(srgb 0.627451 0.686275 0.690196 / 0.7); div.pricing-table-row 357.3x52.6 T:1px color(srgb 0.627451 0.686275 0.690196 / 0.7); a.btn_new.w-inline-block 357.3x48.4 rgb(23, 21, 14) T:1px rgba(0, 0, 0, 0) / R:1px rgba(0, 0, 0, 0) / B:1px rgba(0, 0, 0, 0) / L:1px rgba(0, 0, 0, 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px inset 1440px.

Child layers that carry the look: div 357.3x52.6 border 1px rgba(160, 175, 176, 0.7) `color.primary.opacity.gray.2.70`; div 357.3x52.6 border 1px rgba(160, 175, 176, 0.7) `color.primary.opacity.gray.2.70`; a 357.3x48.4 background #17150e `color.primary.gloss.black` border 1px transparent radius 1440px shadow transparent 0px 0px 0px 0px inset.

![Plan card default](components/crops/plan-card-default.png)

#### Popular plan card
The "Most popular" Gold plan card ($56/$48 monthly) — the .card_new--pricing-small column carrying the amber tag; hover is a pointer hover, never clicked through. Read as `plan-card-popular` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 389.33 x 629.16; radius 16px; background #ffffff `apps.colors.background.default`; text Basel Grotesk Book 40/40 500, #17150e `color.primary.gloss.black`; transition background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) |

![Popular plan card default](components/crops/plan-card-popular-default.png) ![Popular plan card hover](components/crops/plan-card-popular-hover.png)

#### Plan price
The struck/full price block inside a plan card. Read as `plan-price` on the pricing page.

**Values (default).** size 357.33 x 40; background transparent; text Basel Grotesk Book 40/40 500, #17150e `color.primary.gloss.black`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan card's action button/link; its states were measured but it was never followed — no checkout. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 357.33 x 48.41; border 1px solid transparent; radius 1440px; background #17150e `color.primary.gloss.black`; text Basel Grotesk Book 16/22.4 400, #f0f7f6 `color.primary.gloss.white`; transition color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1) |
| hover | background oklab(0.195557 -0.000953875 0.0137073 / 0.800386) |
| focus-visible | outline 1px solid #17150e `color.primary.gloss.black`, offset 1.5px |
| pressed | background oklab(0.195557 -0.000953875 0.0137073 / 0.801763) |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan feature row
A feature/comparison row inside the pricing block (rate or feature line). Read as `plan-row` on the pricing page.

**Values (default).** size 357.33 x 52.59; padding 16px 0px; border T: 1px solid rgba(160, 175, 176, 0.7) `color.primary.opacity.gray.2.70`; background transparent; text Basel Grotesk Book 16/19.2 500, #17150e `color.primary.gloss.black`.

![Plan feature row default](components/crops/plan-row-default.png)

#### Compare-table plan nav
A plan chip in the "Compare plans" table navigator. Read as `ptab-nav` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 323 x 106.8; background transparent; text Basel Grotesk Book 22/26.4 500, #17150e `color.primary.gloss.black`; layers div.label_new.u-bg-gloss-white 323.0x42.4 rgb(240, 247, 246) 8px; a.btn_new.w-inline-block 323.0x48.4 rgb(23, 21, 14) T:1px rgba(0, 0, 0, 0) / R:1px rgba(0, 0, 0, 0) / B:1px rgba(0, 0, 0, 0) / L:1px rgba(0, 0, 0, 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px inset 1440px |
| focus-visible | layers div.label_new.u-bg-gloss-white 323.0x42.4 rgb(240, 247, 246) 8px; a.btn_new.w-inline-block 323.0x48.4 rgb(23, 21, 14) T:1px rgba(0, 0, 0, 0) / R:1px rgba(0, 0, 0, 0) / B:1px rgba(0, 0, 0, 0) / L:1px rgba(0, 0, 0, 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px inset 1px solid rgb(23, 21, 14) offset 1.5px 1440px |

Child layers that carry the look: div 323x42.4 background #f0f7f6 `color.primary.gloss.white` radius 8px; a 323x48.4 background #17150e `color.primary.gloss.black` border 1px transparent radius 1440px shadow transparent 0px 0px 0px 0px inset.

![Compare-table plan nav default](components/crops/ptab-nav-default.png) ![Compare-table plan nav hover](components/crops/ptab-nav-hover.png) ![Compare-table plan nav focus-visible](components/crops/ptab-nav-focus-visible.png) ![Compare-table plan nav pressed](components/crops/ptab-nav-pressed.png)

#### FAQ accordion
A native <details>/<summary> disclosure in the pricing "Included in every plan" list; opened was measured after clicking the summary row (a local UI toggle). Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1352 x 211; border B: 1px solid rgba(160, 175, 176, 0.7) `color.primary.opacity.gray.2.70`; background transparent; text Basel Grotesk Book 32/35.2 500, #17150e `color.primary.gloss.black`; icon 67.88 x 67.88, #17150e `color.primary.gloss.black`; layers details.accordion-item 1352.0x211.0 B:1px color(srgb 0.627451 0.686275 0.690196 / 0.7); div.pricing-table-row 1352.0x57.0 T:1px color(srgb 0.627451 0.686275 0.690196 / 0.7); div.pricing-table-row 1352.0x57.0 color(srgb 0.941176 0.968628 0.964706 / 0.3) T:1px color(srgb 0.627451 0.686275 0.690196 / 0.7); div.pricing-table-row 1352.0x71.4 color(srgb 0.941176 0.968628 0.964706 / 0.3) T:1px color(srgb |
| opened | size 1352 x 97; icon 48 x 48, #17150e `color.primary.gloss.black`; layers details.accordion-item 1352.0x97.0 B:1px color(srgb 0.627451 0.686275 0.690196 / 0.7); div.pricing-table-row 1352.0x57.0 T:1px color(srgb 0.627451 0.686275 0.690196 / 0.7); div.pricing-table-row 1352.0x57.0 color(srgb 0.941176 0.968628 0.964706 / 0.3) T:1px color(srgb 0.627451 0.686275 0.690196 / 0.7); div.pricing-table-row 1352.0x71.4 color(srgb 0.941176 0.968628 0.964706 / 0.3) T:1px color(srgb  |

Child layers that carry the look: details 1352x211 border 1px rgba(160, 175, 176, 0.7) `color.primary.opacity.gray.2.70`; div 1352x57 border 1px rgba(160, 175, 176, 0.7) `color.primary.opacity.gray.2.70`; div 1352x57 background rgba(240, 247, 246, 0.3) `color.primary.opacity.gloss.white.30` border 1px rgba(160, 175, 176, 0.7) `color.primary.opacity.gray.2.70`.

![FAQ accordion default](components/crops/faq-item-default.png) ![FAQ accordion hover](components/crops/faq-item-hover.png) ![FAQ accordion opened](components/crops/faq-item-opened.png)

#### Accordion content
An expanded accordion's answer block (plan feature rows). Read as `faq-answer` on the pricing page.

**Values (default).** size 1352 x 285; background transparent; text Basel Grotesk Book 16/19.2 500, #17150e `color.primary.gloss.black`; layers div.pricing-table-row 1352.0x57.0 T:1px color(srgb 0.627451 0.686275 0.690196 / 0.7); div.pricing-table-row 1352.0x57.0 color(srgb 0.941176 0.968628 0.964706 / 0.3) T:1px color(srgb 0.627451 0.686275 0.690196 / 0.7); div.pricing-table-row 1352.0x57.0 color(srgb 0.941176 0.968628 0.964706 / 0.3) T:1px color(srgb 0.627451 0.686275 0.690196 / 0.7); div.pricing-table-row 1352.0x57.0 color(srgb 0.94117.

Child layers that carry the look: div 1352x57 border 1px rgba(160, 175, 176, 0.7) `color.primary.opacity.gray.2.70`; div 1352x57 background rgba(240, 247, 246, 0.3) `color.primary.opacity.gloss.white.30` border 1px rgba(160, 175, 176, 0.7) `color.primary.opacity.gray.2.70`; div 1352x57 background rgba(240, 247, 246, 0.3) `color.primary.opacity.gloss.white.30` border 1px rgba(160, 175, 176, 0.7) `color.primary.opacity.gray.2.70`.

![Accordion content default](components/crops/faq-answer-default.png)

### Feature page

The /online-booking product page: the display heading, the page CTA and capability cards.

#### Feature headline
The /online-booking display heading ("Book more clients fast", h2.h1_new). Read as `feat-h1` on the online-booking feature page.

**Values (default).** size 1200 x 91.19; background transparent; text Basel Classic Book 96/91.2 400, #17150e `color.primary.gloss.black`.

![Feature headline default](components/crops/feat-h1-default.png)

#### Feature CTA
The feature page's "Get started for free" hero action; measured, never followed. Read as `feat-cta` on the online-booking feature page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 386.66 x 48.41; border 1px solid transparent; radius 1440px; background #17150e `color.primary.gloss.black`; text Basel Grotesk Book 16/22.4 400, #f0f7f6 `color.primary.gloss.white`; transition color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1) |
| hover | background rgba(23, 21, 14, 0.8) `color.primary.opacity.gloss.black.80` |
| focus-visible | outline 1px solid #17150e `color.primary.gloss.black`, offset 1.5px |
| pressed | background oklab(0.195557 -0.000953875 0.0137073 / 0.800165) |

![Feature CTA default](components/crops/feat-cta-default.png) ![Feature CTA hover](components/crops/feat-cta-hover.png) ![Feature CTA focus-visible](components/crops/feat-cta-focus-visible.png) ![Feature CTA pressed](components/crops/feat-cta-pressed.png)

#### Feature card
A capability card on the online-booking feature page. Read as `feat-card` on the online-booking feature page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 386.66 x 302; radius 8px; background #f0f7f6 `color.primary.gloss.white`; text Basel Grotesk Book 72/69.84 500, #17150e `color.primary.gloss.black`; transition background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) |

![Feature card default](components/crops/feat-card-default.png) ![Feature card hover](components/crops/feat-card-hover.png)

#### Feature paragraph
A body paragraph on the feature page. Read as `feat-prose` on the online-booking feature page.

**Values (default).** size 590 x 79.17; background transparent; text Basel Grotesk Book 22/26.4 500, #17150e `color.primary.gloss.black`.

![Feature paragraph default](components/crops/feat-prose-default.png)

### Demo form

The /get-demo step-1 team-size pills and Get a demo control, photographed empty. Step 2 (name, email, phone) was left hidden and was not typed into.

#### Demo headline
The /get-demo page heading ("See how GlossGenius works"). Read as `demo-h1` on the get-demo page.

**Values (default).** size 1280 x 91.19; background transparent; text Basel Classic Book 96/91.2 400, #17150e `color.primary.gloss.black`.

![Demo headline default](components/crops/demo-h1-default.png)

#### Demo select
A step-2 native <select> (professional type / team size / booking system); measured with the step-2 wrapper unhidden — focused, never changed or submitted. Read as `demo-select` on the get-demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 504 x 56; padding 19.2px 16px 0px 16px; border 1px solid transparent; radius 12px; background #ffffff `apps.colors.background.default`; image url(…); text Basel Grotesk Book 16/16 500, transparent; transition background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) |
| focused | border 1px solid #17150e `color.primary.gloss.black` |

![Demo select default](components/crops/demo-select-default.png) ![Demo select focused](components/crops/demo-select-focused.png)

#### Team-size radio pill
A step-1 "How big is your team?" pill (Just me / 2-4 / 5-9 / 10+) — a label.radio_new tab; measured at rest and hovered, never chosen. Read as `demo-radio` on the get-demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 504 x 51.19; padding 16px; radius 16px; background transparent; text Basel Grotesk Book 16/19.2 400, #17150e `color.primary.gloss.black`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1; div.w-form-formradioinput.w-form-formradioinput--inputType-custom 504.0x51.2 rgb(255, 255, 255) T:1px rgb(255, 255, 255) / R:1px rgb(255, 255, 255) / B:1px rgb(255, 255, 255) / L:1px rgb(255, 255, 255) 16px |
| hover | layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1; div.w-form-formradioinput.w-form-formradioinput--inputType-custom 504.0x51.2 rgb(255, 255, 255) T:1px rgb(23, 21, 14) / R:1px rgb(23, 21, 14) / B:1px rgb(23, 21, 14) / L:1px rgb(23, 21, 14) 16px |

Child layers that carry the look: div 504x51.2 background #ffffff `apps.colors.background.default` border 1px #ffffff `apps.colors.background.default` radius 16px.

![Team-size radio pill default](components/crops/demo-radio-default.png) ![Team-size radio pill hover](components/crops/demo-radio-hover.png)

#### Demo form card
The .card-main card holding the two-step demo form on the right of the heading. Read as `demo-card` on the get-demo page.

**Values (default).** size 504 x 637; background transparent; text Basel Grotesk Book 40/40 500, #17150e `color.primary.gloss.black`; layers div.w-form-formradioinput.w-form-formradioinput--inputType-custom 504.0x51.2 rgb(255, 255, 255) T:1px rgb(255, 255, 255) / R:1px rgb(255, 255, 255) / B:1px rgb(255, 255, 255) / L:1px rgb(255, 255, 255) 16px; div.w-form-formradioinput.w-form-formradioinput--inputType-custom 504.0x51.2 rgb(255, 255, 255) T:1px rgb(255, 255, 255) / R:1px rgb(255, 255, 255) / B:1px rgb(255, 255, 255) / L:1px rgb(255, .

Child layers that carry the look: div 504x51.2 background #ffffff `apps.colors.background.default` border 1px #ffffff `apps.colors.background.default` radius 16px; div 504x51.2 background #ffffff `apps.colors.background.default` border 1px #ffffff `apps.colors.background.default` radius 16px; div 504x51.2 background #ffffff `apps.colors.background.default` border 1px #ffffff `apps.colors.background.default` radius 16px.

![Demo form card default](components/crops/demo-card-default.png)

#### Step-1 continue
The "Get a demo" link that reveals step 2; its states were measured but it was never activated — step 2 was read with its wrapper unhidden instead. Read as `demo-step-cta` on the get-demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 504 x 48.41; border 1px solid #17150e `color.primary.gloss.black`; radius 1440px; background transparent; text Basel Grotesk Book 16/22.4 400, #17150e `color.primary.gloss.black`; transition color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1) |
| hover | border 1px solid oklab(0.195557 -0.000953875 0.0137073 / 0.700582); background oklab(0.195557 -0.000953875 0.0137073 / 0.0998061) |
| focus-visible | outline 1px solid #17150e `color.primary.gloss.black`, offset 1.5px |
| pressed | border 1px solid oklab(0.195557 -0.000953875 0.0137073 / 0.702644); background oklab(0.195557 -0.000953875 0.0137073 / 0.0991186) |

![Step-1 continue default](components/crops/demo-step-cta-default.png) ![Step-1 continue hover](components/crops/demo-step-cta-hover.png) ![Step-1 continue focus-visible](components/crops/demo-step-cta-focus-visible.png) ![Step-1 continue pressed](components/crops/demo-step-cta-pressed.png)

### App sign-in

app.glossgenius.com/login — the empty signed-out sign-in card: email and password fields, the primary Log in submit and the forgot-password link. Nothing was typed. The form was not submitted.

#### Sign-in headline
The "Welcome back!" sign-in heading on app.glossgenius.com/login; pinned by size because a 1px hidden heading also matches. Read as `login-h1` on the app sign-in page.

**Values (default).** size 390 x 37; background transparent; text baselClassic 36/37 500, #2a2f2e `banner.content.empty.1`.

![Sign-in headline default](components/crops/login-h1-default.png)

#### Sign-in card
The sign-in form card — e-mail and password fields, the primary "Log in" submit and the forgot-password link. Read as `login-card` on the app sign-in page.

**Values (default).** size 390 x 230; background transparent; text baselGrotesk 17/21 500, #707877 `bottom.tab.bar.content.unselected`; layers div.BaseInputContainer_root__UQzho.BaseInput_inputContainer__Q1AQt 390.0x59.0 rgb(255, 255, 255) T:1px rgb(201, 205, 204) / R:1px rgb(201, 205, 204) / B:1px rgb(201, 205, 204) / L:1px rgb(201, 205, 204) 12px; div.BaseInputContainer_root__UQzho.BaseInput_inputContainer__Q1AQt 390.0x59.0 rgb(255, 255, 255) T:1px rgb(201, 205, 204) / R:1px rgb(201, 205, 204) / B:1px rgb(201, 205, 204) / L:1px rgb(201.

Child layers that carry the look: div 390x59 background #ffffff `apps.colors.background.default` border 1px #c9cdcc `border.dark` radius 12px; div 390x59 background #ffffff `apps.colors.background.default` border 1px #c9cdcc `border.dark` radius 12px; button 28x28 border 1px transparent radius 1000px.

![Sign-in card default](components/crops/login-card-default.png)

#### Email field (sign-in)
The empty sign-in e-mail input. Focused with the keyboard, never typed into, never submitted. Read as `login-field` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 364 x 21; background transparent; text baselGrotesk 17/21 400, #2a2f2e `banner.content.empty.1`; transition box-shadow 0.2s ease-in-out, opacity 0.2s ease; opacity 0; placeholder #757575 |
| focused | opacity none |

![Email field (sign-in) default](components/crops/login-field-default.png) ![Email field (sign-in) focused](components/crops/login-field-focused.png)

#### Password field (sign-in)
The empty sign-in password input. Focused with the keyboard, never typed into, never submitted. Read as `login-pass` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 324 x 21; background transparent; text baselGrotesk 17/21 400, #2a2f2e `banner.content.empty.1`; transition box-shadow 0.2s ease-in-out, opacity 0.2s ease; opacity 0; placeholder #757575 |
| focused | opacity none |

![Password field (sign-in) default](components/crops/login-pass-default.png) ![Password field (sign-in) focused](components/crops/login-pass-focused.png)

#### Sign-in submit
The primary "Log in" submit; its states were measured but the button was never clicked — nothing was submitted. Read as `login-submit` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 390 x 48; padding 0px 24px; border 1px solid transparent; radius 1000px; background #2a2f2e `banner.content.empty.1`; text baselGrotesk 17/21 535, #ffffff `apps.colors.background.default` |
| hover | background #444a49 `button.primary.brand.bg.hover` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #585f5e `button.primary.brand.bg.pressed` |

![Sign-in submit default](components/crops/login-submit-default.png) ![Sign-in submit hover](components/crops/login-submit-hover.png) ![Sign-in submit focus-visible](components/crops/login-submit-focus-visible.png) ![Sign-in submit pressed](components/crops/login-submit-pressed.png)

#### Forgot-password link
The "Forgot Password?" link to /forgot-password; measured, never followed. Read as `login-forgot` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 119.92 x 20; background transparent; text baselGrotesk 15/19 500, #585f5e `button.primary.brand.bg.pressed` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.Login_forgotPasswordLink__06EN7 119.9x20.0 1px auto rgb(0, 95, 204) offset 1px |

![Forgot-password link default](components/crops/login-forgot-default.png) ![Forgot-password link hover](components/crops/login-forgot-hover.png) ![Forgot-password link focus-visible](components/crops/login-forgot-focus-visible.png) ![Forgot-password link pressed](components/crops/login-forgot-pressed.png)

#### Sign-up link
The "Sign up for free trial" link beside the sign-in form; measured, never followed. Read as `login-signup` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 130.27 x 18; background transparent; text baselGrotesk 15/19 500, #2a2f2e `banner.content.empty.1` |
| hover | text baselGrotesk 15/19 500, #444a49 `button.primary.brand.bg.hover` |
| focus-visible | outline 1px auto #005fcc, offset 1px; text baselGrotesk 15/19 500, #585f5e `button.primary.brand.bg.pressed`; layers a.TextAction_root__0Cr5x.TextAction_secondary__EEy5G 130.3x18.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text baselGrotesk 15/19 500, #444a49 `button.primary.brand.bg.hover` |

![Sign-up link default](components/crops/login-signup-default.png) ![Sign-up link hover](components/crops/login-signup-hover.png) ![Sign-up link focus-visible](components/crops/login-signup-focus-visible.png) ![Sign-up link pressed](components/crops/login-signup-pressed.png)

#### App footer
The app's public footer band (About, Careers, Terms, Privacy, Contact, social icons); pinned by width because a 24px footer-classed icon also matches. Read as `login-footer` on the app sign-in page.

**Values (default).** size 1440 x 109; padding 20px 72px; background #eef0f0 `alert.default.bg`; text baselGrotesk 15/19 500, #2a2f2e `banner.content.empty.1`; icon 24 x 24, #585f5e `button.primary.brand.bg.pressed`.

![App footer default](components/crops/login-footer-default.png)

### App sign-up

app.glossgenius.com/signup — the empty signed-out sign-up card: name, email, password and phone fields, the professional checkbox, the promo-code button and the primary submit. Nothing was typed. No account was created.

#### Sign-up headline
The "Let's get started" sign-up heading on app.glossgenius.com/signup. Read as `signup-h1` on the app sign-up page.

**Values (default).** size 450 x 37; background transparent; text baselClassic 36/37 500, #2a2f2e `banner.content.empty.1`.

![Sign-up headline default](components/crops/signup-h1-default.png)

#### Name field (sign-up)
The empty sign-up first-name input. Focused, never typed into, never submitted. Read as `signup-name` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 191 x 21; background transparent; text baselGrotesk 17/21 400, #2a2f2e `banner.content.empty.1`; transition box-shadow 0.2s ease-in-out, opacity 0.2s ease; opacity 0; placeholder #757575 |
| focused | opacity none |

![Name field (sign-up) default](components/crops/signup-name-default.png) ![Name field (sign-up) focused](components/crops/signup-name-focused.png)

#### Email field (sign-up)
The empty sign-up e-mail input. Focused, never typed into, never submitted. Read as `signup-email` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 424 x 21; background transparent; text baselGrotesk 17/21 400, #2a2f2e `banner.content.empty.1`; transition box-shadow 0.2s ease-in-out, opacity 0.2s ease; opacity 0; placeholder #757575 |
| focused | opacity none |

![Email field (sign-up) default](components/crops/signup-email-default.png) ![Email field (sign-up) focused](components/crops/signup-email-focused.png)

#### Password field (sign-up)
The empty sign-up password input. Focused, never typed into, never submitted. Read as `signup-pass` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 21; background transparent; text baselGrotesk 17/21 400, #2a2f2e `banner.content.empty.1`; transition box-shadow 0.2s ease-in-out, opacity 0.2s ease; opacity 0; placeholder #757575 |
| focused | opacity none |

![Password field (sign-up) default](components/crops/signup-pass-default.png) ![Password field (sign-up) focused](components/crops/signup-pass-focused.png)

#### Phone field (sign-up)
The empty sign-up phone input. Focused, never typed into, never submitted. Read as `signup-phone` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 424 x 21; background transparent; text baselGrotesk 17/21 400, #2a2f2e `banner.content.empty.1`; transition box-shadow 0.2s ease-in-out, opacity 0.2s ease; opacity 0; placeholder #757575 |
| focused | opacity none |

![Phone field (sign-up) default](components/crops/signup-phone-default.png) ![Phone field (sign-up) focused](components/crops/signup-phone-focused.png)

#### Professional checkbox
The "I confirm that I'm a professional or business owner" checkbox; focused via .focus() on its inner input — never clicked, never checked. Read as `signup-checkbox` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 450 x 42; background transparent; text baselGrotesk 17/21 500, #2a2f2e `banner.content.empty.1`; layers div.Checkbox_iconContainer__w3ypg 24.0x24.0 T:1px rgb(142, 150, 149) / R:1px rgb(142, 150, 149) / B:1px rgb(142, 150, 149) / L:1px rgb(142, 150, 149) 8px |

Child layers that carry the look: div 24x24 border 1px #8e9695 `checkbox.unchecked.default` radius 8px.

![Professional checkbox default](components/crops/signup-checkbox-default.png) ![Professional checkbox focused](components/crops/signup-checkbox-focused.png)

#### Promo-code button
The "Add Promo Code" secondary button; measured, never activated. Read as `signup-promo` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 157.44 x 36; padding 0px 12px 0px 8px; border 1px solid #c9cdcc `border.dark`; radius 1000px; background #ffffff `apps.colors.background.default`; text baselGrotesk 15/21 535, #2a2f2e `banner.content.empty.1` |
| hover | background #f7f9f9 `button.secondary.hover` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #eef0f0 `alert.default.bg` |

![Promo-code button default](components/crops/signup-promo-default.png) ![Promo-code button hover](components/crops/signup-promo-hover.png) ![Promo-code button focus-visible](components/crops/signup-promo-focus-visible.png) ![Promo-code button pressed](components/crops/signup-promo-pressed.png)

#### Sign-up submit
The primary sign-up submit; its states were measured but the button was never clicked — no account was created. Read as `signup-submit` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 450 x 48; padding 0px 24px; border 1px solid transparent; radius 1000px; background #2a2f2e `banner.content.empty.1`; text baselGrotesk 17/21 535, #ffffff `apps.colors.background.default` |
| hover | background #444a49 `button.primary.brand.bg.hover` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #585f5e `button.primary.brand.bg.pressed` |

![Sign-up submit default](components/crops/signup-submit-default.png) ![Sign-up submit hover](components/crops/signup-submit-hover.png) ![Sign-up submit focus-visible](components/crops/signup-submit-focus-visible.png) ![Sign-up submit pressed](components/crops/signup-submit-pressed.png)

### App restore

app.glossgenius.com/forgot-password — the empty password-recovery card: one email field and the Send reset link button. Nothing was typed. No reset was sent.

#### Restore headline
The "Password recovery" heading on app.glossgenius.com/forgot-password. Read as `forgot-h1` on the app password recovery page.

**Values (default).** size 450 x 37; background transparent; text baselClassic 36/37 500, #2a2f2e `banner.content.empty.1`.

![Restore headline default](components/crops/forgot-h1-default.png)

#### Email field (restore)
The empty restore e-mail input. Focused, never typed into, never submitted. Read as `forgot-field` on the app password recovery page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 424 x 21; background transparent; text baselGrotesk 17/21 400, #2a2f2e `banner.content.empty.1`; transition box-shadow 0.2s ease-in-out, opacity 0.2s ease; opacity 0; placeholder #757575 |
| focused | opacity none |

![Email field (restore) default](components/crops/forgot-field-default.png) ![Email field (restore) focused](components/crops/forgot-field-focused.png)

#### Restore submit
The "Send reset link" submit; its states were measured but the button was never clicked — no reset e-mail was sent. Read as `forgot-send` on the app password recovery page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 450 x 48; padding 0px 24px; border 1px solid transparent; radius 1000px; background #2a2f2e `banner.content.empty.1`; text baselGrotesk 17/21 535, #ffffff `apps.colors.background.default` |
| hover | background #444a49 `button.primary.brand.bg.hover` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #585f5e `button.primary.brand.bg.pressed` |

![Restore submit default](components/crops/forgot-send-default.png) ![Restore submit hover](components/crops/forgot-send-hover.png) ![Restore submit focus-visible](components/crops/forgot-send-focus-visible.png) ![Restore submit pressed](components/crops/forgot-send-pressed.png)

#### Back-to-login link
The "Back to login" link; measured, never followed. Read as `forgot-back` on the app password recovery page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 450 x 48; padding 0px 24px; border 1px solid transparent; radius 1000px; background transparent; text baselGrotesk 17/21 535, #2a2f2e `banner.content.empty.1` |
| hover | background #f7f9f9 `button.secondary.hover` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #eef0f0 `alert.default.bg` |

![Back-to-login link default](components/crops/forgot-back-default.png) ![Back-to-login link hover](components/crops/forgot-back-hover.png) ![Back-to-login link focus-visible](components/crops/forgot-back-focus-visible.png) ![Back-to-login link pressed](components/crops/forgot-back-pressed.png)

### Published booking site

bookings.glossgenius.com — a published booking website: the nav, the Select a Professional menu (opened, never chosen), service cards, and the empty /booking-flow date-picker (Select a Professional or Select a Service Category, both left closed). No service was selected and no appointment was booked.

#### Booking-site nav
The published booking website's top nav (About, Our Team, Services, Portfolio, Shop, Contact, BOOK NOW). Read as `bk-nav` on the booking home page.

**Values (default).** size 115.41 x 80; padding 0px 16px; radius 30px; background transparent; text headingfont 20/34 400, #ffffff `apps.colors.background.default`.

![Booking-site nav default](components/crops/bk-nav-default.png)

#### Booking nav link
A nav link on the booking site; measured, never followed. Read as `bk-nav-item` on the booking home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 83.41 x 34; background transparent; text headingfont 20/34 400, #ffffff `apps.colors.background.default` |
| hover | opacity 0.5 |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a 83.4x34.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | opacity 0.5 |

![Booking nav link default](components/crops/bk-nav-item-default.png) ![Booking nav link hover](components/crops/bk-nav-item-hover.png) ![Booking nav link focus-visible](components/crops/bk-nav-item-focus-visible.png) ![Booking nav link pressed](components/crops/bk-nav-item-pressed.png)

#### Book Now button
The booking site's "BOOK NOW" nav button to the service list; measured, never followed. Read as `bk-book-cta` on the booking home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 177.03 x 54; padding 10px 40px; background transparent; text headingfont 20/34 400, #000000 `apps.colors.foreground.default`; transition color 0.5s ease |
| hover | text headingfont 20/34 400, #fefefe |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a 177.0x54.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | opacity 0.5 |

![Book Now button default](components/crops/bk-book-cta-default.png) ![Book Now button hover](components/crops/bk-book-cta-hover.png) ![Book Now button focus-visible](components/crops/bk-book-cta-focus-visible.png) ![Book Now button pressed](components/crops/bk-book-cta-pressed.png)

#### Booking title
The business-name display heading on the published booking site. Read as `bk-title` on the booking home page.

**Values (default).** size 1230.5 x 167.13; padding 0px 0px 44.5714px 0px; background transparent; text headingfont 89.14/122.57 500, #ffffff `apps.colors.background.default`.

![Booking title default](components/crops/bk-title-default.png)

#### Powered-by badge
The "powered by GLOSSGENIUS" badge on the published site. Read as `bk-badge` on the booking home page.

**Values (default).** size 122.59 x 21.45; background transparent; text headingfont 15.60/21.45 100, #ffffff `apps.colors.background.default`.

![Powered-by badge default](components/crops/bk-badge-default.png)

#### Professional select
The "Select a Professional" react-select on the service list (Any Professional, the business's pros); opened was measured with its .gg-dropdown__menu held open — an option was never chosen. Read as `bk-pro-select` on the booking services page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 320.53 x 56; border 1px solid rgba(146, 149, 165, 0.5) `text.tertiary.50`; radius 10px; background rgba(0, 0, 0, 0.25) `bg.primary.25`; text basefont 16/22 100, #ffffff `apps.colors.background.default`; transition box-shadow 0.2s ease, -webkit-box-shadow 0.2s ease; icon 20 x 20, #ffffff `apps.colors.background.default` |
| focus-visible, opened | shadow #727587 0px 0px 0px 1px; text basefont 16.96/23.32 100, #ffffff `apps.colors.background.default` |

![Professional select default](components/crops/bk-pro-select-default.png) ![Professional select hover](components/crops/bk-pro-select-hover.png) ![Professional select focus-visible](components/crops/bk-pro-select-focus-visible.png) ![Professional select pressed](components/crops/bk-pro-select-pressed.png) ![Professional select opened](components/crops/bk-pro-select-opened.png)

#### Professional option
An option row inside the opened professional menu; measured while the menu was held open, never chosen. Read as `bk-pro-option` on the booking services page.

**Values (default).** size 284.53 x 38; padding 8px 12px; background rgba(214, 214, 214, 0.5); text basefont 16/22 100, #ffffff `apps.colors.background.default`.

![Professional option default](components/crops/bk-pro-option-default.png)

#### Service card
A service card on the published list (category, name, description, price, duration, Select). Read as `bk-service-card` on the booking services page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1364 x 11241.14; background transparent; text headingfont 25.44/38.16 500, #ffffff `apps.colors.background.default`; layers button.Item_button__ndUTu 186.0x52.9 T:1px rgb(255, 255, 255) / R:1px rgb(255, 255, 255) / B:1px rgb(255, 255, 255) / L:1px rgb(255, 255, 255) 30px; span::after.CanvasService_option__lEb8L 0pxx25.4219px R:1px rgb(116, 124, 128); button.Item_button__ndUTu 186.0x52.9 T:1px rgb(255, 255, 255) / R:1px rgb(255, 255, 255) / B:1px rgb(255, 255, 255) / L:1px rgb(255, 255, 255) 30px; span::after.CanvasServ |
| hover | size 1364 x 11245.14 |

Child layers that carry the look: button 186x52.9 border 1px #ffffff `apps.colors.background.default` radius 30px; span::after 0pxx25.4219px border 1px #747c80; button 186x52.9 border 1px #ffffff `apps.colors.background.default` radius 30px.

![Service card default](components/crops/bk-service-card-default.png) ![Service card hover](components/crops/bk-service-card-hover.png)

#### BOOK bar button
The "BOOK n SERVICE" header bar at rest (BOOK 0 SERVICE). Never pressed. Read as `bk-book-btn` on the booking services page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 208 x 40; padding 12px 18px 11px 18px; border 1px solid #ffffff `apps.colors.background.default`; radius 20px; background #000000 `apps.colors.foreground.default`; text headingfont 14/normal 300, #ffffff `apps.colors.background.default`; transition box-shadow 0.2s ease-in-out, opacity 0.2s ease-in-out, -webkit-box-shadow 0.2s ease-in-out; icon 16 x 9.84, #ffffff `apps.colors.background.default` |
| focus-visible | shadow #727587 0px 0px 0px 3px |
| pressed | opacity 0.9 |

![BOOK bar button default](components/crops/bk-book-btn-default.png) ![BOOK bar button focus-visible](components/crops/bk-book-btn-focus-visible.png) ![BOOK bar button pressed](components/crops/bk-book-btn-pressed.png)

#### Service Select button
A service row's "Select" button. Measured at rest, hover, focus-visible and forced pressed. Never clicked: selecting a service starts a booking. Read as `bk-service-select` on the booking services page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 94 x 36; padding 0px 12px; background transparent; image linear-gradient(to right, #505718 0%, #807443 100%); text basefont 12/18 400, #ffffff `apps.colors.background.default`; transition background 0.3s ease; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | opacity 0.8 |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | opacity 0.8 |

![Service Select button default](components/crops/bk-service-select-default.png) ![Service Select button hover](components/crops/bk-service-select-hover.png) ![Service Select button focus-visible](components/crops/bk-service-select-focus-visible.png) ![Service Select button pressed](components/crops/bk-service-select-pressed.png)

### Mobile (390 wide)

The phone surface at 390 wide: the header, the burger menu, the masthead and the hero CTA.

#### Mobile top bar
The phone header at 390 wide: wordmark, the burger and the actions that survive the width. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 390 x 72; padding 8px 16px; background transparent; text Basel Grotesk Book 24/36 400, #17150e `color.primary.gloss.black`; transition background-color 0.25s cubic-bezier(0.165, 0.84, 0.44, 1); layers nav.header_new__nav.w-variant-045f9404-9514-8e8f-98d8-8ee7ebff042a 390.0x0.0 rgb(255, 255, 255); div.header_new__nav-overlay.w-variant-045f9404-9514-8e8f-98d8-8ee7ebff042a 390.0x88.0 rgb(255, 255, 255); ul.nav-list.nav-list--header 358.0x208.0 rgb(255, 255, 255); div.nav-link.w-dropdown-toggle 358.0x52.0 rgb(255, 255, 255); div.dropdown_new__list-content.dropdown_new__list-content--hiw 358.0x1738..

Child layers that carry the look: nav 390x0 background #ffffff `apps.colors.background.default`; div 390x88 background #ffffff `apps.colors.background.default`; ul 358x208 background #ffffff `apps.colors.background.default`.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile burger
The nav burger at 390 wide; opened was measured after tapping it (a local UI toggle opening the mobile menu). Read as `m-burger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 48 x 48; radius 390px; background transparent; text remixicon 20/20 400, #ffffff `apps.colors.background.default` |
| focus-visible | outline 1px auto #e59700, offset 0px; layers button.gg-support-btn 48.0x48.0 1px auto rgb(229, 151, 0) offset 0px 390px |

![Mobile burger default](components/crops/m-burger-default.png) ![Mobile burger hover](components/crops/m-burger-hover.png) ![Mobile burger focus-visible](components/crops/m-burger-focus-visible.png) ![Mobile burger pressed](components/crops/m-burger-pressed.png) ![Mobile burger opened](components/crops/m-burger-opened.png)

#### Mobile menu link
A link inside the opened mobile nav menu. Read as `m-menu-link` on the home page at 390 wide.

**Values (default).** size 156 x 27.8; padding 8px; background transparent; text Basel Grotesk Book 16/19.2 500, #ffffff `apps.colors.background.default`.

![Mobile menu link default](components/crops/m-menu-link-default.png)

#### Mobile hero headline
The hero display heading ("Scheduling, payments, and admin. Handled.") at 390 wide, measured before the nav menu opens. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 326.5 x 116.39; background transparent; text Basel Classic Book 40/38.8 500, #f0f7f6 `color.primary.gloss.white`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The hero action at 390 wide; measured never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 358 x 48.41; border 1px solid #17150e `color.primary.gloss.black`; radius 390px; background transparent; text Basel Grotesk Book 16/22.4 400, #17150e `color.primary.gloss.black`; transition color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.5s cubic-bezier(0.165, 0.84, 0.44, 1); transform translate(0px, -16px); opacity 0 |
| focus-visible | outline 1px solid #17150e `color.primary.gloss.black`, offset 1.5px |
| pressed | border 1px solid oklab(0.195557 -0.000953875 0.0137073 / 0.702644); background oklab(0.195557 -0.000953875 0.0137073 / 0.0991186) |

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

### Footer

The marketing footer: closing CTA, link columns, legal links and social marks.

#### Footer
The marketing footer: closing CTA, link columns, legal links and social marks. Read as `home-footer` on the home page.

**Values (default).** size 135 x 111.97; background transparent; text Basel Grotesk Book 16/17.6 400, #f0f7f6 `color.primary.gloss.white`.

![Footer default](components/crops/home-footer-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the GlossGenius wordmark, the mega-menu feature glyphs, the support bubble, the calendar chevrons and the client brand marks) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

GlossGenius's product is the business-management workspace. Every post-login surface (the calendar, client records, payments, payroll, marketing tools, reports and settings) needs an account and was never reached. app.glossgenius.com/login, /signup and /forgot-password are the signed-out walls. They were photographed empty. Nothing was typed into them. bookings.glossgenius.com is a published booking site. Its /booking-flow page was photographed with both selects closed. No service was selected and no appointment was booked. The product mocks inside the marketing pages are illustrations, not the product.

### Pages

- **The account.** Every post-login surface was never reached. The sign-in, sign-up and password-recovery forms were photographed empty. Log in, Sign up and Send reset link were never pressed. What a submitted form returns is unverified.
- **The demo form.** Step 1 was photographed. Step 2 (name, email, phone) was left hidden. Get a demo was never pressed. No request was sent.
- **Purchase.** Plan CTAs (Get started, Start free trial) were measured, never followed. No checkout or trial flow was started.
- **The booking.** The public /booking-flow page shows two closed selects (Select a Professional, Select a Service Category). Neither was opened. Select on a service row was not clicked. BOOK n SERVICE was not pressed. No day, time, details or payment step was reached.
- **Feature and audience routes** beyond the captured set share the marketing template. One example of each family was captured. The rest are mapped in site-tree.md and were not remeasured.
- **Other booking sites.** bookings.glossgenius.com is one published booking site. Other businesses re-skin the same chrome.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **The booking calendar, time slots, details and payment** were not reached. Opening them means choosing a professional or a service, which starts a booking.

### Themes

Every signed-out surface paints light only — no theme toggle and no applied dark variant was observed on glossgenius.com, app.glossgenius.com or the booking site. Two declared-but-unpainted dark vocabularies are kept as evidence: the app's scoped `.dark` class (emitted inside the app set) and the marketing sheet's `[data-theme="dark"]` block — nothing signed out switches to either, so they are declared evidence, not a captured theme.

### Fonts

- **Basel Grotesk / Basel Classic** (the app's declared --font-family-ui and --font-family-display), **Inter** (--font-family-base) and the editorial **Fraunces**/**Beau Rivage** faces are served faces on the hosts. The style guide falls back to system sans.

### Screenshots

- The product mocks, screenshots-in-screenshots and logo walls are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article copy, testimonial names and the changelog text are the product's content; only frames and components were measured.
