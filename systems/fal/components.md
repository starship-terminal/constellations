# fal.ai components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from fal.ai on 2026-11-14, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought, downloaded or submitted; the OAuth buttons were never followed, no model was ever run, and no code was copied.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (75 components, 201 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (198 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: the marketing and docs pages paint `light` (plus a `docs-dark` pass), the app pages paint `dark` (plus `explore-light`, `model-light` and `login-light` passes). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home (marketing, light) | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Pricing (marketing, light) | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Serverless (marketing, light) | `/serverless` | [default](screenshots/serverless-light-default.png), [full](screenshots/serverless-light-full.png) |
| Contact sales (marketing, light) | `/contact-sales` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Explore catalog (app, dark) | `/explore` | [default](screenshots/explore-dark-default.png), [full](screenshots/explore-dark-full.png) |
| Explore catalog (app, light) | `/explore` | [default](screenshots/explore-light-light-default.png), [full](screenshots/explore-light-light-full.png) |
| Model detail (app, dark) | `/models/krea/v3/text-to-image` | [default](screenshots/model-dark-default.png), [full](screenshots/model-dark-full.png) |
| Model detail (app, light — blocked by the edge check; default shot only) | `/models/krea/v3/text-to-image` | [default](screenshots/model-light-light-default.png) |
| Model API tab (app, dark) | `/models/krea/v3/text-to-image/api` | [default](screenshots/api-dark-default.png), [full](screenshots/api-dark-full.png) |
| Login (app, dark) | `/login` | [default](screenshots/login-dark-default.png) |
| Login (app, light) | `/login` | [default](screenshots/login-light-light-default.png) |
| Documentation (docs, light) | `/docs/documentation` | [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png) |
| Documentation (docs, dark) | `/docs/documentation` | [default](screenshots/docs-dark-dark-default.png), [full](screenshots/docs-dark-dark-full.png) |
| 404 page (marketing, light) | `/this-page-does-not-exist` | [default](screenshots/notfound-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Explore, phone | `/explore` | [default](screenshots/mobile-explore-dark-default.png), [drawer](screenshots/mobile-explore-dark-drawer.png), [full](screenshots/mobile-explore-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent card | every page | hidden, never answered (no consent button was ever clicked) | hidden before every shot and reading |
| Announcement strip | /explore | above the app header; the Dismiss X was measured, never pressed | [app-announce](#dismiss-announcement-button) |
| Products menu | /explore header | the header Products trigger's own disclosure | [app-nav-menu](#products-menu), [app-nav-menu-item](#products-menu-item) |
| Products dropdown | / | the marketing w-dropdown Products trigger | [mkt-nav-products](#products-menu-trigger) |
| Phone nav sheet | /explore at 390 wide | the 'Open navigation' trigger's own toggle | [mobile-explore-dark-drawer](screenshots/mobile-explore-dark-drawer.png), [m-nav-item](#mobile-nav-link) |
| Docs theme control | /docs/documentation | a light/system/dark segment; measured, never cycled | [docs-theme-btn](#theme-switcher) |
| Signed-in product | a fal account | every post-login surface needs an account or an API key | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 37 components were given a real keyboard focus. 14 draw an outline ring: `mkt-nav-products` (2px solid #4d65ff, offset 2px), `mkt-nav-pricing` (1px auto #101010 `border.focus`, offset 1px), `mkt-btn-sales` (1px auto #101010 `border.focus`, offset 1px), `mkt-btn-start` (1px auto #101010 `border.focus`, offset 1px), `mkt-hero-cta` (1px auto #101010 `border.focus`, offset 1px), `pr-plan-cta` (1px auto #101010 `border.focus`, offset 1px), `app-nav-products` (2px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`, offset -2px), `app-nav-docs` (2px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`, offset -2px), `carousel-dot` (2px solid #ffffff `color.white`, offset 2px), `docs-search` (1px auto #5718c0 `color.primary.700`, offset 0px), `docs-theme-btn` (1px auto #5718c0 `color.primary.700`, offset 0px), `docs-hero-search` (1px auto #5718c0 `color.primary.700`, offset 0px), `docs-code-copy` (1px auto #5718c0 `color.primary.700`, offset 0px), `pager-dot` (1px auto #101010, offset 0px). 23 draw a focus ring as a shadow instead: `app-announce-x`, `app-btn-login`, `app-btn-signup`, `card-cta`, `pager-next`, `mp-tab`, `mp-endpoint-btn`, `mp-copy`, `mp-agent-btn`, `mp-sandbox-link`, `mp-param`, `mp-param-more`, `mp-run`, `mp-result-tab`, `mp-download`, `api-copy`, `api-lang-tab`, `li-oauth-github`, `li-oauth-google`, `li-sso`, `li-support`, `m-hamburger`, `card-docs-link`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | background-color, color | mkt-btn-sales, mkt-nav-products |
| 0.15s | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | mp-back |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | api-lang-tab, app-nav-docs, app-nav-products, li-sso, m-nav-item, mp-badge, mp-param |
| 0.16s | `cubic-bezier(0, 0, 0.2, 1)` | background-color, border-color, color, transform | api-tab, mp-tab |
| 0.16s | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | background-color, border-color, color, opacity, transform | api-copy, app-announce-x, card-cta, card-docs-link, mp-agent-btn, mp-copy, mp-download, mp-endpoint-btn and more |
| 0.2s | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | background-color | mkt-logo |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | docs-theme-btn, pager-dot |
| 0.2s | `ease` | border-color | docs-hero-search |
| 0.3s | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | width | mkt-logo |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Model card](#model-card) | 360 x 350.5 | - | - | transparent | none | 0 |
| [Docs section card](#docs-section-card) | 650 x 444 | - | 4px | transparent | none | 0 |
| [Login card](#login-card) | 400 x 388.91 | - | - | transparent | none | 0 |
| [Products menu](#products-menu) | 322 x 201 | 1px solid rgba(255, 255, 255, 0.05) `badge.default.alpha` | 4px | #19191a `palette.neutral.950` | rgba(255, 255, 255, 0.03) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px, rgba(0, 0, 0, 0.4) 0px 1px 3px 0px | 0 |
| [Pricing table](#pricing-table) | 1337.16 x 364.36 | - | - | #e5ece7 `color.sage.100` | none | 17.1429px |
| [Marketing header](#marketing-header) | 1440 x 88 | - | - | transparent | none | 0 |
| [App header](#app-header) | 1440 x 48 | - | - | transparent | none | 0 |
| [Docs sidebar](#docs-sidebar) | 350 x 900 | R: 1px solid oklab(0.906575 0.0040085 -0.00581205 / 0.7) | 4px | transparent | none | 0 |
| [Mobile header](#mobile-header) | 390 x 48 | - | - | transparent | none | 0 |

## Components

### App shell and navigation

The 48px app header (header.dashboard-navigation-header) plus the 88px fixed marketing bar (div.nav-main): the fal wordmark, the Products dropdown, Documentation / Pricing / Enterprise links, Contact Sales and the Log-in / Sign-up pair, over the dismissible announcement strip.

#### Marketing header
The fixed top bar (div.nav-main, z-index 999): fal wordmark, Products / Docs / Pricing / Enterprise / Resources menus, Contact Sales and Get Started. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 88; background transparent; text Focal Web 14/14 500, #000000 `color.black`; layers a.nav-logo-holder.w-inline-block 140.0x68.0 rgba(255, 255, 255, 0.88) 4px; div.nav-list 502.0x35.2 rgba(255, 255, 255, 0.88) 4.8px; div::after.dropdown-toggle.w-dropdown-toggle 4.79688pxx4.79688px; div.nav-dot 8.0x8.0 rgb(153, 153, 153) 100%; nav.dropdown-content.w-dropdown-list 0.0x0.0 rgba(255, 255, 255, 0); nav::before.dropdown-content.w-dropdown-list autoxauto rgb(173, 255, 0) 0px 4.8px 4.8px.

Child layers that carry the look: a 140x68 background rgba(255, 255, 255, 0.88) radius 4px; div 502x35.2 background rgba(255, 255, 255, 0.88) radius 4.8px; div::after 4.79688pxx4.79688px image radial-gradient(circle at 100% 0px, transparent 0.3em, #adff00 `marketing.brand.neon` calc.

![Marketing header default](components/crops/mkt-header-default.png)

#### Logo
The fal wordmark link (a.nav-logo-holder). Read as `mkt-logo` on the home page.

**Values (default).** size 140 x 68; padding 10px; radius 4px; background rgba(255, 255, 255, 0.88); text Focal Web 16/24 400, #000000 `color.black`; transition width 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94), background-color 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94).

![Logo default](components/crops/mkt-logo-default.png)

#### Products menu trigger
The Products dropdown trigger in the marketing nav — a Webflow w-dropdown disclosure; measured, its links never followed. Read as `mkt-nav-products` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 111 x 35.19; padding 10px 18px; background transparent; text Focal Web 14/14 500, #000000 `color.black`; layers ::after rgba(0, 0, 0, 0) 0px none 0; div::after.dropdown-toggle.w-dropdown-toggle 4.79688pxx4.79688px; div.nav-dot 8.0x8.0 rgb(153, 153, 153) 100% |
| hover | radius 4.8px 4.8px 0px 0px; background #adff00 `marketing.brand.neon`; transition background-color 0.1s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.1s cubic-bezier(0.25, 0.46, 0.45, 0.94); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 2px solid #4d65ff, offset 2px; layers ::after rgba(0, 0, 0, 0) 0px none 0; div.dropdown-toggle.w-dropdown-toggle 111.0x35.2 2px solid rgb(77, 101, 255) offset 2px; div::after.dropdown-toggle.w-dropdown-toggle 4.79688pxx4.79688px; div.nav-dot 8.0x8.0 rgb(153, 153, 153) 100% |

Child layers that carry the look: div::after 4.79688pxx4.79688px image radial-gradient(circle at 100% 0px, transparent 0.3em, #adff00 `marketing.brand.neon` calc; div 8x8 background #999999 radius 100%.

![Products menu trigger default](components/crops/mkt-nav-products-default.png) ![Products menu trigger hover](components/crops/mkt-nav-products-hover.png) ![Products menu trigger focus-visible](components/crops/mkt-nav-products-focus-visible.png) ![Products menu trigger pressed](components/crops/mkt-nav-products-pressed.png)

#### Pricing link (marketing)
The marketing nav Pricing link; measured, never followed. Read as `mkt-nav-pricing` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 87 x 35.19; padding 10px 20px; radius 4px; background transparent; text Focal Web 14/14 500, #000000 `color.black` |
| hover | background #ffc4d8 `marketing.brand.pink` |
| focus-visible | background #ffc4d8 `marketing.brand.pink`; outline 1px auto #101010 `border.focus`, offset 1px |
| pressed | background #ffc4d8 `marketing.brand.pink` |

![Pricing link (marketing) default](components/crops/mkt-nav-pricing-default.png) ![Pricing link (marketing) hover](components/crops/mkt-nav-pricing-hover.png) ![Pricing link (marketing) focus-visible](components/crops/mkt-nav-pricing-focus-visible.png) ![Pricing link (marketing) pressed](components/crops/mkt-nav-pricing-pressed.png)

#### Contact Sales button (marketing)
The secondary Contact-Sales button in the marketing header; measured, never followed. Read as `mkt-btn-sales` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 143 x 34.59; padding 10px 26px; border 1px solid #e5ece7 `color.sage.100`; radius 2px; background #e5ece7 `color.sage.100`; text Focal Web 14/12.6 500, #000000 `color.black`; transition background-color 0.1s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.1s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| hover | background #d9d9d9 |
| focus-visible | outline 1px auto #101010 `border.focus`, offset 1px |
| pressed | background #d9d9d9 |

![Contact Sales button (marketing) default](components/crops/mkt-btn-sales-default.png) ![Contact Sales button (marketing) hover](components/crops/mkt-btn-sales-hover.png) ![Contact Sales button (marketing) focus-visible](components/crops/mkt-btn-sales-focus-visible.png) ![Contact Sales button (marketing) pressed](components/crops/mkt-btn-sales-pressed.png)

#### Get Started button (marketing)
The primary Get-Started button in the marketing header; measured, never followed. Read as `mkt-btn-start` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 128 x 34.59; padding 10px 26px; border 1px solid #000000 `color.black`; radius 2px; background #000000 `color.black`; text Focal Web 14/12.6 500, #ffffff `color.white` |
| hover | border 1px solid #e5ece7 `color.sage.100`; background #e5ece7 `color.sage.100`; text Focal Web 14/12.6 500, #000000 `color.black` |
| focus-visible | border 1px solid #e5ece7 `color.sage.100`; background #e5ece7 `color.sage.100`; outline 1px auto #101010 `border.focus`, offset 1px; text Focal Web 14/12.6 500, #000000 `color.black` |
| pressed | border 1px solid #e5ece7 `color.sage.100`; background #e5ece7 `color.sage.100`; text Focal Web 14/12.6 500, #000000 `color.black` |

![Get Started button (marketing) default](components/crops/mkt-btn-start-default.png) ![Get Started button (marketing) hover](components/crops/mkt-btn-start-hover.png) ![Get Started button (marketing) focus-visible](components/crops/mkt-btn-start-focus-visible.png) ![Get Started button (marketing) pressed](components/crops/mkt-btn-start-pressed.png)

#### App header
The app navigation header (header.dashboard-navigation-header): fal mark, Products / Documentation / Pricing / Enterprise / Resources menus, Contact Sales, Log-in, Sign-up. Read as `app-header` on the explore page.

**Values (default).** size 1440 x 48; background transparent; text publicSansRounded 14/normal 600, #f4f4f5 `palette.neutral.100`; layers div.dashboard-navigation-surface 1440.0x48.0 rgb(25, 25, 26) B:1px solid rgba(255, 255, 255, 0.05); div.dashboard-navigation-seam 1440.0x1.0 B:1px solid rgba(255, 255, 255, 0.05); button.inline-flex.items-center 0.0x0.0 rgb(32, 32, 34) 4px; button::after.inline-flex.items-center autoxauto rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255.

Child layers that carry the look: div 1440x48 background #19191a `palette.neutral.950` border 1px solid rgba(255, 255, 255, 0.05) `badge.default.alpha`; div 1440x1 border 1px solid rgba(255, 255, 255, 0.05) `badge.default.alpha`; button 0x0 background #202022 `palette.neutral.900` radius 4px.

![App header default](components/crops/app-header-default.png)

#### Announcement banner
The dismissible announcement strip above the header; the Dismiss button is measured, never pressed. Read as `app-announce` on the explore page.

**Values (default).** size 1440 x 32; padding 6px 44px; background #142657 `palette.info.950`; text focal 14/18 500, #99edff `color.cyan.300`; icon 6 x 6, #115ef3 `color.info.600`.

![Announcement banner default](components/crops/app-announce-default.png)

#### Dismiss-announcement button
The X that closes the announcement strip — a local dismiss; measured, never pressed. Read as `app-announce-x` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 28 x 28; border 1px solid transparent; radius 4px; background transparent; text publicSansRounded 14/14 600, #99edff `color.cyan.300`; transition background-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 16 x 16, #99edff `color.cyan.300` |
| hover | background oklab(0.999994 0.0000455678 0.0000200868 / 0.1) |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | size 27.44 x 27.44; background oklab(0.999994 0.0000455678 0.0000200868 / 0.1); icon 15.68 x 15.68, #99edff `color.cyan.300` |

![Dismiss-announcement button default](components/crops/app-announce-x-default.png) ![Dismiss-announcement button hover](components/crops/app-announce-x-hover.png) ![Dismiss-announcement button focus-visible](components/crops/app-announce-x-focus-visible.png) ![Dismiss-announcement button pressed](components/crops/app-announce-x-pressed.png)

#### Products menu trigger (app)
The Products dropdown trigger in the app header — a local disclosure; the opened state was measured after clicking it, its links never followed. Read as `app-nav-products` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 91.77 x 48; padding 0px 6px 0px 10px; background transparent; text publicSansRounded 14/22.4 600, rgba(255, 255, 255, 0.65) `color.content.lighter`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(255, 255, 255, 0.65) `color.content.lighter` |
| hover | text publicSansRounded 14/22.4 600, rgba(255, 255, 255, 0.8) `badge.default.foreground` |
| focus-visible | radius 4px; outline 2px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`, offset -2px; text publicSansRounded 14/22.4 600, rgba(255, 255, 255, 0.8) `badge.default.foreground`; layers button.group.inline-flex 91.8x48.0 2px solid rgba(255, 255, 255, 0.2) offset -2px 4px |
| pressed | text publicSansRounded 14/22.4 600, rgba(255, 255, 255, 0.8) `badge.default.foreground` |
| opened | text publicSansRounded 14/22.4 600, #f4f4f5 `palette.neutral.100`; icon 16 x 16, #f4f4f5 `palette.neutral.100` |

![Products menu trigger (app) hover](components/crops/app-nav-products-hover.png) ![Products menu trigger (app) focus-visible](components/crops/app-nav-products-focus-visible.png) ![Products menu trigger (app) pressed](components/crops/app-nav-products-pressed.png) ![Products menu trigger (app) opened](components/crops/app-nav-products-opened.png)

#### Products menu
The dropdown opened by the Products trigger (div.top-center ~322x201, holding ul.p-1.5 product links); its links were never followed. Read as `app-nav-menu` on the explore page.

**Values (default).** size 322 x 201; border 1px solid rgba(255, 255, 255, 0.05) `badge.default.alpha`; radius 4px; background #19191a `palette.neutral.950`; shadow rgba(255, 255, 255, 0.03) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px, rgba(0, 0, 0, 0.4) 0px 1px 3px 0px; text publicSansRounded 14/17.5 500, #f4f4f5 `palette.neutral.100`; icon 16 x 16, rgba(255, 255, 255, 0.8) `badge.default.foreground`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Products menu default](components/crops/app-nav-menu-default.png)

#### Products menu item
A product entry inside the opened dropdown (a.text-content-subtle); measured, never followed. Read as `app-nav-menu-item` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 308 x 65.5; padding 8px; radius 4px; background transparent; text publicSansRounded 14/17.5 500, #f4f4f5 `palette.neutral.100`; icon 16 x 16, rgba(255, 255, 255, 0.8) `badge.default.foreground`; layers ::before rgba(0, 0, 0, 0) 0px none 1; div.flex.size-9 36.0x36.0 rgba(255, 255, 255, 0.05) 4px |
| hover | background rgba(255, 255, 255, 0.03) `badge.ghost`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |

Child layers that carry the look: div 36x36 background rgba(255, 255, 255, 0.05) `badge.default.alpha` radius 4px.

![Products menu item hover](components/crops/app-nav-menu-item-hover.png)

#### Documentation link (app)
The app header Documentation link; measured, never followed. Read as `app-nav-docs` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 118.38 x 48; padding 0px 10px; background transparent; text publicSansRounded 14/22.4 600, rgba(255, 255, 255, 0.65) `color.content.lighter`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text publicSansRounded 14/22.4 600, rgba(255, 255, 255, 0.8) `badge.default.foreground` |
| focus-visible | radius 4px; outline 2px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`, offset -2px; text publicSansRounded 14/22.4 600, rgba(255, 255, 255, 0.8) `badge.default.foreground`; layers a.group.inline-flex 118.4x48.0 2px solid rgba(255, 255, 255, 0.2) offset -2px 4px |
| pressed | text publicSansRounded 14/22.4 600, rgba(255, 255, 255, 0.8) `badge.default.foreground` |

![Documentation link (app) default](components/crops/app-nav-docs-default.png) ![Documentation link (app) hover](components/crops/app-nav-docs-hover.png) ![Documentation link (app) focus-visible](components/crops/app-nav-docs-focus-visible.png) ![Documentation link (app) pressed](components/crops/app-nav-docs-pressed.png)

#### Log-in button (app)
The Log-in button in the app header; measured, never followed. Read as `app-btn-login` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 64.17 x 32; padding 4px 12px; radius 4px; background #202022 `palette.neutral.900`; text publicSansRounded 14/normal 600, #f4f4f5 `palette.neutral.100`; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1 |
| hover | background rgba(255, 255, 255, 0.05) `badge.default.alpha`; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.2) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1 |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | background rgba(255, 255, 255, 0.05) `badge.default.alpha`; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.2) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1 |

![Log-in button (app) default](components/crops/app-btn-login-default.png) ![Log-in button (app) hover](components/crops/app-btn-login-hover.png) ![Log-in button (app) focus-visible](components/crops/app-btn-login-focus-visible.png) ![Log-in button (app) pressed](components/crops/app-btn-login-pressed.png)

#### Sign-up button (app)
The primary Sign-up button in the app header; measured, never followed. Read as `app-btn-signup` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 74.03 x 32; padding 4px 12px; radius 4px; background #fafafa `color.neutral.50`; text publicSansRounded 14/normal 600, #161618 `color.neutral.1000` |
| hover | background #e4e4e7 `palette.neutral.200` |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | background #e4e4e7 `palette.neutral.200` |

![Sign-up button (app) default](components/crops/app-btn-signup-default.png) ![Sign-up button (app) hover](components/crops/app-btn-signup-hover.png) ![Sign-up button (app) focus-visible](components/crops/app-btn-signup-focus-visible.png) ![Sign-up button (app) pressed](components/crops/app-btn-signup-pressed.png)

### Home (marketing)

The Webflow home page: the Focal Web display headline on the cyan brand field, the hero CTA and the section headings.

#### Hero headline
The home hero display heading — Focal Web 96px, the cyan brand colour on the olive field. Read as `mkt-hero-h1` on the home page.

**Values (default).** size 1028.56 x 172.78; background transparent; text Focal Web 96/86.4 500, #99edff `color.cyan.300`.

![Hero headline default](components/crops/mkt-hero-h1-default.png)

#### Hero field
The home hero section: the dark bronze field (background-color-darkbronze) behind the cyan display headline. Read as `mkt-hero-field` on the home page.

**Values (default).** size 1440 x 800; background #403700 `marketing.brand.dark.bronze`; text Focal Web 96/86.4 500, #99edff `color.cyan.300`.

![Hero field default](components/crops/mkt-hero-field-default.png)

#### Hero CTA
The primary call-to-action inside the hero; measured never followed. Read as `mkt-hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 134.56 x 44.05; padding 13.7143px 22.2857px; border 1px solid #adff00 `marketing.brand.neon`; radius 2px; background #adff00 `marketing.brand.neon`; text Focal Web 16.28/14.65 500, #403700 `marketing.brand.dark.bronze` |
| hover | border 1px solid #71a600; background #71a600; text Focal Web 16.28/14.65 500, #ffffff `color.white` |
| focus-visible | outline 1px auto #101010 `border.focus`, offset 1px |
| pressed | border 1px solid #71a600; background #71a600; text Focal Web 16.28/14.65 500, #ffffff `color.white` |

![Hero CTA default](components/crops/mkt-hero-cta-default.png) ![Hero CTA hover](components/crops/mkt-hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/mkt-hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/mkt-hero-cta-pressed.png)

#### Section heading (marketing)
A marketing section heading further down the home page. Read as `mkt-section-h2` on the home page.

**Values (default).** size 822.84 x 106.44; background transparent; text Focal Web 59.14/53.22 500, #000000 `color.black`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Pricing (marketing)

The Webflow pricing page: 'Fast, reliable, and cost-efficient.', then usage pricing for GPU compute and model APIs in div.pricing-row-table blocks — there are no plan cards or billing toggle.

#### Pricing headline
The pricing page display heading. Read as `pr-h1` on the pricing page.

**Values (default).** size 1028.56 x 172.78; background transparent; text Focal Web 96/86.4 500, #000000 `color.black`.

![Pricing headline default](components/crops/pr-h1-default.png)

#### Plan CTA
A call-to-action inside a plan column; measured never followed. Read as `pr-plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 151.56 x 44.05; padding 13.7143px 22.2857px; border 1px solid #ffffff `color.white`; radius 2px; background #ffffff `color.white`; text Focal Web 16.28/14.65 500, #000000 `color.black` |
| hover | border 1px solid #e5ece7 `color.sage.100`; background #e5ece7 `color.sage.100` |
| focus-visible | outline 1px auto #101010 `border.focus`, offset 1px |
| pressed | border 1px solid #e5ece7 `color.sage.100`; background #e5ece7 `color.sage.100` |

![Plan CTA default](components/crops/pr-plan-cta-default.png) ![Plan CTA hover](components/crops/pr-plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/pr-plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/pr-plan-cta-pressed.png)

#### Pricing table
A div.pricing-row-table block under the "Serverless & Compute Pricing" heading — fal prices GPU compute and model APIs per usage; there is no plan card or billing toggle. Read as `pr-price-table` on the pricing page.

**Values (default).** size 1337.16 x 364.36; padding 17.1429px; background #e5ece7 `color.sage.100`; text Focal Text 16.28/19.54 400, #000000 `color.black`.

![Pricing table default](components/crops/pr-price-table-default.png)

#### Pricing row
A .pricing-table-row line inside a compute/model pricing table. Read as `pr-price-row` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1302.88 x 32.97; background transparent; text Focal Text 14.65/17.58 500, #ec0648 `color.error.500`; icon 21.98 x 21.98, #000000 `color.black`; layers div.price-card-pill 81.1x33.0 rgb(255, 255, 255) 3.66429px; div.price-card-pill.is-regular 51.0x33.0 rgba(255, 255, 255, 0) 3.66429px; div.price-card-pill.is-regular 55.0x33.0 rgba(255, 255, 255, 0) 3.66429px; div.price-card-pill.is-regular 51.0x33.0 rgba(255, 255, 255, 0) 3.66429px |

Child layers that carry the look: div 81.1x33 background #ffffff `color.white` radius 3.66429px; div 51x33 background rgba(255, 255, 255, 0) radius 3.66429px; div 55x33 background rgba(255, 255, 255, 0) radius 3.66429px.

![Pricing row default](components/crops/pr-price-row-default.png) ![Pricing row hover](components/crops/pr-price-row-hover.png)

### Explore catalog (app, dark)

The dark app catalog (/explore): the model search field, the a.page-model-card grid (~360x350 tiles of endpoint ids and publisher artwork), hero-carousel slide CTAs and the section pagers.

#### Model search field
The "Search models" input over the catalog; focused and typed into then cleared — the catalog only filters locally. Read as `search-models` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 953.08 x 24; background transparent; shadow rgba(255, 255, 255, 0.8) 0px 0px 0px 0px; text publicSansRounded 16/24 400, rgba(255, 255, 255, 0.8) `badge.default.foreground`; placeholder rgba(255, 255, 255, 0.8) `badge.default.foreground`; layers input.flex.min-w-0 953.1x24.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.8) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px |
| focused, filled | shadow #ffffff 0px 0px 0px 0px, rgba(255, 255, 255, 0.8) 0px 0px 0px 0px; layers input.flex.min-w-0 953.1x24.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 0px, rgba(255, 255, 255, 0.8) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px |

![Model search field default](components/crops/search-models-default.png) ![Model search field focused](components/crops/search-models-focused.png) ![Model search field filled](components/crops/search-models-filled.png)

#### Model card
A model tile in the explore grid (a.page-model-card): artwork, endpoint id, publisher and description; measured, never followed. Read as `model-card` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 350.5; background transparent; text publicSansRounded 12/18 600, #163200 `color.lime.950`; icon 12 x 12, #163200 `color.lime.950`; layers div::after.flex.h-full 360pxx350.5px T:1px solid rgba(255, 255, 255, 0.1) / R:1px solid rgba(255, 255, 255, 0.1) / B:1px solid rgba(255, 255, 255, 0.1) / L:1px solid rgba(255, 255, 255, 0.1) 4px; div.relative.aspect-[16/9] 360.0x202.5; div.badge.badge-role-lime 44.6x16.0 rgb(162, 216, 28) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba( |
| hover | layers div::after.flex.h-full 360pxx350.5px T:1px solid rgba(255, 255, 255, 0.2) / R:1px solid rgba(255, 255, 255, 0.2) / B:1px solid rgba(255, 255, 255, 0.2) / L:1px solid rgba(255, 255, 255, 0.2) 4px; div.relative.aspect-[16/9] 360.0x202.5; div.badge.badge-role-lime 44.6x16.0 rgb(162, 216, 28) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba( |

Child layers that carry the look: div::after 360pxx350.5px border 1px solid rgba(255, 255, 255, 0.1) `color.stroke.strong` radius 4px; div 360x202.5 image linear-gradient(to right in oklab, rgba(255, 255, 255, 0.03) `badge.ghost` 0%, rgba(255, 2; div 44.6x16 background #a2d81c `color.lime.500` border 1px solid transparent radius 4px.

![Model card default](components/crops/model-card-default.png) ![Model card hover](components/crops/model-card-hover.png)

#### Model card endpoint line
The endpoint-id text line inside a card (e.g. blackforestlabs/flux-3-max/text-to-video) — a span.truncate, cards carry no heading elements. Read as `model-card-title` on the explore page.

**Values (default).** size 286 x 20; background transparent; text focal 16/20 400, rgba(255, 255, 255, 0.8) `badge.default.foreground`.

![Model card endpoint line default](components/crops/model-card-title-default.png)

#### Card CTA
The "Try it now!" pill on a hero-carousel slide; measured, never followed. Read as `card-cta` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 101.47 x 36; padding 0px 16px; border 1px solid transparent; radius 4px; background #fafafa `color.neutral.50`; text publicSansRounded 14/20 600, #161618 `color.neutral.1000`; transition background-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | size 99.44 x 35.28 |

![Card CTA hover](components/crops/card-cta-hover.png) ![Card CTA focus-visible](components/crops/card-cta-focus-visible.png) ![Card CTA pressed](components/crops/card-cta-pressed.png)

#### Carousel dot
A "Go to slide N" dot in the hero carousel — a local pager; measured, never clicked. Read as `carousel-dot` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 80 x 40; background transparent; text publicSansRounded 10/15 600, #ffffff `color.white`; layers div.relative.h-1.5 80.0x8.0 oklab(0.999994 0.0000455678 0.0000200868 / 0.2) |
| hover | layers div.relative.h-1.5 80.0x24.0 rgb(120, 58, 251) |
| focus-visible | outline 2px solid #ffffff `color.white`, offset 2px; layers button.group.pointer-events-auto 80.0x40.0 2px solid rgb(255, 255, 255) offset 2px; div.relative.h-1.5 80.0x8.0 oklab(0.999994 0.0000455678 0.0000200868 / 0.2) |
| pressed | size 192 x 40; layers div.relative.h-1.5 192.0x8.0 oklab(0.999994 0.0000455678 0.0000200868 / 0.2); span.absolute.inset-0 12.2x8.0 rgb(255, 255, 255) |

Child layers that carry the look: div 80x8 background oklab(0.999994 0.0000455678 0.0000200868 / 0.2).

![Carousel dot default](components/crops/carousel-dot-default.png) ![Carousel dot hover](components/crops/carousel-dot-hover.png) ![Carousel dot focus-visible](components/crops/carousel-dot-focus-visible.png) ![Carousel dot pressed](components/crops/carousel-dot-pressed.png)

#### Section pager arrow
A "Next page" arrow button scrolling a catalog section (~48x96); a local scroller — measured, never clicked. Read as `pager-next` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 96; border 1px solid transparent; radius 4px; background transparent; text publicSansRounded 16/24 600, rgba(255, 255, 255, 0.65) `color.content.lighter`; transition background-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94); opacity 0; icon 30 x 30, #787881 `palette.neutral.500` |
| hover | background rgba(255, 255, 255, 0.05) `badge.default.alpha`; text publicSansRounded 16/24 600, #f4f4f5 `palette.neutral.100`; opacity none |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | size 0 x 0; border 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.05) `badge.default.alpha`; text publicSansRounded 16/24 600, #f4f4f5 `palette.neutral.100`; opacity none; icon none |

![Section pager arrow default](components/crops/pager-next-default.png) ![Section pager arrow hover](components/crops/pager-next-hover.png) ![Section pager arrow focus-visible](components/crops/pager-next-focus-visible.png)

#### Card docs link
The "See docs" pill on a hero-carousel slide; measured, never followed. Read as `card-docs-link` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 92.89 x 36; padding 0px 16px; border 1px solid rgba(255, 255, 255, 0.1) `color.stroke.strong`; radius 4px; background #202022 `palette.neutral.900`; text publicSansRounded 14/20 600, #f4f4f5 `palette.neutral.100`; transition background-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | size 91.03 x 35.28; border 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.05) `badge.default.alpha` |

![Card docs link default](components/crops/card-docs-link-default.png) ![Card docs link focus-visible](components/crops/card-docs-link-focus-visible.png) ![Card docs link pressed](components/crops/card-docs-link-pressed.png) ![Card docs link hover](components/crops/card-docs-link-hover.png)

#### Section pager dot
A "Go to page N" dot paging a catalog section — a local pager; measured, never clicked. Read as `pager-dot` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 6 x 6; background #a6a6ae `palette.neutral.400`; text publicSansRounded 16/24 400, #ffffff `color.white`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f4f4f5 `palette.neutral.100` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background #f4f4f5 `palette.neutral.100` |

![Section pager dot default](components/crops/pager-dot-default.png) ![Section pager dot hover](components/crops/pager-dot-hover.png) ![Section pager dot focus-visible](components/crops/pager-dot-focus-visible.png) ![Section pager dot pressed](components/crops/pager-dot-pressed.png)

### Model page (app, dark)

A model detail page (/models/krea/v3/text-to-image): the endpoint-id heading, badges, the Playground / API / Examples tabs, the prompt composer, parameter pills and the signed-out Sign-in-to-run action.

#### Back to Gallery link
The breadcrumb-style link back to the catalog; measured, never followed. Read as `mp-back` on the model page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 45 x 12; background transparent; text publicSansRounded 12/12 500, #f4f4f5 `palette.neutral.100`; transition color 0.15s cubic-bezier(0.25, 0.46, 0.45, 0.94), background-color 0.15s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.15s cubic-bezier(0.25, 0.46, 0.45, 0.94), outline-color 0.15s cubic-bezier(0.25, 0.46, 0.45, 0.94), text-decoration-color 0.15s cubic-bezier(0.25, 0.46, 0.45, 0.94), fill 0.15s cubic-bezier(0.25, 0.46, 0.45, 0.94), stroke 0.15s cubic-bezier(0.25, 0.46, 0.45, 0.94), --tw-gradient-from 0.15s cubic-bezier(0.25, 0.46, 0.45, 0.94), --tw-gradient-via 0.15s cubic-bezier(0.25, 0.46, 0.45, 0.94), --tw-gradient-to 0.15s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| pressed | text publicSansRounded 12/12 500, #fafafa `color.neutral.50` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Back to Gallery link default](components/crops/mp-back-default.png) ![Back to Gallery link hover](components/crops/mp-back-hover.png) ![Back to Gallery link pressed](components/crops/mp-back-pressed.png)

#### Model heading
"krea/v3/text-to-image" — the model endpoint heading. Read as `mp-h1` on the model page.

**Values (default).** size 355.75 x 32; background transparent; text focal 30/32 400, rgba(255, 255, 255, 0.8) `badge.default.foreground`; layers div.grid.shrink-0 32.0x32.0 rgb(32, 32, 34) T:1px solid rgba(255, 255, 255, 0.05) / R:1px solid rgba(255, 255, 255, 0.05) / B:1px solid rgba(255, 255, 255, 0.05) / L:1px solid rgba(255, 255, 255, 0.05) 2px.

Child layers that carry the look: div 32x32 background #202022 `palette.neutral.900` border 1px solid rgba(255, 255, 255, 0.05) `badge.default.alpha` radius 2px.

![Model heading default](components/crops/mp-h1-default.png)

#### Model badge
A .badge-role-* pill under the heading (Inference / Commercial use / Idle). Read as `mp-badge` on the model page.

**Values (default).** size 65.11 x 14; padding 0px 3px; border 1px solid transparent; radius 4px; background rgba(120, 58, 251, 0.2) `accent.violet.alpha.strong`; text publicSansRounded 10/15 600, #cac4fe `color.primary.200`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 10 x 10, #cac4fe `color.primary.200`.

![Model badge default](components/crops/mp-badge-default.png)

#### Model page tab
A Playground/API/Examples tab on the model page — an in-page tab link; measured, the active tab was not switched for state capture. Read as `mp-tab` on the model page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 95.2 x 40; padding 4px 10px; border 1px solid transparent; radius 8px; background transparent; text publicSansRounded 14/16.8 600, #fafafa `color.neutral.50`; transition background-color 0.16s cubic-bezier(0, 0, 0.2, 1), border-color 0.16s cubic-bezier(0, 0, 0.2, 1), color 0.16s cubic-bezier(0, 0, 0.2, 1), transform 0.16s cubic-bezier(0, 0, 0.2, 1); layers ::after rgb(250, 250, 250) 0px none 1 |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |

![Model page tab default](components/crops/mp-tab-default.png) ![Model page tab hover](components/crops/mp-tab-hover.png) ![Model page tab focus-visible](components/crops/mp-tab-focus-visible.png) ![Model page tab pressed](components/crops/mp-tab-pressed.png)

#### Model endpoint button
The endpoint-id chip button; measured, never activated. Read as `mp-endpoint-btn` on the model page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 132.19 x 32; padding 0px 10px 0px 12px; border 1px solid rgba(255, 255, 255, 0.1) `color.stroke.strong`; radius 4px; background #202022 `palette.neutral.900`; text publicSansRounded 14/20 600, #f4f4f5 `palette.neutral.100`; transition background-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 16 x 16, #787881 `palette.neutral.500` |
| hover | border 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.05) `badge.default.alpha` |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | border 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.05) `badge.default.alpha` |

![Model endpoint button default](components/crops/mp-endpoint-btn-default.png) ![Model endpoint button hover](components/crops/mp-endpoint-btn-hover.png) ![Model endpoint button focus-visible](components/crops/mp-endpoint-btn-focus-visible.png) ![Model endpoint button pressed](components/crops/mp-endpoint-btn-pressed.png)

#### Copy button
A clipboard Copy icon button (endpoint / code); measured, never pressed. Read as `mp-copy` on the model page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; border 1px solid transparent; radius 4px; background transparent; text publicSansRounded 20/28 600, #f4f4f5 `palette.neutral.100`; transition background-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 16 x 16, rgba(255, 255, 255, 0.5) `content.muted` |
| hover | background rgba(255, 255, 255, 0.05) `badge.default.alpha`; icon 16 x 16, #fafafa `color.neutral.50` |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | size 31.36 x 31.36; background rgba(255, 255, 255, 0.05) `badge.default.alpha`; icon 15.68 x 15.68, #fafafa `color.neutral.50` |

![Copy button default](components/crops/mp-copy-default.png) ![Copy button hover](components/crops/mp-copy-hover.png) ![Copy button focus-visible](components/crops/mp-copy-focus-visible.png) ![Copy button pressed](components/crops/mp-copy-pressed.png)

#### Onboard-your-agent button
The "Onboard your agent" button that copies a setup prompt; measured, never pressed. Read as `mp-agent-btn` on the model page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 216.48 x 32; padding 0px 12px 0px 6px; border T: 1px solid rgba(255, 255, 255, 0.1) `color.stroke.strong`; B: 1px solid rgba(255, 255, 255, 0.1) `color.stroke.strong`; L: 1px solid rgba(255, 255, 255, 0.1) `color.stroke.strong`; radius 4px 0px 0px 4px; background #202022 `palette.neutral.900`; text publicSansRounded 14/20 600, #f4f4f5 `palette.neutral.100`; transition background-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 14 x 14, #787881 `palette.neutral.500` |
| hover | border T: 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; B: 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; L: 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.1) `color.stroke.strong` |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | border T: 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; B: 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; L: 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.1) `color.stroke.strong` |

![Onboard-your-agent button default](components/crops/mp-agent-btn-default.png) ![Onboard-your-agent button hover](components/crops/mp-agent-btn-hover.png) ![Onboard-your-agent button focus-visible](components/crops/mp-agent-btn-focus-visible.png) ![Onboard-your-agent button pressed](components/crops/mp-agent-btn-pressed.png)

#### Open in Sandbox link
The Open-in-Sandbox link on the model page (a 120x32 pill, text "SandboxOpen in Sandbox" — a hidden twin ships beside it); measured, never followed. Read as `mp-sandbox-link` on the model page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 120.2 x 32; padding 0px 12px; border 1px solid rgba(255, 255, 255, 0.1) `color.stroke.strong`; radius 4px; background #202022 `palette.neutral.900`; text publicSansRounded 12/16 600, #f4f4f5 `palette.neutral.100`; transition background-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| hover | border 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.05) `badge.default.alpha` |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | size 117.8 x 31.36; border 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.05) `badge.default.alpha` |

![Open in Sandbox link default](components/crops/mp-sandbox-link-default.png) ![Open in Sandbox link hover](components/crops/mp-sandbox-link-hover.png) ![Open in Sandbox link focus-visible](components/crops/mp-sandbox-link-focus-visible.png) ![Open in Sandbox link pressed](components/crops/mp-sandbox-link-pressed.png)

#### Prompt textarea
The playground prompt field ("Write your prompt here..."); focused and typed into then cleared — inference was never run. Read as `mp-prompt` on the model page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 654 x 98; padding 8px 12px; border 1px solid rgba(255, 255, 255, 0.1) `color.stroke.strong`; radius 4px; background transparent; text publicSansRounded 14/20 400, transparent; placeholder rgba(255, 255, 255, 0.65) `color.content.lighter` |
| focused, filled | shadow #a284ff 0px 0px 0px 3px |

![Prompt textarea default](components/crops/mp-prompt-default.png) ![Prompt textarea focused](components/crops/mp-prompt-focused.png) ![Prompt textarea filled](components/crops/mp-prompt-filled.png)

#### Parameter option
A playground parameter option pill (an aspect/size choice) — a local option button; measured, never toggled. Read as `mp-param` on the model page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 192 x 40; padding 6px 12px; border 1px solid rgba(255, 255, 255, 0.1) `color.stroke.strong`; radius 4px; background #202022 `palette.neutral.900`; text publicSansRounded 14/20 600, #f4f4f5 `palette.neutral.100`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #787881 `palette.neutral.500` |
| hover | border 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.05) `badge.default.alpha` |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | border 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.05) `badge.default.alpha` |

![Parameter option default](components/crops/mp-param-default.png) ![Parameter option hover](components/crops/mp-param-hover.png) ![Parameter option focus-visible](components/crops/mp-param-focus-visible.png) ![Parameter option pressed](components/crops/mp-param-pressed.png)

#### More-params button
The "More" disclosure for extra playground parameters — a local disclosure; measured, never opened. Read as `mp-param-more` on the model page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 75.53 x 32; padding 0px 12px; border 1px solid rgba(255, 255, 255, 0.1) `color.stroke.strong`; radius 4px; background #202022 `palette.neutral.900`; text publicSansRounded 12/16 600, #f4f4f5 `palette.neutral.100`; transition background-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 16 x 16, #787881 `palette.neutral.500` |
| hover | border 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.05) `badge.default.alpha` |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | size 74.02 x 31.36; border 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.05) `badge.default.alpha`; icon 15.68 x 15.68, #787881 `palette.neutral.500` |

![More-params button default](components/crops/mp-param-more-default.png) ![More-params button hover](components/crops/mp-param-more-hover.png) ![More-params button focus-visible](components/crops/mp-param-more-focus-visible.png) ![More-params button pressed](components/crops/mp-param-more-pressed.png)

#### Sign-in-to-run button
The playground run button — it links to login signed out; measured, never activated. Read as `mp-run` on the model page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 119.05 x 40; padding 0px 16px; border 1px solid transparent; radius 4px; background #783afb `color.primary.500`; text publicSansRounded 14/20 600, #fafafa `color.neutral.50`; transition background-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| hover | background #6910e9 `color.primary.600` |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | size 116.67 x 39.2; background #6910e9 `color.primary.600` |

![Sign-in-to-run button default](components/crops/mp-run-default.png) ![Sign-in-to-run button hover](components/crops/mp-run-hover.png) ![Sign-in-to-run button focus-visible](components/crops/mp-run-focus-visible.png) ![Sign-in-to-run button pressed](components/crops/mp-run-pressed.png)

#### Result view toggle
The Preview/JSON toggle on the Result pane — a local view switch; measured, never switched. Read as `mp-result-tab` on the model page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 93.05 x 28; padding 0px 10px; radius 2px; background rgba(255, 255, 255, 0.05) `badge.default.alpha`; text publicSansRounded 14/20 600, #f4f4f5 `palette.neutral.100`; icon 16 x 16, rgba(255, 255, 255, 0.65) `color.content.lighter` |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |

![Result view toggle default](components/crops/mp-result-tab-default.png) ![Result view toggle hover](components/crops/mp-result-tab-hover.png) ![Result view toggle focus-visible](components/crops/mp-result-tab-focus-visible.png) ![Result view toggle pressed](components/crops/mp-result-tab-pressed.png)

#### Download button
The result Download button — a licensed download; measured, never pressed. Read as `mp-download` on the model page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 119.89 x 36; padding 0px 16px; border 1px solid rgba(255, 255, 255, 0.1) `color.stroke.strong`; radius 4px; background #202022 `palette.neutral.900`; text publicSansRounded 14/20 600, #f4f4f5 `palette.neutral.100`; transition background-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 16 x 16, #787881 `palette.neutral.500` |
| hover | border 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.05) `badge.default.alpha` |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | size 117.49 x 35.28; border 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.05) `badge.default.alpha`; icon 15.68 x 15.68, #787881 `palette.neutral.500` |

![Download button default](components/crops/mp-download-default.png) ![Download button hover](components/crops/mp-download-hover.png) ![Download button focus-visible](components/crops/mp-download-focus-visible.png) ![Download button pressed](components/crops/mp-download-pressed.png)

### API tab (app, dark)

The model's API tab: the request code sample with the language switch and the copy control — read-only signed out.

#### API tab (active)
The "API" tab of the model page tab bar, active (aria-selected true); measured, never switched. Read as `api-tab` on the model-api page.

**Values (default).** size 44.42 x 40; padding 4px 10px; border 1px solid transparent; radius 8px; background transparent; text publicSansRounded 14/16.8 600, #fafafa `color.neutral.50`; transition background-color 0.16s cubic-bezier(0, 0, 0.2, 1), border-color 0.16s cubic-bezier(0, 0, 0.2, 1), color 0.16s cubic-bezier(0, 0, 0.2, 1), transform 0.16s cubic-bezier(0, 0, 0.2, 1); layers ::after rgb(250, 250, 250) 0px none 1.

![API tab (active) default](components/crops/api-tab-default.png)

#### API code block
A code sample on the API tab (client subscribe / queue call). Read as `api-code` on the model-api page.

**Values (default).** size 1070 x 347; padding 16px; background transparent; text chivoMono 14/21 400, #c678dd.

![API code block default](components/crops/api-code-default.png)

#### Copy button (API)
The code-block Copy button (top-right of the first code sample); measured, never pressed. Read as `api-copy` on the model-api page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; border 1px solid transparent; radius 4px; background transparent; text publicSansRounded 14/20 600, #f4f4f5 `palette.neutral.100`; transition background-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 16 x 16, rgba(255, 255, 255, 0.5) `content.muted` |
| hover | background rgba(255, 255, 255, 0.05) `badge.default.alpha`; icon 16 x 16, #fafafa `color.neutral.50` |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | size 35.28 x 35.28; background rgba(255, 255, 255, 0.05) `badge.default.alpha`; icon 15.68 x 15.68, #fafafa `color.neutral.50` |

![Copy button (API) default](components/crops/api-copy-default.png) ![Copy button (API) hover](components/crops/api-copy-hover.png) ![Copy button (API) focus-visible](components/crops/api-copy-focus-visible.png) ![Copy button (API) pressed](components/crops/api-copy-pressed.png)

#### Language tab
A client-language tab on the API samples ("JavaScript / Node.js") — a local view switch; measured, never switched. Read as `api-lang-tab` on the model-api page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 256 x 36; padding 0px 12px; border 1px solid rgba(255, 255, 255, 0.1) `color.stroke.strong`; radius 4px; background #202022 `palette.neutral.900`; text publicSansRounded 14/20 600, #f4f4f5 `palette.neutral.100`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #787881 `palette.neutral.500` |
| hover | border 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.05) `badge.default.alpha` |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| pressed | border 1px solid rgba(255, 255, 255, 0.2) `overlay.primary.stroke`; background rgba(255, 255, 255, 0.05) `badge.default.alpha` |

![Language tab default](components/crops/api-lang-tab-default.png) ![Language tab hover](components/crops/api-lang-tab-hover.png) ![Language tab focus-visible](components/crops/api-lang-tab-focus-visible.png) ![Language tab pressed](components/crops/api-lang-tab-pressed.png)

### Login (app, dark)

The OAuth-only login card: fal mark, 'Welcome to fal', Continue-with-GitHub / Google / Microsoft, Use SSO and Contact support — no credential fields exist; nothing was submitted.

#### Login card
The OAuth-only login/signup card: fal mark, "Login or sign up", the Continue-with-* buttons and Use SSO; measured at rest, nothing followed. Read as `li-card` on the login page.

**Values (default).** size 400 x 388.91; background transparent; text focal 36/34.92 400, #f4f4f5 `palette.neutral.100`; icon 40 x 40, #f4f4f5 `palette.neutral.100`; layers a::after.inline-flex.items-center 400pxx40px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 4px; a::after.inline-flex.items-center 400pxx40px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, .

Child layers that carry the look: a::after 400pxx40px radius 4px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) `color.stroke.strong` 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px; a::after 400pxx40px radius 4px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) `color.stroke.strong` 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px; a::after 400pxx40px radius 4px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) `color.stroke.strong` 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px.

![Login card default](components/crops/li-card-default.png)

#### Login heading
"Welcome to fal" over the card. Read as `li-h1` on the login page.

**Values (default).** size 400 x 34.91; background transparent; text focal 36/34.92 400, #f4f4f5 `palette.neutral.100`.

![Login heading default](components/crops/li-h1-default.png)

#### Continue-with-GitHub button
A Continue-with-* OAuth button; measured, never followed (it starts the OAuth flow). Read as `li-oauth-github` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 40; padding 8px 16px; radius 4px; background transparent; text publicSansRounded 16/normal 600, #f4f4f5 `palette.neutral.100`; icon 16 x 16, #f4f4f5 `palette.neutral.100`; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1; a::after.inline-flex.items-center 400pxx40px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) 0px 0px 0px 1 |
| hover | background rgba(255, 255, 255, 0.05) `badge.default.alpha`; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.2) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1 |
| focus-visible | shadow #a284ff 0px 0px 0px 3px; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1; a.inline-flex.items-center 400.0x40.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 1px, rgb(162, 132, 255) 0px 0px 0px 3px, rgba(0, 0 |
| pressed | background rgba(255, 255, 255, 0.05) `badge.default.alpha`; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.2) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1 |

