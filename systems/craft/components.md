# Craft components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from craft.do on 2026-11-12, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, submitted or paid for; the billing toggle was switched locally and switched back; Try Craft Free, Log in, the platform downloads and every plan CTA were never followed. There is no auth card on www.craft.do — Log in links out to docs.craft.do. Served the Singapore region: prices render SGD.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (28 components, 70 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (70 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Pricing | `/pricing` | [billing](screenshots/pricing-light-billing.png), [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Download | `/download` | [default](screenshots/download-light-default.png), [full](screenshots/download-light-full.png) |
| Imagine | `/imagine` | [default](screenshots/imagine-light-default.png), [full](screenshots/imagine-light-full.png) |
| Learn | `/learn` | [default](screenshots/learn-light-default.png), [full](screenshots/learn-light-full.png) |
| Write | `/write` | [default](screenshots/write-light-default.png), [full](screenshots/write-light-full.png) |
| Blog index | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the 24px menu glyph's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-menu-row), [m-download](#mobile-download-cta) |
| Billing toggle | /pricing | the Yearly/Monthly switch's own toggle — flipped for the shot, flipped back | [pricing-light-billing](screenshots/pricing-light-billing.png), [billing-toggle](#billing-toggle) |
| Consent overlays | every page | none painted; generic overlay-hiding ran as defence-in-depth, never answered | nothing to hide |
| The signed-in product | craft.do apps | there is no auth card on www.craft.do — Log in links out to docs.craft.do and was never followed; the editors live in the apps | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 14 components were given a real keyboard focus. 11 draw an outline ring: `try-cta` (1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 1px), `hero-cta` (1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 1px), `billing-toggle` (1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 0px), `plan-card` (on a child: 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843) offset 1px), `dl-btn` (1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 1px), `imagine-card` (1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 1px), `footer-link` (1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 1px), `social-icon` (1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 1px), `m-menu-button` (1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 0px), `m-nav-item` (1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 0px), `m-download` (1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 1px). 3 draw a focus ring as a shadow instead: `nav-link`, `login-link`, `faq-row`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.4, 0, 0.2, 1)` | -webkit-backdrop-filter, backdrop-filter | header, m-header |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | faq-row |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, color, fill, opacity, outline-color, stroke, text-decoration-color | footer-link, imagine-card, login-link, logo, m-download, m-menu-button, nav-link, social-icon and more |
| 0.4s | `cubic-bezier(0.4, 0, 0.2, 1)` | grid-template-rows, max-height, opacity | m-menu-open |
| 0.5s | `cubic-bezier(0, 0, 0.2, 1)` | all | dl-btn, hero-cta |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 273.05 x 462.69 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The floating 52px pill header (26px radius): the CRAFT wordmark, Product / Imagine / Community / Pricing / Learn / Download links, Log in (to docs.craft.do) and the black 36px Try Craft Free pill.

#### Header
The floating pill header: the CRAFT wordmark, Product / Imagine / Community / Pricing / Learn / Download links, Log in and the black Try Craft Free pill. Read as `header` on the home page.

**Values (default).** size 920 x 52; radius 26px; background transparent; image linear-gradient(rgba(255, 255, 255, 0.4) 10%, rgba(255, 255, 255, 0.8)); shadow rgba(0, 0, 0, 0.1) 0px 12px 12px 2px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px; text UntitledSansFont 16/22.4 400, #030302 `color.palette.black`; transition -webkit-backdrop-filter 0.1s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 100 x 20, #030302 `color.palette.black`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Header default](components/crops/header-default.png)

#### Logo
The CRAFT wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 108 x 28; padding 4px; radius 3.35544e+07px; background transparent; text UntitledSansFont 16/24 400, #030302 `color.palette.black`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 100 x 20, #030302 `color.palette.black`.

![Logo default](components/crops/logo-default.png)

#### Nav link
A header nav link; measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 57.92 x 20; background transparent; text UntitledSansFont 16/22.4 400, #030302 `color.palette.black`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | radius 3.35544e+07px; shadow #ffffff 0px 0px 0px 2px; layers a.small.transition-colors 57.9x20.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 3.35544e+07px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Try Craft Free pill
The black "Try Craft Free" header pill (leads to /download); measured, never followed. Read as `try-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 134.61 x 36; padding 8px 14px; radius 3.35544e+07px; background #030302 `color.palette.black`; shadow rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px; text UntitledSansFont 16/24 500, #ffffff `color.palette.white`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(3, 3, 2, 0.75) |
| focus-visible | outline 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 1px |
| pressed | background rgba(3, 3, 2, 0.75) |

