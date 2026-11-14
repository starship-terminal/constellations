# Factory components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from factory.com, docs.factory.com and auth.factory.ai on 2026-11-14, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the contact and sign-in forms were never sent; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (59 components, 144 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one; a radius, font size, weight or line-height names its declared `radius.*`/`font.*` token the same way. Text is written family size/line-height weight, then its colour, for example `Geist 60.48/60.48 500 (font.size.measured.masthead, font.weight.medium), #020202 color.darkBasePrimary`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (145 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the surface painted at capture: `light` for every marketing page (`<html data-theme="light">`), `dark` for docs pages after the docs theme selector switched them and for the auth.factory.ai sign-in card. Scoped dark sections inside the light pages — the `[data-dark-hero]` heroes, `.invert-color-scheme` panels and the dark footer — are covered by the dark token set. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages stitched from scrolled viewport tiles at 1x (factory.com's section reveals are scroll-driven, so a one-shot fullPage capture paints them blank); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu-company](screenshots/home-light-menu-company.png), [menu-product](screenshots/home-light-menu-product.png) |
| Enterprise | `/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Factory App (product/desktop) | `/product/desktop` | [default](screenshots/product-desktop-light-default.png), [full](screenshots/product-desktop-light-full.png) |
| Droid CLI | `/product/cli` | [default](screenshots/product-cli-light-default.png), [full](screenshots/product-cli-light-full.png) |
| IDE Integrations | `/product/ide` | [default](screenshots/product-ide-light-default.png), [full](screenshots/product-ide-light-full.png) |
| Custom Automations | `/product/automations` | [default](screenshots/product-automations-light-default.png), [full](screenshots/product-automations-light-full.png) |
| Software Factory | `/product/software-factory` | [default](screenshots/product-software-factory-light-default.png), [full](screenshots/product-software-factory-light-full.png) |
| Security Factory | `/product/security-factory` | [default](screenshots/product-security-factory-light-default.png), [full](screenshots/product-security-factory-light-full.png) |
| Connectors | `/product/connectors` | [default](screenshots/product-connectors-light-default.png), [full](screenshots/product-connectors-light-full.png) |
| Cloud Agents | `/product/cloud-agents` | [default](screenshots/product-cloud-agents-light-default.png), [full](screenshots/product-cloud-agents-light-full.png) |
| Droid Computers | `/product/droid-computers` | [default](screenshots/product-droid-computers-light-default.png), [full](screenshots/product-droid-computers-light-full.png) |
| Agent Effectiveness | `/product/agent-effectiveness` | [default](screenshots/product-agent-effectiveness-light-default.png), [full](screenshots/product-agent-effectiveness-light-full.png) |
| Missions | `/product/missions` | [default](screenshots/product-missions-light-default.png), [full](screenshots/product-missions-light-full.png) |
| Model Routing | `/product/router` | [default](screenshots/product-router-light-default.png), [full](screenshots/product-router-light-full.png) |
| Agent Readiness | `/agent-readiness` | [default](screenshots/agent-readiness-light-default.png), [full](screenshots/agent-readiness-light-full.png) |
| Analytics | `/product/analytics` | [default](screenshots/product-analytics-light-default.png), [full](screenshots/product-analytics-light-full.png) |
| News | `/news` | [default](screenshots/news-light-default.png), [full](screenshots/news-light-full.png) |
| Company | `/company` | [default](screenshots/company-light-default.png), [full](screenshots/company-light-full.png) |
| Events | `/events` | [default](screenshots/events-light-default.png), [full](screenshots/events-light-full.png) |
| Contact | `/contact` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Security | `/security` | [default](screenshots/security-light-default.png), [full](screenshots/security-light-full.png) |
| Partners | `/partners` | [default](screenshots/partners-light-default.png), [full](screenshots/partners-light-full.png) |
| Ambassador | `/ambassador` | [default](screenshots/ambassador-light-default.png), [full](screenshots/ambassador-light-full.png) |
| Open source | `/oss` | [default](screenshots/oss-light-default.png), [full](screenshots/oss-light-full.png) |
| Factory for Science | `/science` | [default](screenshots/science-light-default.png), [full](screenshots/science-light-full.png) |
| Privacy policy | `/privacy-policy` | [default](screenshots/privacy-policy-light-default.png), [full](screenshots/privacy-policy-light-full.png) |
| Docs home | `docs.factory.com/docs` | [default](screenshots/docs-home-dark-default.png), [full](screenshots/docs-home-dark-full.png), [default](screenshots/docs-home-light-default.png), [full](screenshots/docs-home-light-full.png) |
| Docs changelog | `docs.factory.com/docs/changelog/release-notes` | [default](screenshots/docs-changelog-dark-default.png), [default](screenshots/docs-changelog-light-default.png), [full](screenshots/docs-changelog-light-full.png) |
| Docs quickstart | `docs.factory.com/docs/factory-app/quickstart` | [default](screenshots/docs-quickstart-dark-default.png), [full](screenshots/docs-quickstart-dark-full.png), [default](screenshots/docs-quickstart-light-default.png), [full](screenshots/docs-quickstart-light-full.png) |
| Sign-in | `app.factory.ai → auth.factory.ai` | [default](screenshots/signin-dark-default.png), [full](screenshots/signin-dark-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Contact, phone | `/contact` | [default](screenshots/mobile-contact-light-default.png), [full](screenshots/mobile-contact-light-full.png) |
| Docs home, phone | `docs.factory.com/docs` | [default](screenshots/mobile-docs-home-light-default.png), [full](screenshots/mobile-docs-home-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent | marketing pages | a Cookiebot banner appears on some loads; hidden (display:none), never answered | hidden before every shot and reading |
| Product mega-menu | every page header | hovered the 'Product' header button (aria-expanded) | [home-light-menu-product](screenshots/home-light-menu-product.png), [nav-panel](#mega-menu-panel), [nav-menu-item](#mega-menu-item) |
| Company mega-menu | every page header | the same hover on 'Company' | [home-light-menu-company](screenshots/home-light-menu-company.png) |
| Mobile nav overlay | home page, phone width | the 'Open menu' button's own toggle | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-drawer](#mobile-nav-overlay) |
| Docs theme selector | docs pages | clicked the 'Switch to Dark theme' segment — a local UI toggle | [docs-home-dark-default](screenshots/docs-home-dark-default.png), [docs-home-dark-full](screenshots/docs-home-dark-full.png) |
| Contact fields | /contact | typed into then cleared — nothing sent | [field-firstname](#first-name-field), [field-email](#email-field), [field-msg](#message-textarea) |
| Sign-in e-mail field | auth.factory.ai | typed into then cleared — nothing sent | [signin-field](#email-field-sign-in) |
| Signed-in product | a Factory account | the Droid console and every post-login surface needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 23 components were given a real keyboard focus. 21 draw an outline ring: `tier-tab` (1px solid #101010 `color.darkBaseSecondary`, offset 2px), `plan-cta` (1px solid #101010 `color.darkBaseSecondary`, offset 4px), `faq-item` (1px solid #101010 `color.darkBaseSecondary`, offset 2px), `docs-theme-btn` (1px solid #101010 `color.darkBaseSecondary`, offset 2px), `docs-nav-link` (1px solid #101010 `color.darkBaseSecondary`, offset 2px), `docs-cta` (1px solid #101010 `color.darkBaseSecondary`, offset 4px), `signin-submit` (2px solid #b5ada7, offset 2px), `signin-google` (2px solid #b5ada7, offset 2px), `signin-signup` (2px solid #6255ae, offset 2px), `m-cta` (1px solid #101010 `color.darkBaseSecondary`, offset 4px), `m-menu-btn` (1px solid #101010 `color.darkBaseSecondary`, offset 2px), `m-hero-cta` (1px solid #101010 `color.darkBaseSecondary`, offset 4px), `nav-menu-btn` (1px solid #101010 `color.darkBaseSecondary`, offset 2px), `nav-link` (1px solid #101010 `color.darkBaseSecondary`, offset 2px), `nav-signin` (1px solid #101010 `color.darkBaseSecondary`, offset 2px), `nav-cta` (1px solid #101010 `color.darkBaseSecondary`, offset 4px), `nav-cta2` (1px solid #101010 `color.darkBaseSecondary`, offset 4px), `hero-cta` (1px solid #101010 `color.darkBaseSecondary`, offset 4px), `hero-cta2` (1px solid #101010 `color.darkBaseSecondary`, offset 4px), `copy-btn` (1px solid #101010 `color.darkBaseSecondary`, offset 2px), `footer-link` (1px solid #fafafa `color.lightBaseSecondary`, offset 2px). 2 change only their border: `field-select`, `send-btn`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | docs-card, docs-cta, docs-nav-link, docs-nav-link-dk, hero-cta, hero-cta2, m-cta, m-hero-cta and more |
| 0.15s | `ease` | border-color, color | send-btn |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | copy-btn, docs-theme-btn, faq-item, footer-link, nav-link, nav-menu-btn, plan-card, tier-tab |
| 0.2s | `ease` | border-color | field-email, field-firstname, field-msg, field-select |
| 0.22s | `ease-out` | opacity | nav-panel |
| 0.25s | `cubic-bezier(0.4, 0, 0.2, 1)` | opacity | nav-menu-item |
| 0.42s | `cubic-bezier(0.22, 1, 0.36, 1)` | transform | nav-panel |
| 0.7s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | ent-h2 |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Mega-menu panel](#mega-menu-panel) | 1440 x 363 | - | - | transparent | none | 0 |
| [Plan card](#plan-card) | 416 x 408.81 | 1px solid #b8b3b0 `color.neutral.300` | 4px `radius.md` | #f9f9f9 `color.surface.page` | none | 24px 0px |
| [Enterprise feature card](#enterprise-feature-card) | 500 x 198.19 | - | - | transparent | none | 0 |
| [Docs link card](#docs-link-card) | 200 x 27.25 | L: 1px solid #b8b3b0 `color.neutral.300` | - | transparent | none | 4px 0px 4px 12px |
| [Sign-in panel](#sign-in-panel) | 380 x 248.52 | - | - | transparent | none | 0 |

## Components

### Site chrome

The fixed header on every marketing page: the Factory mark, the Product/Enterprise/Company mega-menu triggers, nav links, the locale globe, SIGN IN and the paired CONTACT SALES / DOWNLOAD pills; the mega-menu panel opens under it on hover.

#### Site header
The fixed 72px top bar with the backdrop-blur mask: Factory wordmark, Product/Enterprise/Company mega-menu buttons, Pricing/News/Docs links, locale globe, SIGN IN, CONTACT SALES and DOWNLOAD. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 72; background transparent; text Geist 12/12 400 (`font.size.xs`, `font.weight.normal`), #020202 `color.darkBasePrimary`; layers a::after.text-pretty.ds-label-2 0pxx1px rgb(2, 2, 2); a::after.text-pretty.ds-label-2 0pxx1px rgb(2, 2, 2); a::after.text-pretty.ds-label-2 0pxx1px rgb(2, 2, 2); a::after.text-pretty.ds-label-2 0pxx1px rgb(2, 2, 2); a::after.text-pretty.ds-label-2 0pxx1px rgb(2, 2, 2); a.group.relative 113.9x25.0 rgb(249, 249, 249) T:1px solid rgb(164, 157, 154) / R:1px solid rgb(164, 157, 154) / B:1px solid rgb(1.

Child layers that carry the look: a::after 0pxx1px background #020202 `color.darkBasePrimary`; a::after 0pxx1px background #020202 `color.darkBasePrimary`; a::after 0pxx1px background #020202 `color.darkBasePrimary`.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Factory mark-and-wordmark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 128 x 19; background transparent; text Geist 16/24 400 (`font.size.base`, `font.lineHeight.base`, `font.weight.normal`), #020202 `color.darkBasePrimary`.

![Logo default](components/crops/mkt-logo-default.png)

#### Mega-menu trigger
The "Product" header button — opens the mega-menu panel on hover (aria-expanded). The opened state was measured after a real pointer hover. Read as `nav-menu-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 61 x 60; padding 24px 0px; background transparent; text Geist 12/12 400 (`font.size.xs`, `font.weight.normal`), #020202 `color.darkBasePrimary`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, #020202 `color.darkBasePrimary` |
| focus-visible | radius 2px `radius.xs`; outline 1px solid #101010 `color.darkBaseSecondary`, offset 2px; layers button.text-light-base-primary.hover:text-light-base-primary 61.0x60.0 1px solid rgb(16, 16, 16) offset 2px 2px |