Child layers that carry the look: a::after 400pxx40px radius 4px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) `color.stroke.strong` 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px.

![Continue-with-GitHub button default](components/crops/li-oauth-github-default.png) ![Continue-with-GitHub button hover](components/crops/li-oauth-github-hover.png) ![Continue-with-GitHub button focus-visible](components/crops/li-oauth-github-focus-visible.png) ![Continue-with-GitHub button pressed](components/crops/li-oauth-github-pressed.png)

#### Continue-with-Google button
The Continue-with-Google OAuth button; measured, never followed. Read as `li-oauth-google` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 40; padding 8px 16px; radius 4px; background transparent; text publicSansRounded 16/normal 600, #f4f4f5 `palette.neutral.100`; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1; a::after.inline-flex.items-center 400pxx40px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) 0px 0px 0px 1 |
| hover | background rgba(255, 255, 255, 0.05) `badge.default.alpha`; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.2) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1 |
| focus-visible | shadow #a284ff 0px 0px 0px 3px; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1; a.inline-flex.items-center 400.0x40.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 1px, rgb(162, 132, 255) 0px 0px 0px 3px, rgba(0, 0 |
| pressed | background rgba(255, 255, 255, 0.05) `badge.default.alpha`; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.2) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1 |

Child layers that carry the look: a::after 400pxx40px radius 4px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) `color.stroke.strong` 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px.