![Try Craft Free pill default](components/crops/try-cta-default.png) ![Try Craft Free pill hover](components/crops/try-cta-hover.png) ![Try Craft Free pill focus-visible](components/crops/try-cta-focus-visible.png) ![Try Craft Free pill pressed](components/crops/try-cta-pressed.png)

#### Log-in link
The "Log in" header link (points at docs.craft.do); measured, never followed. Read as `login-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 44.13 x 22.41; background transparent; text UntitledSansFont 16/22.4 400, #030302 `color.palette.black`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | radius 3.35544e+07px; shadow #ffffff 0px 0px 0px 2px; layers a.small.hidden 44.1x22.4 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 3.35544e+07px |

![Log-in link default](components/crops/login-link-default.png) ![Log-in link hover](components/crops/login-link-hover.png) ![Log-in link focus-visible](components/crops/login-link-focus-visible.png) ![Log-in link pressed](components/crops/login-link-pressed.png)

### Home

The 66px Untitled Serif hero ("Your space for notes, tasks, and big ideas") over the sky collage, the white 48px Try Craft Free pill and the product screenshot.

#### Hero headline
The 66px Untitled Serif hero ("Your space for notes, tasks, and big ideas") over the sky collage. Read as `hero-h1` on the home page.

**Values (default).** size 666 x 132; background transparent; text UntitledSerifFont 66/66 400, #030302 `color.palette.black`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero CTA
The white 48px "Try Craft Free" hero pill (leads to /download); measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 170.61 x 48; padding 16px 32px; radius 3.35544e+07px; background transparent; shadow rgba(0, 0, 0, 0.1) 0px 12px 12px 2px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px; text UntitledSansFont 16/24 500, #030302 `color.palette.black`; transition all 0.5s cubic-bezier(0, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1; a.inline-flex.items-center 170.6x48.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 12px 12px 2px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px 3.35544e+07px; a::before.inline-flex.items-center 170.609pxx48px 24px; div.glass-button-gradient-bg.absolute 170. |
| hover | shadow rgba(0, 0, 0, 0.1) 0px 19.9568px 24.9298px 3.9892px, rgba(0, 0, 0, 0.04) 0px 9.95681px 9.96761px -4.97841px; layers ::before rgba(0, 0, 0, 0) 0px none 1; a.inline-flex.items-center 170.6x48.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 19.9568px 24.9298px 3.9892px, rgba(0, 0, 0, 0.04) 0px 9.95681px 9.96761px -4.97841px 3.35544e+07px; a::before.inline-flex.items-center 170.609pxx48px 24px; div.glass |
| focus-visible | outline 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 1px; layers ::before rgba(0, 0, 0, 0) 0px none 1; a.inline-flex.items-center 170.6x48.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 12px 12px 2px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843) offset 1px 3.35544e+07px; a::before.inline-flex.item |
| pressed | shadow rgba(0, 0, 0, 0.1) 0px 19.7526px 24.598px 3.93816px, rgba(0, 0, 0, 0.04) 0px 9.75263px 9.81447px -4.87632px; layers ::before rgba(0, 0, 0, 0) 0px none 1; a.inline-flex.items-center 170.6x48.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 19.7526px 24.598px 3.93816px, rgba(0, 0, 0, 0.04) 0px 9.75263px 9.81447px -4.87632px 3.35544e+07px; a::before.inline-flex.items-center 170.609pxx48px 24px; div.glass |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

### Pricing

The /pricing surface: the Yearly/Monthly pill toggle, the PLUS plan card, the 54px serif prices, the shadow-block TEAM card and the FAQ accordion. Prices render SGD.

#### Pricing headline
"Choose The Plan That’s Right For You". Read as `price-h1` on the pricing page.

**Values (default).** size 1160 x 59.41; background transparent; text UntitledSerifFont 54/59.4 400, #030302 `color.palette.black`.

![Pricing headline default](components/crops/price-h1-default.png)

#### Billing toggle
A segment of the Yearly/Monthly billing switch (112x40 inside a pill); toggled locally for the shot, never submitted. Read as `billing-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 112 x 48; background transparent; text UntitledSansFont 16/24 500, oklch(0.205 0 0) |
| focus-visible | radius 3.35544e+07px; shadow #ffffff 0px 0px 0px 1px; outline 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 0px; layers button.relative.flex 112.0x48.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 1px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843) offset 0px 3.35544e+07px |

