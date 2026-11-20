# Care.com components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from care.com on 2026-11-12, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, joined, searched, booked or paid for; the login and signup forms were never filled; the ZIP search, provider profiles, plan checkout and the signup-gate dialog's own actions were never followed or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (51 components, 133 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (132 files, named `{component}-{state}.png`; 124 at 2x, 6 halved to 1x over the ~1.2-megapixel crop cap (per-crop sizes in [raw/crop-scales.json](raw/crop-scales.json))). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Child care | `/child-care` | [default](screenshots/child-care-light-default.png), [full](screenshots/child-care-light-full.png) |
| Senior care | `/senior-care` | [default](screenshots/senior-care-light-default.png), [full](screenshots/senior-care-light-full.png) |
| Pet care | `/pet-care` | [default](screenshots/pet-care-light-default.png), [full](screenshots/pet-care-light-full.png) |
| Housekeeping | `/housekeeping` | [default](screenshots/housekeeping-light-default.png), [full](screenshots/housekeeping-light-full.png) |
| Tutoring | `/tutoring` | [default](screenshots/tutoring-light-default.png), [full](screenshots/tutoring-light-full.png) |
| Babysitters listing | `/babysitters` | [default](screenshots/babysitters-light-default.png), [faq](screenshots/babysitters-light-faq.png), [full](screenshots/babysitters-light-full.png) |
| Safety | `/about/safety/` | [default](screenshots/safety-light-default.png), [full](screenshots/safety-light-full.png) |
| Resource centre | `/c/` | [default](screenshots/resources-light-default.png), [full](screenshots/resources-light-full.png) |
| About | `/about/` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Plans and pricing | `/app/vhp/plans-and-pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Log in | `/vis/auth/login` | [default](screenshots/login-light-default.png) |
| Get started | `/app/vhp/get-started` | [default](screenshots/join-light-default.png) |
| Caregiver rates | `/caregiver-rates` | [default](screenshots/rates-light-default.png), [full](screenshots/rates-light-full.png) |
| Terms of use | `/about/terms-of-use` | [default](screenshots/terms-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Child care, phone | `/child-care` | [default](screenshots/mobile-child-care-light-default.png), [full](screenshots/mobile-child-care-light-full.png) |
| Senior care, phone | `/senior-care` | [default](screenshots/mobile-senior-care-light-default.png), [full](screenshots/mobile-senior-care-light-full.png) |
| Pet care, phone | `/pet-care` | [default](screenshots/mobile-pet-care-light-default.png), [full](screenshots/mobile-pet-care-light-full.png) |
| Housekeeping, phone | `/housekeeping` | [default](screenshots/mobile-housekeeping-light-default.png), [full](screenshots/mobile-housekeeping-light-full.png) |
| Tutoring, phone | `/tutoring` | [default](screenshots/mobile-tutoring-light-default.png), [full](screenshots/mobile-tutoring-light-full.png) |
| Babysitters listing, phone | `/babysitters` | [default](screenshots/mobile-babysitters-light-default.png), [full](screenshots/mobile-babysitters-light-full.png) |
| Safety, phone | `/about/safety/` | [default](screenshots/mobile-safety-light-default.png), [full](screenshots/mobile-safety-light-full.png) |
| Pricing, phone | `/app/vhp/plans-and-pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Log in, phone | `/vis/auth/login` | [default](screenshots/mobile-login-light-default.png) |
| Get started, phone | `/app/vhp/get-started` | [default](screenshots/mobile-join-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the header menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item) |
| Find care mega menu | every desktop page | the Find care trigger's own toggle | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#mega-menu), [menu-item](#mega-menu-tab), [menu-link](#menu-link) |
| Cookie consent bar | every page | hidden, never answered (the OneTrust buttons were never clicked) | hidden before every shot and reading |
| Join Care.com signup gate | /babysitters | mounts over the results once they are scrolled to; measured open, then hidden, never answered | [gate-dialog](#signup-gate-dialog), [gate-cta](#gate-cta) |
| FAQ accordion | /babysitters | a question row's own toggle | [babysitters-light-faq](screenshots/babysitters-light-faq.png), [list-faq](#faq-question) |
| Signed-in product | care.com member dashboard, messages, bookings, payments | requires an account; only the public login/join shells were measured, never filled | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 24 components were given a real keyboard focus. 3 draw an outline ring: `read-more` (3px auto #4d9380 `color.brand.green-focus`, offset 0px), `passwordless-link` (5px auto #005fcc, offset -2px), `social-icon` (1px auto #005fcc, offset 1px). 10 draw a focus ring as a shadow instead: `join-cta`, `search-cta`, `service-cta`, `city-button`, `filter-button`, `page-item`, `login-button`, `join-option`, `plan-cta`, `plan-alt`. 7 grow a border on a child layer: `nav-trigger`, `login-link`, `menu-item`, `menu-link`, `provider-card`, `footer-link`, `m-nav-item`. 2 paint a background wash: `cat-faq`, `list-faq`. The other 2 show no measured change: `learn-more`, `pricing-faq`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, margin, min-height | cat-faq, list-faq, pricing-faq |
| 0.15s | `ease-in-out` | border-color, box-shadow | login-email |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | boxShadow, transform | m-menu-open |
| 0.25s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, color | page-item |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | box-shadow | addon-card, join-card, review-card, service-card |
| 0.3s | `ease-in-out` | background-color | header, m-header |
| 0.3s | `ease-out` | -webkit-transform, background, transform | city-button, filter-button, join-cta, join-option, login-button, plan-alt, plan-cta, search-cta and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Category card](#category-card) | 200 x 252 | - | 24px | #ffffff `color.neutral.white` | none | 32px 24px |
| [Service card](#service-card) | 608 x 512 | - | 32px | #ffffff `color.neutral.white` | none | 0 |
| [Testimonial card](#testimonial-card) | 410.66 x 256 | - | 24px | #ffffff `color.neutral.white` | none | 8px 0px |
| [Provider card](#provider-card) | 645.33 x 160 | - | - | transparent | none | 0px 0px 0px 24px |
| [Plan card](#plan-card) | 373 x 341 | - | 32px | #ffffff `color.neutral.white` | none | 24px |
| [Add-on card](#add-on-card) | 624 x 188 | - | 24px | #ffffff `color.neutral.white` | none | 32px |
| [Join card](#join-card) | 391 x 376 | - | 32px | #ffffff `color.neutral.white` | none | 48px 24px |
| [Login card](#login-card) | 311 x 252 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The fixed white header: wordmark, the Find care / Find jobs / List your business / Resources mega-menu triggers, Log in and the lime Join-now pill.

#### Header
The fixed header: wordmark, the Find care / Find jobs / List your business / Resources mega-menu triggers, Log in and the Join-now pill. Read as `header` on the home page.

**Values (default).** size 1440 x 104; padding 24px 32px; background transparent; text Oceanic Grotesk 16/24 400, #ffffff `color.neutral.white`; transition background-color 0.3s ease-in-out; layers a::before.MuiTypography-root.MuiTypography-inherit autoxauto T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px; button::before.MuiButtonBase-root.DesktopDropdownButton--root autoxauto T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px; butto.

Child layers that carry the look: a::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 6px; button::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 6px; button::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 6px.

![Header default](components/crops/header-default.png)

#### Logo
The Care.com wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 230 x 40; background transparent; text Oceanic Grotesk 18/28 400, #377a69 `color.brand.green-link`; layers ::before rgba(0, 0, 0, 0) 2px none 1; a::before.MuiTypography-root.MuiTypography-inherit autoxauto T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px.

Child layers that carry the look: a::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 6px.

![Logo default](components/crops/logo-default.png)

#### Nav trigger
The "Find care" button that opens the mega menu; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 92.83 x 24; background transparent; text Oceanic Grotesk 16/24 400, #ffffff `color.neutral.white`; icon 24 x 24, #ffffff `color.neutral.white`; layers ::before rgba(0, 0, 0, 0) 2px none 1; button::before.MuiButtonBase-root.DesktopDropdownButton--root autoxauto T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px |
| focus-visible | layers ::before rgba(0, 0, 0, 0) 2px none 1; button::before.MuiButtonBase-root.Mui-focusVisible 108.828pxx32px T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px |

Child layers that carry the look: button::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 6px.

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Log-in link
The header Log-in action; measured, never followed. Read as `login-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 43.44 x 24; background transparent; text Oceanic Grotesk 16/24 400, #ffffff `color.neutral.white`; layers ::before rgba(0, 0, 0, 0) 2px none 1; a::before.MuiTypography-root.MuiTypography-body2 autoxauto T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px |
| focus-visible | layers ::before rgba(0, 0, 0, 0) 2px none 1; a::before.MuiTypography-root.MuiTypography-body2 59.4375pxx32px T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px |

Child layers that carry the look: a::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 6px.

![Log-in link default](components/crops/login-link-default.png) ![Log-in link hover](components/crops/login-link-hover.png) ![Log-in link focus-visible](components/crops/login-link-focus-visible.png) ![Log-in link pressed](components/crops/login-link-pressed.png)

#### Join CTA
The green Join-now header action; measured, never followed. Read as `join-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 170 x 40; padding 8px 24px; border 1px solid #d0f5a3 `color.brand.lime`; radius 20px; background #d0f5a3 `color.brand.lime`; text Oceanic Grotesk 16/18 500, #025747 `color.brand.green`; transition background 0.3s ease-out |
| hover | border 1px solid #e4ffb8 `color.brand.lime-hover`; background #e4ffb8 `color.brand.lime-hover` |
| focus-visible | border none; shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px |
| pressed | border 1px solid #8ae718 `color.brand.lime-pressed`; background #8ae718 `color.brand.lime-pressed` |

![Join CTA default](components/crops/join-cta-default.png) ![Join CTA hover](components/crops/join-cta-hover.png) ![Join CTA focus-visible](components/crops/join-cta-focus-visible.png) ![Join CTA pressed](components/crops/join-cta-pressed.png)

#### Mega menu
The Find-care mega menu panel, opened by its own trigger. Read as `nav-dropdown` on the home page.

Kept from an earlier run: the 2026-11-12 recapture did not find this component, so these readings may not match the current page or script.

**Values (default).** size 928 x 360; background transparent; text Oceanic Grotesk 16/20 500, #1e1e1e `color.neutral.ink`; icon 24 x 24, #1e1e1e `color.neutral.ink`; layers div.MuiBox-root.mui-bm0daf 196.0x360.0 rgb(246, 243, 238); button.MuiButtonBase-root.MegaMenu--item 164.0x48.0 rgb(255, 255, 255) 8px; button::before.MuiButtonBase-root.MegaMenu--item autoxauto T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 8px; button::before.MuiButtonBase-root.MegaMenu--item autoxauto T:2px solid rgb(.

Child layers that carry the look: div 196x360 background #f6f3ee; button 164x48 background #ffffff `color.neutral.white` radius 8px; button::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 8px.

![Mega menu default](components/crops/nav-dropdown-default.png)

#### Mega-menu tab
A category tab inside the mega menu (Child care active by default). Read as `menu-item` on the home page.

Kept from an earlier run: the 2026-11-12 recapture did not find this component, so these readings may not match the current page or script.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 164 x 48; padding 0px 10px 0px 16px; radius 8px; background #ffffff `color.neutral.white`; text Oceanic Grotesk 16/20 500, #1e1e1e `color.neutral.ink`; icon 24 x 24, #1e1e1e `color.neutral.ink`; layers ::before rgba(0, 0, 0, 0) 2px none 1 |

![Mega-menu tab default](components/crops/menu-item-default.png) ![Mega-menu tab hover](components/crops/menu-item-hover.png) ![Mega-menu tab focus-visible](components/crops/menu-item-focus-visible.png) ![Mega-menu tab pressed](components/crops/menu-item-pressed.png)

#### Menu link
A link inside the opened mega menu. Read as `menu-link` on the home page.

Kept from an earlier run: the 2026-11-12 recapture did not find this component, so these readings may not match the current page or script.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 250 x 44; padding 10px 0px 10px 16px; background transparent; text Oceanic Grotesk 16/24 400, #377a69 `color.brand.green-link`; layers ::before rgba(0, 0, 0, 0) 2px none 1; a::before.MuiTypography-root.MuiTypography-body2 autoxauto T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px |
| focus-visible, pressed | layers ::before rgba(0, 0, 0, 0) 2px none 1; a::before.MuiTypography-root.MuiTypography-body2 250pxx40px T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px |

Child layers that carry the look: a::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 6px.

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link focus-visible](components/crops/menu-link-focus-visible.png) ![Menu link pressed](components/crops/menu-link-pressed.png)

### Home

The full-bleed photo hero with the 64px display headline and the ZIP + Search band, the membership category cards and the testimonials.

#### Hero headline
The hero display headline over the photo ("Connecting families with quality, local caregivers"); the testimonial-name accentHeadline1 h1s are excluded. Read as `hero-title` on the home page.

Kept from an earlier run: the 2026-11-12 recapture did not find this component, so these readings may not match the current page or script.

**Values (default).** size 700 x 144; background transparent; text NaN Druid Sans 64/72 550, #ffffff `color.neutral.white`.

![Hero headline default](components/crops/hero-title-default.png)

#### ZIP field
The hero ZIP-code search input; focused and given a sample ZIP that was deleted again — never searched. Read as `zip-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 270 x 25.88; background transparent; text Oceanic Grotesk 18/24 400, #1e1e1e `color.neutral.ink`; placeholder #707070 `color.neutral.muted` |

![ZIP field default](components/crops/zip-field-default.png) ![ZIP field focused](components/crops/zip-field-focused.png) ![ZIP field filled](components/crops/zip-field-filled.png)

#### Search CTA
The green Search action under the ZIP field; measured, never pressed. Read as `search-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 344 x 56; padding 14px 16px; border 1px solid #d0f5a3 `color.brand.lime`; radius 28px; background #d0f5a3 `color.brand.lime`; text Oceanic Grotesk 20/16 500, #025747 `color.brand.green`; transition background 0.3s ease-out |
| hover | border 1px solid #e4ffb8 `color.brand.lime-hover`; background #e4ffb8 `color.brand.lime-hover` |
| focus-visible | border none; shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px |
| pressed | border 1px solid #8ae718 `color.brand.lime-pressed`; background #8ae718 `color.brand.lime-pressed` |

![Search CTA default](components/crops/search-cta-default.png) ![Search CTA hover](components/crops/search-cta-hover.png) ![Search CTA focus-visible](components/crops/search-cta-focus-visible.png) ![Search CTA pressed](components/crops/search-cta-pressed.png)

#### Category card
A "One membership" category card (Child care, Senior care, Pet care ...); measured, never followed. Read as `category-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 200 x 252; padding 32px 24px; radius 24px; background #ffffff `color.neutral.white`; text Oceanic Grotesk 18/24 500, #1e1e1e `color.neutral.ink`; icon 24 x 24, #1e1e1e `color.neutral.ink`; layers ::before rgba(0, 0, 0, 0) 2px none 1 |
| hover | background #f5f5f5 `color.neutral.grey-hover`; outline 1px solid #707070 `color.neutral.muted`, offset 0px |
| pressed | background #e8e8e8 `color.neutral.grey-pressed`; outline 1px solid #707070 `color.neutral.muted`, offset 0px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Category card default](components/crops/category-card-default.png) ![Category card hover](components/crops/category-card-hover.png) ![Category card pressed](components/crops/category-card-pressed.png)

#### Section heading
A section display heading ("One membership for every season of life"). Read as `section-h2` on the home page.

Kept from an earlier run: the 2026-11-12 recapture did not find this component, so these readings may not match the current page or script.

**Values (default).** size 657.05 x 40; background transparent; text NaN Druid Sans 40/40 550, #1e1e1e `color.neutral.ink`.

![Section heading default](components/crops/section-h2-default.png)

### Category page

A category landing page (/child-care): the display title over photo, the service cards (Nannies / Babysitters / Daycares), member reviews and the FAQ accordion.

#### Category title
The category page display title ("Find child care on your terms"). Read as `cat-h1` on the child care page.

**Values (default).** size 480 x 144; background transparent; text NaN Druid Sans 64/72 550, #ffffff `color.neutral.white`.

![Category title default](components/crops/cat-h1-default.png)

#### Service card
A service-card panel (Nannies / Babysitters / Daycares ...) in the services grid. Read as `service-card` on the child care page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 608 x 512; radius 32px; background #ffffff `color.neutral.white`; text Oceanic Grotesk 24/32 500, #1e1e1e `color.neutral.ink`; transition box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | shadow rgba(0, 0, 0, 0.15) 0px 4px 16px 0px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Service card default](components/crops/service-card-default.png) ![Service card hover](components/crops/service-card-hover.png) ![Service card pressed](components/crops/service-card-pressed.png)

#### Service CTA
A card action ("Find babysitters"); measured, never followed. Read as `service-cta` on the child care page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 144.33 x 40; padding 8px 24px; border 1px solid #025747 `color.brand.green`; radius 20px; background #025747 `color.brand.green`; text Oceanic Grotesk 16/18 500, #e4ffb8 `color.brand.lime-hover`; transition background 0.3s ease-out |
| hover | border 1px solid #377a69 `color.brand.green-link`; background #377a69 `color.brand.green-link` |
| focus-visible | size 142.33 x 40; border none; shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px |
| pressed | border 1px solid #034135; background #034135 |

![Service CTA default](components/crops/service-cta-default.png) ![Service CTA hover](components/crops/service-cta-hover.png) ![Service CTA focus-visible](components/crops/service-cta-focus-visible.png) ![Service CTA pressed](components/crops/service-cta-pressed.png)

#### Testimonial card
A member-quote card ("Trusted by families like yours"). Read as `review-card` on the child care page.

**Values (default).** size 410.66 x 256; padding 8px 0px; radius 24px; background #ffffff `color.neutral.white`; text Oceanic Text Semibold 96/80 450, #025747 `color.brand.green`; transition box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1).

![Testimonial card default](components/crops/review-card-default.png)

#### FAQ question
A question row in the category FAQ block; measured closed. Read as `cat-faq` on the child care page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 722.66 x 72; background transparent; text Oceanic Grotesk 18/24 500, #1e1e1e `color.neutral.ink`; transition min-height 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #1e1e1e `color.neutral.ink` |
| focus-visible | background rgba(0, 0, 0, 0.12) |

![FAQ question default](components/crops/cat-faq-default.png) ![FAQ question hover](components/crops/cat-faq-hover.png) ![FAQ question focus-visible](components/crops/cat-faq-focus-visible.png) ![FAQ question pressed](components/crops/cat-faq-pressed.png)

### Provider listing

The /babysitters public results page: real caregivers' first-name-plus-initial listings (photos, rates, tags) under the City/State and Filter toolbar, the signup-gate modal that mounts on scroll, and the pager.

#### Listing title
The listing display title ("Find Local Babysitters"). Read as `listing-h1` on the babysitters listing page.

**Values (default).** size 640 x 72; background transparent; text NaN Druid Sans 64/72 550, #1e1e1e `color.neutral.ink`.

![Listing title default](components/crops/listing-h1-default.png)

#### Location button
The outlined "City, State" location trigger on the listing toolbar; measured, never opened. Read as `city-button` on the babysitters listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 252 x 32; padding 4px 12px; border 1px solid #025747 `color.brand.green`; radius 20px; background #ffffff `color.neutral.white`; text Oceanic Grotesk 18/20 400, #9b9b9b; transition background 0.3s ease-out; icon 24 x 24, #034135 |
| hover | background #f5f5f5 `color.neutral.grey-hover` |
| focus-visible | border 1px solid #4d9380 `color.brand.green-focus`; shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px |
| pressed | background #e8e8e8 `color.neutral.grey-pressed` |

![Location button default](components/crops/city-button-default.png) ![Location button hover](components/crops/city-button-hover.png) ![Location button focus-visible](components/crops/city-button-focus-visible.png) ![Location button pressed](components/crops/city-button-pressed.png)

#### Filter button
The outlined Filter action on the listing toolbar; measured, never opened. Read as `filter-button` on the babysitters listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 120 x 32; padding 4px 12px; border 1px solid #025747 `color.brand.green`; radius 20px; background #ffffff `color.neutral.white`; text Oceanic Grotesk 18/28 400, #034135; transition background 0.3s ease-out; icon 24 x 24, #034135 |
| hover | background #f5f5f5 `color.neutral.grey-hover` |
| focus-visible | border 1px solid #4d9380 `color.brand.green-focus`; shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px |
| pressed | background #e8e8e8 `color.neutral.grey-pressed` |

![Filter button default](components/crops/filter-button-default.png) ![Filter button hover](components/crops/filter-button-hover.png) ![Filter button focus-visible](components/crops/filter-button-focus-visible.png) ![Filter button pressed](components/crops/filter-button-pressed.png)

#### Signup-gate dialog
The "Join Care.com" modal the listing mounts over the results once they are scrolled to: measured open, then hidden, never answered or submitted. Read as `gate-dialog` on the babysitters listing page.

Not on the page when it was captured.

#### Gate CTA
The gate dialog's primary action; measured, never pressed. Read as `gate-cta` on the babysitters listing page.

Not on the page when it was captured.

#### Provider card
A caregiver listing row (first name + initial, photo, rate, tags, review count) — a real person's public profile summary; structure only, measured, never followed. Read as `provider-card` on the babysitters listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 645.33 x 160; padding 0px 0px 0px 24px; background transparent; text Oceanic Grotesk 24/32 500, #1e1e1e `color.neutral.ink`; icon 24 x 24, #1e1e1e `color.neutral.ink`; layers a::before.MuiTypography-root.MuiTypography-h3 autoxauto T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px |
| focus-visible | layers a::before.MuiTypography-root.MuiTypography-h3 473.984pxx40px T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px |

Child layers that carry the look: a::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 6px.

![Provider card default](components/crops/provider-card-default.png) ![Provider card hover](components/crops/provider-card-hover.png) ![Provider card focus-visible](components/crops/provider-card-focus-visible.png) ![Provider card pressed](components/crops/provider-card-pressed.png)

#### Care tag
A service chip on the provider card (light cleaning, meal prep, travel ...). Read as `care-tag` on the babysitters listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 71.95 x 24; padding 2px 4px; radius 4px; background #f5f5f5 `color.neutral.grey-hover`; text Oceanic Grotesk 14/20 400, #1e1e1e `color.neutral.ink` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Care tag default](components/crops/care-tag-default.png) ![Care tag hover](components/crops/care-tag-hover.png) ![Care tag pressed](components/crops/care-tag-pressed.png)

#### Read-more link
The bio expander on a provider card. Read as `read-more` on the babysitters listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 74 x 24; background transparent; text Oceanic Grotesk 16/24 400, #377a69 `color.brand.green-link`; layers ::before rgba(0, 0, 0, 0) 2px none 1; button::before.MuiTypography-root.MuiTypography-inherit autoxauto T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px |
| hover | text Oceanic Grotesk 16/24 400, #256959 |
| focus-visible | outline 3px auto #4d9380 `color.brand.green-focus`, offset 0px; text Oceanic Grotesk 16/24 400, #4d9380 `color.brand.green-focus`; layers ::before rgba(0, 0, 0, 0) 2px none 1; button.MuiTypography-root.MuiTypography-inherit 74.0x24.0 3px auto rgb(77, 147, 128) offset 0px; button::before.MuiTypography-root.MuiTypography-inherit 82pxx32px T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px |
| pressed | text Oceanic Grotesk 16/24 400, #034135 |

Child layers that carry the look: button::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 6px.

![Read-more link default](components/crops/read-more-default.png) ![Read-more link hover](components/crops/read-more-hover.png) ![Read-more link focus-visible](components/crops/read-more-focus-visible.png) ![Read-more link pressed](components/crops/read-more-pressed.png)

#### Pagination
The results pager (1 2 3 4 5 ... N). Read as `pagination` on the babysitters listing page.

**Values (default).** size 332.23 x 32; background transparent; text Oceanic Grotesk 16/32 400, #ffffff `color.neutral.white`; icon 20 x 20, #c6c6c6; layers a.MuiButtonBase-root.MuiPaginationItem-root 24.0x24.0 rgb(30, 30, 30) 16px.

Child layers that carry the look: a 24x24 background #1e1e1e `color.neutral.ink` radius 16px.

![Pagination default](components/crops/pagination-default.png)

#### Page item
A page-number item in the pager. Read as `page-item` on the babysitters listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; padding 0px 4px; radius 16px; background transparent; text Oceanic Grotesk 16/32 400, #1e1e1e `color.neutral.ink`; transition color 0.25s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.25s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f5f5f5 `color.neutral.grey-hover` |
| focus-visible | shadow #4d9380 0px 0px 0px 1px; layers a.MuiButtonBase-root.Mui-focusVisible 24.0x24.0 rgb(77, 147, 128) 0px 0px 0px 1px 16px |
| pressed | background #e8e8e8 `color.neutral.grey-pressed` |

![Page item default](components/crops/page-item-default.png) ![Page item hover](components/crops/page-item-hover.png) ![Page item focus-visible](components/crops/page-item-focus-visible.png) ![Page item pressed](components/crops/page-item-pressed.png)

#### Learn-more link
A text-button link on the listing page. Read as `learn-more` on the babysitters listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 85.11 x 18; radius 16px; background transparent; text Oceanic Grotesk 16/18 700, #377a69 `color.brand.green-link` |
| hover | text Oceanic Grotesk 16/18 700, #8ae718 `color.brand.lime-pressed` |
| focus-visible | text Oceanic Grotesk 16/18 700, #4d9380 `color.brand.green-focus` |

![Learn-more link default](components/crops/learn-more-default.png) ![Learn-more link hover](components/crops/learn-more-hover.png) ![Learn-more link focus-visible](components/crops/learn-more-focus-visible.png) ![Learn-more link pressed](components/crops/learn-more-pressed.png)

#### FAQ question
A question row in the "FAQs for finding a babysitter" block; measured closed. Read as `list-faq` on the babysitters listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 746.66 x 72; background transparent; text Oceanic Grotesk 18/24 500, #1e1e1e `color.neutral.ink`; transition min-height 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #1e1e1e `color.neutral.ink` |
| focus-visible | background rgba(0, 0, 0, 0.12) |

![FAQ question default](components/crops/list-faq-default.png) ![FAQ question hover](components/crops/list-faq-hover.png) ![FAQ question focus-visible](components/crops/list-faq-focus-visible.png) ![FAQ question pressed](components/crops/list-faq-pressed.png)

### Login page

The signed-out login card on /vis/auth/login: an email step only — the password step sits behind Continue and was never reached.

#### Login card
The sign-in card on /vis/auth/login (redirects to /vis/lcp/login, a legacy form — not the MUI layer): captured as a boundary surface, never filled or submitted. Read as `login-card` on the login page.

**Values (default).** size 311 x 252; background transparent; text Proxima Nova 14/17 400, #172c42; layers input.form-control 311.0x50.0 rgb(255, 255, 255) T:1px solid rgb(179, 186, 193) / R:1px solid rgb(179, 186, 193) / B:1px solid rgb(179, 186, 193) / L:1px solid rgb(179, 186, 193) 10px; button.btn.btn-primary-2 311.0x50.0 rgb(2, 87, 71) T:1px solid rgb(2, 87, 71) / R:1px solid rgb(2, 87, 71) / B:1px solid rgb(2, 87, 71) / L:1px solid rgb(2, 87, 71) 50px.

Child layers that carry the look: input 311x50 background #ffffff `color.neutral.white` border 1px solid #b3bac1 radius 10px; button 311x50 background #025747 `color.brand.green` border 1px solid #025747 `color.brand.green` radius 50px.

![Login card default](components/crops/login-card-default.png)

#### Email field
The login email input (input.form-control); focused only, never typed into. The password step sits behind Continue, never reached. Read as `login-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 311 x 50; padding 6px 12px; border 1px solid #b3bac1; radius 10px; background #ffffff `color.neutral.white`; text Proxima Nova 16/22.85 400, #172c42; transition border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out; placeholder #172c42 |
| focused | border 1px solid #083093 |

![Email field default](components/crops/login-email-default.png) ![Email field focused](components/crops/login-email-focused.png)

#### Login button
The Continue action; measured, never pressed — the password step and the account sit behind it. Read as `login-button` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 311 x 50; padding 7px 30px; border 1px solid #025747 `color.brand.green`; radius 50px; background #025747 `color.brand.green`; text Oceanic Grotesk 20/18 700, #d0f5a3 `color.brand.lime`; transition transform 0.3s ease-out, background 0.3s ease-out, -webkit-transform 0.3s ease-out |
| hover | border 1px solid #377a69 `color.brand.green-link`; background #377a69 `color.brand.green-link`; text Oceanic Grotesk 20/18 700, #e4ffb8 `color.brand.lime-hover` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px |
| pressed | border 1px solid #377a69 `color.brand.green-link`; background #377a69 `color.brand.green-link`; text Oceanic Grotesk 20/18 700, #e4ffb8 `color.brand.lime-hover` |

![Login button default](components/crops/login-button-default.png) ![Login button hover](components/crops/login-button-hover.png) ![Login button focus-visible](components/crops/login-button-focus-visible.png) ![Login button pressed](components/crops/login-button-pressed.png)

#### Passwordless link
The "Log in without a password" link; measured, never followed. Read as `passwordless-link` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 311 x 50; background transparent; text Proxima Nova 18/25.71 700, #025747 `color.brand.green`; layers div.passwordless-login-btn.cta-login-btn 311.0x50.0 rgb(255, 255, 255) T:1px solid rgb(2, 87, 71) / R:1px solid rgb(2, 87, 71) / B:1px solid rgb(2, 87, 71) / L:1px solid rgb(2, 87, 71) 50px |
| hover | layers div.passwordless-login-btn.cta-login-btn 311.0x50.0 rgb(250, 254, 245) T:1px solid rgb(2, 87, 71) / R:1px solid rgb(2, 87, 71) / B:1px solid rgb(2, 87, 71) / L:1px solid rgb(2, 87, 71) 50px |
| focus-visible | outline 5px auto #005fcc, offset -2px; layers a 311.0x50.0 5px auto rgb(0, 95, 204) offset -2px; div.passwordless-login-btn.cta-login-btn 311.0x50.0 rgb(255, 255, 255) T:1px solid rgb(2, 87, 71) / R:1px solid rgb(2, 87, 71) / B:1px solid rgb(2, 87, 71) / L:1px solid rgb(2, 87, 71) 50px |

Child layers that carry the look: div 311x50 background #ffffff `color.neutral.white` border 1px solid #025747 `color.brand.green` radius 50px.

![Passwordless link default](components/crops/passwordless-link-default.png) ![Passwordless link hover](components/crops/passwordless-link-hover.png) ![Passwordless link focus-visible](components/crops/passwordless-link-focus-visible.png) ![Passwordless link pressed](components/crops/passwordless-link-pressed.png)

### Join page

The /app/vhp/get-started chooser: I need a caregiver / I want a care job cards; captured as a boundary, never followed.

#### Join card
A chooser card on /app/vhp/get-started ("I need a caregiver" / "I want a care job"); captured as a boundary, never followed. Read as `join-card` on the join page.

**Values (default).** size 391 x 376; padding 48px 24px; radius 32px; background #ffffff `color.neutral.white`; text Oceanic Grotesk 24/32 500, #1e1e1e `color.neutral.ink`; transition box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1).

![Join card default](components/crops/join-card-default.png)

#### Join option
The Find-care/Find-jobs action inside a chooser card; measured, never pressed. Read as `join-option` on the join page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 170 x 40; padding 8px 24px; border 1px solid #025747 `color.brand.green`; radius 20px; background #025747 `color.brand.green`; text Oceanic Grotesk 16/18 500, #e4ffb8 `color.brand.lime-hover`; transition background 0.3s ease-out |
| hover | border 1px solid #377a69 `color.brand.green-link`; background #377a69 `color.brand.green-link` |
| focus-visible | border none; shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px |
| pressed | border 1px solid #034135; background #034135 |

![Join option default](components/crops/join-option-default.png) ![Join option hover](components/crops/join-option-hover.png) ![Join option focus-visible](components/crops/join-option-focus-visible.png) ![Join option pressed](components/crops/join-option-pressed.png)

### Pricing

The /app/vhp/plans-and-pricing page: the Premium monthly/quarterly/annual columns, the Senior Care Advisor bundle and the add-on cards.

#### Pricing title
The "Flexible plans that fit your life" title. Read as `pricing-h1` on the pricing page.

**Values (default).** size 1183 x 36.8; background transparent; text NaN Druid Sans 32/36.8 550, #1e1e1e `color.neutral.ink`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Plan card
A Premium plan column (monthly/quarterly/annual); measured, never checked out. Read as `plan-card` on the pricing page.

**Values (default).** size 373 x 341; padding 24px; radius 32px; background #ffffff `color.neutral.white`; text Oceanic Grotesk 24/32 500, #1e1e1e `color.neutral.ink`; icon 24 x 24, #1e1e1e `color.neutral.ink`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan price
A plan price figure ($39.99 monthly / $25.99 quarterly / $13.99 annual). Read as `plan-price` on the pricing page.

**Values (default).** size 109.73 x 32; background transparent; text Oceanic Grotesk 32/32 500, #1e1e1e `color.neutral.ink`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan Get-started action; measured, never pressed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 171 x 56; padding 14px 16px; border 1px solid #025747 `color.brand.green`; radius 32px; background #025747 `color.brand.green`; text Oceanic Grotesk 20/16 500, #e4ffb8 `color.brand.lime-hover`; transition background 0.3s ease-out |
| hover | border 1px solid #377a69 `color.brand.green-link`; background #377a69 `color.brand.green-link` |
| focus-visible | border none; shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px |
| pressed | border 1px solid #034135; background #034135 |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan alt
An outlined secondary action (Why join?); measured, never pressed. Read as `plan-alt` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 183.48 x 56; padding 14px 28px 14px 20px; radius 28px; background rgba(255, 255, 255, 0.9); text Oceanic Grotesk 20/24 700, #025747 `color.brand.green`; transition background 0.3s ease-out; transform translate(-91.7422px, -28px); icon 48 x 48, #034135 |
| hover | background #f5f5f5 `color.neutral.grey-hover`; text Oceanic Grotesk 20/24 700, #034135 |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px; text Oceanic Grotesk 20/24 700, #034135 |
| pressed | background #f5f5f5 `color.neutral.grey-hover`; text Oceanic Grotesk 20/24 700, #034135 |

![Plan alt default](components/crops/plan-alt-default.png) ![Plan alt hover](components/crops/plan-alt-hover.png) ![Plan alt focus-visible](components/crops/plan-alt-focus-visible.png) ![Plan alt pressed](components/crops/plan-alt-pressed.png)

#### Add-on card
An add-on product card (Feature your job post, Social Media Check, Hiring Helper). Read as `addon-card` on the pricing page.

**Values (default).** size 624 x 188; padding 32px; radius 24px; background #ffffff `color.neutral.white`; text Oceanic Grotesk 24/32 500, #1e1e1e `color.neutral.ink`; transition box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 40 x 40, #1e1e1e `color.neutral.ink`.

![Add-on card default](components/crops/addon-card-default.png)

#### Pricing FAQ
A billing FAQ row (How do I pay the caregiver once hired?); measured closed. Read as `pricing-faq` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 737 x 24; background transparent; text Oceanic Grotesk 18/24 700, #1e1e1e `color.neutral.ink`; transition margin 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, rgba(0, 0, 0, 0.54); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | layers ::before rgba(0, 0, 0, 0) 0px none 1; div.MuiButtonBase-root.Mui-focusVisible 737.0x24.0 rgba(0, 0, 0, 0.12) |

![Pricing FAQ default](components/crops/pricing-faq-default.png) ![Pricing FAQ hover](components/crops/pricing-faq-hover.png) ![Pricing FAQ focus-visible](components/crops/pricing-faq-focus-visible.png) ![Pricing FAQ pressed](components/crops/pricing-faq-pressed.png)

### Footer

The deep-green GlobalFooter: link columns, legal and the social row.

#### Footer
The inverse (dark) GlobalFooter: link columns, legal and the social row. Read as `footer` on the home page.

**Values (default).** size 1440 x 886.8; padding 40px 0px 8.8px 0px; background #025747 `color.brand.green`; text Oceanic Grotesk 16/20 500, #d0f5a3 `color.brand.lime`; icon 48 x 48, #d0f5a3 `color.brand.lime`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 56.58 x 20; background transparent; text Oceanic Grotesk 14/20 400, #d0f5a3 `color.brand.lime`; layers ::before rgba(0, 0, 0, 0) 2px none 1; a::before.MuiTypography-root.MuiTypography-link3 autoxauto T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px |
| focus-visible | layers ::before rgba(0, 0, 0, 0) 2px none 1; a::before.MuiTypography-root.MuiTypography-link3 64.5781pxx28px T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px |

Child layers that carry the look: a::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 6px.

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A social link/icon in the footer. Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 48 x 56; background transparent; text Oceanic Grotesk 18/28 400, #0000ee; icon 48 x 48, #d0f5a3 `color.brand.lime` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.MuiBox-root.mui-3n26xl 48.0x56.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text Oceanic Grotesk 18/28 400, #ff0000 |

![Social link default](components/crops/social-icon-default.png) ![Social link hover](components/crops/social-icon-hover.png) ![Social link focus-visible](components/crops/social-icon-focus-visible.png) ![Social link pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The same surface at phone width: slimmer header, the full-screen CareMobileDrawer menu, smaller display type.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 56; padding 12px 16px; background transparent; text Oceanic Grotesk 18/28 400, #ffffff `color.neutral.white`; transition background-color 0.3s ease-in-out; icon 24 x 24, #1e1e1e `color.neutral.ink`; layers button::before.MuiButtonBase-root.CareTouchMenuButton-root autoxauto T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px; span.MuiBadge-badge.MuiBadge-dot 0.0x0.0 rgb(215, 50, 24) 4px; a::before.MuiTypography-root.MuiTypography-inherit autoxauto T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid .

Child layers that carry the look: button::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 6px; span 0x0 background #d73218 radius 4px; a::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 6px.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The "Open menu" touch toggle at phone width. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 24 x 24; background transparent; text Arial 13.33/normal 400, #1e1e1e `color.neutral.ink`; icon 24 x 24, #1e1e1e `color.neutral.ink`; layers ::before rgba(0, 0, 0, 0) 2px none 1; button::before.MuiButtonBase-root.CareTouchMenuButton-root autoxauto T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px; span.MuiBadge-badge.MuiBadge-dot 0.0x0.0 rgb(215, 50, 24) 4px.

Child layers that carry the look: button::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 6px; span 0x0 background #d73218 radius 4px.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The CareMobileDrawer panel opened by the header toggle at 390 (full-screen). Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; background #ffffff `color.neutral.white`; shadow rgba(0, 0, 0, 0.15) 0px 4px 16px 0px; text Oceanic Grotesk 18/24 500, #1e1e1e `color.neutral.ink`; transition transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), boxShadow 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #1e1e1e `color.neutral.ink`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
A link inside the opened mobile drawer. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 390 x 56; padding 16px 16px 16px 24px; background transparent; text Oceanic Grotesk 18/24 500, #1e1e1e `color.neutral.ink`; icon 24 x 24, #1e1e1e `color.neutral.ink`; layers ::before rgba(0, 0, 0, 0) 2px none 1; button::before.MuiButtonBase-root.MobileNavTraverseBtn--root autoxauto T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px |
| focus-visible | layers ::before rgba(0, 0, 0, 0) 2px none 1; button::before.MuiButtonBase-root.Mui-focusVisible 390pxx56px T:2px solid rgb(77, 147, 128) / R:2px solid rgb(77, 147, 128) / B:2px solid rgb(77, 147, 128) / L:2px solid rgb(77, 147, 128) 6px |

Child layers that carry the look: button::before autoxauto border 2px solid #4d9380 `color.brand.green-focus` radius 6px.

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 330 x 224; background transparent; text NaN Druid Sans 48/56 550, #ffffff `color.neutral.white`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Care.com wordmark, the mega-menu chevrons and arrows, the rating stars, the social glyphs and the listing photography) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The member product — the dashboard, inbox and messaging, bookings, payments, job applications, caregiver profiles behind login and every membership flow — sits behind the login and join shells. The email step on /vis/auth/login was measured as a card, never filled, so the password step, two-factor screens and everything past them were never reached and are not inferred.

### Pages

- **The member surface.** Everything post-login was never reached; the login card, the get-started chooser and the signup-gate modal were measured as boundaries, never used.
- **Search, booking and payment.** The hero ZIP search, the provider cards' own links, the City/State and Filter controls, the plan Get-started buttons and every "Join now" action were measured or screenshotted, never followed through to a search, message, hire or checkout.
- **Provider profiles.** /babysitters lists real public caregivers (first name + initial, photo, rate, tags); the rows were measured as components, never opened, and no contact detail appears on the public page.
- **External surfaces** (Care for Business, the app-store links, social profiles and the linked partner pages) were never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **The signup gate** was measured open once (it mounts on scroll) and then hidden, never answered; a run where it did not mount records the dialog missing.

### Themes

One theme is painted: the white/light canvas with deep-green and lime accents and the dark footer panel. No dark toggle exists on the public surface; tokens.json keeps the dark-painted surfaces' roles in the dark set.

### Fonts

- **Oceanic Grotesk** is the UI family (400/450/500/550 measured), **NaN Druid Sans** the display family on headlines, **Oceanic Text Semibold** the serif accent on testimonial names — all served from care.com's own /css/cms/font-face/ files. The legacy login form paints in **Proxima Nova**. The style guide falls back to system fonts.

### Screenshots

- Caregiver photography, listing profile photos, the hero imagery and the Care.com wordmark in the screenshots are the product's published content; real public names appear on the listing under the repo's private-library policy (no contact details are shown by the product or kept here).
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Caregiver bios, review text, FAQ answers and marketing copy are the product's content; only frames and components were measured.
