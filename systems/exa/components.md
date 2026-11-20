# Exa components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from exa.ai, auth.exa.ai and exa.ai/docs on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the sign-in e-mail and the demo query fields were focused and filled for measurement, then cleared, and never sent; the demo's Run-preview arrow, every Get-started/Sign-up action and the login buttons were never pressed, and the demo widget's pills were toggled only as local preview configuration. The dashboard, API keys and playground behind login were never reached.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (70 components, 163 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (153 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`: marketing and sign-in surfaces paint `light`; the docs' dark-mode pages are the `*-dark-dark-*` files. Desktop shots are 1440 x 900 at DPR 2 (256-colour PNGs); `-full` shots are whole pages, chunked and stitched; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home (marketing) | `exa.ai/` | [default](screenshots/home-light-default.png), [demo-tabs](screenshots/home-light-demo-tabs.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Pricing | `exa.ai/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [usecase-chatbots](screenshots/pricing-light-usecase-chatbots.png) |
| Search API product | `exa.ai/products/search` | [default](screenshots/product-light-default.png), [full](screenshots/product-light-full.png) |
| About | `exa.ai/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Blog | `exa.ai/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Demos | `exa.ai/demos` | [default](screenshots/demos-light-default.png), [full](screenshots/demos-light-full.png) |
| Evals | `exa.ai/evals` | [default](screenshots/evals-light-default.png), [full](screenshots/evals-light-full.png) |
| Brand | `exa.ai/brand` | [default](screenshots/brand-light-default.png), [full](screenshots/brand-light-full.png) |
| Customers | `exa.ai/customers` | [default](screenshots/customers-light-default.png), [full](screenshots/customers-light-full.png) |
| Versus | `exa.ai/versus` | [default](screenshots/versus-light-default.png), [full](screenshots/versus-light-full.png) |
| Sign in | `dashboard.exa.ai/ → auth.exa.ai` | [default](screenshots/signin-light-default.png) |
| Websets | `websets.exa.ai/websets` | [default](screenshots/websets-light-default.png) |
| Docs (light) | `exa.ai/docs` | [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png) |
| Docs: quickstart | `exa.ai/docs/quickstart` | [default](screenshots/docs-ref-light-default.png), [full](screenshots/docs-ref-light-full.png) |
| Docs (dark) | `exa.ai/docs, dark` | [default](screenshots/docs-dark-dark-default.png), [full](screenshots/docs-dark-dark-full.png) |
| Home, phone | `exa.ai/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `exa.ai/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Sign-in, phone | `dashboard.exa.ai/ → auth.exa.ai` | [default](screenshots/mobile-signin-light-default.png) |
| Docs dark, phone | `exa.ai/docs, dark` | [default](screenshots/mobile-docs-dark-dark-default.png), [full](screenshots/mobile-docs-dark-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Products mega-menu | exa.ai header | a real pointer hover on the 'Products' trigger — a local open, its links never followed | [home-light-menu](screenshots/home-light-menu.png), [mkt-menu](#products-mega-menu), [mkt-menu-item](#mega-menu-link) |
| Demo widget pills | exa.ai home | the LATENCY/CATEGORY/OUTPUT pills' own toggles — they re-configure the preview, never fire it | [home-light-demo-tabs](screenshots/home-light-demo-tabs.png), [demo-pill](#latency-pill), [demo-category](#category-pill), [demo-output-tab](#output-tab) |
| Pricing use-case pills | exa.ai/pricing | the scenario pill's own toggle | [pricing-light-usecase-chatbots](screenshots/pricing-light-usecase-chatbots.png), [pricing-pill](#use-case-pill) |
| Mobile nav drawer | home, phone width | the hamburger's own toggle | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-drawer](#mobile-nav-drawer) |
| Input fields | sign-in card, demo and assistant | focused and filled with test text, then cleared — never submitted or sent | [auth-email](#email-field), [demo-textarea](#demo-query-field), [docs-assistant](#assistant-field) |
| Docs theme | exa.ai/docs | html.dark painted by the capture context (prefers-color-scheme), never through the theme menu | the `d-docs-*` entries and `docs-dark` shots |
| Demo request | exa.ai home | the Run-preview arrow would fire a real search; the widget could not verify the headless browser either way | boundary; [demo-output](#demo-output-panel) shows its honest resting state |
| Signed-in product | dashboard.exa.ai / post-login | every post-login surface needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 23 components were given a real keyboard focus. 15 draw an outline ring: `mkt-nav-link` (1px auto #101010, offset 1px), `mkt-signin` (1px auto #101010, offset 1px), `mkt-sales` (1px auto #101010, offset 1px), `mkt-signup` (1px auto #101010, offset 1px), `hero-cta` (1px auto #101010, offset 1px), `plan-cta` (1px auto #101010, offset 1px), `prod-cta` (1px auto #101010, offset 1px), `docs-theme-btn` (1px auto #1840ed `color.docs.primary`, offset 0px), `docs-nav-item` (1px auto #1840ed `color.docs.primary`, offset -2px), `docs-link` (1px auto #1840ed `color.docs.primary`, offset 1px), `d-docs-theme-btn` (1px auto #5f7cff `color.docs.primary-light`, offset 0px), `d-docs-nav-item` (1px auto #5f7cff `color.docs.primary-light`, offset -2px), `d-docs-link` (1px auto #5f7cff `color.docs.primary-light`, offset 1px), `docs-topbar-cta` (1px auto #1840ed `color.docs.primary`, offset 1px), `d-docs-topbar-cta` (1px auto #5f7cff `color.docs.primary-light`, offset 1px). 2 draw a focus ring as a shadow instead: `docs-search`, `d-docs-search`. The other 6 show no measured change: `demo-mode`, `demo-pill`, `demo-category`, `pricing-pill`, `auth-google`, `m-hamburger`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.2, 0, 0, 1)` | transform | d-docs-search, d-docs-topbar-cta, docs-search, docs-topbar-cta |
| 0.1s | `cubic-bezier(0.4, 0, 0.2, 1)` | all, rotate, scale, transform, translate | auth-google, d-docs-sidebar, docs-sidebar, mkt-menu |
| 0.14s | `cubic-bezier(0.4, 0, 0.2, 1)` | border-color, color | pricing-pill |
| 0.15s | `cubic-bezier(0.2, 0, 0, 1)` | background-color, color | d-docs-nav-item, docs-nav-item |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | demo-category, demo-mode, demo-pill, hero-cta, m-hamburger, mkt-nav-link, mkt-nav-trigger, mkt-sales and more |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | auth-email-btn, demo-run |
| 0.22s | `cubic-bezier(0.2, 0, 0, 1)` | border-color, color | d-docs-search, docs-search |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan grid](#plan-grid) | 1216 x 957.7 | 1px solid rgba(215, 217, 222, 0.7) | - | transparent | none | 0 |
| [Products mega-menu](#products-mega-menu) | 380 x 485 | - | - | transparent | none | 0 |
| [Login card](#login-card) | 360 x 98 | - | - | transparent | none | 0 |
| [Search demo widget](#search-demo-widget) | 700 x 342 | - | - | transparent | none | 0 |
| [CTA banner](#cta-banner) | 224.92 x 65.59 | - | - | transparent | none | 0 |
| [Mobile nav drawer](#mobile-nav-drawer) | 390 x 844 | - | - | #ffffff `color.secondary.default` | rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px | 0 |
| [Docs sidebar](#docs-sidebar) | 288 x 844 | R: 1px solid #eeeff5 `color.docs.gray.100` | - | transparent | none | 0 |

## Components

### Marketing chrome

The exa.ai header: the 55px bar under the Exa 3.0 announcement strip, with the exa wordmark, the Products/Solutions/Resources hover menus, Docs, Pricing, Sign in, Contact sales and the black Sign-up pill.

#### Marketing header
The sticky top bar: wordmark, Products/Solutions/Resources hover menus, Docs, Pricing, Sign in, Contact sales and Sign up, under the Exa 3.0 announcement strip. Read as `mkt-header` on the marketing home page.

**Values (default).** size 1425 x 55; background #ffffff `color.secondary.default`; text ABCDiatype 15/21 400, #5f5a54.

![Marketing header default](components/crops/mkt-header-default.png)

#### Announcement strip
The "Introducing Exa 3.0" banner over the header, with a Learn-more link and a dismiss button (never pressed). Read as `mkt-announce` on the marketing home page.

**Values (default).** size 500 x 20; background transparent; text ABCDiatype 14/20 500, #0972d5.

![Announcement strip default](components/crops/mkt-announce-default.png)

#### Logo
The exa wordmark at the left of the header. Read as `mkt-logo` on the marketing home page.

**Values (default).** size 70.42 x 17; padding 0px 16px 0px 0px; background transparent; text Inter 24/24 400, #1f40ed `color.brand.default`.

![Logo default](components/crops/mkt-logo-default.png)

#### Products menu trigger
The header "Products" item; the mega-menu opens on a real pointer hover, never a click. Read as `mkt-nav-trigger` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 96.61 x 32; padding 4px 12px; radius 4px; background transparent; text ABCDiatype 15/21 400, #5f5a54; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, #5f5a54 |
| hover | background #f3f4f6; text ABCDiatype 15/21 400, #000000 `color.neutral.black`; icon 12 x 12, #000000 `color.neutral.black` |

![Products menu trigger default](components/crops/mkt-nav-trigger-default.png) ![Products menu trigger hover](components/crops/mkt-nav-trigger-hover.png)

#### Products mega-menu
The dropdown the "Products" hover opens: Search/Contents/Agent/Monitors APIs, Exa Snapshot and Library, integrations and use cases — a local toggle, its links never followed. Read as `mkt-menu` on the marketing home page.

**Values (default).** size 380 x 485; background transparent; text Inter 14/18.2 500, #111827 `color.text.light-default`; transition all 0.1s cubic-bezier(0.4, 0, 0.2, 1); transform matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0.19, 0, 1, -0.001, -190, 0, 0, 1); icon 18 x 18, #374151; layers div.overflow-hidden.rounded-[8px] 380.0x475.0 rgb(255, 255, 255) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px 1px solid rgba(0, 0, 0, 0.08) offset 0px 8px; div.mt-0.5.flex 32.0x32.0 rgb(241, 242, 244) 7px; div.mt-0.5.flex 32.0x32.0 rgb(241, 242, 244) 7px; div.mt-0.5.flex 32.0x32.0 rgb(241, 242, 244) 7.

Child layers that carry the look: div 380x475 background #ffffff `color.secondary.default` radius 8px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px; div 32x32 background #f1f2f4 radius 7px; div 32x32 background #f1f2f4 radius 7px.

![Products mega-menu default](components/crops/mkt-menu-default.png)

#### Mega-menu link
One product link inside the open mega-menu; measured, never followed. Read as `mkt-menu-item` on the marketing home page.

**Values (default).** size 364 x 56.06; padding 10px 12px; radius 8px; background transparent; text Inter 14/18.2 500, #111827 `color.text.light-default`; icon 18 x 18, #374151; layers div.mt-0.5.flex 32.0x32.0 rgb(241, 242, 244) 7px.

Child layers that carry the look: div 32x32 background #f1f2f4 radius 7px.

![Mega-menu link default](components/crops/mkt-menu-item-default.png)

#### Nav link
A marketing header link (Docs/Pricing); measured, never followed. Read as `mkt-nav-link` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 58 x 32; padding 4px 12px; radius 4px; background transparent; text ABCDiatype 15/24 400, #5f5a54; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f3f4f6; text ABCDiatype 15/24 400, #000000 `color.neutral.black` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.flex.h-8 58.0x32.0 1px auto rgb(16, 16, 16) offset 1px 4px |
| pressed | background #f3f4f6; text ABCDiatype 15/24 400, #000000 `color.neutral.black` |

![Nav link default](components/crops/mkt-nav-link-default.png) ![Nav link hover](components/crops/mkt-nav-link-hover.png) ![Nav link focus-visible](components/crops/mkt-nav-link-focus-visible.png) ![Nav link pressed](components/crops/mkt-nav-link-pressed.png)

#### Sign-in link
The header "Sign in" link to dashboard.exa.ai; measured, never followed. Read as `mkt-signin` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 72 x 33; padding 6px 12px; radius 4px; background transparent; text Inter 14/21 500, #5f5a54; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f3f4f6; text Inter 14/21 500, #000000 `color.neutral.black` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.signed-out-only.font-inter 72.0x33.0 1px auto rgb(16, 16, 16) offset 1px 4px |
| pressed | background #f3f4f6; text Inter 14/21 500, #000000 `color.neutral.black` |

![Sign-in link default](components/crops/mkt-signin-default.png) ![Sign-in link hover](components/crops/mkt-signin-hover.png) ![Sign-in link focus-visible](components/crops/mkt-signin-focus-visible.png) ![Sign-in link pressed](components/crops/mkt-signin-pressed.png)

#### Contact-sales link
The bordered "Contact sales" button-link; measured, never followed. Read as `mkt-sales` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 121 x 33; padding 6px 12px; radius 4px; background #f2f0ef; text Inter 14/21 500, #514837; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #e8e6e5 |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #e8e6e5 |

![Contact-sales link default](components/crops/mkt-sales-default.png) ![Contact-sales link hover](components/crops/mkt-sales-hover.png) ![Contact-sales link focus-visible](components/crops/mkt-sales-focus-visible.png) ![Contact-sales link pressed](components/crops/mkt-sales-pressed.png)

#### Sign-up button
The black "Sign up" pill — the header's one filled action; measured, never followed. Read as `mkt-signup` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 69.05 x 31.59; padding 6px 12px; radius 4px; background #000000 `color.neutral.black`; text ABCDiatype 14/19.6 500, #ffffff `color.secondary.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #1f2937 |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #1f2937 |

![Sign-up button default](components/crops/mkt-signup-default.png) ![Sign-up button hover](components/crops/mkt-signup-hover.png) ![Sign-up button focus-visible](components/crops/mkt-signup-focus-visible.png) ![Sign-up button pressed](components/crops/mkt-signup-pressed.png)

### Home hero and search demo

The 'The world's data for AI agents' hero and the live search-demo widget below it: the Arizona display, the 'Try API for free' pill, the Search/Agent mode toggle, the LATENCY and CATEGORY pills, the OUTPUT tabs, the blue Run-preview arrow and the output panel's signed-out state.

#### Hero headline
"The world's data for AI agents" — the ABC Arizona Flare display. Read as `hero-h1` on the marketing home page.

**Values (default).** size 757.14 x 45.5; background transparent; text Arizona 63.2/45.50 400, #111827 `color.text.light-default`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero sub
"Search the largest index of public web and private information." Read as `hero-sub` on the marketing home page.

**Values (default).** size 757.14 x 25.77; background transparent; text ABCDiatype 18.4/25.76 400, #6b7280 `color.text.dark-faint`.

![Hero sub default](components/crops/hero-sub-default.png)

#### Try-API CTA
The black "Try API for free" button under the hero copy; measured never pressed (it leads to sign-up). Read as `hero-cta` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 124.2 x 40; padding 0px 16px; radius 4px; background #000000 `color.neutral.black`; text ABCDiatype 15/21 500, #ffffff `color.secondary.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #1f2937 |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #1f2937 |

![Try-API CTA default](components/crops/hero-cta-default.png) ![Try-API CTA hover](components/crops/hero-cta-hover.png) ![Try-API CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Try-API CTA pressed](components/crops/hero-cta-pressed.png)

#### Search demo widget
The interactive preview card under the hero: query field, Search/Agent modes, latency and category pills, output tabs and a result panel that asks the visitor to sign in when the request cannot run. Read as `demo-widget` on the marketing home page.

**Values (default).** size 700 x 342; background transparent; text ABCDiatype 16/24 400, #111827 `color.text.light-default`; icon 14 x 14, #000000 `color.neutral.black`; layers div 700.0x82.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px 1px solid rgba(0, 0, 0, 0.08) offset 0px 12px; textarea.block.w-full 672.0x24.0 2px solid rgba(0, 0, 0, 0) offset 2px; div.relative.inline-flex 180.0x31.6 rgb(242, 241, 240) rgba(0, 0, 0, 0.04) 0px 0px 0px 1px inset 6px; div.pointer-events-none.absolute 86.0x27.6 rgb(255, 255, 255) rgba(0, .

Child layers that carry the look: div 700x82 background #ffffff `color.secondary.default` radius 12px shadow rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px; textarea 672x24; div 180x31.6 background #f2f1f0 radius 6px shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 1px inset.

![Search demo widget default](components/crops/demo-widget-default.png)

#### Demo query field
The "Find anything…" query box, pre-filled with "Latest open source LLMs"; focused and typed into then restored — the preview was never run. Read as `demo-textarea` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 672 x 24; background transparent; outline 2px solid transparent, offset 2px; text ABCDiatype 16/24 400, #111827 `color.text.light-default`; placeholder rgba(0, 0, 0, 0.4); layers textarea.block.w-full 672.0x24.0 2px solid rgba(0, 0, 0, 0) offset 2px |

Child layers that carry the look: textarea 672x24.

![Demo query field default](components/crops/demo-textarea-default.png) ![Demo query field focused](components/crops/demo-textarea-focused.png) ![Demo query field filled](components/crops/demo-textarea-filled.png)

#### Demo mode toggle
The Search/Agent segmented control at the top of the demo; measured, never pressed. Read as `demo-mode` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 86 x 27.59; padding 4px 8px 4px 6px; background transparent; text ABCDiatype 14/19.6 400, #000000 `color.neutral.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, #000000 `color.neutral.black` |

![Demo mode toggle default](components/crops/demo-mode-default.png) ![Demo mode toggle hover](components/crops/demo-mode-hover.png) ![Demo mode toggle focus-visible](components/crops/demo-mode-focus-visible.png) ![Demo mode toggle pressed](components/crops/demo-mode-pressed.png)

#### Latency pill
A LATENCY pill (Lite 300ms / Auto 1s / Deep ~10s); switching it only re-configures the preview, never fires a request. Read as `demo-pill` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 71.33 x 22.8; padding 3px 7px; background transparent; text ABCDiatype 12/16.8 400, rgba(0, 0, 0, 0.45); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | text ABCDiatype 12/16.8 400, rgba(0, 0, 0, 0.6) |

![Latency pill default](components/crops/demo-pill-default.png) ![Latency pill hover](components/crops/demo-pill-hover.png) ![Latency pill focus-visible](components/crops/demo-pill-focus-visible.png) ![Latency pill pressed](components/crops/demo-pill-pressed.png)

#### Category pill
A CATEGORY pill (Full Web / News / Companies / Research / People / Financials); local toggle only. Read as `demo-category` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 72.66 x 22.8; padding 3px 7px; radius 4px; background #ffffff `color.secondary.default`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.08) 0px 1px 2px 0px, rgba(0, 0, 0, 0.06) 0px 4px 12px 0px; text ABCDiatype 12/16.8 400, #000000 `color.neutral.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

![Category pill default](components/crops/demo-category-default.png) ![Category pill hover](components/crops/demo-category-hover.png) ![Category pill focus-visible](components/crops/demo-category-focus-visible.png) ![Category pill pressed](components/crops/demo-category-pressed.png)

#### Output tab
A Results/Answer/Structured output tab; local toggle only. Read as `demo-output-tab` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40.19 x 18.19; background transparent; text ABCDiatype 13/18.2 400, #000000 `color.neutral.black` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Output tab default](components/crops/demo-output-tab-default.png) ![Output tab hover](components/crops/demo-output-tab-hover.png) ![Output tab pressed](components/crops/demo-output-tab-pressed.png)

#### Run-preview button
The blue arrow button that would fire the demo request; measured at rest and hovered — never pressed. Read as `demo-run` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 32; radius 8px; background #d1d5db `color.text.dark-muted`; text ABCDiatype 16/24 400, #ffffff `color.secondary.default`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #ffffff `color.secondary.default` |

![Run-preview button default](components/crops/demo-run-default.png) ![Run-preview button hover](components/crops/demo-run-hover.png)

#### Demo output panel
The output area's signed-out state: "We couldn't verify your browser … Sign in to continue" — the widget's honest resting state in a headless browser. Read as `demo-output` on the marketing home page.

**Values (default).** size 401 x 32.19; background transparent; text ABCDiatype 11.5/16.1 400, rgba(0, 0, 0, 0.6).

![Demo output panel default](components/crops/demo-output-default.png)

### Pricing

The /pricing page: the heading, the use-case scenario pills and the plan cards with their Get-started actions.

#### Plan grid
The pricing plans table (STARTER Free / DEVELOPER Pay as you go / ENTERPRISE Custom): a row-divided grid rather than three independent card divs — the smallest node still holding a tier label and its action. Read as `plan-card` on the pricing page.

**Values (default).** size 1216 x 957.7; border 1px solid rgba(215, 217, 222, 0.7); background transparent; text ABCDiatype 12.8/17.92 500, rgba(255, 255, 255, 0.85); icon 16 x 16, #000000 `color.neutral.black`.

![Plan grid default](components/crops/plan-card-default.png)

#### Plan price
A plan card's price line ("Free" / "Pay as you go" / "Custom"). Read as `plan-price` on the pricing page.

**Values (default).** size 324.66 x 37.59; background transparent; text Arizona 37.6/37.6 400, #ffffff `color.secondary.default`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan card's action ("Start building for free" / "Get an API key" / "Talk to sales"); measured never pressed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 372.66 x 43.61; padding 10px 20px; radius 6px; background #000000 `color.neutral.black`; text ABCDiatype 14.4/21.6 500, #ffffff `color.secondary.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #1f1f1f |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #1f1f1f |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Use-case pill
A pricing scenario pill (Coding agents / Chatbots / …); its own toggle switches the estimate — a local control, never a form post. Read as `pricing-pill` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, opened) | size 111.53 x 30.64; padding 5.44px 9.28px; border 1px solid rgba(17, 17, 17, 0.12); radius 6px; background transparent; text GeistMono 11.84/17.76 500, #4b5563; transition border-color 0.14s cubic-bezier(0.4, 0, 0.2, 1), color 0.14s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | text GeistMono 11.84/17.76 500, #000000 `color.neutral.black` |

![Use-case pill default](components/crops/pricing-pill-default.png) ![Use-case pill hover](components/crops/pricing-pill-hover.png) ![Use-case pill focus-visible](components/crops/pricing-pill-focus-visible.png) ![Use-case pill pressed](components/crops/pricing-pill-pressed.png) ![Use-case pill opened](components/crops/pricing-pill-opened.png)

#### Pricing headline
"Start searching for free" — the pricing page heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 1216 x 47.03; background transparent; text Arizona 48/47.04 400, #000000 `color.neutral.black`.

![Pricing headline default](components/crops/pricing-h1-default.png)

#### FAQ item
A pricing FAQ row if the page ships one. Read as `faq` on the pricing page.

Not on the page when it was captured.

#### Plan feature row
A checkmarked "Includes:" feature row inside a plan card. Read as `plan-includes` on the pricing page.

**Values (default).** size 372.66 x 22.39; background transparent; text ABCDiatype 16/22.4 400, #000000 `color.neutral.black`; icon 16 x 16, #000000 `color.neutral.black`.

![Plan feature row default](components/crops/plan-includes-default.png)

### Product pages

The /products/search page: its heading, code sample and call to action.

#### Product headline
The /products/search page heading. Read as `prod-h1` on the products/search page.

**Values (default).** size 850 x 119.59; background transparent; text Arizona 52/59.8 400, #111827 `color.text.light-default`.

![Product headline default](components/crops/prod-h1-default.png)

#### Code sample
A code block on the product page (the API examples). Read as `prod-code` on the products/search page.

Not on the page when it was captured.

#### Product CTA
A product-page call to action; measured never followed. Read as `prod-cta` on the products/search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 90 x 38.5; padding 8px 16px; radius 4px; background #000000 `color.neutral.black`; text Inter 15/22.5 500, #ffffff `color.secondary.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #1f2937 |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #1f2937 |

![Product CTA default](components/crops/prod-cta-default.png) ![Product CTA hover](components/crops/prod-cta-hover.png) ![Product CTA focus-visible](components/crops/prod-cta-focus-visible.png) ![Product CTA pressed](components/crops/prod-cta-pressed.png)

#### Feature section
An alternating feature block ("Search the public web and proprietary data through one API") with its framed visual card. Read as `prod-feature` on the products/search page.

**Values (default).** size 1425 x 2496; padding 96px 24px; background transparent; text Arizona 41.6/45.76 400, #181818; icon 16 x 16, #52525b; layers a.inline-flex.items-center 150.0x40.5 rgb(255, 255, 255) T:1px solid rgba(9, 9, 11, 0.14) / R:1px solid rgba(9, 9, 11, 0.14) / B:1px solid rgba(9, 9, 11, 0.14) / L:1px solid rgba(9, 9, 11, 0.14) 4px; div.Illustration_root__NRGQe.flex 620.0x516.0 rgb(243, 243, 241); div.absolute.inset-0 520.0x420.0 rgb(243, 243, 241); div.Scene_card__Kth0v.shrink-0 496.0x76.0 rgb(255, 255, 255) T:1px solid rgb(228,.

Child layers that carry the look: a 150x40.5 background #ffffff `color.secondary.default` border 1px solid rgba(9, 9, 11, 0.14) `color.docs.vars.sidebar-search-border` radius 4px; div 620x516 background #f3f3f1 image radial-gradient(rgba(24, 24, 27, 0.07) 1px, transparent 1px); div 520x420 background #f3f3f1 image radial-gradient(rgba(24, 24, 27, 0.07) 1px, transparent 1px).

![Feature section default](components/crops/prod-feature-default.png)

### Sign in (auth.exa.ai)

The signed-out login card dashboard.exa.ai redirects to on auth.exa.ai: 'Start building with Exa', the Continue-with-Google and Continue-with-email buttons, the e-mail field, the SSO link and the code sample — measured, never submitted.

#### Login card
The "Start building with Exa" sign-in card on auth.exa.ai: heading, Continue-with-Google and Continue-with-email buttons, the e-mail field, SSO link and a code sample — measured, never submitted. Read as `auth-card` on the auth.exa.ai sign-in page.

**Values (default).** size 360 x 98; background transparent; text ABC Diatype Unlicensed Trial 16/32 400, #ffffff `color.secondary.default`; icon 16 x 16, lab(65.9269 -0.832707 -8.17473); layers input.jsx-38cf25ff465a5e1d.placeholder:text-gray-400 360.0x44.0 T:1px solid rgb(224, 224, 224) / R:1px solid rgb(224, 224, 224) / B:1px solid rgb(224, 224, 224) / L:1px solid rgb(224, 224, 224) 4px; button.jsx-38cf25ff465a5e1d.h-11 360.0x44.0 rgb(31, 64, 237) 4px.

Child layers that carry the look: input 360x44 border 1px solid #e0e0e0 radius 4px; button 360x44 background #1f40ed `color.brand.default` radius 4px.

![Login card default](components/crops/auth-card-default.png)

#### Login heading
"Start building with Exa". Read as `auth-heading` on the auth.exa.ai sign-in page.

**Values (default).** size 300.28 x 32; background transparent; text ABC Arizona Flare 32/32 400, #1a1a1a `color.auth.text-light.default`.

![Login heading default](components/crops/auth-heading-default.png)

#### Google button
The "Continue with Google" OAuth button; measured never pressed. Read as `auth-google` on the auth.exa.ai sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 360 x 50; padding 24px; border 1px solid #e0e0e0; radius 4px; background #ffffff `color.secondary.default`; shadow rgba(137, 102, 26, 0.2) 0px 2px 3px -1px; text ABC Diatype Unlicensed Trial 16/24 500, #000000 `color.neutral.black`; transition all 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #171717 `color.gray.900` |
| hover, pressed | background #f9f9f9 |

![Google button default](components/crops/auth-google-default.png) ![Google button hover](components/crops/auth-google-hover.png) ![Google button focus-visible](components/crops/auth-google-focus-visible.png) ![Google button pressed](components/crops/auth-google-pressed.png)

#### Email button
The "Continue with email" button; measured never pressed. Read as `auth-email-btn` on the auth.exa.ai sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 360 x 44; radius 4px; background #1f40ed `color.brand.default`; text ABC Diatype Unlicensed Trial 16/32 400, #ffffff `color.secondary.default`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.5 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Email button default](components/crops/auth-email-btn-default.png) ![Email button hover](components/crops/auth-email-btn-hover.png) ![Email button pressed](components/crops/auth-email-btn-pressed.png)

#### Email field
The "Email" input; focused and typed into then cleared — never submitted. Read as `auth-email` on the auth.exa.ai sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 44; padding 12px 16px 12px 40px; border 1px solid #e0e0e0; radius 4px; background transparent; text ABC Diatype Unlicensed Trial 16/24 400, #171717 `color.gray.900`; placeholder lab(65.9269 -0.832707 -8.17473) |
| focused, filled | border 1px solid #1f40ed `color.brand.default` |

![Email field default](components/crops/auth-email-default.png) ![Email field focused](components/crops/auth-email-focused.png) ![Email field filled](components/crops/auth-email-filled.png)

#### Code sample
The exa.search() snippet the login page shows beside the card. Read as `auth-code` on the auth.exa.ai sign-in page.

**Values (default).** size 336 x 60; background transparent; text Geist Mono 14/20 400, #ffffff `color.secondary.default`.

![Code sample default](components/crops/auth-code-default.png)

### Docs (exa.ai/docs) (light)

The Mintlify docs shell in light mode: the sidebar, search pill, theme button, nav items, page heading, body copy, links, code blocks, language tabs, the 'Add Exa to your agent' banner and the assistant field.

#### Docs sidebar
The docs left rail: search, the theme control and the nav tree (Overview / Get Started / Search / Agent / Other APIs). Read as `docs-sidebar` on the docs page.

**Values (default).** size 288 x 844; border R: 1px solid #eeeff5 `color.docs.gray.100`; background transparent; text Inter 14/14 400, #4f4f57 `color.docs.mintlify.exa-gray.800`; transition transform 0.1s cubic-bezier(0.4, 0, 0.2, 1), translate 0.1s cubic-bezier(0.4, 0, 0.2, 1), scale 0.1s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #4f4f57 `color.docs.mintlify.exa-gray.800`; layers nav.hidden.sticky 288.0x844.0 R:1px solid rgb(238, 239, 245); button.docs-sidebar-search 267.0x36.0 T:1px solid rgba(9, 9, 11, 0.14) / R:1px solid rgba(9, 9, 11, 0.14) / B:1px solid rgba(9, 9, 11, 0.14) / L:1px solid rgba(9, 9, 11, 0.14) 6px; kbd 27.0x18.0 rgba(9, 9, 11, 0.05) 4px; kbd 18.0x18.0 rgba(9, 9, 11, 0.05) 4px; a.group.flex 267.0x32.0 rgb(243, 243, 244) 6px; div.sidebar-nav-group-divider.

Child layers that carry the look: nav 288x844 border 1px solid #eeeff5 `color.docs.gray.100`; button 267x36 border 1px solid rgba(9, 9, 11, 0.14) `color.docs.vars.sidebar-search-border` radius 6px; kbd 27x18 background rgba(9, 9, 11, 0.05) `color.docs.vars.code-action-hover` radius 4px.

![Docs sidebar default](components/crops/docs-sidebar-default.png)

#### Docs logo
The exa mark at the top of the docs chrome. Read as `docs-logo` on the docs page.

**Values (default).** size 61.39 x 19.19; background transparent; text Inter 16/24 400, #707177 `color.docs.gray.500`.

![Docs logo default](components/crops/docs-logo-default.png)

#### Search button
The "Search Ctrl K" field-styled button in the docs rail; measured, never opened. Read as `docs-search` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 267 x 36; padding 0px 10px; border 1px solid rgba(9, 9, 11, 0.14) `color.docs.vars.sidebar-search-border`; radius 6px; background transparent; text Inter 14/14 400, #4f4f57 `color.docs.mintlify.exa-gray.800`; transition color 0.22s cubic-bezier(0.2, 0, 0, 1), border-color 0.22s cubic-bezier(0.2, 0, 0, 1), transform 0.1s cubic-bezier(0.2, 0, 0, 1); icon 16 x 16, #4f4f57 `color.docs.mintlify.exa-gray.800` |
| hover | border 1px solid rgba(9, 9, 11, 0.28) `color.docs.vars.sidebar-search-border-hover`; text Inter 14/14 400, #0b0b0d `color.docs.mintlify.exa-gray.1000`; icon 16 x 16, #0b0b0d `color.docs.mintlify.exa-gray.1000` |
| focus-visible | border 1px solid rgba(9, 9, 11, 0.28) `color.docs.vars.sidebar-search-border-hover`; shadow rgba(9, 9, 11, 0.07) 0px 0px 0px 3px |
| pressed | size 258.99 x 34.92; border 1px solid rgba(9, 9, 11, 0.28) `color.docs.vars.sidebar-search-border-hover`; text Inter 14/14 400, #0b0b0d `color.docs.mintlify.exa-gray.1000`; transform scale(0.97); icon 15.52 x 15.52, #0b0b0d `color.docs.mintlify.exa-gray.1000` |

![Search button default](components/crops/docs-search-default.png) ![Search button hover](components/crops/docs-search-hover.png) ![Search button focus-visible](components/crops/docs-search-focus-visible.png) ![Search button pressed](components/crops/docs-search-pressed.png)

#### Theme button
The docs theme preference button; measured, never opened (the dark capture used a prefers-color-scheme context instead). Read as `docs-theme-btn` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 30 x 30; padding 8px; radius 9999px; background oklab(0.273744 0.00110777 -0.00923111 / 0.04); text Inter 14/20 400, oklab(0.154567 -0.000390366 -0.0112101 / 0.5); icon 14 x 16, #505157 `color.docs.gray.600` |
| hover | icon 14 x 16, #26272c `color.docs.gray.800` |
| focus-visible | outline 1px auto #1840ed `color.docs.primary`, offset 0px |
| pressed | icon 14 x 16, #26272c `color.docs.gray.800` |

![Theme button default](components/crops/docs-theme-btn-default.png) ![Theme button hover](components/crops/docs-theme-btn-hover.png) ![Theme button focus-visible](components/crops/docs-theme-btn-focus-visible.png) ![Theme button pressed](components/crops/docs-theme-btn-pressed.png)

#### Nav item
A docs sidebar link; measured, never followed. Read as `docs-nav-item` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 267 x 32; padding 6px 12px 6px 16px; radius 6px; background #f3f3f4 `color.docs.mintlify.exa-gray.200`; text Inter 14/20 600, #000000 `color.neutral.black`; transition background-color 0.15s cubic-bezier(0.2, 0, 0, 1), color 0.15s cubic-bezier(0.2, 0, 0, 1) |
| focus-visible | outline 1px auto #1840ed `color.docs.primary`, offset -2px |

![Nav item default](components/crops/docs-nav-item-default.png) ![Nav item hover](components/crops/docs-nav-item-hover.png) ![Nav item focus-visible](components/crops/docs-nav-item-focus-visible.png) ![Nav item pressed](components/crops/docs-nav-item-pressed.png)

#### Page heading
The doc page's h1 ("Start building with Exa"). Read as `docs-h1` on the docs page.

**Values (default).** size 310.28 x 42; background transparent; text ABCDiatype 32/42 500, #17181e `color.docs.gray.900`.

![Page heading default](components/crops/docs-h1-default.png)

#### Body paragraph
A body paragraph in the doc. Read as `docs-para` on the docs page.

**Values (default).** size 704 x 56; background transparent; text Inter 16.66/28 400, rgba(0, 0, 0, 0.6).

![Body paragraph default](components/crops/docs-para-default.png)

#### Body link
A link inside the doc body; measured, never followed. Read as `docs-link` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 226 x 41.59; padding 10px 12px; border 1px solid rgba(113, 102, 91, 0.08); radius 10px; background #f8f8f9 `color.docs.mintlify.exa-gray.100`; text Inter 14/19.6 400, rgba(0, 0, 0, 0.6) |
| hover | border 1px solid rgba(17, 15, 13, 0.08); background #f3f3f4 `color.docs.mintlify.exa-gray.200`; text Inter 14/19.6 400, rgba(0, 0, 0, 0.9) |
| focus-visible | outline 1px auto #1840ed `color.docs.primary`, offset 1px |
| pressed | border 1px solid rgba(17, 15, 13, 0.08); background #f3f3f4 `color.docs.mintlify.exa-gray.200`; text Inter 14/19.6 400, rgba(0, 0, 0, 0.9) |

![Body link default](components/crops/docs-link-default.png) ![Body link hover](components/crops/docs-link-hover.png) ![Body link focus-visible](components/crops/docs-link-focus-visible.png) ![Body link pressed](components/crops/docs-link-pressed.png)

#### Code block
A code block or inline code span in the doc (Paper Mono). Read as `docs-code` on the docs page.

**Values (default).** size 685 x 269.13; padding 17px 19px; background transparent; shadow rgba(59, 130, 246, 0.5) 0px 0px 0px 0px; text GeistMono 14/19.6 400, #cf222e; layers pre.shiki.shiki-themes 685.0x269.1 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px; code 647.0x235.1 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px.

![Code block default](components/crops/docs-code-default.png)

#### Code-language tab
A Python/JavaScript/cURL language tab in the docs; local toggle only. Read as `docs-tab` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 43 x 18; background transparent; text Inter 13/18 400, #0b0b0d `color.docs.mintlify.exa-gray.1000` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Code-language tab default](components/crops/docs-tab-default.png) ![Code-language tab hover](components/crops/docs-tab-hover.png) ![Code-language tab pressed](components/crops/docs-tab-pressed.png)

#### CTA banner
The blue "Add Exa to your agent" banner with Get-Started and Get-API-Key actions — the actions measured, never followed. Read as `docs-cta` on the docs page.

**Values (default).** size 224.92 x 65.59; background transparent; text ABCDiatype 24/42 500, #ffffff `color.secondary.default`.

![CTA banner default](components/crops/docs-cta-default.png)

#### Assistant field
The "Ask a question…" assistant input; focused and typed into then cleared — never sent. Read as `docs-assistant` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 54 x 50; padding 10px 40px 0px 14px; radius 6px; background transparent; text Inter 14/20 400, #17181e `color.docs.gray.900`; placeholder #505157 `color.docs.gray.600` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Topbar CTA
The "API Dashboard" button in the docs topbar; measured, never followed. Read as `docs-topbar-cta` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 139 x 36; padding 8px 8px 8px 12px; background transparent; text Inter 14/20 500, #ffffff `color.secondary.default`; transition transform 0.1s cubic-bezier(0.2, 0, 0, 1); icon 12 x 12, oklab(0.999994 0.0000455678 0.0000200868 / 0.9); layers span.absolute.inset-0 139.0x36.0 rgb(0, 0, 0) 6px |
| focus-visible | outline 1px auto #1840ed `color.docs.primary`, offset 1px; layers a.group.pl-3 139.0x36.0 1px auto rgb(24, 64, 237) offset 1px; span.absolute.inset-0 139.0x36.0 rgb(0, 0, 0) 6px |
| pressed | size 134.83 x 34.92; transform scale(0.97); icon 11.64 x 11.64, oklab(0.999994 0.0000455678 0.0000200868 / 0.9); layers span.absolute.inset-0 134.8x34.9 rgb(0, 0, 0) 6px |

Child layers that carry the look: span 139x36 background #000000 `color.neutral.black` radius 6px.

![Topbar CTA default](components/crops/docs-topbar-cta-default.png) ![Topbar CTA hover](components/crops/docs-topbar-cta-hover.png) ![Topbar CTA focus-visible](components/crops/docs-topbar-cta-focus-visible.png) ![Topbar CTA pressed](components/crops/docs-topbar-cta-pressed.png)

### Docs (exa.ai/docs) (dark)

The same docs shell under html.dark: the #0b0b10 canvas, flipped borders and code surfaces, the same #1840ed primary.

#### Docs sidebar
The docs left rail: search, the theme control and the nav tree (Overview / Get Started / Search / Agent / Other APIs). Read as `d-docs-sidebar` on the docs dark page.

**Values (default).** size 288 x 844; border R: 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1); background transparent; text Inter 14/14 400, #bababf; transition transform 0.1s cubic-bezier(0.4, 0, 0.2, 1), translate 0.1s cubic-bezier(0.4, 0, 0.2, 1), scale 0.1s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #bababf; layers nav.hidden.sticky 288.0x844.0 R:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1); button.docs-sidebar-search 267.0x36.0 T:1px solid rgba(250, 250, 250, 0.16) / R:1px solid rgba(250, 250, 250, 0.16) / B:1px solid rgba(250, 250, 250, 0.16) / L:1px solid rgba(250, 250, 250, 0.16) 6px; kbd 27.0x18.0 rgba(250, 250, 250, 0.08) 4px; kbd 18.0x18.0 rgba(250, 250, 250, 0.08) 4px; a.group.flex 267.0.

Child layers that carry the look: nav 288x844 border 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1); button 267x36 border 1px solid rgba(250, 250, 250, 0.16) radius 6px; kbd 27x18 background rgba(250, 250, 250, 0.08) radius 4px.

![Docs sidebar default](components/crops/d-docs-sidebar-default.png)

#### Docs logo
The exa mark at the top of the docs chrome. Read as `d-docs-logo` on the docs dark page.

**Values (default).** size 61.39 x 19.19; background transparent; text Inter 16/24 400, #9fa0a5 `color.docs.gray.400`.

![Docs logo default](components/crops/d-docs-logo-default.png)

#### Search button
The "Search Ctrl K" field-styled button in the docs rail; measured, never opened. Read as `d-docs-search` on the docs dark page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 267 x 36; padding 0px 10px; border 1px solid rgba(250, 250, 250, 0.16); radius 6px; background transparent; text Inter 14/14 400, #bababf; transition color 0.22s cubic-bezier(0.2, 0, 0, 1), border-color 0.22s cubic-bezier(0.2, 0, 0, 1), transform 0.1s cubic-bezier(0.2, 0, 0, 1); icon 16 x 16, #bababf |
| hover | border 1px solid rgba(250, 250, 250, 0.32); text Inter 14/14 400, #f5f5f6; icon 16 x 16, #f5f5f6 |
| focus-visible | border 1px solid rgba(250, 250, 250, 0.32); shadow rgba(250, 250, 250, 0.09) 0px 0px 0px 3px |
| pressed | size 258.99 x 34.92; border 1px solid rgba(250, 250, 250, 0.32); text Inter 14/14 400, #f5f5f6; transform scale(0.97); icon 15.52 x 15.52, #f5f5f6 |

![Search button default](components/crops/d-docs-search-default.png) ![Search button hover](components/crops/d-docs-search-hover.png) ![Search button focus-visible](components/crops/d-docs-search-focus-visible.png) ![Search button pressed](components/crops/d-docs-search-pressed.png)

#### Theme button
The docs theme preference button; measured, never opened (the dark capture used a prefers-color-scheme context instead). Read as `d-docs-theme-btn` on the docs dark page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 30 x 30; padding 8px; radius 9999px; background oklab(0.999994 0.0000455678 0.0000200868 / 0.1); text Inter 14/20 400, oklab(0.999994 0.0000455678 0.0000200868 / 0.5); icon 14 x 16, #cecfd5 `color.docs.gray.300` |
| hover | icon 14 x 16, #eeeff5 `color.docs.gray.100` |
| focus-visible | outline 1px auto #5f7cff `color.docs.primary-light`, offset 0px |
| pressed | icon 14 x 16, #eeeff5 `color.docs.gray.100` |

![Theme button default](components/crops/d-docs-theme-btn-default.png) ![Theme button hover](components/crops/d-docs-theme-btn-hover.png) ![Theme button focus-visible](components/crops/d-docs-theme-btn-focus-visible.png) ![Theme button pressed](components/crops/d-docs-theme-btn-pressed.png)

#### Nav item
A docs sidebar link; measured, never followed. Read as `d-docs-nav-item` on the docs dark page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 267 x 32; padding 6px 12px 6px 16px; radius 6px; background rgba(255, 255, 255, 0.08); text Inter 14/20 600, #f5f5f6; transition background-color 0.15s cubic-bezier(0.2, 0, 0, 1), color 0.15s cubic-bezier(0.2, 0, 0, 1) |
| focus-visible | outline 1px auto #5f7cff `color.docs.primary-light`, offset -2px |

![Nav item default](components/crops/d-docs-nav-item-default.png) ![Nav item hover](components/crops/d-docs-nav-item-hover.png) ![Nav item focus-visible](components/crops/d-docs-nav-item-focus-visible.png) ![Nav item pressed](components/crops/d-docs-nav-item-pressed.png)

#### Page heading
The doc page's h1 ("Start building with Exa"). Read as `d-docs-h1` on the docs dark page.

**Values (default).** size 310.28 x 42; background transparent; text ABCDiatype 32/42 500, #dfe0e5 `color.docs.gray.200`.

![Page heading default](components/crops/d-docs-h1-default.png)

#### Body paragraph
A body paragraph in the doc. Read as `d-docs-para` on the docs dark page.

**Values (default).** size 704 x 56; background transparent; text Inter 16.66/28 400, rgba(255, 255, 255, 0.6).

![Body paragraph default](components/crops/d-docs-para-default.png)

#### Body link
A link inside the doc body; measured, never followed. Read as `d-docs-link` on the docs dark page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 226 x 41.59; padding 10px 12px; border 1px solid rgba(255, 255, 255, 0.1); radius 10px; background rgba(255, 255, 255, 0.03); text Inter 14/19.6 400, rgba(255, 255, 255, 0.72) |
| hover | border 1px solid rgba(255, 255, 255, 0.14); background rgba(255, 255, 255, 0.08); text Inter 14/19.6 400, #ffffff `color.secondary.default` |
| focus-visible | outline 1px auto #5f7cff `color.docs.primary-light`, offset 1px |
| pressed | border 1px solid rgba(255, 255, 255, 0.14); background rgba(255, 255, 255, 0.08); text Inter 14/19.6 400, #ffffff `color.secondary.default` |

![Body link default](components/crops/d-docs-link-default.png) ![Body link hover](components/crops/d-docs-link-hover.png) ![Body link focus-visible](components/crops/d-docs-link-focus-visible.png) ![Body link pressed](components/crops/d-docs-link-pressed.png)

#### Code block
A code block or inline code span in the doc (Paper Mono). Read as `d-docs-code` on the docs dark page.

**Values (default).** size 685 x 269.13; padding 17px 19px; background transparent; shadow rgba(59, 130, 246, 0.5) 0px 0px 0px 0px; text GeistMono 14/19.6 400, #c586c0; layers pre.shiki.shiki-themes 685.0x269.1 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px; code 647.0x235.1 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px.

![Code block default](components/crops/d-docs-code-default.png)

#### Code-language tab
A Python/JavaScript/cURL language tab in the docs; local toggle only. Read as `d-docs-tab` on the docs dark page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 43 x 18; background transparent; text Inter 13/18 400, #f5f5f6 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Code-language tab default](components/crops/d-docs-tab-default.png) ![Code-language tab hover](components/crops/d-docs-tab-hover.png) ![Code-language tab pressed](components/crops/d-docs-tab-pressed.png)

#### CTA banner
The blue "Add Exa to your agent" banner with Get-Started and Get-API-Key actions — the actions measured, never followed. Read as `d-docs-cta` on the docs dark page.

**Values (default).** size 224.92 x 65.59; background transparent; text ABCDiatype 24/42 500, #ffffff `color.secondary.default`.

![CTA banner default](components/crops/d-docs-cta-default.png)

#### Assistant field
The "Ask a question…" assistant input; focused and typed into then cleared — never sent. Read as `d-docs-assistant` on the docs dark page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 54 x 50; padding 10px 40px 0px 14px; radius 6px; background transparent; text Inter 14/20 400, #eeeff5 `color.docs.gray.100`; placeholder #cecfd5 `color.docs.gray.300` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Topbar CTA
The "API Dashboard" button in the docs topbar; measured, never followed. Read as `d-docs-topbar-cta` on the docs dark page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 139 x 36; padding 8px 8px 8px 12px; background transparent; text Inter 14/20 500, #ffffff `color.secondary.default`; transition transform 0.1s cubic-bezier(0.2, 0, 0, 1); icon 12 x 12, oklab(0.999994 0.0000455678 0.0000200868 / 0.9); layers span.absolute.inset-0 139.0x36.0 rgb(0, 0, 0) 6px |
| focus-visible | outline 1px auto #5f7cff `color.docs.primary-light`, offset 1px; layers a.group.pl-3 139.0x36.0 1px auto rgb(95, 124, 255) offset 1px; span.absolute.inset-0 139.0x36.0 rgb(0, 0, 0) 6px |
| pressed | size 134.83 x 34.92; transform scale(0.97); icon 11.64 x 11.64, oklab(0.999994 0.0000455678 0.0000200868 / 0.9); layers span.absolute.inset-0 134.8x34.9 rgb(0, 0, 0) 6px |

Child layers that carry the look: span 139x36 background #000000 `color.neutral.black` radius 6px.

![Topbar CTA default](components/crops/d-docs-topbar-cta-default.png) ![Topbar CTA hover](components/crops/d-docs-topbar-cta-hover.png) ![Topbar CTA focus-visible](components/crops/d-docs-topbar-cta-focus-visible.png) ![Topbar CTA pressed](components/crops/d-docs-topbar-cta-pressed.png)

### Footer

The marketing footer: link columns, status and social marks.

#### Footer
The marketing footer: link columns, status and social marks. Read as `mkt-footer` on the marketing home page.

**Values (default).** size 1425 x 1367.84; background transparent; text Arizona 54.4/59.84 400, #000000 `color.neutral.black`; layers div.flex.w-full 1425.0x523.8 rgb(255, 255, 255); a.font-inter.inline-flex 124.2x40.0 rgb(0, 0, 0) 4px; div.flex.items-end 1440.0x900.0 rgb(1, 55, 225); div.absolute.inset-x-0 1440.0x844.0; div.absolute.inset-0 1440.0x900.0; div.left-0.top-0 1358.2x0.6 rgb(0, 111, 255).

Child layers that carry the look: div 1425x523.8 background #ffffff `color.secondary.default`; a 124.2x40 background #000000 `color.neutral.black` radius 4px; div 1440x900 background #0137e1.

![Footer default](components/crops/mkt-footer-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the header, the hamburger and its drawer, the hero display and the demo field.

#### Mobile header
The top bar at 390: wordmark, hamburger and the Sign-up action. Read as `m-header` on the marketing home page at 390 wide.

**Values (default).** size 390 x 64; background #ffffff `color.secondary.default`; text ABCDiatype 16/24 400, #ffffff `color.secondary.default`; icon 20 x 20, #4b5563.

![Mobile header default](components/crops/m-header-default.png)

#### Hamburger
The mobile nav toggle; opened to reveal the drawer — a local toggle, its links never followed. Read as `m-hamburger` on the marketing home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, opened) | size 32 x 32; padding 6px; radius 8px; background transparent; text Inter 16/24 400, #ffffff `color.secondary.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #4b5563 |
| hover, pressed | background #f3f4f6 |

![Hamburger default](components/crops/m-hamburger-default.png) ![Hamburger hover](components/crops/m-hamburger-hover.png) ![Hamburger focus-visible](components/crops/m-hamburger-focus-visible.png) ![Hamburger pressed](components/crops/m-hamburger-pressed.png) ![Hamburger opened](components/crops/m-hamburger-opened.png)

#### Mobile nav drawer
The full-height nav the hamburger opens (div.fixed inset-x-0 inside the header). Read as `m-drawer` on the marketing home page at 390 wide.

**Values (default).** size 390 x 844; background #ffffff `color.secondary.default`; shadow rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px; text ABCDiatype 16/24 500, #111827 `color.text.light-default`; icon 20 x 20, #6b7280 `color.text.dark-faint`.

![Mobile nav drawer default](components/crops/m-drawer-default.png)

#### Hero headline (mobile)
"The world's data for AI agents" at 390 wide. Read as `m-hero-h1` on the marketing home page at 390 wide.

**Values (default).** size 358 x 84; background transparent; text Arizona 38.4/42 400, #111827 `color.text.light-default`.

![Hero headline (mobile) default](components/crops/m-hero-h1-default.png)

#### Demo query field (mobile)
The demo query box at 390; focused and typed into then restored — the preview was never run. Read as `m-demo-textarea` on the marketing home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 330 x 24; background transparent; outline 2px solid transparent, offset 2px; text ABCDiatype 16/24 400, #111827 `color.text.light-default`; placeholder rgba(0, 0, 0, 0.4); layers textarea.block.w-full 330.0x24.0 2px solid rgba(0, 0, 0, 0) offset 2px |
| filled | size 330 x 48; layers textarea.block.w-full 330.0x48.0 2px solid rgba(0, 0, 0, 0) offset 2px |

Child layers that carry the look: textarea 330x24.

![Demo query field (mobile) default](components/crops/m-demo-textarea-default.png) ![Demo query field (mobile) focused](components/crops/m-demo-textarea-focused.png) ![Demo query field (mobile) filled](components/crops/m-demo-textarea-filled.png)

## Icons

55 SVGs were lifted from the pages into [icons/](icons), named by role where a label gave one, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. The set holds the chevrons and hamburger strokes, the mega-menu product glyphs, the demo controls (search, run-preview, clear-query, show-code-view), the use-case pill glyphs and the social/integration marks (parallel, perplexity, brave…). The SVGs are Exa's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [products](icons/products.svg) | 12x12 | 0 0 24 24 | stroke | home; pricing; product | Products / Solutions / Resources |
| [dismiss-announcement](icons/dismiss-announcement.svg) | 12x12 | 0 0 24 24 | stroke | home; pricing; product | Dismiss announcement |
| [parallel](icons/parallel.svg) | 14x14 16x16 | 0 0 273 273 | fill | home; product | Parallel |
| [perplexity](icons/perplexity.svg) | 11x14 12x16 | 0 0 28 36 | stroke | home; product | Perplexity |
| [icon-bee2464c](icons/icon-bee2464c.svg) | 13x16 | 0 0 78.1818 100 | fill | home; product |  |
| [icon-1b666b36](icons/icon-1b666b36.svg) | 15x15 | 0 0 15 15 | fill | home | Watch Cognition case study video |
| [show-code-view](icons/show-code-view.svg) | 13x13 | 0 0 24 24 | stroke | home | Show code view |
| [search](icons/search.svg) | 14x14 | 0 0 24 24 | stroke | home | Search |
| [run-preview](icons/run-preview.svg) | 20x20 | 0 0 24 24 | stroke | home | Run preview |
| [clear-query](icons/clear-query.svg) | 16x16 | 0 0 24 24 | stroke | home | Clear query |
| [brave](icons/brave.svg) | 12x14 14x16 | 0 0 34 40 | fill | home | Brave |
| [exa](icons/exa.svg) | 11x14 | 0 0 78.1818 100 | fill | home | Exa |
| [api-playground](icons/api-playground.svg) | 13x13 | 0 0 24 24 | stroke | home | API Playground |
| [enrichments](icons/enrichments.svg) | 20x20 | 0 0 24 24 | stroke | pricing | Enrichments |
| [icon-0de5e38f](icons/icon-0de5e38f.svg) | 14x16 | 0 0 34 40 | fill | product |  |
| [icon-0e48c38c](icons/icon-0e48c38c.svg) | 18x18 | 0 0 24 24 | stroke | home | Inference Providers Search for open and  |
| [curl](icons/curl.svg) | 14x14 | 0 0 24 24 | stroke | docs | cURL |
| [people-search](icons/people-search.svg) | 20x20 | 0 0 24 24 | stroke | pricing | People search |
| [found-5-results](icons/found-5-results.svg) | 12x14 | 0 0 107 129 | fill | product | Found 5 results / Found 3 brands / Found 4 results |
| [daily-at-9-00am](icons/daily-at-9-00am.svg) | 11x11 | 0 0 24 24 | stroke | pricing | Daily at 9:00AM / Weekly, Mondays / Daily at 6:00PM |
| [icon-3fcb0bde](icons/icon-3fcb0bde.svg) | 18x18 | 0 0 24 24 | stroke | home | Search API Accurate real-time web search |
| [news-monitoring](icons/news-monitoring.svg) | 20x20 | 0 0 24 24 | stroke | pricing | News monitoring |
| [icon-42c79811](icons/icon-42c79811.svg) | 20x20 | 0 0 24 24 | stroke | product | What is the Exa Search API? / How is Exa different from a SE |
| [icon-456d0dca](icons/icon-456d0dca.svg) | 18x18 | 0 0 24 24 | stroke | home | Agent API Async deep research / AI Assistants Live web knowl |
| [read-the-docs](icons/read-the-docs.svg) | 16x16 | 0 0 24 24 | stroke | product | Read the docs / Read about Exa 3.0 |
| [icon-498e3316](icons/icon-498e3316.svg) | 18x18 | 0 0 24 24 | stroke | home | Monitors API Track changes on the web / Model Training Pre-t |
| [icon-4d20378c](icons/icon-4d20378c.svg) | 18x18 | 0 0 24 24 | stroke | home | Exa Library Structured data for your age |
| [icon-4e34fdea](icons/icon-4e34fdea.svg) | 16x16 | 0 0 24 24 | stroke | pricing | Free $10 credits per month / MCP server access / Claude Conn |
| [coding-agents](icons/coding-agents-4f0f75d5.svg) | 18x18 | 0 0 24 24 | stroke | pricing | Coding agents / Chatbots / News monitoring |
| [send-message](icons/send-message.svg) | 10x10 |  | fill | docs | Send message |
| [icon-5fb71824](icons/icon-5fb71824.svg) | 18x18 | 0 0 24 24 | stroke | home | GTM Account and contact intelligence |
| [get-api-key](icons/get-api-key.svg) | 14x14 | 0 0 14 14 | fill | docs | Get API Key |
| [javascript](icons/javascript.svg) | 14x14 | 0 0 15 16 | fill | docs | JavaScript |
| [change-theme-preference](icons/change-theme-preference.svg) | 14x16 |  | fill | docs | Change theme preference |
| [voice-agents](icons/voice-agents.svg) | 20x20 | 0 0 24 24 | stroke | pricing | Voice agents |
| [icon-7f88d096](icons/icon-7f88d096.svg) | 13x13 | 0 0 16 16 | stroke | product |  |
| [company-search](icons/company-search.svg) | 20x20 | 0 0 24 24 | stroke | pricing | Company search |
| [icon-8282bccf](icons/icon-8282bccf.svg) | 18x18 | 0 0 24 24 | stroke | home | Exa Connect Access third-party data prov |
| [x](icons/x.svg) | 20x20 |  | fill | docs | x / linkedin |
| [python](icons/python.svg) | 14x14 | 0 0 16 16 | fill | docs | Python |
| [coding-agents](icons/coding-agents-96d1b602.svg) | 20x20 | 0 0 24 24 | stroke | pricing | Coding agents |
| [ask-assistant](icons/ask-assistant.svg) | 16x16 |  | fill | docs | Ask Assistant |
| [icon-a12beb9f](icons/icon-a12beb9f.svg) | 18x18 | 0 0 24 24 | stroke | home | Contents API Token efficient page extrac |
| [api-dashboard](icons/api-dashboard.svg) | 12x12 |  | fill | docs | API Dashboard |
| [icon-b107ee10](icons/icon-b107ee10.svg) | 18x18 | 0 0 24 24 | stroke | home | Enterprise Search infrastructure at scal |
| [icon-bfbc3fe2](icons/icon-bfbc3fe2.svg) | 18x18 | 0 0 24 24 | stroke | home | Recruiting Find talent by expertise, not |
| [icon-c16a6c99](icons/icon-c16a6c99.svg) | 20x20 | 0 0 24 24 | stroke | pricing | Scroll right through API products |
| [icon-c4bb7a30](icons/icon-c4bb7a30.svg) | 20x20 | 0 0 24 24 | stroke | pricing | Scroll left through API products |
| [icon-d224dd27](icons/icon-d224dd27.svg) | 18x18 | 0 0 24 24 | stroke | home | Exa Snapshot Search the web as it was on |
| [icon-dcfdeccf](icons/icon-dcfdeccf.svg) | 18x18 | 0 0 24 24 | stroke | home | Coding Code and documentation context |
| [data-floating-buttons-bg-gray-10](icons/data-floating-buttons-bg-gray-10.svg) | 16x16 |  | fill | docs | Copy the contents from the code block |
| [chatbots](icons/chatbots.svg) | 20x20 | 0 0 24 24 | stroke | pricing | Chatbots |
| [icon-e4380971](icons/icon-e4380971.svg) | 18x18 | 0 0 24 24 | stroke | home | Legal Case law, statutes, and regulation |
| [icon-eac2b7f5](icons/icon-eac2b7f5.svg) | 18x18 | 0 0 24 24 | stroke | home | Finance Filings, news, and market maps |
| [open-search](icons/open-search.svg) | 16x16 | 0 0 18 18 | stroke | docs | Open search |

## Gaps

### The signed-in product

The real Exa product lives behind login — the dashboard, API keys, the playground and websets all need an account and were never reached. `dashboard.exa.ai` was measured only as the signed-out `auth.exa.ai` card it redirects to; the form was never submitted. The home page's search demo widget is the closest public view of the product: its pills and query field are real controls, but firing a request needs the Run-preview arrow (never pressed) and the widget could not verify the headless browser anyway — its output panel reads 'We couldn't verify your browser … Sign in to continue', the widget's own honest signed-out state.

### Pages

- **The account and API flow.** Every post-login surface was never reached; the sign-in form and the demo/assistant fields were measured as fields and never submitted, and Get-started/Sign-up/API-key actions were never followed.
- **websets.exa.ai** rate-limits headless browsers (HTTP 429); the `websets-light-default` shot, when present, is its block page, kept as the boundary evidence rather than retried.
- **Subpages of /products and /use-cases** (contents, agent, deep, monitors, snapshot, library, the use-case detail pages) share the marketing chrome; a subset beyond the measured pass was screenshotted where listed above.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active), so a state a script adds on real mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **The demo widget is live** — its query field was typed into and restored, its pills toggled as preview configuration; the request itself was never fired.
- **The announcement strip's dismiss button** was never pressed; the strip stays in the shots.

### Themes

Three distinct public surfaces were captured: the marketing site (light only — its sole prefers-color-scheme:dark rule is one utility class, not a theme), the auth.exa.ai sign-in card (light only), and the Mintlify docs, which genuinely switch on `html.dark`. tokens.json keeps real light and dark sets; the dark set holds docs roles only, since marketing and sign-in paint no dark theme.

### Fonts

- **ABCDiatype** (marketing body/UI), **Arizona**/**ABC Arizona Flare** (marketing display, auth display), **SuisseIntlMono** (marketing mono), **ABC Diatype Unlicensed Trial** and **Geist Mono** (auth card), **Inter** and **Paper Mono** (docs) are the served faces — the brand faces are trial-licensed ABC fonts served from the sites' CDNs; the style guide falls back to system sans.

### Screenshots

- The exa wordmark, integration logos, photography and page artwork in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files, never off a screenshot.

### Content left out

- Customer names, quotes, eval copy, blog posts and doc page content are the product's published text; only frames and components were measured.