![Billing toggle default](components/crops/billing-toggle-default.png) ![Billing toggle hover](components/crops/billing-toggle-hover.png) ![Billing toggle focus-visible](components/crops/billing-toggle-focus-visible.png) ![Billing toggle pressed](components/crops/billing-toggle-pressed.png)

#### Plan card
The PLUS plan card (name, serif price, /month, feature list, CTA); measured, never used. Read as `plan-card` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 273.05 x 462.69; background transparent; text UntitledSansFont 16/24 500, #030302 `color.palette.black`; layers span.bg-black-900.self-center 0.0x0.0 rgb(3, 3, 2) 3.35544e+07px; a.inline-flex.items-center 153.8x40.0 rgb(3, 3, 2) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px 3.35544e+07px |
| focus-visible | layers span.bg-black-900.self-center 0.0x0.0 rgb(3, 3, 2) 3.35544e+07px; a.inline-flex.items-center 153.8x40.0 rgb(3, 3, 2) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843) offset 1px  |

Child layers that carry the look: span 0x0 background #030302 `color.palette.black` radius 3.35544e+07px; a 153.8x40 background #030302 `color.palette.black` radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px.

![Plan card default](components/crops/plan-card-default.png) ![Plan card hover](components/crops/plan-card-hover.png) ![Plan card focus-visible](components/crops/plan-card-focus-visible.png) ![Plan card pressed](components/crops/plan-card-pressed.png)

#### Plan price
A 54px Untitled Serif price figure on a plan card. Read as `plan-price` on the pricing page.

**Values (default).** size 409.91 x 66; background transparent; text UntitledSerifFont 54/59.4 400, #030302 `color.palette.black`.

![Plan price default](components/crops/plan-price-default.png)

#### Team card
The TEAM plan card — the shadow-block variant. Read as `team-card` on the pricing page.

**Values (default).** size 1400 x 1545.86; radius 24px; background transparent; shadow rgba(0, 0, 0, 0.01) 0px 50px 40px 0px, rgba(0, 0, 0, 0.02) 0px 50px 40px 0px, rgba(0, 0, 0, 0.05) 0px 20px 40px 0px, rgba(0, 0, 0, 0.08) 0px 3px 10px 0px; text UntitledSerifFont 54/59.4 400, #030302 `color.palette.black`; layers section.shadow-block.relative 1400.0x1545.9 rgba(0, 0, 0, 0.01) 0px 50px 40px 0px, rgba(0, 0, 0, 0.02) 0px 50px 40px 0px, rgba(0, 0, 0, 0.05) 0px 20px 40px 0px, rgba(0, 0, 0, 0.08) 0px 3px 10px 0px 24px; div.shadow-block.absolute 1400.0x1545.9 rgba(0, 0, 0, 0.01) 0px 50px 40px 0px, rgba(0, 0, 0, 0.02) 0px 50px 40px 0px, rgba(0, 0, 0, 0.05) 0px 20px 40px 0px, rgba(0, 0, 0, 0.08) 0px 3px 10px 0px 24.

![Team card default](components/crops/team-card-default.png)

#### FAQ row
A pricing FAQ accordion row (shadcn-style ring on focus-visible); toggled locally. Read as `faq-row` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1000 x 57.2; padding 16px 0px; radius 8px; background transparent; text UntitledSansFont 18/25.2 500, #030302 `color.palette.black`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 22 x 22, #030302 `color.palette.black` |
| focus-visible | shadow oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843) 0px 0px 0px 3px; layers button.focus-visible:border-ring.focus-visible:ring-ring/50 1000.0x57.2 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843) 0px 0px 0px 3px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 8px |

