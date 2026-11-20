# Doppler components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from doppler.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. doppler.com is a Next.js/Tailwind marketing site painting one dark theme (warm-black #1c1624, Doppler Repro / Doppler Repro Mono / Inter). Nothing was signed into, booked, bought or submitted; the demo form's fields were focused and sample-filled then deleted; the dashboard at dashboard.doppler.com was never reached and the cookie-preferences banner was hidden, never answered.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (60 components, 137 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `DopplerRepro 15/15 700, #f1f0ec`, and is read from the first text node inside the component. (The served face names are mangled Next.js locals — `__DopplerRepro_a18e76` — shown here without the `__` prefix and hash.)
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (137 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-dark-{state}.png`: every captured surface paints the same dark theme. Desktop shots are 1440 x 900; `-full` shots are whole pages; mobile shots are `mobile-{page}-dark-{state}.png`, 780 wide (390 at 2x). The mobile full pages exceeded the capture bound and were stitched from chunks.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [menu](screenshots/home-dark-menu.png) |
| Platform: secrets manager | `/platform/secrets-manager` | [default](screenshots/platform-dark-default.png), [full](screenshots/platform-dark-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-dark-default.png), [full](screenshots/pricing-dark-full.png) |
| Demo request | `/demo` | [default](screenshots/demo-dark-default.png), [full](screenshots/demo-dark-full.png) |
| Doppler for Agents | `/agents` | [default](screenshots/agents-dark-default.png), [full](screenshots/agents-dark-full.png) |
| Integrations | `/integrations` | [default](screenshots/integrations-dark-default.png), [full](screenshots/integrations-dark-full.png) |
| Customers | `/customers` | [default](screenshots/customers-dark-default.png), [full](screenshots/customers-dark-full.png) |
| Blog | `/blog` | [default](screenshots/blog-dark-default.png), [full](screenshots/blog-dark-full.png) |
| About | `/about` | [default](screenshots/about-dark-default.png), [full](screenshots/about-dark-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png), [menu](screenshots/mobile-home-dark-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-dark-default.png), [full](screenshots/mobile-pricing-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Platform mega-menu | every marketing page | the nav trigger's own hover | [home-dark-menu](screenshots/home-dark-menu.png), [nav-dropdown](#nav-dropdown), [menu-link](#menu-link) |
| Mobile menu sheet | home, phone width | the hamburger button's own toggle | [mobile-home-dark-menu](screenshots/mobile-home-dark-menu.png), [m-menu-open](#mobile-menu-open) |
| Cookie-preferences banner | every page | hidden, never answered (no consent button was ever clicked, no consent POST sent) | hidden before every shot and reading |
| Pricing FAQ accordion | /pricing | a row is open by default; no row was toggled for the open state | [faq-open](#faq-accordion-open) |
| Demo form | /demo | fields were focused and sample-filled then deleted — the Choose-a-Time submit was never pressed | [demo-field](#text-field), [demo-submit](#submit-button) |
| The product (dashboard) | dashboard.doppler.com | the secrets workspace lives behind sign-in; Start for Free / Sign In point off-site and were never followed | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 22 components were given a real keyboard focus. 22 draw an outline ring: `nav-trigger` (1px auto #005fcc, offset 0px), `nav-link` (1px auto #005fcc, offset 1px), `nav-demo` (1px auto #005fcc, offset 1px), `nav-cta` (1px auto #005fcc, offset 1px), `nav-signin` (1px auto #005fcc, offset 1px), `menu-link` (1px auto #005fcc, offset 1px), `hero-cta` (1px auto #005fcc, offset 1px), `faq-item` (1px auto #005fcc, offset 0px), `demo-submit` (1px auto #005fcc, offset 0px), `filter-chip` (1px auto #005fcc, offset 0px), `request-integration` (1px auto #005fcc, offset 0px), `cat-chip` (1px auto #005fcc, offset 0px), `cat-chip-active` (1px auto #005fcc, offset 0px), `page-number` (1px auto #005fcc, offset 0px), `industry-chip` (1px auto #005fcc, offset 0px), `agents-cta` (1px auto #005fcc, offset 1px), `footer-link` (1px auto #005fcc, offset 1px), `cookie-button` (1px auto #005fcc, offset 0px), `m-nav-item` (1px auto #005fcc, offset 1px), `m-cta` (1px auto #005fcc, offset 1px), `read-more` (1px auto #005fcc, offset 1px), `plan-cta` (1px auto #005fcc, offset 1px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | seat-field |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | agents-cta, cookie-button, demo-email, demo-field, demo-select, demo-submit, footer-link, hero-cta and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Feature card](#feature-card) | 396 x 287.84 | - | 20px | rgba(242, 241, 237, 0.04) `color.alpha.w4` | none | 0 |
| [Plan card](#plan-card) | 396 x 938.55 | - | 20px | rgba(242, 241, 237, 0.04) `color.alpha.w4` | none | 32px |
| [Post card](#post-card) | 396 x 570 | - | 20px | rgba(242, 241, 237, 0.04) `color.alpha.w4` | none | 0 |
| [Integration card](#integration-card) | 289 x 181.2 | - | 20px | rgba(242, 241, 237, 0.04) `color.alpha.w4` | none | 32px |
| [Case-study card](#case-study-card) | 1224 x 590.16 | 1px solid rgba(255, 255, 255, 0.08) `color.alpha.glow` | 20px | #2d2734 `color.warm.raised` | none | 0 |
| [Agents card](#agents-card) | 396 x 168.59 | - | 20px | rgba(242, 241, 237, 0.04) `color.alpha.w4` | none | 0 |
| [Platform feature card](#platform-feature-card) | 610 x 516.25 | - | 20px | rgba(242, 241, 237, 0.04) `color.alpha.w4` | none | 0 |
| [Demo card](#demo-card) | 628.61 x 541.41 | - | 20px | rgba(242, 241, 237, 0.04) `color.alpha.w4` | none | 20px 32px |

## Components

### Shell and navigation

The floating marketing header on the warm-black field: the 72px bar inset 14px from the edge, the Platform mega-menu trigger and panel, plain links, the bordered Get-Demo and Sign-In actions and the fluorescent-green Start-for-Free pill.

#### Header
The sticky marketing header: a 72px warm-black bar with a 1px glow-stroke border and 16px bottom radii — wordmark, the Platform/Solutions/Resources dropdowns, Doppler for Agents, Customers, Pricing, Get Demo, the green Start-for-Free pill and Sign In. Read as `header` on the home page.

**Values (default).** size 1412 x 72; padding 0px 20px; border R: 1px solid #55505b `color.warm.glowStrokeLight`; B: 1px solid #55505b `color.warm.glowStrokeLight`; L: 1px solid #55505b `color.warm.glowStrokeLight`; radius 0px 0px 16px 16px; background #1c1624 `color.warm.black`; text DopplerRepro 15/15 700, #d0c9c4 `color.neutral.silver`; icon 14 x 9, #d0c9c4 `color.neutral.silver`.

![Header default](components/crops/header-default.png)

#### Logo
The Doppler wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 156 x 31; background transparent; text DopplerRepro 16/24 400, #f1f0ec `color.neutral.warmWhite`.

![Logo default](components/crops/logo-default.png)

#### Nav trigger
The Platform button that opens the header mega-menu; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 105.8 x 71; padding 28px 8px; background transparent; text DopplerRepro 15/15 700, #d0c9c4 `color.neutral.silver`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 9, #d0c9c4 `color.neutral.silver` |
| hover | text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite`; icon 14 x 9, #f1f0ec `color.neutral.warmWhite` |
| focus-visible | outline 1px auto #005fcc, offset 0px; text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite`; icon 14 x 9, #f1f0ec `color.neutral.warmWhite`; layers button.flex.items-center 105.8x71.0 1px auto rgb(0, 95, 204) offset 0px |
| pressed | text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite`; icon 14 x 9, #f1f0ec `color.neutral.warmWhite` |

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav link
The plain Pricing header link. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 71.08 x 71; padding 28px 8px; background transparent; text DopplerRepro 15/15 700, #d0c9c4 `color.neutral.silver`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite` |
| focus-visible | outline 1px auto #005fcc, offset 1px; text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite`; layers a.p-8.py-28 71.1x71.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Demo link
The Get-Demo header action; measured never followed. Read as `nav-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 91.91 x 31; padding 8px; background transparent; text DopplerRepro 15/15 700, #d0c9c4 `color.neutral.silver`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite` |
| focus-visible | outline 1px auto #005fcc, offset 1px; text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite`; layers a.p-8.text-link 91.9x31.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite` |

![Demo link default](components/crops/nav-demo-default.png) ![Demo link hover](components/crops/nav-demo-hover.png) ![Demo link focus-visible](components/crops/nav-demo-focus-visible.png) ![Demo link pressed](components/crops/nav-demo-pressed.png)

#### Nav CTA
The fluorescent-green Start-for-Free pill (points off-site to dashboard.doppler.com/register); measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 156.31 x 36.05; padding 10px 16px; radius 12px; background #00f575 `color.brand.green`; text DopplerRepro 15/15 700, #1c1624 `color.warm.black`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 12, #1c1624 `color.warm.black` |
| hover | background #00bf5b `color.brand.greenDark` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #00bf5b `color.brand.greenDark` |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Sign-in link
The bordered Sign-In header action (points off-site to dashboard.doppler.com/login); measured never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 86.75 x 37; padding 10px 16px; border 1px solid #f1f0ec `color.neutral.warmWhite`; radius 12px; background transparent; text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(242, 241, 237, 0.08) `color.alpha.w8` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background rgba(242, 241, 237, 0.08) `color.alpha.w8` |

![Sign-in link default](components/crops/nav-signin-default.png) ![Sign-in link hover](components/crops/nav-signin-hover.png) ![Sign-in link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign-in link pressed](components/crops/nav-signin-pressed.png)

#### Nav dropdown
The Platform mega-menu panel, opened by its own trigger. Read as `nav-dropdown` on the home page.

**Values (default).** size 720 x 372; padding 30px; border R: 1px solid #55505b `color.warm.glowStrokeLight`; B: 1px solid #55505b `color.warm.glowStrokeLight`; L: 1px solid #55505b `color.warm.glowStrokeLight`; radius 0px 0px 20px 20px; background #1c1624 `color.warm.black`; text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite`; icon 32 x 32, #f1f0ec `color.neutral.warmWhite`.

![Nav dropdown default](components/crops/nav-dropdown-default.png)

#### Menu link
A feature link inside the opened mega-menu. Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 314 x 73; background transparent; text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite`; icon 14 x 12, #00f575 `color.brand.green` |
| hover | text DopplerRepro 15/15 700, #00f575 `color.brand.green` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.group.flex 314.0x73.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | outline 1px auto #005fcc, offset 1px; text DopplerRepro 15/15 700, #00f575 `color.brand.green`; layers a.group.flex 314.0x73.0 1px auto rgb(0, 95, 204) offset 1px |

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link focus-visible](components/crops/menu-link-focus-visible.png) ![Menu link pressed](components/crops/menu-link-pressed.png)

### Home hero

The 48px Doppler Repro hero with its lilac-to-carmine gradient line, the silver lede and the bordered Start-for-Free button.

#### Hero headline
The display headline ("One platform. Every secret. Human or AI.") with a lilac-to-carmine gradient line. Read as `hero-title` on the home page.

**Values (default).** size 304.86 x 172.78; background transparent; text DopplerRepro 48/57.6 450, #f1f0ec `color.neutral.warmWhite`; layers span.inline.bg-clip-text 281.6x71.0 image.

Child layers that carry the look: span 281.6x71 image linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%).

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede paragraph under the headline. Read as `hero-sub` on the home page.

**Values (default).** size 450 x 100.81; background transparent; text DopplerRepro 18/25.2 400, #d0c9c4 `color.neutral.silver`.

![Hero copy default](components/crops/hero-sub-default.png)

#### Hero CTA
The green Start-for-Free button in the hero; measured never followed. Read as `hero-cta` on the home page.

**Known wrong; recapture needed.** The reading is an outlined "Start for Free" link (transparent fill, 1px warm-white border), not the green hero CTA: the selector took the last match.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 136.31 x 45; padding 14px 16px; border 1px solid #f1f0ec `color.neutral.warmWhite`; radius 12px; background transparent; text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(242, 241, 237, 0.08) `color.alpha.w8` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background rgba(242, 241, 237, 0.08) `color.alpha.w8` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

### Home

Sections of the home page: light-purple section headings and the 4%-veil interactive cards.

#### Section heading
A gradient-text section heading ("Built for every identity"). Read as `h2-section` on the home page.

**Values (default).** size 315.63 x 38.41; background transparent; text DopplerRepro 32/38.4 450, #b997ff `color.brand.lightPurple`.

![Section heading default](components/crops/h2-section-default.png)

#### Feature card
A .interactive-card tile under a section heading (the "Built for every identity" cards). Read as `feature-card` on the home page.

**Values (default).** size 396 x 287.84; radius 20px; background rgba(242, 241, 237, 0.04) `color.alpha.w4`; text DopplerRepro 24/33.6 700, #f1f0ec `color.neutral.warmWhite`; icon 14 x 12, #d0c9c4 `color.neutral.silver`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 0.

![Feature card default](components/crops/feature-card-default.png)

#### Platform title
The secrets-manager product-page heading. Read as `platform-h1` on the platform secrets-manager page.

**Values (default).** size 470.59 x 115.19; background transparent; text DopplerRepro 48/57.6 450, transparent; layers span.inline.bg-clip-text 470.6x71.0 image.

Child layers that carry the look: span 470.6x71 image linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%).

![Platform title default](components/crops/platform-h1-default.png)

#### Platform feature card
A .interactive-card feature tile on the secrets-manager page. Read as `platform-card` on the platform secrets-manager page.

**Values (default).** size 610 x 516.25; radius 20px; background rgba(242, 241, 237, 0.04) `color.alpha.w4`; text DopplerRepro 24/33.6 700, #f1f0ec `color.neutral.warmWhite`; icon 14 x 12, #d0c9c4 `color.neutral.silver`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 0.

![Platform feature card default](components/crops/platform-card-default.png)

### Pricing

The pricing surface: the seats slider and $100,000 spend field, the three plan cards with their bordered CTAs, the MOST POPULAR badge and the FAQ accordion.

#### Pricing title
The "One bill. No surprises." display heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 572.94 x 201.59; background transparent; text DopplerRepro 96/100.8 450, #f1f0ec `color.neutral.warmWhite`; layers span.inline.bg-clip-text 572.9x130.0 image.

Child layers that carry the look: span 572.9x130 image linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%).

![Pricing title default](components/crops/pricing-h1-default.png)

#### Seat slider
The seats range input in the pricing calculator; focused, never dragged past a checkout. Read as `seat-slider` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1252 x 10; radius 35px; background transparent; image linear-gradient(to right, #7d6ea3 9.45674%, #3e384b 9.45674%); text DopplerRepro 16/24 400, #f1f0ec `color.neutral.warmWhite`; placeholder #f1f0ec `color.neutral.warmWhite` |
| focused | image linear-gradient(to right, #7d6ea3 50.1006%, #3e384b 50.1006%) |

![Seat slider default](components/crops/seat-slider-default.png) ![Seat slider focused](components/crops/seat-slider-focused.png)

#### Spend field
The "$100,000" currency field beside the seats slider; focused only. Read as `seat-field` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 332 x 52; padding 10px 20px; border 1px solid #44403c `color.warm.stone`; radius 6px; background rgba(242, 241, 237, 0.04) `color.alpha.w4`; outline 2px solid transparent, offset 2px; text DopplerRepro 20/30 400, #f1f0ec `color.neutral.warmWhite`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #f1f0ec `color.neutral.warmWhite` |
| focused | border 1px solid #b997ff `color.brand.lightPurple` |

![Spend field default](components/crops/seat-field-default.png) ![Spend field focused](components/crops/seat-field-focused.png)

#### Plan name
A plan card's name. Read as `plan-name` on the pricing page.

**Values (default).** size 332 x 38.41; background transparent; text DopplerRepro 32/38.4 450, #f1f0ec `color.neutral.warmWhite`.

![Plan name default](components/crops/plan-name-default.png)

#### Plan price
A plan card's price figure (e.g. "$8/mo per additional user"). Read as `plan-price` on the pricing page.

**Values (default).** size 332 x 33.59; background transparent; text DopplerRepro 24/33.6 400, #f1f0ec `color.neutral.warmWhite`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan badge
The MOST POPULAR chip on the Team card. Read as `plan-badge` on the pricing page.

**Values (default).** size 332 x 22; background transparent; text DopplerRepro 10/10 700, #f1f0ec `color.neutral.warmWhite`; icon 17.36 x 22, #f1f0ec `color.neutral.warmWhite`; layers span.ease.z-1 96.8x22.0 rgb(48, 44, 55).

Child layers that carry the look: span 96.8x22 background #302c37 `color.warm.badge`.

![Plan badge default](components/crops/plan-badge-default.png)

#### Plan card
A pricing plan card (the painted ancestor of the plan name). Read as `plan-card` on the pricing page.

**Values (default).** size 396 x 938.55; padding 32px; radius 20px; background rgba(242, 241, 237, 0.04) `color.alpha.w4`; text DopplerRepro 32/38.4 450, #f1f0ec `color.neutral.warmWhite`; icon 14 x 14, #f1f0ec `color.neutral.warmWhite`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Plan card default](components/crops/plan-card-default.png)

#### FAQ accordion
A closed FAQ row (aria-expanded=false); the open state below is a row expanded by its own toggle. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 892 x 57.2; padding 16px 0px; background transparent; text DopplerRepro 18/25.2 500, #f1f0ec `color.neutral.warmWhite`; icon 24 x 25, #8b877d `color.neutral.aluminum` |
| focus-visible | outline 1px auto #005fcc, offset 0px; layers button.flex.w-full 892.0x57.2 1px auto rgb(0, 95, 204) offset 0px |

![FAQ accordion default](components/crops/faq-item-default.png) ![FAQ accordion hover](components/crops/faq-item-hover.png) ![FAQ accordion focus-visible](components/crops/faq-item-focus-visible.png) ![FAQ accordion pressed](components/crops/faq-item-pressed.png)

#### FAQ accordion, open
An expanded FAQ row container (question plus revealed answer). Read as `faq-open` on the pricing page.

**Values (default).** size 892 x 181.98; padding 16px 0px; border B: 1px solid rgba(255, 255, 255, 0.08) `color.alpha.glow`; background transparent; text DopplerRepro 18/25.2 500, #f1f0ec `color.neutral.warmWhite`; icon 34.65 x 34.65, #f1f0ec `color.neutral.warmWhite`; layers div.w-full.border-b-1 892.0x182.0 B:1px solid rgba(255, 255, 255, 0.08); span.absolute.-bottom-1 0.0x2.0 rgb(185, 151, 255).

Child layers that carry the look: div 892x182 border 1px solid rgba(255, 255, 255, 0.08) `color.alpha.glow`; span 0x2 background #b997ff `color.brand.lightPurple`.

![FAQ accordion, open default](components/crops/faq-open-default.png)

#### Plan CTA
A plan card's action; measured never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 332 x 45; padding 14px 16px; border 1px solid #f1f0ec `color.neutral.warmWhite`; radius 12px; background transparent; text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(242, 241, 237, 0.08) `color.alpha.w8` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background rgba(242, 241, 237, 0.08) `color.alpha.w8` |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

### Demo request

The 'See Doppler in action' panel: a real form, focused and sample-filled then deleted, never submitted — plus the green-check benefit list.

#### Demo title
The demo-request display heading. Read as `demo-h1` on the demo request page.

**Values (default).** size 563.39 x 172.78; background transparent; text DopplerRepro 48/57.6 450, #f1f0ec `color.neutral.warmWhite`; layers span.inline.bg-clip-text 538.6x128.6 image.

Child layers that carry the look: span 538.6x128.6 image linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%).

![Demo title default](components/crops/demo-h1-default.png)

#### Demo card
The "See Doppler in action" form panel; never submitted. Read as `demo-card` on the demo request page.

**Values (default).** size 628.61 x 541.41; padding 20px 32px; radius 20px; background rgba(242, 241, 237, 0.04) `color.alpha.w4`; text DopplerRepro 24/33.6 450, #b997ff `color.brand.lightPurple`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Demo card default](components/crops/demo-card-default.png)

#### Text field
The First-name input; sample text was typed and deleted, nothing sent. Read as `demo-field` on the demo request page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 276.3 x 43.2; padding 8px 16px; border 1px solid #8b877d `color.neutral.aluminum`; radius 16px; background transparent; text DopplerRepro 18/25.2 400, #f1f0ec `color.neutral.warmWhite`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1); placeholder #f1f0ec `color.neutral.warmWhite` |
| focused, filled | border 1px solid #b997ff `color.brand.lightPurple`; outline 2px solid transparent, offset 2px |

![Text field default](components/crops/demo-field-default.png) ![Text field focused](components/crops/demo-field-focused.png) ![Text field filled](components/crops/demo-field-filled.png)

#### Email field
The company-email input; focused only, never filled or submitted. Read as `demo-email` on the demo request page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 564.61 x 43.2; padding 8px 16px; border 1px solid #8b877d `color.neutral.aluminum`; radius 16px; background transparent; text DopplerRepro 18/25.2 400, #f1f0ec `color.neutral.warmWhite`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1); placeholder #f1f0ec `color.neutral.warmWhite` |
| focused | border 1px solid #b997ff `color.brand.lightPurple`; outline 2px solid transparent, offset 2px |

![Email field default](components/crops/demo-email-default.png) ![Email field focused](components/crops/demo-email-focused.png)

#### Select
The Company-Size select; focused, never opened (a native list would paint). Read as `demo-select` on the demo request page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 276.3 x 43.2; padding 8px 16px; border 1px solid #8b877d `color.neutral.aluminum`; radius 16px; background transparent; text DopplerRepro 18/25.2 400, #f1f0ec `color.neutral.warmWhite`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| focused | border 1px solid #b997ff `color.brand.lightPurple`; outline 2px solid transparent, offset 2px |

![Select default](components/crops/demo-select-default.png) ![Select focused](components/crops/demo-select-focused.png)

#### Submit button
The Choose-a-Time submit; measured, never pressed (a press would submit). Read as `demo-submit` on the demo request page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 146.02 x 43; padding 14px 16px; radius 12px; background #00f575 `color.brand.green`; text DopplerRepro 15/15 700, #1c1624 `color.warm.black`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #00bf5b `color.brand.greenDark` |

![Submit button default](components/crops/demo-submit-default.png) ![Submit button hover](components/crops/demo-submit-hover.png) ![Submit button focus-visible](components/crops/demo-submit-focus-visible.png) ![Submit button pressed](components/crops/demo-submit-pressed.png)

#### Checklist row
A green-check benefit row beside the form. Read as `check-item` on the demo request page.

**Values (default).** size 563.39 x 61.19; background transparent; text Inter 18/30.6 400, #d0c9c4 `color.neutral.silver`.

![Checklist row default](components/crops/check-item-default.png)

### Integrations

The integrations directory: search field, category filter chips and the tile grid.

#### Integrations title
The integrations display heading. Read as `integrations-h1` on the integrations page.

**Values (default).** size 981.7 x 201.59; background transparent; text DopplerRepro 96/100.8 450, transparent; layers span.inline.bg-clip-text 916.8x130.0 image.

Child layers that carry the look: span 916.8x130 image linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%).

![Integrations title default](components/crops/integrations-h1-default.png)

#### Search field
The integrations search input; sample text was typed and deleted, nothing sent. Read as `search-field` on the integrations page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 300 x 46.8; padding 14px 20px 14px 40px; border 1px solid #f1f0ec `color.neutral.warmWhite`; radius 12px; background transparent; text DopplerRepro 14/16.8 500, #f1f0ec `color.neutral.warmWhite`; placeholder #f1f0ec `color.neutral.warmWhite` |
| focused, filled | outline 2px solid transparent, offset 2px |

![Search field default](components/crops/search-field-default.png) ![Search field focused](components/crops/search-field-focused.png) ![Search field filled](components/crops/search-field-filled.png)

#### Filter chip
An integration-category filter button; measured, never toggled (a toggle would filter the grid). Read as `filter-chip` on the integrations page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106.88 x 22; background transparent; text DopplerRepro 10/10 700, #f1f0ec `color.neutral.warmWhite`; icon 17.36 x 22, #f1f0ec `color.neutral.warmWhite`; layers span.ease.z-1 71.0x22.0 rgb(45, 39, 52) |
| hover | layers span.ease.z-1 71.0x22.0 rgb(185, 151, 255) |
| focus-visible | outline 1px auto #005fcc, offset 0px; layers button.group.relative 106.9x22.0 1px auto rgb(0, 95, 204) offset 0px; span.ease.z-1 71.0x22.0 rgb(45, 39, 52) |
| pressed | layers span.ease.z-1 71.0x22.0 rgb(185, 151, 255) |

Child layers that carry the look: span 71x22 background #2d2734 `color.warm.raised`.

![Filter chip default](components/crops/filter-chip-default.png) ![Filter chip hover](components/crops/filter-chip-hover.png) ![Filter chip focus-visible](components/crops/filter-chip-focus-visible.png) ![Filter chip pressed](components/crops/filter-chip-pressed.png)

#### Integration card
An integration tile (a provider name and glyph) in the grid; never followed. Read as `integration-card` on the integrations page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 289 x 181.2; padding 32px; radius 20px; background rgba(242, 241, 237, 0.04) `color.alpha.w4`; text DopplerRepro 18/25.2 400, #f1f0ec `color.neutral.warmWhite`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |

![Integration card default](components/crops/integration-card-default.png) ![Integration card hover](components/crops/integration-card-hover.png)

#### Request link
The Request-Integration action; measured, never followed. Read as `request-integration` on the integrations page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 207.75 x 44.05; padding 14px 16px; radius 12px; background #00f575 `color.brand.green`; text DopplerRepro 15/15 700, #1c1624 `color.warm.black`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 12, #1c1624 `color.warm.black` |
| hover | background #00bf5b `color.brand.greenDark` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #00bf5b `color.brand.greenDark` |

![Request link default](components/crops/request-integration-default.png) ![Request link hover](components/crops/request-integration-hover.png) ![Request link focus-visible](components/crops/request-integration-focus-visible.png) ![Request link pressed](components/crops/request-integration-pressed.png)

### Customers

The customers page: industry filter chips and case-study cards.

#### Customers title
The "Doppler effect" customers heading. Read as `customers-h1` on the customers page.

**Values (default).** size 825.42 x 100.8; background transparent; text DopplerRepro 96/100.8 450, #f1f0ec `color.neutral.warmWhite`.

![Customers title default](components/crops/customers-h1-default.png)

#### Industry chip
A customer-industry filter chip; measured, never toggled. Read as `industry-chip` on the customers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 58.14 x 37.2; padding 6px 20px; background transparent; text DopplerRepro 18/25.2 500, #00f575 `color.brand.green`; icon 20 x 20, #f1f0ec `color.neutral.warmWhite`; layers div.absolute.inset-0 58.1x37.2 rgb(45, 39, 52) T:1px solid rgba(255, 255, 255, 0.08) / R:1px solid rgba(255, 255, 255, 0.08) / L:1px solid rgba(255, 255, 255, 0.08) 20px 20px 0px 0px |
| focus-visible | outline 1px auto #005fcc, offset 0px; layers button.relative.snap-start 58.1x37.2 1px auto rgb(0, 95, 204) offset 0px; div.absolute.inset-0 58.1x37.2 rgb(45, 39, 52) T:1px solid rgba(255, 255, 255, 0.08) / R:1px solid rgba(255, 255, 255, 0.08) / L:1px solid rgba(255, 255, 255, 0.08) 20px 20px 0px 0px |

Child layers that carry the look: div 58.1x37.2 background #2d2734 `color.warm.raised` border 1px solid rgba(255, 255, 255, 0.08) `color.alpha.glow` radius 20px 20px 0px 0px.

![Industry chip default](components/crops/industry-chip-default.png) ![Industry chip hover](components/crops/industry-chip-hover.png) ![Industry chip focus-visible](components/crops/industry-chip-focus-visible.png) ![Industry chip pressed](components/crops/industry-chip-pressed.png)

#### Case-study card
A customer case-study card; never followed. Read as `case-card` on the customers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1224 x 590.16; border 1px solid rgba(255, 255, 255, 0.08) `color.alpha.glow`; radius 20px; background #2d2734 `color.warm.raised`; text DopplerRepro 24/33.6 450, #f1f0ec `color.neutral.warmWhite`; icon 16 x 16, #cccccc |

![Case-study card default](components/crops/case-card-default.png) ![Case-study card hover](components/crops/case-card-hover.png)

### Blog

The blog index: category chips (selected ALL at rest), post cards, Read-More links and round pagination.

#### Blog title
The blog index heading. Read as `blog-h1` on the blog page.

**Values (default).** size 800 x 302.39; background transparent; text DopplerRepro 96/100.8 450, #f1f0ec `color.neutral.warmWhite`.

![Blog title default](components/crops/blog-h1-default.png)

#### Category chip
A blog-category filter chip; measured, never toggled. Labels are sentence-case in the DOM, painted uppercase by text-transform. Read as `cat-chip` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 98.77 x 22; background transparent; text DopplerRepro 10/10 700, #f1f0ec `color.neutral.warmWhite`; icon 17.36 x 22, #f1f0ec `color.neutral.warmWhite`; layers span.ease.z-1 62.9x22.0 rgb(45, 39, 52) |
| hover | layers span.ease.z-1 62.9x22.0 rgb(185, 151, 255) |
| focus-visible | outline 1px auto #005fcc, offset 0px; layers button.group.relative 98.8x22.0 1px auto rgb(0, 95, 204) offset 0px; span.ease.z-1 62.9x22.0 rgb(45, 39, 52) |
| pressed | layers span.ease.z-1 62.9x22.0 rgb(185, 151, 255) |

Child layers that carry the look: span 62.9x22 background #2d2734 `color.warm.raised`.

![Category chip default](components/crops/cat-chip-default.png) ![Category chip hover](components/crops/cat-chip-hover.png) ![Category chip focus-visible](components/crops/cat-chip-focus-visible.png) ![Category chip pressed](components/crops/cat-chip-pressed.png)

#### Category chip, active
The ALL filter chip, selected at rest (no toggle needed for the selected state). Read as `cat-chip-active` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 58.47 x 22; background transparent; text DopplerRepro 10/10 700, #1c1624 `color.warm.black`; icon 17.36 x 22, #f1f0ec `color.neutral.warmWhite`; layers span.ease.z-1 22.6x22.0 rgb(185, 151, 255) |
| focus-visible | outline 1px auto #005fcc, offset 0px; layers button.group.relative 58.5x22.0 1px auto rgb(0, 95, 204) offset 0px; span.ease.z-1 22.6x22.0 rgb(185, 151, 255) |

Child layers that carry the look: span 22.6x22 background #b997ff `color.brand.lightPurple`.

![Category chip, active default](components/crops/cat-chip-active-default.png) ![Category chip, active hover](components/crops/cat-chip-active-hover.png) ![Category chip, active focus-visible](components/crops/cat-chip-active-focus-visible.png) ![Category chip, active pressed](components/crops/cat-chip-active-pressed.png)

#### Post card
A blog post card in the index grid; never followed. Read as `post-card` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 396 x 570; radius 20px; background rgba(242, 241, 237, 0.04) `color.alpha.w4`; text DopplerRepro 10/10 700, #f1f0ec `color.neutral.warmWhite`; icon 17.36 x 22, #f1f0ec `color.neutral.warmWhite`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 0 |
| hover | layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 0.994298 |

![Post card default](components/crops/post-card-default.png) ![Post card hover](components/crops/post-card-hover.png)

#### Pagination button
A numbered pagination control; measured, never followed. Read as `page-number` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 30 x 30; radius 9999px; background transparent; text DopplerRepro 16/24 400, #f1f0ec `color.neutral.warmWhite` |
| hover | background rgba(242, 241, 237, 0.04) `color.alpha.w4`; text DopplerRepro 16/24 400, #00bf5b `color.brand.greenDark` |
| focus-visible | outline 1px auto #005fcc, offset 0px; layers button.z-2.flex 30.0x30.0 1px auto rgb(0, 95, 204) offset 0px 9999px |
| pressed | background rgba(242, 241, 237, 0.04) `color.alpha.w4`; text DopplerRepro 16/24 400, #00bf5b `color.brand.greenDark` |

![Pagination button default](components/crops/page-number-default.png) ![Pagination button hover](components/crops/page-number-hover.png) ![Pagination button focus-visible](components/crops/page-number-focus-visible.png) ![Pagination button pressed](components/crops/page-number-pressed.png)

#### Read-More link
The Read-More card link under each post; measured never followed. Read as `read-more` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106.44 x 15.25; background transparent; text DopplerRepro 15/15 700, #d0c9c4 `color.neutral.silver`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 12, #d0c9c4 `color.neutral.silver`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite`; icon 14 x 12, #f1f0ec `color.neutral.warmWhite` |
| focus-visible | outline 1px auto #005fcc, offset 1px; text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite`; icon 14 x 12, #f1f0ec `color.neutral.warmWhite`; layers ::after rgba(0, 0, 0, 0) 0px none 1; a.card-link.static 106.4x15.3 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite`; icon 14 x 12, #f1f0ec `color.neutral.warmWhite` |

![Read-More link default](components/crops/read-more-default.png) ![Read-More link hover](components/crops/read-more-hover.png) ![Read-More link focus-visible](components/crops/read-more-focus-visible.png) ![Read-More link pressed](components/crops/read-more-pressed.png)

### Agents

The 'Run AI coding agents with Doppler' landing: the Pick-Your-Tool scroll link, interactive cards and the only real code element on the surface — the orange inline span.text-code chip.

#### Agents title
The "Run AI coding agents with Doppler" heading. Read as `agents-h1` on the agents page.

**Values (default).** size 563.39 x 115.19; background transparent; text DopplerRepro 48/57.6 450, #f1f0ec `color.neutral.warmWhite`; layers span.inline.bg-clip-text 179.3x71.0 image.

Child layers that carry the look: span 179.3x71 image linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%).

