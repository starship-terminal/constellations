# Dub components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from dub.co on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. dub.co is three surfaces signed out: the Next.js marketing site (Tailwind + Satoshi/Inter), the app.dub.co auth shell on /login and /register (measured, never submitted), and the Mintlify docs/help surface on /docs and /help — the only place a real theme toggle exists, so docs was measured in both light and dark. Nothing was signed into, sent or submitted; the login, register and contact-sales forms were never filled past a deleted sample; no time the Send or Log-in buttons were ever pressed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (63 components, 162 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 14/20 500, #404040`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (160 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`: the marketing and auth surfaces paint `light` only; `docs-dark-dark-*` is the docs page under its own theme dropdown's Dark preference. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Links (product page) | `/links` | [default](screenshots/links-light-default.png), [full](screenshots/links-light-full.png) |
| Partners (product page) | `/partners` | [default](screenshots/partners-light-default.png), [full](screenshots/partners-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [yearly](screenshots/pricing-light-yearly.png) |
| Customers | `/customers` | [default](screenshots/customers-light-default.png), [full](screenshots/customers-light-full.png) |
| Enterprise | `/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| Compare vs Bitly | `/compare/bitly` | [default](screenshots/compare-light-default.png), [full](screenshots/compare-light-full.png) |
| Contact sales | `/contact/sales` | [default](screenshots/sales-light-default.png), [full](screenshots/sales-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Changelog | `/changelog` | [default](screenshots/changelog-light-default.png), [full](screenshots/changelog-light-full.png) |
| Log in | `/login` | [default](screenshots/login-light-default.png) |
| Register | `/register` | [default](screenshots/register-light-default.png) |
| Docs | `/docs` | [dark-default](screenshots/docs-dark-dark-default.png), [dark-full](screenshots/docs-dark-dark-full.png), [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png) |
| Docs, dark theme | `/docs (theme dropdown)` | [default](screenshots/docs-dark-dark-default.png), [full](screenshots/docs-dark-dark-full.png) |
| Help center | `/help` | [default](screenshots/help-light-default.png), [full](screenshots/help-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Docs, phone | `/docs` | [default](screenshots/mobile-docs-light-default.png), [full](screenshots/mobile-docs-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the round menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |
| Product mega-menu | every marketing page | the nav trigger's own hover | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#mega-menu-panel), [menu-link](#menu-item) |
| Mintlify AI assistant + promo overlays | docs and marketing pages | hidden, never answered (no assistant prompt was ever opened or sent) | hidden before every shot and reading |
| Docs dark theme | /docs | the page's own 'Change theme preference' dropdown (System/Light/Dark), a local UI toggle held in localStorage isDarkMode | [docs-dark-dark-default](screenshots/docs-dark-dark-default.png), the dk-docs-* entries |
| Billing-period toggle | /pricing | the Monthly/Yearly toggle's own click | [pricing-light-yearly](screenshots/pricing-light-yearly.png), [billing-toggle](#billing-toggle) |
| Signed-in product | app.dub.co workspace | the link-management workspace lives behind /login | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 29 components were given a real keyboard focus. 25 draw an outline ring: `nav-trigger` (1px auto #005fcc `measured.focus-outline`, offset 0px), `nav-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `nav-cta` (1px auto #005fcc `measured.focus-outline`, offset 1px), `hero-cta` (1px auto #005fcc `measured.focus-outline`, offset 1px), `hero-demo` (1px auto #005fcc `measured.focus-outline`, offset 1px), `hero-tab` (1px auto #005fcc `measured.focus-outline`, offset 0px), `billing-toggle` (1px auto #005fcc `measured.focus-outline`, offset 0px), `plan-cta` (1px auto #005fcc `measured.focus-outline`, offset 1px), `faq-trigger` (1px auto #005fcc `measured.focus-outline`, offset 0px), `customer-card` (1px auto #005fcc `measured.focus-outline`, offset 1px), `sales-topic` (1px auto #005fcc `measured.focus-outline`, offset 0px), `email-submit` (1px auto #005fcc `measured.focus-outline`, offset 0px), `auth-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `docs-nav-item` (1px auto #155dfc `color.brand.primary`, offset -2px), `docs-search` (1px auto #155dfc `color.brand.primary`, offset 0px), `docs-theme` (1px auto #155dfc `color.brand.primary`, offset 0px), `docs-copy` (1px auto #155dfc `color.brand.primary`, offset 0px), `docs-feedback` (2px solid #155dfc `color.brand.primary`, offset -2px), `docs-nav-tab` (1px auto #155dfc `color.brand.primary`, offset 1px), `dk-docs-nav-item` (1px auto #155dfc `color.brand.primary`, offset -2px), `dk-docs-copy` (1px auto #155dfc `color.brand.primary`, offset 0px), `dk-docs-search` (1px auto #155dfc `color.brand.primary`, offset 0px), `footer-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `social-link` (1px auto #005fcc `measured.focus-outline`, offset 1px), `m-nav-item` (1px auto #005fcc `measured.focus-outline`, offset 0px). 4 change only their border: `nav-login`, `oauth-google`, `oauth-github`, `oauth-saml`. On dub.co the button ring is the browser-default `auto 1px rgb(0, 95, 204)` outline, the docs surface draws its own 1px `#155dfc` ring, and the email field instead takes a black border plus a 1px black ring shadow.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.075s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | footer-link, sales-topic |
| 0.1s | `cubic-bezier(0.4, 0, 0.2, 1)` | rotate, scale, transform, translate | dk-docs-sidebar, docs-sidebar |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | all, background-color, border-color, color, fill, stroke, text-decoration-color | auth-link, billing-toggle, email-submit, faq-trigger, hero-cta, hero-demo, hero-tab, m-nav and more |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | m-menu-button |
| 0.5s | `cubic-bezier(0.215, 0.61, 0.355, 1)` | flex-basis, flex-grow | customer-card |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 1062 x 623 | 1px solid #ededed | 12px | #fafafa `color.neutral.50` | none | 0 |
| [Product demo panel](#product-demo-panel) | 882 x 567 | T: 1px solid #d4d4d4 `color.neutral.300`; R: 1px solid #d4d4d4 `color.neutral.300`; L: 1px solid #d4d4d4 `color.neutral.300` | 12px 12px 0px 0px | #ffffff `color.neutral.white` | none | 0 |
| [Menu item](#menu-item) | 307.41 x 304.45 | 1px solid #f5f5f5 `color.neutral.100` | 12px | #fafafa `color.neutral.50` | none | 0 |
| [Customer card](#customer-card) | 128 x 480 | - | 12px | #171717 `color.neutral.900` | none | 0 |
| [Login card](#login-card) | 384 x 562 | - | - | transparent | none | 0 |
| [Register card](#register-card) | 384 x 510 | - | - | transparent | none | 0 |
| [Contact form card](#contact-form-card) | 800 x 346 | R: 1px solid #e5e5e5 `color.neutral.200`; L: 1px solid #e5e5e5 `color.neutral.200` | - | #ffffff `color.neutral.white` | none | 0 |
| [Copy-page button](#copy-page-button) | 121.55 x 34 | T: 1px solid #dfe1e6 `color.gray.200`; B: 1px solid #dfe1e6 `color.gray.200`; L: 1px solid #dfe1e6 `color.gray.200` | 12px 0px 0px 12px | #ffffff `color.neutral.white` | none | 6px 12px |

## Components

### Shell and navigation

The marketing chrome on the near-white field: wordmark, the Product mega-menu trigger, plain links, Log in and the black Sign-up pill.

#### Nav bar
The top nav: wordmark, Product/Solutions/Resources dropdowns, Customers and Pricing links, Log in and the black Sign-up pill. Read as `nav` on the home page.

**Values (default).** size 472.88 x 32; background transparent; text Inter 14/20 500, #404040 `color.neutral.700`; icon 10 x 10, #404040 `color.neutral.700`; layers div.pointer-events-none.absolute 0.0x32.0 rgba(23, 23, 23, 0.05) 8px.

Child layers that carry the look: div 0x32 background rgba(23, 23, 23, 0.05) radius 8px.

![Nav bar default](components/crops/nav-default.png)

#### Logo
The Dub wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 61.33 x 32; background transparent; text Inter 16/24 400, #0a0a0a `color.neutral.950`; icon 61.33 x 32, #262626 `color.neutral.800`.

![Logo default](components/crops/logo-default.png)

#### Nav trigger
The Product button that opens the mega-menu on hover; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 92.52 x 32; padding 0px 12px; radius 8px; background transparent; text Inter 14/20 500, #404040 `color.neutral.700`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 10 x 10, #404040 `color.neutral.700` |
| hover | text Inter 14/20 500, #171717 `color.neutral.900` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px; layers button.relative.group/item 92.5x32.0 1px auto rgb(0, 95, 204) offset 0px 8px |
| pressed | text Inter 14/20 500, #171717 `color.neutral.900` |

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav link
A plain nav link (Customers/Pricing). Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 96.94 x 32; padding 0px 12px; radius 8px; background transparent; text Inter 14/20 500, #404040 `color.neutral.700`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 14/20 500, #171717 `color.neutral.900` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a.relative.group/item 96.9x32.0 1px auto rgb(0, 95, 204) offset 1px 8px |
| pressed | text Inter 14/20 500, #171717 `color.neutral.900` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log-in button
The bordered Log-in button; measured never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 74.5 x 32; padding 0px 16px; border 1px solid #e5e5e5 `color.neutral.200`; radius 8px; background #ffffff `color.neutral.white`; outline 2px solid transparent, offset 2px; text Inter 14/20 400, #171717 `color.neutral.900`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #fafafa `color.neutral.50` |
| focus-visible | border 1px solid #a3a3a3 `color.neutral.400` |
| pressed | background #fafafa `color.neutral.50` |

![Log-in button default](components/crops/nav-login-default.png) ![Log-in button hover](components/crops/nav-login-hover.png) ![Log-in button focus-visible](components/crops/nav-login-focus-visible.png) ![Log-in button pressed](components/crops/nav-login-pressed.png)

#### Sign-up CTA
The black Sign-up pill; measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 84.03 x 32; padding 0px 16px; border 1px solid #000000 `color.neutral.black`; radius 8px; background #000000 `color.neutral.black`; text Inter 14/20 400, #ffffff `color.neutral.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px |

![Sign-up CTA default](components/crops/nav-cta-default.png) ![Sign-up CTA hover](components/crops/nav-cta-hover.png) ![Sign-up CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Sign-up CTA pressed](components/crops/nav-cta-pressed.png)

#### Mega-menu panel
The Product mega-menu panel, opened by its own trigger on hover. Read as `nav-dropdown` on the home page.

**Values (default).** size 318.66 x 318; border 1px solid #f5f5f5 `color.neutral.100`; radius 12px; background #fafafa `color.neutral.50`; text Inter 14/20 500, #171717 `color.neutral.900`.

![Mega-menu panel default](components/crops/nav-dropdown-default.png)

#### Menu item
A product link inside the opened mega-menu. Only the default reading stands: the menu closed between states during capture, so the hover, focus-visible and pressed readings came from a different element and were removed. Read as `menu-link` on the home page.

**Values (default).** size 307.41 x 304.45; border 1px solid #f5f5f5 `color.neutral.100`; radius 12px; background #fafafa `color.neutral.50`; text Inter 14/20 500, #171717 `color.neutral.900`.

![Menu item default](components/crops/menu-link-default.png)

### Home hero

The 48px Satoshi hero, the announcement pill, the two CTAs and the product-demo panel under it.

#### Announcement pill
The "Introducing our Startup Program / Learn more" pill above the headline; measured never followed. Read as `hero-badge` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 211.31 x 28; padding 6px 10px 6px 16px; background transparent; text Inter 12/16 500, #262626 `color.neutral.800` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Announcement pill default](components/crops/hero-badge-default.png) ![Announcement pill hover](components/crops/hero-badge-hover.png) ![Announcement pill pressed](components/crops/hero-badge-pressed.png)

#### Hero headline
The display headline ("Turn clicks into revenue"), Satoshi. Read as `hero-title` on the home page.

**Values (default).** size 508.78 x 55.19; background transparent; text satoshi 48/55.2 500, #171717 `color.neutral.900`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero lede
The paragraph under the headline. Read as `hero-lede` on the home page.

**Values (default).** size 640 x 56; background transparent; text Inter 20/28 400, #525252 `color.neutral.600`.

![Hero lede default](components/crops/hero-lede-default.png)

#### Primary CTA
The black "Start for free" button; measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 127.42 x 38; padding 8px 20px; border 1px solid #000000 `color.neutral.black`; radius 8px; background #000000 `color.neutral.black`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 14/20 500, #ffffff `color.neutral.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #262626 `color.neutral.800`; shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | background #262626 `color.neutral.800`; shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Primary CTA default](components/crops/hero-cta-default.png) ![Primary CTA hover](components/crops/hero-cta-hover.png) ![Primary CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Primary CTA pressed](components/crops/hero-cta-pressed.png)

#### Demo button
The bordered "Get a demo" button; measured never followed. Read as `hero-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 118.64 x 38; padding 8px 20px; border 1px solid #e5e5e5 `color.neutral.200`; radius 8px; background #ffffff `color.neutral.white`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 14/20 500, #262626 `color.neutral.800`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #a3a3a3 `color.neutral.400`; shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | border 1px solid #a3a3a3 `color.neutral.400`; shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Demo button default](components/crops/hero-demo-default.png) ![Demo button hover](components/crops/hero-demo-hover.png) ![Demo button focus-visible](components/crops/hero-demo-focus-visible.png) ![Demo button pressed](components/crops/hero-demo-pressed.png)

#### Feature tab
An icon tab over the product demo (Affiliate Programs / Conversion Analytics / Short Links). Read as `hero-tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 167.64 x 34; padding 8px 12px; border 1px solid #e5e5e5 `color.neutral.200`; radius 8px; background #ffffff `color.neutral.white`; text Inter 14/14 500, #262626 `color.neutral.800`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 10 x 10, #581c87 |
| hover | icon 11 x 11, #581c87 |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |
| pressed | icon 11 x 11, #581c87 |

![Feature tab default](components/crops/hero-tab-default.png) ![Feature tab hover](components/crops/hero-tab-hover.png) ![Feature tab focus-visible](components/crops/hero-tab-focus-visible.png) ![Feature tab pressed](components/crops/hero-tab-pressed.png)

#### Product demo panel
The rendered dashboard mock under the hero — a published demo illustration, not the real app. Read as `demo-panel` on the home page.

**Values (default).** size 882 x 567; border T: 1px solid #d4d4d4 `color.neutral.300`; R: 1px solid #d4d4d4 `color.neutral.300`; L: 1px solid #d4d4d4 `color.neutral.300`; radius 12px 12px 0px 0px; background #ffffff `color.neutral.white`; text Inter 16/24 400, #0a0a0a `color.neutral.950`.

![Product demo panel default](components/crops/demo-panel-default.png)

#### Product page headline
The /links product-page h1 ("Short links with superpowers"). Read as `links-h1` on the links product page.

**Values (default).** size 480 x 110.38; background transparent; text satoshi 48/55.2 500, #171717 `color.neutral.900`.

![Product page headline default](components/crops/links-h1-default.png)

### Pricing

The pricing surface: the Monthly/Yearly toggle, the shared plan panel with its names, prices and CTAs, and the FAQ accordion.

#### Pricing title
The pricing page heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 672 x 110.38; background transparent; text satoshi 48/55.2 500, #171717 `color.neutral.900`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Billing toggle
The Monthly/Yearly period toggle ("10% discount + 12x usage upfront"), read on its Yearly option at rest, on hover, on keyboard focus and forced pressed; never clicked or checked out. Read as `billing-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 280.58 x 40; padding 10px 12px; radius 12px; background transparent; text Inter 12/12 500, #262626 `color.neutral.800`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers span.max-w-fit.rounded-full 212.5x18.0 T:1px solid rgb(191, 219, 254) / R:1px solid rgb(191, 219, 254) / B:1px solid rgb(191, 219, 254) / L:1px solid rgb(191, 219, 254) 9999px |
| hover | background rgba(229, 229, 229, 0.3); text Inter 12/12 500, #737373 `color.neutral.500`; layers none |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px; layers button.relative.flex 280.6x40.0 1px auto rgb(0, 95, 204) offset 0px 12px; span.max-w-fit.rounded-full 212.5x18.0 T:1px solid rgb(191, 219, 254) / R:1px solid rgb(191, 219, 254) / B:1px solid rgb(191, 219, 254) / L:1px solid rgb(191, 219, 254) 9999px |
| pressed | background rgba(229, 229, 229, 0.3); text Inter 12/12 500, #737373 `color.neutral.500`; layers none |

Child layers that carry the look: span 212.5x18 image linear-gradient(to right, #dbeafe, rgba(219, 234, 254, 0.5), #dbeafe) border 1px solid #bfdbfe radius 9999px.

![Billing toggle default](components/crops/billing-toggle-default.png) ![Billing toggle hover](components/crops/billing-toggle-hover.png) ![Billing toggle focus-visible](components/crops/billing-toggle-focus-visible.png) ![Billing toggle pressed](components/crops/billing-toggle-pressed.png)

#### Plan name
A plan card's name. Read as `plan-name` on the pricing page.

**Values (default).** size 66.48 x 24; background transparent; text Inter 16/24 500, #262626 `color.neutral.800`.

![Plan name default](components/crops/plan-name-default.png)

#### Plan price
A plan card's price figure. Read as `plan-price` on the pricing page.

**Values (default).** size 321.33 x 36; background transparent; text Inter 14/20 500, rgba(23, 23, 23, 0.5).

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan card's "Start 14-day trial" action; measured never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 329.33 x 36; background transparent; text Inter 14/20 400, #171717 `color.neutral.900`; layers button.group.flex 329.3x36.0 rgb(255, 255, 255) T:1px solid rgb(237, 237, 237) / R:1px solid rgb(237, 237, 237) / B:1px solid rgb(237, 237, 237) / L:1px solid rgb(237, 237, 237) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.03) 0px 1px 3px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 10px |
| hover | layers button.group.flex 329.3x36.0 rgb(250, 250, 250) T:1px solid rgb(237, 237, 237) / R:1px solid rgb(237, 237, 237) / B:1px solid rgb(237, 237, 237) / L:1px solid rgb(237, 237, 237) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.03) 0px 1px 3px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 10px |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a.w-full 329.3x36.0 1px auto rgb(0, 95, 204) offset 1px; button.group.flex 329.3x36.0 rgb(255, 255, 255) T:1px solid rgb(237, 237, 237) / R:1px solid rgb(237, 237, 237) / B:1px solid rgb(237, 237, 237) / L:1px solid rgb(237, 237, 237) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.03) 0px 1px 3px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 10px |

Child layers that carry the look: button 329.3x36 background #ffffff `color.neutral.white` border 1px solid #ededed radius 10px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.03) 0px 1px 3px 0px.

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan card
A pricing plan card (the painted ancestor of the plan name). Read as `plan-card` on the pricing page.

**Values (default).** size 1062 x 623; border 1px solid #ededed; radius 12px; background #fafafa `color.neutral.50`; text Inter 16/24 500, #262626 `color.neutral.800`.

![Plan card default](components/crops/plan-card-default.png)

#### FAQ accordion
A billing-FAQ accordion trigger, read closed: at rest, on hover, on keyboard focus and forced pressed. Read as `faq-trigger` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 688 x 56; padding 16px 0px; background transparent; text Inter 16/24 500, #262626 `color.neutral.800`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #0a0a0a `color.neutral.950` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px; layers button.flex.flex-1 688.0x56.0 1px auto rgb(0, 95, 204) offset 0px |

![FAQ accordion default](components/crops/faq-trigger-default.png) ![FAQ accordion hover](components/crops/faq-trigger-hover.png) ![FAQ accordion focus-visible](components/crops/faq-trigger-focus-visible.png) ![FAQ accordion pressed](components/crops/faq-trigger-pressed.png)

### Compare (vs Bitly)

The /compare/bitly surface: the Satoshi headline and the feature comparison table.

#### Compare headline
The "Dub vs Bitly" page heading. Read as `cmp-h1` on the compare page.

**Values (default).** size 576 x 48; background transparent; text satoshi 48/48 500, #171717 `color.neutral.900`.

![Compare headline default](components/crops/cmp-h1-default.png)

#### Comparison table
The feature comparison table (Dub vs Bitly). Read as `cmp-table` on the compare page.

**Values (default).** size 958 x 1384; background transparent; text satoshi 16/24 700, #1f2937; icon 16 x 16, #6b7280; layers th.w-60.p-2 479.0x113.0 B:1px solid rgb(229, 231, 235); div.relative.isolate 134.0x30.0 rgb(255, 255, 255) T:1px solid rgb(209, 213, 219) / R:1px solid rgb(209, 213, 219) / B:1px solid rgb(209, 213, 219) / L:1px solid rgb(209, 213, 219) 9999px; div.absolute.inset-0 40.0x24.0 9999px; th.relative.w-28 239.5x113.0 rgb(255, 255, 255) B:1px solid rgb(229, 231, 235) 16px 16px 0px 0px; div.pointer-events.

Child layers that carry the look: th 479x113 border 1px solid #e5e7eb; div 134x30 background #ffffff `color.neutral.white` image linear-gradient(to right, #f3f4f6, rgba(243, 244, 246, 0)) border 1px solid #d1d5db radius 9999px; div 40x24 image linear-gradient(to right bottom, #1f2937, #6b7280) radius 9999px.

![Comparison table default](components/crops/cmp-table-default.png)

#### Comparison cell
A cell in the comparison table. Read as `cmp-check` on the compare page.

**Values (default).** size 479 x 77; padding 16px; border B: 1px solid #e5e7eb; background transparent; text satoshi 16/24 700, #1f2937; layers td.p-2.md:p-4 479.0x77.0 B:1px solid rgb(229, 231, 235).

Child layers that carry the look: td 479x77 border 1px solid #e5e7eb.

![Comparison cell default](components/crops/cmp-check-default.png)

### Customers

The /customers surface: the Satoshi headline and the dark customer story cards.

#### Customers headline
The "Meet our customers" heading. Read as `cust-h1` on the customers page.

**Values (default).** size 512 x 55.19; background transparent; text satoshi 48/55.2 500, #171717 `color.neutral.900`.

![Customers headline default](components/crops/cust-h1-default.png)

#### Customer card
A customer story card/logo tile; measured never followed. Read as `customer-card` on the customers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 128 x 480; radius 12px; background #171717 `color.neutral.900`; text Inter 18/28 500, #ffffff `color.neutral.white`; transition flex-grow 0.5s cubic-bezier(0.215, 0.61, 0.355, 1), flex-basis 0.5s cubic-bezier(0.215, 0.61, 0.355, 1) |
| hover | size 175.83 x 480 |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px |
| pressed | size 174.66 x 480 |

![Customer card default](components/crops/customer-card-default.png) ![Customer card hover](components/crops/customer-card-hover.png) ![Customer card focus-visible](components/crops/customer-card-focus-visible.png) ![Customer card pressed](components/crops/customer-card-pressed.png)

### Contact sales form

The /contact/sales card: work-email field, message textarea, topic pills and the Send submit — measured, never submitted.

#### Contact form card
The centred Talk-to-sales card; never filled past a deleted sample, never submitted. Read as `sales-card` on the contact-sales page.

**Values (default).** size 800 x 346; border R: 1px solid #e5e5e5 `color.neutral.200`; L: 1px solid #e5e5e5 `color.neutral.200`; background #ffffff `color.neutral.white`; text Inter 14/20 500, #171717 `color.neutral.900`.

![Contact form card default](components/crops/sales-card-default.png)

#### Email field
The work-email input; sample text was typed and deleted, nothing sent. Read as `sales-email` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 750 x 38; padding 8px 12px; border 1px solid #d4d4d4 `color.neutral.300`; radius 6px; background #ffffff `color.neutral.white`; text Inter 14/20 400, #171717 `color.neutral.900`; placeholder #a3a3a3 `color.neutral.400` |
| focused, filled | border 1px solid #737373 `color.neutral.500`; shadow #ffffff 0px 0px 0px 0px, #737373 0px 0px 0px 1px; outline 2px solid transparent, offset 2px |

![Email field default](components/crops/sales-email-default.png) ![Email field focused](components/crops/sales-email-focused.png) ![Email field filled](components/crops/sales-email-filled.png)

#### Message textarea
The "Tell us about your company's needs" textarea; focused only. Read as `sales-message` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 750 x 118; padding 8px 12px; border 1px solid #d4d4d4 `color.neutral.300`; radius 6px; background #ffffff `color.neutral.white`; text Inter 14/20 400, #171717 `color.neutral.900`; placeholder #a3a3a3 `color.neutral.400` |
| focused | border 1px solid #737373 `color.neutral.500`; shadow #ffffff 0px 0px 0px 0px, #737373 0px 0px 0px 1px; outline 2px solid transparent, offset 2px |

![Message textarea default](components/crops/sales-message-default.png) ![Message textarea focused](components/crops/sales-message-focused.png)

#### Topic option
A selectable topic pill on the contact form (Tools/Legal/…), read unselected: at rest, on hover, on keyboard focus and forced pressed; never submitted. Read as `sales-topic` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 57.52 x 20; background transparent; text Inter 14/20 400, #737373 `color.neutral.500`; transition color 0.075s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), fill 0.075s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.075s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, #737373 `color.neutral.500` |
| hover | text Inter 14/20 400, #404040 `color.neutral.700`; icon 14 x 14, #404040 `color.neutral.700` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px; layers button.sm:inline-flex.flex 57.5x20.0 1px auto rgb(0, 95, 204) offset 0px |
| pressed | text Inter 14/20 400, #404040 `color.neutral.700`; icon 14 x 14, #404040 `color.neutral.700` |

![Topic option default](components/crops/sales-topic-default.png) ![Topic option hover](components/crops/sales-topic-hover.png) ![Topic option focus-visible](components/crops/sales-topic-focus-visible.png) ![Topic option pressed](components/crops/sales-topic-pressed.png)

#### Send button
The Send-message submit; measured, never pressed (a press would submit the form). Read as `sales-submit` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 123.75 x 40; padding 0px 12px; border 1px solid #e5e5e5 `color.neutral.200`; radius 8px; background #f5f5f5 `color.neutral.100`; outline 2px solid transparent, offset 2px; text Inter 14/20 400, #737373 `color.neutral.500` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Send button default](components/crops/sales-submit-default.png) ![Send button hover](components/crops/sales-submit-hover.png) ![Send button pressed](components/crops/sales-submit-pressed.png)

### Log in and sign up

The auth boundary cards on app.dub.co, measured but never submitted: the 384px login and register cards, fields and SSO buttons in the plain system stack.

#### Login card
The centred sign-in column (heading, email form, SSO buttons); never filled past a deleted sample, never submitted. Read as `login-card` on the log in page.

**Values (default).** size 384 x 562; background transparent; text ui-sans-serif 20/28 600, #000000 `color.neutral.black`; icon 16 x 16, #171717 `color.neutral.900`; layers input.block.w-full 376.0x38.0 rgb(255, 255, 255) T:1px solid rgb(212, 212, 212) / R:1px solid rgb(212, 212, 212) / B:1px solid rgb(212, 212, 212) / L:1px solid rgb(212, 212, 212) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px 6px; button.group.flex 376.0x40.0 rgb(0, 0, 0) T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(.

Child layers that carry the look: input 376x38 background #ffffff `color.neutral.white` border 1px solid #d4d4d4 `color.neutral.300` radius 6px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; button 376x40 background #000000 `color.neutral.black` border 1px solid #000000 `color.neutral.black` radius 8px; div 171.3x1 border 1px solid #e5e5e5 `color.neutral.200`.

![Login card default](components/crops/login-card-default.png)

#### Email field
The email input; sample text was typed and deleted, nothing sent. Read as `email-field` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 376 x 38; padding 8px 12px; border 1px solid #d4d4d4 `color.neutral.300`; radius 6px; background #ffffff `color.neutral.white`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text ui-sans-serif 14/20 400, #000000 `color.neutral.black`; placeholder #a3a3a3 `color.neutral.400` |
| focused, filled | border 1px solid #000000 `color.neutral.black`; shadow #ffffff 0px 0px 0px 0px, #000000 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; outline 2px solid transparent, offset 2px |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png) ![Email field filled](components/crops/email-field-filled.png)

#### Email submit
The "Log in with email" submit; measured, never pressed (a press would start a sign-in). Read as `email-submit` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 376 x 40; padding 0px 12px; border 1px solid #000000 `color.neutral.black`; radius 8px; background #000000 `color.neutral.black`; text ui-sans-serif 14/20 400, #ffffff `color.neutral.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px |
| pressed | shadow #ffffff 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 4px |

![Email submit default](components/crops/email-submit-default.png) ![Email submit hover](components/crops/email-submit-hover.png) ![Email submit focus-visible](components/crops/email-submit-focus-visible.png) ![Email submit pressed](components/crops/email-submit-pressed.png)

#### Google SSO
The Continue-with-Google button; measured, never followed. Read as `oauth-google` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 376 x 40; padding 0px 12px; border 1px solid #e5e5e5 `color.neutral.200`; radius 8px; background #ffffff `color.neutral.white`; outline 2px solid transparent, offset 2px; text ui-sans-serif 14/20 400, #171717 `color.neutral.900`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #171717 `color.neutral.900` |
| hover | background #fafafa `color.neutral.50` |
| focus-visible | border 1px solid #a3a3a3 `color.neutral.400` |
| pressed | background #fafafa `color.neutral.50` |

![Google SSO default](components/crops/oauth-google-default.png) ![Google SSO hover](components/crops/oauth-google-hover.png) ![Google SSO focus-visible](components/crops/oauth-google-focus-visible.png) ![Google SSO pressed](components/crops/oauth-google-pressed.png)

#### GitHub SSO
The Continue-with-GitHub button; measured, never followed. Read as `oauth-github` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 376 x 40; padding 0px 12px; border 1px solid #e5e5e5 `color.neutral.200`; radius 8px; background #ffffff `color.neutral.white`; outline 2px solid transparent, offset 2px; text ui-sans-serif 14/20 400, #171717 `color.neutral.900`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #000000 `color.neutral.black` |
| hover | background #fafafa `color.neutral.50` |
| focus-visible | border 1px solid #a3a3a3 `color.neutral.400` |
| pressed | background #fafafa `color.neutral.50` |

![GitHub SSO default](components/crops/oauth-github-default.png) ![GitHub SSO hover](components/crops/oauth-github-hover.png) ![GitHub SSO focus-visible](components/crops/oauth-github-focus-visible.png) ![GitHub SSO pressed](components/crops/oauth-github-pressed.png)

#### SAML SSO
The Continue-with-SAML-SSO button; measured, never followed. Read as `oauth-saml` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 376 x 40; padding 0px 12px; border 1px solid #e5e5e5 `color.neutral.200`; radius 8px; background #ffffff `color.neutral.white`; outline 2px solid transparent, offset 2px; text ui-sans-serif 14/20 400, #171717 `color.neutral.900`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #171717 `color.neutral.900` |
| hover | background #fafafa `color.neutral.50` |
| focus-visible | border 1px solid #a3a3a3 `color.neutral.400` |
| pressed | background #fafafa `color.neutral.50` |

![SAML SSO default](components/crops/oauth-saml-default.png) ![SAML SSO hover](components/crops/oauth-saml-hover.png) ![SAML SSO focus-visible](components/crops/oauth-saml-focus-visible.png) ![SAML SSO pressed](components/crops/oauth-saml-pressed.png)

#### Auth switch link
The "Sign up" link under the card; measured never followed. Read as `auth-link` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 50.7 x 17; background transparent; text ui-sans-serif 14/20 600, #404040 `color.neutral.700`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text ui-sans-serif 14/20 600, #171717 `color.neutral.900` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a.font-semibold.text-neutral-700 50.7x17.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text ui-sans-serif 14/20 600, #171717 `color.neutral.900` |

![Auth switch link default](components/crops/auth-link-default.png) ![Auth switch link hover](components/crops/auth-link-hover.png) ![Auth switch link focus-visible](components/crops/auth-link-focus-visible.png) ![Auth switch link pressed](components/crops/auth-link-pressed.png)

#### Register card
The centred create-account column; never filled or submitted. Read as `register-card` on the register page.

**Values (default).** size 384 x 510; background transparent; text ui-sans-serif 20/28 600, #000000 `color.neutral.black`; icon 16 x 16, #171717 `color.neutral.900`; layers input.w-full.max-w-md 376.0x38.0 rgb(255, 255, 255) T:1px solid rgb(212, 212, 212) / R:1px solid rgb(212, 212, 212) / B:1px solid rgb(212, 212, 212) / L:1px solid rgb(212, 212, 212) 6px; button.group.flex 376.0x40.0 rgb(0, 0, 0) T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid rgb(0, 0, 0) 8px; div.grow.basis-0 171.3x1.0 B:1px solid rgb(229, 229, 229); d.

Child layers that carry the look: input 376x38 background #ffffff `color.neutral.white` border 1px solid #d4d4d4 `color.neutral.300` radius 6px; button 376x40 background #000000 `color.neutral.black` border 1px solid #000000 `color.neutral.black` radius 8px; div 171.3x1 border 1px solid #e5e5e5 `color.neutral.200`.

![Register card default](components/crops/register-card-default.png)

#### Register email field
The signup email input; focused only, never filled or submitted. Read as `register-field` on the register page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 376 x 38; padding 8px 12px; border 1px solid #d4d4d4 `color.neutral.300`; radius 6px; background #ffffff `color.neutral.white`; text ui-sans-serif 14/20 400, #171717 `color.neutral.900`; placeholder #a3a3a3 `color.neutral.400` |
| focused | border 1px solid #737373 `color.neutral.500`; shadow #ffffff 0px 0px 0px 0px, #737373 0px 0px 0px 1px; outline 2px solid transparent, offset 2px |

![Register email field default](components/crops/register-field-default.png) ![Register email field focused](components/crops/register-field-focused.png)

### Docs and help (Mintlify)

The Mintlify docs surface on /docs and /help — the only place a real theme toggle exists: the 288px sidebar, search pill, theme button, headings and feedback controls, measured in both light and dark.

#### Docs sidebar
The left docs navigation column. Read as `docs-sidebar` on the docs page.

**Values (default).** size 288 x 804; border R: 1px solid #eef0f5 `color.gray.100`; background transparent; text Inter 12/16 700, #17191e `color.gray.900`; transition transform 0.1s cubic-bezier(0.4, 0, 0.2, 1), translate 0.1s cubic-bezier(0.4, 0, 0.2, 1), scale 0.1s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 8, #9fa1a6 `color.gray.400`; layers nav.hidden.sticky 288.0x804.0 R:1px solid rgb(238, 240, 245); a.group.flex 267.0x32.0 oklab(0.546496 -0.0304804 -0.243625 / 0.1) 12px; div.sidebar-nav-group-divider.h-px 259.0x1.0 rgb(238, 240, 245); div.sidebar-nav-group-divider.h-px 259.0x1.0 rgb(238, 240, 245); div.sidebar-nav-group-divider.h-px 259.0x1.0 rgb(238, 240, 245); div.z-10.flex 4.0x772.0 rgb(250, 250, 250) 9999px.

Child layers that carry the look: nav 288x804 border 1px solid #eef0f5 `color.gray.100`; a 267x32 background oklab(0.546496 -0.0304804 -0.243625 / 0.1) radius 12px; div 259x1 background #eef0f5 `color.gray.100`.

![Docs sidebar default](components/crops/docs-sidebar-default.png)

#### Docs nav item
A sidebar navigation item. Read as `docs-nav-item` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 267 x 32; padding 6px 12px 6px 16px; radius 12px; background oklab(0.546496 -0.0304804 -0.243625 / 0.1); text Inter 14/20 400, #155dfc `color.brand.primary` |
| focus-visible | outline 1px auto #155dfc `color.brand.primary`, offset -2px |

![Docs nav item default](components/crops/docs-nav-item-default.png) ![Docs nav item hover](components/crops/docs-nav-item-hover.png) ![Docs nav item focus-visible](components/crops/docs-nav-item-focus-visible.png) ![Docs nav item pressed](components/crops/docs-nav-item-pressed.png)

#### Search trigger
The "Search… ⌘K" trigger; measured, the palette was never opened. Read as `docs-search` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 36; padding 0px 12px 0px 14px; radius 9999px; background oklab(0.15767 -0.00243126 -0.00955348 / 0.03); shadow oklab(0.708903 -0.000163108 -0.00756282 / 0.3) 0px 0px 0px 0px; text Inter 14/24 400, #707277 `color.gray.500`; icon 16 x 16, #3f4146 `color.gray.700` |
| hover | background oklab(0.15767 -0.00243126 -0.00955348 / 0.1); shadow oklab(0.438538 -0.000211209 -0.00855511 / 0.3) 0px 0px 0px 0px; icon 16 x 16, #25282d `color.gray.800` |
| focus-visible | outline 1px auto #155dfc `color.brand.primary`, offset 0px |
| pressed | background oklab(0.15767 -0.00243126 -0.00955348 / 0.1); shadow oklab(0.438538 -0.000211209 -0.00855511 / 0.3) 0px 0px 0px 0px; icon 16 x 16, #25282d `color.gray.800` |

![Search trigger default](components/crops/docs-search-default.png) ![Search trigger hover](components/crops/docs-search-hover.png) ![Search trigger focus-visible](components/crops/docs-search-focus-visible.png) ![Search trigger pressed](components/crops/docs-search-pressed.png)

#### Theme toggle
The "Change theme preference" button; its dropdown supplied the docs dark shots. Read as `docs-theme` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 30 x 30; padding 8px; radius 9999px; background oklab(0.275869 -0.00163545 -0.0100618 / 0.04); text Inter 14/20 400, oklab(0.15767 -0.00243126 -0.00955348 / 0.5); icon 14 x 16, #505257 `color.gray.600` |
| hover | icon 14 x 16, #25282d `color.gray.800` |
| focus-visible | outline 1px auto #155dfc `color.brand.primary`, offset 0px |
| pressed | icon 14 x 16, #25282d `color.gray.800` |

![Theme toggle default](components/crops/docs-theme-default.png) ![Theme toggle hover](components/crops/docs-theme-hover.png) ![Theme toggle focus-visible](components/crops/docs-theme-focus-visible.png) ![Theme toggle pressed](components/crops/docs-theme-pressed.png)

#### Docs headline
The docs page h1 (Introduction). Read as `docs-h1` on the docs page.

**Values (default).** size 194.67 x 40; background transparent; text Satoshi 36/40 600, #17191e `color.gray.900`.

![Docs headline default](components/crops/docs-h1-default.png)

#### Copy-page button
The "Copy page" action; measured, never pressed. Read as `docs-copy` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 121.55 x 34; padding 6px 12px; border T: 1px solid #dfe1e6 `color.gray.200`; B: 1px solid #dfe1e6 `color.gray.200`; L: 1px solid #dfe1e6 `color.gray.200`; radius 12px 0px 0px 12px; background #ffffff `color.neutral.white`; text Inter 14/20 500, #3f4146 `color.gray.700`; icon 16 x 16, #3f4146 `color.gray.700` |
| hover | background oklab(0.438538 -0.000211209 -0.00855511 / 0.05) |
| focus-visible | outline 1px auto #155dfc `color.brand.primary`, offset 0px |
| pressed | background oklab(0.438538 -0.000211209 -0.00855511 / 0.05) |

![Copy-page button default](components/crops/docs-copy-default.png) ![Copy-page button hover](components/crops/docs-copy-hover.png) ![Copy-page button focus-visible](components/crops/docs-copy-focus-visible.png) ![Copy-page button pressed](components/crops/docs-copy-pressed.png)

#### Feedback button
A docs "Was this helpful" Yes/No button; measured, never pressed (a press would send feedback). Read as `docs-feedback` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 81.98 x 34; padding 8px 14px; border 1px solid oklab(0.909644 -0.000139236 -0.0070951 / 0.7); radius 12px; background oklab(0.999994 0.0000455678 0.0000200868 / 0.5); text Inter 14/16 400, #505257 `color.gray.600`; icon 16 x 16, #505257 `color.gray.600` |
| hover | border 1px solid #707277 `color.gray.500`; text Inter 14/16 400, #3f4146 `color.gray.700`; icon 16 x 16, #3f4146 `color.gray.700` |
| focus-visible | outline 2px solid #155dfc `color.brand.primary`, offset -2px |
| pressed | border 1px solid #707277 `color.gray.500`; text Inter 14/16 400, #3f4146 `color.gray.700`; icon 16 x 16, #3f4146 `color.gray.700` |

![Feedback button default](components/crops/docs-feedback-default.png) ![Feedback button hover](components/crops/docs-feedback-hover.png) ![Feedback button focus-visible](components/crops/docs-feedback-focus-visible.png) ![Feedback button pressed](components/crops/docs-feedback-pressed.png)

#### Docs nav tab
The docs surface's top navigation tab (API Reference); measured never followed. A docs landing card was never captured — an earlier global locator read this nav tab under the card name. Read as `docs-nav-tab` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 118.81 x 40; background transparent; text Inter 14/20 500, #25282d `color.gray.800`; icon 16 x 16, #25282d `color.gray.800`; layers svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 rgb(37, 40, 45) |
| hover | layers svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 rgb(37, 40, 45); div.absolute.bottom-0 118.8x1.0 rgb(223, 225, 230) |
| focus-visible | outline 1px auto #155dfc `color.brand.primary`, offset 1px; layers a.link.nav-tabs-item 118.8x40.0 1px auto rgb(21, 93, 252) offset 1px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 rgb(37, 40, 45) |
| pressed | layers svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 rgb(37, 40, 45); div.absolute.bottom-0 118.8x1.0 rgb(223, 225, 230) |

Child layers that carry the look: svg 16x16 background #25282d `color.gray.800`.

![Docs nav tab default](components/crops/docs-nav-tab-default.png) ![Docs nav tab hover](components/crops/docs-nav-tab-hover.png) ![Docs nav tab focus-visible](components/crops/docs-nav-tab-focus-visible.png) ![Docs nav tab pressed](components/crops/docs-nav-tab-pressed.png)

#### Docs headline (dark)
The docs h1 with html.dark painted — the real dark theme. Read as `dk-docs-h1` on the docs (dark) page.

**Values (default).** size 194.67 x 40; background transparent; text Satoshi 36/40 600, #dfe1e6 `color.gray.200`.

![Docs headline (dark) default](components/crops/dk-docs-h1-default.png)

#### Docs sidebar (dark)
The left nav column in dark. Read as `dk-docs-sidebar` on the docs (dark) page.

**Values (default).** size 288 x 804; border R: 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1); background transparent; text Inter 12/16 700, #dfe1e6 `color.gray.200`; transition transform 0.1s cubic-bezier(0.4, 0, 0.2, 1), translate 0.1s cubic-bezier(0.4, 0, 0.2, 1), scale 0.1s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 8, #505257 `color.gray.600`; layers nav.hidden.sticky 288.0x804.0 R:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1); a.group.flex 267.0x32.0 oklab(0.546496 -0.0304804 -0.243625 / 0.1) 12px; div.sidebar-nav-group-divider.h-px 259.0x1.0 oklab(0.999994 0.0000455678 0.0000200868 / 0.1); div.sidebar-nav-group-divider.h-px 259.0x1.0 oklab(0.999994 0.0000455678 0.0000200868 / 0.1); div.sidebar-nav-group-divider.h-px 259.0x1.0 okl.

Child layers that carry the look: nav 288x804 border 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1); a 267x32 background oklab(0.546496 -0.0304804 -0.243625 / 0.1) radius 12px; div 259x1 background oklab(0.999994 0.0000455678 0.0000200868 / 0.1).

![Docs sidebar (dark) default](components/crops/dk-docs-sidebar-default.png)

#### Docs nav item (dark)
A sidebar item in dark. Read as `dk-docs-nav-item` on the docs (dark) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 267 x 32; padding 6px 12px 6px 16px; radius 12px; background oklab(0.546496 -0.0304804 -0.243625 / 0.1); text Inter 14/20 400, #155dfc `color.brand.primary` |
| focus-visible | outline 1px auto #155dfc `color.brand.primary`, offset -2px |

![Docs nav item (dark) default](components/crops/dk-docs-nav-item-default.png) ![Docs nav item (dark) hover](components/crops/dk-docs-nav-item-hover.png) ![Docs nav item (dark) focus-visible](components/crops/dk-docs-nav-item-focus-visible.png) ![Docs nav item (dark) pressed](components/crops/dk-docs-nav-item-pressed.png)

#### Copy-page button (dark)
The "Copy page" action in dark. Read as `dk-docs-copy` on the docs (dark) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 121.55 x 34; padding 6px 12px; border T: 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.07); B: 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.07); L: 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.07); radius 12px 0px 0px 12px; background #090b10 `color.brand.canvas-dark`; text Inter 14/20 500, #ced0d5 `color.gray.300`; icon 16 x 16, #ced0d5 `color.gray.300` |
| hover | background oklab(0.909644 -0.000139236 -0.0070951 / 0.05) |
| focus-visible | outline 1px auto #155dfc `color.brand.primary`, offset 0px |
| pressed | background oklab(0.909644 -0.000139236 -0.0070951 / 0.05) |

![Copy-page button (dark) default](components/crops/dk-docs-copy-default.png) ![Copy-page button (dark) hover](components/crops/dk-docs-copy-hover.png) ![Copy-page button (dark) focus-visible](components/crops/dk-docs-copy-focus-visible.png) ![Copy-page button (dark) pressed](components/crops/dk-docs-copy-pressed.png)

#### Search trigger (dark)
The "Search…" trigger in dark. Read as `dk-docs-search` on the docs (dark) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 36; padding 0px 12px 0px 14px; radius 9999px; background oklab(0.999994 0.0000455678 0.0000200868 / 0.03); shadow oklab(0.438538 -0.000211209 -0.00855511 / 0.3) 0px 0px 0px 0px; text Inter 14/24 400, oklab(0.999994 0.0000455678 0.0000200868 / 0.5); icon 16 x 16, #9fa1a6 `color.gray.400` |
| hover | background oklab(0.999994 0.0000455678 0.0000200868 / 0.1); shadow oklab(0.551995 -0.000187308 -0.00806379 / 0.3) 0px 0px 0px 0px; icon 16 x 16, #dfe1e6 `color.gray.200` |
| focus-visible | outline 1px auto #155dfc `color.brand.primary`, offset 0px |
| pressed | background oklab(0.999994 0.0000455678 0.0000200868 / 0.1); shadow oklab(0.551995 -0.000187308 -0.00806379 / 0.3) 0px 0px 0px 0px; icon 16 x 16, #dfe1e6 `color.gray.200` |

![Search trigger (dark) default](components/crops/dk-docs-search-default.png) ![Search trigger (dark) hover](components/crops/dk-docs-search-hover.png) ![Search trigger (dark) focus-visible](components/crops/dk-docs-search-focus-visible.png) ![Search trigger (dark) pressed](components/crops/dk-docs-search-pressed.png)

### Footer

The marketing footer: link columns and the round social icon buttons.

#### Footer
The marketing footer: wordmark, social icons and the Product/Solutions/Resources/Tools/Company link columns. Read as `footer` on the home page.

**Values (default).** size 1024 x 402; background transparent; text Inter 14/20 500, #171717 `color.neutral.900`; icon 61.33 x 32, #262626 `color.neutral.800`; layers span.flex.size-4 16.0x16.0 rgb(192, 132, 252) T:1px solid rgba(0, 0, 0, 0.05) / R:1px solid rgba(0, 0, 0, 0.05) / B:1px solid rgba(0, 0, 0, 0.05) / L:1px solid rgba(0, 0, 0, 0.05) 4px; span.flex.size-4 16.0x16.0 rgb(74, 222, 128) T:1px solid rgba(0, 0, 0, 0.05) / R:1px solid rgba(0, 0, 0, 0.05) / B:1px solid rgba(0, 0, 0, 0.05) / L:1px solid rgba(0, 0, 0, 0.05) 4px; span.flex.size-4 16.0x16.0 rgb(.

Child layers that carry the look: span 16x16 background #c084fc border 1px solid rgba(0, 0, 0, 0.05) radius 4px; span 16x16 background #4ade80 `color.brand.green-400` border 1px solid rgba(0, 0, 0, 0.05) radius 4px; span 16x16 background #fb923c border 1px solid rgba(0, 0, 0, 0.05) radius 4px.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 164 x 20; background transparent; text Inter 14/20 400, #737373 `color.neutral.500`; transition color 0.075s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), fill 0.075s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.075s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 14/20 400, #404040 `color.neutral.700` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a.flex.items-center 164.0x20.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text Inter 14/20 400, #404040 `color.neutral.700` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social icon link
A social icon button in the footer (Twitter/GitHub/LinkedIn/YouTube). Read as `social-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; padding 4px; radius 9999px; background transparent; text Inter 16/24 400, #0a0a0a `color.neutral.950`; icon 16 x 16, #171717 `color.neutral.900` |
| hover | icon 16 x 16, #525252 `color.neutral.600` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 1px; layers a.group.rounded-full 24.0x24.0 1px auto rgb(0, 95, 204) offset 1px 9999px |
| pressed | icon 16 x 16, #525252 `color.neutral.600` |

![Social icon link default](components/crops/social-link-default.png) ![Social icon link hover](components/crops/social-link-hover.png) ![Social icon link focus-visible](components/crops/social-link-focus-visible.png) ![Social icon link pressed](components/crops/social-link-pressed.png)

### Mobile (390 wide)

The marketing surface at phone width: the compact header, the menu overlay and the stacked hero.

#### Mobile nav
The sticky top bar at 390 (wordmark + menu button). Read as `m-nav` on the home page at 390 wide.

**Values (default).** size 390 x 56; background transparent; text Inter 16/24 400, #0a0a0a `color.neutral.950`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 46 x 24, #000000 `color.neutral.black`; layers div.absolute.inset-0 390.0x56.0 B:1px solid rgba(0, 0, 0, 0); div.pointer-events-none.absolute 0.0x0.0 rgba(23, 23, 23, 0.05) 8px; a.transition-all.border-border-subtle 0.0x0.0 rgb(255, 255, 255) T:1px solid rgb(229, 229, 229) / R:1px solid rgb(229, 229, 229) / B:1px solid rgb(229, 229, 229) / L:1px solid rgb(229, 229, 229) 2px solid rgba(0, 0, 0, 0) offset 2px 8px; a.transition-all.border-black 0.

Child layers that carry the look: div 390x56 border 1px solid transparent; div 0x0 background rgba(23, 23, 23, 0.05) radius 8px; a 0x0 background #ffffff `color.neutral.white` border 1px solid #e5e5e5 `color.neutral.200` radius 8px.

![Mobile nav default](components/crops/m-nav-default.png)

#### Menu button
The round menu toggle in the mobile nav. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 36 x 36; padding 8px; radius 9999px; background transparent; text Inter 16/24 400, #0a0a0a `color.neutral.950`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #525252 `color.neutral.600`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The menu panel opened by its own toggle. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; padding 64px 20px; background #ffffff `color.neutral.white`; text Inter 16/24 600, #0a0a0a `color.neutral.950`; icon 20 x 20, #737373 `color.neutral.500`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
An item inside the opened mobile menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 350 x 24; background transparent; text Inter 16/24 600, #0a0a0a `color.neutral.950`; icon 20 x 20, #737373 `color.neutral.500` |
| focus-visible | outline 1px auto #005fcc `measured.focus-outline`, offset 0px; layers button.flex.w-full 350.0x24.0 1px auto rgb(0, 95, 204) offset 0px |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 294 x 80; background transparent; text satoshi 36/40 500, #171717 `color.neutral.900`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Dub wordmark, the mega-menu product glyphs, the Google/GitHub SSO marks, the social icons and the docs chrome glyphs) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Dub's product — the link-management workspace, link creation, analytics dashboards, domains, tags, webhooks, integrations and billing — lives behind /login on app.dub.co and was never reached. The auth cards on /login and /register were captured as surfaces, never filled past a deleted sample and never submitted; the contact-sales form on /contact/sales was measured, never sent.

### Pages

- **The workspace.** Every post-login surface (links, analytics, domains, tags, webhooks, settings, billing) needs an account and was never reached; /login and /register were captured as forms and never filled or submitted.
- **The dashboard mock.** The `demo-panel` under the home hero is a published illustration of the product UI, not the app — it was measured as marketing content.
- **Checkout and onboarding.** Every Sign-up, Start-for-free, Start-trial and Send-message action was measured, never followed past its public landing; no plan was ever purchased.
- **The docs search palette.** The 'Search… ⌘K' trigger was measured; the palette it opens (and the Mintlify AI assistant behind it) was never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface (the contact-sales submit paints disabled-grey until the required fields hold text, captured at rest).
- **hero-badge and sales-submit focus-visible** recorded `via: focus failed` — a real keyboard focus could not be held there — so their focus look is uncaptured, not measured as absent.
- **Email-field 'focus-visible'** is the field's `focused` state (clicked into): a black border plus a 1px black ring shadow, not the browser outline buttons draw.

### Themes

dub.co is not a themed product signed out: the marketing pages and the app.dub.co auth shell paint light only. The docs/help surface (Mintlify) carries the site's one real theme toggle — a Light/Dark/System dropdown that sets `dark` on <html> (localStorage isDarkMode) — and was captured in both: the dark set is the .dark re-binding the probe and the dk-docs-* components measured.

### Fonts

- **Satoshi** (Fontshare variable, marketing headings and docs h1s), **Inter** (marketing and docs body, self-hosted woff2 subsets), **Paper Mono** (docs code, Mintlify bundle), **GeistMono** (marketing code, next/font) are the served faces; the app.dub.co auth shell paints a plain ui-sans-serif system stack. None is distributed with the package — the style guide falls back to system sans.

### Screenshots

- Product illustrations, customer logos, the Dub wordmark and blog/changelog post art in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, customer stories, blog and changelog posts and the comparison table's claims are the product's content; only frames and components were measured.
