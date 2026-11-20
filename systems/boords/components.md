# Boords components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from boords.com on 2026-11-11, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the script timer field was filled with sample text, the signup/login forms were never used.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (37 components, 66 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (66 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme (the footer is a near-black section). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [yearly](screenshots/pricing-light-yearly.png) |
| AI storyboard generator | `/ai-storyboard-generator` | [default](screenshots/ai-storyboard-light-default.png), [full](screenshots/ai-storyboard-light-full.png) |
| Storyboard software | `/storyboard-software` | [default](screenshots/storyboard-software-light-default.png), [full](screenshots/storyboard-software-light-full.png) |
| Collaborate | `/collaborate` | [default](screenshots/collaborate-light-default.png), [full](screenshots/collaborate-light-full.png) |
| Customers | `/customers` | [default](screenshots/customers-light-default.png) |
| Customer story (Mobula) | `/customers/mobula` | [default](screenshots/customer-story-light-default.png), [full](screenshots/customer-story-light-full.png) |
| Docs | `/docs` | [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png) |
| Script timer | `/script-timer` | [default](screenshots/script-timer-light-default.png), [full](screenshots/script-timer-light-full.png), [with-script](screenshots/script-timer-light-with-script.png) |
| Log in | `/login` | [default](screenshots/login-light-default.png) |
| Sign up | `/signup` | [default](screenshots/signup-light-default.png) |
| Book a demo | `/demo` | [default](screenshots/demo-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Script timer, phone | `/script-timer` | [default](screenshots/mobile-script-timer-light-default.png), [full](screenshots/mobile-script-timer-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | every page, phone width | the burger button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item) |
| Desktop menu overlay | home page | the round menu button's own toggle (desktop capture only; the button is hidden at desktop width on the measurement page) | [home-light-menu](screenshots/home-light-menu.png) |
| Cookie banner | every page, some loads | hidden, never answered (the banner's own 'Accept & Close' was never clicked) | hidden before every shot and reading |
| Nav flyouts | header | the nav-menu-trigger's own toggle | [nav-trigger-open](#nav-dropdown-open) |
| Billing toggle | pricing page | the Yearly tab's own toggle | [pricing-light-yearly](screenshots/pricing-light-yearly.png) |
| Signup page | /signup | the public route 404s — signup now lives on app.boords.com | [signup-light-default](screenshots/signup-light-default.png); specs recorded as missing |
| Signed-in app | app.boords.com | the product lives behind login on another host | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 12 components were given a real keyboard focus. 6 draw an outline ring: `nav-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `nav-trigger` (1px auto #005fcc `measured.focus-outline`, offset 0px), `cta-demo` (1px auto #005fcc `measured.focus-outline`, offset 1px), `footer-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `social-icon` (1px auto #005fcc `measured.focus-outline`, offset 1px), `m-menu-button` (1px auto #e59700, offset 0px). 2 draw a focus ring as a shadow instead: `timer-toggle`, `feature-row`. The other 4 show no measured change: `hero-cta`, `billing-tab`, `plan-cta`, `m-nav-item`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): buttons and tabs read the same at rest and pressed — Boords controls press through scale in the DOM, not colour. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | all, background-color, border-color, color, fill, opacity, stroke, text-decoration-color | billing-tab, hero-cta, m-menu-button, m-menu-open, m-nav-item, plan-cta, social-icon, timer-toggle |
| 0.2s | `cubic-bezier(0, 0, 0.2, 1)` | background-color, color, transform | nav-trigger, nav-trigger-open |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | cta-demo, nav-link |
| 0.3s | `cubic-bezier(0, 0, 0.2, 1)` | box-shadow | header, m-header |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Feature card](#feature-card) | 324 x 256 | - | 24px | #f3f3e9 `color.neutral.cream` | none | 24px |
| [Plan card](#plan-card) | 324 x 423.8 | - | 24px | #ffffff `color.neutral.paper` | rgba(0, 0, 0, 0.04) 0px 0px 0px 1px | 0 |
| [Feature row](#feature-row) | 882.67 x 80 | - | 24px | transparent | none | 24px 28px |
| [Script field](#script-field) | 552 x 331 | 1px solid rgba(18, 18, 18, 0.1) | 16px | #ffffff `color.neutral.paper` | none | 12px 16px |
| [Mobile nav item](#mobile-nav-item) | 334 x 40 | 2px solid #ffffff `color.neutral.paper` | 9999px | #ffffff `color.neutral.paper` | none | 6px 20px |

## Components

### Shell and navigation

The floating rounded header pill, its nav links and dropdowns, the Book a demo CTA.

#### Header pill
The floating rounded-full header bar: logo, nav, menu button, Book a demo. Read as `header` on the home page.

**Values (default).** size 1344 x 64; padding 0px 8px 0px 32px; radius 9999px; background transparent; shadow #ffffff 0px 0px 0px 0px, rgba(18, 18, 18, 0.04) 0px 0px 0px 1px; text matter 14.4/18 400, rgba(18, 18, 18, 0.6) `color.neutral.body`; transition box-shadow 0.3s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, rgba(18, 18, 18, 0.6) `color.neutral.body`.

![Header pill default](components/crops/header-default.png)

#### Logo
Read as `logo` on the home page.

**Values (default).** size 160 x 20; background transparent; text matter 16/24 400, #000000.

![Logo default](components/crops/logo-default.png)

#### Nav link
Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 69.17 x 28; padding 6px 12px; radius 9999px; background transparent; text matter 14.4/18 400, rgba(18, 18, 18, 0.6) `color.neutral.body`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(18, 18, 18, 0.05) `measured.hover-dim`; text matter 14.4/18 400, #121212 `color.neutral.ink` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a.whitespace-nowrap.rounded-full 69.2x28.0 1px auto rgb(0, 95, 204) offset 1px 9999px |
| pressed | background rgba(18, 18, 18, 0.05) `measured.hover-dim`; text matter 14.4/18 400, #121212 `color.neutral.ink` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Nav dropdown
A nav-menu-trigger in the header; opens a flyout. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101.33 x 30; padding 6px 12px; radius 9999px; background transparent; text matter 14.4/18 400, rgba(18, 18, 18, 0.6) `color.neutral.body`; transition color 0.2s cubic-bezier(0, 0, 0.2, 1), background-color 0.2s cubic-bezier(0, 0, 0.2, 1), transform 0.2s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, rgba(18, 18, 18, 0.6) `color.neutral.body` |
| hover | background rgba(18, 18, 18, 0.05) `measured.hover-dim`; text matter 14.4/18 400, #121212 `color.neutral.ink`; icon 16 x 16, #121212 `color.neutral.ink` |
| focus-visible | background rgba(18, 18, 18, 0.05) `measured.hover-dim`; outline 1px auto #005fcc `measured.focus-outline`, offset 0px; text matter 14.4/18 400, #121212 `color.neutral.ink`; icon 16 x 16, #121212 `color.neutral.ink` |
| pressed | size 98.29 x 29.1; background rgba(18, 18, 18, 0.05) `measured.hover-dim`; text matter 14.4/18 400, #121212 `color.neutral.ink`; transform scale(0.97); icon 15.52 x 15.52, #121212 `color.neutral.ink` |

![Nav dropdown default](components/crops/nav-trigger-default.png) ![Nav dropdown hover](components/crops/nav-trigger-hover.png) ![Nav dropdown focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav dropdown pressed](components/crops/nav-trigger-pressed.png)

#### Nav dropdown, open
After its own toggle; the opened flyout shows in the crop. Read as `nav-trigger-open` on the home page.

**Values (opened).** size 101.33 x 30; padding 6px 12px; radius 9999px; background rgba(18, 18, 18, 0.05) `measured.hover-dim`; text matter 14.4/18 400, #121212 `color.neutral.ink`; transition color 0.2s cubic-bezier(0, 0, 0.2, 1), background-color 0.2s cubic-bezier(0, 0, 0.2, 1), transform 0.2s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #121212 `color.neutral.ink`.

![Nav dropdown, open opened](components/crops/nav-trigger-open-opened.png)

#### Menu button
The round icon button that opens the site menu. Read as `menu-button` on the home page.

Not on the page when it was captured.

#### Book a demo CTA
The header CTA; links to the demo form, measured never followed. Read as `cta-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 111.13 x 30; padding 6px 12px; radius 9999px; background transparent; text matter 14.4/18 400, rgba(18, 18, 18, 0.6) `color.neutral.body`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(18, 18, 18, 0.05) `measured.hover-dim`; text matter 14.4/18 400, #121212 `color.neutral.ink` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a.hidden.whitespace-nowrap 111.1x30.0 1px auto rgb(0, 95, 204) offset 1px 9999px |
| pressed | background rgba(18, 18, 18, 0.05) `measured.hover-dim`; text matter 14.4/18 400, #121212 `color.neutral.ink` |

![Book a demo CTA default](components/crops/cta-demo-default.png) ![Book a demo CTA hover](components/crops/cta-demo-hover.png) ![Book a demo CTA focus-visible](components/crops/cta-demo-focus-visible.png) ![Book a demo CTA pressed](components/crops/cta-demo-pressed.png)

### Home

The hero and the feature cards.

#### Hero headline
Read as `hero-title` on the home page.

**Values (default).** size 1152 x 133.09; background transparent; text matter 64/66.56 600, #121212 `color.neutral.ink`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero CTA
The hero action; measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 222.31 x 56; padding 12px 40px; border 1px solid #e8aa42 `color.brand.amber`; radius 9999px; background transparent; image linear-gradient(to right bottom, rgba(244, 189, 100, 0.8), #f4bd64); text matter 20/30 600, #121212 `color.neutral.ink`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #d89b3c `color.brand.amber-hover`; image linear-gradient(to right bottom, #f4bd64, #f4bd64); shadow rgba(108, 188, 228, 0.2) 0px 4px 6px -1px, rgba(108, 188, 228, 0.2) 0px 2px 4px -2px |
| focus-visible | outline 2px solid transparent, offset 2px |
| pressed | size 211.2 x 53.2; border 1px solid #d89b3c `color.brand.amber-hover`; image linear-gradient(to right bottom, #f4bd64, #f4bd64); shadow rgba(108, 188, 228, 0.2) 0px 4px 6px -1px, rgba(108, 188, 228, 0.2) 0px 2px 4px -2px; transform scale(0.95) |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero copy
The lede paragraph under the headline. Read as `hero-sub` on the home page.

**Values (default).** size 553.88 x 21.68; background transparent; text matter 14.4/25.2 400, #7b7b7b `color.neutral.muted`.

![Hero copy default](components/crops/hero-sub-default.png)

#### Feature card
A card-surface section card on the home page. Read as `feature-card` on the home page.

**Values (default).** size 324 x 256; padding 24px; radius 24px; background #f3f3e9 `color.neutral.cream`; text matter 14.4/18 600, #121212 `color.neutral.ink`; icon 16 x 16, #121212 `color.neutral.ink`.

![Feature card default](components/crops/feature-card-default.png)

#### Feature link
Read as `feature-link` on the home page.

Not on the page when it was captured.

### Pricing

The billing tabs, plan cards and the feature comparison rows.

#### Pricing title
Read as `price-title` on the pricing page.

**Values (default).** size 817.91 x 133.09; background transparent; text matter 64/66.56 600, #121212 `color.neutral.ink`.

![Pricing title default](components/crops/price-title-default.png)

#### Billing tab
A monthly/yearly billing tab; toggled for the yearly screenshot, left on default. Read as `billing-tab` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 84.88 x 36; padding 6px 16px; radius 9999px; background #ffffff `color.neutral.paper`; shadow rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px; outline 2px solid transparent, offset 2px; text matter 14.4/18 400, #121212 `color.neutral.ink`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px |

![Billing tab default](components/crops/billing-tab-default.png) ![Billing tab hover](components/crops/billing-tab-hover.png) ![Billing tab focus-visible](components/crops/billing-tab-focus-visible.png) ![Billing tab pressed](components/crops/billing-tab-pressed.png)

#### Plan card
One plan tier card (the rounded-card surfaces). Read as `plan-card` on the pricing page.

**Values (default).** size 324 x 423.8; radius 24px; background #ffffff `color.neutral.paper`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 1px; text matter 20/26 600, #000000; icon 20 x 20, #121212 `color.neutral.ink`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan price
A plan price figure inside a tier card. Read as `plan-price` on the pricing page.

**Values (default).** size 43.89 x 40.8; background transparent; text matter 20/30 400, #000000.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A tier action; measured never followed or pressed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 268 x 42; padding 6px 20px; border 3px solid #121212 `color.neutral.ink`; radius 9999px; background transparent; text matter 16/24 600, #121212 `color.neutral.ink`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 2px solid transparent, offset 2px |
| pressed | size 254.6 x 39.9; transform scale(0.95) |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Feature row
A comparison-table row/accordion. Read as `feature-row` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 882.67 x 80; padding 24px 28px; radius 24px; background transparent; text matter 20/26 600, #121212 `color.neutral.ink`; icon 16 x 16, rgba(18, 18, 18, 0.6) `color.neutral.body`; layers span.flex.size-8 32.0x32.0 rgba(18, 18, 18, 0.05) 9999px |
| focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(18, 18, 18, 0.4) 0px 0px 0px 2px; outline 2px solid transparent, offset 2px; layers none |

Child layers that carry the look: span 32x32 background rgba(18, 18, 18, 0.05) `measured.hover-dim` radius 9999px.

![Feature row default](components/crops/feature-row-default.png) ![Feature row hover](components/crops/feature-row-hover.png) ![Feature row focus-visible](components/crops/feature-row-focus-visible.png) ![Feature row pressed](components/crops/feature-row-pressed.png)

#### Feature row, open
The accordion row after its own toggle. Read as `feature-row-open` on the pricing page.

**Values (opened).** size 882.67 x 80; padding 24px 28px; radius 24px; background transparent; text matter 20/26 600, #121212 `color.neutral.ink`; icon 16 x 16, rgba(18, 18, 18, 0.6) `color.neutral.body`; layers span.flex.size-8 32.0x32.0 rgba(18, 18, 18, 0.05) 9999px.

Child layers that carry the look: span 32x32 background rgba(18, 18, 18, 0.05) `measured.hover-dim` radius 9999px.

![Feature row, open opened](components/crops/feature-row-open-opened.png)

### Public tools

The free script timer: textarea and option toggles.

#### Timer display
The script timer readout on the public tool page. Read as `timer-display` on the script timer page.

Not on the page when it was captured.

#### Script field
The paste-your-script textarea; filled with sample text and cleared, never submitted. Read as `timer-field` on the script timer page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 552 x 331; padding 12px 16px; border 1px solid rgba(18, 18, 18, 0.1); radius 16px; background #ffffff `color.neutral.paper`; text matter 16/24 400, #121212 `color.neutral.ink`; placeholder rgba(18, 18, 18, 0.6) `color.neutral.body` |
| focused | border 1px solid rgba(18, 18, 18, 0.4); shadow #ffffff 0px 0px 0px 0px, rgba(183, 122, 30, 0.3) 0px 0px 0px 2px; outline 2px solid transparent, offset 2px |
| filled | size 552 x 390.81; border 1px solid rgba(18, 18, 18, 0.4); shadow #ffffff 0px 0px 0px 0px, rgba(183, 122, 30, 0.3) 0px 0px 0px 2px; outline 2px solid transparent, offset 2px |

![Script field default](components/crops/timer-field-default.png) ![Script field focused](components/crops/timer-field-focused.png) ![Script field filled](components/crops/timer-field-filled.png)

#### Timer toggle
An aria-pressed option toggle on the timer. Read as `timer-toggle` on the script timer page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 178.66 x 66.41; padding 12px 8px; border 1px solid rgba(18, 18, 18, 0.15) `color.neutral.line`; radius 16px; background #ffffff `color.neutral.paper`; text matter 14.4/18 500, rgba(18, 18, 18, 0.7); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid rgba(18, 18, 18, 0.3); text matter 14.4/18 500, #121212 `color.neutral.ink` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, rgba(18, 18, 18, 0.4) 0px 0px 0px 4px; outline 2px solid transparent, offset 2px |
| pressed | border 1px solid rgba(18, 18, 18, 0.3); text matter 14.4/18 500, #121212 `color.neutral.ink` |

![Timer toggle default](components/crops/timer-toggle-default.png) ![Timer toggle hover](components/crops/timer-toggle-hover.png) ![Timer toggle focus-visible](components/crops/timer-toggle-focus-visible.png) ![Timer toggle pressed](components/crops/timer-toggle-pressed.png)

### Product pages

The AI storyboard landing page.

#### Product page title
Read as `page-title` on the AI storyboard page page.

**Values (default).** size 1063.28 x 133.09; background transparent; text matter 64/66.56 600, #121212 `color.neutral.ink`.

![Product page title default](components/crops/page-title-default.png)

#### Product page CTA
Read as `page-cta` on the AI storyboard page page.

Not on the page when it was captured.

### Sign-in and demo forms

The login and signup surfaces.

#### Signup form
The public signup card; fields focused/filled only, never submitted. Read as `signup-form` on the signup page.

Not on the page when it was captured.

#### Signup field
Read as `signup-field` on the signup page.

Not on the page when it was captured.

#### Signup submit
The form submit; measured at rest, never pressed. Read as `signup-submit` on the signup page.

Not on the page when it was captured.

#### Login form
The login card; never used. Read as `login-form` on the login page.

Not on the page when it was captured.

#### Login field
Read as `login-field` on the login page.

Not on the page when it was captured.

### Footer

The near-black footer: link columns, social icons, legal.

#### Footer
The footer: link columns, social, legal. Read as `footer` on the home page.

**Values (default).** size 1416 x 492; padding 0px 80px; background transparent; text matter 14.4/21.6 400, #ffffff `color.neutral.paper`; icon 14.41 x 14.41, #f4bd64; layers span.flex.rounded-full 152.0x50.1 rgba(255, 255, 255, 0.1) 9999px; div.w-full.justify-between 1400.0x52.0 rgba(255, 255, 255, 0.06) 24px.

Child layers that carry the look: span 152x50.1 background rgba(255, 255, 255, 0.1) radius 9999px; div 1400x52 background rgba(255, 255, 255, 0.06) radius 24px.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 152 x 50.09; background transparent; text matter 10.4/17.68 400, #ffffff `color.neutral.paper`; icon 14.41 x 14.41, #f4bd64; layers span.flex.rounded-full 152.0x50.1 rgba(255, 255, 255, 0.1) 9999px |
| hover | layers span.flex.rounded-full 152.0x50.1 rgba(255, 255, 255, 0.15) 9999px |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a 152.0x50.1 1px auto rgb(0, 95, 204) offset 1px; span.flex.rounded-full 152.0x50.1 rgba(255, 255, 255, 0.1) 9999px |

Child layers that carry the look: span 152x50.1 background rgba(255, 255, 255, 0.1) radius 9999px.

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social icon
Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 20 x 20; background transparent; text matter 14.4/18 400, #ffffff `color.neutral.paper`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.3; icon 20 x 20, #ffffff `color.neutral.paper` |
| hover | opacity 0.6 |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a.opacity-30.hover:opacity-60 20.0x20.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | opacity 0.6 |

![Social icon default](components/crops/social-icon-default.png) ![Social icon hover](components/crops/social-icon-hover.png) ![Social icon focus-visible](components/crops/social-icon-focus-visible.png) ![Social icon pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The same surface at phone width, with the menu overlay open.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 366 x 56; padding 0px 8px 0px 20px; radius 9999px; background transparent; shadow #ffffff 0px 0px 0px 0px, rgba(18, 18, 18, 0.04) 0px 0px 0px 1px; text matter 16/24 400, #000000; transition box-shadow 0.3s cubic-bezier(0, 0, 0.2, 1).

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; radius 9999px; background transparent; text matter 16/24 400, #000000; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(18, 18, 18, 0.05) `measured.hover-dim` |
| focus-visible | outline 1px auto #e59700, offset 0px; layers button.flex.h-10 40.0x40.0 1px auto rgb(229, 151, 0) offset 0px 9999px |
| pressed | background rgba(18, 18, 18, 0.05) `measured.hover-dim` |

![Menu button default](components/crops/m-menu-button-default.png) ![Menu button hover](components/crops/m-menu-button-hover.png) ![Menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The button after its own toggle; the opened menu shows in the crop. Read as `m-menu-open` on the home page at 390 wide.

**Values (opened).** size 40 x 40; radius 9999px; background transparent; outline 1px auto #e59700, offset 0px; text matter 16/24 400, #000000; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers button.flex.h-10 40.0x40.0 1px auto rgb(229, 151, 0) offset 0px 9999px.

Child layers that carry the look: button 40x40 radius 9999px.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav item
A link inside the opened menu overlay. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 334 x 40; padding 6px 20px; border 2px solid #ffffff `color.neutral.paper`; radius 9999px; background #ffffff `color.neutral.paper`; text matter 16/24 600, #121212 `color.neutral.ink`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 2px solid transparent, offset 2px |
| pressed | size 317.3 x 38; transform scale(0.95) |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 334 x 149.75; background transparent; text matter 36.00/37.44 600, #121212 `color.neutral.ink`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (cart, search, social glyphs, the Boords wordmark) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

app.boords.com holds every storyboard, animatic, shot list, the script editor and all account surfaces behind login; the public site is the marketing shell plus the free script timer. /signup redirects visitors to the app host now (the route 404s on www), so the signup form specs are recorded as missing rather than captured from a dead page.

### Pages

- **The app.** app.boords.com, every project, board, editor and export were never reached — they need an account.
- **Signup.** /signup on www 404s; the real signup is on app.boords.com and was never used.
- **Login.** /login renders the header and a shell; no form fields mount for this client (the login lives on the app host).
- **Demo booking.** /demo shows the pitch; the booking widget (an embedded scheduler) was never interacted with.
- **The script timer's compute.** The textarea and toggles were measured and a sample script was typed and cleared; the timing is a local display, nothing was submitted.
- **Checkout.** Every plan CTA was measured, never followed.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The site paints one light theme; the footer is a near-black section style. No dark mode is offered.

### Fonts

- **matter** is the single self-hosted face for everything from 64px display down to 10.4px footnotes. It is served from the Boords CDN; the style guide falls back to system sans.

### Screenshots

- Illustrations, the Boords wordmark, customer photography and storyboard imagery in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Customer stories, docs content and the demo scheduler are the product's content; only frames and components were measured.