![Agents title default](components/crops/agents-h1-default.png)

#### Agents CTA
The "Pick Your Tool" hero call-to-action on the agents landing (an in-page scroll link); measured never followed. Read as `agents-cta` on the agents page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 161.2 x 44.05; padding 14px 16px; radius 12px; background #00f575 `color.brand.green`; text DopplerRepro 15/15 700, #1c1624 `color.warm.black`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 12, #1c1624 `color.warm.black` |
| hover | background #00bf5b `color.brand.greenDark` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #00bf5b `color.brand.greenDark` |

![Agents CTA default](components/crops/agents-cta-default.png) ![Agents CTA hover](components/crops/agents-cta-hover.png) ![Agents CTA focus-visible](components/crops/agents-cta-focus-visible.png) ![Agents CTA pressed](components/crops/agents-cta-pressed.png)

#### Agents card
A "Why Doppler for agents" / "Pick your tool" .interactive-card tile. Read as `agents-card` on the agents page.

**Values (default).** size 396 x 168.59; radius 20px; background rgba(242, 241, 237, 0.04) `color.alpha.w4`; text DopplerRepro 24/33.6 700, #f1f0ec `color.neutral.warmWhite`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Agents card default](components/crops/agents-card-default.png)

#### Inline code chip
An inline span.text-code ("doppler run") painted as a rounded black4 mono chip; the only real code element on the public pages — CLI samples elsewhere are baked into mock imagery. Read as `code-chip` on the agents page.