![Continue-with-Google button default](components/crops/li-oauth-google-default.png) ![Continue-with-Google button hover](components/crops/li-oauth-google-hover.png) ![Continue-with-Google button focus-visible](components/crops/li-oauth-google-focus-visible.png) ![Continue-with-Google button pressed](components/crops/li-oauth-google-pressed.png)

#### Use SSO button
The Use-SSO button; measured, never followed. Read as `li-sso` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101.03 x 32; padding 0px 12px; radius 4px; background transparent; text publicSansRounded 14/14 600, rgba(255, 255, 255, 0.65) `color.content.lighter`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, #787881 `palette.neutral.500` |
| hover | background rgba(255, 255, 255, 0.05) `badge.default.alpha`; text publicSansRounded 14/14 600, #f4f4f5 `palette.neutral.100` |
| focus-visible | shadow #a284ff 0px 0px 0px 3px; layers button.focus-ring.inline-flex 101.0x32.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 1px, rgb(162, 132, 255) 0px 0px 0px 3px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 4px |
| pressed | background rgba(255, 255, 255, 0.05) `badge.default.alpha`; text publicSansRounded 14/14 600, #f4f4f5 `palette.neutral.100` |

![Use SSO button default](components/crops/li-sso-default.png) ![Use SSO button hover](components/crops/li-sso-hover.png) ![Use SSO button focus-visible](components/crops/li-sso-focus-visible.png) ![Use SSO button pressed](components/crops/li-sso-pressed.png)