![FAQ row default](components/crops/faq-row-default.png) ![FAQ row hover](components/crops/faq-row-hover.png) ![FAQ row focus-visible](components/crops/faq-row-focus-visible.png) ![FAQ row pressed](components/crops/faq-row-pressed.png)

### Download

The /download surface: the 54px serif heading and the platform download buttons.

#### Download headline
"Get Craft for Free". Read as `dl-h1` on the download page.

**Values (default).** size 386.56 x 59.41; background transparent; text UntitledSerifFont 54/59.4 400, #030302 `color.palette.black`.

![Download headline default](components/crops/dl-h1-default.png)

#### Platform button
A platform download action; measured, never followed. Read as `dl-btn` on the download page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 226.42 x 48; padding 16px 32px; radius 3.35544e+07px; background transparent; shadow rgba(0, 0, 0, 0.1) 0px 12px 12px 2px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px; text UntitledSansFont 16/24 500, #030302 `color.palette.black`; transition all 0.5s cubic-bezier(0, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1; a.inline-flex.items-center 226.4x48.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 12px 12px 2px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px 3.35544e+07px; a::before.inline-flex.items-center 226.422pxx48px 24px; div.glass-button-gradient-bg.absolute 226. |
| hover | shadow rgba(0, 0, 0, 0.1) 0px 19.9566px 24.9295px 3.98916px, rgba(0, 0, 0, 0.04) 0px 9.95664px 9.96748px -4.97832px; layers ::before rgba(0, 0, 0, 0) 0px none 1; a.inline-flex.items-center 226.4x48.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 19.9566px 24.9295px 3.98916px, rgba(0, 0, 0, 0.04) 0px 9.95664px 9.96748px -4.97832px 3.35544e+07px; a::before.inline-flex.items-center 226.422pxx48px 24px; div.glas |
| focus-visible | outline 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 1px; layers ::before rgba(0, 0, 0, 0) 0px none 1; a.inline-flex.items-center 226.4x48.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 12px 12px 2px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843) offset 1px 3.35544e+07px; a::before.inline-flex.item |
| pressed | shadow rgba(0, 0, 0, 0.1) 0px 19.8201px 24.7077px 3.95503px, rgba(0, 0, 0, 0.04) 0px 9.8201px 9.86508px -4.91005px; layers ::before rgba(0, 0, 0, 0) 0px none 1; a.inline-flex.items-center 226.4x48.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 19.8201px 24.7077px 3.95503px, rgba(0, 0, 0, 0.04) 0px 9.8201px 9.86508px -4.91005px 3.35544e+07px; a::before.inline-flex.items-center 226.422pxx48px 24px; div.glass |

![Platform button default](components/crops/dl-btn-default.png) ![Platform button hover](components/crops/dl-btn-hover.png) ![Platform button focus-visible](components/crops/dl-btn-focus-visible.png) ![Platform button pressed](components/crops/dl-btn-pressed.png)

### Product pages

The /imagine, /learn and /write surfaces: 54-70px serif headings, template cards.

#### Imagine headline
The imagine page heading. Read as `imagine-h1` on the imagine page.

**Values (default).** size 832.33 x 118.81; background transparent; text UntitledSerifFont 54/59.4 400, #030302 `color.palette.black`.

![Imagine headline default](components/crops/imagine-h1-default.png)

#### Learn headline
The learn page heading. Read as `learn-h1` on the learn page.

**Values (default).** size 475.23 x 126; background transparent; text UntitledSerifFont 70/63 400, #030302 `color.palette.black`.

![Learn headline default](components/crops/learn-h1-default.png)

#### Write headline
The write page heading. Read as `write-h1` on the write page.

**Values (default).** size 647.28 x 132; background transparent; text UntitledSerifFont 66/66 400, #030302 `color.palette.black`.

![Write headline default](components/crops/write-h1-default.png)

