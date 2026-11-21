# Copy.ai components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from copy.ai on 2026-11-21, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, submitted or paid for; the contact form's fields were focused and filled then cleared, never sent; the login.copy.ai auth card was measured, never used; the demo, trial, checkout and OAuth actions were never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (45 components, 120 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (120 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu-gtm](screenshots/home-light-menu-gtm.png), [menu-resources](screenshots/home-light-menu-resources.png), [menu-use-cases](screenshots/home-light-menu-use-cases.png), [menu](screenshots/home-light-menu.png) |
| Pricing | `/prices` | [default](screenshots/pricing-light-default.png), [faq](screenshots/pricing-light-faq.png), [full](screenshots/pricing-light-full.png) |
| Platform (How it Works) | `/platform/how-it-works` | [default](screenshots/platform-light-default.png), [full](screenshots/platform-light-full.png) |
| Use case (Prospecting Cockpit) | `/use-cases/prospecting-cockpit` | [default](screenshots/use-case-light-default.png), [full](screenshots/use-case-light-full.png) |
| Enterprise | `/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| Blog index | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Contact us | `/contact-us` | [default](screenshots/contact-light-default.png), [form-focus](screenshots/contact-light-form-focus.png), [full](screenshots/contact-light-full.png) |
| Changelog | `/changelog` | [default](screenshots/changelog-light-default.png), [full](screenshots/changelog-light-full.png) |
| Sign-in card | `https://login.copy.ai/ (via app.copy.ai/login)` | [default](screenshots/login-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/prices` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the circled burger's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-menu-row), [m-login](#mobile-login), [m-sales](#mobile-sales-cta) |
| Platform mega-menu | every desktop page | the Platform trigger's own hover/click | [home-light-menu](screenshots/home-light-menu.png), [nav-dd-panel](#mega-menu-panel), [dd-link](#dropdown-link) |
| FAQ accordion row | /prices | the FAQ row's own toggle | [pricing-light-faq](screenshots/pricing-light-faq.png), [faq-item](#faq-row) |
| Contact form focus | /contact-us | the Name field's own focus — typed text was deleted again, never sent | [contact-light-form-focus](screenshots/contact-light-form-focus.png), [name-input](#name-field) |
| Cookie consent + chat widget | every page | hidden, never answered (the HubSpot banner and the messages widget were never clicked) | hidden before every shot and reading |
| The signed-in product | app.copy.ai | behind sign-in; the public login.copy.ai card was measured, never used | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 22 components were given a real keyboard focus. 22 draw an outline ring: `nav-dd-toggle` (2px solid #4d65ff `measured.focus-ring-blue`, offset 2px), `btn-nav` (1px auto #005fcc `measured.focus-ring-light`, offset 1px), `login-link` (1px auto #005fcc `measured.focus-ring-light`, offset 1px), `dd-link` (2px solid #4d65ff `measured.focus-ring-blue`, offset 2px), `playbook-card` (1px auto #005fcc `measured.focus-ring-light`, offset 1px), `invert-cta` (1px auto #005fcc `measured.focus-ring-light`, offset 1px), `platform-card` (1px auto #005fcc `measured.focus-ring-light`, offset 1px), `blog-card` (1px auto #005fcc `measured.focus-ring-light`, offset 1px), `plan-toggle` (1px auto #005fcc `measured.focus-ring-light`, offset 0px), `plan-cta` (1px auto #005fcc `measured.focus-ring-light`, offset 1px), `faq-item` (2px solid #4d65ff `measured.focus-ring-blue`, offset 2px), `send-button` (1px auto #005fcc `measured.focus-ring-light`, offset 1px), `contact-faq` (2px solid #4d65ff `measured.focus-ring-blue`, offset 2px), `auth-continue` (2px solid #a396ff `measured.focus-ring-auth`, offset 2px), `auth-oauth` (2px solid #a396ff `measured.focus-ring-auth`, offset -1px), `auth-signup` (2px solid #a396ff `measured.focus-ring-auth`, offset 2px), `footer-link` (1px auto #005fcc `measured.focus-ring-light`, offset 1px), `social-icon` (1px auto #005fcc `measured.focus-ring-light`, offset 1px), `m-menu-button` (1px auto #e59700, offset 1px), `m-nav-item` (2px solid #4d65ff `measured.focus-ring-blue`, offset 2px), `m-login` (1px auto #e59700, offset 1px), `m-sales` (1px auto #e59700, offset 1px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease` | box-shadow | playbook-card |
| 0.2s | `ease` | all, border-color, box-shadow, color | email-input, hero-email, m-nav-item, message-field, name-input |
| 0.3s | `ease` | background-color, border-color, color | blog-card, hero-submit, playbook-card |
| 0.4s | `ease` | box-shadow | m-nav-item, nav-dd-toggle |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 360 x 594.59 | 1px solid #e0e0e0 `color.neutral.border` | - | #ffffff `color.neutral.white` | none | 24px |
| [Platform card](#platform-card) | 700 x 121.97 | - | - | #29007a `color.brand.purple-deep` | none | 24px 105px 24px 24px |
| [Blog card](#blog-card) | 360 x 510.78 | 1px solid #e0e0e0 `color.neutral.border` | - | #ffffff `color.neutral.white` | none | 0px 8px |
| [Auth card](#auth-card) | 344 x 283.89 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The dark promo banner and the sticky white nav: the copy.ai wordmark, the Platform / Use cases / Resources / Pricing / GTM AI mega-menu triggers, and the Login / Get a Demo actions. The Platform trigger opens a full-width mega-menu with four columns.

#### Top banner
The dark promo strip above the nav ("The 2026 Benchmarks Report is Finally Here!" with its arrow action); static, scrolls with the page. Read as `top-banner` on the home page.

**Values (default).** size 1440 x 48; background #171717 `color.neutral.ink`; text Inter 16/24 500, #ffffff `color.neutral.white`; icon 16 x 11, #fbfbfc `color.neutral.off-white`.

![Top banner default](components/crops/top-banner-default.png)

#### Header
The sticky nav.mega--nav (z 1000): wordmark, the Platform/Use cases/Resources/Pricing/GTM AI triggers, Login and the Get a Demo action. Read as `header` on the home page.

**Values (default).** size 1440 x 88; background #ffffff `color.neutral.white`; text Inter 16/24 500, #222222; icon 20 x 20, #222222.

![Header default](components/crops/header-default.png)

#### Logo
The copy.ai wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 100 x 30; background transparent; text Inter 14/20 400, #333333.

![Logo default](components/crops/logo-default.png)

#### Nav dropdown trigger
The Platform trigger that opens the mega-menu; toggled for the menu screenshot, never followed. Read as `nav-dd-toggle` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 132.31 x 88; padding 8px 24px; background transparent; text Inter 16/24 500, #222222; transition box-shadow 0.4s ease; icon 20 x 20, #222222 |
| hover | shadow #171717 0px -1px 0px 0px inset; layers div.mega--nav_dd_toggle.w-dropdown-toggle 132.3x88.0 rgb(23, 23, 23) 0px -1px 0px 0px inset |
| focus-visible | outline 2px solid #4d65ff `measured.focus-ring-blue`, offset 2px; layers div.mega--nav_dd_toggle.w-dropdown-toggle 132.3x88.0 2px solid rgb(77, 101, 255) offset 2px |
| pressed | shadow #171717 0px -0.999058px 0px 0px inset; layers div.mega--nav_dd_toggle.w-dropdown-toggle 132.3x88.0 rgba(23, 23, 23, 1) 0px -0.999058px 0px 0px inset |

![Nav dropdown trigger default](components/crops/nav-dd-toggle-default.png) ![Nav dropdown trigger hover](components/crops/nav-dd-toggle-hover.png) ![Nav dropdown trigger focus-visible](components/crops/nav-dd-toggle-focus-visible.png) ![Nav dropdown trigger pressed](components/crops/nav-dd-toggle-pressed.png)

#### Nav CTA
The purple "Get a Demo" button in the header; measured, never followed. Read as `btn-nav` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 121.78 x 47; padding 12px 16px; radius 4px; background #693edf; text Inter 16/24 700, #ffffff `color.neutral.white` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 1px |

![Nav CTA default](components/crops/btn-nav-default.png) ![Nav CTA hover](components/crops/btn-nav-hover.png) ![Nav CTA focus-visible](components/crops/btn-nav-focus-visible.png) ![Nav CTA pressed](components/crops/btn-nav-pressed.png)

#### Login link
The header Login action (app.copy.ai); measured, never followed. Read as `login-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 42.28 x 24; background transparent; text Inter 16/24 500, #171717 `color.neutral.ink` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 1px; layers a.mega--nav_login-link 42.3x24.0 1px auto rgb(0, 95, 204) offset 1px |

![Login link default](components/crops/login-link-default.png) ![Login link hover](components/crops/login-link-hover.png) ![Login link focus-visible](components/crops/login-link-focus-visible.png) ![Login link pressed](components/crops/login-link-pressed.png)

#### Mega-menu panel
The opened Platform mega-menu (OVERVIEW / WORKFLOWS / INTELLIGENCE LAYER / TECHNICAL RESOURCES columns). Read as `nav-dd-panel` on the home page.

**Values (default).** size 1440 x 365; padding 40px; border T: 1px solid #e0e0e0 `color.neutral.border`; background #ffffff `color.neutral.white`; shadow rgba(0, 0, 0, 0.03) 0px 40px 34px 0px; text Inter 12/24 500, #171717 `color.neutral.ink`; icon 16 x 16, #171717 `color.neutral.ink`.

![Mega-menu panel default](components/crops/nav-dd-panel-default.png)

#### Dropdown link
A link inside the opened Platform mega-menu (How it Works et al.); measured, never followed. Read as `dd-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 277.33 x 32; background transparent; text Inter 16/24 500, #171717 `color.neutral.ink`; icon 16 x 16, #171717 `color.neutral.ink`; layers div.dd-link_icon-wr 32.0x32.0 rgb(251, 251, 252) T:1px solid rgb(224, 224, 224) / R:1px solid rgb(224, 224, 224) / B:1px solid rgb(224, 224, 224) / L:1px solid rgb(224, 224, 224) 8px |
| hover | icon 16 x 16, #ffffff `color.neutral.white`; layers div.dd-link_icon-wr 32.0x32.0 rgb(105, 62, 224) T:1px solid rgb(59, 13, 150) / R:1px solid rgb(59, 13, 150) / B:1px solid rgb(59, 13, 150) / L:1px solid rgb(59, 13, 150) 8px |
| focus-visible, pressed | outline 2px solid #4d65ff `measured.focus-ring-blue`, offset 2px; icon 16 x 16, #ffffff `color.neutral.white`; layers a.dd-link.w-inline-block 277.3x32.0 2px solid rgb(77, 101, 255) offset 2px; div.dd-link_icon-wr 32.0x32.0 rgb(105, 62, 224) T:1px solid rgb(59, 13, 150) / R:1px solid rgb(59, 13, 150) / B:1px solid rgb(59, 13, 150) / L:1px solid rgb(59, 13, 150) 8px |

Child layers that carry the look: div 32x32 background #fbfbfc `color.neutral.off-white` border 1px solid #e0e0e0 `color.neutral.border` radius 8px.

![Dropdown link default](components/crops/dd-link-default.png) ![Dropdown link hover](components/crops/dd-link-hover.png) ![Dropdown link focus-visible](components/crops/dd-link-focus-visible.png) ![Dropdown link pressed](components/crops/dd-link-pressed.png)

### Home

The 88px ABC Normal hero ("The First AI-Native GTM Platform") over the purple circuit artwork, the hero email capture, then light sections with dark feature bands and the deep-purple platform card.

#### Hero headline
The "The First AI-Native GTM Platform" display. Read as `hero-title` on the home page.

**Values (default).** size 349 x 176; background transparent; text ABC Normal 88/88 600, #171717 `color.neutral.ink`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede under the hero headline (Infuse AI across your go-to-market engine…). Read as `hero-sub` on the home page.

**Values (default).** size 384 x 110; background transparent; text Inter 14/22 400, #566b76 `color.neutral.lede`.

![Hero copy default](components/crops/hero-sub-default.png)

#### Email field
The hero "What's your email?" field; focused and given sample text that was deleted again — the form was never submitted. Read as `hero-email` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 308 x 42; padding 0px 8px 0px 18px; border 1px solid #e4edf1 `color.neutral.border-field`; background #f6fafb `color.neutral.field`; text Inter 16/22.85 400, #171717 `color.neutral.ink`; transition border-color 0.2s ease, box-shadow 0.2s ease; placeholder #6c8d9d |
| focused, filled | border 1px solid #171717 `color.neutral.ink`; shadow rgba(0, 0, 0, 0.07) 0px 6px 20px 0px |

![Email field default](components/crops/hero-email-default.png) ![Email field focused](components/crops/hero-email-focused.png) ![Email field filled](components/crops/hero-email-filled.png)

#### Hero submit
The black "Get a demo" submit of the hero email form; measured, never pressed. Read as `hero-submit` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 128.3 x 40; padding 0px 20px; background #171717 `color.neutral.ink`; text Inter 16/24 700, #ffffff `color.neutral.white`; transition border-color 0.3s ease, background-color 0.3s ease; placeholder #ffffff `color.neutral.white` |
| hover, pressed | background #693ee0 `color.brand.purple` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Hero submit default](components/crops/hero-submit-default.png) ![Hero submit hover](components/crops/hero-submit-hover.png) ![Hero submit pressed](components/crops/hero-submit-pressed.png)

#### Playbook card
A "Get Demo" playbook card (the purple GTM-AI-Playbook rail); measured, never followed. Read as `playbook-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 90.63 x 28; padding 0px 16px; border 1px solid #ccd9e0 `color.neutral.border-card`; radius 4px; background #ffffff `color.neutral.white`; shadow rgba(204, 217, 224, 0.2) 0px -3px 0px 0px inset; text Inter 12/14 400, #364045; transition box-shadow 0.1s ease, color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease |
| hover | border 1px solid #000000; background #131516; shadow none; text Inter 12/14 400, #ffffff `color.neutral.white` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 1px |
| pressed | border 1px solid #000000; background #131516; shadow none; text Inter 12/14 400, #ffffff `color.neutral.white` |

![Playbook card default](components/crops/playbook-card-default.png) ![Playbook card hover](components/crops/playbook-card-hover.png) ![Playbook card focus-visible](components/crops/playbook-card-focus-visible.png) ![Playbook card pressed](components/crops/playbook-card-pressed.png)

#### Inverted CTA
A "Get a demo" action on a dark band (the inverted variant); measured, never followed. Read as `invert-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 178.3 x 63; padding 20px 32px; radius 8px; background #ffffff `color.neutral.white`; text Inter 16/24 700, #171717 `color.neutral.ink` |
| hover | background #693ee0 `color.brand.purple` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 1px |

![Inverted CTA default](components/crops/invert-cta-default.png) ![Inverted CTA hover](components/crops/invert-cta-hover.png) ![Inverted CTA focus-visible](components/crops/invert-cta-focus-visible.png) ![Inverted CTA pressed](components/crops/invert-cta-pressed.png)

#### Platform card
A platform-feature card (Agents Automate…); measured, never followed. Read as `platform-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 700 x 121.97; padding 24px 105px 24px 24px; background #29007a `color.brand.purple-deep`; text ABC Normal 28/42 500, #ffffff `color.neutral.white` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 1px |

![Platform card default](components/crops/platform-card-default.png) ![Platform card hover](components/crops/platform-card-hover.png) ![Platform card focus-visible](components/crops/platform-card-focus-visible.png) ![Platform card pressed](components/crops/platform-card-pressed.png)

#### Section heading
A 56px section heading (Design Your GTM AI Playbook). Read as `section-h2` on the home page.

**Values (default).** size 1329 x 66; background transparent; text ABC Normal 56/66 500, #171717 `color.neutral.ink`.

![Section heading default](components/crops/section-h2-default.png)

#### Blog card
A blog/article card in the home slider; measured, never followed. Read as `blog-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 360 x 510.78; padding 0px 8px; border 1px solid #e0e0e0 `color.neutral.border`; background #ffffff `color.neutral.white`; text ABC Normal 24/33.6 500, #000b0f; transition border-color 0.3s ease |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 1px |
| pressed | border 1px solid #171717 `color.neutral.ink` |

![Blog card default](components/crops/blog-card-default.png) ![Blog card hover](components/crops/blog-card-hover.png) ![Blog card focus-visible](components/crops/blog-card-focus-visible.png) ![Blog card pressed](components/crops/blog-card-pressed.png)

### Pricing

The /prices surface: the Self-Serve / Enterprise segmented toggle, the Chat plan card (checklist, Monthly|Annually control, the 20% SAVING badge, $29/mo, Get started) and the FAQ accordion.

#### Pricing title
The "Copy.ai pricing" display heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 427.72 x 74; background transparent; text ABC Normal 64/74 500, #171717 `color.neutral.ink`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Plan toggle
The Self-Serve / Enterprise segmented control; measured at rest — toggling it swaps the pricing view, so the pressed state is the CDP-forced one. Read as `plan-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 264 x 56; padding 4px; radius 48px; background #ffffff `color.neutral.white`; shadow rgba(0, 0, 0, 0.06) 0px 28px 64px 0px; text Inter 16/24 500, #171717 `color.neutral.ink` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 0px |

![Plan toggle default](components/crops/plan-toggle-default.png) ![Plan toggle hover](components/crops/plan-toggle-hover.png) ![Plan toggle focus-visible](components/crops/plan-toggle-focus-visible.png) ![Plan toggle pressed](components/crops/plan-toggle-pressed.png)

#### Plan card
The Chat plan card (name, checklist, Monthly|Annually control, the 20% SAVING badge, $29/mo and Get started). Read as `plan-card` on the pricing page.

**Values (default).** size 360 x 594.59; padding 24px; border 1px solid #e0e0e0 `color.neutral.border`; background #ffffff `color.neutral.white`; text ABC Normal 32/42 500, #171717 `color.neutral.ink`; icon 20 x 20, #76879d.

![Plan card default](components/crops/plan-card-default.png)

#### Plan price
The $29/mo price figure in the plan card. Read as `plan-price` on the pricing page.

**Values (default).** size 310 x 33.59; background transparent; text ABC Normal 24/33.6 500, #693ee0 `color.brand.purple`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
The plan card's "Get started" action; measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 310 x 47; padding 12px 16px; radius 8px; background #171717 `color.neutral.ink`; text Inter 16/24 700, #ffffff `color.neutral.white` |
| hover | background #683ee0 |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 1px |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Saving badge
The "20% SAVING" outlined badge inside the plan card. Read as `saving-badge` on the pricing page.

**Values (default).** size 101.42 x 24; padding 0px 12px; border 1px solid #693ee0 `color.brand.purple`; radius 40px; background transparent; text Inter 12/22 500, #693ee0 `color.brand.purple`.

![Saving badge default](components/crops/saving-badge-default.png)

#### FAQ row
An FAQ accordion row (question + the open chevron); measured closed, the opened state is the screenshot toggle. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 758 x 82; padding 24px 72px 24px 24px; background #ffffff `color.neutral.white`; text ABC Normal 24/34 500, #171717 `color.neutral.ink`; icon 20.92 x 28.8, rgba(93, 93, 93, 0.7) |
| focus-visible | outline 2px solid #4d65ff `measured.focus-ring-blue`, offset 2px |

![FAQ row default](components/crops/faq-item-default.png) ![FAQ row hover](components/crops/faq-item-hover.png) ![FAQ row focus-visible](components/crops/faq-item-focus-visible.png) ![FAQ row pressed](components/crops/faq-item-pressed.png)

### Contact

The /contact-us surface: the 72px Got Questions? display, the three-field contact form with Send message (measured, never submitted) and the FAQ column.

#### Contact title
The "Got Questions?" display heading. Read as `contact-h1` on the contact page.

**Values (default).** size 488.75 x 82; background transparent; text ABC Normal 72/82 700, #171717 `color.neutral.ink`.

![Contact title default](components/crops/contact-h1-default.png)

#### Name field
The "Your Name" field of the contact form; focused and given sample text that was deleted again — never submitted. Read as `name-input` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 550 x 48; padding 12px 16px; border 1px solid #e0e0e0 `color.neutral.border`; radius 5px; background #ffffff `color.neutral.white`; text Inter 14/20 400, #171717 `color.neutral.ink`; transition color 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease; placeholder rgba(93, 93, 93, 0.4) |
| focused, filled | border 1px solid #693ee0 `color.brand.purple`; shadow rgba(0, 0, 0, 0.03) 0px 2px 6px 0px |

![Name field default](components/crops/name-input-default.png) ![Name field focused](components/crops/name-input-focused.png) ![Name field filled](components/crops/name-input-filled.png)

#### Email field
The "Your Email" field of the contact form. Read as `email-input` on the contact page.

**Values (default).** size 550 x 48; padding 12px 16px; border 1px solid #e0e0e0 `color.neutral.border`; radius 5px; background #ffffff `color.neutral.white`; text Inter 14/20 400, #171717 `color.neutral.ink`; transition color 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease; placeholder rgba(93, 93, 93, 0.4).

![Email field default](components/crops/email-input-default.png)

#### Message field
The "What would you like to learn?" textarea. Read as `message-field` on the contact page.

**Values (default).** size 550 x 80; padding 12px 16px; border 1px solid #e0e0e0 `color.neutral.border`; radius 5px; background #ffffff `color.neutral.white`; text Inter 14/20 400, #171717 `color.neutral.ink`; transition color 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease; placeholder rgba(93, 93, 93, 0.4).

![Message field default](components/crops/message-field-default.png)

#### Send button
The "Send message" action of the contact form (the input[type=submit] twin is hidden); measured, never pressed. Read as `send-button` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 178.83 x 63; padding 20px 32px; radius 8px; background #171717 `color.neutral.ink`; text Inter 16/24 700, #ffffff `color.neutral.white` |
| hover | background #683ee0 |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 1px |

![Send button default](components/crops/send-button-default.png) ![Send button hover](components/crops/send-button-hover.png) ![Send button focus-visible](components/crops/send-button-focus-visible.png) ![Send button pressed](components/crops/send-button-pressed.png)

#### Contact FAQ row
An FAQ accordion row beside the form; measured closed, never expanded. Read as `contact-faq` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 548 x 82; padding 24px 72px 24px 24px; background #ffffff `color.neutral.white`; text ABC Normal 24/34 500, #171717 `color.neutral.ink`; icon 18.67 x 28.8, rgba(93, 93, 93, 0.7) |
| focus-visible | outline 2px solid #4d65ff `measured.focus-ring-blue`, offset 2px |

![Contact FAQ row default](components/crops/contact-faq-default.png) ![Contact FAQ row hover](components/crops/contact-faq-hover.png) ![Contact FAQ row focus-visible](components/crops/contact-faq-focus-visible.png) ![Contact FAQ row pressed](components/crops/contact-faq-pressed.png)

### Login

The public auth card on login.copy.ai (reached through app.copy.ai/login): the email field, Continue with email, the Google/Microsoft OAuth anchors and the Sign up link — measured, never used.

#### Auth card
The login.copy.ai sign-in card (email field, Continue with email, the OAuth buttons, the Sign up link); captured, never used. Read as `auth-card` on the login page.

**Values (default).** size 344 x 283.89; background transparent; text interFont 14/20 600, #202020 `color.neutral.auth-ink`; icon 15 x 15, #202020 `color.neutral.auth-ink`; layers div.rt-TextFieldRoot.rt-r-size-3 344.0x40.0 rgba(255, 255, 255, 0.85) rgba(0, 0, 0, 0.192) 0px 0px 0px 1px inset 4.5px; button.rt-reset.rt-BaseButton 344.0x40.0 rgb(105, 62, 224) rgba(0, 0, 0, 0) 0px 0px 0px 1px inset 4.5px; div::before.rt-Text.rt-r-size-1 151.516pxx1px rgba(0, 0, 0, 0.15); div::after.rt-Text.rt-r-size-1 151.516pxx1px rgba(0, 0, 0, 0.15); a.rt-reset.rt-BaseButton 344.0x40.0 rgba(2.

Child layers that carry the look: div 344x40 background rgba(255, 255, 255, 0.85) radius 4.5px shadow rgba(0, 0, 0, 0.192) 0px 0px 0px 1px inset; button 344x40 background #693ee0 `color.brand.purple` radius 4.5px shadow transparent 0px 0px 0px 1px inset; div::before 151.516pxx1px background rgba(0, 0, 0, 0.15).

![Auth card default](components/crops/auth-card-default.png)

#### Auth email field
The "Your email address" input; focused and given sample text that was deleted again — nothing sent. Read as `auth-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 342 x 38; radius 3.5px; background transparent; text interFont 16/24 400, #202020 `color.neutral.auth-ink`; placeholder rgba(0, 0, 0, 0.486) |

![Auth email field default](components/crops/auth-email-default.png) ![Auth email field focused](components/crops/auth-email-focused.png) ![Auth email field filled](components/crops/auth-email-filled.png)

#### Continue button
The "Continue with email" submit; measured, never pressed. Read as `auth-continue` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 344 x 40; padding 0px 16px; radius 4.5px; background #693ee0 `color.brand.purple`; text interFont 16/24 500, #ffffff `color.neutral.white` |
| hover | background #5b36c3 `color.brand.purple-hover` |
| focus-visible | outline 2px solid #a396ff `measured.focus-ring-auth`, offset 2px |
| pressed | background #4e22b1 `color.brand.purple-pressed` |

![Continue button default](components/crops/auth-continue-default.png) ![Continue button hover](components/crops/auth-continue-hover.png) ![Continue button focus-visible](components/crops/auth-continue-focus-visible.png) ![Continue button pressed](components/crops/auth-continue-pressed.png)

#### OAuth button
The "Continue with Google" action (an anchor); measured, never followed — it would leave for the OAuth flow. Read as `auth-oauth` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 344 x 40; padding 0px 8px; radius 4.5px; background rgba(255, 255, 255, 0.8); shadow rgba(0, 0, 0, 0.192) 0px 0px 0px 1px inset; text interFont 16/24 500, #202020 `color.neutral.auth-ink`; icon 15 x 15, #202020 `color.neutral.auth-ink` |
| hover | shadow rgba(0, 0, 0, 0.267) 0px 0px 0px 1px inset |
| focus-visible | outline 2px solid #a396ff `measured.focus-ring-auth`, offset -1px |
| pressed | background rgba(0, 0, 0, 0.06); shadow rgba(0, 0, 0, 0.267) 0px 0px 0px 1px inset |

![OAuth button default](components/crops/auth-oauth-default.png) ![OAuth button hover](components/crops/auth-oauth-hover.png) ![OAuth button focus-visible](components/crops/auth-oauth-focus-visible.png) ![OAuth button pressed](components/crops/auth-oauth-pressed.png)

#### Sign-up link
The "Sign up" link on the auth card; measured, never followed. Read as `auth-signup` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 50.03 x 17; background transparent; text interFont 14/20 400, #5753c6 `color.brand.link` |
| focus-visible | radius 0.735px; outline 2px solid #a396ff `measured.focus-ring-auth`, offset 2px; layers a.rt-Text.BrandedLink 50.0x17.0 2px solid rgb(163, 150, 255) offset 2px 0.735px |

![Sign-up link default](components/crops/auth-signup-default.png) ![Sign-up link hover](components/crops/auth-signup-hover.png) ![Sign-up link focus-visible](components/crops/auth-signup-focus-visible.png) ![Sign-up link pressed](components/crops/auth-signup-pressed.png)

### Footer

The light footer: the link columns, social icons and legal.

#### Footer
The footer: the link columns, social icons and legal. Read as `footer` on the home page.

**Values (default).** size 1440 x 1066; background transparent; text Inter 16/24 700, #171717 `color.neutral.ink`; layers div.foot-line_v2 260.0x1.0 rgb(23, 23, 23); div.foot-line_v2 260.0x1.0 rgb(23, 23, 23); div.foot-line_v2 260.0x1.0 rgb(23, 23, 23); div.foot-line_v2 260.0x1.0 rgb(23, 23, 23); div.footer--bottom 1440.0x165.0 rgb(23, 23, 23).

Child layers that carry the look: div 260x1 background #171717 `color.neutral.ink`; div 260x1 background #171717 `color.neutral.ink`; div 260x1 background #171717 `color.neutral.ink`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer column link (Blog / Contact Support / Changelog); measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 260 x 24; background transparent; text Inter 16/24 500, #171717 `color.neutral.ink` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 1px; layers a.footer_link 260.0x24.0 1px auto rgb(0, 95, 204) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A social link in the footer. Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 36 x 35; background transparent; text Inter 14/20 400, #171717 `color.neutral.ink` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 1px; layers a.w-inline-block 36.0x35.0 1px auto rgb(0, 95, 204) offset 1px |

![Social link default](components/crops/social-icon-default.png) ![Social link hover](components/crops/social-icon-hover.png) ![Social link focus-visible](components/crops/social-icon-focus-visible.png) ![Social link pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The same surface at phone width: the header shrinks to wordmark + circled burger, and the menu opens as a full-height overlay with accordion rows and Login / Contact Sales at the foot.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 80; background #ffffff `color.neutral.white`; text Inter 14/20 400, #171717 `color.neutral.ink`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The circled burger toggle (a.mega--nav_burger_trigger). Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 46 x 46; background transparent; text Inter 14/20 400, #171717 `color.neutral.ink`; icon 17.59 x 17.59, #171717 `color.neutral.ink` |
| focus-visible | outline 1px auto #e59700, offset 1px; layers a.mega--nav_burger_trigger.w-inline-block 46.0x46.0 1px auto rgb(229, 151, 0) offset 1px |

![Menu button default](components/crops/m-menu-button-default.png) ![Menu button hover](components/crops/m-menu-button-hover.png) ![Menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The opened mobile menu: the accordion rows (Platform / Use cases / Resources / Pricing / GTM AI) over the page with Login and Contact Sales at the foot. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; border T: 1px solid #e0e0e0 `color.neutral.border`; background #ffffff `color.neutral.white`; text Inter 16/24 500, #222222; icon 20 x 20, #222222.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile menu row
A row inside the opened mobile menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 350 x 89; padding 32px 0px; border B: 1px solid #e0e0e0 `color.neutral.border`; background transparent; text Inter 16/24 500, #222222; transition all 0.2s ease, box-shadow 0.4s ease; icon 20 x 20, #222222; layers div.mega--nav_dd_toggle.w-dropdown-toggle 350.0x89.0 B:1px solid rgb(224, 224, 224) |
| hover | shadow #171717 0px -1px 0px 0px inset; layers div.mega--nav_dd_toggle.w-dropdown-toggle 350.0x89.0 B:1px solid rgb(224, 224, 224) rgb(23, 23, 23) 0px -1px 0px 0px inset |
| focus-visible | outline 2px solid #4d65ff `measured.focus-ring-blue`, offset 2px; layers div.mega--nav_dd_toggle.w-dropdown-toggle 350.0x89.0 B:1px solid rgb(224, 224, 224) 2px solid rgb(77, 101, 255) offset 2px |
| pressed | shadow #171717 0px -0.999046px 0px 0px inset; layers div.mega--nav_dd_toggle.w-dropdown-toggle 350.0x89.0 B:1px solid rgb(224, 224, 224) rgba(23, 23, 23, 1) 0px -0.999046px 0px 0px inset |

Child layers that carry the look: div 350x89 border 1px solid #e0e0e0 `color.neutral.border`.

![Mobile menu row default](components/crops/m-nav-item-default.png) ![Mobile menu row hover](components/crops/m-nav-item-hover.png) ![Mobile menu row focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile menu row pressed](components/crops/m-nav-item-pressed.png)

#### Mobile login
The Login action inside the mobile menu; measured, never followed. Read as `m-login` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 118 x 50; padding 12px 16px; border 1px solid #e0e0e0 `color.neutral.border`; radius 8px; background transparent; text Inter 16/24 700, #171717 `color.neutral.ink` |
| focus-visible | outline 1px auto #e59700, offset 1px |

![Mobile login default](components/crops/m-login-default.png) ![Mobile login hover](components/crops/m-login-hover.png) ![Mobile login focus-visible](components/crops/m-login-focus-visible.png) ![Mobile login pressed](components/crops/m-login-pressed.png)

#### Mobile sales CTA
The purple Contact Sales action inside the mobile menu; measured, never followed. Read as `m-sales` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 208 x 50; padding 12px 16px; radius 4px; background #693edf; text Inter 16/24 700, #ffffff `color.neutral.white` |
| focus-visible | outline 1px auto #e59700, offset 1px |

![Mobile sales CTA default](components/crops/m-sales-default.png) ![Mobile sales CTA hover](components/crops/m-sales-hover.png) ![Mobile sales CTA focus-visible](components/crops/m-sales-focus-visible.png) ![Mobile sales CTA pressed](components/crops/m-sales-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 215.08 x 107.25; background transparent; text ABC Normal 42.9/53.62 600, #171717 `color.neutral.ink`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the copy.ai wordmark, the Google/Microsoft provider glyphs, the social glyphs and the playbook/blog artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Everything behind the auth card — the workflows builder, the GTM dashboards, chat, tables, teams and billing — was never reached. The public login.copy.ai card (reached through app.copy.ai/login) shows an email field, Continue with email and the Google/Microsoft anchors; the field was measured and its continue action was never pressed. What the product looks like past that card is not documented here — the marketing pages' claims about it were never verified.

### Pages

- **Demo, trial and checkout.** Get a Demo, Try for free, Get started, Sign up and Contact Sales were measured or screenshotted, never followed; no account was created and no payment surface was reached.
- **OAuth providers.** Continue with Google / Microsoft were measured, never pressed — they leave for the providers' flows.
- **The hero email capture and the contact form** were focused and filled then cleared, never submitted — both POST to copy.ai's own stack.
- **Enterprise plan view.** The Self-Serve/Enterprise segmented toggle's Enterprise half was not switched on; the plan card components were measured on Self-Serve, the default.
- **External surfaces** (help.copy.ai, the academy, social profiles) are linked from the site but were never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **The mega-menu auto-closes** a few seconds after it opens; each flyout-child state re-opened it with the Platform trigger before reading.

### Themes

The public surface paints a single light theme, with ink-dark bands inside it: the 48px top banner fills #171717, the platform feature card bands are deep #29007a purple, and the inverted CTA carries a white fill on its dark band — painted dark surfaces, not a user toggle. The export's "dark" set is the small role set those bands paint.

### Fonts

- **ABC Normal** (600 on every display heading, 500 in places) is licensed and served from cdn.prod.website-files.com; the @font-face blocks live in the cross-origin Webflow bundles (harvested src list in raw/css-vars.json). Inter carries UI text; the auth host paints its own interFont stack. The style guide falls back to system sans — the webfonts are licensed, not shipped.

### Screenshots

- The hero circuit artwork, the playbook/blog imagery and the copy.ai wordmark in the screenshots are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Playbook and blog imagery, plan feature lists, marketing copy and the FAQ text are the product's content; only frames and components were measured.
