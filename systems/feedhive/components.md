# FeedHive components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from feedhive.com on 2026-11-15, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the bio-generator and sign-in/sign-up forms were never sent; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (55 components, 130 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/22.5 600, #23252b`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (128 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` — every surface paints light; the marketing site ships no dark mode and no user theme toggle, and the app.feedhive.com sign-in/up cards are light too. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x (bounded to 8 viewport chunks where a page runs long, with the boundary noted in the sidecars); mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu-agents-automation](screenshots/home-light-menu-agents-automation.png), [menu-product](screenshots/home-light-menu-product.png) |
| Pricing | `/pricing` | [billing-monthly](screenshots/pricing-light-billing-monthly.png), [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Feature: Scheduling | `/features/scheduling` | [default](screenshots/features-scheduling-light-default.png), [full](screenshots/features-scheduling-light-full.png) |
| Feature: AI | `/features/ai` | [default](screenshots/features-ai-light-default.png), [full](screenshots/features-ai-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Blog article | `/blog (one article route)` | [default](screenshots/blog-article-light-default.png), [full](screenshots/blog-article-light-full.png) |
| Integrations | `/integrations` | [default](screenshots/integrations-light-default.png), [full](screenshots/integrations-light-full.png) |
| Tools | `/tools` | [default](screenshots/tools-light-default.png), [full](screenshots/tools-light-full.png) |
| Bio generator | `/tools/bio-generator` | [default](screenshots/tools-bio-light-default.png), [full](screenshots/tools-bio-light-full.png) |
| Alternatives | `/alternatives` | [default](screenshots/alternatives-light-default.png), [full](screenshots/alternatives-light-full.png) |
| Privacy policy | `/privacy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Terms of service | `/terms` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| App sign-in | `app.feedhive.com/signin` | [default](screenshots/login-light-default.png) |
| App sign-up | `app.feedhive.com/signup` | [default](screenshots/signup-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Tools, phone | `/tools` | [default](screenshots/mobile-tools-light-default.png), [full](screenshots/mobile-tools-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent | every page | the vanilla-cookieconsent layer (#cc-main) mounts but stays empty on every observed load; any consent overlay would be hidden, never answered | hidden before every shot and reading |
| Nav dropdowns | every page header | clicked the Product / Agents & Automation triggers (local UI toggles, anchors with aria-haspopup) | [home-light-menu-product](screenshots/home-light-menu-product.png), [home-light-menu-agents-automation](screenshots/home-light-menu-agents-automation.png), [nav-panel](#nav-dropdown-panel), [nav-menu-item](#nav-dropdown-item) |
| Billing toggle | /pricing | clicked the Monthly half of the billing pill (a local UI toggle) | [pricing-light-billing-monthly](screenshots/pricing-light-billing-monthly.png), [billing-monthly](#billing-toggle-monthly) |
| Mobile nav overlay | home page, phone width | the icon-only menu button's own toggle | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-drawer](#mobile-nav-overlay) |
| Bio-generator fields | /tools/bio-generator | typed into then cleared — nothing sent | [bio-textarea](#bio-input) |
| Sign-in/up fields | app.feedhive.com/signin and /signup | typed into then cleared — nothing sent | [login-field-email](#email-field-sign-in), [signup-field](#field-sign-up) |
| Signed-in product | a FeedHive account | every post-login surface (the composer, scheduler, analytics, docs at docs.feedhive.com) needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 16 components were given a real keyboard focus. 11 draw an outline ring: `nav-dropdown` (1px auto #101010, offset 1px), `nav-link` (1px auto #101010, offset 1px), `nav-login` (1px auto #101010, offset 1px), `nav-signup` (1px auto #101010, offset 1px), `hero-cta` (1px auto #101010, offset 1px), `footer-link` (1px auto #101010, offset 1px), `billing-yearly` (1px auto #101010, offset 0px), `plan-cta` (1px auto #101010, offset 1px), `feat-cta` (1px auto #101010, offset 1px), `m-menu-btn` (1px auto #e59700, offset 0px), `m-hero-cta` (1px auto #e59700, offset 1px). 4 drop their resting shadow without drawing a ring (the Chakra controls' focus-visible outline is the transparent 2px spec they already paint at rest): `login-google`, `login-submit`, `signup-google`, `signup-submit`. The other 1 show no measured change: `login-forgot`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0, 0, 0.2, 1)` | background-color, border-color, box-shadow, color, fill, opacity, stroke, transform | login-forgot |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, backdrop-filter, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | agent-card, billing-monthly, billing-yearly, bio-platform, bio-tone, footer-link, m-menu-btn, nav-dropdown and more |
| 0.2s | `ease` | background-color, border-color, box-shadow, color, fill, opacity, stroke, transform | login-field-email, login-field-pass, login-google, login-submit, signup-field, signup-google, signup-submit |
| 0.3s | `cubic-bezier(0.22, 1, 0.36, 1)` | box-shadow, transform | feat-card |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | bio-submit, feat-cta, hero-cta, m-hero-cta |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Nav dropdown panel](#nav-dropdown-panel) | 1440 x 316 | - | - | transparent | none | 0 |
| [Agent card](#agent-card) | 585 x 416.16 | - | 15px | #f6f6f8 | rgba(255, 255, 255, 0.7) 0px 1px 0px 0px inset | 24px 34px 0px 34px |
| [Plan card (Business)](#plan-card-business) | 297 x 652.5 | 1px solid #4457ff | 16px | #4457ff | none | 20px 20px 24px 20px |
| [Plan card (Creator)](#plan-card-creator) | 297 x 652.5 | 1px solid #e8e4dd | 16px | #ffffff `color.white` | none | 20px 20px 24px 20px |
| [Feature card](#feature-card) | 247.19 x 225 | - | 0px 0px 5px 0px | #ffffff `color.white` | rgba(66, 74, 119, 0.08) 0px 24px 60px 0px | 0 |
| [Article row](#article-row) | 382.66 x 598.28 | - | - | transparent | none | 0 |
| [Bio input](#bio-input) | 362 x 110 | - | 12px | transparent | none | 14px 16px 0px 16px |
| [Sign-in card](#sign-in-card) | 512 x 610.31 | - | 20px | #ffffff `color.white` | rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.04) 0px 10px 10px -5px | 44.16px |
| [Mobile nav overlay](#mobile-nav-overlay) | 390 x 844 | - | - | #fbfaf7 | none | 0 |

## Components

### Promo bar

The 38px launch banner on top of every marketing page ('Limited launch bonus: Double your AI credits for 3 months when you start today →').

#### Launch promo bar
The top banner ("Limited launch bonus: Double your AI credits for 3 months when you start today →"); measured, never followed. Read as `promo-bar` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1440 x 38; padding 8px 16px; border B: 1px solid oklab(0 0 0 / 0.05); background #f4f3f2; text Inter 14/21 600, #2d2f35; icon 14 x 14, #4f5fd7 |

![Launch promo bar default](components/crops/promo-bar-default.png) ![Launch promo bar hover](components/crops/promo-bar-hover.png)

### Site chrome

The 80px header on every marketing page: the FeedHive mark, the Product / Agents & Automation / Socials / Learn dropdown triggers (anchors with aria-haspopup that open a white mega-panel), Pricing, the neutral Login pill and the indigo Sign Up pill.

#### Site header
The 80px header below the promo bar: FeedHive mark, Product / Agents & Automation / Socials / Learn dropdowns, Pricing, Login and the indigo Sign Up pill. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 80; padding 20px 32px; background transparent; text Inter 14/21 500, #4f5562; icon 12 x 12, #4f5562; layers a.inline-flex.h-10 0.0x0.0 rgb(68, 87, 255) 11px; a.inline-flex.h-10 73.6x40.0 rgb(244, 242, 240) 11px; a.inline-flex.h-10 88.0x40.0 rgb(68, 87, 255) 11px.

Child layers that carry the look: a 0x0 background #4457ff radius 11px; a 73.6x40 background #f4f2f0 radius 11px; a 88x40 background #4457ff radius 11px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The FeedHive mark-and-wordmark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 118 x 30.23; background transparent; text Inter 16/24 400, #20232b.

![Logo default](components/crops/mkt-logo-default.png)

#### Nav dropdown trigger
The "Product" header trigger — an anchor with href="#" and aria-haspopup="true" that opens the product dropdown. The opened state was measured after clicking it. Read as `nav-dropdown` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 69.03 x 21; background transparent; text Inter 14/21 500, #4f5562; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, #4f5562 |
| hover | text Inter 14/21 500, #22252d; icon 12 x 12, #22252d |
| focus-visible | outline 1px auto #101010, offset 1px; text Inter 14/21 500, #22252d; icon 12 x 12, #22252d; layers a.flex.items-center 69.0x21.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed, opened | text Inter 14/21 500, #22252d; icon 12 x 12, #22252d |

![Nav dropdown trigger default](components/crops/nav-dropdown-default.png) ![Nav dropdown trigger hover](components/crops/nav-dropdown-hover.png) ![Nav dropdown trigger focus-visible](components/crops/nav-dropdown-focus-visible.png) ![Nav dropdown trigger pressed](components/crops/nav-dropdown-pressed.png) ![Nav dropdown trigger opened](components/crops/nav-dropdown-opened.png)

#### Nav dropdown panel
The dropdown panel opened by the Product trigger; its links were never followed. Read as `nav-panel` on the home page.

**Values (default).** size 1440 x 316; background transparent; text Inter 12/18 500, #8b9098; icon 20 x 20, #5c7cfa; layers div.border-b.border-t 1440.0x316.0 rgb(255, 255, 255) T:1px solid rgb(239, 239, 237) / B:1px solid rgb(239, 239, 237) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 23, 42, 0.08) 0px 18px 40px 0px; span.flex.h-12 48.0x48.0 rgb(255, 255, 255) T:1px solid rgb(232, 231, 228) / R:1px solid rgb(232, 231, 2.

Child layers that carry the look: div 1440x316 background #ffffff `color.white` border 1px solid #efefed shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(15, 23, 42, 0.08) 0px 18px 40px 0px; span 48x48 background #ffffff `color.white` border 1px solid #e8e7e4 radius 14px; span 48x48 background #ffffff `color.white` border 1px solid #e8e7e4 radius 14px.

![Nav dropdown panel default](components/crops/nav-panel-default.png)

#### Nav dropdown item
A link inside the opened dropdown panel; measured, never followed. Read as `nav-menu-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 369.33 x 56; padding 4px; radius 18px; background transparent; text Inter 15/22.5 600, #17191f; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #5c7cfa; layers span.flex.h-12 48.0x48.0 rgb(255, 255, 255) T:1px solid rgb(232, 231, 228) / R:1px solid rgb(232, 231, 228) / B:1px solid rgb(232, 231, 228) / L:1px solid rgb(232, 231, 228) 14px |
| hover | background #f8f8f7; layers none |

Child layers that carry the look: span 48x48 background #ffffff `color.white` border 1px solid #e8e7e4 radius 14px.

![Nav dropdown item default](components/crops/nav-menu-item-default.png) ![Nav dropdown item hover](components/crops/nav-menu-item-hover.png)

#### Nav link
The "Pricing" header link; measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 47.03 x 21; background transparent; text Inter 14/21 500, #4f5562; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 14/21 500, #22252d |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.flex.items-center 47.0x21.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Inter 14/21 500, #22252d |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Login button
The light "Login" pill in the header linking to app.feedhive.com; measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73.61 x 40; padding 0px 18px; radius 11px; background #f4f2f0; text Inter 14/21 500, #272b34; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #efedeb |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #efedeb |

![Login button default](components/crops/nav-login-default.png) ![Login button hover](components/crops/nav-login-hover.png) ![Login button focus-visible](components/crops/nav-login-focus-visible.png) ![Login button pressed](components/crops/nav-login-pressed.png)

#### Sign Up button
The indigo "Sign Up" pill in the header linking to app.feedhive.com/signup; measured, never followed. Read as `nav-signup` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 88.05 x 40; padding 0px 18px; radius 11px; background #4457ff; text Inter 14/21 500, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #3347fb |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #3347fb |

![Sign Up button default](components/crops/nav-signup-default.png) ![Sign Up button hover](components/crops/nav-signup-hover.png) ![Sign Up button focus-visible](components/crops/nav-signup-focus-visible.png) ![Sign Up button pressed](components/crops/nav-signup-pressed.png)

### Home

The hero on www.feedhive.com: the gradient-ring 'Introducing FeedHive v2.0' badge, the 55px Plus Jakarta Sans masthead 'Social media using Automation & AI Agents.', the muted lede, the 50px indigo 'Get started for free' CTA, the checked feature rows, the clipped product screenshot and the agent/feature cards further down.

#### Release badge
The "Introducing FeedHive v2.0" pill badge over the hero — the gradient-ring outer div. Read as `hero-badge` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 217.94 x 35; radius 3.35544e+07px; background transparent; text Inter 14/21 700, #31343a; layers ::before rgba(0, 0, 0, 0) 0px none 0; ::after rgba(0, 0, 0, 0) 0px none 0; div::before.cta-gradient-ring.cta-gradient-ring-pill 223.938pxx41px 9999px; div::after.cta-gradient-ring.cta-gradient-ring-pill 227.938pxx45px 9999px; div.inline-flex.items-center 217.9x35.0 rgb(255, 255, 255) T:1px solid rgb(223, 223, 228) / R:1px solid rgb(223, 223, 228) / B:1px solid rgb(223, 223, 228) / L:1px solid rgb( |
| hover | layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1; div::before.cta-gradient-ring.cta-gradient-ring-pill 223.938pxx41px 9999px; div::after.cta-gradient-ring.cta-gradient-ring-pill 227.938pxx45px 9999px; div.inline-flex.items-center 217.9x35.0 rgb(255, 255, 255) T:1px solid rgb(223, 223, 228) / R:1px solid rgb(223, 223, 228) / B:1px solid rgb(223, 223, 228) / L:1px solid rgb( |

Child layers that carry the look: div::before 223.938pxx41px image conic-gradient(from 0deg, #4f7dff, #7165ff, #d650ff, #ff7f59, #4f7dff) radius 9999px; div::after 227.938pxx45px image radial-gradient(circle, rgba(99, 110, 255, 0.42), transparent 68%) radius 9999px; div 217.9x35 background #ffffff `color.white` border 1px solid #dfdfe4 radius 3.35544e+07px.

![Release badge default](components/crops/hero-badge-default.png) ![Release badge hover](components/crops/hero-badge-hover.png)

#### Hero headline
"Social media using Automation & AI Agents." — the display heading; the second line paints the indigo accent. Read as `hero-h1` on the home page.

**Values (default).** size 620 x 115.45; background transparent; text Plus Jakarta Sans 55/56.1 600, #23252b; layers span.agent-logo-badge 51.7x51.7 rgba(255, 255, 255, 0.98) T:1px solid rgba(207, 211, 221, 0.9) / R:1px solid rgba(207, 211, 221, 0.9) / B:1px solid rgba(207, 211, 221, 0.9) / L:1px solid rgba(207, 211, 221, 0.9) 11px.

Child layers that carry the look: span 51.7x51.7 background rgba(255, 255, 255, 0.98) border 1px solid rgba(207, 211, 221, 0.9) radius 11px.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero lede
The muted lede under the headline. Read as `hero-sub` on the home page.

**Values (default).** size 560 x 48; background transparent; text Inter 16/24 400, #666c77.

![Hero lede default](components/crops/hero-sub-default.png)

#### Hero CTA
The indigo "Get started for free" button in the hero; measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 196.02 x 50; padding 0px 32px; radius 15px; background #4457ff; text Inter 15/22.5 500, #ffffff `color.white`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #3347fb |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #3347fb |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Feature check row
A checked feature row ("Create with AI. Generate content that fits your tone-of-voice & brand."). Read as `hero-check` on the home page.

**Values (default).** size 560 x 23.19; background transparent; text Inter 16/23.2 700, #24262d; icon 16 x 16, #4457ff.

![Feature check row default](components/crops/hero-check-default.png)

#### Product mock panel
The product screenshot beside the hero — a static public image clipped by a rounded container, not the signed-in product. Read as `hero-mock` on the home page.

**Values (default).** size 688.48 x 592.52; radius 16px 0px 0px 16px; background transparent; text Inter 16/24 400, #20232b; layers div.pointer-events-none.absolute 89.5x592.5; div.pointer-events-none.absolute 688.5x100.7.

Child layers that carry the look: div 89.5x592.5 image linear-gradient(to left, #ffffff `color.white` 0%, oklab(0.999994 0.0000455678 0.000020086; div 688.5x100.7 image linear-gradient(to top, #ffffff `color.white` 0%, oklab(0.999994 0.0000455678 0.0000200868.

![Product mock panel default](components/crops/hero-mock-default.png)

#### Agent card
An AI-agent feature card ("Hermes Agent ↗ — Use Herm…") on the home page; measured, never followed. Read as `agent-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 585 x 416.16; padding 24px 34px 0px 34px; radius 15px; background #f6f6f8; shadow rgba(255, 255, 255, 0.7) 0px 1px 0px 0px inset; text Sometype Mono 11/16.5 700, #4457ff; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f0f1f6 |

![Agent card default](components/crops/agent-card-default.png) ![Agent card hover](components/crops/agent-card-hover.png)

#### Section heading
A marketing section heading further down the home page. Read as `section-h2` on the home page.

**Values (default).** size 760 x 113.66; background transparent; text Plus Jakarta Sans 58/56.84 600, #23252b.

![Section heading default](components/crops/section-h2-default.png)

### Feature tabs

The feature showcase tab pills (Composer / AI Assistant / Automation / …) that switch the demo panel — dashed-border pills that select into the indigo tint.

#### Feature tab pill
One of the feature tab pills (Composer / AI Assistant / Automation / …) that switch the showcase panel — a local UI toggle; selected by clicking. Read as `tab-pill` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 94.77 x 30; padding 0px 12px; border 1px dashed #d8dbe2; radius 3.35544e+07px; background #ffffff `color.white`; text Inter 14/21 500, #585f6b; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px dashed #979daa; text Inter 14/21 500, #2c3139 |
| selected | size 106.77 x 30; padding 0px 20px 0px 16px; border 1px solid #84a1ff; background #eef2ff; text Inter 14/21 500, #5a84ff; icon 14 x 14, #ffffff `color.white` |

![Feature tab pill default](components/crops/tab-pill-default.png) ![Feature tab pill hover](components/crops/tab-pill-hover.png) ![Feature tab pill selected](components/crops/tab-pill-selected.png)

#### Feature tab pill (active)
A feature tab pill in its selected state — the #eef2ff indigo tint, #84a1ff border and #5a84ff ink the pills select into; selected by clicking (the at-load selection auto-rotates). Read as `tab-pill-active` on the home page.

**Values (selected).** size 116.64 x 30; padding 0px 20px 0px 16px; border 1px solid #84a1ff; radius 3.35544e+07px; background #eef2ff; text Inter 14/21 500, #5a84ff; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, #ffffff `color.white`.

![Feature tab pill (active) selected](components/crops/tab-pill-active-selected.png)

### Pricing

The /pricing page: masthead, the Monthly/Yearly billing pill, the indigo Business plan card beside the white plan cards, the 50px Get started buttons and the 7-day-free-trial gradient-ring badge.

#### Pricing headline
"The best social solution, for the best price." — the /pricing masthead. Read as `price-h1` on the pricing page.

**Values (default).** size 760 x 125.44; background transparent; text Plus Jakarta Sans 64/62.72 600, #23252b.

![Pricing headline default](components/crops/price-h1-default.png)

#### Billing toggle (Monthly)
The "Monthly" half of the billing pill — a local UI toggle that re-renders the prices; selected by clicking. Read as `billing-monthly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 112 x 41; padding 10px 20px; radius 3.35544e+07px; background transparent; text Inter 14/21 600, #757b86; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 14/21 600, #2b2f37 |
| selected | background #3347fb; text Inter 14/21 600, #ffffff `color.white` |

![Billing toggle (Monthly) default](components/crops/billing-monthly-default.png) ![Billing toggle (Monthly) hover](components/crops/billing-monthly-hover.png) ![Billing toggle (Monthly) selected](components/crops/billing-monthly-selected.png)

#### Billing toggle (Yearly)
The "Yearly" half of the billing pill, selected on load. Read as `billing-yearly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 112 x 41; padding 10px 20px; radius 3.35544e+07px; background #4457ff; text Inter 14/21 600, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #3347fb |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background #3347fb |

![Billing toggle (Yearly) default](components/crops/billing-yearly-default.png) ![Billing toggle (Yearly) hover](components/crops/billing-yearly-hover.png) ![Billing toggle (Yearly) focus-visible](components/crops/billing-yearly-focus-visible.png) ![Billing toggle (Yearly) pressed](components/crops/billing-yearly-pressed.png)

#### Plan card (Business)
The highlighted indigo "Business" plan card ("POPULAR" chip). Read as `plan-card` on the pricing page.

**Values (default).** size 297 x 652.5; padding 20px 20px 24px 20px; border 1px solid #4457ff; radius 16px; background #4457ff; text Plus Jakarta Sans 31/31 600, #ffffff `color.white`; icon 14 x 14, #ffffff `color.white`.

![Plan card (Business) default](components/crops/plan-card-default.png)

#### Plan card (Creator)
A plain plan card beside the highlighted one. Read as `plan-card-plain` on the pricing page.

**Values (default).** size 297 x 652.5; padding 20px 20px 24px 20px; border 1px solid #e8e4dd; radius 16px; background #ffffff `color.white`; text Plus Jakarta Sans 31/31 600, #23252b; icon 14 x 14, #2c3138.

![Plan card (Creator) default](components/crops/plan-card-plain-default.png)

#### Plan CTA
A plan card's "Get started" button; measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 255 x 50; padding 0px 20px; radius 15px; background #4457ff; text Inter 15/22.5 600, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #3347fb |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #3347fb |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Trial badge
The "7-day free trial" pill over the plan cards — the gradient-ring outer div. Read as `trial-badge` on the pricing page.

**Values (default).** size 154.28 x 35; radius 3.35544e+07px; background transparent; text Inter 14/21 700, #31343a; icon 16 x 16, #5a78ff; layers ::before rgba(0, 0, 0, 0) 0px none 0; ::after rgba(0, 0, 0, 0) 0px none 0; div::before.cta-gradient-ring.cta-gradient-ring-pill 160.281pxx41px 9999px; div::after.cta-gradient-ring.cta-gradient-ring-pill 164.281pxx45px 9999px; div.inline-flex.items-center 154.3x35.0 rgb(255, 255, 255) T:1px solid rgb(223, 223, 228) / R:1px solid rgb(223, 223, 228) / B:1px solid rgb(223, 223, 228) / L:1px solid rgb(.

Child layers that carry the look: div::before 160.281pxx41px image conic-gradient(from 0deg, #4f7dff, #7165ff, #d650ff, #ff7f59, #4f7dff) radius 9999px; div::after 164.281pxx45px image radial-gradient(circle, rgba(99, 110, 255, 0.42), transparent 68%) radius 9999px; div 154.3x35 background #ffffff `color.white` border 1px solid #dfdfe4 radius 3.35544e+07px.

![Trial badge default](components/crops/trial-badge-default.png)

### Feature pages

The /features/scheduling masthead: the Sometype Mono tracked caps eyebrow, the 62px masthead, the Get started CTA and the white feature cards in the grid below.

#### Page eyebrow
The tracked caps eyebrow label ("SCHEDULING", Sometype Mono) over the feature page masthead. Read as `feat-eyebrow` on the features/scheduling page.

**Values (default).** size 560 x 21; background transparent; text Sometype Mono 14/21 700, #4457ff.

![Page eyebrow default](components/crops/feat-eyebrow-default.png)

#### Feature headline
"Plan and schedule your content." — the /features/scheduling masthead. Read as `feat-h1` on the features/scheduling page.

**Values (default).** size 560 x 121.5; background transparent; text Plus Jakarta Sans 62/60.76 600, #23252b.

![Feature headline default](components/crops/feat-h1-default.png)

#### Feature CTA
The feature page's "Get started for free" call-to-action; measured, never followed. Read as `feat-cta` on the features/scheduling page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 196.02 x 50; padding 0px 32px; radius 15px; background #4457ff; text Inter 15/22.5 500, #ffffff `color.white`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #3347fb |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #3347fb |

![Feature CTA default](components/crops/feat-cta-default.png) ![Feature CTA hover](components/crops/feat-cta-hover.png) ![Feature CTA focus-visible](components/crops/feat-cta-focus-visible.png) ![Feature CTA pressed](components/crops/feat-cta-pressed.png)

#### Feature card
A feature card in the scheduling page grid ("AI Image Generation", "Post Recycling", …). Read as `feat-card` on the features/scheduling page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 247.19 x 225; radius 0px 0px 5px 0px; background #ffffff `color.white`; shadow rgba(66, 74, 119, 0.08) 0px 24px 60px 0px; text Plus Jakarta Sans 20/30 600, #2f3343; transition transform 0.3s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.3s cubic-bezier(0.22, 1, 0.36, 1); icon 19 x 19, #df6b85 |
| hover | size 249.66 x 227.25; shadow rgba(66, 74, 119, 0.14) 0px 30px 68px 0px; text Plus Jakarta Sans 20/30 600, #232735; icon 19.77 x 19.77, #df6b85 |

![Feature card default](components/crops/feat-card-default.png) ![Feature card hover](components/crops/feat-card-hover.png)

### Blog

The /blog index: masthead, the featured article card and the archive rows.

#### Blog headline
"FeedHive blog" — the /blog masthead. Read as `blog-h1` on the blog page.

**Values (default).** size 760 x 65.27; background transparent; text Plus Jakarta Sans 68/65.28 600, #23252b.

![Blog headline default](components/crops/blog-h1-default.png)

#### Featured post card
The featured article card on the blog index; measured, never followed. Read as `blog-card` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1248 x 419.59; background transparent; text Inter 11/16.5 600, #516fe2; layers div.overflow-hidden.rounded-[16px] 652.3x366.9 rgb(239, 239, 243) 16px; span.inline-flex.items-center 138.0x30.5 rgb(255, 255, 255) T:1px solid rgb(223, 226, 234) / R:1px solid rgb(223, 226, 234) / B:1px solid rgb(223, 226, 234) / L:1px solid rgb(223, 226, 234) 3.35544e+07px; div.mt-8.flex 555.7x80.0 rgb(246, 246, 248) 16px; span.inline-flex.min-h-[40px] 114.6x40.0 rgb(255, 255, 255) 11px |
| hover | layers div.overflow-hidden.rounded-[16px] 652.3x366.9 rgb(239, 239, 243) 16px; span.inline-flex.items-center 138.0x30.5 rgb(255, 255, 255) T:1px solid rgb(223, 226, 234) / R:1px solid rgb(223, 226, 234) / B:1px solid rgb(223, 226, 234) / L:1px solid rgb(223, 226, 234) 3.35544e+07px; div.mt-8.flex 555.7x80.0 rgb(241, 242, 245) 16px; span.inline-flex.min-h-[40px] 114.6x40.0 rgb(255, 255, 255) 11px |

Child layers that carry the look: div 652.3x366.9 background #efeff3 radius 16px; span 138x30.5 background #ffffff `color.white` border 1px solid #dfe2ea radius 3.35544e+07px; div 555.7x80 background #f6f6f8 radius 16px.

![Featured post card default](components/crops/blog-card-default.png)

#### Article row
An article card/row in the archive list; measured, never followed. Read as `blog-row` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 382.66 x 598.28; background transparent; text Inter 13/19.5 500, #6c7280; layers article.flex.h-full 382.7x598.3 rgb(246, 246, 248) 16px; div.overflow-hidden.bg-[#eceef3] 382.7x215.2 rgb(236, 238, 243); div.mt-6.border-t 326.7x60.0 T:1px solid rgb(231, 232, 236) |
| hover | layers article.flex.h-full 382.7x598.3 rgb(241, 242, 245) 16px; div.overflow-hidden.bg-[#eceef3] 382.7x215.2 rgb(236, 238, 243); div.mt-6.border-t 326.7x60.0 T:1px solid rgb(231, 232, 236) |

Child layers that carry the look: article 382.7x598.3 background #f6f6f8 radius 16px; div 382.7x215.2 background #eceef3; div 326.7x60 border 1px solid #e7e8ec.

![Article row default](components/crops/blog-row-default.png) ![Article row hover](components/crops/blog-row-hover.png)

### Tools

The /tools/bio-generator free tool: platform and tone option chips, the describe-yourself textarea and the Generate submit — measured and typed into then cleared, never submitted.

#### Tool headline
"Free AI bio generator for social media" — the /tools/bio-generator masthead. Read as `bio-h1` on the tools/bio-generator page.

**Values (default).** size 760 x 122.38; background transparent; text Plus Jakarta Sans 60/61.2 600, #23252b.

![Tool headline default](components/crops/bio-h1-default.png)

#### Platform option
A platform option button (TikTok / Instagram / LinkedIn) — a local UI toggle; selected by clicking. Read as `bio-platform` on the tools/bio-generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, selected) | size 116 x 40; radius 9px; background #ffffff `color.white`; shadow #dfdfe4 0px 0px 0px 1px; text Inter 14/21 500, #23252b; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 15 x 15, #23252b |

![Platform option default](components/crops/bio-platform-default.png) ![Platform option hover](components/crops/bio-platform-hover.png) ![Platform option selected](components/crops/bio-platform-selected.png)

#### Tone option
A tone option button (Professional / Friendly / Funny / Bold / Aesthetic); measured at rest. Read as `bio-tone` on the tools/bio-generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 104.89 x 36; padding 0px 14px; border 1px solid #dfdfe4; radius 3.35544e+07px; background #ffffff `color.white`; text Inter 13/19.5 500, #4c525e; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #c6cad4; background #fafafa |

![Tone option default](components/crops/bio-tone-default.png) ![Tone option hover](components/crops/bio-tone-hover.png)

#### Bio input
The "describe yourself" textarea; focused and typed into then cleared — never submitted. Read as `bio-textarea` on the tools/bio-generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 362 x 110; padding 14px 16px 0px 16px; radius 12px; background transparent; text Inter 15/24 400, #23252b; placeholder #a3a8b3 |

![Bio input default](components/crops/bio-textarea-default.png) ![Bio input focused](components/crops/bio-textarea-focused.png) ![Bio input filled](components/crops/bio-textarea-filled.png)

#### Generate button
The "Generate bios" submit; its states were measured but the button was never clicked — nothing was submitted. Read as `bio-submit` on the tools/bio-generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 364 x 50; padding 0px 24px; radius 15px; background #b9c0f5; text Inter 15/22.5 500, #ffffff `color.white`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #ffffff `color.white` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Generate button default](components/crops/bio-submit-default.png) ![Generate button hover](components/crops/bio-submit-hover.png) ![Generate button pressed](components/crops/bio-submit-pressed.png)

### App sign-in (Chakra)

app.feedhive.com/signin — a separate Chakra-UI app: the white 512px card (20px radius, lift shadow) with the Google outline pill, OR divider, pill fields, the #3b82f6 Sign in submit and the Forgot-password link. Measured as a form, never submitted.

#### Sign-in card
The sign-in card over the pale field: "Let's get you signed in". Read as `login-panel` on the app sign-in page.

**Values (default).** size 512 x 610.31; padding 44.16px; radius 20px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.04) 0px 10px 10px -5px; text Inter 18.4/22.08 700, #1a202c `component.login.panel-ink`; icon 14.72 x 14.72, #ffffff `color.white`.

![Sign-in card default](components/crops/login-panel-default.png)

#### Google sign-in
The "Sign in with Google" outlined pill; measured, never followed. Read as `login-google` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 423.69 x 60.88; padding 29.44px; border 1px solid #edf2f7 `component.login.field-border`; radius 9999px; background transparent; shadow rgba(27, 25, 121, 0.05) 0px 2px 8px 0px; outline 2px solid transparent, offset 2px; text Inter 14.72/17.66 400, #1a202c `component.login.panel-ink`; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease |
| hover | background #f7fafc `component.login.google-hover` |
| focus-visible | shadow none |
| pressed | background #edf2f7 `component.login.field-border` |

![Google sign-in default](components/crops/login-google-default.png) ![Google sign-in hover](components/crops/login-google-hover.png) ![Google sign-in focus-visible](components/crops/login-google-focus-visible.png) ![Google sign-in pressed](components/crops/login-google-pressed.png)

#### Email field (sign-in)
The Email input on the app sign-in; focused and typed into then cleared — never submitted. Read as `login-field-email` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 423.69 x 60.88; padding 29.44px; border 1px solid #edf2f7 `component.login.field-border`; radius 9999px; background transparent; shadow rgba(27, 25, 121, 0.05) 0px 2px 8px 0px; outline 2px solid transparent, offset 2px; text Inter 14.72/22.08 400, #1a202c `component.login.panel-ink`; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; placeholder #a0aec0 |
| focused, filled | border 1px solid #3b82f6 `component.login.field-focus`; shadow none |

![Email field (sign-in) default](components/crops/login-field-email-default.png) ![Email field (sign-in) focused](components/crops/login-field-email-focused.png) ![Email field (sign-in) filled](components/crops/login-field-email-filled.png)

#### Password field (sign-in)
The Password input on the app sign-in; focused and typed into then cleared — never submitted. Read as `login-field-pass` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 423.69 x 60.88; padding 29.44px; border 1px solid #edf2f7 `component.login.field-border`; radius 9999px; background transparent; shadow rgba(27, 25, 121, 0.05) 0px 2px 8px 0px; outline 2px solid transparent, offset 2px; text Inter 14.72/22.08 400, #1a202c `component.login.panel-ink`; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; placeholder #a0aec0 |
| focused, filled | border 1px solid #3b82f6 `component.login.field-focus`; shadow none |

![Password field (sign-in) default](components/crops/login-field-pass-default.png) ![Password field (sign-in) focused](components/crops/login-field-pass-focused.png) ![Password field (sign-in) filled](components/crops/login-field-pass-filled.png)

#### Sign in submit
The sign-in submit button; its states were measured but the button was never clicked — nothing was submitted. Read as `login-submit` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 423.69 x 58.88; padding 29.44px; radius 9999px; background #3b82f6 `component.login.field-focus`; image linear-gradient(60deg, #4457ff, #7583fd); shadow rgba(89, 106, 255, 0.28) 0px 0px 35px 10px; outline 2px solid transparent, offset 2px; text Inter 14.72/17.66 600, #ffffff `color.white`; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 14.72 x 14.72, #ffffff `color.white` |
| hover | size 415.21 x 57.7; transform scale(0.98); icon 14.42 x 14.42, #ffffff `color.white` |
| focus-visible | shadow none |
| pressed | size 415.21 x 57.7; transform scale(0.98); icon 14.42 x 14.42, #ffffff `color.white` |

![Sign in submit default](components/crops/login-submit-default.png) ![Sign in submit hover](components/crops/login-submit-hover.png) ![Sign in submit focus-visible](components/crops/login-submit-focus-visible.png) ![Sign in submit pressed](components/crops/login-submit-pressed.png)

#### Forgot password link
The "Forgot your password?" link under the submit; measured, never followed. Read as `login-forgot` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 423.69 x 21; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/21 400, #5d60ec `component.login.link`; transition background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1); layers a.chakra-link.css-5orusm 423.7x21.0 2px solid rgba(0, 0, 0, 0) offset 2px |

Child layers that carry the look: a 423.7x21.

![Forgot password link default](components/crops/login-forgot-default.png) ![Forgot password link hover](components/crops/login-forgot-hover.png) ![Forgot password link focus-visible](components/crops/login-forgot-focus-visible.png) ![Forgot password link pressed](components/crops/login-forgot-pressed.png)

### App sign-up (Chakra)

app.feedhive.com/signup — the same Chakra-UI card system: Google outline pill, pill fields and the filled Sign up submit. Measured as a form, never submitted.

#### Sign-up card
The sign-up card on app.feedhive.com/signup. Read as `signup-panel` on the app sign-up page.

**Values (default).** size 512 x 821.42; padding 44.16px; radius 20px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.04) 0px 10px 10px -5px; text Inter 18.4/22.08 700, #1a202c `component.login.panel-ink`; icon 14.72 x 14.72, #ffffff `color.white`.

![Sign-up card default](components/crops/signup-panel-default.png)

#### Google sign-up
The Google sign-up button; measured, never followed. Read as `signup-google` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 423.69 x 60.88; padding 29.44px; border 1px solid #edf2f7 `component.login.field-border`; radius 9999px; background transparent; shadow rgba(27, 25, 121, 0.05) 0px 2px 8px 0px; outline 2px solid transparent, offset 2px; text Inter 14.72/17.66 400, #1a202c `component.login.panel-ink`; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease |
| hover | background #f7fafc `component.login.google-hover` |
| focus-visible | shadow none |
| pressed | background #edf2f7 `component.login.field-border` |

![Google sign-up default](components/crops/signup-google-default.png) ![Google sign-up hover](components/crops/signup-google-hover.png) ![Google sign-up focus-visible](components/crops/signup-google-focus-visible.png) ![Google sign-up pressed](components/crops/signup-google-pressed.png)

#### Field (sign-up)
The first text field on the app sign-up; focused and typed into then cleared — never submitted. Read as `signup-field` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 423.69 x 60.88; padding 29.44px; border 1px solid #edf2f7 `component.login.field-border`; radius 9999px; background transparent; shadow rgba(27, 25, 121, 0.05) 0px 2px 8px 0px; outline 2px solid transparent, offset 2px; text Inter 14.72/22.08 400, #1a202c `component.login.panel-ink`; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; placeholder #a0aec0 |
| focused, filled | border 1px solid #3b82f6 `component.login.field-focus`; shadow none |

![Field (sign-up) default](components/crops/signup-field-default.png) ![Field (sign-up) focused](components/crops/signup-field-focused.png) ![Field (sign-up) filled](components/crops/signup-field-filled.png)

#### Sign-up submit
The filled "Sign up" submit (the "Sign up with Google" outline is signup-google); its states were measured but the button was never clicked — nothing was submitted. Read as `signup-submit` on the app sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 423.69 x 58.88; padding 29.44px; radius 9999px; background #3b82f6 `component.login.field-focus`; image linear-gradient(60deg, #4457ff, #7583fd); shadow rgba(89, 106, 255, 0.28) 0px 0px 35px 10px; outline 2px solid transparent, offset 2px; text Inter 14.72/17.66 600, #ffffff `color.white`; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 14.72 x 14.72, #ffffff `color.white` |
| hover | size 415.21 x 57.7; transform scale(0.98); icon 14.42 x 14.42, #ffffff `color.white` |
| focus-visible | shadow none |
| pressed | size 415.21 x 57.7; transform scale(0.98); icon 14.42 x 14.42, #ffffff `color.white` |

![Sign-up submit default](components/crops/signup-submit-default.png) ![Sign-up submit hover](components/crops/signup-submit-hover.png) ![Sign-up submit focus-visible](components/crops/signup-submit-focus-visible.png) ![Sign-up submit pressed](components/crops/signup-submit-pressed.png)

### Mobile (390 wide)

The phone surface at 390 wide: the 76px header, the icon-only menu button and the full-viewport nav overlay (#fbfaf7), the hero and CTA.

#### Mobile header
The phone header: FeedHive mark, the icon-only menu button and the Sign Up pill. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 76; padding 16px; background transparent; text Inter 14/21 500, #ffffff `color.white`; layers a.inline-flex.h-10 88.0x40.0 rgb(68, 87, 255) 11px; a.inline-flex.h-10 0.0x0.0 rgb(244, 242, 240) 11px; a.inline-flex.h-10 0.0x0.0 rgb(68, 87, 255) 11px.

Child layers that carry the look: a 88x40 background #4457ff radius 11px; a 0x0 background #f4f2f0 radius 11px; a 0x0 background #4457ff radius 11px.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
The icon-only button (aria-label "Open menu") that opens the phone nav overlay — a local UI toggle; the opened state was measured after clicking it. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 44 x 44; background transparent; text Inter 16/24 400, #17191f; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #17191f |
| focus-visible | outline 1px auto #e59700, offset 0px; layers button.inline-flex.h-11 44.0x44.0 1px auto rgb(229, 151, 0) offset 0px |

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png) ![Mobile menu button opened](components/crops/m-menu-btn-opened.png)

#### Mobile nav overlay
The nav overlay opened by the menu button; its links were never followed. Read as `m-drawer` on the home page at 390 wide.

**Values (default).** size 390 x 844; background #fbfaf7; text Inter 14/21 500, #272b34; icon 20 x 20, #17191f.

![Mobile nav overlay default](components/crops/m-drawer-default.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 358 x 190.56; background transparent; text Plus Jakarta Sans 46/46.92 600, #23252b; icon 25.75 x 25.75, #ea4b71; layers span.agent-logo-badge 43.2x43.2 rgba(255, 255, 255, 0.98) T:1px solid rgba(207, 211, 221, 0.9) / R:1px solid rgba(207, 211, 221, 0.9) / B:1px solid rgba(207, 211, 221, 0.9) / L:1px solid rgba(207, 211, 221, 0.9) 9.2px.

Child layers that carry the look: span 43.2x43.2 background rgba(255, 255, 255, 0.98) border 1px solid rgba(207, 211, 221, 0.9) radius 9.2px.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The hero "Get started for free" button at 390 wide; measured, never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 196.02 x 50; padding 0px 32px; radius 15px; background #4457ff; text Inter 15/22.5 500, #ffffff `color.white`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto #e59700, offset 1px |

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

### Footer

The page footer: sitemap columns, legal links, social icons and the rounded feature chips row.

#### Footer
The page footer: sitemap columns, legal links, social icons, the cookie-preferences button. Read as `footer` on the home page.

**Values (default).** size 1440 x 814.47; background #ffffff `color.white`; text Inter 15/24.75 400, #737987; icon 18 x 18, #767c88.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 44.91 x 19; background transparent; text Inter 15/24 400, #676e7b; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 15/24 400, #22252d |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.transition.hover:text-[#22252d] 44.9x19.0 1px auto rgb(16, 16, 16) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the FeedHive bee mark, the dropdown tile glyphs, the social-channel marks, the check and arrow glyphs) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

FeedHive's product is the app at app.feedhive.com: every post-login surface — the composer, the scheduling calendar, AI generation, analytics — needs an account and was never reached. /signin and /signup are the only app surfaces a signed-out visitor sees, and they were measured as forms, never submitted; docs.feedhive.com is a separate docs site that was not captured. The product screenshots on the marketing pages are published images, not the product.

### Pages

- **The account.** Every post-login surface was never reached; the sign-in and sign-up forms were measured at rest and typed into then cleared — 'Sign in', 'Sign up' and the Google buttons were never pressed; what a submitted form returns is unverified.
- **Blog articles** are covered by one captured article route; the other posts are the same template, unmeasured.
- **Tools** — the /tools index plus one generator (bio-generator) were captured; the other generator routes are the same form pattern, unmeasured.
- **docs.feedhive.com** is a separate surface and was not captured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted (the bio Generate button rests in a desaturated #b9c0f5 fill, which looks disabled-adjacent but is the resting style).
- **Dropdown item focus** is partially covered: the panel closes on blur, so a real keyboard focus inside it could not always be held.

### Themes

The marketing site has no user theme toggle and no `prefers-color-scheme` switch: every page paints light — there is no data-mode attribute and no dark set on the public site. The app.feedhive.com sign-in/sign-up cards are light too, but they belong to a different design system (Chakra UI): a #3b82f6 submit blue, #5d60ec links, 9999px pill controls and a 20px card radius that share no token layer with the marketing site.

### Fonts

- **Inter** (variable wght 100–900, every control and body), **Plus Jakarta Sans** (display headings and plan names) and **Sometype Mono** (tracked caps eyebrows/labels) are the served faces, self-hosted via next/font from /_next/static. The style guide falls back to system sans. The Chakra app uses a plain Inter stack.

### Screenshots

- The product screenshots, brand logos and blog imagery in the captures are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article copy, integration names and the tool demos are the product's content; only frames and components were measured.
