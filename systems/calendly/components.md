# Calendly components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from calendly.com on 2026-11-12, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. calendly.com is two products signed out: the marketing site (Astro + Tailwind, Geist / Calendly Sans / Wulkan Text) and the public invitee booking pages (/calendly-demo, a separate application in Proxima Nova). Nothing was signed into, booked or submitted; the login and signup forms were never filled; a booking day was selected for measurement but no time slot was ever confirmed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (47 components, 119 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (117 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light` (the marketing .dark islands appear inside light shots). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Scheduling (product page) | `/scheduling` | [default](screenshots/scheduling-light-default.png), [full](screenshots/scheduling-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [yearly](screenshots/pricing-light-yearly.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Enterprise solution | `/solutions/enterprise` | [default](screenshots/solutions-light-default.png), [full](screenshots/solutions-light-full.png) |
| Log in | `/login` | [default](screenshots/login-light-default.png) |
| Sign up | `/signup` | [default](screenshots/signup-light-default.png) |
| Booking profile (invitee) | `/calendly-demo` | [default](screenshots/booking-light-default.png), [full](screenshots/booking-light-full.png) |
| Booking event (invitee) | `/calendly-demo/dog-nail-trim-shampoo-small` | [day](screenshots/booking-event-light-day.png), [default](screenshots/booking-event-light-default.png), [full](screenshots/booking-event-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Booking event, phone | `/calendly-demo/dog-nail-trim-shampoo-small` | [default](screenshots/mobile-booking-event-light-default.png), [full](screenshots/mobile-booking-event-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the hamburger button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |
| Products mega-menu | every marketing page | the nav trigger's own hover | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-dropdown), [menu-link](#menu-link) |
| OneTrust / Ketch / Intercom overlays | every page | hidden, never answered (no consent button was ever clicked, no consent POST sent) | hidden before every shot and reading |
| Billing-period radio | /pricing | the Monthly/Yearly radio's own toggle | [pricing-light-yearly](screenshots/pricing-light-yearly.png), [billing-radio](#billing-radio) |
| Booking day selection | booking event page | an enabled day cell's own click — a time slot was never confirmed, nothing was booked | [booking-event-light-day](screenshots/booking-event-light-day.png), [bk-day-selected](#day-cell-selected) |
| Signed-in product | app.calendly.com workspace | the scheduling workspace lives behind /app/login | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 21 components were given a real keyboard focus. 11 draw an outline ring: `nav-login` (2px solid #6bb1ff `color.brand.cornflower`, offset -2px), `menu-link` (2px solid #6bb1ff `color.brand.cornflower`, offset 0px), `signup-email` (2px solid #6bb1ff `color.brand.cornflower`, offset 0px), `plan-cta` (2px solid #6bb1ff `color.brand.cornflower`, offset -2px), `icon-button` (2px solid #6bb1ff `color.brand.cornflower`, offset 0px), `bk-day` (2px solid #0099ff, offset 2px), `bk-timeslot` (2px solid #0099ff, offset 2px), `bk-timezone` (2px solid #0099ff, offset 2px), `sso-btn` (2px solid #6bb1ff `color.brand.cornflower`, offset -2px), `footer-link` (2px solid #6bb1ff `color.brand.cornflower`, offset 0px), `m-nav-item` (2px solid #6bb1ff `color.brand.cornflower`, offset -1px). 4 change only their border: `nav-sales`, `nav-cta`, `signup-google`, `continue-btn`. The other 6 show no measured change: `nav-trigger`, `nav-link`, `billing-radio`, `feature-tip`, `bk-poweredby`, `bk-event`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease` | border-color | bk-event |
| 0.1s | `ease-in` | all | bk-poweredby |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, box-shadow, color, fill, opacity, outline-color, stroke, text-decoration-color | continue-btn, email-field, footer-link, icon-button, menu-link, nav-cta, nav-login, nav-sales and more |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | box-shadow | header, m-header |
| 0.22s | `ease-out` | all | bk-panel |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | opacity, visibility | m-menu-open |
| 0.3s | `ease` | transform, width | bk-timeslot |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Hero card](#hero-card) | 920 x 408.84 | - | 48px | #fcfbf8 `color.neutral.magnolia` | none | 48px |
| [Plan card](#plan-card) | 266 x 300.98 | - | 40px | #ffffff `color.neutral.white` | rgba(95, 109, 119, 0.04) 0px 4px 5px 0px, rgba(95, 109, 119, 0.03) 0px 8px 15px 0px, rgba(95, 109, 119, 0.06) 0px 15px 30px 0px | 24px |
| [Login card](#login-card) | 464 x 500.36 | - | 48px | #ffffff `color.neutral.white` | rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px | 32px 48px |
| [Signup card](#signup-card) | 912 x 579.55 | - | 48px | #ffffff `color.neutral.white` | rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px | 32px 48px |
| [Event link](#event-link) | 360 x 199.97 | T: 1px solid #d4e0ed `color.booking.hairline`; R: 1px solid transparent; B: 1px solid transparent; L: 1px solid transparent | - | transparent | none | 20px |
| [Booking panel](#booking-panel) | 1058 x 698 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The marketing chrome on the magnolia field: wordmark, the Products mega-menu trigger, plain links, Log In and the midnight Get-started pill.

#### Header
The sticky marketing header: wordmark, the Product/Solutions/Resources dropdowns, Pricing, Talk to sales, Log In and the dark Get-started pill. Read as `header` on the home page.

**Values (default).** size 1440 x 68; background #fcfbf8 `color.neutral.magnolia`; text Geist 14/19.6 500, #071a31 `color.neutral.midnight`; transition box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 32 x 32, #000000 `color.neutral.black`.

![Header default](components/crops/header-default.png)

#### Logo
The Calendly wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 156.28 x 32; radius 8px; background transparent; text Geist 16/16 400, #000000 `color.neutral.black`; icon 32 x 32, #000000 `color.neutral.black`.

![Logo default](components/crops/logo-default.png)

#### Nav trigger
The Product button that opens the header mega-menu; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 87.66 x 35.59; padding 8px; radius 16px; background transparent; text Geist 14/19.6 500, #071a31 `color.neutral.midnight`; icon 16 x 16, #071a31 `color.neutral.midnight` |

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav link
The plain Pricing header link. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 61.72 x 35.59; padding 8px; background transparent; text Geist 14/19.6 500, #071a31 `color.neutral.midnight` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Sales link
The Talk-to-sales header action; measured never followed. Read as `nav-sales` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 94.34 x 48; padding 8px 4px; border 2px solid transparent; radius 16px; background transparent; text Geist 14/19.6 500, #071a31 `color.neutral.midnight`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Geist 14/19.6 500, #5f6d77 `color.neutral.steel` |
| focus-visible | border 2px solid #6bb1ff `color.brand.cornflower` |
| pressed | text Geist 14/19.6 500, #1e5ea7 `color.brand.cobalt` |

![Sales link default](components/crops/nav-sales-default.png) ![Sales link hover](components/crops/nav-sales-hover.png) ![Sales link focus-visible](components/crops/nav-sales-focus-visible.png) ![Sales link pressed](components/crops/nav-sales-pressed.png)

#### Login link
The Log-In header action (outlined pill); measured never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73.33 x 48; padding 12px 16px; border 1px solid #071a31 `color.neutral.midnight`; radius 16px; background transparent; text Geist 14/19.6 400, #071a31 `color.neutral.midnight`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #071a31 `color.neutral.midnight`; text Geist 14/19.6 400, #fcfbf8 `color.neutral.magnolia` |
| focus-visible | border 1px solid transparent; outline 2px solid #6bb1ff `color.brand.cornflower`, offset -2px |
| pressed | border 1px solid #0e396a `color.brand.navy`; background #0e396a `color.brand.navy`; text Geist 14/19.6 400, #fcfbf8 `color.neutral.magnolia` |

![Login link default](components/crops/nav-login-default.png) ![Login link hover](components/crops/nav-login-hover.png) ![Login link focus-visible](components/crops/nav-login-focus-visible.png) ![Login link pressed](components/crops/nav-login-pressed.png)

#### Nav CTA
The Get-started-for-free dark pill; measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 158.73 x 48; padding 12px 16px; border 2px solid transparent; radius 16px; background #071a31 `color.neutral.midnight`; text Geist 14/19.6 400, #fcfbf8 `color.neutral.magnolia`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #0e396a `color.brand.navy` |
| focus-visible | border 2px solid #6bb1ff `color.brand.cornflower` |
| pressed | background #1e5ea7 `color.brand.cobalt` |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Nav dropdown
The Product mega-menu panel, opened by its own trigger. Read as `nav-dropdown` on the home page.

**Values (default).** size 304 x 398.5; padding 32px; background #ffffff `color.neutral.white`; text Geist 12/12 500, #5f6d77 `color.neutral.steel`; icon 36 x 36, #000000 `color.neutral.black`.

![Nav dropdown default](components/crops/nav-dropdown-default.png)

#### Menu link
A feature link inside the opened mega-menu. Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 240 x 56.5; padding 8px; radius 24px; background transparent; text Geist 16/22 500, #071a31 `color.neutral.midnight`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 36 x 36, #000000 `color.neutral.black` |
| hover | background #f5f3ee `color.neutral.linen` |
| focus-visible | outline 2px solid #6bb1ff `color.brand.cornflower`, offset 0px; layers a.keyboard-focus-before.group 240.0x56.5 2px solid rgb(107, 177, 255) offset 0px 24px |

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link focus-visible](components/crops/menu-link-focus-visible.png)

### Home hero

The 72px Calendly Sans hero, the Google/email sign-up actions and the gradient hero card.

#### Hero headline
The 72px Calendly-Sans display headline inside the dark hero island. Read as `hero-title` on the home page.

**Values (default).** size 640 x 158.38; background transparent; text Calendly Sans 72/79.2 500, #fcfbf8 `color.neutral.magnolia`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The 18px lede under the headline, Geist on the dark island. Read as `hero-lede` on the home page.

**Values (default).** size 560 x 50.38; background transparent; text Geist 18/25.2 400, #fcfbf8 `color.neutral.magnolia`.

![Hero copy default](components/crops/hero-lede-default.png)

#### Google signup button
The light Sign-up-with-Google pill in the dark hero; measured never followed. Read as `signup-google` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 224.03 x 50; padding 12px 20px; border 1px solid #fcfbf8 `color.neutral.magnolia`; radius 20px; background #fcfbf8 `color.neutral.magnolia`; text Geist 16/22.4 500, #071a31 `color.neutral.midnight`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #c1defe `color.brand.sky`; background #c1defe `color.brand.sky` |
| focus-visible | border 1px solid #6bb1ff `color.brand.cornflower` |
| pressed | border 1px solid #6bb1ff `color.brand.cornflower`; background #6bb1ff `color.brand.cornflower` |

![Google signup button default](components/crops/signup-google-default.png) ![Google signup button hover](components/crops/signup-google-hover.png) ![Google signup button focus-visible](components/crops/signup-google-focus-visible.png) ![Google signup button pressed](components/crops/signup-google-pressed.png)

#### Email signup link
The underlined Sign-up-with-email link under the OAuth buttons; measured never followed. Read as `signup-email` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 100.77 x 16; radius 8px; background transparent; text Geist 12/16.8 400, #fcfbf8 `color.neutral.magnolia`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.8 |
| focus-visible | outline 2px solid #6bb1ff `color.brand.cornflower`, offset 0px; layers a.keyboard-focus-before.underline 100.8x16.0 2px solid rgb(107, 177, 255) offset 0px 8px |
| pressed | opacity 0.8 |

![Email signup link default](components/crops/signup-email-default.png) ![Email signup link hover](components/crops/signup-email-hover.png) ![Email signup link focus-visible](components/crops/signup-email-focus-visible.png) ![Email signup link pressed](components/crops/signup-email-pressed.png)

#### Hero card
The painted island behind the hero (the .dark section card). Read as `hero-card` on the home page.

**Values (default).** size 920 x 408.84; padding 48px; radius 48px; background #fcfbf8 `color.neutral.magnolia`; text Calendly Sans 16/16 500, #071a31 `color.neutral.midnight`; icon 24 x 24, #000000 `color.neutral.black`.

![Hero card default](components/crops/hero-card-default.png)

### Home

Sections of the home page: the Wulkan serif headings and the neutral badge chip.

#### Section heading (serif)
A 48px Wulkan-Text section heading in the light sections. Read as `h2-serif` on the home page.

**Values (default).** size 320 x 118.78; background transparent; text Geist 36/39.6 500, #071a31 `color.neutral.midnight`.

![Section heading (serif) default](components/crops/h2-serif-default.png)

#### Badge
A "Beta"/"New" chip (rounded-ui-xxs). Read as `badge` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 42.38 x 24.8; padding 4px 8px; radius 8px; background rgba(7, 26, 49, 0.05) `color.neutral.alpha.midnight-a05`; text Geist 12/16.8 500, #3d464e `color.ramp.neutral.700` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Badge default](components/crops/badge-default.png) ![Badge hover](components/crops/badge-hover.png) ![Badge pressed](components/crops/badge-pressed.png)

### Pricing

The pricing surface: the Monthly/Yearly radio, the white plan cards with their midnight CTAs and the icon buttons on feature rows.

#### Pricing title
The pricing page display heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 640 x 105.59; background transparent; text Calendly Sans 48/52.8 500, #071a31 `color.neutral.midnight`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Billing toggle
A Billed-monthly/Billed-yearly radio label; the yearly option was toggled for the screenshot state, never checked out. Read as `billing-radio` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 108.27 x 20; background transparent; text Geist 14/19.6 500, #071a31 `color.neutral.midnight`; layers span.flex.size-5 20.0x20.0 rgb(255, 255, 255) T:1px solid rgb(7, 26, 49) / R:1px solid rgb(7, 26, 49) / B:1px solid rgb(7, 26, 49) / L:1px solid rgb(7, 26, 49) 3.35544e+07px; span.size-3.rounded-full 12.0x12.0 rgb(7, 26, 49) 3.35544e+07px |
| focus-visible | layers span.flex.size-5 20.0x20.0 rgb(255, 255, 255) T:1px solid rgb(7, 26, 49) / R:1px solid rgb(7, 26, 49) / B:1px solid rgb(7, 26, 49) / L:1px solid rgb(7, 26, 49) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(107, 177, 255, 0.3) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 3.35544e+07px; span.size-3.rounded-full 12.0x12.0 rgb(7, 26, 49 |

Child layers that carry the look: span 20x20 background #ffffff `color.neutral.white` border 1px solid #071a31 `color.neutral.midnight` radius 3.35544e+07px; span 12x12 background #071a31 `color.neutral.midnight` radius 3.35544e+07px.

![Billing toggle default](components/crops/billing-radio-default.png) ![Billing toggle hover](components/crops/billing-radio-hover.png) ![Billing toggle focus-visible](components/crops/billing-radio-focus-visible.png) ![Billing toggle pressed](components/crops/billing-radio-pressed.png)

#### Plan name
A plan card's name (h3, Calendly Sans). Read as `plan-name` on the pricing page.

**Values (default).** size 66.78 x 39.59; background transparent; text Calendly Sans 36/39.6 500, #071a31 `color.neutral.midnight`.

![Plan name default](components/crops/plan-name-default.png)

#### Plan price
A plan card's price figure. Read as `plan-price` on the pricing page.

**Values (default).** size 67.97 x 52.8; background transparent; text Wulkan Text 48/52.8 500, #071a31 `color.neutral.midnight`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan card's Get-started action; measured never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 218 x 50; padding 12px 20px; border 1px solid #071a31 `color.neutral.midnight`; radius 20px; background transparent; text Geist 16/22.4 500, #071a31 `color.neutral.midnight`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #071a31 `color.neutral.midnight` |
| hover | background #071a31 `color.neutral.midnight`; text Geist 16/22.4 500, #fcfbf8 `color.neutral.magnolia`; icon 24 x 24, #fcfbf8 `color.neutral.magnolia` |
| focus-visible | border 1px solid transparent; outline 2px solid #6bb1ff `color.brand.cornflower`, offset -2px |
| pressed | border 1px solid #0e396a `color.brand.navy`; background #0e396a `color.brand.navy`; text Geist 16/22.4 500, #fcfbf8 `color.neutral.magnolia`; icon 24 x 24, #fcfbf8 `color.neutral.magnolia` |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan card
A pricing plan card (the painted ancestor of the plan name). Read as `plan-card` on the pricing page.

**Values (default).** size 266 x 300.98; padding 24px; radius 40px; background #ffffff `color.neutral.white`; shadow rgba(95, 109, 119, 0.04) 0px 4px 5px 0px, rgba(95, 109, 119, 0.03) 0px 8px 15px 0px, rgba(95, 109, 119, 0.06) 0px 15px 30px 0px; text Calendly Sans 36/39.6 500, #071a31 `color.neutral.midnight`; icon 24 x 24, #071a31 `color.neutral.midnight`.

![Plan card default](components/crops/plan-card-default.png)

#### Icon button
A round icon-only expander (bg-iconbutton-bg). Read as `icon-button` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; border 1px solid rgba(7, 26, 49, 0.05) `color.neutral.alpha.midnight-a05`; radius 8px; background rgba(7, 26, 49, 0.05) `color.neutral.alpha.midnight-a05`; text Geist 16/16 400, #071a31 `color.neutral.midnight`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #071a31 `color.neutral.midnight`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | background rgba(7, 26, 49, 0.1) `color.neutral.alpha.midnight-a10` |
| focus-visible | border 1px solid transparent; outline 2px solid #6bb1ff `color.brand.cornflower`, offset 0px |
| pressed | background rgba(7, 26, 49, 0.2) `color.neutral.alpha.midnight-a20` |

![Icon button default](components/crops/icon-button-default.png) ![Icon button hover](components/crops/icon-button-hover.png) ![Icon button focus-visible](components/crops/icon-button-focus-visible.png) ![Icon button pressed](components/crops/icon-button-pressed.png)

#### Feature tooltip link
A dotted-underline feature name (opens a tooltip on hover, never clicked). Read as `feature-tip` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 274 x 39.19; background transparent; text Geist 14/19.6 400, #071a31 `color.neutral.midnight`; icon 28 x 8.5, #071a31 `color.neutral.midnight`; layers span.bg-midnight.text-magnolia 240.0x49.6 rgb(7, 26, 49) rgba(71, 103, 136, 0.04) 0px 4px 5px 0px, rgba(71, 103, 136, 0.03) 0px 8px 15px 0px, rgba(71, 103, 136, 0.06) 0px 15px 30px 0px 16px |
| focus-visible | layers span.cursor-pointer.underline 274.0x39.2 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(107, 177, 255, 0.3) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 8px; span.bg-midnight.text-magnolia 240.0x49.6 rgb(7, 26, 49) rgba(71, 103, 136, 0.04) 0px 4px 5px 0px, rgba(71, 103, 136, 0.03) 0px 8px 15px 0px, rgba(71, 103, 136, 0.06) 0px 15px 3 |

Child layers that carry the look: span 240x49.6 background #071a31 `color.neutral.midnight` radius 16px shadow rgba(71, 103, 136, 0.04) 0px 4px 5px 0px, rgba(71, 103, 136, 0.03) 0px 8px 15px 0px, rgba(71, 103, 136, 0.06) 0px 15px 30px 0px.

![Feature tooltip link default](components/crops/feature-tip-default.png) ![Feature tooltip link hover](components/crops/feature-tip-hover.png) ![Feature tooltip link focus-visible](components/crops/feature-tip-focus-visible.png) ![Feature tooltip link pressed](components/crops/feature-tip-pressed.png)

### Log in and sign up

The auth boundary cards, measured but never submitted: the 464px login card and the wider two-column signup card, fields and SSO buttons.

#### Login card
The centred login card; never filled or submitted. Read as `login-card` on the log in page.

**Values (default).** size 464 x 500.36; padding 32px 48px; radius 48px; background #ffffff `color.neutral.white`; shadow rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px; text Calendly Sans 36/39.6 500, #071a31 `color.neutral.midnight`; icon 16 x 16, #071a31 `color.neutral.midnight`.

![Login card default](components/crops/login-card-default.png)

#### Email field
The email input; sample text was typed and deleted, nothing sent. Read as `email-field` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 48.39; padding 12px 16px; border 1px solid #c6ccd2 `color.ramp.neutral.200`; radius 16px; background #ffffff `color.neutral.white`; text Geist 16/22.4 400, #071a31 `color.neutral.midnight`; transition border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder transparent |
| focused, filled | border 1px solid #6bb1ff `color.brand.cornflower`; shadow rgba(107, 177, 255, 0.3) 0px 0px 0px 4px |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png) ![Email field filled](components/crops/email-field-filled.png)

#### Continue button
The Continue-with-email submit; measured, never pressed (a press would submit). Read as `continue-btn` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 50.39; padding 12px 20px; border 2px solid transparent; radius 20px; background #071a31 `color.neutral.midnight`; text Geist 16/22.4 500, #fcfbf8 `color.neutral.magnolia`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #0e396a `color.brand.navy` |
| focus-visible | border 2px solid #6bb1ff `color.brand.cornflower` |
| pressed | background #1e5ea7 `color.brand.cobalt` |

![Continue button default](components/crops/continue-btn-default.png) ![Continue button hover](components/crops/continue-btn-hover.png) ![Continue button focus-visible](components/crops/continue-btn-focus-visible.png) ![Continue button pressed](components/crops/continue-btn-pressed.png)

#### SSO button
A Continue-with-Google/Microsoft button; measured, never followed. Read as `sso-btn` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 50; padding 12px 20px; border 1px solid #071a31 `color.neutral.midnight`; radius 20px; background transparent; text Geist 16/22.4 500, #071a31 `color.neutral.midnight`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #071a31 `color.neutral.midnight`; text Geist 16/22.4 500, #fcfbf8 `color.neutral.magnolia` |
| focus-visible | border 1px solid transparent; outline 2px solid #6bb1ff `color.brand.cornflower`, offset -2px |
| pressed | border 1px solid #0e396a `color.brand.navy`; background #0e396a `color.brand.navy`; text Geist 16/22.4 500, #fcfbf8 `color.neutral.magnolia` |

![SSO button default](components/crops/sso-btn-default.png) ![SSO button hover](components/crops/sso-btn-hover.png) ![SSO button focus-visible](components/crops/sso-btn-focus-visible.png) ![SSO button pressed](components/crops/sso-btn-pressed.png)

#### Signup card
The centred create-account card; never filled or submitted. Read as `signup-card` on the sign up page.

**Values (default).** size 912 x 579.55; padding 32px 48px; radius 48px; background #ffffff `color.neutral.white`; shadow rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px; text Calendly Sans 36/39.6 500, #071a31 `color.neutral.midnight`; icon 16 x 16, #071a31 `color.neutral.midnight`.

![Signup card default](components/crops/signup-card-default.png)

#### Signup email field
The signup email input; focused only, never filled or submitted. Read as `signup-field` on the sign up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 48.39; padding 12px 16px; border 1px solid #c6ccd2 `color.ramp.neutral.200`; radius 16px; background #ffffff `color.neutral.white`; text Geist 16/22.4 400, #071a31 `color.neutral.midnight`; transition border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder transparent |
| focused | border 1px solid #6bb1ff `color.brand.cornflower`; shadow rgba(107, 177, 255, 0.3) 0px 0px 0px 4px |

![Signup email field default](components/crops/signup-field-default.png) ![Signup email field focused](components/crops/signup-field-focused.png)

### Booking (invitee flow)

The public invitee surface on /calendly-demo: profile event cards, the month calendar, day cells, time slots and the timezone control — a separate application from the marketing site, in Proxima Nova.

#### Booking panel
The invitee page's centred panel (booking-kit), Proxima Nova. Read as `bk-panel` on the booking profile page.

**Values (default).** size 1058 x 698; background transparent; text Proxima Nova 16/24 700, #476788; transition all 0.22s ease-out; layers a.p5OOZEP33JytcHx09AGf.Y1etSIf8jWSCgzZ8N4ug 360.0x200.0 T:1px solid rgb(212, 224, 237) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0); div.E6A3_hj2CTqFJYH9gG_X.XNmY6Nya_0DuJwssmiqi 30.0x30.0 rgb(74, 145, 233) T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) 50%; div.eqojUi.

Child layers that carry the look: a 360x200 border 1px solid #d4e0ed `color.booking.hairline`; div 30x30 background #4a91e9 border 2px solid #ffffff `color.neutral.white` radius 50%; div 16x16 border 8px solid transparent.

![Booking panel default](components/crops/bk-panel-default.png)

#### Powered-by badge
The "POWERED BY Calendly" badge link; measured never followed. Read as `bk-poweredby` on the booking profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 105 x 105; background transparent; text Proxima Nova 8/9.6 700, #ffffff `color.neutral.white`; transition all 0.1s ease-in; layers ::before rgb(80, 89, 96) 0px none 1; ::after rgb(80, 89, 96) 0px none 1; a::before.ZZii_0xdazPEc5X7l3cZ.czPtBmyta3QIrHHLLfLR 6pxx6px rgb(80, 89, 96); a::after.ZZii_0xdazPEc5X7l3cZ.czPtBmyta3QIrHHLLfLR 6pxx6px rgb(80, 89, 96); div.wKVnbiJhcPutKB97Xm9w.FBx2fW8zQAzwOYlGYw3k 142.4x142.4 rgb(80, 89, 96) rgba(0, 0, 0, 0.2) 0px 2px 4px 0px |
| hover, focus-visible, pressed | size 109.2 x 109.2; transform scale(1.04); layers ::before rgb(0, 0, 0) 0px none 1; ::after rgb(0, 0, 0) 0px none 1; a::before.ZZii_0xdazPEc5X7l3cZ.czPtBmyta3QIrHHLLfLR 8pxx8px rgb(0, 0, 0); a::after.ZZii_0xdazPEc5X7l3cZ.czPtBmyta3QIrHHLLfLR 8pxx8px rgb(0, 0, 0); div.wKVnbiJhcPutKB97Xm9w.FBx2fW8zQAzwOYlGYw3k 148.1x148.1 rgb(64, 71, 76) rgba(0, 0, 0, 0.2) 0px 2px 4px 0px |

Child layers that carry the look: a::before 6pxx6px background #505960; a::after 6pxx6px background #505960; div 142.4x142.4 background #505960 shadow rgba(0, 0, 0, 0.2) 0px 2px 4px 0px.

![Powered-by badge default](components/crops/bk-poweredby-default.png) ![Powered-by badge hover](components/crops/bk-poweredby-hover.png) ![Powered-by badge focus-visible](components/crops/bk-poweredby-focus-visible.png) ![Powered-by badge pressed](components/crops/bk-poweredby-pressed.png)

#### Event link
An event-type link in the invitee list; measured, never opened by a press (the event page was navigated to directly). Read as `bk-event` on the booking profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 199.97; padding 20px; border T: 1px solid #d4e0ed `color.booking.hairline`; R: 1px solid transparent; B: 1px solid transparent; L: 1px solid transparent; background transparent; text Proxima Nova 16/22.4 700, #0a2540 `color.booking.ink`; transition border-color 0.1s ease |
| hover, focus-visible, pressed | background #e7edf6 |

![Event link default](components/crops/bk-event-default.png) ![Event link hover](components/crops/bk-event-hover.png) ![Event link focus-visible](components/crops/bk-event-focus-visible.png) ![Event link pressed](components/crops/bk-event-pressed.png)

#### Calendar
The month grid on the event page. Read as `bk-calendar` on the booking event page.

**Values (default).** size 399 x 452.59; background transparent; text Proxima Nova 14/21 700, #0a2540 `color.booking.ink`; icon 24 x 24, #a6bbd1 `color.booking.month-nav`; layers button.ukre8r9.u1rh2s45 40.0x40.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 9999px; button.ukre8r9.bosxatq 40.0x40.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 9999px; div.booking-kit_generated-7_cad3d51e 4.0x4.0 rgb(10, 37, 64) 50%; button..

Child layers that carry the look: button 40x40 border 1px solid transparent radius 9999px; button 40x40 border 1px solid transparent radius 9999px; div 4x4 background #0a2540 `color.booking.ink` radius 50%.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Month nav button
A previous/next-month arrow button; measured, never pressed. Read as `bk-month-nav` on the booking event page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40 x 40; padding 8px 16px; border 1px solid transparent; radius 9999px; background transparent; text Proxima Nova 14/21 400, #a6bbd1 `color.booking.month-nav`; icon 24 x 24, #a6bbd1 `color.booking.month-nav` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Day cell
An enabled day button in the calendar grid; one was selected for the times-panel state, never booked. Read as `bk-day` on the booking event page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 44 x 44; radius 50%; background #f4f8ff `color.booking.day-fill`; text Proxima Nova 14/21 400, #004eba `color.booking.blue-text` |
| focus-visible | outline 2px solid #0099ff, offset 2px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Day cell, selected
The picked day in its selected state (solid #006bff, locked disabled once picked). Read as `bk-day-selected` on the booking event page.

**Values (default).** size 44 x 44; radius 50%; background #006bff `color.booking.blue`; text Proxima Nova 14/21 400, #ffffff `color.neutral.white`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Time slot
An available time button in the revealed column; measured, never pressed (Next is never reached). Read as `bk-timeslot` on the booking event page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 278.39 x 52; padding 13px 10px; border 1px solid #006bff `color.booking.blue`; radius 8px; background transparent; text Proxima Nova 16/10 700, #004eba `color.booking.blue-text`; transition width 0.3s ease, transform 0.3s ease; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | border 2px solid #006bff `color.booking.blue` |
| focus-visible | border 2px solid #006bff `color.booking.blue`; outline 2px solid #0099ff, offset 2px |
| pressed | border 2px solid #006bff `color.booking.blue` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Timezone control
The timezone dropdown under the calendar (its list was never opened). Read as `bk-timezone` on the booking event page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 245.34 x 21; background transparent; text Proxima Nova 14/21 400, #0a2540 `color.booking.ink`; icon 16 x 16, #0a2540 `color.booking.ink` |
| focus-visible | outline 2px solid #0099ff, offset 2px; layers button.ukre8r9.booking-kit_dropdown-button_72cb6101 245.3x21.0 2px solid rgb(0, 153, 255) offset 2px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Day cell, today
Today's cell (aria-current="date"), an unavailable day here. Read as `bk-day-today` on the booking event page.

**Values (default).** size 44 x 44; radius 50%; background transparent; text Proxima Nova 14/21 400, #0a2540 `color.booking.ink`; layers div.booking-kit_generated-7_cad3d51e 4.0x4.0 rgb(10, 37, 64) 50%.

Child layers that carry the look: div 4x4 background #0a2540 `color.booking.ink` radius 50%.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Footer

The marketing footer: link columns on the magnolia field.

#### Footer
The footer card (a .dark island): link columns, legal and social. Read as `footer` on the home page.

**Values (default).** size 1440 x 1037.66; padding 24px; background #fcfbf8 `color.neutral.magnolia`; text ui-sans-serif 60/66 500, #fcfbf8 `color.neutral.magnolia`; icon 52 x 52, #000000 `color.neutral.black`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 71.91 x 19.59; radius 4px; background transparent; text Geist 14/19.6 400, rgba(252, 251, 248, 0.698) `color.neutral.alpha.magnolia-a70`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Geist 14/19.6 400, #fcfbf8 `color.neutral.magnolia` |
| focus-visible | outline 2px solid #6bb1ff `color.brand.cornflower`, offset 0px; layers a.keyboard-focus-before.inline-flex 71.9x19.6 2px solid rgb(107, 177, 255) offset 0px 4px |
| pressed | text Geist 14/19.6 400, #fcfbf8 `color.neutral.magnolia` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Mobile (390 wide)

The marketing surface at phone width: the compact header, the full-height menu overlay and the stacked hero.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 64; background #fcfbf8 `color.neutral.magnolia`; text Geist 14/19.6 500, #fcfbf8 `color.neutral.magnolia`; transition box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 32 x 32, #000000 `color.neutral.black`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The header menu toggle. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 24 x 24; radius 8px; background transparent; text Geist 16/16 400, #000000 `color.neutral.black`; icon 24 x 24, #000000 `color.neutral.black`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The header menu panel opened by its own toggle. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 780; background transparent; text Geist 16/22.4 500, #000000 `color.neutral.black`; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1), visibility 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #000000 `color.neutral.black`; layers button.absolute.inset-0 390.0x780.0 rgba(7, 26, 49, 0.2); div.absolute.top-0 390.0x780.0 rgb(252, 251, 248) T:1px solid rgba(7, 26, 49, 0.1); div._90SS5G_scrollFadeTop 390.0x40.0; button.keyboard-focus-before.[--kb-focus-offset:-1px] 390.0x57.0 B:1px solid rgba(7, 26, 49, 0.1); div.border-b.border-divider 390.0x651.0 rgb(255, 255, 255) B:1px solid rgba(7, 26, 49, 0.1); span.w-fit.inline-flex 42.4x.

Child layers that carry the look: button 390x780 background rgba(7, 26, 49, 0.2) `color.neutral.alpha.midnight-a20`; div 390x780 background #fcfbf8 `color.neutral.magnolia` border 1px solid rgba(7, 26, 49, 0.1) `color.neutral.alpha.midnight-a10`; div 390x40 image linear-gradient(#fcfbf8 `color.neutral.magnolia`, transparent).

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
An item inside the opened header menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 390 x 57; padding 8px 8px 8px 24px; border B: 1px solid rgba(7, 26, 49, 0.1) `color.neutral.alpha.midnight-a10`; background transparent; text Geist 16/22.4 500, #000000 `color.neutral.black`; icon 24 x 24, #000000 `color.neutral.black`; layers button.keyboard-focus-before.[--kb-focus-offset:-1px] 390.0x57.0 B:1px solid rgba(7, 26, 49, 0.1) |
| focus-visible | outline 2px solid #6bb1ff `color.brand.cornflower`, offset -1px; layers button.keyboard-focus-before.[--kb-focus-offset:-1px] 390.0x57.0 B:1px solid rgba(7, 26, 49, 0.1) 2px solid rgb(107, 177, 255) offset -1px |

Child layers that carry the look: button 390x57 border 1px solid rgba(7, 26, 49, 0.1) `color.neutral.alpha.midnight-a10`.

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 320 x 132; background transparent; text Calendly Sans 40/44 500, #fcfbf8 `color.neutral.magnolia`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Calendly wordmark, the Google SSO glyph, product illustrations and the booking pages' glyphs) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Calendly's product — the event-type editor, scheduled events, routing, analytics, contacts, integrations and billing — lives behind /app/login on app.calendly.com and was never reached. /integrations redirects to /app/login signed out. The public invitee booking pages were captured fully: a day was selected to measure the selected state, but no time slot was ever confirmed and nothing was booked or paid.

### Pages

- **The workspace.** Every post-login surface (event types, availability, meetings, contacts, workflows, settings, billing) needs an account and was never reached; /login and /signup were captured as forms and never filled or submitted.
- **Integrations.** /integrations redirects to /app/login signed out — an authenticated boundary, not a missing page.
- **Checkout and onboarding.** Every Get-started, Sign-up, Talk-to-sales and plan CTA was measured, never followed past its public landing.
- **/enterprise.** Returns 404; the enterprise content lives at /solutions/enterprise, which was captured.
- **The invitee confirmation.** Selecting a time slot opens the name/email form; the form was never reached or filled, so the confirmation step, calendar invites and payment step (the demo event is $53) are uncaptured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing. `menu-link` pressed timed out because the mega-menu closes on the forced press — recorded as a failed state, not a measured absence.
- **Disabled, error and loading states** were not seen on the public surface (an unavailable day cell is the only disabled control captured).
- **Focus-visible on nav-cta, nav-link, signup-google and billing-radio** shows no measured change in computed style; the buttons that do ring draw 2px solid cornflower outlines.
- **Booking `aria-current` today cell** is captured separately as [bk-day-today](#day-cell-today); it is not the selected state.

### Themes

calendly.com is two products, not a theme toggle: the marketing site paints light with `.dark` islands (the hero card, footer card and dark sections re-bind the declared --color-* roles — captured in the dark set), and the booking application paints light from its own token layer (its roles live under light.booking.*). A booking-dark scope is declared in the booking bundle but never paints signed out.

### Fonts

- **Calendly Sans** (marketing headings, nav and buttons), **Geist** (marketing body and fields), **Wulkan Text** (editorial serif headings, weights 400-600) and **Proxima Nova** (the whole booking application) are the served faces, all from Calendly's own CDN; the style guide falls back to system sans.

### Screenshots

- Product illustrations, photography, the Calendly wordmark and customer logos in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, case studies and the demo event's text are the product's content; only frames and components were measured.