![Mega-menu trigger default](components/crops/nav-menu-btn-default.png) ![Mega-menu trigger hover](components/crops/nav-menu-btn-hover.png) ![Mega-menu trigger focus-visible](components/crops/nav-menu-btn-focus-visible.png) ![Mega-menu trigger pressed](components/crops/nav-menu-btn-pressed.png) ![Mega-menu trigger opened](components/crops/nav-menu-btn-opened.png)

#### Mega-menu panel
The mega-menu panel opened under the header by hovering "Product"; its links were never followed. Read as `nav-panel` on the home page.

**Values (default).** size 1440 x 363; background transparent; text Geist Mono 12/12 400 (`font.size.xs`, `font.weight.normal`), #5c5855 `color.neutral.600`; transition transform 0.42s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.22s ease-out; layers div.border-base-800.bg-surface-raised 570.0x363.2 rgb(255, 255, 255) T:1px solid rgb(184, 179, 176) / R:1px solid rgb(184, 179, 176) / B:1px solid rgb(184, 179, 176) / L:1px solid rgb(184, 179, 176) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px.

Child layers that carry the look: div 570x363.2 background #ffffff `color.white` border 1px solid #b8b3b0 `color.neutral.300` radius 6px `radius.default` shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px; div 149x329.2 border 1px solid #b8b3b0 `color.neutral.300`; div 186x329.2 border 1px solid #b8b3b0 `color.neutral.300`.

![Mega-menu panel default](components/crops/nav-panel-default.png)

