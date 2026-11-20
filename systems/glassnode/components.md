# Glassnode components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from glassnode.com and its public subdomains on 2026-11-16, signed out, in headed Chromium under Xvfb at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the newsletter and Auth0 username fields were typed into then cleared, never submitted; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (71 components, 178 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/20.8 400, #000000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (168 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture: `light` for the marketing pages, the studio shell, research and docs; `dark` for the tokenization registry (its painted default). Theme-switched states keep the page's painted theme and take a `theme-*` state name: `*-light-theme-dark.png` is the Ghost/GitBook dark surface reached by the site's own theme control, and `tokenization-dark-theme-light.png` the registry's light surface. The studio's `html[data-theme='dark-theme']` layer is declared but has no public control, so no screenshot paints it — its values are declared-not-painted tokens only. The Auth0 login is reached by the studio shell's real 'Log in' button; its landing URL's volatile `?state=` is sanitized to origin+path in every sidecar. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages bounded at eight chunks with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x) for default shots and 390 wide for stitched `-full` tiles.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `glassnode.com/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu-products](screenshots/home-light-menu-products.png) |
| Studio (product page) | `glassnode.com/products/studio` | [default](screenshots/products-studio-light-default.png), [full](screenshots/products-studio-light-full.png) |
| Data (product page) | `glassnode.com/products/data` | [default](screenshots/products-data-light-default.png), [full](screenshots/products-data-light-full.png) |
| Research services | `glassnode.com/products/research` | [default](screenshots/products-research-light-default.png), [full](screenshots/products-research-light-full.png) |
| Market Compass | `glassnode.com/products/studio/market-compass` | [default](screenshots/products-market-compass-light-default.png), [full](screenshots/products-market-compass-light-full.png) |
| Alpha Lab | `glassnode.com/products/studio/alpha-lab` | [default](screenshots/products-alpha-lab-light-default.png), [full](screenshots/products-alpha-lab-light-full.png) |
| Bitcoin Vector pricing | `glassnode.com/pricing/vector` | [default](screenshots/pricing-vector-light-default.png), [full](screenshots/pricing-vector-light-full.png) |
| About | `glassnode.com/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Contact | `glassnode.com/contact` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Customer stories | `glassnode.com/customer-stories` | [default](screenshots/customer-stories-light-default.png), [full](screenshots/customer-stories-light-full.png) |
| Events | `glassnode.com/events` |  |
| For trading and investing | `glassnode.com/solutions/trading-and-investing` | [default](screenshots/solutions-trading-light-default.png), [full](screenshots/solutions-trading-light-full.png) |
| For content creation | `glassnode.com/solutions/crypto-content-creation` | [default](screenshots/solutions-content-light-default.png), [full](screenshots/solutions-content-light-full.png) |
| Studio pricing | `studio.glassnode.com/pricing` | [default](screenshots/studio-pricing-light-default.png), [full](screenshots/studio-pricing-light-full.png) |
| Studio charts | `studio.glassnode.com/charts` | [default](screenshots/studio-charts-light-default.png) |
| Studio dashboards | `studio.glassnode.com/dashboards` | [default](screenshots/studio-dashboards-light-default.png) |
| Studio Market Compass gate | `studio.glassnode.com/market-compass` | [default](screenshots/studio-market-compass-light-default.png), [full](screenshots/studio-market-compass-light-full.png) |
| Studio get-listed | `studio.glassnode.com/get-listed` | [default](screenshots/studio-get-listed-light-default.png), [full](screenshots/studio-get-listed-light-full.png) |
| Studio contact | `studio.glassnode.com/contact` | [default](screenshots/studio-contact-light-default.png), [full](screenshots/studio-contact-light-full.png) |
| Auth0 login | `auth.glassnode.com/u/login` | [default](screenshots/auth-login-light-default.png), [full](screenshots/auth-login-light-full.png) |
| Research | `research.glassnode.com/` | [default](screenshots/research-home-light-default.png), [full](screenshots/research-home-light-full.png), [theme-dark](screenshots/research-home-light-theme-dark.png) |
| Research article | `research.glassnode.com/ (first index article)` | [default](screenshots/research-article-light-default.png), [full](screenshots/research-article-light-full.png) |
| Docs overview | `docs.glassnode.com/` | [default](screenshots/docs-home-light-default.png), [full](screenshots/docs-home-light-full.png), [theme-dark](screenshots/docs-home-light-theme-dark.png) |
| Docs metric catalog | `docs.glassnode.com/data/metric-catalog` | [default](screenshots/docs-metric-light-default.png) |
| Tokenization registry | `tokenization.glassnode.com/` | [default](screenshots/tokenization-dark-default.png), [full](screenshots/tokenization-dark-full.png), [theme-light](screenshots/tokenization-dark-theme-light.png) |
| Home, phone | `glassnode.com/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Studio pricing, phone | `studio.glassnode.com/pricing` | [default](screenshots/mobile-studio-pricing-light-default.png), [full](screenshots/mobile-studio-pricing-light-full.png) |
| Research, phone | `research.glassnode.com/` | [default](screenshots/mobile-research-home-light-default.png), [full](screenshots/mobile-research-home-light-full.png) |
| Docs, phone | `docs.glassnode.com/` | [default](screenshots/mobile-docs-home-light-default.png), [full](screenshots/mobile-docs-home-light-full.png) |
| Tokenization, phone | `tokenization.glassnode.com/` | [default](screenshots/mobile-tokenization-dark-default.png), [full](screenshots/mobile-tokenization-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Products dropdown | every marketing page header | the 'Products' trigger (a local UI toggle — a hover opens it; click/Enter the fallback) | [nav-dropdown-btn](#nav-dropdown-trigger), [nav-menu-item](#dropdown-item) |
| Mobile nav overlay | home page, phone width | the header hamburger's own toggle | [m-drawer](#mobile-nav-overlay) |
| Research theme toggle | research pages | the '.gh-theme-toggle' button — measured at rest; the dark surface was captured as the theme-dark screenshots rather than by holding the toggle | [res-theme-toggle](#theme-toggle), [research-home-light-theme-dark](screenshots/research-home-light-theme-dark.png) |
| Docs theme buttons | docs pages | 'Switch to light/dark theme' — measured at rest; the dark surface is the theme-dark screenshots | [docs-theme-btn](#theme-button), [docs-home-light-theme-dark](screenshots/docs-home-light-theme-dark.png) |
| Tokenization theme button | the registry | 'Switch to light theme' — measured at rest on the painted dark surface; the light surface is the theme-light screenshot | [tok-theme-btn](#theme-button-2), [tokenization-dark-theme-light](screenshots/tokenization-dark-theme-light.png) |
| Vector FAQ | /pricing/vector | the question rows are local toggles; 'Download sample' and the billing select were measured, never pressed or changed | [vec-faq](#faq-accordion), [vec-download-btn](#download-sample-button), [vec-billing-select](#billing-cycle-select) |
| Studio catalog expanders | studio /pricing | 'Show N more metrics' rows are local toggles; the pricing FAQ rows likewise | [st-metrics-expander](#metric-catalog-expander), [st-faq](#faq-accordion-2) |
| Newsletter + username fields | the marketing footer, /contact, research, the Auth0 card | typed into then cleared — nothing sent; the Auth0 form was never submitted | [newsletter-field](#newsletter-field), [auth-email](#username-field) |
| Log in / Sign up | the studio navbar | 'Log in' navigates to the Auth0 universal login — captured on auth-login; 'Sign up' and every CTA were measured, never followed | [st-login-btn](#log-in-button), [auth-card](#login-card) |
| Signed-in product | a Glassnode account | the charting workbench, saved dashboards, API keys and billing need an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 26 components were given a real keyboard focus. 24 draw an outline ring: `nav-link` (1px auto #101010 `light.measured.border.focusRing`, offset 1px), `nav-cta` (1px auto #101010 `light.measured.border.focusRing`, offset 1px), `privacy-btn` (1px auto #101010 `light.measured.border.focusRing`, offset 0px), `footer-link` (1px auto #101010 `light.measured.border.focusRing`, offset 1px), `vec-download-btn` (1px auto #101010 `light.measured.border.focusRing`, offset 0px), `res-nav-link` (1px auto #101010 `light.measured.border.focusRing`, offset 1px), `res-theme-toggle` (1px auto #101010 `light.measured.border.focusRing`, offset 0px), `docs-nav-link` (2px solid #cbd8fd, offset 1px), `docs-theme-btn` (2px solid #cbd8fd, offset 0px), `docs-quote-btn` (2px solid #cbd8fd, offset 1px), `m-menu-btn` (1px auto #e59700, offset 0px), `st-login-btn` (3px solid #404040, offset 1px), `st-signup-btn` (3px solid #404040, offset 1px), `st-search-btn` (3px solid #404040, offset 1px), `st-plan-signup-btn` (3px solid #404040, offset 1px), `st-configure-btn` (3px solid #404040, offset 1px), `auth-continue` (2px solid #635dff, offset 2px), `auth-google` (2px solid #635dff, offset 2px), `auth-reset` (2px solid #635dff, offset -1px), `auth-signup-link` (2px solid #635dff, offset -1px), `tok-nav-item` (2px solid #16cc8c `core.palette.accent`, offset 2px), `tok-search-btn` (2px solid #16cc8c `core.palette.accent`, offset 2px), `tok-theme-btn` (2px solid #16cc8c `core.palette.accent`, offset 2px), `tok-request-btn` (2px solid #16cc8c `core.palette.accent`, offset 2px). The other 2 show no measured change: `nav-dropdown-btn`, `st-nav-link`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | docs-metric-link |
| 0.12s | `ease` | background, background-color, color | res-theme-toggle, tok-theme-btn |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | docs-quote-btn, docs-side-link, docs-theme-btn, tok-nav-item, tok-request-btn, tok-search-btn, tok-stat |
| 0.15s | `ease` | width | tok-shell |
| 0.15s | `ease-in-out` | background-color, border-color, box-shadow | auth-email, auth-google, auth-password |
| 0.2s | `cubic-bezier(0.645, 0.045, 0.355, 1)` | all | contact-subscribe-btn, nav-cta, nav-dropdown-btn, newsletter-btn, st-configure-btn, st-login-btn, st-plan-signup-btn, st-search-btn and more |
| 0.2s | `ease` | all | partner-report-link |
| 0.2s | `ease-in-out` | all, border | contact-category, footer-link |
| 0.25s | `ease-in-out` | background-color, box-shadow | auth-continue |
| 0.3s | `ease` | color | st-nav-link |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 399.5 x 337.41 | - | - | transparent | none | 32px |
| [Login card](#login-card) | 320 x 210 | - | - | transparent | none | 0 |
| [Article card](#article-card) | 1280 x 407.45 | - | - | transparent | none | 0 |
| [Footer](#footer) | 1425 x 334.39 | - | - | #1a1a1a `light.studio.background.dark` | none | 64px 72px 24px 72px |
| [Mobile nav overlay](#mobile-nav-overlay) | 290 x 844 | - | - | #1a1a1a `light.studio.background.dark` | none | 0px 32px |
| [Contact category card](#contact-category-card) | 384 x 193.59 | 1px solid #dedfe1 `light.theme.border.default` | 2px | #ffffff `light.research.bg.default` | rgba(0, 0, 0, 0.08) 0px 8px 32px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px | 42px 24px |

## Components

### Marketing site chrome

The header on every glassnode.com page: the wordmark, the 'Products' dropdown trigger (hover opens it), Pricing, Data, About and the 'Launch Studio' CTA.

#### Site header
The top bar on every marketing page: the Glassnode wordmark, the Products dropdown trigger, Pricing, Data, About and the "Launch Studio" CTA. Read as `mkt-header` on the home page.

**Values (default).** size 1208 x 72; padding 20px 0px; background transparent; text Inter 14/18.2 400, #000000 `light.studio.overlay`; icon 16 x 16, #000000 `light.studio.overlay`; layers a.style-module-scss-module__NRs3BG__button.style-module-scss-module__NRs3BG__primary 120.8x33.0 rgb(26, 26, 26) T:1px solid rgb(26, 26, 26) / R:1px solid rgb(26, 26, 26) / B:1px solid rgb(26, 26, 26) / L:1px solid rgb(26, 26, 26) 2px.

Child layers that carry the look: a 120.8x33 background #1a1a1a `light.studio.background.dark` border 1px solid #1a1a1a `light.studio.background.dark` radius 2px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Glassnode wordmark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 100 x 32; background transparent; text Inter 14/21 400, #000000 `light.studio.overlay`.

![Logo default](components/crops/mkt-logo-default.png)

#### Nav dropdown trigger
The "Products" header button — aria-expanded flips and the dropdown panel mounts; a hover already opens it and a click toggles it. The opened state was measured after its own toggle. Read as `nav-dropdown-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed, opened) | size 87.06 x 18.19; padding 0px 4px; radius 2px; background transparent; text Inter 14/18.2 400, #000000 `light.studio.overlay`; transition all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1); icon 16 x 16, #000000 `light.studio.overlay` |

![Nav dropdown trigger default](components/crops/nav-dropdown-btn-default.png) ![Nav dropdown trigger focus-visible](components/crops/nav-dropdown-btn-focus-visible.png) ![Nav dropdown trigger pressed](components/crops/nav-dropdown-btn-pressed.png) ![Nav dropdown trigger opened](components/crops/nav-dropdown-btn-opened.png)

#### Dropdown item
A product entry inside the opened "Products" dropdown (Studio, Data, Research, Market Compass, Alpha Lab); measured, never followed. Read as `nav-menu-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 30.48 x 17; background transparent; text Inter 14/21 400, #000000 `light.studio.overlay` |

![Dropdown item default](components/crops/nav-menu-item-default.png)

#### Nav link
The "Pricing" header link; measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 62 x 21; background transparent; text Inter 14/21 400, #000000 `light.studio.overlay`; icon 12 x 12, #000000 `light.studio.overlay` |
| focus-visible | outline 1px auto #101010 `light.measured.border.focusRing`, offset 1px; layers a.style-module-scss-module__LPSrhq__externalNavLink 62.0x21.0 1px auto rgb(16, 16, 16) offset 1px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Header CTA
The "Launch Studio" header action pointing at studio.glassnode.com; measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 120.75 x 32.97; padding 6.4px 12px; border 1px solid #1a1a1a `light.studio.background.dark`; radius 2px; background #1a1a1a `light.studio.background.dark`; text Inter 14/18.2 400, #ffffff `light.research.bg.default`; transition all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) |
| focus-visible | outline 1px auto #101010 `light.measured.border.focusRing`, offset 1px |
| pressed | border 1px solid #333333 `light.studio.button.primary.background.active`; background #333333 `light.studio.button.primary.background.active` |

![Header CTA default](components/crops/nav-cta-default.png) ![Header CTA hover](components/crops/nav-cta-hover.png) ![Header CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Header CTA pressed](components/crops/nav-cta-pressed.png)

### Marketing home

The home hero and sections: the 'Pioneering digital asset market intelligence' masthead, the metric comparison controls and display section headings.

#### Hero headline
"Pioneering digital asset market intelligence" — the home masthead. Read as `hero-h1` on the home page.

**Values (default).** size 604 x 184.31; background transparent; text fraktion 51.2/61.44 700, #333333 `light.studio.button.primary.background.active`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Section heading
A marketing section heading further down the home page ("Our flagship platform", ...) — a display-size h2, so transient microcopy never counts. Read as `section-h2` on the home page.

**Values (default).** size 1208 x 44.8; background transparent; text Inter 32/44.8 700, #ffffff `light.research.bg.default`.

![Section heading default](components/crops/section-h2-default.png)

#### Partner report link
The "Partner Reports" promo link under the hero ("Xapo Bank + Glassnode: Generating Yield on..."); measured, never followed. Read as `partner-report-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 276 x 370; padding 16px; border 1px solid #dedfe1 `light.theme.border.default`; radius 2px; background #f7f8fa `light.studio.background.hover`; shadow rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; text Inter 12/18 700, #6f6f6f `light.studio.button.tertiary.content.default`; transition all 0.2s ease |

![Partner report link default](components/crops/partner-report-link-default.png) ![Partner report link hover](components/crops/partner-report-link-hover.png)

### Vector pricing page

/pricing/vector — the Bitcoin Vector product page: the quarterly/monthly billing select, the plan card, 'Download sample' and the FAQ accordion.

#### Vector headline
The /pricing/vector masthead over the Bitcoin Vector pitch. Read as `vec-h1` on the pricing/vector page.

**Values (default).** size 480 x 122.88; background transparent; text fraktion 51.2/61.44 700, #333333 `light.studio.button.primary.background.active`.

![Vector headline default](components/crops/vec-h1-default.png)

#### Billing-cycle select
The native <select> switching "Bill quarterly"/"Bill monthly" on the Vector price; measured at rest, never changed. Read as `vec-billing-select` on the pricing/vector page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 103 x 17; padding 0px 20px 0px 0px; background transparent; text Inter 14/normal 400, #5a5a5a `light.studio.background.disabled.on.dark` |
| focused | outline 1px auto #101010 `light.measured.border.focusRing`, offset 0px; layers select.style-module-scss-module__neBVSa__billingSelect 103.0x17.0 1px auto rgb(16, 16, 16) offset 0px |

![Billing-cycle select default](components/crops/vec-billing-select-default.png) ![Billing-cycle select focused](components/crops/vec-billing-select-focused.png)

#### Plan card
A price card on /pricing/vector — the plan name, monthly price and CTA inside a bordered card. Read as `vec-plan-card` on the pricing/vector page.

**Values (default).** size 373.66 x 185.8; padding 24px 32px; background #f7f8fa `light.studio.background.hover`; text Inter 16/24 400, #5a5a5a `light.studio.background.disabled.on.dark`.

![Plan card default](components/crops/vec-plan-card-default.png)

#### Download sample button
A "Download sample" control on the Vector page; measured, never pressed — no download was requested. Read as `vec-download-btn` on the pricing/vector page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 179.91 x 43; padding 12px 16px 12px 24px; border 1px solid #4559dc `light.research.accent`; background transparent; text Inter 14/normal 400, #4559dc `light.research.accent`; icon 16 x 16, #4559dc `light.research.accent` |
| focus-visible | outline 1px auto #101010 `light.measured.border.focusRing`, offset 0px |

![Download sample button default](components/crops/vec-download-btn-default.png) ![Download sample button hover](components/crops/vec-download-btn-hover.png) ![Download sample button focus-visible](components/crops/vec-download-btn-focus-visible.png) ![Download sample button pressed](components/crops/vec-download-btn-pressed.png)

#### FAQ accordion
A question row in the Vector FAQ ("How is the Bitcoin Vector delivered?", "Can I unsubscribe at any time?", ...); the opened state was measured after its own toggle — a local UI toggle. Read as `vec-faq` on the pricing/vector page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 822 x 82; padding 24px 0px; background transparent; text Inter 28/normal 400, #333333 `light.studio.button.primary.background.active`; icon 16 x 16, #f7f8fa `light.studio.background.hover`; layers span.style-module__vNz2sq__toggle 32.0x32.0 rgb(26, 26, 26) 100% |

Child layers that carry the look: span 32x32 background #1a1a1a `light.studio.background.dark` radius 100%.

![FAQ accordion default](components/crops/vec-faq-default.png) ![FAQ accordion opened](components/crops/vec-faq-opened.png)

### Marketing contact page

/contact — the 'How can we connect' category cards and the research subscribe band.

#### Contact headline
"How can we connect" — the /contact masthead over the category cards. Read as `contact-h1` on the contact page.

**Values (default).** size 1064 x 67.19; background transparent; text fraktion 56/67.2 700, #333333 `light.studio.button.primary.background.active`.

![Contact headline default](components/crops/contact-h1-default.png)

#### Contact category card
A contact-category card ("Contact Sales", "General Inquiries") that routes to the right form; measured, never followed. Read as `contact-category` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 384 x 193.59; padding 42px 24px; border 1px solid #dedfe1 `light.theme.border.default`; radius 2px; background #ffffff `light.research.bg.default`; shadow rgba(0, 0, 0, 0.08) 0px 8px 32px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; text Inter 24/33.6 700, #333333 `light.studio.button.primary.background.active`; transition border 0.2s ease-in-out |

![Contact category card default](components/crops/contact-category-default.png) ![Contact category card hover](components/crops/contact-category-hover.png)

#### Subscribe button (contact)
The "Send me free research" subscribe button in the contact page's research band; measured, never pressed. Read as `contact-subscribe-btn` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 184.84 x 40; padding 9.6px 16px; border 1px solid #dedfe1 `light.theme.border.default`; radius 0px 2px 2px 0px; background #dedfe1 `light.theme.border.default`; text Inter 14/18.2 400, #808080 `light.studio.border.2.on.dark`; transition all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) |
| pressed | border 1px solid #f7f8fa `light.studio.background.hover` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Subscribe button (contact) default](components/crops/contact-subscribe-btn-default.png) ![Subscribe button (contact) hover](components/crops/contact-subscribe-btn-hover.png) ![Subscribe button (contact) pressed](components/crops/contact-subscribe-btn-pressed.png)

### Studio shell (signed out)

studio.glassnode.com — the React product shell on the declared --gds-* layer: the navbar (Home/Dashboards/Charts/Market Compass/Alpha Lab/Research/Tokenization, search, 'Log in', 'Sign up'), the /pricing plan grid with its metric-catalog expanders and FAQ. Signed-out only; the declared dark-theme layer has no public control.

#### Studio navbar
The product-shell top bar on studio.glassnode.com: the wordmark, Home/Dashboards/Charts/Market Compass/Alpha Lab/Research/Tokenization nav, Resources, the search control, "Log in" and "Sign up". Read as `st-navbar` on the studio /pricing page.

**Values (default).** size 1425 x 70; background #ffffff `light.research.bg.default`; shadow #dedfe1 0px -1px 0px 0px inset; text Inter Variable 14/22.00 400, #6f6f6f `light.studio.button.tertiary.content.default`.

![Studio navbar default](components/crops/st-navbar-default.png)

#### Studio nav link
The "Charts" navbar link to /charts?a=BTC; measured, never followed. Read as `st-nav-link` on the studio /pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 43.7 x 22; background transparent; text Inter Variable 14/22.00 400, #6f6f6f `light.studio.button.tertiary.content.default`; transition color 0.3s ease |
| hover, pressed | text Inter Variable 14/22.00 400, #333333 `light.studio.button.primary.background.active` |

![Studio nav link default](components/crops/st-nav-link-default.png) ![Studio nav link hover](components/crops/st-nav-link-hover.png) ![Studio nav link focus-visible](components/crops/st-nav-link-focus-visible.png) ![Studio nav link pressed](components/crops/st-nav-link-pressed.png)

#### Log in button
The navbar "Log in" — navigates to the Auth0 universal login at auth.glassnode.com; measured, never pressed (the login form is captured on the auth-login pass). Read as `st-login-btn` on the studio /pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 50.5 x 32; padding 0px 4px; border 1px solid transparent; radius 2px; background transparent; text Inter Variable 14/22.00 400, #1a1a1a `light.studio.background.dark`; transition all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) |
| hover | text Inter Variable 14/22.00 400, #000000 `light.studio.overlay` |
| focus-visible | outline 3px solid #404040, offset 1px; transition none |

![Log in button default](components/crops/st-login-btn-default.png) ![Log in button hover](components/crops/st-login-btn-hover.png) ![Log in button focus-visible](components/crops/st-login-btn-focus-visible.png) ![Log in button pressed](components/crops/st-login-btn-pressed.png)

#### Sign up button
The navbar "Sign up" — navigates to the Auth0 signup; measured, never pressed. Read as `st-signup-btn` on the studio /pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 82.03 x 32; padding 0px 15px; border 1px solid transparent; radius 2px; background #1a1a1a `light.studio.background.dark`; shadow rgba(25, 25, 25, 0.1) 0px 2px 0px 0px; text Inter Variable 14/22.00 400, #ffffff `light.research.bg.default`; transition all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) |
| hover | background #262626 |
| focus-visible | outline 3px solid #404040, offset 1px; transition none |
| pressed | background #000000 `light.studio.overlay` |

![Sign up button default](components/crops/st-signup-btn-default.png) ![Sign up button hover](components/crops/st-signup-btn-hover.png) ![Sign up button focus-visible](components/crops/st-signup-btn-focus-visible.png) ![Sign up button pressed](components/crops/st-signup-btn-pressed.png)

#### Search trigger
The navbar search button that opens the metric/asset search; a local UI toggle — measured, never opened. Read as `st-search-btn` on the studio /pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 32 x 32; border 1px solid transparent; radius 2px; background transparent; text Inter Variable 14/22.00 400, rgba(0, 0, 0, 0.88); transition all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1); icon 16 x 16, rgba(0, 0, 0, 0.88) |
| hover | background rgba(0, 0, 0, 0.04) `core.palette.darken.4` |
| focus-visible | outline 3px solid #404040, offset 1px; transition none |

![Search trigger default](components/crops/st-search-btn-default.png) ![Search trigger hover](components/crops/st-search-btn-hover.png) ![Search trigger focus-visible](components/crops/st-search-btn-focus-visible.png) ![Search trigger pressed](components/crops/st-search-btn-pressed.png)

#### Pricing headline
"Plans & Pricing" — the studio /pricing masthead. Read as `st-h1` on the studio /pricing page.

**Values (default).** size 1377 x 48; background transparent; text Inter Variable 40/48 700, #333333 `light.studio.button.primary.background.active`.

![Pricing headline default](components/crops/st-h1-default.png)

#### Plan card
A plan card on studio /pricing — one column of the plan grid (ADVANCED/PROFESSIONAL/...): name, price, billing copy and CTA. Read as `st-plan-card` on the studio /pricing page.

**Values (default).** size 399.5 x 337.41; padding 32px; background transparent; text Inter Variable 12/18.85 500, #5a5a5a `light.studio.background.disabled.on.dark`; icon 12 x 12, #5a5a5a `light.studio.background.disabled.on.dark`; layers div.ant-select.ant-select-sm 100.0x24.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 2px; button.ant-btn.ant 335.5x40.0 rgb(255, 255, 255) T:1px solid rgb(217, 217, 217) / R:1px solid rgb(217, 217, 217) / B:1px solid rgb(217, 217, 217) / L:1px solid rgb(217, 217, 217) rgba(0, 0, 0, 0.02) 0px 2px 0px 0px 2px.

Child layers that carry the look: div 100x24 border 1px solid transparent radius 2px; button 335.5x40 background #ffffff `light.research.bg.default` border 1px solid #d9d9d9 radius 2px shadow rgba(0, 0, 0, 0.02) `core.palette.darken.2` 0px 2px 0px 0px.

![Plan card default](components/crops/st-plan-card-default.png)

#### Plan CTA
A "Sign up" call-to-action inside a plan card; measured, never pressed. Read as `st-plan-signup-btn` on the studio /pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 396.59 x 40; padding 0px 15px; border 1px solid #d9d9d9; radius 2px; background #ffffff `light.research.bg.default`; shadow rgba(0, 0, 0, 0.02) 0px 2px 0px 0px; text Inter Variable 14/22.00 400, rgba(0, 0, 0, 0.88); transition all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) |
| hover | border 1px solid #262626; text Inter Variable 14/22.00 400, #262626 |
| focus-visible | outline 3px solid #404040, offset 1px; transition none |
| pressed | border 1px solid #000000 `light.studio.overlay`; text Inter Variable 14/22.00 400, #000000 `light.studio.overlay` |

![Plan CTA default](components/crops/st-plan-signup-btn-default.png) ![Plan CTA hover](components/crops/st-plan-signup-btn-hover.png) ![Plan CTA focus-visible](components/crops/st-plan-signup-btn-focus-visible.png) ![Plan CTA pressed](components/crops/st-plan-signup-btn-pressed.png)

#### Configure button
The "Configure" control on the custom/enterprise plan card; measured, never pressed. Read as `st-configure-btn` on the studio /pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 335.5 x 40; padding 0px 15px; border 1px solid #333333 `light.studio.button.primary.background.active`; radius 2px; background #333333 `light.studio.button.primary.background.active`; shadow rgba(25, 25, 25, 0.1) 0px 2px 0px 0px; text Inter Variable 14/22.00 400, #ffffff `light.research.bg.default`; transition all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) |
| focus-visible | outline 3px solid #404040, offset 1px; transition none |

![Configure button default](components/crops/st-configure-btn-default.png) ![Configure button hover](components/crops/st-configure-btn-hover.png) ![Configure button focus-visible](components/crops/st-configure-btn-focus-visible.png) ![Configure button pressed](components/crops/st-configure-btn-pressed.png)

#### Metric catalog expander
A "Show N more metrics" expander in the public metric catalog on /pricing; the opened state was measured after its own toggle — a local UI toggle that reveals more catalog rows. Read as `st-metrics-expander` on the studio /pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 1160 x 42.84; padding 12px 0px; background #ffffff `light.research.bg.default`; text Inter Variable 12/18.85 400, #4559dc `light.research.accent` |

![Metric catalog expander default](components/crops/st-metrics-expander-default.png) ![Metric catalog expander opened](components/crops/st-metrics-expander-opened.png)

#### FAQ accordion
A question row in the studio pricing FAQ ("How many assets does Glassnode...", "Is API access included...", ...); the opened state was measured after its own toggle — a local UI toggle. Read as `st-faq` on the studio /pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 510 x 54.39; padding 16px 0px; background transparent; text Inter Variable 16/22.4 500, #333333 `light.studio.button.primary.background.active`; icon 20 x 20, #4559dc `light.research.accent` |
| opened | icon 28.28 x 28.28, #4559dc `light.research.accent` |

![FAQ accordion default](components/crops/st-faq-default.png) ![FAQ accordion opened](components/crops/st-faq-opened.png)

### Auth0 universal login

auth.glassnode.com/u/login — the Auth0 card the studio 'Log in' navigates to (username/password, 'Continue', 'Continue with Google', 'Reset password', 'Sign up'). Reached through the real button; the volatile ?state= is never recorded; the form was never submitted.

#### Auth0 origin reached
Marker: the studio shell's "Log in" was followed to auth.glassnode.com/u/login. Only the sanitized origin+path is recorded — the volatile ?state= parameter is never preserved. Read as `__auth` on the auth login page.


#### Login card
The Auth0 universal-login card on auth.glassnode.com/u/login — the username/password form, "Continue", "Continue with Google", "Reset password" and "Sign up". Reached through the studio shell's real "Log in" button; the volatile ?state= parameter is never recorded. Read as `auth-card` on the auth login page.

**Values (default).** size 320 x 210; background transparent; text ulp-font 16/16 400, #65676e; layers div.c50d1bce1.c0d0ae1c1 320.0x52.0 rgb(255, 255, 255); label.cea96adc7.cd251e14b 121.1x18.0 rgb(255, 255, 255); input.input.cac2a821f 320.0x52.0 rgb(255, 255, 255) T:1px solid rgb(201, 202, 206) / R:1px solid rgb(201, 202, 206) / B:1px solid rgb(201, 202, 206) / L:1px solid rgb(201, 202, 206); div.c50d1bce1.c0d0ae1c1 320.0x54.0 rgb(255, 255, 255) T:1px solid rgb(201, 202, 206) / R:1px solid rgb(20.

Child layers that carry the look: div 320x52 background #ffffff `light.research.bg.default`; label 121.1x18 background #ffffff `light.research.bg.default`; input 320x52 background #ffffff `light.research.bg.default` border 1px solid #c9cace.

![Login card default](components/crops/auth-card-default.png)

#### Username field
The e-mail/username input on the Auth0 card; focused and typed into then cleared — never submitted. Read as `auth-email` on the auth login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 52; padding 0px 16px; border 1px solid #c9cace; background #ffffff `light.research.bg.default`; text ulp-font 16/17.6 400, #000000 `light.studio.overlay`; transition box-shadow 0.15s ease-in-out, border-color 0.15s ease-in-out; placeholder #000000 `light.studio.overlay` |
| focused, filled | border 1px solid #635dff; shadow #635dff 0px 0px 0px 1px |

![Username field default](components/crops/auth-email-default.png) ![Username field focused](components/crops/auth-email-focused.png) ![Username field filled](components/crops/auth-email-filled.png)

#### Password field
The password input on the Auth0 card; focused only — nothing was typed or submitted. Read as `auth-password` on the auth login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 274 x 52; padding 0px 16px; background #ffffff `light.research.bg.default`; text ulp-font 16/17.6 400, #000000 `light.studio.overlay`; transition box-shadow 0.15s ease-in-out, border-color 0.15s ease-in-out; placeholder #000000 `light.studio.overlay` |

![Password field default](components/crops/auth-password-default.png) ![Password field focused](components/crops/auth-password-focused.png)

#### Continue button
The login form's "Continue" submit; its states were measured but the button was never clicked — no credentials were entered and nothing was submitted. Read as `auth-continue` on the auth login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 52; padding 4px 16px; radius 2px; background #000000 `light.studio.overlay`; text ulp-font 16/16 400, #ffffff `light.research.bg.default`; transition background-color 0.25s ease-in-out, box-shadow 0.25s ease-in-out |
| hover | shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 150px inset |
| focus-visible | outline 2px solid #635dff, offset 2px |
| pressed | shadow #c9cfda 0px 0px 2px 0px |

![Continue button default](components/crops/auth-continue-default.png) ![Continue button hover](components/crops/auth-continue-hover.png) ![Continue button focus-visible](components/crops/auth-continue-focus-visible.png) ![Continue button pressed](components/crops/auth-continue-pressed.png)

#### Google SSO button
The "Continue with Google" social-login submit; measured, never pressed. Read as `auth-google` on the auth login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 52; padding 0px 16px; border 1px solid #c9cace; radius 2px; background #ffffff `light.research.bg.default`; text ulp-font 16/16 400, #1e212a; transition box-shadow 0.15s ease-in-out, background-color 0.15s ease-in-out |
| hover | shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 150px inset |
| focus-visible | outline 2px solid #635dff, offset 2px |
| pressed | shadow rgba(99, 93, 255, 0.15) 0px 0px 0px 150px inset |

![Google SSO button default](components/crops/auth-google-default.png) ![Google SSO button hover](components/crops/auth-google-hover.png) ![Google SSO button focus-visible](components/crops/auth-google-focus-visible.png) ![Google SSO button pressed](components/crops/auth-google-pressed.png)

#### Reset password link
The "Reset password" link to the Auth0 password-reset start; measured, never followed. Read as `auth-reset` on the auth login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 115.38 x 24; padding 4px; radius 3px; background transparent; text ulp-font 14/21 700, #635dff |
| focus-visible | outline 2px solid #635dff, offset -1px; layers a.c6017cfca.cdfbf1f1b 115.4x24.0 2px solid rgb(99, 93, 255) offset -1px 3px |

![Reset password link default](components/crops/auth-reset-default.png) ![Reset password link hover](components/crops/auth-reset-hover.png) ![Reset password link focus-visible](components/crops/auth-reset-focus-visible.png) ![Reset password link pressed](components/crops/auth-reset-pressed.png)

#### Sign up link
The "Sign up" link beside the login form; measured, never followed. Read as `auth-signup-link` on the auth login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 59.33 x 24; padding 4px; radius 3px; background transparent; text ulp-font 14/21 700, #635dff |
| focus-visible | outline 2px solid #635dff, offset -1px; layers a.c6017cfca.cd3cfae4f 59.3x24.0 2px solid rgb(99, 93, 255) offset -1px 3px |

![Sign up link default](components/crops/auth-signup-link-default.png) ![Sign up link hover](components/crops/auth-signup-link-hover.png) ![Sign up link focus-visible](components/crops/auth-signup-link-focus-visible.png) ![Sign up link pressed](components/crops/auth-signup-link-pressed.png)

### Research publication (Ghost)

research.glassnode.com — the Ghost publication: the tag nav, the 'Switch to dark mode' toggle (measured at rest), article cards, the subscribe field and a published article's prose.

#### Site header
The Ghost publication header: the Glassnode apps menu, the tag nav (Week On-chain, Strategy Watch, Market Pulse, Partner Reports, Product & Research), search and the theme toggle. Read as `res-header` on the research page.

**Values (default).** size 1425 x 65; padding 0px 36px; border B: 1px solid #e6e7e9 `light.research.line.default`; background transparent; text Inter 15/20 500, #5f636b `light.research.text.2`; icon 16 x 16, #5f636b `light.research.text.2`; layers ::before rgba(255, 255, 255, 0.86) 0px none 1; header.gh-head.outer 1425.0x65.0 B:1px solid rgb(230, 231, 233); header::before.gh-head.outer 1425pxx64px rgba(255, 255, 255, 0.86); div.gh-apps__menu 0.0x0.0 rgb(255, 255, 255) T:1px solid rgb(230, 231, 233) / R:1px solid rgb(230, 231, 233) / B:1px solid rgb(230, 231, 233) / L:1px solid rgb(230, 231, 233) rgba(0, 0, 0, 0.1) 0px 8px 24px -12px; button.

Child layers that carry the look: header 1425x65 border 1px solid #e6e7e9 `light.research.line.default`; header::before 1425pxx64px background rgba(255, 255, 255, 0.86) `light.research.glass.default`; div 0x0 background #ffffff `light.research.bg.default` border 1px solid #e6e7e9 `light.research.line.default` shadow rgba(0, 0, 0, 0.1) `light.studio.tag.danger.border` 0px 8px 24px -12px.

![Site header default](components/crops/res-header-default.png)

#### Nav link
The "Week On-chain" tag link in the header nav; measured, never followed. Read as `res-nav-link` on the research page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 134.36 x 32; padding 6px 12px; background transparent; text Inter 15/20 500, #5f636b `light.research.text.2` |
| hover | text Inter 15/20 500, #08090a `light.research.btn.bg` |
| focus-visible | outline 1px auto #101010 `light.measured.border.focusRing`, offset 1px; layers a 134.4x32.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Inter 15/20 500, #08090a `light.research.btn.bg` |

![Nav link default](components/crops/res-nav-link-default.png) ![Nav link hover](components/crops/res-nav-link-hover.png) ![Nav link focus-visible](components/crops/res-nav-link-focus-visible.png) ![Nav link pressed](components/crops/res-nav-link-pressed.png)

#### Theme toggle
The "Switch to dark mode" Ghost theme toggle — a local UI control that removes data-theme="light" and repaints the page; measured at rest, never switched here (the dark surface is captured in the screenshots pass). Read as `res-theme-toggle` on the research page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; background transparent; text Inter 16/25.6 400, #5f636b `light.research.text.2`; transition color 0.12s ease, background-color 0.12s ease; icon 16 x 16, #5f636b `light.research.text.2` |
| focus-visible | outline 1px auto #101010 `light.measured.border.focusRing`, offset 0px; layers button.gh-theme-toggle 32.0x32.0 1px auto rgb(16, 16, 16) offset 0px |
| pressed | background rgba(0, 0, 0, 0.06) `light.research.hover.2`; text Inter 16/25.6 400, #08090a `light.research.btn.bg`; icon 16 x 16, #08090a `light.research.btn.bg` |

![Theme toggle default](components/crops/res-theme-toggle-default.png) ![Theme toggle focus-visible](components/crops/res-theme-toggle-focus-visible.png) ![Theme toggle pressed](components/crops/res-theme-toggle-pressed.png)

#### Article card
An article card in the research index (the current Week On-chain issue); measured, never followed. Read as `res-post-card` on the research page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1280 x 407.45; background transparent; text Inter 14/18.2 400, #5f636b `light.research.text.2`; icon 13 x 13, #8a8f98 `light.research.text.3`; layers a.post-card-image-link 739.2x407.5 rgb(247, 247, 248) T:1px solid rgb(236, 236, 238) / R:1px solid rgb(236, 236, 238) / B:1px solid rgb(236, 236, 238) / L:1px solid rgb(236, 236, 238) 8px; span::before.post-card-meta-length 2pxx2px rgb(138, 143, 152) 50% |

Child layers that carry the look: a 739.2x407.5 background #f7f7f8 `light.research.surface` border 1px solid #ececee `light.research.line.soft` radius 8px; span::before 2pxx2px background #8a8f98 `light.research.text.3` radius 50%.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Subscribe field
The "Email" subscribe input on the research site; focused and typed into then cleared — never subscribed. Read as `res-subscribe-field` on the research page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 334 x 40; padding 8px 16px; border 1px solid #d2d4d8 `light.research.line.strong`; background #f4f4f5 `light.research.input`; text Inter 15/normal 400, #08090a `light.research.btn.bg`; placeholder #8a8f98 `light.research.text.3` |
| focused, filled | border 1px solid #a9adb5 `light.research.focus` |

![Subscribe field default](components/crops/res-subscribe-field-default.png) ![Subscribe field focused](components/crops/res-subscribe-field-focused.png) ![Subscribe field filled](components/crops/res-subscribe-field-filled.png)

#### Footer
The research footer: the subscribe band, the sitemap columns and the legal links. Read as `res-footer` on the research page.

**Values (default).** size 492.8 x 24; background transparent; text Inter 15/24 400, #8a8f98 `light.research.text.3`; layers span::before.post-card-meta-length 2pxx2px rgb(138, 143, 152) 50%.

Child layers that carry the look: span::before 2pxx2px background #8a8f98 `light.research.text.3` radius 50%.

![Footer default](components/crops/res-footer-default.png)

#### Article headline
The published-article masthead on research.glassnode.com (the current Week On-chain issue); the article URL is recorded on the component. Read as `res-article-h1` on the research article page.

**Values (default).** size 840 x 65.72; background transparent; text Inter 62/65.72 500, #08090a `light.research.btn.bg`.

![Article headline default](components/crops/res-article-h1-default.png)

#### Article body text
A paragraph in the article body — the Ghost theme's serif/sans reading measure. Read as `res-article-p` on the research article page.

**Values (default).** size 640 x 150; background transparent; text Inter 20/30 400, #5f636b `light.research.text.2`.

![Article body text default](components/crops/res-article-p-default.png)

#### Article tag
A tag link on the article; measured, never followed. Read as `res-article-tag` on the research article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 0 x 0; padding 10px 12px; background transparent; text Inter 16/24 500, #08090a `light.research.btn.bg` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Docs site (GitBook)

docs.glassnode.com — the GitBook docs site (the platform's own token layer): the header, Website/Studio/Insights links, the 'Switch to dark theme' button (never switched here), search, sidebar links and the metric catalog.

#### Docs header
The GitBook docs header: "Glassnode Docs", the search field, the Website/Studio/Insights/Twitter links, "More" and the light/system/dark theme buttons. Read as `docs-header` on the docs landing page.

**Values (default).** size 1425 x 64; background oklab(0.999994 0.0000455678 0.0000200868 / 0.88); shadow oklab(0.230743 0.0000105128 0.00000463426 / 0.08) 0px 1px 0px 0px; text Roboto 18/22.5 600, #ffffff `light.research.bg.default`.

![Docs header default](components/crops/docs-header-default.png)

#### Docs nav link
The "Studio" header link out to studio.glassnode.com; measured, never followed. Read as `docs-nav-link` on the docs landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 39.91 x 20; background transparent; text Roboto 14/20 400, #ffffff `light.research.bg.default` |
| hover | text Roboto 14/20 400, oklab(0.999994 0.0000455678 0.0000200868 / 0.64) |
| focus-visible | outline 2px solid #cbd8fd, offset 1px; layers a.flex.items-center 39.9x20.0 2px solid rgb(203, 216, 253) offset 1px |
| pressed | text Roboto 14/20 400, oklab(0.999994 0.0000455678 0.0000200868 / 0.64) |

![Docs nav link default](components/crops/docs-nav-link-default.png) ![Docs nav link hover](components/crops/docs-nav-link-hover.png) ![Docs nav link focus-visible](components/crops/docs-nav-link-focus-visible.png) ![Docs nav link pressed](components/crops/docs-nav-link-pressed.png)

#### Theme button
The GitBook "Switch to dark theme" button — a local UI control that flips .light/.dark on <html>; measured at rest, never switched here (the dark surface is captured in the screenshots pass). Read as `docs-theme-btn` on the docs landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 33 x 33; padding 6px; radius 12px; background transparent; text Roboto 14/21 400, #6e6e6e; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, #6e6e6e; layers button.button.group/button 33.0x33.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 12px |
| focus-visible | background #f2f2f2; outline 2px solid #cbd8fd, offset 0px; text Roboto 14/21 400, #1d1d1d; icon 14 x 14, #1d1d1d; layers none |
| pressed | background #f2f2f2; text Roboto 14/21 400, #1d1d1d; icon 14 x 14, #1d1d1d; layers none |

![Theme button default](components/crops/docs-theme-btn-default.png) ![Theme button hover](components/crops/docs-theme-btn-hover.png) ![Theme button focus-visible](components/crops/docs-theme-btn-focus-visible.png) ![Theme button pressed](components/crops/docs-theme-btn-pressed.png)

#### Search field
The docs "Search" field — focused only; typing was not needed to read the focus ring. Read as `docs-search` on the docs landing page.

**Values (default).** size 121.44 x 37; padding 8px; background transparent; text Roboto 14/21 400, #ffffff `light.research.bg.default`; placeholder oklab(0.999994 0.0000455678 0.0000200868 / 0.72).

![Search field default](components/crops/docs-search-default.png)

#### Doc page headline
"Overview" — the docs landing headline on the GitBook stack. Read as `docs-h1` on the docs landing page.

**Values (default).** size 753 x 45; background transparent; text Roboto 36/45 700, #1d1d1d.

![Doc page headline default](components/crops/docs-h1-default.png)

#### Sidebar link
A sidebar navigation link in the docs tree; measured, never followed. Read as `docs-side-link` on the docs landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 282 x 32; padding 6px 6px 6px 12px; radius 6px; background transparent; text Roboto 14/20 400, oklab(0.230743 0.0000105128 0.00000463426 / 0.64); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | background #f2f2f2; text Roboto 14/20 400, #1d1d1d |

![Sidebar link default](components/crops/docs-side-link-default.png) ![Sidebar link hover](components/crops/docs-side-link-hover.png)

#### Request a quote link
The "Request a quote" banner link on the overview page; measured, never followed. Read as `docs-quote-btn` on the docs landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1361 x 44; padding 12px 48px 12px 16px; radius 6px; background #f7f7f7; shadow #e5e5e5 0px 0px 0px 1px inset; text Roboto 14/20 400, #1d1d1d; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #787878 |
| hover | background #f5f5f5 |
| focus-visible | outline 2px solid #cbd8fd, offset 1px |
| pressed | background #ededed |

![Request a quote link default](components/crops/docs-quote-btn-default.png) ![Request a quote link hover](components/crops/docs-quote-btn-hover.png) ![Request a quote link focus-visible](components/crops/docs-quote-btn-focus-visible.png) ![Request a quote link pressed](components/crops/docs-quote-btn-pressed.png)

#### Metric catalog headline
"Metric Catalog" — the API metric index page on the docs site. Read as `docs-metric-h1` on the docs metric catalog page.

**Values (default).** size 753 x 45; background transparent; text Roboto 36/45 700, #1d1d1d.

![Metric catalog headline default](components/crops/docs-metric-h1-default.png)

#### Metric category link
A metric-category link in the catalog; measured, never followed. Read as `docs-metric-link` on the docs metric catalog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85.61 x 16; background transparent; text Roboto 14/21 400, #6888fb `light.studio.focus`; transition all 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, #6888fb `light.studio.focus` |
| hover | text Roboto 14/21 400, #1a1d25; icon 12 x 12, #1a1d25 |

![Metric category link default](components/crops/docs-metric-link-default.png) ![Metric category link hover](components/crops/docs-metric-link-hover.png)

#### Code or metric label
A code/metric label on the catalog page — the GitBook monospace treatment. Read as `docs-code` on the docs metric catalog page.

Not on the page when it was captured.

### Tokenization registry

tokenization.glassnode.com — the dark-by-default registry app: the nav with live asset/issuer/product/derivative counts, search, the 'Switch to light theme' button and 'Request access'.

#### Registry nav
The registry navigation on tokenization.glassnode.com: the Glassnode apps menu, search, the theme button and the Overview/Assets/Issuers/Products/Derivatives items with their live counts. Read as `tok-shell` on the tokenization registry page.

**Values (default).** size 220 x 852; padding 12px 8px 0px 8px; border R: 1px solid #2a2a2a; background #141414; text inter 11.5/16.67 500, #8a8a87; transition width 0.15s ease; icon 16 x 16, #16cc8c `core.palette.accent`.

![Registry nav default](components/crops/tok-shell-default.png)

#### Nav item
The "Assets" nav item with its live asset count (3,727 at capture); measured, never followed. Read as `tok-nav-item` on the tokenization registry page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 203 x 30; padding 0px 10px; radius 6px; background transparent; text inter 13/18.85 500, #b8b8b5; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #8a8a87 |
| hover | background #232323; text inter 13/18.85 500, #e8e8e6 |
| focus-visible | outline 2px solid #16cc8c `core.palette.accent`, offset 2px; layers a.rail-item.relative 203.0x30.0 2px solid rgb(22, 204, 140) offset 2px 6px |
| pressed | background #232323; text inter 13/18.85 500, #e8e8e6 |

![Nav item default](components/crops/tok-nav-item-default.png) ![Nav item hover](components/crops/tok-nav-item-hover.png) ![Nav item focus-visible](components/crops/tok-nav-item-focus-visible.png) ![Nav item pressed](components/crops/tok-nav-item-pressed.png)

#### Search control
The "Search assets, issuers, products..." search control; a local UI toggle — measured, never opened. Read as `tok-search-btn` on the tokenization registry page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 560 x 32; padding 0px 6px 0px 10px; border 1px solid #2a2a2a; radius 6px; background #262626; text inter 13/18.85 400, #8a8a87; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 15 x 15, #8a8a87 |
| hover | border 1px solid #363636; background #1c1c1c |
| focus-visible | outline 2px solid #16cc8c `core.palette.accent`, offset 2px |
| pressed | border 1px solid #363636; background #1c1c1c |

![Search control default](components/crops/tok-search-btn-default.png) ![Search control hover](components/crops/tok-search-btn-hover.png) ![Search control focus-visible](components/crops/tok-search-btn-focus-visible.png) ![Search control pressed](components/crops/tok-search-btn-pressed.png)

#### Theme button
The "Switch to light theme" control — flips [data-theme] on <html>; measured at rest on the painted dark surface, never switched here (the light surface is captured in the screenshots pass). Read as `tok-theme-btn` on the tokenization registry page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 28 x 28; radius 6px; background transparent; text inter 13/18.85 400, #8a8a87; transition background 0.12s ease, color 0.12s ease; icon 15 x 15, #8a8a87 |
| hover | background #232323; text inter 13/18.85 400, #e8e8e6; icon 15 x 15, #e8e8e6 |
| focus-visible | outline 2px solid #16cc8c `core.palette.accent`, offset 2px; layers button.ib 28.0x28.0 2px solid rgb(22, 204, 140) offset 2px 6px |
| pressed | background #232323; text inter 13/18.85 400, #e8e8e6; icon 15 x 15, #e8e8e6 |

![Theme button default](components/crops/tok-theme-btn-default.png) ![Theme button hover](components/crops/tok-theme-btn-hover.png) ![Theme button focus-visible](components/crops/tok-theme-btn-focus-visible.png) ![Theme button pressed](components/crops/tok-theme-btn-pressed.png)

#### Request access link
The "Request access" nav action to /api-access; measured, never followed. Read as `tok-request-btn` on the tokenization registry page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 203 x 30; padding 0px 10px; radius 6px; background transparent; text inter 13/18.85 500, #b8b8b5; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #8a8a87 |
| hover | background #232323; text inter 13/18.85 500, #e8e8e6 |
| focus-visible | outline 2px solid #16cc8c `core.palette.accent`, offset 2px; layers a.rail-item.relative 203.0x30.0 2px solid rgb(22, 204, 140) offset 2px 6px |
| pressed | background #232323; text inter 13/18.85 500, #e8e8e6 |

![Request access link default](components/crops/tok-request-btn-default.png) ![Request access link hover](components/crops/tok-request-btn-hover.png) ![Request access link focus-visible](components/crops/tok-request-btn-focus-visible.png) ![Request access link pressed](components/crops/tok-request-btn-pressed.png)

#### Registry stat
A live registry count (assets/issuers/products/derivatives) in the nav or hero — the dark theme's numeric treatment. Read as `tok-stat` on the tokenization registry page.

**Values (default).** size 203 x 30; padding 0px 10px; radius 6px; background transparent; text inter 13/18.85 500, #b8b8b5; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #8a8a87.

![Registry stat default](components/crops/tok-stat-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the header with the hamburger, the nav overlay, the hero and the newsletter field.

#### Mobile top bar
The phone header at 390 wide: the wordmark and the hamburger. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 342 x 70; padding 24px 0px; background transparent; text Inter 14/21 400, #000000 `light.studio.overlay`.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile menu button
The hamburger button — a local UI toggle; the opened state was measured after activating it. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 28 x 22; padding 1px 6px; background transparent; text Inter 13.33/normal 400, #000000 `light.studio.overlay` |
| focus-visible | outline 1px auto #e59700, offset 0px; layers button.style-module-scss-module__oFHV5W__hamburger 28.0x22.0 1px auto rgb(229, 151, 0) offset 0px |

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png) ![Mobile menu button opened](components/crops/m-menu-btn-opened.png)

#### Mobile nav overlay
The navigation overlay opened by the hamburger (the same destinations as the desktop header); its links were never followed. Read as `m-drawer` on the home page at 390 wide.

**Values (default).** size 290 x 844; padding 0px 32px; background #1a1a1a `light.studio.background.dark`; text Inter 13.33/normal 400, #dedfe1 `light.theme.border.default`; icon 16 x 16, #dedfe1 `light.theme.border.default`.

![Mobile nav overlay default](components/crops/m-drawer-default.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 342 x 144; background transparent; text fraktion 40/48 700, #333333 `light.studio.button.primary.background.active`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile newsletter field
The "Enter your email" subscribe input at 390 wide; focused and typed into then cleared — never subscribed. Read as `m-newsletter-field` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 342 x 40; padding 0px 16px; border 1px solid #808080 `light.studio.border.2.on.dark`; radius 2px 0px 0px 2px; background transparent; text Inter 14/normal 400, #a0a0a0 `light.studio.content.tertiary.on.dark`; placeholder #757575 `light.measured.form.placeholder` |
| focused, filled | outline 1px auto #e59700, offset 0px |

![Mobile newsletter field default](components/crops/m-newsletter-field-default.png) ![Mobile newsletter field focused](components/crops/m-newsletter-field-focused.png) ![Mobile newsletter field filled](components/crops/m-newsletter-field-filled.png)

### Footer

The marketing page footer: sitemap columns, the 'Enter your email' subscribe field with 'Send me free research', and the 'Privacy settings' consent control.

#### Footer
The page footer: the research subscribe field, the Use cases/Resources/About us/Legal columns and the Privacy settings control. Read as `footer` on the home page.

**Values (default).** size 1425 x 334.39; padding 64px 72px 24px 72px; background #1a1a1a `light.studio.background.dark`; text Inter 16/22.4 700, #f7f8fa `light.studio.background.hover`; icon 24 x 24, #000000 `light.studio.overlay`.

![Footer default](components/crops/footer-default.png)

#### Newsletter field
The "Enter your email" subscribe input; focused and typed into then cleared — never subscribed. Read as `newsletter-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 336 x 40; padding 0px 16px; border 1px solid #808080 `light.studio.border.2.on.dark`; radius 2px 0px 0px 2px; background transparent; text Inter 14/normal 400, #a0a0a0 `light.studio.content.tertiary.on.dark`; placeholder #757575 `light.measured.form.placeholder` |
| focused, filled | outline 1px auto #101010 `light.measured.border.focusRing`, offset 0px |

![Newsletter field default](components/crops/newsletter-field-default.png) ![Newsletter field focused](components/crops/newsletter-field-focused.png) ![Newsletter field filled](components/crops/newsletter-field-filled.png)

#### Subscribe button
The "Send me free research" subscribe button; its states were measured but the button was never clicked — nothing was submitted. Read as `newsletter-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 184.84 x 40; padding 9.6px 16px; border 1px solid #dedfe1 `light.theme.border.default`; radius 0px 2px 2px 0px; background #dedfe1 `light.theme.border.default`; text Inter 14/18.2 400, #808080 `light.studio.border.2.on.dark`; transition all 0.2s cubic-bezier(0.645, 0.045, 0.355, 1) |
| pressed | size 151.58 x 21; padding 1px 6px; border 2px outset rgba(118, 118, 118, 0.3); radius none; background rgba(239, 239, 239, 0.3); text Arial 13.33/normal 400, rgba(16, 16, 16, 0.3); transition none |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Subscribe button default](components/crops/newsletter-btn-default.png) ![Subscribe button hover](components/crops/newsletter-btn-hover.png) ![Subscribe button pressed](components/crops/newsletter-btn-pressed.png)

#### Privacy settings control
The "Privacy settings" footer control that opens the consent manager; a local UI toggle — measured, never opened. Read as `privacy-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 105.28 x 17; background transparent; text Inter 14/normal 400, #dedfe1 `light.theme.border.default` |
| focus-visible | outline 1px auto #101010 `light.measured.border.focusRing`, offset 0px; layers button 105.3x17.0 1px auto rgb(16, 16, 16) offset 0px |

![Privacy settings control default](components/crops/privacy-btn-default.png) ![Privacy settings control hover](components/crops/privacy-btn-hover.png) ![Privacy settings control focus-visible](components/crops/privacy-btn-focus-visible.png) ![Privacy settings control pressed](components/crops/privacy-btn-pressed.png)

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 85.34 x 17; background transparent; text Inter 14/14 400, #dedfe1 `light.theme.border.default`; transition all 0.2s ease-in-out |
| focus-visible | outline 1px auto #101010 `light.measured.border.focusRing`, offset 1px; layers a 85.3x17.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Inter 14/14 400, #f7f8fa `light.studio.background.hover` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Glassnode mark, the nav glyphs, social glyphs and partner logos) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Glassnode's product is Studio: the charting workbench, saved dashboards, the metric workbench editor, alerts, API keys and billing all sit after 'Log in' on auth.glassnode.com and were never reached. The Auth0 login card is the only account surface a signed-out visitor sees, and it was measured as a form, never submitted. studio.glassnode.com /login, /sign-up and /signup are in-app Page Not Found routes — the only real login is the Auth0 page the navbar hands to.

### Pages

- **The account.** Studio's workbench, saved dashboards, alerts, API keys, billing and every post-login surface were never reached; the Auth0 card was measured as a form and never submitted.
- **Forms.** The newsletter fields and the Auth0 username field were typed into then cleared — nothing was sent; what a submission returns is unverified.
- **Studio charts and dashboards** are captured as screenshots of their public signed-out views (/charts and /dashboards redirect to public BTC/asset views); deeper interactions (metric picker, time ranges) sit behind the account wall.
- **The Market Compass page** on studio.glassnode.com is an upgrade gate signed out — its content was captured as shown to an anonymous visitor.
- **Research articles** are exemplar-level: the index and the current first article were captured; sibling articles share the templates, unmeasured.
- **Marketing product pages, solutions, events and customer stories** were captured as index/landing pages; subpages were not.


### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **The studio dark theme** is declared (html[data-theme="dark-theme"] with --gds-*/--ant-* redeclarations) but no public control reaches it signed out — it is captured as declared-not-painted tokens, never as a screenshot or measured state.
- **Theme toggles** (research, docs, tokenization) were measured at rest; the switched surfaces are screenshot evidence, not measured component states.


### Themes

The marketing site paints the `:root` light layer only — dark in-page sections, no global theme or control. The studio shell paints light signed out and declares a `html[data-theme="dark-theme"]` layer no public control reaches (declared-not-painted tokens). research.glassnode.com and docs.glassnode.com each carry a real theme control whose dark surfaces are the `theme-dark` screenshots and the dark.research.* token roles; tokenization.glassnode.com paints dark by default and light via its button (`theme-light` screenshot, light.tokenization.* roles).

### Fonts

- **Inter/Inter Variable** carries the studio shell, the research body and the registry; **fraktion** is the marketing display face (the marketing --font-family var is a system stack — the webfonts paint per-module); **JetBrains Mono** is the registry mono; **Roboto/IBM Plex Mono** are the GitBook docs fonts — all self-hosted. The style guide falls back to system fonts.

### Screenshots

- The product imagery, partner logos and photography in the screenshots are the product's published content; the Auth0 login shot's landing URL is sanitized (the volatile ?state= is never kept).
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, plan prices, report text, issuer/asset names and customer names are the product's content; only frames and components were measured.