#### Contact-support link
The Contact-support link under the card; measured, never followed. Read as `li-support` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 146.91 x 32; padding 4px 12px; radius 4px; background transparent; text publicSansRounded 14/normal 600, rgba(255, 255, 255, 0.65) `color.content.lighter`; icon 14 x 14, #787881 `palette.neutral.500` |
| hover | background rgba(255, 255, 255, 0.05) `badge.default.alpha` |
| focus-visible | shadow #a284ff 0px 0px 0px 3px; layers a.inline-flex.items-center 146.9x32.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 1px, rgb(162, 132, 255) 0px 0px 0px 3px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 4px |
| pressed | background rgba(255, 255, 255, 0.05) `badge.default.alpha` |

![Contact-support link default](components/crops/li-support-default.png) ![Contact-support link hover](components/crops/li-support-hover.png) ![Contact-support link focus-visible](components/crops/li-support-focus-visible.png) ![Contact-support link pressed](components/crops/li-support-pressed.png)

### Documentation (docs, light)

The fumadocs surface (/docs/documentation) on its own token layer: the tab strip, the 'Build with fal' hero, the fixed sidebar tree, section cards, the code-group samples and the on-this-page TOC.

#### Docs top bar
The docs tab strip (.nav-tabs): Documentation / Examples / Model API Reference / SDK Reference / Inference API / Platform API / Changelog. Read as `docs-topbar` on the docs page.

