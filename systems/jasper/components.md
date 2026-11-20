# Jasper components

The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from www.jasper.ai on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or purchased.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (38 components, 88 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (88 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home. Red wordmark, navy nav, light-blue hero, product sections, footer. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Platform overview. | `/platform` | [default](screenshots/platform-light-default.png), [full](screenshots/platform-light-full.png) |
| Agents library. | `/agents` | [default](screenshots/agents-light-default.png), [full](screenshots/agents-light-full.png) |
| Pricing comparison chart. | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Public brand page and logo downloads. | `/brand` | [default](screenshots/brand-light-default.png), [full](screenshots/brand-light-full.png) |
| Blog index. | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Company page. | `/company` | [default](screenshots/company-light-default.png), [full](screenshots/company-light-full.png) |
| Legal index. | `/legal` | [default](screenshots/legal-light-default.png), [full](screenshots/legal-light-full.png) |
| Get a Demo form, at rest. Nothing submitted. | `/demo` | [default](screenshots/demo-light-default.png) |
| app.jasper.ai login card, at rest. Nothing submitted. | `https://app.jasper.ai/auth/login` | [default](screenshots/signin-light-default.png) |
| Home at 390, including the menu toggle state. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing at 390. | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Login card at 390. | `https://app.jasper.ai/auth/login` | [default](screenshots/mobile-signin-light-default.png) |

### Overlays and transient states

Consent overlays (`#cookieBanner`, `#transcend-consent-manager`) and the Qualified chat host were hidden and never clicked. The Platform mega-menu was opened by hover. The demo form and the login card were left at rest.

## Entries

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 16 components were given a real keyboard focus. 13 draw a ring: `nav-link` (2px solid #00063d `swatch.blue-800`, offset 3px), `nav-login` (2px solid #00063d `swatch.blue-800`, offset 3px), `nav-cta` (2px solid #00063d `swatch.blue-800`, offset 3px), `nav-secondary` (2px solid #00063d `swatch.blue-800`, offset 3px), `menu-link` (2px solid #00063d `swatch.blue-800`, offset 3px), `hero-cta` (2px solid #00063d `swatch.blue-800`, offset 3px), `hero-secondary` (2px solid #00063d `swatch.blue-800`, offset 3px), `platform-cta` (2px solid #00063d `swatch.blue-800`, offset 3px), `price-cta` (2px solid #00063d `swatch.blue-800`, offset 3px), `brand-download` (2px solid #00063d `swatch.blue-800`, offset 3px), `demo-submit` (1px auto #0462cd, offset 0px), `footer-link` (2px solid #00063d `swatch.blue-800`, offset 3px), `m-nav-item` (2px solid #00063d `swatch.blue-800`, offset 3px). The other 3 draw none: `login-submit`, `login-google`, `login-signup`.
Focus could not be captured on 1: keyboard focus never reached them (or they took focus without matching :focus-visible), so their focus look is unknown, not absent: `nav-item`.

**Pressed.** Pressed was forced with DevTools `:active:hover` on the measured controls. Read the state row for the colour change. Jasper's primary button moves from flame `#fa4028` to `#801a10` on hover.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | login-google, login-submit |
| 0.2s | `ease` | background-color, box-shadow, transform | hero-cta, hero-secondary, nav-secondary, price-cta |
| 0.4s | `ease` | all | demo-submit |

**Layout.** Desktop captures are 1440 x 900. Phone captures are 390 CSS px at 2x. Content width on the home hero is 840px inside a 1320px section.

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Card](#card) | 1320 x 413.56 | 1px solid #00063d `swatch.blue-800` | - | #ffffff `swatch.light-100` | none | 0 |
| [Demo form](#demo-form) | 547.33 x 393.92 | 1px solid rgba(0, 0, 0, 0.5) | - | #ffffff `swatch.light-100` | none | 0 |
| [Price card](#price-card) | 328 x 119.69 | 1px solid #e0e0e1 `swatch.dark-200` | - | - | none | 16px 0px |
| [Nav dropdown](#nav-dropdown) | 1320 x 561.8 | - | - | #ffffff `swatch.light-100` | none | 24px |
| [Footer](#footer) | 1440 x 1189.5 | - | - | #00063d `swatch.blue-800` | none | 0 |

## Components

### Shell and navigation

The sticky marketing nav: a red wordmark, text menu items, Log in, Free Trial and a navy Get a Demo button.

#### Header
The sticky marketing nav: wordmark, Platform, Solutions, Resources, Company, Pricing, Log in, Free Trial and Get a Demo. Read as `header` on the Home page.

**Values (default).** size 1440 x 80; padding 16px 20px; background #ffffff `swatch.light-100`; text ABC ROM 16/22.4 450, #00063d `swatch.blue-800`; icon 98.72 x 37.02, #fa4028 `swatch.flame-600`.

![Header default](components/crops/header-default.png)

#### Logo
The Jasper wordmark link. Read as `logo` on the Home page.

**Values (default).** size 98.72 x 37.02; background transparent; text ABC ROM 16/22.4 450, #fa4028 `swatch.flame-600`; icon 98.72 x 37.02, #fa4028 `swatch.flame-600`.

![Logo default](components/crops/logo-default.png)

#### Nav item
A header menu item (Platform). Hover opens its dropdown. Measured, never followed. Read as `nav-item` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 85.69 x 28.17; padding 8px 12px; background transparent; text ABC ROM 16/22.4 450, #00063d `swatch.blue-800` |

Child layers that carry the look: div 9.9x28.2 background #ceebff `swatch.blue-300`; div 65.9x28.2 background #ceebff `swatch.blue-300`; div 9.9x28.2 background #ceebff `swatch.blue-300`.

![Nav item default](components/crops/nav-item-default.png) ![Nav item hover](components/crops/nav-item-hover.png) ![Nav item pressed](components/crops/nav-item-pressed.png)

#### Nav link
The Pricing header link. Read as `nav-link` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 74.59 x 28.17; background transparent; text ABC ROM 16/22.4 450, #00063d `swatch.blue-800` |
| focus-visible | outline 2px solid #00063d `swatch.blue-800`, offset 3px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log in link
The Log In header action. Measured, never followed. It opens app.jasper.ai. Read as `nav-login` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 43.97 x 28.17; padding 8px 0px; background transparent; text ABC ROM 16/22.4 450, #00063d `swatch.blue-800` |
| focus-visible | outline 2px solid #00063d `swatch.blue-800`, offset 3px |

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Nav CTA
The Free Trial header button. Measured, never followed. Read as `nav-cta` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 65.48 x 28.17; padding 8px 0px; background transparent; text ABC ROM 16/22.4 450, #00063d `swatch.blue-800` |
| focus-visible | outline 2px solid #00063d `swatch.blue-800`, offset 3px |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Nav secondary
The Get a Demo header link. Measured, never followed. Read as `nav-secondary` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 130.42 x 48.19; padding 12px 18px 11px 18px; background #00063d `swatch.blue-800`; text ABC ROM 18/25.2 500, #ffffff `swatch.light-100`; transition transform 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease |
| hover | shadow #0190ff 4px 4px 0px 0px; transform translate(-4px, -4px) |
| focus-visible | outline 2px solid #00063d `swatch.blue-800`, offset 3px |
| pressed | shadow #0190ff 4px 4px 0px 0px; transform translate(-4px, -4px) |

![Nav secondary default](components/crops/nav-secondary-default.png) ![Nav secondary hover](components/crops/nav-secondary-hover.png) ![Nav secondary focus-visible](components/crops/nav-secondary-focus-visible.png) ![Nav secondary pressed](components/crops/nav-secondary-pressed.png)

#### Nav dropdown
The Platform mega-menu panel, opened by hovering its item. The full-viewport .nav_dropdown_wrap is the scrim, not the panel. Read as `nav-dropdown` on the Home page.

**Values (default).** size 1320 x 561.8; padding 24px; background #ffffff `swatch.light-100`; text ABC ROM 12/16.8 500, #ffffff `swatch.light-100`.

![Nav dropdown default](components/crops/nav-dropdown-default.png)

#### Menu link
A link inside the opened Platform dropdown. Read as `menu-link` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 244.33 x 12.17; background transparent; text ABC ROM 16/22.4 450, #00063d `swatch.blue-800` |
| focus-visible, pressed | outline 2px solid #00063d `swatch.blue-800`, offset 3px |

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link focus-visible](components/crops/menu-link-focus-visible.png) ![Menu link pressed](components/crops/menu-link-pressed.png)

### Home hero

The light-blue hero: a Feature display headline, a red New chip, and two actions (navy Get a Demo, outlined Start Free Trial).

#### Hero headline
The display headline, set in Feature. Read as `hero-title` on the Home page.

**Values (default).** size 840 x 193.59; background transparent; text Feature 88/96.8 400, #00063d `swatch.blue-800`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero CTA
A hero action. Measured, never followed. Read as `hero-cta` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 130.42 x 48.19; padding 12px 18px 11px 18px; background #00063d `swatch.blue-800`; text ABC ROM 18/25.2 500, #ffffff `swatch.light-100`; transition transform 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease |
| hover | shadow #0190ff 4px 4px 0px 0px; transform translate(-4px, -4px) |
| focus-visible | outline 2px solid #00063d `swatch.blue-800`, offset 3px |
| pressed | shadow #0190ff 4px 4px 0px 0px; transform translate(-4px, -4px) |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero secondary
The Explore the Platform link. Measured, never followed. Read as `hero-secondary` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 200.52 x 48.19; padding 12px 18px 11px 18px; background #00063d `swatch.blue-800`; text ABC ROM 18/25.2 500, #ffffff `swatch.light-100`; transition transform 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease |
| hover | shadow #0190ff 4px 4px 0px 0px; transform translate(-4px, -4px) |
| focus-visible | outline 2px solid #00063d `swatch.blue-800`, offset 3px |
| pressed | shadow #0190ff 4px 4px 0px 0px; transform translate(-4px, -4px) |

![Hero secondary default](components/crops/hero-secondary-default.png) ![Hero secondary hover](components/crops/hero-secondary-hover.png) ![Hero secondary focus-visible](components/crops/hero-secondary-focus-visible.png) ![Hero secondary pressed](components/crops/hero-secondary-pressed.png)

### Home

Home sections below the hero: Feature headings and content cards.

#### Section heading
A Feature display heading in a home section. Read as `section-title` on the Home page.

**Values (default).** size 840 x 40; background transparent; text Feature 32/40 400, #00063d `swatch.blue-800`.

![Section heading default](components/crops/section-title-default.png)

#### Card
A content card on the home page. Read as `card` on the Home page.

**Values (default).** size 1320 x 413.56; background transparent; text Feature 32/40 400, #00063d `swatch.blue-800`.

Child layers that carry the look: a 318x413.6 background #ffffff `swatch.light-100` border 1px solid #00063d `swatch.blue-800`; a 318x413.6 background #ffffff `swatch.light-100` border 1px solid #00063d `swatch.blue-800`; a 318x413.6 background #ffffff `swatch.light-100` border 1px solid #00063d `swatch.blue-800`.

![Card default](components/crops/card-default.png)

#### Text link
An in-page text link. Measured, never followed. Read as `text-link` on the Home page.

Not on the page when it was captured.

#### Platform headline
The /platform display headline. Read as `platform-h1` on the Platform page.

**Values (default).** size 786.66 x 240; background transparent; text Feature 80/80 450, #00063d `swatch.blue-800`.

![Platform headline default](components/crops/platform-h1-default.png)

#### Platform CTA
A platform-page action. Measured, never followed. Read as `platform-cta` on the Platform page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 65.48 x 28.17; padding 8px 0px; background transparent; text ABC ROM 16/22.4 450, #00063d `swatch.blue-800` |
| focus-visible | outline 2px solid #00063d `swatch.blue-800`, offset 3px |

![Platform CTA default](components/crops/platform-cta-default.png) ![Platform CTA hover](components/crops/platform-cta-hover.png) ![Platform CTA focus-visible](components/crops/platform-cta-focus-visible.png) ![Platform CTA pressed](components/crops/platform-cta-pressed.png)

### Pricing

The pricing comparison chart: plan columns and their actions. Nothing was checked out.

#### Pricing title
The pricing page headline. Read as `pricing-h1` on the Pricing page.

**Values (default).** size 817.55 x 160; background transparent; text Feature 80/80 450, #00063d `swatch.blue-800`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Price card
A pricing tier card. Read as `price-card` on the Pricing page.

**Values (default).** size 328 x 119.69; padding 16px 0px; border R: 1px solid #e0e0e1 `swatch.dark-200`; L: 1px solid #e0e0e1 `swatch.dark-200`; background transparent; text Feature 24/26.4 450, #00063d `swatch.blue-800`.

Child layers that carry the look: div 328x119.7 border 1px solid #e0e0e1 `swatch.dark-200`; div 164.1x47.7 border 1px solid #00063d `swatch.blue-800`.

![Price card default](components/crops/price-card-default.png)

#### Price CTA
A pricing action. Measured, never followed. Read as `price-cta` on the Pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 130.42 x 48.19; padding 12px 18px 11px 18px; background #00063d `swatch.blue-800`; text ABC ROM 18/25.2 500, #ffffff `swatch.light-100`; transition transform 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease |
| hover | shadow #0190ff 4px 4px 0px 0px; transform translate(-4px, -4px) |
| focus-visible | outline 2px solid #00063d `swatch.blue-800`, offset 3px |
| pressed | shadow #0190ff 4px 4px 0px 0px; transform translate(-4px, -4px) |

![Price CTA default](components/crops/price-cta-default.png) ![Price CTA hover](components/crops/price-cta-hover.png) ![Price CTA focus-visible](components/crops/price-cta-focus-visible.png) ![Price CTA pressed](components/crops/price-cta-pressed.png)

#### FAQ item
An FAQ row. Toggled for its open state. Nothing is submitted. Read as `faq-item` on the Pricing page.

Not on the page when it was captured.

### Brand page

The public brand page, with logo downloads. Measured, never downloaded.

#### Brand title
The /brand page headline. Read as `brand-h1` on the Brand page.

**Values (default).** size 1021.94 x 80; background transparent; text Feature 80/80 450, #00063d `swatch.blue-800`.

![Brand title default](components/crops/brand-h1-default.png)

#### Brand download
A logo download link on /brand. Measured, never followed. Read as `brand-download` on the Brand page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 99.61 x 23.59; padding 4.8px 8px; border 1px solid #00063d `swatch.blue-800`; background #ffffff `swatch.light-100`; text ABC ROM Mono 12/12 450, #00063d `swatch.blue-800` |
| hover | border 1px solid #fa4028 `swatch.flame-600`; background #ffe8e2 `swatch.flame-300`; text ABC ROM Mono 12/12 450, #fa4028 `swatch.flame-600` |
| focus-visible | outline 2px solid #00063d `swatch.blue-800`, offset 3px |
| pressed | border 1px solid #fa4028 `swatch.flame-600`; background #ffe8e2 `swatch.flame-300`; text ABC ROM Mono 12/12 450, #fa4028 `swatch.flame-600` |

![Brand download default](components/crops/brand-download-default.png) ![Brand download hover](components/crops/brand-download-hover.png) ![Brand download focus-visible](components/crops/brand-download-focus-visible.png) ![Brand download pressed](components/crops/brand-download-pressed.png)

### Demo form boundary

The Get a Demo HubSpot form, measured at rest. Nothing was typed or submitted.

#### Demo form
The Get a Demo HubSpot form, measured at rest. Nothing was typed or submitted. Read as `demo-card` on the Demo page.

**Values (default).** size 547.33 x 393.92; background transparent; text ABC ROM 16/20 500, #00063d `swatch.blue-800`.

Child layers that carry the look: input 547.3x48 background #ffffff `swatch.light-100` border 1px solid rgba(0, 0, 0, 0.5); input 265.7x48 background #ffffff `swatch.light-100` border 1px solid rgba(0, 0, 0, 0.5); input 265.7x48 background #ffffff `swatch.light-100` border 1px solid rgba(0, 0, 0, 0.5).

![Demo form default](components/crops/demo-card-default.png)

#### Demo email field
The work-email field. Focused only. Nothing typed, nothing submitted. Read as `demo-field` on the Demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 547.33 x 48; padding 12.8px; border 1px solid rgba(0, 0, 0, 0.5); background #ffffff `swatch.light-100`; text ABC ROM 16/17.6 450, rgba(0, 0, 0, 0.65); placeholder #64748b |
| focused | border 1px solid #fa4028 `swatch.flame-600`; text ABC ROM 16/17.6 450, #00063d `swatch.blue-800` |

![Demo email field default](components/crops/demo-field-default.png) ![Demo email field focused](components/crops/demo-field-focused.png)

#### Demo submit
The form submit. Measured, never pressed. Read as `demo-submit` on the Demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 547.33 x 48; padding 8px; background #fa4028 `swatch.flame-600`; text ABC ROM 16/16 450, #ffffff `swatch.light-100`; transition all 0.4s ease; placeholder #ffffff `swatch.light-100` |
| hover | background #801a10 `swatch.flame-700` |
| focus-visible | outline 1px auto #0462cd, offset 0px |
| pressed | background #801a10 `swatch.flame-700` |

![Demo submit default](components/crops/demo-submit-default.png) ![Demo submit hover](components/crops/demo-submit-hover.png) ![Demo submit focus-visible](components/crops/demo-submit-focus-visible.png) ![Demo submit pressed](components/crops/demo-submit-pressed.png)

### App login boundary

The app.jasper.ai login column. The boundary before the product. Never filled, never submitted, no OAuth followed.

#### Login card
The app.jasper.ai login column. The boundary before the product. Never filled, never submitted, no OAuth followed. Read as `login-card` on the Login page.

Not on the page when it was captured.

#### Login email field
The email field on the login card. Focused only. Nothing typed. Read as `login-field` on the Login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 410 x 20; background transparent; text Inter 14/20 400, #1d2534; placeholder #818794 |

![Login email field default](components/crops/login-field-default.png) ![Login email field focused](components/crops/login-field-focused.png)

#### Continue with email
The email submit. Measured, never pressed. Read as `login-submit` on the Login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 432 x 32; padding 5px 12px; border 1px solid #0070ee; radius 6px; background #0070ee; text Inter 14/20 500, #ffffff `swatch.light-100`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #0056d4; background #2887f0 |
| focus-visible | shadow #cce2fc 0px 0px 0px 3px |
| pressed | border 1px solid #0056d4; background #2887f0 |

![Continue with email default](components/crops/login-submit-default.png) ![Continue with email hover](components/crops/login-submit-hover.png) ![Continue with email focus-visible](components/crops/login-submit-focus-visible.png) ![Continue with email pressed](components/crops/login-submit-pressed.png)

#### Continue with Google
The Google OAuth button. Measured, never followed. Read as `login-google` on the Login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 432 x 32; padding 5px 12px 5px 8px; border 1px solid #dee0e4; radius 6px; background #ffffff `swatch.light-100`; text Inter 14/20 500, #1d2534; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #1d2534 |
| hover | background #f3f4f6 |
| focus-visible | border 1px solid #0070ee; shadow #cce2fc 0px 0px 0px 3px |
| pressed | background #f3f4f6 |

![Continue with Google default](components/crops/login-google-default.png) ![Continue with Google hover](components/crops/login-google-hover.png) ![Continue with Google focus-visible](components/crops/login-google-focus-visible.png) ![Continue with Google pressed](components/crops/login-google-pressed.png)

#### Sign up link
The Sign up action on the login card. Measured, never followed. Read as `login-signup` on the Login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 50.03 x 20; background transparent; text Inter 14/20 400, #0070ee |
| hover, focus-visible, pressed | text Inter 14/20 400, #2887f0 |

![Sign up link default](components/crops/login-signup-default.png) ![Sign up link hover](components/crops/login-signup-hover.png) ![Sign up link focus-visible](components/crops/login-signup-focus-visible.png) ![Sign up link pressed](components/crops/login-signup-pressed.png)

### Footer

The site footer: link columns and legal.

#### Footer
The site footer: link columns and legal. Read as `footer` on the Home page.

**Values (default).** size 1440 x 1189.5; background #00063d `swatch.blue-800`; text Feature 24/26.4 450, #ffffff `swatch.light-100`; icon 12 x 12, #ffffff `swatch.light-100`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 126.73 x 24; background transparent; text Feature 24/26.4 450, #ffffff `swatch.light-100`; icon 12 x 12, #ffffff `swatch.light-100` |
| focus-visible | outline 2px solid #00063d `swatch.blue-800`, offset 3px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Mobile (390 wide)

The same marketing page at 390 x 844, with the menu toggle.

#### Mobile header
Read as `m-header` on the Mobile home page at 390 wide.

**Values (default).** size 390 x 80; background #ffffff `swatch.light-100`; text ABC ROM 16/22.4 450, #00063d `swatch.blue-800`; icon 98.72 x 37.02, #fa4028 `swatch.flame-600`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The mobile menu toggle. Read as `m-menu-button` on the Mobile home page at 390 wide.

**Values (default).** size 104 x 37.02; background transparent; text ABC ROM 16/22.4 450, #00063d `swatch.blue-800`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The mobile nav panel opened by its own toggle. Read as `m-menu-open` on the Mobile home page at 390 wide.

**Values (default).** size 350 x 40; padding 0px 0px 24px 0px; background #ffffff `swatch.light-100`; text Feature 28/30.8 450, #00063d `swatch.blue-800`; icon 12.8 x 8, #00063d `swatch.blue-800`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
An item inside the opened mobile menu. Read as `m-nav-item` on the Mobile home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 43.97 x 28.17; padding 8px 0px; background transparent; text ABC ROM 16/22.4 450, #00063d `swatch.blue-800` |
| focus-visible | outline 2px solid #00063d `swatch.blue-800`, offset 3px |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the Mobile home page at 390 wide.

**Values (default).** size 358 x 88; background transparent; text Feature 40/44 400, #00063d `swatch.blue-800`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted. The wordmark and the illustrated mega-menu art are Jasper's artwork and stay in the screenshots and crops. `icons/` is declared as a layout gap.

## Gaps

### Pages

- **Product app.** The canvas, agents runtime, Brand IQ editor and campaigns sit behind `https://app.jasper.ai/`. The login card at `https://app.jasper.ai/auth/login` was measured at rest. Google OAuth was not followed. Nothing was submitted.
- **Signup.** `https://app.jasper.ai/auth/signup` was not followed.
- **Demo form.** `https://www.jasper.ai/demo` was measured at rest and never submitted.
- **Help center.** `https://help.jasper.ai/` was not captured.
- **Phone menu.** At 390 the desktop `.nav_menu` is `display: none` and no hamburger mounts. The phone menu was not opened.

### States

- **Pressed** was forced with DevTools `:active:hover`, so a script that only runs on a real pointer-down is missing.
- **Disabled, loading and error** were not seen. Forms were not submitted.
- **text-link and faq-item** were not on the pages when measured. Pricing has no FAQ accordion.

### Themes

The marketing pages paint light. `.u-theme-dark` rebinds background to `#262627` and text to `#ffffff` for dark islands (the footer). There is no page-wide theme switch, so no dark page screenshot was taken. The dark set in [tokens.json](tokens.json) is that declared rebinding.

### Fonts

- **ABC ROM** is the UI face. **Feature** is the display face. **ABC ROM Mono** is the mono face. The files are commercial and are not in this package. Inter is also declared on the Webflow sheet and is not the marketing UI face.

### Screenshots

- Illustrations, customer logos and the wordmark are Jasper's content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs. Read exact colours from the tokens or the raw files.
