# Aboard HR components

The discovery list of every page and view captured, then one entry per component with crops of the real site, the icon index and the Gaps. Captured from aboardhr.com on 2026-11-10, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was sent or submitted: the book-a-demo form was measured at rest and focus only, the app.aboardhr.com sign-in was never opened, and no consent strip ever rendered (none was answered).

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (56 components, 109 states). The page layouts at four widths are in [raw/layout.json](raw/layout.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Tobias 64/68 400, #232a20`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (109 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (aboardhr.com has one theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 390 wide.

| Surface | URL | Screenshots |
|---|---|---|
| Home. Display hero, co-pilot demo, pastel product cards. | `/` | [copilot](screenshots/home-light-copilot.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Everyday HR. Product page with mint cards. | `/everyday-hr` | [default](screenshots/everyday-hr-light-default.png), [full](screenshots/everyday-hr-light-full.png) |
| Growth & feedback. Product page. | `/growth-feedback` | [default](screenshots/growth-feedback-light-default.png), [full](screenshots/growth-feedback-light-full.png) |
| Team culture. Product page with pink cards. | `/team-culture` | [default](screenshots/team-culture-light-default.png), [full](screenshots/team-culture-light-full.png) |
| Pricing. The single plan card. | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| What's new. The changelog index. | `/whats-new` | [default](screenshots/whats-new-light-default.png), [full](screenshots/whats-new-light-full.png) |
| What's new detail. The June 2026 release notes. | `/whats-new/june-2026` | [default](screenshots/release-light-default.png), [full](screenshots/release-light-full.png) |
| Book a demo. The request form, measured at rest. | `/book-demo` | [default](screenshots/book-demo-light-default.png), [full](screenshots/book-demo-light-full.png) |
| Teamtailor x Aboard. The partner page. | `/teamtailor-and-aboard` | [default](screenshots/teamtailor-light-default.png), [full](screenshots/teamtailor-light-full.png) |
| Data protection. Legal text. | `/dataprotection` | [default](screenshots/dataprotection-light-default.png), [full](screenshots/dataprotection-light-full.png) |
| Terms. Legal text. | `/terms` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| Home at 390: collapsed header, the opened menu, single-column cards. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Everyday HR at 390. | `/everyday-hr` | [default](screenshots/mobile-everyday-hr-light-default.png), [full](screenshots/mobile-everyday-hr-light-full.png) |
| Pricing at 390. | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu, open | home at 390 | the nav trigger pressed (a local disclosure) | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-nav-panel](#m-nav-panel) |
| Co-pilot demo | home hero | the animated chat mock scrolled into view; a marketing animation, not a live product | [home-light-copilot](screenshots/home-light-copilot.png), [copilot-demo](#copilot-demo) |
| Form focus | book a demo | a field clicked into; nothing typed, nothing sent | [demo-field](#demo-field) |
| App sign-in | nav links out to app.aboardhr.com | never opened; the product app sits behind a sign-in the capture does not take | no screenshot; documented under Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 15 components were given a real keyboard focus. 13 draw a ring: `nav-logo` (1px auto #005fcc `focus-blue`, offset 1px), `nav-cta` (1px auto #005fcc `focus-blue`, offset 1px), `footer-link` (1px auto #005fcc `focus-blue`, offset 1px), `cta-demo` (1px auto #005fcc `focus-blue`, offset 1px), `cta-try` (1px auto #005fcc `focus-blue`, offset 1px), `learn-more` (1px auto #005fcc `focus-blue`, offset 1px), `everyday-hr-cta` (1px auto #005fcc `focus-blue`, offset 1px), `growth-feedback-cta` (1px auto #005fcc `focus-blue`, offset 1px), `team-culture-cta` (1px auto #005fcc `focus-blue`, offset 1px), `plan-cta` (1px auto #005fcc `focus-blue`, offset 1px), `demo-submit` (1px auto #005fcc `focus-blue`, offset 0px), `release-back` (1px auto #005fcc `focus-blue`, offset 1px), `teamtailor-cta` (1px auto #005fcc `focus-blue`, offset 1px). The other 2 draw none, so a keyboard user sees no change: `nav-link`, `m-menu-trigger`.

**Pressed.** Forced `:active` was applied to the buttons and links above; the site changes very little under the finger (the nav CTA and consent buttons keep their fills). See each entry's Pressed row for what did move.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|

**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).

| Page | 1440 | 1920 | 1024 | 390 |
|---|---|---|---|---|
| home | content x 0, 1440 wide; grid 330 330 gap 20px | content x 0, 1920 wide; grid 330 330 gap 20px | content x 0, 1024 wide; grid 330 330 gap 20px | content x 0, 390 wide |
| everyday-hr | content x 0, 1440 wide; grid 330 330 gap 20px | content x 0, 1920 wide; grid 330 330 gap 20px | content x 0, 1024 wide; grid 330 330 gap 20px | content x 0, 390 wide |
| growth-feedback | content x 0, 1440 wide | content x 0, 1920 wide | content x 0, 1024 wide | content x 0, 390 wide |
| team-culture | content x 0, 1440 wide | content x 0, 1920 wide | content x 0, 1024 wide | content x 0, 390 wide |
| pricing | content x 0, 1440 wide; grid 330 330 gap 20px | content x 0, 1920 wide; grid 330 330 gap 20px | content x 0, 1024 wide; grid 330 330 gap 20px | content x 0, 390 wide |
| whats-new | content x 0, 1440 wide | content x 0, 1920 wide | content x 0, 1024 wide | content x 0, 390 wide |
| book-demo | content x 0, 1440 wide | content x 0, 1920 wide | content x 0, 1024 wide | content x 0, 390 wide |
| teamtailor | content x 0, 1440 wide | content x 0, 1920 wide | content x 0, 1024 wide | content x 0, 390 wide |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Feature card](#feature-card) | 476 x 620 | - | 24px | #afe4ff `card-blue` | none | 0 |
| [Feature card](#feature-card) | 476 x 620 | - | 24px | #8df1ed `card-teal` | none | 0 |
| [Feature card](#feature-card) | 476 x 620 | - | - | - | none | 32px |
| [Feature card](#feature-card) | 476 x 620 | - | 24px | #fbcfe8 `card-pink` | none | 0 |
| [Partner card](#partner-card) | 976 x 799 | - | 24px | #ffffff `white` | none | 48px 0px |
| [Plan card](#plan-card) | 976 x 750.41 | - | 24px | #ffffff `white` | none | 48px |
| [Demo form](#demo-form) | 280 x 638.84 | - | 10px | rgba(23, 23, 23, 0.05) `field-fill` | none | 0 |
| [Release row](#release-row) | 240 x 44 | - | - | transparent | none | 10px 0px |
| [Learn-more link](#learn-more-link) | 141.2 x 48 | - | 99px | rgba(255, 255, 255, 0.6) `white-60` | none | 10px 24px |

## Components

### Shell and navigation

The shell every page shares: a 90px fixed header (64px at 390) with the Aboard wordmark, the Product / Price / Resources links and the Sign-in + Book-a-demo actions, and a light footer band with the "Smooth sailing." sign-off and the link columns (Price / What's new / Help center / legal).

#### Top navigation bar
The floating nav: logo, Product / Price / Resources links and the Sign-in / Book-a-demo actions. Read as `nav-bar` on the home page.

**Values (default).** size 1440 x 90; background transparent; shadow rgba(23, 23, 23, 0.08) 0px 0px 0px 0px; text system-ui 15/30 500, rgba(60, 60, 63, 0.7) `body`; icon 83 x 29, #0000ee.

![Top navigation bar default](components/crops/nav-bar-default.png)

#### Logo
The Aboard wordmark linking home. Read as `nav-logo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 111 x 29; background transparent; text sans-serif 12/normal 400, #0000ee; icon 83 x 29, #0000ee |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |
| pressed | text sans-serif 12/normal 400, #ff0000 `active-red`; icon 83 x 29, #ff0000 `active-red` |

![Logo default](components/crops/nav-logo-default.png) ![Logo hover](components/crops/nav-logo-hover.png) ![Logo focus-visible](components/crops/nav-logo-focus-visible.png) ![Logo pressed](components/crops/nav-logo-pressed.png)

#### Nav link
A section link in the top bar. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 74.55 x 38; padding 4px 10px; radius 12px; background transparent; text system-ui 15/30 500, rgba(60, 60, 63, 0.7) `body` |
| hover | background rgba(112, 112, 121, 0.08) `nav-hover`; text system-ui 15/30 500, rgba(38, 38, 38, 0.996) |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Nav CTA
The boxed action at the right of the nav (Sign in / Book a demo). Hovered and focused only; app.aboardhr.com is never opened. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 154.86 x 48; padding 10px 24px; radius 99px; background #e0f2fe `tint-blue`; text system-ui 18/28 600, #008ae8 `accent-ink` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Footer
The "Smooth sailing" footer band: link columns (Price / What's new / Help center / legal) and the Teamtailor credit row. Read as `footer` on the home page.

**Values (default).** size 976 x 128; padding 0px 0px 40px 0px; background transparent; text system-ui 20/30 600, rgba(60, 60, 63, 0.7) `body`.

Child layers that carry the look: div::after 976pxx128px border 1px solid rgba(23, 23, 23, 0.1) `ring`.

![Footer default](components/crops/footer-default.png)

#### Footer heading
The "Smooth sailing." sign-off heading in the footer. Read as `footer-heading` on the home page.

**Values (default).** size 566 x 30; background transparent; text system-ui 20/30 600, rgba(60, 60, 63, 0.7) `body`.

![Footer heading default](components/crops/footer-heading-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 86.2 x 18; background transparent; text system-ui 16/24 500, #777777 `grey-link` |
| hover | text system-ui 16/24 500, #555555 `grey-link-hover` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |
| pressed | text system-ui 16/24 500, #555555 `grey-link-hover` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Home

The home page: the "Run people operations. With clarity." display hero, the animated co-pilot chat demo (a marketing animation, not a live product), the pastel product cards and the logo/feature bands.

#### Hero title
"Run people operations. With clarity." — the display headline. Read as `hero-title` on the home page.

**Values (default).** size 768 x 70.41; background transparent; text system-ui 64/70.4 600, #262626 `ink`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero subtitle
The paragraph under the hero title. Read as `hero-sub` on the home page.

**Values (default).** size 768 x 64; background transparent; text system-ui 20/32 500, rgba(60, 60, 63, 0.7) `body`.

![Hero subtitle default](components/crops/hero-sub-default.png)

#### Primary CTA
The "Book a demo" button under the hero. Hovered and focused only. Read as `cta-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 154.86 x 48; padding 10px 24px; radius 99px; background transparent; text system-ui 18/28 600, #ffffff `white` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

Child layers that carry the look: div 154.9x48 background #009cff `accent`.

![Primary CTA default](components/crops/cta-demo-default.png) ![Primary CTA hover](components/crops/cta-demo-hover.png) ![Primary CTA focus-visible](components/crops/cta-demo-focus-visible.png) ![Primary CTA pressed](components/crops/cta-demo-pressed.png)

#### Secondary CTA
The "Try for free" button. Hovered and focused only. Read as `cta-try` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 139.03 x 48; padding 10px 24px; radius 99px; background #e0f2fe `tint-blue`; text system-ui 18/28 600, #008ae8 `accent-ink` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

![Secondary CTA default](components/crops/cta-try-default.png) ![Secondary CTA hover](components/crops/cta-try-hover.png) ![Secondary CTA focus-visible](components/crops/cta-try-focus-visible.png) ![Secondary CTA pressed](components/crops/cta-try-pressed.png)

#### Co-pilot demo panel
The animated AI-assistant chat mock in the hero (a marketing demo, not a live product): the "Ask me anything" prompt inside the chat panel. Read as `copilot-demo` on the home page.

**Values (default).** size 267.3 x 313.2; background transparent; text system-ui 12/16.8 400, #262626 `ink`; transform matrix(1, 0, 0, 1.00288, 0, 0.499997).

Child layers that carry the look: div 236.2x37.8 background #e0f2fe `tint-blue` radius 3.81111% 3.81111% 1.52444% / 23.8095% 23.8095% 9.52381%; h1 127.9x15.1 image linear-gradient(90deg, transparent 0%, transparent 23%, #ffffff `white` 50%, transparent 7; p 43.6x15.1 image linear-gradient(90deg, transparent 0%, transparent 20%, #ffffff `white` 50%, transparent 8.

![Co-pilot demo panel default](components/crops/copilot-demo-default.png)

#### Section title
A section heading ("Built for people, not just the process"). Read as `section-title` on the home page.

**Values (default).** size 680 x 112; background transparent; text system-ui 56/56 600, #262626 `ink`.

![Section title default](components/crops/section-title-default.png)

#### Feature card
A product-area card (Everyday HR / Team culture / Growth & feedback). Read as `feature-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 476 x 620; radius 24px; background #afe4ff `card-blue`; text system-ui 44/48.4 600, #262626 `ink`; icon 62 x 56, #000000 |

![Feature card default](components/crops/feature-card-default.png) ![Feature card hover](components/crops/feature-card-hover.png)

#### Feature list item
A feature row inside a product card (People directory, Time off, Contracts & documents). Read as `feature-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 278 x 30; background transparent; text system-ui 20/30 600, #262626 `ink` |

![Feature list item default](components/crops/feature-item-default.png) ![Feature list item hover](components/crops/feature-item-hover.png)

#### Learn-more link
The text link inside a feature card. Read as `learn-more` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 141.2 x 48; padding 10px 24px; radius 99px; background rgba(255, 255, 255, 0.6) `white-60`; text system-ui 18/28 600, #262626 `ink` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

![Learn-more link default](components/crops/learn-more-default.png) ![Learn-more link hover](components/crops/learn-more-hover.png) ![Learn-more link focus-visible](components/crops/learn-more-focus-visible.png) ![Learn-more link pressed](components/crops/learn-more-pressed.png)

### Product pages

The three product pages (Everyday HR, Growth & feedback, Team culture) share one layout: a display headline, pastel 24px-radius cards with feature rows, and a blue CTA pill.

#### Page title
Read as `everyday-hr-title` on the Everyday HR page.

**Values (default).** size 976 x 70.41; background transparent; text system-ui 64/70.4 600, #262626 `ink`.

![Page title default](components/crops/everyday-hr-title-default.png)

#### Section title
Read as `everyday-hr-section` on the Everyday HR page.

**Values (default).** size 680 x 112; background transparent; text system-ui 56/56 600, #262626 `ink`.

![Section title default](components/crops/everyday-hr-section-default.png)

#### Feature card
Read as `everyday-hr-card` on the Everyday HR page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 476 x 620; radius 24px; background #8df1ed `card-teal`; text system-ui 44/48.4 600, #262626 `ink`; icon 50 x 61, #000000 |

![Feature card default](components/crops/everyday-hr-card-default.png) ![Feature card hover](components/crops/everyday-hr-card-hover.png)

#### Feature item
Read as `everyday-hr-item` on the Everyday HR page.

**Values (default).** size 278 x 30; background transparent; text system-ui 20/30 600, #262626 `ink`.

![Feature item default](components/crops/everyday-hr-item-default.png)

#### Page CTA
Read as `everyday-hr-cta` on the Everyday HR page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 154.86 x 48; padding 10px 24px; radius 99px; background transparent; text system-ui 18/28 600, #ffffff `white` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

Child layers that carry the look: div 154.9x48 background #009cff `accent`.

![Page CTA default](components/crops/everyday-hr-cta-default.png) ![Page CTA hover](components/crops/everyday-hr-cta-hover.png) ![Page CTA focus-visible](components/crops/everyday-hr-cta-focus-visible.png) ![Page CTA pressed](components/crops/everyday-hr-cta-pressed.png)

#### Page title
Read as `growth-feedback-title` on the Growth & feedback page.

**Values (default).** size 976 x 140.81; background transparent; text system-ui 64/70.4 600, #262626 `ink`.

![Page title default](components/crops/growth-feedback-title-default.png)

#### Section title
Read as `growth-feedback-section` on the Growth & feedback page.

**Values (default).** size 680 x 112; background transparent; text system-ui 56/56 600, #262626 `ink`.

![Section title default](components/crops/growth-feedback-section-default.png)

#### Feature card
Read as `growth-feedback-card` on the Growth & feedback page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 476 x 620; padding 32px; radius 24px; background transparent; text system-ui 44/48.4 600, #ffffff `white`; icon 62 x 62, #ffffff `white` |

Child layers that carry the look: div 476x620 image linear-gradient(transparent 50%, rgba(0, 0, 0, 0.5) 100%).

![Feature card default](components/crops/growth-feedback-card-default.png) ![Feature card hover](components/crops/growth-feedback-card-hover.png)

#### Feature item
A feature row inside a product card. Read as `growth-feedback-item` on the Growth & feedback page.

**Values (default).** size 976 x 32; background transparent; text system-ui 20/32 500, rgba(60, 60, 63, 0.7) `body`.

![Feature item default](components/crops/growth-feedback-item-default.png)

#### Page CTA
Read as `growth-feedback-cta` on the Growth & feedback page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 154.86 x 48; padding 10px 24px; radius 99px; background transparent; text system-ui 18/28 600, #ffffff `white` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

Child layers that carry the look: div 154.9x48 background #009cff `accent`.

![Page CTA default](components/crops/growth-feedback-cta-default.png) ![Page CTA hover](components/crops/growth-feedback-cta-hover.png) ![Page CTA focus-visible](components/crops/growth-feedback-cta-focus-visible.png) ![Page CTA pressed](components/crops/growth-feedback-cta-pressed.png)

#### Page title
Read as `team-culture-title` on the Team culture page.

**Values (default).** size 976 x 140.81; background transparent; text system-ui 64/70.4 600, #262626 `ink`.

![Page title default](components/crops/team-culture-title-default.png)

#### Section title
Read as `team-culture-section` on the Team culture page.

**Values (default).** size 680 x 56; background transparent; text system-ui 56/56 600, #262626 `ink`.

![Section title default](components/crops/team-culture-section-default.png)

#### Feature card
Read as `team-culture-card` on the Team culture page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 476 x 620; radius 24px; background #fbcfe8 `card-pink`; text system-ui 44/48.4 600, #262626 `ink`; icon 75 x 58, #000000 |

![Feature card default](components/crops/team-culture-card-default.png) ![Feature card hover](components/crops/team-culture-card-hover.png)

#### Feature item
A feature row inside a product card. Read as `team-culture-item` on the Team culture page.

**Values (default).** size 976 x 32; background transparent; text system-ui 20/32 500, rgba(60, 60, 63, 0.7) `body`.

![Feature item default](components/crops/team-culture-item-default.png)

#### Page CTA
Read as `team-culture-cta` on the Team culture page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 154.86 x 48; padding 10px 24px; radius 99px; background transparent; text system-ui 18/28 600, #ffffff `white` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

Child layers that carry the look: div 154.9x48 background #009cff `accent`.

![Page CTA default](components/crops/team-culture-cta-default.png) ![Page CTA hover](components/crops/team-culture-cta-hover.png) ![Page CTA focus-visible](components/crops/team-culture-cta-focus-visible.png) ![Page CTA pressed](components/crops/team-culture-cta-pressed.png)

### Pricing

The pricing page: a single white plan card ("80 kr / user / month") on the flat ground with a light-blue CTA. There is no billing-period toggle on the page.

#### Page title
Read as `pricing-title` on the pricing page.

**Values (default).** size 147.59 x 70.41; background transparent; text system-ui 64/70.4 600, #262626 `ink`.

![Page title default](components/crops/pricing-title-default.png)

#### Plan card
A pricing plan card. Read as `price-card` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 976 x 750.41; padding 48px; radius 24px; background #ffffff `white`; text system-ui 64/70.4 600, #262626 `ink`; icon 16 x 23, #000000 |

![Plan card default](components/crops/price-card-default.png) ![Plan card hover](components/crops/price-card-hover.png)

#### Plan price
The "80 kr / user / month" price figure. Read as `price-amount` on the pricing page.

**Values (default).** size 147.59 x 70.41; background transparent; text system-ui 64/70.4 600, #262626 `ink`.

![Plan price default](components/crops/price-amount-default.png)

#### Plan CTA
Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 154.86 x 48; padding 10px 24px; radius 99px; background #e0f2fe `tint-blue`; text system-ui 18/28 600, #008ae8 `accent-ink` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Billing toggle
The monthly/yearly switch, if rendered (never toggled). Read as `billing-toggle` on the pricing page.

Not on the page when it was captured.

### Book a demo (resting only)

The one real form on the site, Framer's own: Inter labels over ink-at-5% fields and a ringed submit. It was measured at rest and at focus only; nothing was typed and the form was never submitted.

#### Page title
"Request a demo" — the form page heading. Read as `demo-title` on the book a demo page.

**Values (default).** size 680 x 56; background transparent; text system-ui 56/56 600, #262626 `ink`.

![Page title default](components/crops/demo-title-default.png)

#### Demo form
The book-a-demo form or scheduler embed. Measured at rest; nothing typed or sent. Read as `demo-form` on the book a demo page.

**Values (default).** size 280 x 638.84; background transparent; text Inter 12/14.4 500, #888888 `grey-label`.

Child layers that carry the look: div 280x40 background rgba(23, 23, 23, 0.05) `field-fill` radius 10px; div 280x40 background rgba(23, 23, 23, 0.05) `field-fill` radius 10px; div 280x40 background rgba(23, 23, 23, 0.05) `field-fill` radius 10px.

![Demo form default](components/crops/demo-form-default.png)

#### Demo field
A text field of the demo form. Clicked into for the focus style; nothing typed. Read as `demo-field` on the book a demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 256 x 16; background transparent; text Inter 16/16 500, #262626 `ink`; placeholder rgba(60, 60, 63, 0.4) `faint` |

![Demo field default](components/crops/demo-field-default.png) ![Demo field focused](components/crops/demo-field-focused.png)

#### Demo submit
The "Let’s talk" form submit button. Measured in every state, never pressed. Read as `demo-submit` on the book a demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 280 x 40; padding 5px 12px; radius 12px; background transparent; image linear-gradient(#ffffff `white` 0%, #fbfaf9 100%); shadow rgba(23, 23, 23, 0.1) 0px 0px 0px 2px; text Inter 15/30 600, #262626 `ink` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 0px |

![Demo submit default](components/crops/demo-submit-default.png) ![Demo submit hover](components/crops/demo-submit-hover.png) ![Demo submit focus-visible](components/crops/demo-submit-focus-visible.png) ![Demo submit pressed](components/crops/demo-submit-pressed.png)

### What's new

The changelog index (dated release rows) and one detail page (June 2026), a plain reading column with a back link.

#### Page title
Read as `whatsnew-title` on the What's new page.

**Values (default).** size 976 x 70.41; background transparent; text system-ui 64/70.4 600, #262626 `ink`.

![Page title default](components/crops/whatsnew-title-default.png)

#### Release row
A dated changelog entry on the Whats-new page. Read as `release-row` on the What's new page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 240 x 44; padding 10px 0px; background transparent; text system-ui 16/24 500, rgba(60, 60, 63, 0.7) `body` |

![Release row default](components/crops/release-row-default.png) ![Release row hover](components/crops/release-row-hover.png)

#### Release title
The dated headline of a changelog detail page (June 2026). Read as `release-title` on the What's new release page.

**Values (default).** size 1152 x 140.81; background transparent; text system-ui 64/70.4 600, #262626 `ink`.

![Release title default](components/crops/release-title-default.png)

#### Back link
The "Link back" anchor returning to the What's new index. Read as `release-back` on the What's new release page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 111 x 29; background transparent; text sans-serif 12/normal 400, #0000ee; icon 83 x 29, #0000ee |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |
| pressed | text sans-serif 12/normal 400, #ff0000 `active-red`; icon 83 x 29, #ff0000 `active-red` |

![Back link default](components/crops/release-back-default.png) ![Back link hover](components/crops/release-back-hover.png) ![Back link focus-visible](components/crops/release-back-focus-visible.png) ![Back link pressed](components/crops/release-back-pressed.png)

#### Release body
The changelog post body on a detail page. Read as `release-post` on the What's new release page.

**Values (default).** size 1200 x 6677.86; padding 132px 24px 0px 24px; background transparent; text system-ui 16/24 500, rgba(60, 60, 63, 0.7) `body`.

![Release body default](components/crops/release-post-default.png)

### Teamtailor partner page

The Teamtailor-x-Aboard co-marketing page: a 32px-radius white partner card, the shared display headline and the same blue CTA.

#### Page title
"The best candidate experience deserves an equally great employee experience." Read as `teamtailor-title` on the Teamtailor page.

**Values (default).** size 880 x 211.22; background transparent; text system-ui 64/70.4 600, #262626 `ink`.

![Page title default](components/crops/teamtailor-title-default.png)

#### Partner card
Read as `teamtailor-card` on the Teamtailor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 976 x 799; padding 48px 0px; radius 32px; background transparent; text Inter 12/14.4 500, #888888 `grey-label` |

Child layers that carry the look: div 340x703 background #ffffff `white` radius 24px; div::after 340pxx703px border 1px solid rgba(23, 23, 23, 0.1) `ring` radius 24px; div 280x40 background rgba(23, 23, 23, 0.05) `field-fill` radius 10px.

![Partner card default](components/crops/teamtailor-card-default.png) ![Partner card hover](components/crops/teamtailor-card-hover.png)

#### Page CTA
Read as `teamtailor-cta` on the Teamtailor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 154.86 x 48; padding 10px 24px; radius 99px; background transparent; text system-ui 18/28 600, #ffffff `white` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

Child layers that carry the look: div 154.9x48 background #009cff `accent`.

![Page CTA default](components/crops/teamtailor-cta-default.png) ![Page CTA hover](components/crops/teamtailor-cta-hover.png) ![Page CTA focus-visible](components/crops/teamtailor-cta-focus-visible.png) ![Page CTA pressed](components/crops/teamtailor-cta-pressed.png)

### Legal text

The data-protection and terms pages: heading plus running legal copy in the same shell.

#### Page title
Read as `dataprotection-title` on the data protection page.

**Values (default).** size 976 x 48.41; background transparent; text system-ui 44/48.4 600, #262626 `ink`.

![Page title default](components/crops/dataprotection-title-default.png)

#### Body text
Read as `dataprotection-body` on the data protection page.

**Values (default).** size 976 x 32; background transparent; text system-ui 20/32 500, rgba(60, 60, 63, 0.7) `body`.

![Body text default](components/crops/dataprotection-body-default.png)

#### Page title
Read as `terms-title` on the terms page.

**Values (default).** size 976 x 48.41; background transparent; text system-ui 44/48.4 600, #262626 `ink`.

![Page title default](components/crops/terms-title-default.png)

#### Body text
Read as `terms-body` on the terms page.

**Values (default).** size 976 x 32; background transparent; text system-ui 20/32 500, rgba(60, 60, 63, 0.7) `body`.

![Body text default](components/crops/terms-body-default.png)

### Mobile (390 wide)

A few components as a phone draws them, at 390 x 844: the collapsed header with its menu trigger, the opened nav panel and the 48px hero title.

#### Mobile top bar
The mobile header: logo left, menu trigger right. Read as `m-nav-bar` on the home page at 390 wide.

**Values (default).** size 37 x 16; background transparent; text sans-serif 12/normal 400, #000000.

![Mobile top bar default](components/crops/m-nav-bar-default.png)

#### Mobile menu trigger
The menu button. Pressed once below to open the menu; a local disclosure. Read as `m-menu-trigger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 37 x 16; background transparent; text sans-serif 12/normal 400, #000000 |

![Mobile menu trigger default](components/crops/m-menu-trigger-default.png) ![Mobile menu trigger hover](components/crops/m-menu-trigger-hover.png) ![Mobile menu trigger focus-visible](components/crops/m-menu-trigger-focus-visible.png) ![Mobile menu trigger pressed](components/crops/m-menu-trigger-pressed.png)

#### Mobile menu (open)
The opened mobile menu panel; pressed once, nothing navigated. Read as `m-nav-panel` on the home page at 390 wide.

**Values (open).** size 390 x 64; background transparent; shadow rgba(23, 23, 23, 0.08) 0px 0px 0px 0px; text sans-serif 12/normal 400, #000000; icon 83 x 29, #0000ee.

![Mobile menu (open) open](components/crops/m-nav-panel-open.png)

#### Mobile hero title
Read as `m-hero-title` on the home page at 390 wide.

**Values (default).** size 358 x 105.59; background transparent; text system-ui 48/52.8 600, #262626 `ink`.

![Mobile hero title default](components/crops/m-hero-title-default.png)

## Icons

28 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Photography and artwork were left out; these are the interface icons (the wordmark, the menu trigger, chevrons, social marks). The SVGs are Aboard's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [icon](icons/icon.svg) | 9x12 |  | fill |  |  |
| [icon-10](icons/icon-10.svg) | 33x30 |  | fill |  |  |
| [icon-11](icons/icon-11.svg) | 32x32 |  | fill |  |  |
| [icon-12](icons/icon-12.svg) | 43x30 |  | fill |  |  |
| [icon-13](icons/icon-13.svg) | 32x32 |  | fill |  |  |
| [icon-14](icons/icon-14.svg) | 24x34 |  | fill |  |  |
| [icon-15](icons/icon-15.svg) | 33x32 |  | fill |  |  |
| [icon-16](icons/icon-16.svg) | 43x43 |  | fill | ; everyday-hr; growth-feedback; team-culture |  |
| [icon-17](icons/icon-17.svg) | 20x20 |  | fill | ; everyday-hr; growth-feedback; team-culture; pricing; whats-new; book-demo; teamtailor-and-aboard; terms |  |
| [icon-18](icons/icon-18.svg) | 32x32 |  | fill | everyday-hr |  |
| [icon-19](icons/icon-19.svg) | 32x31 |  | fill | everyday-hr |  |
| [icon-2](icons/icon-2.svg) | 63x63 |  | fill |  |  |
| [icon-20](icons/icon-20.svg) | 50x61 |  | fill | everyday-hr |  |
| [icon-21](icons/icon-21.svg) | 24x32 |  | fill | everyday-hr |  |
| [icon-22](icons/icon-22.svg) | 62x62 | 0 0 25 25 | fill | growth-feedback |  |
| [icon-23](icons/icon-23.svg) | 63x63 |  | fill | growth-feedback |  |
| [icon-24](icons/icon-24.svg) | 62x62 |  | fill | growth-feedback |  |
| [icon-25](icons/icon-25.svg) | 63x60 |  | fill | team-culture |  |
| [icon-26](icons/icon-26.svg) | 16x23 |  | fill | pricing |  |
| [icon-27](icons/icon-27.svg) | 32x32 |  | fill | pricing |  |
| [icon-3](icons/icon-3.svg) | 29x36 |  | fill |  |  |
| [icon-4](icons/icon-4.svg) | 30x27 |  | fill | ; everyday-hr |  |
| [icon-5](icons/icon-5.svg) | 26x31 |  | fill |  |  |
| [icon-6](icons/icon-6.svg) | 31x31 |  | fill |  |  |
| [icon-7](icons/icon-7.svg) | 32x27 |  | fill |  |  |
| [icon-8](icons/icon-8.svg) | 62x56 |  | fill |  |  |
| [icon-9](icons/icon-9.svg) | 63x61 |  | fill | ; team-culture |  |
| [june-2026-welcoming-new-hires-celebrating-your-team-conn](icons/june-2026-welcoming-new-hires-celebrating-your-team-conn.svg) | 12x12 |  | fill |  | June 2026 — Welcoming new hires, celebrating your team, conn |

## Gaps

### Pages

- **The product app stays out.** app.aboardhr.com (the HR product itself) sits behind a sign-in that was never opened; this package covers the public marketing site only. The co-pilot chat on the home page is a marketing animation, not the app.
- **The Help center is external.** The footer links out to a hosted help centre and to social profiles; outbound pages were not visited.
- **The demo form posts away.** book-a-demo is Framer's form component posting to Framer's endpoint; it was measured at rest and at focus, never submitted.

### States

- **Pressed** was forced with DevTools (`:active`), so a state a script adds on mousedown is missing if one exists. aboardhr.com's Framer stylesheet paints links `#ff0000` under `:active`, which is what the pressed rows show.
- **Focus rings are the browser's.** The site declares no `:focus-visible` style; every ring measured (`#005fcc` 1px offset 1px) is headless Chromium's default, not a product choice.
- **Hover moves are JS.** Framer runs its hovers and reveals in script (spring animations), so CSS transition measurements come back 0s and hover diffs are mostly colour-only.
- **Disabled, error, loading and selected states** were not seen on any public control.

### Themes

aboardhr.com shows one theme: a flat #fafafa ground with pastel card tints and a single blue accent; there is no `prefers-color-scheme` variant and no theme attribute, so the token file ships a single `light` set. The site's design tokens are hashed `--token-<uuid>` custom properties resolved in [raw/css-vars.json](raw/css-vars.json); the token file names them where a leaf aliases one.

### Fonts

- Everything marketing is set in the **OS-ui stack** (`system-ui, -apple-system, ...`): San Francisco on Apple devices, Segoe/Roboto elsewhere. **Inter** appears only inside the book-a-demo form. The @font-face rules are in [raw/css-vars.json](raw/css-vars.json).

### Screenshots

- Photography, illustration and the animated co-pilot demo are Aboard's content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Release-note and legal body copy was not transcribed; only the frames around it were measured.
- No personal data was captured: every page was read signed out, and the only form touched was the demo field measured and left empty.