**Values (default).** size 56.97 x 29.59; padding 2px 8px; radius 6px; background rgba(242, 241, 237, 0.04) `color.alpha.w4`; text DopplerReproMono 16/25.6 400, #f55c15 `color.brand.orange`.

![Inline code chip default](components/crops/code-chip-default.png)

### Footer

The marketing footer: a warm-black sheet with 20px top corners, link columns, the bordered 'Doppler' wordmark tile and the Cookie Preferences button.

#### Footer
The marketing footer: link columns, legal, social icons and the Cookie Preferences button. Read as `footer` on the home page.

**Values (default).** size 1400 x 718.38; padding 32px; radius 20px; background #1c1624 `color.warm.black`; text DopplerRepro 12/12 400, #f1f0ec `color.neutral.warmWhite`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 200.98 x 40; padding 8px 10px; border 2px solid rgba(255, 255, 255, 0.08) `color.alpha.glow`; radius 20px; background rgba(242, 241, 237, 0.04) `color.alpha.w4`; text DopplerRepro 12/12 400, #f1f0ec `color.neutral.warmWhite`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(242, 241, 237, 0.08) `color.alpha.w8` |
| focus-visible | background rgba(242, 241, 237, 0.08) `color.alpha.w8`; outline 1px auto #005fcc, offset 1px |
| pressed | background rgba(242, 241, 237, 0.08) `color.alpha.w8` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Cookie button
The footer Cookie-Preferences button; measured, never pressed (it would open the consent panel). Read as `cookie-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 307.3 x 15; background transparent; text DopplerRepro 15/15 700, #d0c9c4 `color.neutral.silver`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite` |
| focus-visible | outline 1px auto #005fcc, offset 0px; layers button.inline-flex.items-center 307.3x15.0 1px auto rgb(0, 95, 204) offset 0px |
| pressed | text DopplerRepro 15/15 700, #f1f0ec `color.neutral.warmWhite` |