**Values (default).** size 966 x 47; radius 4px; background transparent; text Public Sans 14/20 500, #27262b `docs.gray.800`; layers div.absolute.bottom-0 126.0x1.5 rgb(87, 24, 192) 4px.

Child layers that carry the look: div 126x1.5 background #5718c0 `color.primary.700` radius 4px.

![Docs top bar default](components/crops/docs-topbar-default.png)

#### Docs search trigger
The "Search… Ctrl K" command trigger at the top of the sidebar — a local overlay trigger; measured, never opened. Read as `docs-search` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 232 x 36; padding 0px 12px 0px 14px; radius 4px; background #ffffff `color.white`; shadow oklab(0.705694 0.00425595 -0.00620294 / 0.3) 0px 0px 0px 1px; text Public Sans 14/24 400, #727075 `docs.gray.500`; icon 16 x 16, #413f44 `docs.gray.700` |
| hover | shadow oklab(0.434924 0.00477214 -0.00701782 / 0.3) 0px 0px 0px 1px; icon 16 x 16, #27262b `docs.gray.800` |
| focus-visible | outline 1px auto #5718c0 `color.primary.700`, offset 0px |
| pressed | shadow oklab(0.434924 0.00477214 -0.00701782 / 0.3) 0px 0px 0px 1px; icon 16 x 16, #27262b `docs.gray.800` |

