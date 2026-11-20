# Figma components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from figma.com on 2026-11-15, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the contact, login, signup and Make prompt forms were never sent; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (63 components, 180 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `figmaSans 16/20.8 400, #000000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (180 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture: `light` for every public page — no page carried `data-theme="dark"` while captured (the site declares a complete `:root[data-theme="dark"]` token layer that nothing public resolved; it is the `dark` token set, labelled as declared-not-painted). /community, /login and /signup are the product app shell, a different stack that also paints light. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages bounded at eight chunks — the community and plugins grids grow without bound and were truncated with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu-products](screenshots/home-light-menu-products.png), [menu-solutions](screenshots/home-light-menu-solutions.png) |
| Figma Design | `/design/` | [default](screenshots/design-light-default.png), [full](screenshots/design-light-full.png) |
| FigJam | `/figjam/` | [default](screenshots/figjam-light-default.png), [full](screenshots/figjam-light-full.png) |
| Figma Slides | `/slides/` | [default](screenshots/slides-light-default.png), [full](screenshots/slides-light-full.png) |
| Dev Mode | `/dev-mode/` | [default](screenshots/dev-mode-light-default.png), [full](screenshots/dev-mode-light-full.png) |
| Figma Make | `/make/` | [default](screenshots/make-light-default.png), [full](screenshots/make-light-full.png) |
| Pricing | `/pricing/` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Community | `/community` | [default](screenshots/community-light-default.png), [full](screenshots/community-light-full.png) |
| Community plugins | `/community/plugins` | [default](screenshots/community-plugins-light-default.png), [full](screenshots/community-plugins-light-full.png) |
| Blog | `/blog/` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Customers | `/customers/` | [default](screenshots/customers-light-default.png), [full](screenshots/customers-light-full.png) |
| Enterprise | `/enterprise/` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| Careers | `/careers/` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| Contact sales | `/contact/` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Downloads | `/downloads/` | [default](screenshots/downloads-light-default.png), [full](screenshots/downloads-light-full.png) |
| Design systems | `/design-systems/` | [default](screenshots/design-systems-light-default.png), [full](screenshots/design-systems-light-full.png) |
| Release notes | `/release-notes/` | [default](screenshots/release-notes-light-default.png), [full](screenshots/release-notes-light-full.png) |
| Sign in (product shell) | `/login` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| Sign up (product shell) | `/signup` | [default](screenshots/signup-light-default.png), [full](screenshots/signup-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `/pricing/` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Community, phone | `/community` | [default](screenshots/mobile-community-light-default.png), [full](screenshots/mobile-community-light-full.png) |
| Contact, phone | `/contact/` | [default](screenshots/mobile-contact-light-default.png), [full](screenshots/mobile-contact-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent | every page | the consent layer is hidden before every shot and reading — 'Allow all cookies', 'Do not allow cookies' and 'Cookies settings' were never clicked | hidden, never answered |
| Products dropdown | every page header | clicked the 'Products' trigger (a local UI toggle; keyboard Enter is the fallback) | [home-light-menu-products](screenshots/home-light-menu-products.png), [nav-panel](#products-dropdown-panel), [nav-menu-item](#dropdown-item) |
| Solutions dropdown | every page header | the same activation on 'Solutions' | [home-light-menu-solutions](screenshots/home-light-menu-solutions.png) |
| Mobile nav overlay | home page, phone width | the 'Open navigation menu' button's own toggle | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-drawer](#mobile-nav-overlay) |
| Pricing controls | /pricing | the Monthly/Annual toggle, seat combobox and feature switch were measured at rest — toggling re-prices the grid, so they were never switched | [price-toggle](#billing-toggle), [seat-combo](#seat-combobox), [feature-switch](#feature-switch) |
| Feature accordions | /pricing | clicked one comparison-row accordion — a local UI toggle | [feature-acc](#feature-accordion) |
| Contact fields | /contact | typed into then cleared — nothing sent; the multi-step form's 'Next step' was never pressed | [field-email](#email-field), [field-firstname](#first-name-field), [field-lastname](#last-name-field), [field-topic](#topic-field) |
| Login/signup fields | /login and /signup | typed into then cleared — nothing sent | [login-email](#email-field-login), [signup-email](#email-field-signup) |
| Make prompt | /make | typed into then cleared — nothing sent | [prompt-textarea](#prompt-textarea) |
| Signed-in product | a Figma account | the editor and every post-login surface needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 30 components were given a real keyboard focus. 27 draw an outline ring: `nav-dropdown-btn` (2px dashed #000000 `light.theme.fg.default`, offset 4px), `nav-pricing` (2px dashed #000000 `light.theme.fg.default`, offset 4px), `nav-login` (2px dashed #000000 `light.theme.fg.default`, offset 4px), `nav-cta` (2px dashed #000000 `light.theme.fg.default`, offset 4px), `hero-cta` (2px dashed #000000 `light.theme.fg.default`, offset 4px), `footer-link` (2px dashed #ffffff `light.theme.bg`, offset 4px), `locale-btn` (2px dashed #ffffff `light.theme.bg`, offset 4px), `price-toggle` (2px dashed #000000 `light.theme.fg.default`, offset 4px), `feature-switch` (2px dashed #000000 `light.theme.fg.default`, offset 4px), `plan-cta` (2px dashed #000000 `light.theme.fg.default`, offset 4px), `login-google` (2px dashed #2c2c2c `core.component.productShell.login-submit-fill`, offset 4px), `login-submit` (2px dashed #2c2c2c `core.component.productShell.login-submit-fill`, offset 4px), `login-sso` (1px solid #757575, offset 1px), `signup-google` (2px dashed #2c2c2c `core.component.productShell.login-submit-fill`, offset 4px), `signup-continue` (2px dashed #2c2c2c `core.component.productShell.login-submit-fill`, offset 4px), `comm-cat` (1px solid #0d99ff, offset 1px), `comm-banner-nav` (2px solid #0d99ff, offset 2px), `comm-like` (1px solid #0d99ff, offset 1px), `prompt-submit` (2px dashed #000000 `light.theme.fg.default`, offset 4px), `dl-btn` (2px dashed #000000 `light.theme.fg.default`, offset 4px), `blog-topics` (1px dashed #ffffff `light.theme.bg`, offset 4px), `blog-search` (1px dashed #ffffff `light.theme.bg`, offset 4px), `careers-cta` (2px dashed #000000 `light.theme.fg.default`, offset 4px), `m-cta` (2px dashed #000000 `light.theme.fg.default`, offset 4px), `m-menu-btn` (2px dashed #000000 `light.theme.fg.default`, offset 4px), `m-hero-cta` (2px dashed #000000 `light.theme.fg.default`, offset 4px), `next-btn` (2px dashed #000000 `light.theme.fg.default`, offset 4px). 1 draw a focus ring as a shadow instead: `seat-combo`. 1 change only their border: `comm-signup`. The other 1 show no measured change: `comm-login`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.16s | `ease-out` | border-radius | login-submit, signup-continue |
| 0.18s | `ease` | border-color, box-shadow | prompt-textarea |
| 0.18s | `ease-out` | background, box-shadow | careers-cta, hero-cta, m-cta, m-hero-cta, nav-cta, next-btn, prompt-submit |
| 0.25s | `ease` | padding | faq-acc |
| 0.4s | `cubic-bezier(0.8, 0, 0.2, 1)` | background | mkt-header |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Products dropdown panel](#products-dropdown-panel) | 1440 x 522.84 | - | - | #ffffff `light.theme.bg` | none | 40px 0px |
| [Plan card](#plan-card) | 330 x 802.8 | L: 1px solid rgba(0, 0, 0, 0.16) `light.theme.border.default` | - | transparent | none | 0 |
| [Resource card](#resource-card) | 394.66 x 532.81 | - | - | transparent | none | 0 |
| [Login panel](#login-panel) | 422 x 479.59 | - | - | transparent | none | 0px 32px |
| [Signup panel](#signup-panel) | 422 x 302.59 | - | - | transparent | none | 0px 32px |
| [Mobile nav overlay](#mobile-nav-overlay) | 358 x 844 | - | - | transparent | none | 110px 0px 0px 0px |

## Components

### Site chrome

The header on every marketing page: the Figma mark, the Products/Solutions/Community/Resources dropdown triggers, Pricing and Enterprise links, Log in, Contact sales and the black 'Get started for free' pill; the products dropdown panel opens under the trigger.

#### Site header
The fixed top bar on every marketing page: the Figma mark, Products/Solutions/Community/Resources dropdown triggers, Pricing, Log in, Contact sales and the "Get started for free" CTA. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 78.39; background #ffffff `light.theme.bg`; text figmaSans 16/23.2 400, #000000 `light.theme.fg.default`; transition background 0.4s cubic-bezier(0.8, 0, 0.2, 1); icon 19 x 28, #000000 `light.theme.fg.default`.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Figma mark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 19 x 28; background transparent; text figmaSans 16/23.2 400, #000000 `light.theme.fg.default`; icon 19 x 28, #000000 `light.theme.fg.default`.

![Logo default](components/crops/mkt-logo-default.png)

#### Nav dropdown trigger
The "Products" header button — a data-nav-dropdown-trigger that opens the products dropdown. The opened state was measured after its own toggle click; aria-expanded had to stay true. Read as `nav-dropdown-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 103 x 39.19; padding 8px; background transparent; text figmaSans 16/23.2 400, #000000 `light.theme.fg.default`; icon 18 x 18, #000000 `light.theme.fg.default`; layers ::after rgba(0, 0, 0, 0) 0px none 0; span::after.nav-highlight.fig-1wty479 67pxx1px rgb(0, 0, 0) |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px; layers ::after rgba(0, 0, 0, 0) 0px none 0; button.dropdown-label.fig-7comqs 103.0x39.2 2px dashed rgb(0, 0, 0) offset 4px; span::after.nav-highlight.fig-1wty479 67pxx1px rgb(0, 0, 0) |

Child layers that carry the look: span::after 67pxx1px background #000000 `light.theme.fg.default`.

![Nav dropdown trigger default](components/crops/nav-dropdown-btn-default.png) ![Nav dropdown trigger hover](components/crops/nav-dropdown-btn-hover.png) ![Nav dropdown trigger focus-visible](components/crops/nav-dropdown-btn-focus-visible.png) ![Nav dropdown trigger pressed](components/crops/nav-dropdown-btn-pressed.png) ![Nav dropdown trigger opened](components/crops/nav-dropdown-btn-opened.png)

#### Products dropdown panel
The dropdown panel opened by the "Products" trigger (Figma Design, Make, Weave, Dev Mode, Motion, Specs, FigJam, Slides, Draw, Sites, Buzz, AI workflows, Release notes, Downloads); its links were never followed. Read as `nav-panel` on the home page.

**Values (default).** size 1440 x 522.84; padding 40px 0px; background #ffffff `light.theme.bg`; text figmaMono 14/18.2 400, oklch(0 0 none / 0.54); icon 22.39 x 22.39, #000000 `light.theme.fg.default`.

![Products dropdown panel default](components/crops/nav-panel-default.png)

#### Dropdown item
The "Figma Design" item inside the opened products dropdown; measured, never followed. Read as `nav-menu-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 328 x 49.58; background transparent; text figmaSans 16/22.4 400, #000000 `light.theme.fg.default`; icon 22.39 x 22.39, #000000 `light.theme.fg.default`; layers span::after.nav-highlight 96pxx1px rgb(0, 0, 0) |

Child layers that carry the look: span::after 96pxx1px background #000000 `light.theme.fg.default`.

![Dropdown item default](components/crops/nav-menu-item-default.png) ![Dropdown item hover](components/crops/nav-menu-item-hover.png)

#### Nav link
The "Pricing" header link; measured, never followed. Read as `nav-pricing` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 67 x 39.19; padding 8px; background transparent; text figmaSans 16/23.2 400, #000000 `light.theme.fg.default`; layers span::after.nav-highlight 51pxx1px rgb(0, 0, 0) |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px; layers a.fig-19xeqcu 67.0x39.2 2px dashed rgb(0, 0, 0) offset 4px; span::after.nav-highlight 51pxx1px rgb(0, 0, 0) |

Child layers that carry the look: span::after 51pxx1px background #000000 `light.theme.fg.default`.

![Nav link default](components/crops/nav-pricing-default.png) ![Nav link hover](components/crops/nav-pricing-hover.png) ![Nav link focus-visible](components/crops/nav-pricing-focus-visible.png) ![Nav link pressed](components/crops/nav-pricing-pressed.png)

#### Log in link
The "Log in" header link to /login; measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 59 x 39.19; padding 8px; background transparent; text figmaSans 16/23.2 400, #000000 `light.theme.fg.default`; layers span::after.nav-highlight 43pxx1px rgb(0, 0, 0) |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px; layers a.fig-12retlt 59.0x39.2 2px dashed rgb(0, 0, 0) offset 4px; span::after.nav-highlight 43pxx1px rgb(0, 0, 0) |

Child layers that carry the look: span::after 43pxx1px background #000000 `light.theme.fg.default`.

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Header CTA
The dark "Get started for free" header pill; links to /signup, measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 198 x 46.39; padding 12px 22px; radius 8px; background #000000 `light.theme.fg.default`; text figmaSans 16/22.4 400, #ffffff `light.theme.bg`; transition background 0.18s ease-out, box-shadow 0.18s ease-out; icon 20 x 20, #ffffff `light.theme.bg` |
| hover | background oklch(0 0 none / 0.85) |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px |
| pressed | background oklch(0 0 none / 0.85) |

![Header CTA default](components/crops/nav-cta-default.png) ![Header CTA hover](components/crops/nav-cta-hover.png) ![Header CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Header CTA pressed](components/crops/nav-cta-pressed.png)

### Home

The home hero: the display-size figmaSans masthead, the paired Get-started / Contact-sales pills, a demo video control and section headings.

#### Hero headline
"The full-stack creative canvas" — the figma.com hero display heading. Read as `hero-h1` on the home page.

**Values (default).** size 328 x 168; background transparent; text figmaSans 56/56 400, #000000 `light.theme.fg.default`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero CTA
The dark "Get started" pill in the hero; links to /signup, measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 222.75 x 84; padding 24px 32px; radius 16px; background #000000 `light.theme.fg.default`; text figmaSans 30/36 400, #ffffff `light.theme.bg`; transition background 0.18s ease-out, box-shadow 0.18s ease-out; icon 36 x 36, #ffffff `light.theme.bg` |
| hover | background oklab(0 0 0) |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px |
| pressed | background oklch(0 0 none / 0.85) |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Demo play button
A "Play" control on a hero/section product demo video; a local media toggle, measured not held. Read as `play-btn` on the home page.

Not on the page when it was captured.

#### Section heading
A marketing section heading further down the home page. Read as `section-h2` on the home page.

**Values (default).** size 901.33 x 36; background transparent; text figmaSans 30/36 400, #000000 `light.theme.fg.default`.

![Section heading default](components/crops/section-h2-default.png)

### Pricing

The /pricing grid: the Monthly/Annual pill toggle, the Full-seat combobox and the feature switch that re-price the cards, the plan columns and their CTAs, and the feature-list accordions in the comparison table.

#### Pricing headline
"Pick your plan, choose your seats" — the /pricing masthead. Read as `price-h1` on the pricing page.

**Values (default).** size 840 x 163.38; background transparent; text figmaSans 86/81.7 400, #000000 `light.theme.fg.default`.

![Pricing headline default](components/crops/price-h1-default.png)

#### Billing toggle
The Monthly/Annual segmented control; measured at rest, never toggled (toggling would re-price the grid). Read as `price-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 180 x 29; radius 80px; background rgba(0, 0, 0, 0.08) `light.theme.badge.bg`; text figmaSans 12/15 360, #000000 `light.theme.fg.default` |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px |

![Billing toggle default](components/crops/price-toggle-default.png) ![Billing toggle hover](components/crops/price-toggle-hover.png) ![Billing toggle focus-visible](components/crops/price-toggle-focus-visible.png) ![Billing toggle pressed](components/crops/price-toggle-pressed.png)

#### Seat combobox
The "Full seat" role combobox that re-prices the grid; measured at rest, never opened (its options recompute prices). Read as `seat-combo` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 180 x 53.19; padding 24px 36px 4px 12px; radius 8px; background rgba(0, 0, 0, 0.08) `light.theme.badge.bg`; text figmaSans 18/25.2 330, #000000 `light.theme.fg.default`; layers ::after rgb(0, 0, 0) 0px none 1 |
| hover | shadow #000000 0px 0px 0px 1px inset |
| focus-visible | shadow #000000 0px 0px 0px 2px inset |
| pressed | shadow #000000 0px 0px 0px 1px inset |

![Seat combobox default](components/crops/seat-combo-default.png) ![Seat combobox hover](components/crops/seat-combo-hover.png) ![Seat combobox focus-visible](components/crops/seat-combo-focus-visible.png) ![Seat combobox pressed](components/crops/seat-combo-pressed.png)

#### Feature switch
The "All features / Key features" switch (role=switch); measured at rest, never toggled. Read as `feature-switch` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 280 x 46.5; radius 80px; background rgba(0, 0, 0, 0.08) `light.theme.badge.bg`; text figmaSans 18/22.5 400, #000000 `light.theme.fg.default` |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px |

![Feature switch default](components/crops/feature-switch-default.png) ![Feature switch hover](components/crops/feature-switch-hover.png) ![Feature switch focus-visible](components/crops/feature-switch-focus-visible.png) ![Feature switch pressed](components/crops/feature-switch-pressed.png)

#### Plan card
The Professional plan column: name, price, seat copy and its CTA. Read as `plan-card` on the pricing page.

**Values (default).** size 330 x 802.8; border L: 1px solid rgba(0, 0, 0, 0.16) `light.theme.border.default`; background transparent; text figmaSans 32/41.6 400, #000000 `light.theme.fg.default`; icon 16 x 16, #000000 `light.theme.fg.default`; layers article.fig-1vpss82 330.0x802.8 L:1px solid rgba(0, 0, 0, 0.16); button.fig-sqbkms 180.0x29.0 rgba(0, 0, 0, 0.08) 80px; div.fig-k5xzwr 84.0x21.0 rgb(255, 255, 255) 80px; div.fig-qq6tkq 329.0x94.5 B:1px solid rgba(0, 0, 0, 0.08); div.fig-qq6tkq 329.0x94.5 B:1px solid rgba(0, 0, 0, 0.08); div.fig-qq6tkq 329.0x94.5 B:1px solid rgba(0, 0, 0, 0.08).

Child layers that carry the look: article 330x802.8 border 1px solid rgba(0, 0, 0, 0.16) `light.theme.border.default`; button 180x29 background rgba(0, 0, 0, 0.08) `light.theme.badge.bg` radius 80px; div 84x21 background #ffffff `light.theme.bg` radius 80px.

![Plan card default](components/crops/plan-card-default.png)

#### Plan CTA
A plan card's action (Get started / Contact sales), scoped to a plan article so the header's "Contact sales" link cannot match first; measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 84 x 26.09; radius 2px; background transparent; text figmaSans 14/20.3 340, #697485 |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px; layers a.fig-1d1iijj 84.0x26.1 2px dashed rgb(0, 0, 0) offset 4px 2px |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Feature accordion
A feature-list accordion in the comparison grid ("Components", "Auto layout", ...); the opened state was measured after clicking it — a local UI toggle. Read as `feature-acc` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened, hover) | size 412 x 24; background #ffffff `light.theme.bg`; text figmaSans 16/23.2 320, #000000 `light.theme.fg.default`; icon 24 x 24, #000000 `light.theme.fg.default` |

![Feature accordion default](components/crops/feature-acc-default.png) ![Feature accordion opened](components/crops/feature-acc-opened.png) ![Feature accordion hover](components/crops/feature-acc-hover.png)

### Contact sales form

The /contact sales form's first step: work-email, first/last name, a topic input and one free-text field, then the multi-step 'Next step' button — measured and typed into then cleared, never advanced and never submitted.

#### Contact headline
The /contact masthead over the sales form. Read as `contact-h1` on the contact page.

**Values (default).** size 510 x 61.59; background transparent; text figmaSans 56/61.6 400, #000000 `light.theme.fg.default`.

![Contact headline default](components/crops/contact-h1-default.png)

#### Email field
The work-email input; focused and typed into then cleared — never submitted. Read as `field-email` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 600 x 58.19; padding 27px 12px 6px 12px; radius 8px; background rgba(0, 0, 0, 0.08) `light.theme.badge.bg`; text figmaSans 18/25.2 330, #000000 `light.theme.fg.default`; placeholder #000000 `light.theme.fg.default` |
| focused, filled | shadow #000000 0px 0px 0px 2px inset |

![Email field default](components/crops/field-email-default.png) ![Email field focused](components/crops/field-email-focused.png) ![Email field filled](components/crops/field-email-filled.png)

#### First name field
The first-name input; focused and typed into then cleared — never submitted. Read as `field-firstname` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 294 x 58.19; padding 27px 12px 6px 12px; radius 8px; background rgba(0, 0, 0, 0.08) `light.theme.badge.bg`; text figmaSans 18/25.2 330, #000000 `light.theme.fg.default`; placeholder #000000 `light.theme.fg.default` |
| focused, filled | shadow #000000 0px 0px 0px 2px inset |

![First name field default](components/crops/field-firstname-default.png) ![First name field focused](components/crops/field-firstname-focused.png) ![First name field filled](components/crops/field-firstname-filled.png)

#### Last name field
The last-name input; focused and typed into then cleared — never submitted. Read as `field-lastname` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 294 x 58.19; padding 27px 12px 6px 12px; radius 8px; background rgba(0, 0, 0, 0.08) `light.theme.badge.bg`; text figmaSans 18/25.2 330, #000000 `light.theme.fg.default`; placeholder #000000 `light.theme.fg.default` |
| focused, filled | shadow #000000 0px 0px 0px 2px inset |

![Last name field default](components/crops/field-lastname-default.png) ![Last name field focused](components/crops/field-lastname-focused.png) ![Last name field filled](components/crops/field-lastname-filled.png)

#### Free-text field
The unnamed free-text input on the sales form's first step (the name=topic twin is a display:none honeypot); focused and typed into then cleared — never submitted. Read as `field-topic` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 600 x 58.19; padding 27px 40px 6px 12px; radius 8px; background rgba(0, 0, 0, 0.08) `light.theme.badge.bg`; text figmaSans 18/25.2 330, #000000 `light.theme.fg.default`; placeholder #000000 `light.theme.fg.default` |
| focused | radius 8px 8px 0px 0px; shadow #000000 0px 0px 0px 2px inset |
| filled | shadow #000000 0px 0px 0px 2px inset |

![Free-text field default](components/crops/field-topic-default.png) ![Free-text field focused](components/crops/field-topic-focused.png) ![Free-text field filled](components/crops/field-topic-filled.png)

#### Next step button
The multi-step form's "Next step" button; its states were measured but the button was never clicked — the form never advanced. Read as `next-btn` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 480 x 46.39; padding 12px 22px; radius 8px; background #000000 `light.theme.fg.default`; text figmaSans 16/22.4 400, #ffffff `light.theme.bg`; transition background 0.18s ease-out, box-shadow 0.18s ease-out; icon 20 x 20, #ffffff `light.theme.bg` |
| hover | background oklch(0 0 none / 0.85) |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px |
| pressed | background oklch(0 0 none / 0.85) |

![Next step button default](components/crops/next-btn-default.png) ![Next step button hover](components/crops/next-btn-hover.png) ![Next step button focus-visible](components/crops/next-btn-focus-visible.png) ![Next step button pressed](components/crops/next-btn-pressed.png)

### Login and signup (product shell)

/login and /signup — the product app shell's sign-in and sign-up cards (Google SSO, e-mail/password, 'Continue with email'), a different stack that does not share the marketing --fig-* layer. Measured as forms, never submitted.

#### Login panel
The product-shell sign-in card on /login: "Sign in to Figma" with Google SSO, e-mail and password. Read as `login-panel` on the login page.

**Values (default).** size 422 x 479.59; padding 0px 32px; background transparent; text Figma Sans 32/41.6 500, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink`; icon 18 x 18, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink`; layers button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 T:1px solid rgb(44, 44, 44) / R:1px solid rgb(44, 44, 44) / B:1px solid rgb(44, 44, 44) / L:1px solid rgb(44, 44, 44) 8px; input.lazy_input--lazyInput--akTHe 358.0x53.0 rgba(0, 0, 0, 0.05) 6px; input.lazy_input--lazyInput--akTHe 358.0x53.0 rgba(0, 0, 0, 0.05) 6px; button.brand_buttons--brandButton--Y6xZJ.auth_view--b.

Child layers that carry the look: button 358x48 border 1px solid #2c2c2c `core.component.productShell.login-submit-fill` radius 8px; input 358x53 background rgba(0, 0, 0, 0.05) radius 6px; input 358x53 background rgba(0, 0, 0, 0.05) radius 6px.

![Login panel default](components/crops/login-panel-default.png)

#### Google SSO button
The "Continue with Google" button; measured, never pressed. Read as `login-google` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 358 x 48; padding 0px 20px; border 1px solid #2c2c2c `core.component.productShell.login-submit-fill`; radius 8px; background transparent; text Figma Sans 18/25.2 480, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink`; icon 18 x 18, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink` |
| focus-visible | outline 2px dashed #2c2c2c `core.component.productShell.login-submit-fill`, offset 4px |

![Google SSO button default](components/crops/login-google-default.png) ![Google SSO button hover](components/crops/login-google-hover.png) ![Google SSO button focus-visible](components/crops/login-google-focus-visible.png) ![Google SSO button pressed](components/crops/login-google-pressed.png)

#### Email field (login)
The e-mail input on the sign-in card; focused and typed into then cleared — never submitted. Read as `login-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 358 x 53; padding 24px 12px 6px 12px; radius 6px; background rgba(0, 0, 0, 0.05); text Figma Sans 18/25 320, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink`; placeholder rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink` |
| focused, filled | shadow #444444 0px 0px 0px 2px inset |

![Email field (login) default](components/crops/login-email-default.png) ![Email field (login) focused](components/crops/login-email-focused.png) ![Email field (login) filled](components/crops/login-email-filled.png)

#### Password field (login)
The password input on the sign-in card; focused and typed into then cleared — never submitted. Read as `login-password` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 358 x 53; padding 24px 12px 6px 12px; radius 6px; background rgba(0, 0, 0, 0.05); text Figma Sans 18/25 320, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink`; placeholder rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink` |
| focused, filled | shadow #444444 0px 0px 0px 2px inset |

![Password field (login) default](components/crops/login-password-default.png) ![Password field (login) focused](components/crops/login-password-focused.png) ![Password field (login) filled](components/crops/login-password-filled.png)

#### Log in submit
The "Log in" submit button; its states were measured but the button was never clicked — nothing was submitted. Read as `login-submit` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 358 x 48; padding 0px 20px; radius 8px; background #2c2c2c `core.component.productShell.login-submit-fill`; text Figma Sans 18/25.2 480, rgba(255, 255, 255, 0.898) `core.component.productShell.login-submit-ink`; transition border-radius 0.16s ease-out; icon 22 x 21, rgba(255, 255, 255, 0.898) `core.component.productShell.login-submit-ink` |
| hover | radius none |
| focus-visible | outline 2px dashed #2c2c2c `core.component.productShell.login-submit-fill`, offset 4px |
| pressed | radius none |

![Log in submit default](components/crops/login-submit-default.png) ![Log in submit hover](components/crops/login-submit-hover.png) ![Log in submit focus-visible](components/crops/login-submit-focus-visible.png) ![Log in submit pressed](components/crops/login-submit-pressed.png)

#### SSO link
The "Use single sign-on" link; measured, never followed. Read as `login-sso` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 117 x 20; background transparent; text Figma Sans 14/20 500, #0768cf |
| focus-visible | outline 1px solid #757575, offset 1px; layers a 117.0x20.0 1px solid rgb(117, 117, 117) offset 1px |

![SSO link default](components/crops/login-sso-default.png) ![SSO link hover](components/crops/login-sso-hover.png) ![SSO link focus-visible](components/crops/login-sso-focus-visible.png) ![SSO link pressed](components/crops/login-sso-pressed.png)

#### Signup panel
The product-shell sign-up card on /signup: "Welcome to Figma" with Google SSO and an e-mail field. Read as `signup-panel` on the signup page.

**Values (default).** size 422 x 302.59; padding 0px 32px; background transparent; text Figma Sans 32/41.6 500, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink`; icon 18 x 18, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink`; layers button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 T:1px solid rgb(44, 44, 44) / R:1px solid rgb(44, 44, 44) / B:1px solid rgb(44, 44, 44) / L:1px solid rgb(44, 44, 44) 8px; input.lazy_input--lazyInput--akTHe 358.0x53.0 rgba(0, 0, 0, 0.05) 6px; button.brand_buttons--brandButton--Y6xZJ.auth_view--brandButton--dD0L7 358.0x48.0 rgb(44, 44, 44) 8px.

Child layers that carry the look: button 358x48 border 1px solid #2c2c2c `core.component.productShell.login-submit-fill` radius 8px; input 358x53 background rgba(0, 0, 0, 0.05) radius 6px; button 358x48 background #2c2c2c `core.component.productShell.login-submit-fill` radius 8px.

![Signup panel default](components/crops/signup-panel-default.png)

#### Google SSO button (signup)
The "Continue with Google" button on /signup; measured, never pressed. Read as `signup-google` on the signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 358 x 48; padding 0px 20px; border 1px solid #2c2c2c `core.component.productShell.login-submit-fill`; radius 8px; background transparent; text Figma Sans 18/25.2 480, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink`; icon 18 x 18, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink` |
| focus-visible | outline 2px dashed #2c2c2c `core.component.productShell.login-submit-fill`, offset 4px |

![Google SSO button (signup) default](components/crops/signup-google-default.png) ![Google SSO button (signup) hover](components/crops/signup-google-hover.png) ![Google SSO button (signup) focus-visible](components/crops/signup-google-focus-visible.png) ![Google SSO button (signup) pressed](components/crops/signup-google-pressed.png)

#### Email field (signup)
The e-mail input on the sign-up card; focused and typed into then cleared — never submitted. Read as `signup-email` on the signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 358 x 53; padding 24px 12px 6px 12px; radius 6px; background rgba(0, 0, 0, 0.05); text Figma Sans 18/25 320, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink`; placeholder rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink` |
| focused, filled | shadow #444444 0px 0px 0px 2px inset |

![Email field (signup) default](components/crops/signup-email-default.png) ![Email field (signup) focused](components/crops/signup-email-focused.png) ![Email field (signup) filled](components/crops/signup-email-filled.png)

#### Continue with email
The "Continue with email" button; its states were measured but the button was never clicked — nothing was submitted. Read as `signup-continue` on the signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 358 x 48; padding 0px 20px; radius 8px; background #2c2c2c `core.component.productShell.login-submit-fill`; text Figma Sans 18/25.2 480, rgba(255, 255, 255, 0.898) `core.component.productShell.login-submit-ink`; transition border-radius 0.16s ease-out; icon 22 x 21, rgba(255, 255, 255, 0.898) `core.component.productShell.login-submit-ink` |
| hover | radius none |
| focus-visible | outline 2px dashed #2c2c2c `core.component.productShell.login-submit-fill`, offset 4px |
| pressed | radius none |

![Continue with email default](components/crops/signup-continue-default.png) ![Continue with email hover](components/crops/signup-continue-hover.png) ![Continue with email focus-visible](components/crops/signup-continue-focus-visible.png) ![Continue with email pressed](components/crops/signup-continue-pressed.png)

### Community (product shell)

/community — the public community index inside the product shell: the masthead, the search input, the category filter buttons, the banner carousel control, resource cards, and the shell's Log in / Sign up buttons. The resource grids are bounded; the boundary is recorded on the -full screenshots.

#### Community headline
"Discover community-made libraries, plugins, icon sets, and more" — the /community masthead in the product shell. Read as `comm-h1` on the community page.

**Values (default).** size 420 x 64; background transparent; text Inter 24/32 500, #007be5; icon 92 x 52.9, #007be5; layers img.hero--pluginImg--3qnJi 19.8x19.8 rgba(0, 0, 0, 0) 0px 21px 6px 0px, rgba(0, 0, 0, 0.01) 0px 14px 5px 0px, rgba(0, 0, 0, 0.05) 0px 8px 5px 0px, rgba(0, 0, 0, 0.09) 0px 3px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px 0px 8px; img.hero--pluginImg--3qnJi 19.8x19.8 rgba(0, 0, 0, 0) 0px 21px 6px 0px, rgba(0, 0, 0, 0.01) 0px 14px 5px 0px, rgba(0, 0, 0, 0.05) 0px 8px 5px 0px, rgba(0, 0, 0, 0.09) 0px 3px 3.

Child layers that carry the look: img 19.8x19.8 radius 8px shadow transparent 0px 21px 6px 0px, rgba(0, 0, 0, 0.01) 0px 14px 5px 0px, rgba(0, 0, 0, 0.05) 0px 8px 5px 0px, rgba(0, 0, 0, 0.09) 0px 3px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px 0px; img 19.8x19.8 radius 8px shadow transparent 0px 21px 6px 0px, rgba(0, 0, 0, 0.01) 0px 14px 5px 0px, rgba(0, 0, 0, 0.05) 0px 8px 5px 0px, rgba(0, 0, 0, 0.09) 0px 3px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px 0px; img 18.1x18.1 radius 8px shadow transparent 0px 21px 6px 0px, rgba(0, 0, 0, 0.01) 0px 14px 5px 0px, rgba(0, 0, 0, 0.05) 0px 8px 5px 0px, rgba(0, 0, 0, 0.09) 0px 3px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px 0px.

![Community headline default](components/crops/comm-h1-default.png)

#### Community search
The "Search for resources like …" input; focused and typed into then cleared — never searched. Read as `comm-search` on the community page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 284 x 40; padding 0px 8px 0px 0px; background transparent; text Inter 11/16 450, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink`; placeholder rgba(0, 0, 0, 0.3) |
| filled | size 252 x 40 |

![Community search default](components/crops/comm-search-default.png) ![Community search focused](components/crops/comm-search-focused.png) ![Community search filled](components/crops/comm-search-filled.png)

#### Category button
A category filter button (Design resources / Websites / Extensions / Whiteboarding / Presentations); measured at rest, never toggled. Read as `comm-cat` on the community page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 146.95 x 32; padding 0px 12px; radius 5px; background transparent; text Inter 13/24 500, #000000 `light.theme.fg.default`; icon 8 x 8, #000000 `light.theme.fg.default` |
| hover | background #f5f5f5 |
| focus-visible | outline 1px solid #0d99ff, offset 1px; layers button._19xx72g0.nav_category_selector_2--navCategorySelectorText--V2TK0 147.0x32.0 1px solid rgb(13, 153, 255) offset 1px 5px |

![Category button default](components/crops/comm-cat-default.png) ![Category button hover](components/crops/comm-cat-hover.png) ![Category button focus-visible](components/crops/comm-cat-focus-visible.png) ![Category button pressed](components/crops/comm-cat-pressed.png)

#### Community Log in
The product-shell "Log in" button; measured, never pressed. Read as `comm-login` on the community page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 34.03 x 32; radius 6px; background #ffffff `light.theme.bg`; text Inter 11/16 400, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink` |

![Community Log in default](components/crops/comm-login-default.png) ![Community Log in hover](components/crops/comm-login-hover.png) ![Community Log in focus-visible](components/crops/comm-login-focus-visible.png) ![Community Log in pressed](components/crops/comm-login-pressed.png)

#### Community Sign up
The product-shell "Sign up" button; measured, never pressed. Read as `comm-signup` on the community page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 70.05 x 32; padding 7px 13px; border 1px solid rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink`; radius 6px; background #ffffff `light.theme.bg`; text Inter 11/16 400, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink` |
| focus-visible | padding 6px 12px; border 2px solid #0d99ff |
| pressed | background #e6e6e6 |

![Community Sign up default](components/crops/comm-signup-default.png) ![Community Sign up hover](components/crops/comm-signup-hover.png) ![Community Sign up focus-visible](components/crops/comm-signup-focus-visible.png) ![Community Sign up pressed](components/crops/comm-signup-pressed.png)

#### Banner carousel control
The hero banner carousel's "Next banner" control — a local UI toggle; measured, never cycled. Read as `comm-banner-nav` on the community page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; border 1px solid #e6e6e6; radius 9999px; background #ffffff `light.theme.bg`; text Inter 16/normal 400, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink`; icon 16 x 16, rgba(0, 0, 0, 0.898) `core.component.productShell.comm-signup-ink` |
| hover | background #f5f5f5 |
| focus-visible | outline 2px solid #0d99ff, offset 2px |
| pressed | background #f5f5f5 |

![Banner carousel control default](components/crops/comm-banner-nav-default.png) ![Banner carousel control hover](components/crops/comm-banner-nav-hover.png) ![Banner carousel control focus-visible](components/crops/comm-banner-nav-focus-visible.png) ![Banner carousel control pressed](components/crops/comm-banner-nav-pressed.png)

#### Resource card
A community "Riff" card (thumbnail, title, author, like count); measured, never followed. Read as `comm-card` on the community page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 394.66 x 532.81; background transparent; text Inter 16/normal 400, #000000 `light.theme.fg.default` |

![Resource card default](components/crops/comm-card-default.png) ![Resource card hover](components/crops/comm-card-hover.png)

#### Like button
A resource card's like button; measured, never pressed (a like would write to an account). Read as `comm-like` on the community page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 20 x 20; radius 6px; background transparent; text Inter 14/24 600, #000000 `light.theme.fg.default`; icon 16 x 16, #000000 `light.theme.fg.default`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | radius 5px; outline 1px solid #0d99ff, offset 1px; layers ::after rgba(0, 0, 0, 0) 0px none 1; button.base_like_button--buttonContainerPrettyCompact--6qXsV.base_like_button--buttonContainerPretty--KdBsv 20.0x20.0 1px solid rgb(13, 153, 255) offset 1px 5px |

![Like button default](components/crops/comm-like-default.png) ![Like button hover](components/crops/comm-like-hover.png) ![Like button focus-visible](components/crops/comm-like-focus-visible.png) ![Like button pressed](components/crops/comm-like-pressed.png)

### Prompt surfaces

/make — the Figma Make prompt surface: the 'What do you want to make?' textarea and its Submit, measured and typed into then cleared, never sent.

#### Make headline
The /make masthead — "Figma Make". Read as `prompt-h1` on the make page.

**Values (default).** size 672 x 48.39; background transparent; text figmaSans 44/48.4 400, #000000 `light.theme.fg.default`; icon 39.59 x 39.59, #000000 `light.theme.fg.default`.

![Make headline default](components/crops/prompt-h1-default.png)

#### Prompt textarea
The "What do you want to make?" prompt box on /make; focused and typed into then cleared — never submitted. Read as `prompt-textarea` on the make page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 672 x 97.19; padding 36px 96px 36px 32px; border 1px solid oklch(0 0 none / 0.16); radius 24px; background #ffffff `light.theme.bg`; shadow oklch(0 0 none / 0.1) 0px 24px 70px 0px; text figmaSans 16/22.4 400, #000000 `light.theme.fg.default`; transition box-shadow 0.18s ease, border-color 0.18s ease; placeholder oklch(0 0 none / 0.54) |
| focused, filled | padding 35px 95px 35px 31px; border 2px solid #000000 `light.theme.fg.default` |

![Prompt textarea default](components/crops/prompt-textarea-default.png) ![Prompt textarea focused](components/crops/prompt-textarea-focused.png) ![Prompt textarea filled](components/crops/prompt-textarea-filled.png)

#### Prompt submit
The prompt box's icon-only submit button; its states were measured but the button was never clicked — nothing was sent. Read as `prompt-submit` on the make page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 48 x 48; padding 16px; radius 9999px; background #d2d9e2; text figmaSans 16/18.4 400, #ffffff `light.theme.bg`; transition background 0.18s ease-out, box-shadow 0.18s ease-out; opacity 0.6; icon 16 x 20, #ffffff `light.theme.bg` |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px |
| pressed | background #4d49fc |

![Prompt submit default](components/crops/prompt-submit-default.png) ![Prompt submit hover](components/crops/prompt-submit-hover.png) ![Prompt submit focus-visible](components/crops/prompt-submit-focus-visible.png) ![Prompt submit pressed](components/crops/prompt-submit-pressed.png)

### Blog, downloads and careers

The /blog index (Topics and Search filter buttons, the newsletter field), the /downloads platform links and the /careers open-positions list.

#### Downloads headline
The /downloads masthead — "Figma downloads". Read as `dl-h1` on the downloads page.

**Values (default).** size 780 x 72; background transparent; text figmaSans 72/72 400, #000000 `light.theme.fg.default`.

![Downloads headline default](components/crops/dl-h1-default.png)

#### Download link
The "Desktop app for macOS" download link (desktop apps, mobile apps, font installers, the Chrome extension); measured, never followed. Read as `dl-btn` on the downloads page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 195 x 20; background transparent; text figmaSans 18/25.2 330, #000000 `light.theme.fg.default` |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px; layers a 195.0x20.0 2px dashed rgb(0, 0, 0) offset 4px |

![Download link default](components/crops/dl-btn-default.png) ![Download link hover](components/crops/dl-btn-hover.png) ![Download link focus-visible](components/crops/dl-btn-focus-visible.png) ![Download link pressed](components/crops/dl-btn-pressed.png)

#### Topics button
The blog index's "Topics" filter button — a local UI toggle; measured, never toggled. Read as `blog-topics` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 105.14 x 27; padding 8px 0px 0px 32px; background transparent; text figmaSans 18/18 330, #ffffff `light.theme.bg`; icon 11.14 x 13, #ffffff `light.theme.bg`; layers ::before rgb(255, 255, 255) 0px none 1; button::before.fig-1xfqluc 1pxx19px rgb(255, 255, 255) |
| focus-visible | outline 1px dashed #ffffff `light.theme.bg`, offset 4px; layers ::before rgb(255, 255, 255) 0px none 1; button.fig-1xfqluc 105.1x27.0 1px dashed rgb(255, 255, 255) offset 4px; button::before.fig-1xfqluc 1pxx19px rgb(255, 255, 255) |

Child layers that carry the look: button::before 1pxx19px background #ffffff `light.theme.bg`.

![Topics button default](components/crops/blog-topics-default.png) ![Topics button hover](components/crops/blog-topics-hover.png) ![Topics button focus-visible](components/crops/blog-topics-focus-visible.png) ![Topics button pressed](components/crops/blog-topics-pressed.png)

#### Search button
The blog index's "Search" button — a local UI toggle; measured, never toggled. Read as `blog-search` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40 x 27; background transparent; text figmaSans 18/25.2 330, #ffffff `light.theme.bg`; icon 16 x 16, #ffffff `light.theme.bg` |
| focus-visible | outline 1px dashed #ffffff `light.theme.bg`, offset 4px; layers button.fig-11smye 40.0x27.0 1px dashed rgb(255, 255, 255) offset 4px |

![Search button default](components/crops/blog-search-default.png) ![Search button hover](components/crops/blog-search-hover.png) ![Search button focus-visible](components/crops/blog-search-focus-visible.png) ![Search button pressed](components/crops/blog-search-pressed.png)

#### Newsletter field
The editorial-newsletter e-mail input in the blog rail; focused and typed into then cleared — never subscribed. Read as `blog-subscribe` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 743 x 53.89; padding 0px 70px 0px 0px; border B: 1px solid #ffffff `light.theme.bg`; background transparent; text figmaSans 46/52.9 400, #ffffff `light.theme.bg`; placeholder #757575; layers input.fig-1fitj2g 743.0x53.9 B:1px solid rgb(255, 255, 255) |

Child layers that carry the look: input 743x53.9 border 1px solid #ffffff `light.theme.bg`.

![Newsletter field default](components/crops/blog-subscribe-default.png) ![Newsletter field focused](components/crops/blog-subscribe-focused.png) ![Newsletter field filled](components/crops/blog-subscribe-filled.png)

#### Careers CTA
The "See open positions" link on /careers; measured, never followed. Read as `careers-cta` on the careers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 194 x 46.39; padding 12px 22px; radius 8px; background #000000 `light.theme.fg.default`; text figmaSans 16/22.4 400, #ffffff `light.theme.bg`; transition background 0.18s ease-out, box-shadow 0.18s ease-out; icon 20 x 20, #ffffff `light.theme.bg` |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px |

![Careers CTA default](components/crops/careers-cta-default.png) ![Careers CTA hover](components/crops/careers-cta-hover.png) ![Careers CTA focus-visible](components/crops/careers-cta-focus-visible.png) ![Careers CTA pressed](components/crops/careers-cta-pressed.png)

#### Job link
An open-position link in the careers list; measured, never followed. Read as `job-link` on the careers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 246 x 20; background transparent; text figmaSans 18/25.2 330, #000000 `light.theme.fg.default` |

![Job link default](components/crops/job-link-default.png) ![Job link hover](components/crops/job-link-hover.png)

### FAQ accordions

The /design-systems FAQ rows — the accordions mount open; the closed state was measured after clicking the row, a local UI toggle.

#### FAQ accordion
A question row in the /design-systems FAQ (all accordions mount open); the closed state was measured after clicking the row — a local UI toggle. Read as `faq-acc` on the design-systems page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 720 x 97.59; padding 32px 0px 24px 0px; background transparent; text figmaSans 32/41.6 400, #000000 `light.theme.fg.default`; transition padding 0.25s ease; icon 32 x 32, #000000 `light.theme.fg.default` |
| closed | size 720 x 105.59; padding 32px 0px |

![FAQ accordion default](components/crops/faq-acc-default.png) ![FAQ accordion closed](components/crops/faq-acc-closed.png)

### Mobile (390 wide)

The phone surface at 390 wide: the header with the nav button and 'Get started for free' pill, the full-viewport nav overlay, the hero and CTA.

#### Mobile top bar
The phone header at 390 wide: the Figma mark, "Get started for free", the nav button and the locale button. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 390 x 72; background #ffffff `light.theme.bg`; shadow oklch(0 0 none / 0.16) 0px 1px 0px 0px; text figmaSans 16/22.4 400, #ffffff `light.theme.bg`; icon 32 x 48, #000000 `light.theme.fg.default`.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile header CTA
The header "Get started for free" pill at 390 wide; measured never followed. Read as `m-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 198 x 46.39; padding 12px 22px; radius 8px; background #000000 `light.theme.fg.default`; text figmaSans 16/22.4 400, #ffffff `light.theme.bg`; transition background 0.18s ease-out, box-shadow 0.18s ease-out; icon 20 x 20, #ffffff `light.theme.bg` |
| hover | background oklch(0 0 none / 0.85) |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px |
| pressed | background oklch(0 0 none / 0.85) |

![Mobile header CTA default](components/crops/m-cta-default.png) ![Mobile header CTA hover](components/crops/m-cta-hover.png) ![Mobile header CTA focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile header CTA pressed](components/crops/m-cta-pressed.png)

#### Mobile menu button
The "Open navigation menu" button — a local UI toggle; the opened state was measured after activating it. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 40 x 40; padding 8px; background transparent; text figmaSans 16/23.2 400, #000000 `light.theme.fg.default`; icon 24 x 24, #000000 `light.theme.fg.default` |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px; layers button.fig-1aem8bs 40.0x40.0 2px dashed rgb(0, 0, 0) offset 4px |

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png) ![Mobile menu button opened](components/crops/m-menu-btn-opened.png)

#### Mobile nav overlay
The accordion nav inside the nav overlay opened by the menu button (Products/Solutions/Community/Resources accordions plus the page links); its links were never followed. Read as `m-drawer` on the home page at 390 wide.

**Values (default).** size 358 x 844; padding 110px 0px 0px 0px; background transparent; text figmaSans 24/28.8 400, #000000 `light.theme.fg.default`; icon 24 x 24, #000000 `light.theme.fg.default`; layers div.fig-5w9uj6 358.0x371.8 B:1px solid oklch(0 0 none / 0.16); button.dropdown-label.fig-1wo6hfm 358.0x61.8 T:1px solid oklch(0 0 none / 0.16); span::after.nav-highlight autox1px rgb(0, 0, 0); span::after.nav-highlight autox1px rgb(0, 0, 0); span::after.nav-highlight autox1px rgb(0, 0, 0); span::after.nav-highlight autox1px rgb(0, 0, 0).

Child layers that carry the look: div 358x371.8 border 1px solid oklch(0 0 none / 0.16); button 358x61.8 border 1px solid oklch(0 0 none / 0.16); span::after autox1px background #000000 `light.theme.fg.default`.

![Mobile nav overlay default](components/crops/m-drawer-default.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 358 x 72; background transparent; text figmaSans 36/36 400, #000000 `light.theme.fg.default`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The hero "Get started" pill at 390 wide; measured never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 196.75 x 76.8; padding 24px 32px; radius 16px; background #000000 `light.theme.fg.default`; text figmaSans 24/28.8 400, #ffffff `light.theme.bg`; transition background 0.18s ease-out, box-shadow 0.18s ease-out; icon 36 x 36, #ffffff `light.theme.bg` |
| hover | background oklab(0 0 0 / 0.946565) |
| focus-visible | outline 2px dashed #000000 `light.theme.fg.default`, offset 4px |
| pressed | background oklch(0 0 none / 0.85) |

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

### Footer

The page footer: sitemap columns, social icons and the 'English' locale button. Its field paints black directly, not through a theme scope.

#### Footer
The page footer: product/use-case/resource columns, social icons and the locale button. Read as `footer` on the home page.

**Values (default).** size 1440 x 1261.47; padding 120px 0px; border T: 1px solid rgba(255, 255, 255, 0.16); background #000000 `light.theme.fg.default`; text figmaMono 16/20.8 400, rgba(255, 255, 255, 0.6).

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 56.17 x 20; background transparent; text figmaSans 16/23.2 320, #ffffff `light.theme.bg` |
| focus-visible | outline 2px dashed #ffffff `light.theme.bg`, offset 4px; layers a.fig-1czkxn0 56.2x20.0 2px dashed rgb(255, 255, 255) offset 4px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Locale button
The "English" locale button in the footer — a local UI toggle for the locale list; measured, never toggled. Read as `locale-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 118 x 39.19; padding 8px; background transparent; text figmaSans 16/23.2 400, #ffffff `light.theme.bg`; icon 22 x 22, #ffffff `light.theme.bg` |
| focus-visible | outline 2px dashed #ffffff `light.theme.bg`, offset 4px; layers button.fig-q9rm4z 118.0x39.2 2px dashed rgb(255, 255, 255) offset 4px |

![Locale button default](components/crops/locale-btn-default.png) ![Locale button hover](components/crops/locale-btn-hover.png) ![Locale button focus-visible](components/crops/locale-btn-focus-visible.png) ![Locale button pressed](components/crops/locale-btn-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Figma mark, the product dropdown glyphs, social glyphs, community resource thumbnails) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Figma's product is the editor: the canvas, files, FigJam boards, Dev Mode inside a file, Make projects, the community profile and publish flows — every surface after `Log in` needs an account and was never reached. /login and /signup are the only app surfaces a signed-out visitor sees, and they were measured as forms, never submitted. The product demos embedded in the marketing pages are videos and mocks, not the product.

### Pages

- **The account.** The editor and every post-login surface (files, the canvas, account settings, admin, the community publish flow) was never reached; the /login and /signup forms were measured as forms and never submitted; 'Continue with Google' and 'Use single sign-on' were never followed.
- **Forms.** The /contact sales form, the /make prompt, the blog newsletter field and the community search were measured at rest and typed into then cleared — nothing was sent; what a submission returns is unverified.
- **Careers.** The open-position links leave figma.com for the ATS; individual job posts were not captured.
- **Blog posts, customer stories and release-note entries** are index-level captures only; individual articles are the same templates, unmeasured.
- **Community resource pages** (a plugin's detail page, a creator profile) were not captured — the grids are index surfaces, bounded at eight chunks.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **The billing toggle, seat combobox and feature switch** on /pricing re-price the grid when flipped; they were measured at rest and never switched, so the Monthly prices and the alternate-seat grid are uncaptured.
- **Dropdown panel items' focus/hover** is partially covered: the panel closes on blur, so a real keyboard focus inside it could not always be held.

### Themes

Every public figma.com page paints the `:root` light token layer — the marketing pages, /community, /login and /signup all resolved `--fig-theme-bg: #ffffff` on `<html>` without a `data-theme` attribute. The stylesheet declares a complete `:root[data-theme="dark"]` re-declaration of the `--fig-theme-*` roles (fg/bg invert, the primary button becomes a white pill, the alpha washes switch to white-on-black), but no public page carried the attribute while captured: the `dark` token set resolves declarations the site ships but did not paint. The one black-painted surface on the light pages is the footer, measured as a component, not a dark theme.

### Fonts

- **figmaSans** (a variable face — the declared axes run wght 400/600/700, wdth 96/98/100, slnt -6) carries every heading, control and body on the marketing site, self-hosted under /_netlify/_next/static/media with an Arial-metric fallback; **figmaMono** draws code and numeric styling. The style guide falls back to system sans.

### Screenshots

- The product demos, video frames, community thumbnails and photography in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, plan prices, job titles, plugin names and community author names are the product's content; only frames and components were measured.
