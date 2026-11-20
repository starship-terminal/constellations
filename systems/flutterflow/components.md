# FlutterFlow components

The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from flutterflow.io on 2026-11-15, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or sent — the composer's sample text was deleted and the send, sign-in and form submit controls were measured but never activated.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (74 components, 180 states). The page layouts are described in [raw/layout.json](raw/layout.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/24 510, #1a1a1a`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- The site ships two generations of its marketing skin: home's `.composer`/`.pbtn`/`.pg-*` modules and the `ff-*` layer every other page carries. The Home (earlier skin) group holds the first; the rest is ff-*.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (158 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`; the dark set is `{page}-dark-dark-{state}.png` (the page key carries `-dark`, the theme slot `dark`). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home. The AI prompt hero (the earlier skin), product demo modules, customer proof, the closing band and footer; the composer focused and the Product menu open. | `/` | [dark-default](screenshots/home-dark-dark-default.png), [dark-full](screenshots/home-dark-dark-full.png), [dark-nav-product-open](screenshots/home-dark-dark-nav-product-open.png), [composer-focused](screenshots/home-light-composer-focused.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [nav-product-open](screenshots/home-light-nav-product-open.png) |
| Product. Feature tabs (the Backend tab selected through its own control), editor walkthrough modules and an FAQ. | `/product` | [dark-default](screenshots/product-dark-dark-default.png), [default](screenshots/product-light-default.png), [full](screenshots/product-light-full.png), [tab-selected](screenshots/product-light-tab-selected.png) |
| Pricing. The Monthly/Yearly segmented control (Yearly selected), plan cards and CTAs, the FAQ accordion (its first item ships open; the saved shot shows the list toggled shut). | `/pricing` | [dark-default](screenshots/pricing-dark-dark-default.png), [dark-full](screenshots/pricing-dark-dark-full.png), [billing-yearly](screenshots/pricing-light-billing-yearly.png), [default](screenshots/pricing-light-default.png), [faq-closed](screenshots/pricing-light-faq-closed.png), [full](screenshots/pricing-light-full.png) |
| Enterprise. The Talk-to-sales contact form (a field focused; nothing sent) and the customer cells. | `/enterprise` | [dark-default](screenshots/enterprise-dark-dark-default.png), [default](screenshots/enterprise-light-default.png), [field-focused](screenshots/enterprise-light-field-focused.png), [form](screenshots/enterprise-light-form.png), [full](screenshots/enterprise-light-full.png) |
| FlutterFlow AI. The AI product page. | `/ai` | [default](screenshots/ai-light-default.png), [full](screenshots/ai-light-full.png) |
| FlutterFlow Studio. The agency arm's hero, tags and offering sections. | `/studio` | [default](screenshots/studio-light-default.png), [full](screenshots/studio-light-full.png) |
| Studio showcase. The developer work gallery's cards. | `/studio/showcase` | [default](screenshots/studio-showcase-light-default.png), [full](screenshots/studio-showcase-light-full.png) |
| Studio FAQ. The accordion; its first item ships open, and the saved shot shows it toggled shut. | `/studio/faq` | [default](screenshots/studio-faq-light-default.png), [faq-closed](screenshots/studio-faq-light-faq-closed.png), [full](screenshots/studio-faq-light-full.png) |
| Apply to be a developer. The Studio application page (the form read, never submitted). | `/studio/apply-to-be-a-developer` | [default](screenshots/studio-apply-light-default.png), [full](screenshots/studio-apply-light-full.png) |
| Customer stories. | `/customer-stories` | [default](screenshots/customer-stories-light-default.png), [full](screenshots/customer-stories-light-full.png) |
| Blog index. | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Changelog. | `/changelog` | [default](screenshots/changelog-light-default.png), [full](screenshots/changelog-light-full.png) |
| About us. | `/about-us` | [default](screenshots/about-us-light-default.png), [full](screenshots/about-us-light-full.png) |
| Contact us. | `/contact-us` | [default](screenshots/contact-us-light-default.png), [full](screenshots/contact-us-light-full.png) |
| FlutterFlow vs. Studio comparison. | `/flutterflow-vs-studio` | [default](screenshots/vs-studio-light-default.png), [full](screenshots/vs-studio-light-full.png) |
| FlutterFlow developer groups. | `/flutterflow-developer-groups` | [default](screenshots/dev-groups-light-default.png), [full](screenshots/dev-groups-light-full.png) |
| Student ambassadors. | `/student-ambassadors` | [default](screenshots/student-ambassadors-light-default.png), [full](screenshots/student-ambassadors-light-full.png) |
| Home in the dark theme (the footer switch's Dark pick): the nav menu open. | `/` | [default](screenshots/home-dark-dark-default.png), [full](screenshots/home-dark-dark-full.png), [nav-product-open](screenshots/home-dark-dark-nav-product-open.png) |
| Product, dark. | `/product` | [default](screenshots/product-dark-dark-default.png) |
| Pricing, dark. | `/pricing` | [default](screenshots/pricing-dark-dark-default.png), [full](screenshots/pricing-dark-dark-full.png) |
| Enterprise, dark. | `/enterprise` | [default](screenshots/enterprise-dark-dark-default.png) |
| Home at 390: the collapsed bar and the full-screen menu sheet opened. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Pricing at 390. | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Product dropdown | the top nav, every page | the nav's own Product button; closed with Escape | [home-light-nav-product-open](screenshots/home-light-nav-product-open.png), [nav-panel](#nav-panel) |
| Composer, focused | home hero | clicked into the field; sample text typed and deleted, nothing sent | [home-light-composer-focused](screenshots/home-light-composer-focused.png) |
| Billing: Yearly | pricing | the Monthly/Yearly segmented control's own Yearly option | [pricing-light-billing-yearly](screenshots/pricing-light-billing-yearly.png) |
| FAQ accordion, open and closed | pricing and Studio FAQ | the accordion's own summary; the first item ships open on both pages, so the saved shots show the same list toggled shut | [pricing-light-faq-closed](screenshots/pricing-light-faq-closed.png), [studio-faq-light-faq-closed](screenshots/studio-faq-light-faq-closed.png), [accordion-item](#accordion-item) |
| Contact form, field focused | enterprise | clicked into the first name field; nothing typed or sent | [enterprise-light-form](screenshots/enterprise-light-form.png), [enterprise-light-field-focused](screenshots/enterprise-light-field-focused.png) |
| Feature tab selected | product | the Backend tab's own control | [product-light-tab-selected](screenshots/product-light-tab-selected.png) |
| Mobile menu sheet | home at 390 | the Open menu icon button; closed with its own Close menu button | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-dialog](#m-menu-dialog) |
| Dark theme | home, product, pricing, enterprise | the footer theme switch set to Dark (data-theme=dark), restored to Light after | [home-dark-dark-default](screenshots/home-dark-dark-default.png), [pricing-dark-dark-full](screenshots/pricing-dark-dark-full.png) |
| Cookie consent banner | every page, on load | the privacy-choices dialog (a CookieScript embed) is closed by the kit's closePromo before each capture; it is a vendor widget, not part of the design layer | (dismissed, not kept as a design surface) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 22 components were given a real keyboard focus. 20 draw a ring: `banner-dismiss` (2px solid #1a1a1a `color.ink`, offset 2px), `nav-menu-button` (2px solid #1a1a1a `color.ink`, offset 2px), `nav-link` (2px solid #1a1a1a `color.ink`, offset 2px), `nav-signin` (2px solid #1a1a1a `color.ink`, offset 2px), `billing-seg-option` (2px solid #1a1a1a `color.ink`, offset 2px), `plan-cta` (2px solid #1a1a1a `color.ink`, offset 2px), `plan-cta-primary` (2px solid #1a1a1a `color.ink`, offset 2px), `ff-composer-go` (2px solid #1a1a1a `color.ink`, offset 2px), `ff-composer-key` (2px solid #1a1a1a `color.ink`, offset 2px), `footer-link` (2px solid #1a1a1a `color.ink`, offset 3px), `theme-switch-pick` (2px solid #1a1a1a `color.ink`, offset 3px), `submit` (2px solid #1a1a1a `color.ink`, offset 2px), `tab-selected` (2px solid #1a1a1a `color.ink`, offset -2px), `tab` (2px solid #1a1a1a `color.ink`, offset -2px), `replay-btn` (2px solid #1a1a1a `color.ink`, offset 2px), `composer-go` (2px solid #0a68e0 `color.accent`, offset 2px), `btn-contrast` (2px solid #0a68e0 `color.accent`, offset 2px), `btn-quiet` (2px solid #0a68e0 `color.accent`, offset 2px), `m-open-menu` (2px solid #1a1a1a `color.ink`, offset 2px), `m-menu-close` (2px solid #1a1a1a `color.ink`, offset 2px). 2 paint their focus instead of drawing an outline — a 4px ink-6% box-shadow ring over a darker border on `select`, `select-trigger`. The other 0 show a keyboard user no change: . The ring is `--ff-focus-width` 2px solid `--ff-color-focus` at `--ff-focus-offset` 2px — near-black on the ff-* layer's controls, the accent blue `#0a68e0` on the home skin's buttons and the composer's send.
Focus could not be captured on 5: keyboard focus never reached them (or they took focus without matching :focus-visible), so their focus look is unknown, not absent: `btn-primary-sm`, `link-go`, `composer-nav`, `composer-key`, `replay-btn-home`.

**Pressed.** FlutterFlow's buttons shrink when pressed instead of changing colour: the pill CTAs scale to about 0.94-0.97 (`transform: scale()` at a forced :active). The segmented options and quiet buttons do the same; colour changes on press are minimal.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.12s | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | background-color, border-color, box-shadow, color, transform | banner-dismiss, billing-seg-option, btn-contrast, btn-primary-sm, btn-quiet, composer-go, ff-composer-go, m-btn-primary and more |
| 0.15s | `ease` | background, background-color, box-shadow, color | composer-nav, replay-btn, replay-btn-home |
| 0.2s | `ease` | opacity | replay-btn, replay-btn-home |
| 0.24s | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | box-shadow, opacity, transform | header, m-nav, nav-panel, skip-link |
| 0.24s | `ease` | visibility | nav-panel |
| 0.32s | `cubic-bezier(0.2, 0.8, 0.2, 1)` | height | composer-field, ff-composer-field |

**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).

