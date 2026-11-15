# Fingerprint components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from fingerprint.com on 2026-11-15, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the contact-sales, newsletter, demo, login and signup forms were never sent; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (70 components, 187 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/20.8 400, #000000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (187 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture: `light` for every public page — the marketing site ships no dark theme (an emulated prefers-color-scheme: dark probe resolved :root identically; the only dark redeclaration is the `.dark`-scoped `--fpds-color-syntax-*` code-block set, kept as the `dark` token set, labelled declared-not-painted). The Mintlify docs pages do carry a real theme preference — `docs-*-light-theme-dark.png` shots are the docs' own dark surface reached by the 'Change theme preference' toggle; everything else is `light`. /demo and the IdentifySection panels paint the capture machine's own visitor ID, IP address and geolocation, so those regions are masked in the committed shots (tools/redact-rules/fingerprint.json). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages bounded at eight chunks with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x) for default shots and 390 wide for stitched `-full` tiles.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu-product](screenshots/home-light-menu-product.png), [menu-resources](screenshots/home-light-menu-resources.png), [menu-use-cases](screenshots/home-light-menu-use-cases.png) |
| Identification | `/products/identification/` | [default](screenshots/identification-light-default.png), [full](screenshots/identification-light-full.png) |
| Smart Signals | `/products/smart-signals/` | [default](screenshots/smart-signals-light-default.png), [full](screenshots/smart-signals-light-full.png) |
| AI agent detection | `/products/ai-agent-detection/` | [default](screenshots/ai-agent-detection-light-default.png), [full](screenshots/ai-agent-detection-light-full.png) |
| A use case | `/use-cases/payment-fraud/` | [default](screenshots/use-case-light-default.png), [full](screenshots/use-case-light-full.png) |
| Fingerprint for AI | `/ai/` | [default](screenshots/ai-light-default.png), [full](screenshots/ai-light-full.png) |
| Pricing | `/pricing/` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Demo (live signals masked) | `/demo/` | [default](screenshots/demo-light-default.png), [full](screenshots/demo-light-full.png) |
| Contact sales | `/contact-sales/` | [default](screenshots/contact-sales-light-default.png), [full](screenshots/contact-sales-light-full.png) |
| Blog | `/blog/` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Case studies | `/case-studies/` | [default](screenshots/case-studies-light-default.png), [full](screenshots/case-studies-light-full.png) |
| Resources | `/resources/` | [default](screenshots/resources-light-default.png), [full](screenshots/resources-light-full.png) |
| Security | `/security/` | [default](screenshots/security-light-default.png), [full](screenshots/security-light-full.png) |
| Integrations | `/integrations/` | [default](screenshots/integrations-light-default.png), [full](screenshots/integrations-light-full.png) |
| SDK libraries | `/sdk-libraries/` | [default](screenshots/sdk-libraries-light-default.png), [full](screenshots/sdk-libraries-light-full.png) |
| Bot directory | `/bot-directory/` | [default](screenshots/bot-directory-light-default.png), [full](screenshots/bot-directory-light-full.png) |
| About us | `/about-us/` | [default](screenshots/about-us-light-default.png), [full](screenshots/about-us-light-full.png) |
| Careers | `/careers/` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| Docs landing (Mintlify) | `docs.fingerprint.com/` | [default](screenshots/docs-home-light-default.png), [full](screenshots/docs-home-light-full.png), [theme-dark](screenshots/docs-home-light-theme-dark.png) |
| Docs: Quick Start Guide | `docs.fingerprint.com/docs/quick-start-guide` | [default](screenshots/docs-quickstart-light-default.png), [full](screenshots/docs-quickstart-light-full.png), [theme-dark](screenshots/docs-quickstart-light-theme-dark.png) |
| Docs: Smart Signals | `docs.fingerprint.com/docs/smart-signals-overview` | [default](screenshots/docs-signals-light-default.png), [full](screenshots/docs-signals-light-full.png) |
| Sign in (dashboard shell) | `dashboard.fingerprint.com/login` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| Sign up (dashboard shell) | `dashboard.fingerprint.com/signup` | [default](screenshots/signup-light-default.png), [full](screenshots/signup-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `/pricing/` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Demo, phone (live signals masked) | `/demo/` | [default](screenshots/mobile-demo-light-default.png), [full](screenshots/mobile-demo-light-full.png) |
| Contact sales, phone | `/contact-sales/` | [default](screenshots/mobile-contact-sales-light-default.png), [full](screenshots/mobile-contact-sales-light-full.png) |
| Docs, phone | `docs.fingerprint.com/docs/quick-start-guide` | [default](screenshots/mobile-docs-quickstart-light-default.png), [full](screenshots/mobile-docs-quickstart-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Product dropdown | every page header | clicked the 'Product' trigger (a local UI toggle; keyboard Enter is the fallback) | [home-light-menu-product](screenshots/home-light-menu-product.png), [nav-panel](#product-dropdown-panel), [nav-menu-item](#dropdown-item) |
| Use Cases dropdown | every page header | the same activation on 'Use Cases' | [home-light-menu-use-cases](screenshots/home-light-menu-use-cases.png) |
| Resources dropdown | every page header | the same activation on 'Resources' | [home-light-menu-resources](screenshots/home-light-menu-resources.png) |
| Mobile nav overlay | home page, phone width | the 'Mobile Menu' button's own toggle | [m-drawer](#mobile-nav-overlay) |
| Install prompt expander | home hero | the 'Prompt' button's own toggle | [prompt-expander](#install-prompt-expander) |
| Docs theme preference | docs pages | the 'Change theme preference' button — measured; its dark surface was captured as the theme-dark screenshots rather than by holding the toggle | [docs-theme-btn](#theme-toggle), [docs-quickstart-light-theme-dark](screenshots/docs-quickstart-light-theme-dark.png) |
| Pricing controls | /pricing | the volume slider and its ticks re-price the grid — measured at rest, never dragged or pressed; 'Compare all features' and the feature-group and FAQ accordions are local toggles | [price-slider](#identification-volume-slider), [feature-acc](#feature-group-accordion), [faq-acc](#faq-accordion) |
| Demo tabs and fields | /demo | the signal-group tabs are local UI toggles; the fake checkout field was typed into then cleared — 'Place Order', the demo 'Log In' and 'Analyze my browser again' were never pressed | [demo-tab](#signal-group-tab), [demo-field](#demo-checkout-field) |
| Contact/newsletter fields | /contact-sales, the footer, /blog | typed into then cleared — nothing sent | [contact-email](#email-field), [newsletter-field](#newsletter-field), [blog-subscribe](#blog-subscribe-field) |
| Login/signup buttons | dashboard /login and /signup | the SSO buttons and 'Continue with email' were measured, never pressed — the e-mail form was never opened or submitted | [login-google](#google-sso-button), [login-email-btn](#continue-with-email) |
| Signed-in product | a Fingerprint account | the dashboard and every post-login surface needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 31 components were given a real keyboard focus. 22 draw an outline ring: `nav-dropdown-btn` (1px auto #101010, offset 0px), `nav-pricing` (2px solid #f35820 `light.theme.action.primary`, offset 2px), `prompt-expander` (2px solid #f35820 `light.theme.action.primary`, offset 2px), `install-btn` (2px solid #f35820 `light.theme.action.primary`, offset 2px), `price-tick` (1px auto #101010, offset 0px), `plan-cta` (2px solid #f35820 `light.theme.action.primary`, offset 2px), `compare-btn` (1px auto #101010, offset 0px), `demo-analyze` (1px auto #101010, offset 0px), `demo-order` (1px auto #101010, offset 0px), `demo-login` (1px auto #101010, offset 0px), `contact-submit` (2px solid #f35b22 `light.action.submitFill`, offset 2px), `blog-subscribe-btn` (2px solid #f35b22 `light.action.submitFill`, offset 2px), `docs-search` (1px auto #f35b22 `light.action.submitFill`, offset 0px), `docs-theme-btn` (1px auto #f35b22 `light.action.submitFill`, offset 0px), `login-signup-link` (1px auto #f35820 `light.theme.action.primary`, offset 2px), `m-menu-btn` (1px auto #e59700, offset 0px), `m-cta` (2px solid #f35820 `light.theme.action.primary`, offset 2px), `chat-btn` (2px solid #f35b22 `light.action.submitFill`, offset 0px), `subscribe-btn` (1px auto #101010, offset 0px), `footer-link` (2px solid #f35820 `light.theme.action.primary`, offset 2px), `demo-signal` (1px auto #101010, offset 0px), `demo-tab` (2px solid #f35b22 `light.action.submitFill`, offset 2px). 9 draw a focus ring as a shadow instead: `nav-login`, `nav-cta`, `login-google`, `login-github`, `login-email-btn`, `signup-google`, `signup-email-btn`, `prod-cta`, `careers-cta`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.36, 0.19, 0.29, 1)` | box-shadow | contact-email |
| 0.1s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | careers-cta, install-btn, login-email-btn, login-github, login-google, nav-cta, nav-login, prod-cta and more |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, opacity, outline-color, stroke, text-decoration-color | footer-link, subscribe-btn |
| 0.2s | `ease` | all, border-color, box-shadow, color, opacity | cs-card, demo-analyze, demo-signal, demo-tab |
| 0.25s | `cubic-bezier(0, 0, 0.2, 1)` | background, outline | nav-menu-item |
| 0.25s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, box-shadow, color, fill, opacity, outline-color, stroke, text-decoration-color | contact-submit, m-cta, nav-dropdown-btn, nav-pricing, plan-cta |
| 0.25s | `ease` | background-color, border, box-shadow, color, opacity | blog-subscribe-btn, demo-login, demo-order, res-card |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | box-shadow | login-panel, signup-panel |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Product dropdown panel](#product-dropdown-panel) | 1288 x 262 | - | - | transparent | none | 0 |
| [Plan card](#plan-card) | 329.44 x 461.25 | 1px solid #e4e5e1 `light.theme.border.default` | 16px | #f8f8f6 `core.color.gray.100` | #ffffff 0px 1px 0px 0px inset, rgba(24, 25, 22, 0.04) 0px 1px 3px 0px, rgba(24, 25, 22, 0.08) 0px 1px 2px -1px | 24px |
| [Footer](#footer) | 1440 x 516 | T: 1px solid #e8e8e8 | - | #ffffff `light.theme.ink.inverse` | none | 0 |
| [Login panel](#login-panel) | 384 x 352 | 1px solid #e4e5e1 `light.theme.border.default` | 4px | #ffffff `light.theme.ink.inverse` | rgba(0, 0, 0, 0.08) 0px 3px 15px 0px | 24px |
| [Signup panel](#signup-panel) | 384 x 302 | 1px solid #e4e5e1 `light.theme.border.default` | 4px | #ffffff `light.theme.ink.inverse` | rgba(23, 24, 22, 0.03) 0px 1px 2px 0px | 24px |
| [Mobile nav overlay](#mobile-nav-overlay) | 350 x 812 | - | - | transparent | none | 0 |

## Components

### Site chrome

The header on every marketing page: the Fingerprint wordmark, the Product/Use Cases/Resources dropdown triggers, Docs, Demo and Pricing links, Login, Contact Sales and the orange 'Get Started' pill; the product dropdown panel opens under the trigger. The floating 'Open the chat' launcher pins bottom-right.

#### Site header
The sticky top bar on every marketing page: the Fingerprint wordmark, Product/Use Cases/Resources dropdown triggers, AI, Docs, Demo, Pricing, Login, Contact Sales and the "Get Started" CTA. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 56; background oklab(0.999994 0.0000455677 0.0000200868 / 0.8); shadow rgba(24, 25, 22, 0.06) 0px 1px 2px 0px; text Inter-c0aaf1024c6c51d7 13/22 500, #484946 `core.color.gray.900`.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Fingerprint wordmark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 137.59 x 24; radius 4px; background transparent; text Inter-c0aaf1024c6c51d7 16/24 400, #000000 `light.theme.ink.default`.

![Logo default](components/crops/mkt-logo-default.png)

#### Nav dropdown trigger
The "Product" header button — aria-expanded flips and the dropdown panel mounts beside it. The opened state was measured after its own toggle click; aria-expanded had to stay true. Read as `nav-dropdown-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 69 x 28; padding 3px 10px; radius 4px; background transparent; text Inter-c0aaf1024c6c51d7 13/22 500, #484946 `core.color.gray.900`; transition color 0.25s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.25s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.25s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.25s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.25s cubic-bezier(0.4, 0, 0.2, 1), fill 0.25s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.25s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.25s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.25s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.25s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | layers span.absolute.inset-x-0 69.0x29.0 rgb(250, 250, 248) T:1px solid rgba(228, 229, 225, 0.8) / R:1px solid rgba(228, 229, 225, 0.8) / B:1px solid rgba(228, 229, 225, 0.8) / L:1px solid rgba(228, 229, 225, 0.8) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(119, 54, 28, 0.2) 0px 0.5px 0.5px 0px 8px |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.relative.flex 69.0x28.0 1px auto rgb(16, 16, 16) offset 0px 4px; span.absolute.inset-x-0 69.0x29.0 rgb(250, 250, 248) T:1px solid rgba(228, 229, 225, 0.8) / R:1px solid rgba(228, 229, 225, 0.8) / B:1px solid rgba(228, 229, 225, 0.8) / L:1px solid rgba(228, 229, 225, 0.8) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0p |
| pressed, opened | layers span.absolute.inset-x-0 69.0x29.0 rgb(250, 250, 248) T:1px solid rgba(228, 229, 225, 0.8) / R:1px solid rgba(228, 229, 225, 0.8) / B:1px solid rgba(228, 229, 225, 0.8) / L:1px solid rgba(228, 229, 225, 0.8) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(119, 54, 28, 0.2) 0px 0.5px 0.5px 0px 8px |

![Nav dropdown trigger default](components/crops/nav-dropdown-btn-default.png) ![Nav dropdown trigger hover](components/crops/nav-dropdown-btn-hover.png) ![Nav dropdown trigger focus-visible](components/crops/nav-dropdown-btn-focus-visible.png) ![Nav dropdown trigger pressed](components/crops/nav-dropdown-btn-pressed.png) ![Nav dropdown trigger opened](components/crops/nav-dropdown-btn-opened.png)

#### Product dropdown panel
The dropdown panel opened by the "Product" trigger (Device Intelligence, Smart Signals, product entries); its links were never followed. Read as `nav-panel` on the home page.

**Values (default).** size 1288 x 262; background transparent; text Inter-c0aaf1024c6c51d7 12/16 400, #a0a09d `light.form.placeholder`; icon 14 x 14, #000000 `light.theme.ink.default`; layers div.relative.overflow-hidden 854.0x258.0 rgb(250, 250, 248) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(119, 54, 28, 0.2) 0px 0.5px 0.5px 0px 1px solid rgba(228, 229, 225, 0.8) offset 0px 16px; div.flex.flex-col 846.0x250.4 rgb(255, 255, 255) T:1px solid rgb(217, 217, 214) / R:1px solid rgb(217, 217, 2.

Child layers that carry the look: div 854x258 background #fafaf8 radius 16px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(119, 54, 28, 0.2) 0px 0.5px 0.5px 0px; div 846x250.4 background #ffffff `light.theme.ink.inverse` border 1px solid #d9d9d6 radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.4) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.04) 0px -2px 0px 0px inset; a 280x58.8 radius 8px.

![Product dropdown panel default](components/crops/nav-panel-default.png)

#### Dropdown item
The "Identification" item inside the opened product dropdown; measured, never followed. Read as `nav-menu-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 280 x 58.8; padding 8px; radius 8px; background transparent; outline 1px solid transparent, offset 2px; text Inter-c0aaf1024c6c51d7 14/22 500, #181916 `light.form.fieldInk`; transition background 0.25s cubic-bezier(0, 0, 0.2, 1), outline 0.25s cubic-bezier(0, 0, 0.2, 1); icon 14 x 14, #000000 `light.theme.ink.default`; layers a.group/link.flex 280.0x58.8 1px solid rgba(0, 0, 0, 0) offset 2px 8px; span.flex.h-7 28.0x28.0 rgb(255, 255, 255) T:1px solid rgb(240, 240, 237) / R:1px solid rgb(240, 240, 237) / B:1px solid rgb(240, 240, 237) / L:1px solid rgb(240, 240, 237) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(24, 25, 22, 0. |
| hover | background #fafaf8; shadow rgba(24, 25, 22, 0.02) 0px 2px 1px 0px; outline 1px dashed #e8e8e8, offset 0px; layers none |

Child layers that carry the look: a 280x58.8 radius 8px; span 28x28 background #ffffff `light.theme.ink.inverse` image linear-gradient(301deg, rgba(72, 73, 70, 0.02) 9.55%, rgba(110, 111, 108, 0.02) 67.28%) border 1px solid #f0f0ed radius 8px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(24, 25, 22, 0.06) 0px 1px 2px 0px.

![Dropdown item default](components/crops/nav-menu-item-default.png) ![Dropdown item hover](components/crops/nav-menu-item-hover.png)

#### Nav link
The "Pricing" header link; measured, never followed. Read as `nav-pricing` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 62 x 28; padding 3px 10px; radius 4px; background transparent; text Inter-c0aaf1024c6c51d7 13/22 500, #484946 `core.color.gray.900`; transition color 0.25s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.25s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.25s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.25s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.25s cubic-bezier(0.4, 0, 0.2, 1), fill 0.25s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.25s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.25s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.25s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.25s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | layers span.absolute.inset-x-0 62.0x29.0 rgb(250, 250, 248) T:1px solid rgba(228, 229, 225, 0.8) / R:1px solid rgba(228, 229, 225, 0.8) / B:1px solid rgba(228, 229, 225, 0.8) / L:1px solid rgba(228, 229, 225, 0.8) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(119, 54, 28, 0.2) 0px 0.5px 0.5px 0px 8px |
| focus-visible | outline 2px solid #f35820 `light.theme.action.primary`, offset 2px; layers a.relative.flex 62.0x28.0 2px solid rgb(243, 88, 32) offset 2px 4px; span.absolute.inset-x-0 62.0x29.0 rgb(250, 250, 248) T:1px solid rgba(228, 229, 225, 0.8) / R:1px solid rgba(228, 229, 225, 0.8) / B:1px solid rgba(228, 229, 225, 0.8) / L:1px solid rgba(228, 229, 225, 0.8) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0 |
| pressed | layers span.absolute.inset-x-0 62.0x29.0 rgb(250, 250, 248) T:1px solid rgba(228, 229, 225, 0.8) / R:1px solid rgba(228, 229, 225, 0.8) / B:1px solid rgba(228, 229, 225, 0.8) / L:1px solid rgba(228, 229, 225, 0.8) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(119, 54, 28, 0.2) 0px 0.5px 0.5px 0px 8px |

![Nav link default](components/crops/nav-pricing-default.png) ![Nav link hover](components/crops/nav-pricing-hover.png) ![Nav link focus-visible](components/crops/nav-pricing-focus-visible.png) ![Nav link pressed](components/crops/nav-pricing-pressed.png)

#### Login link
The "Login" header link to dashboard.fingerprint.com/login; measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 31 x 18; radius 6px; background transparent; text Inter-c0aaf1024c6c51d7 12/18 500, #f35b22 `light.action.submitFill`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter-c0aaf1024c6c51d7 12/18 500, #be400f |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px; layers a.relative.select-none 31.0x18.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, rgb(243, 88, 32) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 6px |

![Login link default](components/crops/nav-login-default.png) ![Login link hover](components/crops/nav-login-hover.png) ![Login link focus-visible](components/crops/nav-login-focus-visible.png) ![Login link pressed](components/crops/nav-login-pressed.png)

#### Header CTA
The orange "Get Started" header pill (the brand-primary fill); links to dashboard.fingerprint.com/signup, measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 96 x 32; padding 0px 14px; border 1px solid #bd400f `light.theme.action.primaryHover`; radius 6px; background #f35820 `light.theme.action.primary`; shadow rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.02) 0px -1px 0px 0px inset, rgba(23, 24, 22, 0.03) 0px 1px 2px 0px; text Inter-c0aaf1024c6c51d7 12/16 500, #ffffff `light.theme.ink.inverse`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #bd400f `light.theme.action.primaryHover` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.02) 0px -1px 0px 0px inset, rgba(23, 24, 22, 0.03) 0px 1px 2px 0px |

![Header CTA default](components/crops/nav-cta-default.png) ![Header CTA hover](components/crops/nav-cta-hover.png) ![Header CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Header CTA pressed](components/crops/nav-cta-pressed.png)

#### Chat launcher
The floating "Open the chat" support-widget launcher pinned bottom-right; measured, never opened. Read as `chat-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 56 x 56; padding 4px; border 1px dashed #e4e5e1 `light.theme.border.default`; radius 50%; background transparent; text Inter-c0aaf1024c6c51d7 16/24 400, #000000 `light.theme.ink.default`; icon 24 x 24, #000000 `light.theme.ink.default` |
| focus-visible | outline 2px solid #f35b22 `light.action.submitFill`, offset 0px |

![Chat launcher default](components/crops/chat-btn-default.png) ![Chat launcher hover](components/crops/chat-btn-hover.png) ![Chat launcher focus-visible](components/crops/chat-btn-focus-visible.png) ![Chat launcher pressed](components/crops/chat-btn-pressed.png)

### Home

The home hero: the 'New — We now detect Claude Duet' announcement pill, the display masthead, the 'Prompt' install expander, the 'Install Fingerprint with AI' button and section headings.

#### Hero headline
"Identify Every Visitor" — the fp-hero-block masthead. Read as `hero-h1` on the home page.

**Values (default).** size 828.67 x 56; background transparent; text Inter-c0aaf1024c6c51d7 48/56 500, #000000 `light.theme.ink.default`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Install prompt expander
The "Prompt" expander in the hero that reveals the get-started prompt text and the AI-tool install links; opened by its own toggle. Read as `prompt-expander` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 113.5 x 26; padding 0px 8px; border 1px solid transparent; radius 4px 2px 2px 4px; background transparent; text Inter-c0aaf1024c6c51d7 14/20 500, #484946 `core.color.gray.900`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #484946 `core.color.gray.900` |
| hover | background #f1f1ee `core.color.gray.200` |
| focus-visible | outline 2px solid #f35820 `light.theme.action.primary`, offset 2px |
| opened | background #e4e5e1 `light.theme.border.default` |

![Install prompt expander default](components/crops/prompt-expander-default.png) ![Install prompt expander hover](components/crops/prompt-expander-hover.png) ![Install prompt expander focus-visible](components/crops/prompt-expander-focus-visible.png) ![Install prompt expander pressed](components/crops/prompt-expander-pressed.png) ![Install prompt expander opened](components/crops/prompt-expander-opened.png)

#### Install button
The "Install Fingerprint with AI" hero button — a local UI toggle that reveals install options; measured, never toggled. Read as `install-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 256.08 x 26; padding 0px 8px; border 1px solid transparent; radius 2px 4px 4px 2px; background transparent; text JetBrains Mono-c3e9177549e38394 14/20 500, #171816 `core.color.gray.1000`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #484946 `core.color.gray.900` |
| hover | background #f1f1ee `core.color.gray.200` |
| focus-visible | outline 2px solid #f35820 `light.theme.action.primary`, offset 2px |

![Install button default](components/crops/install-btn-default.png) ![Install button hover](components/crops/install-btn-hover.png) ![Install button focus-visible](components/crops/install-btn-focus-visible.png) ![Install button pressed](components/crops/install-btn-pressed.png)

#### Section heading
A marketing section heading further down the home page ("Not all bots are bad Not all humans are good") — a display-size h2, so transient microcopy such as a widget's error heading never counts. Read as `section-h2` on the home page.

**Values (default).** size 559 x 120; padding 16px 0px; background transparent; text Inter-c0aaf1024c6c51d7 36/44 500, #000000 `light.theme.ink.default`.

![Section heading default](components/crops/section-h2-default.png)

#### News pill
The "New — We now detect Claude Duet" announcement pill above the headline; links to a blog post, measured never followed. Read as `hero-pill` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 329.77 x 42; background transparent; text Inter-c0aaf1024c6c51d7 12/16 500, #f35820 `light.theme.action.primary`; icon 14 x 14, #000000 `light.theme.ink.default`; layers span.inline-flex.items-center 329.8x42.0 T:1px dashed rgb(228, 229, 225) / R:1px dashed rgb(228, 229, 225) / B:1px dashed rgb(228, 229, 225) / L:1px dashed rgb(228, 229, 225) 26px; span.mr-1.shrink-0 42.0x30.0 oklab(0.662011 0.157735 0.123768 / 0.1) 31px |
| hover | layers span.inline-flex.items-center 329.8x42.0 T:1px dashed rgb(193, 193, 190) / R:1px dashed rgb(193, 193, 190) / B:1px dashed rgb(193, 193, 190) / L:1px dashed rgb(193, 193, 190) 26px; span.mr-1.shrink-0 42.0x30.0 oklab(0.662011 0.157735 0.123768 / 0.1) 31px |

Child layers that carry the look: span 329.8x42 image linear-gradient(90deg, rgba(248, 247, 254, 0.2) 0%, rgba(255, 255, 255, 0.2) 100%) border 1px dashed #e4e5e1 `light.theme.border.default` radius 26px; span 42x30 background oklab(0.662011 0.157735 0.123768 / 0.1) radius 31px.

![News pill default](components/crops/hero-pill-default.png) ![News pill hover](components/crops/hero-pill-hover.png)

### Pricing

The /pricing grid: the identification-volume range slider and its 20K-1M+ ticks, the plan columns and their CTAs, 'Compare all features', the feature-group accordions in the comparison table and the FAQ rows — the slider and accordions are local UI toggles.

#### Pricing headline
"Choose your plan" — the /pricing masthead. Read as `price-h1` on the pricing page.

**Values (default).** size 400 x 52; background transparent; text Inter-c0aaf1024c6c51d7 50/52 500, #000000 `light.theme.ink.default`.

![Pricing headline default](components/crops/price-h1-default.png)

#### Identification-volume slider
The "billing-slider" range input that re-prices the plans (20K/100K/200K/500K/1M+ identifications); measured at rest, never dragged. Read as `price-slider` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 444 x 10; background transparent; text Inter-c0aaf1024c6c51d7 16/24 400, #000000 `light.theme.ink.default`; placeholder #000000 `light.theme.ink.default` |

![Identification-volume slider default](components/crops/price-slider-default.png) ![Identification-volume slider focused](components/crops/price-slider-focused.png)

#### Slider tick
A volume tick under the slider (100K identifications); a local UI control that re-prices the grid — measured, never pressed. Read as `price-tick` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 88.8 x 22; background transparent; text JetBrains Mono-c3e9177549e38394 14/22 400, #6e6f6c |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.mt-10.flex-1 88.8x22.0 1px auto rgb(16, 16, 16) offset 0px |

![Slider tick default](components/crops/price-tick-default.png) ![Slider tick hover](components/crops/price-tick-hover.png) ![Slider tick focus-visible](components/crops/price-tick-focus-visible.png) ![Slider tick pressed](components/crops/price-tick-pressed.png)

#### Plan card
A plan card on /pricing — one bordered column of the three-card grid (Free/Pro/Enterprise): name, price, identification allowance and its CTA. Read as `plan-card` on the pricing page.

**Values (default).** size 329.44 x 461.25; padding 24px; border 1px solid #e4e5e1 `light.theme.border.default`; radius 16px; background #f8f8f6 `core.color.gray.100`; shadow #ffffff 0px 1px 0px 0px inset, rgba(24, 25, 22, 0.04) 0px 1px 3px 0px, rgba(24, 25, 22, 0.08) 0px 1px 2px -1px; text Inter-c0aaf1024c6c51d7 20/32 500, #000000 `light.theme.ink.default`; icon 12 x 10, #f35b22 `light.action.submitFill`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan CTA
A plan card's primary action ("Start Free" on the Free/Pro cards, "Contact Sales" on Enterprise); measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 87 x 32; padding 7.21px 14px; border 1px solid #dadad7 `core.color.gray.400`; radius 6px; background #f8f8f6 `core.color.gray.100`; shadow rgba(24, 25, 22, 0.02) 0px 2px 1px 0px, rgba(24, 25, 22, 0.1) 0px -1px 0px 0px inset; text Inter-c0aaf1024c6c51d7 12/15.6 500, #171816 `core.color.gray.1000`; transition background-color 0.25s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.25s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.25s cubic-bezier(0.4, 0, 0.2, 1), color 0.25s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.25s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f1f1ee `core.color.gray.200`; shadow rgba(255, 255, 255, 0.4) 0px 1px 0px 0px inset, rgba(24, 25, 22, 0.02) 0px 2px 1px 0px, rgba(24, 25, 22, 0.1) 0px -1px 0px 0px inset |
| focus-visible | outline 2px solid #f35820 `light.theme.action.primary`, offset 2px |
| pressed | background #e4e5e1 `light.theme.border.default`; shadow rgba(255, 255, 255, 0.4) 0px 1px 0px 0px inset, rgba(24, 25, 22, 0.02) 0px 2px 1px 0px, rgba(24, 25, 22, 0.1) 0px -1px 0px 0px inset |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Compare features control
The "Compare all features" control that opens the feature-comparison grid; a local UI toggle — measured at rest, never toggled. Read as `compare-btn` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1038.33 x 62; padding 24px; border R: 1px dashed #e4e5e1 `light.theme.border.default`; L: 1px dashed #e4e5e1 `light.theme.border.default`; background transparent; text Inter-c0aaf1024c6c51d7 14/14 400, #f35b22 `light.action.submitFill`; icon 10 x 10, #f35b22 `light.action.submitFill`; layers button.col-[2/12].flex 1038.3x62.0 R:1px dashed rgb(228, 229, 225) / L:1px dashed rgb(228, 229, 225) |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.col-[2/12].flex 1038.3x62.0 R:1px dashed rgb(228, 229, 225) / L:1px dashed rgb(228, 229, 225) 1px auto rgb(16, 16, 16) offset 0px |

Child layers that carry the look: button 1038.3x62 border 1px dashed #e4e5e1 `light.theme.border.default`.

![Compare features control default](components/crops/compare-btn-default.png) ![Compare features control hover](components/crops/compare-btn-hover.png) ![Compare features control focus-visible](components/crops/compare-btn-focus-visible.png) ![Compare features control pressed](components/crops/compare-btn-pressed.png)

#### Feature-group accordion
A feature-group accordion in the comparison table ("Identification Features", "Smart Signals", "Support", ...); the opened state was measured after its own toggle click — a local UI toggle. Read as `feature-acc` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened, hover) | size 1036.33 x 73; background transparent; text Inter-c0aaf1024c6c51d7 18/28 500, #181916 `light.form.fieldInk`; icon 16 x 30, #f35b22 `light.action.submitFill`; layers button.relative.flex 414.5x73.0 rgb(252, 252, 251) R:1px dashed rgb(228, 229, 225) / B:1px dashed rgb(228, 229, 225); button::before.relative.flex 1.5pxx72px rgb(243, 91, 34); div.h-full.border-b 207.3x73.0 R:1px dashed rgb(228, 229, 225) / B:1px dashed rgb(228, 229, 225); div.h-full.w-full 190.3x72.0 rgb(247, 247, 245) R:1px solid rgb(228, 229, 225) / L:1px solid rgb(228, 229, 225); div.h-full.bo |

Child layers that carry the look: button 414.5x73 background #fcfcfb border 1px dashed #e4e5e1 `light.theme.border.default`; button::before 1.5pxx72px background #f35b22 `light.action.submitFill`; div 207.3x73 border 1px dashed #e4e5e1 `light.theme.border.default`.

![Feature-group accordion default](components/crops/feature-acc-default.png) ![Feature-group accordion opened](components/crops/feature-acc-opened.png) ![Feature-group accordion hover](components/crops/feature-acc-hover.png)

#### FAQ accordion
A question row in the pricing FAQ ("How does billing for Fingerprint work?", "Do you offer annual billing...", ...); the opened state was measured after its own toggle — a local UI toggle. Read as `faq-acc` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 508.17 x 54.41; padding 16px 24px; background transparent; text Inter-c0aaf1024c6c51d7 16/22.4 500, #484946 `core.color.gray.900`; icon 17 x 16, #484946 `core.color.gray.900` |
| opened | text Inter-c0aaf1024c6c51d7 16/22.4 500, #f35b22 `light.action.submitFill`; icon 16 x 17, #f35b22 `light.action.submitFill` |

![FAQ accordion default](components/crops/faq-acc-default.png) ![FAQ accordion opened](components/crops/faq-acc-opened.png)

### Contact sales form

The /contact-sales form: the e-mail field and the 'Submit' button — measured and typed into then cleared, never submitted.

#### Contact headline
"Talk to Our Sales Team" — the /contact-sales masthead over the form. Read as `contact-h1` on the contact-sales page.

**Values (default).** size 597 x 45; background transparent; text Inter-c0aaf1024c6c51d7 36/45 500, #181916 `light.form.fieldInk`.

![Contact headline default](components/crops/contact-h1-default.png)

#### Email field
The e-mail input on the sales form; focused and typed into then cleared — never submitted. Read as `contact-email` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 413 x 40.39; padding 9px 12px; radius 6px; background #ffffff `light.theme.ink.inverse`; shadow #e8e8e8 0px 0px 0px 1px; text Inter-c0aaf1024c6c51d7 14/22.4 400, #181916 `light.form.fieldInk`; transition box-shadow 0.1s cubic-bezier(0.36, 0.19, 0.29, 1); placeholder #a0a09d `light.form.placeholder` |
| focused, filled | shadow #f35b22 0px 0px 0px 1px, rgba(243, 91, 34, 0.2) 0px 0px 0px 6px |

![Email field default](components/crops/contact-email-default.png) ![Email field focused](components/crops/contact-email-focused.png) ![Email field filled](components/crops/contact-email-filled.png)

#### Submit button
The sales form's "Submit" button; its states were measured but the button was never clicked — the form was never sent. Read as `contact-submit` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 413 x 37.59; padding 8px 16px; border 1px solid #be400f; radius 6px; background #f35b22 `light.action.submitFill`; shadow rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset, rgba(24, 25, 22, 0.06) 0px 1px 2px 0px, rgba(24, 25, 22, 0.1) 0px -1px 0px 0px inset; text Inter-c0aaf1024c6c51d7 14/19.6 500, #ffffff `light.theme.ink.inverse`; transition background-color 0.25s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.25s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.25s cubic-bezier(0.4, 0, 0.2, 1), color 0.25s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #be400f |
| focus-visible | outline 2px solid #f35b22 `light.action.submitFill`, offset 2px |
| pressed | background #be400f |

![Submit button default](components/crops/contact-submit-default.png) ![Submit button hover](components/crops/contact-submit-hover.png) ![Submit button focus-visible](components/crops/contact-submit-focus-visible.png) ![Submit button pressed](components/crops/contact-submit-pressed.png)

### Login and signup (dashboard shell)

dashboard.fingerprint.com /login and /signup — the product shell's auth cards (Continue with Google/GitHub/Microsoft, 'Continue with email', 'Sign up'), a different stack that does not share the marketing token layer. Measured as forms, never opened or submitted.

#### Login panel
The dashboard-shell sign-in card on dashboard.fingerprint.com/login — the elevated MuiPaper card holding "Log In", the Google/GitHub/Microsoft SSO buttons and "Continue with email" — not the full-page main behind it. Read as `login-panel` on the login page.

**Values (default).** size 384 x 352; padding 24px; border 1px solid #e4e5e1 `light.theme.border.default`; radius 4px; background #ffffff `light.theme.ink.inverse`; shadow rgba(0, 0, 0, 0.08) 0px 3px 15px 0px; text Inter 20/28 500, #171816 `core.color.gray.1000`; transition box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 17, #484946 `core.color.gray.900`.

![Login panel default](components/crops/login-panel-default.png)

#### Google SSO button
The "Continue with Google" button; measured, never pressed. Read as `login-google` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 334 x 36; padding 0px 16px; border 1px solid #dadad7 `core.color.gray.400`; radius 6px; background #ffffff `light.theme.ink.inverse`; shadow rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.02) 0px -1px 0px 0px inset, rgba(23, 24, 22, 0.03) 0px 1px 2px 0px; text Inter 14/20 500, #171816 `core.color.gray.1000`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 17, #484946 `core.color.gray.900` |
| hover | background #f1f1ee `core.color.gray.200` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.02) 0px -1px 0px 0px inset, rgba(23, 24, 22, 0.03) 0px 1px 2px 0px |

![Google SSO button default](components/crops/login-google-default.png) ![Google SSO button hover](components/crops/login-google-hover.png) ![Google SSO button focus-visible](components/crops/login-google-focus-visible.png) ![Google SSO button pressed](components/crops/login-google-pressed.png)

#### GitHub SSO button
The "Continue with GitHub" button; measured, never pressed. Read as `login-github` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 334 x 36; padding 0px 16px; border 1px solid #dadad7 `core.color.gray.400`; radius 6px; background #ffffff `light.theme.ink.inverse`; shadow rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.02) 0px -1px 0px 0px inset, rgba(23, 24, 22, 0.03) 0px 1px 2px 0px; text Inter 14/20 500, #171816 `core.color.gray.1000`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 17, #484946 `core.color.gray.900` |
| hover | background #f1f1ee `core.color.gray.200` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.02) 0px -1px 0px 0px inset, rgba(23, 24, 22, 0.03) 0px 1px 2px 0px |

![GitHub SSO button default](components/crops/login-github-default.png) ![GitHub SSO button hover](components/crops/login-github-hover.png) ![GitHub SSO button focus-visible](components/crops/login-github-focus-visible.png) ![GitHub SSO button pressed](components/crops/login-github-pressed.png)

#### Continue with email
The "Continue with email" control that reveals the e-mail form; measured, never pressed — the form was never opened or submitted. Read as `login-email-btn` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 334 x 36; padding 0px 16px; border 1px solid #dadad7 `core.color.gray.400`; radius 6px; background #ffffff `light.theme.ink.inverse`; shadow rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.02) 0px -1px 0px 0px inset, rgba(23, 24, 22, 0.03) 0px 1px 2px 0px; text Inter 14/20 500, #171816 `core.color.gray.1000`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f1f1ee `core.color.gray.200` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.02) 0px -1px 0px 0px inset, rgba(23, 24, 22, 0.03) 0px 1px 2px 0px |

![Continue with email default](components/crops/login-email-btn-default.png) ![Continue with email hover](components/crops/login-email-btn-hover.png) ![Continue with email focus-visible](components/crops/login-email-btn-focus-visible.png) ![Continue with email pressed](components/crops/login-email-btn-pressed.png)

#### Sign up link
The "Sign up" link beside "New to Fingerprint?"; measured, never followed. Read as `login-signup-link` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 49.42 x 17; background transparent; text Inter 14/20 400, #f35820 `light.theme.action.primary` |
| focus-visible | outline 1px auto #f35820 `light.theme.action.primary`, offset 2px; layers a.MuiTypography-root.MuiTypography-inherit 49.4x17.0 1px auto rgb(243, 88, 32) offset 2px |

![Sign up link default](components/crops/login-signup-link-default.png) ![Sign up link hover](components/crops/login-signup-link-hover.png) ![Sign up link focus-visible](components/crops/login-signup-link-focus-visible.png) ![Sign up link pressed](components/crops/login-signup-link-pressed.png)

#### Signup panel
The dashboard-shell sign-up card on dashboard.fingerprint.com/signup — the elevated MuiPaper card holding "Sign up" and the SSO/email controls, not the full-page main behind it. Read as `signup-panel` on the signup page.

**Values (default).** size 384 x 302; padding 24px; border 1px solid #e4e5e1 `light.theme.border.default`; radius 4px; background #ffffff `light.theme.ink.inverse`; shadow rgba(23, 24, 22, 0.03) 0px 1px 2px 0px; text Inter 20/28 500, #171816 `core.color.gray.1000`; transition box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 17, #484946 `core.color.gray.900`.

![Signup panel default](components/crops/signup-panel-default.png)

#### Google SSO button (signup)
The "Continue with Google" button on /signup; measured, never pressed. Read as `signup-google` on the signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 334 x 36; padding 0px 16px; border 1px solid #dadad7 `core.color.gray.400`; radius 6px; background transparent; text Inter 14/20 500, #171816 `core.color.gray.1000`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 17, #484946 `core.color.gray.900` |
| hover | background #f1f1ee `core.color.gray.200` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px |

![Google SSO button (signup) default](components/crops/signup-google-default.png) ![Google SSO button (signup) hover](components/crops/signup-google-hover.png) ![Google SSO button (signup) focus-visible](components/crops/signup-google-focus-visible.png) ![Google SSO button (signup) pressed](components/crops/signup-google-pressed.png)

#### Continue with email (signup)
The "Continue with email" control on /signup; measured, never pressed. Read as `signup-email-btn` on the signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 334 x 36; padding 0px 16px; border 1px solid transparent; radius 6px; background transparent; text Inter 14/20 500, #171816 `core.color.gray.1000`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f1f1ee `core.color.gray.200` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px |

![Continue with email (signup) default](components/crops/signup-email-btn-default.png) ![Continue with email (signup) hover](components/crops/signup-email-btn-hover.png) ![Continue with email (signup) focus-visible](components/crops/signup-email-btn-focus-visible.png) ![Continue with email (signup) pressed](components/crops/signup-email-btn-pressed.png)

### Demo surface

/demo — the product's own public demo: the 01/02/03 signal-group tabs, the 'See <signal> in the signals below' reveal controls, 'Analyze my browser again', and the fake checkout/sign-in fields inside the demo pane. The live panel paints the capture machine's visitor ID, IP and rough location, so its committed shots are masked; the controls were measured, never pressed.

#### Demo headline
"See Fingerprint in Action" — the /demo masthead over the live device-intelligence demo. Read as `demo-h1` on the demo page.

**Values (default).** size 565.83 x 56; background transparent; text Inter-c0aaf1024c6c51d7 48/56 500, #181916 `light.form.fieldInk`.

![Demo headline default](components/crops/demo-h1-default.png)

#### Re-analyze button
The "Analyze my browser again" control — it re-runs the public demo on the visitor's own browser; measured, never pressed. Read as `demo-analyze` on the demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 146 x 23; padding 4px 8px; border 1px solid #e4e5e1 `light.theme.border.default`; radius 4px; background #f8f8f6 `core.color.gray.100`; shadow #ffffff 0px 1px 0px 0px inset; text Inter-c0aaf1024c6c51d7 10/13 500, #181916 `light.form.fieldInk`; transition all 0.2s ease |
| hover | size 164 x 23; icon 16.97 x 16.97, #181916 `light.form.fieldInk` |
| focus-visible | size 164 x 23; outline 1px auto #101010, offset 0px; icon 14.09 x 14.09, #181916 `light.form.fieldInk` |
| pressed | size 164 x 23; icon 15.23 x 15.23, #181916 `light.form.fieldInk` |

![Re-analyze button default](components/crops/demo-analyze-default.png) ![Re-analyze button hover](components/crops/demo-analyze-hover.png) ![Re-analyze button focus-visible](components/crops/demo-analyze-focus-visible.png) ![Re-analyze button pressed](components/crops/demo-analyze-pressed.png)

#### Demo checkout field
A mock card-number input inside the demo's fake checkout; typed into then cleared — the demo form was never placed. Read as `demo-field` on the demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 262 x 40; padding 7.5px 50px; border 1px solid #e4e5e1 `light.theme.border.default`; radius 4px; background #ffffff `light.theme.ink.inverse`; text JetBrains Mono-c3e9177549e38394 14/16 400, #484946 `core.color.gray.900`; placeholder oklab(0.40341 -0.0026598 0.00434527 / 0.5) |

![Demo checkout field default](components/crops/demo-field-default.png) ![Demo checkout field focused](components/crops/demo-field-focused.png) ![Demo checkout field filled](components/crops/demo-field-filled.png)

#### Demo order button
The fake checkout's "Place Order" button inside the demo pane; measured, never pressed. Read as `demo-order` on the demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 262 x 38; padding 12px 15.045px; border 1px solid #f1739d; radius 4px; background #c2336c; shadow rgba(0, 0, 0, 0.2) 0px -1px 0px 0px inset, rgba(255, 255, 255, 0.6) 0px 1px 0px 0px inset; text Inter-c0aaf1024c6c51d7 12/12 600, #ffffff `light.theme.ink.inverse`; transition background-color 0.25s ease, border 0.25s ease, opacity 0.25s ease, color 0.25s ease |
| focus-visible | outline 1px auto #101010, offset 0px |

![Demo order button default](components/crops/demo-order-default.png) ![Demo order button hover](components/crops/demo-order-hover.png) ![Demo order button focus-visible](components/crops/demo-order-focus-visible.png) ![Demo order button pressed](components/crops/demo-order-pressed.png)

#### Demo login button
The fake sign-in "Log In" inside the demo pane; measured, never pressed. Read as `demo-login` on the demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 262 x 38; padding 12px 15.045px; border 1px solid #52a5e1; radius 4px; background #0174b3; shadow rgba(0, 0, 0, 0.2) 0px -1px 0px 0px inset, rgba(255, 255, 255, 0.6) 0px 1px 0px 0px inset; text Inter-c0aaf1024c6c51d7 12/12 600, #ffffff `light.theme.ink.inverse`; transition background-color 0.25s ease, border 0.25s ease, opacity 0.25s ease, color 0.25s ease |
| focus-visible | outline 1px auto #101010, offset 0px |

![Demo login button default](components/crops/demo-login-default.png) ![Demo login button hover](components/crops/demo-login-hover.png) ![Demo login button focus-visible](components/crops/demo-login-focus-visible.png) ![Demo login button pressed](components/crops/demo-login-pressed.png)

#### Signal reveal button
A "See <signal> in the signals below" control that scrolls the signal panel to a row — a local UI toggle; measured, never pressed. The signal values it points at can name this machine's IP and rough location, so the panel's crops are masked before commit. Read as `demo-signal` on the demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 14 x 14; background transparent; text Inter-c0aaf1024c6c51d7 16/18.4 400, #a0a09d `light.form.placeholder`; transition opacity 0.2s ease; opacity 0; icon 14 x 14, #a0a09d `light.form.placeholder` |
| hover | text Inter-c0aaf1024c6c51d7 16/18.4 400, #484946 `core.color.gray.900`; opacity none; icon 14 x 14, #484946 `core.color.gray.900` |
| focus-visible | outline 1px auto #101010, offset 0px; opacity none; layers button.flex.size-[14px] 14.0x14.0 1px auto rgb(16, 16, 16) offset 0px |
| pressed | text Inter-c0aaf1024c6c51d7 16/18.4 400, #484946 `core.color.gray.900`; icon 14 x 14, #484946 `core.color.gray.900` |

![Signal reveal button default](components/crops/demo-signal-default.png) ![Signal reveal button hover](components/crops/demo-signal-hover.png) ![Signal reveal button focus-visible](components/crops/demo-signal-focus-visible.png) ![Signal reveal button pressed](components/crops/demo-signal-pressed.png)

#### Signal-group tab
The "01 IDENTIFICATION SIGNALS" tab in the demo (02 BROWSER SMART SIGNALS, 03 MOBILE SMART SIGNALS are its siblings); opened by its own toggle — a local UI tab. Read as `demo-tab` on the demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 199.09 x 37; padding 8px 16px; border R: 1px solid #e4e5e1 `light.theme.border.default`; B: 1px solid #ffffff `light.theme.ink.inverse`; background transparent; text JetBrains Mono-c3e9177549e38394 11/20 300, #f35b22 `light.action.submitFill`; transition color 0.2s ease; layers ::after rgba(0, 0, 0, 0) 0px none 1; button.relative.inline-flex 199.1x37.0 R:1px solid rgb(228, 229, 225) / B:1px solid rgb(255, 255, 255); button::after.relative.inline-flex 198.094pxx2px |
| focus-visible | outline 2px solid #f35b22 `light.action.submitFill`, offset 2px; layers ::after rgba(0, 0, 0, 0) 0px none 1; button.relative.inline-flex 199.1x37.0 R:1px solid rgb(228, 229, 225) / B:1px solid rgb(255, 255, 255) 2px solid rgb(243, 91, 34) offset 2px; button::after.relative.inline-flex 198.094pxx2px |

Child layers that carry the look: button 199.1x37 border 1px solid #e4e5e1 `light.theme.border.default`; button::after 198.094pxx2px image linear-gradient(90deg, #f35b22 `light.action.submitFill` 0%, rgba(243, 91, 34, 0.05) 100%).

![Signal-group tab default](components/crops/demo-tab-default.png) ![Signal-group tab hover](components/crops/demo-tab-hover.png) ![Signal-group tab focus-visible](components/crops/demo-tab-focus-visible.png) ![Signal-group tab pressed](components/crops/demo-tab-pressed.png) ![Signal-group tab opened](components/crops/demo-tab-opened.png)

### Product pages

The product marketing pages (/products/identification and siblings): the masthead, the demo <select>, and CTAs.

#### Product headline
"Device identification_" — the /products/identification masthead. Read as `prod-h1` on the identification page.

**Values (default).** size 175.16 x 20; background transparent; text JetBrains Mono-c3e9177549e38394 13/20 500, #6b6c6a `core.color.gray.800`.

![Product headline default](components/crops/prod-h1-default.png)

#### Demo select
The native <select> in the page's interactive identification demo (a region/device picker); measured at rest, never changed. Read as `prod-select` on the identification page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 76 x 22; background transparent; text Inter-c0aaf1024c6c51d7 16/normal 400, #000000 `light.theme.ink.default` |
| focused | outline 1px auto #101010, offset 0px; layers select 76.0x22.0 1px auto rgb(16, 16, 16) offset 0px |

![Demo select default](components/crops/prod-select-default.png) ![Demo select focused](components/crops/prod-select-focused.png)

#### Product CTA
A "Get started" call-to-action on the product page; measured, never followed. Read as `prod-cta` on the identification page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 109 x 32; padding 0px 14px; border 1px solid #f35b22 `light.action.submitFill`; radius 6px; background #fefefd; text Inter-c0aaf1024c6c51d7 12/16 500, #f35b22 `light.action.submitFill`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #fff3ef |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px |

![Product CTA default](components/crops/prod-cta-default.png) ![Product CTA hover](components/crops/prod-cta-hover.png) ![Product CTA focus-visible](components/crops/prod-cta-focus-visible.png) ![Product CTA pressed](components/crops/prod-cta-pressed.png)

### Blog and resource indexes

The /blog index (article cards, the newsletter field and Subscribe button), the /resources, /case-studies and /careers surfaces and the /about-us values cards.

#### Blog headline
"Fingerprint Blog" — the /blog index masthead. Read as `blog-h1` on the blog page.

**Values (default).** size 1248 x 37.44; background transparent; text JetBrains Mono 32/37.44 700, #141415.

![Blog headline default](components/crops/blog-h1-default.png)

#### Article card
An article card in the blog index; measured, never followed. Read as `blog-card` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 290.66 x 206.31; background transparent; text Inter 14/21 400, #141415 |

![Article card default](components/crops/blog-card-default.png) ![Article card hover](components/crops/blog-card-hover.png)

#### Blog subscribe field
The newsletter e-mail input on the blog index; focused and typed into then cleared — never subscribed. Read as `blog-subscribe` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 370 x 57; padding 16px; radius 6px; background #ffffff `light.theme.ink.inverse`; shadow #c4cdd5 0px 0px 0px 1px; text Inter 16/21 400, #000000 `light.theme.ink.default`; placeholder #5b5b5b |
| focused, filled | shadow #ff5e24 0px 0px 0px 2px |

![Blog subscribe field default](components/crops/blog-subscribe-default.png) ![Blog subscribe field focused](components/crops/blog-subscribe-focused.png) ![Blog subscribe field filled](components/crops/blog-subscribe-filled.png)

#### Blog subscribe button
The blog subscribe button; measured, never pressed. Read as `blog-subscribe-btn` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 109 x 57; padding 10px 20px; border 1px solid #be400f; radius 6px; background #f35b22 `light.action.submitFill`; shadow rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset, rgba(24, 25, 22, 0.06) 0px 1px 2px 0px, rgba(24, 25, 22, 0.1) 0px -1px 0px 0px inset; text Inter 14/19.6 500, #ffffff `light.theme.ink.inverse`; transition background-color 0.25s ease, border 0.25s ease, opacity 0.25s ease, color 0.25s ease |
| hover | background #be400f |
| focus-visible | outline 2px solid #f35b22 `light.action.submitFill`, offset 2px |
| pressed | background #be400f |

![Blog subscribe button default](components/crops/blog-subscribe-btn-default.png) ![Blog subscribe button hover](components/crops/blog-subscribe-btn-hover.png) ![Blog subscribe button focus-visible](components/crops/blog-subscribe-btn-focus-visible.png) ![Blog subscribe button pressed](components/crops/blog-subscribe-btn-pressed.png)

#### Careers headline
The /careers masthead. Read as `careers-h1` on the careers page.

**Values (default).** size 1248 x 64; padding 0px 0px 8px 0px; background transparent; text Inter-c0aaf1024c6c51d7 48/56 500, #000000 `light.theme.ink.default`.

![Careers headline default](components/crops/careers-h1-default.png)

#### Resources headline
The /resources resource-center masthead. Read as `res-h1` on the resources page.

**Values (default).** size 744 x 67.2; background transparent; text Inter 56/67.2 600, #141415.

![Resources headline default](components/crops/res-h1-default.png)

#### Resource card
A resource card on the /resources index — an anchor holding a thumbnail and a kicker label (ARTICLE/TUTORIAL/..., painted by text-transform); measured, never followed. Read as `res-card` on the resources page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 296 x 390.97; border 1px solid #e8e8e8; radius 6px; background #ffffff `light.theme.ink.inverse`; shadow rgba(209, 209, 209, 0.15) 0px 2px 4px 0px; text JetBrains Mono 11/16 400, #f5614b; transition box-shadow 0.25s ease, border 0.25s ease |
| hover | border 1px solid transparent; shadow rgba(20, 20, 21, 0.02) 0px 100px 80px 0px, rgba(20, 20, 21, 0.02) 0px 42px 33px 0px, rgba(20, 20, 21, 0.03) 0px 22px 18px 0px, rgba(20, 20, 21, 0.03) 0px 12px 10px 0px, rgba(20, 20, 21, 0.04) 0px 7px 6px 0px, rgba(115, 115, 115, 0.15) 0px 0px 1px 0px, rgba(20, 20, 21, 0.02) 0px 3px 2px 0px |

![Resource card default](components/crops/res-card-default.png) ![Resource card hover](components/crops/res-card-hover.png)

#### Case-studies headline
The /case-studies index masthead. Read as `cs-h1` on the case-studies page.

**Values (default).** size 1248 x 67.2; background transparent; text Inter-c0aaf1024c6c51d7 56/67.2 600, #171816 `core.color.gray.1000`.

![Case-studies headline default](components/crops/cs-h1-default.png)

#### Case-study card
A case-study card on the index; measured, never followed. Read as `cs-card` on the case-studies page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 402.66 x 405.67; border 1px solid #e8e8e8; radius 6px; background #ffffff `light.theme.ink.inverse`; shadow rgba(208, 208, 208, 0.15) 0px 2px 4px 0px; text Inter-c0aaf1024c6c51d7 20/28 600, #171816 `core.color.gray.1000`; transition box-shadow 0.2s ease, border-color 0.2s ease |
| hover | border 1px solid transparent; shadow rgba(20, 20, 21, 0.02) 0px 100px 80px 0px, rgba(20, 20, 21, 0.02) 0px 42px 33px 0px, rgba(20, 20, 21, 0.03) 0px 22px 18px 0px, rgba(20, 20, 21, 0.03) 0px 12px 10px 0px, rgba(20, 20, 21, 0.04) 0px 7px 6px 0px, rgba(114, 114, 115, 0.15) 0px 0px 1px 0px, rgba(20, 20, 21, 0.02) 0px 3px 2px 0px |

![Case-study card default](components/crops/cs-card-default.png) ![Case-study card hover](components/crops/cs-card-hover.png)

#### About headline
"About us" — the /about-us masthead. Read as `about-h1` on the about-us page.

**Values (default).** size 244 x 67.19; background transparent; text Inter-c0aaf1024c6c51d7 56/67.2 600, #141415.

![About headline default](components/crops/about-h1-default.png)

#### Value card heading
A "Our Values" card heading (No Nonsense., Fail. Learn. Grow., Be level 5 helpful.). Read as `about-value` on the about-us page.

**Values (default).** size 288 x 28; background transparent; text Inter-c0aaf1024c6c51d7 20/28 500, #141415.

![Value card heading default](components/crops/about-value-default.png)

#### Careers CTA
The "Explore Our Jobs" button on /careers — a local anchor to the jobs list; measured, never followed. Read as `careers-cta` on the careers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 138.66 x 32; padding 8px 12px; border 1px solid #bd400f `light.theme.action.primaryHover`; radius 6px; background #f35820 `light.theme.action.primary`; shadow rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.02) 0px -1px 0px 0px inset, rgba(23, 24, 22, 0.03) 0px 1px 2px 0px; text Inter-c0aaf1024c6c51d7 14/20 500, #ffffff `light.theme.ink.inverse`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #bd400f `light.theme.action.primaryHover` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.02) 0px -1px 0px 0px inset, rgba(23, 24, 22, 0.03) 0px 1px 2px 0px |

![Careers CTA default](components/crops/careers-cta-default.png) ![Careers CTA hover](components/crops/careers-cta-hover.png) ![Careers CTA focus-visible](components/crops/careers-cta-focus-visible.png) ![Careers CTA pressed](components/crops/careers-cta-pressed.png)

### Docs site (Mintlify)

docs.fingerprint.com — a Mintlify docs site with its own token layer and a real light/dark preference: the 'Open search' trigger, the 'Change theme preference' button (never switched), nav tabs, sidebar links and code blocks.

#### Doc page headline
"Quick Start Guide" — a docs article headline on the Mintlify stack. Read as `docs-h1` on the docs article page.

**Values (default).** size 294.7 x 40; background transparent; text Inter 36/40 500, #181916 `light.form.fieldInk`.

![Doc page headline default](components/crops/docs-h1-default.png)

#### Docs nav tab
A docs top-nav tab (Home/Start/AI/Guides/API Reference/Changelogs); measured, never followed. Read as `docs-nav-tab` on the docs landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 56.59 x 48; background transparent; text Inter 14/20 500, #8b8b89 `core.color.gray.700`; icon 16 x 16, #8b8b89 `core.color.gray.700` |
| hover | text Inter 14/20 500, #484946 `core.color.gray.900`; icon 16 x 16, #484946 `core.color.gray.900` |

![Docs nav tab default](components/crops/docs-nav-tab-default.png) ![Docs nav tab hover](components/crops/docs-nav-tab-hover.png)

#### Search trigger
The docs' "Open search" button — a local UI toggle for the search overlay; measured, never opened. Read as `docs-search` on the docs article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 437.33 x 36; padding 0px 12px; radius 4px; background #f8f8f6 `core.color.gray.100`; shadow #d9d9d6 0px 0px 0px 1px; text Inter 14/24 400, #a0a09d `light.form.placeholder`; icon 16 x 16, #6b6c69 |
| hover | icon 16 x 16, #484946 `core.color.gray.900` |
| focus-visible | outline 1px auto #f35b22 `light.action.submitFill`, offset 0px |
| pressed | icon 16 x 16, #484946 `core.color.gray.900` |

![Search trigger default](components/crops/docs-search-default.png) ![Search trigger hover](components/crops/docs-search-hover.png) ![Search trigger focus-visible](components/crops/docs-search-focus-visible.png) ![Search trigger pressed](components/crops/docs-search-pressed.png)

#### Theme toggle
The docs' "Change theme preference" button — a local UI toggle that flips data-theme-preference between light and dark; measured at rest, never switched here (the dark surface is captured in the screenshots pass). Read as `docs-theme-btn` on the docs article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 32; padding 8px; radius 8px; background transparent; text Inter 14/20 400, oklab(0.211125 -0.00315349 0.00507477 / 0.5) |
| focus-visible | outline 1px auto #f35b22 `light.action.submitFill`, offset 0px; layers button.group.disabled:pointer-events-none 32.0x32.0 1px auto rgb(243, 91, 34) offset 0px 8px |

![Theme toggle default](components/crops/docs-theme-btn-default.png) ![Theme toggle hover](components/crops/docs-theme-btn-hover.png) ![Theme toggle focus-visible](components/crops/docs-theme-btn-focus-visible.png) ![Theme toggle pressed](components/crops/docs-theme-btn-pressed.png)

#### Sidebar link
A sidebar navigation link in the docs tree; measured, never followed. Read as `docs-side-link` on the docs article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 256 x 36; padding 6px 12px 6px 16px; radius 4px; background oklab(0.664739 0.154526 0.123505 / 0.1); text Inter 14/24 400, #f35b22 `light.action.submitFill`; icon 16 x 16, #f35b22 `light.action.submitFill` |

![Sidebar link default](components/crops/docs-side-link-default.png) ![Sidebar link hover](components/crops/docs-side-link-hover.png)

#### Code block
A code block on the docs article; the site's .dark syntax-highlight scope paints these. Read as `docs-code` on the docs article page.

**Values (default).** size 656.81 x 24; background transparent; shadow rgba(59, 130, 246, 0.5) 0px 0px 0px 0px; text paperMono 14/24 400, #f69d50; layers pre.shiki.shiki-themes 656.8x24.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px; code 656.8x24.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0.

![Code block default](components/crops/docs-code-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the header with the 'Mobile Menu' button, the full-viewport nav overlay, the hero and the CTA.

#### Mobile top bar
The phone header at 390 wide: the wordmark, the CTA and the "Mobile Menu" button. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 390 x 56; background oklab(0.999994 0.0000455677 0.0000200868 / 0.8); shadow rgba(24, 25, 22, 0.06) 0px 1px 2px 0px; text Inter-c0aaf1024c6c51d7 16/24 400, #000000 `light.theme.ink.default`.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile menu button
The "Mobile Menu" button — a local UI toggle; the opened state was measured after activating it. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 16 x 16; background transparent; text Inter-c0aaf1024c6c51d7 16/24 400, #000000 `light.theme.ink.default`; layers span.absolute.left-0 16.0x2.0 rgb(32, 32, 33); span.absolute.left-0 16.0x2.0 rgb(32, 32, 33); span.absolute.left-0 16.0x2.0 rgb(32, 32, 33); span.absolute.left-0 16.0x2.0 rgb(32, 32, 33) |
| focus-visible | outline 1px auto #e59700, offset 0px; layers button.relative.ml-4 16.0x16.0 1px auto rgb(229, 151, 0) offset 0px; span.absolute.left-0 16.0x2.0 rgb(32, 32, 33); span.absolute.left-0 16.0x2.0 rgb(32, 32, 33); span.absolute.left-0 16.0x2.0 rgb(32, 32, 33); span.absolute.left-0 16.0x2.0 rgb(32, 32, 33) |
| opened | layers span.absolute.block 0.0x2.0 rgb(32, 32, 33); span.absolute.left-0 12.7x12.7 rgb(32, 32, 33); span.absolute.left-0 12.7x12.7 rgb(32, 32, 33); span.absolute.block 0.0x2.0 rgb(32, 32, 33) |

Child layers that carry the look: span 16x2 background #202021; span 16x2 background #202021; span 16x2 background #202021.

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png) ![Mobile menu button opened](components/crops/m-menu-btn-opened.png)

#### Mobile nav overlay
The navigation overlay opened by the menu button (the same destinations as the desktop header); its links were never followed. Read as `m-drawer` on the home page at 390 wide.

**Values (default).** size 350 x 812; background transparent; text Inter-c0aaf1024c6c51d7 12/12 400, #89898a; layers span.inline-flex.items-center 74.0x20.0 rgb(255, 255, 255) T:1px solid rgb(255, 202, 181) / R:1px solid rgb(255, 202, 181) / B:1px solid rgb(255, 202, 181) / L:1px solid rgb(255, 202, 181) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(190, 64, 15, 0.1) 0px -1px 0px 0px inset, rgba(255, 255, 255, 0.1) 0px.

Child layers that carry the look: span 74x20 background #ffffff `light.theme.ink.inverse` image linear-gradient(301deg, rgba(243, 91, 34, 0.01) 9.55%, rgba(243, 91, 34, 0.1) 67.28%) border 1px solid #ffcab5 radius 5px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(190, 64, 15, 0.1) 0px -1px 0px 0px inset, rgba(255, 255, 255, 0.1) 0px 1.5px 0px 0px inset, rgba(0, 0, 0, 0.03) 0px 0.5px 0px 0px.

![Mobile nav overlay default](components/crops/m-drawer-default.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 348 x 80; padding 0px 0px 0px 12px; background transparent; text Inter-c0aaf1024c6c51d7 32/40 500, #000000 `light.theme.ink.default`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile CTA
A "Get Started" action at 390 wide (the header pill is hidden on phones); measured never followed. Read as `m-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 141 x 34.8; padding 8px 14px; border 1px solid #bd400f `light.theme.action.primaryHover`; radius 6px; background #f35820 `light.theme.action.primary`; shadow rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset, rgba(24, 25, 22, 0.06) 0px 1px 2px 0px, rgba(24, 25, 22, 0.1) 0px -1px 0px 0px inset; text Inter-c0aaf1024c6c51d7 12/16.8 500, #ffffff `light.theme.ink.inverse`; transition background-color 0.25s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.25s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.25s cubic-bezier(0.4, 0, 0.2, 1), color 0.25s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.25s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 2px solid #f35820 `light.theme.action.primary`, offset 2px |

![Mobile CTA default](components/crops/m-cta-default.png) ![Mobile CTA hover](components/crops/m-cta-hover.png) ![Mobile CTA focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile CTA pressed](components/crops/m-cta-pressed.png)

### Footer

The page footer: sitemap columns, social icons and the newsletter field with 'Subscribe to newsletter' — typed into then cleared, never subscribed.

#### Footer
The page footer: the newsletter subscribe field, the Product/Use Cases/Resources/Developers columns, social icons and company links. Read as `footer` on the home page.

**Values (default).** size 1440 x 516; border T: 1px solid #e8e8e8; background #ffffff `light.theme.ink.inverse`; text Inter-c0aaf1024c6c51d7 14/21 400, #6e6f6c; icon 14 x 14, #a0a09d `light.form.placeholder`.

![Footer default](components/crops/footer-default.png)

#### Newsletter field
The "Email address*" subscribe input in the footer; focused and typed into then cleared — never subscribed. Read as `newsletter-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 211 x 21; background transparent; text Inter-c0aaf1024c6c51d7 14/21 400, #6e6f6c; placeholder rgba(24, 25, 22, 0.5) |

![Newsletter field default](components/crops/newsletter-field-default.png) ![Newsletter field focused](components/crops/newsletter-field-focused.png) ![Newsletter field filled](components/crops/newsletter-field-filled.png)

#### Subscribe button
The newsletter subscribe button; its states were measured but the button was never clicked — nothing was submitted. Read as `subscribe-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 44 x 44; background transparent; text Inter-c0aaf1024c6c51d7 14/21 400, #a0a09d `light.form.placeholder`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, #a0a09d `light.form.placeholder` |
| focus-visible | outline 1px auto #101010, offset 0px; text Inter-c0aaf1024c6c51d7 14/21 400, #f35b22 `light.action.submitFill`; icon 14 x 14, #f35b22 `light.action.submitFill`; layers button.flex.min-h-[44px] 44.0x44.0 1px auto rgb(16, 16, 16) offset 0px |

![Subscribe button default](components/crops/subscribe-btn-default.png) ![Subscribe button hover](components/crops/subscribe-btn-hover.png) ![Subscribe button focus-visible](components/crops/subscribe-btn-focus-visible.png) ![Subscribe button pressed](components/crops/subscribe-btn-pressed.png)

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 168 x 21; background transparent; text Inter-c0aaf1024c6c51d7 14/21 400, #6e6f6c; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.7 |
| focus-visible | outline 2px solid #f35820 `light.theme.action.primary`, offset 2px; layers a.inline-flex.items-center 168.0x21.0 2px solid rgb(243, 88, 32) offset 2px |
| pressed | opacity 0.7 |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Fingerprint mark, the dropdown glyphs, social glyphs, partner logos) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Fingerprint's product is the dashboard: API keys, the events and signals explorer, playground, billing and every surface after `Log In` needs an account and was never reached. dashboard.fingerprint.com /login and /signup are the only app surfaces a signed-out visitor sees, and they were measured as forms, never submitted. The /demo page's live signal panel IS the product's public demo — it paints the capture machine's own visitor ID, IP and geolocation, so those regions are masked in the committed shots.

### Pages

- **The account.** The dashboard and every post-login surface (API keys, events explorer, playground, billing) was never reached; the /login and /signup cards were measured as forms and never submitted; 'Continue with Google/GitHub/Microsoft' were never followed.
- **Forms.** The /contact-sales form, the footer and blog newsletter fields and the demo's fake checkout were measured at rest and typed into then cleared — nothing was sent; what a submission returns is unverified.
- **Blog posts, case studies, docs articles and use-case pages** are index- or exemplar-level captures; sibling articles share the templates, unmeasured.
- **The bot directory, integrations and SDK lists** were captured as index pages; per-entry detail pages were not captured.
- **Product dropdown panels** for 'Use Cases' and 'Resources' were screenshot-captured only; only the Product panel's contents were component-measured.
- **The 'Before Pro / After Pro' comparison toggle** on /products/identification is IntersectionObserver-gated and did not paint during measurement — the element exists but never became visible.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **The pricing slider** re-prices the grid when dragged; it was measured at rest, so alternate volumes' prices are uncaptured.
- **The docs theme preference** was never held in the dark position; the docs dark surface is captured as screenshots instead of measured states.

### Themes

Every public fingerprint.com marketing page paints the `:root` light token layer — the FPDS ramps and `--color-*` aliases resolve identically under an emulated `prefers-color-scheme: dark` (the `dark:` utilities the stylesheet ships are vestigial), and no page carries a `data-theme` attribute or a theme control. The only dark redeclaration the stylesheets ship is the `.dark`-scoped `--fpds-color-syntax-*` set — eleven code-highlighting colours re-pointed at lighter ramp steps, which is the `dark` token set, labelled as declared-not-painted. docs.fingerprint.com is a different stack (Mintlify) with a real light/dark preference; its dark surface is captured in the `docs-*-theme-dark` screenshots.

### Fonts

- **Inter** (400-700) carries every heading, control and body; **Petrona** is the serif display face on editorial sections; **JetBrains Mono** draws code, prompts and signal values; **Geist Pixel** is the pixel display face — all self-hosted under /_astro with hashed family names and system fallbacks. The style guide falls back to system fonts.

### Screenshots

- The product demos, the IdentifySection panels, partner logos and photography in the screenshots are the product's published content; the live-signal regions that painted this machine's visitor ID, IP and location are masked (tools/redact-rules/fingerprint.json).
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, plan prices, job titles, partner names and customer names are the product's content; only frames and components were measured.
