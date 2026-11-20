# FlowMapp components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from www.flowmapp.com and app.flowmapp.com on 2026-11-15, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the sign-in, sign-up, restore and contact forms were never sent; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (71 components, 189 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value in the component's own surface set (light / app — the two hosts declare separate vocabularies), when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/24 500, #131e40`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (184 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the surface painted at capture: `light` for every page — www.flowmapp.com and app.flowmapp.com are light-only (no theme toggle, no dark media query on any signed-out route). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [features-menu](screenshots/home-light-features-menu.png), [full](screenshots/home-light-full.png) |
| Pricing | `/pricing` | [billed-monthly](screenshots/pricing-light-billed-monthly.png), [default](screenshots/pricing-light-default.png), [faq-open](screenshots/pricing-light-faq-open.png), [full](screenshots/pricing-light-full.png) |
| Product overview | `/product-overview` | [default](screenshots/product-overview-light-default.png), [full](screenshots/product-overview-light-full.png) |
| Sitemap feature | `/features/sitemap` | [default](screenshots/feature-sitemap-light-default.png), [full](screenshots/feature-sitemap-light-full.png) |
| User flow feature | `/features/userflow` | [default](screenshots/feature-userflow-light-default.png), [full](screenshots/feature-userflow-light-full.png) |
| Wireframes feature | `/features/wireframes` | [default](screenshots/feature-wireframes-light-default.png), [full](screenshots/feature-wireframes-light-full.png) |
| Use case | `/features/use-case-boost-website-sales` | [default](screenshots/use-case-light-default.png), [full](screenshots/use-case-light-full.png) |
| Reviews | `/reviews` | [default](screenshots/reviews-light-default.png), [full](screenshots/reviews-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Blog article | `/blog/articles/13-startups-focused-on-clean-ui` | [default](screenshots/blog-article-light-default.png), [full](screenshots/blog-article-light-full.png) |
| Security | `/security` | [default](screenshots/security-light-default.png), [full](screenshots/security-light-full.png) |
| Privacy | `/privacy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Terms | `/terms` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| Contact | `/contact-us` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Sitemap generator | `/sitemap-generator` | [default](screenshots/sitemap-generator-light-default.png), [full](screenshots/sitemap-generator-light-full.png) |
| App sign-in | `app.flowmapp.com/signin` | [default](screenshots/login-light-default.png) |
| App sign-up | `app.flowmapp.com/signup` | [default](screenshots/signup-light-default.png) |
| App restore | `app.flowmapp.com/restore` | [default](screenshots/restore-light-default.png) |
| Shared project | `app.flowmapp.com/share/projects/215285` | [default](screenshots/share-project-light-default.png), [full](screenshots/share-project-light-full.png) |
| Shared sitemap viewer | `app.flowmapp.com/share/projects/215285/sitemap/<id>` | [default](screenshots/share-sitemap-light-default.png), [demo-menu](screenshots/share-sitemap-light-demo-menu.png), [estimation](screenshots/share-sitemap-light-estimation.png), [structure-back](screenshots/share-sitemap-light-structure-back.png) |
| Shared user-flow viewer | `app.flowmapp.com/share/projects/215285/userflow/<id>` | [default](screenshots/share-userflow-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Shared sitemap, phone | `app.flowmapp.com/share/projects/215285/sitemap/<id>` | [default](screenshots/mobile-share-sitemap-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Consent overlay | every page | no consent banner was observed on either host; any layer would be hidden, never answered | hidden before every shot and reading |
| Features flyout | marketing header | hovered the 'Features' nav trigger to open .nav__pop-wrap | [home-light-features-menu](screenshots/home-light-features-menu.png), [nav-features](#features-nav-trigger), [nav-pop-item](#features-flyout-item) |
| Billing tabs | pricing | clicked 'Billed monthly' — a local UI toggle | [pricing-light-billed-monthly](screenshots/pricing-light-billed-monthly.png), [ptab-monthly](#billing-tab-monthly), [ptab-annual](#billing-tab-annual) |
| Pricing FAQ | pricing | clicked a .faq__q-wrap disclosure row | [pricing-light-faq-open](screenshots/pricing-light-faq-open.png), [faq-q](#faq-disclosure), [faq-a](#faq-answer) |
| Mobile menu | home, phone width | tapped the nav burger | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-burger](#mobile-burger), [m-menu-link](#mobile-menu-link) |
| Demo project dropdown | share viewer | clicked the 'Demo Project' ant-dropdown trigger | [share-sitemap-light-demo-menu](screenshots/share-sitemap-light-demo-menu.png), [sh-menu](#project-dropdown) |
| Estimation tab | share viewer | clicked the 'Estimation' toolbar tab | [share-sitemap-light-estimation](screenshots/share-sitemap-light-estimation.png), [sh-tab-estimation](#estimation-tab) |
| Auth fields | app.flowmapp.com | typed into then cleared — nothing sent; the sign-in submit's enabled fill was measured with sample text in both fields, never clicked | [login-field](#email-field-sign-in), [login-submit](#sign-in-submit) |
| Signed-in product | a FlowMapp account | every post-login surface (the editor workspaces, dashboards, billing) needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 26 components were given a real keyboard focus. 10 draw an outline ring: `login-google` (1px auto #101010, offset 0px), `signup-submit` (1px auto #101010, offset 0px), `signup-google` (1px auto #101010, offset 0px), `sh-menu` (1px auto #101010, offset 0px), `sh-tab-structure` (1px auto #101010, offset 0px), `sh-tab-estimation` (1px auto #101010, offset 0px), `sh-login-btn` (1px auto #101010, offset 0px), `sh-signup-btn` (1px auto #101010, offset 0px), `sh-zoom` (1px auto #101010, offset 0px), `sh-help` (1px auto #101010, offset 0px). The other 16 show no measured change: `nav-link`, `nav-demo`, `nav-login`, `nav-cta`, `hero-cta`, `ptab-monthly`, `ptab-annual`, `plan-cta`, `feat-cta`, `contact-submit`, `login-forgot`, `login-signup`, `restore-back`, `sh-toolbar-btn`, `m-burger`, `m-hero-cta`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease-in-out` | opacity | sh-card |
| 0.3s | `ease` | background-color, border-color, color | feat-cta, login-forgot, login-signup, m-menu-link, nav-cta, nav-demo, nav-features, nav-link and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Home card](#home-card) | 386.66 x 518 | 3px solid #0050ff `apps.charts.chart.1.default` | 32px | transparent | none | 24px |
| [Plan card](#plan-card) | 305 x 435.09 | - | 24px | #ffffff `apps.colors.card.default` | none | 24px |
| [Paid plan card](#paid-plan-card) | 305 x 435.09 | - | 24px | #000000 `apps.colors.foreground.default` | none | 24px |
| [Feature card](#feature-card) | 1060 x 776.88 | - | - | transparent | none | 0 |
| [Sign-in card](#sign-in-card) | 440 x 640 | - | - | transparent | none | 0 |
| [Sitemap page card](#sitemap-page-card) | 95.07 x 104.35 | 2px solid #1f1f1f `primary.basic.gray.default` | 16px | #ffffff `apps.colors.card.default` | none | 0 |
| [User-flow card](#user-flow-card) | 139.22 x 191.43 | - | - | transparent | none | 0 |
| [Sign-up nudge](#sign-up-nudge) | 251.58 x 80 | - | 14px | rgba(0, 0, 0, 0.56) `surface.popup` | none | 16px 20px |
| [Contact field](#contact-field) | 492 x 50.08 | B: 2px solid #cbd8e5 `light.steel.blue` | - | #ffffff `apps.colors.card.default` | none | 8px 0px |
| [Mobile menu link](#mobile-menu-link) | 348.53 x 47.7 | - | 8px | transparent | none | 11.388px 14.508px |

## Components

### Site chrome

The header on every marketing page: the FlowMapp wordmark, 'Try Demo Project', the Features flyout, Use cases, Pricing, Help and Blog links, 'Log in' and the black 'Try for free' pill.

#### Site header
The marketing top bar: wordmark, "Try Demo Project", Features and Use cases dropdowns, Pricing, Help, Blog, "Log in" and the "Try for free" pill. Read as `mkt-header` on the home page.

**Values (default).** size 1416 x 82.06; padding 12px 0px 0px 0px; background transparent; text Inter 16/22.4 400, #000000 `apps.colors.foreground.default`; icon 16 x 16, #ffffff `apps.colors.card.default`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1; div.container.nav-cont__is-br-12--is-sh-img 1416.0x70.1 rgba(255, 255, 255, 0.8) rgba(120, 124, 132, 0.19) -9.92904px 11.043px 59.7576px 0px 12px; div.nav__link-underline 121.8x23.4 B:1px rgb(140, 155, 170); div.nav__pop.is-sh-l--is-bg-wh--is-br-12--is-t-sh-0 377.0x490.5 rgb(255, 255, 255) rgba(151, 169, 187, 0.58) 0px 8px .

Child layers that carry the look: div 1416x70.1 background rgba(255, 255, 255, 0.8) radius 12px shadow rgba(120, 124, 132, 0.19) -9.92904px 11.043px 59.7576px 0px; div 121.8x23.4 border 1px #8c9baa `service.grey`; div 377x490.5 background #ffffff `apps.colors.card.default` radius 12px shadow rgba(151, 169, 187, 0.58) 0px 8px 10px 0px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The FlowMapp wordmark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 136.95 x 32.98; background transparent; text Inter 14/20 400, #333333.

![Logo default](components/crops/mkt-logo-default.png)

#### Nav link
A marketing header nav link (Pricing); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 76.69 x 44.47; padding 11.04px 14.08px; radius 8px; background transparent; text Inter 16/22.4 600, #222222 `text.muted`; transition background-color 0.3s ease |
| hover, pressed | background #f6f8fa `apps.colors.background.default` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Features nav trigger
The "Features" nav item that opens the .nav__pop-wrap flyout on hover (Sitemap, User flow, Wireframes, Content, Estimation & invoice…). Read as `nav-features` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 109.05 x 44.47; padding 11.04px 14.08px; radius 8px; background transparent; text Inter 16/22.4 600, #000000 `apps.colors.foreground.default`; transition background-color 0.3s ease; layers div.nav__pop.is-sh-l--is-bg-wh--is-br-12--is-t-sh-0 377.0x490.5 rgb(255, 255, 255) rgba(151, 169, 187, 0.58) 0px 8px 10px 0px 12px |
| hover, pressed | background #f6f8fa `apps.colors.background.default`; layers none |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 377x490.5 background #ffffff `apps.colors.card.default` radius 12px shadow rgba(151, 169, 187, 0.58) 0px 8px 10px 0px.

![Features nav trigger default](components/crops/nav-features-default.png) ![Features nav trigger hover](components/crops/nav-features-hover.png) ![Features nav trigger pressed](components/crops/nav-features-pressed.png) ![Features nav trigger opened](components/crops/nav-features-opened.png)

#### Features flyout item
A row inside the opened Features flyout (icon, name, one-line description); measured while the flyout was held open by hover. Read as `nav-pop-item` on the home page.

**Values (default).** size 353 x 93.3; padding 12px; radius 8px; background transparent; text Inter 16/22.4 600, #000000 `apps.colors.foreground.default`; transition background-color 0.3s ease.

![Features flyout item default](components/crops/nav-pop-item-default.png)

#### Try Demo Project link
The header link to the published read-only demo project on app.flowmapp.com; measured, never followed. Read as `nav-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 177.92 x 46.06; padding 11.04px 14.08px; radius 8px; background transparent; text Inter 16/22.4 600, #000000 `apps.colors.foreground.default`; transition background-color 0.3s ease; layers div.nav__link-underline 121.8x23.4 B:1px rgb(140, 155, 170) |
| hover, pressed | background #f6f8fa `apps.colors.background.default`; layers none |

Child layers that carry the look: div 121.8x23.4 border 1px #8c9baa `service.grey`.

![Try Demo Project link default](components/crops/nav-demo-default.png) ![Try Demo Project link hover](components/crops/nav-demo-hover.png) ![Try Demo Project link focus-visible](components/crops/nav-demo-focus-visible.png) ![Try Demo Project link pressed](components/crops/nav-demo-pressed.png)

#### Log in link
The "Log in" nav action to app.flowmapp.com/signin; measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 77.17 x 38.47; padding 7.04px 16px; border 1px solid rgba(0, 0, 0, 0.1); radius 12px; background transparent; text Inter 16/22.4 600, #000000 `apps.colors.foreground.default`; transition color 0.3s ease, background-color 0.3s ease |
| hover, pressed | background #000000 `apps.colors.foreground.default`; text Inter 16/22.4 600, #ffffff `apps.colors.card.default` |

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Try for free pill
The black "Try for free" header pill to app.flowmapp.com/signup; measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 127.31 x 38.47; padding 7.04px 10.08px 7.04px 16px; border 1px solid #000000 `apps.colors.foreground.default`; radius 12px; background #000000 `apps.colors.foreground.default`; text Inter 16/22.4 600, #ffffff `apps.colors.card.default`; transition border-color 0.3s ease, color 0.3s ease, background-color 0.3s ease; icon 16 x 16, #ffffff `apps.colors.card.default` |
| hover, pressed | border 1px solid #cbd8e5 `light.steel.blue`; background transparent; text Inter 16/22.4 600, #000000 `apps.colors.foreground.default` |

![Try for free pill default](components/crops/nav-cta-default.png) ![Try for free pill hover](components/crops/nav-cta-hover.png) ![Try for free pill focus-visible](components/crops/nav-cta-focus-visible.png) ![Try for free pill pressed](components/crops/nav-cta-pressed.png)

### Home

The light home page: the 72px 'Visual platform for planning UX and pitching web design' masthead over the 'Over 400,000 users' trust line, the giant dodger-blue 'Start planning' pill with its translucent halo, client marks and feature cards.

#### Hero eyebrow
The "Over 400,000 users" trust line above the hero heading. Read as `hero-eyebrow` on the home page.

**Values (default).** size 237 x 16.8; background transparent; text Inter 12/16.8 500, #000000 `apps.colors.foreground.default`.

![Hero eyebrow default](components/crops/hero-eyebrow-default.png)

#### Hero headline
"Visual platform for planning UX and pitching web design" — the display heading. Read as `hero-h1` on the home page.

**Values (default).** size 1280 x 216; padding 0px 240px; background transparent; text Inter 72/72 700, #000000 `apps.colors.foreground.default`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero CTA
The hero "Start planning" button (blue pill with the squiggle arrow); measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 477.91 x 120.06; padding 12px; radius 1600px; background rgba(0, 128, 255, 0.2) `dodger.blue.20`; text Inter 30/42 600, #ffffff `apps.colors.card.default`; icon 97.59 x 20.53, #ffffff `apps.colors.card.default` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Avatar cluster
The stacked-user avatar cluster beside the trust line. Read as `hero-avatars` on the home page.

**Values (default).** size 237 x 34; background transparent; text Inter 14/20 400, #000000 `apps.colors.foreground.default`; layers img.ava-main-1 34.0x34.0 T:1px rgb(255, 255, 255) / R:1px rgb(255, 255, 255) / B:1px rgb(255, 255, 255) / L:1px rgb(255, 255, 255) 1600px; img.ava-main 34.0x34.0 T:1px rgb(255, 255, 255) / R:1px rgb(255, 255, 255) / B:1px rgb(255, 255, 255) / L:1px rgb(255, 255, 255) 1600px; img.ava-main 34.0x34.0 T:1px rgb(255, 255, 255) / R:1px rgb(255, 255, 255) / B:1px rgb(255, 255, 255) / L:1px rgb(255, 255, .

Child layers that carry the look: img 34x34 border 1px #ffffff `apps.colors.card.default` radius 1600px; img 34x34 border 1px #ffffff `apps.colors.card.default` radius 1600px; img 34x34 border 1px #ffffff `apps.colors.card.default` radius 1600px.

![Avatar cluster default](components/crops/hero-avatars-default.png)

#### Client mark
One of the "Win more clients" brand marks under the hero CTA (Webflow, Framer, WordPress…). Read as `trusted-mark` on the home page.

**Values (default).** size 141.42 x 31.14; background transparent; text Inter 14/20 400, #000000 `apps.colors.foreground.default`.

![Client mark default](components/crops/trusted-mark-default.png)

#### Section heading
A section heading on the marketing home. Read as `home-h2` on the home page.

**Values (default).** size 1280 x 72; background transparent; text Inter 72/72 700, #000000 `apps.colors.foreground.default`.

![Section heading default](components/crops/home-h2-default.png)

#### Body paragraph
A body paragraph on the marketing home. Read as `home-prose` on the home page.

**Values (default).** size 57.53 x 22.41; background transparent; text Inter 16/22.4 600, #000000 `apps.colors.foreground.default`.

![Body paragraph default](components/crops/home-prose-default.png)

#### Home card
A feature/benefit card on the marketing home. Read as `home-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 386.66 x 518; padding 24px; border 3px solid #0050ff `apps.charts.chart.1.default`; radius 32px; background transparent; outline 3px solid rgba(0, 128, 255, 0.2) `dodger.blue.20`, offset 0px; text Inter 30/42 400, #000000 `apps.colors.foreground.default` |

![Home card default](components/crops/home-card-default.png) ![Home card hover](components/crops/home-card-hover.png)

### Pricing

The /pricing page: the Billed-monthly/Billed-annually pill tabs ('45% off' annual), the Free/Pro/Team/Agency plan cards — Team inverted black — and the FAQ disclosures.

#### Billing tab (monthly)
The "Billed monthly" toggle in the pricing switcher; opened is the selected state after clicking (a local UI toggle). Read as `ptab-monthly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 330 x 59.91; padding 16px 19.2px; radius 1600px; background #ffffff `apps.colors.card.default`; text Inter 25.6/27.90 400, #222222 `text.muted` |
| opened | background #0080ff `dodger.blue.default`; shadow rgba(0, 128, 255, 0.34) 0px 8px 10px 0px; text Inter 25.6/27.90 400, #ffffff `apps.colors.card.default` |

![Billing tab (monthly) default](components/crops/ptab-monthly-default.png) ![Billing tab (monthly) hover](components/crops/ptab-monthly-hover.png) ![Billing tab (monthly) focus-visible](components/crops/ptab-monthly-focus-visible.png) ![Billing tab (monthly) pressed](components/crops/ptab-monthly-pressed.png) ![Billing tab (monthly) opened](components/crops/ptab-monthly-opened.png)

#### Billing tab (annual)
The "Billed annually" toggle carrying the "45% off" badge. Read as `ptab-annual` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 330 x 59.91; padding 16px 19.2px; radius 1600px; background #ffffff `apps.colors.card.default`; text Inter 25.6/27.90 400, #222222 `text.muted` |

![Billing tab (annual) default](components/crops/ptab-annual-default.png) ![Billing tab (annual) hover](components/crops/ptab-annual-hover.png) ![Billing tab (annual) focus-visible](components/crops/ptab-annual-focus-visible.png) ![Billing tab (annual) pressed](components/crops/ptab-annual-pressed.png)

#### Plan card
A pricing plan card (Free: $0 forever, features list, CTA). Read as `plan-card` on the pricing page.

**Values (default).** size 305 x 435.09; padding 24px; radius 24px; background #ffffff `apps.colors.card.default`; text Inter 36/39.24 400, #000000 `apps.colors.foreground.default`.

![Plan card default](components/crops/plan-card-default.png)

#### Paid plan card
A paid pricing card ($35/mo monthly, $19.25/mo annual); hover is a pointer hover, never clicked through. Read as `plan-card-paid` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 305 x 435.09; padding 24px; radius 24px; background #000000 `apps.colors.foreground.default`; text Inter 36/39.24 400, #ffffff `apps.colors.card.default` |

![Paid plan card default](components/crops/plan-card-paid-default.png) ![Paid plan card hover](components/crops/plan-card-paid-hover.png)

#### Plan price
The price block inside a plan card. Read as `plan-price` on the pricing page.

**Values (default).** size 257 x 31.39; background transparent; text Inter 28.8/31.39 400, #000000 `apps.colors.foreground.default`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan card's action button/link; its states were measured but it was never followed — no checkout. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 257 x 75.66; padding 6px; radius 1600px; background rgba(0, 128, 255, 0.2) `dodger.blue.20`; text Inter 24/33.6 700, #ffffff `apps.colors.card.default` |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan feature row
A feature row inside a plan card. Read as `plan-row` on the pricing page.

**Values (default).** size 80.25 x 22.41; background transparent; text Inter 16/22.4 400, #8c9baa `service.grey`.

![Plan feature row default](components/crops/plan-row-default.png)

#### FAQ disclosure
A pricing FAQ disclosure row ("Can I cancel a subscription at any time?"); opened was measured after clicking it (a local UI toggle). Read as `faq-q` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 730 x 69; border B: 1px solid #cbd8e5 `light.steel.blue`; background transparent; text Inter 20/28 400, #8c9baa `service.grey`; layers div.faq__item.slide-in 730.0x69.0 B:1px rgb(203, 216, 229) |
| opened | size 730 x 159.41; layers div.faq__item.slide-in 730.0x159.4 B:1px rgb(203, 216, 229) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 730x69 border 1px #cbd8e5 `light.steel.blue`.

![FAQ disclosure default](components/crops/faq-q-default.png) ![FAQ disclosure hover](components/crops/faq-q-hover.png) ![FAQ disclosure pressed](components/crops/faq-q-pressed.png) ![FAQ disclosure opened](components/crops/faq-q-opened.png)

#### FAQ answer
An expanded pricing FAQ answer paragraph. Read as `faq-a` on the pricing page.

**Values (default).** size 730 x 159.41; border B: 1px solid #cbd8e5 `light.steel.blue`; background transparent; text Inter 20/28 400, #8c9baa `service.grey`; layers div.faq__item.slide-in 730.0x159.4 B:1px rgb(203, 216, 229).

Child layers that carry the look: div 730x159.4 border 1px #cbd8e5 `light.steel.blue`.

![FAQ answer default](components/crops/faq-a-default.png)

### Feature page

The /features/sitemap product page: the 96px display heading, the page CTA and capability cards.

#### Feature headline
The /features/sitemap page heading. Read as `feat-h1` on the sitemap feature page.

**Values (default).** size 366.84 x 99.84; background transparent; text Inter 96/99.84 700, #000000 `apps.colors.foreground.default`.

![Feature headline default](components/crops/feat-h1-default.png)

#### Feature CTA
The feature page's primary action; measured, never followed. Read as `feat-cta` on the sitemap feature page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 127.31 x 38.47; padding 7.04px 10.08px 7.04px 16px; border 1px solid #000000 `apps.colors.foreground.default`; radius 12px; background #000000 `apps.colors.foreground.default`; text Inter 16/22.4 600, #ffffff `apps.colors.card.default`; transition border-color 0.3s ease, color 0.3s ease, background-color 0.3s ease; icon 16 x 16, #ffffff `apps.colors.card.default` |
| hover, pressed | border 1px solid #cbd8e5 `light.steel.blue`; background transparent; text Inter 16/22.4 600, #000000 `apps.colors.foreground.default` |

![Feature CTA default](components/crops/feat-cta-default.png) ![Feature CTA hover](components/crops/feat-cta-hover.png) ![Feature CTA focus-visible](components/crops/feat-cta-focus-visible.png) ![Feature CTA pressed](components/crops/feat-cta-pressed.png)

#### Feature card
A capability card on the sitemap feature page. Read as `feat-card` on the sitemap feature page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1060 x 776.88; background transparent; text Inter 16/22.4 400, #000000 `apps.colors.foreground.default`; layers div.f-tools__card.is-br-32--slide-in 340.0x179.2 rgb(255, 255, 255) 32px; div.f-tools__card.is-br-32--slide-in 340.0x179.2 rgb(255, 255, 255) 32px; div.f-tools__card.is-br-32--slide-in 340.0x179.2 rgb(255, 255, 255) 32px; div.f-tools__card.is-br-32--slide-in 340.0x179.2 rgb(255, 255, 255) 32px; div.f-tools__card.is-br-32--slide-in 340.0x179.2 rgb(255, 255, 255) 32px; div.f-tools__card.is-br-32--sl |

Child layers that carry the look: div 340x179.2 background #ffffff `apps.colors.card.default` radius 32px; div 340x179.2 background #ffffff `apps.colors.card.default` radius 32px; div 340x179.2 background #ffffff `apps.colors.card.default` radius 32px.

![Feature card hover](components/crops/feat-card-hover.png)

#### Feature paragraph
A body paragraph on the feature page. Read as `feat-prose` on the sitemap feature page.

**Values (default).** size 57.53 x 22.41; background transparent; text Inter 16/22.4 600, #000000 `apps.colors.foreground.default`.

![Feature paragraph default](components/crops/feat-prose-default.png)

### Contact

The /contact-us form: name, account e-mail, organization, subject and message fields with the send button — measured at rest and typed into then cleared, never submitted.

#### Contact headline
The contact page heading. Read as `contact-h1` on the contact page.

**Values (default).** size 730 x 99.84; background transparent; text Inter 96/99.84 700, #000000 `apps.colors.foreground.default`.

![Contact headline default](components/crops/contact-h1-default.png)

#### Contact field
A text input in the contact form; focused and typed into then cleared — the form was never submitted. Read as `contact-field` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 492 x 50.08; padding 8px 0px; border B: 2px solid #cbd8e5 `light.steel.blue`; background #ffffff `apps.colors.card.default`; text Inter 20/28.57 400, #333333; placeholder #000000 `apps.colors.foreground.default` |
| focused, filled | border B: 2px solid #3898ec |

![Contact field default](components/crops/contact-field-default.png) ![Contact field focused](components/crops/contact-field-focused.png) ![Contact field filled](components/crops/contact-field-filled.png)

#### Contact message area
The message textarea; focused and typed into then cleared — never sent. Read as `contact-area` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 492 x 50.08; padding 8px 0px; border B: 2px solid #cbd8e5 `light.steel.blue`; background #ffffff `apps.colors.card.default`; text Inter 20/28.57 400, #333333; placeholder #000000 `apps.colors.foreground.default` |
| focused, filled | border B: 2px solid #3898ec |

![Contact message area default](components/crops/contact-area-default.png) ![Contact message area focused](components/crops/contact-area-focused.png) ![Contact message area filled](components/crops/contact-area-filled.png)

#### Contact submit
The contact form's send button; its states were measured but it was never clicked — nothing was sent. Read as `contact-submit` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 337.05 x 75.66; padding 9px 15px; background transparent; text Inter 14/20 400, transparent; placeholder transparent |

![Contact submit default](components/crops/contact-submit-default.png) ![Contact submit hover](components/crops/contact-submit-hover.png) ![Contact submit focus-visible](components/crops/contact-submit-focus-visible.png) ![Contact submit pressed](components/crops/contact-submit-pressed.png)

### App sign-in

app.flowmapp.com/signin — the signed-out SPA sign-in card: e-mail and password fields, the primary 'Log In' submit (disabled at rest; enabled once both fields hold sample text — never clicked) and the Google OAuth button.

#### Sign-in headline
The app sign-in heading on app.flowmapp.com/signin. Read as `login-h1` on the app sign-in page.

**Values (default).** size 61.2 x 24; background transparent; text Inter 20/24 500, #1f1f1f `primary.basic.gray.default`.

![Sign-in headline default](components/crops/login-h1-default.png)

#### Sign-in card
The sign-in form card — e-mail and password fields, the primary submit and OAuth buttons. Read as `login-card` on the app sign-in page.

**Values (default).** size 440 x 640; background transparent; text Inter 32/40 400, #1f1f1f `primary.basic.gray.default`; icon 16 x 16, #ffffff `apps.colors.card.default`; layers form.form--I3Zcx 440.0x414.0 rgb(255, 255, 255) T:1px rgb(224, 224, 224) / R:1px rgb(224, 224, 224) / B:1px rgb(224, 224, 224) / L:1px rgb(224, 224, 224) 24px; button.button--PGwt3.xl--uHTBT 374.0x56.0 rgb(255, 255, 255) T:1px rgba(0, 0, 0, 0.12) / R:1px rgba(0, 0, 0, 0.12) / B:1px rgba(0, 0, 0, 0.12) / L:1px rgba(0, 0, 0, 0.12) 16px; input.input--LVdIP.xl--i7mzS 374.0x56.0 rgb(245, 245, 245) T:1p.

Child layers that carry the look: form 440x414 background #ffffff `apps.colors.card.default` border 1px #e0e0e0 `neutral.gray.120` radius 24px; button 374x56 background #ffffff `apps.colors.card.default` border 1px rgba(0, 0, 0, 0.12) `neutral.gray.opacity.120` radius 16px; input 374x56 background #f5f5f5 `neutral.gray.40` border 1px #f5f5f5 `neutral.gray.40` radius 16px.

![Sign-in card default](components/crops/login-card-default.png)

#### Email field (sign-in)
The sign-in e-mail input; focused and typed into then cleared — never submitted. Read as `login-field` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 374 x 56; padding 20px 20px 20px 44px; border 1px solid #f5f5f5 `neutral.gray.40`; radius 16px; background #f5f5f5 `neutral.gray.40`; text Inter 16/16 400, #999999 `neutral.gray.gray.400`; placeholder #999999 `neutral.gray.gray.400` |
| focused | border 1px solid #e0e0e0 `neutral.gray.120`; background #ffffff `apps.colors.card.default`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 4px |
| filled | border 1px solid #e0e0e0 `neutral.gray.120`; background #ffffff `apps.colors.card.default`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 4px; text Inter 16/16 400, #1f1f1f `primary.basic.gray.default` |

![Email field (sign-in) default](components/crops/login-field-default.png) ![Email field (sign-in) focused](components/crops/login-field-focused.png) ![Email field (sign-in) filled](components/crops/login-field-filled.png)

#### Password field (sign-in)
The sign-in password input; focused and typed into then cleared — never submitted. Read as `login-pass` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 374 x 56; padding 20px 20px 20px 44px; border 1px solid #f5f5f5 `neutral.gray.40`; radius 16px; background #f5f5f5 `neutral.gray.40`; text Inter 16/16 400, #999999 `neutral.gray.gray.400`; placeholder #999999 `neutral.gray.gray.400` |
| focused | border 1px solid #e0e0e0 `neutral.gray.120`; background #ffffff `apps.colors.card.default`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 4px |
| filled | border 1px solid #e0e0e0 `neutral.gray.120`; background #ffffff `apps.colors.card.default`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 4px; text Inter 16/16 400, #1f1f1f `primary.basic.gray.default` |

![Password field (sign-in) default](components/crops/login-pass-default.png) ![Password field (sign-in) focused](components/crops/login-pass-focused.png) ![Password field (sign-in) filled](components/crops/login-pass-filled.png)

#### Sign-in submit
The primary "Log In" submit; every state was measured but the button was never clicked — nothing was submitted. Disabled at rest until both fields validate; `enabled` is the fill it paints once sample text sits in both fields. Read as `login-submit` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 374 x 56; padding 20px; radius 16px; background #9fb8f9 `action.primary-fill-disabled`; text Inter 16/16 400, #ffffff `apps.colors.card.default` |
| pressed | background #102f93 |
| enabled | background #0050ff `apps.charts.chart.1.default` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Sign-in submit default](components/crops/login-submit-default.png) ![Sign-in submit hover](components/crops/login-submit-hover.png) ![Sign-in submit pressed](components/crops/login-submit-pressed.png) ![Sign-in submit enabled](components/crops/login-submit-enabled.png)

#### Google OAuth button
The "Sign in with Google" OAuth button; measured, never activated. Read as `login-google` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 374 x 56; padding 19px; border 1px solid rgba(0, 0, 0, 0.12) `neutral.gray.opacity.120`; radius 16px; background #ffffff `apps.colors.card.default`; text Inter 16/16 400, rgba(0, 0, 0, 0.56) `surface.popup`; icon 16 x 16, #ffffff `apps.colors.card.default` |
| hover | background rgba(0, 0, 0, 0.06) `neutral.gray.opacity.60`; text Inter 16/16 400, #1f1f1f `primary.basic.gray.default` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background rgba(0, 0, 0, 0.08) `neutral.gray.opacity.80`; text Inter 16/16 400, #1f1f1f `primary.basic.gray.default` |

![Google OAuth button default](components/crops/login-google-default.png) ![Google OAuth button hover](components/crops/login-google-hover.png) ![Google OAuth button focus-visible](components/crops/login-google-focus-visible.png) ![Google OAuth button pressed](components/crops/login-google-pressed.png)

#### Forgot-password link
The "Forgot password?" link to /restore; measured, never followed. Read as `login-forgot` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 165.2 x 24; padding 8px 0px 0px 20px; background transparent; text Inter 14/16 400, #999999 `neutral.gray.gray.400`; transition color 0.3s ease |
| hover, pressed | text Inter 14/16 400, #0050ff `apps.charts.chart.1.default` |

![Forgot-password link default](components/crops/login-forgot-default.png) ![Forgot-password link hover](components/crops/login-forgot-hover.png) ![Forgot-password link focus-visible](components/crops/login-forgot-focus-visible.png) ![Forgot-password link pressed](components/crops/login-forgot-pressed.png)

#### Sign-up link
The "Sign Up" link beside the sign-in form; measured, never followed. Read as `login-signup` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 88.48 x 20; background transparent; text Inter 16/20 400, #0050ff `apps.charts.chart.1.default`; transition color 0.3s ease |

![Sign-up link default](components/crops/login-signup-default.png) ![Sign-up link hover](components/crops/login-signup-hover.png) ![Sign-up link focus-visible](components/crops/login-signup-focus-visible.png) ![Sign-up link pressed](components/crops/login-signup-pressed.png)

### App sign-up

app.flowmapp.com/signup — the signed-out sign-up card: e-mail, name and password fields, the primary submit and the Google button. Measured as a form, never submitted.

#### Sign-up headline
The app sign-up heading on app.flowmapp.com/signup. Read as `signup-h1` on the app sign-up page.

**Values (default).** size 70.2 x 24; background transparent; text Inter 20/24 500, #1f1f1f `primary.basic.gray.default`.

![Sign-up headline default](components/crops/signup-h1-default.png)

#### Email field (sign-up)
The sign-up e-mail input; focused and typed into then cleared — never submitted. Read as `signup-field` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 374 x 56; padding 20px 20px 20px 44px; border 1px solid #f5f5f5 `neutral.gray.40`; radius 16px; background #f5f5f5 `neutral.gray.40`; text Inter 16/16 400, #999999 `neutral.gray.gray.400`; placeholder #999999 `neutral.gray.gray.400` |
| focused | border 1px solid #e0e0e0 `neutral.gray.120`; background #ffffff `apps.colors.card.default`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 4px |
| filled | border 1px solid #e0e0e0 `neutral.gray.120`; background #ffffff `apps.colors.card.default`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 4px; text Inter 16/16 400, #1f1f1f `primary.basic.gray.default` |

![Email field (sign-up) default](components/crops/signup-field-default.png) ![Email field (sign-up) focused](components/crops/signup-field-focused.png) ![Email field (sign-up) filled](components/crops/signup-field-filled.png)

#### Name field (sign-up)
The sign-up name input; focused and typed into then cleared — never submitted. Read as `signup-name` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 374 x 56; padding 20px 20px 20px 44px; border 1px solid #f5f5f5 `neutral.gray.40`; radius 16px; background #f5f5f5 `neutral.gray.40`; text Inter 16/16 400, #999999 `neutral.gray.gray.400`; placeholder #999999 `neutral.gray.gray.400` |
| focused | border 1px solid #e0e0e0 `neutral.gray.120`; background #ffffff `apps.colors.card.default`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 4px |
| filled | border 1px solid #e0e0e0 `neutral.gray.120`; background #ffffff `apps.colors.card.default`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 4px; text Inter 16/16 400, #1f1f1f `primary.basic.gray.default` |

![Name field (sign-up) default](components/crops/signup-name-default.png) ![Name field (sign-up) focused](components/crops/signup-name-focused.png) ![Name field (sign-up) filled](components/crops/signup-name-filled.png)

#### Password field (sign-up)
The sign-up password input; focused and typed into then cleared — never submitted. Read as `signup-pass` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 374 x 56; padding 20px 20px 20px 44px; border 1px solid #f5f5f5 `neutral.gray.40`; radius 16px; background #f5f5f5 `neutral.gray.40`; text Inter 16/16 400, #999999 `neutral.gray.gray.400`; placeholder #999999 `neutral.gray.gray.400` |
| focused | border 1px solid #e0e0e0 `neutral.gray.120`; background #ffffff `apps.colors.card.default`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 4px |
| filled | border 1px solid #e0e0e0 `neutral.gray.120`; background #ffffff `apps.colors.card.default`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 4px; text Inter 16/16 400, #1f1f1f `primary.basic.gray.default` |

![Password field (sign-up) default](components/crops/signup-pass-default.png) ![Password field (sign-up) focused](components/crops/signup-pass-focused.png) ![Password field (sign-up) filled](components/crops/signup-pass-filled.png)

#### Sign-up submit
The primary sign-up submit; its states were measured but the button was never clicked — no account was created. Read as `signup-submit` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 374 x 56; padding 19px; border 1px solid rgba(0, 0, 0, 0.12) `neutral.gray.opacity.120`; radius 16px; background #ffffff `apps.colors.card.default`; text Inter 16/16 400, rgba(0, 0, 0, 0.56) `surface.popup`; icon 16 x 16, #ffffff `apps.colors.card.default` |
| hover | background rgba(0, 0, 0, 0.06) `neutral.gray.opacity.60`; text Inter 16/16 400, #1f1f1f `primary.basic.gray.default` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background rgba(0, 0, 0, 0.08) `neutral.gray.opacity.80`; text Inter 16/16 400, #1f1f1f `primary.basic.gray.default` |

![Sign-up submit default](components/crops/signup-submit-default.png) ![Sign-up submit hover](components/crops/signup-submit-hover.png) ![Sign-up submit focus-visible](components/crops/signup-submit-focus-visible.png) ![Sign-up submit pressed](components/crops/signup-submit-pressed.png)

#### Google OAuth button (sign-up)
The "Sign up with Google" button; measured, never activated. Read as `signup-google` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 374 x 56; padding 19px; border 1px solid rgba(0, 0, 0, 0.12) `neutral.gray.opacity.120`; radius 16px; background #ffffff `apps.colors.card.default`; text Inter 16/16 400, rgba(0, 0, 0, 0.56) `surface.popup`; icon 16 x 16, #ffffff `apps.colors.card.default` |
| hover | background rgba(0, 0, 0, 0.06) `neutral.gray.opacity.60`; text Inter 16/16 400, #1f1f1f `primary.basic.gray.default` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background rgba(0, 0, 0, 0.08) `neutral.gray.opacity.80`; text Inter 16/16 400, #1f1f1f `primary.basic.gray.default` |

![Google OAuth button (sign-up) default](components/crops/signup-google-default.png) ![Google OAuth button (sign-up) hover](components/crops/signup-google-hover.png) ![Google OAuth button (sign-up) focus-visible](components/crops/signup-google-focus-visible.png) ![Google OAuth button (sign-up) pressed](components/crops/signup-google-pressed.png)

#### Terms line
The terms/privacy line under the sign-up form; its links were never followed. Read as `signup-terms` on the app sign-up page.

**Values (default).** size 115.77 x 17; background transparent; text Inter 14/18 400, #999999 `neutral.gray.gray.400`.

![Terms line default](components/crops/signup-terms-default.png)

### App restore

app.flowmapp.com/restore — the password-restore card: one e-mail field and the send button. Measured as a form, never submitted.

#### Restore headline
The password-restore heading on app.flowmapp.com/restore. Read as `restore-h1` on the app restore page.

**Values (default).** size 185.2 x 24; background transparent; text Inter 20/24 500, #1f1f1f `primary.basic.gray.default`.

![Restore headline default](components/crops/restore-h1-default.png)

#### Email field (restore)
The restore e-mail input; focused and typed into then cleared — never submitted. Read as `restore-field` on the app restore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 374 x 56; padding 20px 20px 20px 44px; border 1px solid #f5f5f5 `neutral.gray.40`; radius 16px; background #f5f5f5 `neutral.gray.40`; text Inter 16/16 400, #999999 `neutral.gray.gray.400`; placeholder #999999 `neutral.gray.gray.400` |
| focused | border 1px solid #e0e0e0 `neutral.gray.120`; background #ffffff `apps.colors.card.default`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 4px |
| filled | border 1px solid #e0e0e0 `neutral.gray.120`; background #ffffff `apps.colors.card.default`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 4px; text Inter 16/16 400, #1f1f1f `primary.basic.gray.default` |

![Email field (restore) default](components/crops/restore-field-default.png) ![Email field (restore) focused](components/crops/restore-field-focused.png) ![Email field (restore) filled](components/crops/restore-field-filled.png)

#### Restore submit
The restore submit; its states were measured but the button was never clicked — no reset e-mail was sent. Read as `restore-send` on the app restore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 374 x 56; padding 20px; radius 16px; background #9fb8f9 `action.primary-fill-disabled`; text Inter 16/16 400, #ffffff `apps.colors.card.default` |
| pressed | background #102f93 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Restore submit default](components/crops/restore-send-default.png) ![Restore submit hover](components/crops/restore-send-hover.png) ![Restore submit pressed](components/crops/restore-send-pressed.png)

#### Back-to-login link
The link back to the sign-in form; measured, never followed. Read as `restore-back` on the app restore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 47.77 x 20; background transparent; text Inter 16/20 400, #0050ff `apps.charts.chart.1.default`; transition color 0.3s ease |

![Back-to-login link default](components/crops/restore-back-default.png) ![Back-to-login link hover](components/crops/restore-back-hover.png) ![Back-to-login link focus-visible](components/crops/restore-back-focus-visible.png) ![Back-to-login link pressed](components/crops/restore-back-pressed.png)

### Shared demo project

app.flowmapp.com/share/projects/215285 — a real published, read-only demo project: the sitemap page cards on canvas, the Structure/Estimation tabs, the 'Demo Project' dropdown, the toolbar and the 'Log In or Sign Up' nudge toast. The user-flow board carries screen cards and status tags.

#### Project dropdown
The "Demo Project" dropdown in the share viewer header listing the published project's boards; opened was measured after clicking it — a local UI toggle whose items were never activated. Read as `sh-menu` on the shared demo sitemap page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 141.64 x 40; padding 12px; radius 12px; background transparent; text Inter 14/16 400, #707070 `primary.basic.gray.560`; icon 16 x 16, #707070 `primary.basic.gray.560` |
| hover | background rgba(0, 0, 0, 0.04) `neutral.gray.opacity.40`; text Inter 14/16 400, #1f1f1f `primary.basic.gray.default`; icon 16 x 16, #1f1f1f `primary.basic.gray.default` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.ant-dropdown-trigger.button--PGwt3 141.6x40.0 1px auto rgb(16, 16, 16) offset 0px 12px |
| pressed, opened | background rgba(0, 0, 0, 0.04) `neutral.gray.opacity.40`; text Inter 14/16 400, #1f1f1f `primary.basic.gray.default`; icon 16 x 16, #1f1f1f `primary.basic.gray.default` |

![Project dropdown default](components/crops/sh-menu-default.png) ![Project dropdown hover](components/crops/sh-menu-hover.png) ![Project dropdown focus-visible](components/crops/sh-menu-focus-visible.png) ![Project dropdown pressed](components/crops/sh-menu-pressed.png) ![Project dropdown opened](components/crops/sh-menu-opened.png)

#### Structure tab
The "Structure" toolbar tab in the share viewer. Read as `sh-tab-structure` on the shared demo sitemap page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 113.48 x 40; padding 12px; radius 12px; background transparent; text Inter 14/16 400, #707070 `primary.basic.gray.560`; icon 16 x 16, #707070 `primary.basic.gray.560` |
| hover | background rgba(0, 0, 0, 0.04) `neutral.gray.opacity.40`; text Inter 14/16 400, #1f1f1f `primary.basic.gray.default`; icon 16 x 16, #1f1f1f `primary.basic.gray.default` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.button--PGwt3.m--_mvvS 113.5x40.0 1px auto rgb(16, 16, 16) offset 0px 12px |
| pressed | background rgba(0, 0, 0, 0.04) `neutral.gray.opacity.40`; text Inter 14/16 400, #1f1f1f `primary.basic.gray.default`; icon 16 x 16, #1f1f1f `primary.basic.gray.default` |

![Structure tab default](components/crops/sh-tab-structure-default.png) ![Structure tab hover](components/crops/sh-tab-structure-hover.png) ![Structure tab focus-visible](components/crops/sh-tab-structure-focus-visible.png) ![Structure tab pressed](components/crops/sh-tab-structure-pressed.png)

#### Estimation tab
The "Estimation" toolbar tab; opened was measured after clicking it — a local UI toggle switching the viewer pane. Read as `sh-tab-estimation` on the shared demo sitemap page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 122.2 x 40; padding 12px; radius 12px; background transparent; text Inter 14/16 400, #707070 `primary.basic.gray.560`; icon 16 x 16, #707070 `primary.basic.gray.560` |
| hover | background rgba(0, 0, 0, 0.04) `neutral.gray.opacity.40`; text Inter 14/16 400, #1f1f1f `primary.basic.gray.default`; icon 16 x 16, #1f1f1f `primary.basic.gray.default` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.button--PGwt3.m--_mvvS 122.2x40.0 1px auto rgb(16, 16, 16) offset 0px 12px |
| pressed | background rgba(0, 0, 0, 0.04) `neutral.gray.opacity.40`; text Inter 14/16 400, #1f1f1f `primary.basic.gray.default`; icon 16 x 16, #1f1f1f `primary.basic.gray.default` |

![Estimation tab default](components/crops/sh-tab-estimation-default.png) ![Estimation tab hover](components/crops/sh-tab-estimation-hover.png) ![Estimation tab focus-visible](components/crops/sh-tab-estimation-focus-visible.png) ![Estimation tab pressed](components/crops/sh-tab-estimation-pressed.png) ![Estimation tab opened](components/crops/sh-tab-estimation-opened.png)

#### Share Log In button
The "Log In" header button in the share viewer; measured, never clicked — the viewer stays signed out. Read as `sh-login-btn` on the shared demo sitemap page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 65.33 x 40; padding 12px; radius 12px; background transparent; text Inter 14/16 400, #707070 `primary.basic.gray.560` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.button--PGwt3.m--_mvvS 65.3x40.0 1px auto rgb(16, 16, 16) offset 0px 12px |
| pressed | background rgba(0, 0, 0, 0.04) `neutral.gray.opacity.40`; text Inter 14/16 400, #1f1f1f `primary.basic.gray.default` |

![Share Log In button default](components/crops/sh-login-btn-default.png) ![Share Log In button hover](components/crops/sh-login-btn-hover.png) ![Share Log In button focus-visible](components/crops/sh-login-btn-focus-visible.png) ![Share Log In button pressed](components/crops/sh-login-btn-pressed.png)

#### Share Sign Up button
The "Sign Up" header button in the share viewer; measured, never clicked. Read as `sh-signup-btn` on the shared demo sitemap page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 76.05 x 40; padding 12px; radius 12px; background transparent; text Inter 14/16 400, #707070 `primary.basic.gray.560` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.button--PGwt3.m--_mvvS 76.0x40.0 1px auto rgb(16, 16, 16) offset 0px 12px |
| pressed | background rgba(0, 0, 0, 0.04) `neutral.gray.opacity.40`; text Inter 14/16 400, #1f1f1f `primary.basic.gray.default` |

![Share Sign Up button default](components/crops/sh-signup-btn-default.png) ![Share Sign Up button hover](components/crops/sh-signup-btn-hover.png) ![Share Sign Up button focus-visible](components/crops/sh-signup-btn-focus-visible.png) ![Share Sign Up button pressed](components/crops/sh-signup-btn-pressed.png)

#### Sign-up nudge
The "Hi, Log In or Sign Up to start planning amazing websites!" toast pinned over the viewer (dismissable, left in place for the reading). Read as `sh-popup` on the shared demo sitemap page.

**Values (default).** size 251.58 x 80; padding 16px 20px; radius 14px; background rgba(0, 0, 0, 0.56) `surface.popup`; text Inter 14/24 400, #ffffff `apps.colors.card.default`.

![Sign-up nudge default](components/crops/sh-popup-default.png)

#### Sitemap page card
A page card on the published sitemap canvas (title, mini-map of sections); read-only. Read as `sh-card` on the shared demo sitemap page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 95.07 x 104.35; border 2px solid #1f1f1f `primary.basic.gray.default`; radius 16px; background #ffffff `apps.colors.card.default`; text Inter 16/20 400, #1f1f1f `primary.basic.gray.default`; transition opacity 0.2s ease-in-out |

![Sitemap page card default](components/crops/sh-card-default.png) ![Sitemap page card hover](components/crops/sh-card-hover.png)

#### Sitemap card blocks
The section list inside a sitemap page card (Menu, Header, Featured Services…). Read as `sh-blocks` on the shared demo sitemap page.

**Values (default).** size 81.16 x 113.62; background transparent; text Inter 12/20 400, #f5cc00 `secondary.yellow.default`; icon 6.96 x 6.96, #1f1f1f `primary.basic.gray.default`; layers div.block--uZwRO 81.2x20.9 rgba(245, 204, 0, 0.16) 8px; div.block--uZwRO 81.2x20.9 rgba(255, 163, 52, 0.16) 8px; div.block--uZwRO 81.2x20.9 rgba(255, 163, 52, 0.16) 8px; div.block--uZwRO 81.2x20.9 rgba(255, 163, 52, 0.16) 8px; div.block--uZwRO 81.2x20.9 rgba(54, 235, 141, 0.16) 8px.

Child layers that carry the look: div 81.2x20.9 background rgba(245, 204, 0, 0.16) radius 8px; div 81.2x20.9 background rgba(255, 163, 52, 0.16) radius 8px; div 81.2x20.9 background rgba(255, 163, 52, 0.16) radius 8px.

![Sitemap card blocks default](components/crops/sh-blocks-default.png)

#### Canvas toolbar button
An icon button on the share viewer's bottom toolbar panel. Read as `sh-toolbar-btn` on the shared demo sitemap page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 36 x 36; padding 10px; radius 12px; background transparent; text Inter 20/20 400, #1f1f1f `primary.basic.gray.default`; icon 16 x 16, #1f1f1f `primary.basic.gray.default` |
| pressed | background rgba(0, 0, 0, 0.04) `neutral.gray.opacity.40`; text Inter 20/20 400, #0050ff `apps.charts.chart.1.default`; icon 16 x 16, #0050ff `apps.charts.chart.1.default` |

![Canvas toolbar button default](components/crops/sh-toolbar-btn-default.png) ![Canvas toolbar button hover](components/crops/sh-toolbar-btn-hover.png) ![Canvas toolbar button focus-visible](components/crops/sh-toolbar-btn-focus-visible.png) ![Canvas toolbar button pressed](components/crops/sh-toolbar-btn-pressed.png)

#### Disabled toolbar button
A disabled icon button on the share viewer's bottom toolbar. Read as `sh-toolbar-disabled` on the shared demo sitemap page.

**Values (default).** size 40 x 40; padding 10px; radius 12px; background transparent; text Inter 20/20 400, #1f1f1f `primary.basic.gray.default`; opacity 0.2; icon 16 x 16, #1f1f1f `primary.basic.gray.default`.

![Disabled toolbar button default](components/crops/sh-toolbar-disabled-default.png)

#### Zoom button
The zoom-percentage button on the share viewer toolbar; measured, never toggled. Read as `sh-zoom` on the shared demo sitemap page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 53.19 x 40; padding 12px; radius 12px; background transparent; text Inter 14/16 400, #707070 `primary.basic.gray.560` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.button--PGwt3.m--_mvvS 53.2x40.0 1px auto rgb(16, 16, 16) offset 0px 12px |
| pressed | background rgba(0, 0, 0, 0.04) `neutral.gray.opacity.40`; text Inter 14/16 400, #1f1f1f `primary.basic.gray.default` |

![Zoom button default](components/crops/sh-zoom-default.png) ![Zoom button hover](components/crops/sh-zoom-hover.png) ![Zoom button focus-visible](components/crops/sh-zoom-focus-visible.png) ![Zoom button pressed](components/crops/sh-zoom-pressed.png)

#### Help button
The "?" help button on the share viewer chrome. Read as `sh-help` on the shared demo sitemap page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 32; padding 8px; radius 100%; background rgba(0, 0, 0, 0.4) `neutral.gray.400`; text Inter 14/16 400, #ffffff `apps.colors.card.default`; icon 16 x 16, #ffffff `apps.colors.card.default` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background #1f1f1f `primary.basic.gray.default` |

![Help button default](components/crops/sh-help-default.png) ![Help button hover](components/crops/sh-help-hover.png) ![Help button focus-visible](components/crops/sh-help-focus-visible.png) ![Help button pressed](components/crops/sh-help-pressed.png)

#### User-flow card
A screen/flow card on the published user-flow canvas; read-only. Read as `uf-card` on the shared demo user flow page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 139.22 x 191.43; background transparent; text Inter 16/20 400, #1f1f1f `primary.basic.gray.default`; icon 100.94 x 62.65, #6696ff `secondary.blue.default`; layers div.card--ua7fI 142.7x194.9 rgb(255, 255, 255) T:2px rgb(31, 31, 31) / R:2px rgb(31, 31, 31) / B:2px rgb(31, 31, 31) / L:2px rgb(31, 31, 31) 16px; div.label--ICrwG 31.3x13.9 rgba(245, 204, 0, 0.4) T:1px rgba(245, 204, 0, 0.4) / R:1px rgba(245, 204, 0, 0.4) / B:1px rgba(245, 204, 0, 0.4) / L:1px rgba(245, 204, 0, 0.4) 12px; div.label--ICrwG 63.5x13.9 rgba(255, 124, 67, 0.4) T:1px rgba(255, 124, 67, |

Child layers that carry the look: div 142.7x194.9 background #ffffff `apps.colors.card.default` border 2px #1f1f1f `primary.basic.gray.default` radius 16px; div 31.3x13.9 background rgba(245, 204, 0, 0.4) border 1px rgba(245, 204, 0, 0.4) radius 12px; div 63.5x13.9 background rgba(255, 124, 67, 0.4) border 1px rgba(255, 124, 67, 0.4) radius 12px.

![User-flow card default](components/crops/uf-card-default.png) ![User-flow card hover](components/crops/uf-card-hover.png)

#### Status tag
A status pill on the user-flow canvas (NEW / IN PROGRESS / DONE…). Read as `uf-tag` on the shared demo user flow page.

**Values (default).** size 104.42 x 34.81; padding 0px 0px 4px 0px; background transparent; text Inter 9/12 400, #f5cc00 `secondary.yellow.default`; layers div.label--ICrwG 31.3x13.9 rgba(245, 204, 0, 0.4) T:1px rgba(245, 204, 0, 0.4) / R:1px rgba(245, 204, 0, 0.4) / B:1px rgba(245, 204, 0, 0.4) / L:1px rgba(245, 204, 0, 0.4) 12px; div.label--ICrwG 63.5x13.9 rgba(255, 124, 67, 0.4) T:1px rgba(255, 124, 67, 0.4) / R:1px rgba(255, 124, 67, 0.4) / B:1px rgba(255, 124, 67, 0.4) / L:1px rgba(255, 124, 67, 0.4) 12px; div.label--ICrwG 54.8x13.9 rgba(102, 15.

Child layers that carry the look: div 31.3x13.9 background rgba(245, 204, 0, 0.4) border 1px rgba(245, 204, 0, 0.4) radius 12px; div 63.5x13.9 background rgba(255, 124, 67, 0.4) border 1px rgba(255, 124, 67, 0.4) radius 12px; div 54.8x13.9 background rgba(102, 150, 255, 0.4) border 1px rgba(102, 150, 255, 0.4) radius 12px.

![Status tag default](components/crops/uf-tag-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the header, the burger menu, the masthead and the hero CTA.

#### Mobile top bar
The phone header at 390 wide: wordmark, the burger and the actions that survive the width. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 381.75 x 54.69; padding 4.134px 0px 0px 0px; background transparent; text Inter 14/20 400, #000000 `apps.colors.foreground.default`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1; div.nav__bg 0.0x0.0 rgba(0, 0, 0, 0.5); div.container.nav-cont__is-br-12--is-sh-img 381.8x50.6 rgba(255, 255, 255, 0.8) rgba(120, 124, 132, 0.19) -9.92904px 11.043px 59.7576px 0px 12px; div.nav__links 0.0x0.0 rgb(255, 255, 255) 12px; div.nav__link-underline 0.0x0.0 B:1px rgb(140, 155, 170); div.nav__pop.is-sh-l--is-bg-wh--i.

Child layers that carry the look: div 0x0 background rgba(0, 0, 0, 0.5); div 381.8x50.6 background rgba(255, 255, 255, 0.8) radius 12px shadow rgba(120, 124, 132, 0.19) -9.92904px 11.043px 59.7576px 0px; div 0x0 background #ffffff `apps.colors.card.default` radius 12px.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile burger
The nav burger at 390 wide; opened was measured after tapping it (a local UI toggle opening the mobile menu). Read as `m-burger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 35.88 x 35.88; background transparent; text Inter 24/20 400, #000000 `apps.colors.foreground.default`; icon 35.88 x 35.88, #000000 `apps.colors.foreground.default` |
| opened | text Inter 24/20 400, #ffffff `apps.colors.card.default`; icon 35.88 x 35.88, #ffffff `apps.colors.card.default` |

![Mobile burger default](components/crops/m-burger-default.png) ![Mobile burger hover](components/crops/m-burger-hover.png) ![Mobile burger focus-visible](components/crops/m-burger-focus-visible.png) ![Mobile burger pressed](components/crops/m-burger-pressed.png) ![Mobile burger opened](components/crops/m-burger-opened.png)

#### Mobile menu link
A link inside the opened mobile nav menu. Read as `m-menu-link` on the home page at 390 wide.

**Values (default).** size 348.53 x 47.7; padding 11.388px 14.508px; radius 8px; background transparent; text Inter 16.61/23.25 600, #000000 `apps.colors.foreground.default`; transition background-color 0.3s ease; layers div.nav__link-underline 135.0x24.3 B:1px rgb(140, 155, 170).

Child layers that carry the look: div 135x24.3 border 1px #8c9baa `service.grey`.

![Mobile menu link default](components/crops/m-menu-link-default.png)

#### Mobile hero headline
The hero display heading at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 348.53 x 99.7; background transparent; text Inter 33.22/33.22 700, #000000 `apps.colors.foreground.default`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The hero action at 390 wide; measured never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 316.75 x 78.17; padding 5.85px; radius 780px; background rgba(0, 128, 255, 0.2) `dodger.blue.20`; text Inter 22.62/29.04 600, #ffffff `apps.colors.card.default`; icon 65.52 x 13.78, #ffffff `apps.colors.card.default` |

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the FlowMapp wordmark, the flyout feature glyphs, the squiggle-arrow CTA mark, the sitemap/user-flow node icons and the client brand marks) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

FlowMapp's product is the planning workspace: every post-login surface — the sitemap and user-flow editors, wireframes, content and estimation tools, dashboards and billing — needs an account and was never reached. app.flowmapp.com/signin, /signup and /restore are the only auth surfaces a signed-out visitor sees, and they were measured as forms, never submitted. The published demo project at /share/projects/215285 is genuinely public — the marketing 'Try Demo Project' link points to it — and paints the real viewers read-only behind a 'Log In or Sign Up' nudge. The product mocks inside the marketing cards are illustrations, not the product.

### Pages

- **The account.** Every post-login surface was never reached; the sign-in, sign-up and restore forms were measured and typed into then cleared — 'Log In', 'Sign Up' and the restore send were never pressed, and what a submitted form returns is unverified.
- **The contact form.** Fields were focused and typed into then cleared; 'Send message' was never pressed — no message was sent and the post-submit state is uncaptured.
- **Purchase.** Plan CTAs ('Sign up Free', 'Start Free Trial') were measured, never followed; no checkout or trial flow was started.
- **Feature/use-case routes** beyond the captured set (/features/content, /features/estimation-invoice, /features/flowchart, /features/sitemaps-from-url, the other use cases and blog categories/articles) are the same templates, unmeasured; one example of each family was captured.
- **Help centre.** The 'Help' nav item links to FlowMapp's help centre on a separate surface; it was not captured this pass.
- **Mobile sign-in.** app.flowmapp.com/signin returned a security challenge on the 390-wide pass; the desktop capture stands, the phone-width auth card is uncaptured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Error, loading and validation states** were not seen on the public surface — the forms were never submitted. The sign-in submit's disabled fill is measured at rest and its enabled fill with sample text in both fields.
- **The share viewer's interactive states** (canvas pan/zoom gestures, node selection, estimation editing) are read-only projections of the editor; the nudge toast was left in place, never dismissed.

### Themes

Every signed-out surface paints light only — no theme toggle and no `prefers-color-scheme` dark rule was observed on www.flowmapp.com or app.flowmapp.com (`color-scheme: normal`). The marketing sheet does declare a parallel dark vocabulary in the Webflow `_apps---colors--*-dark` variables — captured verbatim in core.apps.* — but nothing signed out switches to it, so it is declared evidence, not a captured theme.

### Fonts

- **Inter** (self-hosted woff2 400–700 on the marketing site's Webflow CDN; Google-Fonts Inter 500 on the app) is the served face on both hosts. The style guide falls back to system sans.

### Screenshots

- The product mocks, screenshots-in-screenshots and logo walls are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article copy, testimonial names and the changelog text are the product's content; only frames and components were measured.