![Docs search trigger default](components/crops/docs-search-default.png) ![Docs search trigger hover](components/crops/docs-search-hover.png) ![Docs search trigger focus-visible](components/crops/docs-search-focus-visible.png) ![Docs search trigger pressed](components/crops/docs-search-pressed.png)

#### Theme switcher
One segment of the light/system/dark theme control — a local display toggle; measured, never cycled (the page was captured at its light default). Read as `docs-theme-btn` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 20 x 20; radius 4px; background transparent; text Public Sans 16/24 400, #a19fa4 `docs.gray.400`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, #a19fa4 `docs.gray.400` |
| hover | text Public Sans 16/24 400, #525055 `docs.gray.600`; icon 12 x 12, #525055 `docs.gray.600` |
| focus-visible | outline 1px auto #5718c0 `color.primary.700`, offset 0px; layers button.switch-option.z-10 20.0x20.0 1px auto rgb(87, 24, 192) offset 0px 4px |
| pressed | text Public Sans 16/24 400, #525055 `docs.gray.600`; icon 12 x 12, #525055 `docs.gray.600` |

![Theme switcher default](components/crops/docs-theme-btn-default.png) ![Theme switcher hover](components/crops/docs-theme-btn-hover.png) ![Theme switcher focus-visible](components/crops/docs-theme-btn-focus-visible.png) ![Theme switcher pressed](components/crops/docs-theme-btn-pressed.png)