#### Mega-menu item
A link inside the opened mega-menu panel; measured, never followed. Read as `nav-menu-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 124 x 32.8; padding 8px 12px; radius 4px `radius.md`; background transparent; text Geist 14/16.8 400 (`font.size.sm`, `font.weight.normal`), #020202 `color.darkBasePrimary`; transition opacity 0.25s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #ebebeb `color.surface.sunken` |

![Mega-menu item default](components/crops/nav-menu-item-default.png) ![Mega-menu item hover](components/crops/nav-menu-item-hover.png)

#### Nav link
A header nav link (Pricing); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 41 x 12; background transparent; text Geist 12/12 400 (`font.size.xs`, `font.weight.normal`), #020202 `color.darkBasePrimary`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); layers ::after rgb(2, 2, 2) 0px none 1; a::after.text-pretty.ds-label-2 0pxx1px rgb(2, 2, 2) |
| hover | layers ::after rgb(2, 2, 2) 0px none 1; a::after.text-pretty.ds-label-2 41pxx1px rgb(2, 2, 2) |
| focus-visible | radius 2px `radius.xs`; outline 1px solid #101010 `color.darkBaseSecondary`, offset 2px; layers ::after rgb(2, 2, 2) 0px none 1; a.text-pretty.ds-label-2 41.0x12.0 1px solid rgb(16, 16, 16) offset 2px 2px; a::after.text-pretty.ds-label-2 0pxx1px rgb(2, 2, 2) |
| pressed | layers ::after rgb(2, 2, 2) 0px none 1; a::after.text-pretty.ds-label-2 41pxx1px rgb(2, 2, 2) |

Child layers that carry the look: a::after 0pxx1px background #020202 `color.darkBasePrimary`.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Sign in link
The "SIGN IN" header link to app.factory.ai; measured, never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 55.33 x 12; padding 0px 4px; background transparent; text Geist Mono 12/12 400 (`font.size.xs`, `font.weight.normal`), #020202 `color.darkBasePrimary`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | radius 2px `radius.xs`; outline 1px solid #101010 `color.darkBaseSecondary`, offset 2px; layers a.text-base-300.hover:text-foreground 55.3x12.0 1px solid rgb(16, 16, 16) offset 2px 2px |

![Sign in link default](components/crops/nav-signin-default.png) ![Sign in link hover](components/crops/nav-signin-hover.png) ![Sign in link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign in link pressed](components/crops/nav-signin-pressed.png)

#### Header primary CTA
The dark "DOWNLOAD" pill in the header; links to /product/desktop, measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 80.09 x 25; padding 0px 12px; border 1px solid transparent; radius 3px `radius.sm`; background #101010 `color.darkBaseSecondary`; text Geist Mono 12/12 400 (`font.size.xs`, `font.weight.normal`), #f9f9f9 `color.surface.page`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #8a8380 `color.neutral.500`; background #f9f9f9 `color.surface.page`; text Geist Mono 12/12 400 (`font.size.xs`, `font.weight.normal`), #101010 `color.darkBaseSecondary` |
| focus-visible | border 1px solid #8a8380 `color.neutral.500`; background #f9f9f9 `color.surface.page`; outline 1px solid #101010 `color.darkBaseSecondary`, offset 4px; text Geist Mono 12/12 400 (`font.size.xs`, `font.weight.normal`), #101010 `color.darkBaseSecondary` |
| pressed | border 1px solid #8a8380 `color.neutral.500`; background #f9f9f9 `color.surface.page`; text Geist Mono 12/12 400 (`font.size.xs`, `font.weight.normal`), #101010 `color.darkBaseSecondary` |

![Header primary CTA default](components/crops/nav-cta-default.png) ![Header primary CTA hover](components/crops/nav-cta-hover.png) ![Header primary CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Header primary CTA pressed](components/crops/nav-cta-pressed.png)

#### Header secondary CTA
The bordered "CONTACT SALES" pill in the header; links to /contact, measured never followed. Read as `nav-cta2` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 113.89 x 25; padding 0px 12px; border 1px solid #a49d9a `color.neutral.400`; radius 3px `radius.sm`; background #f9f9f9 `color.surface.page`; text Geist Mono 12/12 400 (`font.size.xs`, `font.weight.normal`), #020202 `color.darkBasePrimary`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #101010 `color.darkBaseSecondary`; text Geist Mono 12/12 400 (`font.size.xs`, `font.weight.normal`), #f9f9f9 `color.surface.page` |
| focus-visible | background #101010 `color.darkBaseSecondary`; outline 1px solid #101010 `color.darkBaseSecondary`, offset 4px; text Geist Mono 12/12 400 (`font.size.xs`, `font.weight.normal`), #f9f9f9 `color.surface.page` |
| pressed | background #101010 `color.darkBaseSecondary`; text Geist Mono 12/12 400 (`font.size.xs`, `font.weight.normal`), #f9f9f9 `color.surface.page` |

![Header secondary CTA default](components/crops/nav-cta2-default.png) ![Header secondary CTA hover](components/crops/nav-cta2-hover.png) ![Header secondary CTA focus-visible](components/crops/nav-cta2-focus-visible.png) ![Header secondary CTA pressed](components/crops/nav-cta2-pressed.png)

### Home

The light hero on factory.com: the uppercase Geist masthead 'AI CODING AGENTS FOR THE ENTERPRISE', the paired DOWNLOAD / BOOK DEMO pills, the install-command copy box and the section headings down the page.

#### Hero mark
The Factory asterisk mark above the masthead. Read as `hero-mark` on the home page.

**Values (default).** size 87.5 x 84.88; background transparent; text Geist 16/24 400 (`font.size.base`, `font.lineHeight.base`, `font.weight.normal`), #020202 `color.darkBasePrimary`; icon 87.5 x 84.88, #020202 `color.darkBasePrimary`.

![Hero mark default](components/crops/hero-mark-default.png)

#### Hero headline
"AI CODING AGENTS FOR THE ENTERPRISE" — the uppercase Geist masthead. Read as `hero-h1` on the home page.

**Values (default).** size 593.69 x 120.97; background transparent; text Geist 60.48/60.48 500 (`font.size.measured.masthead`, `font.weight.medium`), #020202 `color.darkBasePrimary`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero subline
"Model agnostic. Deployed anywhere." — the mono tagline under the masthead. Read as `hero-sub` on the home page.

**Values (default).** size 374 x 20.55; background transparent; text Geist Mono 18.68/20.55 400 (`font.size.measured.body`, `font.weight.normal`), #8a8380 `color.neutral.500`.

![Hero subline default](components/crops/hero-sub-default.png)

#### Hero CTA
The dark "DOWNLOAD" pill in the hero; measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 109.77 x 31; padding 0px 14px; border 1px solid transparent; radius 3px `radius.sm`; background #101010 `color.darkBaseSecondary`; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #f9f9f9 `color.surface.page`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 10 x 10, #f9f9f9 `color.surface.page` |
| hover | border 1px solid #8a8380 `color.neutral.500`; background #f9f9f9 `color.surface.page`; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #101010 `color.darkBaseSecondary`; icon 10 x 10, #101010 `color.darkBaseSecondary` |
| focus-visible | border 1px solid #8a8380 `color.neutral.500`; background #f9f9f9 `color.surface.page`; outline 1px solid #101010 `color.darkBaseSecondary`, offset 4px; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #101010 `color.darkBaseSecondary`; icon 10 x 10, #101010 `color.darkBaseSecondary` |
| pressed | border 1px solid #8a8380 `color.neutral.500`; background #f9f9f9 `color.surface.page`; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #101010 `color.darkBaseSecondary`; icon 10 x 10, #101010 `color.darkBaseSecondary` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero secondary CTA
The bordered "BOOK DEMO" pill beside it; measured never followed. Read as `hero-cta2` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 123.48 x 31; padding 0px 14px; border 1px solid #a49d9a `color.neutral.400`; radius 3px `radius.sm`; background #f9f9f9 `color.surface.page`; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #020202 `color.darkBasePrimary`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #020202 `color.darkBasePrimary` |
| hover | background #101010 `color.darkBaseSecondary`; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #f9f9f9 `color.surface.page`; icon 16 x 16, #f9f9f9 `color.surface.page` |
| focus-visible | background #101010 `color.darkBaseSecondary`; outline 1px solid #101010 `color.darkBaseSecondary`, offset 4px; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #f9f9f9 `color.surface.page`; icon 16 x 16, #f9f9f9 `color.surface.page` |
| pressed | background #101010 `color.darkBaseSecondary`; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #f9f9f9 `color.surface.page`; icon 16 x 16, #f9f9f9 `color.surface.page` |

![Hero secondary CTA default](components/crops/hero-cta2-default.png) ![Hero secondary CTA hover](components/crops/hero-cta2-hover.png) ![Hero secondary CTA focus-visible](components/crops/hero-cta2-focus-visible.png) ![Hero secondary CTA pressed](components/crops/hero-cta2-pressed.png)

#### Install command
The mono `curl -fsSL https://app.factory.ai/cli | sh` copy box under the CTAs. Read as `install-cmd` on the home page.

