# Chargetrip components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from www.chargetrip.com (plus the public sign-in card on account.chargetrip.io) on 2026-11-16, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, booked, sent or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (46 components, 99 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 14/21 500, #111827`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (95 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the marketing site paints one light theme (the hero band and the Popular plan card are dark islands inside it). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages (1x on desktop, 2x on mobile); mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Routing | `/products/routing` | [default](screenshots/routing-light-default.png), [full](screenshots/routing-light-full.png) |
| API | `/api` | [default](screenshots/api-light-default.png), [full](screenshots/api-light-full.png) |
| No-code | `/no-code` | [default](screenshots/nocode-light-default.png), [full](screenshots/nocode-light-full.png) |
| CPO | `/cpo` | [default](screenshots/cpo-light-default.png), [full](screenshots/cpo-light-full.png) |
| API pricing | `/pricing/api` | [default](screenshots/pricing-api-light-default.png), [full](screenshots/pricing-api-light-full.png) |
| No-code pricing | `/pricing/nocode` | [default](screenshots/pricing-nocode-light-default.png), [full](screenshots/pricing-nocode-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Newsroom | `/newsroom` | [default](screenshots/newsroom-light-default.png), [full](screenshots/newsroom-light-full.png) |
| Contact | `/contact` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Contact sales | `/contact/sales` | [default](screenshots/sales-light-default.png), [full](screenshots/sales-light-full.png) |
| Terms | `/legal/terms-and-conditions` | [default](screenshots/terms-light-default.png) |
| Sign-in (boundary) | `https://account.chargetrip.io/sign-in` | [default](screenshots/signin-light-default.png) |
| Developers | `https://developers.chargetrip.com/` | [default](screenshots/developers-light-default.png), [full](screenshots/developers-light-full.png) |
| API playground (boundary) | `https://playground.chargetrip.com/` | [default](screenshots/playground-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| API pricing, phone | `/pricing/api` | [default](screenshots/mobile-pricing-api-light-default.png), [full](screenshots/mobile-pricing-api-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Products menu, open | header, desktop | the nav item's own press | [home-light-menu](screenshots/home-light-menu.png), [menu-panel](#mega-menu) |
| Mobile menu, open | header, phone | the menu trigger's own press | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 13 components were given a real keyboard focus (a further 1 could not be driven: `nav-item`). 13 show a visible focus state: `nav-cta` (1px auto #101010, offset 1px), `nav-signin` (1px auto #101010, offset 1px), `cta-accent` (1px auto #101010, offset 1px), `cta-dark` (1px auto #101010, offset 1px), `logo-chip` (1px auto #005fcc, offset 1px), `plan-cta` (1px auto #005fcc, offset 1px), `plan-cta-dark` (1px auto #005fcc, offset 1px), `form-submit` (1px auto #005fcc, offset 0px), `signin-continue` (1px solid oklch(0.5152 0.0118 58.04), offset 1px), `signin-create` (1px solid oklch(0.5152 0.0118 58.04), offset 1px), `footer-link` (1px auto #101010, offset 1px), `footer-social` (1px auto #101010, offset 1px), `newsletter-cta` (1px auto #101010, offset 1px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): the marketing controls' painted fills do not move (the anchors' UA `:active` red only shows on their unstyled `color`); the footer text links take the orange accent on press; and the sign-in card's Tailwind buttons lighten and shrink to scale(0.97). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.2, 0, 0, 1)` | background-color, border-color, color, scale | signin-continue, signin-create |
| 0.2s | `ease-out` | background-color, border-color, color, fill, stroke, text-decoration-color | signin-input |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card (light)](#plan-card-light) | 458.66 x 628.84 | - | 24px | #fffffb `color.paper.0` | none | 72px |
| [Plan card (dark)](#plan-card-dark) | 442.67 x 586.84 | - | 16px | #262322 `color.ink.800` | none | 38px 72px 72px 72px |
| [Book-a-demo card](#book-a-demo-card) | 205.3 x 65.09 | - | 12px | #fffffb `color.paper.0` | none | 8px 12px |
| [Hero band](#hero-band) | 1391.98 x 1086 | - | 24px | radial-gradient(103% 223% at 49.2% 170.8%, #38312f 35%, #262321 67.3371%) | none | 72px 48px 0px 48px |

## Components

### Shell and navigation

The cream header bar, its Products flyout and the dark sign-in pills.

#### Header
The white 64px top bar: wordmark, the Products/Use-cases/Developers/Pricing/Company menu triggers, and the Contact-sales + Sign-in buttons. Read as `header` on the home page.

**Values (default).** size 1440 x 64; padding 16px 0px 0px 0px; background transparent; text Geist Variable 18/28.8 400, #efede5 `color.paper.200`; icon 106 x 24, #000000.

Child layers that carry the look: a 139x40 background #262322 `color.ink.800` radius 8px; a::after 83pxx40px border 1px solid #262322 `color.ink.800` radius 8px; a 453.3x776 background #efede5 `color.paper.200` radius 8px.

![Header default](components/crops/header-default.png)

#### Logo
The chargetrip wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 106 x 24; background transparent; text sans-serif 12/normal 400, #0000ee; icon 106 x 24, #000000.

![Logo default](components/crops/logo-default.png)

#### Nav item
The "Products" menu trigger; its own press opens the mega menu (opened state, then the menu stays up for the next two entries). Read as `nav-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 99 x 32; background transparent; text Geist Variable 18/28.8 400, #262322 `color.ink.800` |
| hover | text Geist Variable 18/28.8 400, #dc3b04; child paint div.framer-tBbOV.framer-i5yBN: size 99.0x32.0; background rgba(221, 59, 0, 0.15); radius 24px |
| opened | text Geist Variable 18/28.8 400, #dd3b00 `color.orange.600`; child paint div.framer-tBbOV.framer-i5yBN: size 99.0x32.0; background rgba(221, 59, 0, 0.15); radius 24px |

![Nav item default](components/crops/nav-item-default.png) ![Nav item hover](components/crops/nav-item-hover.png) ![Nav item pressed](components/crops/nav-item-pressed.png) ![Nav item opened](components/crops/nav-item-opened.png)

#### Mega menu
The Products mega-menu card row (No-code / API / Integration Partners photo cards), held open by the nav-item toggle. Read as `menu-panel` on the home page.

**Values (default).** size 1376 x 816; padding 0px 0px 40px 0px; background transparent; text Geist Medium 22/26 400, #efede5 `color.paper.200`.

Child layers that carry the look: a 453.3x776 background #efede5 `color.paper.200` radius 8px; a 453.3x776 background #efede5 `color.paper.200` radius 8px; a 453.3x776 background #efede5 `color.paper.200` radius 8px.

![Mega menu default](components/crops/menu-panel-default.png)

#### Menu card
The No-code photo card inside the open mega menu. Read as `menu-card` on the home page.

**Values (default).** size 453.33 x 776; padding 16px; radius 8px; background #efede5 `color.paper.200`; text Geist Medium 22/26 400, #efede5 `color.paper.200`.

![Menu card default](components/crops/menu-card-default.png)

#### Nav CTA
The dark "Contact sales" button; links to /contact/sales, measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 139 x 40; padding 0px 12px; radius 8px; background #262322 `color.ink.800`; text Geist Variable 18/28.8 400, #efede5 `color.paper.200` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.framer-SWyCz.framer-i5yBN: outline 1px auto rgb(16, 16, 16) offset 1px |
| hover | size unmeasured — the capture failed on this pass |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Sign-in button
The outlined "Sign in" button; links to account.chargetrip.com, measured never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 83 x 40; padding 0px 12px; radius 8px; background transparent; text Geist Variable 18/28.8 400, #262322 `color.ink.800` |
| focus-visible | outline 1px auto #101010, offset 1px; text Geist Variable 18/28.8 400, #282322; child paint a.framer-SWyCz.framer-i5yBN: size 83.0x40.0; radius 8px; outline 1px auto rgb(16, 16, 16) offset 1px; a::after.framer-SWyCz.framer-i5yBN: border 1px solid #282322 |
| hover | size unmeasured — the capture failed on this pass |

Child layers that carry the look: a::after 83pxx40px border 1px solid #262322 `color.ink.800` radius 8px.

![Sign-in button default](components/crops/nav-signin-default.png) ![Sign-in button focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign-in button pressed](components/crops/nav-signin-pressed.png)

### Home

The dark hero band, the orange CTAs and the Cirka display type.

#### Hero title
The 88px Cirka display headline on the dark hero card. Read as `hero-title` on the home page.

**Values (default).** size 855.34 x 156; background transparent; text Cirka Regular 88/78 400, #f4f3f2 `color.paper.100`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero subcopy
The muted lede under the display headline. Read as `hero-sub` on the home page.

**Values (default).** size 647.98 x 86.39; background transparent; text Geist Variable 18/28.8 400, rgba(255, 255, 251, 0.52) `color.white-alpha.52`.

![Hero subcopy default](components/crops/hero-sub-default.png)

#### Hero band
The dark rounded hero card the headline sits on. Read as `hero-card` on the home page.

**Values (default).** size 1391.98 x 1086; padding 72px 48px 0px 48px; radius 24px; background transparent; image radial-gradient(103% 223% at 49.2% 170.8%, #38312f 35%, #262321 67.3371%); text Cirka Regular 88/78 400, #f4f3f2 `color.paper.100`; icon 8 x 8, #0000ee.

![Hero band default](components/crops/hero-card-default.png)

#### Accent CTA
The orange "Book a demo" button (links to a HubSpot meeting page, never followed). Read as `cta-accent` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 148 x 48; padding 8px 12px; radius 8px; background #f94d00 `color.orange.500`; text Geist Variable 16/24 400, #f4f3f2 `color.paper.100`; icon 8 x 8, #0000ee |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.framer-0phDM.framer-npPic: outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | icon 8 x 8, #ff0000 |

![Accent CTA default](components/crops/cta-accent-default.png) ![Accent CTA hover](components/crops/cta-accent-hover.png) ![Accent CTA focus-visible](components/crops/cta-accent-focus-visible.png) ![Accent CTA pressed](components/crops/cta-accent-pressed.png)

#### Dark CTA
The dark "Plan a route" button with its map thumbnail (links to go.chargetrip.com, never followed). Read as `cta-dark` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 179 x 48; padding 8px 12px 8px 4px; radius 8px; background #44403f `color.ink.700`; text Geist Variable 16/24 400, #f4f3f2 `color.paper.100`; icon 8 x 8, #0000ee |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.framer-0phDM.framer-npPic: outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | icon 8 x 8, #ff0000 |

![Dark CTA default](components/crops/cta-dark-default.png) ![Dark CTA hover](components/crops/cta-dark-hover.png) ![Dark CTA focus-visible](components/crops/cta-dark-focus-visible.png) ![Dark CTA pressed](components/crops/cta-dark-pressed.png)

#### Section title
Read as `section-title` on the home page.

**Values (default).** size 619.98 x 144; background transparent; text Cirka Regular 48/48 400, #262322 `color.ink.800`.

![Section title default](components/crops/section-title-default.png)

#### Page ground
The body element's own painted fill — the warm-cream ground under every section. Read as `page-ground` on the home page.

**Values (default).** size 1440 x 8274.78; background #efede5 `color.paper.200`; text Cirka Regular 88/78 400, #f4f3f2 `color.paper.100`; icon 8 x 8, #0000ee.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Pricing

The API plan cards (one dark 'Popular' island), the logo-strip band and the usage slider.

#### Pricing title
"Build for free and go live with the best plan for you." in 88px Cirka. Read as `pricing-h1` on the pricing page.

**Values (default).** size 998.38 x 234; background transparent; text Cirka Regular 88/78 400, #262322 `color.ink.800`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Customer chip
A dark customer-logo chip under the headline (Plugsurfing). Read as `logo-chip` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 1247.98 x 93.5; padding 24px 0px; background #262322 `color.ink.800`; text Geist Variable 18/25.2 400, #f4f3f2 `color.paper.100` |
| hover | icon 24 x 24, #0000ee |
| focus-visible | outline 1px auto #005fcc, offset 1px; child paint a.framer-CVbmc.framer-ubeCh: outline 1px auto rgb(0, 95, 204) offset 1px |

![Customer chip default](components/crops/logo-chip-default.png) ![Customer chip hover](components/crops/logo-chip-hover.png) ![Customer chip focus-visible](components/crops/logo-chip-focus-visible.png) ![Customer chip pressed](components/crops/logo-chip-pressed.png)

#### Plan card (light)
The white Lite plan card. Read as `plan-card` on the pricing page.

**Values (default).** size 458.66 x 628.84; padding 72px; radius 24px; background #fffffb `color.paper.0`; text Cirka Regular 48/48 400, #262322 `color.ink.800`.

![Plan card (light) default](components/crops/plan-card-default.png)

#### Plan card (dark)
The dark Standard card under the "Most popular" banner. Read as `plan-card-dark` on the pricing page.

**Values (default).** size 442.67 x 586.84; padding 38px 72px 72px 72px; radius 16px; background #262322 `color.ink.800`; text Cirka Regular 48/48 400, #f4f3f2 `color.paper.100`.

![Plan card (dark) default](components/crops/plan-card-dark-default.png)

#### Plan CTA (accent)
The orange "Get started" inside the Standard card; links to the sign-up, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 107.78 x 40; padding 8px 12px; radius 8px; background #f94d00 `color.orange.500`; text Geist Variable 16/24 400, #f4f3f2 `color.paper.100` |
| hover | size 132.91 x 40; icon 8 x 8, #0000ee; child paint a.framer-0phDM.framer-npPic: size 132.9x40.0; div.framer-144aqy4: size 148.9x148.9; div.framer-e7hcqw: size 148.9x148.9 |
| focus-visible | outline 1px auto #005fcc, offset 1px; child paint a.framer-0phDM.framer-npPic: outline 1px auto rgb(0, 95, 204) offset 1px |

![Plan CTA (accent) default](components/crops/plan-cta-default.png) ![Plan CTA (accent) hover](components/crops/plan-cta-hover.png) ![Plan CTA (accent) focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA (accent) pressed](components/crops/plan-cta-pressed.png)

#### Plan CTA (dark)
A dark "Get started"/"Get a quote" plan action; never followed. Read as `plan-cta-dark` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 107.78 x 40; padding 8px 12px; radius 8px; background #44403f `color.ink.700`; text Geist Variable 16/24 400, #f4f3f2 `color.paper.100` |
| hover | size 110.14 x 40; child paint a.framer-0phDM.framer-npPic: size 110.1x40.0; div.framer-144aqy4: size 126.1x126.1; div.framer-e7hcqw: size 126.1x126.1 |
| focus-visible | outline 1px auto #005fcc, offset 1px; child paint a.framer-0phDM.framer-npPic: outline 1px auto rgb(0, 95, 204) offset 1px |

![Plan CTA (dark) default](components/crops/plan-cta-dark-default.png) ![Plan CTA (dark) hover](components/crops/plan-cta-dark-hover.png) ![Plan CTA (dark) focus-visible](components/crops/plan-cta-dark-focus-visible.png) ![Plan CTA (dark) pressed](components/crops/plan-cta-dark-pressed.png)

#### Popular tag
The "Most popular" label above the Standard card. Read as `popular-tag` on the pricing page.

**Values (default).** size 442.67 x 16; background transparent; text Geist 16/16 500, #f4f3f2 `color.paper.100`.

![Popular tag default](components/crops/popular-tag-default.png)

#### Feature row
An Includes list row with its orange check glyph. Read as `check-item` on the pricing page.

**Values (default).** size 294.66 x 22.41; background transparent; text Geist Variable 16/22.4 400, #262322 `color.ink.800`.

![Feature row default](components/crops/check-item-default.png)

#### Range slider
The price calculator's usage slider (0-3 steps); focused only, never dragged. Read as `range-slider` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 313.33 x 12; radius 24px; background transparent; image linear-gradient(to right, #f94d00 `color.orange.500` 0%, #f94d00 `color.orange.500` 0%, #44403f `color.ink.700` 0%, #44403f `color.ink.700` 100%); text sans-serif 12/normal 400, #101010; placeholder #101010 |
| focused | outline 1px auto #005fcc, offset 0px; child paint input: outline 1px auto rgb(0, 95, 204) offset 0px |

![Range slider default](components/crops/range-slider-default.png) ![Range slider focused](components/crops/range-slider-focused.png)

### Contact sales form

The Book-a-demo form fields; every input was focused, none was sent.

#### Contact title
"Grow your business with routing." in 64px Cirka. Read as `contact-h1` on the contact-sales page.

**Values (default).** size 622 x 128; background transparent; text Cirka Regular 64/64 400, #262322 `color.ink.800`.

![Contact title default](components/crops/contact-h1-default.png)

#### Text field
The First-name text field; filled with sample text then deleted, never submitted. Read as `form-input` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 283 x 16; background transparent; text Geist Regular 14/16.8 400, #071c1f `measured.form-ink`; placeholder #59524f `color.ink.500` |

![Text field default](components/crops/form-input-default.png) ![Text field focused](components/crops/form-input-focused.png) ![Text field filled](components/crops/form-input-filled.png)

#### E-mail field
The required E-mail field. Read as `form-email` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 283 x 16; background transparent; text Geist Regular 14/16.8 400, #071c1f `measured.form-ink`; placeholder #59524f `color.ink.500` |

![E-mail field default](components/crops/form-email-default.png) ![E-mail field focused](components/crops/form-email-focused.png)

#### Phone field
The optional Phone-number field. Read as `form-tel` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 283 x 16; background transparent; text Geist Regular 14/16.8 400, #071c1f `measured.form-ink`; placeholder #59524f `color.ink.500` |

![Phone field default](components/crops/form-tel-default.png) ![Phone field focused](components/crops/form-tel-focused.png)

#### Select
The Job-function native select; focused only, its dropdown never opened. Read as `form-select` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 295 x 40; padding 12px; background transparent; text Geist Regular 14/16.8 400, #000000 |

![Select default](components/crops/form-select-default.png) ![Select focused](components/crops/form-select-focused.png)

#### Textarea
The Message textarea. Read as `form-textarea` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 622 x 112; padding 12px; background transparent; text Geist Regular 14/16.8 400, #071c1f `measured.form-ink`; placeholder #59524f `color.ink.500` |

![Textarea default](components/crops/form-textarea-default.png) ![Textarea focused](components/crops/form-textarea-focused.png)

#### Submit button
The dark "Submit" button; measured in all non-submitting states, never pressed for real. Read as `form-submit` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 622 x 40; radius 10px; background #262322 `color.ink.800`; text Geist Medium 16/24 400, #efede5 `color.paper.200` |
| hover | background #59524f `color.ink.500`; child paint button.framer-siKYy.framer-Kue87: background #59524f `color.ink.500` |
| focus-visible | outline 1px auto #005fcc, offset 0px; child paint button.framer-siKYy.framer-Kue87: outline 1px auto rgb(0, 95, 204) offset 0px |

![Submit button default](components/crops/form-submit-default.png) ![Submit button hover](components/crops/form-submit-hover.png) ![Submit button focus-visible](components/crops/form-submit-focus-visible.png) ![Submit button pressed](components/crops/form-submit-pressed.png)

#### Book-a-demo card
The white "Book a demo · 30 minutes" card beside the form; never followed. Read as `demo-card` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 205.3 x 65.09; padding 8px 12px; radius 12px; background #fffffb `color.paper.0`; text Geist Variable 18/28.8 400, #262322 `color.ink.800` |
| hover | child paint div.framer-150syir: size 14.1x14.1 |

![Book-a-demo card default](components/crops/demo-card-default.png) ![Book-a-demo card hover](components/crops/demo-card-hover.png)

### Sign-in page (boundary)

account.chargetrip.io's public sign-in card, a different stack (Tailwind, oklch) from the Framer marketing site.

#### Sign-in title
"Sign in to your account." in 48px Cirka. Read as `signin-h1` on the sign-in page.

**Values (default).** size 384 x 96; background transparent; wrapper div.card.rounded-4xl: shadow oklch(0.9046 0.0199 87.52 / 0.32) 0px 0px 0px 1px, oklch(0 0 0 / 0.16) 0px 0px 1px 0px; text Cirka 48/48 400, oklch(0.2591 0.0049 39.4).

![Sign-in title default](components/crops/signin-h1-default.png)

#### E-mail field
The E-mail-address field on the sign-in card; filled with sample text then deleted, Continue never pressed. Read as `signin-input` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 358 x 46; background transparent; outline 2px solid transparent, offset 2px; wrapper div.input-form-control.will-change-color: outline 0px solid oklch(0.4444 0.0105 44.76); text Geist 14/20 500, oklch(0.2591 0.0049 39.4); transition color 0.2s ease-out, background-color 0.2s ease-out, border-color 0.2s ease-out, text-decoration-color 0.2s ease-out, fill 0.2s ease-out, stroke 0.2s ease-out; placeholder oklch(0.6015 0.0143 63.78) |

Child layers that carry the look: input 358x46.

![E-mail field default](components/crops/signin-input-default.png) ![E-mail field focused](components/crops/signin-input-focused.png)

#### Continue button
The dark Continue button; measured in all non-submitting states, never pressed for real. Read as `signin-continue` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 40; padding 0px 12px; border 2px solid transparent; radius 12px; background oklch(0.2591 0.0049 39.4); wrapper div.card.rounded-4xl: shadow oklch(0.9046 0.0199 87.52 / 0.32) 0px 0px 0px 1px, oklch(0 0 0 / 0.16) 0px 0px 1px 0px; text Geist 14/20 500, oklch(0.995 0.0034 67.78); transition color 0.15s cubic-bezier(0.2, 0, 0, 1), background-color 0.15s cubic-bezier(0.2, 0, 0, 1), border-color 0.15s cubic-bezier(0.2, 0, 0, 1), scale 0.15s cubic-bezier(0.2, 0, 0, 1) |
| hover | background oklch(0.3751 0.0058 34.3); child paint button.ct-link.base-button: background oklch(0.3751 0.0058 34.3) |
| focus-visible | outline 1px solid oklch(0.5152 0.0118 58.04), offset 1px; child paint button.ct-link.base-button: outline 1px solid oklch(0.5152 0.0118 58.04) offset 1px |
| pressed | size 372.48 x 38.8; background oklab(0.2591 0.00378639 0.00311018); transform scale(0.97); child paint button.ct-link.base-button: size 372.5x38.8; background oklab(0.2591 0.00378639 0.00311018) |

![Continue button default](components/crops/signin-continue-default.png) ![Continue button hover](components/crops/signin-continue-hover.png) ![Continue button focus-visible](components/crops/signin-continue-focus-visible.png) ![Continue button pressed](components/crops/signin-continue-pressed.png)

#### Create-account button
The secondary Create-account action; never followed. Read as `signin-create` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 40; padding 0px 12px; border 2px solid transparent; radius 12px; background oklch(0.9492 0.0111 89.72); wrapper div.card.rounded-4xl: shadow oklch(0.9046 0.0199 87.52 / 0.32) 0px 0px 0px 1px, oklch(0 0 0 / 0.16) 0px 0px 1px 0px; text Geist 14/20 500, oklch(0.2591 0.0049 39.4); transition color 0.15s cubic-bezier(0.2, 0, 0, 1), background-color 0.15s cubic-bezier(0.2, 0, 0, 1), border-color 0.15s cubic-bezier(0.2, 0, 0, 1), scale 0.15s cubic-bezier(0.2, 0, 0, 1) |
| hover | background oklab(0.9492 0.0000542448 0.0110999); child paint a.ct-link.base-button: background oklab(0.9492 0.0000542448 0.0110999) |
| focus-visible | outline 1px solid oklch(0.5152 0.0118 58.04), offset 1px; child paint a.ct-link.base-button: outline 1px solid oklch(0.5152 0.0118 58.04) offset 1px |
| pressed | size 372.48 x 38.8; background oklab(0.9492 0.0000542448 0.0110999); transform scale(0.97); child paint a.ct-link.base-button: size 372.5x38.8; background oklab(0.9492 0.0000542448 0.0110999) |

![Create-account button default](components/crops/signin-create-default.png) ![Create-account button hover](components/crops/signin-create-hover.png) ![Create-account button focus-visible](components/crops/signin-create-focus-visible.png) ![Create-account button pressed](components/crops/signin-create-pressed.png)

#### Trust row
A check-marked reassurance row under the hero panel. Read as `signin-trust` on the sign-in page.

**Values (default).** size 244 x 20; background transparent; text Geist 14/20 500, oklch(0.2591 0.0049 39.4).

![Trust row default](components/crops/signin-trust-default.png)

### Footer

The white footer panel on the cream page, its link columns and the status line.

#### Footer
The footer band: link columns, the "chargetrip presents" newsletter block, badges, the legal subfooter. Read as `footer` on the home page.

**Values (default).** size 1391.98 x 481.17; padding 24px 0px 0px 0px; radius 24px 24px 0px 0px; background #fffffb `color.paper.0`; text Geist Variable 16/24 400, #877f78 `color.ink.300`; icon 94 x 20.02, #000000.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 65 x 21; background transparent; text Geist Variable 16/22.4 400, #262322 `color.ink.800` |
| hover | text Geist Variable 16/22.4 400, #f94d00 `color.orange.500` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.framer-text.framer-styles-preset-zjjg3u: size 65.0x21.0; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Geist Variable 16/22.4 400, #f94d00 `color.orange.500` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 61 x 21; background transparent; text Geist Variable 16/22.4 400, #262322 `color.ink.800` |
| hover | text Geist Variable 16/22.4 400, #f94d00 `color.orange.500` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.framer-text.framer-styles-preset-zjjg3u: size 61.0x21.0; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Geist Variable 16/22.4 400, #f94d00 `color.orange.500` |

![Social link default](components/crops/footer-social-default.png) ![Social link hover](components/crops/footer-social-hover.png) ![Social link focus-visible](components/crops/footer-social-focus-visible.png) ![Social link pressed](components/crops/footer-social-pressed.png)

#### Newsletter CTA
The footer newsletter "Sign up" button; never followed. Read as `newsletter-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 56 x 21; background transparent; text Geist Variable 16/22.4 400, #262322 `color.ink.800` |
| hover | text Geist Variable 16/22.4 400, #f94d00 `color.orange.500` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.framer-text.framer-styles-preset-zjjg3u: size 56.0x21.0; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Geist Variable 16/22.4 400, #f94d00 `color.orange.500` |

![Newsletter CTA default](components/crops/newsletter-cta-default.png) ![Newsletter CTA hover](components/crops/newsletter-cta-hover.png) ![Newsletter CTA focus-visible](components/crops/newsletter-cta-focus-visible.png) ![Newsletter CTA pressed](components/crops/newsletter-cta-pressed.png)

#### Status pill
The "● Stable" status link in the footer (green dot; links to status.chargetrip.com, never followed). Read as `status-pill` on the home page.

**Values (default).** size 208.33 x 171.22; background transparent; text Geist Variable 16/24 400, #877f78 `color.ink.300`.

Child layers that carry the look: div 8x8 background #278859 radius 100%.

![Status pill default](components/crops/status-pill-default.png)

### Mobile (390 wide)

The same surface at phone width, with its menu overlay.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 64; padding 0px 8px; background transparent; text Geist Variable 18/28.8 400, #262322 `color.ink.800`; icon 106 x 24, #000000.

Child layers that carry the look: div 374x64 background rgba(252, 252, 251, 0) radius 12px; div::after 374pxx64px border 1px solid #efede5 `color.paper.200` radius 12px; a::after 83pxx40px border 1px solid #262322 `color.ink.800` radius 8px.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The dark-teal hamburger at the bar's right edge; its own press opens the menu overlay. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 40 x 40; padding 12px; radius 8px; background #071c1f `measured.form-ink`; text sans-serif 12/normal 400, #000000.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The full-screen menu overlay after the trigger's own toggle: orange No-code card, dark API card, Integration Partners, the Use-cases list. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 828; background transparent; text Geist Regular 16/24 400, #fffffb `color.paper.0`; icon 106 x 24, #000000.

Child layers that carry the look: div 390x828 background rgba(0, 0, 0, 0.2); div 373.9x828 background #fffffb `color.paper.0` radius 3.20856% / 1.44928% shadow rgba(0, 0, 0, 0.12) 0px 0px 40px 0px; div 479x40 background #262322 `color.ink.800` radius 0px 0px 12px 12px.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile menu card
The orange No-code card in the open mobile menu. Read as `m-menu-card` on the home page at 390 wide.

**Values (default).** size 350 x 86; padding 16px; radius 8px; background #f94d00 `color.orange.500`; text PP Cirka Medium 28/30 400, #efede5 `color.paper.200`.

![Mobile menu card default](components/crops/m-menu-card-default.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 326 x 208; background transparent; text Cirka Regular 56/52 400, #f4f3f2 `color.paper.100`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Chargetrip's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The product itself.** Chargetrip's routing engine, dashboard and API responses are behind sign-in; account.chargetrip.io's card was measured but never filled beyond the documented test text, and developers.chargetrip.com / playground.chargetrip.com were captured as boundaries, never used.
- **Anything that sends, books or signs in.** No demo was booked, no form was submitted, no account was created; the Book-a-demo / Plan-a-route / Contact-sales / Sign-in / Create-account / Send actions were never followed.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The marketing site paints one light theme on every captured route; the Framer bundle declares no dark variant (the hero band and the Popular plan card are dark islands inside the light theme, not a theme switch).

### Fonts

- **The UI fonts** are webfonts the Framer bundle declares (83 @font-face entries — Inter, Geist, Cirka, Fragment Mono; `fonts` in [raw/css-vars.json](raw/css-vars.json)); the font files themselves are not committed.
- Illustration, map and wordmark artwork in the screenshots are Chargetrip's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The route-map imagery, customer logos and the wordmark are Chargetrip's content; only the frames and components were measured.
