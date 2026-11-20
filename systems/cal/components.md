# Cal.com components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from cal.com on 2026-11-11, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page across three public hosts: the marketing pages on cal.com, the public booking page on i.cal.com (cal.com/peer) and the auth cards on app.cal.com. Nothing was signed into, booked or submitted; the login and signup forms were never filled; the confirm action was never pressed; no booking was created.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (59 components, 139 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (139 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: the marketing pages paint `light`, the app-shell pages `dark`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `cal.com/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Pricing | `cal.com/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [monthly](screenshots/pricing-light-monthly.png), [teams](screenshots/pricing-light-teams.png) |
| Feature (Cal Video) | `cal.com/features/cal-video` | [default](screenshots/feature-light-default.png), [full](screenshots/feature-light-full.png) |
| Teams | `cal.com/teams` | [default](screenshots/teams-light-default.png), [full](screenshots/teams-light-full.png) |
| Enterprise | `cal.com/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| Customers | `cal.com/customers` | [default](screenshots/customers-light-default.png), [full](screenshots/customers-light-full.png) |
| Blog | `cal.com/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| FAQ | `cal.com/faq` | [default](screenshots/faq-light-default.png), [full](screenshots/faq-light-full.png) |
| Booking page (public) | `cal.com/peer` | [default](screenshots/booking-light-default.png), [form](screenshots/booking-light-form.png), [slots](screenshots/booking-light-slots.png) |
| Booking page, dark | `cal.com/peer?theme=dark&embed=true` | [default](screenshots/booking-dark-dark-default.png) |
| Log in | `app.cal.com/auth/login` | [default](screenshots/login-light-default.png) |
| Sign up | `app.cal.com/signup` | [default](screenshots/signup-light-default.png) |
| Home, phone | `cal.com/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Booking page, phone | `cal.com/peer` | [default](screenshots/mobile-booking-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu drawer | home, phone width | the menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item) |
| Products mega-menu | every marketing page | the Products trigger's own click | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-dropdown), [menu-link](#menu-link) |
| Pricing plan tabs | /pricing | the Teams tab's own toggle | [pricing-light-teams](screenshots/pricing-light-teams.png), [plan-tab](#plan-tab) |
| Billing-period switch | /pricing | the YEARLY switch's own toggle | [pricing-light-monthly](screenshots/pricing-light-monthly.png), [billing-toggle](#billing-toggle) |
| Slot list | booking page | another day cell's own toggle | [booking-light-slots](screenshots/booking-light-slots.png), [bk-slot](#slot-button) |
| Guest details form | booking page | a time slot's own toggle — opened, never filled or confirmed | [booking-light-form](screenshots/booking-light-form.png), [bk-form](#details-form), [bk-confirm](#confirm-button) |
| Booker dark theme | booking page | the page's supported ?theme=dark&embed=true parameter | [booking-dark-dark-default](screenshots/booking-dark-dark-default.png), [bkd-*](#booking-page-dark) |
| Signed-in product | app.cal.com dashboard | the scheduler, event types, settings and teams live behind login | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 25 components were given a real keyboard focus. 8 draw an outline ring: `hero-email` (1px auto rgba(156, 162, 174, 0.5), offset 1px), `plan-tab` (1px auto rgba(156, 162, 174, 0.5), offset 0px), `billing-toggle` (1px auto rgba(156, 162, 174, 0.5), offset 0px), `plan-cta` (1px auto rgba(156, 162, 174, 0.5), offset 1px), `feature-accordion` (1px auto rgba(156, 162, 174, 0.5), offset 0px), `bk-day` (1px auto rgba(160, 160, 160, 0.5), offset 0px), `forgot-link` (1px auto rgba(160, 160, 160, 0.5), offset 1px), `footer-link` (1px auto rgba(156, 162, 174, 0.5), offset 1px). 17 draw a focus ring as a shadow instead: `nav-trigger`, `nav-link`, `nav-signin`, `nav-cta`, `hero-google`, `hero-microsoft`, `changelog`, `sales-cta`, `bk-slot`, `bk-confirm`, `bkd-slot`, `sso-google`, `continue-btn`, `saml-link`, `signup-google`, `signup-email`, `m-nav-item`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | changelog, menu-link |
| 0.1s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, rotate, scale, stroke, text-decoration-color, transform, translate | bk-confirm, feature-accordion, plan-tab |
| 0.15s | `cubic-bezier(0, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, box-shadow, color, fill, outline-color, stroke, text-decoration-color | nav-cta, nav-signin, plan-cta, sales-cta |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, all, backdrop-filter, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | billing-toggle, bk-day, bk-day-today, bk-field, continue-btn, footer-link, hero-google, hero-microsoft and more |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | box-shadow, opacity, translate | bk-slot, bkd-slot, m-menu-open |
| 5e+06s | `ease-in-out` | background-color | email-field, pass-field |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 311.75 x 598.44 | 1px solid #dee1e6 `color.hp.line-2` | 14px | #ffffff `color.hp.page` | none | 16px |
| [Nav dropdown](#nav-dropdown) | 954 x 518.89 | - | - | transparent | none | 0 |
| [Menu link](#menu-link) | 216 x 219.7 | - | 18px | transparent | none | 8px |
| [Login card](#login-card) | 446 x 516 | - | - | transparent | none | 40px |
| [Signup card](#signup-card) | 440 x 184 | - | - | transparent | none | 0 |
| [Details form](#details-form) | 371 x 429.33 | - | - | transparent | none | 0 |
| [Mobile nav item](#mobile-nav-item) | 341 x 48 | - | 10px | transparent | none | 12px |

## Components

### Shell and navigation

The floating 72%-white glass header bar: wordmark, the Products/Use-cases/Features/Resources mega-menu triggers, plain links, Sign in and the dark Get-started pill.

#### Header
The floating rounded nav bar: wordmark, the Products/Use-cases/Features/Resources dropdowns, Enterprise and Pricing links, Sign in and the dark Get-started button. Read as `header` on the home page.

**Values (default).** size 1320 x 64; padding 0px 14px; radius 18px; background rgba(244, 244, 244, 0.72) `color.paint.bar`; text calSans 14/21 500, #242424 `color.hp.ink`; icon 12 x 12, #242424 `color.hp.ink`.

![Header default](components/crops/header-default.png)

#### Logo
The Cal.com wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 101 x 22; background transparent; text calSans 16/24 400, #242424 `color.hp.ink`.

![Logo default](components/crops/logo-default.png)

#### Nav trigger
The Products button that opens the header dropdown; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 104.27 x 36; padding 0px 14px; radius 10px; background transparent; text calSans 14/21 500, #242424 `color.hp.ink`; icon 12 x 12, #242424 `color.hp.ink` |
| focus-visible | shadow #9ca3af 0px 0px 0px 2px; layers button.flex.h-9 104.3x36.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(156, 163, 175) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 10px |

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav link
A plain header link (Pricing). Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 97.03 x 36; padding 0px 14px; radius 10px; background transparent; text calSans 14/21 500, #242424 `color.hp.ink` |
| focus-visible | shadow #9ca3af 0px 0px 0px 2px; layers a.flex.h-9 97.0x36.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(156, 163, 175) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 10px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Sign-in link
The Sign-in header action, linking to app.cal.com; measured never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73.09 x 36; padding 0px 14px; radius 10px; background transparent; text calSans 14/21 500, #242424 `color.hp.ink`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1) |
| hover | background rgba(36, 35, 35, 0.04) |
| focus-visible | shadow #9ca3af 0px 0px 0px 2px; layers a.h-9.shrink-0 73.1x36.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(156, 163, 175) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 10px |
| pressed | background rgba(36, 35, 35, 0.04) |

![Sign-in link default](components/crops/nav-signin-default.png) ![Sign-in link hover](components/crops/nav-signin-hover.png) ![Sign-in link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign-in link pressed](components/crops/nav-signin-pressed.png)

#### Nav CTA
The dark Get-started header button, linking to app.cal.com/signup; measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106.13 x 36; padding 1px 14px 0px 14px; border 1px solid #242424 `color.hp.ink`; radius 12px; background #242424 `color.hp.ink`; shadow rgba(254, 254, 254, 0.16) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text calSans 14/21 500, #ffffff `color.hp.page`; transition background-color 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | background rgba(36, 35, 35, 0.9) |
| focus-visible | shadow rgba(254, 254, 254, 0.16) 0px 1px 0px 0px inset, #ffffff 0px 0px 0px 1px, #9ca3af 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |
| pressed | background rgba(36, 35, 35, 0.9); shadow rgba(0, 0, 0, 0.08) 0px 1px 0px 0px inset; transition background-color 0.1s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.1s cubic-bezier(0, 0, 0.2, 1) |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Nav dropdown
The Products mega-menu panel, opened by its own trigger: product links beside a booking-app preview card. Read as `nav-dropdown` on the home page.

**Values (default).** size 954 x 518.89; background transparent; text -apple-system 15/15 600, #111111 `color.hp.text`; icon 10.2 x 6.6, #111111 `color.hp.text`; layers ::before rgba(0, 0, 0, 0) 0px none 1; nav.relative.h-(--popup-height) 954.0x518.9 rgb(255, 255, 255) T:1px solid rgb(229, 231, 235) / R:1px solid rgb(229, 231, 235) / B:1px solid rgb(229, 231, 235) / L:1px solid rgb(229, 231, 235) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px .

Child layers that carry the look: nav 954x518.9 background #ffffff `color.hp.page` border 1px solid #e5e7eb `color.hp.well` radius 18px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px; div 896x132 background #f3f4f6 `color.hp.field` radius 10px; div 204x409.2 background #1a1a1a radius 54px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.4) 0px 0px 0px 1px, transparent 0px 0px 0px 0px.

![Nav dropdown default](components/crops/nav-dropdown-default.png)

#### Menu link
A product card inside the opened Products dropdown (title, blurb, thumbnail). Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 216 x 219.7; padding 8px; radius 18px; background transparent; text calSans 14/20 500, rgba(36, 35, 35, 0.85); transition color 0.1s cubic-bezier(0, 0, 0.2, 1), background-color 0.1s cubic-bezier(0, 0, 0.2, 1), border-color 0.1s cubic-bezier(0, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0, 0, 0.2, 1), fill 0.1s cubic-bezier(0, 0, 0.2, 1), stroke 0.1s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0, 0, 0.2, 1); layers div.ev-photo.relative 200.0x133.3 rgb(243, 244, 246) rgba(0, 0, 0, 0.06) 0px 1px 2px 0px, rgba(0, 0, 0, 0.22) 0px 10px 18px -10px 10px; div::after.ev-photo.relative 200pxx133.328px |
| hover, pressed | background rgba(36, 35, 35, 0.04); text calSans 14/20 500, #242424 `color.hp.ink`; layers none |

Child layers that carry the look: div 200x133.3 background #f3f4f6 `color.hp.field` radius 10px shadow rgba(0, 0, 0, 0.06) 0px 1px 2px 0px, rgba(0, 0, 0, 0.22) 0px 10px 18px -10px; div::after 200pxx133.328px image radial-gradient(120% 90%, transparent 55%, rgba(0, 0, 0, 0.28) 100%), url(data:…)'/%3E%3C/.

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link pressed](components/crops/menu-link-pressed.png)

### Home

The 80px hero over the booking-page product mock, the dark Google/Microsoft sign-up buttons and the NEW changelog pill.

#### Hero headline
The "Where people find the time to meet" display headline (it wraps the product mock, so its rect covers the mock too — the text readings are the headline's). Read as `hero-title` on the home page.

**Values (default).** size 980 x 172.78; background transparent; text calSans 80/86.4 700, #242424 `color.hp.ink`; icon 13.67 x 13.67, #cc4510 `color.hp.accent`; layers span.relative.inline-block 120.0x68.8 rgb(243, 244, 246) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(229, 231, 235) 0px 0px 0px 1px inset 16px; canvas.block.size-full 120.0x68.8 rgb(227, 220, 205); canvas.block.size-full 120.0x68.8 rgb(227, 220, 205); canvas.block.size-full 120.0x68.8 rgb(227, 220, 205).

Child layers that carry the look: span 120x68.8 background #f3f4f6 `color.hp.field` radius 16px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #e5e7eb `color.hp.well` 0px 0px 0px 1px inset; canvas 120x68.8 background #e3dccd; canvas 120x68.8 background #e3dccd.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede under the headline. Read as `hero-sub` on the home page.

**Values (default).** size 1292 x 28; background transparent; text calSans 20/28 500, #6a6e78 `color.hp.muted`.

![Hero copy default](components/crops/hero-sub-default.png)

#### Google signup
The hero Sign-up-with-Google action, linking to app.cal.com SSO; measured never followed. Read as `hero-google` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 312 x 64; padding 0px 15px; border 1px solid #242424 `color.hp.ink`; radius 14px; background #242424 `color.hp.ink`; shadow rgba(254, 254, 254, 0.16) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text calSans 20/28 500, #ffffff `color.hp.page`; transition box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | background rgba(36, 35, 35, 0.9) |
| focus-visible | shadow rgba(254, 254, 254, 0.16) 0px 1px 0px 0px inset, #ffffff 0px 0px 0px 1px, #9ca3af 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |
| pressed | background rgba(36, 35, 35, 0.9); shadow rgba(0, 0, 0, 0.08) 0px 1px 0px 0px inset |

![Google signup default](components/crops/hero-google-default.png) ![Google signup hover](components/crops/hero-google-hover.png) ![Google signup focus-visible](components/crops/hero-google-focus-visible.png) ![Google signup pressed](components/crops/hero-google-pressed.png)

#### Microsoft signup
The hero Sign-up-with-Microsoft action; measured never followed. Read as `hero-microsoft` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 312 x 64; padding 0px 15px; border 1px solid #e5e7eb `color.hp.well`; radius 14px; background #ffffff `color.hp.page`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text calSans 20/28 500, #242424 `color.hp.ink`; transition box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0 0 0 / 0.04) 0px 1px 0px 0px 1 |
| hover | background rgba(243, 243, 245, 0.5) |
| focus-visible | shadow #ffffff 0px 0px 0px 1px, #9ca3af 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |
| pressed | background rgba(243, 243, 245, 0.5); shadow none; layers ::before rgba(0, 0, 0, 0) 0px none 1 |

![Microsoft signup default](components/crops/hero-microsoft-default.png) ![Microsoft signup hover](components/crops/hero-microsoft-hover.png) ![Microsoft signup focus-visible](components/crops/hero-microsoft-focus-visible.png) ![Microsoft signup pressed](components/crops/hero-microsoft-pressed.png)

#### Email signup link
The quiet "Sign up with email." link under the SSO buttons. Read as `hero-email` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 126.86 x 16; background transparent; text calSans 14/20 500, #242424 `color.hp.ink` |
| hover | text calSans 14/20 500, #676b75 |
| focus-visible | outline 1px auto rgba(156, 162, 174, 0.5), offset 1px; layers a.font-medium.text-foreground 126.9x16.0 1px auto oklab(0.713643 -0.00286406 -0.0189429 / 0.5) offset 1px |
| pressed | text calSans 14/20 500, #676b75 |

![Email signup link default](components/crops/hero-email-default.png) ![Email signup link hover](components/crops/hero-email-hover.png) ![Email signup link focus-visible](components/crops/hero-email-focus-visible.png) ![Email signup link pressed](components/crops/hero-email-pressed.png)

#### Changelog badge
The NEW "Cal.com launches" release pill under the hero. Read as `changelog` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 228.09 x 32; padding 0px 12px 0px 3px; border 1px solid #e5e7eb `color.hp.well`; radius 8px; background #ffffff `color.hp.page`; text calSans 11/11 500, #242424 `color.hp.ink`; transition color 0.1s cubic-bezier(0, 0, 0.2, 1), background-color 0.1s cubic-bezier(0, 0, 0.2, 1), border-color 0.1s cubic-bezier(0, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0, 0, 0.2, 1), fill 0.1s cubic-bezier(0, 0, 0.2, 1), stroke 0.1s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0, 0, 0.2, 1) |
| hover | background #f5f6f8 |
| focus-visible | shadow #ffffff 0px 0px 0px 1px, #9ca3af 0px 0px 0px 3px |
| pressed | background #f5f6f8 |

![Changelog badge default](components/crops/changelog-default.png) ![Changelog badge hover](components/crops/changelog-hover.png) ![Changelog badge focus-visible](components/crops/changelog-focus-visible.png) ![Changelog badge pressed](components/crops/changelog-pressed.png)

#### Product mock
The booking-page mock inside the hero (Intro call card with the 12:30 slot chips and the Booked badge). Read as `hero-mock` on the home page.

**Values (default).** size 1320 x 676.78; padding 168px 14px 96px 14px; background transparent; text calSans 11/11 500, #242424 `color.hp.ink`; icon 13.67 x 13.67, #cc4510 `color.hp.accent`; layers a.relative.inline-flex 228.1x32.0 rgb(255, 255, 255) T:1px solid rgb(229, 231, 235) / R:1px solid rgb(229, 231, 235) / B:1px solid rgb(229, 231, 235) / L:1px solid rgb(229, 231, 235) 8px; span.inline-flex.h-6 44.8x24.0 rgb(243, 244, 246) 4px; span.relative.inline-block 120.0x68.8 rgb(243, 244, 246) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px.

Child layers that carry the look: a 228.1x32 background #ffffff `color.hp.page` border 1px solid #e5e7eb `color.hp.well` radius 8px; span 44.8x24 background #f3f4f6 `color.hp.field` radius 4px; span 120x68.8 background #f3f4f6 `color.hp.field` radius 16px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #e5e7eb `color.hp.well` 0px 0px 0px 1px inset.

![Product mock default](components/crops/hero-mock-default.png)

### Pricing

The pricing surface: plan tabs, the monthly/yearly switch, the white plan cards with their dark actions, and the feature accordion.

#### Pricing title
The "Choose your Cal.com subscription" display heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 1024 x 64; background transparent; text calSans 64/64 700, #242424 `color.hp.ink`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Pricing copy
The lede under the pricing heading. Read as `pricing-sub` on the pricing page.

**Values (default).** size 672 x 48; background transparent; text calSans 16/24 400, #676b75.

![Pricing copy default](components/crops/pricing-sub-default.png)

#### Plan tab
A plan-group tab (Individuals/Teams/Organizations/Enterprise); toggled, never checked out. Read as `plan-tab` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 92.97 x 22; background transparent; text calSans 22/22 700, #242424 `color.hp.ink`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #676b75 |
| hover | text calSans 22/22 700, #676b75 |
| focus-visible | outline 1px auto rgba(156, 162, 174, 0.5), offset 0px; layers button.mt-14.mb-4 93.0x22.0 1px auto oklab(0.713643 -0.00286406 -0.0189429 / 0.5) offset 0px |
| pressed | text calSans 22/22 700, #676b75 |

![Plan tab default](components/crops/plan-tab-default.png) ![Plan tab hover](components/crops/plan-tab-hover.png) ![Plan tab focus-visible](components/crops/plan-tab-focus-visible.png) ![Plan tab pressed](components/crops/plan-tab-pressed.png)

#### Billing switch
The YEARLY billing switch; toggled locally, never checked out. Read as `billing-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 30 x 18; radius 3.35544e+07px; background #242424 `color.hp.ink`; text calSans 10/15 400, #242424 `color.hp.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 1px auto rgba(156, 162, 174, 0.5), offset 0px |

![Billing switch default](components/crops/billing-toggle-default.png) ![Billing switch hover](components/crops/billing-toggle-hover.png) ![Billing switch focus-visible](components/crops/billing-toggle-focus-visible.png) ![Billing switch pressed](components/crops/billing-toggle-pressed.png)

#### Plan card
The Free plan card ("Everything you could need for scheduling as an individual"). Read as `plan-card` on the pricing page.

**Values (default).** size 311.75 x 598.44; padding 16px; border 1px solid #dee1e6 `color.hp.line-2`; radius 14px; background #ffffff `color.hp.page`; text calSans 19/24.7 700, #242424 `color.hp.ink`; icon 14 x 14, #ffffff `color.hp.page`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan CTA
The Free plan "Use for free" action; measured never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 277.75 x 36; padding 6px 8px; radius 12px; background #242424 `color.hp.ink`; text calSans 14/21 500, #ffffff `color.hp.page`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1); icon 14 x 14, #ffffff `color.hp.page` |
| hover | background rgba(36, 35, 35, 0.9) |
| focus-visible | outline 1px auto rgba(156, 162, 174, 0.5), offset 1px |
| pressed | background rgba(36, 35, 35, 0.8) |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Sales CTA
The Talk-to-sales action beside the heading; measured never followed. Read as `sales-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 155.55 x 36; padding 0px 14px; radius 10px; background transparent; text calSans 14/21 500, #242424 `color.hp.ink`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1); layers span.relative.size-6 24.0x24.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 3.35544e+07px; span.relative.size-6 24.0x24.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, rgba(0, 0, 0,  |
| hover | background rgba(36, 35, 35, 0.04); layers none |
| focus-visible | shadow #9ca3af 0px 0px 0px 2px; layers a.flex.h-9 155.5x36.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(156, 163, 175) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 10px; span.relative.size-6 24.0x24.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px |
| pressed | background rgba(36, 35, 35, 0.04); layers none |

Child layers that carry the look: span 24x24 radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #ffffff `color.hp.page` 0px 0px 0px 2px, transparent 0px 0px 0px 0px; span 24x24 radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #ffffff `color.hp.page` 0px 0px 0px 2px, transparent 0px 0px 0px 0px.

![Sales CTA default](components/crops/sales-cta-default.png) ![Sales CTA hover](components/crops/sales-cta-hover.png) ![Sales CTA focus-visible](components/crops/sales-cta-focus-visible.png) ![Sales CTA pressed](components/crops/sales-cta-pressed.png)

#### Feature accordion
A feature-breakdown accordion section; measured closed, never expanded. Read as `feature-accordion` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 223.7 x 22; background transparent; text calSans 22/22 700, #242424 `color.hp.ink`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #676b75 |
| hover | text calSans 22/22 700, #676b75 |
| focus-visible | outline 1px auto rgba(156, 162, 174, 0.5), offset 0px; layers button.mt-14.mb-4 223.7x22.0 1px auto oklab(0.713643 -0.00286406 -0.0189429 / 0.5) offset 0px |
| pressed | text calSans 22/22 700, #676b75 |

![Feature accordion default](components/crops/feature-accordion-default.png) ![Feature accordion hover](components/crops/feature-accordion-hover.png) ![Feature accordion focus-visible](components/crops/feature-accordion-focus-visible.png) ![Feature accordion pressed](components/crops/feature-accordion-pressed.png)

### Booking page (public)

The public event-type page (cal.com/peer, served from i.cal.com): host card, month grid, day cells, time slots and the guest-details form a slot opens. Measured, never submitted.

#### Booker canvas
The booking page's outer container on the lab-grey canvas. Read as `bk-page` on the booking page.

**Values (default).** size 1440 x 900; background transparent; text Inter 14/20 600, #6b7280 `color.cal.text-subtle`; icon 16 x 16, #3c3e44 `color.cal.bg-primary-emphasis`; layers div.[--booker-timeslots-width:240px].lg:[--booker-timeslots-width:280px] 1040.0x489.8 rgb(255, 255, 255) T:1px solid rgb(229, 231, 235) / R:1px solid rgb(229, 231, 235) / B:1px solid rgb(229, 231, 235) / L:1px solid rgb(229, 231, 235) 8px; span::before.current-timezone.flex 163pxx28px rgb(238, 239, 242) 8px; div.font-normal.border-default 121.6x36.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, .

Child layers that carry the look: div 1040x489.8 background #ffffff `color.hp.page` border 1px solid #e5e7eb `color.hp.well` radius 8px; span::before 163pxx28px background #eeeff2 `color.cal.bg-subtle` radius 8px; div 121.6x36 radius 10px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px.

![Booker canvas default](components/crops/bk-page-default.png)

#### Event title
The event name ("15 Minute Meeting"). Read as `bk-title` on the booking page.

**Values (default).** size 232 x 28; background transparent; text Inter 20/28 600, #3c3e44 `color.cal.bg-primary-emphasis`.

![Event title default](components/crops/bk-title-default.png)

#### Host line
The host line under the title (other people's names stay per policy). Read as `bk-host` on the booking page.

**Values (default).** size 232 x 72; background transparent; text Inter 14/20 400, #3c3e44 `color.cal.bg-primary-emphasis`.

![Host line default](components/crops/bk-host-default.png)

#### Confirmation badge
The "Requires confirmation" badge under the title. Read as `bk-badge` on the booking page.

**Values (default).** size 232 x 20; background transparent; text Inter 14/20 500, #3c3e44 `color.cal.bg-primary-emphasis`; icon 16 x 16, #3c3e44 `color.cal.bg-primary-emphasis`.

![Confirmation badge default](components/crops/bk-badge-default.png)

#### Timezone row
The timezone meta row (Asia/Singapore). Read as `bk-meta` on the booking page.

**Values (default).** size 232 x 22; background transparent; text Inter 14/20 400, #3c3e44 `color.cal.bg-primary-emphasis`; icon 16 x 16, #3c3e44 `color.cal.bg-primary-emphasis`; layers span::before.current-timezone.flex 163pxx28px rgb(238, 239, 242) 8px; div.font-normal.border-default 121.6x36.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 10px.

Child layers that carry the look: span::before 163pxx28px background #eeeff2 `color.cal.bg-subtle` radius 8px; div 121.6x36 radius 10px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px.

![Timezone row default](components/crops/bk-meta-default.png)

#### Calendar grid
The month grid (grid-cols-7) holding the day buttons. Read as `bk-calendar` on the booking page.

**Values (default).** size 439 x 375.78; background transparent; text Inter 14/20 300, #3c3e44 `color.cal.bg-primary-emphasis`; layers button.disabled:text-bookinglighter.absolute 59.3x59.3 T:2px solid rgba(0, 0, 0, 0) / R:2px solid rgba(0, 0, 0, 0) / B:2px solid rgba(0, 0, 0, 0) / L:2px solid rgba(0, 0, 0, 0) 8px; button.disabled:text-bookinglighter.absolute 59.3x59.3 T:2px solid rgba(0, 0, 0, 0) / R:2px solid rgba(0, 0, 0, 0) / B:2px solid rgba(0, 0, 0, 0) / L:2px solid rgba(0, 0, 0, 0) 8px; button.disabled:text-bookinglighter..

Child layers that carry the look: button 59.3x59.3 border 2px solid transparent radius 8px; button 59.3x59.3 border 2px solid transparent radius 8px; button 59.3x59.3 border 2px solid transparent radius 8px.

![Calendar grid default](components/crops/bk-calendar-default.png)

#### Day button
A bookable day in the month grid; clicking it is a local toggle that shows that day's slots. Read as `bk-day` on the booking page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 59.28 x 59.3; border 2px solid transparent; radius 8px; background #e5e7eb `color.hp.well`; text Inter 14/20 500, #070a0d `color.cal.bg-inverted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 2px solid #292929 `color.hp.ink-2` |
| focus-visible | outline 1px auto rgba(160, 160, 160, 0.5), offset 0px |
| pressed | border 2px solid #292929 `color.hp.ink-2` |

![Day button default](components/crops/bk-day-default.png) ![Day button hover](components/crops/bk-day-hover.png) ![Day button focus-visible](components/crops/bk-day-focus-visible.png) ![Day button pressed](components/crops/bk-day-pressed.png)

#### Today cell
The today cell in the month grid (its "Today" label is sr-only; the date number paints). Read as `bk-day-today` on the booking page.

**Values (default).** size 59.3 x 59.3; border 2px solid transparent; radius 8px; background #292929 `color.hp.ink-2`; text Inter 14/20 500, #ffffff `color.hp.page`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Today cell default](components/crops/bk-day-today-default.png)

#### Time slot
An available time slot; clicking it opens the guest details form (captured, never filled or confirmed). Read as `bk-slot` on the booking page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 239 x 36; padding 8px 10px; border 1px solid #d1d5db `color.cal.border`; radius 10px; background #ffffff `color.hp.page`; shadow rgba(0, 0, 0, 0.03) 0px 2px 3px 0px, rgba(0, 0, 0, 0.03) 0px 2px 2px -1px; text Inter 14/14 500, #3c3e44 `color.cal.bg-primary-emphasis`; transition box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #292929 `color.hp.ink-2`; background #f6f7f9 `color.cal.bg-muted`; text Inter 14/14 500, #070a0d `color.cal.bg-inverted` |
| focus-visible | background #eeeff2 `color.cal.bg-subtle`; shadow rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(255, 255, 255, 0.2) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 0px 0px 2px |
| pressed | border 1px solid #292929 `color.hp.ink-2`; background #f6f7f9 `color.cal.bg-muted`; shadow rgba(0, 0, 0, 0.05) 0px 2px 1px 0px inset; text Inter 14/14 500, #070a0d `color.cal.bg-inverted` |

![Time slot default](components/crops/bk-slot-default.png) ![Time slot hover](components/crops/bk-slot-hover.png) ![Time slot focus-visible](components/crops/bk-slot-focus-visible.png) ![Time slot pressed](components/crops/bk-slot-pressed.png)

#### Details form
The guest details form a slot opens: name/email/notes fields and the confirm action. Measured, never filled or submitted. Read as `bk-form` on the booking page.

**Values (default).** size 371 x 429.33; background transparent; text Inter 14/14 500, #070a0d `color.cal.bg-inverted`; layers button.relative.inline-flex 0.0x0.0 rgb(255, 255, 255) T:1px solid oklab(0.177624 0.00000809133 0.00000356138 / 0.1) / B:1px solid oklab(0.177624 0.00000809133 0.00000356138 / 0.1) / L:1px solid oklab(0.177624 0.00000809133 0.00000356138 / 0.1) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, lab(0 0 0 / 0.05) 0.

Child layers that carry the look: button 0x0 background #ffffff `color.hp.page` border 1px solid rgba(17, 16, 16, 0.1) radius 10px 0px 0px 10px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; button::before autoxauto radius 9px 0px 0px 9px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(17, 16, 17, 0.04) 0px 1px 0px 0px; div 0x0 background rgba(17, 16, 16, 0.1).

![Details form default](components/crops/bk-form-default.png)

#### Form field
A text field in the details form; focused by a click, never typed into or submitted. Read as `bk-field` on the booking page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 371 x 32; padding 8px 12px; border 1px solid #d1d5db `color.cal.border`; radius 10px; background #ffffff `color.hp.page`; shadow rgba(0, 0, 0, 0.03) 0px 2px 3px 0px, rgba(0, 0, 0, 0.03) 0px 2px 2px -1px; text Inter 14/14 500, #3c3e44 `color.cal.bg-primary-emphasis`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #9ca3b0 `color.cal.text-muted` |
| focused | border 1px solid #9ca3b0 `color.cal.text-muted`; shadow rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(255, 255, 255, 0.2) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 0px 0px 2px |

![Form field default](components/crops/bk-field-default.png) ![Form field focused](components/crops/bk-field-focused.png)

#### Confirm button
The booking confirm action; measured only — a real press would create a booking, so it was never clicked (pressed is a CDP-forced state). Read as `bk-confirm` on the booking page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 76.06 x 32; padding 8px 10px; border 1px solid #292929 `color.hp.ink-2`; radius 10px; background #292929 `color.hp.ink-2`; shadow rgba(0, 0, 0, 0.06) 0px 2px 3px 0px, rgba(0, 0, 0, 0.08) 0px 1px 1px 0px, rgba(0, 0, 0, 0.12) 1px 4px 8px 0px, rgba(255, 255, 255, 0.12) 0px 2px 0.4px 0px inset, rgba(0, 0, 0, 0.04) 0px -3px 2px 0px inset; text Inter 14/14 500, #ffffff `color.hp.page`; transition transform 0.1s cubic-bezier(0.4, 0, 0.2, 1), translate 0.1s cubic-bezier(0.4, 0, 0.2, 1), scale 0.1s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #696969 `color.paint.muted-auth`; shadow rgba(0, 0, 0, 0.1) 0px 1px 1px 0px, rgba(0, 0, 0, 0.08) 0px 2px 3px 0px, rgba(0, 0, 0, 0.12) 1px 4px 8px 0px, rgba(0, 0, 0, 0.1) 0px -3px 2px 0px inset, rgba(255, 255, 255, 0.24) 0px 2px 0.4px 0px inset |
| focus-visible | background #696969 `color.paint.muted-auth`; shadow rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1px 1px 0px, rgba(0, 0, 0, 0.08) 0px 2px 3px 0px, rgba(0, 0, 0, 0.12) 1px 4px 8px 0px, rgba(0, 0, 0, 0.1) 0px -3px 2px 0px inset, rgba(255, 255, 255, 0.24) 0px 2px 0.4px 0px inset |
| pressed | background #696969 `color.paint.muted-auth`; shadow rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 3px 1px 0px inset, rgba(0, 0, 0, 0.1) 0px 0px 2px 0px inset |

![Confirm button default](components/crops/bk-confirm-default.png) ![Confirm button hover](components/crops/bk-confirm-hover.png) ![Confirm button focus-visible](components/crops/bk-confirm-focus-visible.png) ![Confirm button pressed](components/crops/bk-confirm-pressed.png)

### Booking page, dark

The same booker under its supported ?theme=dark&embed=true mode — the only dark surface that paints signed out.

#### Dark booker canvas
The booking page under its supported ?theme=dark&embed=true mode: the real dark theme, not a forced class. Read as `bkd-canvas` on the booking (dark) page.

**Values (default).** size 1440 x 900; background transparent; text Inter 14/20 600, #a3a3a3; icon 16 x 16, #d4d4d4; layers div.[--booker-timeslots-width:240px].lg:[--booker-timeslots-width:280px] 1040.0x489.8 rgb(23, 23, 23) T:1px solid rgb(38, 38, 38) / R:1px solid rgb(38, 38, 38) / B:1px solid rgb(38, 38, 38) / L:1px solid rgb(38, 38, 38) 8px; span::before.current-timezone.flex 163pxx28px rgb(38, 38, 38) 8px; div.font-normal.border-default 121.6x36.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px.

Child layers that carry the look: div 1040x489.8 background #171717 border 1px solid #262626 `color.paint.emphasis-auth` radius 8px; span::before 163pxx28px background #262626 `color.paint.emphasis-auth` radius 8px; div 121.6x36 radius 10px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px.

![Dark booker canvas default](components/crops/bkd-canvas-default.png)

#### Dark event title
Read as `bkd-title` on the booking (dark) page.

**Values (default).** size 232 x 28; background transparent; text Inter 20/28 600, #d4d4d4.

![Dark event title default](components/crops/bkd-title-default.png)

#### Dark calendar
Read as `bkd-calendar` on the booking (dark) page.

**Values (default).** size 439 x 375.78; background transparent; text Inter 14/20 300, #d4d4d4; layers button.disabled:text-bookinglighter.absolute 59.3x59.3 T:2px solid rgba(0, 0, 0, 0) / R:2px solid rgba(0, 0, 0, 0) / B:2px solid rgba(0, 0, 0, 0) / L:2px solid rgba(0, 0, 0, 0) 8px; button.disabled:text-bookinglighter.absolute 59.3x59.3 T:2px solid rgba(0, 0, 0, 0) / R:2px solid rgba(0, 0, 0, 0) / B:2px solid rgba(0, 0, 0, 0) / L:2px solid rgba(0, 0, 0, 0) 8px; button.disabled:text-bookinglighter..

Child layers that carry the look: button 59.3x59.3 border 2px solid transparent radius 8px; button 59.3x59.3 border 2px solid transparent radius 8px; button 59.3x59.3 border 2px solid transparent radius 8px.

![Dark calendar default](components/crops/bkd-calendar-default.png)

#### Dark time slot
A dark-mode slot button; measured, never followed. Read as `bkd-slot` on the booking (dark) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 239 x 36; padding 8px 10px; border 1px solid #4d4d4d; radius 10px; background #0f0f0f `color.cal.brand-emphasis`; shadow rgba(0, 0, 0, 0.03) 0px 2px 3px 0px, rgba(0, 0, 0, 0.03) 0px 2px 2px -1px; text Inter 14/14 500, #d4d4d4; transition box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #fafafa; background #171717; text Inter 14/14 500, #fafafa |
| focus-visible | background #262626 `color.paint.emphasis-auth`; shadow rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(255, 255, 255, 0.2) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 0px 0px 2px |
| pressed | border 1px solid #fafafa; background #171717; shadow rgba(0, 0, 0, 0.05) 0px 2px 1px 0px inset; text Inter 14/14 500, #fafafa |

![Dark time slot default](components/crops/bkd-slot-default.png) ![Dark time slot hover](components/crops/bkd-slot-hover.png) ![Dark time slot focus-visible](components/crops/bkd-slot-focus-visible.png) ![Dark time slot pressed](components/crops/bkd-slot-pressed.png)

### Auth cards

The login and signup cards on app.cal.com, captured as the boundary of the signed-in product: SSO buttons, fields and actions measured, never filled or followed.

#### Login card
The sign-in card on app.cal.com: SSO buttons, the email and password fields, Forgot?, Continue. Captured as a boundary — never filled or submitted. Read as `auth-card` on the log in page.

**Values (default).** size 446 x 516; padding 40px; background transparent; text fontHeading 20/28 700, #070a0d `color.cal.bg-inverted`; icon 16 x 16, #262626 `color.paint.emphasis-auth`; layers button.relative.inline-flex 366.0x36.0 lab(15.204 0 -0.00000596046) T:1px solid lab(15.204 0 -0.00000596046) / R:1px solid lab(15.204 0 -0.00000596046) / B:1px solid lab(15.204 0 -0.00000596046) / L:1px solid lab(15.204 0 -0.00000596046) oklab(0.999994 0.0000455678 0.0000200868 / 0.16) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0.

Child layers that carry the look: button 366x36 background #262626 `color.paint.emphasis-auth` border 1px solid #262626 `color.paint.emphasis-auth` radius 10px shadow rgba(254, 254, 254, 0.16) 0px 1px 0px 0px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(38, 38, 38, 0.24) 0px 1px 2px 0px; button 366x36 background rgba(17, 16, 16, 0.04) border 1px solid transparent radius 10px; div 160.2x1 background rgba(17, 16, 16, 0.08).

![Login card default](components/crops/auth-card-default.png)

#### Login title
The "Welcome back! Sign in to continue" heading. Read as `auth-title` on the log in page.

**Values (default).** size 366 x 20; background transparent; text fontSans 14/20 400, #696969 `color.paint.muted-auth`.

![Login title default](components/crops/auth-title-default.png)

#### Google SSO
The Sign-in-with-Google button; measured never followed. Read as `sso-google` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 366 x 36; padding 0px 13px; border 1px solid #262626 `color.paint.emphasis-auth`; radius 10px; background #262626 `color.paint.emphasis-auth`; shadow rgba(254, 254, 254, 0.16) 0px 1px 0px 0px inset, rgba(38, 38, 38, 0.24) 0px 1px 2px 0px; text fontSans 14/20 500, #f9f9f9; transition box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | background rgba(38, 38, 38, 0.9) |
| focus-visible | shadow rgba(254, 254, 254, 0.16) 0px 1px 0px 0px inset, #ffffff 0px 0px 0px 1px, #a0a0a0 0px 0px 0px 3px, rgba(38, 38, 38, 0.24) 0px 1px 2px 0px |
| pressed | background rgba(38, 38, 38, 0.9); shadow rgba(17, 16, 17, 0.08) 0px 1px 0px 0px inset |

![Google SSO default](components/crops/sso-google-default.png) ![Google SSO hover](components/crops/sso-google-hover.png) ![Google SSO focus-visible](components/crops/sso-google-focus-visible.png) ![Google SSO pressed](components/crops/sso-google-pressed.png)

#### Email field
The email input; focused by a click, never typed into or submitted. Read as `email-field` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 364 x 30; padding 0px 11px; radius 10px; background transparent; text fontSans 14/30 400, #262626 `color.paint.emphasis-auth`; transition background-color 5e+06s ease-in-out; placeholder #262626 `color.paint.emphasis-auth` |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png)

#### Password field
The password input; focused by a click, never typed into or submitted. Read as `pass-field` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 337 x 30; padding 0px 8px 0px 11px; background transparent; text fontSans 14/30 400, #262626 `color.paint.emphasis-auth`; transition background-color 5e+06s ease-in-out; placeholder #262626 `color.paint.emphasis-auth` |

![Password field default](components/crops/pass-field-default.png) ![Password field focused](components/crops/pass-field-focused.png)

#### Forgot link
The "Forgot?" password link. Read as `forgot-link` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 51.25 x 20; background transparent; text fontSans 14/20 400, #696969 `color.paint.muted-auth` |
| hover | text fontSans 14/20 400, #262626 `color.paint.emphasis-auth` |
| focus-visible | outline 1px auto rgba(160, 160, 160, 0.5), offset 1px; layers a.col-start-2.row-start-1 51.3x20.0 1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5) offset 1px |
| pressed | text fontSans 14/20 400, #262626 `color.paint.emphasis-auth` |

![Forgot link default](components/crops/forgot-link-default.png) ![Forgot link hover](components/crops/forgot-link-hover.png) ![Forgot link focus-visible](components/crops/forgot-link-focus-visible.png) ![Forgot link pressed](components/crops/forgot-link-pressed.png)

#### Continue button
The sign-in submit; measured only, never clicked (pressed is CDP-forced). Read as `continue-btn` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 366 x 36; padding 0px 13px; border 1px solid #262626 `color.paint.emphasis-auth`; radius 10px; background #262626 `color.paint.emphasis-auth`; shadow rgba(254, 254, 254, 0.16) 0px 1px 0px 0px inset, rgba(38, 38, 38, 0.24) 0px 1px 2px 0px; text fontSans 14/20 500, #f9f9f9; transition box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | background rgba(38, 38, 38, 0.9) |
| focus-visible | shadow rgba(254, 254, 254, 0.16) 0px 1px 0px 0px inset, #ffffff 0px 0px 0px 1px, #a0a0a0 0px 0px 0px 3px, rgba(38, 38, 38, 0.24) 0px 1px 2px 0px |
| pressed | background rgba(38, 38, 38, 0.9); shadow rgba(17, 16, 17, 0.08) 0px 1px 0px 0px inset |

![Continue button default](components/crops/continue-btn-default.png) ![Continue button hover](components/crops/continue-btn-hover.png) ![Continue button focus-visible](components/crops/continue-btn-focus-visible.png) ![Continue button pressed](components/crops/continue-btn-pressed.png)

#### SAML link
The "Sign in with SAML/OIDC" action. Read as `saml-link` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 163.81 x 32; border 1px solid transparent; radius 10px; background transparent; text fontSans 14/20 500, #262626 `color.paint.emphasis-auth`; transition box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | shadow #ffffff 0px 0px 0px 1px, #a0a0a0 0px 0px 0px 3px |

![SAML link default](components/crops/saml-link-default.png) ![SAML link hover](components/crops/saml-link-hover.png) ![SAML link focus-visible](components/crops/saml-link-focus-visible.png) ![SAML link pressed](components/crops/saml-link-pressed.png)

#### Signup title
The "Claim cal.com/you" heading on the signup card. Read as `signup-title` on the sign up page.

**Values (default).** size 440 x 112; background transparent; text fontHeading 56/56 700, #262626 `color.paint.emphasis-auth`.

![Signup title default](components/crops/signup-title-default.png)

#### Google continue
The Continue-with-Google button; measured never followed. Read as `signup-google` on the sign up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 440 x 40; padding 0px 15px; border 1px solid #262626 `color.paint.emphasis-auth`; radius 14px; background #262626 `color.paint.emphasis-auth`; shadow rgba(254, 254, 254, 0.16) 0px 1px 0px 0px inset, rgba(38, 38, 38, 0.24) 0px 1px 2px 0px; text fontSans 16/24 500, #f9f9f9; transition box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | background rgba(38, 38, 38, 0.9) |
| focus-visible | shadow rgba(254, 254, 254, 0.16) 0px 1px 0px 0px inset, #ffffff 0px 0px 0px 1px, #a0a0a0 0px 0px 0px 3px, rgba(38, 38, 38, 0.24) 0px 1px 2px 0px |
| pressed | background rgba(38, 38, 38, 0.9); shadow rgba(17, 16, 17, 0.08) 0px 1px 0px 0px inset |

![Google continue default](components/crops/signup-google-default.png) ![Google continue hover](components/crops/signup-google-hover.png) ![Google continue focus-visible](components/crops/signup-google-focus-visible.png) ![Google continue pressed](components/crops/signup-google-pressed.png)

#### Email continue
The Continue-with-Email button; measured never followed. Read as `signup-email` on the sign up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 440 x 40; padding 0px 15px; border 1px solid rgba(17, 16, 16, 0.1); radius 14px; background #ffffff `color.hp.page`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text fontSans 16/24 500, #262626 `color.paint.emphasis-auth`; transition box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 18 x 18, #262626 `color.paint.emphasis-auth`; layers ::before rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, lab(5.06335 -0.00000745058 -0.00000298023 / 0.04) 0px 1px 0px 0px 1 |
| hover | background rgba(17, 16, 16, 0.02) |
| focus-visible | shadow #ffffff 0px 0px 0px 1px, #a0a0a0 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |
| pressed | background rgba(17, 16, 16, 0.02); shadow none; layers ::before rgba(0, 0, 0, 0) 0px none 1 |

![Email continue default](components/crops/signup-email-default.png) ![Email continue hover](components/crops/signup-email-hover.png) ![Email continue focus-visible](components/crops/signup-email-focus-visible.png) ![Email continue pressed](components/crops/signup-email-pressed.png)

#### Trust row
The rating row (Trustpilot / Product Hunt / G2) beside the signup card. Read as `trust-row` on the sign up page.

**Values (default).** size 78 x 13; background transparent; text fontSans 13/13 400, #696969 `color.paint.muted-auth`.

![Trust row default](components/crops/trust-row-default.png)

#### Signup card
The signup card on app.cal.com: Continue-with-SSO buttons and the plan pitch. Captured as a boundary — never followed. Read as `signup-card` on the sign up page.

**Values (default).** size 440 x 184; background transparent; text fontSans 16/24 500, #f9f9f9; icon 18 x 18, #262626 `color.paint.emphasis-auth`; layers button.relative.inline-flex 440.0x40.0 lab(15.204 0 -0.00000596046) T:1px solid lab(15.204 0 -0.00000596046) / R:1px solid lab(15.204 0 -0.00000596046) / B:1px solid lab(15.204 0 -0.00000596046) / L:1px solid lab(15.204 0 -0.00000596046) oklab(0.999994 0.0000455678 0.0000200868 / 0.16) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0.

Child layers that carry the look: button 440x40 background #262626 `color.paint.emphasis-auth` border 1px solid #262626 `color.paint.emphasis-auth` radius 14px shadow rgba(254, 254, 254, 0.16) 0px 1px 0px 0px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(38, 38, 38, 0.24) 0px 1px 2px 0px; button 440x40 background #ffffff `color.hp.page` border 1px solid rgba(17, 16, 16, 0.1) radius 14px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; button::before 438pxx38px radius 9px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(17, 16, 17, 0.04) 0px 1px 0px 0px.

![Signup card default](components/crops/signup-card-default.png)

### Footer

The near-black footer: link columns and social links.

#### Footer
The near-black footer: link columns, app-store badges, social links. Read as `footer` on the home page.

**Values (default).** size 1440 x 1487.31; background #111111 `color.hp.text`; text calSans 14/21 400, rgba(254, 254, 254, 0.6); icon 16 x 16, rgba(254, 254, 254, 0.85).

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 118.47 x 16; background transparent; text calSans 14/21 400, rgba(254, 254, 254, 0.6); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text calSans 14/21 400, #ffffff `color.hp.page` |
| focus-visible | outline 1px auto rgba(156, 162, 174, 0.5), offset 1px; layers a.text-white/85 118.5x16.0 1px auto oklab(0.713643 -0.00286406 -0.0189429 / 0.5) offset 1px |
| pressed | text calSans 14/21 400, #ffffff `color.hp.page` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Mobile (390 wide)

The marketing surface at phone width: the same glass bar, a full-screen menu drawer and 42px display type.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 374 x 64; padding 0px 14px; radius 18px; background rgba(244, 244, 244, 0.72) `color.paint.bar`; text calSans 14/21 500, #ffffff `color.hp.page`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The nav menu toggle at 390px. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 36 x 36; border 1px solid transparent; radius 10px; background transparent; text calSans 16/24 500, #242424 `color.hp.ink`; transition box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 18 x 18, #242424 `color.hp.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The full-screen nav drawer opened by its own toggle. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; border L: 1px solid #e5e7eb `color.hp.well`; background #ffffff `color.hp.page`; shadow rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px; text calSans 16/24 500, #242424 `color.hp.ink`; transition opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1), translate 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #242424 `color.hp.ink`; layers ::before rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0 0 0 / 0.04) 0px 1px 0px 0px 1.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
A link inside the opened nav drawer. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 341 x 48; padding 12px; radius 10px; background transparent; text calSans 16/24 500, #242424 `color.hp.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | shadow rgba(36, 35, 35, 0.4) 0px 0px 0px 2px; layers a.flex.w-full 341.0x48.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.260318 0.0000118539 0.00000520051 / 0.4) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 10px |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 346 x 136.08; background transparent; text calSans 42/45.36 700, #242424 `color.hp.ink`; icon 8.13 x 8.13, #cc4510 `color.hp.accent`; layers span.relative.inline-block 63.0x41.2 rgb(243, 244, 246) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(229, 231, 235) 0px 0px 0px 1px inset 8.4px; canvas.block.size-full 63.0x41.2 rgb(227, 220, 205); canvas.block.size-full 63.0x41.2 rgb(227, 220, 205); canvas.block.size-full 63.0x41.2 rgb(227, 220, 205); s.

Child layers that carry the look: span 63x41.2 background #f3f4f6 `color.hp.field` radius 8.4px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #e5e7eb `color.hp.well` 0px 0px 0px 1px inset; canvas 63x41.2 background #e3dccd; canvas 63x41.2 background #e3dccd.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Cal.com wordmark, the Google/Microsoft/Twitter marks, the chevrons and calendar glyphs) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The Cal.com product itself lives behind app.cal.com — the scheduler, event-type editor, availability, bookings list, workflows, insights, settings and team management all need an account and were never reached. The login and signup cards on app.cal.com were captured as that boundary: measured as forms, never filled or submitted. A signed-in pass would add the real product coverage this package deliberately lacks.

### Pages

- **The app.** Every post-login surface on app.cal.com was never reached; only the /auth/login and /signup cards were measured.
- **Signup and SSO.** Every Get-started, Sign-up-with and Continue action was measured, never followed; no account was created.
- **Booking completion.** The guest-details form opens locally on a slot press; it was measured and never filled or confirmed, so no booking exists.
- **Booking-page variants.** The captured page is one user's event type (cal.com/peer); other hosts' pages vary in brand colour, layout and fields.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface (past days paint disabled styling only inside the grid).
- **FAQ answers** stay closed: the accordion questions were measured, never expanded.
- **The mobile menu** drawer was captured open at phone width; its nested sub-menus were not opened.

### Themes

The marketing pages are light-only — their stylesheets declare --color-hp-* dark overrides but no dark marketing page paints signed out, so tokens.json does not export them as a theme. The public booking page does paint dark under its supported ?theme=dark&embed=true mode; tokens.json keeps those roles in the dark set.

### Fonts

- **calSans** (marketing), **fontSans**/**fontHeading** (the app.cal.com auth cards) and **Inter** (the booking page) are the served faces. They are served from Cal.com's CDN; the style guide falls back to system sans.

### Screenshots

- The product mocks, calendar artwork, customer logos, the Cal.com wordmark and any photography in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Blog articles, feature copy, customer stories and docs are the product's content; only frames and components were measured.