**Values (default).** size 420 x 34.5; padding 8px; background #ebebeb `color.surface.sunken`; text Geist Mono 12/16.5 400 (`font.size.xs`, `font.lineHeight.snug`, `font.weight.normal`), #5c5855 `color.neutral.600`; icon 16 x 16, #4d4947 `color.neutral.700`.

![Install command default](components/crops/install-cmd-default.png)

#### Copy button
The "Copy code" control beside the install command; measured, never clicked. Read as `copy-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; padding 8px; background #ebebeb `color.surface.sunken`; text Geist 16/24 400 (`font.size.base`, `font.lineHeight.base`, `font.weight.normal`), #2e2c2b `color.neutral.900`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #4d4947 `color.neutral.700` |
| hover | background oklab(0.701012 0.00662428 0.00657374 / 0.2); icon 16 x 16, #2e2c2b `color.neutral.900` |
| focus-visible | radius 2px `radius.xs`; outline 1px solid #101010 `color.darkBaseSecondary`, offset 2px |
| pressed | background oklab(0.701012 0.00662428 0.00657374 / 0.2); icon 16 x 16, #2e2c2b `color.neutral.900` |

![Copy button default](components/crops/copy-btn-default.png) ![Copy button hover](components/crops/copy-btn-hover.png) ![Copy button focus-visible](components/crops/copy-btn-focus-visible.png) ![Copy button pressed](components/crops/copy-btn-pressed.png)

#### Section heading
A marketing section heading further down the home page. Read as `section-h2` on the home page.

**Values (default).** size 778.63 x 49.27; background transparent; text Geist 44/49.28 400 (`font.size.measured.docsH1`, `font.weight.normal`), #1d0f07.

![Section heading default](components/crops/section-h2-default.png)

### Scoped dark surfaces

The scoped dark sections inside the light pages — the [data-dark-hero] heroes on /enterprise and the /product pages, .invert-color-scheme panels and the dark site footer; the only dark surfaces the marketing site paints.

#### Dark scoped section
A [data-container-variant="inverted"] panel painting the dark token layer inside the light page — /enterprise's "Built for large enterprises" section. Read as `dark-hero` on the enterprise page.

**Values (default).** size 1280 x 677.56; padding 48px 32px; radius 10px `radius.2xl`; background #1f1d1c `color.neutral.1000`; image linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)), url(…); text Geist 12/12 400 (`font.size.xs`, `font.weight.normal`), #eeeeee `color.lightBasePrimary`; icon 24 x 24, #a49d9a `color.neutral.400`.

![Dark scoped section default](components/crops/dark-hero-default.png)

#### Dark section headline
The inverted section's heading, light ink on the near-black field. Read as `dark-h1` on the enterprise page.

**Values (default).** size 311.45 x 70.41; background transparent; text Geist 32/35.2 400 (`font.weight.normal`), #eeeeee `color.lightBasePrimary`.

![Dark section headline default](components/crops/dark-h1-default.png)

#### Dark section eyebrow
The small uppercase eyebrow label inside the inverted section. Read as `dark-eyebrow` on the enterprise page.

**Values (default).** size 102.41 x 12; background transparent; text Geist 12/12 400 (`font.size.xs`, `font.weight.normal`), #fafafa `color.lightBaseSecondary`.

![Dark section eyebrow default](components/crops/dark-eyebrow-default.png)

#### Dark feature label
A feature row label inside the inverted section ("SSO + SAML") — the section carries no CTA. Read as `dark-cta` on the enterprise page.

**Values (default).** size 203.55 x 16.8; background transparent; text Geist 14/16.8 400 (`font.size.sm`, `font.weight.normal`), #eeeeee `color.lightBasePrimary`.

![Dark feature label default](components/crops/dark-cta-default.png)

### Pricing

The /pricing page: the masthead, the plan-tier switcher, plan cards and the FAQ accordion.

#### Pricing headline
The "Pricing Plans" masthead. Read as `price-h1` on the pricing page.

**Values (default).** size 1296 x 39.59; background transparent; text Geist 36/39.6 400 (`font.size.4xl`, `font.weight.normal`), #020202 `color.darkBasePrimary`.

![Pricing headline default](components/crops/price-h1-default.png)

#### Plan-tier tab
A plan-tier switcher button (PRO/PLUS/MAX, role=radio). PRO is the page's own default, so another tier was selected first and the resting states read PRO unselected; the selected state was measured after clicking PRO — a local UI toggle. Read as `tier-tab` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 116 x 22; padding 0px 12px; radius 2px `radius.xs`; background transparent; text Geist Mono 16/24 400 (`font.size.base`, `font.lineHeight.base`, `font.weight.normal`), #4d4947 `color.neutral.700`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #d6d3d2 `color.neutral.100` |
| focus-visible | outline 1px solid #101010 `color.darkBaseSecondary`, offset 2px; layers button.flex.h-full 116.0x22.0 1px solid rgb(16, 16, 16) offset 2px 2px |
| pressed | background rgba(214, 211, 210, 0.455) |
| selected | background rgba(16, 16, 16, 0.996); text Geist Mono 16/24 400 (`font.size.base`, `font.lineHeight.base`, `font.weight.normal`), #f9f9f9 `color.surface.page` |

![Plan-tier tab default](components/crops/tier-tab-default.png) ![Plan-tier tab hover](components/crops/tier-tab-hover.png) ![Plan-tier tab focus-visible](components/crops/tier-tab-focus-visible.png) ![Plan-tier tab pressed](components/crops/tier-tab-pressed.png) ![Plan-tier tab selected](components/crops/tier-tab-selected.png)

#### Plan card
A pricing plan card (name, price, feature list). Read as `plan-card` on the pricing page.

**Values (default).** size 416 x 408.81; padding 24px 0px; border 1px solid #b8b3b0 `color.neutral.300`; radius 4px `radius.md`; background #f9f9f9 `color.surface.page`; text Geist 24/24 400 (`font.size.2xl`, `font.weight.normal`), #4d4947 `color.neutral.700`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #020202 `color.darkBasePrimary`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan CTA
A plan card's action; measured never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 113.89 x 25; padding 0px 12px; border 1px solid #a49d9a `color.neutral.400`; radius 3px `radius.sm`; background #f9f9f9 `color.surface.page`; text Geist Mono 12/12 400 (`font.size.xs`, `font.weight.normal`), #020202 `color.darkBasePrimary`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #101010 `color.darkBaseSecondary`; text Geist Mono 12/12 400 (`font.size.xs`, `font.weight.normal`), #f9f9f9 `color.surface.page` |
| focus-visible | background #101010 `color.darkBaseSecondary`; outline 1px solid #101010 `color.darkBaseSecondary`, offset 4px; text Geist Mono 12/12 400 (`font.size.xs`, `font.weight.normal`), #f9f9f9 `color.surface.page` |
| pressed | background #101010 `color.darkBaseSecondary`; text Geist Mono 12/12 400 (`font.size.xs`, `font.weight.normal`), #f9f9f9 `color.surface.page` |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### FAQ accordion item
A question row in the pricing FAQ accordion; the opened state was measured after clicking the question toggle, and the revealed answer region is measured beside the button (the opened crop shows the answer). Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 1368 x 67.2; padding 24px 0px; background transparent; text Geist Mono 16/19.2 400 (`font.size.base`, `font.weight.normal`), #020202 `color.darkBasePrimary`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | radius 2px `radius.xs`; outline 1px solid #101010 `color.darkBaseSecondary`, offset 2px; layers button.group/trigger.text-base-500 1368.0x67.2 1px solid rgb(16, 16, 16) offset 2px 2px |

![FAQ accordion item default](components/crops/faq-item-default.png) ![FAQ accordion item hover](components/crops/faq-item-hover.png) ![FAQ accordion item focus-visible](components/crops/faq-item-focus-visible.png) ![FAQ accordion item pressed](components/crops/faq-item-pressed.png) ![FAQ accordion item opened](components/crops/faq-item-opened.png)

### Contact form

The /contact HubSpot form: text fields, the topic select, the message textarea and the SUBMIT button — measured and typed into then cleared, never submitted.

#### Contact headline
"Bring Autonomy to your Engineering Organization" — the /contact masthead beside the form. Read as `contact-h1` on the contact page.

**Values (default).** size 560 x 92.41; background transparent; text Geist 44/46.2 400 (`font.size.measured.docsH1`, `font.weight.normal`), #020202 `color.darkBasePrimary`.

![Contact headline default](components/crops/contact-h1-default.png)

#### First name field
The HubSpot First Name text input; focused and typed into then cleared — never submitted. Read as `field-firstname` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 287 x 36; padding 8px 16px; border 1px solid #a49d9a `color.neutral.400`; radius 3px `radius.sm`; background transparent; text Geist 12/18 400 (`font.size.xs`, `font.lineHeight.normal`, `font.weight.normal`), #020202 `color.darkBasePrimary`; transition border-color 0.2s ease; placeholder #b8b3b0 `color.neutral.300` |
| focused, filled | border 1px solid #ef6f2e `color.accent.100` |

![First name field default](components/crops/field-firstname-default.png) ![First name field focused](components/crops/field-firstname-focused.png) ![First name field filled](components/crops/field-firstname-filled.png)

#### Email field
The Work Email input; focused and typed into then cleared — never submitted. Read as `field-email` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 287 x 36; padding 8px 16px; border 1px solid #a49d9a `color.neutral.400`; radius 3px `radius.sm`; background transparent; text Geist 12/18 400 (`font.size.xs`, `font.lineHeight.normal`, `font.weight.normal`), #020202 `color.darkBasePrimary`; transition border-color 0.2s ease; placeholder #b8b3b0 `color.neutral.300` |
| focused | border 1px solid #ef6f2e `color.accent.100` |
| filled | padding 8px 40px 8px 16px; border 1px solid #ef6f2e `color.accent.100` |

![Email field default](components/crops/field-email-default.png) ![Email field focused](components/crops/field-email-focused.png) ![Email field filled](components/crops/field-email-filled.png)

#### Topic select
The "Select one..." dropdown field (a HubSpot select rendered as a read-only input); the opened state was measured after clicking it — a local UI toggle, no option chosen — and the revealed options list is measured beside the field (the opened crop shows the list). Read as `field-select` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 606 x 36; padding 8px 36px 8px 16px; border 1px solid #a49d9a `color.neutral.400`; radius 3px `radius.sm`; background transparent; text Geist 12/18 400 (`font.size.xs`, `font.lineHeight.normal`, `font.weight.normal`), #101010 `color.darkBaseSecondary`; transition border-color 0.2s ease; placeholder #b8b3b0 `color.neutral.300` |
| hover, focus-visible, pressed, opened | border 1px solid #ef6f2e `color.accent.100` |

![Topic select default](components/crops/field-select-default.png) ![Topic select hover](components/crops/field-select-hover.png) ![Topic select focus-visible](components/crops/field-select-focus-visible.png) ![Topic select pressed](components/crops/field-select-pressed.png) ![Topic select opened](components/crops/field-select-opened.png)

#### Message textarea
The "how can we help" textarea; focused and typed into then cleared — never submitted. Read as `field-msg` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 606 x 72; padding 8px 16px; border 1px solid #a49d9a `color.neutral.400`; radius 3px `radius.sm`; background transparent; text Geist 12/18 400 (`font.size.xs`, `font.lineHeight.normal`, `font.weight.normal`), #020202 `color.darkBasePrimary`; transition border-color 0.2s ease; placeholder #b8b3b0 `color.neutral.300` |
| focused, filled | border 1px solid #ef6f2e `color.accent.100` |

![Message textarea default](components/crops/field-msg-default.png) ![Message textarea focused](components/crops/field-msg-focused.png) ![Message textarea filled](components/crops/field-msg-filled.png)

#### Submit button
The form's SUBMIT button; its states were measured but the button was never clicked — nothing was submitted. Read as `send-btn` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 100.33 x 31; padding 0px 38px 0px 14px; border 1px solid transparent; radius 3px `radius.sm`; background transparent; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #f9f9f9 `color.surface.page`; transition color 0.15s ease, border-color 0.15s ease |
| focus-visible | border 1px solid #8a8380 `color.neutral.500`; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #101010 `color.darkBaseSecondary` |
| pressed | border 1px solid #ffffff `color.white`; background #000000 `color.black`; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #ffffff `color.white`; transform translate(0px, 1px) |

![Submit button default](components/crops/send-btn-default.png) ![Submit button hover](components/crops/send-btn-hover.png) ![Submit button focus-visible](components/crops/send-btn-focus-visible.png) ![Submit button pressed](components/crops/send-btn-pressed.png)

### Docs (docs.factory.com)

docs.factory.com — the docs app: top bar, sidebar nav, article body and code blocks, plus the three-way theme selector that flips the whole page to dark.

#### Docs header
The docs top bar: wordmark, Documentation/API Reference/Changelog tabs, GitHub + Discord icons, SIGN IN, DOWNLOAD, the three-way theme selector. Read as `docs-header` on the docs page.

**Values (default).** size 1440 x 73; border B: 1px solid #b8b3b0 `color.neutral.300`; background #f9f9f9 `color.surface.page`; text Geist 12/12 400 (`font.size.xs`, `font.weight.normal`), #020202 `color.darkBasePrimary`.

![Docs header default](components/crops/docs-header-default.png)

#### Theme selector button
One segment of the docs light/dark/system theme selector; a local UI toggle. Read as `docs-theme-btn` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 24; radius 3px `radius.sm`; background transparent; text Geist 16/24 400 (`font.size.base`, `font.lineHeight.base`, `font.weight.normal`), #020202 `color.darkBasePrimary`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 15 x 14, #020202 `color.darkBasePrimary` |
| focus-visible | outline 1px solid #101010 `color.darkBaseSecondary`, offset 2px; layers button.theme-selector-button.relative 24.0x24.0 1px solid rgb(16, 16, 16) offset 2px 3px |

![Theme selector button default](components/crops/docs-theme-btn-default.png) ![Theme selector button hover](components/crops/docs-theme-btn-hover.png) ![Theme selector button focus-visible](components/crops/docs-theme-btn-focus-visible.png) ![Theme selector button pressed](components/crops/docs-theme-btn-pressed.png)

#### Docs sidebar
The left navigation column of the docs. Read as `docs-sidebar` on the docs page.

**Values (default).** size 311 x 72; background transparent; text Geist 12/12 400 (`font.size.xs`, `font.weight.normal`), #020202 `color.darkBasePrimary`; layers a.flex.h-[72px] 111.0x72.0 B:2px solid rgb(239, 111, 46); a.flex.h-[72px] 105.0x72.0 B:2px solid rgba(0, 0, 0, 0); a.flex.h-[72px] 87.0x72.0 B:2px solid rgba(0, 0, 0, 0).

Child layers that carry the look: a 111x72 border 2px solid #ef6f2e `color.accent.100`; a 105x72 border 2px solid transparent; a 87x72 border 2px solid transparent.

![Docs sidebar default](components/crops/docs-sidebar-default.png)

#### Docs nav link
A sidebar navigation link; measured, never followed. Read as `docs-nav-link` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 203 x 32; padding 6px 8px; radius 4px `radius.md`; background transparent; text Geist 14/20 400 (`font.size.sm`, `font.lineHeight.sm`, `font.weight.normal`), #4d4947 `color.neutral.700`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.86889 0.00281054 0.00229794 / 0.6); text Geist 14/20 400 (`font.size.sm`, `font.lineHeight.sm`, `font.weight.normal`), #020202 `color.darkBasePrimary` |
| focus-visible | outline 1px solid #101010 `color.darkBaseSecondary`, offset 2px; layers a.relative.flex 203.0x32.0 1px solid rgb(16, 16, 16) offset 2px 4px |
| pressed | background oklab(0.86889 0.00281054 0.00229794 / 0.6); text Geist 14/20 400 (`font.size.sm`, `font.lineHeight.sm`, `font.weight.normal`), #020202 `color.darkBasePrimary` |

![Docs nav link default](components/crops/docs-nav-link-default.png) ![Docs nav link hover](components/crops/docs-nav-link-hover.png) ![Docs nav link focus-visible](components/crops/docs-nav-link-focus-visible.png) ![Docs nav link pressed](components/crops/docs-nav-link-pressed.png)

#### Docs headline
"Welcome to Factory" — the docs landing masthead. Read as `docs-h1` on the docs page.

**Values (default).** size 824 x 46.2; background transparent; text Geist 44/46.2 400 (`font.size.measured.docsH1`, `font.weight.normal`), #020202 `color.darkBasePrimary`.

![Docs headline default](components/crops/docs-h1-default.png)

#### Docs CTA
The "CREATE AN ACCOUNT" action; measured, never followed. Read as `docs-cta` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 185.25 x 31; padding 0px 14px; border 1px solid #a49d9a `color.neutral.400`; radius 3px `radius.sm`; background #f9f9f9 `color.surface.page`; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #020202 `color.darkBasePrimary`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #020202 `color.darkBasePrimary` |
| hover | background #101010 `color.darkBaseSecondary`; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #f9f9f9 `color.surface.page`; icon 16 x 16, #f9f9f9 `color.surface.page` |
| focus-visible | background #101010 `color.darkBaseSecondary`; outline 1px solid #101010 `color.darkBaseSecondary`, offset 4px; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #f9f9f9 `color.surface.page`; icon 16 x 16, #f9f9f9 `color.surface.page` |
| pressed | background #101010 `color.darkBaseSecondary`; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #f9f9f9 `color.surface.page`; icon 16 x 16, #f9f9f9 `color.surface.page` |

![Docs CTA default](components/crops/docs-cta-default.png) ![Docs CTA hover](components/crops/docs-cta-hover.png) ![Docs CTA focus-visible](components/crops/docs-cta-focus-visible.png) ![Docs CTA pressed](components/crops/docs-cta-pressed.png)

#### Code block
A docs code block (rehype-pretty-code / shiki themed). Read as `docs-code` on the docs page.

**Values (default).** size 824 x 515; background transparent; text Geist 11/16.5 400 (`font.lineHeight.normal`, `font.weight.normal`), #7a6f68; icon 14 x 14, #3d3a39 `color.neutral.800`; layers div.relative.w-full 824.0x515.0 rgb(243, 241, 238) T:1px solid rgb(220, 214, 208) / R:1px solid rgb(220, 214, 208) / B:1px solid rgb(220, 214, 208) / L:1px solid rgb(220, 214, 208) 20px; div.absolute.inset-0 822.0x513.0 rgb(251, 250, 248); div.flex.h-9 822.0x36.0 rgb(236, 235, 232) B:1px solid rgb(220, 214, 208); span.block.h-3 12.0x12.0 rgb(255, 95, 87) 3.35544e+07px; span.block.h-3 12.0x12.0 rgb.

Child layers that carry the look: div 824x515 background #f3f1ee border 1px solid #dcd6d0 radius 20px; div 822x513 background #fbfaf8; div 822x36 background #ecebe8 border 1px solid #dcd6d0.

![Code block default](components/crops/docs-code-default.png)

#### Docs link card
A docs path card (QUICKSTART GUIDE / "Ship Code Faster"); measured, never followed. Read as `docs-card` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 200 x 27.25; padding 4px 0px 4px 12px; border L: 1px solid #b8b3b0 `color.neutral.300`; background transparent; text Geist 14/19.25 400 (`font.size.sm`, `font.lineHeight.snug`, `font.weight.normal`), #4d4947 `color.neutral.700`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers a.line-clamp-2.border-l 200.0x27.3 L:1px solid rgb(184, 179, 176) |
| hover | text Geist 14/19.25 400 (`font.size.sm`, `font.lineHeight.snug`, `font.weight.normal`), #020202 `color.darkBasePrimary` |

Child layers that carry the look: a 200x27.3 border 1px solid #b8b3b0 `color.neutral.300`.

![Docs link card default](components/crops/docs-card-default.png) ![Docs link card hover](components/crops/docs-card-hover.png)

#### Docs headline (dark)
The docs masthead re-measured after the theme selector switched the page to dark. Read as `docs-h1-dk` on the docs page.

**Values (dark).** size 824 x 46.2; background transparent; text Geist 44/46.2 400 (`font.size.measured.docsH1`, `font.weight.normal`), #eeeeee `color.lightBasePrimary`.

![Docs headline (dark) dark](components/crops/docs-h1-dk-dark.png)

#### Docs sidebar (dark)
The sidebar re-measured in dark. Read as `docs-sidebar-dk` on the docs page.

**Values (dark).** size 311 x 72; background transparent; text Geist 12/12 400 (`font.size.xs`, `font.weight.normal`), #eeeeee `color.lightBasePrimary`; layers a.flex.h-[72px] 111.0x72.0 B:2px solid rgb(239, 111, 46); a.flex.h-[72px] 105.0x72.0 B:2px solid rgba(0, 0, 0, 0); a.flex.h-[72px] 87.0x72.0 B:2px solid rgba(0, 0, 0, 0).

Child layers that carry the look: a 111x72 border 2px solid #ef6f2e `color.accent.100`; a 105x72 border 2px solid transparent; a 87x72 border 2px solid transparent.

![Docs sidebar (dark) dark](components/crops/docs-sidebar-dk-dark.png)

#### Code block (dark)
The code block re-measured in dark (the --shiki-dark palette). Read as `docs-code-dk` on the docs page.

**Values (dark).** size 824 x 515; background transparent; text Geist 11/16.5 400 (`font.lineHeight.normal`, `font.weight.normal`), #807670; icon 14 x 14, #b8b3b0 `color.neutral.300`; layers div.relative.w-full 824.0x515.0 rgb(6, 6, 6) T:1px solid rgb(30, 28, 27) / R:1px solid rgb(30, 28, 27) / B:1px solid rgb(30, 28, 27) / L:1px solid rgb(30, 28, 27) 20px; div.absolute.inset-0 822.0x513.0 rgb(13, 12, 11); div.flex.h-9 822.0x36.0 rgb(19, 18, 17) B:1px solid rgb(30, 28, 27); span.block.h-3 12.0x12.0 rgb(255, 95, 87) 3.35544e+07px; span.block.h-3 12.0x12.0 rgb(254, 188, 46) 3.35544e+07p.

Child layers that carry the look: div 824x515 background #060606 border 1px solid #1e1c1b radius 20px; div 822x513 background #0d0c0b; div 822x36 background #131211 border 1px solid #1e1c1b.

![Code block (dark) dark](components/crops/docs-code-dk-dark.png)

#### Docs nav link (dark)
A sidebar link re-measured in dark; measured, never followed. Read as `docs-nav-link-dk` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| dark | size 203 x 32; padding 6px 8px; radius 4px `radius.md`; background transparent; text Geist 14/20 400 (`font.size.sm`, `font.lineHeight.sm`, `font.weight.normal`), #a49d9a `color.neutral.400`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.232587 0.00241723 0.00273159 / 0.0195021); text Geist 14/20 400 (`font.size.sm`, `font.lineHeight.sm`, `font.weight.normal`), #a6a09d |

![Docs nav link (dark) dark](components/crops/docs-nav-link-dk-dark.png) ![Docs nav link (dark) hover](components/crops/docs-nav-link-dk-hover.png)

### Sign-in card (auth.factory.ai)

app.factory.ai redirects to auth.factory.ai — a separate auth app: the dark sign-in card with the e-mail field, 'Continue with email' and 'Continue with Google'. Measured as a form, never submitted.

#### Sign-in panel
The dark auth.factory.ai sign-in card: "Sign in", email field, Continue-with-email and Google actions. Read as `signin-panel` on the sign-in page.

**Values (default).** size 380 x 248.52; background transparent; text Geist 13/18 500 (`font.weight.medium`), #b5ada7; icon 15 x 15, #f5f2ef `component.signin.field-ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1; div.rt-TextFieldRoot.rt-r-size-3 380.0x36.0 rgb(12, 11, 10) rgb(70, 63, 60) 0px 0px 0px 1px inset 2px; button.rt-reset.rt-BaseButton 380.0x36.0 rgb(253, 252, 251) T:1px solid rgb(253, 252, 251) / R:1px solid rgb(253, 252, 251) / B:1px solid rgb(253, 252, 251) / L:1px solid rgb(253, 252, 251) 2px; div::before.rt-Text.rt-r-si.

