# Canva components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from canva.com on 2026-11-12, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Canva served the Singapore region (prices in S$). Nothing was signed into, created, submitted or paid for; the auth card was measured and its email step revealed, never completed; the Sign up, trial, checkout and OAuth actions were never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (39 components, 102 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (102 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png), [tools](screenshots/home-light-tools.png) |
| Pricing (Singapore region, S$) | `/pricing/` | [billing](screenshots/pricing-light-billing.png), [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Template categories | `/templates/` | [default](screenshots/templates-light-default.png), [full](screenshots/templates-light-full.png) |
| Presentation templates gallery | `/presentations/templates/` | [default](screenshots/templates-presentations-light-default.png), [full](screenshots/templates-presentations-light-full.png) |
| Presentations product page | `/presentations/` | [default](screenshots/presentations-light-default.png), [full](screenshots/presentations-light-full.png) |
| Docs product page | `/docs/` | [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png) |
| Whiteboards product page | `/whiteboard/` | [default](screenshots/whiteboard-light-default.png), [full](screenshots/whiteboard-light-full.png) |
| Design editor marketing ("create") | `/create/` | [default](screenshots/create-light-default.png), [full](screenshots/create-light-full.png) |
| Canva Pro | `/pro/` | [default](screenshots/pro-light-default.png), [full](screenshots/pro-light-full.png) |
| Features | `/features/` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| Log in card | `/login` | [default](screenshots/login-light-default.png) |
| Sign up card | `/signup` | [default](screenshots/signup-light-default.png) |
| Terms of use | `/policies/terms-of-use/` | [default](screenshots/terms-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Templates, phone | `/templates/` | [default](screenshots/mobile-templates-light-default.png), [full](screenshots/mobile-templates-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the header menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item), [m-signup](#mobile-sign-up) |
| Design mega-menu | every desktop page | the Design trigger's own click | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-flyout), [menu-link](#flyout-link) |
| Tools showcase tab | home | the Presentations tab's own click | [home-light-tools](screenshots/home-light-tools.png), [tool-tab](#tool-tab), [tool-panel](#tool-panel) |
| Billing switch | /pricing | the Monthly/Yearly switch's own toggle | [pricing-light-billing](screenshots/pricing-light-billing.png), [billing-switch](#billing-switch) |
| Cookie consent banner | every page | hidden, never answered (Accept all cookies / Manage cookies were never clicked) | hidden before every shot and reading |
| Email sign-in step | /login | Continue with email pressed once — a local UI step; the field was focused and given sample text that was deleted, never sent | [username-input](#email-field), [continue-button](#continue-button) |
| The editor and every signed-in surface | canva.com editor, Brand Kit, dashboards | behind sign-in; the auth card was measured, never used | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 20 components were given a real keyboard focus. 20 draw an outline ring: `nav-trigger` (2px auto #99c8ff `measured.focus-ring-dark`, offset -2px), `signup-cta` (1px auto #99c8ff `measured.focus-ring-dark`, offset 1px), `login-link` (1px auto #99c8ff `measured.focus-ring-dark`, offset 1px), `menu-link` (1px auto #005fcc `measured.focus-ring-light`, offset 1px), `hero-cta` (1px auto #99c8ff `measured.focus-ring-dark`, offset 0px), `tool-tab` (1px auto #005fcc `measured.focus-ring-light`, offset 3px), `feature-card` (on a child: 1px auto rgb(153, 200, 255) offset 1px), `explore-link` (1px auto #99c8ff `measured.focus-ring-dark`, offset 1px), `plan-tab` (on a child: 3px auto rgb(0, 95, 204) offset -1px), `billing-switch` (1px auto #005fcc `measured.focus-ring-light`, offset 2px), `plan-cta` (1px auto #005fcc `measured.focus-ring-light`, offset 3px), `feature-accordion` (1px auto #005fcc `measured.focus-ring-light`, offset 0px), `category-card` (3px auto #005fcc `measured.focus-ring-light`, offset -3px), `oauth-button` (1px auto #005fcc `measured.focus-ring-light`, offset 0px), `email-continue` (1px auto #005fcc `measured.focus-ring-light`, offset 0px), `continue-button` (1px auto #005fcc `measured.focus-ring-light`, offset 3px), `footer-link` (1px auto #005fcc `measured.focus-ring-light`, offset 1px), `social-icon` (1px auto #005fcc `measured.focus-ring-light`, offset 1px), `m-nav-item` (1px auto #e59700 `measured.focus-ring-mobile`, offset 0px), `m-signup` (1px auto #e59700 `measured.focus-ring-mobile`, offset 1px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.07s | `ease` | transform | continue-button, email-continue, explore-link, footer-link, hero-cta, login-link, m-menu-button, m-nav-item and more |
| 0.1s | `linear` | background-color, border-color, box-shadow, color | continue-button, email-continue, explore-link, footer-link, hero-cta, login-link, m-menu-button, m-nav-item and more |
| 0.2s | `linear` | background-color | billing-switch |
| 0.25s | `ease-in-out` | height | tool-panel |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 262 x 353 | - | - | transparent | none | 0 |
| [Feature card](#feature-card) | 850.66 x 166 | - | - | transparent | none | 32px 32px 0px 32px |
| [Auth card](#auth-card) | 304 x 348 | - | - | transparent | none | 0 |
| [Category card](#category-card) | 240 x 80 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The header on the dark home band: the Canva wordmark, the Design / Product / Plans / Business / Education / Help flyout triggers, and the Sign up / Log in actions. The Design trigger opens a mega-menu with four link columns.

#### Header
The dark header bar (.theme.dark): the Canva logo, the Design/Product/Plans/Business/Education/Help flyout triggers and the Sign up / Log in actions. Read as `header` on the home page.

**Values (default).** size 1440 x 80; background transparent; text Canva Sans 14/22 500, rgba(255, 255, 255, 0.898); layers button 0.0x0.0 rgba(255, 255, 255, 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px inset 10px; button.n156ng 62.1x32.0 rgba(255, 255, 255, 0) 12px; button.n156ng 70.5x32.0 rgba(255, 255, 255, 0) 12px; button.n156ng 52.9x32.0 rgba(255, 255, 255, 0) 12px; button.n156ng 75.9x32.0 rgba(255, 255, 255, 0) 12px; button.n156ng 84.8x32.0 rgba(255, 255, 255, 0) 12px.

Child layers that carry the look: button 0x0 background rgba(255, 255, 255, 0) radius 10px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px inset; button 62.1x32 background rgba(255, 255, 255, 0) radius 12px; button 70.5x32 background rgba(255, 255, 255, 0) radius 12px.

![Header default](components/crops/header-default.png)

#### Logo
The "Canva home" wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 90 x 32; background transparent; text Times 10/normal 400, #000000.

![Logo default](components/crops/logo-default.png)

#### Nav trigger
The Design button that opens the header mega-menu; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 62.13 x 32; padding 4px 8px; radius 12px; background rgba(255, 255, 255, 0); text Canva Sans 14/22 500, rgba(255, 255, 255, 0.898); transition background-color 0.1s linear, border-color 0.1s linear, color 0.1s linear |
| hover | background rgba(163, 112, 252, 0.2); text Canva Sans 14/22 500, #ffffff `color.neutral.white` |
| focus-visible | outline 2px auto #99c8ff `measured.focus-ring-dark`, offset -2px |
| pressed | background rgba(255, 255, 255, 0.15) |

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Sign-up action
The header Sign up action (the purple pill); measured, never followed. Read as `signup-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 74 x 32; padding 0px 12px; radius 10px; background rgba(255, 255, 255, 0); shadow rgba(255, 255, 255, 0.2) 0px 0px 0px 1px inset; text Canva Sans 14/22 500, #ffffff `color.neutral.white`; transition background-color 0.1s linear, box-shadow 0.1s linear, color 0.1s linear, transform 0.07s ease |
| hover | background rgba(255, 255, 255, 0.07) |
| focus-visible | outline 1px auto #99c8ff `measured.focus-ring-dark`, offset 1px |
| pressed | background rgba(255, 255, 255, 0.15) |

![Sign-up action default](components/crops/signup-cta-default.png) ![Sign-up action hover](components/crops/signup-cta-hover.png) ![Sign-up action focus-visible](components/crops/signup-cta-focus-visible.png) ![Sign-up action pressed](components/crops/signup-cta-pressed.png)

#### Log-in action
The header Log in action; measured, never followed. Read as `login-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 64.42 x 32; padding 0px 12px; radius 10px; background rgba(255, 255, 255, 0.898); shadow rgba(255, 255, 255, 0.08) 0px 24px 24px -18px inset, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px inset, rgba(0, 0, 0, 0.25) 0px -1px 0.5px 0px inset, rgba(0, 0, 0, 0.14) 0px 1px 2px 0px, rgba(0, 0, 0, 0.07) 0px 3px 4px 0px; text Canva Sans 14/22 500, #0f1015 `color.neutral.ink`; transition background-color 0.1s linear, box-shadow 0.1s linear, color 0.1s linear, transform 0.07s ease |
| hover | background #ffffff `color.neutral.white` |
| focus-visible | outline 1px auto #99c8ff `measured.focus-ring-dark`, offset 1px |
| pressed | size 63.78 x 31.68; background rgba(255, 255, 255, 0.8); transform scale(0.99) |

![Log-in action default](components/crops/login-link-default.png) ![Log-in action hover](components/crops/login-link-hover.png) ![Log-in action focus-visible](components/crops/login-link-focus-visible.png) ![Log-in action pressed](components/crops/login-link-pressed.png)

#### Nav flyout
The Design mega-menu panel (Digital design / Print design / Images / Videos columns), opened by its own trigger. Read as `nav-dropdown` on the home page.

**Values (default).** size 870 x 478; background transparent; text Canva Sans 14/22 400, rgba(16, 18, 25, 0.698) `color.neutral.muted`; layers div.M7FgEA 216.0x478.0 rgb(255, 255, 255) 32px 0px 0px 32px; a.Yx3HJA 200.0x38.0 rgba(15, 16, 21, 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px inset 12px; a.Yx3HJA 200.0x38.0 rgba(15, 16, 21, 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px inset 12px; a.Yx3HJA 200.0x38.0 rgba(15, 16, 21, 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0p.

Child layers that carry the look: div 216x478 background #ffffff `color.neutral.white` radius 32px 0px 0px 32px; a 200x38 background rgba(15, 16, 21, 0) radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px inset; a 200x38 background rgba(15, 16, 21, 0) radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px inset.

![Nav flyout default](components/crops/nav-dropdown-default.png)

#### Flyout link
A link inside the opened Design flyout. Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 200 x 38; padding 4px 12px; radius 12px; background rgba(15, 16, 21, 0); text Canva Sans 14/22 500, #0f1015 `color.neutral.ink`; transition background-color 0.1s linear, box-shadow 0.1s linear, color 0.1s linear, transform 0.07s ease |
| hover | background rgba(64, 79, 109, 0.06) `color.neutral.wash-hover` |
| focus-visible | background rgba(64, 79, 109, 0.06) `color.neutral.wash-hover`; outline 1px auto #005fcc `measured.focus-ring-light`, offset 1px |
| pressed | background rgba(57, 70, 96, 0.14) `color.neutral.wash-pressed`; outline 1px auto #005fcc `measured.focus-ring-light`, offset 1px |

![Flyout link default](components/crops/menu-link-default.png) ![Flyout link hover](components/crops/menu-link-hover.png) ![Flyout link focus-visible](components/crops/menu-link-focus-visible.png) ![Flyout link pressed](components/crops/menu-link-pressed.png)

### Home

The gradient hero with the 80px "What will you design today?" display and the Start designing CTA, the tools showcase (AI / Presentations / Social / Video / Print Shop tabs over a media panel), then light sections with dark feature cards.

#### Hero headline
The "What will you design today?" headline, white on the gradient hero band. Read as `hero-title` on the home page.

**Values (default).** size 1044.42 x 88; background transparent; text Canva Sans 80/88 400, #ffffff `color.neutral.white`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede under the headline on the gradient hero. Read as `hero-sub` on the home page.

**Values (default).** size 866.11 x 33.59; background transparent; text Canva Sans 24/33.6 400, rgba(255, 255, 255, 0.898).

![Hero copy default](components/crops/hero-sub-default.png)

#### Hero CTA
The "Start designing" action on the dark hero; measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 192 x 56; padding 0px 20px; radius 20px; background rgba(255, 255, 255, 0.898); shadow rgba(255, 255, 255, 0.08) 0px 24px 24px -18px inset, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px inset, rgba(0, 0, 0, 0.25) 0px -1px 0.5px 0px inset, rgba(0, 0, 0, 0.14) 0px 1px 2px 0px, rgba(0, 0, 0, 0.07) 0px 3px 4px 0px; text Canva Sans 16/22 600, #0f1015 `color.neutral.ink`; transition background-color 0.1s linear, box-shadow 0.1s linear, color 0.1s linear, transform 0.07s ease |
| hover | background #ffffff `color.neutral.white` |
| focus-visible | outline 1px auto #99c8ff `measured.focus-ring-dark`, offset 0px |
| pressed | size 190.08 x 55.44; background rgba(255, 255, 255, 0.8); transform scale(0.99) |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Tool tab
A tools-showcase tab (AI / Presentations / Social / Video / Print Shop); measured unselected — the selected state is the screenshot toggle. Read as `tool-tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 213.53 x 64; padding 16px 24px; radius 9999px; background transparent; text Canva Sans 18/24 600, #0f1015 `color.neutral.ink`; icon 40 x 40, #ff6105 |
| hover | background rgba(64, 79, 109, 0.06) `color.neutral.wash-hover` |
| focus-visible | image linear-gradient(98deg, #00c4cc -9%, #5a32fa 78%, #7630d7 `color.brand.purple-hover` 158%); outline 1px auto #005fcc `measured.focus-ring-light`, offset 3px; text Canva Sans 18/24 600, #ffffff `color.neutral.white`; icon 40 x 40, #ffffff `color.neutral.white` |
| pressed | background rgba(64, 79, 109, 0.06) `color.neutral.wash-hover`; image linear-gradient(98deg, #00c4cc -9%, #5a32fa 78%, #7630d7 `color.brand.purple-hover` 158%); text Canva Sans 18/24 600, #ffffff `color.neutral.white`; icon 40 x 40, #ffffff `color.neutral.white` |

![Tool tab default](components/crops/tool-tab-default.png) ![Tool tab hover](components/crops/tool-tab-hover.png) ![Tool tab focus-visible](components/crops/tool-tab-focus-visible.png) ![Tool tab pressed](components/crops/tool-tab-pressed.png)

#### Tool panel
The tools-showcase panel under the tabs (the selected tool's artwork and copy). Read as `tool-panel` on the home page.

**Values (default).** size 1332 x 1063.5; background transparent; text Canva Sans 28/35 500, #ffffff `color.neutral.white`; transition height 0.25s ease-in-out; layers div._3tJw4g 850.7x519.8; a 181.5x40.0 rgba(255, 255, 255, 0.898) rgba(255, 255, 255, 0.08) 0px 24px 24px -18px inset, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px inset, rgba(0, 0, 0, 0.25) 0px -1px 0.5px 0px inset, rgba(0, 0, 0, 0.14) 0px 1px 2px 0px, rgba(0, 0, 0, 0.07) 0px 3px 4px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px inset 12px; div._3tJw4g 413.3x519.8; a 155.8x40.0 rgba(255, 255, 255, 0.898) r.

Child layers that carry the look: div 850.7x519.8 image linear-gradient(#f25e07 0%, #d97218 28%, #ffc94f 100%); a 181.5x40 background rgba(255, 255, 255, 0.898) radius 12px shadow rgba(255, 255, 255, 0.08) 0px 24px 24px -18px inset, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px inset, rgba(0, 0, 0, 0.25) 0px -1px 0.5px 0px inset, rgba(0, 0, 0, 0.14) 0px 1px 2px 0px, rgba(0, 0, 0, 0.07) 0px 3px 4px 0px, transparent 0px 0px 0px 0px inset; div 413.3x519.8 image linear-gradient(#ffdac4 0%, #ffdac4 0%).

![Tool panel default](components/crops/tool-panel-default.png)

#### Feature card
A dark feature card on the home page (the Magic-Layers card with an "Explore" link); the link was measured, never followed. Read as `feature-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 850.66 x 166; padding 32px 32px 0px 32px; background transparent; text Canva Sans 28/35 500, #ffffff `color.neutral.white`; layers a 175.3x40.0 rgba(255, 255, 255, 0.898) rgba(255, 255, 255, 0.08) 0px 24px 24px -18px inset, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px inset, rgba(0, 0, 0, 0.25) 0px -1px 0.5px 0px inset, rgba(0, 0, 0, 0.14) 0px 1px 2px 0px, rgba(0, 0, 0, 0.07) 0px 3px 4px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px inset 12px |
| focus-visible | layers a 175.3x40.0 rgba(255, 255, 255, 0.898) rgba(255, 255, 255, 0.08) 0px 24px 24px -18px inset, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px inset, rgba(0, 0, 0, 0.25) 0px -1px 0.5px 0px inset, rgba(0, 0, 0, 0.14) 0px 1px 2px 0px, rgba(0, 0, 0, 0.07) 0px 3px 4px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px inset 1px auto rgb(153, 200, 255) offset 1px 12px |

Child layers that carry the look: a 175.3x40 background rgba(255, 255, 255, 0.898) radius 12px shadow rgba(255, 255, 255, 0.08) 0px 24px 24px -18px inset, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px inset, rgba(0, 0, 0, 0.25) 0px -1px 0.5px 0px inset, rgba(0, 0, 0, 0.14) 0px 1px 2px 0px, rgba(0, 0, 0, 0.07) 0px 3px 4px 0px, transparent 0px 0px 0px 0px inset.

![Feature card default](components/crops/feature-card-default.png) ![Feature card hover](components/crops/feature-card-hover.png) ![Feature card focus-visible](components/crops/feature-card-focus-visible.png) ![Feature card pressed](components/crops/feature-card-pressed.png)

#### Explore link
An "Explore X" link inside a dark feature card; measured, never followed. Read as `explore-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 175.28 x 40; padding 0px 16px; radius 12px; background rgba(255, 255, 255, 0.898); shadow rgba(255, 255, 255, 0.08) 0px 24px 24px -18px inset, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px inset, rgba(0, 0, 0, 0.25) 0px -1px 0.5px 0px inset, rgba(0, 0, 0, 0.14) 0px 1px 2px 0px, rgba(0, 0, 0, 0.07) 0px 3px 4px 0px; text Canva Sans 14/22 600, #0f1015 `color.neutral.ink`; transition background-color 0.1s linear, box-shadow 0.1s linear, color 0.1s linear, transform 0.07s ease |
| hover | background #ffffff `color.neutral.white` |
| focus-visible | outline 1px auto #99c8ff `measured.focus-ring-dark`, offset 1px |
| pressed | size 173.53 x 39.6; background rgba(255, 255, 255, 0.8); transform scale(0.99) |

![Explore link default](components/crops/explore-link-default.png) ![Explore link hover](components/crops/explore-link-hover.png) ![Explore link focus-visible](components/crops/explore-link-focus-visible.png) ![Explore link pressed](components/crops/explore-link-pressed.png)

#### Section heading
A section heading below the dark band (the light part of the page). Read as `section-h2` on the home page.

**Values (default).** size 1288 x 61.59; background transparent; text Canva Sans 56/61.6 400, #0f1015 `color.neutral.ink`.

![Section heading default](components/crops/section-h2-default.png)

### Pricing

The /pricing surface served in Singapore dollars: the audience tabs (Individuals and business / Education), the Monthly/Yearly switch, the Free / Pro / Business / Enterprise cards and the feature-comparison rows.

#### Pricing title
The "Plans and pricing" display heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 1376 x 70.41; background transparent; text Canva Sans 64/70.4 400, #0f1015 `color.neutral.ink`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Plan tab
A plan-audience tab (Individuals and business / Education); keyboard focus auto-activates it, which swaps the pricing view — measured last so the tab switch cannot contaminate the other components. Read as `plan-tab` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 142.08 x 64; background transparent; text Canva Sans 16/24 400, #0f1015 `color.neutral.ink`; layers div::before.MRLK3w._LBjXA 142.078pxx48px 9999px; div::after.MRLK3w._LBjXA 142.078pxx48px rgba(57, 70, 96, 0.14) 9999px; div::before.MRLK3w._LBjXA 142.078pxx48px 9999px; div::after.MRLK3w._LBjXA 142.078pxx48px rgba(57, 70, 96, 0.14) 9999px |
| focus-visible | size 143.05 x 64; text Canva Sans 16/24 600, #ffffff `color.neutral.white`; layers span 151.0x64.0 3px auto rgb(0, 95, 204) offset -1px 8px; div::before.MRLK3w.IpBcsg 143.047pxx48px 9999px; div::after.MRLK3w.IpBcsg 143.047pxx48px rgba(57, 70, 96, 0.14) 9999px; div::before.MRLK3w.IpBcsg 143.047pxx48px 9999px; div::after.MRLK3w.IpBcsg 143.047pxx48px rgba(57, 70, 96, 0.14) 9999px |
| pressed | size 143.05 x 64; text Canva Sans 16/24 600, #ffffff `color.neutral.white`; layers div::before.MRLK3w.IpBcsg 143.047pxx48px 9999px; div::after.MRLK3w.IpBcsg 143.047pxx48px rgba(57, 70, 96, 0.14) 9999px; div::before.MRLK3w.IpBcsg 143.047pxx48px 9999px; div::after.MRLK3w.IpBcsg 143.047pxx48px rgba(57, 70, 96, 0.14) 9999px |

Child layers that carry the look: div::before 142.078pxx48px image linear-gradient(90deg, #476cdc, #7e2be8) radius 9999px; div::after 142.078pxx48px background rgba(57, 70, 96, 0.14) `color.neutral.wash-pressed` radius 9999px; div::before 142.078pxx48px image linear-gradient(90deg, #476cdc, #7e2be8) radius 9999px.

![Plan tab default](components/crops/plan-tab-default.png) ![Plan tab hover](components/crops/plan-tab-hover.png) ![Plan tab focus-visible](components/crops/plan-tab-focus-visible.png) ![Plan tab pressed](components/crops/plan-tab-pressed.png)

#### Billing switch
The Monthly/Yearly billing switch next to "Save from 16%"; toggled for the billing screenshot, never checked out. Read as `billing-switch` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 24; padding 2px; radius 9999px; background #8b3dff `color.brand.purple`; text Arial 13.33/normal 400, #0f1015 `color.neutral.ink`; transition background-color 0.2s linear; icon 12 x 12, #8b3dff `color.brand.purple` |
| hover | background #7630d7 `color.brand.purple-hover` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 2px |
| pressed | background #7630d7 `color.brand.purple-hover` |

![Billing switch default](components/crops/billing-switch-default.png) ![Billing switch hover](components/crops/billing-switch-hover.png) ![Billing switch focus-visible](components/crops/billing-switch-focus-visible.png) ![Billing switch pressed](components/crops/billing-switch-pressed.png)

#### Plan card
A pricing plan card (plan name, price in S$ — the capture was served the Singapore region — and its action). Read as `plan-card` on the pricing page.

**Values (default).** size 262 x 353; background transparent; text Canva Sans 12/20 600, rgba(16, 18, 25, 0.698) `color.neutral.muted`; icon 16 x 16, rgba(16, 18, 25, 0.698) `color.neutral.muted`; layers button 262.0x40.0 rgb(139, 61, 255) rgba(255, 255, 255, 0.16) 0px 24px 24px -18px inset, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px inset, rgba(21, 30, 130, 0.12) 0px -1px 0.5px 0px inset, rgba(21, 30, 130, 0.07) 0px 1px 2px 0px, rgba(21, 30, 130, 0.03) 0px 3px 4px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px inset 12px.

Child layers that carry the look: button 262x40 background #8b3dff `color.brand.purple` radius 12px shadow rgba(255, 255, 255, 0.16) 0px 24px 24px -18px inset, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px inset, rgba(21, 30, 130, 0.12) 0px -1px 0.5px 0px inset, rgba(21, 30, 130, 0.07) 0px 1px 2px 0px, rgba(21, 30, 130, 0.03) 0px 3px 4px 0px, transparent 0px 0px 0px 0px inset.

![Plan card default](components/crops/plan-card-default.png)

#### Plan price
A plan card's price figure (S$ in the Singapore region the capture was served). Read as `plan-price` on the pricing page.

**Values (default).** size 63.44 x 49; background transparent; text Canva Sans 28.8/normal 500, #0f1015 `color.neutral.ink`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan card's action (Get started / Try for free / Start a free trial); measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 262 x 40; padding 0px 16px; radius 12px; background #8b3dff `color.brand.purple`; shadow rgba(255, 255, 255, 0.16) 0px 24px 24px -18px inset, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px inset, rgba(21, 30, 130, 0.12) 0px -1px 0.5px 0px inset, rgba(21, 30, 130, 0.07) 0px 1px 2px 0px, rgba(21, 30, 130, 0.03) 0px 3px 4px 0px; text Canva Sans 14/22 600, #ffffff `color.neutral.white`; transition background-color 0.1s linear, box-shadow 0.1s linear, color 0.1s linear, transform 0.07s ease |
| hover | background #7630d7 `color.brand.purple-hover` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 3px |
| pressed | size 259.38 x 39.6; background #612dae `color.brand.purple-pressed`; transform scale(0.99) |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Feature row
A feature-comparison row in the plan table; measured closed, never expanded. Read as `feature-accordion` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1286 x 64; radius 14px 14px 0px 0px; background rgba(57, 70, 96, 0.14) `color.neutral.wash-pressed`; text Canva Sans 18/24 600, #0f1015 `color.neutral.ink`; icon 24 x 24, #0d1216 |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 0px |

![Feature row default](components/crops/feature-accordion-default.png) ![Feature row hover](components/crops/feature-accordion-hover.png) ![Feature row focus-visible](components/crops/feature-accordion-focus-visible.png) ![Feature row pressed](components/crops/feature-accordion-pressed.png)

### Templates

The /templates gallery: the Free templates title, the template-search field and the category cards.

#### Templates title
The "Free templates" display heading. Read as `templates-h1` on the templates page.

**Values (default).** size 565.23 x 79.19; background transparent; text Canva Sans 64/70.4 400, #0f1015 `color.neutral.ink`; layers div.su2OzQ._8P8IGw 61.3x61.3 T:1px solid rgba(255, 255, 255, 0.5) / R:1px solid rgba(255, 255, 255, 0.5) / B:1px solid rgba(255, 255, 255, 0.5) / L:1px solid rgba(255, 255, 255, 0.5) rgba(24, 44, 89, 0.07) 0px 0px 0px 0.5px 12px; div.su2OzQ.KCtSjQ 61.3x61.3 T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255) rgba(24, 44,.

Child layers that carry the look: div 61.3x61.3 image linear-gradient(#c23dcf, #63046c) border 1px solid rgba(255, 255, 255, 0.5) radius 12px shadow rgba(24, 44, 89, 0.07) 0px 0px 0px 0.5px; div 61.3x61.3 image linear-gradient(#a21caf 0%, #63046c 100%) border 1px solid #ffffff `color.neutral.white` radius 12px shadow rgba(24, 44, 89, 0.07) 0px 0px 0px 0.5px.

![Templates title default](components/crops/templates-h1-default.png)

#### Search field
The "Search templates" input; focused only — typing was never sent so no live query ran. Read as `search-field` on the templates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 323 x 46; padding 0px 0px 1px 0px; background rgba(255, 255, 255, 0); text Canva Sans 14/22 400, #0f1015 `color.neutral.ink`; placeholder rgba(19, 22, 32, 0.6) `color.neutral.scrim` |

![Search field default](components/crops/search-field-default.png) ![Search field focused](components/crops/search-field-focused.png)

#### Category card
A template-category card (image tile + label linking /presentations/templates/ etc.); measured, never followed. Read as `category-card` on the templates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 240 x 80; background transparent; text Times 10/normal 400, #0000ee |
| focus-visible | radius 16px; outline 3px auto #005fcc `measured.focus-ring-light`, offset -3px; layers a 240.0x80.0 3px auto rgb(0, 95, 204) offset -3px 16px |
| pressed | text Times 10/normal 400, #ff0000 |

![Category card default](components/crops/category-card-default.png) ![Category card hover](components/crops/category-card-hover.png) ![Category card focus-visible](components/crops/category-card-focus-visible.png) ![Category card pressed](components/crops/category-card-pressed.png)

### Login and signup

The /login card over the template collage: Google / Facebook / email / another-way actions and the terms line. Continue with email was pressed once to reveal the username field — focused and given sample text that was deleted again, never sent.

#### Auth card
The sign-in card (Continue with Google / Facebook / email / another way + terms); captured, never used. Read as `auth-card` on the login page.

**Values (default).** size 304 x 348; background transparent; text Canva Sans 24/32 600, #0f1015 `color.neutral.ink`; icon 24 x 24, #0f1015 `color.neutral.ink`; layers button.w_WokQ._7IvJg 304.0x40.0 rgba(15, 16, 21, 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(53, 65, 90, 0.2) 0px 0px 0px 1px inset 12px; button.HvfyOw._7IvJg 304.0x40.0 rgba(15, 16, 21, 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(53, 65, 90, 0.2) 0px 0px 0px 1px inset 12px; button.COAWQQ._7IvJg 304.0x40.0 rgba(15, 16, 21, 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(53, 65, 90, 0.2) 0px 0px 0px 1px inse.

Child layers that carry the look: button 304x40 background rgba(15, 16, 21, 0) radius 12px shadow transparent 0px 0px 0px 0px, rgba(53, 65, 90, 0.2) `color.neutral.hairline` 0px 0px 0px 1px inset; button 304x40 background rgba(15, 16, 21, 0) radius 12px shadow transparent 0px 0px 0px 0px, rgba(53, 65, 90, 0.2) `color.neutral.hairline` 0px 0px 0px 1px inset; button 304x40 background rgba(15, 16, 21, 0) radius 12px shadow transparent 0px 0px 0px 0px, rgba(53, 65, 90, 0.2) `color.neutral.hairline` 0px 0px 0px 1px inset.

![Auth card default](components/crops/auth-card-default.png)

#### OAuth button
The "Continue with Google" action; measured, never pressed — it would leave for the OAuth flow. Read as `oauth-button` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 304 x 40; padding 0px 8px; radius 12px; background rgba(15, 16, 21, 0); shadow rgba(53, 65, 90, 0.2) 0px 0px 0px 1px inset; text Canva Sans 14/22 600, #0f1015 `color.neutral.ink`; transition background-color 0.1s linear, box-shadow 0.1s linear, color 0.1s linear, transform 0.07s ease; icon 24 x 24, #0f1015 `color.neutral.ink` |
| hover | background rgba(64, 79, 109, 0.06) `color.neutral.wash-hover` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 0px |
| pressed | background rgba(57, 70, 96, 0.14) `color.neutral.wash-pressed` |

![OAuth button default](components/crops/oauth-button-default.png) ![OAuth button hover](components/crops/oauth-button-hover.png) ![OAuth button focus-visible](components/crops/oauth-button-focus-visible.png) ![OAuth button pressed](components/crops/oauth-button-pressed.png)

#### Email continue
The "Continue with email" action that reveals the email form; pressed once below to open that form (a local step, still signed out). Read as `email-continue` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 304 x 40; padding 0px 8px; radius 12px; background rgba(15, 16, 21, 0); shadow rgba(53, 65, 90, 0.2) 0px 0px 0px 1px inset; text Canva Sans 14/22 600, #0f1015 `color.neutral.ink`; transition background-color 0.1s linear, box-shadow 0.1s linear, color 0.1s linear, transform 0.07s ease; icon 24 x 24, #0f1015 `color.neutral.ink` |
| hover | background rgba(64, 79, 109, 0.06) `color.neutral.wash-hover` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 0px |
| pressed | background rgba(57, 70, 96, 0.14) `color.neutral.wash-pressed` |

![Email continue default](components/crops/email-continue-default.png) ![Email continue hover](components/crops/email-continue-hover.png) ![Email continue focus-visible](components/crops/email-continue-focus-visible.png) ![Email continue pressed](components/crops/email-continue-pressed.png)

#### Email field
The email/username input revealed by "Continue with email"; focused and given sample text that was deleted again — nothing sent. Read as `username-input` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 278 x 38; padding 0px 0px 1px 0px; background rgba(255, 255, 255, 0); text Canva Sans 14/22 400, #0f1015 `color.neutral.ink`; placeholder #0f1015 `color.neutral.ink` |

![Email field default](components/crops/username-input-default.png) ![Email field focused](components/crops/username-input-focused.png) ![Email field filled](components/crops/username-input-filled.png)

#### Continue button
The email form's Continue action; measured, never pressed. Read as `continue-button` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 304 x 40; padding 0px 16px; radius 12px; background #8b3dff `color.brand.purple`; shadow rgba(255, 255, 255, 0.16) 0px 24px 24px -18px inset, rgba(255, 255, 255, 0.25) 0px 1px 0.5px 0px inset, rgba(21, 30, 130, 0.12) 0px -1px 0.5px 0px inset, rgba(21, 30, 130, 0.07) 0px 1px 2px 0px, rgba(21, 30, 130, 0.03) 0px 3px 4px 0px; text Canva Sans 14/22 600, #ffffff `color.neutral.white`; transition background-color 0.1s linear, box-shadow 0.1s linear, color 0.1s linear, transform 0.07s ease |
| hover | background #7630d7 `color.brand.purple-hover` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 3px |
| pressed | size 300.96 x 39.6; background #612dae `color.brand.purple-pressed`; transform scale(0.99) |

![Continue button default](components/crops/continue-button-default.png) ![Continue button hover](components/crops/continue-button-hover.png) ![Continue button focus-visible](components/crops/continue-button-focus-visible.png) ![Continue button pressed](components/crops/continue-button-pressed.png)

### Footer

The light footer: download links, the Product / Plans / About columns, social icons and legal.

#### Footer
The footer: download links, the Product/Plans/About columns, social icons and legal. Read as `footer` on the home page.

**Values (default).** size 1440 x 1420; padding 48px 0px 0px 0px; background transparent; image linear-gradient(transparent, #f6f7f8 `color.neutral.footer-fade`); text Canva Sans 16/22.4 500, rgba(15, 16, 21, 0.85).

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 93.47 x 40; padding 0px 16px; radius 12px; background rgba(15, 16, 21, 0); shadow rgba(53, 65, 90, 0.2) 0px 0px 0px 1px inset; text Canva Sans 14/22 600, #0f1015 `color.neutral.ink`; transition background-color 0.1s linear, box-shadow 0.1s linear, color 0.1s linear, transform 0.07s ease |
| hover | background rgba(64, 79, 109, 0.06) `color.neutral.wash-hover` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 1px |
| pressed | background rgba(57, 70, 96, 0.14) `color.neutral.wash-pressed` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A social link in the footer. Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; padding 0px 8px; radius 10px; background rgba(15, 16, 21, 0); text Canva Sans 14/22 600, #0f1015 `color.neutral.ink`; transition background-color 0.1s linear, box-shadow 0.1s linear, color 0.1s linear, transform 0.07s ease; icon 24 x 24, #0f1015 `color.neutral.ink` |
| hover | background rgba(64, 79, 109, 0.06) `color.neutral.wash-hover` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-light`, offset 1px |
| pressed | background rgba(57, 70, 96, 0.14) `color.neutral.wash-pressed` |

![Social link default](components/crops/social-icon-default.png) ![Social link hover](components/crops/social-icon-hover.png) ![Social link focus-visible](components/crops/social-icon-focus-visible.png) ![Social link pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The same surface at phone width: the header shrinks to logo + burger, the menu opens as a full panel with nav rows and the auth actions.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 80; background transparent; text Canva Sans 14/22 500, #0f1015 `color.neutral.ink`; icon 24 x 24, #ffffff `color.neutral.white`; layers button 32.0x32.0 rgba(255, 255, 255, 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px inset 10px; button.n156ng 0.0x0.0 rgba(255, 255, 255, 0) 12px; button.n156ng 0.0x0.0 rgba(255, 255, 255, 0) 12px; button.n156ng 0.0x0.0 rgba(255, 255, 255, 0) 12px; button.n156ng 0.0x0.0 rgba(255, 255, 255, 0) 12px; button.n156ng 0.0x0.0 rgba(255, 255, 255, 0) 12px.

Child layers that carry the look: button 32x32 background rgba(255, 255, 255, 0) radius 10px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px inset; button 0x0 background rgba(255, 255, 255, 0) radius 12px; button 0x0 background rgba(255, 255, 255, 0) radius 12px.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The "Open navigation menu" burger toggle. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 32 x 32; padding 0px 8px; radius 10px; background rgba(255, 255, 255, 0); text Canva Sans 14/22 600, #ffffff `color.neutral.white`; transition background-color 0.1s linear, box-shadow 0.1s linear, color 0.1s linear, transform 0.07s ease; icon 24 x 24, #ffffff `color.neutral.white`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The opened mobile navigation panel (the fixed overlay holding the menu links and the auth actions). Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; background transparent; text Canva Sans 21/26 500, #0f1015 `color.neutral.ink`; icon 24 x 24, #0f1015 `color.neutral.ink`; layers ::after rgba(0, 0, 0, 0) 0px none 1; div._aTIuw 346.0x844.0 rgb(255, 255, 255) rgba(64, 79, 109, 0.06) 0px 0px 0px 0.5px, rgba(21, 30, 130, 0.12) 0px 8px 16px 0px, rgba(21, 30, 130, 0.06) 0px 24px 24px 0px; div.cLOwww 346.0x144.0 rgb(204, 225, 255); div._46qB5w 346.0x144.0 rgb(231, 219, 255); div._6Tlurw 346.0x144.0 rgb(255, 255, 255); button 32.0x32.0 rgba(15, 16, 21, 0) rgba(0, 0, 0, 0) 0px 0px .

Child layers that carry the look: div 346x844 background #ffffff `color.neutral.white` shadow rgba(64, 79, 109, 0.06) `color.neutral.wash-hover` 0px 0px 0px 0.5px, rgba(21, 30, 130, 0.12) 0px 8px 16px 0px, rgba(21, 30, 130, 0.06) 0px 24px 24px 0px; div 346x144 background #cce1ff; div 346x144 background #e7dbff.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
A row inside the opened mobile menu (Design / Product / Plans / Business / Education / Help). Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 322 x 42; padding 8px 12px; radius 12px; background rgba(15, 16, 21, 0); text Canva Sans 21/26 500, #0f1015 `color.neutral.ink`; transition background-color 0.1s linear, box-shadow 0.1s linear, color 0.1s linear, transform 0.07s ease; icon 21.61 x 24, #0f1015 `color.neutral.ink` |
| focus-visible | outline 1px auto #e59700 `measured.focus-ring-mobile`, offset 0px |
| pressed | background rgba(57, 70, 96, 0.14) `color.neutral.wash-pressed` |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile sign-up
The Sign up action inside the mobile menu; measured, never followed. Read as `m-signup` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 322 x 40; padding 0px 12px; radius 12px; background rgba(15, 16, 21, 0); shadow rgba(53, 65, 90, 0.2) 0px 0px 0px 1px inset; text Canva Sans 14/22 500, #0f1015 `color.neutral.ink`; transition background-color 0.1s linear, box-shadow 0.1s linear, color 0.1s linear, transform 0.07s ease |
| focus-visible | outline 1px auto #e59700 `measured.focus-ring-mobile`, offset 1px |
| pressed | background rgba(57, 70, 96, 0.14) `color.neutral.wash-pressed` |

![Mobile sign-up default](components/crops/m-signup-default.png) ![Mobile sign-up hover](components/crops/m-signup-hover.png) ![Mobile sign-up focus-visible](components/crops/m-signup-focus-visible.png) ![Mobile sign-up pressed](components/crops/m-signup-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 270 x 148.5; background transparent; text Canva Sans 45/49.5 400, #ffffff `color.neutral.white`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Canva wordmark and its teal-to-purple gradient mark, the Google/Facebook/email provider glyphs, the social glyphs and the template/tool artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Everything behind the auth card — the design editor, Brand Kit, dashboards, teams, billing and account surfaces — was never reached. /login and /signup show only the provider card; Continue with email reveals a username field that was measured and given sample text that was deleted again, and the Continue action was never pressed. What the editor, the Brand Kit and the dashboards look like or how they behave is not documented here — the marketing pages' claims about them were never verified.

### Pages

- **/solutions/brand-management/ returned 404** (Canva's generic not-found page): recorded as a boundary, not retried as a different URL.
- **Sign up, trial and checkout.** Sign up, Get started, Start a free trial, Contact Sales and Book a demo were measured or screenshotted, never followed; no account was created and no payment surface was reached.
- **OAuth providers.** Continue with Google / Facebook were measured, never pressed — they leave for the providers' flows.
- **Education pricing view.** Focusing the Education plan tab auto-activates it (ARIA automatic activation); the view switches to ?tab=education. That view was not separately captured — the plans grid components were measured on Individuals and business, the default.
- **External surfaces** (canva.com/help, the apps store, social profiles) are linked from the site but were never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **The mega-menu auto-closes** a few seconds after it opens; each flyout-child state re-opened it with the Design trigger before reading.
- **The Education tab's focus-visible state** shows the tab in its activated view — focusing it really does switch the page.

### Themes

The public surface paints light, with genuinely dark bands: the home header+hero sit inside `.theme.dark` and feature sections carry it too — painted dark surfaces, not a user toggle. The StyleX layer declares `.light`/`.dark` redeclarations of the same hashed variables; the export's "dark" set is the translucent-white state set the dark band paints.

### Fonts

- **Canva Sans** (400/500/600 seen on the surface) is served from static.canva.com; the @font-face blocks live in the cross-origin bundles (harvested src list in raw/css-vars.json). The style guide falls back to system sans — Canva's webfonts are licensed, not shipped.

### Screenshots

- The hero gradient band, the tool artwork, the template gallery imagery and the Canva wordmark in the screenshots are the product's published content. The hero's colour field is a painted media layer (a video/image element behind the hero), not a CSS value — no flat-colour token claims to be it.
- mobile-home's full-page capture hit the GPU texture cap and was stitched from two chunks; the second chunk's PNG came back 10px shorter than expected (a late layout settle) — kept, flagged in its sidecar.
- The capture was served the Singapore region: prices render S$ and the footer locale reads English (US) with Singapore content — a documented geo behaviour, not an error.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Template artwork, plan feature lists, marketing copy and the terms text are the product's content; only frames and components were measured.
