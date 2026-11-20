# Clearful components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from clearful.com on 2026-11-16, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. The sign-in group is a Flutter canvas read through its semantics overlay at devicePixelRatio 1; its colours are pixel-sampled from the screenshot, not computed. Nothing was signed into, paid for or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (31 components, 64 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Manrope 16/24 600, #222`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (63 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`; every public route paints the same light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages (1x on desktop, 2x on mobile); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Journal library | `/library` | [default](screenshots/library-light-default.png), [full](screenshots/library-light-full.png) |
| Journal prompts | `/journal-prompts` | [default](screenshots/prompts-light-default.png), [full](screenshots/prompts-light-full.png) |
| What's new | `/whatsnew` | [default](screenshots/whatsnew-light-default.png), [full](screenshots/whatsnew-light-full.png) |
| Widgets | `/widgets` | [default](screenshots/widgets-light-default.png), [full](screenshots/widgets-light-full.png) |
| Flow editor | `/floweditor` | [default](screenshots/floweditor-light-default.png), [full](screenshots/floweditor-light-full.png) |
| Contact | `/contact` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Press | `/press` | [default](screenshots/press-light-default.png), [full](screenshots/press-light-full.png) |
| Terms | `/terms` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| Privacy | `/privacy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Sign-in (boundary) | `app.clearful.com/#/sign-in` | [default](screenshots/signin-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Library, phone | `/library` | [default](screenshots/mobile-library-light-default.png), [full](screenshots/mobile-library-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu, open | bar, phone | the hamburger's own press | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-open](#mobile-menu-open) |
| Billing tabs | pricing page | the Monthly/Yearly tab's own click | [pricing-light-default](screenshots/pricing-light-default.png), [billing-tab](#billing-tab) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 11 components were given a real keyboard focus. 9 show a visible focus state: `nav-item` (1px auto #101010 `color.focus.0`, offset 1px), `nav-signin` (1px auto #101010 `color.focus.0`, offset 1px), `nav-cta` (1px auto #101010 `color.focus.0`, offset 1px), `cta` (1px auto #101010 `color.focus.0`, offset 1px), `plan-cta` (1px auto #101010 `color.focus.0`, offset 1px), `footer-link` (1px auto #101010 `color.focus.0`, offset 1px), `footer-social` (1px auto #101010 `color.focus.0`, offset 1px), `prompt-card` (1px auto #101010 `color.focus.0`, offset 1px), `m-menu-link` (1px auto #101010 `color.focus.0`, offset 1px). The other 2 show no change a keyboard user can see: `tab-link`, `billing-tab`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): the blue controls hold their #1b1bbc hover step through press, and the text links keep their #f7f7f7 wash — hover and pressed are the same painted step on this surface. Nothing a real press would submit or navigate was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease` | color | tab-link |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | -webkit-backdrop-filter, backdrop-filter, background-color, border-color, box-shadow, color, fill, filter, opacity, stroke, text-decoration-color, transform | prompt-card |
| 0.4s | `ease` | transform | m-menu-open |
| 0.5s | `ease` | height | m-menu-open |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Feature card](#feature-card) | 1280 x 720 | 1px solid #ffffff `color.white` | 24px | #f7f7f7 `color.grey.000` | none | 0 |
| [Journal card](#journal-card) | 394.66 x 160 | 1px solid #e1e1e1 `color.grey.100` | 16px | #ffffff `color.white` | rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px | 32px |
| [Feature row](#feature-row) | 1280 x 56 | - | 8px | #f7f7f7 `color.grey.000` | none | 0 |

## Components

### Shell and navigation

The white nav bar on the light ground, the wordmark, the link row and the blue Start-a-journal pill.

#### Nav bar
The 1440x72 top nav (Webflow w-nav): logo, Guided Journals link, Log In and the blue Start-a-journal pill. Read as `header` on the home page.

**Values (default).** size 1440 x 72; padding 0px 72px; border B: 1px solid #e1e1e1 `color.grey.100`; background #ffffff `color.white`; text Manrope 16/24 600, #222222 `color.grey.900`.

![Nav bar default](components/crops/header-default.png)

#### Logo
The Clearful logo anchor (150x30). Read as `logo` on the home page.

**Values (default).** size 150 x 29.56; background transparent; text Manrope 16/24 400, #333333.

![Logo default](components/crops/logo-default.png)

#### Nav link
The "Guided Journals" nav link (16px/600 ink); links to /library, never followed. Read as `nav-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 167 x 40; padding 8px 20px; background transparent; text Manrope 16/24 600, #222222 `color.grey.900` |
| hover | radius 8px; background #f7f7f7 `color.grey.000`; child paint a.navbar1_link.w-nav-link: size 167.0x40.0; background #f7f7f7 `color.grey.000`; radius 8px |
| focus-visible | outline 1px auto #101010 `color.focus.0`, offset 1px; child paint a.navbar1_link.w-nav-link: size 167.0x40.0; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | radius 8px; background #f7f7f7 `color.grey.000`; child paint a.navbar1_link.w-nav-link: size 167.0x40.0; background #f7f7f7 `color.grey.000`; radius 8px |

![Nav link default](components/crops/nav-item-default.png) ![Nav link hover](components/crops/nav-item-hover.png) ![Nav link focus-visible](components/crops/nav-item-focus-visible.png) ![Nav link pressed](components/crops/nav-item-pressed.png)

#### Log-in link
The "Log In" nav action linking to app.clearful.com/#/sign-in; measured never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 86 x 40; padding 8px 20px; background transparent; text Manrope 16/24 600, #222222 `color.grey.900` |
| hover | radius 8px; background #f7f7f7 `color.grey.000`; child paint a.navbar1_link.w-nav-link: size 86.0x40.0; background #f7f7f7 `color.grey.000`; radius 8px |
| focus-visible | outline 1px auto #101010 `color.focus.0`, offset 1px; child paint a.navbar1_link.w-nav-link: size 86.0x40.0; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | radius 8px; background #f7f7f7 `color.grey.000`; child paint a.navbar1_link.w-nav-link: size 86.0x40.0; background #f7f7f7 `color.grey.000`; radius 8px |

![Log-in link default](components/crops/nav-signin-default.png) ![Log-in link hover](components/crops/nav-signin-hover.png) ![Log-in link focus-visible](components/crops/nav-signin-focus-visible.png) ![Log-in link pressed](components/crops/nav-signin-pressed.png)

#### Nav CTA
The 999px blue "Start a journal — it's free" pill in the nav (225x50, #1953ff); the anchor points at #, measured never pressed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 230 x 50; padding 12px 20px; border 1px solid #1953ff `color.blue.500`; radius 999px; background #1953ff `color.blue.500`; text Manrope 16/24 600, #ffffff `color.white` |
| hover | border 1px solid #1b1bbc `color.blue.hover`; background #1b1bbc `color.blue.hover`; child paint a.button.is-small: background #1b1bbc `color.blue.hover`; border 1px solid #1b1bbc `color.blue.hover` |
| focus-visible | outline 1px auto #101010 `color.focus.0`, offset 1px; child paint a.button.is-small: outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | border 1px solid #1b1bbc `color.blue.hover`; background #1b1bbc `color.blue.hover`; child paint a.button.is-small: background #1b1bbc `color.blue.hover`; border 1px solid #1b1bbc `color.blue.hover` |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

### Home

The Literatatt hero (no lede — the headline stands alone), the haloed blue CTA, the feature cards, tabs and the brand-light accent band.

#### Hero title
"Be a more thoughtful, resilient, and happier you with daily journaling" — the 72px/700 Literatatt display headline. Read as `hero-title` on the home page.

**Values (default).** size 1024 x 259.17; background transparent; text Literatatt 72/86.4 700, #222222 `color.grey.900`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero CTA
The 999px blue "Start journaling for free" pill under the hero (289x82, 20px/600); measured never pressed. Read as `cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 298 x 82; padding 20px 28px; border 6px solid #adc2ff `color.blue.200`; radius 999px; background #1953ff `color.blue.500`; text Manrope 20/30 600, #ffffff `color.white` |
| hover | background #1b1bbc `color.blue.hover`; child paint a.button.is-large: background #1b1bbc `color.blue.hover` |
| focus-visible | outline 1px auto #101010 `color.focus.0`, offset 1px; child paint a.button.is-large: outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | background #1b1bbc `color.blue.hover`; child paint a.button.is-large: background #1b1bbc `color.blue.hover` |

![Hero CTA default](components/crops/cta-default.png) ![Hero CTA hover](components/crops/cta-hover.png) ![Hero CTA focus-visible](components/crops/cta-focus-visible.png) ![Hero CTA pressed](components/crops/cta-pressed.png)

#### Section title
The first 60px/700 section heading ("We're Clearful, the award-winning, modern jour…", navy #001452). Read as `section-title` on the home page.

**Values (default).** size 1024 x 432; background transparent; text Literatatt 60/72 700, #001452 `color.blue.900`.

![Section title default](components/crops/section-title-default.png)

#### Feature card
A 1280x720 feature card (layout409): copy column + app screenshot. Read as `feature-card` on the home page.

**Values (default).** size 1280 x 720; border 1px solid #ffffff `color.white`; radius 24px; background #f7f7f7 `color.grey.000`; text Manrope 18/31.5 700, #1953ff `color.blue.500`; icon 20 x 20, #1953ff `color.blue.500`.

![Feature card default](components/crops/feature-card-default.png)

#### Cadence tab
A cadence tab (Weekly/Monthly/Quarterly/Bi-Yearly/Yearly) in the timeline14 w-tabs widget; the held tab carries w--current, tabs switch panes locally. Read as `tab-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 256 x 73.59; padding 8px 0px; border B: 1px solid transparent; background transparent; text Manrope 24/33.6 700, #222222 `color.grey.900`; transition color 0.2s ease; icon 15 x 15, #222222 `color.grey.900` |

Child layers that carry the look: a 256x73.6 border 1px solid transparent; div 64x6 image linear-gradient(270deg, transparent, #ffffff `color.white`); div 120.5x3 background #e1e1e1 `color.grey.100`.

![Cadence tab default](components/crops/tab-link-default.png) ![Cadence tab hover](components/crops/tab-link-hover.png) ![Cadence tab focus-visible](components/crops/tab-link-focus-visible.png) ![Cadence tab pressed](components/crops/tab-link-pressed.png)

#### Brand-light band
The #d6e0ff brand-light section fill (background-color-brand-light) — the site's one tinted band. Read as `section-accent` on the home page.

**Values (default).** size 1440 x 1200; background #d6e0ff `color.blue.100`; text Literatatt 60/72 700, #001452 `color.blue.900`.

![Brand-light band default](components/crops/section-accent-default.png)

#### Store badge
The App Store badge artwork (153x80); the anchor links to apps.apple.com, never followed. Read as `app-badge` on the home page.

**Values (default).** size 153.42 x 80; background transparent; text Manrope 16/24 400, #222222 `color.grey.900`.

![Store badge default](components/crops/app-badge-default.png)

#### Page ground
The body element's painted fill — the white ground (html itself is transparent). Read as `page-ground` on the home page.

**Values (default).** size 1440 x 32520.81; background #ffffff `color.white`; text Manrope 20/30 800, #222222 `color.grey.900`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Pricing

The pricing route: the Monthly/Yearly billing tabs, the plan columns and the blue plan buttons.

#### Pricing title
"Pricing Plans" — the 60px/700 heading over the Free/Premium comparison table. Read as `pricing-title` on the pricing page.

**Values (default).** size 768 x 72; background transparent; text Literatatt 60/72 700, #222222 `color.grey.900`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Billing tab
The Monthly/Yearly billing tab (w-tab-menu, 108x40); the held period carries w--current. A local pane switch, measured never flipped. Read as `billing-tab` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 106 x 40; padding 8px 24px; background transparent; text Manrope 16/24 400, #222222 `color.grey.900` |

![Billing tab default](components/crops/billing-tab-default.png) ![Billing tab hover](components/crops/billing-tab-hover.png) ![Billing tab focus-visible](components/crops/billing-tab-focus-visible.png) ![Billing tab pressed](components/crops/billing-tab-pressed.png)

#### Plan column
A plan column top (347x247): price, cadence and the Get-started button. Read as `plan-column` on the pricing page.

**Values (default).** size 347.42 x 246.78; background transparent; text Manrope 24/33.6 700, #222222 `color.grey.900`.

Child layers that carry the look: a 347.4x58 background #1953ff `color.blue.500` border 1px solid #1953ff `color.blue.500` radius 999px.

![Plan column default](components/crops/plan-column-default.png)

#### Plan price
The "$0/mo"/"$9.99/mo" price line (56px/700). Read as `plan-price` on the pricing page.

**Values (default).** size 347.42 x 67.19; background transparent; text Manrope 24/33.6 700, #222222 `color.grey.900`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
The blue "Get started" pill under each price (347x58, #1953ff); never pressed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 347.42 x 58; padding 16px 24px; border 1px solid #1953ff `color.blue.500`; radius 999px; background #1953ff `color.blue.500`; text Manrope 16/24 600, #ffffff `color.white` |
| hover | border 1px solid #1b1bbc `color.blue.hover`; background #1b1bbc `color.blue.hover`; child paint a.button-4.max-width-full: background #1b1bbc `color.blue.hover`; border 1px solid #1b1bbc `color.blue.hover` |
| focus-visible | outline 1px auto #101010 `color.focus.0`, offset 1px; child paint a.button-4.max-width-full: outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | border 1px solid #1b1bbc `color.blue.hover`; background #1b1bbc `color.blue.hover`; child paint a.button-4.max-width-full: background #1b1bbc `color.blue.hover`; border 1px solid #1b1bbc `color.blue.hover` |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Feature row
A feature row in the Free/Premium comparison table (1280x56 on the #f7f7f7 alternate band). Read as `feature-row` on the pricing page.

**Values (default).** size 1280 x 56; radius 8px; background #f7f7f7 `color.grey.000`; text Manrope 16/24 600, #222222 `color.grey.900`.

![Feature row default](components/crops/feature-row-default.png)

### Guided-journals library (Tailwind surface)

/library — a separate Tailwind build in Mulish on the same light theme: its own h1 and the prompt cards.

#### Library title
"Guided Journaling Library" — 60px/800 Mulish in Tailwind gray-900 (#111827); /library is a Tailwind sibling stack, not the Webflow marketing sheet. Read as `library-h1` on the library page.

**Values (default).** size 832 x 76; background transparent; text Mulish 60/76 800, #111827.

![Library title default](components/crops/library-h1-default.png)

#### Journal card
A guided-journal link card (white, 395x160, radius 16, Tailwind utilities); links into the library, never followed. Read as `prompt-card` on the library page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 394.66 x 160; padding 32px; border 1px solid #e1e1e1 `color.grey.100`; radius 16px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px; text Mulish 24/32 700, #111827; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), filter 0.3s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.3s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f7f7f7 `color.grey.000`; transform translate(0px, -4px); child paint a.flex.flex-col: background #f7f7f7 `color.grey.000` |
| focus-visible | outline 1px auto #101010 `color.focus.0`, offset 1px; child paint a.flex.flex-col: outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | background #f7f7f7 `color.grey.000`; transform translate(0px, -4px); child paint a.flex.flex-col: background #f7f7f7 `color.grey.000` |

![Journal card default](components/crops/prompt-card-default.png) ![Journal card hover](components/crops/prompt-card-hover.png) ![Journal card focus-visible](components/crops/prompt-card-focus-visible.png) ![Journal card pressed](components/crops/prompt-card-pressed.png)

### App sign-in (Flutter boundary)

app.clearful.com's public sign-in card — a Flutter canvas app read through its semantics overlay at devicePixelRatio 1; the canvas paints its own colours, which CSSOM cannot read. Nothing was signed into or submitted.

#### Welcome illustration
The "Welcome Back Image" artwork on the sign-in card (264x176) — read through Flutter's flt-semantics overlay; the card paints on canvas so only geometry/roles are DOM-readable. Read as `signin-image` on the sign-in page.

**Values (default).** size 264 x 176; background transparent; text Times New Roman 16/normal 400, transparent; transform translate(588px, 56px).

![Welcome illustration default](components/crops/signin-image-default.png)

#### Sign-in button
A "Continue with email/Apple/Google" button on the sign-in card (400x56); canvas-painted, measured via the semantics overlay — never pressed. Read as `signin-button` on the sign-in page.

**Values (default).** size 400 x 56; background transparent; text Times New Roman 16/normal 400, transparent; transform translate(520px, 384.5px).

![Sign-in button default](components/crops/signin-button-default.png)

### Footer

The #f7f7f7 footer band, its link columns and social icons.

#### Footer
The #f7f7f7 footer band (1440x535): resource links, store badges, social icons and the legal subfooter. Read as `footer` on the home page.

**Values (default).** size 1440 x 548.05; border T: 1px solid #e1e1e1 `color.grey.100`; background #f7f7f7 `color.grey.000`; text Manrope 18/31.5 600, #222222 `color.grey.900`; icon 20 x 20, #626262 `color.grey.600`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85 x 40; padding 8px 0px; background transparent; text Manrope 16/24 400, #515151 `color.grey.700` |
| hover | text Manrope 16/24 400, #1953ff `color.blue.500` |
| focus-visible | outline 1px auto #101010 `color.focus.0`, offset 1px; child paint a.footer1_link: size 85.0x40.0; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Manrope 16/24 400, #1953ff `color.blue.500` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A footer social icon link (Instagram). Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106 x 40; padding 8px 0px; background transparent; text Manrope 16/24 400, #626262 `color.grey.600`; icon 20 x 20, #626262 `color.grey.600` |
| hover | text Manrope 16/24 400, #1953ff `color.blue.500`; icon 20 x 20, #1953ff `color.blue.500` |
| focus-visible | outline 1px auto #101010 `color.focus.0`, offset 1px; child paint a.footer1_social-link.w-inline-block: size 106.0x40.0; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Manrope 16/24 400, #1953ff `color.blue.500`; icon 20 x 20, #1953ff `color.blue.500` |

![Social link default](components/crops/footer-social-default.png) ![Social link hover](components/crops/footer-social-hover.png) ![Social link focus-visible](components/crops/footer-social-focus-visible.png) ![Social link pressed](components/crops/footer-social-pressed.png)

### Mobile (390 wide)

The same surface at phone width: the fixed bar and the full-height menu overlay.

#### Mobile bar
The 390x64 mobile nav bar: logo + hamburger. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 64; padding 0px 19.5px; border B: 1px solid #e1e1e1 `color.grey.100`; background #ffffff `color.white`; text Manrope 16/24 400, #222222 `color.grey.900`.

![Mobile bar default](components/crops/m-header-default.png)

#### Menu button
The 40x48 hamburger (w-nav-button, the menu-icon1 lines); its own press opens the nav menu. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 40 x 48; background transparent; text Manrope 24/36 400, #222222 `color.grey.900`.

Child layers that carry the look: div 24x2 background #222222 `color.grey.900`; div 24x2 background #222222 `color.grey.900`; div 24x2 background #222222 `color.grey.900`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The nav menu after the hamburger press (Webflow w-nav-menu). Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; padding 16px 19.5px 96px 19.5px; background #ffffff `color.white`; text Manrope 18/27 600, #222222 `color.grey.900`; transition height 0.5s ease, transform 0.4s ease.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Menu link
A link row inside the open mobile menu. Read as `m-menu-link` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 351 x 51; padding 12px 0px; background transparent; text Manrope 18/27 600, #222222 `color.grey.900` |
| hover | radius 8px; background #f7f7f7 `color.grey.000`; child paint a.navbar1_link.w-nav-link: size 351.0x51.0; background #f7f7f7 `color.grey.000`; radius 8px |
| focus-visible | outline 1px auto #101010 `color.focus.0`, offset 1px; child paint a.navbar1_link.w-nav-link: size 351.0x51.0; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | radius 8px; background #f7f7f7 `color.grey.000`; child paint a.navbar1_link.w-nav-link: size 351.0x51.0; background #f7f7f7 `color.grey.000`; radius 8px |

![Menu link default](components/crops/m-menu-link-default.png) ![Menu link hover](components/crops/m-menu-link-hover.png) ![Menu link focus-visible](components/crops/m-menu-link-focus-visible.png) ![Menu link pressed](components/crops/m-menu-link-pressed.png)

#### Mobile headline
The hero headline at 390. Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 351 x 470.31; background transparent; text Literatatt 56/67.2 700, #222222 `color.grey.900`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Clearful's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The product itself.** Clearful's app — the journal, entries and settings — lives behind app.clearful.com sign-in; the public sign-in card was measured but never submitted, and the paid checkout flow was never entered.
- **The sign-in card's computed styles.** The app is a Flutter canvas; its controls were located through the semantics overlay (real rects), but the canvas paints its own colours — CSSOM reads only UA defaults, so app-surface colours are pixel-sampled off the screenshot and labelled as such in tokens.json.
- **/journal-prompts** threw a transient human-verification challenge on one pass; it captured clean on retry. If it recurs the route is a boundary.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

One theme: the whole public surface paints light. The Webflow marketing routes and the Tailwind /library share it; the Flutter sign-in is a separate stack's surface, not a theme — its sampled shades sit under `core.sampled.app.*`.

### Fonts

- **The UI fonts** are webfonts the site declares (Manrope on the Webflow surface, Mulish on /library, Literatatt display; `fonts` in [raw/css-vars.json](raw/css-vars.json) holds the 64 @font-face records — the Webflow sheet imports a broad Google-Fonts set wider than what the pages actually use); the font files themselves are not committed.
- Illustrations, app-badge artwork and the wordmark in the screenshots are Clearful's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The illustrations, app-store badges and the wordmark are Clearful's content; only the frames and components were measured.