Child layers that carry the look: div 380x36 background #0c0b0a radius 2px `radius.xs` shadow #463f3c 0px 0px 0px 1px inset; button 380x36 background #fdfcfb `component.signin.submit-fill` border 1px solid #fdfcfb `component.signin.submit-fill` radius 2px `radius.xs`; div::before 169.469pxx1px background #26211f.

![Sign-in panel default](components/crops/signin-panel-default.png)

#### Email field (sign-in)
The e-mail input on the sign-in card; focused and typed into then cleared — never submitted. Read as `signin-field` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 378 x 34; padding 0px 10px; background transparent; text Geist 14/21 400 (`font.size.sm`, `font.lineHeight.normal`, `font.weight.normal`), #f5f2ef `component.signin.field-ink`; placeholder #807973 |

![Email field (sign-in) default](components/crops/signin-field-default.png) ![Email field (sign-in) focused](components/crops/signin-field-focused.png) ![Email field (sign-in) filled](components/crops/signin-field-filled.png)

#### Continue with email
The email submit button; its states were measured but the button was never clicked — nothing was submitted. Read as `signin-submit` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 380 x 36; padding 0px 16px; border 1px solid #fdfcfb `component.signin.submit-fill`; radius 2px `radius.xs`; background #fdfcfb `component.signin.submit-fill`; text Geist 14/24 500 (`font.size.sm`, `font.weight.medium`), #17120f `component.signin.submit-ink` |
| hover | background #e4dfdb |
| focus-visible | outline 2px solid #b5ada7, offset 2px |
| pressed | background #e4dfdb |