#### Template card
A template card on /imagine (Blog Publisher, Reading Tracker); measured, never followed. Read as `imagine-card` on the imagine page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 712 x 398.78; background transparent; text UntitledSerifFont 46/56.12 400, #030302 `color.palette.black`; transition opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #030302 `color.palette.black`; layers div.bg-card.text-card-foreground 712.0x398.8 rgb(255, 255, 255) T:1px solid rgba(3, 3, 2, 0.09) / R:1px solid rgba(3, 3, 2, 0.09) / B:1px solid rgba(3, 3, 2, 0.09) / L:1px solid rgba(3, 3, 2, 0.09) rgba(0, 0, 0, 0.01) 0px 50px 40px 0px, rgba(0, 0, 0, 0.02) 0px 50px 40px 0px, rgba(0, 0, 0, 0.05) 0px 20px 40px 0px, rgba(0, 0, 0, 0.08) 0px 3px 10px 0px 24px; div.relative.flex 339.0x372.8 rgb(250, 248 |
| hover | opacity 0.8 |
| focus-visible | outline 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 1px; layers a.group.block 712.0x398.8 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843) offset 1px; div.bg-card.text-card-foreground 712.0x398.8 rgb(255, 255, 255) T:1px solid rgba(3, 3, 2, 0.09) / R:1px solid rgba(3, 3, 2, 0.09) / B:1px solid rgba(3, 3, 2, 0.09) / L:1px solid rgba(3, 3, 2, 0.09) rgba(0, 0, 0, 0.01) 0px 50px 40px 0px, rgba(0, 0, 0, 0.02) 0px 50px 40px 0px, rgba(0, 0, 0, 0.05) 0px 2 |
| pressed | opacity 0.8 |

Child layers that carry the look: div 712x398.8 background #ffffff `color.palette.white` border 1px solid rgba(3, 3, 2, 0.09) `color.palette.black-100` radius 24px shadow rgba(0, 0, 0, 0.01) 0px 50px 40px 0px, rgba(0, 0, 0, 0.02) 0px 50px 40px 0px, rgba(0, 0, 0, 0.05) 0px 20px 40px 0px, rgba(0, 0, 0, 0.08) 0px 3px 10px 0px; div 339x372.8 background #faf8f4 radius 10px; div 24x24 radius 6px shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px.

![Template card default](components/crops/imagine-card-default.png) ![Template card hover](components/crops/imagine-card-hover.png) ![Template card focus-visible](components/crops/imagine-card-focus-visible.png) ![Template card pressed](components/crops/imagine-card-pressed.png)

### Footer

The black 24px-radius footer panel: white link columns, socials and legal.

#### Footer
The footer: link columns, the app badges and the legal row. Read as `footer` on the home page.

**Values (default).** size 1408 x 562.5; padding 0px 24px; radius 24px; background #030302 `color.palette.black`; text UntitledSansFont 14/21 500, #ffffff `color.palette.white`; icon 24 x 24, #ffffff `color.palette.white`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 114.28 x 17; background transparent; text UntitledSansFont 14/21 400, #ffffff `color.palette.white`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 1px; layers a.text-white 114.3x17.0 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A social link in the footer. Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 69.38 x 17; background transparent; text UntitledSansFont 14/21 400, #ffffff `color.palette.white`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 1px; layers a.text-white 69.4x17.0 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843) offset 1px |

![Social link default](components/crops/social-icon-default.png) ![Social link hover](components/crops/social-icon-hover.png) ![Social link focus-visible](components/crops/social-icon-focus-visible.png) ![Social link pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The same surface at phone width: the header keeps the wordmark + Try pill + 24px menu glyph, and the menu opens as a pill overlay with accordion rows and a black Download for iOS pill.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 342 x 52; radius 26px; background transparent; image linear-gradient(rgba(255, 255, 255, 0.4) 10%, rgba(255, 255, 255, 0.8)); shadow rgba(0, 0, 0, 0.1) 0px 12px 12px 2px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px; text UntitledSansFont 13/19.5 500, #ffffff `color.palette.white`; transition -webkit-backdrop-filter 0.1s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 100 x 20, #030302 `color.palette.black`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The header menu button that opens the nav overlay. Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 24; background transparent; text UntitledSansFont 15/21 400, #030302 `color.palette.black`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #030302 `color.palette.black` |
| focus-visible | outline 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 0px; layers button.small.text-black-900 24.0x24.0 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843) offset 0px |

