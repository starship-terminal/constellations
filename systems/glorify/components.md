# Glorify components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from glorify.com and app.glorify.com on 2026-11-16, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the sign-in and sign-up forms were never sent; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (84 components, 226 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value in the component's own surface set (light / app — the two hosts declare separate vocabularies), when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/24 500, #131e40`, and is read from the first text node inside the component.
- Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the surface painted at capture: `light` for the marketing pages (light-only — no toggle, no dark media query) and `app` for the dark app/editor surfaces. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (207 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [features-menu](screenshots/home-light-features-menu.png), [full](screenshots/home-light-full.png) |
| Pricing | `/pricing` | [billed-monthly](screenshots/pricing-light-billed-monthly.png), [billed-yearly](screenshots/pricing-light-billed-yearly.png), [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Background Remover feature | `/features/background-remover` | [default](screenshots/feature-bg-light-default.png), [full](screenshots/feature-bg-light-full.png) |
| Templates | `/templates` | [default](screenshots/templates-light-default.png), [full](screenshots/templates-light-full.png) |
| Template marketplace | `/template-marketplace` | [default](screenshots/marketplace-light-default.png), [full](screenshots/marketplace-light-full.png) |
| Learn | `/learn` | [default](screenshots/learn-light-default.png), [full](screenshots/learn-light-full.png) |
| Learn article | `/learn/facebook-ad-sizes-best-practices-2024` | [default](screenshots/learn-article-light-default.png), [full](screenshots/learn-article-light-full.png) |
| Team | `/team` | [default](screenshots/team-light-default.png), [full](screenshots/team-light-full.png) |
| Affiliates | `/affiliates` | [default](screenshots/affiliates-light-default.png), [full](screenshots/affiliates-light-full.png) |
| Webinars | `/webinars` | [default](screenshots/webinars-light-default.png), [full](screenshots/webinars-light-full.png) |
| Submit a template | `/submit-template` | [default](screenshots/submit-template-light-default.png), [full](screenshots/submit-template-light-full.png) |
| Canva alternative | `/canva-alternative` | [default](screenshots/canva-alternative-light-default.png), [full](screenshots/canva-alternative-light-full.png) |
| Terms | `/terms-of-service` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| Privacy | `/privacy-policy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| App sign-in | `app.glorify.com/dashboard/login` | [default](screenshots/login-app-default.png), [full](screenshots/login-app-full.png) |
| App sign-up | `app.glorify.com/dashboard/register` | [default](screenshots/register-app-default.png), [full](screenshots/register-app-full.png) |
| Anonymous editor | `app.glorify.com/designer/use-template/0` | [canvas](screenshots/designer-app-canvas.png), [default](screenshots/designer-app-default.png), [dialog](screenshots/designer-app-dialog.png), [layers](screenshots/designer-app-layers.png), [style-picked](screenshots/designer-app-style-picked.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| App sign-in, phone | `app.glorify.com/dashboard/login` | [default](screenshots/mobile-login-app-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Consent overlay | every page | no consent banner was observed on either host; any layer would be hidden, never answered | hidden before every shot and reading |
| Features dropdown | marketing header | hovered the 'Features' nav trigger to open its Framer dropdown | [home-light-features-menu](screenshots/home-light-features-menu.png), [nav-features](#features-nav-trigger) |
| Billing switcher | pricing | clicked 'Monthly' and 'Yearly' — local UI toggles that only swap the displayed prices | [pricing-light-billed-yearly](screenshots/pricing-light-billed-yearly.png), [pricing-light-billed-monthly](screenshots/pricing-light-billed-monthly.png), [bill-monthly](#billing-tab-monthly), [bill-yearly](#billing-tab-yearly) |
| Mobile menu | home, phone width | tapped the nav burger | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-burger](#mobile-burger), [m-menu-link](#mobile-menu-link) |
| Craft dialog | anonymous editor | clicked the 'Try with Placeholder Image' card — the product's demo path on the scratch file | [designer-app-dialog](screenshots/designer-app-dialog.png), [ed-craft](#craft-dialog), [ob-ph](#placeholder-image-card) |
| Craft style pick | anonymous editor | clicked the 'Modern' style card — the local toggle that enables 'Add to canvas' | [designer-app-style-picked](screenshots/designer-app-style-picked.png), [ed-craft-style](#style-card), [ed-add](#add-to-canvas) |
| Canvas view | anonymous editor | pressed 'Add to canvas' once on the scratch file (the screenshot pass) — it ran a server-side AI generation; a boundary since 2026-11, no longer pressed | [designer-app-canvas](screenshots/designer-app-canvas.png) |
| Inspector LAYERS tab | anonymous editor | clicked the LAYERS inspector tab — a local UI toggle | [designer-app-layers](screenshots/designer-app-layers.png), [ed-tab](#inspector-tab), [ed-tab-layers](#layers-tab) |
| Auth fields | app.glorify.com | typed into then cleared — nothing sent; the sign-in submit's enabled fill was measured with sample text in both fields, never clicked | [login-field](#email-field-sign-in), [login-submit](#sign-in-submit) |
| Signed-in product | a Glorify account | every post-login surface (the real projects, dashboards, brand kit, billing) needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 22 components were given a real keyboard focus. 12 draw an outline ring: `nav-link` (1px auto #101010, offset 1px), `nav-login` (1px auto #101010, offset 1px), `nav-play` (1px auto #101010, offset 1px), `hero-cta` (1px auto #101010, offset 1px), `home-learn-more` (1px auto #101010, offset 1px), `footer-link` (1px auto #101010, offset 1px), `plan-cta` (1px auto #101010, offset 1px), `feat-cta` (1px auto #101010, offset 1px), `tpl-cat` (1px auto #101010, offset 1px), `reg-terms` (1px auto #101010, offset 1px), `ed-close` (2px solid #646363 `token.5dd49439.e215.4b63.80c0.703cbaec2c75`, offset 0px), `m-hero-cta` (1px auto #101010, offset 1px). 6 draw a focus ring as a shadow instead: `login-google`, `reg-google`, `ed-login`, `ed-signup`, `ed-add`, `ed-replace`. The other 4 show no measured change: `ed-share`, `ed-download`, `ed-zoom`, `ed-tool`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | ed-craft |
| 0.25s | `linear` | all | ed-add, ed-close, ed-craft-style, ed-login, ed-replace, ed-signup, login-google, login-submit and more |
| 0.3s | `cubic-bezier(0.44, 0, 0.56, 1)` | color | footer-link |
| 0.3s | `linear` | all, background-color, border-color, color, fill, none, stroke | ed-color, ed-download, ed-header, ed-inspector, ed-share, ed-tool, ed-zoom, login-field and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Home card](#home-card) | 252 x 257.34 | - | 16px | #ffffff `chat.bg.color` | rgba(0, 0, 0, 0.1) 0px 4px 24px 0px | 12px |
| [Plan card](#plan-card) | 230 x 149.41 | - | - | #ffffff `chat.bg.color` | none | 18px |
| [Feature card](#feature-card) | 1200 x 572.8 | - | - | transparent | none | 0 |
| [Template tile](#template-tile) | 193.93 x 102.31 | - | 8px | transparent | none | 0 |
| [Marketplace card](#marketplace-card) | 384 x 256 | - | 8px | transparent | none | 0 |
| [Article card](#article-card) | 384 x 433.86 | - | 8px | #fff9f3 `token.1a71ae8b.0ebf.47f2.9b16.91692b35aeb7` | none | 12px |
| [Privileges card](#privileges-card) | 1200 x 148.8 | - | - | transparent | none | 0 |
| [Sign-in card](#sign-in-card) | 352 x 384 | - | - | transparent | none | 0 |
| [Placeholder Image card](#placeholder-image-card) | 206 x 46 | - | - | transparent | none | 0 |
| [Craft dialog](#craft-dialog) | 792 x 640 | - | 16px | #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7` | rgba(0, 0, 0, 0.1) 0px 1px 10px 0px | 0 |
| [Style card](#style-card) | 97.19 x 106 | 1px solid transparent | 8px | #3e261d | none | 8px |
| [Inspector panel](#inspector-panel) | 280 x 824 | 1px solid #434242 `token.437b14b7.0164.40e6.a64c.c9076019a119` | 12px | #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7` | none | 0 |
| [Mobile menu link](#mobile-menu-link) | 75 x 24 | - | - | transparent | none | 0 |

## Components

### Site chrome

The header on every marketing page: the Glorify wordmark, the 'Who is it for?'/Features/Resources/Templates dropdowns, Pricing, Login, 'Play for free' and 'Get Started Now'.

#### Page field
The marketing body element — the painted field every page sits on. Read as `page-bg` on the home page.

**Values (default).** size 1440 x 15728.42; background #ffffff `chat.bg.color`; text Inter 9/10.8 700, #fff9f3 `token.1a71ae8b.0ebf.47f2.9b16.91692b35aeb7`; icon 75 x 24, #0000ee.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Site header
The marketing top bar: wordmark, the "Who is it for?"/Features/Resources/Templates dropdowns, Pricing, Login, "Play for free" and "Get Started Now". Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 64; background #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`; text Inter 9/10.8 700, #fff9f3 `token.1a71ae8b.0ebf.47f2.9b16.91692b35aeb7`; icon 75 x 24, #0000ee.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Glorify wordmark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 182 x 24; background transparent; text Inter 9/10.8 700, #fff9f3 `token.1a71ae8b.0ebf.47f2.9b16.91692b35aeb7`; icon 75 x 24, #0000ee; layers a.framer-1pxcn6y.framer-1v7amdl 97.0x23.6 rgb(17, 17, 17) 2px.

Child layers that carry the look: a 97x23.6 background #111111 `token.4afff1e1.ad66.4449.a126.34071669c871` radius 2px.

![Logo default](components/crops/mkt-logo-default.png)

#### Nav link
A marketing header nav link (Pricing); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 61.61 x 30; padding 8px; radius 8px; background #ffffff `chat.bg.color`; text Inter 14/14 500, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871` |
| hover | background #eceffd `token.a392612b.78bb.4d6b.bbd0.20d6b8f5a47a`; text Inter 14/14 500, rgba(69, 94, 237, 0.992) |
| focus-visible | outline 1px auto #101010, offset 1px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Features nav trigger
The "Features" nav item that opens the feature-page dropdown on hover. Read as `nav-features` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 59.41 x 14; background transparent; text Inter 14/14 500, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871` |
| hover | text Inter 14/14 500, rgba(69, 94, 237, 0.894) |
| opened | text Inter 14/14 500, #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Features nav trigger default](components/crops/nav-features-default.png) ![Features nav trigger hover](components/crops/nav-features-hover.png) ![Features nav trigger pressed](components/crops/nav-features-pressed.png) ![Features nav trigger opened](components/crops/nav-features-opened.png)

#### Login link
The "Login" nav action to app.glorify.com/welcome; measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 57.02 x 32; padding 8px; radius 4px; background #ffffff `chat.bg.color`; text Inter-Medium 16/16 500, #000000 `border.focus-ring` |
| hover | background #eceffd `token.a392612b.78bb.4d6b.bbd0.20d6b8f5a47a`; text Inter-Medium 16/16 500, #455eec |
| focus-visible | outline 1px auto #101010, offset 1px |

![Login link default](components/crops/nav-login-default.png) ![Login link hover](components/crops/nav-login-hover.png) ![Login link focus-visible](components/crops/nav-login-focus-visible.png) ![Login link pressed](components/crops/nav-login-pressed.png)

#### Play for free link
The "Play for free" nav action to the anonymous editor on app.glorify.com; measured, never followed. Read as `nav-play` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 119.41 x 42; padding 14px 18px; radius 8px; background #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479`; text Inter 14/14 500, #fff9f3 `token.1a71ae8b.0ebf.47f2.9b16.91692b35aeb7` |
| hover | background #374bbf |
| focus-visible | outline 1px auto #101010, offset 1px |

![Play for free link default](components/crops/nav-play-default.png) ![Play for free link hover](components/crops/nav-play-hover.png) ![Play for free link focus-visible](components/crops/nav-play-focus-visible.png) ![Play for free link pressed](components/crops/nav-play-pressed.png)

#### Get Started Now button
The header "Get Started Now" CTA on /pricing ([data-framer-name="Button Wrap"]); measured, never followed. Read as `nav-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 188.42 x 42; background transparent; text Inter-Medium 16/16 500, #000000 `border.focus-ring`; layers a.framer-nVpef.framer-R8fVZ 57.0x32.0 rgb(255, 255, 255) 4px; a.framer-cLpv3.framer-R8fVZ 119.4x42.0 rgb(69, 94, 237) 8px |
| hover | layers a.framer-nVpef.framer-R8fVZ 57.0x32.0 rgb(255, 255, 255) 4px; a.framer-cLpv3.framer-R8fVZ 119.4x42.0 rgb(55, 75, 191) 8px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: a 57x32 background #ffffff `chat.bg.color` radius 4px; a 119.4x42 background #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479` radius 8px.

![Get Started Now button default](components/crops/nav-cta-default.png) ![Get Started Now button hover](components/crops/nav-cta-hover.png) ![Get Started Now button pressed](components/crops/nav-cta-pressed.png)

### Home

The light home page: the 'Easily create marketing visuals that turn browsers to buyers' masthead over the Ecom subline, the 'Play for free' action into the anonymous editor, and the feature cards.

#### Hero headline
"Easily create marketing visuals that turn browsers to buyers." — the display heading. Read as `hero-h1` on the home page.

**Values (default).** size 838 x 230.39; background transparent; text PolySans Trial Median 64/76.8 400, #ffffff `chat.bg.color`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero subline
The paragraph under the hero heading ("Enjoy the ultimate Ecom design tool…"). Read as `hero-sub` on the home page.

**Values (default).** size 432 x 51.19; background transparent; text Inter 16/25.6 500, #737373 `token.8ce0d4bb.84b2.4aa8.b7fa.cf8d27b8e0c7`.

![Hero subline default](components/crops/hero-sub-default.png)

#### Hero CTA
The hero "Play for free" button to the anonymous editor — an outlined ghost on the dark hero band, not the filled nav button (the leaf text is tagged in-page: the nav's identical label is the DOM-first match). Measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 119.41 x 46; padding 14px 18px; radius 8px; background transparent; text Inter 14/14 500, #ffffff `chat.bg.color`; layers ::after rgba(0, 0, 0, 0) 1px none 1; a::after.framer-13l81z2.framer-19c9wqe 119.406pxx46px T:1px rgb(255, 255, 255) / R:1px rgb(255, 255, 255) / B:1px rgb(255, 255, 255) / L:1px rgb(255, 255, 255) 8px |
| hover | opacity 0.8 |
| focus-visible | outline 1px auto #101010, offset 1px; layers ::after rgba(0, 0, 0, 0) 1px none 1; a.framer-13l81z2.framer-19c9wqe 119.4x46.0 1px auto rgb(16, 16, 16) offset 1px 8px; a::after.framer-13l81z2.framer-19c9wqe 119.406pxx46px T:1px rgb(255, 255, 255) / R:1px rgb(255, 255, 255) / B:1px rgb(255, 255, 255) / L:1px rgb(255, 255, 255) 8px |

Child layers that carry the look: a::after 119.406pxx46px border 1px #ffffff `chat.bg.color` radius 8px.

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Section heading
A section heading on the marketing home. Read as `home-h2` on the home page.

**Values (default).** size 288 x 28.8; background transparent; text PolySans Trial Median 24/28.8 400, #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7`.

![Section heading default](components/crops/home-h2-default.png)

#### Home card
A feature/benefit card on the marketing home. Read as `home-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 252 x 257.34; padding 12px; radius 16px; background #ffffff `chat.bg.color`; shadow rgba(0, 0, 0, 0.1) 0px 4px 24px 0px; text Inter 14/19.6 500, #403d3a `token.f52c85c9.4b46.4081.9ae2.43cd4051929f`; icon 24 x 24, #fd4370 `token.b2fe3658.3bde.4027.8a2d.5c69cb4736d3`; layers ::after rgba(0, 0, 0, 0) 1px none 1 |

![Home card default](components/crops/home-card-default.png) ![Home card hover](components/crops/home-card-hover.png)

#### Learn more link
A "Learn more" link inside a home feature row; measured, never followed. Read as `home-learn-more` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 89.02 x 34; padding 10px 0px; radius 8px; background transparent; text Inter-SemiBold 12/12 600, #51cab4 `token.2ff71b15.79ff.4961.a5d5.3c255280b832`; icon 14 x 14, #0000ee |
| hover | size 99.05 x 34; radius 8.07662% 23.5294% |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-cLpv3.framer-R8fVZ 89.0x34.0 1px auto rgb(16, 16, 16) offset 1px 8px |
| pressed | icon 14 x 14, #ff0000 |

![Learn more link default](components/crops/home-learn-more-default.png) ![Learn more link hover](components/crops/home-learn-more-hover.png) ![Learn more link focus-visible](components/crops/home-learn-more-focus-visible.png) ![Learn more link pressed](components/crops/home-learn-more-pressed.png)

### Pricing

The /pricing page: the Monthly/Yearly billing switcher and the Basic/Pro/Business plan cards with their 'Start … Trial' actions.

#### Billing tab (monthly)
The "Monthly" side of the pricing billing switcher; opened is the state after clicking it — a local UI toggle. Read as `bill-monthly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 60.33 x 20; background transparent; text Inter-Medium 16/20 500, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Billing tab (monthly) default](components/crops/bill-monthly-default.png) ![Billing tab (monthly) hover](components/crops/bill-monthly-hover.png) ![Billing tab (monthly) pressed](components/crops/bill-monthly-pressed.png) ![Billing tab (monthly) opened](components/crops/bill-monthly-opened.png)

#### Billing tab (yearly)
The "Yearly" side of the billing switcher; opened is the state after clicking it — a local UI toggle. Read as `bill-yearly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 46.56 x 20; background transparent; text Inter-Medium 16/20 500, #acacac |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Billing tab (yearly) default](components/crops/bill-yearly-default.png) ![Billing tab (yearly) hover](components/crops/bill-yearly-hover.png) ![Billing tab (yearly) pressed](components/crops/bill-yearly-pressed.png) ![Billing tab (yearly) opened](components/crops/bill-yearly-opened.png)

#### Plan card
A pricing plan card (name, price, feature list, trial CTA) — the Framer "Card/Card Plans Free" component (~230x154). Read as `plan-card` on the pricing page.

**Values (default).** size 230 x 149.41; padding 18px; background #ffffff `chat.bg.color`; text PolySans Trial Median 22/26.4 400, #000000 `border.focus-ring`; icon 14 x 14, #0000ee; layers ::after rgba(0, 0, 0, 0) 0px none 1.

![Plan card default](components/crops/plan-card-default.png)

#### Plan price
The price figure inside a plan card. Read as `plan-price` on the pricing page.

**Values (default).** size 34 x 38.41; background transparent; text PolySans Trial Median 32/38.4 400, #000000 `border.focus-ring`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan card's "Start … Trial" action to /dashboard/register; its states were measured but it was never followed — no trial was started. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 135 x 39.2; padding 10px 14px; radius 8px; background #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479`; text Inter-Medium 12/19.2 500, #fff9f3 `token.1a71ae8b.0ebf.47f2.9b16.91692b35aeb7` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan feature row
A feature row inside a plan card or the compare table. Read as `plan-row` on the pricing page.

**Values (default).** size 90.2 x 14; background transparent; text Inter 14/14 500, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`.

![Plan feature row default](components/crops/plan-row-default.png)

#### Compare heading
The "Compare Plans" table heading. Read as `compare-h2` on the pricing page.

**Values (default).** size 1200 x 38.41; background transparent; text PolySans Trial Median 32/38.4 400, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`.

![Compare heading default](components/crops/compare-h2-default.png)

### Feature page

A /features/<name> product page (background-remover captured): the display heading, the page CTA and the capability cards.

#### Feature headline
The /features/background-remover page heading. Read as `feat-h1` on the background-remover feature page.

**Values (default).** size 568 x 153.59; background transparent; text PolySans Trial Median 64/76.8 400, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`.

![Feature headline default](components/crops/feat-h1-default.png)

#### Feature CTA
The feature hero's filled "Get Started Now" action — the nav's "Play for free" is the DOM-first match, so the leaf text is tagged in-page. Measured, never followed. Read as `feat-cta` on the background-remover feature page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 178.02 x 48; padding 14px 18px; radius 8px; background #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479`; text Inter 14/14 500, #fff9f3 `token.1a71ae8b.0ebf.47f2.9b16.91692b35aeb7` |
| hover | background #374bbf |
| focus-visible | outline 1px auto #101010, offset 1px |

![Feature CTA default](components/crops/feat-cta-default.png) ![Feature CTA hover](components/crops/feat-cta-hover.png) ![Feature CTA focus-visible](components/crops/feat-cta-focus-visible.png) ![Feature CTA pressed](components/crops/feat-cta-pressed.png)

#### Feature card
A benefit card on the feature page ("Fast", "Inexpensive", "Manual Option"). Read as `feat-card` on the background-remover feature page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1200 x 572.8; background transparent; text PolySans Trial Median 24/28.8 400, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871` |

![Feature card default](components/crops/feat-card-default.png) ![Feature card hover](components/crops/feat-card-hover.png)

#### Feature paragraph
A body paragraph on the feature page. Read as `feat-prose` on the background-remover feature page.

**Values (default).** size 518 x 84; background transparent; text Inter-Medium 20/28 500, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`.

![Feature paragraph default](components/crops/feat-prose-default.png)

### Templates

The /templates gallery: template cards and the category links.

#### Templates headline
The templates gallery heading. Read as `tpl-h1` on the templates page.

**Values (default).** size 149 x 19.2; background transparent; text Inter-Medium 12/19.2 500, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`.

![Templates headline default](components/crops/tpl-h1-default.png)

#### Template tile
A template thumbnail tile on the /templates draggable canvas (a Framer "Row n - m"/"Beauty n - m" tile with artwork) — the gallery is a pan-canvas, not a link grid. Read as `tpl-card` on the templates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 193.93 x 102.31; radius 8px; background transparent; text sans-serif 12/normal 400, #000000 `border.focus-ring` |
| hover | size 187.14 x 102.26 |

![Template tile default](components/crops/tpl-card-default.png) ![Template tile hover](components/crops/tpl-card-hover.png)

#### Template category link
A template-category link; measured, never followed. Read as `tpl-cat` on the templates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 97.61 x 28; padding 8px 12px; background transparent; text Inter-SemiBold 12/12 600, #ffffff `chat.bg.color` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-Gl7qc.framer-vGu9P 97.6x28.0 1px auto rgb(16, 16, 16) offset 1px |

![Template category link default](components/crops/tpl-cat-default.png) ![Template category link hover](components/crops/tpl-cat-hover.png) ![Template category link focus-visible](components/crops/tpl-cat-focus-visible.png) ![Template category link pressed](components/crops/tpl-cat-pressed.png)

### Template marketplace

The /template-marketplace grid: the use-case filter pills and template cards.

#### Marketplace headline
The "New template marketplace" heading. Read as `mk-h1` on the template marketplace page.

**Values (default).** size 185 x 19.2; background transparent; text Inter-Medium 12/19.2 500, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`.

![Marketplace headline default](components/crops/mk-h1-default.png)

#### Marketplace filter
A use-case/style filter pill on the marketplace. Read as `mk-tag` on the template marketplace page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 100 x 23.41; background transparent; text Inter 18/23.4 700, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Marketplace filter default](components/crops/mk-tag-default.png) ![Marketplace filter hover](components/crops/mk-tag-hover.png) ![Marketplace filter pressed](components/crops/mk-tag-pressed.png)

#### Marketplace card
A template card in the marketplace grid (the first thumbnail link over 150px); measured, never followed. Read as `mk-card` on the template marketplace page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 256; radius 8px; background transparent; text Inter 14/14 700, #51cab4 `token.2ff71b15.79ff.4961.a5d5.3c255280b832`; layers div.framer-jDlMw.framer-qt0hyh 47.2x30.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.15) 0px 1px 3px 0px 6px; span.framer-text 35.4x18.2 |
| hover | size 395.52 x 263.68; transform scale(1.03); layers div.framer-jDlMw.framer-qt0hyh 48.6x30.9 rgb(255, 255, 255) rgba(0, 0, 0, 0.15) 0px 1px 3px 0px 6px; span.framer-text 36.5x18.7 |

Child layers that carry the look: div 47.2x30 background #ffffff `chat.bg.color` radius 6px shadow rgba(0, 0, 0, 0.15) 0px 1px 3px 0px; span 35.4x18.2 image linear-gradient(54deg, #1db89b 8%, #2cd1b3 74%).

![Marketplace card default](components/crops/mk-card-default.png) ![Marketplace card hover](components/crops/mk-card-hover.png)

### Learn

The /learn hub: the category filters and article cards.

#### Learn headline
The "Learn about Glorify, Ecom, Design and more" heading. Read as `learn-h1` on the learn page.

**Values (default).** size 768 x 153.59; background transparent; text PolySans Trial Median 64/76.8 400, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`.

![Learn headline default](components/crops/learn-h1-default.png)

#### Learn filter
The "All" category pill on the Learn hub; the leaf text node is tagged in-page because a hasText filter resolves the page wrapper. Read as `learn-cat` on the learn page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 18.41 x 16; background transparent; text Inter-Medium 16/16 500, #fff9f3 `token.1a71ae8b.0ebf.47f2.9b16.91692b35aeb7` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Learn filter default](components/crops/learn-cat-default.png) ![Learn filter hover](components/crops/learn-cat-hover.png) ![Learn filter pressed](components/crops/learn-cat-pressed.png)

#### Article card
A Learn article card (cover, category tag, title) — the card wrapping the first article-title heading; measured, never followed. Read as `learn-card` on the learn page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 433.86; padding 12px; radius 8px; background #fff9f3 `token.1a71ae8b.0ebf.47f2.9b16.91692b35aeb7`; text Inter-Bold 14/19.6 700, #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479`; layers ::after rgba(0, 0, 0, 0) 1px none 1 |
| hover | background #ffffff `chat.bg.color` |

![Article card default](components/crops/learn-card-default.png) ![Article card hover](components/crops/learn-card-hover.png)

#### Article tag
A category tag on an article card. Read as `learn-tag` on the learn page.

**Values (default).** size 84.2 x 28; background transparent; text Inter-SemiBold 12/12 600, #8c8c87 `token.1fe56cfa.d2fd.419f.acc6.c63b3e1e5afa`; layers a.framer-Gl7qc.framer-vGu9P 84.2x28.0 rgb(255, 249, 243) 4px.

Child layers that carry the look: a 84.2x28 background #fff9f3 `token.1a71ae8b.0ebf.47f2.9b16.91692b35aeb7` radius 4px.

![Article tag default](components/crops/learn-tag-default.png)

### Submit a template

The /submit-template page: the guidelines copy and the creator-privileges card.

#### Submit headline
The "Submit your template" heading. Read as `st-h1` on the submit a template page.

**Values (default).** size 1200 x 76.8; background transparent; text PolySans Trial Median 64/76.8 400, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`.

![Submit headline default](components/crops/st-h1-default.png)

#### Privileges card
The "Creator Privileges" card on the submit-a-template page. Read as `st-quote` on the submit a template page.

**Values (default).** size 1200 x 148.8; background transparent; text PolySans Trial Median 24/28.8 400, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`; layers div.framer-ezV4n.framer-V0vyO 369.3x88.0 rgb(238, 250, 248) 16px; div::after.framer-ezV4n.framer-V0vyO 369.328pxx88px T:1px rgb(124, 215, 198) / R:1px rgb(124, 215, 198) / B:1px rgb(124, 215, 198) / L:1px rgb(124, 215, 198) 16px; div::after.framer-hh2qk4 64pxx64px T:1px rgb(81, 202, 180) / R:1px rgb(81, 202, 180) / B:1px rgb(81, 202, 180) / L:1px rgb(81, 202, 180) 8px; div.framer-ezV4n.framer-V0vy.

Child layers that carry the look: div 369.3x88 background #eefaf8 `token.10556817.ac0a.44f7.ae26.ccb76c9fd09b` radius 16px; div::after 369.328pxx88px border 1px #7cd7c6 `token.0bf72244.e448.4725.ab25.338f97c28655` radius 16px; div::after 64pxx64px border 1px #51cab4 `token.2ff71b15.79ff.4961.a5d5.3c255280b832` radius 8px.

![Privileges card default](components/crops/st-quote-default.png)

#### Submit paragraph
A guidelines paragraph on the submit page. Read as `st-prose` on the submit a template page.

**Values (default).** size 718 x 76.78; background transparent; text Inter 16/25.6 500, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`.

![Submit paragraph default](components/crops/st-prose-default.png)

### App sign-in

app.glorify.com/dashboard/login (reached through /welcome) — the signed-out dark sign-in card: e-mail and password fields, the primary 'Sign in' submit (disabled at rest; enabled once both fields hold sample text — never clicked), the Google OAuth button and the sign-up link.

#### App page field
The app body element — the dark field the auth cards and editor chrome sit on. Read as `app-bg` on the app sign-in page.

**Values (default).** size 1440 x 900; background #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7`; text Inter 20/32 500, #ffffff `chat.bg.color`; icon 16 x 16, #6a7ef1 `action.oauth-ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Sign-in headline
The "Sign in to your account" heading (a p leaf) on app.glorify.com/dashboard/login. Read as `login-title` on the app sign-in page.

**Values (default).** size 219 x 32; background transparent; text Inter 20/32 500, #ffffff `chat.bg.color`.

![Sign-in headline default](components/crops/login-title-default.png)

#### Sign-in card
The sign-in form card — the flex column (~352px) holding the e-mail and password fields, the primary submit and the Google OAuth button; tagged by walking up from the e-mail input to the first card-sized ancestor. Read as `login-card` on the app sign-in page.

**Values (default).** size 352 x 384; background transparent; text Inter 20/32 500, #ffffff `chat.bg.color`; icon 16 x 16, #6a7ef1 `action.oauth-ink`; layers div.w-full.justify-center 352.0x48.0 rgb(33, 33, 33); button.button.button-primary 352.0x32.0 T:1px rgb(106, 126, 241) / R:1px rgb(106, 126, 241) / B:1px rgb(106, 126, 241) / L:1px rgb(106, 126, 241) 2px solid rgba(0, 0, 0, 0) offset 2px 8px; hr.w-full.border-light-300 158.5x1.0 T:1px rgb(67, 66, 66); hr.w-full.border-light-300 158.5x1.0 T:1px rgb(67, 66, 66); div.field-container.flex 352.0x32.0 r.

Child layers that carry the look: div 352x48 background #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7`; button 352x32 border 1px #6a7ef1 `action.oauth-ink` radius 8px; hr 158.5x1 border 1px #434242 `token.437b14b7.0164.40e6.a64c.c9076019a119`.

![Sign-in card default](components/crops/login-card-default.png)

#### Email field (sign-in)
The sign-in e-mail input; focused and typed into then cleared — never submitted. Read as `login-field` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 336 x 30; padding 6px 0px; border 1px solid transparent; radius 2px; background transparent; text Inter 12/16 400, #ffffff `chat.bg.color`; transition background-color 0.3s linear, border-color 0.3s linear, color 0.3s linear, fill 0.3s linear, stroke 0.3s linear; placeholder #a7a5a5 `token.521d7dea.ae19.4cea.a86f.413df69ece62` |
| focused, filled | shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px; outline 2px solid transparent, offset 2px |

![Email field (sign-in) default](components/crops/login-field-default.png) ![Email field (sign-in) focused](components/crops/login-field-focused.png) ![Email field (sign-in) filled](components/crops/login-field-filled.png)

#### Password field (sign-in)
The sign-in password input; focused and typed into then cleared — never submitted. Read as `login-pass` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 313.09 x 30; padding 6px 0px; border 1px solid transparent; radius 2px; background transparent; text Inter 12/16 400, #ffffff `chat.bg.color`; transition background-color 0.3s linear, border-color 0.3s linear, color 0.3s linear, fill 0.3s linear, stroke 0.3s linear; placeholder #a7a5a5 `token.521d7dea.ae19.4cea.a86f.413df69ece62` |
| focused, filled | shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px; outline 2px solid transparent, offset 2px |

![Password field (sign-in) default](components/crops/login-pass-default.png) ![Password field (sign-in) focused](components/crops/login-pass-focused.png) ![Password field (sign-in) filled](components/crops/login-pass-filled.png)

#### Sign-in submit
The primary "Sign in" submit; every state was measured but the button was never clicked — nothing was submitted. `enabled` is the fill it paints once sample text sits in both fields. Read as `login-submit` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 352 x 32; padding 8px 16px; border 1px solid transparent; radius 8px; background #868484 `token.9c080050.c197.4d22.857c.662351924483`; outline 2px solid transparent, offset 2px; text Inter 12/16 500, #ffffff `chat.bg.color`; transition all 0.25s linear |
| enabled | background #6a7ef1 `action.oauth-ink` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Sign-in submit default](components/crops/login-submit-default.png) ![Sign-in submit hover](components/crops/login-submit-hover.png) ![Sign-in submit pressed](components/crops/login-submit-pressed.png) ![Sign-in submit enabled](components/crops/login-submit-enabled.png)

#### Google OAuth button
The "Sign in with Google" OAuth button; measured, never activated. Read as `login-google` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 352 x 32; padding 8px 16px; border 1px solid #6a7ef1 `action.oauth-ink`; radius 8px; background transparent; outline 2px solid transparent, offset 2px; text Inter 12/16 500, #6a7ef1 `action.oauth-ink`; transition all 0.25s linear; icon 16 x 16, #6a7ef1 `action.oauth-ink` |
| hover | background #6a7ef1 `action.oauth-ink`; text Inter 12/16 500, #ffffff `chat.bg.color`; icon 16 x 16, #ffffff `chat.bg.color` |
| focus-visible | border 1px solid #272b42 `primary.700`; shadow #272b42 0px 0px 0px 1px |
| pressed | background #6a7ef1 `action.oauth-ink`; text Inter 12/16 500, #ffffff `chat.bg.color`; icon 16 x 16, #ffffff `chat.bg.color` |

![Google OAuth button default](components/crops/login-google-default.png) ![Google OAuth button hover](components/crops/login-google-hover.png) ![Google OAuth button focus-visible](components/crops/login-google-focus-visible.png) ![Google OAuth button pressed](components/crops/login-google-pressed.png)

#### Forgot/remember control
The "Forgot password?" link or "Remember me" checkbox label on the sign-in card; measured, never followed. Read as `login-forgot` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 113 x 16; padding 0px 0px 0px 24px; background transparent; text Inter 12/16 500, #ffffff `chat.bg.color`; icon 16 x 16, #a7a5a5 `token.521d7dea.ae19.4cea.a86f.413df69ece62`; layers ::after rgb(33, 33, 33) 0px none 1; label::after.selection-control.checkbox 12pxx12px rgb(33, 33, 33) 9999px; input.hidden 0.0x0.0 rgb(255, 255, 255) T:1px rgb(107, 114, 128) / R:1px rgb(107, 114, 128) / B:1px rgb(107, 114, 128) / L:1px rgb(107, 114, 128) |
| hover | icon 16 x 16, #ffffff `chat.bg.color` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: label::after 12pxx12px background #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7` radius 9999px; input 0x0 background #ffffff `chat.bg.color` border 1px #6b7280.

![Forgot/remember control default](components/crops/login-forgot-default.png) ![Forgot/remember control hover](components/crops/login-forgot-hover.png) ![Forgot/remember control pressed](components/crops/login-forgot-pressed.png)

#### Sign-up link
The "Sign up" link beside the sign-in form; measured, never followed. Read as `login-signup` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 46 x 16; background transparent; text Inter 12/16 400, #6a7ef1 `action.oauth-ink` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Sign-up link default](components/crops/login-signup-default.png) ![Sign-up link hover](components/crops/login-signup-hover.png) ![Sign-up link pressed](components/crops/login-signup-pressed.png)

### App sign-up

app.glorify.com/dashboard/register — the signed-out dark sign-up card: name, e-mail and password fields, the primary submit and the Google button. Measured as a form, never submitted.

#### Sign-up headline
The "Create your account" heading (a p leaf) on app.glorify.com/dashboard/register. Read as `reg-title` on the app sign-up page.

**Values (default).** size 199 x 32; background transparent; text Inter 20/32 500, #ffffff `chat.bg.color`.

![Sign-up headline default](components/crops/reg-title-default.png)

#### Name field (sign-up)
The sign-up "Full name" input; focused and typed into then cleared — never submitted. Read as `reg-name` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 336 x 30; padding 6px 0px; border 1px solid transparent; radius 2px; background transparent; text Inter 12/16 400, #ffffff `chat.bg.color`; transition background-color 0.3s linear, border-color 0.3s linear, color 0.3s linear, fill 0.3s linear, stroke 0.3s linear; placeholder #a7a5a5 `token.521d7dea.ae19.4cea.a86f.413df69ece62` |
| focused, filled | shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px; outline 2px solid transparent, offset 2px |

![Name field (sign-up) default](components/crops/reg-name-default.png) ![Name field (sign-up) focused](components/crops/reg-name-focused.png) ![Name field (sign-up) filled](components/crops/reg-name-filled.png)

#### Email field (sign-up)
The sign-up e-mail input; focused and typed into then cleared — never submitted. Read as `reg-email` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 336 x 30; padding 6px 0px; border 1px solid transparent; radius 2px; background transparent; text Inter 12/16 400, #ffffff `chat.bg.color`; transition background-color 0.3s linear, border-color 0.3s linear, color 0.3s linear, fill 0.3s linear, stroke 0.3s linear; placeholder #a7a5a5 `token.521d7dea.ae19.4cea.a86f.413df69ece62` |
| focused, filled | shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px; outline 2px solid transparent, offset 2px |

![Email field (sign-up) default](components/crops/reg-email-default.png) ![Email field (sign-up) focused](components/crops/reg-email-focused.png) ![Email field (sign-up) filled](components/crops/reg-email-filled.png)

#### Password field (sign-up)
The sign-up password input; focused and typed into then cleared — never submitted. Read as `reg-pass` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 313.09 x 30; padding 6px 0px; border 1px solid transparent; radius 2px; background transparent; text Inter 12/16 400, #ffffff `chat.bg.color`; transition background-color 0.3s linear, border-color 0.3s linear, color 0.3s linear, fill 0.3s linear, stroke 0.3s linear; placeholder #a7a5a5 `token.521d7dea.ae19.4cea.a86f.413df69ece62` |
| focused, filled | shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px; outline 2px solid transparent, offset 2px |

![Password field (sign-up) default](components/crops/reg-pass-default.png) ![Password field (sign-up) focused](components/crops/reg-pass-focused.png) ![Password field (sign-up) filled](components/crops/reg-pass-filled.png)

#### Sign-up submit
The primary sign-up submit; its states were measured but the button was never clicked — no account was created. Read as `reg-submit` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 352 x 32; padding 8px 16px; border 1px solid transparent; radius 8px; background #868484 `token.9c080050.c197.4d22.857c.662351924483`; outline 2px solid transparent, offset 2px; text Inter 12/16 500, #ffffff `chat.bg.color`; transition all 0.25s linear |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Sign-up submit default](components/crops/reg-submit-default.png) ![Sign-up submit hover](components/crops/reg-submit-hover.png) ![Sign-up submit pressed](components/crops/reg-submit-pressed.png)

#### Google OAuth button (sign-up)
The "Sign up with Google" button; measured, never activated. Read as `reg-google` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 352 x 32; padding 8px 16px; border 1px solid #6a7ef1 `action.oauth-ink`; radius 8px; background transparent; outline 2px solid transparent, offset 2px; text Inter 12/16 500, #6a7ef1 `action.oauth-ink`; transition all 0.25s linear; icon 16 x 16, #6a7ef1 `action.oauth-ink` |
| hover | background #6a7ef1 `action.oauth-ink`; text Inter 12/16 500, #ffffff `chat.bg.color`; icon 16 x 16, #ffffff `chat.bg.color` |
| focus-visible | border 1px solid #272b42 `primary.700`; shadow #272b42 0px 0px 0px 1px |
| pressed | background #6a7ef1 `action.oauth-ink`; text Inter 12/16 500, #ffffff `chat.bg.color`; icon 16 x 16, #ffffff `chat.bg.color` |

![Google OAuth button (sign-up) default](components/crops/reg-google-default.png) ![Google OAuth button (sign-up) hover](components/crops/reg-google-hover.png) ![Google OAuth button (sign-up) focus-visible](components/crops/reg-google-focus-visible.png) ![Google OAuth button (sign-up) pressed](components/crops/reg-google-pressed.png)

#### Terms link
The terms/privacy link under the sign-up form; measured, never followed. Read as `reg-terms` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 117 x 15; background transparent; text Inter 12/16 500, #6a7ef1 `action.oauth-ink` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.text-link-1.text-primary-300 117.0x15.0 1px auto rgb(16, 16, 16) offset 1px |

![Terms link default](components/crops/reg-terms-default.png) ![Terms link hover](components/crops/reg-terms-hover.png) ![Terms link focus-visible](components/crops/reg-terms-focus-visible.png) ![Terms link pressed](components/crops/reg-terms-pressed.png)

### Anonymous editor

app.glorify.com/designer/use-template/0 — the product's own Play-for-free path: the SPA creates a scratch /file/<id> and paints the upload onboarding, the Craft dialog behind 'Try with Placeholder Image', and the canvas chrome — header, tool rail, inspector — of the real editor.

#### Onboarding headline
The "Generate designs for your campaign" heading on the anonymous editor's upload screen. Read as `ob-title` on the anonymous editor page.

**Values (default).** size 346 x 24; background transparent; text Inter 16/24 500, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`.

![Onboarding headline default](components/crops/ob-title-default.png)

#### Upload dropzone
The onboarding upload dropzone — the card-sized ancestor of the "Drag and drop…" prompt; measured at rest — no file was ever chosen or uploaded. Read as `ob-drop` on the anonymous editor page.

**Values (default).** size 398 x 200; radius 12px; background #ffffff `chat.bg.color`; text Inter 12/16 500, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`; transition all 0.25s linear; icon 20 x 20, #a7a5a5 `token.521d7dea.ae19.4cea.a86f.413df69ece62`.

![Upload dropzone default](components/crops/ob-drop-default.png)

#### Placeholder Image card
The "Try with Placeholder Image" card — the product's own demo path into the canvas; measured, and only ever activated through its own spec flow. Read as `ob-ph` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 206 x 46; background transparent; text Inter 12/16 600, #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Placeholder Image card default](components/crops/ob-ph-default.png) ![Placeholder Image card hover](components/crops/ob-ph-hover.png) ![Placeholder Image card pressed](components/crops/ob-ph-pressed.png)

#### Own-start link
The "I'll get started on my own" link (it bounces to /dashboard/register signed out); measured, never followed. Read as `ob-own` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 142 x 16; background transparent; text Inter 12/16 500, #111111 `token.4afff1e1.ad66.4449.a126.34071669c871` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Own-start link default](components/crops/ob-own-default.png) ![Own-start link hover](components/crops/ob-own-hover.png) ![Own-start link pressed](components/crops/ob-own-pressed.png)

#### Editor header
The editor top bar: file name dropdown, Login/Signup, zoom, Share, Download. Read as `ed-header` on the anonymous editor page.

**Values (default).** size 545 x 56; background transparent; text Inter 12/16 400, #ffffff `chat.bg.color`; transition all 0.3s linear; icon 20 x 20, #ffffff `chat.bg.color`; layers div.panel-header-side-wrapper.sm:w-[fit-content] 331.0x56.0 rgb(33, 33, 33) T:1px rgb(67, 66, 66) / R:1px rgb(67, 66, 66) / B:1px rgb(67, 66, 66) / L:1px rgb(67, 66, 66) 12px; div.panel-header-side.flex 75.0x50.0 rgb(33, 33, 33) 12px; button.default.dropdown__trigger 58.0x42.0 T:1px rgba(0, 0, 0, 0) / R:1px rgba(0, 0, 0, 0) / B:1px rgba(0, 0, 0, 0) / L:1px rgba(0, 0, 0, 0) 2px solid rgba(0, 0, 0, .

Child layers that carry the look: div 331x56 background #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7` border 1px #434242 `token.437b14b7.0164.40e6.a64c.c9076019a119` radius 12px; div 75x50 background #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7` radius 12px; button 58x42 border 1px transparent radius 8px.

![Editor header default](components/crops/ed-header-default.png)

#### Editor Login button
The outlined "Login" button in the editor header; measured, never clicked. Read as `ed-login` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 65 x 32; padding 8px 16px; border 1px solid #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479`; radius 8px; background transparent; outline 2px solid transparent, offset 2px; text Inter 12/16 500, #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479`; transition all 0.25s linear |
| focus-visible | border 1px solid #272b42 `primary.700`; shadow #272b42 0px 0px 0px 1px |
| pressed | background #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479`; text Inter 12/16 500, #ffffff `chat.bg.color` |

![Editor Login button default](components/crops/ed-login-default.png) ![Editor Login button hover](components/crops/ed-login-hover.png) ![Editor Login button focus-visible](components/crops/ed-login-focus-visible.png) ![Editor Login button pressed](components/crops/ed-login-pressed.png)

#### Editor Signup button
The filled "Signup" button in the editor header; measured, never clicked. Read as `ed-signup` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 73 x 32; padding 8px 16px; border 1px solid transparent; radius 8px; background #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479`; outline 2px solid transparent, offset 2px; text Inter 12/16 500, #ffffff `chat.bg.color`; transition all 0.25s linear |
| focus-visible | border 1px solid #272b42 `primary.700`; shadow #272b42 0px 0px 0px 1px |
| pressed | background #374bbe `token.72222110.6151.4c46.b86b.6c9b034c5d6e` |

![Editor Signup button default](components/crops/ed-signup-default.png) ![Editor Signup button hover](components/crops/ed-signup-hover.png) ![Editor Signup button focus-visible](components/crops/ed-signup-focus-visible.png) ![Editor Signup button pressed](components/crops/ed-signup-pressed.png)

#### Share button
The "Share" button in the editor header; measured, never clicked. Read as `ed-share` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 60 x 32; padding 0px 12px; border 1px solid #434242 `token.437b14b7.0164.40e6.a64c.c9076019a119`; radius 8px; background #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7`; outline 2px solid transparent, offset 2px; text Inter 12/16 500, #ffffff `chat.bg.color`; transition none 0.3s linear |
| pressed | border 1px solid #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479`; background #272b42 `primary.700` |

![Share button default](components/crops/ed-share-default.png) ![Share button hover](components/crops/ed-share-hover.png) ![Share button focus-visible](components/crops/ed-share-focus-visible.png) ![Share button pressed](components/crops/ed-share-pressed.png)

#### Download button
The "Download" button in the editor header; measured, never clicked. Read as `ed-download` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 82 x 32; padding 0px 12px; radius 8px; background #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479`; outline 2px solid transparent, offset 2px; text Inter 12/16 500, #ffffff `chat.bg.color`; transition all 0.3s linear |
| pressed | background #475beb `active.interactive` |

![Download button default](components/crops/ed-download-default.png) ![Download button hover](components/crops/ed-download-hover.png) ![Download button focus-visible](components/crops/ed-download-focus-visible.png) ![Download button pressed](components/crops/ed-download-pressed.png)

#### Zoom control
The zoom-percentage dropdown trigger in the editor header; measured, never toggled. Read as `ed-zoom` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 72 x 32; padding 8px; radius 8px; background transparent; outline 2px solid transparent, offset 2px; text Inter 12/16 500, #ffffff `chat.bg.color`; transition none 0.3s linear; icon 16 x 16, #ffffff `chat.bg.color`; layers button.p-2.dropdown__trigger 72.0x32.0 2px solid rgba(0, 0, 0, 0) offset 2px 8px |
| pressed | background #272b42 `primary.700`; icon 16 x 16, #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479`; layers none |

Child layers that carry the look: button 72x32 radius 8px.

![Zoom control default](components/crops/ed-zoom-default.png) ![Zoom control hover](components/crops/ed-zoom-hover.png) ![Zoom control focus-visible](components/crops/ed-zoom-focus-visible.png) ![Zoom control pressed](components/crops/ed-zoom-pressed.png)

#### Tool rail button
A labelled tool-rail button (Text/Video/Elements…) on the editor's left rail — 48x48 .dropdown-toolbar buttons over a 20px icon; its flyout was never opened. Read as `ed-tool` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 48 x 48; border 1px solid transparent; radius 8px; background #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7`; outline 2px solid transparent, offset 2px; text Inter 10/16 400, #a7a5a5 `token.521d7dea.ae19.4cea.a86f.413df69ece62`; transition all 0.3s linear; icon 20 x 20, #a7a5a5 `token.521d7dea.ae19.4cea.a86f.413df69ece62` |
| pressed | background #272b42 `primary.700`; text Inter 10/16 400, #ffffff `chat.bg.color`; icon 20 x 20, #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479` |

![Tool rail button default](components/crops/ed-tool-default.png) ![Tool rail button hover](components/crops/ed-tool-hover.png) ![Tool rail button focus-visible](components/crops/ed-tool-focus-visible.png) ![Tool rail button pressed](components/crops/ed-tool-pressed.png)

#### Active tool button
The selected tool on the left rail (Pointer, marked dropdown--icon-active). Read as `ed-tool-active` on the anonymous editor page.

**Values (default).** size 48 x 48; border 1px solid #475beb `active.interactive`; radius 8px; background transparent; text Inter 10/16 400, #ffffff `chat.bg.color`; icon 20 x 20, #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479`.

![Active tool button default](components/crops/ed-tool-active-default.png)

#### Inspector panel
The right-hand inspector (.panel--inspector, ~280px): EDIT/LAYERS/PAGES tabs over the Page Background and Color controls. Read as `ed-inspector` on the anonymous editor page.

**Values (default).** size 280 x 824; border 1px solid #434242 `token.437b14b7.0164.40e6.a64c.c9076019a119`; radius 12px; background #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7`; text Inter 11/16 600, #ffffff `chat.bg.color`; transition all 0.3s linear; icon 20 x 20, #ffffff `chat.bg.color`.

![Inspector panel default](components/crops/ed-inspector-default.png)

#### Inspector tab
The EDIT inspector tab; opened was measured after switching to LAYERS — a local UI toggle. Read as `ed-tab` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 92.67 x 40; background #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7`; text Inter 11/16 600, #ffffff `chat.bg.color`; layers ::after rgb(69, 94, 237) 0px none 1 |
| opened | layers ::after rgb(69, 94, 237) 0px none 0 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Inspector tab default](components/crops/ed-tab-default.png) ![Inspector tab pressed](components/crops/ed-tab-pressed.png) ![Inspector tab opened](components/crops/ed-tab-opened.png)

#### Layers tab
The LAYERS inspector tab; measured at rest. Read as `ed-tab-layers` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 92.66 x 40; background #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7`; text Inter 11/16 600, #ffffff `chat.bg.color`; layers ::after rgb(69, 94, 237) 0px none 1 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Layers tab default](components/crops/ed-tab-layers-default.png) ![Layers tab hover](components/crops/ed-tab-layers-hover.png) ![Layers tab pressed](components/crops/ed-tab-layers-pressed.png)

#### Inspector colour field
The page-background colour input in the inspector (the hex field, placeholder "000"); focused, never typed into. Read as `ed-color` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 86 x 28; padding 8px 4px 8px 26px; border 1px solid #434242 `token.437b14b7.0164.40e6.a64c.c9076019a119`; radius 8px; background #323232 `token.a4c9cff4.c09a.4573.ac8b.b10161e09446`; text Inter 12/16 400, #ffffff `chat.bg.color`; transition background-color 0.3s linear, border-color 0.3s linear, color 0.3s linear, fill 0.3s linear, stroke 0.3s linear; placeholder #868484 `token.9c080050.c197.4d22.857c.662351924483` |
| focused | shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px; outline 2px solid transparent, offset 2px |

![Inspector colour field default](components/crops/ed-color-default.png) ![Inspector colour field focused](components/crops/ed-color-focused.png)

#### Craft dialog
The "Craft Professional Assets" dialog (.modal__content): brand name, product description, the style grid, the image pane and "Add to canvas". Read as `ed-craft` on the anonymous editor page.

**Values (default).** size 792 x 640; radius 16px; background #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7`; shadow rgba(0, 0, 0, 0.1) 0px 1px 10px 0px; text Inter 12/16 600, #ffffff `chat.bg.color`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #ffffff `chat.bg.color`.

![Craft dialog default](components/crops/ed-craft-default.png)

#### Brand-name field
The "Enter your brand name" textarea in the Craft dialog; focused and typed into then cleared — never used. Read as `ed-craft-field` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 307.59 x 32; padding 8px 12px; border 1px solid #434242 `token.437b14b7.0164.40e6.a64c.c9076019a119`; radius 8px; background #323232 `token.a4c9cff4.c09a.4573.ac8b.b10161e09446`; text Inter 12/16 400, #ffffff `chat.bg.color`; placeholder #868484 `token.9c080050.c197.4d22.857c.662351924483` |
| focused, filled | border 1px solid #475beb `active.interactive`; background #272b42 `primary.700`; shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px; outline 2px solid transparent, offset 2px |

![Brand-name field default](components/crops/ed-craft-field-default.png) ![Brand-name field focused](components/crops/ed-craft-field-focused.png) ![Brand-name field filled](components/crops/ed-craft-field-filled.png)

#### Description area
The "Write a short description about your product" textarea; focused and typed into then cleared — never used. Read as `ed-craft-area` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 307.59 x 73; padding 8px 12px; border 1px solid #434242 `token.437b14b7.0164.40e6.a64c.c9076019a119`; radius 8px; background #323232 `token.a4c9cff4.c09a.4573.ac8b.b10161e09446`; text Inter 12/16 400, #ffffff `chat.bg.color`; placeholder #868484 `token.9c080050.c197.4d22.857c.662351924483` |
| focused, filled | border 1px solid #475beb `active.interactive`; background #272b42 `primary.700`; shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px; outline 2px solid transparent, offset 2px |

![Description area default](components/crops/ed-craft-area-default.png) ![Description area focused](components/crops/ed-craft-area-focused.png) ![Description area filled](components/crops/ed-craft-area-filled.png)

#### Style card
A style card in the Craft dialog grid (Modern); opened is the selected state after clicking it — a local UI toggle that enables "Add to canvas". Read as `ed-craft-style` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 97.19 x 106; padding 8px; border 1px solid transparent; radius 8px; background #3e261d; text Inter 12/16 400, #ffffff `chat.bg.color`; transition all 0.25s linear |
| opened | border 1px solid #b53d11 `border.style-selected-border` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Style card default](components/crops/ed-craft-style-default.png) ![Style card hover](components/crops/ed-craft-style-hover.png) ![Style card pressed](components/crops/ed-craft-style-pressed.png) ![Style card opened](components/crops/ed-craft-style-opened.png)

#### Add to canvas
The Craft dialog's primary submit — disabled until a style is picked; `enabled` is the fill after the style click. The button itself was never pressed in this pass. Read as `ed-add` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: enabled) | size 424.41 x 40; padding 8px 16px; border 1px solid transparent; radius 8px; background #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479`; outline 2px solid transparent, offset 2px; text Inter 12/16 500, #ffffff `chat.bg.color`; transition all 0.25s linear |
| hover | background #374bbe `token.72222110.6151.4c46.b86b.6c9b034c5d6e` |
| focus-visible | border 1px solid #272b42 `primary.700`; shadow #272b42 0px 0px 0px 1px |
| pressed | background #374bbe `token.72222110.6151.4c46.b86b.6c9b034c5d6e` |

![Add to canvas default](components/crops/ed-add-default.png) ![Add to canvas hover](components/crops/ed-add-hover.png) ![Add to canvas focus-visible](components/crops/ed-add-focus-visible.png) ![Add to canvas pressed](components/crops/ed-add-pressed.png) ![Add to canvas enabled](components/crops/ed-add-enabled.png)

#### Replace image button
The "Replace" button on the Craft dialog's image pane; measured, never clicked. Read as `ed-replace` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 104 x 32; padding 8px 16px; border 1px solid transparent; radius 8px; background #ffffff `chat.bg.color`; outline 2px solid transparent, offset 2px; text Inter 12/16 500, #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7`; transition all 0.25s linear; icon 16 x 16, #212121 `token.71ff440c.ed97.42a2.b452.db1bf5b85fb7` |
| hover | background #a7a5a5 `token.521d7dea.ae19.4cea.a86f.413df69ece62` |
| focus-visible | border 1px solid #323232 `token.a4c9cff4.c09a.4573.ac8b.b10161e09446`; shadow #323232 0px 0px 0px 1px |
| pressed | background #a7a5a5 `token.521d7dea.ae19.4cea.a86f.413df69ece62` |

![Replace image button default](components/crops/ed-replace-default.png) ![Replace image button hover](components/crops/ed-replace-hover.png) ![Replace image button focus-visible](components/crops/ed-replace-focus-visible.png) ![Replace image button pressed](components/crops/ed-replace-pressed.png)

#### Dialog close
The Craft dialog's own close button; measured, never clicked. Read as `ed-close` on the anonymous editor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 32; padding 8px; radius 8px; background transparent; outline 2px solid transparent, offset 0px; text Inter 14/20 400, #ffffff `chat.bg.color`; transition all 0.25s linear; icon 16 x 16, #ffffff `chat.bg.color`; layers button.button-icon.group 32.0x32.0 2px solid rgba(0, 0, 0, 0) offset 0px 8px |
| focus-visible | background #434242 `token.437b14b7.0164.40e6.a64c.c9076019a119`; outline 2px solid #646363 `token.5dd49439.e215.4b63.80c0.703cbaec2c75`, offset 0px; layers none |
| pressed | background #434242 `token.437b14b7.0164.40e6.a64c.c9076019a119`; layers none |

Child layers that carry the look: button 32x32 radius 8px.

![Dialog close default](components/crops/ed-close-default.png) ![Dialog close hover](components/crops/ed-close-hover.png) ![Dialog close focus-visible](components/crops/ed-close-focus-visible.png) ![Dialog close pressed](components/crops/ed-close-pressed.png)

### Mobile (390 wide)

The phone surface at 390 wide: the header, the burger menu, the masthead and the hero CTA.

#### Mobile top bar
The phone header at 390 wide: wordmark, the burger and the actions that survive the width. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 390 x 64; background #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`; text Inter 9/10.8 700, #fff9f3 `token.1a71ae8b.0ebf.47f2.9b16.91692b35aeb7`; icon 75 x 24, #0000ee.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile burger
The nav burger at 390 wide (the 60x60 "Menu Icon" — the overlay it opens is the [data-framer-name="Menu"] panel); opened was measured after tapping it. Read as `m-burger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 60 x 60; background transparent; text sans-serif 12/normal 400, #000000 `border.focus-ring`; layers div.framer-17rl7jd 20.0x2.0 rgb(64, 64, 64) 10px; div.framer-c8jx7r 20.0x2.0 rgb(64, 64, 64) 10px |
| opened | layers div.framer-17rl7jd 15.6x15.6 rgb(64, 64, 64) 50% / 500%; div.framer-c8jx7r 15.6x15.6 rgb(64, 64, 64) 50% / 500% |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 20x2 background #404040 radius 10px; div 20x2 background #404040 radius 10px.

![Mobile burger default](components/crops/m-burger-default.png) ![Mobile burger hover](components/crops/m-burger-hover.png) ![Mobile burger pressed](components/crops/m-burger-pressed.png) ![Mobile burger opened](components/crops/m-burger-opened.png)

#### Mobile menu link
A link inside the opened mobile nav menu. Read as `m-menu-link` on the home page at 390 wide.

**Values (default).** size 75 x 24; background transparent; text sans-serif 12/normal 400, #0000ee; icon 75 x 24, #0000ee.

![Mobile menu link default](components/crops/m-menu-link-default.png)

#### Mobile hero headline
The hero display heading at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 350 x 172.81; background transparent; text PolySans Trial Median 36/43.2 400, #ffffff `chat.bg.color`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The hero action at 390 wide — the same outlined ghost as desktop, centred under the hero copy (the DOM-first "Play for free" is the menu overlay's full-width filled button, so the leaf text is tagged in-page). Measured, never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 119.41 x 46; padding 14px 18px; radius 8px; background transparent; text Inter 14/14 500, #ffffff `chat.bg.color`; layers ::after rgba(0, 0, 0, 0) 1px none 1; a::after.framer-13l81z2.framer-19c9wqe 119.406pxx46px T:1px rgb(69, 94, 237) / R:1px rgb(69, 94, 237) / B:1px rgb(69, 94, 237) / L:1px rgb(69, 94, 237) 8px |
| hover | opacity 0.8 |
| focus-visible | outline 1px auto #101010, offset 1px; layers ::after rgba(0, 0, 0, 0) 1px none 1; a.framer-13l81z2.framer-19c9wqe 119.4x46.0 1px auto rgb(16, 16, 16) offset 1px 8px; a::after.framer-13l81z2.framer-19c9wqe 119.406pxx46px T:1px rgb(69, 94, 237) / R:1px rgb(69, 94, 237) / B:1px rgb(69, 94, 237) / L:1px rgb(69, 94, 237) 8px |

Child layers that carry the look: a::after 119.406pxx46px border 1px #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479` radius 8px.

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

### Footer

The marketing footer: sitemap columns, legal links and social marks.

#### Footer
The marketing footer: sitemap columns, legal and social links. Read as `footer-col` on the home page.

**Values (default).** size 1440 x 916.39; padding 48px 48px 0px 48px; background #111111 `token.4afff1e1.ad66.4449.a126.34071669c871`; text Inter 9/10.8 700, #111110 `token.e4a486da.0f3e.4f0f.a156.7359e80ab5ee`; icon 100 x 32, #0000ee.

![Footer default](components/crops/footer-col-default.png)

#### Footer link
A link inside the marketing footer; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 113.2 x 17; background transparent; text Inter 14/19.6 500, #c0bcb8 `token.f89db159.2d55.481a.856f.4b4f2bdd6086`; transition color 0.3s cubic-bezier(0.44, 0, 0.56, 1) |
| hover | text Inter 14/19.6 500, #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-text.framer-styles-preset-e6xapj 113.2x17.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Inter 14/19.6 500, #455eed `token.63f7635c.4044.4753.b791.268bd3d1a479` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Glorify wordmark, the feature-card glyphs, the editor tool-rail icons and the template artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Glorify's product is the design workspace: every post-login surface — saved projects, the real editor on a user's files, brand kit, dashboards and billing — needs an account and was never reached. app.glorify.com/dashboard/login and /dashboard/register are the auth surfaces a signed-out visitor sees, and they were measured as forms, never submitted. The anonymous editor at /designer/use-template/0 is genuinely public — the marketing 'Play for free' action opens it on a scratch file the SPA creates — and it paints the real chrome (header, tool rail, inspector) around the onboarding and Craft dialog; deeper editor work (saving, sharing, downloading, the tool flyouts) is the product's own demo path or needs the account. The product mocks inside the marketing cards are illustrations, not the product.

### Pages

- **The account.** Every post-login surface was never reached; the sign-in and sign-up forms were measured and typed into then cleared — 'Sign in', 'Sign up' and the OAuth buttons were never pressed, and what a submitted form returns is unverified.
- **Purchase.** Plan CTAs ('Start Basic/Pro/Business Trial', 'Book a demo') were measured, never followed; no checkout or trial flow was started.
- **Feature and comparison routes** beyond the captured set (the other /features/* pages, the alternative pages, the rest of /learn's articles) are the same templates, unmeasured; one example of each family was captured.
- **Editor depth.** On the anonymous scratch file the Craft dialog was opened, a style picked, and 'Add to canvas' pressed once to paint the canvas state, which ran a server-side AI generation (a boundary since 2026-11: the screenshot pass no longer presses it). Share, Download, the tool flyouts and the sign-in nudges inside the editor were measured, never activated.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Error, loading and validation states** were not seen on the public surface — the forms were never submitted. The sign-in submit's disabled fill is measured at rest and its enabled fill with sample text in both fields.
- **The editor's deeper states** (canvas editing gestures, layer selection beyond the tab switch, generation progress) are beyond what a state list can capture; the canvas state is a screenshot.

### Themes

The marketing site paints light only — no theme toggle and no `prefers-color-scheme` dark rule was observed on glorify.com (`color-scheme: normal`). The app surface genuinely paints dark chrome — the auth cards and the editor are dark signed out — and its tokens live in the separate `app` set. No theme switcher was observed on either host; the SPA's `--light-*` and `--dark-*` ramps are both declared on the same :root, not alternate themes.

### Fonts

- The served faces (the marketing site's Framer-bundled fonts and the app's own faces, listed in raw/css-vars.json `fonts`) are the product's; the style guide falls back to system sans.

### Screenshots

- The product mocks, screenshots-in-screenshots and logo walls are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article copy, testimonial names and the changelog text are the product's content; only frames and components were measured.