![Continue with email default](components/crops/signin-submit-default.png) ![Continue with email hover](components/crops/signin-submit-hover.png) ![Continue with email focus-visible](components/crops/signin-submit-focus-visible.png) ![Continue with email pressed](components/crops/signin-submit-pressed.png)

#### Continue with Google
The Google OAuth action; measured, never followed. Read as `signin-google` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 380 x 36; padding 0px 8px; border 1px solid #6b615c; radius 2px `radius.xs`; background transparent; text Geist 16/24 500 (`font.size.base`, `font.lineHeight.base`, `font.weight.medium`), #f5f2ef `component.signin.field-ink`; icon 15 x 15, #f5f2ef `component.signin.field-ink` |
| hover | background #1d1a18 |
| focus-visible | outline 2px solid #b5ada7, offset 2px |
| pressed | background #1d1a18 |

![Continue with Google default](components/crops/signin-google-default.png) ![Continue with Google hover](components/crops/signin-google-hover.png) ![Continue with Google focus-visible](components/crops/signin-google-focus-visible.png) ![Continue with Google pressed](components/crops/signin-google-pressed.png)

#### Sign up link
The "Sign up" link under the card; measured, never followed. Read as `signin-signup` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 48 x 18; background transparent; text Geist 14/20 400 (`font.size.sm`, `font.lineHeight.sm`, `font.weight.normal`), #f5f2ef `component.signin.field-ink` |
| focus-visible | outline 2px solid #6255ae, offset 2px; layers a.rt-Text.BrandedLink 48.0x18.0 2px solid rgb(98, 85, 174) offset 2px |