![Menu button default](components/crops/m-menu-button-default.png) ![Menu button hover](components/crops/m-menu-button-hover.png) ![Menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The opened nav overlay: the Product / Imagine / Pricing rows with Try Craft Free and Log in. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 342 x 617.75; background transparent; text UntitledSansFont 15/21 400, #030302 `color.palette.black`; transition grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1), max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.914931; icon 24.76 x 24.76, #030302 `color.palette.black`; layers li.flex.h-full 310.0x304.6 oklab(1 0 5.96046e-8 / 0.5) 16px; div.bg-black-200.h-px 286.0x0.4 rgba(3, 3, 2, 0.12); div.absolute.inset-0 286.0x22.6 oklab(0 0 0 / 0) 14px; div.h-2.w-2 8.0x8.0 rgb(253, 233, 155) 3.35544e+07px; div.absolute.inset-0 286.0x22.5 oklab(0 0 0 / 0) 14px; div.h-2.w-2 8.0x8.0 rgb(184, 202, 245) 3.35544e+07px.

Child layers that carry the look: li 310x304.6 background oklab(1 0 5.96046e-8 / 0.5) radius 16px; div 286x0.4 background rgba(3, 3, 2, 0.12) `color.palette.black-200`; div 286x22.6 background oklab(0 0 0 / 0) radius 14px.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile menu row
A row inside the opened nav overlay. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 310 x 46; padding 12px; background transparent; text UntitledSansFont 15/21 400, #030302 `color.palette.black`; icon 22 x 22, #030302 `color.palette.black` |
| focus-visible | outline 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 0px; layers button.flex.w-full 310.0x46.0 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843) offset 0px |

![Mobile menu row default](components/crops/m-nav-item-default.png) ![Mobile menu row hover](components/crops/m-nav-item-hover.png) ![Mobile menu row focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile menu row pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 318 x 144; background transparent; text UntitledSerifFont 48/48 400, #030302 `color.palette.black`.

![Mobile headline default](components/crops/m-hero-default.png)

#### Mobile download CTA
The black "Download for iOS" pill at the foot of the mobile menu; measured, never followed. Read as `m-download` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 310 x 46; padding 8px 12px; radius 16px; background #030302 `color.palette.black`; shadow rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px; text UntitledSansFont 16/24 500, #ffffff `color.palette.white`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto oklab(0.0959089 -0.00155481 0.00499368 / 0.0607843), offset 1px |

![Mobile download CTA default](components/crops/m-download-default.png) ![Mobile download CTA hover](components/crops/m-download-hover.png) ![Mobile download CTA focus-visible](components/crops/m-download-focus-visible.png) ![Mobile download CTA pressed](components/crops/m-download-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the CRAFT wordmark, the menu glyph, the social glyphs and the collage artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The editors — the docs editor, tasks, calendar and every app surface — were never reached. www.craft.do has no auth card: the header Log in links out to docs.craft.do (never followed) and Try Craft Free leads to /download (never used). What the product looks like past the marketing surface is not documented here.

### Pages

- **Downloads and CTAs.** Try Craft Free, the platform download buttons, every plan CTA and Get Started were measured or screenshotted, never followed; no purchase was made and no file fetched.
- **Log in** links out to docs.craft.do and was never followed — there is no credential surface on www.craft.do.
- **External surfaces** (docs.craft.do, the Slack community invite, social profiles) are linked from the site but were never opened.
- **Regional pricing.** Prices render in the served region's currency (SGD) — the plan-card prices are regional, not a universal figure.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **The mega-menu auto-closes** a few seconds after it opens; each flyout-child state re-opened it with the Platform trigger before reading.

### Themes

The public surface paints a single light theme; no dark var set exists in the sheets. The only painted dark surface is the black footer panel (and the black pills) — a section fill, not a theme.

### Fonts

- **Untitled Serif** (400 on every display heading) and **Untitled Sans** (400/500 UI) are Klim faces served same-origin (harvested src list in raw/css-vars.json). The style guide falls back to system serif/sans — the webfonts are licensed, not shipped.

### Screenshots

- The collage artwork, product screenshots and the CRAFT wordmark in the screenshots are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The collage illustration, product screenshots, template imagery, plan feature lists and marketing copy are the product's content; only frames and components were measured.
