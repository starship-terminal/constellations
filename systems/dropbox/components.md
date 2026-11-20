# Dropbox components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from dropbox.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Prices render in US dollars in the region the capture was served. Nothing was signed into, created, submitted or paid for; the login and register cards were measured and their email fields given sample text that was deleted again, and the Continue, Get started, Try for free, Buy now and OAuth actions were never pressed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (53 components, 139 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (137 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light` (the dig-Theme-vis2023--bright scope; the declared vis2023--dark palette never paints signed out). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Dropbox product page | `/dropbox` | [default](screenshots/dropbox-light-default.png), [full](screenshots/dropbox-light-full.png) |
| Replay product page | `/replay` | [default](screenshots/replay-light-default.png), [full](screenshots/replay-light-full.png) |
| Dropbox Sign product page | `/sign` | [default](screenshots/sign-light-default.png), [full](screenshots/sign-light-full.png) |
| DocSend product page | `/docsend` | [default](screenshots/docsend-light-default.png), [full](screenshots/docsend-light-full.png) |
| Business landing | `/business` | [default](screenshots/business-light-default.png), [full](screenshots/business-light-full.png) |
| Enterprise landing | `/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| Plans and pricing | `/plans` | [default](screenshots/plans-light-default.png), [full](screenshots/plans-light-full.png), [monthly](screenshots/plans-light-monthly.png) |
| Features overview | `/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| Log-in card | `/login` | [default](screenshots/login-light-default.png) |
| Sign-up card | `/register` | [default](screenshots/register-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Plans, phone | `/plans` | [default](screenshots/mobile-plans-light-default.png), [full](screenshots/mobile-plans-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the hamburger button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item), [m-signup](#mobile-sign-up) |
| Products mega-menu | every desktop page | the Products trigger's own hover — a click toggles it closed again | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-mega-menu), [menu-link](#mega-menu-link) |
| Billing radio | /plans | the Billed-monthly radio label's own click (the page defaults to yearly) | [plans-light-monthly](screenshots/plans-light-monthly.png), [billing-radio](#billing-radio) |
| Privacy consent banner / Google One Tap | every page | hidden, never answered (no consent button was ever clicked) | hidden before every shot and reading |
| Auth email field | /login and /register | focused and given sample text that was deleted again — never sent | [email-field](#email-field), [register-email](#register-email-field), [continue-button](#continue-button) |
| The product and every signed-in surface | the Dropbox file dashboard, Paper, account and checkout flows | behind sign-in; the auth cards were measured, never used | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 25 components were given a real keyboard focus. 7 draw an outline ring: `hero-cta` (3px solid #ffffff `color.brand.coconut.200`, offset 3px), `transparent-btn` (3px solid #428bff `color.brand.utility.focusring`, offset 3px), `text-link` (3px solid #428bff `color.brand.utility.focusring`, offset 3px), `diff-toggle` (2px solid #0061fe `color.brand.status.attention.border.default`, offset 4px), `help-choose` (2px solid #0061fe `color.brand.status.attention.border.default`, offset 2px), `footer-link` (1px auto #005fcc, offset 1px), `social-icon` (1px auto #005fcc, offset 1px). 18 draw a focus ring as a shadow instead: `nav-trigger`, `nav-link`, `nav-contact`, `nav-signup`, `nav-login`, `nav-cta`, `icon-button`, `plan-cta`, `plan-cta-alt`, `plan-outline`, `biz-cta`, `sign-cta`, `sso-button`, `sso-button-alt`, `continue-button`, `register-cta`, `m-nav-item`, `m-signup`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.4, 0, 0.6, 1)` | background-color, border-color | biz-cta, continue-button, hero-cta, nav-cta, plan-cta, plan-cta-alt, plan-outline, register-cta and more |
| 0.125s | `linear` | background-color, color | m-nav-item, m-signup, menu-link, nav-contact, nav-link, nav-login, nav-signup, nav-trigger |
| 0.2s | `cubic-bezier(0.785, 0.135, 0.15, 0.86)` | max-height, opacity | nav-dropdown |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 416 x 1079.41 | - | 12px | #faf9f7 `color.brand.coconut.300` | none | 24px 48px 48px 48px |
| [Feature card](#feature-card) | 413.53 x 517.55 | - | - | transparent | none | 0px 24px |
| [Auth card](#auth-card) | 368 x 272.2 | - | - | transparent | none | 0 |
| [Register card](#register-card) | 368 x 272.2 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The sticky dwg-nav bar on the coconut theme: the Dropbox mark, the Products / Solutions flyout triggers, the Business / Pricing / Contact sales links, Get app, and Sign up / Log in / Get started. Products opens a mega-menu of product cards.

#### Header
The sticky dwg-nav bar (dwg-theme--coconut, z 120): the Dropbox mark, the Products / Solutions flyout triggers, the Business / Pricing / Contact sales links, the Get app trigger and Sign up / Log in / Get started. Read as `header` on the home page.

**Values (default).** size 1440 x 72; padding 16px 24px; background #ffffff `color.brand.coconut.200`; text Atlas Grotesk Web 14/20 500, #1e1919 `color.brand.graphite.default`; icon 32 x 27, #0000ee; layers ::after rgba(166, 145, 113, 0.2) 0px none 1.

![Header default](components/crops/header-default.png)

#### Logo
The Dropbox mark anchor in the nav. Read as `logo` on the home page.

**Values (default).** size 154.5 x 40; background transparent; text Times 16/normal 400, #0000ee; icon 32 x 27, #0000ee; layers span.dwg-nav-logo-button__glyph.dwg-nav-logo-button__glyph--updated 32.0x40.0 rgb(255, 255, 255).

Child layers that carry the look: span 32x40 background #ffffff `color.brand.coconut.200`.

![Logo default](components/crops/logo-default.png)

#### Nav trigger
The Products button that opens the mega-menu; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 105.48 x 72; padding 16px 12px; background transparent; text Atlas Grotesk Web 14/20 500, #1e1919 `color.brand.graphite.default`; transition color 0.125s linear; icon 16 x 16, rgba(82, 74, 62, 0.82) `color.brand.status.faint.text` |
| hover | text Atlas Grotesk Web 14/20 500, #0061fe `color.brand.status.attention.border.default`; icon 16 x 16, #0061fe `color.brand.status.attention.border.default` |
| focus-visible | shadow #428bff 0px 0px 0px 3px inset; layers button.dwg-nav-item-button.dwg-nav-item-button--nav-redesign 105.5x72.0 rgb(66, 139, 255) 0px 0px 0px 3px inset |
| pressed | text Atlas Grotesk Web 14/20 500, #0061fe `color.brand.status.attention.border.default`; icon 16 x 16, #0061fe `color.brand.status.attention.border.default` |

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav link
The Pricing link in the nav; measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 72.48 x 72; padding 16px 12px; background transparent; text Atlas Grotesk Web 14/20 500, #1e1919 `color.brand.graphite.default`; transition color 0.125s linear |
| hover | text Atlas Grotesk Web 14/20 500, #0061fe `color.brand.status.attention.border.default` |
| focus-visible | shadow #428bff 0px 0px 0px 3px inset; layers a.dwg-nav-item-button.dwg-nav-item-button--nav-redesign 72.5x72.0 rgb(66, 139, 255) 0px 0px 0px 3px inset |
| pressed | text Atlas Grotesk Web 14/20 500, #0061fe `color.brand.status.attention.border.default` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Nav contact link
The Contact sales link in the nav; measured, never followed. Read as `nav-contact` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 114.47 x 72; padding 16px 12px; background transparent; text Atlas Grotesk Web 14/20 400, #1e1919 `color.brand.graphite.default`; transition color 0.125s linear |
| hover | text Atlas Grotesk Web 14/20 400, #0061fe `color.brand.status.attention.border.default` |
| focus-visible | shadow #428bff 0px 0px 0px 3px inset; layers a.dwg-nav-item-button.dwg-nav-item-button--nav-redesign 114.5x72.0 rgb(66, 139, 255) 0px 0px 0px 3px inset |
| pressed | text Atlas Grotesk Web 14/20 400, #0061fe `color.brand.status.attention.border.default` |

![Nav contact link default](components/crops/nav-contact-default.png) ![Nav contact link hover](components/crops/nav-contact-hover.png) ![Nav contact link focus-visible](components/crops/nav-contact-focus-visible.png) ![Nav contact link pressed](components/crops/nav-contact-pressed.png)

#### Sign-up link
The header Sign up link; measured, never followed. Read as `nav-signup` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 75.83 x 72; padding 16px 12px; background transparent; text Atlas Grotesk Web 14/20 400, #1e1919 `color.brand.graphite.default`; transition color 0.125s linear |
| hover | text Atlas Grotesk Web 14/20 400, #0061fe `color.brand.status.attention.border.default` |
| focus-visible | shadow #428bff 0px 0px 0px 3px inset; layers a.dwg-nav-item-button.dwg-nav-item-button--nav-redesign 75.8x72.0 rgb(66, 139, 255) 0px 0px 0px 3px inset |
| pressed | text Atlas Grotesk Web 14/20 400, #0061fe `color.brand.status.attention.border.default` |

![Sign-up link default](components/crops/nav-signup-default.png) ![Sign-up link hover](components/crops/nav-signup-hover.png) ![Sign-up link focus-visible](components/crops/nav-signup-focus-visible.png) ![Sign-up link pressed](components/crops/nav-signup-pressed.png)

#### Log-in link
The header Log in link; measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 65.42 x 72; padding 16px 12px; background transparent; text Atlas Grotesk Web 14/20 400, #1e1919 `color.brand.graphite.default`; transition color 0.125s linear |
| hover | text Atlas Grotesk Web 14/20 400, #0061fe `color.brand.status.attention.border.default` |
| focus-visible | shadow #428bff 0px 0px 0px 3px inset; layers a.dwg-nav-item-button.dwg-nav-item-button--nav-redesign 65.4x72.0 rgb(66, 139, 255) 0px 0px 0px 3px inset |
| pressed | text Atlas Grotesk Web 14/20 400, #0061fe `color.brand.status.attention.border.default` |

![Log-in link default](components/crops/nav-login-default.png) ![Log-in link hover](components/crops/nav-login-hover.png) ![Log-in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log-in link pressed](components/crops/nav-login-pressed.png)

#### Get-started action
The header Get started action (the blue pill); measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 117.13 x 40; padding 0px 12px; border 2px solid #0061fe `color.brand.status.attention.border.default`; radius 12px; background #0061fe `color.brand.status.attention.border.default`; text Atlas Grotesk Web 16/19.2 500, #f7f5f2 `color.brand.status.faint.background`; transition background-color 0.1s cubic-bezier(0.4, 0, 0.6, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.6, 1) |
| hover | background #0057e5 `color.brand.button.primary.hover` |
| focus-visible | shadow #428bff 0px 0px 0px 3px |
| pressed | background #0050d0 `color.brand.button.primary.active` |

![Get-started action default](components/crops/nav-cta-default.png) ![Get-started action hover](components/crops/nav-cta-hover.png) ![Get-started action focus-visible](components/crops/nav-cta-focus-visible.png) ![Get-started action pressed](components/crops/nav-cta-pressed.png)

#### Nav mega-menu
The Products mega-menu panel (Dropbox / Replay / Sign / Reclaim.ai / Dash / DocSend / Early access), opened by its own trigger. Read as `nav-dropdown` on the home page.

**Values (default).** size 480 x 400; background transparent; text Atlas Grotesk Web 16/20 500, #1e1919 `color.brand.graphite.default`; transition max-height 0.2s cubic-bezier(0.785, 0.135, 0.15, 0.86), opacity 0.2s cubic-bezier(0.785, 0.135, 0.15, 0.86); transform translate(0px, 72px).

![Nav mega-menu default](components/crops/nav-dropdown-default.png)

#### Mega-menu link
A product link inside the opened Products mega-menu (pointer-driven; the menu closes on keyboard focus). Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 240 x 92; padding 16px; radius 12px; background transparent; text Atlas Grotesk Web 16/20 500, #1e1919 `color.brand.graphite.default`; transition background-color 0.125s linear, color 0.125s linear |
| hover | background rgba(167, 146, 114, 0.14) `measured.menu-hover-wash`; text Atlas Grotesk Web 16/20 500, #0061fe `color.brand.status.attention.border.default` |

![Mega-menu link default](components/crops/menu-link-default.png) ![Mega-menu link hover](components/crops/menu-link-hover.png)

### Home

The home page: the Sharp Grotesk hero ("One place to store, share, and collaborate") with the Try Dropbox free CTA, AI-integration cards with transparent Connect now actions and dwg-text-link links, an icon-button carousel, and the section palettes — coconut fields with dark dwg-theme--graphite bands.

#### Hero headline
The "One place to store, share, and collaborate" display heading. Read as `hero-title` on the home page.

**Values (default).** size 1072 x 143.06; background transparent; text Sharp Grotesk 66.24/71.53 500, #ffffff `color.brand.coconut.200`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede under the hero headline. Read as `hero-sub` on the home page.

**Values (default).** size 513.22 x 90; background transparent; text Atlas Grotesk Web 20/30 400, rgba(82, 74, 62, 0.82) `color.brand.status.faint.text`.

![Hero copy default](components/crops/hero-sub-default.png)

#### Hero CTA
The "Try Dropbox free" primary action on the hero; measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 230.52 x 71.19; padding 24px; border 2px solid #ffffff `color.brand.coconut.200`; radius 16px; background transparent; text Atlas Grotesk Web 16/19.2 500, #ffffff `color.brand.coconut.200`; transition background-color 0.1s cubic-bezier(0.4, 0, 0.6, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.6, 1); icon 24 x 24, #ffffff `color.brand.coconut.200` |
| hover | background rgba(255, 255, 255, 0.12) |
| focus-visible | shadow #428bff 0px 0px 0px 9px; outline 3px solid #ffffff `color.brand.coconut.200`, offset 3px |
| pressed | background rgba(255, 255, 255, 0.12) |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Transparent button
A dwg-button2 transparent-variant action (See all integrations / Connect now / Learn more); measured, never followed. Read as `transparent-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 179.5 x 19.2; background transparent; text Atlas Grotesk Web 16/19.2 500, #f7f5f2 `color.brand.status.faint.background`; transition background-color 0.1s cubic-bezier(0.4, 0, 0.6, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.6, 1); icon 24 x 24, #f7f5f2 `color.brand.status.faint.background` |
| focus-visible | outline 3px solid #428bff `color.brand.utility.focusring`, offset 3px; layers a.dwg-button2.dwg-button2--button-style-transparent 179.5x19.2 3px solid rgb(66, 139, 255) offset 3px |

![Transparent button default](components/crops/transparent-btn-default.png) ![Transparent button hover](components/crops/transparent-btn-hover.png) ![Transparent button focus-visible](components/crops/transparent-btn-focus-visible.png) ![Transparent button pressed](components/crops/transparent-btn-pressed.png)

#### Text link
A dwg-text-link inline link (the AI-integration names); measured, never followed. Read as `text-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 68.94 x 20; background transparent; text Atlas Grotesk Web 16/24 400, #f7f5f2 `color.brand.status.faint.background` |
| focus-visible | outline 3px solid #428bff `color.brand.utility.focusring`, offset 3px; layers a.dwg-text.dwg-font-family--atlas-grotesk 68.9x20.0 3px solid rgb(66, 139, 255) offset 3px |

![Text link default](components/crops/text-link-default.png) ![Text link hover](components/crops/text-link-hover.png) ![Text link focus-visible](components/crops/text-link-focus-visible.png) ![Text link pressed](components/crops/text-link-pressed.png)

#### Icon button
A dwg-icon-button glyph action on the page (a carousel arrow). Read as `icon-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; background transparent; text Arial 13.33/normal 400, #1e1919 `color.brand.graphite.default`; icon 32 x 32, #1e1919 `color.brand.graphite.default`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0.08) 0px none 1; button::after.dwg-icon-button.dwg-icon-button--hoverActiveFilter 32pxx32px rgba(0, 0, 0, 0.08) |
| focus-visible | shadow #428bff 0px 0px 0px 3px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.dwg-icon-button.dwg-icon-button--hoverActiveFilter 32.0x32.0 rgb(66, 139, 255) 0px 0px 0px 3px |
| pressed | layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0.08) 0px none 1; button::after.dwg-icon-button.dwg-icon-button--hoverActiveFilter 32pxx32px rgba(0, 0, 0, 0.08) |

![Icon button default](components/crops/icon-button-default.png) ![Icon button hover](components/crops/icon-button-hover.png) ![Icon button focus-visible](components/crops/icon-button-focus-visible.png) ![Icon button pressed](components/crops/icon-button-pressed.png)

#### Section heading
A section heading below the hero. Read as `section-h2` on the home page.

**Values (default).** size 886.14 x 24; background transparent; text Atlas Grotesk Web 20/24 500, #1e1919 `color.brand.graphite.default`.

![Section heading default](components/crops/section-h2-default.png)

#### Graphite band
A dark dwg-theme--graphite section painted inside the light page. Read as `graphite-band` on the home page.

**Values (default).** size 1440 x 2988; background #f7f5f2 `color.brand.status.faint.background`; text Atlas Grotesk Web 16/19.2 500, #f7f5f2 `color.brand.status.faint.background`; icon 24 x 24, #f7f5f2 `color.brand.status.faint.background`.

![Graphite band default](components/crops/graphite-band-default.png)

#### Coconut band
A cream dwg-theme--coconut section. Read as `coconut-band` on the home page.

**Values (default).** size 1440 x 120; padding 0px 0px 72px 0px; background #f7f5f2 `color.brand.status.faint.background`; text Atlas Grotesk Web 16/24 400, #1e1919 `color.brand.graphite.default`; layers ::before rgb(247, 245, 242) 0px none 1; ::after rgb(247, 245, 242) 0px none 1.

![Coconut band default](components/crops/coconut-band-default.png)

### Plans and pricing

The /plans surface in US dollars: plan cards with Monthly/Yearly billing radios (real radio inputs), Try for free / Buy now primary actions with "or buy now" transparent secondaries, the Show only differences comparison toggle and the Help me choose trigger.

#### Plans title
The plans-page heading (the markup carries no h1; the first heading element is read). Read as `plans-title` on the plans page.

**Values (default).** size 827.06 x 38.41; background transparent; text Sharp Grotesk 32/38.4 400, #1e1919 `color.brand.graphite.default`.

![Plans title default](components/crops/plans-title-default.png)

#### Billing radio
A Monthly/Yearly billing-period radio label (the input is a real radio — dwg-input-radio__input); the Yearly side was toggled for the screenshot, never checked out. Read as `billing-radio` on the plans page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 138.11 x 24; padding 0px 0px 0px 28px; background transparent; text Atlas Grotesk Web 16/24 400, #1e1919 `color.brand.graphite.default`; layers input::before.dwg-input-radio__input 20pxx20px T:1px solid rgb(30, 25, 25) / R:1px solid rgb(30, 25, 25) / B:1px solid rgb(30, 25, 25) / L:1px solid rgb(30, 25, 25) 50% |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: input::before 20pxx20px border 1px solid #1e1919 `color.brand.graphite.default` radius 50%.

![Billing radio default](components/crops/billing-radio-default.png) ![Billing radio hover](components/crops/billing-radio-hover.png) ![Billing radio pressed](components/crops/billing-radio-pressed.png)

#### Plan card
A pricing plan card (plan name, price and its action). Read as `plan-card` on the plans page.

**Values (default).** size 416 x 1079.41; padding 24px 48px 48px 48px; radius 12px; background #faf9f7 `color.brand.coconut.300`; text Atlas Grotesk Web 14/16.8 400, rgba(82, 74, 62, 0.82) `color.brand.status.faint.text`; icon 24 x 24, #f7f5f2 `color.brand.status.faint.background`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan name
A plan card's plan name. Read as `plan-name` on the plans page.

**Values (default).** size 61.92 x 20; background transparent; text Atlas Grotesk Web 14/20 500, #1e1919 `color.brand.graphite.default`.

![Plan name default](components/crops/plan-name-default.png)

#### Plan price
A plan card's price figure (US$ in the region the capture was served). Read as `plan-price` on the plans page.

**Values (default).** size 142.23 x 25; background transparent; text Atlas Grotesk Web 20/24 500, #1e1919 `color.brand.graphite.default`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan card's primary action (Try for free / Buy now); measured, never followed. Read as `plan-cta` on the plans page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 55.2; padding 16px 24px; border 2px solid #0061fe `color.brand.status.attention.border.default`; radius 16px; background #0061fe `color.brand.status.attention.border.default`; text Atlas Grotesk Web 16/19.2 500, #f7f5f2 `color.brand.status.faint.background`; transition background-color 0.1s cubic-bezier(0.4, 0, 0.6, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.6, 1); icon 24 x 24, #f7f5f2 `color.brand.status.faint.background` |
| hover | background #0057e5 `color.brand.button.primary.hover` |
| focus-visible | shadow #428bff 0px 0px 0px 3px |
| pressed | background #0050d0 `color.brand.button.primary.active` |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan secondary CTA
The "or buy now" transparent action under a plan CTA; measured, never followed. Read as `plan-cta-alt` on the plans page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 114.2 x 19.2; background transparent; text Atlas Grotesk Web 16/19.2 500, #1e1919 `color.brand.graphite.default`; transition background-color 0.1s cubic-bezier(0.4, 0, 0.6, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.6, 1); icon 24 x 24, #1e1919 `color.brand.graphite.default` |
| focus-visible | shadow #428bff 0px 0px 0px 3px; layers button.dwg-button2.dwg-button2--button-style-transparent 114.2x19.2 rgb(66, 139, 255) 0px 0px 0px 3px |

![Plan secondary CTA default](components/crops/plan-cta-alt-default.png) ![Plan secondary CTA hover](components/crops/plan-cta-alt-hover.png) ![Plan secondary CTA focus-visible](components/crops/plan-cta-alt-focus-visible.png) ![Plan secondary CTA pressed](components/crops/plan-cta-alt-pressed.png)

#### Outline button
A dwg-button2 outline-variant action (Get Basic / Contact us); measured, never followed. Read as `plan-outline` on the plans page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 127.48 x 39.2; padding 8px 24px; border 2px solid #1e1919 `color.brand.graphite.default`; radius 12px; background transparent; text Atlas Grotesk Web 16/19.2 500, #1e1919 `color.brand.graphite.default`; transition background-color 0.1s cubic-bezier(0.4, 0, 0.6, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.6, 1) |
| hover | background rgba(0, 0, 0, 0.08) |
| focus-visible | shadow #428bff 0px 0px 0px 3px |
| pressed | background rgba(0, 0, 0, 0.08) |

![Outline button default](components/crops/plan-outline-default.png) ![Outline button hover](components/crops/plan-outline-hover.png) ![Outline button focus-visible](components/crops/plan-outline-focus-visible.png) ![Outline button pressed](components/crops/plan-outline-pressed.png)

#### Difference toggle
The "Show only differences" comparison-table toggle; measured, never toggled. Read as `diff-toggle` on the plans page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 223.53 x 32; padding 4px 0px; background transparent; text Atlas Grotesk Web 16/24 400, #000000 `color.brand.graphite.600`; layers span.cf-diff-toggle__track 44.0x24.0 T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid rgb(0, 0, 0) 12px; span.cf-diff-toggle__knob 16.0x16.0 rgb(0, 0, 0) 50% |
| focus-visible | radius 4px; outline 2px solid #0061fe `color.brand.status.attention.border.default`, offset 4px; layers button.cf-diff-toggle 223.5x32.0 2px solid rgb(0, 97, 254) offset 4px 4px; span.cf-diff-toggle__track 44.0x24.0 T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid rgb(0, 0, 0) 12px; span.cf-diff-toggle__knob 16.0x16.0 rgb(0, 0, 0) 50% |

Child layers that carry the look: span 44x24 border 1px solid #000000 `color.brand.graphite.600` radius 12px; span 16x16 background #000000 `color.brand.graphite.600` radius 50%.

![Difference toggle default](components/crops/diff-toggle-default.png) ![Difference toggle hover](components/crops/diff-toggle-hover.png) ![Difference toggle focus-visible](components/crops/diff-toggle-focus-visible.png) ![Difference toggle pressed](components/crops/diff-toggle-pressed.png)

#### Help-me-choose
The "? Help me choose" assistant trigger; measured, never pressed. Read as `help-choose` on the plans page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 168.94 x 38; padding 0px 14px; border 1px solid rgba(30, 25, 25, 0.65); radius 3.35544e+07px; background rgba(255, 255, 255, 0.9); text Atlas Grotesk Web 12/12 700, #1e1919 `color.brand.graphite.default` |
| focus-visible | outline 2px solid #0061fe `color.brand.status.attention.border.default`, offset 2px |

![Help-me-choose default](components/crops/help-choose-default.png) ![Help-me-choose hover](components/crops/help-choose-hover.png) ![Help-me-choose focus-visible](components/crops/help-choose-focus-visible.png) ![Help-me-choose pressed](components/crops/help-choose-pressed.png)

### Features and products

The /features, /business, /sign and /replay product and landing pages: display headings, primary dwg-button2 actions, feature cards and the dwg-theme section palettes (navy, graphite, cloud, lime).

#### Business headline
The /business display heading ("Everything your business needs to work efficiently, all in one place"). Read as `biz-title` on the business page.

**Values (default).** size 384 x 240; background transparent; text Sharp Grotesk 40/48 400, #f7f5f2 `color.brand.status.faint.background`.

![Business headline default](components/crops/biz-title-default.png)

#### Business CTA
A primary dwg-button2 action on /business; measured, never followed. Read as `biz-cta` on the business page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 117.13 x 40; padding 0px 12px; border 2px solid #0061fe `color.brand.status.attention.border.default`; radius 12px; background #0061fe `color.brand.status.attention.border.default`; text Atlas Grotesk Web 16/19.2 500, #f7f5f2 `color.brand.status.faint.background`; transition background-color 0.1s cubic-bezier(0.4, 0, 0.6, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.6, 1) |
| hover | background #0057e5 `color.brand.button.primary.hover` |
| focus-visible | shadow #428bff 0px 0px 0px 3px |
| pressed | background #0050d0 `color.brand.button.primary.active` |

![Business CTA default](components/crops/biz-cta-default.png) ![Business CTA hover](components/crops/biz-cta-hover.png) ![Business CTA focus-visible](components/crops/biz-cta-focus-visible.png) ![Business CTA pressed](components/crops/biz-cta-pressed.png)

#### Navy band
A dwg-theme--navy coloured section. Read as `navy-band` on the business page.

**Values (default).** size 1440 x 720; background #283750 `color.brand.accent.navy`; text Sharp Grotesk 24/28.8 400, #f7f5f2 `color.brand.status.faint.background`; icon 24 x 24, #f7f5f2 `color.brand.status.faint.background`; layers ::before rgb(40, 55, 80) 0px none 1; ::after rgb(40, 55, 80) 0px none 1.

![Navy band default](components/crops/navy-band-default.png)

#### Features headline
The /features display heading ("What is Dropbox?"). Read as `feat-title` on the features page.

**Values (default).** size 384 x 48; background transparent; text Sharp Grotesk 40/48 400, #f7f5f2 `color.brand.status.faint.background`.

![Features headline default](components/crops/feat-title-default.png)

#### Feature card
A dwg-card / dwg-nav-card feature tile on /features; the link was measured, never followed. Read as `feat-card` on the features page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 413.53 x 517.55; padding 0px 24px; background transparent; text Atlas Grotesk Web 20/24 500, #1e1919 `color.brand.graphite.default`; layers div.dwg-media-frame.dwg-box 365.5x365.5 rgb(238, 233, 226) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 365.5x365.5 background #eee9e2 `color.brand.coconut.600`.

![Feature card default](components/crops/feat-card-default.png) ![Feature card hover](components/crops/feat-card-hover.png) ![Feature card pressed](components/crops/feat-card-pressed.png)

#### Sign headline
The /sign product-page heading ("Sign paperwork without all the paperwork"). Read as `sign-title` on the sign page.

**Values (default).** size 384 x 144; background transparent; text Sharp Grotesk 40/48 400, #f7f5f2 `color.brand.status.faint.background`.

![Sign headline default](components/crops/sign-title-default.png)

#### Sign CTA
A primary dwg-button2 action on /sign; measured, never followed. Read as `sign-cta` on the sign page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 117.13 x 40; padding 0px 12px; border 2px solid #0061fe `color.brand.status.attention.border.default`; radius 12px; background #0061fe `color.brand.status.attention.border.default`; text Atlas Grotesk Web 16/19.2 500, #f7f5f2 `color.brand.status.faint.background`; transition background-color 0.1s cubic-bezier(0.4, 0, 0.6, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.6, 1) |
| hover | background #0057e5 `color.brand.button.primary.hover` |
| focus-visible | shadow #428bff 0px 0px 0px 3px |
| pressed | background #0050d0 `color.brand.button.primary.active` |

![Sign CTA default](components/crops/sign-cta-default.png) ![Sign CTA hover](components/crops/sign-cta-hover.png) ![Sign CTA focus-visible](components/crops/sign-cta-focus-visible.png) ![Sign CTA pressed](components/crops/sign-cta-pressed.png)

### Login and signup

The /login and /register cards on the coconut field: Continue with Apple / Google / Microsoft SSO actions, the email field (focused and given sample text that was deleted again, never sent) and the Continue / Get started primary actions — measured, never used.

#### Auth card
The log-in card (Continue with Apple / Google / Microsoft + the email field and terms); captured, never used. Read as `auth-card` on the login page.

**Values (default).** size 368 x 272.2; background transparent; text Atlas Grotesk Web 14/16 400, #1e1919 `color.brand.graphite.default`; layers div.nsm7Bb-HzV7m-LgbsSe.TzA9Ye-LgbsSe 0.0x0.0 rgb(255, 255, 255) T:1px solid rgb(218, 220, 224) / R:1px solid rgb(218, 220, 224) / B:1px solid rgb(218, 220, 224) / L:1px solid rgb(218, 220, 224) 4px; button.dwg-sso-button.dwg-sso-button-v2 368.0x40.0 rgb(255, 255, 255) T:1px solid rgb(202, 197, 190) / R:1px solid rgb(202, 197, 190) / B:1px solid rgb(202, 197, 190) / L:1px solid rgb(202, 197, 190) .

Child layers that carry the look: div 0x0 background #ffffff `color.brand.coconut.200` border 1px solid #dadce0 radius 4px; button 368x40 background #ffffff `color.brand.coconut.200` border 1px solid #cac5be radius 4px; button 368x40 background #ffffff `color.brand.coconut.200` border 1px solid #cac5be radius 4px.

![Auth card default](components/crops/auth-card-default.png)

#### SSO button
The "Continue with Apple" SSO action; measured, never pressed — it would leave for the provider flow. Read as `sso-button` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 40; border 1px solid #cac5be; radius 4px; background #ffffff `color.brand.coconut.200`; text Atlas Grotesk Web 14/16 400, #1e1919 `color.brand.graphite.default`; icon 32 x 32, #000000 `color.brand.graphite.600` |
| hover | background rgba(0, 0, 0, 0.08) |
| focus-visible | shadow #428bff 0px 0px 0px 3px |
| pressed | border 1px solid rgba(166, 158, 146, 0.6) `color.brand.standard.border`; background rgba(0, 0, 0, 0.08); text Atlas Grotesk Web 14/16 400, rgba(82, 74, 62, 0.82) `color.brand.status.faint.text`; icon 32 x 32, rgba(82, 74, 62, 0.82) `color.brand.status.faint.text` |

![SSO button default](components/crops/sso-button-default.png) ![SSO button hover](components/crops/sso-button-hover.png) ![SSO button focus-visible](components/crops/sso-button-focus-visible.png) ![SSO button pressed](components/crops/sso-button-pressed.png)

#### SSO button (alt)
A second SSO action (Google or Microsoft); measured, never pressed. Read as `sso-button-alt` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 40; border 1px solid #cac5be; radius 4px; background #ffffff `color.brand.coconut.200`; text Atlas Grotesk Web 14/16 400, #1e1919 `color.brand.graphite.default` |
| hover | background rgba(0, 0, 0, 0.08) |
| focus-visible | shadow #428bff 0px 0px 0px 3px |
| pressed | border 1px solid rgba(166, 158, 146, 0.6) `color.brand.standard.border`; background rgba(0, 0, 0, 0.08); text Atlas Grotesk Web 14/16 400, rgba(82, 74, 62, 0.82) `color.brand.status.faint.text` |

![SSO button (alt) default](components/crops/sso-button-alt-default.png) ![SSO button (alt) hover](components/crops/sso-button-alt-hover.png) ![SSO button (alt) focus-visible](components/crops/sso-button-alt-focus-visible.png) ![SSO button (alt) pressed](components/crops/sso-button-alt-pressed.png)

#### Email field
The email input on the auth card; focused and given sample text that was deleted again — nothing sent. Read as `email-field` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 48; padding 16px; border 1px solid #b0b4ba; background #ffffff `color.brand.coconut.200`; text lucida grande 16/normal 400, #65696e; placeholder #65696e |
| focused, filled | border 1px solid #050505; shadow #428bff 0px 0px 0px 3px |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png) ![Email field filled](components/crops/email-field-filled.png)

#### Continue button
The auth card's Continue action; measured, never pressed. Read as `continue-button` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 55.2; padding 16px 24px; border 2px solid #0061fe `color.brand.status.attention.border.default`; radius 16px; background #0061fe `color.brand.status.attention.border.default`; text Atlas Grotesk Web 16/19.2 500, #f7f5f2 `color.brand.status.faint.background`; transition background-color 0.1s cubic-bezier(0.4, 0, 0.6, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.6, 1) |
| hover | background #0057e5 `color.brand.button.primary.hover` |
| focus-visible | shadow #428bff 0px 0px 0px 3px |
| pressed | background #0050d0 `color.brand.button.primary.active` |

![Continue button default](components/crops/continue-button-default.png) ![Continue button hover](components/crops/continue-button-hover.png) ![Continue button focus-visible](components/crops/continue-button-focus-visible.png) ![Continue button pressed](components/crops/continue-button-pressed.png)

#### Register card
The "Get started with Dropbox" sign-up card; captured, never used. Read as `register-card` on the register page.

**Values (default).** size 368 x 272.2; background transparent; text Atlas Grotesk Web 14/16 400, #1e1919 `color.brand.graphite.default`; layers div.nsm7Bb-HzV7m-LgbsSe.TzA9Ye-LgbsSe 0.0x0.0 rgb(255, 255, 255) T:1px solid rgb(218, 220, 224) / R:1px solid rgb(218, 220, 224) / B:1px solid rgb(218, 220, 224) / L:1px solid rgb(218, 220, 224) 4px; button.dwg-sso-button.dwg-sso-button-v2 368.0x40.0 rgb(255, 255, 255) T:1px solid rgb(202, 197, 190) / R:1px solid rgb(202, 197, 190) / B:1px solid rgb(202, 197, 190) / L:1px solid rgb(202, 197, 190) .

Child layers that carry the look: div 0x0 background #ffffff `color.brand.coconut.200` border 1px solid #dadce0 radius 4px; button 368x40 background #ffffff `color.brand.coconut.200` border 1px solid #cac5be radius 4px; button 368x40 background #ffffff `color.brand.coconut.200` border 1px solid #cac5be radius 4px.

![Register card default](components/crops/register-card-default.png)

#### Register email field
The name@company.com email input on the sign-up card; focused and given sample text that was deleted again — nothing sent. Read as `register-email` on the register page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 48; padding 16px; border 1px solid #b0b4ba; background #ffffff `color.brand.coconut.200`; text lucida grande 16/normal 400, #65696e; placeholder #65696e |
| focused, filled | border 1px solid #050505; shadow #428bff 0px 0px 0px 3px |

![Register email field default](components/crops/register-email-default.png) ![Register email field focused](components/crops/register-email-focused.png) ![Register email field filled](components/crops/register-email-filled.png)

#### Register CTA
The sign-up card's Continue action; measured, never pressed. Read as `register-cta` on the register page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 55.2; padding 16px 24px; border 2px solid #0061fe `color.brand.status.attention.border.default`; radius 16px; background #0061fe `color.brand.status.attention.border.default`; text Atlas Grotesk Web 16/19.2 500, #f7f5f2 `color.brand.status.faint.background`; transition background-color 0.1s cubic-bezier(0.4, 0, 0.6, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.6, 1) |
| hover | background #0057e5 `color.brand.button.primary.hover` |
| focus-visible | shadow #428bff 0px 0px 0px 3px |
| pressed | background #0050d0 `color.brand.button.primary.active` |

![Register CTA default](components/crops/register-cta-default.png) ![Register CTA hover](components/crops/register-cta-hover.png) ![Register CTA focus-visible](components/crops/register-cta-focus-visible.png) ![Register CTA pressed](components/crops/register-cta-pressed.png)

### Footer

The footer: product/company link columns as dwg-text-links, app links, language and legal.

#### Footer
The footer: the product/company link columns, app links, the language and legal links. Read as `footer` on the home page.

**Values (default).** size 1440 x 619.2; background transparent; text Atlas Grotesk Web 20/30 500, #f7f5f2 `color.brand.status.faint.background`; icon 32 x 32, #f7f5f2 `color.brand.status.faint.background`; layers div.dwg-footer-plank.dwg-plank-frame 1440.0x478.0 rgb(0, 0, 0); div::before.dwg-footer-plank.dwg-plank-frame 1440pxx96px rgb(0, 0, 0); div::after.dwg-footer-plank.dwg-plank-frame 1440pxx0px rgb(0, 0, 0); div.warp-dwg-locale-selector-plank.dwg-plank-frame 1440.0x141.2 rgb(0, 0, 0); div::before.warp-dwg-locale-selector-plank.dwg-plank-frame 1440pxx0px rgb(0, 0, 0); div::after.warp-dwg-locale-selecto.

Child layers that carry the look: div 1440x478 background #000000 `color.brand.graphite.600`; div::before 1440pxx96px background #000000 `color.brand.graphite.600`; div::after 1440pxx0px background #000000 `color.brand.graphite.600`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 83.66 x 17; background transparent; text Atlas Grotesk Web 14/22 400, #f7f5f2 `color.brand.status.faint.background` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.dwg-text.dwg-font-family--atlas-grotesk 83.7x17.0 1px auto rgb(0, 95, 204) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A social link in the footer. Read as `social-icon` on the home page.

**Wrong element.** `footer a[href*="x.com"]` also matches dropbox.com, so these are the "Dropbox Sign" footer link's values, not a social icon's. The selector is fixed in tools/capture/public/measure.mjs; the entry needs a recapture.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 91.03 x 17; background transparent; text Atlas Grotesk Web 14/22 400, #f7f5f2 `color.brand.status.faint.background` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.dwg-text.dwg-font-family--atlas-grotesk 91.0x17.0 1px auto rgb(0, 95, 204) offset 1px |

![Social link default](components/crops/social-icon-default.png) ![Social link hover](components/crops/social-icon-hover.png) ![Social link focus-visible](components/crops/social-icon-focus-visible.png) ![Social link pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The same surface at phone width: the nav shrinks to mark + hamburger, the menu opens as a full panel with nav rows and the auth actions.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 48; background #ffffff `color.brand.coconut.200`; text Atlas Grotesk Web 14/20 400, #1e1919 `color.brand.graphite.default`; icon 32 x 27, #0000ee; layers ::after rgba(166, 145, 113, 0.2) 0px none 1.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The hamburger toggle in the mobile nav. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 48 x 48; padding 1px 6px; background transparent; text Arial 13.33/normal 400, #1e1919 `color.brand.graphite.default`; icon 32 x 32, #1e1919 `color.brand.graphite.default`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The opened mobile navigation panel (the overlay holding the menu items and the auth actions). Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 708; background transparent; text Atlas Grotesk Web 24/28.8 500, #1e1919 `color.brand.graphite.default`; icon 24 x 24, rgba(82, 74, 62, 0.82) `color.brand.status.faint.text`; layers div.dwg-nav-mobile-dropdown__backdrop.dwg-box 390.0x844.0 rgb(255, 255, 255); div.dwg-nav-dropdown.dwg-nav-dropdown--2-col 390.0x624.0 rgb(250, 249, 247); div.dwg-nav-dropdown.dwg-nav-dropdown--3-col 390.0x1098.0 rgb(250, 249, 247); div.dwg-nav-dropdown.dwg-nav-dropdown--1-col 390.0x164.0 rgb(250, 249, 247); div.dwg-nav-mobile-dropdown__cta-container.dwg-nav-mobile-dropdown--nav-redesign__cta-cont.

Child layers that carry the look: div 390x844 background #ffffff `color.brand.coconut.200`; div 390x624 background #faf9f7 `color.brand.coconut.300`; div 390x1098 background #faf9f7 `color.brand.coconut.300`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
A row inside the opened mobile menu (Products / Solutions / Business / Pricing / Get app). Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 382 x 76.8; padding 24px 16px; background transparent; text Atlas Grotesk Web 24/28.8 500, #1e1919 `color.brand.graphite.default`; transition color 0.125s linear; icon 24 x 24, rgba(82, 74, 62, 0.82) `color.brand.status.faint.text` |
| hover | text Atlas Grotesk Web 24/28.8 500, #0061fe `color.brand.status.attention.border.default`; icon 24 x 24, #0061fe `color.brand.status.attention.border.default` |
| focus-visible | shadow #428bff 0px 0px 0px 3px inset; layers button.dwg-nav-item-button.dwg-nav-item-button--nav-redesign 382.0x76.8 rgb(66, 139, 255) 0px 0px 0px 3px inset |
| pressed | text Atlas Grotesk Web 24/28.8 500, #0061fe `color.brand.status.attention.border.default`; icon 24 x 24, #0061fe `color.brand.status.attention.border.default` |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile sign-up
The Sign up action in the mobile top bar, visible above the opened menu; measured, never followed. Read as `m-signup` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 67.83 x 48; padding 8px; background transparent; text Atlas Grotesk Web 14/20 400, #1e1919 `color.brand.graphite.default`; transition color 0.125s linear |
| hover | text Atlas Grotesk Web 14/20 400, #0061fe `color.brand.status.attention.border.default` |
| focus-visible | shadow #428bff 0px 0px 0px 3px inset; layers a.dwg-nav-item-button.dwg-nav-item-button--nav-redesign 67.8x48.0 rgb(66, 139, 255) 0px 0px 0px 3px inset |
| pressed | text Atlas Grotesk Web 14/20 400, #0061fe `color.brand.status.attention.border.default` |

![Mobile sign-up default](components/crops/m-signup-default.png) ![Mobile sign-up hover](components/crops/m-signup-hover.png) ![Mobile sign-up focus-visible](components/crops/m-signup-focus-visible.png) ![Mobile sign-up pressed](components/crops/m-signup-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 342 x 115.22; background transparent; text Sharp Grotesk 32/38.4 500, #1e1919 `color.brand.graphite.default`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Dropbox box mark, the product glyphs in the mega-menu, the Apple/Google/Microsoft provider glyphs, the carousel arrows and the illustration artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Everything behind the auth cards — the Dropbox file dashboard, Paper, Replay and Sign workspaces, Dash, account, billing and checkout flows — was never reached. /login and /register show only the provider cards; the email fields were focused and given sample text that was deleted again, and the Continue / Get started actions were never pressed. What the product itself looks like or how it behaves is not documented here — the marketing pages' claims about it were never verified.

### Pages

- **Dash (dash.dropbox.com) and Reclaim.ai (app.reclaim.ai)** are separate products on separate hosts, linked from the nav; they were never opened.
- **Paper** redirects /paper to a product page (/paper/start); the Paper workspace itself is a signed-in surface and was never reached.
- **Purchase flows.** Try for free, Buy now, Get Basic, Contact sales and Get started were measured or screenshotted, never followed; no account was created and no payment surface was reached.
- **OAuth providers.** Continue with Apple / Google / Microsoft were measured, never pressed — they leave for the providers' flows.
- **External surfaces** (help.dropbox.com, dropbox.com/developers, the blog and social profiles) are linked from the site but were never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface (the DIG layer declares disabled roles; nothing on the marketing pages paints them).
- **The mega-menu** closes on outside interaction; flyout-child states re-opened it before reading.

### Themes

The public surface paints one scope — `dig-Theme-vis2023 dig-Theme-vis2023--bright` on `dig-Mode--bright`. Inside it, sections carry `dwg-theme--*` palettes: coconut (the nav and cream fields), graphite (dark bands), navy and the accent hues. `light.dwg.coconut|graphite|navy` in tokens.json are those painted section roles. The `dig-Theme-vis2023--dark` scope is fully declared in the token layer but never paints signed out — the export's "dark" set is that declared palette, not a painted theme.

### Fonts

- **Sharp Grotesk** (titles) and **Atlas Grotesk Web** (body) are Dropbox's served faces; the @font-face blocks live in the cfl.dropboxstatic.com font bundles (harvested src list in raw/css-vars.json). The style guide falls back to system sans — the webfonts are licensed, not shipped.

### Screenshots

- The product imagery, illustrations and the Dropbox wordmark in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Plan feature lists, customer logos, marketing copy and the terms text are the product's content; only frames and components were measured.