![Sign up link default](components/crops/signin-signup-default.png) ![Sign up link hover](components/crops/signin-signup-hover.png) ![Sign up link focus-visible](components/crops/signin-signup-focus-visible.png) ![Sign up link pressed](components/crops/signin-signup-pressed.png)

### Mobile (390 wide)

The phone surface at 390 wide: the header, the 'Open menu' button and full-viewport nav overlay, the hero and CTAs.

#### Mobile top bar
The phone header: the mark, the locale globe and the "Open menu" button — there is no header CTA pill at 390 wide. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 390 x 72; background transparent; text Geist 16/19.2 400 (`font.size.base`, `font.weight.normal`), #4d4947 `color.neutral.700`; layers a::after.text-pretty.ds-label-2 0pxx1px rgb(2, 2, 2); a::after.text-pretty.ds-label-2 0pxx1px rgb(2, 2, 2); a::after.text-pretty.ds-label-2 0pxx1px rgb(2, 2, 2); a::after.text-pretty.ds-label-2 0pxx1px rgb(2, 2, 2); a::after.text-pretty.ds-label-2 0pxx1px rgb(2, 2, 2); a.group.relative 0.0x0.0 rgb(249, 249, 249) T:1px solid rgb(164, 157, 154) / R:1px solid rgb(164, 157, 154) / B:1px solid rgb(164,.

