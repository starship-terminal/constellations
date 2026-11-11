# Asana components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from asana.com on 2026-11-11, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was sent, submitted or signed into.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (33 components, 80 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (80 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [flyout](screenshots/home-light-flyout.png), [full](screenshots/home-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [faq](screenshots/pricing-light-faq.png), [full](screenshots/pricing-light-full.png) |
| Asana AI | `/product/ai` | [default](screenshots/product-ai-light-default.png), [full](screenshots/product-ai-light-full.png) |
| Features | `/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| Contact sales | `/sales` | [default](screenshots/sales-light-default.png), [full](screenshots/sales-light-full.png) |
| Create account | `/create-account` | [default](screenshots/create-account-light-default.png), [full](screenshots/create-account-light-full.png) |
| Resources | `/resources` | [default](screenshots/resources-light-default.png), [full](screenshots/resources-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Nav flyout, open | home | the nav item's own hover | [home-light-flyout](screenshots/home-light-flyout.png), [flyout-open](#flyout-open) |
| Pricing FAQ, open | pricing | the accordion's own toggle | [pricing-light-faq](screenshots/pricing-light-faq.png), [faq-open](#faq-open) |
| Mobile menu, open | home, phone | the menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 14 components were given a real keyboard focus (a further 1 could not be driven: `hero-cta`). 14 show a visible focus state: `nav-link` (2px solid #4786ff `glow.blue`, offset 2px), `nav-login` (2px solid #4786ff `glow.blue`, offset 2px), `nav-sales` (2px solid #4786ff `glow.blue`, offset 2px), `nav-cta` (2px solid #4786ff `glow.blue`, offset 2px), `flyout-trigger` (1px auto #005fcc, offset 0px), `billing-toggle` (2px solid #24a651, offset 2px), `plan-cta` (1px auto #005fcc, offset 1px), `faq-question` (2px solid #4786ff `glow.blue`, offset 2px), `gate-cta` (2px solid #0d0d0d `black.1000`, offset 2px), `gate-sso` (1px auto #005fcc, offset 0px), `sales-select` (visible change in borderTopColor), `footer-link` (1px auto #005fcc, offset 1px), `footer-social` (1px auto #005fcc, offset 1px), `m-menu-button` (2px solid #4786ff `glow.blue`, offset 2px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): nothing that would submit, sign in or navigate was pressed. Log in, Get started, plan CTAs and the form submits were measured, never followed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `ease` | background-color, border, none | gate-cta, gate-field, m-menu-button, m-menu-open, sales-field, sales-select |
| 0.15s | `ease-in-out` | color | gate-cta |
| 0.2s | `ease` | color | billing-toggle |
| 0.25s | `ease` | border-color | gate-sso |
| 0.3s | `ease` | border, color, none | card, flyout-open, flyout-trigger, footer-link, footer-social, hero-cta, logo, m-nav-link and more |
| 0.8s | `ease` | padding-bottom | faq-open, faq-question |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Header](#header) | 1440 x 68 | - | 6px | #ffffff `white` | rgba(0, 0, 0, 0.15) 0px 2px 8px 0px | 0 |
| [Hero title](#hero-title) | 873.44 x 183.59 | - | - | - | none | 0 |
| [Get started button](#get-started-button) | 104.56 x 44 | - | 100px | #0d0d0d `black.1000` | none | 0px 16px |
| [Plan card](#plan-card) | 298 x 974 | 1px solid transparent | 100px | #f3f3f3 `black.50` | none | 32px |
| [Gate field](#gate-field) | 251.33 x 50 | T: 1px solid #e0e6e8 `gray.3`; B: 1px solid #e0e6e8 `gray.3`; L: 1px solid #e0e6e8 `gray.3` | 3px 0px 0px 3px | #ffffff `white` | none | 0px 0px 0px 16px |
| [Sales field](#sales-field) | 512 x 50 | 1px solid #cfcfcf `black.200` | 2px | #ffffff `white` | none | 10px 32px 10px 16px |
| [Footer](#footer) | 1440 x 845.5 | - | - | #0d0d0d `black.1000` | none | 0 |

## Components

### Shell and navigation

The top nav: logo, Pricing link, Log in, Contact sales and Get started, plus the product flyout.

#### Header
The top nav: logo, Pricing link, Log in, Contact sales, Get started. Read as `header` on the home page.

**Values (default).** size 1440 x 68; background transparent; text TWK Lausanne 14/36 500, #0d0d0d `black.1000`; icon 112 x 22, #0d0e10.

Child layers that carry the look: nav 1440x68 background #ffffff `white`; svg 28x28 border 4px solid transparent; div 209.9x55 background #ffffff `white` radius 6px shadow rgba(0, 0, 0, 0.15) 0px 2px 8px 0px.

![Header default](components/crops/header-default.png)

#### Logo
Read as `logo` on the home page.

**Values (default).** size 136 x 44; padding 0px 12px; radius 100px; background transparent; text TWK Lausanne 16/24 500, #0d0e10; transition color 0.3s ease, border 0.3s ease; icon 112 x 22, #0d0e10.

![Logo default](components/crops/logo-default.png)

#### Nav link
A top-level nav link. Measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 68.81 x 44; padding 0px 12px; radius 100px; background transparent; text TWK Lausanne 14/21 500, #0d0d0d `black.1000`; transition color 0.3s ease |
| hover | text TWK Lausanne 14/21 500, #6e6e6e `black.600` |
| focus-visible | outline 2px solid #4786ff `glow.blue`, offset 2px |
| pressed | text TWK Lausanne 14/21 500, #6e6e6e `black.600` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log in link
The Log in nav action. Measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 63.14 x 44; padding 0px 12px; radius 100px; background transparent; text TWK Lausanne 14/21 500, #0d0d0d `black.1000`; transition none 0.3s ease |
| hover | text TWK Lausanne 14/21 500, #6e6e6e `black.600` |
| focus-visible | outline 2px solid #4786ff `glow.blue`, offset 2px; text TWK Lausanne 14/21 500, #6e6e6e `black.600` |
| pressed | text TWK Lausanne 14/21 500, #6e6e6e `black.600` |

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Contact sales button
The secondary CTA. Measured, never followed. Read as `nav-sales` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 120.36 x 44; padding 0px 16px; radius 100px; background #ffffff `white`; shadow #0d0d0d 0px 0px 0px 1px inset; text TWK Lausanne 14/21 500, #0d0d0d `black.1000`; transition none 0.3s ease |
| hover | background #fafafa `black.20` |
| focus-visible | outline 2px solid #4786ff `glow.blue`, offset 2px |
| pressed | background #fafafa `black.20` |

![Contact sales button default](components/crops/nav-sales-default.png) ![Contact sales button hover](components/crops/nav-sales-hover.png) ![Contact sales button focus-visible](components/crops/nav-sales-focus-visible.png) ![Contact sales button pressed](components/crops/nav-sales-pressed.png)

#### Get started button
The primary CTA. Measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 104.56 x 44; padding 0px 16px; radius 100px; background #0d0d0d `black.1000`; text TWK Lausanne 14/21 500, #ffffff `white`; transition none 0.3s ease |
| hover | background #6e6e6e `black.600` |
| focus-visible | outline 2px solid #4786ff `glow.blue`, offset 2px |
| pressed | background #6e6e6e `black.600` |

![Get started button default](components/crops/nav-cta-default.png) ![Get started button hover](components/crops/nav-cta-hover.png) ![Get started button focus-visible](components/crops/nav-cta-focus-visible.png) ![Get started button pressed](components/crops/nav-cta-pressed.png)

#### Flyout trigger
The nav item opening the product flyout. Read as `flyout-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 119.91 x 44; padding 8px 24px; radius 100px; background transparent; text TWK Lausanne 14/36 500, #0d0d0d `black.1000`; transition none 0.3s ease; icon 10 x 10, #0d0d0d `black.1000` |
| hover | text TWK Lausanne 14/36 500, #6e6e6e `black.600`; icon 10 x 10, #6e6e6e `black.600` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | text TWK Lausanne 14/36 500, #6e6e6e `black.600`; icon 10 x 10, #6e6e6e `black.600` |

