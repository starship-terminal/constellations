# Acctual components

The discovery list of every page and view captured, then one entry per component with crops of the real site, the icon index and the Gaps. Captured from acctual.com on 2026-11-10, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was sent or submitted: the app.acctual.com Log-in and Sign-up links were never opened, and no consent banner ever rendered (none was answered).

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (49 components, 91 states). The page layouts at four widths are in [raw/layout.json](raw/layout.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `system-ui 64/70.4 600, #262626`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (88 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (acctual.com has one theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 390 wide.

| Surface | URL | Screenshots |
|---|---|---|
| Home. Display hero, interactive invoice mock, fee rows, FAQ. | `/` | [default](screenshots/home-light-default.png), [faq-open](screenshots/home-light-faq-open.png), [full](screenshots/home-light-full.png), [invoice-demo](screenshots/home-light-invoice-demo.png) |
| Pricing. The fee comparison. | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Teams. The team plan page. Sitemap only; not in the current nav. | `/teams` | [default](screenshots/teams-light-default.png), [full](screenshots/teams-light-full.png) |
| About. Company page. Sitemap only; not in the current nav. | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Blog index. | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Blog post. Acctual joins Altitude. | `/blog/acctual-joins-altitude` | [default](screenshots/blog-post-light-default.png), [full](screenshots/blog-post-light-full.png) |
| Altitude announcement page the banner links to. | `/altitude` | [default](screenshots/altitude-light-default.png), [full](screenshots/altitude-light-full.png) |
| Freelancer invoicing. Persona landing page. | `/freelancer-invoicing` | [default](screenshots/freelancer-invoicing-light-default.png), [full](screenshots/freelancer-invoicing-light-full.png) |
| Agency invoicing. The nav Agency link. | `/agency-invoicing` | [default](screenshots/agency-invoicing-light-default.png), [full](screenshots/agency-invoicing-light-full.png) |
| Stablecoin invoicing. Product landing page. | `/stablecoin-invoicing` | [default](screenshots/stablecoin-invoicing-light-default.png), [full](screenshots/stablecoin-invoicing-light-full.png) |
| USDC invoicing. Product landing page. | `/usdc-invoicing` | [default](screenshots/usdc-invoicing-light-default.png), [full](screenshots/usdc-invoicing-light-full.png) |
| USDT invoicing. Product landing page. | `/usdt-invoicing` | [default](screenshots/usdt-invoicing-light-default.png), [full](screenshots/usdt-invoicing-light-full.png) |
| Exporters landing page. | `/exporters` | [default](screenshots/exporters-light-default.png), [full](screenshots/exporters-light-full.png) |
| Invoice templates. Footer link. | `/invoice-templates` | [default](screenshots/invoice-templates-light-default.png), [full](screenshots/invoice-templates-light-full.png) |
| FreshBooks alternative. Footer link. | `/freshbooks-alternative` | [default](screenshots/freshbooks-alternative-light-default.png), [full](screenshots/freshbooks-alternative-light-full.png) |
| Free invoice software. Reached from the public graph. | `/free-invoice-software` | [default](screenshots/free-invoice-software-light-default.png), [full](screenshots/free-invoice-software-light-full.png) |
| US to Japan corridor. Sitemap template, not linked from the homepage footer. | `/locations/us-to-japan` | [default](screenshots/location-light-default.png), [full](screenshots/location-light-full.png) |
| US to UK corridor. Footer link. | `/locations/us-to-uk` | [default](screenshots/location-us-uk-light-default.png), [full](screenshots/location-us-uk-light-full.png) |
| Terms. Legal text. | `/terms` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| Privacy. Legal text. | `/privacy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Retired homepage. Sitemap only. | `/old-home` | [default](screenshots/old-home-light-default.png), [full](screenshots/old-home-light-full.png) |
| Retired blog index. Sitemap only. | `/blog-old` | [default](screenshots/blog-old-light-default.png), [full](screenshots/blog-old-light-full.png) |
| The published 404 page. | `/404` | [default](screenshots/not-found-light-default.png), [full](screenshots/not-found-light-full.png) |
| Footer-linked post. Recurring invoices. | `/blog/how-to-set-up-recurring-invoices` | [default](screenshots/blog-recurring-light-default.png), [full](screenshots/blog-recurring-light-full.png) |
| Footer-linked post. Graphic design invoice. | `/blog/graphic-design-invoice` | [default](screenshots/blog-graphic-light-default.png), [full](screenshots/blog-graphic-light-full.png) |
| Footer-linked post. Web design invoice. | `/blog/web-design-development-invoice` | [default](screenshots/blog-web-light-default.png), [full](screenshots/blog-web-light-full.png) |
| Footer-linked post. Video production invoice. | `/blog/video-film-production-invoices` | [default](screenshots/blog-video-light-default.png), [full](screenshots/blog-video-light-full.png) |
| Footer-linked post. PayPal invoice fees. | `/blog/paypal-invoice-fees-are-they-worth-it` | [default](screenshots/blog-paypal-light-default.png), [full](screenshots/blog-paypal-light-full.png) |
| Footer-linked post. Upwork alternatives. | `/blog/best-upwork-alternatives-12-platforms-to-find-better-work-in-2026` | [default](screenshots/blog-upwork-light-default.png), [full](screenshots/blog-upwork-light-full.png) |
| Footer-linked post. Past due vs overdue. | `/blog/past-due-vs-overdue-invoices` | [default](screenshots/blog-pastdue-light-default.png), [full](screenshots/blog-pastdue-light-full.png) |
| Public help centre. Getting started. | `https://guides.acctual.com/guide/getting-started` | [default](screenshots/guide-light-default.png), [full](screenshots/guide-light-full.png) |
| Public help centre. Overview. | `https://guides.acctual.com/guide/overview` | [default](screenshots/guide-overview-light-default.png), [full](screenshots/guide-overview-light-full.png) |
| Public help centre. Create and send an invoice. | `https://guides.acctual.com/guide/send-an-invoice/create-send-an-invoice` | [default](screenshots/guide-invoice-light-default.png), [full](screenshots/guide-invoice-light-full.png) |
| Public help centre. Pay a bill from wallet. | `https://guides.acctual.com/guide/pay-a-bill/pay-a-bill-from-wallet` | [default](screenshots/guide-pay-light-default.png), [full](screenshots/guide-pay-light-full.png) |
| Public help centre. Rates and fees. | `https://guides.acctual.com/guide/resources/rates-fees` | [default](screenshots/guide-rates-light-default.png), [full](screenshots/guide-rates-light-full.png) |
| Home at 390: collapsed header, the opened menu, single-column cards. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Pricing at 390. | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Blog index at 390. | `/blog` | [default](screenshots/mobile-blog-light-default.png), [full](screenshots/mobile-blog-light-full.png) |
| Freelancer invoicing at 390. | `/freelancer-invoicing` | [default](screenshots/mobile-freelancer-invoicing-light-default.png), [full](screenshots/mobile-freelancer-invoicing-light-full.png) |
| Agency invoicing at 390. | `/agency-invoicing` | [default](screenshots/mobile-agency-invoicing-light-default.png), [full](screenshots/mobile-agency-invoicing-light-full.png) |
| Altitude announcement at 390. | `/altitude` | [default](screenshots/mobile-altitude-light-default.png), [full](screenshots/mobile-altitude-light-full.png) |
| Invoice templates at 390. | `/invoice-templates` | [default](screenshots/mobile-invoice-templates-light-default.png), [full](screenshots/mobile-invoice-templates-light-full.png) |
| Altitude blog post at 390. | `/blog/acctual-joins-altitude` | [default](screenshots/mobile-blog-post-light-default.png), [full](screenshots/mobile-blog-post-light-full.png) |
| US to UK corridor at 390. | `/locations/us-to-uk` | [default](screenshots/mobile-location-light-default.png), [full](screenshots/mobile-location-light-full.png) |
| Terms at 390. Full page is truncated at 8 tiles. | `/terms` | [default](screenshots/mobile-terms-light-default.png), [full](screenshots/mobile-terms-light-full.png) |
| Privacy at 390. Full page is truncated at 8 tiles. | `/privacy` | [default](screenshots/mobile-privacy-light-default.png), [full](screenshots/mobile-privacy-light-full.png) |
| Getting started guide at 390. | `https://guides.acctual.com/guide/getting-started` | [default](screenshots/mobile-guide-light-default.png), [full](screenshots/mobile-guide-light-full.png) |
| Create-invoice guide at 390. | `https://guides.acctual.com/guide/send-an-invoice/create-send-an-invoice` | [default](screenshots/mobile-guide-invoice-light-default.png), [full](screenshots/mobile-guide-invoice-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu, open | home at 390 | the nav trigger pressed (a local disclosure) | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-nav-panel](#m-nav-panel) |
| Invoice demo | home hero | the interactive invoice mock scrolled into view; a marketing demo, not a live product | [home-light-invoice-demo](screenshots/home-light-invoice-demo.png), [invoice-demo](#invoice-demo) |
| FAQ answer, open | home FAQs | the question pressed (a local accordion disclosure) | [home-light-faq-open](screenshots/home-light-faq-open.png), [faq-item](#faq-item) |
| App sign-in / sign-up | nav links out to app.acctual.com | recorded at https://app.acctual.com/sign-in (email, password, Continue with Google); nothing typed, Google not clicked, branch stopped | no screenshot; documented under Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 12 components were given a real keyboard focus. 12 draw a ring: `nav-logo` (1px auto #005fcc `focus`, offset 1px), `nav-link` (1px auto #005fcc `focus`, offset 1px), `nav-cta` (1px auto #005fcc `focus`, offset 1px), `nav-login` (1px auto #005fcc `focus`, offset 1px), `announcement` (1px auto #005fcc `focus`, offset 1px), `footer-link` (1px auto #005fcc `focus`, offset 1px), `plan-cta` (1px auto #005fcc `focus`, offset 1px), `blog-post-link` (1px auto #005fcc `focus`, offset 1px), `altitude-link` (1px auto #005fcc `focus`, offset 1px), `freelancer-invoicing-cta` (1px auto #005fcc `focus`, offset 1px), `stablecoin-invoicing-cta` (1px auto #005fcc `focus`, offset 1px), `location-cta` (1px auto #005fcc `focus`, offset 1px). The other 0 draw none, so a keyboard user sees no change: . Focus could not be captured on 1 more (keyboard focus never landed on them, so their readings are left out): `m-menu-trigger`.

**Pressed.** Forced `:active` was applied to the buttons and links above; the buttons keep their fills, and Framer's stylesheet paints the links `#ff0000` under `:active`. See each entry's Pressed row for what did move.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|

**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).

| Page | 1440 | 1920 | 1024 | 390 |
|---|---|---|---|---|
| home | content x 208, 1024 wide; grid 325.3 325.3 325.3 gap 24px | content x 448, 1024 wide; grid 325.3 325.3 325.3 gap 24px | content x 0, 1024 wide; grid 476 476 gap 24px | content x 24, 342 wide; grid 171 171 gap 0px |
| pricing | content x 208, 1024 wide | content x 448, 1024 wide | content x 0, 1024 wide | content x 0, 390 wide; grid 171 171 gap 0px |
| teams | content x 208, 1024 wide | content x 448, 1024 wide | content x 0, 1024 wide; grid 428 428 gap 24px | content x 24, 342 wide; grid 171 171 gap 0px |
| about | content x 208, 1024 wide | content x 448, 1024 wide | content x 0, 1024 wide; grid 428 428 gap 24px | content x 24, 342 wide; grid 171 171 gap 0px |
| blog | content x 204, 1032 wide | content x 444, 1032 wide | content x 0, 1024 wide | content x 0, 390 wide; grid 171 171 gap 0px |
| freelancer-invoicing | content x 208, 1024 wide | content x 448, 1024 wide | content x 0, 1024 wide | content x 24, 342 wide; grid 171 171 gap 0px |
| stablecoin-invoicing | content x 120, 1200 wide | content x 360, 1200 wide | content x 50, 924 wide | content x 16, 358 wide; grid 171 171 gap 0px |
| location | content x 292, 856 wide; grid 508 508 gap 24px | content x 532, 856 wide; grid 508 508 gap 24px | content x 125, 775 wide; grid 460 460 gap 24px | content x 16, 358 wide; grid 171 171 gap 0px |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Persona card](#persona-card) | 325.33 x 166 | - | 16px | #fafafa `paper` | none | 24px |
| [Fee comparison row](#fee-comparison-row) | 1024 x 64 | - | - | rgba(240, 240, 240, 0.95) `row` | none | 0 |
| [Invoice demo](#invoice-demo) | 514.92 x 294.11 | - | 16px | #ffffff `white` | rgba(10, 13, 20, 0.03) 0px 1px 2px 0px | 28px 28px 24px 28px |
| [FAQ item](#faq-item) | 1024 x 25 | - | - | - | none | 0 |
| [Blog item](#blog-item) | 1032 x 90.84 | - | - | transparent | none | 0 |
| [Nav CTA](#nav-cta) | 148.56 x 40 | - | 100px | #0d111b `cta` | #242628 0px 0px 0px 1px, rgba(27, 28, 29, 0.48) 0px 1px 2px 0px | 6px 14px |

## Components

### Shell and navigation

The shell every page shares: a top bar with the Acctual wordmark, the Freelancer / Agency / Pricing / Blog links, Log in and the dark Sign-up pill, under the 'Acctual is joining Altitude' announcement strip; and a footer with the 'Create the world&rsquo;s most flexible invoice in seconds' heading, link columns and the 'from NYC' credit.

#### Top navigation bar <a id="nav-bar"></a>
The top bar: wordmark, Freelancer / Agency / Pricing / Blog links, Log in and the Sign-up pill. Read as `nav-bar` on the home page.

**Values (default).** size 1440 x 80; padding 0px 20px; background transparent; text Inter 14/24 500, #0098f2 `blue`; icon 14 x 14, #0000ee.

Child layers that carry the look: div 1034x80 background rgba(245, 245, 245, 0.6) `frost` radius 0px 0px 20px 20px shadow rgba(0, 0, 0, 0.1) `nav-shadow` 0px 1px 2px 0px; div 112x16 image url(data:…)%22></path><path d=%22M 17.846 0.4 C 17.846 0.179 17.667 0 17.446 0 L 14.554 0 ; a 148.6x40 background #0d111b `cta` radius 100px shadow #242628 `cta-ring` 0px 0px 0px 1px, rgba(27, 28, 29, 0.48) `cta-shadow` 0px 1px 2px 0px.

![Top navigation bar default](components/crops/nav-bar-default.png)

#### Logo <a id="nav-logo"></a>
The Acctual wordmark linking home. Read as `nav-logo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 112 x 32; padding 8px 0px; background transparent; text sans-serif 12/normal 400, #0000ee |
| focus-visible | outline 1px auto #005fcc `focus`, offset 1px |
| pressed | text sans-serif 12/normal 400, #ff0000 `pressed` |

Child layers that carry the look: div 112x16 image url(data:…)%22></path><path d=%22M 17.846 0.4 C 17.846 0.179 17.667 0 17.446 0 L 14.554 0 .

![Logo default](components/crops/nav-logo-default.png) ![Logo hover](components/crops/nav-logo-hover.png) ![Logo focus-visible](components/crops/nav-logo-focus-visible.png) ![Logo pressed](components/crops/nav-logo-pressed.png)

#### Nav link <a id="nav-link"></a>
A section link in the top bar. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 74.63 x 35.36; padding 8px 12px; radius 100px; background transparent; text Open Runde 16/19.36 500, rgba(30, 30, 30, 0.7) `ink-70` |
| hover | text Open Runde 16/19.36 500, #000000 `cta-edge` |
| focus-visible | outline 1px auto #005fcc `focus`, offset 1px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Nav CTA <a id="nav-cta"></a>
The "Sign up for free" pill. Hovered and focused only; app.acctual.com is never opened. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 148.56 x 40; padding 6px 14px; radius 100px; background #0d111b `cta`; shadow #242628 0px 0px 0px 1px, rgba(27, 28, 29, 0.48) 0px 1px 2px 0px; text Open Runde 16/24 500, #ffffff `white` |
| hover | background rgba(0, 0, 0, 0.88) `black-88` |
| focus-visible | outline 1px auto #005fcc `focus`, offset 1px |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Log-in link <a id="nav-login"></a>
The plain Log-in link beside the CTA. app.acctual.com is never opened. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 80.41 x 40; padding 6px 14px; radius 100px; background transparent; text Open Runde 16/24 500, rgba(30, 30, 30, 0.6) `ink-60` |
| hover | text Open Runde 16/24 500, #1e1e1e `ink` |
| focus-visible | outline 1px auto #005fcc `focus`, offset 1px |

![Log-in link default](components/crops/nav-login-default.png) ![Log-in link hover](components/crops/nav-login-hover.png) ![Log-in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log-in link pressed](components/crops/nav-login-pressed.png)

#### Announcement banner <a id="announcement"></a>
The "Acctual is joining Altitude" strip above the nav, linking to /altitude. Read as `announcement` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1034 x 32; padding 4px 14px 4px 20px; background transparent; text Inter 14/24 500, #0098f2 `blue`; icon 14 x 14, #0000ee |
| focus-visible | outline 1px auto #005fcc `focus`, offset 1px |
| pressed | icon 14 x 14, #ff0000 `pressed` |

![Announcement banner default](components/crops/announcement-default.png) ![Announcement banner hover](components/crops/announcement-hover.png) ![Announcement banner focus-visible](components/crops/announcement-focus-visible.png) ![Announcement banner pressed](components/crops/announcement-pressed.png)

#### Footer <a id="footer"></a>
The footer band: the "Create the world’s most flexible invoice" heading, link columns and the "from NYC" credit. Read as `footer` on the home page.

**Values (default).** size 1024 x 404; background transparent; text Open Runde 20/28 600, #1e1e1e `ink`; icon 112 x 40, #1e1e1e `ink`.

Child layers that carry the look: a 163.1x40 background #0d111b `cta` radius 100px shadow #242628 `cta-ring` 0px 0px 0px 1px, rgba(27, 28, 29, 0.48) `cta-shadow` 0px 1px 2px 0px; a::after 163.141pxx40px border 1px solid #000000 `cta-edge` radius 100px.

![Footer default](components/crops/footer-default.png)

#### Footer heading <a id="footer-heading"></a>
The sign-off heading in the footer. Read as `footer-heading` on the home page.

**Values (default).** size 256 x 56; background transparent; text Open Runde 20/28 600, #1e1e1e `ink`.

![Footer heading default](components/crops/footer-heading-default.png)

#### Footer link <a id="footer-link"></a>
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40.08 x 17; background transparent; text Open Runde 14/20 500, #8d8d8d `muted` |
| hover | text Open Runde 14/20 500, rgba(0, 0, 0, 0.9) `black-90` |
| focus-visible | outline 1px auto #005fcc `focus`, offset 1px |
| pressed | text Open Runde 14/20 500, rgba(0, 0, 0, 0.9) `black-90` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Home

The home page: the 'Small business invoices: Get paid on time' display hero with the interactive invoice mock (a marketing demo, not a live product), the fee-comparison rows, persona cards, the security trust rows and the FAQ accordion.

#### Hero title <a id="hero-title"></a>
"Small business invoices: Get paid on time" — the display headline. Read as `hero-title` on the home page.

**Values (default).** size 768 x 72; background transparent; text Open Runde 64/72 600, #1e1e1e `ink`.

![Hero title default](components/crops/hero-title-default.png)

#### Invoice demo <a id="invoice-demo"></a>
The interactive invoice mock in the hero (a marketing demo, not a live product): payment-method dropdown, amount and currency fields. Read as `invoice-demo` on the home page.

**Values (default).** size 514.92 x 294.11; padding 28px 28px 24px 28px; background transparent; text Open Runde 12/16 500, #8b8b8b `muted-2`.

Child layers that carry the look: div::after 498pxx260px border 1px solid #eeeeee `line-3`; div 146.4x77.7 background #ffffff `white` radius 16px shadow rgba(10, 13, 20, 0.03) 0px 1px 2px 0px; div::after 142pxx68px border 1px solid #d8d8d8 `line` radius 16px.

![Invoice demo default](components/crops/invoice-demo-default.png)

#### Section title <a id="section-title"></a>
A section heading ("We designed an invoice that works harder for your business"). Read as `section-title` on the home page.

**Values (default).** size 768 x 96; background transparent; text Open Runde 40/48 600, #1e1e1e `ink`.

![Section title default](components/crops/section-title-default.png)

#### Fee item <a id="fee-item"></a>
A fee-comparison row (1% bank transfer / 2.7% card / 1% stablecoin). Read as `fee-item` on the home page.

**Values (default).** size 82.89 x 24; background transparent; text Open Runde 16/24 500, #0098f2 `blue`.

![Fee item default](components/crops/fee-item-default.png)

#### Persona card <a id="persona-card"></a>
A who-it-is-for card (Contractors). Read as `persona-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 325.33 x 166; padding 24px; radius 16px; background #fafafa `paper`; text Open Runde 20/28 600, #1e1e1e `ink`; icon 18 x 20, #0000ee |

![Persona card default](components/crops/persona-card-default.png) ![Persona card hover](components/crops/persona-card-hover.png)

#### Security item <a id="security-item"></a>
A trust row (PCI standards / SSL encryption & tokenization). Read as `security-item` on the home page.

**Values (default).** size 500 x 84; background transparent; text Open Runde 20/28 600, #1e1e1e `ink`.

![Security item default](components/crops/security-item-default.png)

#### FAQ item <a id="faq-item"></a>
An accordion question in the FAQs section; toggled open once (a local disclosure). Read as `faq-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1024 x 25; background transparent; text Open Runde 16/24 500, #1e1e1e `ink` |
| open | size 1024 x 120 |

Child layers that carry the look: div 18x5 image url(data:…)%22></path></svg>"); div 5x18 image url(data:…)%22></path></svg>").

![FAQ item default](components/crops/faq-item-default.png) ![FAQ item open](components/crops/faq-item-open.png)

### Pricing

The pricing page: the fee comparison (bank transfer / card / stablecoin, currencies, payout speed) and the same Sign-up CTA.

#### Page title <a id="pricing-title"></a>
Read as `pricing-title` on the pricing page.

**Values (default).** size 768 x 112; background transparent; text Open Runde 48/56 600, #1e1e1e `ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Fee comparison row <a id="fee-row"></a>
A comparison row on the pricing page (payment method, currencies, payout). Read as `fee-row` on the pricing page.

**Values (default).** size 1024 x 64; background rgba(240, 240, 240, 0.95) `row`; text Open Runde 14/20 500, #1e1e1e `ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Page CTA <a id="plan-cta"></a>
Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 148.56 x 40; padding 6px 14px; radius 100px; background #0d111b `cta`; shadow #242628 0px 0px 0px 1px, rgba(27, 28, 29, 0.48) 0px 1px 2px 0px; text Open Runde 16/24 500, #ffffff `white` |
| focus-visible | outline 1px auto #005fcc `focus`, offset 1px |

![Page CTA default](components/crops/plan-cta-default.png) ![Page CTA hover](components/crops/plan-cta-hover.png) ![Page CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Page CTA pressed](components/crops/plan-cta-pressed.png)

### Company and content pages

Teams, About, the blog index, one post (the Altitude announcement) and the /altitude page the banner links to.

#### Page title <a id="teams-title"></a>
Read as `teams-title` on the teams page.

**Values (default).** size 768 x 112; background transparent; text Open Runde 48/56 600, #1e1e1e `ink`.

![Page title default](components/crops/teams-title-default.png)

#### Body text <a id="teams-body"></a>
Read as `teams-body` on the teams page.

**Values (default).** size 600 x 48; background transparent; text Open Runde 16/24 500, #8d8d8d `muted`.

![Body text default](components/crops/teams-body-default.png)

#### Page title <a id="about-title"></a>
Read as `about-title` on the about page.

**Values (default).** size 768 x 112; background transparent; text Open Runde 48/56 600, #1e1e1e `ink`.

![Page title default](components/crops/about-title-default.png)

#### Body text <a id="about-body"></a>
Read as `about-body` on the about page.

**Values (default).** size 600 x 48; background transparent; text Open Runde 16/24 500, #8d8d8d `muted`.

![Body text default](components/crops/about-body-default.png)

#### Page title <a id="blog-title"></a>
Read as `blog-title` on the blog page.

**Values (default).** size 130.02 x 72; background transparent; text Open Runde 64/72 600, #1e1e1e `ink`.

![Page title default](components/crops/blog-title-default.png)

#### Body text <a id="blog-body"></a>
Read as `blog-body` on the blog page.

**Values (default).** size 388 x 72; background transparent; text Open Runde 16/24 500, #8d8d8d `muted`.

![Body text default](components/crops/blog-body-default.png)

#### Blog item <a id="blog-item"></a>
A post row or card on the blog index. Read as `blog-item` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1032 x 90.84; background transparent; text Open Runde 20/28 600, #1e1e1e `ink` |

![Blog item default](components/crops/blog-item-default.png) ![Blog item hover](components/crops/blog-item-hover.png)

#### Page title <a id="blog-post-title"></a>
Read as `blog-post-title` on the blog post page.

**Values (default).** size 800 x 42; background transparent; text Open Runde 30/42 600, #000000 `cta-edge`.

![Page title default](components/crops/blog-post-title-default.png)

#### Body text <a id="blog-post-body"></a>
Read as `blog-post-body` on the blog post page.

**Values (default).** size 800 x 25.59; background transparent; text Open Runde 16/25.6 400, #666666 `grey`.

![Body text default](components/crops/blog-post-body-default.png)

#### Back link <a id="blog-post-link"></a>
The link returning to the index. Read as `blog-post-link` on the blog post page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 56.69 x 35.36; padding 8px 12px; radius 100px; background transparent; text Open Runde 16/19.36 500, rgba(30, 30, 30, 0.7) `ink-70` |
| hover | text Open Runde 16/19.36 500, #000000 `cta-edge` |
| focus-visible | outline 1px auto #005fcc `focus`, offset 1px |

![Back link default](components/crops/blog-post-link-default.png) ![Back link hover](components/crops/blog-post-link-hover.png) ![Back link focus-visible](components/crops/blog-post-link-focus-visible.png) ![Back link pressed](components/crops/blog-post-link-pressed.png)

#### Page title <a id="altitude-title"></a>
Read as `altitude-title` on the Altitude announcement page.

**Values (default).** size 768 x 112; background transparent; text Open Runde 48/56 600, #ffffff `white`.

![Page title default](components/crops/altitude-title-default.png)

#### Body text <a id="altitude-body"></a>
Read as `altitude-body` on the Altitude announcement page.

**Values (default).** size 600 x 48; background transparent; text Open Runde 16/24 500, #ffffff `white`.

![Body text default](components/crops/altitude-body-default.png)

#### Back link <a id="altitude-link"></a>
The link returning to the index. Read as `altitude-link` on the Altitude announcement page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 56.69 x 35.36; padding 8px 12px; radius 100px; background transparent; text Open Runde 16/19.36 500, rgba(30, 30, 30, 0.7) `ink-70` |
| hover | text Open Runde 16/19.36 500, #000000 `cta-edge` |
| focus-visible | outline 1px auto #005fcc `focus`, offset 1px |

![Back link default](components/crops/altitude-link-default.png) ![Back link hover](components/crops/altitude-link-hover.png) ![Back link focus-visible](components/crops/altitude-link-focus-visible.png) ![Back link pressed](components/crops/altitude-link-pressed.png)

### Landing pages (programmatic)

The templated landing pages: freelancer-invoicing, stablecoin-invoicing and one location corridor (US to Japan) standing in for the ~30 corridor pages.

#### Page title <a id="freelancer-invoicing-title"></a>
Read as `freelancer-invoicing-title` on the freelancer invoicing page.

**Values (default).** size 780 x 112; background transparent; text Open Runde 48/56 600, #1e1e1e `ink`.

![Page title default](components/crops/freelancer-invoicing-title-default.png)

#### Page CTA <a id="freelancer-invoicing-cta"></a>
Read as `freelancer-invoicing-cta` on the freelancer invoicing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 148.56 x 40; padding 6px 14px; radius 100px; background #0d111b `cta`; shadow #242628 0px 0px 0px 1px, rgba(27, 28, 29, 0.48) 0px 1px 2px 0px; text Open Runde 16/24 500, #ffffff `white` |
| hover | background rgba(0, 0, 0, 0.88) `black-88` |
| focus-visible | outline 1px auto #005fcc `focus`, offset 1px |

![Page CTA default](components/crops/freelancer-invoicing-cta-default.png) ![Page CTA hover](components/crops/freelancer-invoicing-cta-hover.png) ![Page CTA focus-visible](components/crops/freelancer-invoicing-cta-focus-visible.png) ![Page CTA pressed](components/crops/freelancer-invoicing-cta-pressed.png)

#### Section title <a id="freelancer-invoicing-section"></a>
Read as `freelancer-invoicing-section` on the freelancer invoicing page.

**Values (default).** size 640 x 96; background transparent; text Open Runde 40/48 600, #1e1e1e `ink`.

![Section title default](components/crops/freelancer-invoicing-section-default.png)

#### Page title <a id="stablecoin-invoicing-title"></a>
Read as `stablecoin-invoicing-title` on the stablecoin invoicing page.

**Values (default).** size 576 x 216; background transparent; text Selecta Medium 72/72 500, #ffffff `white`.

![Page title default](components/crops/stablecoin-invoicing-title-default.png)

#### Page CTA <a id="stablecoin-invoicing-cta"></a>
Read as `stablecoin-invoicing-cta` on the stablecoin invoicing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 148.56 x 40; padding 6px 14px; radius 100px; background #0d111b `cta`; shadow #242628 0px 0px 0px 1px, rgba(27, 28, 29, 0.48) 0px 1px 2px 0px; text Open Runde 16/24 500, #ffffff `white` |
| hover | background rgba(0, 0, 0, 0.88) `black-88` |
| focus-visible | outline 1px auto #005fcc `focus`, offset 1px |

![Page CTA default](components/crops/stablecoin-invoicing-cta-default.png) ![Page CTA hover](components/crops/stablecoin-invoicing-cta-hover.png) ![Page CTA focus-visible](components/crops/stablecoin-invoicing-cta-focus-visible.png) ![Page CTA pressed](components/crops/stablecoin-invoicing-cta-pressed.png)

#### Section title <a id="stablecoin-invoicing-section"></a>
Read as `stablecoin-invoicing-section` on the stablecoin invoicing page.

**Values (default).** size 297.38 x 56; background transparent; text Selecta Medium 56/56 500, rgba(0, 0, 0, 0.9) `black-90`.

![Section title default](components/crops/stablecoin-invoicing-section-default.png)

#### Page title <a id="location-title"></a>
Read as `location-title` on the US to Japan corridor page.

**Values (default).** size 695 x 128; background transparent; text Selecta Medium 64/64 500, #ffffff `white`.

![Page title default](components/crops/location-title-default.png)

#### Page CTA <a id="location-cta"></a>
Read as `location-cta` on the US to Japan corridor page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 148.56 x 40; padding 6px 14px; radius 100px; background #0d111b `cta`; shadow #242628 0px 0px 0px 1px, rgba(27, 28, 29, 0.48) 0px 1px 2px 0px; text Open Runde 16/24 500, #ffffff `white` |
| hover | background rgba(0, 0, 0, 0.88) `black-88` |
| focus-visible | outline 1px auto #005fcc `focus`, offset 1px |

![Page CTA default](components/crops/location-cta-default.png) ![Page CTA hover](components/crops/location-cta-hover.png) ![Page CTA focus-visible](components/crops/location-cta-focus-visible.png) ![Page CTA pressed](components/crops/location-cta-pressed.png)

#### Section title <a id="location-section"></a>
Read as `location-section` on the US to Japan corridor page.

**Values (default).** size 1200 x 64; background transparent; text Selecta Medium 64/64 500, #1a1a1a `ink-2`.

![Section title default](components/crops/location-section-default.png)

### Legal text

The terms and privacy pages: heading plus running legal copy in the same shell.

#### Page title <a id="terms-title"></a>
Read as `terms-title` on the terms page.

**Values (default).** size 158.05 x 64; background transparent; text Open Runde 64/64 600, #000000 `cta-edge`.

![Page title default](components/crops/terms-title-default.png)

#### Body text <a id="terms-body"></a>
Read as `terms-body` on the terms page.

**Values (default).** size 704 x 196; background transparent; text Selecta Regular 18/28 400, #666666 `grey`.

![Body text default](components/crops/terms-body-default.png)

#### Page title <a id="privacy-title"></a>
Read as `privacy-title` on the privacy page.

**Values (default).** size 158.05 x 64; background transparent; text Open Runde 64/64 600, #000000 `cta-edge`.

![Page title default](components/crops/privacy-title-default.png)

#### Body text <a id="privacy-body"></a>
Read as `privacy-body` on the privacy page.

**Values (default).** size 704 x 308; background transparent; text Selecta Regular 18/28 400, #666666 `grey`.

![Body text default](components/crops/privacy-body-default.png)

### Mobile (390 wide)

A few components as a phone draws them, at 390 x 844: the collapsed header with its menu trigger, the opened nav panel and the hero title.

#### Mobile top bar <a id="m-nav-bar"></a>
The mobile header: logo left, menu trigger right. Read as `m-nav-bar` on the home page at 390 wide.

**Values (default).** size 358 x 48; padding 0px 24px 8px 20px; radius 0px 0px 24px 24px; background transparent; text sans-serif 12/normal 400, #000000 `cta-edge`; icon 18 x 14, #000000 `cta-edge`.

Child layers that carry the look: div 112x16 image url(data:…)%22></path><path d=%22M 17.846 0.4 C 17.846 0.179 17.667 0 17.446 0 L 14.554 0 .

![Mobile top bar default](components/crops/m-nav-bar-default.png)

#### Mobile menu trigger <a id="m-menu-trigger"></a>
The menu button (the 24px icon box at the right of the top bar). Pressed once below to open the menu; a local disclosure. Read as `m-menu-trigger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 40; background transparent; text sans-serif 12/normal 400, #000000 `cta-edge`; icon 18 x 14, #000000 `cta-edge` |

![Mobile menu trigger default](components/crops/m-menu-trigger-default.png) ![Mobile menu trigger hover](components/crops/m-menu-trigger-hover.png) ![Mobile menu trigger pressed](components/crops/m-menu-trigger-pressed.png)

#### Mobile hero title <a id="m-hero-title"></a>
Read as `m-hero-title` on the home page at 390 wide.

**Values (default).** size 342 x 48; background transparent; text Open Runde 40/48 600, #1e1e1e `ink`.

![Mobile hero title default](components/crops/m-hero-title-default.png)

#### Mobile menu (open) <a id="m-nav-panel"></a>
The opened mobile menu panel; pressed once, nothing navigated. Read as `m-nav-panel` on the home page at 390 wide.

**Values (open).** size 390 x 844; padding 0px 16px; background #fafafa `paper`; text Selecta Medium 40/40 500, rgba(0, 0, 0, 0.9) `black-90`; icon 14 x 14, #0000ee.

![Mobile menu (open) open](components/crops/m-nav-panel-open.png)

## Icons

54 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Photography and artwork were left out; these are the interface icons (the wordmark, the menu trigger, fee and feature marks, social marks). The SVGs are Acctual's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [acctual-is-joining-altitude](icons/acctual-is-joining-altitude.svg) | 14x14 |  | fill | ; pricing; teams; about; blog; freelancer-invoicing; stablecoin-invoicing; locations/us-to-japan; terms; privacy | Acctual is joining Altitude |
| [agencies-reclaim-billable-hours-and-shift-your-team-s-focus](icons/agencies-reclaim-billable-hours-and-shift-your-team-s-focus.svg) | 22x17 |  | fill |  | Agencies  Reclaim billable hours and shift your team’s focus |
| [consultants-target-high-ticket-clients-thanks-to-improved](icons/consultants-target-high-ticket-clients-thanks-to-improved.svg) | 23x18 |  | fill |  | Consultants  Target high ticket clients thanks  to improved  |
| [contractors-get-paid-on-the-job-and-book-bigger-projects-wi](icons/contractors-get-paid-on-the-job-and-book-bigger-projects-wi.svg) | 18x20 |  | fill |  | Contractors  Get paid on the job and book bigger projects wi |
| [cross-border-reach-new-markets-and-win-global-contracts-wit](icons/cross-border-reach-new-markets-and-win-global-contracts-wit.svg) | 20x20 |  | fill |  | Cross border  Reach new markets and win global contracts wit |
| [freelancers-make-more-profit-on-every-project-and-get-paid](icons/freelancers-make-more-profit-on-every-project-and-get-paid.svg) | 22x19 |  | fill |  | Freelancers  Make more profit on every project and get paid  |
| [icon](icons/icon.svg) | 20x20 |  | fill | ; pricing; teams; about; freelancer-invoicing |  |
| [icon-10](icons/icon-10.svg) | 16x13 |  | fill |  |  |
| [icon-11](icons/icon-11.svg) | 16x16 |  | fill |  |  |
| [icon-12](icons/icon-12.svg) | 16x14 | 0 0 25 23 | fill |  |  |
| [icon-13](icons/icon-13.svg) | 18x18 |  | fill |  |  |
| [icon-14](icons/icon-14.svg) | 18x18 |  | fill |  |  |
| [icon-15](icons/icon-15.svg) | 18x14 |  | fill | ; pricing; teams; about; blog; freelancer-invoicing; stablecoin-invoicing; locations/us-to-japan; terms; privacy |  |
| [icon-16](icons/icon-16.svg) | 25x23 | -2 -2 25 23 | fill |  |  |
| [icon-17](icons/icon-17.svg) | 15x15 |  | fill | pricing |  |
| [icon-18](icons/icon-18.svg) | 20x20 | 0 0 20 20 | fill | stablecoin-invoicing |  |
| [icon-19](icons/icon-19.svg) | 21x21 | 0 0 21 21 | fill | stablecoin-invoicing |  |
| [icon-2](icons/icon-2.svg) | 30x30 |  | fill | ; teams; freelancer-invoicing |  |
| [icon-20](icons/icon-20.svg) | 42x28 | 0 0 42 28 | fill | stablecoin-invoicing |  |
| [icon-21](icons/icon-21.svg) | 21x21 | 0 0 20 20 | fill | stablecoin-invoicing |  |
| [icon-22](icons/icon-22.svg) | 11x10 | 0 0 11 10 | fill | stablecoin-invoicing |  |
| [icon-23](icons/icon-23.svg) | 40x30 | 0 0 40 30 | fill | stablecoin-invoicing |  |
| [icon-24](icons/icon-24.svg) | 21x21 |  | fill | stablecoin-invoicing; locations/us-to-japan |  |
| [icon-25](icons/icon-25.svg) | 22x20 |  | fill | stablecoin-invoicing |  |
| [icon-26](icons/icon-26.svg) | 20x20 | 0 0 20 20 | stroke | stablecoin-invoicing |  |
| [icon-27](icons/icon-27.svg) | 28x28 | 0 0 20 20 | stroke | stablecoin-invoicing |  |
| [icon-28](icons/icon-28.svg) | 22x29 | 0 0 20 27 | fill | stablecoin-invoicing |  |
| [icon-29](icons/icon-29.svg) | 21x21 | 0 0 19 19 | fill | stablecoin-invoicing |  |
| [icon-3](icons/icon-3.svg) | 30x30 |  | fill | ; teams; freelancer-invoicing |  |
| [icon-30](icons/icon-30.svg) | 38x38 | 0 0 35 35 | fill | stablecoin-invoicing |  |
| [icon-31](icons/icon-31.svg) | 38x38 | 0 0 35 35 | fill | stablecoin-invoicing |  |
| [icon-32](icons/icon-32.svg) | 20x20 | 0 0 20 20 | fill | stablecoin-invoicing |  |
| [icon-33](icons/icon-33.svg) | 21x21 | -1 -1 21 21 | fill | stablecoin-invoicing |  |
| [icon-34](icons/icon-34.svg) | 42x28 | -7 -7 42 28 | fill | stablecoin-invoicing |  |
| [icon-35](icons/icon-35.svg) | 25x25 | 0 0 25 25 | fill | stablecoin-invoicing |  |
| [icon-36](icons/icon-36.svg) | 20x20 | -1 -1 20 20 | fill | stablecoin-invoicing |  |
| [icon-37](icons/icon-37.svg) | 11x10 | -2 -2 11 10 | stroke | stablecoin-invoicing |  |
| [icon-38](icons/icon-38.svg) | 40x30 | -1 -1 40 30 | fill | stablecoin-invoicing |  |
| [icon-39](icons/icon-39.svg) | 20x27 | 0 0 20 27 | stroke | stablecoin-invoicing |  |
| [icon-4](icons/icon-4.svg) | 30x30 |  | fill | ; teams; freelancer-invoicing |  |
| [icon-40](icons/icon-40.svg) | 19x19 | 0 0 19 19 | fill | stablecoin-invoicing |  |
| [icon-41](icons/icon-41.svg) | 35x35 | 0 0 35 35 | stroke | stablecoin-invoicing |  |
| [icon-42](icons/icon-42.svg) | 35x35 | 0 0 35 35 | stroke | stablecoin-invoicing |  |
| [icon-43](icons/icon-43.svg) | 38x24 | 0 0 38 26 | fill | locations/us-to-japan |  |
| [icon-44](icons/icon-44.svg) | 20x19 | 0 0 20 20 | fill | locations/us-to-japan |  |
| [icon-45](icons/icon-45.svg) | 18x19 | 0 0 18 20 | fill | locations/us-to-japan |  |
| [icon-46](icons/icon-46.svg) | 38x26 | -1 -1 38 26 | fill | locations/us-to-japan |  |
| [icon-47](icons/icon-47.svg) | 20x20 | 0 0 20 20 | fill | locations/us-to-japan |  |
| [icon-48](icons/icon-48.svg) | 18x20 | 0 0 18 20 | fill | locations/us-to-japan |  |
| [icon-5](icons/icon-5.svg) | 16x16 |  | fill |  |  |
| [icon-6](icons/icon-6.svg) | 15x13 |  | fill |  |  |
| [icon-7](icons/icon-7.svg) | 15x15 |  | fill |  |  |
| [icon-8](icons/icon-8.svg) | 15x15 |  | fill |  |  |
| [icon-9](icons/icon-9.svg) | 15x15 |  | fill |  |  |

## Gaps

### Pages

- **The product app stays out.** app.acctual.com (the invoicing product itself) sits behind a sign-in that was never opened; this package covers the public marketing site only. The invoice mock on the home page is an interactive demo, not the app.
- **Programmatic pages are sampled, not exhaustive.** ~30 /locations/* corridors and the persona/product landing pages share templates; one of each was captured (US to Japan, freelancer-invoicing, stablecoin-invoicing). /old-home, /blog-old and /404 were skipped by choice.
- **External destinations.** Help/docs links and social profiles outbound were not visited.

### States

- **Pressed** was forced with DevTools (`:active`), so a state a script adds on mousedown is missing if one exists. The site's stylesheet paints links `#ff0000` under `:active` where the Framer rule applies.
- **Focus rings are the browser's.** Where the site declares no `:focus-visible` style, the measured ring is headless Chromium's default, not a product choice.
- **Hover moves are JS.** Framer runs its hovers and reveals in script (spring animations), so CSS transition measurements come back 0s and hover diffs are mostly colour-only.
- **Disabled, error, loading and selected states** were not seen on any public control.

### Themes

acctual.com shows one theme: a #fafafa ground with dark text, a single #0098f2 accent and #0d111b button pills; there is no `prefers-color-scheme` variant and no theme attribute, so the token file ships a single `light` set. The site's design tokens are hashed `--token-<uuid>` custom properties resolved in [raw/css-vars.json](raw/css-vars.json); the token file names them where a leaf aliases one.

### Fonts

- Everything reads **Open Runde** except the programmatic landing pages (**Selecta Medium**), the legal body (**Selecta Regular**) and the announcement strip (**Inter**). Geist, Caveat, Fragment Mono and the SF Pro family are declared in @font-face (see [raw/css-vars.json](raw/css-vars.json)) but nothing measured uses them.

### Screenshots

- Photography, illustration and the invoice demo are Acctual's content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Blog-post and legal body copy was not transcribed; only the frames around it were measured.
- No personal data was captured: every page was read signed out and no form exists on the marketing surface to touch.