Child layers that carry the look: a::after 0pxx1px background #020202 `color.darkBasePrimary`; a::after 0pxx1px background #020202 `color.darkBasePrimary`; a::after 0pxx1px background #020202 `color.darkBasePrimary`.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile drawer CTA
The "DOWNLOAD" row inside the opened nav overlay at 390 wide; measured never followed. Read as `m-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 358 x 31; padding 0px 14px; border 1px solid transparent; radius 3px `radius.sm`; background #101010 `color.darkBaseSecondary`; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #f9f9f9 `color.surface.page`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible, pressed | border 1px solid #8a8380 `color.neutral.500`; background #f9f9f9 `color.surface.page`; outline 1px solid #101010 `color.darkBaseSecondary`, offset 4px; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #101010 `color.darkBaseSecondary` |

![Mobile drawer CTA default](components/crops/m-cta-default.png) ![Mobile drawer CTA hover](components/crops/m-cta-hover.png) ![Mobile drawer CTA focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile drawer CTA pressed](components/crops/m-cta-pressed.png)

#### Mobile menu button
The "Open menu" button that opens the phone nav overlay — a local UI toggle; the opened state was measured after clicking it. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 32 x 32; padding 4px; background transparent; text Geist 16/24 400 (`font.size.base`, `font.lineHeight.base`, `font.weight.normal`), oklch(0.551 0.027 264.364); icon 24 x 24, oklch(0.551 0.027 264.364) |
| focus-visible | radius 2px `radius.xs`; outline 1px solid #101010 `color.darkBaseSecondary`, offset 2px; layers button.relative.-m-1 32.0x32.0 1px solid rgb(16, 16, 16) offset 2px 2px |

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png) ![Mobile menu button opened](components/crops/m-menu-btn-opened.png)

#### Mobile nav overlay
The nav overlay opened by the menu button; its links were never followed. Read as `m-drawer` on the home page at 390 wide.

**Values (default).** size 390 x 844; padding 80px 0px 0px 0px; background #f9f9f9 `color.surface.page`; text Geist 16/19.2 400 (`font.size.base`, `font.weight.normal`), #4d4947 `color.neutral.700`; icon 16 x 16, #020202 `color.darkBasePrimary`.

![Mobile nav overlay default](components/crops/m-drawer-default.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 318.22 x 64; background transparent; text Geist 32/32 500 (`font.weight.medium`), #020202 `color.darkBasePrimary`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The hero "GET STARTED" pill at 390 wide; measured never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 114.92 x 31; padding 0px 14px; border 1px solid transparent; radius 3px `radius.sm`; background #101010 `color.darkBaseSecondary`; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #f9f9f9 `color.surface.page`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | border 1px solid #8a8380 `color.neutral.500`; background #f9f9f9 `color.surface.page`; outline 1px solid #101010 `color.darkBaseSecondary`, offset 4px; text Geist Mono 14/14 400 (`font.size.sm`, `font.weight.normal`), #101010 `color.darkBaseSecondary` |

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

### Footer

The dark page footer: sitemap columns (Resources/Company/Legal), social links and the mark.

#### Footer
The dark page footer: sitemap columns (Resources/Company/Legal), the mark. Read as `footer` on the home page.

**Values (default).** size 1392 x 430; radius 12px `radius.3xl`; background #101010 `color.darkBaseSecondary`; text Geist 14/14 400 (`font.size.sm`, `font.weight.normal`), #eeeeee `color.lightBasePrimary`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link on the dark footer; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 35 x 14; background transparent; text Geist 14/14 400 (`font.size.sm`, `font.weight.normal`), #8a8380 `color.neutral.500`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); layers ::after rgb(138, 131, 128) 0px none 1; a::after.text-pretty.ds-label-1 0pxx1px rgb(138, 131, 128) |
| hover | text Geist 14/14 400 (`font.size.sm`, `font.weight.normal`), oklch(0.705 0.213 47.604); layers ::after oklab(0.702349 0.13958 0.15286) 0px none 1; a::after.text-pretty.ds-label-1 35pxx1px oklab(0.702349 0.13958 0.15286) |
| focus-visible | radius 2px `radius.xs`; outline 1px solid #fafafa `color.lightBaseSecondary`, offset 2px; layers ::after rgb(138, 131, 128) 0px none 1; a.text-pretty.ds-label-1 35.0x14.0 1px solid rgb(250, 250, 250) offset 2px 2px; a::after.text-pretty.ds-label-1 0pxx1px rgb(138, 131, 128) |
| pressed | text Geist 14/14 400 (`font.size.sm`, `font.weight.normal`), oklch(0.705 0.213 47.604); layers ::after oklab(0.698228 0.133308 0.145957) 0px none 1; a::after.text-pretty.ds-label-1 35pxx1px oklab(0.698228 0.133308 0.145957) |

Child layers that carry the look: a::after 0pxx1px background #8a8380 `color.neutral.500`.

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Enterprise / product pages

The /enterprise and /product/* marketing pages: mastheads, scoped dark heroes and feature cards.

#### Section heading (enterprise)
An /enterprise section heading. Read as `ent-h2` on the enterprise page.

**Values (default).** size 149.78 x 144; background transparent; text Geist 144/144 400 (`font.weight.normal`), #5c5855 `color.neutral.600`; transition all 0.7s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.15.

![Section heading (enterprise) default](components/crops/ent-h2-default.png)

#### Enterprise feature card
An enterprise capability card on the light field. Read as `ent-card` on the enterprise page.

**Values (default).** size 500 x 198.19; background transparent; text Geist 36/39.6 400 (`font.size.4xl`, `font.weight.normal`), #ebebeb `color.surface.sunken`; icon 40 x 40, #ebebeb `color.surface.sunken`; layers a.group.relative 154.4x31.0 rgb(249, 249, 249) T:1px solid rgb(164, 157, 154) / R:1px solid rgb(164, 157, 154) / B:1px solid rgb(164, 157, 154) / L:1px solid rgb(164, 157, 154) 3px; div.group-hover:running.group-focus-visible:running 152.4x29.0.

Child layers that carry the look: a 154.4x31 background #f9f9f9 `color.surface.page` border 1px solid #a49d9a `color.neutral.400` radius 3px `radius.sm`; div 152.4x29 image repeating-linear-gradient(45deg, transparent 0px, transparent 2px, #4d4947 `color.neutral..

![Enterprise feature card default](components/crops/ent-card-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Factory asterisk mark, the mono product glyphs in the mega-menu, connector and social logos) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Factory's product is the Droid platform: every post-login surface — the Factory app console, droid sessions, missions and settings — needs an account and was never reached. app.factory.ai redirects to auth.factory.ai, whose sign-in card is the only app surface a signed-out visitor sees, and it was measured as a form, never submitted. The product screenshots and video frames on the marketing pages are product mocks, not the product.

### Pages

- **The account.** Every post-login surface was never reached; the sign-in card was measured as a form and never submitted; 'Continue with Google' and 'Sign up' were never followed.
- **Forms.** The /contact HubSpot form was measured at rest and typed into then cleared — SUBMIT was never pressed; what a submitted inquiry returns is unverified.
- **factory.ai vs factory.com.** The product is catalogued as factory.ai — the identity used by app.factory.ai and the `curl -fsSL https://app.factory.ai/cli | sh` install command — while the public marketing site and docs live on factory.com/docs.factory.com. factory.com/changelog and docs.factory.com/changelog answered a Vercel-login 404 shape; the working changelog is docs.factory.com/docs/changelog/release-notes.
- **Articles and events** are covered by the /news and /events indexes; individual article and event pages are the same templates, unmeasured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **Mega-menu items' focus/hover** is partially covered: the panel closes on blur, so a real keyboard focus inside it could not always be held.
- **Scroll-driven reveals.** Sections animate in on scroll; the -full shots stitch scrolled viewport tiles, so a section may sit mid-animation the way a real reader sees it.

### Themes

The marketing site has no user theme toggle and no `prefers-color-scheme` switch: every page ships `<html data-theme="light">`. Dark on factory.com is scoped — the `[data-dark-hero]` heroes, `.invert-color-scheme` panels and the dark footer resolve the dark semantic layer (`:root` declares the dark palette as the default; `data-theme="light"` remaps it). docs.factory.com shares the token layer and ships a real three-way theme selector (Light/Dark/System); the docs dark shots and measurements were taken after switching it to Dark. auth.factory.ai is a third surface: its own dark sign-in card, a different app that does not share this token layer.

### Fonts

- **Geist** and **Geist Mono** (variable, wght 100–900, every heading, control, body and code frame) plus **Geist Pixel Square** (the pixel label face) are the served faces, self-hosted via next/font. The style guide falls back to system sans.

### Screenshots

- The product mocks, photography and video frames in the screenshots are the product's published content; hero video panels can paint as black rectangles under headless capture.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article copy, customer names, pricing figures and testimonial text are the product's content; only frames and components were measured.
