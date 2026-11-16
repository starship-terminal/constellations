# Fourthwall components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from fourthwall.com, products.fourthwall.com, docs.fourthwall.com, help.fourthwall.com and the /get-started auth shell on 2026-11-16, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought, designed or submitted; the auth choices and 'Sign in to design' were never pressed; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (101 components, 201 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value in the component's own surface set (light+core marketing / ink / catalog / docs / help and their dark sets — the hosts carry separate vocabularies), when there is one. Text is written family size/line-height weight, then its colour, for example `Suisse Intl 17/28 420, #0a0a0a`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (204 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the surface painted at capture: `light` for the marketing pages, the catalogue and docs/help in light — the marketing site is one light surface (its dark bands are scoped on-ink sections, not a theme); `dark` for the docs quickstart under `html.dark` (the site's own 'Change theme preference' menu) and the help category under `data-theme=dark` (its own colour-mode toggle). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [mega-menu](screenshots/home-light-mega-menu.png) |
| Pricing | `/pricing` | [billing-monthly](screenshots/pricing-light-billing-monthly.png), [default](screenshots/pricing-light-default.png), [faq-open](screenshots/pricing-light-faq-open.png), [full](screenshots/pricing-light-full.png) |
| FAQ | `/faq` | [default](screenshots/faq-light-default.png), [full](screenshots/faq-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Compare | `/compare` | [default](screenshots/compare-light-default.png), [full](screenshots/compare-light-full.png), [search](screenshots/compare-light-search.png) |
| Comparison (vs Shopify) | `/compare/fourthwall-vs-shopify` | [default](screenshots/compare-shopify-light-default.png), [full](screenshots/compare-shopify-light-full.png) |
| Shops | `/shops` | [default](screenshots/shops-light-default.png), [full](screenshots/shops-light-full.png) |
| Get inspired | `/get-inspired` | [default](screenshots/get-inspired-light-default.png), [full](screenshots/get-inspired-light-full.png) |
| Features | `/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| Memberships | `/memberships` | [default](screenshots/memberships-light-default.png), [full](screenshots/memberships-light-full.png) |
| Contact | `/contact` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Get started (auth shell) | `/get-started → auth.fourthwall.com` | [default](screenshots/signup-light-default.png) |
| Catalogue home | `products.fourthwall.com` | [default](screenshots/catalog-light-default.png), [full](screenshots/catalog-light-full.png), [quiz-answer](screenshots/catalog-light-quiz-answer.png), [search](screenshots/catalog-light-search.png) |
| Product page | `products.fourthwall.com/comfort-colors-…-dtg` | [default](screenshots/catalog-pdp-light-default.png), [full](screenshots/catalog-pdp-light-full.png), [size-guide](screenshots/catalog-pdp-light-size-guide.png) |
| Catalogue /all | `products.fourthwall.com/all` | [default](screenshots/catalog-all-light-default.png), [full](screenshots/catalog-all-light-full.png) |
| Docs home | `docs.fourthwall.com` | [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png), [search](screenshots/docs-light-search.png), [theme-menu](screenshots/docs-light-theme-menu.png) |
| Docs quickstart | `docs.fourthwall.com/quickstart` | [default](screenshots/docs-quickstart-light-default.png), [full](screenshots/docs-quickstart-light-full.png) |
| Docs quickstart, dark | `docs.fourthwall.com/quickstart` | [default](screenshots/docs-dark-dark-default.png), [full](screenshots/docs-dark-dark-full.png) |
| Help home | `help.fourthwall.com` | [default](screenshots/help-light-default.png), [full](screenshots/help-light-full.png), [search](screenshots/help-light-search.png) |
| Help category | `help.fourthwall.com/category/setting-up-your-shop` | [default](screenshots/help-category-light-default.png), [full](screenshots/help-category-light-full.png) |
| Help category, dark | `help.fourthwall.com/category/setting-up-your-shop` | [default](screenshots/help-dark-dark-default.png), [full](screenshots/help-dark-dark-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Catalogue, phone | `products.fourthwall.com` | [default](screenshots/mobile-catalog-light-default.png), [full](screenshots/mobile-catalog-light-full.png) |
| Help category, phone | `help.fourthwall.com/category/setting-up-your-shop` | [default](screenshots/mobile-help-light-default.png), [full](screenshots/mobile-help-light-full.png), [menu](screenshots/mobile-help-light-menu.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Consent overlay | marketing + docs pages | the Osano cookie-consent layer (.cc_div/#cc-main) is hidden before every shot and reading — never answered | hidden, never answered |
| Features mega-menu | nav bar | hovered the 'Features' nav item | [home-light-mega-menu](screenshots/home-light-mega-menu.png), [mega-clip](#mega-menu-panel) |
| Signup modal | nav Start now | the nav 'Start now' control navigates to /get-started on this build — the modal was not reachable as a local toggle; the auth shell was shot instead | [signup-light-default](screenshots/signup-light-default.png); boundary, see Gaps |
| Billing toggle | pricing | clicked 'Pay monthly' — a local toggle that repaints the plan prices | [pricing-light-billing-monthly](screenshots/pricing-light-billing-monthly.png), [billing-toggle](#billing-toggle) |
| FAQ disclosure | pricing | clicked one .ph-faq-summary | [pricing-light-faq-open](screenshots/pricing-light-faq-open.png), [faq-summary](#faq-disclosure) |
| Compare search | /compare | typed 'shopify' into the platform search then cleared it | [compare-light-search](screenshots/compare-light-search.png), [cmp-search](#platform-search) |
| Catalogue search | products.fourthwall.com | typed 'hoodie' into the search then cleared it | [catalog-light-search](screenshots/catalog-light-search.png), [cat-search](#catalogue-search) |
| Quiz option | products.fourthwall.com | clicked one product-finder answer — a local selection, nothing submitted | [catalog-light-quiz-answer](screenshots/catalog-light-quiz-answer.png), [quiz-option](#quiz-option) |
| Size-guide dialog | product page | clicked 'Size guide' — a local dialog toggle | [catalog-pdp-light-size-guide](screenshots/catalog-pdp-light-size-guide.png), [pdp-sizeguide](#size-guide-dialog) |
| Docs search | docs.fourthwall.com | clicked the search — the cmdk dialog opened; typed 'auth' | [docs-light-search](screenshots/docs-light-search.png), [docs-search-dialog](#search-dialog) |
| Docs theme menu | docs.fourthwall.com | clicked 'Change theme preference' | [docs-light-theme-menu](screenshots/docs-light-theme-menu.png), [docs-theme-btn](#theme-menu-button) |
| Docs dark mode | docs.fourthwall.com | chose Dark in the site's own theme menu — html.dark painted | [docs-dark-dark-default](screenshots/docs-dark-dark-default.png) |
| Help search | help.fourthwall.com | typed 'storefront' into the navbar search then cleared it | [help-light-search](screenshots/help-light-search.png) |
| Help dark mode | help.fourthwall.com | clicked the navbar colour-mode toggle — data-theme=dark painted | [help-dark-dark-default](screenshots/help-dark-dark-default.png) |
| Auth providers | /get-started → auth.fourthwall.com | the Google/Apple/email choices were measured at rest — never pressed, no OAuth flow started | [auth-card](#auth-card); boundary, see Gaps |
| Sign in to design | product page | the PDP's design action starts an auth flow; measured, never pressed | [pdp-design-cta](#sign-in-to-design-cta); boundary, see Gaps |
| Signed-in product | a Fourthwall account | every post-login surface (the shop dashboard, the designer, checkout) needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 26 components were given a real keyboard focus. 26 draw an outline ring: `nav-features` (1px auto #101010, offset 1px), `nav-link` (1px auto #101010, offset 1px), `nav-login` (1px auto #101010, offset 1px), `footer-link` (1px auto #101010, offset 1px), `billing-btn` (1px auto #101010, offset 0px), `faq-summary` (1px auto #101010, offset 0px), `auth-google` (2px solid #161712 `bg.brand.default`, offset 2px), `auth-apple` (2px solid #161712 `bg.brand.default`, offset 2px), `auth-email` (2px solid #161712 `bg.brand.default`, offset 2px), `auth-login` (1px auto #101010, offset 1px), `quiz-option` (1px auto #101010, offset 0px), `pdp-swatch` (1px auto #101010, offset 0px), `pdp-sizeguide-btn` (1px auto #101010, offset 0px), `pdp-design-cta` (2px solid #161712 `bg.brand.default`, offset 2px), `docs-search` (1px auto #000000 `color.black`, offset 0px), `docs-theme-btn` (1px auto #000000 `color.black`, offset 0px), `docs-side-item` (1px auto #000000 `color.black`, offset -2px), `docs-anchor` (1px auto #000000 `color.black`, offset -2px), `help-theme` (1px auto #101010, offset 0px), `help-fw-link` (1px auto #101010, offset 1px), `help-side-item` (1px auto #101010, offset 1px), `help-doc-link` (1px auto #101010, offset 1px), `m-menu-btn` (1px auto #e59700, offset 0px), `closer-cta` (1px auto #101010, offset 1px), `nav-cta` (1px auto #101010, offset 1px), `hero-cta` (1px auto #101010, offset 1px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease` | background-color, border-color | quiz-option |
| 0.15s | `ease` | background-color, color | hd-card, help-side-item |
| 0.2s | `cubic-bezier(0.08, 0.52, 0.52, 1)` | background, color | help-card, help-doc-link, help-fw-link |
| 0.2s | `ease` | background, box-shadow, color, text-decoration-color | billing-btn, blog-card, blog-news, closer-cta, contact-card, footer-link, help-theme, hero-cta and more |
| 0.25s | `cubic-bezier(0.22, 1, 0.36, 1)` | opacity, scale, transform | docs-search-dialog |
| 0.32s | `ease` | background-color, color | m-nav, mkt-logo, mkt-nav, nav-cta, nav-features, nav-link, nav-login |
| 0.4s | `cubic-bezier(0.16, 1, 0.3, 1)` | transform | plan-card |
| 0.9s | `cubic-bezier(0.16, 1, 0.3, 1)` | transform | cmpart-card |
| 1.1s | `cubic-bezier(0.16, 1, 0.3, 1)` | opacity, transform, translate | cmp-card, plan-card |
| 1.8s | `cubic-bezier(0.16, 1, 0.3, 1)` | opacity, transform | design-preview, shops-tile, tile |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Product tile](#product-tile) | 336.88 x 428.31 | - | - | #f6f6f6 `_primitives.color.paper.soft` | none | 24px |
| [Plan card](#plan-card) | 544 x 613.53 | - | - | #18181b `_primitives.color.ink.deep` | none | 40px |
| [Product card](#product-card) | 243.19 x 323.44 | - | - | transparent | none | 0 |
| [Category link](#category-link) | 252 x 24 | - | - | transparent | none | 0 |
| [Docs card](#docs-card) | 336.41 x 182 | 1px solid oklab(0.144787 0.00000661612 0.00000289828 / 0.1) | 16px | #ffffff `color.white` | none | 0 |
| [Rating chip](#rating-chip) | 50 x 20 | - | 999px | #ffffff `_primitives.color.paper.default` | none | 4px 10px 4px 8px |
| [Auth card](#auth-card) | 440 x 176 | - | - | transparent | none | 0 |
| [Shop tile](#shop-tile) | 432 x 475.31 | - | - | transparent | none | 0 |
| [Creator card](#creator-card) | 432 x 358.94 | - | - | transparent | none | 0 |
| [Comparison card](#comparison-card) | 1360 x 161.44 | B: 1px solid rgba(10, 10, 10, 0.16) `_primitives.color.ink.alpha.16` | - | transparent | none | 32px 0px |

## Components

### Site chrome

The fixed .nav-bar on every marketing page: the Fourthwall wordmark, the Features mega-menu and Learn dropdowns, Product catalog / Pricing links, Log in and the 'Start now' pill.

#### Nav bar
The fixed top bar: the Fourthwall wordmark, the Features mega-menu and Learn dropdowns, Product catalog / Pricing links, Log in and the "Start now" pill. Read as `mkt-nav` on the home page.

**Values (default).** size 1440 x 71.03; padding 14px 40px; background transparent; text Suisse Intl 16.99/28.04 450, #ffffff `_primitives.color.paper.default`; transition color 0.32s ease; layers ::before rgb(10, 10, 10) 0px none 0; nav::before.nav-bar.is-warm 1440pxx71.0312px rgb(10, 10, 10); a::after.nav-link 89.5156pxx1px rgb(255, 255, 255); a::after.mega-link 128pxx1px rgb(255, 255, 255); a::after.mega-link 138pxx1px rgb(255, 255, 255); a::after.mega-link 199pxx1px rgb(255, 255, 255); a::after.mega-link 127pxx1px rgb(255, 255, 255).

Child layers that carry the look: nav::before 1440pxx71.0312px background #0a0a0a `_primitives.color.ink.default`; a::after 89.5156pxx1px background #ffffff `_primitives.color.paper.default`; a::after 128pxx1px background #ffffff `_primitives.color.paper.default`.

![Nav bar default](components/crops/mkt-nav-default.png)

#### Wordmark
The Fourthwall wordmark in the nav, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 124.3 x 24; background transparent; text Suisse Intl 16.99/28.04 400, #ffffff `_primitives.color.paper.default`; transition background-color 0.32s ease, color 0.32s ease.

![Wordmark default](components/crops/mkt-logo-default.png)

#### Mega-menu trigger
The "Features" nav item that opens the mega-menu on hover; its links were never followed. Read as `nav-features` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 89.52 x 36.05; padding 4px 0px; background transparent; text Suisse Intl 16.99/28.04 450, #ffffff `_primitives.color.paper.default`; transition background-color 0.32s ease, color 0.32s ease; icon 12.58 x 8.48, #ffffff `_primitives.color.paper.default`; layers ::after rgb(255, 255, 255) 0px none 1; a::after.nav-link 89.5156pxx1px rgb(255, 255, 255) |
| hover | transition none; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgb(255, 255, 255) 0px none 1; a::after.nav-link 89.5156pxx1px rgb(255, 255, 255) |
| focus-visible | outline 1px auto #101010, offset 1px; transition none; layers ::after rgb(255, 255, 255) 0px none 1; a.nav-link 89.5x36.0 1px auto rgb(16, 16, 16) offset 1px; a::after.nav-link 89.5156pxx1px rgb(255, 255, 255) |

Child layers that carry the look: a::after 89.5156pxx1px background #ffffff `_primitives.color.paper.default`.

![Mega-menu trigger default](components/crops/nav-features-default.png) ![Mega-menu trigger hover](components/crops/nav-features-hover.png) ![Mega-menu trigger focus-visible](components/crops/nav-features-focus-visible.png) ![Mega-menu trigger pressed](components/crops/nav-features-pressed.png)

#### Nav link
A marketing nav link (Pricing); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 56 x 36.05; padding 4px 0px; background transparent; text Suisse Intl 16.99/28.04 450, #ffffff `_primitives.color.paper.default`; transition background-color 0.32s ease, color 0.32s ease; layers ::after rgb(255, 255, 255) 0px none 1; a::after.nav-link 56pxx1px rgb(255, 255, 255) |
| focus-visible | outline 1px auto #101010, offset 1px; layers ::after rgb(255, 255, 255) 0px none 1; a.nav-link 56.0x36.0 1px auto rgb(16, 16, 16) offset 1px; a::after.nav-link 56pxx1px rgb(255, 255, 255) |

Child layers that carry the look: a::after 56pxx1px background #ffffff `_primitives.color.paper.default`.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log in link
The "Log in" nav link to the shop admin; measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 49 x 36.05; padding 4px 0px; background transparent; text Suisse Intl 16.99/28.04 450, #ffffff `_primitives.color.paper.default`; transition background-color 0.32s ease, color 0.32s ease; layers ::after rgb(255, 255, 255) 0px none 1; a::after.nav-login 49pxx1px rgb(255, 255, 255) |
| focus-visible | outline 1px auto #101010, offset 1px; layers ::after rgb(255, 255, 255) 0px none 1; a.nav-login 49.0x36.0 1px auto rgb(16, 16, 16) offset 1px; a::after.nav-login 49pxx1px rgb(255, 255, 255) |

Child layers that carry the look: a::after 49pxx1px background #ffffff `_primitives.color.paper.default`.

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Mega-menu panel
The Features mega-menu panel — nav columns plus featured cards; opened by hovering its own trigger. Read as `mega-clip` on the home page.

**Values (default).** size 1440 x 431.08; background transparent; text Suisse Intl 16.99/28.04 450, #ffffff `_primitives.color.paper.default`; layers a::after.mega-link 128pxx1px rgb(255, 255, 255); a::after.mega-link 138pxx1px rgb(255, 255, 255); a::after.mega-link 199pxx1px rgb(255, 255, 255); a::after.mega-link 127pxx1px rgb(255, 255, 255); a::after.mega-link 119pxx1px rgb(255, 255, 255); a::after.mega-link 102pxx1px rgb(255, 255, 255).

Child layers that carry the look: a::after 128pxx1px background #ffffff `_primitives.color.paper.default`; a::after 138pxx1px background #ffffff `_primitives.color.paper.default`; a::after 199pxx1px background #ffffff `_primitives.color.paper.default`.

![Mega-menu panel default](components/crops/mega-clip-default.png)

#### Start now button
The "Start now" pill in the nav — it links to /get-started; measured, never activated. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 116 x 43.03; padding 12px 20px; radius 12px; background #ffffff `_primitives.color.paper.default`; text Suisse Intl 16.99/19.03 450, #0a0a0a `_primitives.color.ink.default`; transition background-color 0.32s ease, color 0.32s ease; layers ::after rgb(10, 10, 10) 0px none 1 |
| focus-visible | outline 1px auto #101010, offset 1px |

![Start now button default](components/crops/nav-cta-default.png) ![Start now button hover](components/crops/nav-cta-hover.png) ![Start now button focus-visible](components/crops/nav-cta-focus-visible.png) ![Start now button pressed](components/crops/nav-cta-pressed.png)

#### Mega-menu card
A .mega-card tile inside the Features mega-menu (Get inspired / Designers / Help / Blog); measured with the menu open, never followed. The tiles compute visibility:hidden until a Webflow reveal — earlier passes read mid-reveal or before it; the settle wait lets it paint. Read as `mega-card` on the home page.

**Values (default).** size 316 x 325.98; padding 4px 0px; background transparent; text Suisse Intl 16.99/28.04 400, #ffffff `_primitives.color.paper.default`; transition text-decoration-color 0.2s ease, color 0.2s ease; layers div.mega-card-img 316.0x210.7 rgba(255, 255, 255, 0.07).

Child layers that carry the look: div 316x210.7 background rgba(255, 255, 255, 0.07).

![Mega-menu card default](components/crops/mega-card-default.png)

### Home

The marketing home page: the 'One platform for premium products and branded shops' masthead, the Start-now CTA, the Features mega-menu, product tiles, rating cards, the logo wall and the closing section.

#### Hero headline
"One platform for premium products and branded shops." — the display masthead. Read as `hero-h1` on the home page.

**Values (default).** size 1008 x 181.41; background transparent; text Saans 57.6/60.48 420, #ffffff `_primitives.color.paper.default`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero lede
The hero standfirst under the masthead. Read as `hero-sub` on the home page.

**Values (default).** size 300 x 49.28; background transparent; text Suisse Intl 16.99/24.64 400, rgba(255, 255, 255, 0.5) `_primitives.color.paper.alpha.50`; transition color 0.2s ease.

![Hero lede default](components/crops/hero-sub-default.png)

#### Product tile
A .ph-tile product/showcase tile in the home scatter grid (product card with hover-swap imagery). Read as `tile` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 336.88 x 428.31; padding 24px; background #f6f6f6 `_primitives.color.paper.soft`; text Suisse Intl 12/12 500, #0a0a0a `_primitives.color.ink.default`; transition opacity 1.8s cubic-bezier(0.16, 1, 0.3, 1), transform 1.8s cubic-bezier(0.16, 1, 0.3, 1) |

![Product tile default](components/crops/tile-default.png) ![Product tile hover](components/crops/tile-hover.png)

#### Rating chip
The star-rating chip inside a product tile (rating + price). Read as `rating-card` on the home page.

**Values (default).** size 50 x 20; padding 4px 10px 4px 8px; radius 999px; background #ffffff `_primitives.color.paper.default`; text Suisse Intl 12/12 500, #0a0a0a `_primitives.color.ink.default`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Rating chip default](components/crops/rating-card-default.png)

#### Logo wall
The .ws--trusted "trusted by" section — the creator/company logo wall. Read as `brand-grid` on the home page.

**Values (default).** size 1440 x 444.05; padding 88px 40px; background #ffffff `_primitives.color.paper.default`; text Suisse Intl 16.99/28.04 400, rgba(10, 10, 10, 0.6) `_primitives.color.ink.alpha.60`.

![Logo wall default](components/crops/brand-grid-default.png)

#### Design preview carousel
The storefront design-preview carousel in the .on-ink design section. Read as `design-preview` on the home page.

**Values (default).** size 516 x 619.19; background transparent; text Suisse Intl 16.99/28.04 400, #0a0a0a `_primitives.color.ink.default`; transition opacity 1.8s cubic-bezier(0.16, 1, 0.3, 1), transform 1.8s cubic-bezier(0.16, 1, 0.3, 1).

![Design preview carousel default](components/crops/design-preview-default.png)

#### Hero CTA
The primary "Start now" hero action — the only hero action; measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 132 x 55.03; padding 18px 28px; radius 12px; background #ffffff `_primitives.color.paper.default`; text Suisse Intl 16.99/19.03 450, #0a0a0a `_primitives.color.ink.default`; transition color 0.2s ease, text-decoration-color 0.2s ease |
| focus-visible | outline 1px auto #101010, offset 1px |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

### Pricing

The /pricing page: the Pay yearly / Pay monthly billing toggle (clicked once to paint monthly), the Free / Pro / Managed plan cards, feature rows and the FAQ disclosures.

#### Pricing headline
The /pricing masthead. Read as `price-h1` on the pricing page.

**Values (default).** size 968 x 60.47; background transparent; text Saans 57.6/60.48 420, #ffffff `_primitives.color.paper.default`.

![Pricing headline default](components/crops/price-h1-default.png)

#### Billing toggle
The "Pay yearly / Pay monthly" toggle — the monthly state was painted by clicking it (a local UI toggle; Pro reads $19 vs $15). Read as `billing-toggle` on the pricing page.

**Values (default).** size 290 x 48; padding 4px; radius 999px; background rgba(255, 255, 255, 0.1) `_primitives.color.paper.alpha.10`; text Suisse Intl 16/16 500, #0a0a0a `_primitives.color.ink.default`.

![Billing toggle default](components/crops/billing-toggle-default.png)

#### Billing option
The "Pay monthly" toggle button; measured, and clicked once to paint the monthly state. Read as `billing-btn` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 140 x 40; padding 12px 18px; radius 999px; background transparent; text Suisse Intl 16/16 500, rgba(255, 255, 255, 0.5) `_primitives.color.paper.alpha.50`; transition color 0.2s ease |
| hover | text Suisse Intl 16/16 500, #ffffff `_primitives.color.paper.default` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.billing-toggle-btn 140.0x40.0 1px auto rgb(16, 16, 16) offset 0px 999px |
| pressed | text Suisse Intl 16/16 500, #ffffff `_primitives.color.paper.default` |

![Billing option default](components/crops/billing-btn-default.png) ![Billing option hover](components/crops/billing-btn-hover.png) ![Billing option focus-visible](components/crops/billing-btn-focus-visible.png) ![Billing option pressed](components/crops/billing-btn-pressed.png)

#### Plan card
A plan card on /pricing (Free / Pro) — one .plan-card cell inside the .pricing-plans grid. Read as `plan-card` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 544 x 613.53; padding 40px; background #18181b `_primitives.color.ink.deep`; text Saans 34.56/36.28 435, #ffffff `_primitives.color.paper.default`; transition opacity 1.1s cubic-bezier(0.16, 1, 0.3, 1), translate 1.1s cubic-bezier(0.16, 1, 0.3, 1), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1); icon 18 x 18, #ffffff `_primitives.color.paper.default`; layers ::before rgba(0, 0, 0, 0) 0px none 0.918754; ::after rgba(0, 0, 0, 0) 0px none 0.307089 |
| hover | transition transform 0.32s cubic-bezier(0.16, 1, 0.3, 1); layers ::before rgba(0, 0, 0, 0) 0px none 0.440095; ::after rgba(0, 0, 0, 0) 0px none 0.413754 |

![Plan card default](components/crops/plan-card-default.png) ![Plan card hover](components/crops/plan-card-hover.png)

#### Plan feature row
A .plan-feature row inside a plan card's .plan-features list. Read as `plan-row` on the pricing page.

**Values (default).** size 464 x 24.64; background transparent; text Suisse Intl 16.99/24.64 400, #ffffff `_primitives.color.paper.default`; icon 18 x 18, #ffffff `_primitives.color.paper.default`.

![Plan feature row default](components/crops/plan-row-default.png)

#### FAQ disclosure
A disclosure button in the pricing FAQ; the opened state was measured after clicking it (a local UI toggle). Read as `faq-summary` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 800 x 69; padding 20px 24px; background transparent; text Suisse Intl 16.99/normal 450, #0a0a0a `_primitives.color.ink.default`; layers div::before.ph-faq-icon 14pxx1.5px rgba(10, 10, 10, 0.6); div::after.ph-faq-icon 14pxx1.5px rgba(10, 10, 10, 0.6) |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.ph-faq-summary 800.0x69.0 1px auto rgb(16, 16, 16) offset 0px; div::before.ph-faq-icon 14pxx1.5px rgba(10, 10, 10, 0.6); div::after.ph-faq-icon 14pxx1.5px rgba(10, 10, 10, 0.6) |

Child layers that carry the look: div::before 14pxx1.5px background rgba(10, 10, 10, 0.6) `_primitives.color.ink.alpha.60`; div::after 14pxx1.5px background rgba(10, 10, 10, 0.6) `_primitives.color.ink.alpha.60`.

![FAQ disclosure default](components/crops/faq-summary-default.png) ![FAQ disclosure hover](components/crops/faq-summary-hover.png) ![FAQ disclosure focus-visible](components/crops/faq-summary-focus-visible.png) ![FAQ disclosure pressed](components/crops/faq-summary-pressed.png) ![FAQ disclosure opened](components/crops/faq-summary-opened.png)

### Blog

The /blog index: post cards and the newsletter field (typed into, then cleared — never subscribed).

#### Blog headline
The /blog masthead. Read as `blog-h1` on the blog page.

**Values (default).** size 434.41 x 121; background transparent; text Saans 110/121 400, #0a0a0a `_primitives.color.ink.default`.

![Blog headline default](components/crops/blog-h1-default.png)

#### Post card
A post card on the blog index; measured, never followed. Read as `blog-card` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1240 x 430.53; background transparent; text Suisse Intl 16.99/28.04 400, #0a0a0a `_primitives.color.ink.default`; transition color 0.2s ease, text-decoration-color 0.2s ease |

![Post card default](components/crops/blog-card-default.png) ![Post card hover](components/crops/blog-card-hover.png)

#### Newsletter field
The newsletter email input on /blog; focused and typed into then cleared — never subscribed. Read as `blog-news` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 488 x 56; padding 12px 9px 12px 16px; border 1px solid #b5b3b0; radius 12px; background #ffffff `_primitives.color.paper.default`; text Suisse Intl 16/24 400, #212d3a `text.muted`; transition box-shadow 0.2s ease; placeholder #6e6e68 |

![Newsletter field default](components/crops/blog-news-default.png) ![Newsletter field focused](components/crops/blog-news-focused.png) ![Newsletter field filled](components/crops/blog-news-filled.png)

### Compare

The /compare index: the 'Compare Fourthwall to…' search field (typed into, then cleared) and the platform comparison cards.

#### Compare headline
The /compare masthead. Read as `cmp-h1` on the compare page.

**Values (default).** size 1360 x 60.47; background transparent; text Saans 57.6/60.48 420, #0a0a0a `_primitives.color.ink.default`.

![Compare headline default](components/crops/cmp-h1-default.png)

#### Platform search
The "Compare Fourthwall to…" search field; focused and typed into then cleared — a local filter, nothing sent. Read as `cmp-search` on the compare page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 152 x 24.63; background transparent; text Suisse Intl 16.99/24.64 400, #0a0a0a `_primitives.color.ink.default`; placeholder rgba(10, 10, 10, 0.6) `_primitives.color.ink.alpha.60` |

![Platform search default](components/crops/cmp-search-default.png) ![Platform search focused](components/crops/cmp-search-focused.png) ![Platform search filled](components/crops/cmp-search-filled.png)

#### Comparison card
A comparison card linking to a vs-page (Shopify, Patreon…); measured, never followed. Read as `cmp-card` on the compare page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1360 x 161.44; padding 32px 0px; border B: 1px solid rgba(10, 10, 10, 0.16) `_primitives.color.ink.alpha.16`; background transparent; text Saans 20.99/28.34 465, #0a0a0a `_primitives.color.ink.default`; transition opacity 1.1s cubic-bezier(0.16, 1, 0.3, 1), transform 1.1s cubic-bezier(0.16, 1, 0.3, 1); layers a.cmp-row.reveal 1360.0x161.4 B:1px solid rgba(10, 10, 10, 0.16); div::before.btn-secondary 187pxx55.0312px rgba(10, 10, 10, 0.06) 12px; div::after.btn-secondary 187pxx55.0312px rgba(10, 10, 10, 0.11) 12px |

Child layers that carry the look: a 1360x161.4 border 1px solid rgba(10, 10, 10, 0.16) `_primitives.color.ink.alpha.16`; div::before 187pxx55.0312px background rgba(10, 10, 10, 0.06) `_primitives.color.ink.alpha.06` radius 12px; div::after 187pxx55.0312px background rgba(10, 10, 10, 0.11) `_primitives.color.ink.alpha.11` radius 12px.

![Comparison card default](components/crops/cmp-card-default.png) ![Comparison card hover](components/crops/cmp-card-hover.png)

### Comparison page

A vs-page (/compare/fourthwall-vs-shopify): the masthead and the 'Choose X if' comparison cards.

#### Vs-page headline
The "Fourthwall vs Shopify" masthead. Read as `cmpart-h1` on the comparison (fourthwall-vs-shopify) page.

**Values (default).** size 683.05 x 60.47; background transparent; text Saans 57.6/60.48 420, #0a0a0a `_primitives.color.ink.default`.

![Vs-page headline default](components/crops/cmpart-h1-default.png)

#### Vs comparison card
A "Choose X if" card in the .cmp2-pair comparison on a vs-page. Read as `cmpart-card` on the comparison (fourthwall-vs-shopify) page.

**Values (default).** size 544 x 604.75; padding 40px; background #18161d `_primitives.color.ink.violet`; text Saans 28.8/32.25 435, #ffffff `_primitives.color.paper.default`; transition transform 0.9s cubic-bezier(0.16, 1, 0.3, 1); layers ::before rgba(0, 0, 0, 0) 0px none 0.965607; ::after rgba(0, 0, 0, 0) 0px none 0.745791.

![Vs comparison card default](components/crops/cmpart-card-default.png)

### Shops

The /shops showcase: example-shop tiles.

#### Shops headline
The /shops masthead. Read as `shops-h1` on the shops page.

**Values (default).** size 968 x 60.47; background transparent; text Saans 57.6/60.48 420, #ffffff `_primitives.color.paper.default`.

![Shops headline default](components/crops/shops-h1-default.png)

#### Shop tile
An example-shop card on /shops (.brand-card showcase / .pg-card grid); measured, never followed. Read as `shops-tile` on the shops page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 432 x 475.31; background transparent; text Saans 20.99/30.44 450, #0a0a0a `_primitives.color.ink.default`; transition opacity 1.8s cubic-bezier(0.16, 1, 0.3, 1), transform 1.8s cubic-bezier(0.16, 1, 0.3, 1); transform translate(0px, 56px); opacity 0; layers div.brand-card-box.card-grid-box 432.0x360.0 rgb(246, 246, 246) |
| hover | transform none; opacity none |

Child layers that carry the look: div 432x360 background #f6f6f6 `_primitives.color.paper.soft`.

![Shop tile default](components/crops/shops-tile-default.png) ![Shop tile hover](components/crops/shops-tile-hover.png)

### Get inspired

The /get-inspired showcase: creator and storefront cards.

#### Get-inspired headline
The /get-inspired masthead. Read as `insp-h1` on the get-inspired page.

**Values (default).** size 968 x 60.47; background transparent; text Saans 57.6/60.48 420, #0a0a0a `_primitives.color.ink.default`.

![Get-inspired headline default](components/crops/insp-h1-default.png)

#### Creator card
An .ex-tile creator/showcase card on /get-inspired; measured, never followed. Read as `insp-card` on the get-inspired page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 432 x 358.94; background transparent; text Saans 16.99/22.94 465, #0a0a0a `_primitives.color.ink.default`; transition color 0.2s ease, text-decoration-color 0.2s ease; layers ::before rgba(0, 0, 0, 0) 0px none 0; img.ex-tile-img.is-loaded 432.0x324.0 T:1px solid rgba(10, 10, 10, 0.11) / R:1px solid rgba(10, 10, 10, 0.11) / B:1px solid rgba(10, 10, 10, 0.11) / L:1px solid rgba(10, 10, 10, 0.11) |

Child layers that carry the look: img 432x324 border 1px solid rgba(10, 10, 10, 0.11) `_primitives.color.ink.alpha.11`.

![Creator card default](components/crops/insp-card-default.png) ![Creator card hover](components/crops/insp-card-hover.png)

### Contact

The /contact page: the contact and support cards.

#### Contact headline
The /contact masthead. Read as `contact-h1` on the contact page.

**Values (default).** size 968 x 60.47; background transparent; text Saans 57.6/60.48 420, #0a0a0a `_primitives.color.ink.default`.

![Contact headline default](components/crops/contact-h1-default.png)

#### Contact card
An a.contact-card on /contact (Contact support / Contact sales); measured, never followed. Read as `contact-card` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 316 x 355.14; background transparent; text Saans 20.99/28.34 465, #0a0a0a `_primitives.color.ink.default`; transition color 0.2s ease, text-decoration-color 0.2s ease; layers div.contact-card-img 316.0x210.7 rgba(10, 10, 10, 0.06) |

Child layers that carry the look: div 316x210.7 background rgba(10, 10, 10, 0.06) `_primitives.color.ink.alpha.06`.

![Contact card default](components/crops/contact-card-default.png) ![Contact card hover](components/crops/contact-card-hover.png)

### Signup (auth shell)

fourthwall.com/get-started — the auth.fourthwall.com (Keycloak) shell it redirects to: the Google / Apple / email provider choices on the catalogue DS. Measured at rest, never pressed.

#### Auth card
The signed-out auth surface at /get-started (auth.fourthwall.com, Keycloak on the catalogue DS) — the panel holding the Google/Apple/email choices; measured at rest, nothing pressed. Read as `auth-card` on the get-started auth shell page.

**Values (default).** size 440 x 176; background transparent; text Suisse Int'l 16/24 500, #161712 `bg.brand.default`; icon 21 x 20, #161712 `bg.brand.default`; layers a.sc-kLLXSa.ioAyRT 440.0x48.0 rgb(242, 242, 242) 8px; a.sc-kLLXSa.ioAyRT 440.0x48.0 rgb(242, 242, 242) 8px; a.sc-kLLXSa.ioAyRT 440.0x48.0 rgb(242, 242, 242) 8px.

Child layers that carry the look: a 440x48 background #f2f2f2 `bg.primary.hover` radius 8px; a 440x48 background #f2f2f2 `bg.primary.hover` radius 8px; a 440x48 background #f2f2f2 `bg.primary.hover` radius 8px.

![Auth card default](components/crops/auth-card-default.png)

#### Google provider
The "Continue with Google" provider button; states measured, never pressed — no OAuth flow was started. Read as `auth-google` on the get-started auth shell page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 440 x 48; padding 0px 16px; radius 8px; background #f2f2f2 `bg.primary.hover`; text Suisse Int'l 16/24 500, #161712 `bg.brand.default`; icon 21 x 20, #161712 `bg.brand.default` |
| hover | background #eaeae9 `bg.primary.active` |
| focus-visible | outline 2px solid #161712 `bg.brand.default`, offset 2px |
| pressed | background #e1e0df `bg.secondary.active` |

![Google provider default](components/crops/auth-google-default.png) ![Google provider hover](components/crops/auth-google-hover.png) ![Google provider focus-visible](components/crops/auth-google-focus-visible.png) ![Google provider pressed](components/crops/auth-google-pressed.png)

#### Apple provider
The "Continue with Apple" provider button; measured, never pressed. Read as `auth-apple` on the get-started auth shell page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 440 x 48; padding 0px 16px; radius 8px; background #f2f2f2 `bg.primary.hover`; text Suisse Int'l 16/24 500, #161712 `bg.brand.default`; icon 18 x 20, #161712 `bg.brand.default` |
| hover | background #eaeae9 `bg.primary.active` |
| focus-visible | outline 2px solid #161712 `bg.brand.default`, offset 2px |
| pressed | background #e1e0df `bg.secondary.active` |

![Apple provider default](components/crops/auth-apple-default.png) ![Apple provider hover](components/crops/auth-apple-hover.png) ![Apple provider focus-visible](components/crops/auth-apple-focus-visible.png) ![Apple provider pressed](components/crops/auth-apple-pressed.png)

#### Email provider
The "Continue with email" action; measured, never pressed. Read as `auth-email` on the get-started auth shell page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 440 x 48; padding 0px 16px; radius 8px; background #f2f2f2 `bg.primary.hover`; text Suisse Int'l 16/24 500, #161712 `bg.brand.default`; icon 20 x 20, #161712 `bg.brand.default` |
| hover | background #eaeae9 `bg.primary.active` |
| focus-visible | outline 2px solid #161712 `bg.brand.default`, offset 2px |
| pressed | background #e1e0df `bg.secondary.active` |

![Email provider default](components/crops/auth-email-default.png) ![Email provider hover](components/crops/auth-email-hover.png) ![Email provider focus-visible](components/crops/auth-email-focus-visible.png) ![Email provider pressed](components/crops/auth-email-pressed.png)

#### Login link
The "Log in" link on the signup surface; measured, never followed. Read as `auth-login` on the get-started auth shell page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 42 x 28; background transparent; text Suisse Int'l 16/normal 400, #161712 `bg.brand.default` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.sc-gicCDH.fjjreh 42.0x28.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Suisse Int'l 16/normal 400, #6e6e68 `bg.quaternary.active` |

![Login link default](components/crops/auth-login-default.png) ![Login link hover](components/crops/auth-login-hover.png) ![Login link focus-visible](components/crops/auth-login-focus-visible.png) ![Login link pressed](components/crops/auth-login-pressed.png)

### Product catalogue

products.fourthwall.com — the public catalogue: the nav with category tabs and search, the product-finder quiz, product cards and badges.

#### Catalogue nav
The products.fourthwall.com top bar — logo, category tabs, search, Log in / Sign up. Read as `cat-nav` on the catalogue home page.

**Values (default).** size 551 x 50.39; background transparent; text Suisse Int'l 16/18.4 500, #161712 `bg.brand.default`; layers span::after.sc-9ae1efd9-1.ePbzzw 69pxx2px rgb(22, 23, 18).

Child layers that carry the look: span::after 69pxx2px background #161712 `bg.brand.default`.

![Catalogue nav default](components/crops/cat-nav-default.png)

#### Catalogue search
The catalogue search field — a bare input[type=text] in the nav; focused and typed into then cleared — a local filter, nothing sent. Read as `cat-search` on the catalogue home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 218 x 38; padding 0px 14px 0px 41px; background transparent; text Suisse Int'l 16/38 400, #161712 `bg.brand.default`; placeholder #161712 `bg.brand.default` |
| focused | size 638 x 48; text Suisse Int'l 16/48 400, #161712 `bg.brand.default`; placeholder #757575 |
| filled | size 638 x 48; padding 0px 41px; text Suisse Int'l 16/48 400, #161712 `bg.brand.default`; placeholder #757575 |

![Catalogue search default](components/crops/cat-search-default.png) ![Catalogue search focused](components/crops/cat-search-focused.png) ![Catalogue search filled](components/crops/cat-search-filled.png)

#### Quiz card
The "What are you looking for?" product-finder card on the catalogue home. Read as `quiz-card` on the catalogue home page.

**Values (default).** size 1344 x 907.45; background transparent; text Suisse Int'l 14/21 400, #6e6e68 `bg.quaternary.active`; icon 20 x 20, #161712 `bg.brand.default`; layers div.sc-a30299a3-0.UwkhN 1344.0x262.0 rgb(255, 255, 255) T:1px solid rgb(225, 224, 223) / R:1px solid rgb(225, 224, 223) / B:1px solid rgb(225, 224, 223) / L:1px solid rgb(225, 224, 223) 8px; button.sc-d64fc78e-2.gsJhKO 639.0x137.0 rgb(242, 242, 242) T:2px solid rgba(0, 0, 0, 0) / R:2px solid rgba(0, 0, 0, 0) / B:2px solid rgba(0, 0, 0, 0) / L:2px solid rgba(0, 0, 0, 0) 8px; button.sc-d64fc78e-2.gs.

Child layers that carry the look: div 1344x262 background #ffffff `bg.primary.default` border 1px solid #e1e0df `bg.secondary.active` radius 8px; button 639x137 background #f2f2f2 `bg.primary.hover` border 2px solid transparent radius 8px; button 639x137 background #f2f2f2 `bg.primary.hover` border 2px solid transparent radius 8px.

![Quiz card default](components/crops/quiz-card-default.png)

#### Quiz option
A product-finder answer chip; clicking selects it locally (the quiz needs more steps before recommending) — nothing is submitted. Read as `quiz-option` on the catalogue home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 639 x 137; padding 24px; border 2px solid transparent; radius 8px; background #f2f2f2 `bg.primary.hover`; text Suisse Int'l 16/24 500, #161712 `bg.brand.default`; transition border-color 0.1s ease, background-color 0.1s ease; icon 20 x 20, #161712 `bg.brand.default` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | border 2px solid #161712 `bg.brand.default`; background #e1e0df `bg.secondary.active` |

![Quiz option default](components/crops/quiz-option-default.png) ![Quiz option hover](components/crops/quiz-option-hover.png) ![Quiz option focus-visible](components/crops/quiz-option-focus-visible.png) ![Quiz option pressed](components/crops/quiz-option-pressed.png)

#### Product card
A catalogue product card (thumbnail, name, colour count, "From $" price); measured, never followed. Read as `prod-card` on the catalogue home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 243.19 x 323.44; background transparent; text Suisse Int'l 16/18.4 400, #161712 `bg.brand.default` |

![Product card default](components/crops/prod-card-default.png) ![Product card hover](components/crops/prod-card-hover.png)

#### Product badge
A "Best seller" / "Staff pick" badge on a product card. Read as `prod-badge` on the catalogue home page.

**Values (default).** size 77 x 22; padding 2px 6px; border 1px solid rgba(0, 0, 0, 0.12) `bg.highlight.active`; radius 100px; background #161712 `bg.brand.default`; text Suisse Int'l 12/16 600, #fdfcfb `color.gray.200`.

![Product badge default](components/crops/prod-badge-default.png)

#### Log in action
The "Log in" catalogue action; measured, never followed. Hydration swaps the nav copy roughly a minute after load, so focus/pressed states could not be captured reliably. Read as `cat-login` on the catalogue home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 75 x 40; padding 0px 14px; radius 8px; background #f2f2f2 `bg.primary.hover`; text Suisse Int'l 16/24 500, #161712 `bg.brand.default` |
| hover | background #eaeae9 `bg.primary.active` |

![Log in action default](components/crops/cat-login-default.png) ![Log in action hover](components/crops/cat-login-hover.png)

#### Sign up action
The "Sign up" catalogue action; measured, never followed. Focus/pressed states were not reliably measurable (hydration nav swap). Read as `cat-signup` on the catalogue home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 87 x 40; padding 0px 14px; radius 8px; background #161712 `bg.brand.default`; text Suisse Int'l 16/24 500, #fdfcfb `color.gray.200` |
| hover | background #252621 `bg.brand.hover` |

![Sign up action default](components/crops/cat-signup-default.png) ![Sign up action hover](components/crops/cat-signup-hover.png)

#### Category tab
A category tab in the catalogue nav strip (Discover / All Products / Apparel…); measured, never followed. Focus/pressed states were not reliably measurable (hydration nav swap). Read as `cat-tab` on the catalogue home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 69 x 28; background transparent; text Suisse Int'l 16/18.4 500, #161712 `bg.brand.default`; layers span::after.sc-9ae1efd9-1.ePbzzw 69pxx2px rgb(22, 23, 18) |

Child layers that carry the look: span::after 69pxx2px background #161712 `bg.brand.default`.

![Category tab default](components/crops/cat-tab-default.png) ![Category tab hover](components/crops/cat-tab-hover.png)

### Product page

A catalogue PDP (Comfort Colors 1717): title and badge, colour swatches, the static 'S–4XL' size-range label and size-guide dialog, price and the 'Sign in to design' CTA — measured, never activated. This PDP exposes no per-size selector or decoration picker.

#### Product headline
The PDP product title ("Comfort Colors Garment-Dyed Heavyweight T-Shirt"). Read as `pdp-h1` on the product page page.

**Values (default).** size 400 x 60; background transparent; text Saans VF 24/30 480, #161712 `bg.brand.default`.

![Product headline default](components/crops/pdp-h1-default.png)

#### PDP badge
The "Best seller" badge beside the title. Read as `pdp-badge` on the product page page.

**Values (default).** size 77 x 22; padding 2px 6px; border 1px solid rgba(0, 0, 0, 0.12) `bg.highlight.active`; radius 100px; background #161712 `bg.brand.default`; text Suisse Int'l 12/16 600, #fdfcfb `color.gray.200`.

![PDP badge default](components/crops/pdp-badge-default.png)

#### Colour swatch
A colour swatch button on the PDP (classless styled-components swatch buttons); selecting one repaints the photo locally — measured, selection states only. Read as `pdp-swatch` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 28 x 28; background transparent; text Suisse Int'l 16/18.4 400, #161712 `bg.brand.default`; layers div.sc-ee66eef2-0.hIhVCE 28.0x28.0 rgb(8, 8, 8) T:1px solid rgb(181, 179, 176) / R:1px solid rgb(181, 179, 176) / B:1px solid rgb(181, 179, 176) / L:1px solid rgb(181, 179, 176) 50%; div::before.sc-ee66eef2-0.hIhVCE 36pxx36px T:2px solid rgb(22, 23, 18) / R:2px solid rgb(22, 23, 18) / B:2px solid rgb(22, 23, 18) / L:2px solid rgb(22, 23, 18) 50% |
| focus-visible | outline 1px auto #101010, offset 0px; layers button 28.0x28.0 1px auto rgb(16, 16, 16) offset 0px; div.sc-ee66eef2-0.hIhVCE 28.0x28.0 rgb(8, 8, 8) T:1px solid rgb(181, 179, 176) / R:1px solid rgb(181, 179, 176) / B:1px solid rgb(181, 179, 176) / L:1px solid rgb(181, 179, 176) 50%; div::before.sc-ee66eef2-0.hIhVCE 36pxx36px T:2px solid rgb(22, 23, 18) / R:2px solid rgb(22, 23, 18) / B:2px solid rgb(22, 23, 18) / L:2px solid rgb(22, 23, 18) 50 |

Child layers that carry the look: div 28x28 background #080808 border 1px solid #b5b3b0 `bg.quaternary.default` radius 50%; div::before 36pxx36px border 2px solid #161712 `bg.brand.default` radius 50%.

![Colour swatch default](components/crops/pdp-swatch-default.png) ![Colour swatch hover](components/crops/pdp-swatch-hover.png) ![Colour swatch focus-visible](components/crops/pdp-swatch-focus-visible.png) ![Colour swatch pressed](components/crops/pdp-swatch-pressed.png)

#### Size-guide button
The "Size guide" control — a local dialog toggle. Read as `pdp-sizeguide-btn` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 79 x 18.39; background transparent; text Suisse Int'l 16/18.4 400, #161712 `bg.brand.default` |
| hover | text Suisse Int'l 16/18.4 400, #0042ff `bg.chart` |
| focus-visible | outline 1px auto #101010, offset 0px; text Suisse Int'l 16/18.4 400, #0042ff `bg.chart`; layers button.sc-7d3c69e8-0.iJstzX 79.0x18.4 1px auto rgb(16, 16, 16) offset 0px |
| pressed | text Suisse Int'l 16/18.4 400, #0042ff `bg.chart` |

![Size-guide button default](components/crops/pdp-sizeguide-btn-default.png) ![Size-guide button hover](components/crops/pdp-sizeguide-btn-hover.png) ![Size-guide button focus-visible](components/crops/pdp-sizeguide-btn-focus-visible.png) ![Size-guide button pressed](components/crops/pdp-sizeguide-btn-pressed.png)

#### Price text
The "From $15.45" price text. Read as `pdp-price` on the product page page.

**Values (default).** size 79 x 21; background transparent; text Suisse Int'l 14/21 400, #6e6e68 `bg.quaternary.active`.

![Price text default](components/crops/pdp-price-default.png)

#### Sign-in-to-design CTA
The "Sign in to design" action — it starts an auth flow; measured, never pressed. Read as `pdp-design-cta` on the product page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 48; padding 0px 16px; radius 8px; background #161712 `bg.brand.default`; text Suisse Int'l 16/24 500, #fdfcfb `color.gray.200` |
| hover | background #252621 `bg.brand.hover` |
| focus-visible | outline 2px solid #161712 `bg.brand.default`, offset 2px |
| pressed | background #343531 `bg.brand.active` |

![Sign-in-to-design CTA default](components/crops/pdp-design-cta-default.png) ![Sign-in-to-design CTA hover](components/crops/pdp-design-cta-hover.png) ![Sign-in-to-design CTA focus-visible](components/crops/pdp-design-cta-focus-visible.png) ![Sign-in-to-design CTA pressed](components/crops/pdp-design-cta-pressed.png)

#### Product description
The product description paragraph (materials, fit, print specs). Read as `pdp-desc` on the product page page.

**Values (default).** size 179 x 24; background transparent; text Suisse Int'l 16/24 600, #161712 `bg.brand.default`.

![Product description default](components/crops/pdp-desc-default.png)

#### Size-range label
The static "S–4XL" size-range label — no per-size option exists on the public PDP. Read as `pdp-size` on the product page page.

**Values (default).** size 49 x 18.39; background transparent; text Suisse Int'l 16/18.4 400, #161712 `bg.brand.default`.

![Size-range label default](components/crops/pdp-size-default.png)

#### Size-guide dialog
The size-table dialog mounted by the Size-guide control; opened by its own toggle. Read as `pdp-sizeguide` on the product page page.

**Values (default).** size 1440 x 804; radius 32px 32px 0px 0px; background #ffffff `bg.primary.default`; text Suisse Int'l 20/28 400, #161712 `bg.brand.default`; icon 16 x 16, #161712 `bg.brand.default`; layers ::after rgb(255, 255, 255) 0px none 1.

![Size-guide dialog default](components/crops/pdp-sizeguide-default.png)

### Developer docs

docs.fourthwall.com — the Mintlify docs: navbar, cmdk search dialog, sidebar, article typography, code blocks and the 'Change theme preference' menu.

#### Docs navbar
The Mintlify top bar — logo, tabs, search and the theme menu. Read as `docs-nav` on the docs home page.

**Values (default).** size 1440 x 112; background transparent; text Inter 14/24 400, #6f6f6f; icon 16 x 16, #3e3e3e; layers div.absolute.w-full 1440.0x112.0 rgb(255, 255, 255) B:1px solid oklab(0.541658 0.0000246018 0.000010848 / 0.05); div.h-full.relative 1344.0x64.0 B:1px solid oklab(0.541658 0.0000246018 0.000010848 / 0.05); button.group/search.flex 437.3x36.0 rgb(255, 255, 255) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.69924 0.0000317991 0.00001406.

Child layers that carry the look: div 1440x112 background #ffffff `color.white` border 1px solid oklab(0.541658 0.0000246018 0.000010848 / 0.05); div 1344x64 border 1px solid oklab(0.541658 0.0000246018 0.000010848 / 0.05); button 437.3x36 background #ffffff `color.white` radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, oklab(0.69924 0.0000317991 0.0000140667 / 0.3) 0px 0px 0px 1px, transparent 0px 0px 0px 0px.

![Docs navbar default](components/crops/docs-nav-default.png)

#### Search trigger
The docs search control — opens the cmdk dialog; states measured. Read as `docs-search` on the docs home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 437.33 x 36; padding 0px 12px 0px 14px; radius 12px; background #ffffff `color.white`; shadow oklab(0.69924 0.0000317991 0.0000140667 / 0.3) 0px 0px 0px 1px; text Inter 14/24 400, #6f6f6f; icon 16 x 16, #3e3e3e |
| hover | shadow oklab(0.427603 0.0000194311 0.00000855327 / 0.3) 0px 0px 0px 1px; icon 16 x 16, #252525 |
| focus-visible | outline 1px auto #000000 `color.black`, offset 0px |
| pressed | shadow oklab(0.427603 0.0000194311 0.00000855327 / 0.3) 0px 0px 0px 1px; icon 16 x 16, #252525 |

![Search trigger default](components/crops/docs-search-default.png) ![Search trigger hover](components/crops/docs-search-hover.png) ![Search trigger focus-visible](components/crops/docs-search-focus-visible.png) ![Search trigger pressed](components/crops/docs-search-pressed.png)

#### Theme menu button
The "Change theme preference" button — the docs site's real Light/Dark/System menu; measured, the Dark choice is made only on the docsdark pass. Read as `docs-theme-btn` on the docs home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; padding 8px; radius 8px; background transparent; text Inter 14/20 400, oklab(0.144787 0.00000661612 0.00000289828 / 0.5); icon 16 x 16, #6f6f6f |
| hover | icon 16 x 16, #3e3e3e |
| focus-visible | outline 1px auto #000000 `color.black`, offset 0px; layers button.group.disabled:pointer-events-none 32.0x32.0 1px auto rgb(0, 0, 0) offset 0px 8px |
| pressed | icon 16 x 16, #3e3e3e |

![Theme menu button default](components/crops/docs-theme-btn-default.png) ![Theme menu button hover](components/crops/docs-theme-btn-hover.png) ![Theme menu button focus-visible](components/crops/docs-theme-btn-focus-visible.png) ![Theme menu button pressed](components/crops/docs-theme-btn-pressed.png)

#### Docs sidebar
The Mintlify sidebar nav tree. Read as `docs-sidebar` on the docs home page.

**Values (default).** size 288 x 788; background transparent; text Inter 14/24 500, #4f4f4f; icon 16 x 16, #9e9e9e; layers div.sticky.top-0 256.0x32.0; div.mr-4.rounded-md 24.0x24.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.144787 0.00000661612 0.00000289828 / 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 6px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 rgb(158, 158, 158); div.mr-4.rounded-md 24..

Child layers that carry the look: div 256x32 image linear-gradient(in oklab, #ffffff `color.white` 0%, transparent 100%); div 24x24 radius 6px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, oklab(0.144787 0.00000661612 0.00000289828 / 0.07) 0px 0px 0px 1px, transparent 0px 0px 0px 0px; svg 16x16 background #9e9e9e.

![Docs sidebar default](components/crops/docs-sidebar-default.png)

#### Sidebar item
A sidebar nav link; measured, never followed. Read as `docs-side-item` on the docs home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 256 x 36; padding 6px 12px 6px 16px; radius 12px; background transparent; text Inter 14/24 400, #3e3e3e |
| hover | background oklab(0.427603 0.0000194311 0.00000855327 / 0.05); text Inter 14/24 400, #161616 `text.ink` |
| focus-visible | outline 1px auto #000000 `color.black`, offset -2px; layers a.group.flex 256.0x36.0 1px auto rgb(0, 0, 0) offset -2px 12px |
| pressed | background oklab(0.427603 0.0000194311 0.00000855327 / 0.05); text Inter 14/24 400, #161616 `text.ink` |

![Sidebar item default](components/crops/docs-side-item-default.png) ![Sidebar item hover](components/crops/docs-side-item-hover.png) ![Sidebar item focus-visible](components/crops/docs-side-item-focus-visible.png) ![Sidebar item pressed](components/crops/docs-side-item-pressed.png)

#### Docs card
A .card tile on the docs landing page (Platform API / Webhooks / …); measured, never followed. Read as `docs-card` on the docs home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 336.41 x 182; border 1px solid oklab(0.144787 0.00000661612 0.00000289828 / 0.1); radius 16px; background #ffffff `color.white`; text Inter 16/24 600, #252525 |
| hover | border 1px solid #000000 `color.black` |

![Docs card default](components/crops/docs-card-default.png) ![Docs card hover](components/crops/docs-card-hover.png)

#### Article headline
The docs article title (the /quickstart page). Read as `docs-h1` on the docs article page.

**Values (default).** size 172.02 x 40; background transparent; text Inter 36/40 600, #161616 `text.ink`.

![Article headline default](components/crops/docs-h1-default.png)

#### Article body
A body paragraph in a docs article. Read as `docs-prose` on the docs article page.

**Values (default).** size 688.81 x 28; background transparent; text Inter 18/28 400, #3e3e3e.

![Article body default](components/crops/docs-prose-default.png)

#### Code block
A fenced code block in a docs article. Read as `docs-code` on the docs article page.

**Values (default).** size 650.81 x 72; background transparent; shadow rgba(59, 130, 246, 0.5) 0px 0px 0px 0px; text Paper Mono 14/24 400, #6e7781; layers pre.shiki.shiki-themes 650.8x72.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px; code 650.8x72.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0.

![Code block default](components/crops/docs-code-default.png)

#### Article link
An in-content link inside a docs article; measured, never followed. Read as `docs-anchor` on the docs article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 264 x 32; padding 4px 0px; background transparent; text Inter 14/24 400, #000000 `color.black` |
| focus-visible | size 268 x 32; padding 4px 0px 4px 4px; outline 1px auto #000000 `color.black`, offset -2px; layers a.text-primary.dark:text-primary-light 268.0x32.0 1px auto rgb(0, 0, 0) offset -2px |

![Article link default](components/crops/docs-anchor-default.png) ![Article link hover](components/crops/docs-anchor-hover.png) ![Article link focus-visible](components/crops/docs-anchor-focus-visible.png) ![Article link pressed](components/crops/docs-anchor-pressed.png)

#### On-this-page rail
The right-hand table-of-contents rail. Read as `docs-toc` on the docs article page.

**Values (default).** size 264 x 176; background transparent; text Inter 14/24 500, #3e3e3e; icon 12 x 12, #3e3e3e.

![On-this-page rail default](components/crops/docs-toc-default.png)

#### Search dialog
The Mintlify search dialog; opened by its own search control, nothing sent. Read as `docs-search-dialog` on the docs home page.

**Values (default).** size 640 x 62; radius 20px; background #ffffff `color.white`; shadow oklab(0.144787 0.00000661612 0.00000289828 / 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.01) 0px 57px 34px 0px, rgba(0, 0, 0, 0.02) 0px 25px 25px 0px, rgba(0, 0, 0, 0.02) 0px 6px 14px 0px; text Inter 16/24 400, #000000 `color.black`; transition transform 0.25s cubic-bezier(0.22, 1, 0.36, 1), scale 0.25s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.25s cubic-bezier(0.22, 1, 0.36, 1); icon 16 x 16, #6f6f6f.

![Search dialog default](components/crops/docs-search-dialog-default.png)

### Developer docs (dark)

The same docs page under html.dark, painted by the site's own theme menu — the real user-facing toggle, not a reconstruction.

#### Docs page (dark)
The docs article surface under html.dark — reached through the site's own theme menu, not a reconstruction. Read as `dd-page` on the docs article page.

**Values (default).** size 1088 x 1887.7; background transparent; text Inter 14/24 500, #cecece; icon 12 x 12, #cecece; layers a::before.anchor-link 24pxx24px rgb(10, 10, 12) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.363827 0.0000165999 0.00000724196 / 0.25) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px 6px; a::after.anchor-link 12pxx12px oklab(0.999994 0.0000455678 0.0000200868 / 0.5); div.callout.my-4 688.8x54.0 oklab(0.54615 -0.026671 -0.213549 .

Child layers that carry the look: a::before 24pxx24px background #0a0a0c `surface.card` radius 6px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, oklab(0.363827 0.0000165999 0.00000724196 / 0.25) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; a::after 12pxx12px background oklab(0.999994 0.0000455678 0.0000200868 / 0.5); div 688.8x54 background oklab(0.54615 -0.026671 -0.213549 / 0.2) border 1px solid #1e3a8a radius 16px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Article headline (dark)
The article title under html.dark. Read as `dd-h1` on the docs article page.

**Values (default).** size 172.02 x 40; background transparent; text Inter 36/40 600, #dedede `text.ink`.

![Article headline (dark) default](components/crops/dd-h1-default.png)

#### Docs navbar (dark)
The Mintlify navbar under html.dark. Read as `dd-nav` on the docs article page.

**Values (default).** size 1440 x 112; background transparent; text Inter 14/24 400, oklab(0.999994 0.0000455678 0.0000200868 / 0.5); icon 16 x 16, #9e9e9e `text.muted`; layers div.absolute.w-full 1440.0x112.0 rgb(10, 10, 12) B:1px solid oklab(0.85137 0.0000389516 0.0000170469 / 0.06); div.h-full.relative 1344.0x64.0 B:1px solid oklab(0.85137 0.0000389516 0.0000170469 / 0.06); button.group/search.flex 437.3x36.0 rgb(10, 10, 12) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.427603 0.0000194311 0.00000855327 /.

Child layers that carry the look: div 1440x112 background #0a0a0c `surface.card` border 1px solid oklab(0.85137 0.0000389516 0.0000170469 / 0.06); div 1344x64 border 1px solid oklab(0.85137 0.0000389516 0.0000170469 / 0.06); button 437.3x36 background #0a0a0c `surface.card` radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, oklab(0.427603 0.0000194311 0.00000855327 / 0.3) 0px 0px 0px 1px, transparent 0px 0px 0px 0px.

![Docs navbar (dark) default](components/crops/dd-nav-default.png)

#### Article body (dark)
A body paragraph under html.dark. Read as `dd-prose` on the docs article page.

**Values (default).** size 688.81 x 28; background transparent; text Inter 18/28 400, #9e9e9e `text.muted`.

![Article body (dark) default](components/crops/dd-prose-default.png)

#### Code block (dark)
A code block under html.dark. Read as `dd-code` on the docs article page.

**Values (default).** size 650.81 x 72; background transparent; shadow rgba(59, 130, 246, 0.5) 0px 0px 0px 0px; text Paper Mono 14/24 400, #6a9955; layers pre.shiki.shiki-themes 650.8x72.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px; code 650.8x72.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0.

![Code block (dark) default](components/crops/dd-code-default.png)

#### Docs card (dark)
A docs card under html.dark. Read as `dd-card` on the docs article page.

**Values (default).** size 336.41 x 134; border 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1); radius 16px; background #0a0a0c `surface.card`; text Inter 16/24 600, #ffffff `color.white`.

![Docs card (dark) default](components/crops/dd-card-default.png)

### Help center

help.fourthwall.com — the Docusaurus help center: navbar with the ctrl-K search and the colour-mode toggle, category cards and article lists.

#### Help navbar
The Docusaurus navbar — "Help center" wordmark, the ctrl-K search, the Fourthwall link and the colour-mode toggle. Read as `help-navbar` on the help home page.

**Values (default).** size 1440 x 56; padding 8px 20px; background #ffffff `fw.bg.primary`; text Suisse Intl 16/24 500, #161712 `docusaurus.progress.bar.color`.

![Help navbar default](components/crops/help-navbar-default.png)

#### Search field
The help search field (ctrl-K hint); focused and typed into then cleared — a local filter, nothing sent. Read as `help-search` on the help home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 852 x 48; padding 0px 16px 0px 48px; radius 4px; background rgba(0, 0, 0, 0.05) `docusaurus.highlighted.code.line.bg`; text Arial 16/normal 400, #444950 `ifm.blockquote.color`; placeholder #6e6e68 `fw.search.icon.color` |

![Search field default](components/crops/help-search-default.png) ![Search field focused](components/crops/help-search-focused.png) ![Search field filled](components/crops/help-search-filled.png)

#### Colour-mode toggle
The navbar colour-mode button — the help site's real dark toggle (data-theme); its states were measured but it was only switched on the helpdark pass. Read as `help-theme` on the help home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 50%; background transparent; text Suisse Intl 13.33/normal 400, #161712 `docusaurus.progress.bar.color`; transition background 0.2s ease |
| hover | background #ebedf0 `ifm.color.emphasis.200` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.clean-btn.toggleButton_gllP 32.0x32.0 1px auto rgb(16, 16, 16) offset 0px 50% |
| pressed | background #ebedf0 `ifm.color.emphasis.200` |

![Colour-mode toggle default](components/crops/help-theme-default.png) ![Colour-mode toggle hover](components/crops/help-theme-hover.png) ![Colour-mode toggle focus-visible](components/crops/help-theme-focus-visible.png) ![Colour-mode toggle pressed](components/crops/help-theme-pressed.png)

#### Fourthwall link
The "Fourthwall ↗" navbar link back to the product; measured, never followed. Read as `help-fw-link` on the help home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 117 x 32; padding 4px 12px; background transparent; text Suisse Intl 16/24 500, #161712 `docusaurus.progress.bar.color`; transition color 0.2s cubic-bezier(0.08, 0.52, 0.52, 1) |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.navbar__item.navbar__link 117.0x32.0 1px auto rgb(16, 16, 16) offset 1px |

![Fourthwall link default](components/crops/help-fw-link-default.png) ![Fourthwall link hover](components/crops/help-fw-link-hover.png) ![Fourthwall link focus-visible](components/crops/help-fw-link-focus-visible.png) ![Fourthwall link pressed](components/crops/help-fw-link-pressed.png)

#### Category link
A category link row on the help landing list ("Setting up your shop", "Design my storefront", …); measured, never followed. Read as `help-card` on the help home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 252 x 24; background transparent; text Suisse Intl 16/24 400, #6e6e68 `fw.search.icon.color`; transition color 0.2s cubic-bezier(0.08, 0.52, 0.52, 1) |
| hover | text Suisse Intl 16/24 400, #161712 `docusaurus.progress.bar.color` |

![Category link default](components/crops/help-card-default.png) ![Category link hover](components/crops/help-card-hover.png)

#### Sidebar item
A help sidebar menu link on the category page; measured, never followed. Read as `help-side-item` on the help category page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 238 x 36; padding 4px 14px; radius 4px; background transparent; text Suisse Intl 14/21 500, #161712 `docusaurus.progress.bar.color`; transition background-color 0.15s ease, color 0.15s ease |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.categoryLink_byQd.menu__link 238.0x36.0 1px auto rgb(16, 16, 16) offset 1px 4px |

![Sidebar item default](components/crops/help-side-item-default.png) ![Sidebar item hover](components/crops/help-side-item-hover.png) ![Sidebar item focus-visible](components/crops/help-side-item-focus-visible.png) ![Sidebar item pressed](components/crops/help-side-item-pressed.png)

#### Category headline
The category page title ("Setting up your shop"). Read as `help-h1` on the help category page.

**Values (default).** size 740 x 50; background transparent; text Saans 40/50 450, #161712 `docusaurus.progress.bar.color`.

![Category headline default](components/crops/help-h1-default.png)

#### Article link
An article link inside a help category; measured, never followed. Read as `help-doc-link` on the help category page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 38.06 x 28.22; padding 5.12px 10.24px; radius 24px; background transparent; text Suisse Intl 12/18 400, #6e6e68 `fw.search.icon.color`; transition background 0.2s cubic-bezier(0.08, 0.52, 0.52, 1), color 0.2s cubic-bezier(0.08, 0.52, 0.52, 1); icon 17.59 x 17.59, #6e6e68 `fw.search.icon.color` |
| hover | background rgba(0, 0, 0, 0.05) `docusaurus.highlighted.code.line.bg` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.breadcrumbs__link 38.1x28.2 1px auto rgb(16, 16, 16) offset 1px 24px |
| pressed | background rgba(0, 0, 0, 0.05) `docusaurus.highlighted.code.line.bg` |

![Article link default](components/crops/help-doc-link-default.png) ![Article link hover](components/crops/help-doc-link-hover.png) ![Article link focus-visible](components/crops/help-doc-link-focus-visible.png) ![Article link pressed](components/crops/help-doc-link-pressed.png)

#### Category body
A body paragraph on the help category page. Read as `help-prose` on the help category page.

**Values (default).** size 740 x 48; background transparent; text Suisse Intl 16/24 400, #6e6e68 `fw.search.icon.color`.

![Category body default](components/crops/help-prose-default.png)

#### Search results dropdown
The local-search results dropdown the navbar search opens while typing. Read as `help-search-pop` on the help home page.

**Values (default).** size 852 x 652.39; padding 12px; radius 6px; background #ffffff `fw.bg.primary`; shadow rgba(0, 0, 0, 0.12) 0px 4px 16px 0px; text Suisse Intl 14.4/21.6 500, #ffffff `fw.bg.primary`.

![Search results dropdown default](components/crops/help-search-pop-default.png)

### Help center (dark)

The same help page under data-theme=dark, painted by the site's own colour-mode toggle — the real user-facing theme.

#### Help page (dark)
The help category surface under data-theme=dark — reached through the site's own colour-mode toggle, not a reconstruction. Read as `hd-page` on the help category page.

**Values (default).** size 1140 x 788; background transparent; text Suisse Intl 12/18 400, #b5b3b0 `fw.text.secondary`; icon 17.59 x 17.59, #b5b3b0 `fw.text.secondary`; layers li::after.breadcrumbs__item 8pxx8px; li::after.breadcrumbs__item 8pxx8px; span.breadcrumbs__link 138.5x28.2 rgba(255, 255, 255, 0.05) 24px; a.card_FHn8 358.0x131.0 T:1px solid rgb(52, 53, 49) / R:1px solid rgb(52, 53, 49) / B:1px solid rgb(52, 53, 49) / L:1px solid rgb(52, 53, 49) 4px; a.card_FHn8 358.0x131.0 T:1px solid rgb(52, 53, 49) / R:1px solid rgb(52, 53, 49) / B:1px solid rgb(52, 53, 49) /.

Child layers that carry the look: li::after 8pxx8px image url(data:…); li::after 8pxx8px image url(data:…); span 138.5x28.2 background rgba(255, 255, 255, 0.05) `docusaurus.collapse.button.bg.default` radius 24px.

![Help page (dark) default](components/crops/hd-page-default.png)

#### Category headline (dark)
The category title under data-theme=dark. Read as `hd-h1` on the help category page.

**Values (default).** size 740 x 50; background transparent; text Saans 40/50 450, #fdfcfb `docusaurus.progress.bar.color`.

![Category headline (dark) default](components/crops/hd-h1-default.png)

#### Help navbar (dark)
The Docusaurus navbar under data-theme=dark. Read as `hd-navbar` on the help category page.

**Values (default).** size 1440 x 56; padding 8px 20px; background #161712 `fw.bg.primary`; text Suisse Intl 16/24 500, #fdfcfb `docusaurus.progress.bar.color`; icon 16 x 16, #fdfcfb `docusaurus.progress.bar.color`.

![Help navbar (dark) default](components/crops/hd-navbar-default.png)

#### Search field (dark)
The help search field under data-theme=dark. Read as `hd-search` on the help category page.

**Values (default).** size 500 x 36; padding 4px 12px 4px 40px; radius 4px; background rgba(255, 255, 255, 0.06) `fw.bg.transparent`; text Suisse Intl 16/normal 400, #fdfcfb `docusaurus.progress.bar.color`; placeholder #b5b3b0 `fw.text.secondary`.

![Search field (dark) default](components/crops/hd-search-default.png)

#### Category card (dark)
A help category card under data-theme=dark. Read as `hd-card` on the help category page.

**Values (default).** size 238 x 36; padding 4px 14px; radius 4px; background transparent; text Suisse Intl 14/21 500, #fdfcfb `docusaurus.progress.bar.color`; transition background-color 0.15s ease, color 0.15s ease.

![Category card (dark) default](components/crops/hd-card-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the nav bar, the menu toggle and the Start-now pill.

#### Mobile nav bar
The phone nav bar: wordmark, menu toggle and the Start-now pill. Read as `m-nav` on the home page at 390 wide.

**Values (default).** size 390 x 64; padding 0px 20px; background transparent; text Suisse Intl 16/26.4 400, #ffffff `_primitives.color.paper.default`; transition color 0.32s ease; icon 113 x 20, #ffffff `_primitives.color.paper.default`; layers ::before rgb(10, 10, 10) 0px none 0; nav::before.nav-bar.is-warm 390pxx64px rgb(10, 10, 10); a::after.nav-link 100%x1px rgb(255, 255, 255); a::after.mega-link 100%x1px rgb(255, 255, 255); a::after.mega-link 100%x1px rgb(255, 255, 255); a::after.mega-link 100%x1px rgb(255, 255, 255); a::after.mega-link 100%x1px rgb(255, 255, 255).

Child layers that carry the look: nav::before 390pxx64px background #0a0a0a `_primitives.color.ink.default`; a::after 100%x1px background #ffffff `_primitives.color.paper.default`; a::after 100%x1px background #ffffff `_primitives.color.paper.default`.

![Mobile nav bar default](components/crops/m-nav-default.png)

#### Menu toggle
The mobile menu toggle; measured, never used to navigate. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 44 x 44; background transparent; text Suisse Intl 16/26.4 400, #ffffff `_primitives.color.paper.default`; layers span.nav-burger-bar 22.0x2.0 rgb(255, 255, 255); span.nav-burger-bar 22.0x2.0 rgb(255, 255, 255) |
| focus-visible | outline 1px auto #e59700, offset 0px; layers button.nav-burger 44.0x44.0 1px auto rgb(229, 151, 0) offset 0px; span.nav-burger-bar 22.0x2.0 rgb(255, 255, 255); span.nav-burger-bar 22.0x2.0 rgb(255, 255, 255) |

Child layers that carry the look: span 22x2 background #ffffff `_primitives.color.paper.default`; span 22x2 background #ffffff `_primitives.color.paper.default`.

![Menu toggle default](components/crops/m-menu-btn-default.png) ![Menu toggle hover](components/crops/m-menu-btn-hover.png) ![Menu toggle focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Menu toggle pressed](components/crops/m-menu-btn-pressed.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 350 x 131; background transparent; text Saans 29.25/32.76 420, #ffffff `_primitives.color.paper.default`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

### Footer

The .site-footer.is-warm footer — sitemap columns, legal links and social icons on the ink surface.

#### Footer
The .site-footer.is-warm footer — sitemap columns, social and legal links on the ink surface. Read as `footer` on the home page.

**Values (default).** size 1440 x 362.33; padding 56px 40px 32px 40px; background #0a0a0a `_primitives.color.ink.default`; shadow #0a0a0a 0px 4px 0px 0px; text Suisse Intl 16.99/28.04 400, #ffffff `_primitives.color.paper.default`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 55 x 28.05; background transparent; text Suisse Intl 16.99/28.04 400, rgba(255, 255, 255, 0.5) `_primitives.color.paper.alpha.50`; transition color 0.2s ease; layers ::after rgba(255, 255, 255, 0.5) 0px none 1; a::after.footer-link 55pxx1px rgba(255, 255, 255, 0.5) |
| hover | text Suisse Intl 16.99/28.04 400, rgba(255, 255, 255, 0.9); layers ::after rgba(255, 255, 255, 0.9) 0px none 1; a::after.footer-link 55pxx1px rgba(255, 255, 255, 0.9) |
| focus-visible | outline 1px auto #101010, offset 1px; layers ::after rgba(255, 255, 255, 0.5) 0px none 1; a.footer-link 55.0x28.0 1px auto rgb(16, 16, 16) offset 1px; a::after.footer-link 55pxx1px rgba(255, 255, 255, 0.5) |
| pressed | text Suisse Intl 16.99/28.04 400, #ffffff `_primitives.color.paper.default`; layers ::after rgb(255, 255, 255) 0px none 1; a::after.footer-link 55pxx1px rgb(255, 255, 255) |

Child layers that carry the look: a::after 55pxx1px background rgba(255, 255, 255, 0.5) `_primitives.color.paper.alpha.50`.

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### On-ink (dark sections)

The marketing dark bands — .leg-section.gs1000, .wordmark-section, .closer-section, the .is-warm nav/footer — painted by the sheet's own on-ink scope classes, not a user theme.

#### Dark feature section
A .page-section.on-ink dark band — the sheet's own on-ink scope class repaints the --_surface---* variables; measured as painted, no theme toggle exists. Read as `leg-section` on the home page.

**Values (default).** size 1440 x 1355.89; padding 140px 40px; background #0a0a0a `_primitives.color.ink.default`; text Saans 57.6/60.48 420, #ffffff `_primitives.color.paper.default`; icon 9 x 9, #ffffff `_primitives.color.paper.default`.

![Dark feature section default](components/crops/leg-section-default.png)

#### Wordmark section
The dark "Made with Fourthwall" wordmark band — on-ink surface values. Read as `wordmark-section` on the home page.

**Values (default).** size 1440 x 456.75; padding 80px 40px 40px 40px; background #0a0a0a `_primitives.color.ink.default`; shadow #0a0a0a 0px -4px 0px 0px; text Suisse Intl 16.99/28.04 400, rgba(255, 255, 255, 0.5) `_primitives.color.paper.alpha.50`.

![Wordmark section default](components/crops/wordmark-section-default.png)

#### Closing CTA section
The closing "Make something worth buying / Start now for free" section. Read as `closer` on the home page.

**Values (default).** size 1440 x 512.8; padding 40px 0px 0px 0px; background #0a0a0a `_primitives.color.ink.default`; text Saans 57.6/60.48 420, #ffffff `_primitives.color.paper.default`; layers ::before rgb(173, 1, 50) 0px none 1.

![Closing CTA section default](components/crops/closer-default.png)

#### Made-with band
The .made-with "Made with Fourthwall" storefront showcase band — on-ink surface values. Read as `made-with` on the home page.

**Values (default).** size 1440 x 1067.19; padding 140px 0px 0px 0px; background #0a0a0a `_primitives.color.ink.default`; text Saans 57.6/60.48 420, #ffffff `_primitives.color.paper.default`.

![Made-with band default](components/crops/made-with-default.png)

#### Closer CTA
The giant "Make something worth buying" word-link in the closing section — it carries the start flow; measured, never followed. Read as `closer-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 412.88 x 135.47; background transparent; text Saans 57.6/60.48 420, #ffffff `_primitives.color.paper.default`; transition color 0.2s ease, text-decoration-color 0.2s ease |
| hover | size 429.42 x 140.88 |
| focus-visible | size 429.34 x 140.87; outline 1px auto #101010, offset 1px; layers a.closer-link 429.3x140.9 1px auto rgb(16, 16, 16) offset 1px |

![Closer CTA default](components/crops/closer-cta-default.png) ![Closer CTA hover](components/crops/closer-cta-hover.png) ![Closer CTA focus-visible](components/crops/closer-cta-focus-visible.png) ![Closer CTA pressed](components/crops/closer-cta-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Fourthwall wordmark, the nav mega-menu glyphs, the product and help category artwork, the Eli assistant marks) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Fourthwall's product is the creator storefront platform: every post-login surface — the shop dashboard (my-shop.fourthwall.com/admin), the product designer, checkout and order flows, the mobile app — needs an account and was never reached. /get-started (auth.fourthwall.com, Keycloak) is the only account surface a signed-out visitor sees, and it was measured at rest: the Google/Apple/email provider buttons were never pressed, and the signup modal's controls were never submitted. The PDP's 'Sign in to design' starts the same flow and was measured, never activated.

### Pages

- **The account.** Every post-login surface was never reached; no provider button was pressed, nothing was typed into an auth field, and the Keycloak URLs carry session/signing parameters that were sanitized out of every sidecar and never stored.
- **The signup modal.** The marketing sheet mounts a `.signup-modal` (Google/Apple/email) but the nav 'Start now' control navigates to /get-started on this build, so the modal was not reachable as a local toggle — its markup was probed, the auth shell it leads to was shot instead.
- **Feature/product pages** beyond the captured set (/design-and-sell, /bespoke, /designers, /websites, /print-on-demand, the /features/* detail pages, /ai-assistant-eli, the other /compare/* pages, /legal/*) are the same templates, unmeasured; one example of each family was captured.
- **Blog posts and help articles** — the indexes and one category were captured; individual articles are the same template, unmeasured.
- **The home page is ~14k px tall** — captured in full, stitched from contiguous parts (the part clips are recorded in the `.capture.json` sidecar).

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the search fields were typed into then cleared, and no form was ever submitted.
- **The quiz's later steps** (recommendations after several answers), the catalogue's logged-in design controls and any cart state are boundary states — the quiz was answered once, never completed.

### Themes

The marketing site paints one light surface — no user-facing theme control was found (`color-scheme: normal`); its dark bands are the sheet's own on-ink scope classes (.on-ink, .leg-section.gs1000, .wordmark-section, .closer-section, the .is-warm nav/footer), captured as the ink set. products.fourthwall.com declares every role as a light-dark() pair — the catalogDark set is the declared dark branch resolved under a forced color-scheme probe: declared, not observed (the catalogue ships no theme toggle and no dark paint was captured signed out). docs.fourthwall.com's 'Change theme preference' menu sets html.dark for real (the docsDark set and measurements). help.fourthwall.com's colour-mode toggle sets data-theme="dark" for real (the helpDark set and measurements).

### Fonts

- **Suisse Intl** (marketing + help) and **Saans** (display) are served proprietary faces; **Inter** (docs) and a mono appear on the docs/catalogue hosts. The style guide falls back to system sans.

### Screenshots

- The product photos, creator names, shop examples and logo walls are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article copy, product descriptions, creator names and shop handles are the product's content; only frames and components were measured.
