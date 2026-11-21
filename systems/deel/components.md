# Deel components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from deel.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or downloaded; the nav dropdowns, hero action tiles and FAQ accordions are local UI toggles, and hover/focus/pressed states were forced. Log in, Book a demo, Claim offer and every product/store link were measured, never followed; the Cookiebot banner was hidden for clean captures, never answered; app.deel.com was never reached.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (36 components, 82 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (82 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every page paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at CSS scale (one CSS pixel per image pixel — mobile fulls are 390 wide); mobile viewport shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Pricing | `/pricing/` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Deel HR | `/hr/` | [default](screenshots/hr-light-default.png), [full](screenshots/hr-light-full.png) |
| Global Payroll | `/global-payroll/` | [default](screenshots/payroll-light-default.png), [full](screenshots/payroll-light-full.png) |
| About | `/about-us/` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `/pricing/` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Solutions mega dropdown | the nav | the nav item hovered locally | [nav-link](#nav-link) states + [home-light-menu](screenshots/home-light-menu.png) |
| Mobile drawer | home, phone width | the mobile hamburger | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png) |
| Promo strip | every page | the banner was measured, never dismissed | [promo-banner](#promo-banner) |
| Cookiebot consent | every page | the dialog was hidden for clean captures, never answered | boundary; see Gaps |
| Log in / app.deel.com | the nav | the outbound link was measured, never followed | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 16 components were given a real keyboard focus. 14 draw an outline ring: `promo-cta` (1px auto #005fcc `light.border.focus`, offset 0px), `nav-link` (1px auto #005fcc `light.border.focus`, offset 0px), `nav-plain-link` (1px auto #005fcc `light.border.focus`, offset 1px), `nav-locale` (1px auto #005fcc `light.border.focus`, offset 0px), `nav-login` (1px auto #005fcc `light.border.focus`, offset 1px), `nav-demo` (1px auto #005fcc `light.border.focus`, offset 0px), `hero-demo` (1px auto #005fcc `light.border.focus`, offset 0px), `product-card` (1px auto #005fcc `light.border.focus`, offset 1px), `footer-link` (1px auto #005fcc `light.border.focus`, offset 1px), `social-link` (1px auto #005fcc `light.border.focus`, offset 1px), `price-cta` (1px auto #005fcc `light.border.focus`, offset 0px), `hr-cta` (1px auto #101010, offset 0px), `m-demo` (1px auto #e59700, offset 0px), `menu-item` (1px auto #005fcc `light.border.focus`, offset 1px). 1 draw a focus ring as a shadow instead: `hero-tile`. The other 1 show no measured change: `faq-item`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease-in-out` | all, background, color, opacity | faq-item, footer-link, hero-demo, hr-cta, m-demo, m-hamburger, m-logo, menu-item and more |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | hero-tile, nav-locale |
| 0.2s | `ease-in-out` | box-shadow | header-nav, m-nav-bar |
| 0.3s | `cubic-bezier(0, 0, 0.2, 1)` | all | product-card |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Hero action tile](#hero-action-tile) | 181.5 x 80 | 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1) | 12px | oklab(0.999994 0.0000455678 0.0000200868 / 0.04) | none | 12px |
| [Product card](#product-card) | 418.66 x 438 | - | 16px | #f7f5f2 `core.color.surface.latte-light` | none | 24px |
| [Price card](#price-card) | 458.66 x 928.31 | - | 12px | #ffffff `core.color.content.on-color` | rgba(27, 27, 27, 0.04) 0px 8px 16px 0px, rgba(27, 27, 27, 0.04) 0px 2px 8px 0px | 0 |
| [Reviews band](#reviews-band) | 1440 x 1205.88 | - | - | #ffffff `core.color.content.on-color` | none | 0 |
| [FAQ accordion](#faq-accordion) | 952 x 80.2 | T: 1px solid rgba(250, 244, 238, 0.16) `core.color.border.primary-on-dark` | - | transparent | none | 0 |

## Components

### Shell and navigation

The sticky chrome shared by every page: the 64px #1b1b1b promo strip (SPECIAL OFFER chip, Claim offer pill, close), the 80px white nav (78px wordmark, 15px BagossStandardVF dropdown items, Pricing, EN, Log in, the 118x40 #1b1b1b Book-a-demo pill), and the ~1015px footer with cream column headings and link lists.

#### Promo banner
The "Special Offer" strip above the nav ("Get 3 months free of PEO" + Claim offer + close); a dismissible banner, never dismissed. Read as `promo-banner` on the home page.

**Values (default).** size 1440 x 64; background transparent; text Inter 12/12 600, rgba(0, 0, 0, 0.87) `light.text.body`; icon 24 x 24, #ffffff `core.color.content.on-color`; layers div.MuiBox-root.mui-r1bhz9 1440.0x64.0 rgb(27, 27, 27); div.MuiBox-root.mui-1wjc8ik 111.1x28.0 rgb(177, 216, 252) 2px; button.mui-1rh4x73 85.4x32.0 rgb(255, 255, 255) 200px.

Child layers that carry the look: div 1440x64 background #1b1b1b `core.color.primary`; div 111.1x28 background #b1d8fc `core.color.blue.325` radius 2px; button 85.4x32 background #ffffff `core.color.content.on-color` radius 200px.

![Promo banner default](components/crops/promo-banner-default.png)

#### Promo CTA
"Claim offer" — the banner button; measured, never followed. Read as `promo-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85.36 x 32; padding 6px 12px; radius 200px; background #ffffff `core.color.content.on-color`; text BagossStandardVF 12/20.4 500, #1b1b1b `core.color.primary`; transition all 0.1s ease-in-out |
| hover | background #3f3f3f `light.action.pressed-fill`; text BagossStandardVF 12/20.4 500, #ffffff `core.color.content.on-color` |
| focus-visible | outline 1px auto #005fcc `light.border.focus`, offset 0px |
| pressed | background #3f3f3f `light.action.pressed-fill`; text BagossStandardVF 12/20.4 500, #ffffff `core.color.content.on-color` |

![Promo CTA default](components/crops/promo-cta-default.png) ![Promo CTA hover](components/crops/promo-cta-hover.png) ![Promo CTA focus-visible](components/crops/promo-cta-focus-visible.png) ![Promo CTA pressed](components/crops/promo-cta-pressed.png)

#### Header nav
The sticky nav inside the header: logo, Solutions/Use cases/Who we serve/Resources, Pricing, EN, Log in, Book a demo. Read as `header-nav` on the home page.

**Values (default).** size 1440 x 80; padding 20px 64px; background #ffffff `core.color.content.on-color`; text BagossStandardVF 15/24 500, #1b1b1b `core.color.primary`; transition box-shadow 0.2s ease-in-out; icon 24 x 24, #1b1b1b `core.color.primary`.

![Header nav default](components/crops/header-nav-default.png)

#### Logo
The Deel wordmark in the nav. Read as `nav-logo` on the home page.

**Values (default).** size 78 x 28; background transparent; text Inter 16/24 400, #1b1b1b `core.color.primary`; transition color 0.1s ease-in-out.

![Logo default](components/crops/nav-logo-default.png)

#### Nav item (dropdown)
"Solutions" — a dropdown nav item; measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 95.31 x 40; padding 8px 0px; background transparent; text BagossStandardVF 15/24 500, #1b1b1b `core.color.primary`; transition all 0.1s ease-in-out; icon 24 x 24, #1b1b1b `core.color.primary` |
| hover | opacity 0.7 |
| focus-visible | outline 1px auto #005fcc `light.border.focus`, offset 0px; layers button.mui-1fo3fxi 95.3x40.0 1px auto rgb(0, 95, 204) offset 0px |
| pressed, opened | opacity 0.7 |

![Nav item (dropdown) default](components/crops/nav-link-default.png) ![Nav item (dropdown) hover](components/crops/nav-link-hover.png) ![Nav item (dropdown) focus-visible](components/crops/nav-link-focus-visible.png) ![Nav item (dropdown) pressed](components/crops/nav-link-pressed.png) ![Nav item (dropdown) opened](components/crops/nav-link-opened.png)

#### Nav link
"Pricing" — a plain nav link; measured, never followed. Read as `nav-plain-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 50.2 x 40; padding 8px 0px; background transparent; text BagossStandardVF 15/24 500, #1b1b1b `core.color.primary`; transition color 0.1s ease-in-out |
| hover | text BagossStandardVF 15/24 500, #4e4e4e `light.action.hover-fill` |
| focus-visible | outline 1px auto #005fcc `light.border.focus`, offset 1px; layers a.mui-1moi9ht 50.2x40.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text BagossStandardVF 15/24 500, #4e4e4e `light.action.hover-fill` |

![Nav link default](components/crops/nav-plain-link-default.png) ![Nav link hover](components/crops/nav-plain-link-hover.png) ![Nav link focus-visible](components/crops/nav-plain-link-focus-visible.png) ![Nav link pressed](components/crops/nav-plain-link-pressed.png)

#### Locale switch
The "EN" language/locale switch in the nav; measured, never changed. Read as `nav-locale` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 68.11 x 36; padding 8px 12px; radius 3.35544e+07px; background transparent; text Inter 14/20 600, #1b1b1b `core.color.primary`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1); layers img.border.border-white 12.5x12.5 T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255) 3.35544e+07px |
| hover | background oklab(0.98 0.00449496 0.0153556 / 0.8); layers none |
| focus-visible | outline 1px auto #005fcc `light.border.focus`, offset 0px; layers button.flex.items-center 68.1x36.0 1px auto rgb(0, 95, 204) offset 0px 3.35544e+07px; img.border.border-white 12.5x12.5 T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255) 3.35544e+07px |
| pressed | background oklab(0.98 0.00449496 0.0153556 / 0.8); layers none |

Child layers that carry the look: img 12.5x12.5 border 1px solid #ffffff `core.color.content.on-color` radius 3.35544e+07px.

![Locale switch default](components/crops/nav-locale-default.png) ![Locale switch hover](components/crops/nav-locale-hover.png) ![Locale switch focus-visible](components/crops/nav-locale-focus-visible.png) ![Locale switch pressed](components/crops/nav-locale-pressed.png)

#### Log in link
"Log in" — outbound to app.deel.com; measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 75.14 x 40; background transparent; text BagossStandardVF 14/23.8 500, #1b1b1b `core.color.primary`; transition color 0.1s ease-in-out; layers button.hidden-phone.mui-ti8o1k 75.1x40.0 T:2px solid rgba(27, 27, 27, 0.16) / R:2px solid rgba(27, 27, 27, 0.16) / B:2px solid rgba(27, 27, 27, 0.16) / L:2px solid rgba(27, 27, 27, 0.16) 200px |
| hover | layers button.hidden-phone.mui-ti8o1k 75.1x40.0 T:2px solid rgba(27, 27, 27, 0.4) / R:2px solid rgba(27, 27, 27, 0.4) / B:2px solid rgba(27, 27, 27, 0.4) / L:2px solid rgba(27, 27, 27, 0.4) 200px |
| focus-visible | outline 1px auto #005fcc `light.border.focus`, offset 1px; layers a.mui-15k05j0 75.1x40.0 1px auto rgb(0, 95, 204) offset 1px; button.hidden-phone.mui-ti8o1k 75.1x40.0 T:2px solid rgba(27, 27, 27, 0.16) / R:2px solid rgba(27, 27, 27, 0.16) / B:2px solid rgba(27, 27, 27, 0.16) / L:2px solid rgba(27, 27, 27, 0.16) 200px |

Child layers that carry the look: button 75.1x40 border 2px solid rgba(27, 27, 27, 0.16) `core.color.border.primary` radius 200px.

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Book a demo CTA
The nav "Book a demo" button; measured, never followed. Read as `nav-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 117.22 x 40; padding 8px 16px; radius 200px; background #1b1b1b `core.color.primary`; text BagossStandardVF 14/23.8 500, #ffffff `core.color.content.on-color`; transition all 0.1s ease-in-out |
| hover | background #4e4e4e `light.action.hover-fill` |
| focus-visible | outline 1px auto #005fcc `light.border.focus`, offset 0px |
| pressed | background #4e4e4e `light.action.hover-fill` |

![Book a demo CTA default](components/crops/nav-demo-default.png) ![Book a demo CTA hover](components/crops/nav-demo-hover.png) ![Book a demo CTA focus-visible](components/crops/nav-demo-focus-visible.png) ![Book a demo CTA pressed](components/crops/nav-demo-pressed.png)

#### Footer
The footer band: product/company/resource columns, social icons, legal links. Read as `footer` on the home page.

**Values (default).** size 1440 x 1015.38; padding 0px 64px; background #1b1b1b `core.color.primary`; text Inter 14/23.8 560, #faf4ee `core.color.content.on-dark`; icon 20 x 20, #ffffff `core.color.content.on-color`; ancestors body bg #ffffff `core.color.content.on-color`.

![Footer default](components/crops/footer-default.png)

#### Footer column heading
A footer column heading ("Solutions"/"Deel Platform"/"Resources"). Read as `footer-heading` on the home page.

**Values (default).** size 236.8 x 18.41; background transparent; text BagossCondensedFont 16/18.4 500, #faf4ee `core.color.content.on-dark`.

![Footer column heading default](components/crops/footer-heading-default.png)

#### Footer link
"About us" — a footer menu link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 60.42 x 23.8; background transparent; text Inter 14/23.8 560, #faf4ee `core.color.content.on-dark`; transition color 0.1s ease-in-out |
| hover | opacity 0.8 |
| focus-visible | outline 1px auto #005fcc `light.border.focus`, offset 1px; layers a.mui-i1l04d 60.4x23.8 1px auto rgb(0, 95, 204) offset 1px |
| pressed | opacity 0.8 |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social icon link
A social icon link in the footer; measured, never followed. Read as `social-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; background transparent; text Inter 16/24 400, #0000ee |
| hover | opacity 0.8 |
| focus-visible | outline 1px auto #005fcc `light.border.focus`, offset 1px; layers a.mui-j04pfz 32.0x32.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text Inter 16/24 400, #ff0000; opacity 0.8 |

![Social icon link default](components/crops/social-link-default.png) ![Social icon link hover](components/crops/social-link-hover.png) ![Social icon link focus-visible](components/crops/social-link-focus-visible.png) ![Social icon link pressed](components/crops/social-link-pressed.png)

#### Mega-menu item
"Deel Payroll - Pay teams locally or globally" — a link inside the Solutions mega dropdown; measured after clicking the nav item open, never followed. Read as `menu-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 334 x 66; padding 8px; radius 14px; background transparent; text BagossStandardVF 16/25.6 540, #1b1b1b `core.color.primary`; transition background 0.1s ease-in-out; layers div.link-icon.MuiBox-root 48.0x48.0 rgb(246, 240, 254) 12px |
| focus-visible | outline 1px auto #005fcc `light.border.focus`, offset 1px; layers a.mui-egns2o 334.0x66.0 1px auto rgb(0, 95, 204) offset 1px 14px; div.link-icon.MuiBox-root 48.0x48.0 rgb(246, 240, 254) 12px |

Child layers that carry the look: div 48x48 background #f6f0fe `core.color.purple.100` radius 12px.

![Mega-menu item default](components/crops/menu-item-default.png) ![Mega-menu item focus-visible](components/crops/menu-item-focus-visible.png)

#### Mega-menu panel
The Solutions mega dropdown container (1241x629) opened by the nav item click; measured open, its links never followed. Read as `menu-panel` on the home page.

**Values (default).** size 1241 x 629; background transparent; text BagossStandardVF 13/14.95 500, rgba(27, 27, 27, 0.7) `core.color.content.tertiary`; icon 12 x 12, #ffffff `core.color.content.on-color`; layers p.mui-194yby4 692.0x32.0 B:1px solid rgba(27, 27, 27, 0.16); div.link-icon.MuiBox-root 48.0x48.0 rgb(246, 240, 254) 12px; div.link-icon.MuiBox-root 48.0x48.0 rgb(246, 240, 254) 12px; div.link-icon.MuiBox-root 48.0x48.0 rgb(246, 240, 254) 12px; div.link-icon.MuiBox-root 48.0x48.0 rgb(246, 240, 254) 12px; div.link-icon.MuiBox-root 48.0x48.0 rgb(246, 240, 254) 12px.

Child layers that carry the look: p 692x32 border 1px solid rgba(27, 27, 27, 0.16) `core.color.border.primary`; div 48x48 background #f6f0fe `core.color.purple.100` radius 12px; div 48x48 background #f6f0fe `core.color.purple.100` radius 12px.

![Mega-menu panel default](components/crops/menu-panel-default.png)

### Home

The landing: a 732px #201547 purple hero panel (60px BagossCondensed white headline, five glass action tiles — Hire anywhere, Run payroll, Secure visas, Manage HR & people, Ship equipment — and the 375x51 rounded-full Book-a-demo pill), then the global-people-platform product cards, the AI-readiness band, the 1206px customer-reviews video carousel and the footer.

#### Hero block
The dark hero section ("Hire, manage, pay, & equip anyone, anywhere." on a dark field). Read as `hero-block` on the home page.

**Values (default).** size 1416 x 732; background transparent; text BagossCondensedFont 60/63 500, #ffffff `core.color.content.on-color`; layers div.w-full.flex 702.6x732.0 rgb(32, 21, 71) 12px; button.group.flex 181.5x80.0 oklab(0.999994 0.0000455678 0.0000200868 / 0.04) T:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1) / R:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1) / B:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1) / L:1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1) 12px; span.inline-flex.ite; ancestors section.w-full.overflow-hidden bg #ffffff `core.color.content.on-color`.

Child layers that carry the look: div 702.6x732 background #201547 `core.color.purple.950` image linear-gradient(118deg, rgba(89, 56, 183, 0) 48.33%, #5938b7 `core.color.core.acai` 92.96% radius 12px; button 181.5x80 background oklab(0.999994 0.0000455678 0.0000200868 / 0.04) border 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1) radius 12px; span 18x18 border 2px solid #a98df6 `core.color.purple.525` radius 4px.

![Hero block default](components/crops/hero-block-default.png)

#### Hero heading
"Hire, manage, pay, & equip anyone, anywhere." — the BagossCondensed hero title. Read as `hero-h1` on the home page.

**Values (default).** size 574.59 x 189; background transparent; text BagossCondensedFont 60/63 500, #ffffff `core.color.content.on-color`.

![Hero heading default](components/crops/hero-h1-default.png)

#### Hero action tile
"Hire anywhere" — a quick-action tile under the hero title; measured, never followed. Read as `hero-tile` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 181.5 x 80; padding 12px; border 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.1); radius 12px; background oklab(0.999994 0.0000455678 0.0000200868 / 0.04); text Inter 14/16.8 600, #ffffff `core.color.content.on-color`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | shadow oklab(0.999994 0.0000455677 0.0000200868 / 0.7) 0px 0px 0px 2px |
| pressed | border 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.2); background oklab(0.999994 0.0000455678 0.0000200868 / 0.08) |

![Hero action tile default](components/crops/hero-tile-default.png) ![Hero action tile hover](components/crops/hero-tile-hover.png) ![Hero action tile focus-visible](components/crops/hero-tile-focus-visible.png) ![Hero action tile pressed](components/crops/hero-tile-pressed.png)

#### Hero demo button
The hero "Book a demo" pill (375x51 rounded-full); measured, never followed. Read as `hero-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 375 x 51; padding 12px 16px; radius 3.35544e+07px; background #ffffff `core.color.content.on-color`; text Inter 18/30.6 600, #1b1b1b `core.color.primary`; transition all 0.1s ease-in-out |
| hover | background oklab(0.999994 0.0000455678 0.0000200868 / 0.9) |
| focus-visible | outline 1px auto #005fcc `light.border.focus`, offset 0px |
| pressed | background oklab(0.999994 0.0000455678 0.0000200868 / 0.9) |

![Hero demo button default](components/crops/hero-demo-default.png) ![Hero demo button hover](components/crops/hero-demo-hover.png) ![Hero demo button focus-visible](components/crops/hero-demo-focus-visible.png) ![Hero demo button pressed](components/crops/hero-demo-pressed.png)

#### Section heading
A big Bagoss section heading ("The global people platform"). Read as `section-heading` on the home page.

**Values (default).** size 506.84 x 46.19; background transparent; text BagossCondensedFont 44/46.2 500, rgba(0, 0, 0, 0.87) `light.text.body`.

![Section heading default](components/crops/section-heading-default.png)

#### Product card
A "Deel Payroll" product card in the global-people-platform grid; measured, never followed. Read as `product-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 418.66 x 438; padding 24px; radius 16px; background #f7f5f2 `core.color.surface.latte-light`; text BagossCondensedFont 24/27.6 500, #1b1b1b `core.color.primary`; transition all 0.3s cubic-bezier(0, 0, 0.2, 1) |
| hover | shadow rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px |
| focus-visible | outline 1px auto #005fcc `light.border.focus`, offset 1px |

![Product card default](components/crops/product-card-default.png) ![Product card hover](components/crops/product-card-hover.png) ![Product card focus-visible](components/crops/product-card-focus-visible.png)

#### Review card
A customer-review slide inside the video-carousel band (the ~840x638 video card plus caption and case-study link); its link measured, never followed. Read as `review-card` on the home page.

**Values (default).** size 840 x 638; background transparent; text Inter 16/24 400, rgba(0, 0, 0, 0.87) `light.text.body`; icon 60 x 60, #000000 `core.color.black`; layers div.relative.w-full 840.0x500.0 rgb(20, 20, 20) 24px; span.mui-mv42ai 183.4x51.0 T:2px solid rgba(27, 27, 27, 0.16) / R:2px solid rgba(27, 27, 27, 0.16) / B:2px solid rgba(27, 27, 27, 0.16) / L:2px solid rgba(27, 27, 27, 0.16) 200px.

Child layers that carry the look: div 840x500 background #141414 `core.color.content.primary` radius 24px; span 183.4x51 border 2px solid rgba(27, 27, 27, 0.16) `core.color.border.primary` radius 200px.

![Review card default](components/crops/review-card-default.png)

#### Reviews band
The "Our customer reviews" video-carousel band (1440x1206). Read as `review-band` on the home page.

**Values (default).** size 1440 x 1205.88; background #ffffff `core.color.content.on-color`; text Inter 13/22.1 500, rgba(27, 27, 27, 0.7) `core.color.content.tertiary`; icon 60 x 60, #000000 `core.color.black`.

![Reviews band default](components/crops/review-band-default.png)

### Pricing

The /pricing/ page: the 56px BagossCondensed heading on a dark hero, the 459x928 elevation-2dp tier cards (Find talent / Hire contractors / Hire employees) with #1b1b1b pill CTAs, and the MUI FAQ accordion with its 16%-cream hairlines.

#### Pricing heading
"Transparent and fair pricing that grows with your business". Read as `price-h1` on the pricing page.

**Values (default).** size 1000 x 117.59; background transparent; text BagossCondensedFont 56/58.8 500, #ffffff `core.color.content.on-color`.

![Pricing heading default](components/crops/price-h1-default.png)

#### Price card
A pricing tier card (Find talent / Hire contractors / Hire employees). Read as `price-card` on the pricing page.

**Values (default).** size 458.66 x 928.31; radius 12px; background #ffffff `core.color.content.on-color`; shadow rgba(27, 27, 27, 0.04) 0px 8px 16px 0px, rgba(27, 27, 27, 0.04) 0px 2px 8px 0px; text BagossCondensedFont 28/32.2 500, #1b1b1b `core.color.primary`.

![Price card default](components/crops/price-card-default.png)

#### Price CTA
The "Book a demo"/"Get started" button inside a pricing tier card (395x51); measured, never followed. Read as `price-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 394.66 x 51; padding 12px 16px; radius 200px; background #1b1b1b `core.color.primary`; text BagossStandardVF 16/27.2 500, #ffffff `core.color.content.on-color`; transition all 0.1s ease-in-out; ancestors div.relative.flex bg #ffffff `core.color.content.on-color` |
| hover | background #4e4e4e `light.action.hover-fill` |
| focus-visible | outline 1px auto #005fcc `light.border.focus`, offset 0px |
| pressed | background #4e4e4e `light.action.hover-fill` |

![Price CTA default](components/crops/price-cta-default.png) ![Price CTA hover](components/crops/price-cta-hover.png) ![Price CTA focus-visible](components/crops/price-cta-focus-visible.png) ![Price CTA pressed](components/crops/price-cta-pressed.png)

#### FAQ accordion
A product-faqs MUI accordion summary; opened via its own click toggle. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 952 x 80.2; border T: 1px solid rgba(250, 244, 238, 0.16) `core.color.border.primary-on-dark`; background transparent; text BagossStandardVF 24/31.2 440, #ffffff `core.color.content.on-color`; transition opacity 0.1s ease-in-out; ancestors div.MuiPaper-root.MuiPaper-elevation bg #201547 `core.color.purple.950` |
| opened | opacity 0.6; icon 30 x 30, #ffffff `core.color.content.on-color` |
| focus-visible | background rgba(0, 0, 0, 0.12); icon 30 x 30, #ffffff `core.color.content.on-color` |

![FAQ accordion default](components/crops/faq-item-default.png) ![FAQ accordion opened](components/crops/faq-item-opened.png) ![FAQ accordion focus-visible](components/crops/faq-item-focus-visible.png)

### Deel HR

The /hr/ product page: the BagossCondensed hero heading and the 430x51 white CTA pill.

#### Product heading
The Deel HR page hero heading. Read as `hr-h1` on the hr page.

**Values (default).** size 574.59 x 109.19; background transparent; text BagossCondensedFont 52/54.6 500, #ffffff `core.color.content.on-color`.

![Product heading default](components/crops/hr-h1-default.png)

#### Product CTA
A product-page CTA; measured, never followed. Read as `hr-cta` on the hr page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 430 x 51; padding 12px 16px; radius 3.35544e+07px; background #ffffff `core.color.content.on-color`; text Inter 18/30.6 600, #1b1b1b `core.color.primary`; transition all 0.1s ease-in-out |
| hover | background oklab(0.999994 0.0000455678 0.0000200868 / 0.9) |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background oklab(0.999994 0.0000455678 0.0000200868 / 0.9) |

![Product CTA default](components/crops/hr-cta-default.png) ![Product CTA hover](components/crops/hr-cta-hover.png) ![Product CTA focus-visible](components/crops/hr-cta-focus-visible.png) ![Product CTA pressed](components/crops/hr-cta-pressed.png)

### Global Payroll

The /global-payroll/ product page: the 56px BagossCondensed hero heading.

#### Payroll heading
The Global Payroll page hero heading. Read as `payroll-h1` on the global-payroll page.

**Values (default).** size 610 x 117.59; background transparent; text BagossCondensedFont 56/58.8 500, #faf4ee `core.color.content.on-dark`.

![Payroll heading default](components/crops/payroll-h1-default.png)

### About

The /about-us/ page: the 160px BagossCondensed display numeral.

#### About heading
The About page heading. Read as `about-h1` on the about page.

**Values (default).** size 283 x 160; background transparent; text BagossCondensedFont 160/160 600, #ffffff `core.color.content.on-color`.

![About heading default](components/crops/about-h1-default.png)

### Mobile (390 wide)

The home and /pricing/ at phone width: the 64px nav, the 40px hamburger circle, the 38px hero heading and the drawer.

#### Mobile nav
Read as `m-nav-bar` on the home page at 390 wide.

**Values (default).** size 390 x 64; padding 12px 24px; background #ffffff `core.color.content.on-color`; text BagossStandardVF 14/23.8 500, #ffffff `core.color.content.on-color`; transition box-shadow 0.2s ease-in-out.

![Mobile nav default](components/crops/m-nav-bar-default.png)

#### Mobile logo
Read as `m-logo` on the home page at 390 wide.

**Values (default).** size 78 x 28; background transparent; text Inter 16/24 400, #1b1b1b `core.color.primary`; transition color 0.1s ease-in-out.

![Mobile logo default](components/crops/m-logo-default.png)

#### Mobile hamburger
The hamburger/drawer trigger at 390px. Read as `m-hamburger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; radius 50%; background transparent; text BagossStandardVF 16/27.2 500, #1b1b1b `core.color.primary`; transition all 0.1s ease-in-out; icon 24 x 24, #1b1b1b `core.color.primary` |
| pressed | opacity 0.7 |

![Mobile hamburger default](components/crops/m-hamburger-default.png) ![Mobile hamburger pressed](components/crops/m-hamburger-pressed.png)

#### Mobile hero heading
The hero h1 at 390px. Read as `m-h1` on the home page at 390 wide.

**Values (default).** size 334 x 119.67; background transparent; text BagossCondensedFont 38/39.9 500, #ffffff `core.color.content.on-color`.

![Mobile hero heading default](components/crops/m-h1-default.png)

#### Mobile demo CTA
A Book a demo button at 390px; measured, never followed. Read as `m-demo` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 118.31 x 40; padding 8px 16px; radius 200px; background #1b1b1b `core.color.primary`; text BagossStandardVF 14/23.8 500, #ffffff `core.color.content.on-color`; transition all 0.1s ease-in-out |
| hover | background #4e4e4e `light.action.hover-fill` |
| focus-visible | outline 1px auto #e59700, offset 0px |
| pressed | background #4e4e4e `light.action.hover-fill` |

![Mobile demo CTA default](components/crops/m-demo-default.png) ![Mobile demo CTA hover](components/crops/m-demo-hover.png) ![Mobile demo CTA focus-visible](components/crops/m-demo-focus-visible.png) ![Mobile demo CTA pressed](components/crops/m-demo-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the wordmark, the social icons, the hero tile glyphs) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Members and external destinations

Deel's product sits behind a login wall. A 2026-11-21 refresh opened Log in and stopped. Desktop: [login-wall-light-default](screenshots/login-wall-light-default.png). Phone: [mobile-login-wall-light-default](screenshots/mobile-login-wall-light-default.png). The wall offers the Deel app, SSO, Google, email, and password. Nothing was typed. Nothing was submitted. Those buttons were not clicked. Book a demo opens a public dialog ([home-light-demo-dialog](screenshots/home-light-demo-dialog.png)) and was not filled. The control map is [site-tree.md](site-tree.md).

### Pages

- **Login wall.** Log in opens the login wall and that branch stops. See [login-review.json](login-review.json). Book a demo opens a public dialog and was not filled. Claim offer and product links stay measured destinations.
- **Product sub-pages.** /hr/, /global-payroll/ and /about-us/ were captured; the dozens of other product/resource/solution pages share the same chrome and hero/card vocabulary but are not individually documented.
- **The Solutions/Use cases/Who we serve/Resources dropdowns** open on hover as mega panels; the open panel was screenshot (home-light-menu) but its inner items were not individually componentized.
- **Geo/personalisation.** The promo strip and offers are served per region and campaign. What was captured is the offer that loaded for this signed-out visit.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **The nav dropdowns, hero action tiles and FAQ accordions** were toggled locally (the site's own triggers); nothing was typed into or submitted anywhere.
- **No forms exist on the captured surface** — every demo/contact flow sits behind a CTA; fields, validation, disabled and error states are therefore absent rather than measured.
- **Hero tiles switch a preview panel** (they are tab-like buttons); the panels behind the other four tiles were not individually measured.

### Themes

One painted theme, no toggle: a white field, a #1b1b1b promo strip and primary buttons, a #201547 purple hero and dark video cards, with #b1d8fc sky accents and #faf4ee cream details. The dark regions are recorded as surfaces inside the single theme; tokens.json emits light only (the only resolved :root vars are the --font-* families and --swiper-theme-color).

### Fonts

- **Inter** (UI/body), **BagossStandardVF** (nav, pill buttons) and **BagossCondensedFont** (every display heading) are served by the site; Bagoss Extended exists as a font var but no measured element used it. Font files are not shipped in this package.

### Screenshots

- Customer names, faces and quotes in the review carousel and the artwork inside hero panels are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Testimonial copy, pricing figures and the artwork inside panels are the product's content; only frames and components were measured.