![Flyout trigger default](components/crops/flyout-trigger-default.png) ![Flyout trigger hover](components/crops/flyout-trigger-hover.png) ![Flyout trigger focus-visible](components/crops/flyout-trigger-focus-visible.png) ![Flyout trigger pressed](components/crops/flyout-trigger-pressed.png)

#### Flyout, open
The nav after a hover opens the flyout; the crop is the opened panel. Read as `flyout-open` on the home page.

**Values (opened).** size 119.91 x 44; padding 8px 24px; radius 100px; background #f3f3f3 `black.50`; text TWK Lausanne 14/36 500, #0d0d0d `black.1000`; transition none 0.3s ease; icon 10 x 10, #0d0d0d `black.1000`.

![Flyout, open opened](components/crops/flyout-open-opened.png)

### Home

The landing: hero, caps eyebrow labels, section headings and linked cards.

#### Hero title
Read as `hero-title` on the home page.

**Values (default).** size 873.44 x 183.59; background transparent; text TWK Lausanne 102/91.8 300, #0d0e10.

Child layers that carry the look: span 589.6x113 image linear-gradient(90deg, #ff453e 0%, #f481f4 50%, #ff453e 100%).

![Hero title default](components/crops/hero-title-default.png)

#### Hero CTA
A hero action. Measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 167.81 x 64; padding 16px 32px; border 1px solid transparent; radius 100px; background #ffffff `white`; text TWK Lausanne 20/30 400, #0d0d0d `black.1000`; transition color 0.3s ease, border 0.3s ease |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Caps label
A small-caps eyebrow label. Read as `caps-label` on the home page.

**Values (default).** size 180.44 x 24.5; padding 4px 8px; radius 4px; background #f3f3f3 `black.50`; text TWK Lausanne 11/16.5 500, #0d0d0d `black.1000`.

![Caps label default](components/crops/caps-label-default.png)

#### Section heading
Read as `section-title` on the home page.

**Values (default).** size 628 x 108; background transparent; text TWK Lausanne 54/54 300, #0d0d0d `black.1000`.

![Section heading default](components/crops/section-title-default.png)

#### Card
A linked feature/customer card. Read as `card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 282.25 x 63.5; padding 10px; background transparent; text TWK Lausanne 16/24 500, #0d0d0d `black.1000`; transition color 0.3s ease, border 0.3s ease; icon 10 x 10, #0d0d0d `black.1000` |

![Card default](components/crops/card-default.png) ![Card hover](components/crops/card-hover.png)

### Pricing

The pricing grid: plan columns, CTAs and the FAQ accordion.

#### Pricing title
Read as `pricing-title` on the pricing page.

**Values (default).** size 215.39 x 24; background transparent; text TWK Lausanne 16/24 500, #0d0d0d `black.1000`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Billing toggle
The monthly/annual switch. Measured, never switched. Read as `billing-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 62.31 x 24; background transparent; text TWK Lausanne 16/24 500, #6e6e6e `black.600`; transition color 0.2s ease |
| hover | background #f06a6a; text TWK Lausanne 16/24 500, #0d0d0d `black.1000` |
| focus-visible | outline 2px solid #24a651, offset 2px |
| pressed | background #f06a6a; text TWK Lausanne 16/24 500, #0d0d0d `black.1000` |

![Billing toggle default](components/crops/billing-toggle-default.png) ![Billing toggle hover](components/crops/billing-toggle-hover.png) ![Billing toggle focus-visible](components/crops/billing-toggle-focus-visible.png) ![Billing toggle pressed](components/crops/billing-toggle-pressed.png)

#### Plan card
A pricing plan column. Read as `plan-card` on the pricing page.

**Values (default).** size 298 x 974; padding 32px; border 1px solid #cfcfcf `black.200`; radius 16px; background transparent; text TWK Lausanne 36/36 400, #0d0d0d `black.1000`; icon 16 x 16, #0d0d0d `black.1000`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan CTA
The plan column's action. Measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 232 x 58; padding 16px 32px; border 1px solid transparent; radius 100px; background #f3f3f3 `black.50`; text TWK Lausanne 16/24 500, #0d0d0d `black.1000`; transition color 0.3s ease, border 0.3s ease |
| hover | background #e7e7e7 `black.100` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### FAQ question
Read as `faq-question` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 738 x 92.8; padding 32px 0px; background transparent; text TWK Lausanne 24/28.8 500, #0d0d0d `black.1000`; transition padding-bottom 0.8s ease; icon 26 x 13, #0d0d0d `black.1000` |
| focus-visible | outline 2px solid #4786ff `glow.blue`, offset 2px |

Child layers that carry the look: span 24x24 background #f3f3f3 `black.50` radius 100%.

![FAQ question default](components/crops/faq-question-default.png) ![FAQ question hover](components/crops/faq-question-hover.png) ![FAQ question focus-visible](components/crops/faq-question-focus-visible.png) ![FAQ question pressed](components/crops/faq-question-pressed.png)

#### FAQ, open
The row after its own toggle. Read as `faq-open` on the pricing page.

**Values (opened).** size 738 x 76.8; padding 32px 0px 16px 0px; background transparent; text TWK Lausanne 24/28.8 500, #0d0d0d `black.1000`; transition padding-bottom 0.8s ease; icon 26 x 13, #0d0d0d `black.1000`.

Child layers that carry the look: span 24x24 background #f3f3f3 `black.50` radius 100%.

![FAQ, open opened](components/crops/faq-open-opened.png)

### Create account gate

The /create-account sign-up gate: email field, SSO options and continue, measured, never submitted.

#### Gate title
Read as `gate-title` on the create-account page.

Not on the page when it was captured.

#### Gate field
Focused only; nothing typed or sent. Read as `gate-field` on the create-account page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 251.33 x 50; padding 0px 0px 0px 16px; border T: 1px solid #e0e6e8 `gray.3`; B: 1px solid #e0e6e8 `gray.3`; L: 1px solid #e0e6e8 `gray.3`; radius 3px 0px 0px 3px; background #ffffff `white`; text TWK Lausanne 16/normal 400, #222b37 `gray.9`; transition border 0.15s ease; placeholder #6e6e6e `black.600` |
| focused | border T: 1px solid #222b37 `gray.9`; B: 1px solid #222b37 `gray.9`; L: 1px solid #222b37 `gray.9` |

![Gate field default](components/crops/gate-field-default.png) ![Gate field focused](components/crops/gate-field-focused.png)

#### Gate CTA
The form action. Measured, never pressed. Read as `gate-cta` on the create-account page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 173.67 x 50; padding 0px 24px; radius 0px 3px 3px 0px; background #0d0e10; text TWK Lausanne 16/50 500, #ffffff `white`; transition background-color 0.15s ease, color 0.15s ease-in-out; icon 20 x 20, #ffffff `white` |
| hover | background #f06a6a; text TWK Lausanne 16/50 500, #0d0e10; icon 20 x 20, #0d0e10 |
| focus-visible | outline 2px solid #0d0d0d `black.1000`, offset 2px |
| pressed | background #f06a6a; text TWK Lausanne 16/50 500, #0d0e10; icon 20 x 20, #0d0e10 |

![Gate CTA default](components/crops/gate-cta-default.png) ![Gate CTA hover](components/crops/gate-cta-hover.png) ![Gate CTA focus-visible](components/crops/gate-cta-focus-visible.png) ![Gate CTA pressed](components/crops/gate-cta-pressed.png)

#### SSO button
A single-sign-on option. Measured, never pressed. Read as `gate-sso` on the create-account page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 208.5 x 52; padding 6px 10px 6px 4px; border 1px solid #cfcfcf `black.200`; radius 6px; background #ffffff `white`; text TWK Lausanne 16/24 500, #0d0d0d `black.1000`; transition border-color 0.25s ease |
| hover | border 1px solid #273240 |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | border 1px solid #273240 |

![SSO button default](components/crops/gate-sso-default.png) ![SSO button hover](components/crops/gate-sso-hover.png) ![SSO button focus-visible](components/crops/gate-sso-focus-visible.png) ![SSO button pressed](components/crops/gate-sso-pressed.png)

### Contact sales

The sales form's fields and dropdowns, measured, never submitted.

#### Sales title
Read as `sales-title` on the contact sales page.

**Values (default).** size 408 x 402; background transparent; text TWK Lausanne 30/36 400, #0d0e10.

![Sales title default](components/crops/sales-title-default.png)

#### Sales field
Focused only; nothing typed or sent. Read as `sales-field` on the contact sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 512 x 50; padding 10px 32px 10px 16px; border 1px solid #cfcfcf `black.200`; radius 2px; background #ffffff `white`; text Helvetica 13/normal 400, #0d0d0d `black.1000`; transition border 0.15s ease; placeholder #3d3d3d `black.800` |
| focused | border 2px solid #727272 |

![Sales field default](components/crops/sales-field-default.png) ![Sales field focused](components/crops/sales-field-focused.png)

#### Sales select
A form dropdown. Measured, never opened. Read as `sales-select` on the contact sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 512 x 50; padding 10px 64px 10px 16px; border 1px solid #cfcfcf `black.200`; radius 2px; background #ffffff `white`; image an image (data URI); text Helvetica 13/normal 400, #0d0d0d `black.1000`; transition border 0.15s ease |
| hover | border 2px solid #9e9e9e `black.400` |
| focus-visible | border 2px solid #727272 |
| pressed | border 2px solid #9e9e9e `black.400` |

![Sales select default](components/crops/sales-select-default.png) ![Sales select hover](components/crops/sales-select-hover.png) ![Sales select focus-visible](components/crops/sales-select-focus-visible.png) ![Sales select pressed](components/crops/sales-select-pressed.png)

### Footer

The link columns, headings and legal.

#### Footer
Read as `footer` on the home page.

**Values (default).** size 1440 x 845.5; background transparent; text TWK Lausanne 14/24.5 500, #ffffff `white`; icon 24 x 24, #ffffff `white`.

Child layers that carry the look: div 1440x741.5 background #0d0d0d `black.1000`; a 126.2x19 border 1px solid transparent; a 80.9x19 border 1px solid transparent.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; background transparent; text TWK Lausanne 16/24 500, #0d0e10; transition color 0.3s ease, border 0.3s ease; icon 24 x 24, #ffffff `white` |
| hover | text TWK Lausanne 16/24 500, #cd4848 |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | text TWK Lausanne 16/24 500, #cd4848 |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer social icon
Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 16px; background #ffffff `white`; text TWK Lausanne 22/33 500, #0d0e10; transition color 0.3s ease, border 0.3s ease; icon 16 x 16, #0d0e10 |
| hover | background #0d0d0d `black.1000`; text TWK Lausanne 22/33 500, #cd4848; icon 16 x 16, #cd4848 |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #0d0d0d `black.1000`; text TWK Lausanne 22/33 500, #cd4848; icon 16 x 16, #cd4848 |

![Footer social icon default](components/crops/footer-social-default.png) ![Footer social icon hover](components/crops/footer-social-hover.png) ![Footer social icon focus-visible](components/crops/footer-social-focus-visible.png) ![Footer social icon pressed](components/crops/footer-social-pressed.png)

### Mobile (390 wide)

The same surface at phone width, with the menu open.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 64; background transparent; text TWK Lausanne 12/18 500, #ffffff `white`; icon 112 x 22, #0d0e10.

Child layers that carry the look: nav 390x64 background #ffffff `white`; svg 0x0 border 4px solid transparent; div 0x0 background #ffffff `white` radius 6px shadow rgba(0, 0, 0, 0.15) 0px 2px 8px 0px.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; padding 0px 10px; radius 3px; background transparent; text TWK Lausanne 14/36 500, #ffffff `white`; transition none 0.15s ease |
| hover | text TWK Lausanne 14/36 500, #0d0e10 |
| focus-visible | outline 2px solid #4786ff `glow.blue`, offset 2px; transition outline 0.1s ease-in-out, background 0.2s ease-in-out |
| pressed | text TWK Lausanne 14/36 500, #0d0e10 |

Child layers that carry the look: div 16x2 background #0d0d0d `black.1000` radius 1px; div::before 16pxx2px background #0d0d0d `black.1000` radius 1px; div::after 16pxx2px background #0d0d0d `black.1000` radius 1px.

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button hover](components/crops/m-menu-button-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The bar after its own toggle; the crop is the opened nav panel. Read as `m-menu-open` on the home page at 390 wide.

**Values (opened).** size 40 x 40; padding 0px 10px; radius 3px; background transparent; text TWK Lausanne 14/36 500, #0d0e10; transition none 0.15s ease.

Child layers that carry the look: div 12.7x12.7 background #0d0d0d `black.1000` radius 1px; div::before 16pxx2px background #0d0d0d `black.1000` radius 1px; div::after 16pxx2px background #0d0d0d `black.1000` radius 1px.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav link
Read inside the open menu. Read as `m-nav-link` on the home page at 390 wide.

**Values (default).** size 374 x 61; padding 20px; border B: 1px solid #e7e7e7 `black.100`; background transparent; text TWK Lausanne 16/20 500, #0d0d0d `black.1000`; transition color 0.3s ease, border 0.3s ease.

Child layers that carry the look: a 374x61 border 1px solid #e7e7e7 `black.100`.

![Mobile nav link default](components/crops/m-nav-link-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Asana's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **Anything that sends, submits or signs in.** No form was submitted, no prompt was sent, no account was created. The contact-sales .ds-input fields were focused and one sample value typed and deleted, never submitted.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface. The --darkmode-* roles are declared in the shipped CSS but no captured route binds a dark theme; they are emitted as declared evidence, not a painted page.

### Themes

The site paints light on every captured route; the --darkmode-* role vars are declared in the same stylesheet and emitted as the dark set (declared evidence, unbound on the captured pages). The full token layer is recorded in [raw/css-vars.json](raw/css-vars.json).

### Fonts

- **The face** is TWK Lausanne, a webfont the site loads via inline @font-face, falling back to Helvetica Neue/Helvetica; --fontFamily-mono (Consolas) and -print (Georgia) ship for code and print. The style guide renders with system fallbacks.
- Product imagery and the Asana mark in the screenshots are Asana's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The -full shots are whole pages stitched from GPU-texture tiles; the tallest (pricing) is ~9,740 px. No captured page reports an unbounded height.

### Content left out

- Product imagery and the wordmark are Asana's content; only the frames and components were measured.