#### Docs nav item
A sidebar navigation item on the docs tree (a.group); measured, never followed. Read as `docs-nav-section` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 286 x 32; padding 6px 12px 6px 16px; border L: 1px solid #5718c0 `color.primary.700`; radius 4px; background transparent; text Public Sans 14/20 400, #5718c0 `color.primary.700`; layers a.group.flex 286.0x32.0 L:1px solid rgb(87, 24, 192) 4px |

Child layers that carry the look: a 286x32 border 1px solid #5718c0 `color.primary.700` radius 4px.

![Docs nav item default](components/crops/docs-nav-section-default.png) ![Docs nav item hover](components/crops/docs-nav-section-hover.png)

#### Docs heading
"Build with fal" — the docs hero heading (Focal, h1.fal-hero-title). Read as `docs-h1` on the docs page.

**Values (default).** size 309 x 112; radius 4px; background transparent; text Focal Medium 56/56 500, #242426; layers a::before.anchor-link 24pxx24px rgb(255, 255, 255) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.705694 0.00425595 -0.00620294 / 0.3) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px 6px; a::after.anchor-link 12pxx12px rgb(161, 159, 164).

Child layers that carry the look: a::before 24pxx24px background #ffffff `color.white` radius 6px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, oklab(0.705694 0.00425595 -0.00620294 / 0.3) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; a::after 12pxx12px background #a19fa4 `docs.gray.400`.

![Docs heading default](components/crops/docs-h1-default.png)

#### Docs body text
A hero/body paragraph in the docs prose (Public Sans, p.fal-hero-body). Read as `docs-prose` on the docs page.

**Values (default).** size 309 x 40; radius 4px; background transparent; text Focal Medium 20/20 500, #242426.

![Docs body text default](components/crops/docs-prose-default.png)

#### Docs section card
A section card in the docs .columns grid (Model APIs / Serverless / Compute); measured, its link never followed. Read as `docs-card` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 650 x 444; radius 4px; background transparent; text Focal 16/24 600, #27262b `docs.gray.800`; layers div.card.block 317.0x206.0 rgb(255, 255, 255) T:1px solid oklab(0.150358 0.00656244 -0.0113211 / 0.1) / R:1px solid oklab(0.150358 0.00656244 -0.0113211 / 0.1) / B:1px solid oklab(0.150358 0.00656244 -0.0113211 / 0.1) / L:1px solid oklab(0.150358 0.00656244 -0.0113211 / 0.1) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0 |

Child layers that carry the look: div 317x206 background #ffffff `color.white` border 1px solid oklab(0.150358 0.00656244 -0.0113211 / 0.1) radius 4px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 2px, transparent 0px 0px 0px 0px; a 0x0 border 1px solid #5718c0 `color.primary.700` radius 4px; svg 24x24 background #5718c0 `color.primary.700` radius 4px.

![Docs section card default](components/crops/docs-card-default.png) ![Docs section card hover](components/crops/docs-card-hover.png)

#### On-this-page TOC
The right-hand "On this page" table of contents. Read as `docs-toc` on the docs page.

**Values (default).** size 264 x 208; radius 4px; background transparent; text Focal 14/24 500, #413f44 `docs.gray.700`; icon 12 x 12, #413f44 `docs.gray.700`; layers a.text-primary.dark:text-primary-light 264.0x32.0 L:1px solid rgb(87, 24, 192) 4px; a 264.0x32.0 L:1px solid oklab(0.150358 0.00656244 -0.0113211 / 0.05) 4px; a 264.0x32.0 L:1px solid oklab(0.150358 0.00656244 -0.0113211 / 0.05) 4px; a 264.0x32.0 L:1px solid oklab(0.150358 0.00656244 -0.0113211 / 0.05) 4px.

Child layers that carry the look: a 264x32 border 1px solid #5718c0 `color.primary.700` radius 4px; a 264x32 border 1px solid oklab(0.150358 0.00656244 -0.0113211 / 0.05) radius 4px; a 264x32 border 1px solid oklab(0.150358 0.00656244 -0.0113211 / 0.05) radius 4px.

![On-this-page TOC default](components/crops/docs-toc-default.png)

#### Docs code block
A .code-group sample block in the docs (Python/JavaScript/cURL tabs). Read as `docs-code` on the docs page.

**Values (default).** size 650 x 212; padding 2px; border 1px solid oklab(0.150358 0.00656244 -0.0113211 / 0.1); radius 4px; background #f5f3f8 `docs.gray.50`; text Public Sans 12/24 500, #5718c0 `color.primary.700`; icon 16 x 16, #a19fa4 `docs.gray.400`.

![Docs code block default](components/crops/docs-code-default.png)

#### Docs tab item
A tab inside the docs tab strip; measured, never followed. Read as `docs-tab-item` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 126 x 47; background transparent; text Public Sans 14/20 500, #27262b `docs.gray.800`; layers div.absolute.bottom-0 126.0x1.5 rgb(87, 24, 192) 4px |

Child layers that carry the look: div 126x1.5 background #5718c0 `color.primary.700` radius 4px.

![Docs tab item default](components/crops/docs-tab-item-default.png) ![Docs tab item hover](components/crops/docs-tab-item-hover.png)

#### Docs hero search
The "Search or ask…" field in the docs hero — a local overlay trigger; measured, never opened. Read as `docs-hero-search` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 309 x 40.75; padding 8px 10px; border 1px solid rgba(18, 18, 22, 0.1) `color.stroke.base`; radius 4px; background #ffffff `color.white`; text Public Sans 13/22.75 400, #9ca3af; transition border-color 0.2s ease; icon 14 x 14, #787881 `palette.neutral.500` |
| hover | border 1px solid rgba(18, 18, 22, 0.2) `stroke.stronger.default` |
| focus-visible | outline 1px auto #5718c0 `color.primary.700`, offset 0px |
| pressed | border 1px solid rgba(18, 18, 22, 0.2) `stroke.stronger.default` |

![Docs hero search default](components/crops/docs-hero-search-default.png) ![Docs hero search hover](components/crops/docs-hero-search-hover.png) ![Docs hero search focus-visible](components/crops/docs-hero-search-focus-visible.png) ![Docs hero search pressed](components/crops/docs-hero-search-pressed.png)

#### Docs sidebar
The fixed docs sidebar: search, Status/Community/Blog and the grouped nav tree. Read as `docs-sidebar` on the docs page.