![Cookie button default](components/crops/cookie-button-default.png) ![Cookie button hover](components/crops/cookie-button-hover.png) ![Cookie button focus-visible](components/crops/cookie-button-focus-visible.png) ![Cookie button pressed](components/crops/cookie-button-pressed.png)

### Mobile (390 wide)

The same dark surface at phone width: the 72px header, the fixed full-height menu sheet and the stacked hero.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 72; padding 16px; border R: 1px solid #55505b `color.warm.glowStrokeLight`; B: 1px solid #55505b `color.warm.glowStrokeLight`; L: 1px solid #55505b `color.warm.glowStrokeLight`; radius 0px 0px 16px 16px; background #1c1624 `color.warm.black`; text DopplerRepro 16/24 400, #f1f0ec `color.neutral.warmWhite`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The header hamburger toggle. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 24 x 24; background transparent; text DopplerRepro 16/24 400, #f1f0ec `color.neutral.warmWhite`; layers div.transition-transform.duration-[350ms] 18.0x2.0 rgb(241, 240, 236); div.transition-transform.duration-[350ms] 18.0x2.0 rgb(241, 240, 236); div.transition-transform.duration-[350ms] 18.0x2.0 rgb(241, 240, 236).

Child layers that carry the look: div 18x2 background #f1f0ec `color.neutral.warmWhite`; div 18x2 background #f1f0ec `color.neutral.warmWhite`; div 18x2 background #f1f0ec `color.neutral.warmWhite`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The header menu panel opened by its own toggle. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 789; padding 30px 16px; border R: 1px solid #55505b `color.warm.glowStrokeLight`; B: 1px solid #55505b `color.warm.glowStrokeLight`; L: 1px solid #55505b `color.warm.glowStrokeLight`; background #1c1624 `color.warm.black`; text DopplerRepro 24/33.6 700, #f1f0ec `color.neutral.warmWhite`; icon 16 x 10.28, #f1f0ec `color.neutral.warmWhite`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
An item inside the opened header menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 356 x 50.59; padding 8px 0px; border B: 1px solid rgba(255, 255, 255, 0.08) `color.alpha.glow`; background transparent; text DopplerRepro 24/33.6 700, #f1f0ec `color.neutral.warmWhite`; layers a.flex.items-center 356.0x50.6 B:1px solid rgba(255, 255, 255, 0.08) |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.flex.items-center 356.0x50.6 B:1px solid rgba(255, 255, 255, 0.08) 1px auto rgb(0, 95, 204) offset 1px |

