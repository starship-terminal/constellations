# Gladia components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. First read from gladia.io on 2026-11-16, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Later recaptures merge into the same file, so every entry names the date its own states were read; a state a re-read missed keeps its earlier date and says so. Nothing was signed into, bought or submitted; the demo-request, calculator, login and signup forms were never sent; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (58 components, 132 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/20.8 400, #000000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (118 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture: `dark` for every www.gladia.io marketing page — the site's :root paints dark and carries no theme control — except `library`, the one page on the light `body.light-mode` scope, and `blog`, the legacy Webflow stack; both paint `light`. The Mintlify docs pages carry a real theme preference — `docs-*-light-theme-dark.png` shots are the docs' own dark surface reached by the 'Change theme preference' toggle. app.gladia.io / and /signup paint `dark`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages bounded at eight chunks with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x) for default shots and 390 wide for stitched `-full` tiles.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [menu-company](screenshots/home-dark-menu-company.png), [menu-developers](screenshots/home-dark-menu-developers.png), [menu-product](screenshots/home-dark-menu-product.png), [menu-resources](screenshots/home-dark-menu-resources.png), [menu-solutions](screenshots/home-dark-menu-solutions.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-dark-default.png), [full](screenshots/pricing-dark-full.png), [toggle-realtime](screenshots/pricing-dark-toggle-realtime.png) |
| Speech-to-Text API | `/product/speech-to-text-api` | [default](screenshots/product-stt-dark-default.png), [full](screenshots/product-stt-dark-full.png) |
| Real-time STT | `/product/speech-to-text-api/real-time` | [default](screenshots/product-realtime-dark-default.png), [full](screenshots/product-realtime-dark-full.png) |
| Async STT | `/product/speech-to-text-api/async` | [default](screenshots/product-async-dark-default.png), [full](screenshots/product-async-dark-full.png) |
| Audio intelligence | `/product/audio-intelligence` | [default](screenshots/product-audio-intel-dark-default.png), [full](screenshots/product-audio-intel-dark-full.png) |
| Use case: voice agents | `/use-cases/voice-agents` | [default](screenshots/use-case-voice-agents-dark-default.png), [full](screenshots/use-case-voice-agents-dark-full.png) |
| Use case: meeting assistants | `/use-cases/meeting-assistants` | [default](screenshots/use-case-meeting-dark-default.png), [full](screenshots/use-case-meeting-dark-full.png) |
| Use case: CCaaS | `/use-cases/ccaas` | [default](screenshots/use-case-ccaas-dark-default.png), [full](screenshots/use-case-ccaas-dark-full.png) |
| Use case: media | `/use-cases/media` | [default](screenshots/use-case-media-dark-default.png), [full](screenshots/use-case-media-dark-full.png) |
| About us | `/about-us` | [default](screenshots/about-us-dark-default.png), [full](screenshots/about-us-dark-full.png) |
| Blog (Webflow) | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Changelog | `/changelog` | [default](screenshots/changelog-dark-default.png), [full](screenshots/changelog-dark-full.png) |
| Testimonials | `/testimonials` | [default](screenshots/testimonials-dark-default.png), [full](screenshots/testimonials-dark-full.png) |
| Partners | `/partners` | [default](screenshots/partners-dark-default.png), [full](screenshots/partners-dark-full.png) |
| Library (light scope) | `/library` | [default](screenshots/library-light-default.png), [full](screenshots/library-light-full.png) |
| Demo request | `/demo-request` | [default](screenshots/demo-request-dark-default.png), [full](screenshots/demo-request-dark-full.png) |
| Security | `/security` | [default](screenshots/security-dark-default.png), [full](screenshots/security-dark-full.png) |
| Compliance hub | `/compliance-hub` | [default](screenshots/compliance-hub-dark-default.png), [full](screenshots/compliance-hub-dark-full.png) |
| GladiaFlow | `/gladiaflow` | [default](screenshots/gladiaflow-dark-default.png), [full](screenshots/gladiaflow-dark-full.png) |
| Solaria-3 | `/solaria-3` | [default](screenshots/solaria-3-dark-default.png), [full](screenshots/solaria-3-dark-full.png) |
| Creator program | `/creator-program` | [default](screenshots/creator-program-dark-default.png), [full](screenshots/creator-program-dark-full.png) |
| Start-up studio | `/start-up-studio` | [default](screenshots/start-up-studio-dark-default.png), [full](screenshots/start-up-studio-dark-full.png) |
| Meeting-assistant market map | `/meeting-assistant-market-map` | [default](screenshots/market-map-light-default.png), [full](screenshots/market-map-light-full.png) |
| Benchmark reliability checker | `/benchmark-reliability-checker` | [default](screenshots/benchmark-checker-dark-default.png), [full](screenshots/benchmark-checker-dark-full.png) |
| Competitor benchmarks | `/competitors/benchmarks` | [default](screenshots/competitors-benchmarks-dark-default.png), [full](screenshots/competitors-benchmarks-dark-full.png) |
| Docs: introduction (Mintlify) | `docs.gladia.io/chapters/introduction` | [default](screenshots/docs-home-light-default.png), [full](screenshots/docs-home-light-full.png), [theme-dark](screenshots/docs-home-light-theme-dark.png), [dark 2026-11-21](screenshots/docs-home-dark-theme.png) |
| Docs: quickstart | `docs.gladia.io/chapters/pre-recorded-stt/quickstart` | [default](screenshots/docs-quickstart-light-default.png), [full](screenshots/docs-quickstart-light-full.png), [theme-dark](screenshots/docs-quickstart-light-theme-dark.png) |
| Docs: API reference | `docs.gladia.io/api-reference` | [default](screenshots/docs-api-light-default.png), [full](screenshots/docs-api-light-full.png) |
| Sign in (app shell) | `app.gladia.io/signin` | [default](screenshots/login-dark-default.png) (empty, 2026-11-21), [forgot](screenshots/login-dark-forgot.png), [phone](screenshots/mobile-login-dark-default.png), [full](screenshots/login-dark-full.png) |
| Sign up (app shell) | `app.gladia.io/signup` | [default](screenshots/signup-dark-default.png), [full](screenshots/signup-dark-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [drawer](screenshots/mobile-home-dark-drawer.png), [full](screenshots/mobile-home-dark-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-dark-default.png), [full](screenshots/mobile-pricing-dark-full.png) |
| Demo request, phone | `/demo-request` | [default](screenshots/mobile-demo-request-dark-default.png), [full](screenshots/mobile-demo-request-dark-full.png) |
| Library, phone | `/library` | [default](screenshots/mobile-library-light-default.png), [full](screenshots/mobile-library-light-full.png) |
| Docs, phone | `docs.gladia.io/chapters/pre-recorded-stt/quickstart` | [default](screenshots/mobile-docs-quickstart-light-default.png), [full](screenshots/mobile-docs-quickstart-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Product mega-menu | every page header | hovered the 'Product' trigger — the site's own hover-intent activation; keyboard focus+Enter is the fallback | [home-dark-menu-product](screenshots/home-dark-menu-product.png), [mega-panel](#mega-menu-panel), [mega-item](#mega-menu-item) |
| Other mega-menus | every page header | the same activation on Solutions, Developers, Resources and Company — captured as screenshots | [home-dark-menu-solutions](screenshots/home-dark-menu-solutions.png), [home-dark-menu-developers](screenshots/home-dark-menu-developers.png), [home-dark-menu-resources](screenshots/home-dark-menu-resources.png), [home-dark-menu-company](screenshots/home-dark-menu-company.png) |
| Mobile nav sheet | home page, phone width | the 'Open menu' button's own toggle | [m-drawer](#mobile-nav-overlay) |
| Pricing mode toggle | /pricing | the 'Real-time' half's own toggle re-priced the grid; restored afterwards | [pricing-dark-toggle-realtime](screenshots/pricing-dark-toggle-realtime.png), [price-mode-rt](#pricing-mode-real-time), [price-mode-async](#pricing-mode-async) |
| Pricing calculator | /pricing | the hours field was typed into then cleared; the range and feature checkboxes were measured at rest, never dragged or toggled | [calc-hours](#calculator-hours-field), [calc-range](#calculator-range), [calc-feature](#calculator-feature-checkbox) |
| FAQ accordion | /pricing | a question row's own toggle | [faq-acc](#faq-accordion) |
| Docs theme preference | docs pages | the 'Change theme preference' control — measured; its dark surface was captured as the theme-dark screenshots rather than by holding the toggle | [docs-theme-btn](#theme-toggle), [docs-quickstart-light-theme-dark](screenshots/docs-quickstart-light-theme-dark.png) |
| Demo-request/auth fields | /demo-request, app.gladia.io / /signup | typed into then cleared — nothing sent | [demo-email](#email-field), [login-email](#email-field) |
| Login/signup buttons | app.gladia.io / and /signup | the SSO buttons and sign-in/sign-up actions were measured, never pressed — the forms were never opened or submitted | [login-sso](#sso-button), [signup-sso](#sso-button-signup) |
| Signed-in product | a Gladia account | the app and every post-login surface needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 16 components were given a real keyboard focus. 16 draw an outline ring: `nav-menu-btn` (2px solid #947afc `light.bg.brand`, offset 2px), `nav-pricing` (1px auto #101010, offset 1px), `nav-demo` (1px auto #101010, offset 1px), `nav-cta` (1px auto #101010, offset 1px), `footer-link` (1px auto #101010, offset 1px), `prod-cta` (1px auto #101010, offset 1px), `price-mode-async` (2px solid #1a9eff `light.border.focus`, offset 2px), `price-mode-rt` (2px solid #1a9eff `light.border.focus`, offset 2px), `demo-submit` (1px auto #101010, offset 0px), `docs-search` (1px auto #2e343e, offset 0px), `docs-theme-btn` (1px auto #2e343e, offset 0px), `login-sso` (2px solid #7e65e1, offset 2px), `login-submit` (2px solid #7e65e1, offset 2px), `signup-sso` (2px solid #7e65e1, offset 2px), `signup-submit` (2px solid #7e65e1, offset 2px), `m-menu-btn` (2px solid #947afc `light.bg.brand`, offset 2px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.16s | `cubic-bezier(0, 0, 0.2, 1)` | background, background-color, border-color, color, transform | demo-company-size, demo-email, demo-name, footer-link, hero-badge, lib-card, m-menu-btn, mega-item and more |
| 0.2s | `cubic-bezier(0, 0, 0.2, 1)` | background-color, border-color, color, opacity | nav-cta, nav-demo |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | docs-theme-btn |
| 0.25s | `cubic-bezier(0, 0, 0.2, 1)` | box-shadow | nav-cta, nav-demo |
| 0.25s | `cubic-bezier(0.34, 1.56, 0.64, 1)` | transform | nav-cta, nav-demo |
| 0.32s | `cubic-bezier(0, 0, 0.2, 1)` | border-color, box-shadow, color | plan-card, price-mode-async, price-mode-rt |
| 0.8s | `cubic-bezier(0, 0, 0.2, 1)` | opacity, transform | demo-h1, lib-h1 |
| 0.9s | `cubic-bezier(0.22, 1, 0.36, 1)` | opacity, transform | prod-h1 |
| 1.25s | `cubic-bezier(0, 0, 0.2, 1)` | opacity, transform | demo-submit |
| 1.4s | `cubic-bezier(0, 0, 0.2, 1)` | opacity, transform | plan-card |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Mega-menu panel](#mega-menu-panel) | 1080 x 361.66 | - | - | transparent | none | 0 |
| [Plan card](#plan-card) | 428 x 888.13 | 1px solid rgba(255, 255, 255, 0.08) `core.color.alpha.white8` | 24px | transparent | rgba(0, 0, 0, 0.22) 0px 8px 28px 0px | 48px 40px 40px 40px |
| [Footer](#footer) | 1440 x 849.38 | T: 1px solid #0c0c0c `core.color.neutral.900` | - | transparent | none | 72px 0px 64px 0px |
| [Login panel](#login-panel) | 720 x 900 | - | - | transparent | none | 0 |
| [Signup panel](#signup-panel) | 720 x 900 | - | - | transparent | none | 0 |
| [Mobile nav overlay](#mobile-nav-overlay) | 390 x 844 | - | - | transparent | none | 0 |

## Components

### Site chrome

The floating glass navbar on every marketing page: the Gladia wordmark, the Product/Solutions/Developers/Resources/Company mega-menu triggers (hover intent, keyboard Enter the fallback), Pricing, 'Request a demo' and the purple signup pill; the product mega-menu panel opens under the trigger.

#### Site header
The floating rounded glass navbar at the top of every marketing page: the Gladia wordmark, the Product/Solutions/Developers/Resources/Company mega-menu triggers, Pricing, "Request a demo" and the signup CTA. Read as `mkt-header` on the home page.
Read on 2026-11-16.

**Values (default).** size 1200 x 72; border 1px solid #1f1f1f; radius 20px; background rgba(0, 0, 0, 0.65); text Suisse Intl 15/normal 400, rgba(255, 255, 255, 0.68); icon 109.94 x 28, #ffffff `light.bg.primary`.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The inline-SVG Gladia symbol + wordmark in the header, linking home. Read as `mkt-logo` on the home page.
Read on 2026-11-16.

**Values (default).** size 323.5 x 28; background transparent; text Suisse Intl 16/22.4 400, #ffffff `light.bg.primary`; icon 109.94 x 28, #ffffff `light.bg.primary`.

![Logo default](components/crops/mkt-logo-default.png)

#### Mega-menu trigger
The "Product" header button — a hover-intent trigger whose aria-expanded flips while the mega-menu mounts (the opened panel is the mega-panel component below). Hover is the site's own activation, focus+Enter the fallback. Read as `nav-menu-btn` on the home page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 55 x 31; padding 6px 0px; background transparent; text Suisse Intl 15/normal 400, rgba(255, 255, 255, 0.68); transition color 0.16s cubic-bezier(0, 0, 0.2, 1) |
| hover | size 73 x 31; text Suisse Intl 15/normal 400, #ffffff `light.bg.primary`; icon 12 x 12, #ffffff `light.bg.primary` |
| focus-visible | size 73 x 31; outline 2px solid #947afc `light.bg.brand`, offset 2px; text Suisse Intl 15/normal 400, #ffffff `light.bg.primary`; icon 12 x 12, #ffffff `light.bg.primary`; layers button.is-active 73.0x31.0 2px solid rgb(148, 122, 252) offset 2px |
| pressed | size 73 x 31; text Suisse Intl 15/normal 400, #ffffff `light.bg.primary`; icon 12 x 12, #ffffff `light.bg.primary` |

![Mega-menu trigger default](components/crops/nav-menu-btn-default.png) ![Mega-menu trigger hover](components/crops/nav-menu-btn-hover.png) ![Mega-menu trigger focus-visible](components/crops/nav-menu-btn-focus-visible.png) ![Mega-menu trigger pressed](components/crops/nav-menu-btn-pressed.png)

#### Mega-menu panel
The product mega-menu panel opened by the "Product" trigger — glass card with product and feature links; its links were never followed. Read as `mega-panel` on the home page.
Read on 2026-11-16.

**Values (default).** size 1080 x 361.66; background transparent; text Geist Mono 11/15.4 400, rgba(148, 122, 252, 0.95); layers div.mega-menu-panel-body.mega-menu-panel-body--product 1080.0x361.7 rgb(0, 0, 0) 23px; div.mega-menu-grid.mega-menu-grid--flat 0.0x0.0 rgb(0, 0, 0); div.mega-menu-overview-card 360.0x361.7 R:1px solid rgba(255, 255, 255, 0.1) rgba(255, 255, 255, 0.14) 0px 1px 0px 0px inset; div::before.mega-menu-overview-card 1pxx361.656px; span.btn.btn-primary 138.0x32.0 rgb(255, 255, 255) 40px; div.mega-menu-ove.

Child layers that carry the look: div 1080x361.7 background #000000 `light.bg.inverse` radius 23px; div 0x0 background #000000 `light.bg.inverse`; div 360x361.7 image linear-gradient(160deg, rgba(255, 255, 255, 0.06) 0%, rgba(255, 255, 255, 0) 42%), linear- border 1px solid rgba(255, 255, 255, 0.1) shadow rgba(255, 255, 255, 0.14) `core.color.alpha.white14` 0px 1px 0px 0px inset.

![Mega-menu panel default](components/crops/mega-panel-default.png)

#### Mega-menu item
A product link inside the opened mega-menu; measured, never followed. Read as `mega-item` on the home page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 359 x 172.98; padding 0px 32px 24px 32px; background transparent; text Geist Mono 11/15.4 400, rgba(148, 122, 252, 0.95); transition background 0.16s cubic-bezier(0, 0, 0.2, 1); layers span.btn.btn-primary 138.0x32.0 rgb(255, 255, 255) 40px |
| hover | layers span.btn.btn-primary 144.8x32.6 rgb(255, 255, 255) 40px |

Child layers that carry the look: span 138x32 background #ffffff `light.bg.primary` radius 40px.

![Mega-menu item default](components/crops/mega-item-default.png) ![Mega-menu item hover](components/crops/mega-item-hover.png)

#### Nav link
The "Pricing" header link; measured, never followed. Read as `nav-pricing` on the home page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 46 x 21; background transparent; text Suisse Intl 15/21 400, rgba(255, 255, 255, 0.68); transition color 0.16s cubic-bezier(0, 0, 0.2, 1), transform 0.16s cubic-bezier(0, 0, 0.2, 1) |
| hover | text Suisse Intl 15/21 400, #ffffff `light.bg.primary`; transform translate(3px, 0px) |
| focus-visible | outline 1px auto #101010, offset 1px; text Suisse Intl 15/21 400, #ffffff `light.bg.primary`; transform translate(3px, 0px); layers a 46.0x21.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Suisse Intl 15/21 400, #ffffff `light.bg.primary`; transform translate(3px, 0px) |

![Nav link default](components/crops/nav-pricing-default.png) ![Nav link hover](components/crops/nav-pricing-hover.png) ![Nav link focus-visible](components/crops/nav-pricing-focus-visible.png) ![Nav link pressed](components/crops/nav-pricing-pressed.png)

#### Demo link
The "Request a demo" header link to /demo-request; measured, never followed. Read as `nav-demo` on the home page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 146 x 32; padding 6px 16px; border 1px solid rgba(255, 255, 255, 0.12) `core.color.alpha.white12`; radius 40px; background #1c1c1e `core.color.neutral.800`; text Suisse Intl 14/19.6 400, #ffffff `light.bg.primary`; transition transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.25s cubic-bezier(0, 0, 0.2, 1), background-color 0.2s cubic-bezier(0, 0, 0.2, 1), color 0.2s cubic-bezier(0, 0, 0.2, 1), border-color 0.2s cubic-bezier(0, 0, 0.2, 1), opacity 0.2s cubic-bezier(0, 0, 0.2, 1) |
| hover | size 148.92 x 32.64; transform scale(1.02) |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | size 148.92 x 32.64; transform scale(1.02) |

![Demo link default](components/crops/nav-demo-default.png) ![Demo link hover](components/crops/nav-demo-hover.png) ![Demo link focus-visible](components/crops/nav-demo-focus-visible.png) ![Demo link pressed](components/crops/nav-demo-pressed.png)

#### Header CTA
The header signup CTA (the brand-purple fill) linking to app.gladia.io/signup; measured, never followed. Read as `nav-cta` on the home page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 81 x 32; padding 6px 16px; radius 40px; background #ffffff `light.bg.primary`; text Suisse Intl 14/19.6 400, #000000 `light.bg.inverse`; transition transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.25s cubic-bezier(0, 0, 0.2, 1), background-color 0.2s cubic-bezier(0, 0, 0.2, 1), color 0.2s cubic-bezier(0, 0, 0.2, 1), border-color 0.2s cubic-bezier(0, 0, 0.2, 1), opacity 0.2s cubic-bezier(0, 0, 0.2, 1) |
| hover | size 82.62 x 32.64; background rgba(255, 255, 255, 0.88); transform scale(1.02) |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | size 82.62 x 32.64; background rgba(255, 255, 255, 0.88); transform scale(1.02) |

![Header CTA default](components/crops/nav-cta-default.png) ![Header CTA hover](components/crops/nav-cta-hover.png) ![Header CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Header CTA pressed](components/crops/nav-cta-pressed.png)

### Home

The home hero: the announcement badge, the display masthead on the dark :root surface, frosted-glass marketing cards and section headings.

#### Hero headline
The home masthead display heading on the dark :root surface. Read as `hero-h1` on the home page.
Read on 2026-11-16.

**Values (default).** size 767.41 x 189.59; background transparent; text Suisse Intl 79/94.8 400, #000000 `light.bg.inverse`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero badge
The announcement badge/pill above the hero headline; measured, never followed. Read as `hero-badge` on the home page.
Read on 2026-11-16.

**Values (default).** size 338.11 x 37.59; padding 4px 12px 4px 4px; border 1px solid rgba(0, 0, 0, 0.12) `light.border.transparent`; radius 9999px; background #ffffff `light.bg.primary`; text Suisse Intl 14/19.6 500, rgba(0, 0, 0, 0.8); transition border-color 0.16s cubic-bezier(0, 0, 0.2, 1).

![Hero badge default](components/crops/hero-badge-default.png)

#### Section heading
A marketing section heading further down the home page — a display-size h2, so transient microcopy never counts. Read as `section-h2` on the home page.
Read on 2026-11-16.

**Values (default).** size 523.19 x 57.59; background transparent; text Suisse Intl 48/57.6 400, #ffffff `light.bg.primary`.

![Section heading default](components/crops/section-h2-default.png)

#### Glass card
A frosted-glass marketing card (the site's --bg-glass + blur + hairline border treatment); measured, never followed. Read as `glass-card` on the home page.

Not on the page when it was captured.

### Pricing

The /pricing grid: the Async/Real-time pricing-mode segmented toggle (aria-pressed, a local UI toggle that re-prices the grid), the plan cards and their CTAs, the calculator's hours field and range slider, the feature checkboxes and the FAQ rows.

#### Pricing headline
The /pricing masthead. Read as `price-h1` on the pricing page.
Read on 2026-11-16.

**Values (default).** size 860 x 76.8; background transparent; text Suisse Intl 64/76.8 400, #ffffff `light.bg.primary`.

![Pricing headline default](components/crops/price-h1-default.png)

#### Pricing mode: Async
The "Async" half of the pricing-mode segmented toggle (data-pricing-mode, aria-pressed); a local UI toggle that re-prices the grid — the opened state was measured after its own toggle. Read as `price-mode-async` on the pricing page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 88 x 35.59; padding 8px 24px; radius 9999px; background transparent; text Suisse Intl 14/19.6 400, #000000 `light.bg.inverse`; transition background-color 0.16s cubic-bezier(0, 0, 0.2, 1), color 0.32s cubic-bezier(0, 0, 0.2, 1) |
| focus-visible | outline 2px solid #1a9eff `light.border.focus`, offset 2px; layers button.pricing-toggle__btn.is-active 88.0x35.6 2px solid rgb(26, 158, 255) offset 2px 9999px |

![Pricing mode: Async default](components/crops/price-mode-async-default.png) ![Pricing mode: Async hover](components/crops/price-mode-async-hover.png) ![Pricing mode: Async focus-visible](components/crops/price-mode-async-focus-visible.png) ![Pricing mode: Async pressed](components/crops/price-mode-async-pressed.png) ![Pricing mode: Async opened](components/crops/price-mode-async-opened.png)

#### Pricing mode: Real-time
The "Real-time" half of the pricing-mode segmented toggle; a local UI toggle — the opened state was measured after its own toggle, then the async side was restored. Read as `price-mode-rt` on the pricing page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 114 x 35.59; padding 8px 24px; radius 9999px; background transparent; text Suisse Intl 14/19.6 400, #a3a3a3 `light.text.disabled`; transition background-color 0.16s cubic-bezier(0, 0, 0.2, 1), color 0.32s cubic-bezier(0, 0, 0.2, 1) |
| hover | text Suisse Intl 14/19.6 400, #ffffff `light.bg.primary` |
| focus-visible | outline 2px solid #1a9eff `light.border.focus`, offset 2px; layers button.pricing-toggle__btn 114.0x35.6 2px solid rgb(26, 158, 255) offset 2px 9999px |
| pressed | text Suisse Intl 14/19.6 400, #ffffff `light.bg.primary` |
| opened | text Suisse Intl 14/19.6 400, #000000 `light.bg.inverse` |

![Pricing mode: Real-time default](components/crops/price-mode-rt-default.png) ![Pricing mode: Real-time hover](components/crops/price-mode-rt-hover.png) ![Pricing mode: Real-time focus-visible](components/crops/price-mode-rt-focus-visible.png) ![Pricing mode: Real-time pressed](components/crops/price-mode-rt-pressed.png) ![Pricing mode: Real-time opened](components/crops/price-mode-rt-opened.png)

#### Plan card
A plan card on /pricing — one column of the pricing grid (.pricing-grid--plans > .pricing-card): name, per-hour price, feature list and its CTA. Read as `plan-card` on the pricing page.
Read on 2026-11-16.

**Values (default).** size 428 x 888.13; padding 48px 40px 40px 40px; border 1px solid rgba(255, 255, 255, 0.08) `core.color.alpha.white8`; radius 24px; background transparent; shadow rgba(0, 0, 0, 0.22) 0px 8px 28px 0px; text Suisse Intl 16/22.4 400, #ffffff `light.bg.primary`; transition opacity 1.4s cubic-bezier(0, 0, 0.2, 1), transform 1.4s cubic-bezier(0, 0, 0.2, 1), border-color 0.32s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.32s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #a3a3a3 `light.text.disabled`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Plan CTA
A plan card's primary action ("Start with 50€ free credits" or the enterprise contact link); measured, never followed. Read as `plan-cta` on the pricing page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 346 x 40; padding 8px 20px; radius 40px; background #ffffff `light.bg.primary`; text Suisse Intl 14/19.6 400, #000000 `light.bg.inverse`; transition transform 0.16s cubic-bezier(0, 0, 0.2, 1) |
| pressed | size 352.92 x 40.8; transform scale(1.02) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Calculator hours field
The pricing calculator's hours-per-month number input (default 500); typed into then cleared — a local UI control, nothing submitted. Read as `calc-hours` on the pricing page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 72 x 19.59; background transparent; text Suisse Intl 14/19.6 400, #ffffff `light.bg.primary`; placeholder #ffffff `light.bg.primary` |

![Calculator hours field default](components/crops/calc-hours-default.png) ![Calculator hours field focused](components/crops/calc-hours-focused.png) ![Calculator hours field filled](components/crops/calc-hours-filled.png)

#### Calculator range
The "Hours of audio per month" range slider in the calculator; measured at rest, never dragged. Read as `calc-range` on the pricing page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 391 x 20; background transparent; text Arial 13.33/normal 400, #9d968e; placeholder #9d968e |
| focused | radius 8px; outline 2px solid #925bff `core.color.purple.500`, offset 4px; layers input.pricing-calc__range 391.0x20.0 2px solid rgb(146, 91, 255) offset 4px 8px |

![Calculator range default](components/crops/calc-range-default.png) ![Calculator range focused](components/crops/calc-range-focused.png)

#### Calculator feature checkbox
A feature add-on checkbox in the pricing calculator (summarization, sentiment, translation, NER, PII); a local UI control — measured, never toggled. Read as `calc-feature` on the pricing page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 13 x 13; background transparent; text Arial 13.33/normal 400, #000000 `light.bg.inverse`; opacity 0; placeholder #000000 `light.bg.inverse` |
| focused | outline 1px auto #101010, offset 2px; layers input 13.0x13.0 1px auto rgb(16, 16, 16) offset 2px |

![Calculator feature checkbox default](components/crops/calc-feature-default.png) ![Calculator feature checkbox focused](components/crops/calc-feature-focused.png)

#### FAQ accordion
A question row in the pricing FAQ; the opened state was measured after its own toggle — a local UI toggle. Read as `faq-acc` on the pricing page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 720 x 86.39; padding 32px 0px; background transparent; text Suisse Intl 16/22.4 400, #ffffff `light.bg.primary`; icon 20 x 20, #727272 `light.text.tertiary` |
| opened | icon 20 x 20, #a3a3a3 `light.text.disabled` |

![FAQ accordion default](components/crops/faq-acc-default.png) ![FAQ accordion opened](components/crops/faq-acc-opened.png)

### Demo request form

The /demo-request form: e-mail, name, company-size select, the terms checkbox and the submit button — measured and typed into then cleared, never submitted.

#### Demo headline
The /demo-request masthead over the sales form. Read as `demo-h1` on the demo-request page.
Read on 2026-11-16.

**Values (default).** size 860 x 76.8; background transparent; text Suisse Intl 64/76.8 400, #ffffff `light.bg.primary`; transition opacity 0.8s cubic-bezier(0, 0, 0.2, 1), transform 0.8s cubic-bezier(0, 0, 0.2, 1).

![Demo headline default](components/crops/demo-h1-default.png)

#### Email field
The work-e-mail input on the demo-request form; focused and typed into then cleared — never submitted. Read as `demo-email` on the demo-request page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 462 x 44; padding 0px 16px; border 1px solid rgba(255, 255, 255, 0.08) `core.color.alpha.white8`; radius 8px; background rgba(255, 255, 255, 0.04); text Suisse Intl 14/19.6 400, #ffffff `light.bg.primary`; transition border-color 0.16s cubic-bezier(0, 0, 0.2, 1), background-color 0.16s cubic-bezier(0, 0, 0.2, 1); placeholder #727272 `light.text.tertiary` |
| focused, filled | border 1px solid #947afc `light.bg.brand`; background rgba(255, 255, 255, 0.06) |

![Email field default](components/crops/demo-email-default.png) ![Email field focused](components/crops/demo-email-focused.png) ![Email field filled](components/crops/demo-email-filled.png)

#### First-name field
The first-name input on the demo-request form; focused and typed into then cleared — never submitted. Read as `demo-name` on the demo-request page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 223 x 44; padding 0px 16px; border 1px solid rgba(255, 255, 255, 0.08) `core.color.alpha.white8`; radius 8px; background rgba(255, 255, 255, 0.04); text Suisse Intl 14/19.6 400, #ffffff `light.bg.primary`; transition border-color 0.16s cubic-bezier(0, 0, 0.2, 1), background-color 0.16s cubic-bezier(0, 0, 0.2, 1); placeholder #727272 `light.text.tertiary` |
| focused, filled | border 1px solid #947afc `light.bg.brand`; background rgba(255, 255, 255, 0.06) |

![First-name field default](components/crops/demo-name-default.png) ![First-name field focused](components/crops/demo-name-focused.png) ![First-name field filled](components/crops/demo-name-filled.png)

#### Company-size select
The company-size select on the demo-request form; measured at rest, never changed. Read as `demo-company-size` on the demo-request page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 462 x 44; padding 0px 40px 0px 16px; border 1px solid rgba(255, 255, 255, 0.08) `core.color.alpha.white8`; radius 8px; background rgba(255, 255, 255, 0.04); image an image (data URI); text Suisse Intl 14/19.6 400, #727272 `light.text.tertiary`; transition border-color 0.16s cubic-bezier(0, 0, 0.2, 1), background-color 0.16s cubic-bezier(0, 0, 0.2, 1) |
| focused | border 1px solid #947afc `light.bg.brand`; background rgba(255, 255, 255, 0.06) |

![Company-size select default](components/crops/demo-company-size-default.png) ![Company-size select focused](components/crops/demo-company-size-focused.png)

#### Terms checkbox
The required terms-acceptance checkbox on the demo-request form (the input is visually hidden behind its styled label); measured at rest, never toggled. Read as `demo-terms` on the demo-request page.
Read on 2026-11-16.

**Values (default).** size 462 x 18; background transparent; text Suisse Intl 12/18 400, #727272 `light.text.tertiary`; layers span.form-checkbox-mark 16.0x16.0 rgb(28, 28, 30) T:1px solid rgb(37, 37, 37) / R:1px solid rgb(37, 37, 37) / B:1px solid rgb(37, 37, 37) / L:1px solid rgb(37, 37, 37).

**Focus not capturable.** A real keyboard focus could not be held on this element (`focused` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: span 16x16 background #1c1c1e `core.color.neutral.800` border 1px solid #252525 `core.color.neutral.700`.

![Terms checkbox default](components/crops/demo-terms-default.png)

#### Submit button
The demo-request form's submit button; its states were measured but the button was never clicked — the form was never sent. Read as `demo-submit` on the demo-request page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 462 x 48; padding 12px 28px; radius 40px; background #ffffff `light.bg.primary`; text Suisse Intl 16/normal 400, #000000 `light.bg.inverse`; transition opacity 1.25s cubic-bezier(0, 0, 0.2, 1), transform 1.25s cubic-bezier(0, 0, 0.2, 1) |
| focus-visible | outline 1px auto #101010, offset 0px |

![Submit button default](components/crops/demo-submit-default.png) ![Submit button hover](components/crops/demo-submit-hover.png) ![Submit button focus-visible](components/crops/demo-submit-focus-visible.png) ![Submit button pressed](components/crops/demo-submit-pressed.png)

### Login and signup (app shell)

app.gladia.io / and /signup — the product shell's auth cards (e-mail/password, 'Continue with' SSO, the sign-in/sign-up actions), a different stack that does not share the marketing token layer. Measured as forms, never opened or submitted.

#### Login panel
The sign-in card on app.gladia.io/ — the shell's only signed-out landing: fields, SSO and the sign-in action. Measured, never submitted. Read as `login-panel` on the login page.
Read on 2026-11-15.

**Values (default).** size 720 x 900; background transparent; text Inter 24/32 600, #ffffff `light.bg.primary`; layers div.relative.py-2 360.0x40.0 rgb(21, 24, 29) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(46, 52, 62) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px 8px; div.relative.py-2 360.0x40.0 rgb(21, 24, 29) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(46, 52, 62) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px .

Child layers that carry the look: div 360x40 background #15181d radius 8px shadow transparent 0px 0px 0px 0px, #2e343e 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) `light.bg.glassLight` 0px 1px 2px 0px; div 360x40 background #15181d radius 8px shadow transparent 0px 0px 0px 0px, #2e343e 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) `light.bg.glassLight` 0px 1px 2px 0px; button 360x44 background #6446db radius 8px shadow transparent 0px 0px 0px 0px, oklab(0.999994 0.0000455678 0.0000200868 / 0.12) 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px.

![Login panel default](components/crops/login-panel-default.png)

#### Email field
The e-mail input on the sign-in shell; focused and typed into then cleared — never submitted. Read as `login-email` on the login page.
Read on 2026-11-15.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 0 x 0; background transparent; text Inter 16/24 400, #ffffff `light.bg.primary`; placeholder #ffffff `light.bg.primary` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Password field
The password input on the sign-in shell; focused and typed into then cleared — never submitted. Read as `login-password` on the login page.
Read on 2026-11-15.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 336 x 24; background transparent; text Inter 16/24 400, #f1f2f4; placeholder #6f7c90 |

![Password field default](components/crops/login-password-default.png) ![Password field focused](components/crops/login-password-focused.png) ![Password field filled](components/crops/login-password-filled.png)

#### SSO button
A "Continue with" SSO button on the sign-in shell; measured, never pressed. Read as `login-sso` on the login page.
Read on 2026-11-15.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 360 x 44; padding 10px 16px; radius 8px; background #15181d; shadow #404854 0px 0px 0px 1px inset; text Inter 16/24 600, #f1f2f4; icon 20 x 20, #f1f2f4 |
| focus-visible | outline 2px solid #7e65e1, offset 2px |

![SSO button default](components/crops/login-sso-default.png) ![SSO button hover](components/crops/login-sso-hover.png) ![SSO button focus-visible](components/crops/login-sso-focus-visible.png) ![SSO button pressed](components/crops/login-sso-pressed.png)

#### Sign-in button
The sign-in action; its states were measured but the button was never clicked — nothing was submitted. Read as `login-submit` on the login page.
Read on 2026-11-15.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 360 x 44; padding 10px 16px; radius 8px; background #6446db; shadow oklab(0.999994 0.0000455678 0.0000200868 / 0.12) 0px 0px 0px 1px inset; text Inter 16/24 600, #ffffff `light.bg.primary` |
| focus-visible | outline 2px solid #7e65e1, offset 2px |

![Sign-in button default](components/crops/login-submit-default.png) ![Sign-in button hover](components/crops/login-submit-hover.png) ![Sign-in button focus-visible](components/crops/login-submit-focus-visible.png) ![Sign-in button pressed](components/crops/login-submit-pressed.png)

#### Sign-up link
The sign-up link on the login shell; measured, never followed. Read as `login-signup-link` on the login page.

Not on the page when it was captured.

#### Signup panel
The sign-up card on app.gladia.io/signup; measured, never submitted. Read as `signup-panel` on the signup page.
Read on 2026-11-15.

**Values (default).** size 720 x 900; background transparent; text Inter 24/32 600, #ffffff `light.bg.primary`; layers div.relative.py-2 360.0x40.0 rgb(21, 24, 29) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(46, 52, 62) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px 8px; div.relative.py-2 360.0x40.0 rgb(21, 24, 29) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(46, 52, 62) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px .

Child layers that carry the look: div 360x40 background #15181d radius 8px shadow transparent 0px 0px 0px 0px, #2e343e 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) `light.bg.glassLight` 0px 1px 2px 0px; div 360x40 background #15181d radius 8px shadow transparent 0px 0px 0px 0px, #2e343e 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) `light.bg.glassLight` 0px 1px 2px 0px; div 360x40 background #15181d radius 8px shadow transparent 0px 0px 0px 0px, #2e343e 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) `light.bg.glassLight` 0px 1px 2px 0px.

![Signup panel default](components/crops/signup-panel-default.png)

#### Email field (signup)
The e-mail input on the sign-up shell; focused and typed into then cleared — never submitted. Read as `signup-email` on the signup page.
Read on 2026-11-15.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 0 x 0; background transparent; text Inter 16/24 400, #ffffff `light.bg.primary`; placeholder #ffffff `light.bg.primary` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### SSO button (signup)
A "Continue with" SSO button on /signup; measured, never pressed. Read as `signup-sso` on the signup page.
Read on 2026-11-15.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 360 x 44; padding 10px 16px; radius 8px; background #15181d; shadow #404854 0px 0px 0px 1px inset; text Inter 16/24 600, #f1f2f4; icon 20 x 20, #f1f2f4 |
| focus-visible | outline 2px solid #7e65e1, offset 2px |

![SSO button (signup) default](components/crops/signup-sso-default.png) ![SSO button (signup) hover](components/crops/signup-sso-hover.png) ![SSO button (signup) focus-visible](components/crops/signup-sso-focus-visible.png) ![SSO button (signup) pressed](components/crops/signup-sso-pressed.png)

#### Sign-up button
The sign-up action; measured, never clicked — nothing was submitted. Read as `signup-submit` on the signup page.
Read on 2026-11-15.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 360 x 44; padding 10px 16px; radius 8px; background #6446db; shadow oklab(0.999994 0.0000455678 0.0000200868 / 0.12) 0px 0px 0px 1px inset; text Inter 16/24 600, #ffffff `light.bg.primary` |
| focus-visible | outline 2px solid #7e65e1, offset 2px |

![Sign-up button default](components/crops/signup-submit-default.png) ![Sign-up button hover](components/crops/signup-submit-hover.png) ![Sign-up button focus-visible](components/crops/signup-submit-focus-visible.png) ![Sign-up button pressed](components/crops/signup-submit-pressed.png)

### Product pages

The product marketing pages (/product/speech-to-text-api and siblings): the masthead, code samples, feature headings and CTAs.

#### Product headline
The /product/speech-to-text-api masthead on the dark surface. Read as `prod-h1` on the product page.
Read on 2026-11-16.

**Values (default).** size 639.98 x 95.03; background transparent; text Suisse Intl 79.2/95.04 400, #ffffff `light.bg.primary`; transition opacity 0.9s cubic-bezier(0.22, 1, 0.36, 1), transform 0.9s cubic-bezier(0.22, 1, 0.36, 1).

![Product headline default](components/crops/prod-h1-default.png)

#### Product CTA
A call-to-action on the product page; measured, never followed. Read as `prod-cta` on the product page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 146 x 32; padding 6px 16px; border 1px solid rgba(255, 255, 255, 0.12) `core.color.alpha.white12`; radius 40px; background #1c1c1e `core.color.neutral.800`; text Suisse Intl 14/19.6 400, #ffffff `light.bg.primary`; transition transform 0.16s cubic-bezier(0, 0, 0.2, 1) |
| hover | size 148.92 x 32.64; transform scale(1.02) |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | size 148.92 x 32.64; transform scale(1.02) |

![Product CTA default](components/crops/prod-cta-default.png) ![Product CTA hover](components/crops/prod-cta-hover.png) ![Product CTA focus-visible](components/crops/prod-cta-focus-visible.png) ![Product CTA pressed](components/crops/prod-cta-pressed.png)

#### Code sample
A code sample block on the product page — mono face on an elevated surface. Read as `prod-code` on the product page.
Read on 2026-11-16.

**Values (default).** size 549.5 x 681.94; padding 20px; border T: 1px solid rgba(255, 255, 255, 0.08) `core.color.alpha.white8`; R: 1px solid rgba(255, 255, 255, 0.1); B: 1px solid rgba(255, 255, 255, 0.1); L: 1px solid rgba(255, 255, 255, 0.1); radius 0px 0px 16px 16px; background #141414; text Geist Mono 13/20.15 400, rgba(255, 255, 255, 0.82).

![Code sample default](components/crops/prod-code-default.png)

#### Feature heading
A feature section heading on the product page. Read as `prod-feature` on the product page.
Read on 2026-11-16.

**Values (default).** size 398.41 x 52; background transparent; text Suisse Intl 40/52 400, #ffffff `light.bg.primary`.

![Feature heading default](components/crops/prod-feature-default.png)

### Blog, library and marketing indexes

The /library index (the one marketing page on the light .light-mode scope), and /blog — a legacy Webflow stack on its own stylesheets, painted light.

#### Library headline
The /library masthead — the one marketing page that carries body.light-mode and paints the light token scope. Read as `lib-h1` on the library page.
Read on 2026-11-15.

**Values (default).** size 357.64 x 57.59; background transparent; text Suisse Intl 48/57.6 400, #000000 `light.bg.inverse`; transition opacity 0.8s cubic-bezier(0, 0, 0.2, 1), transform 0.8s cubic-bezier(0, 0, 0.2, 1).

![Library headline default](components/crops/lib-h1-default.png)

#### Resource card
A content card on the library index; measured, never followed. Read as `lib-card` on the library page.
Read on 2026-11-15. `hover` failed at capture (locator.hover: Element is not visible).

**Values (default).** size 0 x 0; padding 10px 32px; background transparent; text Suisse Intl 16/22.4 400, #000000 `light.bg.inverse`; transition background 0.16s cubic-bezier(0, 0, 0.2, 1).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Blog headline
The /blog index masthead on the legacy Webflow stack — its own stylesheets, painted light. Read as `blog-h1` on the blog page.
Read on 2026-11-15.

**Values (default).** size 0 x 0; background transparent; text Suisseintl 120/132 400, #ffffff `light.bg.primary`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Article card
An article card in the blog index; measured, never followed. Read as `blog-card` on the blog page.
Read on 2026-11-15. `hover` failed at capture (locator.hover: Element is not visible).

**Values (default).** size 0 x 0; padding 16px 12px; border 1px solid #0d0d0d; radius 12px; background transparent; text Suisseintl 16/24 400, #ffffff `light.bg.primary`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Docs site (Mintlify)

docs.gladia.io — a Mintlify docs site with its own token layer and a real light/dark preference: the search trigger, the theme-preference control (never held), sidebar links, code blocks and language tabs.

#### Docs headline
The docs introduction masthead on the Mintlify stack. Read as `docs-h1` on the docs introduction page.
Read on 2026-11-15.

**Values (default).** size 309.7 x 40; background transparent; text Inter 36/40 600, #181818.

![Docs headline default](components/crops/docs-h1-default.png)

#### Sidebar link
A sidebar navigation link in the docs tree; measured, never followed. Read as `docs-nav-link` on the docs introduction page.
Read on 2026-11-15.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 240 x 32; padding 6px 12px 6px 16px; radius 12px; background transparent; text Inter 14/20 400, #3f4040 |
| hover | background oklab(0.434945 0.0000198185 0.00000870228 / 0.05); text Inter 14/20 400, #181818 |

![Sidebar link default](components/crops/docs-nav-link-default.png) ![Sidebar link hover](components/crops/docs-nav-link-hover.png)

#### Doc page headline
"Quickstart" — a docs article headline on the Mintlify stack. Read as `docs-h1b` on the docs quickstart page.
Read on 2026-11-16.

**Values (default).** size 172.02 x 40; background transparent; text Inter 36/40 600, #181818.

![Doc page headline default](components/crops/docs-h1b-default.png)

#### Search trigger
The docs' search button — a local UI toggle for the search overlay; measured, never opened. Read as `docs-search` on the docs quickstart page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 224 x 36; padding 0px 12px 0px 14px; radius 12px; background #ffffff `light.bg.primary`; shadow oklab(0.704915 -0.00107276 -0.000326514 / 0.3) 0px 0px 0px 1px; text Inter 14/24 400, #717171; icon 16 x 16, #3f4040 |
| hover | shadow oklab(0.434945 0.0000198185 0.00000870228 / 0.3) 0px 0px 0px 1px; icon 16 x 16, #262627 |
| focus-visible | outline 1px auto #2e343e, offset 0px |
| pressed | shadow oklab(0.434945 0.0000198185 0.00000870228 / 0.3) 0px 0px 0px 1px; icon 16 x 16, #262627 |

![Search trigger default](components/crops/docs-search-default.png) ![Search trigger hover](components/crops/docs-search-hover.png) ![Search trigger focus-visible](components/crops/docs-search-focus-visible.png) ![Search trigger pressed](components/crops/docs-search-pressed.png)

#### Theme toggle
The docs' theme-preference control — a local UI toggle that flips the Mintlify page between light and dark; measured at rest, never switched here (the dark surface is captured in the screenshots pass). Read as `docs-theme-btn` on the docs quickstart page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 20 x 20; radius 9999px; background oklab(0.905852 -0.000996143 -0.000301898 / 0.5); text Inter 16/24 400, #515151 `light.text.link`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, #515151 `light.text.link` |
| focus-visible | outline 1px auto #2e343e, offset 0px |

![Theme toggle default](components/crops/docs-theme-btn-default.png) ![Theme toggle hover](components/crops/docs-theme-btn-hover.png) ![Theme toggle focus-visible](components/crops/docs-theme-btn-focus-visible.png) ![Theme toggle pressed](components/crops/docs-theme-btn-pressed.png)

#### Code block
A code block on the docs article; Mintlify's own syntax-highlight layer paints these. Inline code (`transcribe()` and friends) is a different element and never counts. Read as `docs-code` on the docs quickstart page.
Read on 2026-11-16.

**Values (default).** size 592 x 24; background transparent; shadow rgba(59, 130, 246, 0.5) 0px 0px 0px 0px; text Paper Mono 14/24 400, #953800; layers pre.shiki.shiki-themes 592.0x24.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px; code 592.0x24.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0.

![Code block default](components/crops/docs-code-default.png)

#### Code-language tab
A language tab on a docs code sample; a local UI toggle — measured, never switched. Read as `docs-tab` on the docs quickstart page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 75 x 24; background transparent; text Inter 12/24 500, #2e343e; layers div.absolute.-bottom-1.5 75.0x2.0 rgb(46, 52, 62) 9999px |
| opened | layers div.peer/title.flex 75.0x24.0 oklab(0.905852 -0.000996143 -0.000301898 / 0.5) 8px; div.absolute.-bottom-1.5 75.0x2.0 rgb(46, 52, 62) 9999px |

Child layers that carry the look: div 75x2 background #2e343e radius 9999px.

![Code-language tab default](components/crops/docs-tab-default.png) ![Code-language tab opened](components/crops/docs-tab-opened.png)

### Mobile (390 wide)

The phone surface at 390 wide: the header with the 'Open menu' button, the nav sheet (div#mobileNav.mobile-nav), the hero.

#### Mobile top bar
The phone header at 390 wide: the wordmark and the "Open menu" button. Read as `m-topbar` on the home page at 390 wide.
Read on 2026-11-16.

**Values (default).** size 358 x 56; border 1px solid #1f1f1f; radius 20px; background rgba(0, 0, 0, 0.65); text Suisse Intl 14/19.6 400, #000000 `light.bg.inverse`.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile menu button
The "Open menu" button — a local UI toggle; the opened state was measured after activating it. Read as `m-menu-btn` on the home page at 390 wide.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; border 1px solid rgba(255, 255, 255, 0.1); radius 999px; background rgba(255, 255, 255, 0.04); text Suisse Intl 13.33/normal 400, #ffffff `light.bg.primary`; transition background 0.16s cubic-bezier(0, 0, 0.2, 1), border-color 0.16s cubic-bezier(0, 0, 0.2, 1) |
| hover | border 1px solid rgba(255, 255, 255, 0.18); background rgba(255, 255, 255, 0.1) |
| focus-visible | border 1px solid rgba(255, 255, 255, 0.18); background rgba(255, 255, 255, 0.1); outline 2px solid #947afc `light.bg.brand`, offset 2px |
| pressed, opened | border 1px solid rgba(255, 255, 255, 0.18); background rgba(255, 255, 255, 0.1) |

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png) ![Mobile menu button opened](components/crops/m-menu-btn-opened.png)

#### Mobile nav overlay
The navigation sheet opened by the menu button (div#mobileNav.mobile-nav, .is-open while aria-hidden flips to false); its links were never followed. Read as `m-drawer` on the home page at 390 wide.
Read on 2026-11-16.

**Values (default).** size 390 x 844; background transparent; text Suisse Intl 16/normal 500, #ffffff `light.bg.primary`; icon 16 x 16, rgba(255, 255, 255, 0.8); layers div.mobile-nav-backdrop 390.0x844.0 rgba(0, 0, 0, 0.55); div.mobile-nav-sheet 358.0x744.0 rgb(13, 13, 13) T:1px solid rgb(31, 31, 31) / R:1px solid rgb(31, 31, 31) / B:1px solid rgb(31, 31, 31) / L:1px solid rgb(31, 31, 31) 20px; div.mobile-nav-section.is-open 324.0x640.0 B:1px solid rgba(255, 255, 255, 0.06); span.mega-menu-item-icon 32.0x32.0 rgba(255, 255, 255, 0.05) T:1px solid rgba(255, 255, .

Child layers that carry the look: div 390x844 background rgba(0, 0, 0, 0.55); div 358x744 background #0d0d0d border 1px solid #1f1f1f radius 20px; div 324x640 border 1px solid rgba(255, 255, 255, 0.06).

![Mobile nav overlay default](components/crops/m-drawer-default.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.
Read on 2026-11-16.

**Values (default).** size 342 x 144; background transparent; text Suisse Intl 40/48 400, #000000 `light.bg.inverse`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

### Footer

The page footer: sitemap columns, social icons and legal links.

#### Footer
The page footer: sitemap columns, social icons, legal links and the Gladia mark. Read as `footer` on the home page.
Read on 2026-11-16.

**Values (default).** size 1440 x 849.38; padding 72px 0px 64px 0px; border T: 1px solid #0c0c0c `core.color.neutral.900`; background transparent; text Suisse Intl 14/19.6 400, #ffffff `light.bg.primary`; icon 94.23 x 24, #ffffff `light.bg.primary`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on the home page.
Read on 2026-11-16.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 211.19 x 21; background transparent; text Suisse Intl 14/21 400, #a3a3a3 `light.text.disabled`; transition color 0.16s cubic-bezier(0, 0, 0.2, 1) |
| hover | text Suisse Intl 14/21 400, #ffffff `light.bg.primary` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a 211.2x21.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Suisse Intl 14/21 400, #ffffff `light.bg.primary` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

## Icons

54 distinct inline-SVG icons were collected from the live pages into [icons/](icons) by `tools/capture/icons.mjs`, indexed in [icons/INDEX.tsv](icons/INDEX.tsv): a file is named from `tools/capture/icon-names.tsv` where its geometry hash is listed, else the label or class of the control it sits in, else `icon-<hash>`; colour is kept as `currentColor` wherever it matched the text colour, so each icon recolours from CSS `color` the way it does on the site. The icons are the product's artwork — borrow the set's grammar (sizes, stroke-vs-fill, naming roles), never the artwork itself.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [show-all-features](icons/show-all-features.svg) | 20x20 | 0 0 20 20 | stroke | home; product-stt; product-realtime; pricing; nav | Show all features / Is Gladia’s speech-to-text API more accu |
| [expand](icons/expand.svg) | 14x14 | 0 0 16 16 | stroke | home; nav | Expand |
| [icon-7b3ca081](icons/icon-7b3ca081.svg) | 16x16 | 0 0 16 16 | stroke | home; nav | WebSocket streaming, REST upload, and li / Any audio format  |
| [see-the-report](icons/see-the-report.svg) | 11x11 | 0 0 12 12 | stroke | home; nav | See the report |
| [video-stream](icons/video-stream.svg) | 14x14 | 0 0 14 14 | stroke | home; nav | Video Stream |
| [icon-6ef40b59](icons/icon-6ef40b59.svg) | 16x16 | 0 0 16 16 | stroke | home; nav | Pipeline complete · 3.29s total |
| [real-time](icons/real-time.svg) | 14x14 20x20 | 0 0 24 24 | fill | product-stt; product-realtime; use-case-voice-agents | Real-time |
| [microphone](icons/microphone.svg) | 14x14 | 0 0 14 14 | stroke | home; nav | Microphone |
| [phone-call](icons/phone-call.svg) | 14x14 | 0 0 14 14 | stroke | home; nav | Phone Call |
| [audio-stream-received](icons/audio-stream-received.svg) | 14x14 | 0 0 14 14 | stroke | home; nav | Audio stream received |
| [cell-icon](icons/cell-icon-0d131177.svg) | 20x20 36x36 | 0 0 24 24 | fill | product-stt; product-realtime | Word-level timestamps on every utterance |
| [icon-2a0a5bac](icons/icon-2a0a5bac.svg) | 20x20 36x36 | 0 0 24 24 | fill | product-realtime; use-case-voice-agents | 99.9% uptime SLA on Enterprise |
| [icon-33ba7308](icons/icon-33ba7308.svg) | 20x20 36x36 | 0 0 24 24 | fill | product-realtime; use-case-voice-agents | Custom vocabulary for product names, acr |
| [cell-icon](icons/cell-icon-4d2c2c93.svg) | 20x20 | 0 0 24 24 | fill | product-stt; product-realtime |  |
| [cell-icon](icons/cell-icon-4fbca3e7.svg) | 20x20 | 0 0 24 24 | fill | product-stt; product-realtime |  |
| [cell-icon](icons/cell-icon-95116016.svg) | 20x20 | 0 0 24 24 | fill | product-stt; product-realtime |  |
| [cell-icon](icons/cell-icon-98813b14.svg) | 20x20 | 0 0 24 24 | fill | product-stt; product-realtime |  |
| [cell-icon](icons/cell-icon-9ec3b75a.svg) | 20x20 | 0 0 24 24 | fill | product-stt; product-realtime |  |
| [cell-icon](icons/cell-icon-a3e2b2aa.svg) | 20x20 | 0 0 24 24 | fill | product-stt; use-case-voice-agents |  |
| [see-our-startup-program](icons/see-our-startup-program.svg) | 14x14 | 0 0 16 16 | stroke | pricing; partners | See our Startup Program / Complete guide to building voice a |
| [cell-icon](icons/cell-icon-e895a871.svg) | 20x20 | 0 0 24 24 | fill | product-stt; product-realtime |  |
| [cell-icon](icons/cell-icon-efe59b19.svg) | 20x20 36x36 | 0 0 24 24 | fill | product-stt; product-realtime | 100+ languages, so no call falls outside |
| [learn-more](icons/learn-more.svg) | 14x14 16x16 | 0 0 24 24 | stroke | product-stt; product-realtime | Learn more / Discover the Product / Read the Docs |
| [cell-icon](icons/cell-icon-00879a4c.svg) | 20x20 | 0 0 24 24 | fill | product-stt |  |
| [icon-0437c395](icons/icon-0437c395.svg) | 36x36 | 0 0 24 24 | fill | product-realtime | #1 on Switchboard: the lowest error rate |
| [icon-0b661a95](icons/icon-0b661a95.svg) | 36x36 | 0 0 24 24 | fill | product-realtime | WebSockets, SIP, VoIP for any protocol |
| [icon-1628de06](icons/icon-1628de06.svg) | 36x36 | 0 0 24 24 | fill | product-realtime | Code-switching detected mid-sentence, au / Auto language det |
| [view-our-docs](icons/view-our-docs.svg) | 14x14 | 0 0 24 24 | stroke | use-case-voice-agents | View our docs |
| [icon](icons/icon-21348b79.svg) | 20x20 | 0 0 24 24 | fill | product-stt |  |
| [icon-2275df80](icons/icon-2275df80.svg) | 36x36 | 0 0 24 24 | fill | product-realtime | Audio enhancer: pre-processing for noisy |
| [icon](icons/icon-29eb2b36.svg) | 20x20 | 0 0 24 24 | fill | product-stt |  |
| [icon-2aec7ebb](icons/icon-2aec7ebb.svg) | 20x20 | 0 0 20 20 | stroke | demo-request | How do I get started with your API? / What authentication me |
| [100-languages](icons/100-languages.svg) | 14x14 | 0 0 24 24 | fill | use-case-voice-agents | 100+ languages |
| [icon-35d4c0db](icons/icon-35d4c0db.svg) | 36x36 | 0 0 24 24 | fill | product-realtime | Twilio, Recall, Meeting BaaS for telepho |
| [enable-sound](icons/enable-sound.svg) | 16x16 | 0 0 16 16 | fill | solaria-3 | Enable sound |
| [cell-icon](icons/cell-icon-4dd43b47.svg) | 20x20 | 0 0 24 24 | fill | product-stt |  |
| [icon-535ce5b0](icons/icon-535ce5b0.svg) | 36x36 | 0 0 24 24 | fill | product-realtime | Sub-300ms end-to-end latency for uninter |
| [gladia](icons/gladia.svg) | 24x24 | 0 0 82 82 | fill | nav | Gladia |
| [25-concurrent-requests](icons/25-concurrent-requests.svg) | 16x16 | 0 0 16 16 | stroke | pricing | 25 concurrent requests / Rates drop as volume grows / Up to  |
| [enterprise-terms](icons/enterprise-terms.svg) | 14x14 | 0 0 24 24 | fill | use-case-voice-agents | Enterprise terms |
| [icon-68cba3f5](icons/icon-68cba3f5.svg) | 36x36 | 0 0 24 24 | fill | product-realtime | Adjustable endpointing to tune speed vs. |
| [play-video](icons/play-video.svg) | 16x16 | 0 0 16 16 | fill | solaria-3 | Play video |
| [replay-video](icons/replay-video.svg) | 16x16 | 0 0 24 24 | stroke | solaria-3 | Replay video |
| [icon-8cbae4e5](icons/icon-8cbae4e5.svg) | 36x36 | 0 0 24 24 | fill | product-realtime | Multi-channel transcription with separat / Pipecat, LiveKit, |
| [product](icons/product-8ef4f869.svg) | 12x12 | 0 0 12 12 | stroke | nav | Product |
| [product](icons/product-b7561d22.svg) | 16x16 | 0 0 16 16 | stroke | nav | Product / Solutions / Developers |
| [unmute-video](icons/unmute-video.svg) | 16x16 | 0 0 16 16 | fill | solaria-3 | Unmute video |
| [cell-icon](icons/cell-icon-db87ac53.svg) | 20x20 | 0 0 24 24 | fill | product-realtime |  |
| [icon-dbd3411d](icons/icon-dbd3411d.svg) | 36x36 | 0 0 24 24 | fill | product-realtime | Stable finals: partials resolve into acc |
| [icon-ddaf5acc](icons/icon-ddaf5acc.svg) | 36x36 | 0 0 24 24 | fill | product-realtime | 103ms partial transcripts: words appear  |
| [copy-sample-response](icons/copy-sample-response.svg) | 14x14 | 0 0 24 24 | stroke | product-stt | Copy sample response |
| [icon-eed8bccb](icons/icon-eed8bccb.svg) | 20x20 | 0 0 20 20 | stroke | use-case-voice-agents | Does Gladia integrate with LiveKit, Pipe / What happens to l |
| [icon](icons/icon-f01ede7a.svg) | 20x20 | 0 0 24 24 | fill | product-stt |  |
| [icon-fbe2ec3d](icons/icon-fbe2ec3d.svg) | 16x16 | 0 0 24 24 | fill | product-realtime | #1 on European business audio and conver / Optimized for EN, |

## Gaps

### The signed-in product

Gladia's product is the app console: API keys, the transcription playground, usage and billing and every surface after sign-in needs an account and was never reached. app.gladia.io / and /signup are the only app surfaces a signed-out visitor sees, and they were measured as forms, never submitted.

### Pages

- **The account.** The app console and every post-login surface (API keys, the transcription playground, usage, billing) was never reached; the / and /signup cards were measured as forms and never submitted; 'Continue with' SSO buttons were never followed.
- **Forms.** The /demo-request form and the pricing calculator's fields were measured at rest and typed into then cleared — nothing was sent; what a submission returns is unverified.
- **Blog posts, docs articles, use-case and competitor pages** are index- or exemplar-level captures; sibling pages share the templates, unmeasured.
- **The /blog stack** is a legacy Webflow build on its own stylesheets — its components were measured at index level only.
- **Mega-menu panels** for Solutions, Developers, Resources and Company were screenshot-captured only; only the Product panel's contents were component-measured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **The pricing calculator** re-prices as inputs change; the hours field was typed then cleared and the range/checkbox controls measured at rest, so alternate calculator prices are uncaptured.
- **The docs theme preference** was never held in the dark position; the docs dark surface is captured as screenshots instead of measured states.

### Themes

Every public www.gladia.io marketing page paints the dark `:root` token layer — an emulated `prefers-color-scheme: dark` pass resolved `:root` identically to light, and no page carries a theme control; dark is simply what the site paints. `body.light-mode` re-points the 19 semantic roles to the light values the /library page paints (the `light` token set), and `.section--white` re-points 5 for white sections inside dark pages. docs.gladia.io is a different stack (Mintlify) with a real light/dark preference; its dark surface is captured in the `docs-*-theme-dark` screenshots.

### Fonts

- **'Suisse Intl'** (book/regular/medium/semibold) carries every heading, control and body on the marketing site; **'Geist Mono'** draws code — self-hosted woff2 under /assets and /css. The /blog Webflow stack and the Mintlify docs ship their own faces. The style guide falls back to system fonts.

### Screenshots

- Testimonial photos, partner logos and marketing imagery in the screenshots are the product's published content; no machine-private data appears on these public pages.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, plan prices, partner names and customer names are the product's content; only frames and components were measured.
