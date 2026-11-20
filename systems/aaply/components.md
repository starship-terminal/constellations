# aaply components

The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from aaply.app on 2026-11-10, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was bought, downloaded, signed into, sent or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (51 components, 90 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Poppins 57/60 700, #000000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (89 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (the marketing site is light, with a black footer band). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). The app host go.aaply.app returned "Not found" on /login, /sign, /signup and /workspace/demo, so the authenticated product is listed as an unreachable boundary, not captured.

| Surface | URL | Screenshots |
|---|---|---|
| Home. Display headline, hero CTAs, product mockup, chat bubbles, black footer; full page. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Features. Numbered workflow steps, product panels, mega demo CTA; full page. | `/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| Value. Display heading, value cells; full page. | `/value` | [default](screenshots/value-light-default.png), [full](screenshots/value-light-full.png) |
| Pricing. Billing rail, plan cards, feature table; yearly state and full page. | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [yearly](screenshots/pricing-light-yearly.png) |
| Reviews. Featured slide, testimonial grid; full page. | `/reviews` | [default](screenshots/reviews-light-default.png), [full](screenshots/reviews-light-full.png) |
| Our story. The editorial column; full page. | `/our-story` | [default](screenshots/our-story-light-default.png), [full](screenshots/our-story-light-full.png) |
| Team. Display heading, member grid; full page. | `/team` | [default](screenshots/team-light-default.png), [full](screenshots/team-light-full.png) |
| Figma plugin. Display heading, export steps; full page. | `/figma_plugin` | [default](screenshots/figma-plugin-light-default.png), [full](screenshots/figma-plugin-light-full.png) |
| Home at 390: burger, hero, CTAs; full page. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing at 390; full page. | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Features at 390; full page. | `/features` | [default](screenshots/mobile-features-light-default.png), [full](screenshots/mobile-features-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Monthly billing | pricing | the Monthly segment pressed (client-side state, nothing sent) | [billing-monthly-on](#monthly-option-selected), [plan-price-monthly](#plan-price-monthly) |
| App host | go.aaply.app | nav Log in / Sign up / demo links followed to the app host | every route returned "Not found" — an unreachable boundary, not captured |
| Chat bubbles | home / features / value | static annotation bubbles baked into the marketing pages | measured as elements ([chat-bubble](#chat-annotation-bubble)); no live widget was opened |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 10 components were given a real keyboard focus. 10 draw a ring: `logo` (3px auto #2015ff, offset 4px), `nav-link` (3px auto #2015ff, offset 4px), `nav-login` (3px auto #2015ff, offset 4px), `nav-signup` (3px auto #2015ff, offset 4px), `cta-signup-free` (3px auto #2015ff, offset 4px), `cta-demo` (3px auto #2015ff, offset 4px), `footer-link` (3px auto #2015ff, offset 4px), `social-icon` (3px auto #2015ff, offset 4px), `plan-cta` (3px auto #2015ff, offset 4px), `mega-demo-cta` (3px auto #2015ff, offset 4px). The other 0 draw none, so a keyboard user sees no change: . Focus could not be driven to `compare-cta` — its focus state is recorded as not captured.

**Pressed.** Only the nav Sign up pill swaps under :active — black to lime, the same as its hover; the hero and mega demo pills hold black through hover and pressed, and the lime pills hold flat; see the per-component state rows.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease-in-out` | background-color, border-color, box-shadow, color | billing-monthly, billing-monthly-on, billing-yearly, chat-bubble, compare-cta, cta-demo, cta-signup-free, early-birds and more |
| 0.3s | `ease-in-out` | all | footer-link |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Nav bar](#nav-bar) | 1200 x 166 | - | 40px | #ffffff `white` | none | 0 |
| [Plan card (Free)](#plan-card-free) | 561 x 618 | - | 36px | #ffffff `white` | none | 0 |
| [Plan card (Plus)](#plan-card-plus) | 561 x 618 | - | 36px | #e6e51e `lime` | none | 0 |
| [Review slide](#review-slide) | 1157 x 418 | - | 40px | #e7e51e `lime-slide` | none | 0 |
| [Review card](#review-card) | 370 x 580 | - | 40px | #ffffff `white` | none | 0 |
| [Member card](#member-card) | 359 x 479 | 1px solid #cccccc `border-gray` | 36px | transparent | none | 0 |
| [Value card](#value-card) | 271 x 272 | - | 40px | #ffffff `white` | none | 0 |
| [Feature table](#feature-table) | 527 x 1166 | - | 40px | #e6e51e `lime` | none | 0 |
| [Export step card](#export-step-card) | 561 x 273 | 1px solid #cccccc `border-gray` | 36px | transparent | none | 0 |
| [Billing toggle](#billing-toggle) | 1440 x 75 | - | - | #f2f2f2 `page-gray` | none | 0 |
| [Footer](#footer) | 1440 x 1088 | - | - | #000000 `black` | none | 0 |

## Components

### Shell and navigation

The chrome on the public pages: the floating white nav bar (aaply wordmark left, Features / Value / Pricing / Reviews links centre, Log in ghost pill and the black Sign up pill right), and the black footer band with the mail link, social icons and second nav list.

#### Nav bar
The floating rounded-white bar: aaply logo left, Features / Value / Pricing / Reviews links centre, Log in ghost button and the black Sign up pill right. Read as `nav-bar` on the home page.

**Values (default).** size 1200 x 166; radius 40px; background #ffffff `white`; text Times 16/normal 400, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Nav bar default](components/crops/nav-bar-default.png)

#### Logo
The aaply wordmark with the lime chevron-roof mark, top-left of the nav bar. Read as `logo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 119 x 31.72; background transparent; text Times 16/normal 400, #ff8562 `coral`; transition box-shadow 0.2s ease-in-out |
| focus-visible | outline 3px auto #2015ff, offset 4px |

![Logo default](components/crops/logo-default.png) ![Logo hover](components/crops/logo-hover.png) ![Logo focus-visible](components/crops/logo-focus-visible.png) ![Logo pressed](components/crops/logo-pressed.png)

#### Nav link
A text link in the nav bar (Features / Value / Pricing / Reviews), Inter 18px. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 68 x 34; radius 30px; background transparent; text Inter 18/27.9 400, #000000 `black`; transition background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out |
| hover | text Inter 18/27.9 400, #494949 `hover-gray` |
| focus-visible | outline 3px auto #2015ff, offset 4px |
| pressed | text Inter 18/27.9 400, #494949 `hover-gray` |

Child layers that carry the look: a::after 100%x100% shadow #000000 `black` 0px 0px 0px 0px inset.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log in button
The ghost pill in the nav bar; links to the app host (go.aaply.app). Hovered and focused only — pressing leaves for auth. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 90 x 44; border 1px solid #cccccc `border-gray`; radius 30px; background transparent; text Inter 18/27.9 300, #000000 `black`; transition background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out |
| hover | text Inter 18/27.9 300, #494949 `hover-gray` |
| focus-visible | outline 3px auto #2015ff, offset 4px |
| pressed | text Inter 18/27.9 300, #494949 `hover-gray` |

![Log in button default](components/crops/nav-login-default.png) ![Log in button hover](components/crops/nav-login-hover.png) ![Log in button focus-visible](components/crops/nav-login-focus-visible.png) ![Log in button pressed](components/crops/nav-login-pressed.png)

#### Sign up button
The black Sign up pill in the nav bar; links to go.aaply.app/signup. Hovered and focused only. Read as `nav-signup` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 134 x 44; border 1px solid #000000 `black`; radius 30px; background #000000 `black`; text Inter 18/27.9 400, #ffffff `white`; transition background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out |
| hover | border 1px solid #e6e51e `lime`; background #e6e51e `lime`; text Inter 18/27.9 400, #000000 `black` |
| focus-visible | outline 3px auto #2015ff, offset 4px |
| pressed | border 1px solid #e6e51e `lime`; background #e6e51e `lime`; text Inter 18/27.9 400, #000000 `black` |

![Sign up button default](components/crops/nav-signup-default.png) ![Sign up button hover](components/crops/nav-signup-hover.png) ![Sign up button focus-visible](components/crops/nav-signup-focus-visible.png) ![Sign up button pressed](components/crops/nav-signup-pressed.png)

#### Footer
The black footer band: "Made remotely with love", the aaply@aaply.app mail link, social icons (Twitter, Medium, LinkedIn, Discord, YouTube, Instagram) and the second nav list. Read as `footer` on the home page.

**Values (default).** size 1440 x 1088; background #000000 `black`; text Times 16/normal 400, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Footer default](components/crops/footer-default.png)

#### Footer mail link
The aaply@aaply.app contact link in the footer. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 121.28 x 19; background transparent; text Inter 15/23 400, #e6e51e `lime`; transition all 0.3s ease-in-out |
| hover | text Inter 15/23 400, #c4c4c4 `silver` |
| focus-visible | outline 3px auto #2015ff, offset 4px |
| pressed | text Inter 15/23 400, #c4c4c4 `silver` |

![Footer mail link default](components/crops/footer-link-default.png) ![Footer mail link hover](components/crops/footer-link-hover.png) ![Footer mail link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer mail link pressed](components/crops/footer-link-pressed.png)

#### Social icon
One of the social-icon links in the footer. Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 32; background transparent; text Times New Roman 16/normal 400, #ff8562 `coral`; transition box-shadow 0.2s ease-in-out |
| focus-visible | outline 3px auto #2015ff, offset 4px |

![Social icon default](components/crops/social-icon-default.png) ![Social icon hover](components/crops/social-icon-hover.png) ![Social icon focus-visible](components/crops/social-icon-focus-visible.png) ![Social icon pressed](components/crops/social-icon-pressed.png)

#### Early birds heading
"Join the early birds" — the Poppins display heading of the pre-footer CTA band ("Be the first to try"). Read as `early-birds` on the home page.

**Values (default).** size 560 x 81; background transparent; text Poppins 52/81 700, #ffffff `white`; transition box-shadow 0.2s ease-in-out.

![Early birds heading default](components/crops/early-birds-default.png)

### Home

The landing page: the Poppins display headline with inline emoji/avatar atoms, the lime "Sign up fo free" and black "Try demo project" pills, the browser-chrome product mockup, chat-annotation bubbles and the numbered how-it-works steps down ~5000px.

#### Hero title
The Poppins 700 display headline with inline emoji/avatar atoms inside the sentence flow ("Tool that helps teams design mobile apps…"). Read as `hero-title` on the home page.

**Values (default).** size 792 x 240; background transparent; text Poppins 57/60 700, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Hero title default](components/crops/hero-title-default.png)

#### Hero inline image
One of the inline emoji/squiggle/avatar atoms set inside the headline flow — the design's signature move. Read as `hero-emoji` on the home page.

**Values (default).** size 144 x 60; background transparent; text Times 16/normal 400, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Hero inline image default](components/crops/hero-emoji-default.png)

#### Sign up free CTA
The lime "Sign up fo free →" pill (the typo is the product's own). Links to go.aaply.app/signup; hovered and focused only. Read as `cta-signup-free` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 286 x 60; radius 30px; background #e6e51e `lime`; text Inter 18/27.9 400, #000000 `black`; transition background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out |
| focus-visible | outline 3px auto #2015ff, offset 4px |

![Sign up free CTA default](components/crops/cta-signup-free-default.png) ![Sign up free CTA hover](components/crops/cta-signup-free-hover.png) ![Sign up free CTA focus-visible](components/crops/cta-signup-free-focus-visible.png) ![Sign up free CTA pressed](components/crops/cta-signup-free-pressed.png)

#### Try demo CTA
The black "Try demo project" pill beside the lime CTA. Links to the app host's demo workspace; hovered and focused only. Read as `cta-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 286 x 60; radius 30px; background #000000 `black`; text Inter 18/27.9 400, #ffffff `white`; transition background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out |
| focus-visible | outline 3px auto #2015ff, offset 4px |

![Try demo CTA default](components/crops/cta-demo-default.png) ![Try demo CTA hover](components/crops/cta-demo-hover.png) ![Try demo CTA focus-visible](components/crops/cta-demo-focus-visible.png) ![Try demo CTA pressed](components/crops/cta-demo-pressed.png)

#### Hero product mockup
The product canvas inside a browser-chrome frame: the aaply workspace with screen tiles, connection arrows and collaborator cursors. Read as `hero-mock` on the home page.

**Values (default).** size 695 x 521.25; background transparent; text Times 16/normal 400, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Hero product mockup default](components/crops/hero-mock-default.png)

#### Chat annotation bubble
One of the fake-chat bubbles annotating the page (Have you seen this? / Looks nice! / I wanna try too) — rounded white bubbles with avatar stamps. Read as `chat-bubble` on the home page.

**Values (default).** size 371 x 48; background transparent; text Inter 31/48 500, #ffffff `white`; transition box-shadow 0.2s ease-in-out.

![Chat annotation bubble default](components/crops/chat-bubble-default.png)

#### Step number
The circled step numeral opening the "how it works" sequence. Read as `step-number` on the home page.

**Values (default).** size 60 x 42; background transparent; text Poppins 27/42 700, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Step number default](components/crops/step-number-default.png)

### Features

The workflow walkthrough: numbered steps (Start your new mobile app design project / Add your first mobile screen …), each pairing a chat bubble with a browser-chrome product panel, ending on the oversized "Try DEMO project" button.

#### Features title
"Here's what aaply workflow looks like" — Poppins display with an inline squiggle. Read as `features-title` on the features page.

**Values (default).** size 792 x 180; background transparent; text Poppins 57/60 700, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Features title default](components/crops/features-title-default.png)

#### Step title
A numbered step heading in the workflow sequence ("Start your new mobile app design project"). Read as `step-title` on the features page.

**Values (default).** size 380 x 156; background transparent; text Poppins 47/52 700, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Step title default](components/crops/step-title-default.png)

#### Step card
A workflow step's product panel: the browser-chrome-framed app screenshot beside the chat annotation bubble. Read as `step-card` on the features page.

**Values (default).** size 1131 x 642.86; background transparent; text Times 16/normal 400, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Step card default](components/crops/step-card-default.png)

#### Mega demo CTA
The oversized "Try DEMO project →" button (520x96) closing the features page. Links to the demo workspace; hovered and focused only. Read as `mega-demo-cta` on the features page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 520 x 96; radius 50px; background #000000 `black`; text Inter 18/27.9 400, #ffffff `white`; transition background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out |
| focus-visible | outline 3px auto #2015ff, offset 4px |

![Mega demo CTA default](components/crops/mega-demo-cta-default.png) ![Mega demo CTA hover](components/crops/mega-demo-cta-hover.png) ![Mega demo CTA focus-visible](components/crops/mega-demo-cta-focus-visible.png) ![Mega demo CTA pressed](components/crops/mega-demo-cta-pressed.png)

### Value

The value page: the "Aaply is here to boost your creativity" display and a grid of square rounded value cells.

#### Value title
"Aaply is here to boost your creativity" — the Poppins display heading. Read as `value-title` on the value page.

**Values (default).** size 605 x 120; background transparent; text Poppins 57/60 700, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Value title default](components/crops/value-title-default.png)

#### Value card
A square value-proposition cell in the Value grid (lime/white rounded shape with icon and caption atoms). Read as `value-card` on the value page.

**Values (default).** size 271 x 272; radius 40px; background #ffffff `white`; text Times 16/normal 400, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Value card default](components/crops/value-card-default.png)

### Pricing

The pricing page: the Monthly / Yearly segment rail with the "Save 30%" badge, the white Free card and lime Plus card with 3D characters, "Compare features" and the feature-comparison table.

#### Pricing title
The page heading in Poppins 700. Read as `pricing-title` on the pricing page.

**Values (default).** size 851 x 60; background transparent; text Poppins 57/60 700, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Pricing title default](components/crops/pricing-title-default.png)

#### Billing toggle
The Monthly / Yearly segment pair: 152x60 pills, the held segment filled lime. Read as `billing-toggle` on the pricing page.

**Values (default).** size 1440 x 75; background #f2f2f2 `page-gray`; text Inter 18/27.9 400, #000000 `black`.

![Billing toggle default](components/crops/billing-toggle-default.png)

#### Yearly option
The Yearly segment pill; selected by default. Read as `billing-yearly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 152 x 60; radius 30px; background transparent; text Inter 18/27.9 400, #000000 `black`; transition background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out |

![Yearly option default](components/crops/billing-yearly-default.png) ![Yearly option hover](components/crops/billing-yearly-hover.png) ![Yearly option pressed](components/crops/billing-yearly-pressed.png)

#### Monthly option
The Monthly segment pill. Read as `billing-monthly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 152 x 60; radius 30px; background transparent; text Inter 18/27.9 400, #000000 `black`; transition background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out |

![Monthly option default](components/crops/billing-monthly-default.png) ![Monthly option hover](components/crops/billing-monthly-hover.png)

#### Monthly option (selected)
The Monthly segment after pressing it: client-side state swap, nothing posted. Read as `billing-monthly-on` on the pricing page.

**Values (open).** size 152 x 60; radius 30px; background transparent; text Inter 18/27.9 400, #000000 `black`; transition background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out.

![Monthly option (selected) open](components/crops/billing-monthly-on-open.png)

#### Plan price (monthly)
The plan price after switching to Monthly (the price is split across sibling atoms: a "$" atom and a ".1 /month" numeral atom). Read as `plan-price-monthly` on the pricing page.

**Values (open).** size 308 x 47; background transparent; text Poppins 35/47 500, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Plan price (monthly) open](components/crops/plan-price-monthly-open.png)

#### Save badge
The coral "Save 30%" badge beside the billing toggle. Read as `save-badge` on the pricing page.

**Values (default).** size 87 x 34; radius 30px; background #fa3e3e `red`; text Inter 15/23.25 400, #ffffff `white`; transition background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out.

![Save badge default](components/crops/save-badge-default.png)

#### Plan card (Free)
The white Free plan card: $0, "Easy start for mobile creators", feature list, 3D character render. Read as `plan-card-free` on the pricing page.

**Values (default).** size 561 x 618; radius 36px; background #ffffff `white`; text Times 16/normal 400, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Plan card (Free) default](components/crops/plan-card-free-default.png)

#### Plan card (Plus)
The lime Plus card: $11.1 /month billed yearly, "Full access for the price of a cup of coffee", 3D character render. Read as `plan-card-plus` on the pricing page.

**Values (default).** size 561 x 618; radius 36px; background #e6e51e `lime`; text Times 16/normal 400, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Plan card (Plus) default](components/crops/plan-card-plus-default.png)

#### Plan name
A plan name (Free / Plus) on the card. Read as `plan-name` on the pricing page.

**Values (default).** size 88 x 47; background transparent; text Poppins 35/47 700, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Plan name default](components/crops/plan-name-default.png)

#### Plan price
The large price numeral with the /month suffix. Read as `plan-price` on the pricing page.

**Values (default).** size 308 x 47; background transparent; text Poppins 35/47 500, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
The Get started / Start for free button inside a plan card. Hovered and focused only. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 227 x 60; radius 30px; background #e6e51e `lime`; text Inter 18/27.9 400, #000000 `black`; transition background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out |
| focus-visible | outline 3px auto #2015ff, offset 4px |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Compare features link
The "Compare features →" link under the cards. Read as `compare-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 851 x 60; background transparent; text Poppins 57/60 700, #000000 `black`; transition box-shadow 0.2s ease-in-out |

![Compare features link default](components/crops/compare-cta-default.png) ![Compare features link hover](components/crops/compare-cta-hover.png) ![Compare features link pressed](components/crops/compare-cta-pressed.png)

#### Feature table
The feature-comparison table card: rows of features with checkmarks, "+" and "soon" pills. Read as `feature-table` on the pricing page.

**Values (default).** size 527 x 1166; radius 40px; background #e6e51e `lime`; text Times 16/normal 400, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Feature table default](components/crops/feature-table-default.png)

### Reviews

The reviews page: a wide lime featured-review slide (avatar, quote, "Try it for free" pill) with carousel dots, over a grid of testimonial cards.

#### Review card
A testimonial card in the grid (370x580): quote text, an embedded image or chat screenshot. Read as `review-card` on the reviews page.

**Values (default).** size 370 x 580; radius 40px; background #ffffff `white`; text Times 16/normal 400, #000000 `black`.

![Review card default](components/crops/review-card-default.png)

#### Review quote
The quote text inside a review card or the featured slide. Read as `review-text` on the reviews page.

**Values (default).** size 951 x 84; background transparent; text Poppins 35/42 500, #000000 `black`.

![Review quote default](components/crops/review-text-default.png)

#### Review slide
The wide lime featured-review slide at the top: avatar, name and role, the quote in Poppins, a "Try it for free" ghost pill; carousel dots below. Read as `review-slide` on the reviews page.

**Values (default).** size 1157 x 418; radius 40px; background #e7e51e `lime-slide`; text Times 16/normal 400, #000000 `black`.

![Review slide default](components/crops/review-slide-default.png)

### Our story

The our-story page: a single editorial column in the display face — "Our story started with a wish!" and long-form paragraphs.

#### Story paragraph
A long-form body paragraph in the story. Read as `story-block` on the our-story page.

**Values (default).** size 565 x 230; background transparent; text Poppins 35/46 500, #000000 `black`.

![Story paragraph default](components/crops/story-block-default.png)

#### Story lead
"Our story started with a wish!" — the page's opening editorial block. Read as `story-lead` on the our-story page.

**Values (default).** size 851 x 420; background transparent; text Poppins 57/60 700, #000000 `black`.

![Story lead default](components/crops/story-lead-default.png)

### Team

The team page: "Our Team" display and a grid of member cards (3D character avatar, name, role).

#### Team title
"Our Team" — the Poppins display heading. Read as `team-title` on the team page.

**Values (default).** size 851 x 60; background transparent; text Poppins 57/60 700, #000000 `black`.

![Team title default](components/crops/team-title-default.png)

#### Member card
A team-member card (359x479): 3D character avatar, name, role. Read as `member-card` on the team page.

**Values (default).** size 359 x 479; border 1px solid #cccccc `border-gray`; radius 36px; background transparent; text Times 16/normal 400, #000000 `black`.

![Member card default](components/crops/member-card-default.png)

### Figma plugin

The figma-plugin page: "Aaply Figma Plugin" display and numbered export-step cards (Design in aaply → Click export → Follow the link).

#### Figma plugin title
"Aaply Figma Plugin" display heading. Read as `figma-title` on the figma-plugin page.

**Values (default).** size 605 x 60; background transparent; text Poppins 57/60 700, #000000 `black`.

![Figma plugin title default](components/crops/figma-title-default.png)

#### Export step card
A numbered step card in the export instructions (Design your app in Aaply → Click the export button → Follow the link). Read as `figma-step` on the figma-plugin page.

**Values (default).** size 561 x 273; border 1px solid #cccccc `border-gray`; radius 36px; background transparent; text Times 16/normal 400, #000000 `black`.

![Export step card default](components/crops/figma-step-default.png)

### Mobile (390 wide)

The same pages as a phone draws them, at 390 x 844 with an iPhone user agent: the burger menu, the hero and the full-width CTAs.

#### Mobile nav bar
The mobile header: logo left, hamburger right. Read as `m-nav-bar` on the home page at 390 wide.

**Values (default).** size 370.5 x 166; background transparent; text Times 16/normal 400, #000000 `black`.

Child layers that carry the look: div 370.5x166 background #ffffff `white` radius 40px.

![Mobile nav bar default](components/crops/m-nav-bar-default.png)

#### Hamburger
The mobile menu button at the top right. Not opened — the menu overlays the measured content. Read as `m-burger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 92 x 24.53; background transparent; text Times 16/normal 400, #ff8562 `coral`; transition box-shadow 0.2s ease-in-out |

![Hamburger default](components/crops/m-burger-default.png) ![Hamburger pressed](components/crops/m-burger-pressed.png)

#### Mobile hero title
The first painted line of the mobile Poppins headline — the mobile title splits one atom per line. Read as `m-hero-title` on the home page at 390 wide.

**Values (default).** size 264 x 27; background transparent; text Poppins 27/27 700, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Mobile hero title default](components/crops/m-hero-title-default.png)

#### Mobile sign up CTA
The full-width lime pill. Read as `m-cta-signup` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 280 x 55; radius 30px; background #e6e51e `lime`; text Inter 15/23.25 400, #000000 `black`; transition background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out |

![Mobile sign up CTA default](components/crops/m-cta-signup-default.png) ![Mobile sign up CTA pressed](components/crops/m-cta-signup-pressed.png)

#### Mobile demo CTA
The full-width black pill. Read as `m-cta-demo` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 280 x 55; radius 30px; background #000000 `black`; text Inter 15/23.25 400, #ffffff `white`; transition background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out |

![Mobile demo CTA default](components/crops/m-cta-demo-default.png) ![Mobile demo CTA pressed](components/crops/m-cta-demo-pressed.png)

#### Mobile step number
The circled step numeral in the mobile how-it-works column. Read as `m-step-number` on the home page at 390 wide.

**Values (default).** size 30 x 23; background transparent; text Poppins 15/23 700, #000000 `black`; transition box-shadow 0.2s ease-in-out.

![Mobile step number default](components/crops/m-step-number-default.png)
## Gaps

### Pages

- **The app and everything behind sign-in.** The product itself lives on go.aaply.app (Log in / Sign up / "Try demo project" all point there), and every tested route — /login, /sign, /signup, /workspace/demo — returned the bare body "Not found" to this client. Whether the app host is retired, region-gated or simply down, no authenticated surface exists to measure: the package covers the marketing site only and records the app as an unreachable boundary. The footer still reads ©2024 and the Figma plugin page still links an export flow, so the product may be in maintenance mode.
- **Anything that sends.** No form was submitted, nothing bought, nothing signed into; the auth-bound pills (Log in, Sign up, the demo CTAs) were hovered and focused but never pressed through.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover), so a state a script adds on mousedown (if any) is missing.
- **The billing toggle's held segment** paints its lime fill on a sibling shape, not on the text atom itself — the segment atoms measure transparent in both positions; the swap is visible in [pricing-light-yearly.png](screenshots/pricing-light-yearly.png).
- **Monthly billing** was reached by pressing the Monthly segment (client-side state, nothing posted); Yearly was restored after.
- **The reviews carousel** was measured on its first slide only; the dots' other slides were not advanced.

### Themes

The marketing site paints one theme — light surfaces with a black footer band. Tilda declares no `[data-theme]` overrides and the app (which may theme differently) was never reached.

### Fonts

- **Poppins** (display, 700 and 500) and **Inter** (UI, 400 / 500 / 300) load from Google Fonts via stylesheet link, so they do not appear in the page's own @font-face rules (`fonts` in [raw/css-vars.json](raw/css-vars.json) is empty). The style guide renders them with the system fallback stack.

### Screenshots

- Screens and product imagery are aaply.app's content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- No personal data was captured: every page was read signed out with an empty session, and the only presses were the Monthly billing toggle; no text was ever typed into a form.