Child layers that carry the look: a 356x50.6 border 1px solid rgba(255, 255, 255, 0.08) `color.alpha.glow`.

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 228.64 x 108; background transparent; text DopplerRepro 36/36 450, #f1f0ec `color.neutral.warmWhite`; layers span.inline.bg-clip-text 211.2x56.0 image.

Child layers that carry the look: span 211.2x56 image linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%).

![Mobile headline default](components/crops/m-hero-default.png)

#### Mobile CTA
The hero Start-for-Free button at phone width; measured never followed. Read as `m-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 156.31 x 36.05; padding 10px 16px; radius 12px; background #00f575 `color.brand.green`; text DopplerRepro 15/15 700, #1c1624 `color.warm.black`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 12, #1c1624 `color.warm.black` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #00bf5b `color.brand.greenDark` |

![Mobile CTA default](components/crops/m-cta-default.png) ![Mobile CTA hover](components/crops/m-cta-hover.png) ![Mobile CTA focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile CTA pressed](components/crops/m-cta-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Doppler asterisk wordmark, the menu-link glyphs, the integration logos and the footer badges) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Doppler's product — the secrets dashboard, projects, configs, service tokens, logs, integrations management and billing — lives behind sign-in on dashboard.doppler.com and was never reached. /demo carries a real request form: its fields were focused and sample-filled then deleted, but the Choose-a-Time submit was never pressed, so no scheduling or booking surface was captured. The dashboard mock-ups in the hero and product screenshots are marketing imagery: the 'Take a self-guided tour' affordance is painted inside the image, not a DOM control.

### Pages

- **The workspace.** Every post-login surface (dashboard, project/config views, token management, audit logs) needs an account and was never reached; Start for Free and Sign In point off-site to dashboard.doppler.com/register and /login and were measured, never followed.
- **The demo flow.** /demo's form was never submitted; the scheduling step behind Choose a Time is uncaptured.
- **Long-tail pages.** The captured set covers home, /platform/secrets-manager, /pricing, /demo, /agents, /integrations, /customers, /blog and /about; the site's other public routes (platform sub-pages, use-case pages, case studies, comparisons, legal) share the same components and were not screenshotted individually.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **Selected chips** are captured at rest (the blog's ALL chip) — toggling a chip only filters the grid.
- **The mega-menu's pressed state** is measured with the panel held open; a real press would navigate.

### Themes

doppler.com's public surface paints one dark theme (warm-black #1c1624); the stylesheet declares no light variant on the captured routes and the probe resolved only `dark`. The tokens.json export therefore holds core + dark only.

### Fonts

- **Doppler Repro** (all headings, nav, buttons and body — a variable face that also paints the 450 display weight), **Doppler Repro Mono** (inline code chips, CLI samples) and **Inter** (long-form copy such as the demo checklist) are the served faces, all self-hosted under /_next/static/media; the style guide falls back to system sans.

### Screenshots

- Product illustrations, dashboard mock-ups, the Doppler wordmark and customer logos in the screenshots are the product's published content. The CLI/terminal samples visible in several shots are baked into that imagery — the only real code element measured is the inline `span.text-code` chip on /agents.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The mobile full pages were taller than the capture bound: mobile-home-dark-full is stitched from two chunks (14,000 + 2,104 px) and mobile-pricing-dark-full from three (14,000 + 14,000 + 1,712 px) — the stitch boundaries are a capture artifact, not a page feature.

### Content left out

- Marketing copy, blog posts, case studies and integration descriptions are the product's content; only frames and components were measured.
