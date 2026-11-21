# Amie components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from amie.so on 2026-11-10, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (35 components, 87 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (89 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [features](screenshots/home-light-features.png), [full](screenshots/home-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [faq](screenshots/pricing-light-faq.png), [full](screenshots/pricing-light-full.png), [yearly](screenshots/pricing-light-yearly.png) |
| Changelog | `/changelog` | [default](screenshots/changelog-light-default.png), [full](screenshots/changelog-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Stories | `/stories` | [default](screenshots/stories-light-default.png), [full](screenshots/stories-light-full.png) |
| Calendar | `/calendar` | [default](screenshots/calendar-light-default.png), [full](screenshots/calendar-light-full.png) |
| Tools | `/tools` | [default](screenshots/tools-light-default.png), [full](screenshots/tools-light-full.png) |
| Templates | `/templates` | [default](screenshots/templates-light-default.png), [full](screenshots/templates-light-full.png) |
| Download | `/download` | [default](screenshots/download-light-default.png), [full](screenshots/download-light-full.png) |
| Contact | `/contact` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Features flyout | header, home | the nav button's own Radix toggle | [home-light-features](screenshots/home-light-features.png), [nav-flyout-open](#features-flyout-open) |
| Billing, yearly | pricing | the toggle's own press; plan cards re-render | [pricing-light-yearly](screenshots/pricing-light-yearly.png), [billing-yearly-on](#billing-toggle-yearly-on) |
| Pricing FAQ, open | pricing | the accordion's own toggle | [faq-open](#faq-accordion-open), [pricing-light-faq](screenshots/pricing-light-faq.png) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 18 components were given a real keyboard focus. 9 show a visible focus state: `nav-cta` (1px auto #005fcc `measured.focus-outline`, offset 1px), `changelog-pill` (1px auto #005fcc `measured.focus-outline`, offset 1px), `cta-primary` (1px auto #005fcc `measured.focus-outline`, offset 1px), `download-button` (visible change in boxShadow), `contact-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `footer-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `footer-social` (1px auto #005fcc `measured.focus-outline`, offset 1px), `footer-legal` (1px auto #005fcc `measured.focus-outline`, offset 1px), `m-cta` (1px auto #e59700, offset 1px). The other 9 show no change a keyboard user can see: `nav-flyout-button`, `nav-link`, `nav-login`, `cta-secondary`, `billing-monthly`, `billing-yearly`, `plan-select`, `plan-cta`, `faq-question`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): controls deepen their fill or dim rather than scale; the nav flyout and framework icons keep their hover scale. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, opacity, stroke, text-decoration-color | billing-monthly, billing-yearly, billing-yearly-on, contact-field, download-button, m-cta, m-nav-link, nav-cta and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 480 x 431 | - | 16px | #ffffff `color.white` | rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 1px 1px -0.5px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px | 0 |
| [FAQ accordion button](#faq-accordion-button) | 976 x 68 | - | - | transparent | none | 20px |
| [Contact field](#contact-field) | 554.67 x 54 | 1px solid #afafaf `color.gray.300` | 12px | #ffffff `color.white` | none | 12px 16px |

## Components

### Shell and navigation

The floating bar and the Radix Features flyout.

#### Header
The floating bar: logo, Features flyout, Pricing, Login, Get started. Read as `header` on the home page.

**Values (default).** size 1024 x 59; padding 0px 24px; background transparent; text Inter 14/14 500, #000000 `color.black`; icon 24 x 24, #000000 `color.black`.

Child layers that carry the look: button 78.2x32 radius 8px; a 66.7x32 radius 8px; a 57x32 radius 8px.

![Header default](components/crops/header-default.png)

#### Logo
Read as `logo` on the home page.

**Values (default).** size 24 x 24; background transparent; text Inter 16/28 400, #000000 `color.black`; icon 24 x 24, #000000 `color.black`.

![Logo default](components/crops/logo-default.png)

#### Nav flyout button
A Radix dropdown trigger; opens the Features panel. Read as `nav-flyout-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 78.16 x 32; padding 6px 10px; radius 8px; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/14 500, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(0, 0, 0, 0.05) |
| focus-visible | outline none |
| pressed | background rgba(0, 0, 0, 0.05) |

Child layers that carry the look: button 78.2x32 radius 8px.

![Nav flyout button default](components/crops/nav-flyout-button-default.png) ![Nav flyout button hover](components/crops/nav-flyout-button-hover.png) ![Nav flyout button focus-visible](components/crops/nav-flyout-button-focus-visible.png) ![Nav flyout button pressed](components/crops/nav-flyout-button-pressed.png)

#### Features flyout, open
The Features button after its own toggle; the crop is the opened panel. Read as `nav-flyout-open` on the home page.

**Values (opened).** size 78.16 x 32; padding 6px 10px; radius 8px; background rgba(0, 0, 0, 0.05); text Inter 14/14 500, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Features flyout, open opened](components/crops/nav-flyout-open-opened.png)

#### Nav link
Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 66.72 x 32; padding 6px 10px; radius 8px; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/14 500, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | background rgba(0, 0, 0, 0.05) |

Child layers that carry the look: a 66.7x32 radius 8px.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Login link
The secondary nav link. Measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 56.98 x 32; padding 6px 10px; radius 8px; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/14 500, #5c5c5c `color.gray.600`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | background rgba(0, 0, 0, 0.05) |

Child layers that carry the look: a 57x32 radius 8px.

![Login link default](components/crops/nav-login-default.png) ![Login link hover](components/crops/nav-login-hover.png) ![Login link focus-visible](components/crops/nav-login-focus-visible.png) ![Login link pressed](components/crops/nav-login-pressed.png)

#### Nav CTA
The small blue Get started. Measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106.63 x 32; padding 6px 16px; radius 8px; background #11a8ff `color.blue.500`; text Inter 14/20 500, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #218fcd `color.blue.600` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | background #218fcd `color.blue.600` |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

### Home

The hero pair and the what's-new pill.

#### Hero title
Read as `hero-title` on the home page.

Not on the page when it was captured.

#### Changelog pill
The "what's new" link under the hero. Read as `changelog-pill` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 391.95 x 15.83; radius 9999px; background transparent; text Inter 12/15.84 500, #5c5c5c `color.gray.600`; icon 12 x 12, #a0a0a0 `color.gray.350` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |

![Changelog pill default](components/crops/changelog-pill-default.png) ![Changelog pill hover](components/crops/changelog-pill-hover.png) ![Changelog pill focus-visible](components/crops/changelog-pill-focus-visible.png) ![Changelog pill pressed](components/crops/changelog-pill-pressed.png)

#### Primary CTA
The hero blue Get started. Measured, never followed. Read as `cta-primary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 140.23 x 49.59; padding 12px 28px; radius 12px; background #11a8ff `color.blue.500`; text Inter 16/25.6 600, #ffffff `color.white` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |

![Primary CTA default](components/crops/cta-primary-default.png) ![Primary CTA hover](components/crops/cta-primary-hover.png) ![Primary CTA focus-visible](components/crops/cta-primary-focus-visible.png) ![Primary CTA pressed](components/crops/cta-primary-pressed.png)

#### Secondary CTA
The ghost Download beside it. Measured, never pressed. Read as `cta-secondary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 155.94 x 49.59; padding 12px 28px; radius 12px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 1px 1px -0.5px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px; text Inter 16/25.6 600, #5c5c5c `color.gray.600`; icon 16 x 16, #a0a0a0 `color.gray.350` |

![Secondary CTA default](components/crops/cta-secondary-default.png) ![Secondary CTA hover](components/crops/cta-secondary-hover.png) ![Secondary CTA focus-visible](components/crops/cta-secondary-focus-visible.png) ![Secondary CTA pressed](components/crops/cta-secondary-pressed.png)

#### Section title
Read as `section-title` on the home page.

**Values (default).** size 260.67 x 28; background transparent; text Inter 20/28 600, #000000 `color.black`.

![Section title default](components/crops/section-title-default.png)

### Pricing

The billing toggle, plan cards, trial CTA and FAQ accordions.

#### Pricing title
Read as `pricing-title` on the pricing page.

**Values (default).** size 976 x 128; background transparent; text Inter 56/64 700, #171717 `color.gray.900`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Billing toggle, monthly
Read as `billing-monthly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 112.8 x 28; padding 0px 12px; background transparent; text Inter 16/28 500, #000000 `color.black`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | opacity 0.8 |

![Billing toggle, monthly default](components/crops/billing-monthly-default.png) ![Billing toggle, monthly hover](components/crops/billing-monthly-hover.png) ![Billing toggle, monthly focus-visible](components/crops/billing-monthly-focus-visible.png) ![Billing toggle, monthly pressed](components/crops/billing-monthly-pressed.png)

#### Billing toggle, yearly
Read as `billing-yearly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 98.19 x 28; padding 0px 12px; background transparent; text Inter 16/28 500, #000000 `color.black`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | opacity 0.8 |

![Billing toggle, yearly default](components/crops/billing-yearly-default.png) ![Billing toggle, yearly hover](components/crops/billing-yearly-hover.png) ![Billing toggle, yearly focus-visible](components/crops/billing-yearly-focus-visible.png) ![Billing toggle, yearly pressed](components/crops/billing-yearly-pressed.png)

#### Billing toggle, yearly on
The yearly side after its own toggle; plan prices flip and the trial button is re-rendered. Read as `billing-yearly-on` on the pricing page.

**Values (opened).** size 98.19 x 28; padding 0px 12px; background transparent; text Inter 16/28 500, #000000 `color.black`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.8.

![Billing toggle, yearly on opened](components/crops/billing-yearly-on-opened.png)

#### Select button
The white plan row action. Measured, never pressed. Read as `plan-select` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 253.11 x 32; padding 6px 0px; radius 8px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 1px 1px -0.5px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px; text Inter 14/20 500, #000000 `color.black` |
| hover, pressed | background #fafafa `color.background` |

![Select button default](components/crops/plan-select-default.png) ![Select button hover](components/crops/plan-select-hover.png) ![Select button focus-visible](components/crops/plan-select-focus-visible.png) ![Select button pressed](components/crops/plan-select-pressed.png)

#### Plan card
Read as `plan-card` on the pricing page.

**Values (default).** size 480 x 431; radius 16px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 1px 1px -0.5px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px; text Inter 20/28 500, #000000 `color.black`; icon 24 x 24, #fe6600 `color.orange.500`.

![Plan card default](components/crops/plan-card-default.png)

#### Trial button
"Start 7 day free trial": the black plan CTA. Measured, never pressed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 440 x 36; padding 8px 0px; radius 12px; background #000000 `color.black`; shadow rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 1px 1px -0.5px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px; text Inter 14/20 600, #ffffff `color.white` |

![Trial button default](components/crops/plan-cta-default.png) ![Trial button hover](components/crops/plan-cta-hover.png) ![Trial button focus-visible](components/crops/plan-cta-focus-visible.png) ![Trial button pressed](components/crops/plan-cta-pressed.png)

#### FAQ accordion button
Read as `faq-question` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 976 x 68; padding 20px; background transparent; text Inter 16/28 500, #000000 `color.black`; icon 16 x 16, #a0a0a0 `color.gray.350` |

![FAQ accordion button default](components/crops/faq-question-default.png) ![FAQ accordion button hover](components/crops/faq-question-hover.png) ![FAQ accordion button focus-visible](components/crops/faq-question-focus-visible.png) ![FAQ accordion button pressed](components/crops/faq-question-pressed.png)

#### FAQ accordion, open
The same item after its own toggle. Read as `faq-open` on the pricing page.

**Values (opened).** size 976 x 68; padding 20px; background transparent; text Inter 16/28 500, #000000 `color.black`; icon 16 x 16, #a0a0a0 `color.gray.350`.

![FAQ accordion, open opened](components/crops/faq-open-opened.png)

### Download

The app download action.

#### Download title
Read as `download-title` on the download page.

**Values (default).** size 245.16 x 28; background transparent; text Inter 32/28 700, #000000 `color.black`.

![Download title default](components/crops/download-title-default.png)

#### Download button
The app download action. Measured, never pressed. Read as `download-button` on the download page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 259.53 x 56; padding 8px 16px 8px 8px; radius 12px; background #2e2e2e `color.gray.800`; shadow rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px; text Inter 18/28 600, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #454545 `color.gray.700` |
| focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(147, 197, 253, 0.5) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px |
| pressed | background #454545 `color.gray.700` |

![Download button default](components/crops/download-button-default.png) ![Download button hover](components/crops/download-button-hover.png) ![Download button focus-visible](components/crops/download-button-focus-visible.png) ![Download button pressed](components/crops/download-button-pressed.png)

### Contact

The contact form fields.

#### Contact title
Read as `contact-title` on the contact page.

**Values (default).** size 944 x 54.41; background transparent; text Inter 40/54.4 700, #000000 `color.black`.

![Contact title default](components/crops/contact-title-default.png)

#### Contact link
Read as `contact-link` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 72.44 x 20; background transparent; text Inter 14/20 500, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |

![Contact link default](components/crops/contact-link-default.png) ![Contact link hover](components/crops/contact-link-hover.png) ![Contact link focus-visible](components/crops/contact-link-focus-visible.png) ![Contact link pressed](components/crops/contact-link-pressed.png)

#### Contact field
Focused only; nothing was typed. Read as `contact-field` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 554.67 x 54; padding 12px 16px; border 1px solid #afafaf `color.gray.300`; radius 12px; background #ffffff `color.white`; outline 2px solid transparent, offset 2px; text Inter 16/28 400, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #919191 `color.gray.400` |
| focused | border 1px solid #11a8ff `color.blue.500`; shadow #ffffff 0px 0px 0px 0px, #11a8ff 0px 0px 0px 2px |

![Contact field default](components/crops/contact-field-default.png) ![Contact field focused](components/crops/contact-field-focused.png)

### Footer

The link columns, socials and legal.

#### Footer
Read as `footer` on the home page.

**Values (default).** size 1440 x 577; padding 40px 0px; background transparent; text Inter 14/20 500, #000000 `color.black`.

Child layers that carry the look: div 976x469 border 1px solid rgba(0, 0, 0, 0.04) `shadow.wysiwyg.inner`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 154.2 x 20; background transparent; text Inter 14/20 500, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer social icon
Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 66.94 x 20; background transparent; text Inter 14/20 500, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |

![Footer social icon default](components/crops/footer-social-default.png) ![Footer social icon hover](components/crops/footer-social-hover.png) ![Footer social icon focus-visible](components/crops/footer-social-focus-visible.png) ![Footer social icon pressed](components/crops/footer-social-pressed.png)

#### Legal link
Read as `footer-legal` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 109.78 x 28; padding 4px 8px; background transparent; text Inter 14/20 500, #000000 `color.black`; opacity 0.4 |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |

![Legal link default](components/crops/footer-legal-default.png) ![Legal link hover](components/crops/footer-legal-hover.png) ![Legal link focus-visible](components/crops/footer-legal-focus-visible.png) ![Legal link pressed](components/crops/footer-legal-pressed.png)

### Mobile (390 wide)

The same surface at phone width.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 59; padding 0px 24px; background transparent; text Inter 14/14 500, #000000 `color.black`; icon 24 x 24, #000000 `color.black`.

Child layers that carry the look: button 0x0 radius 8px; a 66.7x32 radius 8px; a 106.6x32 background #11a8ff `color.blue.500` radius 8px.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the home page at 390 wide.

Not on the page when it was captured.

#### Mobile menu, open
The button after its own toggle; the open panel shows in the crop. Read as `m-menu-open` on the home page at 390 wide.

Not on the page when it was captured.

#### Mobile nav link
Read as `m-nav-link` on the home page at 390 wide.

**Values (default).** size 66.72 x 32; padding 6px 10px; radius 8px; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/14 500, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1).

Child layers that carry the look: a 66.7x32 radius 8px.

![Mobile nav link default](components/crops/m-nav-link-default.png)

#### Mobile CTA
Read as `m-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106.63 x 32; padding 6px 16px; radius 8px; background #11a8ff `color.blue.500`; text Inter 14/20 500, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #218fcd `color.blue.600` |
| focus-visible | outline 1px auto #e59700, offset 1px |
| pressed | background #218fcd `color.blue.600` |

![Mobile CTA default](components/crops/m-cta-default.png) ![Mobile CTA hover](components/crops/m-cta-hover.png) ![Mobile CTA focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile CTA pressed](components/crops/m-cta-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Amie's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The app behind login and the download.** Amie's product (calendar, inbox, notes, recording) sits behind https://calendar.amie.so/login (Continue with Google, Continue with Outlook, Continue with the app; no email field). That branch was recorded in [site-tree.md](site-tree.md) and not entered. https://app.amie.so/login returned 404. Download buttons were measured, never pressed.
- **Anything that sends, downloads or signs in.** No form was submitted, no field was typed, no app was downloaded, no trial was started, no account was created. Contact, subscribe, and tool feedback fields were left empty.
- **The Features flyout** was opened and screenshotted ([home-light-features](screenshots/home-light-features.png)). Its menu items were not re-measured as crops on 2026-11-21. The mobile header offers no hamburger at 390px.
- **Watch demo dialog** on `/features/notes` was opened and measured ([raw/dialog-computed.json](raw/dialog-computed.json)): scrim `rgba(0, 0, 0, 0.6)`, panel `#000` at 16px radius, 896×504, close button 40px `rgba(255,255,255,0.2)`. The YouTube iframe was not interacted with. Tooltip and toast were not present.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The site paints one light theme on every captured route. The stylesheet does carry a `.dark` block — it re-declares only `--foreground` and the two `--shadow-wysiwyg-*` values — plus `dark:` utility variants, but nothing on the captured routes sets the dark attribute, so the dark set is recorded in [raw/css-vars.json](raw/css-vars.json) and not emitted.

### Fonts

- **The UI font** is the SF/Inter system stack; no custom @font-face ships on the marketing pages.
- Illustration and wordmark artwork in the screenshots are Amie's property.

### Screenshots

- The mobile header at 390px offers no hamburger button (the m-menu-* entries are recorded missing): nav links collapse to the icon row.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- `/recap`, the pomodoro timer, the prompt generator, and a few docs pages paint wider than the viewport. Their `-full` PNGs record that overflow. Viewport shots stay 1440×900 and 390×844 at 2x.

### Content left out

- Feature imagery, the animated product shots and the wordmark are Amie's content; only the frames and components were measured.