| Page | 1440 | 1920 | 1024 | 390 |
|---|---|---|---|---|
| home | content x 0, 1440 wide; grid 448 448 448 gap normal on ol | content x 0, 1920 wide; grid 448 448 448 gap normal on ol | content x 0, 1024 wide; grid 314.0 314.0 314.0 gap normal on ol | content x 0, 390 wide; grid 294 294 294 294 gap 12px on div |
| product | content x 0, 1440 wide; grid 440 904 gap normal on section.ff-split.ff-block.ff-tbs | content x 0, 1920 wide; grid 440 904 gap normal on section.ff-split.ff-block.ff-tbs | content x 0, 1024 wide; grid 440 502.0 gap normal on section.ff-split.ff-block.ff-tbs | content x 0, 390 wide; grid 28 190 302 40 gap 16px on div.ff-sj-row |
| pricing | content x 0, 1440 wide; grid 336 336 336 336 gap normal on ul.ff-plg.ff-plg-reg | content x 0, 1920 wide; grid 336 336 336 336 gap normal on ul.ff-plg.ff-plg-reg | content x 0, 1024 wide; grid 235.5 235.5 235.5 235.5 gap normal on ul.ff-plg.ff-plg-reg | content x 0, 390 wide |
| studio | content x 0, 1440 wide; grid 440 904 gap normal on section.ff-split.ff-block.ff-stg | content x 0, 1920 wide; grid 440 904 gap normal on section.ff-split.ff-block.ff-stg | content x 0, 1024 wide; grid 440 502.0 gap normal on section.ff-split.ff-block.ff-stg | content x 0, 390 wide; grid 294 294 294 gap 12px on div.ff-prf-qw-row |
| studio-showcase | content x 0, 1440 wide; grid 303.6 303.6 303.6 303.6 gap 43.2px on section.ff-block.ff-lst-aw-wall | content x 0, 1920 wide; grid 300 300 300 300 gap 48px on section.ff-block.ff-lst-aw-wall | content x 0, 1024 wide; grid 212.4 212.4 212.4 212.4 gap 30.72px on section.ff-block.ff-lst-aw-wall | content x 0, 390 wide; grid 167 167 gap 16px on section.ff-block.ff-lst-aw-wall |
| studio-faq | content x 0, 1440 wide; grid 200 1096 gap 48px on section.ff-rgp-g | content x 0, 1920 wide; grid 200 1096 gap 48px on section.ff-rgp-g | content x 0, 1024 wide; grid 200 694.0 gap 48px on section.ff-rgp-g | content x 0, 390 wide |
| vs-studio | content x 0, 1440 wide; grid 111 1112 89 gap 16px on div.ff-pch-axis | content x 0, 1920 wide; grid 111 1112 89 gap 16px on div.ff-pch-axis | content x 0, 1024 wide; grid 111 710.0 89 gap 16px on div.ff-pch-axis | content x 0, 390 wide; grid 102 145 83 gap 10px on div.ff-pch-axis |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 336 x 581.25 | - | - | transparent | none | 32px |
| [Showcase card](#showcase-card) | 303.61 x 624.52 | - | - | transparent | none | 0 |
| [Generated app card](#app-card) | 318 x 518 | - | - | transparent | none | 0 |
| [Nav dropdown panel](#nav-panel) | 248 x 236 | - | 16px | #ffffff `color.card` | rgba(0, 0, 0, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 24px 48px -20px | 8px |
| [Custom select listbox](#select-popup) | 410 x 308 | - | 20px | #ffffff `color.card` | rgba(0, 0, 0, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 24px 48px -20px | 0 |
| [FAQ accordion item](#accordion-item) | 840 x 150 | B: 1px solid rgba(0, 0, 0, 0.08) `color.line` | - | transparent | none | 0 |
| [Contact form](#contact-form) | 904 x 952 | - | - | transparent | none | 64px 0px 64px 64px |
| [Mobile menu sheet](#m-menu-dialog) | 390 x 844 | - | - | #fcfcfb `color.page` | none | 0 |

## Components

### Shell and navigation

The chrome every public page carries: the skip link, the 64px announcement + nav bar (56px at 390), the Product dropdown panel and its sign-in row. Sign in and Start building were read, never followed.

<a id="skip-link"></a>
#### Skip to content link
The first tab stop on every page: a visually-hidden link that paints when focused. Read as `skip-link` on the pricing page.

**Values (default).** size 152 x 44; padding 0px 22px; radius 999px; background #1a1a1a `color.ink`; text Inter 15/23.25 510, #ffffff `color.card`; transition transform 0.24s cubic-bezier(0.25, 0.46, 0.45, 0.94); transform translate(0px, -68px).

![Skip to content link default](components/crops/skip-link-default.png)

<a id="announcement"></a>
#### Announcement banner
The slim bar above the header ("FlutterFlow for Web is here"): the accent line colour, a "What's changing" link and a Dismiss icon button. Shown, never dismissed. Read as `announcement` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1440 x 40; padding 8px 48px; background #f5f5f5 `color.well`; shadow rgba(0, 0, 0, 0.08) 0px -0.5px 0px 0px inset; text Inter 13/20 400, #3d3d3d `color.ink-2`; icon 15 x 15, #6b6b6b `color.muted` |
| dark | background #0b0b0b; shadow rgba(255, 255, 255, 0.08) 0px -0.5px 0px 0px inset; text Inter 13/20 400, #c8c8c8; icon 15 x 15, #a0a0a0 |

![Announcement banner default](components/crops/announcement-default.png) ![Announcement banner dark](components/crops/announcement-dark.png)

<a id="banner-dismiss"></a>
#### Banner dismiss button
The small square icon button that closes the announcement bar. Measured, never pressed. Read as `banner-dismiss` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 28 x 28; radius 50%; background transparent; text Inter 13/20 400, #6b6b6b `color.muted`; transition background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 15 x 15, #6b6b6b `color.muted` |
| hover | background rgba(26, 26, 26, 0.06); text Inter 13/20 400, #1a1a1a `color.ink`; icon 15 x 15, #1a1a1a `color.ink` |
| focus-visible | outline 2px solid #1a1a1a `color.ink`, offset 2px |
| pressed | background rgba(26, 26, 26, 0.06); text Inter 13/20 400, #1a1a1a `color.ink`; icon 15 x 15, #1a1a1a `color.ink` |

![Banner dismiss button default](components/crops/banner-dismiss-default.png) ![Banner dismiss button hover](components/crops/banner-dismiss-hover.png) ![Banner dismiss button focus-visible](components/crops/banner-dismiss-focus-visible.png) ![Banner dismiss button pressed](components/crops/banner-dismiss-pressed.png)

<a id="header"></a>
#### Top nav
The floating bar over every page: brand lockup, the Product/Studio/Resources menu buttons, Pricing and Enterprise links, Sign in and the Start building pill. Read as `header` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1440 x 64; background rgba(252, 252, 251, 0.86); text Inter 14/21.7 400, #6b6b6b `color.muted`; transition box-shadow 0.24s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 101.95 x 14.44, #1a1a1a `color.ink` |
| dark | background rgba(18, 18, 18, 0.86); text Inter 14/21.7 400, #a0a0a0; icon 101.95 x 14.44, #ededed |

![Top nav default](components/crops/header-default.png) ![Top nav dark](components/crops/header-dark.png)

<a id="nav-menu-button"></a>
#### Nav menu button
A top-level menu trigger (Product): 14px nav text with a chevron; opens the snav panel. Read as `nav-menu-button` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 92 x 37.69; padding 8px 10px 8px 12px; radius 999px; background transparent; text Inter 14/21.7 400, #6b6b6b `color.muted`; transition color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 14 x 14, #6b6b6b `color.muted` |
| hover | text Inter 14/21.7 400, #1a1a1a `color.ink`; icon 14 x 14, #1a1a1a `color.ink` |
| focus-visible | outline 2px solid #1a1a1a `color.ink`, offset 2px |
| pressed | text Inter 14/21.7 400, #1a1a1a `color.ink`; icon 14 x 14, #1a1a1a `color.ink` |
| dark | text Inter 14/21.7 400, #a0a0a0; icon 14 x 14, #a0a0a0 |

![Nav menu button default](components/crops/nav-menu-button-default.png) ![Nav menu button hover](components/crops/nav-menu-button-hover.png) ![Nav menu button focus-visible](components/crops/nav-menu-button-focus-visible.png) ![Nav menu button pressed](components/crops/nav-menu-button-pressed.png) ![Nav menu button dark](components/crops/nav-menu-button-dark.png)

<a id="nav-panel"></a>
#### Nav dropdown panel
The Product flyout: a card-radius floating panel with lead link, column headings and item rows. Read as `nav-panel` on the pricing page.

**Values (default).** size 248 x 236; padding 8px; radius 16px; background #ffffff `color.card`; shadow rgba(0, 0, 0, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 24px 48px -20px; text Inter 12/16 510, #6b6b6b `color.muted`; transition opacity 0.24s cubic-bezier(0.25, 0.46, 0.45, 0.94), visibility 0.24s ease; icon 13 x 13, #6b6b6b `color.muted`.

![Nav dropdown panel default](components/crops/nav-panel-default.png)

<a id="nav-panel-item"></a>
#### Nav dropdown item
Read as `nav-panel-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 216 x 32; padding 0px 8px; radius 10px; background transparent; text Inter 14/21.7 400, #1a1a1a `color.ink` |

![Nav dropdown item default](components/crops/nav-panel-item-default.png) ![Nav dropdown item hover](components/crops/nav-panel-item-hover.png)

<a id="nav-link"></a>
#### Nav link
The plain text links in the bar (Pricing, Enterprise). Read as `nav-link` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 69 x 37.69; padding 8px 12px; radius 999px; background transparent; text Inter 14/21.7 400, #6b6b6b `color.muted`; transition color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| hover | text Inter 14/21.7 400, #1a1a1a `color.ink` |
| focus-visible | outline 2px solid #1a1a1a `color.ink`, offset 2px |
| pressed | text Inter 14/21.7 400, #1a1a1a `color.ink` |
| dark | text Inter 14/21.7 400, #a0a0a0 |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png) ![Nav link dark](components/crops/nav-link-dark.png)

<a id="nav-signin"></a>
#### Sign in link
The secondary text link in the nav end. Measured, never followed. Read as `nav-signin` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 68 x 37.69; padding 8px 12px; radius 999px; background transparent; text Inter 14/21.7 400, #6b6b6b `color.muted`; transition color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| hover | text Inter 14/21.7 400, #1a1a1a `color.ink` |
| focus-visible | outline 2px solid #1a1a1a `color.ink`, offset 2px |
| pressed | text Inter 14/21.7 400, #1a1a1a `color.ink` |

![Sign in link default](components/crops/nav-signin-default.png) ![Sign in link hover](components/crops/nav-signin-hover.png) ![Sign in link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign in link pressed](components/crops/nav-signin-pressed.png)

<a id="btn-primary-sm"></a>
#### Start building (nav, small)
The small contrast pill in the nav: --ff-color-contrast fill, --ff-color-contrast-ink text, radius pill. Measured, never followed. Read as `btn-primary-sm` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 183 x 32; padding 0px 14px; radius 999px; background #1a1a1a `color.ink`; text Inter 13/20.15 510, #ffffff `color.card`; transition transform 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), box-shadow 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| pressed | size 177.51 x 31.04; transform scale(0.97) |
| dark | background #ededed; text Inter 13/20.15 510, #111111 |

![Start building (nav, small) default](components/crops/btn-primary-sm-default.png) ![Start building (nav, small) hover](components/crops/btn-primary-sm-hover.png) ![Start building (nav, small) pressed](components/crops/btn-primary-sm-pressed.png) ![Start building (nav, small) dark](components/crops/btn-primary-sm-dark.png)

<a id="brand"></a>
#### Brand lockup
The FlutterFlow mark + wordmark link; the mark is a filtered image (--ff-theme-logo-filter) so it inverts in dark. Read as `brand` on the pricing page.

**Values (default).** size 139.95 x 30; background transparent; text Inter 20/31 400, #1a1a1a `color.ink`; icon 101.95 x 14.44, #1a1a1a `color.ink`.

![Brand lockup default](components/crops/brand-default.png)

### Pricing

The pricing page's plan grid, the Monthly/Yearly segmented control (Yearly selected through the site's own toggle), the plan CTAs and the FAQ accordion.

<a id="plan-grid"></a>
#### Plan grid
The plans list: a carded grid of plan columns under the billing toggle. Read as `plan-grid` on the pricing page.

**Values (default).** size 1344 x 581.25; radius 16px; background #f5f5f5 `color.well`; shadow rgba(0, 0, 0, 0.08) 0px 0px 0px 0.5px inset; text Inter 16/24 600, #1a1a1a `color.ink`; icon 15 x 15, #6b6b6b `color.muted`.

![Plan grid default](components/crops/plan-grid-default.png)

<a id="plan-card"></a>
#### Plan card
One plan column: name, price, feature rows and its CTA. Read as `plan-card` on the pricing page.

**Values (default).** size 336 x 581.25; padding 32px; background transparent; text Inter 16/24 600, #1a1a1a `color.ink`; icon 15 x 15, #6b6b6b `color.muted`.

Child layers that carry the look: span 7x7 background #4b39ef `color.studio-ink` radius 50%; a 272x44 background #ffffff `color.card` radius 999px shadow rgba(0, 0, 0, 0.08) `color.line` 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px; div 272x103.5 border 1px rgba(0, 0, 0, 0.08) `color.line`.

![Plan card default](components/crops/plan-card-default.png)

<a id="billing-seg"></a>
#### Billing period segmented control
A two-option radiogroup (Monthly/Yearly) with a sliding badge: role=radiogroup, each option a role=radio button; the pill slides via --ff-seg-x/width vars. Read as `billing-seg` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 231 x 38; padding 3px; radius 999px; background transparent; shadow rgba(0, 0, 0, 0.08) 0px 0px 0px 1px inset; text Inter 14/21.7 510, #1a1a1a `color.ink` |
| selected | text Inter 14/21.7 510, #6b6b6b `color.muted` |

![Billing period segmented control default](components/crops/billing-seg-default.png) ![Billing period segmented control selected](components/crops/billing-seg-selected.png)

<a id="billing-seg-option"></a>
#### Segmented control option
Read as `billing-seg-option` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 82 x 32; padding 0px 14px; radius 999px; background transparent; text Inter 14/21.7 510, #6b6b6b `color.muted`; transition color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| hover | text Inter 14/21.7 510, #1a1a1a `color.ink` |
| focus-visible | outline 2px solid #1a1a1a `color.ink`, offset 2px |
| pressed | text Inter 14/21.7 510, #1a1a1a `color.ink` |

![Segmented control option default](components/crops/billing-seg-option-default.png) ![Segmented control option hover](components/crops/billing-seg-option-hover.png) ![Segmented control option focus-visible](components/crops/billing-seg-option-focus-visible.png) ![Segmented control option pressed](components/crops/billing-seg-option-pressed.png)

<a id="plan-cta"></a>
#### Plan CTA (secondary)
The secondary button: --ff-color-card fill with the hairline rule and resting shadow. Measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 272 x 44; padding 0px 22px; radius 999px; background #ffffff `color.card`; shadow rgba(0, 0, 0, 0.08) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px; text Inter 15/23.25 510, #1a1a1a `color.ink`; transition transform 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), box-shadow 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| hover | background #f0f0f0 `color.card-2` |
| focus-visible | outline 2px solid #1a1a1a `color.ink`, offset 2px |
| pressed | size 263.84 x 42.68; background #f0f0f0 `color.card-2`; transform scale(0.97) |
| dark | background #1b1b1b; shadow rgba(255, 255, 255, 0.08) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px; text Inter 15/23.25 510, #ededed |

![Plan CTA (secondary) default](components/crops/plan-cta-default.png) ![Plan CTA (secondary) hover](components/crops/plan-cta-hover.png) ![Plan CTA (secondary) focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA (secondary) pressed](components/crops/plan-cta-pressed.png) ![Plan CTA (secondary) dark](components/crops/plan-cta-dark.png)

<a id="plan-cta-primary"></a>
#### Plan CTA (primary)
A contrast-fill call to action in the plan grid. Measured, never followed. Read as `plan-cta-primary` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 108 x 32; padding 0px 14px; radius 999px; background #1a1a1a `color.ink`; text Inter 13/20.15 510, #ffffff `color.card`; transition transform 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), box-shadow 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| focus-visible | outline 2px solid #1a1a1a `color.ink`, offset 2px |
| pressed | size 104.76 x 31.04; transform scale(0.97) |

![Plan CTA (primary) default](components/crops/plan-cta-primary-default.png) ![Plan CTA (primary) hover](components/crops/plan-cta-primary-hover.png) ![Plan CTA (primary) focus-visible](components/crops/plan-cta-primary-focus-visible.png) ![Plan CTA (primary) pressed](components/crops/plan-cta-primary-pressed.png)

<a id="accordion-item"></a>
#### FAQ accordion item
A details/summary row in the questions list: hairline-separated, a plus/cross marker that turns on open. The first item ships open, so this resting reading is the open look. Read as `accordion-item` on the pricing page.

**Values (default).** size 840 x 150; border B: 1px solid rgba(0, 0, 0, 0.08) `color.line`; background transparent; text Inter 17/26 510, #1a1a1a `color.ink`; icon 21.21 x 21.21, #1a1a1a `color.ink`.

Child layers that carry the look: details 840x150 border 1px rgba(0, 0, 0, 0.08) `color.line`; span 39.6x39.6 background rgba(26, 26, 26, 0.06) radius 50%.

![FAQ accordion item default](components/crops/accordion-item-default.png)

<a id="accordion-closed"></a>
#### FAQ accordion, closed
The same details element measured closed: the first item ships open, and toggling its own summary shut it — the run's original save named this state "open" before the click was understood. Read as `accordion-closed` on the pricing page.

**Values (default).** size 840 x 72; border B: 1px solid rgba(0, 0, 0, 0.08) `color.line`; background transparent; text Inter 17/26 510, #1a1a1a `color.ink`; icon 15 x 15, #1a1a1a `color.ink`.

Child layers that carry the look: details 840x72 border 1px rgba(0, 0, 0, 0.08) `color.line`; span 28x28 background rgba(26, 26, 26, 0.06) radius 50%.

![FAQ accordion, closed default](components/crops/accordion-closed-default.png)

<a id="link-go"></a>
#### Arrow link
The text link with a trailing arrow ("Contact us", question rows): --ff-lnk. Measured, never followed. Read as `link-go` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 174.53 x 26; background transparent; text Inter 15/26 510, #1a1a1a `color.ink`; icon 16.05 x 16.05, #1a1a1a `color.ink` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Prompt composer

FlutterFlow leads with an AI prompt field on the home hero and a slimmer variant on later pages: ghost idea text, idea arrows, a Tab hint chip and the round send button. Sample text was typed and deleted; the composer was never submitted.

<a id="ff-composer"></a>
#### Prompt composer (new skin)
The "What should your app do?" field on inner pages: a rounded field (radius-field) with the prompt textarea, idea nav and the send button. Read as `ff-composer` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 640 x 130; background transparent; text Inter 12/18 500, #1a1a1a `color.ink`; icon 17 x 17, #6b6b6b `color.muted` |
| hover | text Inter 16/24 400, rgba(107, 107, 107, 0.8) |

Child layers that carry the look: div 640x130 background #ffffff `color.card` border 1px rgba(26, 26, 26, 0.12) radius 22px shadow rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px; span 1.5x18.4 background rgba(107, 107, 107, 0.8); button 37x21 background #fcfcfb `color.page` border 1px rgba(0, 0, 0, 0.08) `color.line` radius 6px.

![Prompt composer (new skin) default](components/crops/ff-composer-default.png) ![Prompt composer (new skin) hover](components/crops/ff-composer-hover.png)

<a id="ff-composer-field"></a>
#### Composer field
The single-line prompt textarea. Text was typed and deleted; nothing was sent. Read as `ff-composer-field` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 638 x 128; padding 16px 18px 56px 18px; background transparent; text Inter 16/24 400, #1a1a1a `color.ink`; transition height 0.32s cubic-bezier(0.2, 0.8, 0.2, 1); placeholder transparent |
| focused, filled | radius 6px |

![Composer field default](components/crops/ff-composer-field-default.png) ![Composer field focused](components/crops/ff-composer-field-focused.png) ![Composer field filled](components/crops/ff-composer-field-filled.png)

<a id="ff-composer-go"></a>
#### Composer send button
The round submit arrow (type=submit). Measured, never pressed. Read as `ff-composer-go` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 36 x 36; radius 50%; background rgba(26, 26, 26, 0.08); text Inter 16/24.8 400, rgba(26, 26, 26, 0.4); transition background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 18 x 18, rgba(26, 26, 26, 0.4) |
| focus-visible | outline 2px solid #1a1a1a `color.ink`, offset 2px |
| pressed | size 33.84 x 33.84; transform scale(0.94); icon 16.92 x 16.92, rgba(26, 26, 26, 0.4) |

![Composer send button default](components/crops/ff-composer-go-default.png) ![Composer send button hover](components/crops/ff-composer-go-hover.png) ![Composer send button focus-visible](components/crops/ff-composer-go-focus-visible.png) ![Composer send button pressed](components/crops/ff-composer-go-pressed.png)

<a id="ff-composer-key"></a>
#### Idea key chip
The "Use this idea" suggestion chip inside the composer. Read as `ff-composer-key` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 37 x 21; padding 0px 7px; border T: 1px solid rgba(0, 0, 0, 0.08) `color.line`; R: 1px solid rgba(0, 0, 0, 0.08) `color.line`; B: 2px solid rgba(0, 0, 0, 0.08) `color.line`; L: 1px solid rgba(0, 0, 0, 0.08) `color.line`; radius 6px; background #fcfcfb `color.page`; text Inter 12/18 500, #1a1a1a `color.ink` |
| hover | border T: 1px solid rgba(26, 26, 26, 0.3); R: 1px solid rgba(26, 26, 26, 0.3); B: 2px solid rgba(26, 26, 26, 0.3); L: 1px solid rgba(26, 26, 26, 0.3) |
| focus-visible | outline 2px solid #1a1a1a `color.ink`, offset 2px |
| pressed | border T: 1px solid rgba(26, 26, 26, 0.3); R: 1px solid rgba(26, 26, 26, 0.3); B: 2px solid rgba(26, 26, 26, 0.3); L: 1px solid rgba(26, 26, 26, 0.3) |

![Idea key chip default](components/crops/ff-composer-key-default.png) ![Idea key chip hover](components/crops/ff-composer-key-hover.png) ![Idea key chip focus-visible](components/crops/ff-composer-key-focus-visible.png) ![Idea key chip pressed](components/crops/ff-composer-key-pressed.png)

<a id="composer"></a>
#### Prompt composer (home skin)
The hero prompt field: a large rounded card with the ghost idea text, the Tab hint and the round send button. Read as `composer` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 720 x 130; background transparent; text Inter 16/24 400, rgba(107, 107, 107, 0.8); icon 17 x 17, #6b6b6b `color.muted` |
| dark | text Inter 16/24 400, rgba(160, 160, 160, 0.8); icon 17 x 17, #a0a0a0 |

Child layers that carry the look: div 720x130 background #ffffff `color.card` border 1px rgba(26, 26, 26, 0.12) radius 22px shadow rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px; span 1.5x18.4 background rgba(107, 107, 107, 0.8); button 39x21 background #fcfcfb `color.page` border 1px rgba(0, 0, 0, 0.07) `legacy.edge` radius 6px.

![Prompt composer (home skin) default](components/crops/composer-default.png) ![Prompt composer (home skin) hover](components/crops/composer-hover.png) ![Prompt composer (home skin) dark](components/crops/composer-dark.png)

<a id="composer-field"></a>
#### Composer textarea
The prompt textarea; text was typed and deleted, nothing sent. Read as `composer-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 718 x 128; padding 16px 18px 56px 18px; background transparent; text Inter 16/24 400, #1a1a1a `color.ink`; transition height 0.32s cubic-bezier(0.2, 0.8, 0.2, 1); placeholder transparent |
| focused, filled | radius 6px |

![Composer textarea default](components/crops/composer-field-default.png) ![Composer textarea focused](components/crops/composer-field-focused.png) ![Composer textarea filled](components/crops/composer-field-filled.png)

<a id="composer-ghost"></a>
#### Composer ghost idea
The suggested prompt painted as placeholder ghost text. Read as `composer-ghost` on the home page.

**Values (default).** size 225 x 20; background transparent; text Inter 16/24 400, rgba(107, 107, 107, 0.8).

![Composer ghost idea default](components/crops/composer-ghost-default.png)

<a id="composer-nav"></a>
#### Idea nav button
The previous/next idea arrows in the composer. Read as `composer-nav` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 30 x 30; radius 50%; background transparent; text Inter 16/24.8 400, #6b6b6b `color.muted`; transition background-color 0.15s ease, color 0.15s ease; icon 17 x 17, #6b6b6b `color.muted` |
| hover | background rgba(26, 26, 26, 0.06); text Inter 16/24.8 400, #1a1a1a `color.ink`; icon 17 x 17, #1a1a1a `color.ink` |
| pressed | size 0 x 0; background rgba(26, 26, 26, 0.06); text Inter 16/24.8 400, #1a1a1a `color.ink`; icon none |

![Idea nav button default](components/crops/composer-nav-default.png) ![Idea nav button hover](components/crops/composer-nav-hover.png)

<a id="composer-key"></a>
#### Idea key chip
The "Use this idea" chip under the ghost text (home skin); only painted in the dock composer on this page. Read as `composer-key` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 39 x 21; padding 0px 7px; border T: 1px solid rgba(0, 0, 0, 0.07) `legacy.edge`; R: 1px solid rgba(0, 0, 0, 0.07) `legacy.edge`; B: 2px solid rgba(0, 0, 0, 0.07) `legacy.edge`; L: 1px solid rgba(0, 0, 0, 0.07) `legacy.edge`; radius 6px; background #fcfcfb `color.page`; text Inter 12/18 500, #1a1a1a `color.ink` |
| pressed | size 0 x 0; border T: 1px solid rgba(26, 26, 26, 0.3); R: 1px solid rgba(26, 26, 26, 0.3); B: 2px solid rgba(26, 26, 26, 0.3); L: 1px solid rgba(26, 26, 26, 0.3) |

![Idea key chip default](components/crops/composer-key-default.png)

<a id="composer-go"></a>
#### Send button
The round submit arrow in the composer (type=submit). Measured, never pressed. Read as `composer-go` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 36 x 36; radius 50%; background rgba(26, 26, 26, 0.08); text Inter 16/24.8 400, rgba(26, 26, 26, 0.4); transition background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 18 x 18, rgba(26, 26, 26, 0.4) |
| focus-visible | outline 2px solid #0a68e0 `color.accent`, offset 2px |
| pressed | size 33.84 x 33.84; transform scale(0.94); icon 16.92 x 16.92, rgba(26, 26, 26, 0.4) |

![Send button default](components/crops/composer-go-default.png) ![Send button hover](components/crops/composer-go-hover.png) ![Send button focus-visible](components/crops/composer-go-focus-visible.png) ![Send button pressed](components/crops/composer-go-pressed.png)

### Enterprise contact form

The Talk-to-sales form on /enterprise: labels, pill text fields, a tall textarea, radios, a custom select (opened, never submitted) and the declared-but-unpainted error slot.

<a id="contact-form"></a>
#### Contact form
The enterprise inquiry form: a carded column of labelled fields, topic radios, two custom selects, a textarea and the submit button. Measured and shot; never submitted. Read as `contact-form` on the enterprise page.

**Values (default).** size 904 x 952; padding 64px 0px 64px 64px; background transparent; text Inter 14/20 510, #1a1a1a `color.ink`.

Child layers that carry the look: input 410x44 background #ffffff `color.card` border 1px rgba(26, 26, 26, 0.12) radius 999px shadow rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px; input 410x44 background #ffffff `color.card` border 1px rgba(26, 26, 26, 0.12) radius 999px shadow rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px; input 410x44 background #ffffff `color.card` border 1px rgba(26, 26, 26, 0.12) radius 999px shadow rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px.

![Contact form default](components/crops/contact-form-default.png)

<a id="field"></a>
#### Field wrapper
One form row: label (.ff-fld-l), the control (.ff-fld-i), an optional hint and the alert slot (.ff-fld-e). Read as `field` on the enterprise page.

**Values (default).** size 410 x 72; background transparent; text Inter 14/20 510, #1a1a1a `color.ink`.

Child layers that carry the look: input 410x44 background #ffffff `color.card` border 1px rgba(26, 26, 26, 0.12) radius 999px shadow rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px.

![Field wrapper default](components/crops/field-default.png)

<a id="field-label"></a>
#### Field label
Read as `field-label` on the enterprise page.

**Values (default).** size 410 x 20; background transparent; text Inter 14/20 510, #1a1a1a `color.ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

<a id="text-field"></a>
#### Text field
A .ff-fld-i input: --ff-color-card fill, hairline border, radius-field-tall, --ff-shadow-field; focus paints --ff-shadow-field-focus. Text was typed and deleted; the form was never submitted. Read as `text-field` on the enterprise page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 410 x 44; padding 0px 18px; border 1px solid rgba(26, 26, 26, 0.12); radius 999px; background #ffffff `color.card`; shadow rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px; text Inter 16/24 400, #1a1a1a `color.ink`; transition border-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), box-shadow 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94); placeholder rgba(107, 107, 107, 0.8) |
| focused, filled | border 1px solid rgba(26, 26, 26, 0.4); shadow rgba(26, 26, 26, 0.06) 0px 0px 0px 4px, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px |

![Text field hover](components/crops/text-field-hover.png) ![Text field focused](components/crops/text-field-focused.png) ![Text field filled](components/crops/text-field-filled.png)

<a id="textarea"></a>
#### Text area
Read as `textarea` on the enterprise page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 840 x 122; padding 12px 18px; border 1px solid rgba(26, 26, 26, 0.12); radius 22px; background #ffffff `color.card`; shadow rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px; text Inter 16/24 400, #1a1a1a `color.ink`; transition border-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), box-shadow 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94); placeholder rgba(107, 107, 107, 0.8) |
| focused | border 1px solid rgba(26, 26, 26, 0.4); shadow rgba(26, 26, 26, 0.06) 0px 0px 0px 4px, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px |

![Text area default](components/crops/textarea-default.png) ![Text area focused](components/crops/textarea-focused.png)

<a id="radio"></a>
#### Topic radio
A native radio in the topic list; the checked state is the accent dot. Read as `radio` on the enterprise page.

**Values (default).** size 18 x 18; border 1px solid rgba(26, 26, 26, 0.3); radius 50%; background #ffffff `color.card`; text Arial 13.33/normal 400, #000000 `color.statusbar-ink`; transition background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94); placeholder #000000 `color.statusbar-ink`.

![Topic radio default](components/crops/radio-default.png)

<a id="radio-checked"></a>
#### Topic radio, checked
Read as `radio-checked` on the enterprise page.

**Values (default).** size 18 x 18; border 1px solid #1a1a1a `color.ink`; radius 50%; background #1a1a1a `color.ink`; text Arial 13.33/normal 400, #000000 `color.statusbar-ink`; transition background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94); placeholder #000000 `color.statusbar-ink`.

![Topic radio, checked default](components/crops/radio-checked-default.png)

<a id="select"></a>
#### Select (custom combobox)
A role=combobox button styled as a field (.ff-fld-i.ff-sel-t); opens .ff-sel-p listbox of .ff-sel-o options. The native select behind it is kept at 1x1 off screen. Read as `select` on the enterprise page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 410 x 44; padding 0px 44px 0px 18px; border 1px solid rgba(26, 26, 26, 0.12); radius 999px; background #ffffff `color.card`; image an image (data URI); shadow rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px; text Inter 16/24 400, #6b6b6b `color.muted`; transition border-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), box-shadow 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| focus-visible | border 1px solid rgba(26, 26, 26, 0.4); shadow rgba(26, 26, 26, 0.06) 0px 0px 0px 4px, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px |

![Select (custom combobox) default](components/crops/select-default.png) ![Select (custom combobox) hover](components/crops/select-hover.png) ![Select (custom combobox) focus-visible](components/crops/select-focus-visible.png)

<a id="select-trigger"></a>
#### Custom select trigger
A role=combobox button styled as a field (.ff-fld-i.ff-sel-t); opens .ff-sel-p listbox of .ff-sel-o options. Read as `select-trigger` on the enterprise page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 410 x 44; padding 0px 44px 0px 18px; border 1px solid rgba(26, 26, 26, 0.12); radius 999px; background #ffffff `color.card`; image an image (data URI); shadow rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px; text Inter 16/24 400, #6b6b6b `color.muted`; transition border-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), box-shadow 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| focus-visible | border 1px solid rgba(26, 26, 26, 0.4); shadow rgba(26, 26, 26, 0.06) 0px 0px 0px 4px, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px |

![Custom select trigger default](components/crops/select-trigger-default.png) ![Custom select trigger hover](components/crops/select-trigger-hover.png) ![Custom select trigger focus-visible](components/crops/select-trigger-focus-visible.png) ![Custom select trigger pressed](components/crops/select-trigger-pressed.png)

<a id="select-popup"></a>
#### Custom select listbox
The option popup: role=listbox card with option rows and the floating shadow. Read as `select-popup` on the enterprise page.

**Values (default).** size 410 x 308; radius 20px; background #ffffff `color.card`; shadow rgba(0, 0, 0, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 24px 48px -20px; text Inter 16/24 400, #6b6b6b `color.muted`.

![Custom select listbox default](components/crops/select-popup-default.png)

<a id="select-option"></a>
#### Custom select option
Read as `select-option` on the enterprise page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 410 x 44; padding 10px 18px; background transparent; text Inter 16/24 400, #6b6b6b `color.muted` |

![Custom select option default](components/crops/select-option-default.png) ![Custom select option hover](components/crops/select-option-hover.png)

<a id="field-error"></a>
#### Field error text
The alert slot under a field ("Pick the topic that best fits."): role=alert, --ff-color-danger text. Rendered in the DOM at rest but not painted until validation, so this is the declared style of the slot, not an observed error. Read as `field-error` on the enterprise page.

**Values (default).** size 0 x 0; background transparent; text Inter 13/18 400, #c4320a `color.danger`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

<a id="submit"></a>
#### Submit button
The primary submit ("Submit"). Measured, never pressed — the form was never sent. Read as `submit` on the enterprise page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 94 x 44; padding 0px 22px; radius 999px; background #1a1a1a `color.ink`; text Inter 15/23.25 510, #ffffff `color.card`; transition transform 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), box-shadow 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| focus-visible | outline 2px solid #1a1a1a `color.ink`, offset 2px |
| pressed | size 91.19 x 42.68; transform scale(0.970101) |

![Submit button default](components/crops/submit-default.png) ![Submit button hover](components/crops/submit-hover.png) ![Submit button focus-visible](components/crops/submit-focus-visible.png) ![Submit button pressed](components/crops/submit-pressed.png)

### Tabs and disclosure

The product page's feature tab list (a tab selected through its own control) and the accordions shared by pricing, product and the Studio FAQ.

<a id="tablist"></a>
#### Tab list
A vertical tablist ("Parts of the backend"): role=tab rows over tabpanels; the selected tab is filled. Read as `tablist` on the product page.

**Values (default).** size 376 x 220; border T: 1px solid rgba(0, 0, 0, 0.08) `color.line`; background transparent; text Inter 15/24 510, #1a1a1a `color.ink`; icon 16 x 16, #1a1a1a `color.ink`.

![Tab list default](components/crops/tablist-default.png)

<a id="tab-selected"></a>
#### Tab, selected
The aria-selected tab: filled with the tint wash. Read as `tab-selected` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 376 x 112; background transparent; text Inter 15/24 510, #1a1a1a `color.ink`; transition color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 16 x 16, #1a1a1a `color.ink` |
| focus-visible | radius 8px; outline 2px solid #1a1a1a `color.ink`, offset -2px |

![Tab, selected default](components/crops/tab-selected-default.png) ![Tab, selected hover](components/crops/tab-selected-hover.png) ![Tab, selected focus-visible](components/crops/tab-selected-focus-visible.png)

<a id="tab"></a>
#### Tab
An unselected tab row. The selected state was reached by clicking it (a UI toggle). Read as `tab` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 376 x 52; background transparent; text Inter 15/24 510, #6b6b6b `color.muted`; transition color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 16 x 16, #6b6b6b `color.muted` |
| hover | text Inter 15/24 510, #1a1a1a `color.ink`; icon 16 x 16, #1a1a1a `color.ink` |
| focus-visible | radius 8px; outline 2px solid #1a1a1a `color.ink`, offset -2px |
| pressed | text Inter 15/24 510, #1a1a1a `color.ink`; icon 16 x 16, #1a1a1a `color.ink` |

![Tab hover](components/crops/tab-hover.png) ![Tab focus-visible](components/crops/tab-focus-visible.png) ![Tab pressed](components/crops/tab-pressed.png)

<a id="tab-after-click"></a>
#### Tab after selection
The same tab after the page's own click selected it. Read as `tab-after-click` on the product page.

**Values (default).** size 376 x 112; background transparent; text Inter 15/24 510, #1a1a1a `color.ink`; transition color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 16 x 16, #1a1a1a `color.ink`.

![Tab after selection default](components/crops/tab-after-click-default.png)

<a id="accordion-item-product"></a>
#### FAQ accordion item (product)
Read as `accordion-item-product` on the product page.

**Values (default).** size 840 x 176; border B: 1px solid rgba(0, 0, 0, 0.08) `color.line`; background transparent; text Inter 17/26 510, #1a1a1a `color.ink`; icon 21.21 x 21.21, #1a1a1a `color.ink`.

Child layers that carry the look: details 840x176 border 1px rgba(0, 0, 0, 0.08) `color.line`; span 39.6x39.6 background rgba(26, 26, 26, 0.06) radius 50%.

![FAQ accordion item (product) default](components/crops/accordion-item-product-default.png)

### Content pages

Headings, tag chips, link rows and cards from /studio, /studio/showcase and the feature cells on /enterprise.

<a id="cells-grid"></a>
#### Feature cells grid
The bordered feature grid on the studio/enterprise pages: hairline cells with an icon, a title and a line each. Read as `cells-grid` on the enterprise page.

**Values (default).** size 1344 x 456; radius 16px; background #f5f5f5 `color.well`; shadow rgba(0, 0, 0, 0.08) 0px 0px 0px 0.5px inset; text Inter 18/26 510, #1a1a1a `color.ink`.

![Feature cells grid default](components/crops/cells-grid-default.png)

<a id="studio-hero"></a>
#### Studio page display
Read as `studio-hero` on the studio page.

**Values (default).** size 505.42 x 67.97; background transparent; text Inter 66/67.98 600, #1a1a1a `color.ink`.

![Studio page display default](components/crops/studio-hero-default.png)

<a id="ptag-studio"></a>
#### Studio product tag
The tinted product tag (.ff-ptag-studio): --ff-color-studio-tint ground, --ff-color-studio-ink label. Read as `ptag-studio` on the studio page.

**Values (default).** size 134 x 24; padding 0px 10px 0px 8px; radius 999px; background #ececfd `color.studio-tint`; text Inter 12/16 510, #4b39ef `color.studio-ink`.

![Studio product tag default](components/crops/ptag-studio-default.png)

<a id="cells-item"></a>
#### Feature cell
Read as `cells-item` on the enterprise page.

Not on the page when it was captured.

<a id="showcase-card"></a>
#### Showcase card
A published-app card in the Studio showcase grid. Hovered only; never opened. Read as `showcase-card` on the studio showcase page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 303.61 x 624.52; background transparent; text Inter 12/16 510, #1a1a1a `color.ink`; icon 13 x 13, #1a1a1a `color.ink` |

Child layers that carry the look: div 240x503.2 background #111113 radius 36px shadow #4a4a4f 0px 0px 0px 0.96px inset, #7c7c82 0px 0px 0px 0.72px, rgba(0, 0, 0, 0.45) 0px 24px 48px -28px; span 202x24 background #ffffff `color.card` radius 999px shadow rgba(0, 0, 0, 0.08) `color.line` 0px 0px 0px 0.5px inset.

![Showcase card default](components/crops/showcase-card-default.png) ![Showcase card hover](components/crops/showcase-card-hover.png)

### Home (earlier skin)

The home page still ships the previous generation of the design (the `.composer`/`.pbtn`/`.pg-*` modules and the legacy `--accent`/`--ink` shorthand), measured alongside the ff-* layer the other pages carry.

<a id="replay-btn"></a>
#### Replay button
The small outline "Replay" control on the demo panels (.ff-pbtn-outline). Read as `replay-btn` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 92 x 32; padding 0px 12px; radius 24px; background transparent; shadow #dedede 0px 0px 0px 1px inset; text Inter 14/21.7 500, #1a1a1a `color.ink`; transition background 0.15s ease, box-shadow 0.15s ease, opacity 0.2s ease; icon 16 x 16, #1a1a1a `color.ink` |
| hover | background #bcbcbc; shadow #a3a3a3 0px 0px 0px 1px inset |
| focus-visible | outline 2px solid #1a1a1a `color.ink`, offset 2px |
| pressed | background #bcbcbc; shadow #a3a3a3 0px 0px 0px 1px inset |

![Replay button default](components/crops/replay-btn-default.png) ![Replay button hover](components/crops/replay-btn-hover.png) ![Replay button focus-visible](components/crops/replay-btn-focus-visible.png) ![Replay button pressed](components/crops/replay-btn-pressed.png)

<a id="home-hero"></a>
#### Home hero
The first band: the two-line display headline, the lede, the prompt composer and the check line, over the page ground with its grain texture. Read as `home-hero` on the home page.

**Values (default).** size 1344 x 651.13; padding 115.2px 0px 0px 0px; background transparent; text Inter 14/20 500, #555555 `color.ink-soft`; icon 12.2 x 15, #1a1a1a `color.ink`.

Child layers that carry the look: p 191.1x34 background rgba(255, 255, 255, 0.6) radius 999px shadow rgba(0, 0, 0, 0.08) `color.line` 0px 0px 0px 1px inset; i 1x12 background rgba(26, 26, 26, 0.14); div 720x130 background #ffffff `color.card` border 1px rgba(26, 26, 26, 0.12) radius 22px shadow rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

<a id="home-title"></a>
#### Hero display
"Build an app by describing it" in the --ff-text-display size. Read as `home-title` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 427.05 x 135.94; background transparent; text Inter 66/67.98 600, #1a1a1a `color.ink` |
| dark | text Inter 66/67.98 600, #ededed |

![Hero display default](components/crops/home-title-default.png) ![Hero display dark](components/crops/home-title-dark.png)

<a id="btn-contrast"></a>
#### Contrast button (footer band)
The "Talk to sales" pill in the closing band: the old skin's contrast fill. Read as `btn-contrast` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 135 x 44; padding 0px 22px; radius 999px; background #1a1a1a `color.ink`; text Inter 15/23.25 510, #ffffff `color.card`; transition transform 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), box-shadow 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| focus-visible | outline 2px solid #0a68e0 `color.accent`, offset 2px |
| dark | background #ededed; text Inter 15/23.25 510, #111111 |

![Contrast button (footer band) default](components/crops/btn-contrast-default.png) ![Contrast button (footer band) hover](components/crops/btn-contrast-hover.png) ![Contrast button (footer band) focus-visible](components/crops/btn-contrast-focus-visible.png) ![Contrast button (footer band) pressed](components/crops/btn-contrast-pressed.png) ![Contrast button (footer band) dark](components/crops/btn-contrast-dark.png)

<a id="btn-quiet"></a>
#### Quiet button
The secondary pill next to it. Read as `btn-quiet` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 219 x 44; padding 0px 22px; radius 999px; background #ffffff `color.card`; shadow rgba(0, 0, 0, 0.08) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px; text Inter 15/23.25 510, #1a1a1a `color.ink`; transition transform 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), box-shadow 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| hover | background #f0f0f0 `color.card-2` |
| focus-visible | outline 2px solid #0a68e0 `color.accent`, offset 2px |

![Quiet button default](components/crops/btn-quiet-default.png) ![Quiet button hover](components/crops/btn-quiet-hover.png) ![Quiet button focus-visible](components/crops/btn-quiet-focus-visible.png) ![Quiet button pressed](components/crops/btn-quiet-pressed.png)

<a id="replay-btn-home"></a>
#### Replay button (home skin)
The small outline Replay on the demo modules; never painted at rest on this page, so this is the hidden DOM slot's declared style, not a painted reading. Read as `replay-btn-home` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 0 x 0; padding 0px 12px; radius 24px; background transparent; shadow #dedede 0px 0px 0px 1px inset; text Inter 14/21.7 500, #6b6b6b `color.muted`; transition background 0.15s ease, box-shadow 0.15s ease, opacity 0.2s ease |
| pressed | background #ffffff `color.card`; shadow #a3a3a3 0px 0px 0px 1px inset; text Inter 14/21.7 500, #1a1a1a `color.ink` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

<a id="app-card"></a>
#### Generated app card
A generated-app tile in the demo reel. Read as `app-card` on the home page.

**Values (default).** size 318 x 518; background transparent; text -apple-system 10.39/10.39 600, #000000 `color.statusbar-ink`; icon 11.22 x 7.48, #000000 `color.statusbar-ink`.

Child layers that carry the look: div 318x430 background #f5f5f5 `color.well` radius 16px shadow rgba(0, 0, 0, 0.08) `color.line` 0px 0px 0px 0.5px inset; div 241.7x508.4 background #111113 radius 38.67px shadow #4a4a4f 0px 0px 0px 0.96675px inset, #1c1c1f 0px 0px 0px 2.65856px inset, #7c7c82 0px 0px 0px 0.725062px, rgba(0, 0, 0, 0.45) 0px 24px 60px -30px; div 227.2x493.9 background #f0f0f0 `color.card-2` radius 31.4194px.

![Generated app card default](components/crops/app-card-default.png)

<a id="ptag"></a>
#### Product tag chip
The small platform/product tag (dot + label). Read as `ptag` on the home page.

Not on the page when it was captured.

### Footer

The closing band and the real theme switch (the Light/Dark pick the dark set was captured through).

<a id="footer"></a>
#### Footer
The site foot: brand lockup, link columns, the legal bar, the theme switch and the privacy-choices button. Read as `footer` on the pricing page.

**Values (default).** size 1344 x 868.59; padding 64px 0px 0px 0px; border T: 1px solid rgba(0, 0, 0, 0.08) `color.line`; background transparent; text Inter 13/19.5 400, #6b6b6b `color.muted`; icon 91.69 x 12.98, #1a1a1a `color.ink`.

![Footer default](components/crops/footer-default.png)

<a id="footer-link"></a>
#### Footer link
Read as `footer-link` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 125.88 x 27; background transparent; text Inter 18/27.9 400, #1a1a1a `color.ink`; icon 91.69 x 12.98, #1a1a1a `color.ink` |
| focus-visible | radius 4px; outline 2px solid #1a1a1a `color.ink`, offset 3px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

<a id="theme-switch"></a>
#### Theme switch
The footer Light/Dark/"Match your system" radiogroup (data-ff-tsw; writes ff-theme to localStorage). The dark reading is measured with the switch on Dark. Read as `theme-switch` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 96 x 30; padding 3px; radius 999px; background transparent; shadow rgba(0, 0, 0, 0.08) 0px 0px 0px 1px inset; text Inter 13/20.15 400, #6b6b6b `color.muted`; icon 14 x 14, #6b6b6b `color.muted` |
| dark | shadow rgba(255, 255, 255, 0.08) 0px 0px 0px 1px inset; text Inter 13/20.15 400, #a0a0a0; icon 14 x 14, #a0a0a0 |

![Theme switch default](components/crops/theme-switch-default.png) ![Theme switch dark](components/crops/theme-switch-dark.png)

<a id="theme-switch-pick"></a>
#### Theme switch option
A role=radio button in the switch; the checked one carries aria-checked=true. Read as `theme-switch-pick` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 30 x 24; radius 999px; background transparent; text Inter 13/20.15 400, #6b6b6b `color.muted`; icon 14 x 14, #6b6b6b `color.muted` |
| hover | text Inter 13/20.15 400, #1a1a1a `color.ink`; icon 14 x 14, #1a1a1a `color.ink` |
| focus-visible | radius 4px; outline 2px solid #1a1a1a `color.ink`, offset 3px |
| pressed | text Inter 13/20.15 400, #1a1a1a `color.ink`; icon 14 x 14, #1a1a1a `color.ink` |

![Theme switch option default](components/crops/theme-switch-pick-default.png) ![Theme switch option hover](components/crops/theme-switch-pick-hover.png) ![Theme switch option focus-visible](components/crops/theme-switch-pick-focus-visible.png) ![Theme switch option pressed](components/crops/theme-switch-pick-pressed.png)

<a id="cookie-button"></a>
#### Privacy choices button
The "Your Privacy Choices" footer button (hidden outside banner regions). Measured at rest. Read as `cookie-button` on the pricing page.

**Values (default).** size 0 x 0; background transparent; text Inter 13/20.15 400, #6b6b6b `color.muted`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

<a id="theme-switch-home"></a>
#### Theme switch (home skin)
Read as `theme-switch-home` on the home page.

**Values (default).** size 96 x 30; padding 3px; radius 999px; background transparent; shadow #e7e7e5 0px 0px 0px 1px inset; text Inter 13/20.15 400, #6b6b6b `color.muted`; icon 14 x 14, #6b6b6b `color.muted`.

![Theme switch (home skin) default](components/crops/theme-switch-home-default.png)

### Mobile (390 wide)

A few components as a phone draws them, at 390 x 844 with a mobile user agent: the collapsed bar and the full-screen menu sheet.

<a id="m-nav"></a>
#### Top nav (390)
The 390-wide bar: brand, the Open menu icon button. Read as `m-nav` on the home page at 390 wide.

**Values (default).** size 390 x 56; background rgba(252, 252, 251, 0.86); text Inter 13/20.15 510, #ffffff `color.card`; transition box-shadow 0.24s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 91.69 x 12.98, #1a1a1a `color.ink`.

![Top nav (390) default](components/crops/m-nav-default.png)

<a id="m-open-menu"></a>
#### Open menu button
Read as `m-open-menu` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 36 x 36; radius 50%; background transparent; text Inter 16/24.8 400, #6b6b6b `color.muted`; transition background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 18 x 18, #6b6b6b `color.muted` |
| focus-visible | outline 2px solid #1a1a1a `color.ink`, offset 2px |

![Open menu button default](components/crops/m-open-menu-default.png) ![Open menu button hover](components/crops/m-open-menu-hover.png) ![Open menu button focus-visible](components/crops/m-open-menu-focus-visible.png) ![Open menu button pressed](components/crops/m-open-menu-pressed.png)

<a id="m-menu-close"></a>
#### Close menu button
Read as `m-menu-close` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 36 x 36; radius 50%; background transparent; text Inter 16/24.8 400, #6b6b6b `color.muted`; transition background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 18 x 18, #6b6b6b `color.muted` |
| focus-visible | outline 2px solid #1a1a1a `color.ink`, offset 2px |

![Close menu button default](components/crops/m-menu-close-default.png) ![Close menu button hover](components/crops/m-menu-close-hover.png) ![Close menu button focus-visible](components/crops/m-menu-close-focus-visible.png) ![Close menu button pressed](components/crops/m-menu-close-pressed.png)

<a id="m-composer"></a>
#### Composer (390)
Read as `m-composer` on the home page at 390 wide.

**Values (default).** size 350 x 170; background transparent; text Inter 16/24 400, rgba(107, 107, 107, 0.8); icon 17 x 17, #6b6b6b `color.muted`.

Child layers that carry the look: div 350x170 background #ffffff `color.card` border 1px rgba(26, 26, 26, 0.12) radius 22px shadow rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.14) 0px 8px 24px -14px; span 1.5x18.4 background rgba(107, 107, 107, 0.8); button 50x21 background #fcfcfb `color.page` border 1px rgba(0, 0, 0, 0.07) `legacy.edge` radius 6px.

![Composer (390) default](components/crops/m-composer-default.png)

<a id="m-btn-primary"></a>
#### Primary button (390)
Read as `m-btn-primary` on the home page at 390 wide.

**Values (default).** size 0 x 0; padding 0px 12px; radius 999px; background #1a1a1a `color.ink`; text Inter 13/20.15 510, #ffffff `color.card`; transition transform 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), background-color 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94), box-shadow 0.12s cubic-bezier(0.25, 0.46, 0.45, 0.94).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

<a id="m-hero-title"></a>
#### Hero display (390)
Read as `m-hero-title` on the home page at 390 wide.

**Values (default).** size 265.48 x 88.19; background transparent; text Inter 42/44.1 600, #1a1a1a `color.ink`.

![Hero display (390) default](components/crops/m-hero-title-default.png)

### Dialogs and overlays

Overlays and transient surfaces opened through the pages' own controls.

<a id="m-menu-dialog"></a>
#### Mobile menu sheet
The full-screen dialog.ff-snav-ms opened by the menu button: nav links, the lead card and the sign-in row. Read as `m-menu-dialog` on the home page.

**Values (default).** size 390 x 844; background #fcfcfb `color.page`; text Inter 22/28 510, #1a1a1a `color.ink`; icon 91.69 x 12.98, #1a1a1a `color.ink`.

![Mobile menu sheet default](components/crops/m-menu-dialog-default.png)

## Icons

109 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Logos inside customer marks and the product-shot artwork were left out; these are the interface icons. The SVGs are FlutterFlow's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [dark](icons/dark.svg) | 14x14 | 0 0 24 24 | stroke | home; product; pricing; enterprise; ai; studio; studio-showcase; studio-faq; customer-stories; blog; changelog; about-us; contact-us; vs-studio; nav; home-dark | Dark |
| [light](icons/light.svg) | 14x14 | 0 0 24 24 | stroke | home; product; pricing; enterprise; ai; studio; studio-showcase; studio-faq; customer-stories; blog; changelog; about-us; contact-us; vs-studio; nav; home-dark | Light |
| [match-your-system](icons/match-your-system.svg) | 14x14 | 0 0 24 24 | stroke | home; product; pricing; enterprise; ai; studio; studio-showcase; studio-faq; customer-stories; blog; changelog; about-us; contact-us; vs-studio; nav; home-dark | Match your system |
| [product](icons/product.svg) | 14x14 | 0 0 24 24 | stroke | home; product; pricing; enterprise; ai; studio; studio-showcase; studio-faq; customer-stories; blog; changelog; about-us; contact-us; vs-studio; nav; home-dark | Product / Studio / Resources |
| [icon-de1b34cf](icons/icon-de1b34cf.svg) | 11x11 | 0 0 24 24 | stroke | product; pricing; enterprise; ai; studio; studio-showcase; studio-faq; customer-stories; blog; changelog; about-us; contact-us; vs-studio | Docs (opens in a new tab) / Templates (opens in a new tab) / |
| [dismiss](icons/dismiss.svg) | 15x15 | 0 0 24 24 | stroke | product; pricing; enterprise; ai; studio; studio-showcase; customer-stories; blog; changelog; about-us; contact-us; vs-studio | Dismiss |
| [iphone](icons/iphone.svg) | 12x15 | 0 0 814 1000 | fill | home; product; ai; nav; home-dark | iPhone |
| [contact-us](icons/contact-us.svg) | 16x16 | 0 0 24 24 | stroke | product; pricing; ai; studio; studio-faq; vs-studio | Contact us / FlutterFlow or Studio? / All of Studio’s AI too |
| [previous-idea](icons/previous-idea-2502261d.svg) | 17x17 | 0 0 24 24 | stroke | home; nav; home-dark | Previous idea |
| [icon-3141b6a8](icons/icon-3141b6a8.svg) | 15x15 | 0 0 24 24 | stroke | home; nav; home-dark | One build for the App Store and Google P / Backend built in  |
| [next-idea](icons/next-idea-3f2d41a6.svg) | 13x13 17x17 | 0 0 24 24 | stroke | home; nav; home-dark | Next idea |
| [icon-40febefc](icons/icon-40febefc.svg) | 28x28 | 0 0 800 800 | fill | home; nav; home-dark |  |
| [icon-4776fd47](icons/icon-4776fd47.svg) | 14x14 | 0 0 24 24 | stroke | home; nav; home-dark |  |
| [icon-49057930](icons/icon-49057930.svg) | 18x18 | 0 0 24 24 | stroke | home; nav; home-dark | Branching and review Work in parallel, r |
| [tender-home](icons/tender-home.svg) | 19x19 20x20 22x22 | 0 0 20 20 | fill | home; nav; home-dark | Tender Home / Tender 1.1 |
| [icon-4eb89e62](icons/icon-4eb89e62.svg) | 18x18 | 0 0 24 24 | stroke | home; nav; home-dark | Enterprise-grade SSO, audit logs, privat |
| [icon-4f7c8c15](icons/icon-4f7c8c15.svg) | 16x16 | 0 0 24 24 | stroke | home; nav; home-dark | Real users 131 users signed up to the pu |
| [send-to-stores](icons/send-to-stores.svg) | 17x17 | 0 0 24 24 | stroke | home; nav; home-dark | Send to stores |
| [icon-6e3baa5b](icons/icon-6e3baa5b.svg) | 14x14 | 0 0 24 24 | stroke | home; nav; home-dark |  |
| [icon-6fd82807](icons/icon-6fd82807.svg) | 15x15 21x21 | 0 0 24 24 | stroke | product; pricing; ai; studio; studio-faq |  |
| [icon-77a8eed9](icons/icon-77a8eed9.svg) | 16x16 | 0 0 28.99 31.99 | fill | home; nav; home-dark |  |
| [home](icons/home.svg) | 12x12 | 0 0 24 24 | stroke | home; nav; home-dark | Home |
| [icon-87f993d8](icons/icon-87f993d8.svg) | 16x16 | 0 0 48 48 | fill | home; nav; home-dark | Google People continue with their Google |
| [start-building](icons/start-building-944376a0.svg) | 15x15 16x16 17x17 18x18 | 0 0 24 24 | stroke | home; nav; home-dark | Start building |
| [icon-aa82496a](icons/icon-aa82496a.svg) | 20x20 | 0 0 24 24 | stroke | home; nav; home-dark | Email and password Minimum password leng / Google People con |
| [icon-ad026c53](icons/icon-ad026c53.svg) | 18x18 | 0 0 24 24 | stroke | home; nav; home-dark | Shared libraries Components, themes, and |
| [transactions](icons/transactions.svg) | 16x16 | 0 0 24 24 | stroke | home; nav; home-dark | Transactions / Transactions Real data |
| [icon-bd7d1832](icons/icon-bd7d1832.svg) | 18x18 | 0 0 24 24 | stroke | home; nav; home-dark | Custom code and export Drop in Dart wher |
| [icon-c7e3a141](icons/icon-c7e3a141.svg) | 14x14 | 0 0 24 24 | stroke | home; nav; home-dark |  |
| [icon-d3422bfd](icons/icon-d3422bfd.svg) | 15x15 | 0 0 24 24 | stroke | home; nav; home-dark |  |
| [icon-d7a15678](icons/icon-d7a15678.svg) | 14x14 | 0 0 24 24 | stroke | home; nav; home-dark |  |
| [icon-d92e02e1](icons/icon-d92e02e1.svg) | 16x16 | 0 0 24 24 | fill | home; nav; home-dark | Apple People continue with their Apple I |
| [icon-d9bff4f3](icons/icon-d9bff4f3.svg) | 14x14 | 0 0 24 24 | stroke | home; nav; home-dark |  |
| [transactions-real-data](icons/transactions-real-data.svg) | 16x16 | 0 0 24 24 | stroke | home; nav; home-dark | Transactions Real data |
| [icon-df853deb](icons/icon-df853deb.svg) | 16x16 | 0 0 24 24 | stroke | home; nav; home-dark | Email and password Minimum password leng |
| [icon-e8778eda](icons/icon-e8778eda.svg) | 12x12 | 0 0 24 24 | stroke | home; nav; home-dark |  |
| [icon-ba946ac6](icons/icon-ba946ac6.svg) | 16x16 | 0 0 24 24 | stroke | pricing; studio; studio-faq | All integrations (opens in a new tab) |
| [icon-412b113a](icons/icon-412b113a.svg) | 13x13 17x17 | 0 0 24 24 | stroke | nav | Docs (opens in a new tab) / Trainings (opens in a new tab) / |
| [icon-5c19756e](icons/icon-5c19756e.svg) | 16x16 | 0 0 24 24 | stroke | product; ai | Data Edit records right in Backend. Savi / Every table / A c |
| [app-flutterflow-io](icons/app-flutterflow-io.svg) | 11x11 | 0 0 24 24 | stroke | studio; vs-studio | app.flutterflow.io / FlutterFlow Studio Use Studio if you wa |
| [icon-80e0ed02](icons/icon-80e0ed02.svg) | 14x14 | 0 0 24 24 | stroke | studio-faq; about-us | Ask the community (opens in a new tab) / View our launch vid |
| [open-on-the-stage](icons/open-on-the-stage.svg) | 14x14 | 0 0 24 24 | stroke | product | Open on the stage |
| [open-menu](icons/open-menu.svg) | 18x18 | 0 0 24 24 | stroke | nav | Open menu |
| [replay](icons/replay-0a77aaf7.svg) | 16x16 | 0 0 24 24 | stroke | product | Replay |
| [icon-0ab86f2e](icons/icon-0ab86f2e.svg) | 18x18 | 0 0 24 24 | stroke | product |  |
| [included](icons/included.svg) | 16x16 | 0 0 24 24 | stroke | pricing | Included |
| [icon-15326818](icons/icon-15326818.svg) | 15x16 | 0 0 28.99 31.99 | fill | product |  |
| [icon-1a3f209e](icons/icon-1a3f209e.svg) | 16x16 | 0 0 24 24 | stroke | product |  |
| [icon-1bc869f4](icons/icon-1bc869f4.svg) | 14x14 | 0 0 24 24 | stroke | product |  |
| [icon-1d1188c6](icons/icon-1d1188c6.svg) | 18x18 | 0 0 24 24 | stroke | product |  |
| [icon-1d245e70](icons/icon-1d245e70.svg) | 18x18 | 0 0 24 24 | stroke | contact-us | Enterprise If you’re interested in discu |
| [previous-idea](icons/previous-idea-1d473cff.svg) | 17x17 | 0 0 24 24 | stroke | pricing | Previous idea |
| [preview-updated](icons/preview-updated.svg) | 13x13 | 0 0 24 24 | stroke | product | Preview updated |
| [qr-code](icons/qr-code.svg) | 14x14 | 0 0 24 24 | stroke | product | QR code |
| [replay](icons/replay-210e7498.svg) | 16x16 | 0 0 24 24 | stroke | product | Replay |
| [start-building](icons/start-building-27086164.svg) | 18x18 | 0 0 24 24 | stroke | pricing | Start building |
| [icon-2a9ed1e9](icons/icon-2a9ed1e9.svg) | 18x18 | 0 0 24 24 | stroke | product |  |
| [download](icons/download.svg) | 15x15 | 0 0 24 24 | stroke | studio | Download |
| [icon-2dd12e21](icons/icon-2dd12e21.svg) | 18x18 | 0 0 24 24 | stroke | product |  |
| [3-changes](icons/3-changes-2dd4cd34.svg) | 14x14 | 0 0 24 24 | stroke | product | 3 changes |
| [share](icons/share.svg) | 16x16 | 0 0 24 24 | stroke | product | Share |
| [8-214-30](icons/8-214-30.svg) | 12x12 | 0 0 24 24 | stroke | product | $8,214.30 |
| [icon-3bc11799](icons/icon-3bc11799.svg) | 18x18 | 0 0 24 24 | stroke | contact-us | Schools If you have a question about gro |
| [icon-4db21492](icons/icon-4db21492.svg) | 18x18 | 0 0 24 24 | stroke | product |  |
| [in-transit-settled](icons/in-transit-settled.svg) | 14x14 | 0 0 24 24 | stroke | product | In transit Settled |
| [close-menu](icons/close-menu.svg) | 18x18 | 0 0 24 24 | stroke | nav | Close menu |
| [icon-5490a80e](icons/icon-5490a80e.svg) | 18x18 | 0 0 24 24 | stroke | ai | Test Pilot Write tests in plain English. |
| [icon-577cbaef](icons/icon-577cbaef.svg) | 15x15 | 0 0 24 24 | stroke | product |  |
| [icon-5c13e803](icons/icon-5c13e803.svg) | 13x13 | 0 0 24 24 | stroke | studio-showcase | FlutterFlow App of the Month Breatho Gui / FlutterFlow App o |
| [icon-6001b861](icons/icon-6001b861.svg) | 20x20 | 0 0 20 20 | stroke | product |  |
| [icon-638cd14f](icons/icon-638cd14f.svg) | 18x18 | 0 0 24 24 | stroke | ai | FlutterFlow Designer Describe an app and |
| [next-idea](icons/next-idea-65b32117.svg) | 17x17 | 0 0 24 24 | stroke | pricing | Next idea |
| [icon-65bc5597](icons/icon-65bc5597.svg) | 18x18 | 0 0 24 24 | stroke | ai | MCP server Let your coding agents read,  |
| [icon-66b54d8d](icons/icon-66b54d8d.svg) | 18x18 | 0 0 24 24 | stroke | ai | Generate with Designer Describe a page o |
| [icon-67cd702d](icons/icon-67cd702d.svg) | 18x18 | 0 0 24 24 | stroke | product |  |
| [open](icons/open.svg) | 14x14 | 0 0 24 24 | stroke | product | Open |
| [icon-791d2e7d](icons/icon-791d2e7d.svg) | 17x17 | 0 0 24 24 | stroke | ai | AI Agent Panel Use your Claude, Codex, A / Plugins for Claud |
| [icon-79545ca7](icons/icon-79545ca7.svg) | 18x18 | 0 0 24 24 | stroke | product |  |
| [icon-7d953232](icons/icon-7d953232.svg) | 16x16 | 0 0 24 24 | stroke | product |  |
| [icon-87b3a74e](icons/icon-87b3a74e.svg) | 18x18 | 0 0 24 24 | stroke | product |  |
| [icon-8911bb7b](icons/icon-8911bb7b.svg) | 10x11 | 0 0 28.99 31.99 | fill | product |  |
| [search-movements](icons/search-movements.svg) | 14x14 | 0 0 24 24 | stroke | product | Search movements… |
| [icon-8d16a6ab](icons/icon-8d16a6ab.svg) | 18x18 | 0 0 24 24 | stroke | ai | AI Agent Panel Use your Claude, Codex, A |
| [icon-97cb0676](icons/icon-97cb0676.svg) | 18x18 | 0 0 24 24 | stroke | studio-faq |  |
| [pricing](icons/pricing.svg) | 18x18 | 0 0 24 24 | stroke | nav | Pricing / Enterprise |
| [icon-9eeb1904](icons/icon-9eeb1904.svg) | 14x14 | 0 0 24 24 | stroke | pricing | Apply (opens in a new tab) |
| [replay](icons/replay-a01c3ebc.svg) | 16x16 | 0 0 24 24 | stroke | product | Replay |
| [icon-a392fc86](icons/icon-a392fc86.svg) | 17x17 | 0 0 24 24 | stroke | contact-us | General questions Our documentation can  / Schools If you ha |
| [icon-a6b3e0be](icons/icon-a6b3e0be.svg) | 13x13 | 0 0 800 800 | fill | product |  |
| [in-your-app](icons/in-your-app.svg) | 12x12 14x14 | 0 0 24 24 | stroke | product | In your app / Push to your app |
| [a-free-ai-allowance](icons/a-free-ai-allowance.svg) | 15x15 | 0 0 24 24 | stroke | pricing | A free AI allowance / 2 projects / AI usage for a simple app |
| [icon-ab0b78fb](icons/icon-ab0b78fb.svg) | 17x17 | 0 0 24 24 | stroke | contact-us | Enterprise If you’re interested in discu / Partners If you a |
| [icon-ba4195e8](icons/icon-ba4195e8.svg) | 18x18 | 0 0 24 24 | stroke | contact-us | Partners If you are interested in partne |
| [icon-beee6d96](icons/icon-beee6d96.svg) | 14x14 | 0 0 24 24 | stroke | product |  |
| [icon-c13e8a14](icons/icon-c13e8a14.svg) | 18x18 | 0 0 24 24 | stroke | contact-us | General questions Our documentation can  |
| [icon-c64760b6](icons/icon-c64760b6.svg) | 20x20 | 0 0 800 800 | fill | product |  |
| [icon-ce04288a](icons/icon-ce04288a.svg) | 14x14 | 0 0 24 24 | stroke | product |  |
| [ledger](icons/ledger.svg) | 14x14 | 0 0 24 24 | stroke | product | Ledger |
| [icon-d3957788](icons/icon-d3957788.svg) | 14x14 | 0 0 24 24 | stroke | product |  |
| [icon-d8b88764](icons/icon-d8b88764.svg) | 14x14 | 0 0 24 24 | stroke | product |  |
| [replay](icons/replay-dde7cd6c.svg) | 16x16 | 0 0 24 24 | stroke | product | Replay |
| [3-changes](icons/3-changes-ded197a2.svg) | 12x12 13x13 | 0 0 24 24 | stroke | product | 3 changes |
| [icon-e4ed4987](icons/icon-e4ed4987.svg) | 14x14 | 0 0 24 24 | stroke | product |  |
| [icon-e5d53e90](icons/icon-e5d53e90.svg) | 18x18 | 0 0 24 24 | stroke | ai | Plugins for Claude Code and Codex Build  |
| [icon-e99b06b1](icons/icon-e99b06b1.svg) | 12x12 | 0 0 24 24 | stroke | studio | F Firebase , Backend (opens in a new tab / Supabase , Backen |
| [replay](icons/replay-ebd64fb8.svg) | 16x16 | 0 0 24 24 | stroke | product | Replay |
| [icon-f4414c73](icons/icon-f4414c73.svg) | 16x16 | 0 0 24 24 | stroke | product |  |
| [icon-fb7d9bdb](icons/icon-fb7d9bdb.svg) | 16x16 | 0 0 24 24 | stroke | product |  |
| [movements](icons/movements.svg) | 12x12 | 0 0 24 24 | stroke | product | Movements |

## Gaps

### Pages

- **Signed-in surfaces.** app.flutterflow.io, the project dashboard, the editor canvas, the AI generation flow, billing/account pages and every "Start building"/"Sign in"/"Open Studio" destination sit behind login and were never opened. The composer submits to a signed-in flow; it was measured, focused and typed in (then cleared) but never submitted, so what a prompt generates was not captured.
- **Form submissions.** The enterprise Talk-to-sales form and the Studio application form were read and focused; neither was filled meaningfully or submitted, so their success/error screens are missing. The `.ff-fld-err` error slot is in the DOM with a declared danger colour but unpainted at rest, so there is no painted validation state in the package.
- **Checkout.** Choosing a paid plan leads to a signed-in checkout; the plan CTAs were measured but never followed.
- **Blog and changelog entries.** The index pages were captured; individual posts follow the same article shell and were not paged through.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover), so a state a script adds on real mousedown (if any) is missing; the `How` row of each pressed reading says so.
- **Hover** on several controls (the secondary plan CTA, select options, the composer send) changed nothing measurable beyond what the entry lists; the nav links' hover is a colour change to ink.
- **The select popup's scroll region** was measured open; option-level checked state inside it was not exercised (an option click would close the popup).
- **Disabled states** were not seen on any public control; the composer's send sits disabled until text is entered, painted at 40% ink.
- **Scroll-driven animations.** Several sections animate in on scroll (the sheets declare scroll-timeline work); the measurements read resting states, and reduced-motion behaviour is in [raw/motion.json](raw/motion.json), not per-component.

### Themes

Both themes are real: the footer switch writes `ff-theme` to localStorage and sets `html[data-theme]`; the sheets rebind every `--ff-*` under `:root[data-theme="dark"]` and under `prefers-color-scheme: dark` when no choice is stored. The dark set's values come from the switch's own Dark pick (verified painted, not inferred), on home, product, pricing and enterprise plus per-component `dark` states on the home composer, the announcement bar and the contrast button. Dark shots of the other pages and a mobile dark pass were not taken; the token file still carries a full dark set because the declarations are complete.

### Fonts

- **Inter** is self-hosted (variable, wght 100-900) and is what every role measures; FlutterFlow's 510 is the semibold stop.
- The **mono** roles use the `ui-monospace` stack: SF Mono where present, else the platform mono — not a shipped face.

### Screenshots

- Customer logos, product-shot artwork and testimonial photos are FlutterFlow's and their customers' content and appear only inside screenshots and crops. Several hero and product modules animate or video-loop, so two captures of the same view can differ.
- Full-page shots are capped at eight chunks; `/blog` and `/customer-stories` index pages are long but every captured page fit the cap (the height each shot reached is in its `.capture.json` sidecar).
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The cookie-consent banner (a CookieScript vendor widget) was closed before each capture and is not part of the design layer; its `--ck-*` variables are in [raw/css-vars.json](raw/css-vars.json) under `vendor`.
- The demo videos and animated product modules inside the pages' mock windows were not transcribed; only the frames around them were measured.
- No personal data was captured: the pages were read signed out, and no form was submitted.