**Values (default).** size 350 x 900; border R: 1px solid oklab(0.906575 0.0040085 -0.00581205 / 0.7); radius 4px; background transparent; text Public Sans 14/24 400, #727075 `docs.gray.500`; icon 12 x 12, #a19fa4 `docs.gray.400`; layers nav.hidden.lg:flex 350.0x900.0 R:1px solid oklab(0.906575 0.0040085 -0.00581205 / 0.7) 4px; div.min-w-0.flex-1 350.0x811.0 rgb(247, 247, 248); div::before.min-w-0.flex-1 1440pxx811px rgb(247, 247, 248); div.flex.items-center 76.0x28.0 T:1px solid oklab(0.906575 0.0040085 -0.00581205 / 0.7) / R:1px solid oklab(0.906575 0.0040085 -0.00581205 / 0.7) / B:1px solid oklab(0.906575 0.0040085 -0.00581205 .

Child layers that carry the look: nav 350x900 border 1px solid oklab(0.906575 0.0040085 -0.00581205 / 0.7) radius 4px; div 350x811 background #f7f7f8; div::before 1440pxx811px background #f7f7f8.

![Docs sidebar default](components/crops/docs-sidebar-default.png)

#### Docs code-copy button
The Copy button on a docs code block; measured, never pressed. Read as `docs-code-copy` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 26 x 26; radius 4px; background transparent; text Public Sans 16/28 400, #0c0a10 `docs.gray.950`; icon 16 x 16, #a19fa4 `docs.gray.400` |
| hover | icon 16 x 16, #727075 `docs.gray.500` |
| focus-visible | outline 1px auto #5718c0 `color.primary.700`, offset 0px; layers button.size-6.5.flex 26.0x26.0 1px auto rgb(87, 24, 192) offset 0px 4px |
| pressed | icon 16 x 16, #727075 `docs.gray.500` |

![Docs code-copy button default](components/crops/docs-code-copy-default.png) ![Docs code-copy button hover](components/crops/docs-code-copy-hover.png) ![Docs code-copy button focus-visible](components/crops/docs-code-copy-focus-visible.png) ![Docs code-copy button pressed](components/crops/docs-code-copy-pressed.png)

### Mobile (390 wide)

The app surface at 390 wide: the 48px top bar, the hamburger that opens the vaul bottom-sheet nav, and the model cards at phone width.

#### Mobile header
The phone top bar (header.dashboard-navigation-header): fal mark and the "Open navigation" trigger. Read as `m-header` on the explore page at 390 wide.

**Values (default).** size 390 x 48; background transparent; text publicSansRounded 14/normal 600, #f4f4f5 `palette.neutral.100`; icon 20 x 20, #ffffff `color.white`; layers div.dashboard-navigation-surface 390.0x48.0 rgb(25, 25, 26) B:1px solid rgba(255, 255, 255, 0.05); div.dashboard-navigation-seam 0.0x0.0 B:1px solid rgba(255, 255, 255, 0.05); button.inline-flex.items-center 48.0x32.0 rgb(32, 32, 34) 4px; button::after.inline-flex.items-center 48pxx32px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, .

Child layers that carry the look: div 390x48 background #19191a `palette.neutral.950` border 1px solid rgba(255, 255, 255, 0.05) `badge.default.alpha`; div 0x0 border 1px solid rgba(255, 255, 255, 0.05) `badge.default.alpha`; button 48x32 background #202022 `palette.neutral.900` radius 4px.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu trigger
The "Open navigation" icon button — a local disclosure; the opened state was measured after clicking it. Read as `m-hamburger` on the explore page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 32; radius 4px; background #202022 `palette.neutral.900`; text publicSansRounded 14/normal 600, #f4f4f5 `palette.neutral.100`; icon 16 x 16, #f4f4f5 `palette.neutral.100`; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1 |
| focus-visible | shadow #a284ff 0px 0px 0px 3px |
| opened | background rgba(255, 255, 255, 0.05) `badge.default.alpha`; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.2) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1 |

![Mobile menu trigger default](components/crops/m-hamburger-default.png) ![Mobile menu trigger hover](components/crops/m-hamburger-hover.png) ![Mobile menu trigger focus-visible](components/crops/m-hamburger-focus-visible.png) ![Mobile menu trigger pressed](components/crops/m-hamburger-pressed.png) ![Mobile menu trigger opened](components/crops/m-hamburger-opened.png)

#### Mobile nav link
A menuitem row inside the opened vaul bottom-sheet nav; measured, never followed. Read as `m-nav-item` on the explore page at 390 wide.

**Values (default).** size 499 x 32; padding 12px 16px; radius 4px; background transparent; text publicSansRounded 14/20 400, #f4f4f5 `palette.neutral.100`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(255, 255, 255, 0.8) `badge.default.foreground`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile search field
The model search field at phone width. Read as `m-search` on the explore page at 390 wide.

**Values (default).** size 206.95 x 19.99; background transparent; shadow rgba(255, 255, 255, 0.8) 0px 0px 0px 0px; text publicSansRounded 16/22.85 400, rgba(255, 255, 255, 0.8) `badge.default.foreground`; placeholder rgba(255, 255, 255, 0.8) `badge.default.foreground`; layers input.flex.min-w-0 207.0x20.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.8) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px.

![Mobile search field default](components/crops/m-search-default.png)

#### Mobile model card
A model tile (a.page-model-card) in the phone catalog grid. Read as `m-model-card` on the explore page at 390 wide.

**Values (default).** size 283.19 x 307.28; background transparent; text publicSansRounded 12/18 600, #163200 `color.lime.950`; icon 12 x 12, #163200 `color.lime.950`; layers div::after.flex.h-full 283.188pxx307.281px T:1px solid rgba(255, 255, 255, 0.1) / R:1px solid rgba(255, 255, 255, 0.1) / B:1px solid rgba(255, 255, 255, 0.1) / L:1px solid rgba(255, 255, 255, 0.1) 4px; div.relative.aspect-[16/9] 283.2x159.3; div.badge.badge-role-lime 44.6x16.0 rgb(162, 216, 28) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid.

Child layers that carry the look: div::after 283.188pxx307.281px border 1px solid rgba(255, 255, 255, 0.1) `color.stroke.strong` radius 4px; div 283.2x159.3 image linear-gradient(to right in oklab, rgba(255, 255, 255, 0.03) `badge.ghost` 0%, rgba(255, 2; div 44.6x16 background #a2d81c `color.lime.500` border 1px solid transparent radius 4px.

![Mobile model card default](components/crops/m-model-card-default.png)

### Footer

The page footers: link columns, socials and legal.

#### Marketing footer
The marketing page footer (section.is-footer): link columns, socials, legal. Read as `mkt-footer` on the home page.

**Values (default).** size 1440 x 537.22; padding 17.1429px; background #ffc4d8 `marketing.brand.pink`; text Focal Web 15.2/19.15 500, #000000 `color.black`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Marketing footer default](components/crops/mkt-footer-default.png)

#### App footer
The app page footer: product/learn/social columns, legal and privacy links. Read as `app-footer` on the model page.

**Values (default).** size 1440 x 886.19; padding 32px; background transparent; text focal 30/36 500, #fafafa `color.neutral.50`; layers a.inline-flex.items-center 144.9x44.0 rgb(250, 250, 250) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 4px; div.shrink-0.bg-stroke-base 1440.0x1.0 rgba(255, 255, 255, 0.05).

Child layers that carry the look: a 144.9x44 background #fafafa `color.neutral.50` border 1px solid transparent radius 4px; div 1440x1 background rgba(255, 255, 255, 0.05) `badge.default.alpha`.

![App footer default](components/crops/app-footer-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the fal wordmark, the model-card publisher marks, the badge and nav glyphs, the social icons) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The signed-in fal product lives behind /login — the dashboard, API keys, billing, real playground runs, the sandbox and deployments all need an account and were never reached. /explore, /models/* and /docs/* are genuinely public signed-out surfaces; the playground's run button is a Sign-in-to-run link signed out, so what a real inference looks like is unverified.

### Pages

- **The account.** Every post-login surface was never reached; the OAuth buttons and Use SSO were measured, never followed.
- **Inference.** No model was ever run — Sign in to run links to login signed out, and the prompt was typed into then cleared.
- **Checkout and sales.** Every Get Started, Contact Sales and pricing action was measured, never followed.
- **Edge challenge.** The model route intermittently serves a security-verification interstitial to headless browsers (the light-theme model capture is a default shot only); a blocked pass never erases earlier readings.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover), so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

fal.ai paints three surfaces: the single-theme Webflow marketing pages, the Next.js app whose html.light|html.dark class follows prefers-color-scheme (no user toggle signed out), and the fumadocs docs on their own layer with a light/system/dark control — so tokens.json keeps real light and dark sets (light resolves the app-light values with the marketing and docs-light passes folded in for surface-only names).

### Fonts

- **Public Sans Rounded** (all app UI text and controls), **Focal** (product headings; Focal Web / Focal Text on the marketing pages, Focal in the docs), **Chivo Mono** and **halMono** (code and mono labels), **Hal** (serif accents), **Public Sans** (docs body) and **Paper Mono** (docs code) are the declared faces. The app --font-* stacks are next/font stacks whose var() chains only resolve on the live html — the emitted stacks are the declared raw values; the style guide falls back to system sans.

### Screenshots

- The model names, publisher artwork, the fal wordmark and any photography in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Model names, publisher marks and catalog artwork are the product's content; only frames and components were measured. The OAuth login card is the product's own branded form; nothing was entered into it beyond a cleared sample string in the local prompt field.
