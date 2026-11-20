# Enode components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from enode.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the contact and login forms were never sent; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (46 components, 105 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Enode Sans 15/22 490, #252322`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (105 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode `<html>` painted at capture: `light` for most marketing pages (`data-mode="light" data-ink="alpha"`), `dark` for /platform/overview and /platform/flexibility (whole dark pages, `data-mode="dark"`) and for the signed-out platform login — a light sign-in panel over a dark product showcase. Scoped `[data-mode="dark"]` sections inside the light pages (the showcase panel, the mega-menu) are covered by the dark token set. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu-platform](screenshots/home-light-menu-platform.png), [menu-resources](screenshots/home-light-menu-resources.png) |
| Platform overview | `/platform/overview` | [default](screenshots/platform-overview-dark-default.png), [full](screenshots/platform-overview-dark-full.png) |
| Homes | `/platform/homes` | [default](screenshots/platform-homes-light-default.png), [full](screenshots/platform-homes-light-full.png) |
| Flexibility | `/platform/flexibility` | [default](screenshots/platform-flexibility-dark-default.png), [full](screenshots/platform-flexibility-dark-full.png) |
| Assets | `/platform/assets` | [default](screenshots/platform-assets-light-default.png), [full](screenshots/platform-assets-light-full.png) |
| Enterprise | `/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| Customers | `/customers` | [default](screenshots/customers-light-default.png), [full](screenshots/customers-light-full.png) |
| Customer story (Vattenfall) | `/customers/vattenfall` | [default](screenshots/customers-vattenfall-light-default.png), [full](screenshots/customers-vattenfall-light-full.png) |
| Company | `/company` | [default](screenshots/company-light-default.png), [full](screenshots/company-light-full.png) |
| Careers | `/careers` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| Partnerships | `/partnerships` | [default](screenshots/partnerships-light-default.png), [full](screenshots/partnerships-light-full.png) |
| Newsroom | `/newsroom` | [default](screenshots/newsroom-light-default.png), [full](screenshots/newsroom-light-full.png) |
| Newsroom article | `/newsroom/vattenfall-and-enode-bring-smart-charging-to-ev-owners-in-sweden` | [default](screenshots/newsroom-article-light-default.png), [full](screenshots/newsroom-article-light-full.png) |
| Updates | `/updates` | [default](screenshots/updates-light-default.png), [full](screenshots/updates-light-full.png) |
| Updates article | `/updates/introducing-asset-overview-find-the-right-assets-in-seconds-not-days` | [default](screenshots/updates-article-light-default.png), [full](screenshots/updates-article-light-full.png) |
| Contact | `/contact` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Contact (partnerships) | `/contact/partnerships` | [default](screenshots/contact-partnerships-light-default.png), [full](screenshots/contact-partnerships-light-full.png) |
| Privacy policy | `/privacy-policy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Platform login | `platform.enode.com/login` | [default](screenshots/login-dark-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Platform overview, phone | `/platform/overview` | [default](screenshots/mobile-platform-overview-dark-default.png), [full](screenshots/mobile-platform-overview-dark-full.png) |
| Contact, phone | `/contact` | [default](screenshots/mobile-contact-light-default.png), [full](screenshots/mobile-contact-light-full.png) |
| Updates, phone | `/updates` | [default](screenshots/mobile-updates-light-default.png), [full](screenshots/mobile-updates-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent | every page | the Cookiebot script loads dormant and shows no banner; any consent layer would be hidden, never answered | hidden before every shot and reading |
| Platform mega-menu | every page header | focused the 'Platform' trigger and pressed Enter (pointer clicks do not flip it in headless Chromium) | [home-light-menu-platform](screenshots/home-light-menu-platform.png), [nav-panel](#mega-menu-panel), [nav-menu-item](#mega-menu-item) |
| Resources mega-menu | every page header | the same keyboard activation on 'Resources' | [home-light-menu-resources](screenshots/home-light-menu-resources.png) |
| Mobile nav overlay | home page, phone width | the round menu button's own toggle | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-drawer](#mobile-nav-overlay) |
| Contact fields | /contact | typed into then cleared — nothing sent | [field-firstname](#first-name-field), [field-email](#email-field), [field-inquiry](#message-textarea) |
| Login e-mail field | platform.enode.com/login | typed into then cleared — nothing sent | [login-field](#email-field-login) |
| Signed-in product | an Enode account | every post-login surface (platform dashboard, docs) needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 15 components were given a real keyboard focus. 5 draw an outline ring: `nav-link` (2px solid #b0f87c `color.brand.225`, offset 2px), `nav-signin` (2px solid #b0f87c `color.brand.225`, offset 2px), `footer-link` (2px solid #b0f87c `color.brand.225`, offset 2px), `login-submit` (2px solid #b0f87c `color.brand.225`, offset 2px), `login-sso` (2px solid #b0f87c `color.brand.225`, offset 2px). The other 10 show no measured change: `nav-menu-btn`, `nav-cta`, `hero-cta`, `hero-cta2`, `ent-cta`, `upd-link`, `send-btn`, `m-cta`, `m-menu-btn`, `m-hero-cta`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, backdrop-filter, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | ent-cta, field-email, field-firstname, field-inquiry, field-phone, footer-link, hero-cta, hero-cta2 and more |
| 0.15s | `ease` | background-color, border-color, box-shadow, color | login-field, login-sso, login-submit |
| 0.2s | `cubic-bezier(0, 0, 0.2, 1)` | opacity | mkt-logo |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, opacity, outline-color, stroke, text-decoration-color | ov-lede, upd-card |
| 0.2s | `ease` | background-color | code-frame, visual-frame |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Mega-menu panel](#mega-menu-panel) | 1120 x 290 | - | - | transparent | none | 0 |
| [Stat card](#stat-card) | 396 x 184 | - | 6px | oklch(0.9447 0.003 48.7) | oklch(0.9214 0.0032 48.7) 0px 0px 0px 1px inset | 20px |
| [Article card](#article-card) | 916 x 75.5 | - | - | transparent | none | 24px 0px |
| [Partner quote card](#partner-quote-card) | 356 x 413.89 | - | - | transparent | none | 0 |
| [Visual frame (product mock)](#visual-frame-product-mock) | 304 x 171 | - | 4px | #32302f `color.gray.750` | oklch(1 0 0 / 0.042) 0px 0px 0px 1px inset | 0 |
| [Login panel](#login-panel) | 600 x 900 | R: 1px solid #dcd8d6 `color.gray.175` | - | transparent | none | 64px 72px |

## Components

### Site chrome

The fixed header on every marketing page: wordmark, the Platform and Resources mega-menu triggers, nav pills, Sign in and the dark 'Talk to our team' pill; the mega-menu panel itself is a dark glass [data-mode] surface.

#### Site header
The fixed glass top bar: wordmark, Platform/Resources mega-menu buttons, Enterprise/Updates/Company nav pills, Sign in and the "Talk to our team" pill. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 58; background transparent; text Enode Sans 15/22 490, rgba(37, 35, 34, 0.827); icon 81.83 x 16, #252322 `color.gray.800`; layers div.relative.chrome-glass 1440.0x58.0 oklab(0.978722 -0.0210906 0.0224455 / 0.92) oklab(0.257937 0.00235393 0.00265922 / 0.06) 0px 1px 0px 0px; button::before.inline-flex.items-center 85pxx34px oklch(0.858722 0.06 133.217 / 0.6) 4px; button::before.inline-flex.items-center 100pxx34px oklch(0.858722 0.06 133.217 / 0.6) 4px; a::before.nav-pill.rounded-sm 99pxx34px oklch(0.858722 0.06 133.217 / 0.6) .

Child layers that carry the look: div 1440x58 background oklab(0.978722 -0.0210906 0.0224455 / 0.92) shadow oklab(0.257937 0.00235393 0.00265922 / 0.06) 0px 1px 0px 0px; button::before 85pxx34px background oklch(0.858722 0.06 133.217 / 0.6) radius 4px; button::before 100pxx34px background oklch(0.858722 0.06 133.217 / 0.6) radius 4px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Enode mark-and-wordmark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 81.83 x 16; radius 2px; background transparent; text Enode Sans 18/26.1 470, #252322 `color.gray.800`; transition opacity 0.2s cubic-bezier(0, 0, 0.2, 1); icon 81.83 x 16, #252322 `color.gray.800`.

![Logo default](components/crops/mkt-logo-default.png)

#### Mega-menu trigger
The "Platform" header button — an aria-haspopup="dialog" trigger for the product mega-menu. The opened state was measured after focusing it and pressing Enter. Read as `nav-menu-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85 x 34; padding 6px 12px; radius 4px; background transparent; text Enode Sans 15/22 490, rgba(37, 35, 34, 0.827); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::before oklch(0.858722 0.06 133.217 / 0.6) 0px none 0; button::before.inline-flex.items-center 85pxx34px oklch(0.858722 0.06 133.217 / 0.6) 4px |
| hover | text Enode Sans 15/22 490, #252322 `color.gray.800`; layers ::before oklch(0.858722 0.06 133.217 / 0.6) 0px none 1; button::before.inline-flex.items-center 85pxx34px oklch(0.858722 0.06 133.217 / 0.6) 4px |
| focus-visible | layers ::before oklch(0.858722 0.06 133.217 / 0.6) 0px none 1; button::before.inline-flex.items-center 85pxx34px oklch(0.858722 0.06 133.217 / 0.6) 4px |
| pressed, opened | text Enode Sans 15/22 490, #252322 `color.gray.800`; layers ::before oklch(0.858722 0.06 133.217 / 0.6) 0px none 1; button::before.inline-flex.items-center 85pxx34px oklch(0.858722 0.06 133.217 / 0.6) 4px |

Child layers that carry the look: button::before 85pxx34px background oklch(0.858722 0.06 133.217 / 0.6) radius 4px.

![Mega-menu trigger default](components/crops/nav-menu-btn-default.png) ![Mega-menu trigger hover](components/crops/nav-menu-btn-hover.png) ![Mega-menu trigger focus-visible](components/crops/nav-menu-btn-focus-visible.png) ![Mega-menu trigger pressed](components/crops/nav-menu-btn-pressed.png) ![Mega-menu trigger opened](components/crops/nav-menu-btn-opened.png)

#### Nav link
A marketing header nav pill (Enterprise); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 99 x 34; padding 6px 12px; radius 4px; background transparent; text Enode Sans 15/22 490, rgba(37, 35, 34, 0.827); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::before oklch(0.858722 0.06 133.217 / 0.6) 0px none 0; a::before.nav-pill.rounded-sm 99pxx34px oklch(0.858722 0.06 133.217 / 0.6) 4px |
| hover | text Enode Sans 15/22 490, rgba(37, 35, 34, 0.973); layers ::before oklch(0.858722 0.06 133.217 / 0.6) 0px none 0.852485; a::before.nav-pill.rounded-sm 99pxx34px oklch(0.858722 0.06 133.217 / 0.6) 4px |
| focus-visible | outline 2px solid #b0f87c `color.brand.225`, offset 2px; layers ::before oklch(0.858722 0.06 133.217 / 0.6) 0px none 1; a.nav-pill.rounded-sm 99.0x34.0 2px solid rgb(176, 248, 124) offset 2px 4px; a::before.nav-pill.rounded-sm 99pxx34px oklch(0.858722 0.06 133.217 / 0.6) 4px |
| pressed | text Enode Sans 15/22 490, #252322 `color.gray.800`; layers ::before oklch(0.858722 0.06 133.217 / 0.6) 0px none 1; a::before.nav-pill.rounded-sm 99pxx34px oklch(0.858722 0.06 133.217 / 0.6) 4px |

Child layers that carry the look: a::before 99pxx34px background oklch(0.858722 0.06 133.217 / 0.6) radius 4px.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Sign in link
The "Sign in" nav pill linking to platform.enode.com; measured, never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 72 x 34; padding 6px 12px; radius 4px; background transparent; text Enode Sans 15/22 490, rgba(37, 35, 34, 0.827); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::before oklch(0.858722 0.06 133.217 / 0.6) 0px none 0; a::before.nav-pill.rounded-sm 72pxx34px oklch(0.858722 0.06 133.217 / 0.6) 4px |
| hover | text Enode Sans 15/22 490, #252322 `color.gray.800`; layers ::before oklch(0.858722 0.06 133.217 / 0.6) 0px none 1; a::before.nav-pill.rounded-sm 72pxx34px oklch(0.858722 0.06 133.217 / 0.6) 4px |
| focus-visible | outline 2px solid #b0f87c `color.brand.225`, offset 2px; layers ::before oklch(0.858722 0.06 133.217 / 0.6) 0px none 1; a.nav-pill.rounded-sm 72.0x34.0 2px solid rgb(176, 248, 124) offset 2px 4px; a::before.nav-pill.rounded-sm 72pxx34px oklch(0.858722 0.06 133.217 / 0.6) 4px |
| pressed | text Enode Sans 15/22 490, #252322 `color.gray.800`; layers ::before oklch(0.858722 0.06 133.217 / 0.6) 0px none 1; a::before.nav-pill.rounded-sm 72pxx34px oklch(0.858722 0.06 133.217 / 0.6) 4px |

Child layers that carry the look: a::before 72pxx34px background oklch(0.858722 0.06 133.217 / 0.6) radius 4px.

![Sign in link default](components/crops/nav-signin-default.png) ![Sign in link hover](components/crops/nav-signin-hover.png) ![Sign in link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign in link pressed](components/crops/nav-signin-pressed.png)

#### Header CTA
The dark "Talk to our team" pill in the header; links to /contact, measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 138.2 x 32; padding 0px 12px; radius 3.35544e+07px; background #252322 `color.gray.800`; text Enode Sans 15/15 490, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #b0f87c `color.brand.225`; text Enode Sans 15/15 490, #151413 `color.gray.850` |

![Header CTA default](components/crops/nav-cta-default.png) ![Header CTA hover](components/crops/nav-cta-hover.png) ![Header CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Header CTA pressed](components/crops/nav-cta-pressed.png)

#### Mega-menu panel
The dark glass mega-menu panel opened by its own trigger; its links were never followed. Read as `nav-panel` on the home page.

**Values (default).** size 1120 x 290; background transparent; text Enode Sans 15/22 520, #ffffff `color.white`; transform translate(146px, 0px); icon 16 x 16, #c5c1bf `color.gray.225`; layers div.overflow-hidden.rounded-lg 1120.0x290.0 oklch(1 0 0 / 0.1) 0px 0px 0px 1px 10px; div::before.overflow-hidden.rounded-lg 1120pxx290px oklch(0.231995 0.00257147 67.5681 / 0.72) 10px; a::before.nav-pill.group 271pxx266px rgba(255, 255, 255, 0.08) 6px; div.relative.aspect-[3/2] 255.0x170.0 rgb(21, 20, 19) 4px; div.relative.aspect-[3/2] 255.0x170.0 rgb(21, 20, 19) 4px; div.relative.aspect-[3/2] 255.

Child layers that carry the look: div 1120x290 radius 10px shadow oklch(1 0 0 / 0.1) 0px 0px 0px 1px; div::before 1120pxx290px background oklch(0.231995 0.00257147 67.5681 / 0.72) radius 10px; a::before 271pxx266px background rgba(255, 255, 255, 0.08) radius 6px.

![Mega-menu panel default](components/crops/nav-panel-default.png)

#### Mega-menu item
A link inside the opened mega-menu panel; measured, never followed. Read as `nav-menu-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 271 x 266; padding 8px; radius 6px; background transparent; text Enode Sans 15/22 520, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::before rgba(255, 255, 255, 0.08) 0px none 1; a::before.nav-pill.group 271pxx266px rgba(255, 255, 255, 0.08) 6px; div.relative.aspect-[3/2] 255.0x170.0 rgb(21, 20, 19) 4px |

Child layers that carry the look: a::before 271pxx266px background rgba(255, 255, 255, 0.08) radius 6px; div 255x170 background #151413 `color.gray.850` radius 4px.

![Mega-menu item default](components/crops/nav-menu-item-default.png) ![Mega-menu item hover](components/crops/nav-menu-item-hover.png)

### Home

The light hero on enode.com: the 68px Enode Sans masthead 'Orchestrating energy for the next grid', the paired Talk-to-our-team / Explore-our-platform pills, stat cards and section headings.

#### Hero headline
"Orchestrating energy for the next grid" — the text-masthead display heading. Read as `hero-h1` on the home page.

**Values (default).** size 1024 x 142.78; background transparent; text Enode Sans 68/71.4 475, #252322 `color.gray.800`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero CTA
The dark "Talk to our team" pill in the hero; measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 138.2 x 32; padding 0px 12px; radius 3.35544e+07px; background #252322 `color.gray.800`; text Enode Sans 15/15 490, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #b0f87c `color.brand.225`; text Enode Sans 15/15 490, #151413 `color.gray.850` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero secondary CTA
The outlined "Explore our platform" pill beside it; measured never followed. Read as `hero-cta2` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 169.5 x 32; padding 0px 12px; radius 3.35544e+07px; background transparent; shadow rgba(21, 20, 19, 0.165) 0px 0px 0px 1px inset; text Enode Sans 15/15 490, #252322 `color.gray.800`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers a.inline-flex.h-8 169.5x32.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(21, 20, 19, 0.165) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 3.35544e+07px |
| hover | shadow rgba(21, 20, 19, 0.263) 0px 0px 0px 1px inset; layers a.inline-flex.h-8 169.5x32.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(21, 20, 19, 0.263) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 3.35544e+07px |

![Hero secondary CTA default](components/crops/hero-cta2-default.png) ![Hero secondary CTA hover](components/crops/hero-cta2-hover.png) ![Hero secondary CTA focus-visible](components/crops/hero-cta2-focus-visible.png) ![Hero secondary CTA pressed](components/crops/hero-cta2-pressed.png)

#### Stat card
A metric card ("960+ Energy device models supported" / "1.6M+ Connected households" / "4,799+ MW"). Read as `stat-card` on the home page.

**Values (default).** size 396 x 184; padding 20px; radius 6px; background oklch(0.9447 0.003 48.7); shadow oklch(0.9214 0.0032 48.7) 0px 0px 0px 1px inset; text Enode Sans 36/41.4 470, #252322 `color.gray.800`.

![Stat card default](components/crops/stat-card-default.png)

#### Section heading
A marketing section heading (text-h2) further down the home page. Read as `section-h2` on the home page.

**Values (default).** size 604 x 72; background transparent; text Enode Sans 30/36 510, #252322 `color.gray.800`.

![Section heading default](components/crops/section-h2-default.png)

### Platform pages

The /platform/* pages: mastheads, the sticky product-area nav, .visual-frame product and code demo tiles. /platform/overview paints a whole dark page (data-mode="dark" on <html>); /platform/homes stays light.

#### Page headline
"Connect. Coordinate. Shape." — the platform overview masthead. Read as `ov-h1` on the platform overview page.

**Values (default).** size 1024 x 71.39; background transparent; text Enode Sans 68/71.4 475, #efedeb `color.gray.125`.

![Page headline default](components/crops/ov-h1-default.png)

#### Platform card copy
The 15px muted feature-card description ("One API for 1,000+ device models…"). Read as `ov-lede` on the platform overview page.

**Values (default).** size 288 x 90; background transparent; text Enode Sans 15/22.5 470, #b0adab `color.gray.300`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1).

![Platform card copy default](components/crops/ov-lede-default.png)

#### Section heading (platform)
A platform page section heading. Read as `section-h2-ov` on the platform overview page.

**Values (default).** size 576 x 42.47; background transparent; text Enode Sans 36/42.48 500, #efedeb `color.gray.125`.

![Section heading (platform) default](components/crops/section-h2-ov-default.png)

#### Platform section nav item
One item in the sticky product-area nav (Asset connectivity / Home energy coordination / Residential flexibility / Intelligence layer). Read as `feature-row` on the platform overview page.

**Values (default).** size 188 x 26.09; background transparent; text Enode Sans 15/21.75 450, #b0adab `color.gray.300`.

![Platform section nav item default](components/crops/feature-row-default.png)

#### Visual frame (product mock)
A .visual-frame demo tile holding a platform product mock (the browser-framed "platform.enode.com — Client / Users / Assets" screenshot). Read as `visual-frame` on the platform overview page.

**Values (default).** size 304 x 171; radius 4px; background #32302f `color.gray.750`; shadow oklch(1 0 0 / 0.042) 0px 0px 0px 1px inset; text Enode Sans 13/19.5 470, #b0adab `color.gray.300`; transition background-color 0.2s ease; icon 5.12 x 5.12, #7e7977.

![Visual frame (product mock) default](components/crops/visual-frame-default.png)

#### Visual frame (code)
A .visual-frame demo tile holding a code/terminal mock ("import …", "kubectl logs"). Read as `code-frame` on the platform overview page.

**Values (default).** size 304 x 171; radius 4px; background #32302f `color.gray.750`; shadow oklch(1 0 0 / 0.042) 0px 0px 0px 1px inset; text Enode Sans 13/19.5 470, #b0adab `color.gray.300`; transition background-color 0.2s ease; icon 5.12 x 5.12, #7e7977.

![Visual frame (code) default](components/crops/code-frame-default.png)

### Updates

The /updates index: masthead, article rows and the social pill.

#### Updates headline
"Product news, insights, and stories…" — the /updates masthead. Read as `upd-h1` on the updates page.

**Values (default).** size 1024 x 214.17; background transparent; text Enode Sans 68/71.4 475, #252322 `color.gray.800`.

![Updates headline default](components/crops/upd-h1-default.png)

#### Article card
An article card on the updates index (image, tag, title, date); measured, never followed. Read as `upd-card` on the updates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 916 x 75.5; padding 24px 0px; background transparent; text Enode Sans 20/27.5 500, #252322 `color.gray.800`; transition opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, #6e6a68 `color.gray.475` |
| hover | icon 12 x 12, #4c4948 `color.gray.650` |

![Article card default](components/crops/upd-card-default.png) ![Article card hover](components/crops/upd-card-hover.png)

#### Follow link
The "Follow Enode on LinkedIn" social pill; measured, never followed. Read as `upd-link` on the updates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 205.81 x 32; padding 0px 12px; radius 3.35544e+07px; background transparent; shadow #dcd8d6 0px 0px 0px 1px inset; text Enode Sans 15/15 490, #252322 `color.gray.800`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers a.inline-flex.h-8 205.8x32.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(220, 216, 214) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 3.35544e+07px |
| hover | shadow #c5c1bf 0px 0px 0px 1px inset; layers a.inline-flex.h-8 205.8x32.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(197, 193, 191) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 3.35544e+07px |

![Follow link default](components/crops/upd-link-default.png) ![Follow link hover](components/crops/upd-link-hover.png) ![Follow link focus-visible](components/crops/upd-link-focus-visible.png) ![Follow link pressed](components/crops/upd-link-pressed.png)

### Enterprise

The /enterprise page: masthead, CTA and the partner quote card.

#### Enterprise headline
The /enterprise masthead. Read as `ent-h1` on the enterprise page.

**Values (default).** size 722.73 x 142.78; background transparent; text Enode Sans 68/71.4 475, #252322 `color.gray.800`.

![Enterprise headline default](components/crops/ent-h1-default.png)

#### Enterprise CTA
The enterprise contact/demo pill; measured never followed. Read as `ent-cta` on the enterprise page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 138.2 x 32; padding 0px 12px; radius 3.35544e+07px; background #252322 `color.gray.800`; text Enode Sans 15/15 490, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #b0f87c `color.brand.225`; text Enode Sans 15/15 490, #151413 `color.gray.850` |

![Enterprise CTA default](components/crops/ent-cta-default.png) ![Enterprise CTA hover](components/crops/ent-cta-hover.png) ![Enterprise CTA focus-visible](components/crops/ent-cta-focus-visible.png) ![Enterprise CTA pressed](components/crops/ent-cta-pressed.png)

#### Partner quote card
The enterprise partner quote card ("We’re partnering with Easee…"). Read as `quote-card` on the enterprise page.

**Values (default).** size 356 x 413.89; background transparent; text Enode Sans 18/26.1 470, #4c4948 `color.gray.650`; layers div.flex.aspect-[3/2] 356.0x237.3 rgb(21, 20, 19) 4px; span.inline-block.bg-current 195.8x48.0 rgb(255, 255, 255).

Child layers that carry the look: div 356x237.3 background #151413 `color.gray.850` radius 4px; span 195.8x48 background #ffffff `color.white`.

![Partner quote card default](components/crops/quote-card-default.png)

### Contact form

The /contact inquiry form: text fields, the inquiry-type radios, the textarea and the 'Send message' pill — measured and typed into then cleared, never submitted.

#### Contact headline
The /contact masthead over the inquiry form. Read as `contact-h1` on the contact page.

**Values (default).** size 604 x 93; background transparent; text Enode Sans 36/41.4 500, #252322 `color.gray.800`.

![Contact headline default](components/crops/contact-h1-default.png)

#### First name field
The First name text input; focused and typed into then cleared — never submitted. Read as `field-firstname` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 294 x 48.09; padding 10px 16px; border 1px solid #dcd8d6 `color.gray.175`; radius 6px; background #ffffff `color.white`; text Enode Sans 18/26.1 470, #252322 `color.gray.800`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #252322 `color.gray.800` |
| focused, filled | border 1px solid #252322 `color.gray.800` |

![First name field default](components/crops/field-firstname-default.png) ![First name field focused](components/crops/field-firstname-focused.png) ![First name field filled](components/crops/field-firstname-filled.png)

#### Email field
The work-email input; focused and typed into then cleared — never submitted. Read as `field-email` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 294 x 48.09; padding 10px 16px; border 1px solid #dcd8d6 `color.gray.175`; radius 6px; background #ffffff `color.white`; text Enode Sans 18/26.1 470, #252322 `color.gray.800`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #252322 `color.gray.800` |
| focused, filled | border 1px solid #252322 `color.gray.800` |

![Email field default](components/crops/field-email-default.png) ![Email field focused](components/crops/field-email-focused.png) ![Email field filled](components/crops/field-email-filled.png)

#### Phone field
The optional phone input; focused and typed into then cleared — never submitted. Read as `field-phone` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 294 x 48.09; padding 10px 16px; border 1px solid #dcd8d6 `color.gray.175`; radius 6px; background #ffffff `color.white`; text Enode Sans 18/26.1 470, #252322 `color.gray.800`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #252322 `color.gray.800` |
| focused, filled | border 1px solid #252322 `color.gray.800` |

![Phone field default](components/crops/field-phone-default.png) ![Phone field focused](components/crops/field-phone-focused.png) ![Phone field filled](components/crops/field-phone-filled.png)

#### Inquiry radio
One option of the inquiry-type radio group (sr-only inputs behind styled labels); measured, never toggled. Read as `radio-inquiry` on the contact page.

**Values (default).** size 298 x 41.59; padding 10px 16px; border 1px solid #dcd8d6 `color.gray.175`; radius 3.35544e+07px; background transparent; text Enode Sans 14/19.6 450, #4c4948 `color.gray.650`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Inquiry radio default](components/crops/radio-inquiry-default.png)

#### Send message button
The form's dark "Send message" pill; its states were measured but the button was never clicked — nothing was submitted. Read as `send-btn` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 129.91 x 32; padding 0px 12px; radius 3.35544e+07px; background #252322 `color.gray.800`; text Enode Sans 15/15 490, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #b0f87c `color.brand.225`; text Enode Sans 15/15 490, #151413 `color.gray.850` |

![Send message button default](components/crops/send-btn-default.png) ![Send message button hover](components/crops/send-btn-hover.png) ![Send message button focus-visible](components/crops/send-btn-focus-visible.png) ![Send message button pressed](components/crops/send-btn-pressed.png)

#### Message textarea
The inquiry-detail textarea; focused and typed into then cleared — never submitted. Read as `field-inquiry` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 604 x 100.28; padding 10px 16px; border 1px solid #dcd8d6 `color.gray.175`; radius 6px; background #ffffff `color.white`; text Enode Sans 18/26.1 470, #252322 `color.gray.800`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #252322 `color.gray.800` |

![Message textarea default](components/crops/field-inquiry-default.png) ![Message textarea focused](components/crops/field-inquiry-focused.png) ![Message textarea filled](components/crops/field-inquiry-filled.png)

### Platform login (dark)

platform.enode.com/login — a separate app: a light sign-in panel (e-mail field, 'Log in' submit, SAML SSO link, 'Contact us') over a dark product showcase. Measured as a form, never submitted.

#### Login panel
The dark sign-in panel over a dimmed product screenshot: "Sign in to Enode Platform". Read as `login-panel` on the platform login page.

**Values (default).** size 600 x 900; padding 64px 72px; border R: 1px solid #dcd8d6 `color.gray.175`; background transparent; text Enode Sans 30/36 500, #252322 `color.gray.800`; icon 81.83 x 16, #252322 `color.gray.800`; layers div.panel 600.0x900.0 R:1px solid rgb(220, 216, 214); input.input 455.0x41.0 rgb(255, 255, 255) T:1px solid rgb(220, 216, 214) / R:1px solid rgb(220, 216, 214) / B:1px solid rgb(220, 216, 214) / L:1px solid rgb(220, 216, 214) 6px; button.enode-button 455.0x32.0 rgb(37, 35, 34) 999px; p::before.divider 210pxx1px rgb(220, 216, 214); p::after.divider 210pxx1px rgb(220, 216, 214); a.enode-button 455.0.

Child layers that carry the look: div 600x900 border 1px solid #dcd8d6 `color.gray.175`; input 455x41 background #ffffff `color.white` border 1px solid #dcd8d6 `color.gray.175` radius 6px; button 455x32 background #252322 `color.gray.800` radius 999px.

![Login panel default](components/crops/login-panel-default.png)

#### Email field (login)
The e-mail input on the platform login; focused and typed into then cleared — never submitted. Read as `login-field` on the platform login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 455 x 41; padding 10px 16px; border 1px solid #dcd8d6 `color.gray.175`; radius 6px; background #ffffff `color.white`; text Enode Sans 16/normal 450, #252322 `color.gray.800`; transition border-color 0.15s ease; placeholder #252322 `color.gray.800` |
| focused, filled | border 1px solid #252322 `color.gray.800` |

![Email field (login) default](components/crops/login-field-default.png) ![Email field (login) focused](components/crops/login-field-focused.png) ![Email field (login) filled](components/crops/login-field-filled.png)

#### Log in submit
The login submit button; its states were measured but the button was never clicked — nothing was submitted. Read as `login-submit` on the platform login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 455 x 32; padding 1px 12px; radius 999px; background #252322 `color.gray.800`; text Enode Sans 15/15 490, #ffffff `color.white`; transition background-color 0.15s ease, color 0.15s ease, box-shadow 0.15s ease |
| hover | background #b0f87c `color.brand.225`; text Enode Sans 15/15 490, #151413 `color.gray.850` |
| focus-visible | outline 2px solid #b0f87c `color.brand.225`, offset 2px |
| pressed | background #b0f87c `color.brand.225`; text Enode Sans 15/15 490, #151413 `color.gray.850`; opacity 0.9 |

![Log in submit default](components/crops/login-submit-default.png) ![Log in submit hover](components/crops/login-submit-hover.png) ![Log in submit focus-visible](components/crops/login-submit-focus-visible.png) ![Log in submit pressed](components/crops/login-submit-pressed.png)

#### SAML SSO link
The "Continue with SAML SSO" action; measured, never followed. Read as `login-sso` on the platform login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 455 x 32; padding 0px 12px; radius 999px; background transparent; shadow #dcd8d6 0px 0px 0px 1px inset; text Enode Sans 15/15 490, #252322 `color.gray.800`; transition background-color 0.15s ease, color 0.15s ease, box-shadow 0.15s ease; icon 16 x 16, #252322 `color.gray.800`; layers a.enode-button 455.0x32.0 rgb(220, 216, 214) 0px 0px 0px 1px inset 999px |
| hover | shadow #c5c1bf 0px 0px 0px 1px inset; layers a.enode-button 455.0x32.0 rgb(197, 193, 191) 0px 0px 0px 1px inset 999px |
| focus-visible | outline 2px solid #b0f87c `color.brand.225`, offset 2px; layers a.enode-button 455.0x32.0 rgb(220, 216, 214) 0px 0px 0px 1px inset 2px solid rgb(176, 248, 124) offset 2px 999px |
| pressed | shadow #c5c1bf 0px 0px 0px 1px inset; opacity 0.9; layers a.enode-button 455.0x32.0 rgb(197, 193, 191) 0px 0px 0px 1px inset 999px |

![SAML SSO link default](components/crops/login-sso-default.png) ![SAML SSO link hover](components/crops/login-sso-hover.png) ![SAML SSO link focus-visible](components/crops/login-sso-focus-visible.png) ![SAML SSO link pressed](components/crops/login-sso-pressed.png)

### Mobile (390 wide)

The phone surface at 390 wide: the header, round menu button and full-viewport nav overlay, the hero and CTA.

#### Mobile top bar
The phone header: Enode mark, the round menu button and the "Talk to our team" pill. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 390 x 60; background transparent; text Enode Sans 15/15 490, #ffffff `color.white`; icon 81.83 x 16, #252322 `color.gray.800`; layers div.relative.chrome-glass 390.0x60.0 oklab(0.978722 -0.0210906 0.0224455 / 0.92) oklab(0.257937 0.00235393 0.00265922 / 0.06) 0px 1px 0px 0px; button::before.inline-flex.items-center autoxauto oklch(0.858722 0.06 133.217 / 0.6) 4px; button::before.inline-flex.items-center autoxauto oklch(0.858722 0.06 133.217 / 0.6) 4px; a::before.nav-pill.rounded-sm autoxauto oklch(0.858722 0.06 133.217 / 0.6) 4p.

Child layers that carry the look: div 390x60 background oklab(0.978722 -0.0210906 0.0224455 / 0.92) shadow oklab(0.257937 0.00235393 0.00265922 / 0.06) 0px 1px 0px 0px; button::before autoxauto background oklch(0.858722 0.06 133.217 / 0.6) radius 4px; button::before autoxauto background oklch(0.858722 0.06 133.217 / 0.6) radius 4px.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile header CTA
The header "Talk to our team" pill at 390 wide; measured never followed. Read as `m-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 138.2 x 32; padding 0px 12px; radius 3.35544e+07px; background #252322 `color.gray.800`; text Enode Sans 15/15 490, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #b0f87c `color.brand.225`; text Enode Sans 15/15 490, #151413 `color.gray.850` |

![Mobile header CTA default](components/crops/m-cta-default.png) ![Mobile header CTA hover](components/crops/m-cta-hover.png) ![Mobile header CTA focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile header CTA pressed](components/crops/m-cta-pressed.png)

#### Mobile menu button
The icon-only round button that opens the phone nav overlay — a local UI toggle; the opened state was measured after clicking it. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed, opened) | size 36 x 36; radius 3.35544e+07px; background transparent; text Enode Sans 18/26.1 470, #252322 `color.gray.800`; icon 20 x 20, #252322 `color.gray.800` |

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png) ![Mobile menu button opened](components/crops/m-menu-btn-opened.png)

#### Mobile nav overlay
The nav overlay opened by the menu button; its links were never followed. Read as `m-drawer` on the home page at 390 wide.

**Values (default).** size 390 x 844; background transparent; text Enode Sans 15/15 490, #ffffff `color.white`; icon 81.83 x 16, #252322 `color.gray.800`; layers div.shrink-0.border-b 390.0x61.0 B:1px solid rgba(21, 20, 19, 0.165); a.inline-flex.h-8 138.2x32.0 rgb(37, 35, 34) 3.35544e+07px; span.inline-flex.items-center 21.6x20.0 T:1px solid rgba(21, 20, 19, 0.165) / R:1px solid rgba(21, 20, 19, 0.165) / B:1px solid rgba(21, 20, 19, 0.165) / L:1px solid rgba(21, 20, 19, 0.165) 3.35544e+07px.

Child layers that carry the look: div 390x61 border 1px solid rgba(21, 20, 19, 0.165) `color.grayAlpha.175`; a 138.2x32 background #252322 `color.gray.800` radius 3.35544e+07px; span 21.6x20 border 1px solid rgba(21, 20, 19, 0.165) `color.grayAlpha.175` radius 3.35544e+07px.

![Mobile nav overlay default](components/crops/m-drawer-default.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 358 x 72.63; background transparent; text Enode Sans 34.58/36.31 475, #252322 `color.gray.800`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The hero "Talk to our team" pill at 390 wide; measured never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 138.2 x 32; padding 0px 12px; radius 3.35544e+07px; background #252322 `color.gray.800`; text Enode Sans 15/15 490, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #b0f87c `color.brand.225`; text Enode Sans 15/15 490, #151413 `color.gray.850` |

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

### Footer

The page footer: sitemap columns, legal links and social icons.

#### Footer
The page footer: sitemap columns, legal links, social icons. Read as `footer` on the home page.

**Values (default).** size 1425 x 682.75; background transparent; text Enode Sans 15/22.5 490, #252322 `color.gray.800`; icon 18 x 18, #4c4948 `color.gray.650`; layers span.inline-flex.items-center 20.0x20.0 T:1px solid rgb(220, 216, 214) / R:1px solid rgb(220, 216, 214) / B:1px solid rgb(220, 216, 214) / L:1px solid rgb(220, 216, 214) 3.35544e+07px.

Child layers that carry the look: span 20x20 border 1px solid #dcd8d6 `color.gray.175` radius 3.35544e+07px.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 76 x 21.75; background transparent; text Enode Sans 15/21.75 450, rgba(37, 35, 34, 0.827); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Enode Sans 15/21.75 450, #252322 `color.gray.800` |
| focus-visible | outline 2px solid #b0f87c `color.brand.225`, offset 2px; layers a.group.inline-flex 76.0x21.8 2px solid rgb(176, 248, 124) offset 2px |
| pressed | text Enode Sans 15/21.75 450, #252322 `color.gray.800` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Dark showcase sections

The scoped [data-mode="dark"] sections inside the light pages — the hero media/showcase panel with the live energy diagram, and the mega-menu panel; the only dark surfaces the marketing site paints.

#### Dark showcase panel
A scoped [data-mode="dark"] section inside the light page — the hero media/showcase panel painting the dark semantic layer. Read as `dark-showcase` on the home page.

**Values (default).** size 1360 x 765; background #151413 `color.gray.850`; text Enode Sans 15/21.75 490, #b0f87d `color.enodeGreen`; icon 32 x 32, #efedeb `color.gray.125`.

![Dark showcase panel default](components/crops/dark-showcase-default.png)

#### Product demo card
A product-UI demo tile inside the dark showcase (the live energy diagram/charging numbers); a public demo, not the signed-in product. Read as `demo-card` on the home page.

**Values (default).** size 1360 x 765; background transparent; text Enode Sans 15/21.75 490, #b0f87d `color.enodeGreen`; layers span.h-px.shrink-0 72.0x1.0 rgb(161, 157, 155); span.inline-block.size-2 8.0x8.0 rgb(176, 248, 124) 50%; span.h-px.shrink-0 72.0x1.0 rgb(161, 157, 155); span.inline-block.size-2 8.0x8.0 rgb(176, 248, 124) 50%; span.h-px.shrink-0 72.0x1.0 rgb(161, 157, 155); span.inline-block.size-2 8.0x8.0 rgb(176, 248, 124) 50%.

Child layers that carry the look: span 72x1 background #a19d9b `color.gray.350`; span 8x8 background #b0f87c `color.brand.225` radius 50%; span 72x1 background #a19d9b `color.gray.350`.

![Product demo card default](components/crops/demo-card-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Enode mark, the mono product-area glyphs in the mega-menu, social glyphs, the node/diagram marks) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Enode's product is the platform: every post-login surface — the dashboard, asset management, API keys, the docs portal — needs an account and was never reached. platform.enode.com/login is the only app surface a signed-out visitor sees, and it was measured as a form, never submitted. The .visual-frame demo tiles on the marketing pages are product mocks, not the product.

### Pages

- **The account.** Every post-login surface was never reached; the platform login form was measured as a form and never submitted; 'Continue with SAML SSO' was never followed.
- **Forms.** The /contact and /contact/partnerships forms were measured at rest and typed into then cleared — 'Send message' was never pressed; what a submitted inquiry returns is unverified.
- **Careers.** The 'View open positions' link leaves enode.com for the ATS; the positions board was not captured.
- **Newsroom/updates articles and customer stories** are covered by one captured example each (vattenfall customer story, one newsroom launch post, one updates post); the other article routes are the same templates, unmeasured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **Mega-menu items' focus/hover** is partially covered: the panel closes on blur, so a real keyboard focus inside it could not always be held.

### Themes

The marketing site has no user theme toggle and no `prefers-color-scheme` switch: the mode is chosen per page. Most pages paint `data-mode="light" data-ink="alpha"`; /platform/overview and /platform/flexibility paint `data-mode="dark"` on `<html>` itself — whole dark pages whose hero, cards and header glass all resolve the dark semantic layer. The light pages additionally carry scoped `[data-mode="dark"]` sections (the showcase panel, the mega-menu, `.chrome-glass--dark` elements). The dark token set resolves those declarations. The platform login is a third surface: dark-framed with a light sign-in panel, a different app that does not share this token layer.

### Fonts

- **Enode Sans VF** (wght 375–635, every heading, control and body) and **Enode Mono VF** (product demo/code frames) are the served faces, self-hosted from /assets. The style guide falls back to system sans.

### Screenshots

- The product mocks, photography and video frames in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article copy, customer names and the demo metrics are the product's content; only frames and components were measured.
