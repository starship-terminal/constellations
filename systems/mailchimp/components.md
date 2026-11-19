# Mailchimp components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from mailchimp.com on 2026-11-18, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted. The log-in username field was typed into and cleared. Every link and call to action was measured, never followed. Sign-in was not started.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (27 components, 67 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/22.5 600, #23252b`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (67 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`. Every surface paints light. Desktop shots are 1440 x 900 at 1x. `-full` shots are whole pages at 1x. Mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `https://mailchimp.com/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu-industries-and-solutions](screenshots/home-light-menu-industries-and-solutions.png), [menu-resources](screenshots/home-light-menu-resources.png) |
| Pricing | `https://mailchimp.com/pricing/marketing/` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Features | `https://mailchimp.com/features/` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| About | `https://mailchimp.com/about/` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Log in | `https://login.mailchimp.com/` | [default](screenshots/login-light-default.png) |
| Home, phone | `https://mailchimp.com/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `https://mailchimp.com/pricing/marketing/` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Features, phone | `https://mailchimp.com/features/` | [default](screenshots/mobile-features-light-default.png) |
| Log in, phone | `https://login.mailchimp.com/` | [default](screenshots/mobile-login-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent | every marketing page | OneTrust is hidden, never answered | hidden before every shot and reading |
| Home survey | mailchimp.com / | the customize-my-experience survey is hidden, never submitted | hidden before every shot and reading |
| Nav menus | every marketing page | clicked Industries and Solutions and Resources | [home-light-menu-resources](screenshots/home-light-menu-resources.png) |
| Mobile menu | home, phone width | clicked Main Menu | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |
| Log-in field | login.mailchimp.com | typed into then cleared. Nothing sent. Sign-in was not started | [login-username](#username-field) |
| Signed-in product | a Mailchimp account | the account and campaign builder need sign-in | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 12 components were given a real keyboard focus. 11 draw an outline ring: `nav-menu` (2px solid #4bc4c2, offset 2px), `nav-link` (2px solid #4bc4c2, offset 2px), `nav-login` (on a child: 2px solid rgb(75, 196, 194) offset 3.25px), `nav-trial` (on a child: 2px solid rgb(75, 196, 194) offset 3.25px), `hero-cta` (on a child: 2px solid rgb(75, 196, 194) offset 3.25px), `hero-secondary` (on a child: 2px solid rgb(75, 196, 194) offset 2.5px), `footer-link` (2px solid #4bc4c2, offset 6.5px), `price-cta` (on a child: 2px solid rgb(75, 196, 194) offset 3.25px), `login-forgot` (1px auto #005fcc, offset 1px), `login-create` (1px auto #005fcc, offset 1px), `m-menu` (2px solid #4bc4c2, offset 2px). 1 draw a focus ring as a shadow instead: `login-submit`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `ease` | background-color | m-menu, nav-link, nav-logo, nav-menu |
| 0.15s | `ease-in-out` | color | hero-secondary |
| 0.2s | `ease` | -webkit-clip-path, clip-path, opacity | nav-panel |
| 0.2s | `ease-in-out` | all, background-color, opacity | login-submit, login-username |
| 0.3s | `cubic-bezier(0.5, 2.5, 0.7, 0.7)` | box-shadow, transform | hero-cta, nav-login, nav-trial, price-cta |
| 0.3s | `ease` | transform | hero-secondary |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Nav menu panel](#nav-menu-panel) | 1440 x 507.5 | - | - | transparent | none | 0px 0px 80px 0px |
| [Plan card](#plan-card) | 370 x 508.25 | - | - | transparent | none | 0 |
| [Log-in card](#log-in-card) | 422 x 453 | - | - | transparent | none | 0 |
| [Footer](#footer) | 1440 x 1041.78 | - | - | #e7b75f | none | 60px 0px |

## Components

### Announcement bar

The trial announcement link above the nav on marketing pages.

#### Announcement link
The trial announcement link above the nav ("Start today"). Measured, never followed. It points at pricing, not a signup submit. Read as `announce-bar` on the home page.

**Values (default).** size 64.83 x 16; border B: 1px dashed #ffffff; background transparent; text Tally 13/17.55 400, #ffffff; layers a 64.8x16.0 B:1px dashed rgb(255, 255, 255).

Child layers that carry the look: a 64.8x16 border 1px dashed #ffffff.

![Announcement link default](components/crops/announce-bar-default.png)

### Site chrome

The header: wordmark, Industries and Solutions / Integrations / Resources menus, Pricing, Search, Log In, and the yellow Start Free Trial pill.

#### Site nav
The header (header.iaGlobalNav): wordmark, Industries and Solutions / Integrations / Resources menus, Pricing, Search, Log In, and the yellow Start Free Trial pill. The announcement strip above it is a separate aside. Read as `site-nav` on the home page.

**Values (default).** size 1440 x 68; background transparent; text Tally 13/14.3 700, #231e15 `color.caviar`; layers section::after.iaNav__panel.panel__top 100%x100% rgba(0, 0, 0, 0.16) 4px 8px 32px 0px; div.iaNav__panelContentHolder 0.0x0.0 rgb(255, 255, 255); div::after.iaNav__panelContent.flex 1440pxx100% rgb(246, 246, 244); a::before.ctaArrow.cta--small autox32px rgb(255, 224, 27) 16px; span.badge.badge--square 0.0x0.0 rgb(35, 30, 21) rgba(0, 0, 0, 0.13) 0px 2px 4px 0px, rgba(0, 0, 0, 0.11) 0px 0px 1px 0px 4.

Child layers that carry the look: section::after 100%x100% shadow rgba(0, 0, 0, 0.16) 4px 8px 32px 0px; div 0x0 background #ffffff; div::after 1440pxx100% background #f6f6f4.

![Site nav default](components/crops/site-nav-default.png)

#### Wordmark
The Mailchimp wordmark linking home. Read as `nav-logo` on the home page.

**Values (default).** size 162.45 x 46; radius 3px; background transparent; text Tally 13/14.3 700, #231e15 `color.caviar`; transition background-color 0.15s ease.

![Wordmark default](components/crops/nav-logo-default.png)

#### Nav menu button
The Resources button (aria-haspopup) that opens the mega menu. The opened state was measured after clicking it. Menu links were never followed. Read as `nav-menu` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101.3 x 30.3; padding 8px; radius 3px; background transparent; text Tally 13/14.3 700, #231e15 `color.caviar`; transition background-color 0.15s ease; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | background rgba(35, 30, 21, 0.05) |
| focus-visible | background rgba(35, 30, 21, 0.05); outline 2px solid #4bc4c2, offset 2px |
| pressed, opened | background rgba(35, 30, 21, 0.05) |

![Nav menu button default](components/crops/nav-menu-default.png) ![Nav menu button hover](components/crops/nav-menu-hover.png) ![Nav menu button focus-visible](components/crops/nav-menu-focus-visible.png) ![Nav menu button pressed](components/crops/nav-menu-pressed.png) ![Nav menu button opened](components/crops/nav-menu-opened.png)

#### Nav menu panel
The panel opened by Resources (section.iaNav__panel.expanded). Its links were never followed. Read as `nav-panel` on the home page.

**Values (default).** size 1440 x 507.5; padding 0px 0px 80px 0px; background transparent; text Means Web 24/31.99 400, #231e15 `color.caviar`; transition opacity 0.2s ease, -webkit-clip-path 0.2s ease, clip-path 0.2s ease; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0.16) 4px 8px 32px 0px 1; section::after.iaNav__panel.panel__top 100%x100% rgba(0, 0, 0, 0.16) 4px 8px 32px 0px; div.iaNav__panelContentHolder 1440.0x427.5 rgb(255, 255, 255); div::after.iaNav__panelContent.flex 1440pxx427.5px rgb(246, 246, 244); a::before.ctaArrow.cta--small 32pxx32px rgb(255, 224, 27) 16px; div.iaNav__panelContent__aux 453.3x427.5 rgb(2.

Child layers that carry the look: section::after 100%x100% shadow rgba(0, 0, 0, 0.16) 4px 8px 32px 0px; div 1440x427.5 background #ffffff; div::after 1440pxx427.5px background #f6f6f4.

![Nav menu panel default](components/crops/nav-panel-default.png)

#### Nav link
The Pricing link in the nav. Measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 58.95 x 30.3; padding 8px; radius 3px; background transparent; text Tally 13/14.3 700, #231e15 `color.caviar`; transition background-color 0.15s ease |
| hover | background rgba(35, 30, 21, 0.05) |
| focus-visible | background rgba(35, 30, 21, 0.05); outline 2px solid #4bc4c2, offset 2px |
| pressed | background rgba(35, 30, 21, 0.05) |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log In
The outlined Log In pill. It points at login.mailchimp.com. Measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85.56 x 43.5; padding 12px 24px; radius 26px; background rgba(35, 30, 21, 0); shadow #231e15 0px 0px 0px 1px; text Tally 13/19.5 700, #231e15 `color.caviar`; transition transform 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7), box-shadow 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | shadow #231e15 0px 0px 0px 1px, #231e15 0px 4.875px 0px 0px; transform translate(0px, -4.875px) |
| focus-visible | shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px; transform translate(0px, -1.625px); layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| pressed | shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px; transform translate(0px, -1.625px) |

![Log In default](components/crops/nav-login-default.png) ![Log In hover](components/crops/nav-login-hover.png) ![Log In focus-visible](components/crops/nav-login-focus-visible.png) ![Log In pressed](components/crops/nav-login-pressed.png)

#### Start Free Trial
The yellow Start Free Trial pill. Measured, never followed. Signup was not started. Read as `nav-trial` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 140.36 x 43.5; padding 12px 24px; radius 26px; background #ffe01b `color.yellow`; shadow #231e15 0px 0px 0px 1px; text Tally 13/19.5 700, #231e15 `color.caviar`; transition transform 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7), box-shadow 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | shadow #231e15 0px 0px 0px 1px, #231e15 0px 4.875px 0px 0px; transform translate(0px, -4.875px) |
| focus-visible | shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px; transform translate(0px, -1.625px); layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| pressed | shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px; transform translate(0px, -1.625px) |

![Start Free Trial default](components/crops/nav-trial-default.png) ![Start Free Trial hover](components/crops/nav-trial-hover.png) ![Start Free Trial focus-visible](components/crops/nav-trial-focus-visible.png) ![Start Free Trial pressed](components/crops/nav-trial-pressed.png)

### Home

The home hero on a photo band, Means Web headline, yellow trial button.

#### Hero headline
The home masthead, set in Means Web on the dark hero. Read as `hero-h1` on the home page.

**Values (default).** size 960 x 153.59; background transparent; text Means Web 64/76.8 400, #ffffff.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero CTA
The hero Start Free Trial button. It points at pricing. Measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 343 x 48; padding 12px 24px; radius 40px; background #ffe01b `color.yellow`; shadow #231e15 0px 0px 0px 1px; text Tally 15/24 600, #231e15 `color.caviar`; transition transform 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7), box-shadow 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | shadow #231e15 0px 0px 0px 1px, #231e15 0px 5.625px 0px 0px; transform translate(0px, -5.625px) |
| focus-visible | shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px; transform translate(0px, -1.625px); layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| pressed | shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px; transform translate(0px, -1.625px) |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### See all demos
The hero secondary link under the photo band. Measured, never followed. Read as `hero-secondary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 136.72 x 32; padding 0px 40px 0px 0px; radius 32px; background transparent; text Tally 16/32 400, #ffffff; transition color 0.15s ease-in-out, transform 0.3s ease; layers ::before rgb(255, 224, 27) 0px none 1; a::before.ctaArrow 32pxx32px rgb(255, 224, 27) 16px |
| hover | text Tally 16/32 400, #231e15 `color.caviar`; transform translate(4px, 0px); layers ::before rgb(255, 224, 27) 0px none 1; a::before.ctaArrow 152.719pxx32px rgb(255, 224, 27) 16px |
| focus-visible | layers ::before rgb(255, 224, 27) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1; a::before.ctaArrow 152.719pxx32px rgb(255, 224, 27) 16px; a::after.ctaArrow 152.719pxx32px 2px solid rgb(75, 196, 194) offset 2.5px 16px |
| pressed | text Tally 16/32 400, #231e15 `color.caviar`; transform translate(4px, 0px); layers ::before rgb(255, 224, 27) 0px none 1; a::before.ctaArrow 152.719pxx32px rgb(255, 224, 27) 16px |

Child layers that carry the look: a::before 32pxx32px background #ffe01b `color.yellow` radius 16px.

![See all demos default](components/crops/hero-secondary-default.png) ![See all demos hover](components/crops/hero-secondary-hover.png) ![See all demos focus-visible](components/crops/hero-secondary-focus-visible.png) ![See all demos pressed](components/crops/hero-secondary-pressed.png)

### Pricing

The /pricing/marketing/ page: plan card, trial link, contacts select, and plan radio.

#### Plan card
The Standard plan card on /pricing/marketing/. The trial link was measured, never followed. Checkout was not started. Read as `price-plan` on the pricing page.

**Values (default).** size 370 x 508.25; background transparent; text Means Web 40/40 400, #000000; layers div.singlePlanCard.backgroundWhite 370.0x472.3 rgb(255, 255, 255) rgba(35, 30, 21, 0.15) 0px 0px 20px 3px; form.flex.flex--middle 338.0x47.0 T:1px solid rgba(35, 30, 21, 0.3) / R:1px solid rgba(35, 30, 21, 0.3) / B:1px solid rgba(35, 30, 21, 0.3) / L:1px solid rgba(35, 30, 21, 0.3) 10px; div.formSelect 224.0x44.0 rgb(255, 255, 255) 10px; div.card 338.0x102.3 rgb(255, 255, 255) T:1px solid rgb(188,.

Child layers that carry the look: div 370x472.3 background #ffffff shadow rgba(35, 30, 21, 0.15) 0px 0px 20px 3px; form 338x47 border 1px solid rgba(35, 30, 21, 0.3) radius 10px; div 224x44 background #ffffff radius 10px.

![Plan card default](components/crops/price-plan-default.png)

#### Plan trial button
The Standard plan Start Free Trial link. It points at /signup/ with a plan query. Measured, never followed. Signup was not started and checkout was not started. Read as `price-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 338 x 43.5; padding 12px 24px; radius 26px; background #ffe01b `color.yellow`; shadow #231e15 0px 0px 0px 1px; text Tally 13/19.5 700, #231e15 `color.caviar`; transition transform 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7), box-shadow 0.3s cubic-bezier(0.5, 2.5, 0.7, 0.7); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | shadow #231e15 0px 0px 0px 1px, #231e15 0px 4.875px 0px 0px; transform translate(0px, -4.875px) |
| focus-visible | shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px; transform translate(0px, -1.625px); layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| pressed | shadow #231e15 0px 0px 0px 1px, #231e15 0px 3.25px 0px 0px; transform translate(0px, -1.625px) |

![Plan trial button default](components/crops/price-cta-default.png) ![Plan trial button hover](components/crops/price-cta-hover.png) ![Plan trial button focus-visible](components/crops/price-cta-focus-visible.png) ![Plan trial button pressed](components/crops/price-cta-pressed.png)

#### Contacts select
The contacts-count select on the pricing page. Measured at rest. The value was not changed and nothing was submitted. Read as `price-select` on the pricing page.

**Values (default).** size 214 x 44; padding 8px 48px 8px 0px; background transparent; text Means Web 18/normal 400, #000000.

![Contacts select default](components/crops/price-select-default.png)

#### Plan radio
A trial-or-discount radio on a plan card. Measured at rest, never changed. Read as `price-radio` on the pricing page.

**Values (default).** size 20 x 20; background transparent; text Tally 16/18.4 400, #000000; placeholder #000000.

![Plan radio default](components/crops/price-radio-default.png)

### Features

The /features/ masthead.

#### Features headline
The /features/ masthead. Read as `feat-h1` on the features page.

**Values (default).** size 853.33 x 96; background transparent; text Means Web 48/48 400, #231e15 `color.caviar`.

![Features headline default](components/crops/feat-h1-default.png)

### About

The /about/ masthead, a public page that loads signed out.

#### About headline
The /about/ masthead. A public page that loads signed out. Read as `about-h1` on the about page.

**Values (default).** size 365.89 x 48; background transparent; text Means Web 48/48 400, #231e15 `color.caviar`.

![About headline default](components/crops/about-h1-default.png)

### App log-in

login.mailchimp.com, a separate signed-out card. Measured, never submitted. Sign-in was not started.

#### Log-in card
The signed-out log-in card on login.mailchimp.com. A separate app from the marketing site. Nothing was submitted. Sign-in was not started. Read as `login-panel` on the app log-in page.

**Values (default).** size 422 x 453; background transparent; text Graphik Web 20/22 500, #21262a; layers a 140.2x20.0 B:1px solid rgb(1, 126, 137); input.rounded-corners-4.av-text 422.0x46.0 rgb(255, 255, 255) T:1px solid rgb(195, 206, 213) / R:1px solid rgb(195, 206, 213) / B:1px solid rgb(195, 206, 213) / L:1px solid rgb(195, 206, 213) 4px; button.identifier-first-login-btn.button-wide 422.0x36.0 rgb(1, 126, 137) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0.

Child layers that carry the look: a 140.2x20 border 1px solid #017e89; input 422x46 background #ffffff border 1px solid #c3ced5 radius 4px; button 422x36 background #017e89 border 1px solid transparent radius 4px.

![Log-in card default](components/crops/login-panel-default.png)

#### Username field
The Username or Email field. Focused and typed into with a placeholder, then cleared. Nothing was submitted. Read as `login-username` on the app log-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 422 x 46; padding 0px 15px; border 1px solid #c3ced5; radius 4px; background #ffffff; text Graphik Web 17/20 400, #21262a; transition all 0.2s ease-in-out; placeholder #21262a |
| focused, filled | border 1px solid #007c89; shadow #007c89 0px 0px 0px 1px inset |

![Username field default](components/crops/login-username-default.png) ![Username field focused](components/crops/login-username-focused.png) ![Username field filled](components/crops/login-username-filled.png)

#### Log in submit
The Log in submit. States were measured. The button was never clicked. Sign-in was not started. Read as `login-submit` on the app log-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 422 x 36; padding 0px 42px; border 1px solid transparent; radius 4px; background #017e89; text Graphik Web 14/34 500, #ffffff; transition background-color 0.2s ease-in-out, opacity 0.2s ease-in-out |
| hover | background #006771 |
| focus-visible | shadow #017e89 0px 0px 0px 1px inset |
| pressed | background #006771 |

![Log in submit default](components/crops/login-submit-default.png) ![Log in submit hover](components/crops/login-submit-hover.png) ![Log in submit focus-visible](components/crops/login-submit-focus-visible.png) ![Log in submit pressed](components/crops/login-submit-pressed.png)

#### Forgot username
A forgot-username or forgot-password link. Measured, never followed. Read as `login-forgot` on the app log-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 138 x 20; border B: 1px solid #017e89; background transparent; text Graphik Web 16/normal 500, #017e89; layers a 138.0x20.0 B:1px solid rgb(1, 126, 137) |
| hover | border B: 1px solid #004e56; text Graphik Web 16/normal 500, #004e56; layers a 138.0x20.0 B:1px solid rgb(0, 78, 86) |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a 138.0x20.0 B:1px solid rgb(1, 126, 137) 1px auto rgb(0, 95, 204) offset 1px |
| pressed | border B: 1px solid #004e56; text Graphik Web 16/normal 500, #004e56; layers a 138.0x20.0 B:1px solid rgb(0, 78, 86) |

Child layers that carry the look: a 138x20 border 1px solid #017e89.

![Forgot username default](components/crops/login-forgot-default.png) ![Forgot username hover](components/crops/login-forgot-hover.png) ![Forgot username focus-visible](components/crops/login-forgot-focus-visible.png) ![Forgot username pressed](components/crops/login-forgot-pressed.png)

#### Create an account
The Create an account link. Signup was not started and was not followed. Read as `login-create` on the app log-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 140.17 x 20; border B: 1px solid #017e89; background transparent; text Graphik Web 16/normal 500, #017e89; layers a 140.2x20.0 B:1px solid rgb(1, 126, 137) |
| hover | border B: 1px solid #004e56; text Graphik Web 16/normal 500, #004e56; layers a 140.2x20.0 B:1px solid rgb(0, 78, 86) |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a 140.2x20.0 B:1px solid rgb(1, 126, 137) 1px auto rgb(0, 95, 204) offset 1px |
| pressed | border B: 1px solid #004e56; text Graphik Web 16/normal 500, #004e56; layers a 140.2x20.0 B:1px solid rgb(0, 78, 86) |

Child layers that carry the look: a 140.2x20 border 1px solid #017e89.

![Create an account default](components/crops/login-create-default.png) ![Create an account hover](components/crops/login-create-hover.png) ![Create an account focus-visible](components/crops/login-create-focus-visible.png) ![Create an account pressed](components/crops/login-create-pressed.png)

### Mobile (390 wide)

The phone nav, Main Menu button, and hero at 390 wide.

#### Mobile nav
The phone nav bar. Read as `m-nav` on the home page at 390 wide.

**Values (default).** size 390 x 60; background transparent; text Tally 13/19.5 700, #231e15 `color.caviar`; layers nav.iaNav__nav 390.0x60.0 rgb(255, 255, 255); section::after.iaNav__panel.panel__top 100%x100% rgba(0, 0, 0, 0.16) 4px 8px 32px 0px; div.iaNav__panelContentHolder 0.0x0.0 rgb(255, 255, 255); div::after.iaNav__panelContent.flex 390pxx100% rgb(246, 246, 244); a::before.ctaArrow.cta--small autox32px rgb(255, 224, 27) 16px; span.badge.badge--square 0.0x0.0 rgb(35, 30, 21) rgba(0, 0, 0, 0.13) 0px 2px 4.

Child layers that carry the look: nav 390x60 background #ffffff; section::after 100%x100% shadow rgba(0, 0, 0, 0.16) 4px 8px 32px 0px; div 0x0 background #ffffff.

![Mobile nav default](components/crops/m-nav-default.png)

#### Mobile menu button
The Main Menu button. Opened locally. Links were never followed. Read as `m-menu` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 46 x 39.3; padding 8px; radius 3px; background transparent; text Tally 13/14.3 700, #231e15 `color.caviar`; transition background-color 0.15s ease; layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | background rgba(35, 30, 21, 0.05) |
| focus-visible | background rgba(35, 30, 21, 0.05); outline 2px solid #4bc4c2, offset 2px |
| pressed | background rgba(35, 30, 21, 0.05) |

![Mobile menu button default](components/crops/m-menu-default.png) ![Mobile menu button hover](components/crops/m-menu-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-pressed.png) ![Mobile menu button opened](components/crops/m-menu-opened.png)

#### Mobile hero
The home masthead at 390 wide. Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 343 x 93.59; background transparent; text Means Web 36/46.8 400, #ffffff.

![Mobile hero default](components/crops/m-hero-default.png)

### Footer

The page footer and a sitemap link.

#### Footer
The page footer: sitemap columns and legal links. Read as `footer` on the home page.

**Values (default).** size 1440 x 1041.78; padding 60px 0px; background #e7b75f; text Tally 16/24 400, #231e15 `color.caviar`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link. Measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 90.34 x 15; background transparent; text Tally 13/17.55 400, #231e15 `color.caviar` |
| hover | background rgba(255, 224, 27, 0.65); shadow rgba(255, 224, 27, 0.65) 0px 0px 0px 3.25px |
| focus-visible | background rgba(255, 224, 27, 0.65); shadow rgba(255, 224, 27, 0.65) 0px 0px 0px 3.25px; outline 2px solid #4bc4c2, offset 6.5px |
| pressed | background rgba(255, 224, 27, 0.65); shadow rgba(255, 224, 27, 0.65) 0px 0px 0px 3.25px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass. The wordmark and menu glyphs in the crops are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Mailchimp's product is the account and campaign builder behind login.mailchimp.com. Audiences, the email designer, automations, reports and billing need sign-in and were never reached. The log-in card at https://login.mailchimp.com/ was measured and never submitted. Sign-in was not started. Signup at https://login.mailchimp.com/signup/ was not started. Plan links on https://mailchimp.com/pricing/marketing/ point at signup with a plan query and were measured, never followed. Checkout was not started.

### Pages

- **The account.** Every post-login surface needs sign-in and was never reached. The log-in username field was typed into and cleared. Log in was never clicked.
- **Signup.** https://login.mailchimp.com/signup/ was not started and was not submitted.
- **Password reset.** Forgot username and forgot password are linked from the log-in card and were not followed.
- **Checkout and trial.** Plan links on https://mailchimp.com/pricing/marketing/ point at signup with a plan query and were measured, never followed. Checkout was not started.
- **Request a demo and Chat with Sales.** Linked from pricing. Neither form was submitted.
- **admin.mailchimp.com.** Redirects to the log-in card. The account was never reached.

### States

- **Pressed** was forced with DevTools on controls, so a scripted mousedown state is missing.
- **Disabled, error, loading and validation** were not seen. Forms were never submitted.

### Themes

The captured mailchimp.com pages have no theme toggle. Every page paints light. A Tailwind .dark class exists in the sheets and was not painted. The log-in card is also light, and it uses Graphik Web rather than the marketing Tally stack.

### Fonts

- **Means Web** draws display headlines. **Tally**, then **Graphik Web**, draws UI and body on mailchimp.com. **Graphik Web** draws the log-in card. The style guide falls back to system sans.

### Screenshots

- The product screenshots, brand logos and blog imagery in the captures are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article copy, integration names and the tool demos are the product's content; only frames and components were measured.
