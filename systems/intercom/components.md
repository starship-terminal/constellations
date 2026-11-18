# Intercom components

The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from www.intercom.com on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (45 components, 89 states). The page layouts are described in [raw/pages.md](raw/pages.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Saans 64/64 400, #111111`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (85 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (the site paints one theme, `body.theme-light`). Desktop shots are 1440 x 900 at 1x (the PNG matches the viewport); `-full` shots are whole pages at the same 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). A page taller than one GPU texture is stitched from `-full.partN.png` tiles into one `-full.png`. Component crops stay at 2x.

| Surface | URL | Screenshots |
|---|---|---|
| Home. The Fin 4 promo banner, shared header, hero, logo wall, feature sections and the footer; the Product mega-menu opened. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [nav-menu](screenshots/home-light-nav-menu.png) |
| Pricing. Billing toggle, savings badge, plan columns, FAQ (one item opened). | `/pricing` | [default](screenshots/pricing-light-default.png), [faq](screenshots/pricing-light-faq.png), [full](screenshots/pricing-light-full.png) |
| Helpdesk product page. | `/helpdesk` | [default](screenshots/helpdesk-light-default.png), [full](screenshots/helpdesk-light-full.png) |
| Inbox product page (a very tall page: the full shot is stitched from two parts). | `/helpdesk/inbox` | [default](screenshots/inbox-light-default.png), [full](screenshots/inbox-light-full.png) |
| Copilot product page. | `/helpdesk/copilot` | [default](screenshots/copilot-light-default.png), [full](screenshots/copilot-light-full.png) |
| Customers page. | `/customers` | [default](screenshots/customers-light-default.png), [full](screenshots/customers-light-full.png) |
| Integrations page. | `/integrations` | [default](screenshots/integrations-light-default.png), [full](screenshots/integrations-light-full.png) |
| Security page. | `/security` | [default](screenshots/security-light-default.png), [full](screenshots/security-light-full.png) |
| View demos page. | `/view-demos` | [default](screenshots/view-demos-light-default.png), [full](screenshots/view-demos-light-full.png) |
| Contact sales. The first form step and the company-size select opened. | `/contact-sales` | [default](screenshots/contact-sales-light-default.png), [full](screenshots/contact-sales-light-full.png), [select-open](screenshots/contact-sales-light-select-open.png) |
| Why choose Intercom. | `/why-choose-intercom` | [default](screenshots/why-choose-light-default.png), [full](screenshots/why-choose-light-full.png) |
| Enterprise page. | `/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| Blog index. | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Help center home. | `/help/en/` | [default](screenshots/help-light-default.png), [full](screenshots/help-light-full.png) |
| Changelog. | `/changes/en` | [default](screenshots/changes-light-default.png), [full](screenshots/changes-light-full.png) |
| Home at 390: header collapsed to wordmark plus menu button; the menu sheet opened. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing at 390. | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Helpdesk at 390. | `/helpdesk` | [default](screenshots/mobile-helpdesk-light-default.png), [full](screenshots/mobile-helpdesk-light-full.png) |
| Help center at 390. | `/help/en/` | [default](screenshots/mobile-help-light-default.png), [full](screenshots/mobile-help-light-full.png) |
| Contact sales at 390. | `/contact-sales` | [default](screenshots/mobile-contact-sales-light-default.png), [full](screenshots/mobile-contact-sales-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Nav mega-menu | home header | the Product trigger pressed (opened and left open) | [home-light-nav-menu](screenshots/home-light-nav-menu.png), [nav-menu](#nav-mega-menu) |
| FAQ accordion item | pricing | its own question row pressed | [pricing-light-faq](screenshots/pricing-light-faq.png), [faq-item](#faq-accordion-item) |
| Select listbox | contact sales | the company-size select's own button pressed; no option chosen | [contact-sales-light-select-open](screenshots/contact-sales-light-select-open.png), [select-popup](#select-popup) |
| Mobile menu sheet | home at 390 | the menu button pressed (opened, then dismissed with Escape) | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-overlay](#mobile-menu-overlay) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 13 components were given a real keyboard focus. 13 draw a ring: `nav-item` (1px auto #101010, offset 0px), `nav-link` (2px solid #101010, offset 2px), `nav-login` (1px auto #101010, offset 1px), `nav-cta` (2px solid #101010, offset 2px), `hero-cta` (2px solid #101010, offset 2px), `hero-secondary` (2px solid #101010, offset 2px), `billing-toggle` (1px auto #101010, offset 0px), `billing-toggle-off` (1px auto #101010, offset 0px), `promo-badge` (1px auto #101010, offset 0px), `next-button` (2px solid #101010, offset 2px), `m-menu-button` (1px auto #e59700, offset 0px), `footer-link` (1px auto #101010, offset 1px), `locale-select` (1px auto #101010, offset 1px). The measured rings are black (`#101010`) on the desktop controls and orange (`#e59700`) on the mobile menu button. The declared `--color-focus-outline` (`--color-blue`, #000ce1) is a stylesheet value; these controls did not paint it.

**Hover and pressed.** The primary buttons (nav CTA, hero CTA, the form's Next) repaint rather than transform: `--button-primary-hover-background` is the helpdesk blue #0007cb, the pressed state the same blue at 85%. Ghost nav items fill with `--color-chalk` on hover. Pressed was forced with DevTools, so a state a script adds on mousedown (if any) is missing.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | billing-toggle, billing-toggle-off, promo-badge |
| 0.15s | `ease` | background, background-color, border-color | help-card, help-search |
| 0.15s | `linear` | background-color, border, box-shadow, opacity, transform | changes-entry |
| 0.2s | `ease-out` | background-size | footer-link |
| 0.25s | `cubic-bezier(0.4, 0, 0.2, 1)` | top | header, m-header |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | opacity | faq-item |

**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).

| Page | 1440 | 1920 | 1024 | 390 |
|---|---|---|---|---|
| home | content x 0, 1440 wide; grid 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 gap 16px | content x 0, 1920 wide; grid 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 gap 16px | content x 0, 1024 wide; grid 68 68 68 68 68 68 68 68 68 68 68 68 gap 16px | content x 0, 390 wide; grid 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 gap 16px |
| pricing | content x 0, 1440 wide; grid 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 gap 16px | content x 0, 1920 wide; grid 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 gap 16px | content x 0, 1024 wide; grid 68 68 68 68 68 68 68 68 68 68 68 68 gap 16px | content x 0, 390 wide; grid 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 gap 16px |
| helpdesk | content x 0, 1440 wide; grid 105.3 105.3 105.3 105.3 105.3 105.3 105.3 105.3 105.3 105.3 105.3 105.3 gap 16px | content x 0, 1920 wide; grid 145.3 145.3 145.3 145.3 145.3 145.3 145.3 145.3 145.3 145.3 145.3 145.3 gap 16px | content x 0, 1024 wide; grid 70.6 70.6 70.6 70.6 70.6 70.6 70.6 70.6 70.6 70.6 70.6 70.6 gap 16px | content x 0, 390 wide; grid 17.8 17.8 17.8 17.8 17.8 17.8 17.8 17.8 17.8 17.8 17.8 17.8 gap 16px |
| help | content x 324, 830 wide; grid 260 830 222 gap 48px | content x 555, 830 wide; grid 260 1292 240 gap 48px | content x 97, 830 wide; grid 260.6 260.6 260.6 gap 24px | content x 16, 358 wide; grid 326 20 gap 12px |
| contact-sales | content x 0, 1440 wide; grid 120 120 120 120 120 120 120 120 120 120 120 120 gap normal | content x 0, 1920 wide; grid 160 160 160 160 160 160 160 160 160 160 160 160 gap normal | content x 0, 1024 wide; grid 85.3 85.3 85.3 85.3 85.3 85.3 85.3 85.3 85.3 85.3 85.3 85.3 gap normal | content x 0, 390 wide; grid 32.5 32.5 32.5 32.5 32.5 32.5 32.5 32.5 32.5 32.5 32.5 32.5 gap normal |
| blog | content x 0, 1440 wide; grid 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 102.6 gap 16px | content x 0, 1920 wide; grid 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 142.6 gap 16px | content x 0, 1024 wide; grid 68 68 68 68 68 68 68 68 68 68 68 68 gap 16px | content x 0, 390 wide; grid 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 15.1 gap 16px |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Feature card](#feature-card) | 728 x 686 | 1px solid rgba(0, 0, 0, 0.06) | 14px | transparent | none | 0 |
| [Plan card](#plan-card) | 286 x 607.56 | - | - | transparent | none | 24px |
| [Promo badge button](#promo-badge-button) | 157 x 20.8 | - | 2px | rgba(0, 7, 203, 0.15) | none | 2px 8px |
| [FAQ accordion item](#faq-accordion-item) | 696.02 x 64 | - | - | transparent | none | 20px 0px |
| [Text field](#text-field) | 448 x 40 | 1px solid rgba(17, 17, 17, 0.2) | 2px | #faf9f6 `neutral.offWhite` | none | 0px 12px |
| [Select (combobox)](#select-combobox) | 448 x 40 | 1px solid rgba(17, 17, 17, 0.2) | 2px | #faf9f6 `neutral.offWhite` | none | 0px 12px |
| [Help article card](#help-article-card) | 260.66 x 252 | 1px solid rgba(26, 26, 26, 0.15) | 8px | #ffffff `neutral.white` | none | 0 |
| [Blog article card](#blog-article-card) | 696.5 x 274 | T: 1px solid rgba(0, 0, 0, 0.1) `nav.hover` `nav.hover` 1px solid rgba(0, 0, 0, 0.1) `nav.hover` `nav.hover` | - | transparent | none | 32px 32px 32px 0px |
| [Changelog entry](#changelog-entry) | 900 x 967.39 | - | 4px | #ffffff `neutral.white` | rgba(0, 0, 0, 0.03) 0px 3px 8px 0px | 0 |

## Components

### Shell and navigation

The chrome every marketing page shares: the "Introducing Fin 4" promo banner, the shared header (`header.shared-header`) with the wordmark, Product/Customers/Resources mega-menu triggers, Pricing, Log in, Contact sales, View demo and the black "Start free trial" CTA. Everything is ghost-on-white until hover, when the chalk fill (`--color-nav-background-highlight`) shows.

#### Promo banner
The announcement row at the very top of the shared header ("Introducing Fin 4 … Learn more"): real chrome, kept. Read as `promo-banner` on the Home page.

**Values (default).** size 1440 x 34; background #e1e2e5; text Saans 14/18.00 400, #111111 `neutral.offBlack`; icon 16 x 16, #111111 `neutral.offBlack`.

![Promo banner default](components/crops/promo-banner-default.png)

#### Nav bar
The shared site header (header.shared-header): Intercom logo, Product/Customers/Resources menu triggers, Pricing link, Log in, Contact sales, View demo and the black "Start free trial" button. Read as `header` on the Home page.

**Values (default).** size 1440 x 108; background #ffffff `neutral.white`; text Saans 14/18.00 400, #111111 `neutral.offBlack`; transition top 0.25s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #111111 `neutral.offBlack`.

![Nav bar default](components/crops/header-default.png)

#### Logo
The Intercom wordmark home anchor in the nav. Read as `logo` on the Home page.

**Values (default).** size 129.56 x 40; background transparent; text Saans 16/24 400, #111111 `neutral.offBlack`.

![Logo default](components/crops/logo-default.png)

#### Nav menu trigger
A mega-menu trigger in the nav ("Product"): 40px, radius 6, opens the nav panel. Read as `nav-item` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85 x 40; padding 0px 4px 0px 12px; radius 6px; background transparent; text Saans 14/15.4 400, #111111 `neutral.offBlack`; icon 18 x 18, #111111 `neutral.offBlack` |
| hover | background #f1eee9 `neutral.chalk` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background #f1eee9 `neutral.chalk` |

![Nav menu trigger default](components/crops/nav-item-default.png) ![Nav menu trigger hover](components/crops/nav-item-hover.png) ![Nav menu trigger focus-visible](components/crops/nav-item-focus-visible.png) ![Nav menu trigger pressed](components/crops/nav-item-pressed.png)

#### Nav link
A plain nav link ("Pricing"): 40px ghost row, radius 6. Read as `nav-link` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 68 x 40; padding 0px 12px; radius 6px; background transparent; text Saans 14/15.4 400, #111111 `neutral.offBlack` |
| hover | background #f1eee9 `neutral.chalk` |
| focus-visible | outline 2px solid #101010, offset 2px |
| pressed | background #f1eee9 `neutral.chalk` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Nav log in
The "Log in" link to app.intercom.com; measured, never followed. Read as `nav-login` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 61 x 40; padding 0px 12px; radius 6px; background transparent; text Saans 14/15.4 400, #111111 `neutral.offBlack` |
| hover | background #f1eee9 `neutral.chalk` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #f1eee9 `neutral.chalk` |

![Nav log in default](components/crops/nav-login-default.png) ![Nav log in hover](components/crops/nav-login-hover.png) ![Nav log in focus-visible](components/crops/nav-login-focus-visible.png) ![Nav log in pressed](components/crops/nav-login-pressed.png)

#### Nav CTA
The black "Start free trial" button in the nav (--button-primary-* tokens, --button-radius 4px, height --button-height 40px); links to /signup, never followed. Read as `nav-cta` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 109 x 40; padding 0px 12px; radius 4px; background #111111 `neutral.offBlack`; text Saans 14/15.4 400, #ffffff `neutral.white` |
| hover | background #0007cb `blue.helpdesk` |
| focus-visible | outline 2px solid #101010, offset 2px |
| pressed | background rgba(0, 7, 203, 0.85) |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Nav mega-menu
The panel the Product/Customers/Resources triggers open (shared-header-switch-card): a white card with the nav-panel border and a drop shadow. Read as `nav-menu` on the Home page.

The saved reading is a hidden switch-card (opacity 0), not the open Product panel. No correct overlay reading is in the raw file, so this entry is a gap until a recapture.

### Home

The intercom.com home page: a cream ground (`--body-bg` = `--color-cream`) under a Saans hero, eyebrow labels in SaansMono, and cards bordered at black 6%.

#### Hero title
The home hero headline ("A complete system for AI and human customer service", text-heading-2: Saans, tight tracking). Read as `hero-title` on the Home page.

**Values (default).** size 585.63 x 192; background transparent; text Saans 64/64 400, rgba(17, 17, 17, 0.4).

![Hero title default](components/crops/hero-title-default.png)

#### Eyebrow label
A small label over a section (text-label-lg: SaansMono-family uppercase micro type). Read as `eyebrow` on the Home page.

**Values (default).** size 1170.67 x 12; background transparent; text SaansMono 12/12 400, #111111 `neutral.offBlack`.

![Eyebrow label default](components/crops/eyebrow-default.png)

#### Hero CTA
The black "Start free trial" button under the hero copy (--button-primary-*, --button-radius); links to /signup, never followed. Read as `hero-cta` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 123 x 40; padding 4px 14px; radius 4px; background #111111 `neutral.offBlack`; text Saans 16/24 400, #ffffff `neutral.white` |
| hover | background #0007cb `blue.helpdesk` |
| focus-visible | outline 2px solid #101010, offset 2px |
| pressed | background rgba(0, 7, 203, 0.85) |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero secondary link
The secondary action beside the hero CTA ("View demo" style link button). Read as `hero-secondary` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 110 x 40; padding 4px 14px; border 1px solid #111111 `neutral.offBlack`; radius 4px; background transparent; text Saans 16/24 400, #111111 `neutral.offBlack` |
| hover | border 1px solid rgba(17, 17, 17, 0.75); text Saans 16/24 400, rgba(17, 17, 17, 0.75) |
| focus-visible | outline 2px solid #101010, offset 2px |
| pressed | border 1px solid rgba(17, 17, 17, 0.75); background rgba(17, 17, 17, 0.02); text Saans 16/24 400, #000000 `neutral.black` |

![Hero secondary link default](components/crops/hero-secondary-default.png) ![Hero secondary link hover](components/crops/hero-secondary-hover.png) ![Hero secondary link focus-visible](components/crops/hero-secondary-focus-visible.png) ![Hero secondary link pressed](components/crops/hero-secondary-pressed.png)

#### Section title
A display section heading in page flow (text-heading-3: Saans). Read as `section-title` on the Home page.

**Values (default).** size 1164 x 24; background transparent; text Saans 24/24 400, rgba(17, 17, 17, 0.4).

![Section title default](components/crops/section-title-default.png)

#### Feature card
A painted card on the home page (the first bordered/filled rounded container in main). Read as `feature-card` on the Home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 728 x 686; border 1px solid rgba(0, 0, 0, 0.06); radius 14px; background transparent; text system-ui 14/21 600, #111111 `neutral.offBlack`; icon 16 x 16, #111111 `neutral.offBlack` |

![Feature card default](components/crops/feature-card-default.png) ![Feature card hover](components/crops/feature-card-hover.png)

#### Page ground
The body element: --body-bg = --color-cream under the current brand scope. Read as `page-ground` on the Home page.

**Values (default).** size 1440 x 9579.03; background transparent; text Saans 14/18.00 400, #111111 `neutral.offBlack`; icon 16 x 16, #111111 `neutral.offBlack`.

Child layers that carry the look: header 1440x108 background #ffffff `neutral.white`; div 1440x34 background #e1e2e5; div 0x0 background #d9d9d9.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Pricing

The pricing page: the billed-annually/monthly segmented control, the helpdesk-blue savings badge, the plan columns and the FAQ accordion.

#### Pricing title
"Get Fin and Intercom for a single, fully integrated customer service stack" (text-heading-3). Read as `pricing-title` on the Pricing page.

**Values (default).** size 896 x 96; background transparent; text Saans 48/48 400, #111111 `neutral.offBlack`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Billing toggle (selected)
The selected half of the annual/monthly billing segmented control ("Billed annually": canvas fill, radius none). Local UI state, switched and switched back. Read as `billing-toggle` on the Pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 104 x 27.59; padding 4px 8px; background #e7e3db `neutral.canvas`; text Saans 14/19.6 400, #111111 `neutral.offBlack`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto #101010, offset 0px |

![Billing toggle (selected) default](components/crops/billing-toggle-default.png) ![Billing toggle (selected) hover](components/crops/billing-toggle-hover.png) ![Billing toggle (selected) focus-visible](components/crops/billing-toggle-focus-visible.png) ![Billing toggle (selected) pressed](components/crops/billing-toggle-pressed.png)

#### Billing toggle (unselected)
The unselected half ("Billed monthly": transparent). Read as `billing-toggle-off` on the Pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 104 x 27.59; padding 4px 8px; background transparent; text Saans 14/19.6 400, #111111 `neutral.offBlack`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #111111 `neutral.offBlack`; text Saans 14/19.6 400, #ffffff `neutral.white` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background #111111 `neutral.offBlack`; text Saans 14/19.6 400, #ffffff `neutral.white` |

![Billing toggle (unselected) default](components/crops/billing-toggle-off-default.png) ![Billing toggle (unselected) hover](components/crops/billing-toggle-off-hover.png) ![Billing toggle (unselected) focus-visible](components/crops/billing-toggle-off-focus-visible.png) ![Billing toggle (unselected) pressed](components/crops/billing-toggle-off-pressed.png)

#### Promo badge button
The helpdesk-blue tinted badge button on pricing ("New customers save 35%", bg-helpdesk/15, 2px radius). Read as `promo-badge` on the Pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 157 x 20.8; padding 2px 8px; radius 2px; background rgba(0, 7, 203, 0.15); text Saans 12/16.8 400, #0007cb `blue.helpdesk`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(0, 7, 203, 0.25) |
| focus-visible | background rgba(0, 7, 203, 0.25); outline 1px auto #101010, offset 0px |
| pressed | background rgba(0, 7, 203, 0.25) |

![Promo badge button default](components/crops/promo-badge-default.png) ![Promo badge button hover](components/crops/promo-badge-hover.png) ![Promo badge button focus-visible](components/crops/promo-badge-focus-visible.png) ![Promo badge button pressed](components/crops/promo-badge-pressed.png)

#### Plan card
A pricing plan column (the Essential cell of the @container plan grid: unpainted itself, its plan name, "Includes Fin AI Agent" list and CTA inside). Read as `plan-card` on the Pricing page.

**Values (default).** size 286 x 607.56; padding 24px; background transparent; text Saans 24/24 400, #111111 `neutral.offBlack`; icon 12 x 12, rgba(17, 17, 17, 0.8).

Child layers that carry the look: del::after 37.4375pxx1.1875px background rgba(17, 17, 17, 0.5); button 157x20.8 background rgba(0, 7, 203, 0.15) radius 2px; a 113x40 background #111111 `neutral.offBlack` radius 4px.

![Plan card default](components/crops/plan-card-default.png)

#### FAQ accordion item
A question row in the pricing FAQ accordion; opened by its own press. Read as `faq-item` on the Pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 696.02 x 64; padding 20px 0px; background transparent; text Saans 20/24 400, #111111 `neutral.offBlack`; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #111111 `neutral.offBlack` |

![FAQ accordion item default](components/crops/faq-item-default.png) ![FAQ accordion item opened](components/crops/faq-item-opened.png)

### Contact sales form

The first step of the contact-sales form: labels, a text field, the company-size select and its listbox, the opt-in checkbox and the Next button. Nothing was typed past the throwaway filled-state reading (sample text typed and immediately deleted), nothing advanced, nothing sent.

#### Contact sales form
The first step of the contact-sales form (Business Email, company size select, opt-in checkbox, Next): measured at rest, never advanced or sent. Read as `form` on the Contact sales page.

**Values (default).** size 448 x 372.19; background transparent; text Saans 14/19.6 400, #111111 `neutral.offBlack`; icon 8 x 5, rgba(17, 17, 17, 0.6).

Child layers that carry the look: input 448x40 background #faf9f6 `neutral.offWhite` border 1px solid rgba(17, 17, 17, 0.2) radius 2px; button 448x40 background #faf9f6 `neutral.offWhite` border 1px solid rgba(17, 17, 17, 0.2) radius 2px; div 0x0 background #faf9f6 `neutral.offWhite` border 1px solid #111111 `neutral.offBlack` shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px.

![Contact sales form default](components/crops/form-default.png)

#### Form page title
"Discover the perfect fit with Intercom". Read as `form-title` on the Contact sales page.

**Values (default).** size 512 x 80; background transparent; text Saans 40/40 400, #111111 `neutral.offBlack`.

![Form page title default](components/crops/form-title-default.png)

#### Field label
A field label (.label: "Business Email *"). Read as `input-label` on the Contact sales page.

**Values (default).** size 448 x 25.59; padding 0px 0px 6px 0px; background transparent; text Saans 14/19.6 400, #111111 `neutral.offBlack`.

![Field label default](components/crops/input-label-default.png)

#### Text field
The "Business email address" text input (.input: off-white fill, 2px radius, 40px). Sample text typed and deleted; nothing sent. Read as `input` on the Contact sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 448 x 40; padding 0px 12px; border 1px solid rgba(17, 17, 17, 0.2); radius 2px; background #faf9f6 `neutral.offWhite`; text Saans 16/24 400, #111111 `neutral.offBlack`; placeholder rgba(17, 17, 17, 0.6) |
| focused, filled | border 1px solid #111111 `neutral.offBlack`; background #f1eee9 `neutral.chalk` |

![Text field default](components/crops/input-default.png) ![Text field focused](components/crops/input-focused.png) ![Text field filled](components/crops/input-filled.png)

#### Select (combobox)
The "Your company size" select (button.select, same field styling as .input): its own listbox opened, nothing chosen. Read as `select` on the Contact sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 448 x 40; padding 0px 12px; border 1px solid rgba(17, 17, 17, 0.2); radius 2px; background #faf9f6 `neutral.offWhite`; text Saans 16/24 400, rgba(17, 17, 17, 0.6); icon 8 x 5, rgba(17, 17, 17, 0.6) |
| opened | border 1px solid #111111 `neutral.offBlack`; background #f1eee9 `neutral.chalk` |

![Select (combobox) default](components/crops/select-default.png) ![Select (combobox) opened](components/crops/select-opened.png)

#### Select popup
The open listbox of the select (div.select-popup): options list, held open by the select entry. Read as `select-popup` on the Contact sales page.

The saved reading is a 0x0 listbox, not the open select popup. No correct overlay reading is in the raw file, so this entry is a gap until a recapture.

#### Checkbox row
The opt-in checkbox row (label.checkbox-label: "Get updates about upcoming events…"). Never ticked. Read as `checkbox` on the Contact sales page.

**Values (default).** size 420 x 40; background transparent; text Saans 14/20 400, #000000 `neutral.black`.

![Checkbox row default](components/crops/checkbox-default.png)

#### Next button
The form's black "Next" submit control (--button-primary-*, --button-radius, --button-height): measured with CDP-forced pseudo states only — never pressed, so the form was never advanced. Read as `next-button` on the Contact sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 448 x 40; padding 0px 14px; radius 4px; background #111111 `neutral.offBlack`; text Saans 16/24 400, #ffffff `neutral.white` |
| hover | background #0007cb `blue.helpdesk` |
| focus-visible | outline 2px solid #101010, offset 2px |
| pressed | background rgba(0, 7, 203, 0.85) |

![Next button default](components/crops/next-button-default.png) ![Next button hover](components/crops/next-button-hover.png) ![Next button focus-visible](components/crops/next-button-focus-visible.png) ![Next button pressed](components/crops/next-button-pressed.png)

### Help center

intercom.com/help/en/, the Intercom help center: its own header and search, article cards and the docs navigation. A separate surface from the marketing shell.

#### Help center header
The help center's own header bar (a different surface from the marketing shell: white, no theme-light class). Read as `help-header` on the Help center page.

**Values (default).** size 1440 x 60; border B: 1px solid rgba(17, 17, 17, 0.12) 1px solid rgba(17, 17, 17, 0.12); background #ffffff `neutral.white`; text MediumLLWeb-Regular 14/14 400, rgba(17, 17, 17, 0.78); icon 14 x 14, rgba(17, 17, 17, 0.78).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Help search field
The help center search ("Search for articles… ⌘K"): focused once, nothing typed. Read as `help-search` on the Help center page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 140 x 30; padding 0px 16px; border 1px solid rgba(17, 17, 17, 0.5); radius 8px; background rgba(17, 17, 17, 0.05); text MediumLLWeb-Regular 14/21.7 400, rgba(17, 17, 17, 0.78); transition background 0.15s ease, border-color 0.15s ease |

![Help search field default](components/crops/help-search-default.png) ![Help search field focused](components/crops/help-search-focused.png)

#### Help center title
"Great service changes everything." Read as `help-hero` on the Help center page.

**Values (default).** size 700 x 134.38; background transparent; text IvoryLLSub-Light 60/67.2 500, #ffffff `neutral.white`.

![Help center title default](components/crops/help-hero-default.png)

#### Help article card
A category/article card on the help center home (first painted rounded container in main). Read as `help-card` on the Help center page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 260.66 x 252; border 1px solid rgba(26, 26, 26, 0.15); radius 8px; background #ffffff `neutral.white`; text IvoryLLSub-Light 15/19.5 600, #1a1a1a; transition background-color 0.15s ease |

![Help article card default](components/crops/help-card-default.png) ![Help article card hover](components/crops/help-card-hover.png)

#### Docs nav
The help center's expandable docs navigation tree (Overview, Getting Started, Operator, Fin AI Agent …). Read as `help-nav` on the Help center page.

**Values (default).** size 287 x 14; background transparent; text MediumLLWeb-Regular 14/14 400, rgba(17, 17, 17, 0.78).

![Docs nav default](components/crops/help-nav-default.png)

### Changelog

intercom.com/changes/en, the release-notes feed: the older `header__lite` surface (#f3f5f7 ground, `div.paper.newsfeed__newsitem` cards) running the MediumLL-era styles under `.intercom-legacy`.

#### Changelog title
The changelog header (the older "header__lite" surface: #f3f5f7 ground, MediumLL-era type). Read as `changes-title` on the Changelog page.

**Values (default).** size 900 x 40.91; background transparent; text system-ui 33/40.92 400, #3a3c4c.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Changelog entry
A release-note entry on /changes/en (div.paper.newsfeed__newsitem: white card, 4px radius on the #f3f5f7 header__lite ground). Read as `changes-entry` on the Changelog page.

**Values (default).** size 900 x 967.39; radius 4px; background #ffffff `neutral.white`; shadow rgba(0, 0, 0, 0.03) 0px 3px 8px 0px; text system-ui 14/22 600, #ffffff `neutral.white`; transition border 0.15s linear, transform 0.15s linear, background-color 0.15s linear, box-shadow 0.15s linear, opacity 0.15s linear.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Blog

intercom.com/blog: the article index list over a white band.

#### Blog title
"Blog" (text-heading-*: Saans). Read as `blog-title` on the Blog page.

**Values (default).** size 814.66 x 48; background transparent; text Saans 48/48 400, #000000 `neutral.black`.

![Blog title default](components/crops/blog-title-default.png)

#### Blog article card
An article row in the /blog index list (li.border-t over the white section). Read as `blog-card` on the Blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 696.5 x 274; padding 32px 32px 32px 0px; border T: 1px solid rgba(0, 0, 0, 0.1) `nav.hover` `nav.hover` 1px solid rgba(0, 0, 0, 0.1) `nav.hover` `nav.hover`; background transparent; text Saans 14/14 400, #000000 `neutral.black` |

![Blog article card default](components/crops/blog-card-default.png) ![Blog article card hover](components/crops/blog-card-hover.png)

### Footer

The site footer shared by every page: link columns, social icons, the locale selector and the legal row on the cream ground.

#### Footer
The site footer: link columns, social icons, the locale selector and legal row on the page ground. Read as `footer` on the Blog page.

**Values (default).** size 1440 x 577.69; background transparent; text SaansMono 12/15.6 500, rgba(0, 0, 0, 0.6) `nav.content-tertiary` `nav.content-tertiary`; icon 26 x 12, #000000 `neutral.black`.

Child layers that carry the look: a 33x17 image linear-gradient(to right in oklab, #000000 `neutral.black` 0%, #000000 `neutral.black` 100; a 58x17 image linear-gradient(to right in oklab, #000000 `neutral.black` 0%, #000000 `neutral.black` 100; a 45x17 image linear-gradient(to right in oklab, #000000 `neutral.black` 0%, #000000 `neutral.black` 100.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer link (Saans, muted); focus-visible carries the site outline. Read as `footer-link` on the Blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 33 x 17; background transparent; image linear-gradient(to right in oklab, #000000 `neutral.black` 0%, #000000 `neutral.black` 100%); text Saans 14/17.5 400, #000000 `neutral.black`; transition background-size 0.2s ease-out; opacity 0.9 |
| hover | opacity 1 |
| focus-visible | outline 1px auto #101010, offset 1px; opacity 1 |
| pressed | opacity 1 |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Locale selector
The footer language selector ("English"). Read as `locale-select` on the Blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 17; background transparent; text Saans 14/17.5 400, #000000 `neutral.black`; opacity 0.9 |
| hover | opacity 1 |
| focus-visible | outline 1px auto #101010, offset 1px; opacity 1 |
| pressed | opacity 1 |

![Locale selector default](components/crops/locale-select-default.png) ![Locale selector hover](components/crops/locale-select-hover.png) ![Locale selector focus-visible](components/crops/locale-select-focus-visible.png) ![Locale selector pressed](components/crops/locale-select-pressed.png)

### Mobile (390 wide)

A few components as a phone draws them, at 390 x 844 with a mobile user agent: the header collapses to the wordmark plus the menu button, which opens a full-height navigation sheet.

#### Mobile header
The header at 390: logo + the menu button (the desktop nav unmounts). Read as `m-header` on the Home page at 390 wide.

**Values (default).** size 390 x 108; background #ffffff `neutral.white`; text Saans 14/18.00 400, #111111 `neutral.offBlack`; transition top 0.25s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #111111 `neutral.offBlack`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
The hamburger toggle in the mobile header (aria-label "Open navigation menu"); opens the menu overlay. Read as `m-menu-button` on the Home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40 x 40; padding 8px; radius 6px; background transparent; text Saans 16/24 400, #111111 `neutral.offBlack`; icon 24 x 24, #111111 `neutral.offBlack` |
| focus-visible | outline 1px auto #e59700, offset 0px |

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button hover](components/crops/m-menu-button-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile hero
The hero title at 390 (the responsive text-heading-*-mobile size). Read as `m-hero` on the Home page at 390 wide.

**Values (default).** size 358 x 152; background transparent; text Saans 40/38 400, rgba(17, 17, 17, 0.4).

![Mobile hero default](components/crops/m-hero-default.png)

#### Mobile menu overlay
The full-height navigation sheet the mobile menu button opens (div[role=dialog].shared-header-portal, off-white ground). Read as `m-menu-overlay` on the Home page at 390 wide.

The saved reading is a demo form, not the navigation sheet. No correct overlay reading is in the raw file, so this entry is a gap until a recapture.

## Icons

55 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Marketing illustrations and product imagery were left out; these are the interface icons. The SVGs are Intercom's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [product](icons/product.svg) | 18x18 | 0 0 18 18 | stroke | home; pricing; helpdesk; inbox; copilot; customers; integrations; security; contact-sales; why-choose; enterprise; blog | Product / Customers / Resources |
| [your-privacy-choices](icons/your-privacy-choices-344719a1.svg) | 26x12 | 0 0 30 14 | fill | home; pricing; helpdesk; inbox; copilot; customers; integrations; security; why-choose; enterprise; blog | Your Privacy Choices |
| [icon-1885c355](icons/icon-1885c355.svg) | 20x20 | 0 0 24 24 | fill | pricing; inbox; integrations; security; why-choose; enterprise | How does Intercom pricing work? / How is Fin AI Agent priced |
| [per-outcome](icons/per-outcome-3237a902.svg) | 12x12 16x16 | 0 0 12 12 | fill | home; pricing; integrations | PER OUTCOME / More information / $0.99 per outcome |
| [g2](icons/g2.svg) | 12x13 15x16 24x25 | 0 0 24 25 | fill | home; pricing; customers | G2 |
| [a24-meet-our-customers](icons/a24-meet-our-customers.svg) | 55x32 | 0 0 41 24 | fill | home; inbox; enterprise | A24 — Meet our customers |
| [icon-59612db1](icons/icon-59612db1.svg) | 16x16 | 0 0 16 16 | fill | home; pricing | 14 day free trial. No credit card requir / 14-day cardless f |
| [9-841px-82-665px-0-rgba-0-0-0-0-](icons/9-841px-82-665px-0-rgba-0-0-0-0-.svg) | 12x12 16x16 | 0 0 25 25 | fill | home; copilot | Play the Introducing Fin 4 video / See Copilot in action |
| [close-banner](icons/close-banner.svg) | 16x16 | 0 0 24 24 | stroke | home | Close banner |
| [icon-003c494c](icons/icon-003c494c.svg) | 16x16 | 0 0 32 32 | fill | changes |  |
| [svg-h-auto](icons/svg-h-auto.svg) | 49x20 | 0 0 60 25 | fill | customers |  |
| [expand-overview](icons/expand-overview.svg) | 16x16 | 0 0 15 15 | fill | help | Expand Overview / Expand Getting Started / Expand Operator |
| [salesforce](icons/salesforce.svg) | 18x18 | 0 0 17.92 17.92 | fill | pricing | Salesforce |
| [per-outcome](icons/per-outcome-14ad7c08.svg) | 12x12 | 0 0 12 12 | fill | why-choose | PER OUTCOME |
| [freshdesk](icons/freshdesk.svg) | 18x18 | 0 0 17.92 17.92 | fill | pricing | Freshdesk |
| [english](icons/english-245ef7cf.svg) | 14x14 | 0 0 16 16 | stroke | help | English |
| [icon-25315474](icons/icon-25315474.svg) | 16x16 | 0 0 32 32 | fill | changes |  |
| [icon-3078bb0b](icons/icon-3078bb0b.svg) | 26x26 | 0 0 24 24 | fill | integrations | Intercom Helpdesk Fin is natively integr / Intercom MCP Serv |
| [icon-37e89370](icons/icon-37e89370.svg) | 16x16 | 0 0 16 16 | fill | view-demos |  |
| [hubspot](icons/hubspot.svg) | 18x18 | 0 0 17.92 17.92 | fill | pricing | HubSpot |
| [icon-4f50e4fb](icons/icon-4f50e4fb.svg) | 16x16 | 0 0 16.036 16 | fill | view-demos |  |
| [chat](icons/chat.svg) | 12x12 | 0 0 12 12.0064 | fill | view-demos | Chat |
| [icon-54fec6d1](icons/icon-54fec6d1.svg) | 26x26 | -0.5 0 20 23 | fill | integrations | Shopify Fin uses your Shopify store data |
| [icon-55b3c288](icons/icon-55b3c288.svg) | 16x16 | 0 0 16 16 | fill | view-demos |  |
| [intercom-helpdesk](icons/intercom-helpdesk.svg) | 20x20 | 0 0 20 20 | fill | pricing | Intercom helpdesk |
| [whatsapp](icons/whatsapp.svg) | 12x12 | 0 0 12 12 | fill | view-demos | WhatsApp |
| [icon-57902c12](icons/icon-57902c12.svg) | 16x16 | 0 0 16 16 | fill | view-demos |  |
| [linkedin](icons/linkedin.svg) | 24x24 |  | fill | customers | LinkedIn |
| [search-docs-k](icons/search-docs-k.svg) | 18x18 | 0 0 15 15 | fill | help | Search docs (⌘K) |
| [icon-5bd7ac47](icons/icon-5bd7ac47.svg) | 26x26 | 0 0 256 256 | fill | integrations | Zapier Connect Fin to the apps you alrea |
| [financial-services](icons/financial-services.svg) | 12x12 | 0 0 16 16 | fill | view-demos | Financial Services |
| [icon-5f667125](icons/icon-5f667125.svg) | 40x40 | 0 0 32 32 | fill | pricing | Fin AI Agent on all plans for $0.99 per  |
| [icon-6dfee70f](icons/icon-6dfee70f.svg) | 26x26 | 0 3 32 32 | fill | integrations | Freshdesk Fin resolves Freshdesk tickets |
| [icon-6ea40fb8](icons/icon-6ea40fb8.svg) | 20x20 | 0 0 25 25 | fill | view-demos | Play the Intercom, the helpdesk demo (7: / Play the Fin AI A |
| [software-technology](icons/software-technology.svg) | 12x12 | 0 0 16 16 | fill | view-demos | Software & Technology |
| [icon-709cdd5c](icons/icon-709cdd5c.svg) | 26x26 | 0 0 24 24 | fill | integrations | Zendesk Fin resolves Zendesk tickets and |
| [fin-ai-agent](icons/fin-ai-agent.svg) | 20x20 | 0 0 20 20 | fill | pricing | Fin AI Agent |
| [go-to-intercom](icons/go-to-intercom.svg) | 13x13 | 0 0 14 14 | stroke | changes | Go to Intercom |
| [icon-8595d86d](icons/icon-8595d86d.svg) | 16x16 | 0 0 16 16 | fill | view-demos |  |
| [gaming](icons/gaming.svg) | 12x12 | 0 0 16 16 | fill | view-demos | Gaming |
| [x](icons/x.svg) | 24x21 |  | fill | customers | X |
| [icon-8f7653ae](icons/icon-8f7653ae.svg) | 26x26 | 0 0 24 24 | fill | integrations | HubSpot Service Hub Fin resolves HubSpot / HubSpot CRM Fin p |
| [icon-9963aea6](icons/icon-9963aea6.svg) | 20x20 | 0 0 20 20.011 | fill | view-demos |  |
| [icon-9fcb2f73](icons/icon-9fcb2f73.svg) | 16x16 | 0 0 16 16 | fill | view-demos |  |
| [we-run-on-intercom](icons/we-run-on-intercom.svg) | 14x14 | 0 0 16 16 | fill | help | We run on Intercom |
| [essential](icons/essential.svg) | 12x12 | 0 0 12 12 | stroke | pricing | Essential |
| [english](icons/english-afa07479.svg) | 14x14 | 0 0 16 16 | stroke | help | English |
| [icon-c1816223](icons/icon-c1816223.svg) | 26x26 | 0 0 24 24 | fill | integrations | Custom MCP Connect any MCP-compliant too |
| [icon-c4f8969a](icons/icon-c4f8969a.svg) | 26x26 | 0 0 24 24 | fill | integrations | Salesforce Service Cloud Fin resolves Sa / Salesforce Fin pu |
| [neo-meet-our-customers](icons/neo-meet-our-customers.svg) | 48x32 |  | fill | copilot | Neo — Meet our customers |
| [ecommerce-retail](icons/ecommerce-retail.svg) | 12x12 | 0 0 16 16 | fill | view-demos | Ecommerce & Retail |
| [icon-d7298568](icons/icon-d7298568.svg) | 16x16 | 0 0 32 32 | fill | changes |  |
| [your-privacy-choices](icons/your-privacy-choices-e5f37a90.svg) | 25x12 | 0 0 25 12 | fill | help | Your Privacy Choices |
| [icon-f80df86f](icons/icon-f80df86f.svg) | 26x26 | 0 0 24 24 | fill | integrations | Any helpdesk Deploy Fin on any helpdesk  |
| [healthcare](icons/healthcare.svg) | 12x12 | 0 0 16 16 | fill | view-demos | Healthcare |

## Gaps

### Pages

- **Signed-in pages.** Nothing behind sign-in was captured: the Intercom app itself (app.intercom.com inbox, tickets, reports), trial onboarding at /signup, and any account surface. The kit never signs in and never follows a Log in or Start free trial link.
- **Anything that sends or creates.** No form was submitted: the contact-sales form was never advanced past its first step (Next was measured with forced pseudo states, never pressed), no demo was booked, no search was run, no option was chosen in the company-size select, the marketing checkbox was never ticked, and no trial was started.
- **Careers and docs.** `/careers` and `developers.intercom.com` were left out of scope; the capture covers the marketing site, the help center and the changelog.

### States

- **Pressed** was forced with DevTools on every button and link, so a state a script adds on mousedown (if any) is missing.
- **Hover on the plan cards, the article rows and the billing toggle's unselected half** changed nothing measurable; their entries read 'same'.
- **The promo banner's close** was exercised by the capture kit itself; no banner dismissal state is stored.
- **Disabled states** were not seen on any public control.

### Themes

www.intercom.com paints one light theme (`body.theme-light`). Its stylesheets do not declare a dark surface: no `prefers-color-scheme` dark rules that repaint the marketing pages, no dark class or attribute anywhere, and a forced `prefers-color-scheme: dark` pass changed nothing (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). The token file therefore ships no dark set.

### Fonts

- **Saans**, **SaansMono** and **Serrif** are Intercom's own faces, declared by `@font-face` on the page. Serrif is declared and styled (`.brand-i2y4`'s `--font-serif`) but no captured page painted it, so the style guide falls back where it would have been used.
- **MediumLL**, **IvoryLL** and **DmMono** are the older help/changelog faces under `.intercom-legacy`.
- **Beretta, Honey, Maxi, Ozik, Planar and Raster** are campaign display faces loaded by `next/font` variable classes for one-off sections.

### Screenshots

- Product screenshots, campaign illustrations and customer logos are Intercom's content and appear only inside screenshots and crops. Animated sections (hero canvases, marquee rows) keep moving, so two captures of the same view can differ.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article and release-note body text was not transcribed; only the frames around it were measured.
- No personal data was captured: the pages were read signed out, the contact form was never advanced, and the one filled-field reading typed and deleted a placeholder address that belongs to no one.
