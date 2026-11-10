# Ballpark components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from ballparkhq.com on 2026-11-10, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (41 components, 109 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 14/21 500, #111827`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (109 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [solutions-menu](screenshots/home-light-solutions-menu.png) |
| Features | `/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| Coach | `/coach` | [default](screenshots/coach-light-default.png), [full](screenshots/coach-light-full.png) |
| Templates | `/templates` | [default](screenshots/templates-light-default.png), [full](screenshots/templates-light-full.png) |
| Enterprise | `/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Contact sales | `/contact/sales` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Sign in | `/sign-in` | [default](screenshots/signin-light-default.png), [full](screenshots/signin-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Features, phone | `/features` | [default](screenshots/mobile-features-light-default.png), [full](screenshots/mobile-features-light-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Solutions menu, open | header, home | the nav link's own hover | [home-light-solutions-menu](screenshots/home-light-solutions-menu.png), [nav-solutions-open](#solutions-menu-open) |
| Mobile menu, open | header, phone | the menu trigger's own press | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 19 components were given a real keyboard focus (a further 1 could not be driven: `nav-solutions`). 18 show a visible focus state: `announcement-bar` (1px auto #005fcc `measured.focus-outline`, offset 1px), `nav-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `nav-signin` (1px auto #005fcc `measured.focus-outline`, offset 1px), `nav-cta` (1px auto #005fcc `measured.focus-outline`, offset 1px), `intercom-launcher` (visible change in boxShadow), `feature-card` (1px auto #005fcc `measured.focus-outline`, offset 1px), `cta-request` (1px auto #005fcc `measured.focus-outline`, offset 1px), `plan-cta` (1px auto #005fcc `measured.focus-outline`, offset 1px), `contact-submit` (1px auto #005fcc `measured.focus-outline`, offset 0px), `signin-google` (visible change in boxShadow), `signin-sso` (visible change in boxShadow), `signin-forgot` (2px solid oklab(0.209998 -0.00316383 -0.0338463 / 0.1), offset 4px), `footer-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `footer-social` (1px auto #005fcc `measured.focus-outline`, offset 1px), `footer-rating` (1px auto #005fcc `measured.focus-outline`, offset 1px), `footer-legal` (1px auto #005fcc `measured.focus-outline`, offset 1px), `carousel-dot` (1px auto #005fcc `measured.focus-outline`, offset 0px), `coach-submit` (1px auto #005fcc `measured.focus-outline`, offset 0px). The other 1 show no change a keyboard user can see: `signin-submit`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): controls deepen their fill or dim rather than scale; the nav flyout and framework icons keep their hover scale. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.167s | `cubic-bezier(0.33, 0, 0, 1)` | transform | intercom-launcher |
| 0.3s | `cubic-bezier(0.23, 1, 0.32, 1)` | all, background-color, border-color, box-shadow, color, opacity, transform | signin-field, signin-forgot, signin-google, signin-password, signin-sso, signin-submit |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 384 x 594.39 | - | 24px | #ffffff `color.white` | rgba(0, 0, 0, 0.01) 0px 0.839802px 0.839802px -0.125px, rgba(0, 0, 0, 0.01) 0px 1.99048px 1.99048px -0.25px, rgba(0, 0, 0, 0.01) 0px 3.63084px 3.63084px -0.375px, rgba(0, 0, 0, 0.01) 0px 6.03627px 6.03627px -0.5px, rgba(0, 0, 0, 0.02) 0px 9.74808px 9.74808px -0.625px, rgba(0, 0, 0, 0.02) 0px 15.9566px 15.9566px -0.75px, rgba(0, 0, 0, 0.03) 0px 27.4762px 27.4762px -0.875px, rgba(0, 0, 0, 0.04) 0px 50px 50px -1px, rgba(75, 85, 99, 0.2) 0px 0px 0px 0.5px | 0 |
| [Feature card](#feature-card) | 366.67 x 600 | - | 16px | #ffffff `color.white` | rgba(0, 0, 0, 0.04) 0px 0.597144px 0.597144px -0.9375px, rgba(0, 0, 0, 0.04) 0px 1.81088px 1.81088px -1.875px, rgba(0, 0, 0, 0.04) 0px 4.78699px 4.78699px -2.8125px, rgba(0, 0, 0, 0.02) 0px 15px 15px -3.75px, rgba(75, 85, 99, 0.1) 0px 0px 0px 1px | 0 |
| [Coach demo widget](#coach-demo-widget) | 320 x 560 | - | 0px 12px 0px 0px | #f9fafb `color.gray.50` | none | 0 |

## Components

### Shell and navigation

The announcement strip, the two-row header with the Solutions flyout, and the Intercom launcher.

#### Header
The two-row bar under the announcement strip: logo, the nav (Platform, Solutions, Templates, Pricing), Sign in and the black Book a demo pill. Read as `header` on the home page.

**Values (default).** size 1392 x 156; radius 0px 0px 16px 16px; background #ffffff `color.white`; text IBM Plex Mono 11/16.5 600, #ffffff `color.white`; icon 13 x 13, #0000ee.

![Header default](components/crops/header-default.png)

#### Announcement bar
The "NEW · Ballpark is now available in Claude" banner over the header: a centred pill link with a coral NEW chip. Measured, never followed. Read as `announcement-bar` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1280 x 56; radius 0px 0px 16px 16px; background #f9fafb `color.gray.50`; text IBM Plex Mono 11/16.5 600, #ffffff `color.white`; icon 13 x 13, #0000ee |
| hover | background #f3f4f6 `color.gray.100` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | icon 13 x 13, #ff0000 |

![Announcement bar default](components/crops/announcement-bar-default.png) ![Announcement bar hover](components/crops/announcement-bar-hover.png) ![Announcement bar focus-visible](components/crops/announcement-bar-focus-visible.png) ![Announcement bar pressed](components/crops/announcement-bar-pressed.png)

#### Nav link
Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 84.08 x 36; padding 0px 14px; radius 7px; background #ffffff `color.white`; text Inter 14/20 600, #111827 `color.gray.900` |
| hover | background #f3f4f6 `color.gray.100` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Solutions menu link
The nav item that opens the mega menu of solutions pages on hover. Read as `nav-solutions` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 90 x 36; padding 0px 14px; radius 7px; background #ffffff `color.white`; text Inter 14/20 600, #111827 `color.gray.900` |
| hover | background #f3f4f6 `color.gray.100` |

![Solutions menu link default](components/crops/nav-solutions-default.png) ![Solutions menu link hover](components/crops/nav-solutions-hover.png) ![Solutions menu link focus-visible](components/crops/nav-solutions-focus-visible.png) ![Solutions menu link pressed](components/crops/nav-solutions-pressed.png)

#### Solutions menu, open
The link after its own hover opens the menu; the crop holds the opened panel region. Read as `nav-solutions-open` on the home page.

**Values (opened).** size 90 x 36; padding 0px 14px; radius 7px; background #f3f4f6 `color.gray.100`; text Inter 14/20 600, #111827 `color.gray.900`.

![Solutions menu, open opened](components/crops/nav-solutions-open-opened.png)

#### Sign in link
The secondary action on the right of the nav. Measured, never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 72.88 x 36; padding 0px 14px; radius 7px; background #ffffff `color.white`; shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px, rgba(75, 85, 99, 0.2) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 2px 2px 0px; text Inter 14/20 600, #111827 `color.gray.900` |
| hover | background #f9fafb `color.gray.50`; shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px, rgba(75, 85, 99, 0.4) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 4px 6px -1px; transform translate(0px, -1px) |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |

![Sign in link default](components/crops/nav-signin-default.png) ![Sign in link hover](components/crops/nav-signin-hover.png) ![Sign in link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign in link pressed](components/crops/nav-signin-pressed.png)

#### Book a demo button
The black pill on the right of the nav. Measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 139.95 x 36; padding 0px 14px; radius 7px; background #111827 `color.gray.900`; shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px, #111827 0px 0px 0px 1px; text Inter 14/20 600, #f9fafb `color.gray.50`; icon 13 x 13, #0000ee |
| hover | background #1f2937 `color.gray.800`; shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px, #1f2937 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px; transform translate(0px, -1px) |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | icon 13 x 13, #ff0000 |

![Book a demo button default](components/crops/nav-cta-default.png) ![Book a demo button hover](components/crops/nav-cta-hover.png) ![Book a demo button focus-visible](components/crops/nav-cta-focus-visible.png) ![Book a demo button pressed](components/crops/nav-cta-pressed.png)

#### Intercom launcher
The round chat bubble Intercom mounts at the bottom-right of every page (third-party widget). Read as `intercom-launcher` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 48; radius 50%; background #0071b2; shadow rgba(0, 0, 0, 0.06) 0px 1px 6px 0px, rgba(0, 0, 0, 0.16) 0px 2px 32px 0px; text system-ui 12/normal 400, #000000 `color.black`; transition transform 0.167s cubic-bezier(0.33, 0, 0, 1); icon 24 x 24, #000000 `color.black` |
| hover | size 52.8 x 52.8; transition transform 0.25s cubic-bezier(0.33, 0, 0, 1); transform scale(1.1); icon 26.4 x 26.4, #000000 `color.black` |
| focus-visible | shadow #38373e 0px 0px 0px 5px inset |
| pressed | size 40.8 x 40.8; transition transform 0.134s cubic-bezier(0.45, 0, 0.2, 1); transform scale(0.85); icon 20.4 x 20.4, #000000 `color.black` |

![Intercom launcher default](components/crops/intercom-launcher-default.png) ![Intercom launcher hover](components/crops/intercom-launcher-hover.png) ![Intercom launcher focus-visible](components/crops/intercom-launcher-focus-visible.png) ![Intercom launcher pressed](components/crops/intercom-launcher-pressed.png)

#### Logo
Read as `logo` on the home page.

**Values (default).** size 96 x 26; background transparent; text Inter 14/20 400, #111827 `color.gray.900`; icon 96 x 26, #0000ee.

![Logo default](components/crops/logo-default.png)

### Home

The serif hero, the feature cards, the closing CTA and the stories carousel dots.

#### Hero title
"Research without the complexity" in the site's display face (Inter Display). Read as `hero-title` on the home page.

**Values (default).** size 850 x 192; background transparent; text Inter Display 96/96 800, #000000 `color.black`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero subcopy
Read as `hero-sub` on the home page.

**Values (default).** size 670 x 60; background transparent; text Inter 20/30 400, #4b5563 `color.gray.600`.

![Hero subcopy default](components/crops/hero-sub-default.png)

#### Section title
Read as `section-title` on the home page.

**Values (default).** size 590 x 84; background transparent; text Inter Display 42/42 700, #111827 `color.gray.900`.

![Section title default](components/crops/section-title-default.png)

#### Feature card
A tall image card linking a feature page (live interviews, creative testing, …). Measured, never followed. Read as `feature-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 366.67 x 600; radius 16px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.04) 0px 0.597144px 0.597144px -0.9375px, rgba(0, 0, 0, 0.04) 0px 1.81088px 1.81088px -1.875px, rgba(0, 0, 0, 0.04) 0px 4.78699px 4.78699px -2.8125px, rgba(0, 0, 0, 0.02) 0px 15px 15px -3.75px, rgba(75, 85, 99, 0.1) 0px 0px 0px 1px; text Inter 12/16 700, #ffffff `color.white` |
| hover | transform translate(0px, -1px) |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |

![Feature card default](components/crops/feature-card-default.png) ![Feature card hover](components/crops/feature-card-hover.png) ![Feature card focus-visible](components/crops/feature-card-focus-visible.png) ![Feature card pressed](components/crops/feature-card-pressed.png)

#### Request a demo button
The closing CTA over the footer ("Try Ballpark with your team"). Measured, never followed. Read as `cta-request` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 160.73 x 36; padding 0px 14px; radius 7px; background #111827 `color.gray.900`; shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px, #111827 0px 0px 0px 1px; text Inter 14/20 600, #f9fafb `color.gray.50`; icon 13 x 13, #0000ee |
| hover | background #1f2937 `color.gray.800`; shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px, #1f2937 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px; transform translate(0px, -1px) |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | icon 13 x 13, #ff0000 |

![Request a demo button default](components/crops/cta-request-default.png) ![Request a demo button hover](components/crops/cta-request-hover.png) ![Request a demo button focus-visible](components/crops/cta-request-focus-visible.png) ![Request a demo button pressed](components/crops/cta-request-pressed.png)

#### Carousel page dot
The pagination dots of the stories carousel ("Scroll to page 1"…). Read as `carousel-dot` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 19 x 24; padding 8px 3px 8px 8px; background transparent; text sans-serif 12/normal 400, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |

Child layers that carry the look: div 8x8 background #ffffff `color.white` radius 50%.

![Carousel page dot default](components/crops/carousel-dot-default.png) ![Carousel page dot hover](components/crops/carousel-dot-hover.png) ![Carousel page dot focus-visible](components/crops/carousel-dot-focus-visible.png) ![Carousel page dot pressed](components/crops/carousel-dot-pressed.png)

#### Coach demo widget
The working "Ask Coach" demo box on the home page: the product's chat UI with an "Ask me anything…" field and a round submit. Read as `coach-widget` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 560; radius 16px; background transparent; shadow rgba(0, 0, 0, 0.07) 0px 0.602187px 0.602187px -1.25px, rgba(0, 0, 0, 0.06) 0px 2.28853px 2.28853px -2.5px, rgba(0, 0, 0, 0.03) 0px 10px 10px -3.75px, rgba(0, 0, 0, 0.2) 0px 20px 40px -15px, rgba(75, 85, 99, 0.1) 0px 0px 0px 1px, rgba(0, 0, 0, 0.03) 0px 0px 0px 5px; wrapper div.framer-v8hx28: shadow rgba(0, 0, 0, 0.07) 0px 0.602187px 0.602187px -1.25px, rgba(0, 0, 0, 0.06) 0px 2.28853px 2.28853px -2.5px, rgba(0, 0, 0, 0.03) 0px 10px 10px -3.75px, rgba(0, 0, 0, 0.2) 0px 20px 40px -15px, rgba(75, 85, 99, 0.1) 0px 0px 0px 1px, rgba(0, 0, 0, 0.03) 0px 0px 0px 5px; text Inter 14/20 600, #111827 `color.gray.900`; icon 30 x 24, #000000 `color.black` |
| hover | icon 10 x 10, #000000 `color.black` |

![Coach demo widget default](components/crops/coach-widget-default.png) ![Coach demo widget hover](components/crops/coach-widget-hover.png)

#### Coach ask field
The demo's ask field. The box paints a fake field (a Framer div, not an input or textarea), so the entry is recorded missing when the sweep finds no real input. Read as `coach-field` on the home page.

Not on the page when it was captured.

#### Coach send button
The round send button inside the demo. Measured, never pressed. Read as `coach-submit` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 24 x 24; radius 6px; background #e5e7eb `color.gray.200`; wrapper div.framer-5tv6xb: shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 10/14 400, #111827 `color.gray.900`; icon 10 x 10, #000000 `color.black` |
| hover | transform translate(0px, -1px) |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |

![Coach send button default](components/crops/coach-submit-default.png) ![Coach send button hover](components/crops/coach-submit-hover.png) ![Coach send button focus-visible](components/crops/coach-submit-focus-visible.png) ![Coach send button pressed](components/crops/coach-submit-pressed.png)

### Pricing

The plan card and its demo CTA.

#### Pricing title
Read as `pricing-title` on the pricing page.

**Values (default).** size 850 x 192; background transparent; text Inter Display 96/96 800, #000000 `color.black`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Plan CTA
The action inside an enterprise plan card. Measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 36; padding 0px 14px; radius 7px; background #111827 `color.gray.900`; shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px, #111827 0px 0px 0px 1px; text Inter 14/20 600, #f9fafb `color.gray.50`; icon 13 x 13, #0000ee |
| hover | background #1f2937 `color.gray.800`; shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px, #1f2937 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px; transform translate(0px, -1px) |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | icon 13 x 13, #ff0000 |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan card
Read as `plan-card` on the pricing page.

**Values (default).** size 384 x 594.39; radius 24px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.01) 0px 0.839802px 0.839802px -0.125px, rgba(0, 0, 0, 0.01) 0px 1.99048px 1.99048px -0.25px, rgba(0, 0, 0, 0.01) 0px 3.63084px 3.63084px -0.375px, rgba(0, 0, 0, 0.01) 0px 6.03627px 6.03627px -0.5px, rgba(0, 0, 0, 0.02) 0px 9.74808px 9.74808px -0.625px, rgba(0, 0, 0, 0.02) 0px 15.9566px 15.9566px -0.75px, rgba(0, 0, 0, 0.03) 0px 27.4762px 27.4762px -0.875px, rgba(0, 0, 0, 0.04) 0px 50px 50px -1px, rgba(75, 85, 99, 0.2) 0px 0px 0px 0.5px; text Inter Display 22/30.8 600, #111827 `color.gray.900`; icon 32 x 32, #4b5563 `color.gray.600`.

![Plan card default](components/crops/plan-card-default.png)

### Contact sales

The sales form's fields and submit.

#### Contact title
Read as `contact-title` on the contact sales page.

**Values (default).** size 489.5 x 42; background transparent; text Inter Display 42/42 700, #111827 `color.gray.900`.

![Contact title default](components/crops/contact-title-default.png)

#### Contact field
A short text field of the sales form (first/last name pair); sample text was typed and deleted, nothing sent. Read as `contact-field` on the contact sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 204.75 x 19.59; background transparent; wrapper div.framer-form-text-input.framer-form-input-wrapper: shadow rgba(0, 0, 0, 0.25) 0px 0px 0px 0px, rgba(0, 0, 0, 0.25) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 14/19.6 400, #111827 `color.gray.900`; placeholder #6b7280 `color.gray.500` |
| focused, filled | wrapper div.framer-form-text-input.framer-form-input-wrapper: shadow rgba(255, 255, 255, 0.25) 0px 0px 0px 0px, #d0d5db 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Contact field default](components/crops/contact-field-default.png) ![Contact field focused](components/crops/contact-field-focused.png) ![Contact field filled](components/crops/contact-field-filled.png)

#### Contact email field
The wider field under the name pair (work email); focused only, nothing typed. Read as `contact-email` on the contact sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 465.5 x 19.59; background transparent; wrapper div.framer-form-text-input.framer-form-input-wrapper: shadow rgba(0, 0, 0, 0.25) 0px 0px 0px 0px, rgba(0, 0, 0, 0.25) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 14/19.6 400, #111827 `color.gray.900`; placeholder #6b7280 `color.gray.500` |
| focused | wrapper div.framer-form-text-input.framer-form-input-wrapper: shadow rgba(255, 255, 255, 0.25) 0px 0px 0px 0px, #d0d5db 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Contact email field default](components/crops/contact-email-default.png) ![Contact email field focused](components/crops/contact-email-focused.png)

#### Message textarea
The form's message box; focused only, nothing typed. Read as `contact-message` on the contact sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 489.5 x 136; padding 10px 12px; background transparent; wrapper div.framer-form-text-input.framer-form-input-wrapper: shadow rgba(0, 0, 0, 0.25) 0px 0px 0px 0px, rgba(0, 0, 0, 0.25) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 14/19.6 400, #111827 `color.gray.900`; placeholder #6b7280 `color.gray.500` |
| focused | wrapper div.framer-form-text-input.framer-form-input-wrapper: shadow rgba(255, 255, 255, 0.25) 0px 0px 0px 0px, #d0d5db 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Message textarea default](components/crops/contact-message-default.png) ![Message textarea focused](components/crops/contact-message-focused.png)

#### Submit request button
The form's black submit. Measured, never pressed. Read as `contact-submit` on the contact sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 489.5 x 40; radius 6px; background #111827 `color.gray.900`; shadow #ffffff 0px 0px 0px 0px, #111827 0px 0px 0px 0px, rgba(0, 0, 0, 0.06) 0px 2px 3px 0px, rgba(0, 0, 0, 0.06) 0px 1px 2px -1px; text Inter 14/20 600, #ffffff `color.white` |
| hover | background #1f2937 `color.gray.800`; shadow #ffffff 0px 0px 0px 0px, #1f2937 0px 0px 0px 0px, rgba(0, 0, 0, 0.06) 0px 2px 3px 0px, rgba(0, 0, 0, 0.06) 0px 1px 2px -1px; transform translate(0px, -1px) |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |

![Submit request button default](components/crops/contact-submit-default.png) ![Submit request button hover](components/crops/contact-submit-hover.png) ![Submit request button focus-visible](components/crops/contact-submit-focus-visible.png) ![Submit request button pressed](components/crops/contact-submit-pressed.png)

### Sign in

The OAuth links, the email and password fields and the submit.

#### Sign-in title
Read as `signin-title` on the sign-in page.

**Values (default).** size 169.77 x 28; background transparent; text Inter 20/28 600, lab(8.11897 0.811279 -12.254).

![Sign-in title default](components/crops/signin-title-default.png)

#### Continue with Google
The OAuth link. Measured, never followed — no sign-in was attempted. Read as `signin-google` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 36; padding 0px 16px 0px 14px; radius 6px; background #ffffff `color.white`; shadow oklab(0.445998 -0.00685382 -0.0291959 / 0.2) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 2px 2px 0px; text Inter 14/20 600, lab(8.11897 0.811279 -12.254); transition background-color 0.3s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.3s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.3s cubic-bezier(0.23, 1, 0.32, 1), color 0.3s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.3s cubic-bezier(0.23, 1, 0.32, 1), transform 0.3s cubic-bezier(0.23, 1, 0.32, 1); icon 16 x 16, lab(8.11897 0.811279 -12.254) |
| hover | background lab(98.2596 -0.247031 -0.706708); shadow oklab(0.445998 -0.00685382 -0.0291959 / 0.4) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px |
| focus-visible | shadow lab(35.6337 -1.58697 -10.8425) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 2px 2px 0px |
| pressed | background lab(96.1596 -0.0823438 -1.13575); shadow oklab(0.445998 -0.00685382 -0.0291959 / 0.25) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 2px 2px 0px |

![Continue with Google default](components/crops/signin-google-default.png) ![Continue with Google hover](components/crops/signin-google-hover.png) ![Continue with Google focus-visible](components/crops/signin-google-focus-visible.png) ![Continue with Google pressed](components/crops/signin-google-pressed.png)

#### Continue with SSO
The SSO link. Measured, never followed. Read as `signin-sso` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 36; padding 0px 16px 0px 14px; radius 6px; background #ffffff `color.white`; shadow oklab(0.445998 -0.00685382 -0.0291959 / 0.2) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 2px 2px 0px; text Inter 14/20 600, lab(8.11897 0.811279 -12.254); transition background-color 0.3s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.3s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.3s cubic-bezier(0.23, 1, 0.32, 1), color 0.3s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.3s cubic-bezier(0.23, 1, 0.32, 1), transform 0.3s cubic-bezier(0.23, 1, 0.32, 1); icon 16 x 16, lab(8.11897 0.811279 -12.254) |
| hover | background lab(98.2596 -0.247031 -0.706708); shadow oklab(0.445998 -0.00685382 -0.0291959 / 0.4) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px |
| focus-visible | shadow lab(35.6337 -1.58697 -10.8425) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 2px 2px 0px |
| pressed | background lab(96.1596 -0.0823438 -1.13575); shadow oklab(0.445998 -0.00685382 -0.0291959 / 0.25) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 2px 2px 0px |

![Continue with SSO default](components/crops/signin-sso-default.png) ![Continue with SSO hover](components/crops/signin-sso-hover.png) ![Continue with SSO focus-visible](components/crops/signin-sso-focus-visible.png) ![Continue with SSO pressed](components/crops/signin-sso-pressed.png)

#### Email field
The sign-in email field; sample text was typed and deleted, nothing sent. Read as `signin-field` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 38; padding 0px 12px; border 1px solid oklab(0.445998 -0.00685382 -0.0291959 / 0.2); radius 6px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 14/20 400, lab(8.11897 0.811279 -12.254); transition background-color 0.3s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.3s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.3s cubic-bezier(0.23, 1, 0.32, 1), color 0.3s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.3s cubic-bezier(0.23, 1, 0.32, 1), transform 0.3s cubic-bezier(0.23, 1, 0.32, 1); placeholder lab(47.7841 -0.393182 -10.0268) |
| focused, filled | border 1px solid lab(35.6337 -1.58697 -10.8425); shadow lab(85.1236 -0.612259 -3.7138) 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Email field default](components/crops/signin-field-default.png) ![Email field focused](components/crops/signin-field-focused.png) ![Email field filled](components/crops/signin-field-filled.png)

#### Password field
The password field; focused only — nothing was typed into it. Read as `signin-password` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 38; padding 0px 12px; border 1px solid oklab(0.445998 -0.00685382 -0.0291959 / 0.2); radius 6px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 14/20 400, lab(8.11897 0.811279 -12.254); transition background-color 0.3s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.3s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.3s cubic-bezier(0.23, 1, 0.32, 1), color 0.3s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.3s cubic-bezier(0.23, 1, 0.32, 1), transform 0.3s cubic-bezier(0.23, 1, 0.32, 1); placeholder lab(47.7841 -0.393182 -10.0268) |
| focused | border 1px solid lab(35.6337 -1.58697 -10.8425); shadow lab(85.1236 -0.612259 -3.7138) 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Password field default](components/crops/signin-password-default.png) ![Password field focused](components/crops/signin-password-focused.png)

#### Continue with email button
The email sign-in submit. Measured, never pressed. Read as `signin-submit` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 384 x 36; padding 0px 16px; radius 6px; background #0a4481 `color.brand.navy.900`; shadow #0a4481 0px 0px 0px 1px; text Inter 14/20 600, lab(98.2596 -0.247031 -0.706708); transition background-color 0.3s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.3s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.3s cubic-bezier(0.23, 1, 0.32, 1), color 0.3s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.3s cubic-bezier(0.23, 1, 0.32, 1), transform 0.3s cubic-bezier(0.23, 1, 0.32, 1) |
| hover | background #0954a5 `color.brand.navy.700`; shadow #0954a5 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px |
| pressed | background #0954a5 `color.brand.navy.700`; shadow #0954a5 0px 0px 0px 1px |

![Continue with email button default](components/crops/signin-submit-default.png) ![Continue with email button hover](components/crops/signin-submit-hover.png) ![Continue with email button focus-visible](components/crops/signin-submit-focus-visible.png) ![Continue with email button pressed](components/crops/signin-submit-pressed.png)

#### Forgot password link
Read as `signin-forgot` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 102.7 x 16; background transparent; text Inter 12/16 500, lab(47.7841 -0.393182 -10.0268); transition all 0.3s cubic-bezier(0.23, 1, 0.32, 1) |
| hover | text Inter 12/16 500, lab(8.11897 0.811279 -12.254) |
| focus-visible | radius 2px; outline 2px solid oklab(0.209998 -0.00316383 -0.0338463 / 0.1), offset 4px |
| pressed | text Inter 12/16 500, lab(8.11897 0.811279 -12.254) |

![Forgot password link default](components/crops/signin-forgot-default.png) ![Forgot password link hover](components/crops/signin-forgot-hover.png) ![Forgot password link focus-visible](components/crops/signin-forgot-focus-visible.png) ![Forgot password link pressed](components/crops/signin-forgot-pressed.png)

### Footer

The link columns, socials, the G2 badge and legal.

#### Footer
Read as `footer` on the home page.

**Values (default).** size 1392 x 1539; radius 16px; background #f9fafb `color.gray.50`; text Inter Display 60/60 800, #111827 `color.gray.900`; icon 13 x 13, #0000ee.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 160.73 x 36; padding 0px 14px; radius 7px; background #111827 `color.gray.900`; shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px, #111827 0px 0px 0px 1px; text Inter 14/20 600, #f9fafb `color.gray.50`; icon 13 x 13, #0000ee |
| hover | background #1f2937 `color.gray.800`; shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px, #1f2937 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px; transform translate(0px, -1px) |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | icon 13 x 13, #ff0000 |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer social icon
Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 36 x 36; radius 100px; background #f9fafb `color.gray.50`; text Inter 12/16 500, #111827 `color.gray.900`; icon 22 x 22, #4b5563 `color.gray.600` |
| hover | background #f3f4f6 `color.gray.100`; icon 22 x 22, #111827 `color.gray.900` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |

![Footer social icon default](components/crops/footer-social-default.png) ![Footer social icon hover](components/crops/footer-social-hover.png) ![Footer social icon focus-visible](components/crops/footer-social-focus-visible.png) ![Footer social icon pressed](components/crops/footer-social-pressed.png)

#### G2 rating badge
The "4.6 Star Rating" badge linking the G2 review page. Measured, never followed. Read as `footer-rating` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 156.28 x 44; background transparent; text Inter 14/20 500, #111827 `color.gray.900`; icon 44 x 44, #0000ee |
| hover | text Inter 14/20 500, #fc4a2b `color.brand.flame.500`; transform translate(0px, -1px) |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | icon 44 x 44, #ff0000 |

Child layers that carry the look: div 44x44 background #ff492c radius 100px.

![G2 rating badge default](components/crops/footer-rating-default.png) ![G2 rating badge hover](components/crops/footer-rating-hover.png) ![G2 rating badge focus-visible](components/crops/footer-rating-focus-visible.png) ![G2 rating badge pressed](components/crops/footer-rating-pressed.png)

#### Legal link
Read as `footer-legal` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 53.91 x 17; background transparent; text Inter 14/20 400, #4b5563 `color.gray.600` |
| hover | text Inter 14/20 400, #111827 `color.gray.900` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | text Inter 14/20 400, #111827 `color.gray.900` |

![Legal link default](components/crops/footer-legal-default.png) ![Legal link hover](components/crops/footer-legal-hover.png) ![Legal link focus-visible](components/crops/footer-legal-focus-visible.png) ![Legal link pressed](components/crops/footer-legal-pressed.png)

### Mobile (390 wide)

The same surface at phone width, with its full-sheet menu.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 72; background transparent; text Inter 14/20 400, #111827 `color.gray.900`; icon 96 x 26, #0000ee.

Child layers that carry the look: div 390x72 background #ffffff `color.white`; div 36x36 background #ffffff `color.white` radius 100px; div 20x2 background #111827 `color.gray.900` radius 1px.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
The 36px trigger at the right of the mobile bar; its own press opens the menu overlay. Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 36 x 36; radius 100px; background #ffffff `color.white`; text sans-serif 12/normal 400, #000000 `color.black` |

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The trigger after its own toggle; the open overlay shows in the crop. Read as `m-menu-open` on the home page at 390 wide.

**Values (opened).** size 36 x 36; radius 100px; background #f9fafb `color.gray.50`; text sans-serif 12/normal 400, #000000 `color.black`.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Ballpark's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The app behind sign-in.** Ballpark's product sits behind /sign-in and was never reached; the OAuth links and email form were measured, never used.
- **Anything that sends or signs in.** No form was submitted, no demo was booked, no account was created, the Intercom chat was never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The site paints one light theme on every captured route; the Framer bundle declares no dark variant, so no dark set is emitted.

### Fonts

- **The UI fonts** are Framer-served webfonts (Inter Display, Inter, Source Serif 4 and five more faces; `fonts` in [raw/css-vars.json](raw/css-vars.json)); the font files themselves are not committed.
- Illustration and wordmark artwork in the screenshots are Ballpark's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Feature imagery, the animated product shots and the wordmark are Ballpark's content; only the frames and components were measured.
