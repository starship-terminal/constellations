# Exactly.ai components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from exactly.ai on 2026-11-14, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; Log in, Start for free, Book a demo and every threads.exactly.ai link were measured, never followed; the search was typed into and cleared, never submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (63 components, 128 states). The layout patterns are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (130 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: every captured surface paints the single light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Showcase | `/showcase` | [default](screenshots/showcase-light-default.png), [full](screenshots/showcase-light-full.png) |
| Showcase brand (Revolut) | `/showcase/revolut` | [default](screenshots/showcase-brand-light-default.png), [full](screenshots/showcase-brand-light-full.png) |
| Case studies | `/case-studies` | [default](screenshots/case-studies-light-default.png), [full](screenshots/case-studies-light-full.png) |
| Case-study article (inDrive) | `/case-studies/how-indrive-scales-global-brand-assets-at-the-speed-of-mobility-with-exactly-ai` | [default](screenshots/case-study-light-default.png), [full](screenshots/case-study-light-full.png) |
| Industries | `/industries` | [default](screenshots/industries-light-default.png), [full](screenshots/industries-light-full.png) |
| Industry (SaaS & mobile apps) | `/industries/saas-n-mobile-apps` | [default](screenshots/industry-light-default.png), [full](screenshots/industry-light-full.png) |
| Help center | `/help-center` | [default](screenshots/help-center-light-default.png), [full](screenshots/help-center-light-full.png), [search](screenshots/help-center-light-search.png) |
| Help FAQ article | `/help-center/frequently-asked-questions` | [default](screenshots/help-faq-light-default.png), [full](screenshots/help-faq-light-full.png) |
| Book a demo | `/book-a-demo` | [default](screenshots/book-a-demo-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Framer search modal | /help-center | the Search… field's overlay button — a local UI toggle; text was typed and deleted, never submitted | [help-center-light-search](screenshots/help-center-light-search.png), [search-trigger](#search-trigger), [search-field](#search-field) |
| Mobile nav overlay | home, phone width | the 'Mobile menu toggle' hamburger's own toggle | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [mobile-hamburger](#mobile-hamburger), [drawer-link](#drawer-link) |
| Scheduler cookie line | /book-a-demo | inside the embedded scheduler iframe; hidden, never answered | hidden before every shot and reading |
| Support bubble | every page | the small chat button pinned bottom-right; hidden, never opened | hidden before every shot and reading |
| Signed-in product | threads.exactly.ai | the app sits behind a Cloudflare challenge that was never bypassed | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 18 components were given a real keyboard focus. 18 draw an outline ring: `nav-link` (1px auto #101010, offset 1px), `nav-login` (1px auto #101010, offset 1px), `nav-cta` (1px auto #101010, offset 1px), `hero-cta` (1px auto #101010, offset 1px), `hero-demo` (1px auto #101010, offset 1px), `footer-link` (1px auto #101010, offset 1px), `plan-cta` (1px auto #101010, offset 1px), `plan-demo-cta` (1px auto #101010, offset 1px), `showcase-card` (1px auto #101010, offset 1px), `industry-card` (1px auto #101010, offset 1px), `help-nav-link` (1px auto #101010, offset 1px), `help-card` (1px auto #101010, offset 1px), `article-link` (1px auto #101010, offset 1px), `m-join` (1px auto #e59700, offset 1px), `m-hamburger` (1px auto #e59700, offset 0px), `m-hero-cta` (1px auto #e59700, offset 1px), `m-hero-demo` (1px auto #e59700, offset 1px), `case-read` (1px auto #101010, offset 1px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `cubic-bezier(0.12, 0.23, 0.5, 1)` | color | footer-link |
| 0.2s | `ease-out` | opacity | article-link |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 389.33 x 745 | - | - | transparent | none | 0 |
| [Article-collection card](#article-collection-card) | 640 x 296 | - | 40px | rgba(124, 124, 124, 0.08) `color.palette.warm-08` | none | 40px |
| [Brand card](#brand-card) | 708 x 798.03 | - | - | transparent | none | 0 |
| [Industry card](#industry-card) | 708 x 892 | - | - | transparent | none | 0 |
| [Case-study row](#case-study-row) | 767 x 240 | - | - | transparent | none | 0 |
| [Plan comparison bar](#plan-comparison-bar) | 1344 x 148 | - | - | #ffffff `color.palette.paper` | none | 40px 0px |
| [Mobile top bar](#mobile-top-bar) | 390 x 56 | - | - | transparent | none | 0 |

## Components

### App shell and navigation

The fixed marketing header: exactly.ai wordmark, Industries/Showcase/Case studies/Pricing, Log in and the Start-for-free pill. Over the home photo-hero the header inverts — white text and a white pill; on interior pages it is dark ink and the #fb411f pill.

#### Marketing header
The fixed top bar: exactly.ai wordmark, Industries/Showcase/Case studies/Pricing, Log in and the orange Start-for-free pill. Read as `nav-header` on the home page.

**Values (default).** size 1440 x 68; background transparent; text Inter Variable 14/20 400, #ffffff `color.palette.paper`; icon 24 x 24, #0000ee; layers nav.framer-TqhsX.framer-gd57sn 1440.0x68.0 rgba(255, 255, 255, 0); a.framer-VULEO.framer-BjxQL 122.0x36.0 rgb(255, 255, 255) 1000px.

Child layers that carry the look: nav 1440x68 background rgba(255, 255, 255, 0); a 122x36 background #ffffff `color.palette.paper` radius 1000px.

![Marketing header default](components/crops/nav-header-default.png)

#### Logo
The exactly.ai wordmark in the header; links home. Read as `nav-logo` on the home page.

**Values (default).** size 124 x 24; background transparent; text sans-serif 12/normal 400, #0000ee; icon 24 x 24, #0000ee.

![Logo default](components/crops/nav-logo-default.png)

#### Nav link
A header link (Industries/Showcase/Case studies/Pricing); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 94 x 36; padding 8px 12px; radius 1000px; background transparent; text Inter Variable 14/20 400, #ffffff `color.palette.paper` |
| hover | opacity 0.6 |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-Ozp9V.framer-BjxQL 94.0x36.0 1px auto rgb(16, 16, 16) offset 1px 1000px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log in link
The Log-in link to threads.exactly.ai/signin; measured never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 67 x 36; padding 8px 12px; radius 1000px; background transparent; text Inter Variable 14/20 400, #ffffff `color.palette.paper` |
| hover | opacity 0.6 |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-Ozp9V.framer-BjxQL 67.0x36.0 1px auto rgb(16, 16, 16) offset 1px 1000px |

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Start-for-free pill
The #fb411f orange Start-for-free pill; links to threads.exactly.ai/signin?action=create, measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 122 x 36; padding 8px 16px; radius 1000px; background #ffffff `color.palette.paper`; text Inter Variable 14/20 400, #000000 `color.palette.black` |
| hover | size 115.9 x 34.2; transform scale(0.95); opacity 0.8 |
| focus-visible | outline 1px auto #101010, offset 1px |

![Start-for-free pill default](components/crops/nav-cta-default.png) ![Start-for-free pill hover](components/crops/nav-cta-hover.png) ![Start-for-free pill focus-visible](components/crops/nav-cta-focus-visible.png) ![Start-for-free pill pressed](components/crops/nav-cta-pressed.png)

### Home

The photo-hero home page: the 47px Inter wght-300 display over the photograph, the white Start-for-free and glass Book-a-demo pills, the trusted-by logo wall.

#### Hero headline
"AI automation for your brand's daily creative work." — the display headline over the photo hero. Read as `hero-h1` on the home page.

**Values (default).** size 1424 x 120; background transparent; text Inter 47/60 300, #ffffff `color.palette.paper`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero sub
"Across design, illustration and photography." — the second span inside the hero h1. Read as `hero-sub` on the home page.

**Values (default).** size 888.28 x 57; background transparent; text Inter 47/60 300, rgba(255, 255, 255, 0.6) `color.palette.white-60`.

![Hero sub default](components/crops/hero-sub-default.png)

#### Hero CTA
The white Start-for-free pill over the hero photo; measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 148 x 56; padding 18px 24px; radius 1000px; background #ffffff `color.palette.paper`; text Inter Variable 14/20 400, #1e1e1e `color.palette.ink` |
| hover | size 147.39 x 55.77; transform scale(0.995888) |
| focus-visible | outline 1px auto #101010, offset 1px |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Book-a-demo pill
The translucent Book-a-demo pill beside the hero CTA; links to /book-a-demo, measured never followed. Read as `hero-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 148 x 56; padding 18px 24px; radius 1000px; background rgba(255, 255, 255, 0.1) `color.palette.white-10`; text Inter Variable 14/20 400, #ffffff `color.palette.paper` |
| hover | size 140.6 x 53.2; transform scale(0.95); opacity 0.8 |
| focus-visible | outline 1px auto #101010, offset 1px |

![Book-a-demo pill default](components/crops/hero-demo-default.png) ![Book-a-demo pill hover](components/crops/hero-demo-hover.png) ![Book-a-demo pill focus-visible](components/crops/hero-demo-focus-visible.png) ![Book-a-demo pill pressed](components/crops/hero-demo-pressed.png)

#### Trusted-by line
The "Trusted by the best creative teams and companies, globally" line over the logo wall (UNIQLO, Pentagram, Sony, Glossier, Nike). Read as `trusted-strip` on the home page.

**Values (default).** size 1200 x 20; background transparent; text Inter 14/20 400, #ffffff `color.palette.paper`.

![Trusted-by line default](components/crops/trusted-strip-default.png)

#### Section heading
A marketing section heading further down the home page. Read as `section-h2` on the home page.

**Values (default).** size 1424 x 120; background transparent; text Inter 47/60 300, #1e1e1e `color.palette.ink`.

![Section heading default](components/crops/section-h2-default.png)

### Pricing

The /pricing surface: headline, laurel stats, the 'For free' chip, Pilot/Team/Enterprise plan cards with dark CTAs, the sticky Solo/Team/Enterprise compare bar and the closing FAQ strip.

#### Pricing headline
"Bring AI into your creative work to automate routine tasks." Read as `pricing-h1` on the pricing page.

**Values (default).** size 1440 x 120; background transparent; text Inter 47/60 300, #1e1e1e `color.palette.ink`.

![Pricing headline default](components/crops/pricing-h1-default.png)

#### Plan card
A plan card (Pilot): name chip, price, feature list and its Start-for-free CTA. Read as `plan-card` on the pricing page.

**Values (default).** size 389.33 x 745; background transparent; text Inter 21/32 400, #1e1e1e `color.palette.ink`; icon 60 x 60, #000000 `color.palette.black`; layers a.framer-V0nb0.framer-BjxQL 140.0x56.0 rgb(30, 30, 30) 100px; div.framer-1vzejj9 6.0x6.0 rgb(30, 30, 30) 100%; div.framer-3m782w 6.0x6.0 rgb(30, 30, 30) 100%; div.framer-1xu1f0h 6.0x6.0 rgb(30, 30, 30) 100%; div.framer-qthi04 6.0x6.0 rgb(30, 30, 30) 100%; div.framer-1akdkbf 6.0x6.0 rgb(30, 30, 30) 100%.

Child layers that carry the look: a 140x56 background #1e1e1e `color.palette.ink` radius 100px; div 6x6 background #1e1e1e `color.palette.ink` radius 100%; div 6x6 background #1e1e1e `color.palette.ink` radius 100%.

![Plan card default](components/crops/plan-card-default.png)

#### Plan name
The plan-name label on a card. Read as `plan-name` on the pricing page.

**Values (default).** size 389.33 x 32; background transparent; text Inter 21/32 400, #1e1e1e `color.palette.ink`.

![Plan name default](components/crops/plan-name-default.png)

#### Plan price
"£500 / mo," on the Pilot card. Read as `plan-price` on the pricing page.

**Values (default).** size 389.33 x 64; background transparent; text Inter Variable 21/32 400, rgba(64, 64, 64, 0.6) `color.palette.grey-60`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan feature row
A feature line inside a plan card. Read as `plan-feature` on the pricing page.

**Values (default).** size 365.33 x 20; background transparent; text Inter 14/20 400, #1e1e1e `color.palette.ink`.

![Plan feature row default](components/crops/plan-feature-default.png)

#### Plan CTA
A plan card's Start-for-free action; measured never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 140 x 56; padding 18px 24px; radius 100px; background #1e1e1e `color.palette.ink`; text Inter Variable 14/20 400, #ffffff `color.palette.paper` |
| hover | size 133 x 53.2; transform scale(0.95); opacity 0.9 |
| focus-visible | outline 1px auto #101010, offset 1px |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan Book-a-demo
The dark Book-a-demo action on the enterprise cards; measured never followed. Read as `plan-demo-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 140 x 56; padding 18px 24px; radius 100px; background #1e1e1e `color.palette.ink`; text Inter Variable 14/20 400, #ffffff `color.palette.paper` |
| hover | size 133 x 53.2; transform scale(0.95); opacity 0.9 |
| focus-visible | outline 1px auto #101010, offset 1px |

![Plan Book-a-demo default](components/crops/plan-demo-cta-default.png) ![Plan Book-a-demo hover](components/crops/plan-demo-cta-hover.png) ![Plan Book-a-demo focus-visible](components/crops/plan-demo-cta-focus-visible.png) ![Plan Book-a-demo pressed](components/crops/plan-demo-cta-pressed.png)

#### Plan comparison bar
The sticky Solo/Team/Enterprise bar that pins over the comparison table on scroll. Read as `compare-bar` on the pricing page.

**Values (default).** size 1344 x 148; padding 40px 0px; background #ffffff `color.palette.paper`; text Inter Variable 14/20 400, #1e1e1e `color.palette.ink`.

![Plan comparison bar default](components/crops/compare-bar-default.png)

#### Compare heading
"Compare our plans in detail and find the right fit for your team". Read as `compare-h2` on the pricing page.

**Values (default).** size 1424 x 120; background transparent; text Inter 47/60 300, #1e1e1e `color.palette.ink`.

![Compare heading default](components/crops/compare-h2-default.png)

#### FAQ strip
The "Still have questions? Take a look at our FAQ" closing block. Read as `faq-strip` on the pricing page.

**Values (default).** size 1424 x 120; background transparent; text Inter 47/60 300, #1e1e1e `color.palette.ink`.

![FAQ strip default](components/crops/faq-strip-default.png)

### Showcase and case studies

The /showcase brand gallery, a per-brand page, the /case-studies index and a case-study article.

#### Showcase headline
"Any brand's visual style, mastered. We just get what works." Read as `showcase-h1` on the showcase page.

**Values (default).** size 1424 x 120; background transparent; text Inter 47/60 300, #1e1e1e `color.palette.ink`.

![Showcase headline default](components/crops/showcase-h1-default.png)

#### Category chip
A category tag on a brand card ("Tech"); the card links to /showcase/opal, measured never followed. Read as `showcase-chip` on the showcase page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 35 x 20; background transparent; text Inter Variable 14/20 400, #ffffff `color.palette.paper` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Category chip default](components/crops/showcase-chip-default.png) ![Category chip hover](components/crops/showcase-chip-hover.png) ![Category chip pressed](components/crops/showcase-chip-pressed.png)

#### Brand card
A showcase brand card (cover image, category chip, brand name, tagline, Read more); measured, never followed. Read as `showcase-card` on the showcase page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 708 x 798.03; background transparent; text Inter Variable 14/20 400, #ffffff `color.palette.paper`; icon 23 x 23, #0000ee; layers div.framer-cp81vd 708.0x690.0 rgb(247, 247, 247) 40px; div::after.framer-cp81vd 708pxx690.031px T:1px solid / R:1px solid / B:1px solid / L:1px solid 40px; div.framer-18vbn0f 4.0x4.0 rgb(255, 255, 255) 100px; div.framer-OHYgj.framer-VKc57 64.0x64.0 rgba(255, 255, 255, 0.2) 100px; div::after.framer-OHYgj.framer-VKc57 64pxx64px T:1px solid / R:1px solid / B:1px solid / L:1px solid 100px |
| hover | icon 11.5 x 11.5, #0000ee; layers div.framer-cp81vd 708.0x690.0 rgb(247, 247, 247) 40px; div::after.framer-cp81vd 708pxx690.031px T:1px solid / R:1px solid / B:1px solid / L:1px solid 40px; div.framer-18vbn0f 4.0x4.0 rgb(255, 255, 255) 100px; div.framer-OHYgj.framer-VKc57 138.8x60.0 rgba(255, 255, 255, 0.2) 100px; div::after.framer-OHYgj.framer-VKc57 138.75pxx60px T:1px solid / R:1px solid / B:1px solid / L:1px solid 100px |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-owwqjv.framer-12v43ry 708.0x798.0 1px auto rgb(16, 16, 16) offset 1px; div.framer-cp81vd 708.0x690.0 rgb(247, 247, 247) 40px; div::after.framer-cp81vd 708pxx690.031px T:1px solid / R:1px solid / B:1px solid / L:1px solid 40px; div.framer-18vbn0f 4.0x4.0 rgb(255, 255, 255) 100px; div.framer-OHYgj.framer-VKc57 64.0x64.0 rgba(255, 255, 255, 0.2) 100px; div::after.framer-OHYgj.framer-VKc57 64 |
| pressed | icon 23 x 23, #ff0000 |

Child layers that carry the look: div 708x690 background #f7f7f7 `color.palette.mist` radius 40px; div::after 708pxx690.031px border 1px solid radius 40px; div 4x4 background #ffffff `color.palette.paper` radius 100px.

![Brand card default](components/crops/showcase-card-default.png) ![Brand card hover](components/crops/showcase-card-hover.png) ![Brand card focus-visible](components/crops/showcase-card-focus-visible.png) ![Brand card pressed](components/crops/showcase-card-pressed.png)

#### Brand name
The brand name heading on a showcase card. Read as `showcase-card-title` on the showcase page.

**Values (default).** size 43.48 x 32; background transparent; text Inter Variable 21/32 400, #1e1e1e `color.palette.ink`.

![Brand name default](components/crops/showcase-card-title-default.png)

#### Read-more link
The "Read more" caption link on a brand card; measured, never followed. Read as `read-more` on the showcase page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 37.38 x 10; background transparent; text Inter 14/20 600, #ffffff `color.palette.paper` |
| hover | size 41.16 x 11.01 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Read-more link default](components/crops/read-more-default.png) ![Read-more link hover](components/crops/read-more-hover.png) ![Read-more link pressed](components/crops/read-more-pressed.png)

#### Brand headline
The brand page headline ("Revolut — Change the way you money"). Read as `brand-h1` on the showcase brand page.

**Values (default).** size 1424 x 60; background transparent; text Inter 47/60 300, #1e1e1e `color.palette.ink`.

![Brand headline default](components/crops/brand-h1-default.png)

#### Brand category
The category label on the brand page. Read as `brand-chip` on the showcase brand page.

**Values (default).** size 363.17 x 60; background transparent; text Inter 47/60 300, #ffffff `color.palette.paper`.

![Brand category default](components/crops/brand-chip-default.png)

#### Brand intro
The brand description paragraph. Read as `brand-body` on the showcase brand page.

**Values (default).** size 588 x 224; background transparent; text Inter Variable 22/32 400, #1e1e1e `color.palette.ink`.

![Brand intro default](components/crops/brand-body-default.png)

#### Case-studies headline
The case-studies index headline. Read as `cases-h1` on the case studies page.

**Values (default).** size 1424 x 120; background transparent; text Inter 47/60 300, #1e1e1e `color.palette.ink`.

![Case-studies headline default](components/crops/cases-h1-default.png)

#### Case-study row
A case-study row on the index: brand name, tagline, description, Read-study pill and image. Read as `case-card` on the case studies page.

**Values (default).** size 767 x 240; background transparent; text Inter Variable 21/32 400, #1e1e1e `color.palette.ink`; layers a.framer-RjskD.framer-BjxQL 140.0x56.0 rgba(124, 124, 124, 0.08) 1000px.

Child layers that carry the look: a 140x56 background rgba(124, 124, 124, 0.08) `color.palette.warm-08` radius 1000px.

![Case-study row default](components/crops/case-card-default.png)

#### Article headline
The case-study article headline. Read as `article-h1` on the case-study article page.

**Values (default).** size 1152 x 120; background transparent; text Inter 47/60 300, #1e1e1e `color.palette.ink`.

![Article headline default](components/crops/article-h1-default.png)

#### Article body
A body paragraph in the article prose. Read as `article-body` on the case-study article page.

**Values (default).** size 730.67 x 128; background transparent; text Inter Variable 22/32 400, #1e1e1e `color.palette.ink`.

![Article body default](components/crops/article-body-default.png)

#### Article quote
A pull quote or stat line inside the article, where the page carries one. Read as `article-quote` on the case-study article page.

Not on the page when it was captured.

#### Read-study pill
The "Read study" pill on a case-study row — the outer anchor that paints the grey fill, not the text box inside it; measured, never followed. Read as `case-read` on the case studies page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 140 x 56; padding 18px 24px; radius 1000px; background rgba(124, 124, 124, 0.08) `color.palette.warm-08`; text Inter Variable 14/20 400, #1e1e1e `color.palette.ink` |
| hover | size 133 x 53.2; transform scale(0.95); opacity 0.8 |
| focus-visible | outline 1px auto #101010, offset 1px |

![Read-study pill default](components/crops/case-read-default.png) ![Read-study pill hover](components/crops/case-read-hover.png) ![Read-study pill focus-visible](components/crops/case-read-focus-visible.png) ![Read-study pill pressed](components/crops/case-read-pressed.png)

#### Article heading
A section heading inside the article. Read as `article-h2` on the case-study article page.

**Values (default).** size 730.67 x 88; background transparent; text Inter Variable 32/44 400, #1e1e1e `color.palette.ink`.

![Article heading default](components/crops/article-h2-default.png)

### Industries

The /industries index and a per-industry page.

#### Industries headline
The industries index headline. Read as `industries-h1` on the industries page.

**Values (default).** size 1424 x 120; background transparent; text Inter 47/60 300, #1e1e1e `color.palette.ink`.

![Industries headline default](components/crops/industries-h1-default.png)

#### Industry card
An industry card on the index; measured, never followed. Read as `industry-card` on the industries page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 708 x 892; background transparent; text Inter 14/20 600, #ffffff `color.palette.paper`; icon 20 x 20, #0000ee; layers div.framer-ij66mj 708.0x708.0 rgb(247, 247, 247) 32px; div::after.framer-ij66mj 708pxx708px T:1px solid / R:1px solid / B:1px solid / L:1px solid 32px; div.framer-OHYgj.framer-VKc57 52.0x52.0 rgba(255, 255, 255, 0.2) 100px; div::after.framer-OHYgj.framer-VKc57 52pxx52px T:1px solid / R:1px solid / B:1px solid / L:1px solid 100px |
| hover | icon 11.5 x 11.5, #0000ee; layers div.framer-ij66mj 708.0x708.0 rgb(247, 247, 247) 32px; div::after.framer-ij66mj 708pxx708px T:1px solid / R:1px solid / B:1px solid / L:1px solid 32px; div.framer-OHYgj.framer-VKc57 138.8x60.0 rgba(255, 255, 255, 0.2) 100px; div::after.framer-OHYgj.framer-VKc57 138.75pxx60px T:1px solid / R:1px solid / B:1px solid / L:1px solid 100px |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-bP7zE.framer-WHDvl 708.0x892.0 1px auto rgb(16, 16, 16) offset 1px; div.framer-ij66mj 708.0x708.0 rgb(247, 247, 247) 32px; div::after.framer-ij66mj 708pxx708px T:1px solid / R:1px solid / B:1px solid / L:1px solid 32px; div.framer-OHYgj.framer-VKc57 52.0x52.0 rgba(255, 255, 255, 0.2) 100px; div::after.framer-OHYgj.framer-VKc57 52pxx52px T:1px solid / R:1px solid / B:1px solid / L:1px soli |
| pressed | icon 20 x 20, #ff0000 |

Child layers that carry the look: div 708x708 background #f7f7f7 `color.palette.mist` radius 32px; div::after 708pxx708px border 1px solid radius 32px; div 52x52 background rgba(255, 255, 255, 0.2) `color.palette.white-20` radius 100px.

![Industry card default](components/crops/industry-card-default.png) ![Industry card hover](components/crops/industry-card-hover.png) ![Industry card focus-visible](components/crops/industry-card-focus-visible.png) ![Industry card pressed](components/crops/industry-card-pressed.png)

#### Industry headline
The industry page headline. Read as `industry-h1` on the industry page.

**Values (default).** size 1408 x 120; background transparent; text Inter 47/60 300, #1e1e1e `color.palette.ink`.

![Industry headline default](components/crops/industry-h1-default.png)

#### Industry body
A body paragraph on the industry page. Read as `industry-body` on the industry page.

**Values (default).** size 640 x 40; background transparent; text Inter Variable 14/20 400, rgba(64, 64, 64, 0.48) `color.palette.grey-48`.

![Industry body default](components/crops/industry-body-default.png)

### Help center

The doc-style /help-center: the left rail of article links, the Search… trigger that opens Framer's search modal, collection cards, and the FAQ article's anchor-linked questions.

#### Help sidebar
The left doc rail: Getting started, AI style transfer, Library and more groups of article links. Read as `help-sidebar` on the help center page.

**Values (default).** size 240 x 1560; padding 240px 24px 24px 24px; background transparent; text Inter Variable 14/20 400, #1e1e1e `color.palette.ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Nav group label
A sidebar group label ("Getting started"). Read as `help-nav-group` on the help center page.

**Values (default).** size 106 x 28; background transparent; text Inter Variable 14/20 400, #1e1e1e `color.palette.ink`.

![Nav group label default](components/crops/help-nav-group-default.png)

#### Sidebar link
A sidebar article link; measured, never followed. Read as `help-nav-link` on the help center page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 86 x 32; padding 6px 0px 6px 24px; radius 1000px; background transparent; text Inter 14/20 400, #1e1e1e `color.palette.ink` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-t2H42.framer-siwSQ 86.0x32.0 1px auto rgb(16, 16, 16) offset 1px 1000px |

![Sidebar link default](components/crops/help-nav-link-default.png) ![Sidebar link hover](components/crops/help-nav-link-hover.png) ![Sidebar link focus-visible](components/crops/help-nav-link-focus-visible.png) ![Sidebar link pressed](components/crops/help-nav-link-pressed.png)

#### Help headline
"Help center". Read as `help-h1` on the help center page.

**Values (default).** size 640 x 60; background transparent; text Inter 47/60 300, #1e1e1e `color.palette.ink`.

![Help headline default](components/crops/help-h1-default.png)

#### Search trigger
The "Search…" affordance on the help landing: a rounded field that opens the Framer search modal when its overlay button is clicked (a local UI toggle). Read as `help-search` on the help center page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 640 x 52; background transparent; text Inter 14/20 400, rgba(64, 64, 64, 0.48) `color.palette.grey-48`; layers div.framer-6tgDK.framer-siwSQ 640.0x52.0 rgba(124, 124, 124, 0.08) 32px; div.framer-i4x7f7 15.0x15.0 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 640x52 background rgba(124, 124, 124, 0.08) `color.palette.warm-08` radius 32px; div 15x15 image url(data:…)%22></path></svg>").

![Search trigger default](components/crops/help-search-default.png) ![Search trigger hover](components/crops/help-search-hover.png) ![Search trigger pressed](components/crops/help-search-pressed.png)

#### Search field
The real input inside the Framer search modal; focused and typed into then cleared — never submitted. Read as `help-search-input` on the help center page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 348 x 32; background transparent; text Inter 16/32 400, #1e1e1e `color.palette.ink`; placeholder rgba(0, 0, 0, 0.4) |
| filled | size 316 x 32 |

![Search field default](components/crops/help-search-input-default.png) ![Search field focused](components/crops/help-search-input-focused.png) ![Search field filled](components/crops/help-search-input-filled.png)

#### Article-collection card
A collection card ("FAQ — Get quick answers — 12 articles"); measured, never followed. Read as `help-card` on the help center page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 640 x 296; padding 40px; radius 40px; background rgba(124, 124, 124, 0.08) `color.palette.warm-08`; text Inter 21/32 400, #1e1e1e `color.palette.ink` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Article-collection card default](components/crops/help-card-default.png) ![Article-collection card hover](components/crops/help-card-hover.png) ![Article-collection card focus-visible](components/crops/help-card-focus-visible.png) ![Article-collection card pressed](components/crops/help-card-pressed.png)

#### FAQ headline
"Frequently asked questions" — the FAQ article page. Read as `faq-h1` on the help FAQ page.

**Values (default).** size 640 x 60; background transparent; text Inter 47/60 300, #1e1e1e `color.palette.ink`.

![FAQ headline default](components/crops/faq-h1-default.png)

#### FAQ question
An anchor-linked question heading inside the FAQ article (H3). Read as `faq-question` on the help FAQ page.

**Values (default).** size 640 x 32; background transparent; text Inter Variable 22/32 400, #1e1e1e `color.palette.ink`.

![FAQ question default](components/crops/faq-question-default.png)

#### FAQ answer
The answer paragraph under a question heading. Read as `faq-answer` on the help FAQ page.

**Values (default).** size 640 x 64; background transparent; text Inter Variable 22/32 400, #1e1e1e `color.palette.ink`.

![FAQ answer default](components/crops/faq-answer-default.png)

#### Inline link
The "Data protection & privacy" link inside the FAQ article prose (the #help-center-rich-text body); measured, never followed. Read as `article-link` on the help FAQ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 292.41 x 26; background transparent; text Inter Variable 22/32 400, #1e1e1e `color.palette.ink`; transition opacity 0.2s ease-out |
| hover | opacity 0.7 |
| focus-visible | outline 1px auto #101010, offset 1px; layers a 292.4x26.0 1px auto rgb(16, 16, 16) offset 1px |

![Inline link default](components/crops/article-link-default.png) ![Inline link hover](components/crops/article-link-hover.png) ![Inline link focus-visible](components/crops/article-link-focus-visible.png) ![Inline link pressed](components/crops/article-link-pressed.png)

### Book a demo

The /book-a-demo page: headline and the embedded scheduler, measured at rest — no day, time or contact detail was ever picked or typed.

#### Demo headline
"See how exactly.ai works. Let us help you scale your creative processes." Read as `demo-h1` on the book-a-demo page.

**Values (default).** size 1440 x 180; background transparent; text Inter 47/60 300, #1e1e1e `color.palette.ink`.

![Demo headline default](components/crops/demo-h1-default.png)

#### Scheduler embed
The embedded scheduling widget (a Calendly-style day picker in a srcdoc iframe): measured as a region at rest — no day, time or contact detail was ever picked or typed. Read as `demo-scheduler` on the book-a-demo page.

**Values (default).** size 1440 x 600; background transparent; text sans-serif 12/normal 400, #000000 `color.palette.black`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Mobile (390 wide)

The phone surface at 390 wide: the top bar with Join pill, the hamburger and its nav overlay, the hero at 27px.

#### Mobile top bar
The phone top bar: exactly.ai wordmark, Join pill, hamburger. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 390 x 56; background transparent; text Inter Variable 14/20 400, #1e1e1e `color.palette.ink`; icon 86 x 24, #0000ee; layers nav.framer-TqhsX.framer-gd57sn 390.0x56.0 rgba(255, 255, 255, 0); div.framer-194xxwj 28.0x2.0 rgb(255, 255, 255); div.framer-1713bdv 28.0x2.0 rgb(255, 255, 255); a.framer-VULEO.framer-BjxQL 55.0x32.0 rgb(255, 255, 255) 1000px.

Child layers that carry the look: nav 390x56 background rgba(255, 255, 255, 0); div 28x2 background #ffffff `color.palette.paper`; div 28x2 background #ffffff `color.palette.paper`.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Join pill
The white Join pill in the phone top bar; measured never followed. Read as `m-join` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 55 x 32; padding 6px 12px; radius 1000px; background #ffffff `color.palette.paper`; text Inter Variable 14/20 400, #1e1e1e `color.palette.ink` |
| hover | size 52.25 x 30.4; transform scale(0.95) |
| focus-visible | outline 1px auto #e59700, offset 1px |

![Join pill default](components/crops/m-join-default.png) ![Join pill hover](components/crops/m-join-hover.png) ![Join pill focus-visible](components/crops/m-join-focus-visible.png) ![Join pill pressed](components/crops/m-join-pressed.png)

#### Mobile hamburger
The burger that opens the phone nav overlay — a local UI toggle; the opened state was measured after tapping it. Read as `m-hamburger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 32; background transparent; text sans-serif 12/normal 400, #000000 `color.palette.black`; layers div.framer-194xxwj 28.0x2.0 rgb(255, 255, 255); div.framer-1713bdv 28.0x2.0 rgb(255, 255, 255) |
| focus-visible | outline 1px auto #e59700, offset 0px; layers div.framer-1dourkh 32.0x32.0 1px auto rgb(229, 151, 0) offset 0px; div.framer-194xxwj 28.0x2.0 rgb(255, 255, 255); div.framer-1713bdv 28.0x2.0 rgb(255, 255, 255) |
| opened | layers div.framer-194xxwj 18.4x18.4 rgb(30, 30, 30); div.framer-1713bdv 18.4x18.4 rgb(30, 30, 30) |

Child layers that carry the look: div 28x2 background #ffffff `color.palette.paper`; div 28x2 background #ffffff `color.palette.paper`.

![Mobile hamburger default](components/crops/m-hamburger-default.png) ![Mobile hamburger hover](components/crops/m-hamburger-hover.png) ![Mobile hamburger focus-visible](components/crops/m-hamburger-focus-visible.png) ![Mobile hamburger pressed](components/crops/m-hamburger-pressed.png) ![Mobile hamburger opened](components/crops/m-hamburger-opened.png)

#### Drawer link
A nav link inside the opened overlay; measured, never followed. Read as `m-drawer-link` on the home page at 390 wide.

**Values (default).** size 350 x 32; padding 4px 16px; radius 1000px; background transparent; text Inter 17/24 400, #1e1e1e `color.palette.ink`.

![Drawer link default](components/crops/m-drawer-link-default.png)

#### Mobile hero headline
The hero display at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 374 x 144; background transparent; text Inter 27/36 300, #ffffff `color.palette.paper`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The white Start-for-free pill over the phone hero; measured never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 132 x 56; padding 18px 24px; radius 1000px; background #ffffff `color.palette.paper`; text Inter Variable 14/20 400, #1e1e1e `color.palette.ink` |
| focus-visible | outline 1px auto #e59700, offset 1px |

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

#### Mobile demo pill
The translucent Book-a-demo pill on the phone hero; measured never followed. Read as `m-hero-demo` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 132 x 56; padding 18px 24px; radius 1000px; background rgba(255, 255, 255, 0.1) `color.palette.white-10`; text Inter Variable 14/20 400, #ffffff `color.palette.paper` |
| focus-visible | outline 1px auto #e59700, offset 1px |

![Mobile demo pill default](components/crops/m-hero-demo-default.png) ![Mobile demo pill hover](components/crops/m-hero-demo-hover.png) ![Mobile demo pill focus-visible](components/crops/m-hero-demo-focus-visible.png) ![Mobile demo pill pressed](components/crops/m-hero-demo-pressed.png)

### Footer

The near-black footer: link columns, the watermark wordmark and the copyright line.

#### Footer
The near-black footer: Follow/Company/Industries/Policies link columns, a watermark exactly.ai wordmark and the © line. Read as `footer` on the home page.

**Values (default).** size 1440 x 952; padding 328px 8px 160px 8px; background transparent; text Inter Variable 21/32 400, rgba(255, 255, 255, 0.6) `color.palette.white-60`.

![Footer default](components/crops/footer-default.png)

#### Footer column label
A column heading in the footer ("Policies"). Read as `footer-col` on the home page.

**Values (default).** size 69.64 x 32; background transparent; text Inter Variable 21/32 400, rgba(255, 255, 255, 0.6) `color.palette.white-60`.

![Footer column label default](components/crops/footer-col-default.png)

#### Footer link
A legal link in the footer; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 260.09 x 25; background transparent; text Inter Variable 21/32 400, #ffffff `color.palette.paper`; transition color 0.2s cubic-bezier(0.12, 0.23, 0.5, 1) |
| hover | text Inter Variable 21/32 400, rgba(255, 255, 255, 0.6) `color.palette.white-60` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-text.framer-styles-preset-lqmk1b 260.1x25.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Inter Variable 21/32 400, rgba(255, 255, 255, 0.6) `color.palette.white-60` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

## Icons

15 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv): the exactly.ai mark and wordmark in both their on-image (white) and on-light (dark) paint, the plan-card glyphs, the laurel flourishes, the search magnifier, the list dots and the plus markers. Framer ships most artwork as `<use>` references into a shared sprite; each file holds the resolved geometry. Partner logos in the trusted-by strip are the customers' artwork and were left out. The SVGs are Exactly.ai's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [logo-on-image](icons/logo-on-image.svg) | 24x24 | 0 0 24 24 | inline | home | Logo |
| [wordmark-on-image](icons/wordmark-on-image.svg) | 86x24 | 0 0 85.383 24 | inline | home | LogoText |
| [laurel-left](icons/laurel-left.svg) | 28x56 | 0 0 27.98 56 | inline | home, mobile-home, pricing | Section Header/Buttons |
| [laurel-right](icons/laurel-right.svg) | 28x56 | 0 0 27.98 56 | inline | home, mobile-home, pricing | Section Header/Buttons |
| [plan-glyph-1](icons/plan-glyph-1.svg) | 60x60 | 0 0 60 60 | inline | home, mobile-home, pricing | Icon |
| [plan-glyph-2](icons/plan-glyph-2.svg) | 64x64 | 0 0 64 64 | inline | home, mobile-home, pricing | Icon |
| [plan-glyph-3](icons/plan-glyph-3.svg) | 63x63 | 0 0 63 63 | inline | home, mobile-home, pricing | Icon |
| [dot](icons/dot.svg) | 6x6 | 0 0 6 6 | background data-URI | home | Dot |
| [logo-on-light](icons/logo-on-light.svg) | 24x24 | 0 0 24 24 | inline | book-a-demo, case-studies, help-center, help-center-frequently-asked-questions, industries, pricing, showcase | Logo |
| [wordmark-on-light](icons/wordmark-on-light.svg) | 86x24 | 0 0 85.383 24 | inline | book-a-demo, case-studies, help-center, help-center-frequently-asked-questions, industries, mobile-home, pricing, showcase | LogoText; LogoWrap |
| [plus](icons/plus.svg) | 23x23 | 0 0 22.403 22.4 | inline | pricing, showcase | Plus |
| [plus-c1cd28e8](icons/plus-c1cd28e8.svg) | 23x23 | 0 0 22.403 22.4 | inline | pricing | Plus |
| [desktop](icons/desktop.svg) | 91x16 | 0 0 90.667 16 | background data-URI | pricing | Desktop |
| [plus-d7dee377](icons/plus-d7dee377.svg) | 20x20 | 0 0 19.914 19.911 | inline | industries | Plus |
| [search](icons/search.svg) | 15x15 | 0 0 15.068 15.067 | background data-URI | help-center, help-center-frequently-asked-questions | Search |

## Gaps

### The signed-in product

The 2026-11-14 headless capture stopped at a Cloudflare check on threads.exactly.ai. The 2026-11-21 signed-in pass got past that check and stopped on the unanswered audience step. The studio, model training, the image generator, credits, billing and settings are still not evidence. The shell that was visible is in [screenshots/onboarding-light-default.png](screenshots/onboarding-light-default.png) and [screenshots/onboarding-mobile-light-default.png](screenshots/onboarding-mobile-light-default.png).

### Pages

- **The app.** The 2026-11-21 pass captured the onboarding audience step and did not answer it. The canvas, datasets, models, credits, billing and settings stay behind that step. The 2026-11-14 public capture measured Log in and Start for free and did not follow them.
- **The scheduler.** The /book-a-demo calendar was measured at rest; no day, time or contact detail was ever picked or typed, so its interactive states are uncaptured.
- **The help search results.** The modal was opened and typed into, but result rows were never clicked.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover) on every control, so a state a script adds on mousedown (if any) is missing. Links' pressed colour is the browser's own :active paint, not a site value.
- **Disabled, error and loading states** were not seen on the public surface.
- **Hover on links** mostly repaints nothing the computed styles can see: exactly.ai's link hovers are Framer variants on child layers, and several anchors' own `color` stays the browser default while the painted text inside carries the real colour — each entry's Text node row shows the painted value.

### Themes

Exactly.ai paints one light theme on every signed-out surface. Its stylesheets carry a single `prefers-color-scheme: dark` media rule that repaints nothing, and no page sets a dark attribute. The token file therefore ships core and light only; no dark set was invented.

### Fonts

- **Inter** (the wght-300 display and article/help prose) and **Inter Variable** (nav, CTAs, card titles, footer) are loaded from Google Fonts; the style guide falls back to system sans.

### Screenshots

- The brand photography, showcase covers, laurel artwork and the customers' logos in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The generated-image examples, brand marks and article prose are the product's content; only frames and components were measured.
