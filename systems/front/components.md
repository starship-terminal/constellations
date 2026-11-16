# Front components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from front.com, app.frontapp.com, help.front.com and dev.frontapp.com on 2026-11-16, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, booked, created or submitted; the demo, signup, signin, help-search and reset forms were never sent; every link, CTA, SSO button and submit was measured, never followed or pressed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (69 components, 164 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/20.8 400, #000000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (160 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture: `light` for every marketing, help and dev page — front.com themes its sections, not the page (the plum [data-theme=theme-dark-violet], theme-white and theme-gray blocks alternate down the same page), and neither the help centre nor the ReadMe portal offered a switch. The app shell does carry a real theme: `signindark-*`, `signupappdark-*`, `forgotdark-*` and `mobile-signindark-*` shots paint app.frontapp.com under its own [data-theme="dark"] (the front-theme-preference localStorage key plus prefers-color-scheme — the product's switch, not an emulated paint). The OneTrust banner and the Qualified 'Quinn' widget are hidden in every shot except `home-light-widget.png`, which shows the vendor surface as shipped — never answered, never engaged. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages bounded at eight chunks with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x) for default shots and 390 wide for stitched `-full` tiles.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu-product](screenshots/home-light-menu-product.png), [menu-resources](screenshots/home-light-menu-resources.png), [menu-solutions](screenshots/home-light-menu-solutions.png), [widget](screenshots/home-light-widget.png) |
| Pricing | `/pricing` | [billed-monthly](screenshots/pricing-light-billed-monthly.png), [default](screenshots/pricing-light-default.png), [faq-open](screenshots/pricing-light-faq-open.png), [full](screenshots/pricing-light-full.png) |
| Product | `/product` | [default](screenshots/product-light-default.png), [full](screenshots/product-light-full.png) |
| Omnichannel inbox | `/product/omnichannel-support-inbox` | [default](screenshots/product-omnichannel-light-default.png), [full](screenshots/product-omnichannel-light-full.png) |
| Front AI | `/product/ai` | [default](screenshots/product-ai-light-default.png), [full](screenshots/product-ai-light-full.png) |
| Customer service | `/customer-service` | [default](screenshots/customer-service-light-default.png), [full](screenshots/customer-service-light-full.png) |
| Customer stories | `/customer-stories` | [default](screenshots/customer-stories-light-default.png), [full](screenshots/customer-stories-light-full.png) |
| A customer story | `/customer-stories/uber-freight` | [default](screenshots/story-light-default.png), [full](screenshots/story-light-full.png) |
| Integrations | `/integrations` | [default](screenshots/integrations-light-default.png), [full](screenshots/integrations-light-full.png) |
| Front vs Intercom | `/compare/front-vs-intercom` | [default](screenshots/compare-light-default.png), [full](screenshots/compare-light-full.png) |
| B2B tech industry | `/industries/b2b-tech` | [default](screenshots/industry-light-default.png), [full](screenshots/industry-light-full.png) |
| Teams: customer service | `/teams/customer-service-support` | [default](screenshots/team-light-default.png), [full](screenshots/team-light-full.png) |
| Resources | `/resources` | [default](screenshots/resources-light-default.png), [full](screenshots/resources-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| A blog article | `/blog/customer-service-automation-ai` | [default](screenshots/article-light-default.png), [full](screenshots/article-light-full.png) |
| Glossary | `/glossary` | [default](screenshots/glossary-light-default.png), [full](screenshots/glossary-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Reviews | `/reviews` | [default](screenshots/reviews-light-default.png), [full](screenshots/reviews-light-full.png) |
| Download | `/download` | [default](screenshots/download-light-default.png), [full](screenshots/download-light-full.png) |
| Security | `/security` | [default](screenshots/security-light-default.png), [full](screenshots/security-light-full.png) |
| Request a demo | `/request-demo` | [default](screenshots/request-demo-light-default.png), [filled](screenshots/request-demo-light-filled.png), [full](screenshots/request-demo-light-full.png) |
| Marketing signup | `/signup` | [default](screenshots/signup-light-default.png), [filled](screenshots/signup-light-filled.png), [full](screenshots/signup-light-full.png) |
| What's new | `/whats-new` | [default](screenshots/whats-new-light-default.png), [full](screenshots/whats-new-light-full.png) |
| Sign in (app shell) | `app.frontapp.com/signin` | [default](screenshots/signin-light-default.png), [filled](screenshots/signin-light-filled.png), [full](screenshots/signin-light-full.png) |
| Sign in, dark theme | `app.frontapp.com/signin` | [default](screenshots/signindark-dark-default.png), [full](screenshots/signindark-dark-full.png) |
| Sign up (app shell) | `app.frontapp.com/signup` | [default](screenshots/signup-app-light-default.png), [full](screenshots/signup-app-light-full.png) |
| Sign up, dark | `app.frontapp.com/signup` | [default](screenshots/signupappdark-dark-default.png) |
| Forgot password | `app.frontapp.com/forgot-password` | [default](screenshots/forgot-light-default.png), [full](screenshots/forgot-light-full.png) |
| Forgot password, dark | `app.frontapp.com/forgot-password` | [default](screenshots/forgotdark-dark-default.png) |
| Help centre | `help.front.com/` | [default](screenshots/help-light-default.png), [full](screenshots/help-light-full.png) |
| A help article | `help.front.com/en/…` | [default](screenshots/help-article-light-default.png), [full](screenshots/help-article-light-full.png) |
| Help: contact us | `help.front.com/en/contact-us` | [default](screenshots/help-contact-light-default.png), [full](screenshots/help-contact-light-full.png) |
| Developer docs | `dev.frontapp.com/docs/welcome` | [default](screenshots/dev-light-default.png), [full-scroll](screenshots/dev-light-full-scroll.png), [full](screenshots/dev-light-full.png) |
| API reference | `dev.frontapp.com/reference/getting-started` | [default](screenshots/dev-ref-light-default.png), [full-scroll](screenshots/dev-ref-light-full-scroll.png), [full](screenshots/dev-ref-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Sign in, phone | `app.frontapp.com/signin` | [dark-default](screenshots/mobile-signin-dark-dark-default.png), [default](screenshots/mobile-signin-light-default.png) |
| Sign in, phone, dark | `app.frontapp.com/signin` | [default](screenshots/mobile-signindark-dark-default.png) |
| Help centre, phone | `help.front.com/` | [default](screenshots/mobile-help-light-default.png), [full](screenshots/mobile-help-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Product mega menu | every page header | clicked the 'Product' trigger (a local UI toggle; keyboard Enter is the fallback) | [home-light-menu-product](screenshots/home-light-menu-product.png), [nav-panel](#mega-menu-panel), [nav-menu-item](#mega-menu-item) |
| Solutions mega menu | every page header | the same activation on 'Solutions' | [home-light-menu-solutions](screenshots/home-light-menu-solutions.png) |
| Resources mega menu | every page header | the same activation on 'Resources' | [home-light-menu-resources](screenshots/home-light-menu-resources.png) |
| Mobile nav overlay | home page, phone width | the burger button's own toggle | [m-drawer](#mobile-nav-overlay), [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |
| Billing switch | /pricing | the 'Billed Annually' switch repaints the per-seat prices — a local UI toggle, toggled once each way | [pricing-light-billed-monthly](screenshots/pricing-light-billed-monthly.png), [billing-toggle](#billing-switch) |
| Pricing FAQ | /pricing | the 'What is a seat?' disclosure's own toggle | [pricing-light-faq-open](screenshots/pricing-light-faq-open.png), [faq-item](#faq-disclosure), [faq-answer](#faq-answer) |
| Quinn widget (vendor) | marketing home | auto-opens on load — shot once as shipped, never opened or typed into | [home-light-widget](screenshots/home-light-widget.png), [quinn-launcher](#quinn-widget-vendor) |
| Demo/signup/auth fields | /request-demo, /signup, app /signin /signup /forgot-password, help search | typed into then cleared — nothing sent | [demo-email](#work-email-field), [app-email](#email-field), [help-search](#search-field) |
| Auth buttons | app /signin /signup /forgot-password | the Continue/SSO/submit buttons were measured in every state, never pressed — nothing was submitted | [app-continue](#continue-button), [app-sso](#sso-button) |
| App dark theme | app /signin /signup /forgot-password | the shell's own switch: front-theme-preference= 'dark' plus prefers-color-scheme — html[data-theme=dark] painted | [signindark-dark-default](screenshots/signindark-dark-default.png), appd-* components below |
| Signed-in product | a Front account | the workspace — inbox, conversations, contacts, settings — needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 23 components were given a real keyboard focus. 14 draw an outline ring: `nav-menu-btn` (1px solid #8034bf `light.button.surface`, offset 2px), `nav-pricing` (1px solid #8034bf `light.button.surface`, offset 2px), `nav-signin` (1px solid #8034bf `light.button.surface`, offset 2px), `nav-demo` (1px solid #ffffff `light.surface.l0`, offset 2px), `nav-try` (1px solid #f8f1fe `light.button.textDefault`, offset 2px), `plan-cta` (1px solid #5b1f76 `light.button.surfaceActive`, offset 2px), `sales-link` (1px solid #ffffff `light.surface.l0`, offset 2px), `faq-item` (1px solid #1c1e20 `core.component.marketing.faq.openColour`, offset 2px), `product-cta` (1px solid #f8f1fe `light.button.textDefault`, offset 2px), `demo-submit` (1px solid #300c41 `violet.surface.l0`, offset 2px), `signup-submit` (1px solid #300c41 `violet.surface.l0`, offset 2px), `m-menu-btn` (1px solid #1c1e20 `core.component.marketing.faq.openColour`, offset 1.98438px), `m-cta` (1px solid #000000, offset 1.98438px), `hero-cta` (1px solid #ffffff `light.surface.l0`, offset 2px). 1 draw a focus ring as a shadow instead: `dev-search`. The other 8 show no measured change: `app-continue`, `app-sso`, `app-forgot`, `appd-continue`, `appd-sso`, `appd-forgot`, `forgot-submit`, `signup-app-submit`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease` | background-color | app-continue, app-sso, appd-continue, appd-sso, forgot-submit, signup-app-submit |
| 0.15s | `cubic-bezier(0.16, 1, 0.3, 1)` | -webkit-box-shadow, box-shadow | dev-search |
| 0.2s | `cubic-bezier(0.55, 0.085, 0.68, 0.53)` | background-color, border-color, color, fill, stroke, text-decoration-color | footer-link |
| 0.4s | `cubic-bezier(0.16, 1, 0.3, 1)` | all, background-color, border-color, color, fill, stroke, text-decoration-color | demo-submit, hero-cta, m-cta, m-menu-btn, nav-demo, nav-menu-btn, nav-pricing, nav-signin and more |
| 0.6s | `cubic-bezier(0.16, 1, 0.3, 1)` | all | m-topbar, mkt-header |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Mega-menu panel](#mega-menu-panel) | 1271 x 419 | 5px solid #e2dcf6 `light.button.surfaceOutlineActive` | 20px | #ffffff `light.surface.l0` | rgba(0, 0, 0, 0.04) 0px 60px 60px 0px, rgba(0, 0, 0, 0.03) 0px 30.375px 26.156px 0px, rgba(0, 0, 0, 0.02) 0px 12px 9.75px 0px, rgba(0, 0, 0, 0.01) 0px 2.625px 3.469px 0px | 32px 8px |
| [Plan card](#plan-card) | 313 x 460 | - | 24px | #ffffff `light.surface.l0` | none | 0 |
| [Site footer](#site-footer) | 1440 x 1481.39 | - | - | transparent | none | 0 |
| [Auth panel](#auth-panel) | 332 x 576.69 | 1px solid rgba(0, 0, 0, 0.08) `help.border.color` | 20px | #ffffff `light.surface.l0` | rgba(0, 0, 0, 0.09) 0px 2px 8px 0px | 48px |
| [Auth panel under [data-theme=dark]](#auth-panel-under-data-themedark) | 332 x 576.69 | 1px solid rgba(255, 255, 255, 0.08) | 20px | #221e29 `dark.color.bg.surface.highlight.default` | rgba(0, 0, 0, 0.09) 0px 2px 8px 0px | 48px |
| [Signup panel](#signup-panel) | 332 x 576.69 | 1px solid rgba(0, 0, 0, 0.08) `help.border.color` | 20px | #ffffff `light.surface.l0` | rgba(0, 0, 0, 0.09) 0px 2px 8px 0px | 48px |
| [Reset panel](#reset-panel) | 332 x 576.69 | 1px solid rgba(0, 0, 0, 0.08) `help.border.color` | 20px | #ffffff `light.surface.l0` | rgba(0, 0, 0, 0.09) 0px 2px 8px 0px | 48px |
| [Category card](#category-card) | 402 x 259 | 1px solid rgba(0, 0, 0, 0.08) `help.border.color` | 24px | #ffffff `light.surface.l0` | rgba(0, 0, 0, 0.08) 0px 1px 9px 0px | 32px |
| [Mobile nav overlay](#mobile-nav-overlay) | 390 x 844 | - | - | #ffffff `light.surface.l0` | none | 96px 0px 120px 0px |

## Components

### Site chrome

The header on every marketing page: the Front wordmark, the Product/Solutions/Resources mega-menu triggers, AI, Customers and Pricing links, Sign in, the bordered 'Request a demo' and the 'Try for free' action; the Product mega menu opens a full-width panel under the bar. The Qualified 'Quinn' vendor widget pins bottom-right — measured at rest, never opened.

#### Site header
The top bar on every marketing page: the Front wordmark, Product/Solutions/Resources mega-menu triggers, AI, Customers, Pricing, Sign in, Request a demo and Try for free. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 80; background transparent; text Suisse Intl 16/40 500, #ffffff `light.surface.l0`; transition all 0.6s cubic-bezier(0.16, 1, 0.3, 1); icon 112 x 26, #ffffff `light.surface.l0`; layers button.block.button 153.0x40.0 rgb(255, 255, 255) 40px; button.block.button 111.0x40.0 rgb(208, 198, 240) 0px 0px 0px 1px inset 40px; button.button.button-size-circle-medium 0.0x0.0 rgb(243, 243, 244) 44px; div.rounded-20.bg-white 26.0x74.0 rgb(255, 255, 255) T:5px rgb(226, 220, 246) / R:5px rgb(226, 220, 246) / B:5px rgb(226, 220, 246) / L:5px rgb(226, 220, 246) rgba(0, 0, 0, 0) 0px 0px 0px 0px, .

Child layers that carry the look: button 153x40 background #ffffff `light.surface.l0` radius 40px; button 111x40 radius 40px shadow #d0c6f0 `violet.button.textTab` 0px 0px 0px 1px inset; button 0x0 background #f3f3f4 `light.button.surfaceDisabled` radius 44px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Front wordmark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 112 x 26; background transparent; text Suisse Intl 14/20 400, #1c1e20 `core.component.marketing.faq.openColour`; icon 112 x 26, #ffffff `light.surface.l0`.

![Logo default](components/crops/mkt-logo-default.png)

#### Mega-menu trigger
The "Product" header button — a local UI toggle whose mega menu mounts under the header; the opened state was measured after its own click (aria-expanded had to stay true). Read as `nav-menu-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 90 x 40; padding 0px 16px; radius 40px; background transparent; text Suisse Intl 16/40 500, #ffffff `light.surface.l0`; transition color 0.4s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), fill 0.4s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) |
| hover | background #5b1f76 `light.button.surfaceActive` |
| focus-visible | outline 1px solid #8034bf `light.button.surface`, offset 2px; layers button.block.button 90.0x40.0 1px solid rgb(128, 52, 191) offset 2px 40px |
| pressed | background #8034bf `light.button.surface` |
| opened | background #5b1f76 `light.button.surfaceActive` |

![Mega-menu trigger default](components/crops/nav-menu-btn-default.png) ![Mega-menu trigger hover](components/crops/nav-menu-btn-hover.png) ![Mega-menu trigger focus-visible](components/crops/nav-menu-btn-focus-visible.png) ![Mega-menu trigger pressed](components/crops/nav-menu-btn-pressed.png) ![Mega-menu trigger opened](components/crops/nav-menu-btn-opened.png)

#### Mega-menu panel
The panel opened by the "Product" trigger (product entries with icons and descriptions); its links were never followed. Read as `nav-panel` on the home page.

**Values (default).** size 1271 x 419; padding 32px 8px; border 5px solid #e2dcf6 `light.button.surfaceOutlineActive`; radius 20px; background #ffffff `light.surface.l0`; shadow rgba(0, 0, 0, 0.04) 0px 60px 60px 0px, rgba(0, 0, 0, 0.03) 0px 30.375px 26.156px 0px, rgba(0, 0, 0, 0.02) 0px 12px 9.75px 0px, rgba(0, 0, 0, 0.01) 0px 2.625px 3.469px 0px; text Suisse Intl 16/20 500, #1c1e20 `core.component.marketing.faq.openColour`; icon 18 x 18, #1c1e20 `core.component.marketing.faq.openColour`.

![Mega-menu panel default](components/crops/nav-panel-default.png)

#### Mega-menu item
A product entry inside the opened mega menu; measured, never followed. Read as `nav-menu-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 64 x 19; background transparent; text Suisse Intl 15/19 400, #1c1e20 `core.component.marketing.faq.openColour`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |

![Mega-menu item default](components/crops/nav-menu-item-default.png) ![Mega-menu item hover](components/crops/nav-menu-item-hover.png)

#### Nav link
The "Pricing" header link; measured, never followed. Read as `nav-pricing` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 84 x 40; padding 0px 16px; radius 40px; background transparent; text Suisse Intl 16/40 500, #ffffff `light.surface.l0`; transition color 0.4s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), fill 0.4s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) |
| hover | background #5b1f76 `light.button.surfaceActive` |
| focus-visible | outline 1px solid #8034bf `light.button.surface`, offset 2px; layers a.block.button 84.0x40.0 1px solid rgb(128, 52, 191) offset 2px 40px |
| pressed | background #8034bf `light.button.surface` |

![Nav link default](components/crops/nav-pricing-default.png) ![Nav link hover](components/crops/nav-pricing-hover.png) ![Nav link focus-visible](components/crops/nav-pricing-focus-visible.png) ![Nav link pressed](components/crops/nav-pricing-pressed.png)

#### Sign-in link
The "Sign in" header link to app.frontapp.com/signin; measured, never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 82 x 40; padding 0px 16px; radius 40px; background transparent; text Suisse Intl 16/40 500, #ffffff `light.surface.l0`; transition color 0.4s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), fill 0.4s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) |
| hover | background #5b1f76 `light.button.surfaceActive` |
| focus-visible | outline 1px solid #8034bf `light.button.surface`, offset 2px; layers a.block.button 82.0x40.0 1px solid rgb(128, 52, 191) offset 2px 40px |
| pressed | background #8034bf `light.button.surface` |

![Sign-in link default](components/crops/nav-signin-default.png) ![Sign-in link hover](components/crops/nav-signin-hover.png) ![Sign-in link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign-in link pressed](components/crops/nav-signin-pressed.png)

#### Request-demo button
The "Request a demo" header action (a bordered secondary button); links to /request-demo, measured never followed. Read as `nav-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 153 x 40; padding 0px 16px; radius 40px; background #ffffff `light.surface.l0`; text Suisse Intl 16/40 500, #300c41 `violet.surface.l0`; transition color 0.4s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), fill 0.4s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) |
| hover | background #e2dcf6 `light.button.surfaceOutlineActive` |
| focus-visible | outline 1px solid #ffffff `light.surface.l0`, offset 2px |
| pressed | background #e2dcf6 `light.button.surfaceOutlineActive` |

![Request-demo button default](components/crops/nav-demo-default.png) ![Request-demo button hover](components/crops/nav-demo-hover.png) ![Request-demo button focus-visible](components/crops/nav-demo-focus-visible.png) ![Request-demo button pressed](components/crops/nav-demo-pressed.png)

#### Try-free button
The "Try for free" header action; links to /signup, measured never followed. Read as `nav-try` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 111 x 40; padding 0px 16px; radius 40px; background transparent; shadow #d0c6f0 0px 0px 0px 1px inset; text Suisse Intl 16/40 500, #d0c6f0 `violet.button.textTab`; transition color 0.4s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), fill 0.4s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1); layers button.block.button 111.0x40.0 rgb(208, 198, 240) 0px 0px 0px 1px inset 40px |
| hover | background rgba(248, 241, 254, 0.2); shadow #f8f1fe 0px 0px 0px 1px inset; layers none |
| focus-visible | outline 1px solid #f8f1fe `light.button.textDefault`, offset 2px; layers button.block.button 111.0x40.0 rgb(208, 198, 240) 0px 0px 0px 1px inset 1px solid rgb(248, 241, 254) offset 2px 40px |
| pressed | background #f8f1fe `light.button.textDefault`; shadow #f8f1fe 0px 0px 0px 1px inset; text Suisse Intl 16/40 500, #300c41 `violet.surface.l0`; layers none |

![Try-free button default](components/crops/nav-try-default.png) ![Try-free button hover](components/crops/nav-try-hover.png) ![Try-free button focus-visible](components/crops/nav-try-focus-visible.png) ![Try-free button pressed](components/crops/nav-try-pressed.png)

#### Quinn widget (vendor)
The Qualified "Quinn" chat widget host pinned bottom-right — a vendor surface, measured at rest and never opened or typed into. Read as `quinn-launcher` on the home page.

**Values (default).** size 1440 x 900; background transparent; text Suisse Intl 14/20 400, #1c1e20 `core.component.marketing.faq.openColour`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Home

The home hero on the plum [data-theme=theme-dark-violet] field: the display1 masthead 'All your teams. All your AI agents. One place to …', the sub copy, the violet primary 'Try for free' and secondary 'Request a demo', and the themed sections below (theme-white, theme-gray).

#### Hero headline
"All your teams. All your AI agents. One place to …" — the display1 masthead. Read as `hero-h1` on the home page.

**Values (default).** size 840 x 104; background transparent; text Suisse Intl 43/52 500, #f8f1fe `light.button.textDefault`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero subcopy
The paragraph under the hero headline (text-p1). Read as `hero-sub` on the home page.

**Values (default).** size 840 x 56; background transparent; text Suisse Intl 20/28 400, #e2dcf6 `light.button.surfaceOutlineActive`.

![Hero subcopy default](components/crops/hero-sub-default.png)

#### Section heading
The first h2 section heading below the hero. Read as `section-heading` on the home page.

**Values (default).** size 840 x 72; background transparent; text Suisse Intl 30/36 500, #0d1d39 `light.button.textInverted`.

![Section heading default](components/crops/section-heading-default.png)

#### Plum section
A section themed [data-theme=theme-dark-violet] — the marketing site's signature dark-plum surface (surface-l0 #300c41, text-primary #f8f1fe). Read as `dark-violet-section` on the home page.

**Values (default).** size 1440 x 952; background transparent; text Suisse Intl 43/52 500, #f8f1fe `light.button.textDefault`; layers div.surface-l0.-mt-header-height-mobile 1440.0x952.0 rgb(48, 12, 65); button.transition-colors.duration-400 140.0x48.0 rgb(222, 233, 72) 64px.

Child layers that carry the look: div 1440x952 background #300c41 `violet.surface.l0`; button 140x48 background #dee948 `light.surface.highlight` radius 64px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Gray section
A section themed [data-theme=theme-gray]. Read as `gray-section` on the home page.

**Values (default).** size 1440 x 404; background transparent; text Suisse Intl 25/30 500, #0d1d39 `light.button.textInverted`; icon 90 x 23, #1c1e20 `core.component.marketing.faq.openColour`; layers div.surface-l0.flex 1440.0x404.0 rgb(243, 243, 244); div.surface-l1.relative 160.0x94.0 rgb(255, 255, 255) 8px; div.surface-l1.relative 160.0x94.0 rgb(255, 255, 255) 8px; div.surface-l1.relative 215.0x200.0 rgb(255, 255, 255) 8px; span.surface-l2.rounded-full 24.0x24.0 rgb(243, 243, 244) 100%; div.surface-l1.relative 160.0x94.0 rgb(255, 255, 255) 8px.

Child layers that carry the look: div 1440x404 background #f3f3f4 `light.button.surfaceDisabled`; div 160x94 background #ffffff `light.surface.l0` radius 8px; div 160x94 background #ffffff `light.surface.l0` radius 8px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Product headline
The /product masthead. Read as `product-h1` on the product page.

**Values (default).** size 1272 x 136; background transparent; text Suisse Intl 62/68 500, #f8f1fe `light.button.textDefault`.

![Product headline default](components/crops/product-h1-default.png)

#### Product CTA
The primary action on the product page; measured never followed. Read as `product-cta` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 111 x 40; padding 0px 16px; radius 40px; background transparent; shadow #d0c6f0 0px 0px 0px 1px inset; text Suisse Intl 16/40 500, #d0c6f0 `violet.button.textTab`; transition color 0.4s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), fill 0.4s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1); layers button.block.button 111.0x40.0 rgb(208, 198, 240) 0px 0px 0px 1px inset 40px |
| hover | background rgba(248, 241, 254, 0.2); shadow #f8f1fe 0px 0px 0px 1px inset; layers none |
| focus-visible | outline 1px solid #f8f1fe `light.button.textDefault`, offset 2px; layers button.block.button 111.0x40.0 rgb(208, 198, 240) 0px 0px 0px 1px inset 1px solid rgb(248, 241, 254) offset 2px 40px |
| pressed | background #f8f1fe `light.button.textDefault`; shadow #f8f1fe 0px 0px 0px 1px inset; text Suisse Intl 16/40 500, #300c41 `violet.surface.l0`; layers none |

![Product CTA default](components/crops/product-cta-default.png) ![Product CTA hover](components/crops/product-cta-hover.png) ![Product CTA focus-visible](components/crops/product-cta-focus-visible.png) ![Product CTA pressed](components/crops/product-cta-pressed.png)

#### Hero CTA
The "Request demo" button under the hero copy — the hero's single CTA; links to /request-demo, measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 140 x 48; padding 12px 16px; radius 64px; background #dee948 `light.surface.highlight`; text Suisse Intl 16/24 500, #0d1d39 `light.button.textInverted`; transition color 0.4s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), fill 0.4s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) |
| hover | background #d6d943 `core.component.marketing.button.primary.bgHover` |
| focus-visible | outline 1px solid #ffffff `light.surface.l0`, offset 2px |
| pressed | background #d3d140 `violet.button.surfaceActive` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Customer-story card
A customer-outcome stat card on the product page (rounded-20, the grid cells that link into customer stories); measured, never followed. Read as `feature-card` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 312 x 358; padding 8px; radius 20px; background rgba(255, 255, 255, 0) `app.color.bg.fill.secondary.default`; text Suisse Intl 62/68 500, #001b38 `core.froyo.ramp.dark.blue.1000`; icon 14 x 14, #001b38 `core.froyo.ramp.dark.blue.1000` |
| hover | background #d4b5f4 |

![Customer-story card default](components/crops/feature-card-default.png) ![Customer-story card hover](components/crops/feature-card-hover.png)

### Pricing

The /pricing surface: 'PRICING PLANS' kicker, the 'Build the best CX' display, the 'Billed Annually / SAVE 24%' switch that repaints the per-seat prices (a local UI toggle), the plan cards with their 'Try for Free' actions, 'Talk to sales', and the FAQ disclosures.

#### Pricing heading
The first heading on /pricing (the page carries no h1; the first h2 is measured instead). Read as `pricing-h1` on the pricing page.

**Values (default).** size 496.89 x 52; background transparent; text Suisse Intl 42/52 500, #0d1d39 `light.button.textInverted`.

![Pricing heading default](components/crops/pricing-h1-default.png)

#### Billing switch
The "Billed Annually"/"SAVE 24%" switch — a local UI toggle that repaints the plan prices; the opened state is the monthly-billed side, toggled and restored. Read as `billing-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 66 x 36; background transparent; text Suisse Intl 14/20 400, #1c1e20 `core.component.marketing.faq.openColour`; layers div.h-3.rounded-[8px] 66.0x36.0 rgb(128, 52, 191) 8px; div.absolute.w-[24px] 24.0x24.0 rgb(255, 255, 255) 4px |
| opened | layers div.h-3.rounded-[8px] 66.0x36.0 rgb(208, 198, 240) 8px; div.absolute.w-[24px] 24.0x24.0 rgb(255, 255, 255) 4px |

Child layers that carry the look: div 66x36 background #8034bf `light.button.surface` radius 8px; div 24x24 background #ffffff `light.surface.l0` radius 4px.

![Billing switch default](components/crops/billing-toggle-default.png) ![Billing switch opened](components/crops/billing-toggle-opened.png)

#### Plan card
A pricing tier card (name, price per seat/month, feature list, CTA) — the Starter column of the plan grid. Read as `plan-card` on the pricing page.

**Values (default).** size 313 x 460; radius 24px; background #ffffff `light.surface.l0`; text Suisse Intl 20/28 500, #0d1d39 `light.button.textInverted`; icon 12 x 12, #1c1e20 `core.component.marketing.faq.openColour`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan CTA
A plan card's "Try for Free" action (the first tier column's button); links to /signup, measured never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 265 x 40; padding 0px 16px; radius 40px; background transparent; shadow #5b1f76 0px 0px 0px 1px inset; text Suisse Intl 16/40 500, #5b1f76 `light.button.surfaceActive`; transition color 0.4s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), fill 0.4s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1); layers button.block.w-full 265.0x40.0 rgb(91, 31, 118) 0px 0px 0px 1px inset 40px |
| hover | background rgba(91, 31, 118, 0.1); layers none |
| focus-visible | outline 1px solid #5b1f76 `light.button.surfaceActive`, offset 2px; layers button.block.w-full 265.0x40.0 rgb(91, 31, 118) 0px 0px 0px 1px inset 1px solid rgb(91, 31, 118) offset 2px 40px |
| pressed | background #5b1f76 `light.button.surfaceActive`; text Suisse Intl 16/40 500, #f8f1fe `light.button.textDefault`; layers none |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Talk-to-sales link
The "Talk to sales" action in the pricing hero; links to /request-demo, measured never followed. Read as `sales-link` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 121.56 x 26; background transparent; text Suisse Intl 17/26 500, #ffffff `light.surface.l0` |
| focus-visible | outline 1px solid #ffffff `light.surface.l0`, offset 2px; layers button.flex.font-500 121.6x26.0 1px solid rgb(255, 255, 255) offset 2px |

![Talk-to-sales link default](components/crops/sales-link-default.png) ![Talk-to-sales link hover](components/crops/sales-link-hover.png) ![Talk-to-sales link focus-visible](components/crops/sales-link-focus-visible.png) ![Talk-to-sales link pressed](components/crops/sales-link-pressed.png)

#### FAQ disclosure
A "Frequently asked questions" disclosure button ("What is a seat?") — a local UI toggle whose answer mounts below; opened by its own click, left open for the shot. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 872 x 100; padding 32px 24px; background transparent; text Suisse Intl 30/36 500, #000000; icon 32 x 32, #1c1e20 `core.component.marketing.faq.openColour` |
| focus-visible | outline 1px solid #1c1e20 `core.component.marketing.faq.openColour`, offset 2px; layers button.w-full.flex 872.0x100.0 1px solid rgb(28, 30, 32) offset 2px |

![FAQ disclosure default](components/crops/faq-item-default.png) ![FAQ disclosure hover](components/crops/faq-item-hover.png) ![FAQ disclosure focus-visible](components/crops/faq-item-focus-visible.png) ![FAQ disclosure pressed](components/crops/faq-item-pressed.png) ![FAQ disclosure opened](components/crops/faq-item-opened.png)

#### FAQ answer
The answer text revealed by the FAQ disclosure. Read as `faq-answer` on the pricing page.

**Values (default).** size 824 x 28; background transparent; text Suisse Intl 20/28 400, #7c8088 `core.palette.gray.600`.

![FAQ answer default](components/crops/faq-answer-default.png)

### Demo and signup forms

The /request-demo and marketing /signup forms — HubSpot-powered fields and their submit buttons. Fields were typed into then cleared; the submits were measured in every state, never pressed.

#### Demo heading
The first heading on /request-demo (no h1 ships; the first h2 is measured). Read as `demo-h1` on the request-demo page.

**Values (default).** size 507.84 x 84; background transparent; text Suisse Works 36/42 500, #0d1d39 `light.button.textInverted`.

![Demo heading default](components/crops/demo-h1-default.png)

#### Work email field
The work-email input on the demo form; focused and typed into then cleared — the form was never submitted. Read as `demo-email` on the request-demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 576 x 48; padding 12px 16px; radius 6px; background #f3f3f4 `light.button.surfaceDisabled`; outline 2px solid transparent, offset 2px; text Suisse Intl 16/24 400, #0d1d39 `light.button.textInverted`; placeholder #8e929b `light.text.primaryInactive` |
| focused, filled | shadow #ffffff 0px 0px 0px 0px, #dee948 0px 0px 0px 2px; outline none |

![Work email field default](components/crops/demo-email-default.png) ![Work email field focused](components/crops/demo-email-focused.png) ![Work email field filled](components/crops/demo-email-filled.png)

#### Demo submit
The demo form's submit button; its states were measured but the button was never clicked — the form was never sent. Read as `demo-submit` on the request-demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 576 x 48; padding 12px 16px; radius 64px; background #f3f3f4 `light.button.surfaceDisabled`; text Suisse Intl 16/24 500, #caccd0 `light.button.textDisabled`; transition color 0.4s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), fill 0.4s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) |
| focus-visible | outline 1px solid #300c41 `violet.surface.l0`, offset 2px |

![Demo submit default](components/crops/demo-submit-default.png) ![Demo submit hover](components/crops/demo-submit-hover.png) ![Demo submit focus-visible](components/crops/demo-submit-focus-visible.png) ![Demo submit pressed](components/crops/demo-submit-pressed.png)

#### Signup headline
The marketing /signup masthead. Read as `signup-h1` on the marketing signup page.

**Values (default).** size 480 x 30; background transparent; text Suisse Intl 25/30 500, #0d1d39 `light.button.textInverted`.

![Signup headline default](components/crops/signup-h1-default.png)

#### Signup field
The first field on the marketing signup form; focused and typed into then cleared — the form was never submitted. Read as `signup-field` on the marketing signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 480 x 48; padding 12px 16px; radius 6px; background #f3f3f4 `light.button.surfaceDisabled`; outline 2px solid transparent, offset 2px; text Suisse Intl 16/24 400, #0d1d39 `light.button.textInverted`; placeholder #8e929b `light.text.primaryInactive` |
| focused, filled | shadow #ffffff 0px 0px 0px 0px, #dee948 0px 0px 0px 2px; outline none |

![Signup field default](components/crops/signup-field-default.png) ![Signup field focused](components/crops/signup-field-focused.png) ![Signup field filled](components/crops/signup-field-filled.png)

#### Signup submit
The marketing signup form's submit button (the rounded-[64px] "Submit" under the e-mail field); measured, never pressed. Read as `signup-submit` on the marketing signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 480 x 48; padding 12px 16px; radius 64px; background #f3f3f4 `light.button.surfaceDisabled`; text Suisse Intl 16/24 500, #caccd0 `light.button.textDisabled`; transition color 0.4s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), fill 0.4s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.4s cubic-bezier(0.16, 1, 0.3, 1) |
| focus-visible | outline 1px solid #300c41 `violet.surface.l0`, offset 2px |

![Signup submit default](components/crops/signup-submit-default.png) ![Signup submit hover](components/crops/signup-submit-hover.png) ![Signup submit focus-visible](components/crops/signup-submit-focus-visible.png) ![Signup submit pressed](components/crops/signup-submit-pressed.png)

#### Company-size select
The company-size select on the demo form; focused, never changed or submitted. Read as `demo-field` on the request-demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 576 x 48; padding 12px 48px 12px 16px; radius 6px; background #f3f3f4 `light.button.surfaceDisabled`; outline 2px solid transparent, offset 2px; text Suisse Intl 16/24 400, #0d1d39 `light.button.textInverted` |
| focused | shadow #ffffff 0px 0px 0px 0px, #dee948 0px 0px 0px 2px |

![Company-size select default](components/crops/demo-field-default.png) ![Company-size select focused](components/crops/demo-field-focused.png)

### Auth shell (app.frontapp.com)

app.frontapp.com /signin, /signup and /forgot-password — the product SPA's auth cards on the real --color-* token layer (Indivisible, the 'Froyo' design system), painted light and under the shell's own [data-theme=dark] (the front-theme-preference localStorage key plus prefers-color-scheme). Fields were typed into then cleared; Continue, the SSO buttons and the submits were measured, never pressed.

#### Auth panel
The sign-in card on app.frontapp.com — the elevated panel holding the e-mail field, Continue, the SSO buttons and the legal links. Read as `app-panel` on the signin page.

**Values (default).** size 332 x 576.69; padding 48px; border 1px solid rgba(0, 0, 0, 0.08) `help.border.color`; radius 20px; background #ffffff `light.surface.l0`; shadow rgba(0, 0, 0, 0.09) 0px 2px 8px 0px; text system-ui 14/20 700, #ffffff `light.surface.l0`; icon 112 x 26.69, #15131b `app.color.bg.base.inverse`.

![Auth panel default](components/crops/app-panel-default.png)

#### Email field
The e-mail input on the sign-in form; focused and typed into then cleared — Enter was never pressed and nothing was submitted. Read as `app-email` on the signin page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 210 x 20; background transparent; text Arial 14/20 400, #15131b `app.color.bg.base.inverse`; placeholder #a9abb2 `app.color.icon.disabled` |
| filled | size 186 x 20 |

![Email field default](components/crops/app-email-default.png) ![Email field focused](components/crops/app-email-focused.png) ![Email field filled](components/crops/app-email-filled.png)

#### Continue button
The sign-in form's primary button (the --color-bg-fill-brand fill); measured, never pressed. Read as `app-continue` on the signin page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 234 x 38; padding 0px 12px; radius 8px; background #6257f4 `app.color.accent.blue.highlight`; text system-ui 14/20 700, #ffffff `light.surface.l0`; transition background-color 0.1s ease |
| hover | background #584def `app.color.accent.blue.text.primary` |
| pressed | background #3c3faa `app.color.bg.fill.primary.pressed` |

![Continue button default](components/crops/app-continue-default.png) ![Continue button hover](components/crops/app-continue-hover.png) ![Continue button focus-visible](components/crops/app-continue-focus-visible.png) ![Continue button pressed](components/crops/app-continue-pressed.png)

#### SSO button
A single-sign-on button on the auth shell; measured, never pressed. Read as `app-sso` on the signin page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 234 x 38; padding 0px 12px; border 1px solid #d8d6db `app.color.border.secondary`; radius 8px; background rgba(255, 255, 255, 0) `app.color.bg.fill.secondary.default`; text system-ui 14/20 500, #15131b `app.color.bg.base.inverse`; transition background-color 0.1s ease |
| hover | background rgba(0, 0, 0, 0.05) `help.article.bg.color` |
| pressed | background rgba(0, 0, 0, 0.08) `help.border.color` |

![SSO button default](components/crops/app-sso-default.png) ![SSO button hover](components/crops/app-sso-hover.png) ![SSO button focus-visible](components/crops/app-sso-focus-visible.png) ![SSO button pressed](components/crops/app-sso-pressed.png)

#### Forgot link
The "Forgot password" link to /forgot-password; measured, never followed. Read as `app-forgot` on the signin page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 234 x 16; background transparent; text system-ui 12/16 600, #584def `app.color.accent.blue.text.primary` |
| hover, pressed | text system-ui 12/16 600, #3c3faa `app.color.bg.fill.primary.pressed` |

![Forgot link default](components/crops/app-forgot-default.png) ![Forgot link hover](components/crops/app-forgot-hover.png) ![Forgot link focus-visible](components/crops/app-forgot-focus-visible.png) ![Forgot link pressed](components/crops/app-forgot-pressed.png)

#### Auth panel under [data-theme=dark]
The sign-in card on app.frontapp.com under [data-theme=dark] — the elevated panel holding the e-mail field, Continue, the SSO buttons and the legal links. Read as `appd-panel` on the signin (dark) page.

**Values (default).** size 332 x 576.69; padding 48px; border 1px solid rgba(255, 255, 255, 0.08); radius 20px; background #221e29 `dark.color.bg.surface.highlight.default`; shadow rgba(0, 0, 0, 0.09) 0px 2px 8px 0px; text system-ui 14/20 700, #ffffff `light.surface.l0`; icon 112 x 26.69, #f4f2f8 `app.color.bg.base.secondary`.

![Auth panel under [data-theme=dark] default](components/crops/appd-panel-default.png)

#### Email field under [data-theme=dark]
The e-mail input on the sign-in form under [data-theme=dark]; focused and typed into then cleared — Enter was never pressed and nothing was submitted. Read as `appd-email` on the signin (dark) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 210 x 20; background transparent; text Arial 14/20 400, #f4f2f8 `app.color.bg.base.secondary`; placeholder #656972 `app.color.icon.secondary` |
| filled | size 186 x 20 |

![Email field under [data-theme=dark] default](components/crops/appd-email-default.png) ![Email field under [data-theme=dark] focused](components/crops/appd-email-focused.png) ![Email field under [data-theme=dark] filled](components/crops/appd-email-filled.png)

#### Continue button under [data-theme=dark]
The sign-in form's primary button under [data-theme=dark] (the --color-bg-fill-brand fill); measured, never pressed. Read as `appd-continue` on the signin (dark) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 234 x 38; padding 0px 12px; radius 8px; background #584def `app.color.accent.blue.text.primary`; text system-ui 14/20 700, #ffffff `light.surface.l0`; transition background-color 0.1s ease |
| hover | background #6257f4 `app.color.accent.blue.highlight` |
| pressed | background #7989f7 `app.color.accent.blue.text.secondary` |

![Continue button under [data-theme=dark] default](components/crops/appd-continue-default.png) ![Continue button under [data-theme=dark] hover](components/crops/appd-continue-hover.png) ![Continue button under [data-theme=dark] focus-visible](components/crops/appd-continue-focus-visible.png) ![Continue button under [data-theme=dark] pressed](components/crops/appd-continue-pressed.png)

#### SSO button under [data-theme=dark]
A single-sign-on button on the auth shell under [data-theme=dark]; measured, never pressed. Read as `appd-sso` on the signin (dark) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 234 x 38; padding 0px 12px; border 1px solid #504c57 `app.color.accent.gray.highlight`; radius 8px; background rgba(255, 255, 255, 0) `app.color.bg.fill.secondary.default`; text system-ui 14/20 500, #f4f2f8 `app.color.bg.base.secondary`; transition background-color 0.1s ease |
| hover | background rgba(255, 255, 255, 0.05) |
| pressed | background rgba(255, 255, 255, 0.08) |

![SSO button under [data-theme=dark] default](components/crops/appd-sso-default.png) ![SSO button under [data-theme=dark] hover](components/crops/appd-sso-hover.png) ![SSO button under [data-theme=dark] focus-visible](components/crops/appd-sso-focus-visible.png) ![SSO button under [data-theme=dark] pressed](components/crops/appd-sso-pressed.png)

#### Forgot link under [data-theme=dark]
The "Forgot password" link to /forgot-password; measured, never followed. Read as `appd-forgot` on the signin (dark) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 234 x 16; background transparent; text system-ui 12/16 600, #7989f7 `app.color.accent.blue.text.secondary` |
| hover, pressed | text system-ui 12/16 600, #6257f4 `app.color.accent.blue.highlight` |

![Forgot link under [data-theme=dark] default](components/crops/appd-forgot-default.png) ![Forgot link under [data-theme=dark] hover](components/crops/appd-forgot-hover.png) ![Forgot link under [data-theme=dark] focus-visible](components/crops/appd-forgot-focus-visible.png) ![Forgot link under [data-theme=dark] pressed](components/crops/appd-forgot-pressed.png)

#### Signup panel
The create-account card on app.frontapp.com/signup. Read as `signup-panel` on the product signup page.

**Values (default).** size 332 x 576.69; padding 48px; border 1px solid rgba(0, 0, 0, 0.08) `help.border.color`; radius 20px; background #ffffff `light.surface.l0`; shadow rgba(0, 0, 0, 0.09) 0px 2px 8px 0px; text system-ui 14/20 700, #ffffff `light.surface.l0`; icon 112 x 26.69, #15131b `app.color.bg.base.inverse`.

![Signup panel default](components/crops/signup-panel-default.png)

#### Signup email field
The e-mail input on the product signup form; typed into then cleared — never submitted. Read as `signup-email` on the product signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 210 x 20; background transparent; text Arial 14/20 400, #15131b `app.color.bg.base.inverse`; placeholder #a9abb2 `app.color.icon.disabled` |
| filled | size 186 x 20 |

![Signup email field default](components/crops/signup-email-default.png) ![Signup email field focused](components/crops/signup-email-focused.png) ![Signup email field filled](components/crops/signup-email-filled.png)

#### Reset panel
The reset-password card on app.frontapp.com/forgot-password. Read as `forgot-panel` on the forgot-password page.

**Values (default).** size 332 x 576.69; padding 48px; border 1px solid rgba(0, 0, 0, 0.08) `help.border.color`; radius 20px; background #ffffff `light.surface.l0`; shadow rgba(0, 0, 0, 0.09) 0px 2px 8px 0px; text system-ui 14/20 700, #ffffff `light.surface.l0`; icon 112 x 26.69, #15131b `app.color.bg.base.inverse`.

![Reset panel default](components/crops/forgot-panel-default.png)

#### Reset email field
The e-mail input on the reset form; typed into then cleared — never submitted. Read as `forgot-email` on the forgot-password page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 210 x 20; background transparent; text Arial 14/20 400, #15131b `app.color.bg.base.inverse`; placeholder #a9abb2 `app.color.icon.disabled` |
| filled | size 186 x 20 |

![Reset email field default](components/crops/forgot-email-default.png) ![Reset email field focused](components/crops/forgot-email-focused.png) ![Reset email field filled](components/crops/forgot-email-filled.png)

#### Reset submit
The submit on /forgot-password — the route paints the same auth card as /signin, so no dedicated reset button exists signed out; measured, never pressed. Read as `forgot-submit` on the forgot-password page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 234 x 38; padding 0px 12px; radius 8px; background #6257f4 `app.color.accent.blue.highlight`; text system-ui 14/20 700, #ffffff `light.surface.l0`; transition background-color 0.1s ease |
| hover | background #584def `app.color.accent.blue.text.primary` |
| pressed | background #3c3faa `app.color.bg.fill.primary.pressed` |

![Reset submit default](components/crops/forgot-submit-default.png) ![Reset submit hover](components/crops/forgot-submit-hover.png) ![Reset submit focus-visible](components/crops/forgot-submit-focus-visible.png) ![Reset submit pressed](components/crops/forgot-submit-pressed.png)

#### Signup submit (app)
The submit on app.frontapp.com/signup — the route paints the same auth card as /signin (email, password, "Sign in"); measured, never pressed. Read as `signup-app-submit` on the product signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 234 x 38; padding 0px 12px; radius 8px; background #6257f4 `app.color.accent.blue.highlight`; text system-ui 14/20 700, #ffffff `light.surface.l0`; transition background-color 0.1s ease |
| hover | background #584def `app.color.accent.blue.text.primary` |
| pressed | background #3c3faa `app.color.bg.fill.primary.pressed` |

![Signup submit (app) default](components/crops/signup-app-submit-default.png) ![Signup submit (app) hover](components/crops/signup-app-submit-hover.png) ![Signup submit (app) focus-visible](components/crops/signup-app-submit-focus-visible.png) ![Signup submit (app) pressed](components/crops/signup-app-submit-pressed.png)

### Help centre (help.front.com)

help.front.com — Front's own Knowledge Base product serving the help centre: its own header, the search field (typed into then cleared, never submitted), category cards and article pages on the --article-*/--gray-shade* :root layer. Front embeds its Companion messenger here (companion.frontapp.com — the Froyo token sheet's home).

#### Help header
The help centre's own header (Front's Knowledge Base product): the mark, the nav and the search. Read as `help-header` on the help centre home page.

**Values (default).** size 1440 x 306; background #f8f1fe `light.button.textDefault`; text CustomFont 18/21.6 600, #3e3e40 `help.article.code.bg`.

![Help header default](components/crops/help-header-default.png)

#### Search field
The help centre's search input; focused and typed into then cleared — no search was submitted. Read as `help-search` on the help centre home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 408 x 40; background transparent; text CustomFont 14/normal 400, #3e3e40 `help.article.code.bg`; placeholder #3e3e40 `help.article.code.bg` |
| focused, filled | size 404 x 40; text CustomFont 14/normal 400, #19191a `help.gray.shade90`; placeholder #19191a `help.gray.shade90` |

![Search field default](components/crops/help-search-default.png) ![Search field focused](components/crops/help-search-focused.png) ![Search field filled](components/crops/help-search-filled.png)

#### Category card
A help-category card (kb-category-card) on the help home; measured, never followed. Read as `help-card` on the help centre home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 402 x 259; padding 32px; border 1px solid rgba(0, 0, 0, 0.08) `help.border.color`; radius 24px; background #ffffff `light.surface.l0`; shadow rgba(0, 0, 0, 0.08) 0px 1px 9px 0px; text CustomFont 18/24 600, #19191a `help.gray.shade90`; icon 32 x 32, #803fbf `help.secondary.color` |
| hover | background #f5f5f5 `help.primary.bg.color.active` |

![Category card default](components/crops/help-card-default.png) ![Category card hover](components/crops/help-card-hover.png)

#### Article headline
A help article headline inside Front's Knowledge Base product. Read as `helpa-h1` on the help article page.

**Values (default).** size 630 x 32; background transparent; text CustomFont 24/32 800, #19191a `help.gray.shade90`.

![Article headline default](components/crops/helpa-h1-default.png)

#### Article body
The article body column (--article-* vars paint the prose). Read as `helpa-body` on the help article page.

**Values (default).** size 840 x 5285.33; padding 80px 104px; border 1px solid rgba(0, 0, 0, 0.08) `help.border.color`; radius 24px; background #ffffff `light.surface.l0`; shadow rgba(0, 0, 0, 0.08) 0px 1px 9px 0px; text CustomFont 24/32 800, #19191a `help.gray.shade90`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Breadcrumb link
A breadcrumb or section link on the article page; measured, never followed. Read as `helpa-crumb` on the help article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 145 x 21.59; background transparent; text CustomFont 18/21.6 600, #3e3e40 `help.article.code.bg` |

![Breadcrumb link default](components/crops/helpa-crumb-default.png) ![Breadcrumb link hover](components/crops/helpa-crumb-hover.png)

#### Category card (second)
A second help-category card on the help home — the home lists categories, not article links; measured, never followed. Read as `help-card-2` on the help centre home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 402 x 259; padding 32px; border 1px solid rgba(0, 0, 0, 0.08) `help.border.color`; radius 24px; background #ffffff `light.surface.l0`; shadow rgba(0, 0, 0, 0.08) 0px 1px 9px 0px; text CustomFont 18/24 600, #19191a `help.gray.shade90`; icon 32 x 32, #803fbf `help.secondary.color` |
| hover | background #f5f5f5 `help.primary.bg.color.active` |

![Category card (second) default](components/crops/help-card-2-default.png) ![Category card (second) hover](components/crops/help-card-2-hover.png)

### Developer portal (dev.frontapp.com)

dev.frontapp.com — the developer documentation on the ReadMe vendor platform (readme.io) skinned to Front: its header, search trigger, sidebar tree and code blocks, plus the same Companion embed. Vendor platform; kept as measured evidence, not a token set.

#### Dev header
The developer portal's header — the ReadMe vendor platform skinned to Front. Read as `dev-header` on the developer docs page.

**Values (default).** size 1430 x 94; background #300c41 `violet.surface.l0`; shadow rgba(0, 0, 0, 0.1) 0px 1px 0px 0px; text Twemoji Country Flags 14/normal 500, #300c41 `violet.surface.l0`.

![Dev header default](components/crops/dev-header-default.png)

#### Search trigger
The portal's search control — a local UI toggle for the search overlay; measured at rest, never opened. Read as `dev-search` on the developer docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 150 x 32; padding 0px 8px; radius 6px; background #ffffff `light.surface.l0`; shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 1px; text Twemoji Country Flags 14/32 400, #666b79; transition box-shadow 0.15s cubic-bezier(0.16, 1, 0.3, 1), -webkit-box-shadow 0.15s cubic-bezier(0.16, 1, 0.3, 1) |
| focus-visible | shadow rgba(255, 255, 255, 0.75) 0px 0px 0px 1px, rgba(255, 255, 255, 0.25) 0px 0px 0px 4px |

![Search trigger default](components/crops/dev-search-default.png) ![Search trigger hover](components/crops/dev-search-hover.png) ![Search trigger focus-visible](components/crops/dev-search-focus-visible.png) ![Search trigger pressed](components/crops/dev-search-pressed.png)

#### Doc headline
A docs headline on dev.frontapp.com (ReadMe). Read as `dev-h1` on the developer docs page.

**Values (default).** size 1078 x 39.84; background transparent; text Twemoji Country Flags 31/39.85 600, #32343a `core.component.dev.code.text`.

![Doc headline default](components/crops/dev-h1-default.png)

#### Sidebar link
A sidebar navigation link in the docs tree; measured, never followed. Read as `dev-side-link` on the developer docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 251 x 32; padding 6.006px 5px 6.006px 10px; radius 8px; background rgba(0, 144, 218, 0.09); text Twemoji Country Flags 14/20.00 450, #0090da `core.component.dev.sidebar.link` |

![Sidebar link default](components/crops/dev-side-link-default.png) ![Sidebar link hover](components/crops/dev-side-link-hover.png)

#### Reference headline
An API-reference page headline on the ReadMe stack. Read as `devref-h1` on the developer reference page.

**Values (default).** size 239.92 x 39.84; background transparent; text Twemoji Country Flags 31/39.85 600, #32343a `core.component.dev.code.text`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Code block
A code block on the reference page. Read as `devref-code` on the developer reference page.

**Values (default).** size 430 x 45; border B: 1px solid rgba(255, 255, 255, 0.05); background transparent; shadow rgba(0, 0, 0, 0.1) 0px -1px 0px 0px inset; text SF Mono 12/18 400, #bebcd7; layers pre.CodeSnippet 430.0x45.0 B:1px rgba(255, 255, 255, 0.05) rgba(0, 0, 0, 0.1) 0px -1px 0px 0px inset; div.CodeMirror-gutter-filler 0.0x0.0 rgb(255, 255, 255); div.CodeMirror-sizer 446.0x44.0 R:50px rgba(0, 0, 0, 0).

![Code block default](components/crops/devref-code-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the header with the burger ('Open menu'), the full-viewport nav overlay, the hero and the CTAs.

#### Mobile top bar
The phone header at 390 wide: the wordmark, the CTAs and the burger. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 390 x 96; background transparent; text Suisse Intl 14/20 400, #1c1e20 `core.component.marketing.faq.openColour`; transition all 0.6s cubic-bezier(0.16, 1, 0.3, 1); icon 112 x 26, #ffffff `light.surface.l0`; layers button.block.button 0.0x0.0 rgb(255, 255, 255) 40px; button.block.button 0.0x0.0 rgb(208, 198, 240) 0px 0px 0px 1px inset 40px; button.button.button-size-circle-medium 44.0x44.0 rgb(243, 243, 244) 44px; div.rounded-20.bg-white 0.0x0.0 rgb(255, 255, 255) T:5px rgb(226, 220, 246) / R:5px rgb(226, 220, 246) / B:5px rgb(226, 220, 246) / L:5px rgb(226, 220, 246) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0.

Child layers that carry the look: button 0x0 background #ffffff `light.surface.l0` radius 40px; button 0x0 radius 40px shadow #d0c6f0 `violet.button.textTab` 0px 0px 0px 1px inset; button 44x44 background #f3f3f4 `light.button.surfaceDisabled` radius 44px.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Burger button
The mobile menu button — a local UI toggle; the opened state was measured after activating it. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; radius 44px; background #f3f3f4 `light.button.surfaceDisabled`; text Suisse Intl 14/44 400, #1c1e20 `core.component.marketing.faq.openColour`; transition all 0.4s cubic-bezier(0.16, 1, 0.3, 1) |
| hover | background #dedfe2 `light.surface.l1Active` |
| focus-visible | background #dedfe2 `light.surface.l1Active`; outline 1px solid #1c1e20 `core.component.marketing.faq.openColour`, offset 1.98438px |
| pressed | background #dedfe2 `light.surface.l1Active` |
| opened | background #dfe0e3 |

![Burger button default](components/crops/m-menu-btn-default.png) ![Burger button hover](components/crops/m-menu-btn-hover.png) ![Burger button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Burger button pressed](components/crops/m-menu-btn-pressed.png) ![Burger button opened](components/crops/m-menu-btn-opened.png)

#### Mobile nav overlay
The navigation overlay opened by the burger (the same destinations as the desktop header); its links were never followed. Read as `m-drawer` on the home page at 390 wide.

**Values (default).** size 390 x 844; padding 96px 0px 120px 0px; background #ffffff `light.surface.l0`; text Suisse Intl 28/28 500, #1c1e20 `core.component.marketing.faq.openColour`; icon 20 x 20, #1c1e20 `core.component.marketing.faq.openColour`.

![Mobile nav overlay default](components/crops/m-drawer-default.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 358 x 184; background transparent; text Suisse Intl 36/46 500, #f8f1fe `light.button.textDefault`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile CTA
The hero action at 390 wide; measured never followed. Read as `m-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 167 x 40; padding 0px 16px; radius 40px; background transparent; shadow #caccd0 0px 0px 0px 1px inset; text Suisse Intl 16/40 500, #000000; transition all 0.4s cubic-bezier(0.16, 1, 0.3, 1); layers button.block.button 167.0x40.0 rgb(202, 204, 208) 0px 0px 0px 1px inset 40px |
| hover | shadow #a1a5ad 0px 0px 0px 1px inset; layers button.block.button 167.0x40.0 rgb(161, 165, 173) 0px 0px 0px 1px inset 40px |
| focus-visible | shadow #a1a5ad 0px 0px 0px 1px inset; outline 1px solid #000000, offset 1.98438px; layers button.block.button 167.0x40.0 rgb(161, 165, 173) 0px 0px 0px 1px inset 1px solid rgb(0, 0, 0) offset 1.98438px 40px |
| pressed | shadow #a1a5ad 0px 0px 0px 1px inset; layers button.block.button 167.0x40.0 rgb(161, 165, 173) 0px 0px 0px 1px inset 40px |

![Mobile CTA default](components/crops/m-cta-default.png) ![Mobile CTA hover](components/crops/m-cta-hover.png) ![Mobile CTA focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile CTA pressed](components/crops/m-cta-pressed.png)

### Footer

The page footer: 'The AI customer operations platform.', the link columns, social icons, certifications and legal row.

#### Site footer
The footer on every marketing page — "The AI customer operations platform.", the link columns, certifications and legal row. Read as `footer` on the home page.

**Values (default).** size 1440 x 1481.39; background transparent; text Suisse Intl 30/36 400, #e2dcf6 `light.button.surfaceOutlineActive`; layers div.px-container-mobile.md:px-container-desktop 1440.0x820.0 rgb(91, 31, 118); a.flex.flex-col 48.0x48.0 rgb(128, 52, 191) 100%; a.flex.flex-col 48.0x48.0 rgb(128, 52, 191) 100%; a.flex.flex-col 48.0x48.0 rgb(128, 52, 191) 100%; div.px-container-mobile.md:px-container-desktop 1440.0x359.0 rgb(48, 12, 65); div.border-t.border-solid 1248.0x49.0 T:1px rgb(179, 117, 244).

Child layers that carry the look: div 1440x820 background #5b1f76 `light.button.surfaceActive`; a 48x48 background #8034bf `light.button.surface` radius 100%; a 48x48 background #8034bf `light.button.surface` radius 100%.

![Site footer default](components/crops/footer-default.png)

#### Footer link
A link in the footer columns; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 48; radius 100%; background #8034bf `light.button.surface`; text Suisse Intl 14/20 400, #e2dcf6 `light.button.surfaceOutlineActive`; transition color 0.2s cubic-bezier(0.55, 0.085, 0.68, 0.53), background-color 0.2s cubic-bezier(0.55, 0.085, 0.68, 0.53), border-color 0.2s cubic-bezier(0.55, 0.085, 0.68, 0.53), text-decoration-color 0.2s cubic-bezier(0.55, 0.085, 0.68, 0.53), fill 0.2s cubic-bezier(0.55, 0.085, 0.68, 0.53), stroke 0.2s cubic-bezier(0.55, 0.085, 0.68, 0.53) |
| hover | background rgba(128, 52, 191, 0.5) |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Front wordmark, the mega-menu product glyphs, the chevrons and social glyphs, partner logos) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Front's product is the workspace: the shared inbox, conversations, contacts, rules, analytics and settings — everything past the auth wall on app.frontapp.com needs an account and was never reached. /signin, /signup and /forgot-password are the only product surfaces a signed-out visitor sees, and they were measured as forms, never submitted. The app's --color-* token layer is real evidence (it paints the auth shell); what it does on the inbox itself is uncaptured.

### Pages

- **The workspace.** Inbox, conversations, contacts, rules, analytics, settings and every post-login surface was never reached; the auth cards were measured as forms, never submitted, and the SSO buttons were never followed.
- **Forms.** /request-demo, the marketing /signup, the auth shell's e-mail fields and the help-centre search and contact forms were typed into then cleared — nothing was sent; what a submission returns is unverified.
- **Blog articles, customer stories, help articles and dev docs pages** are exemplar-level captures; sibling pages share the templates, unmeasured.
- **Solutions and Resources mega-menu panels** were screenshot-captured; only the Product panel's items were component-measured.
- **The Companion messenger** (companion.frontapp.com) paints inside Front's own embed on help.front.com and dev.frontapp.com; its token sheet was captured, the widget UI itself was not measured (it did not open on the captured pages).
- **academy.front.com, community.front.com, frontstatus.com and research.front.com** are further signed-out surfaces on other platforms, not captured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **The billing switch** was toggled each way for the screenshots; the component reading is the annual side. The 'SAVE 24%' prices are the marketing's content, not tokens.

### Themes

front.com's marketing pages paint three section themes down each page — the plum `[data-theme=theme-dark-violet]` default plus theme-white and theme-gray blocks — and offer no page-level theme switch; the three `violet`/`light`/`gray` token sets are the role tables the stylesheet declares for each. app.frontapp.com's shell carries the real theme: `html[data-theme="dark"]` repaints the whole --color-* layer, driven by the front-theme-preference localStorage key falling back to prefers-color-scheme — the `app`/`dark` token sets are those two live resolutions. The Froyo messenger layer ships the same vocabulary as `--colors-*` with its own `[data-theme]` repointings (the `companion`/`companionDark` sets). help.front.com paints one theme; dev.frontapp.com follows the visitor's ReadMe preference, captured light.

### Fonts

- **Suisse Intl** carries every heading, control and body on the marketing site; **Suisse Intl Mono** draws figures and code; **Suisse Works** is the serif display face — all self-hosted. The app shell sets "Indivisible" with Inter fallbacks, and the help centre declares a "CustomFont" stack. The style guide falls back to system fonts.

### Screenshots

- The product UI mockups, customer logos, photography and the Wistia video surfaces in the screenshots are the product's published content; the Qualified widget shot shows the vendor surface as shipped.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, plan prices, customer names, testimonial quotes and partner names are the product's content; only frames and components were measured.
