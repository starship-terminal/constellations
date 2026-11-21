# Riverside components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from riverside.com on 2026-11-20, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent, submitted or uploaded. Login and Start for Free were measured and never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (26 components, 39 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (39 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [platform-menu](screenshots/home-light-platform-menu.png), [resources-menu](screenshots/home-light-resources-menu.png), [solutions-menu](screenshots/home-light-solutions-menu.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [monthly](screenshots/pricing-light-monthly.png) |
| Recording | `/recording` | [default](screenshots/recording-light-default.png), [full](screenshots/recording-light-full.png) |
| Editor | `/video-editor` | [default](screenshots/editor-light-default.png), [full](screenshots/editor-light-full.png) |
| Agents | `/agents` | [default](screenshots/agents-light-default.png), [full](screenshots/agents-light-full.png) |
| Business | `/business` | [default](screenshots/business-light-default.png), [full](screenshots/business-light-full.png) |
| FAQ | `/faq` | [default](screenshots/faq-light-default.png), [full](screenshots/faq-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Tools | `/tools` | [default](screenshots/tools-light-default.png), [full](screenshots/tools-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Login wall | `/login` | [wall](screenshots/login-light-wall.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Recording, phone | `/recording` | [default](screenshots/mobile-recording-light-default.png), [full](screenshots/mobile-recording-light-full.png) |
| FAQ, phone | `/faq` | [default](screenshots/mobile-faq-light-default.png), [full](screenshots/mobile-faq-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Platform menu | header | the Platform toggle opens a menu already in the DOM | [home-light-platform-menu](screenshots/home-light-platform-menu.png) |
| Solutions menu | header | the Solutions toggle opens a menu already in the DOM | [home-light-solutions-menu](screenshots/home-light-solutions-menu.png) |
| Resources menu | header | the Resources toggle opens a menu already in the DOM | [home-light-resources-menu](screenshots/home-light-resources-menu.png) |
| Pricing monthly | pricing | the Monthly control is a local toggle; checkout was not opened | [pricing-light-monthly](screenshots/pricing-light-monthly.png) |
| Login wall | /login | recorded and stopped; password was not submitted | [login-light-wall](screenshots/login-light-wall.png) |
| Mobile menu, open | home, phone | the hamburger's own toggle; Google One Tap was hidden, never clicked | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 5 components were given a real keyboard focus. 4 show a visible focus state: `nav-link` (1px auto #005fcc `measured.focus-ring`, offset 1px), `nav-login` (1px auto #005fcc `measured.focus-ring`, offset 1px), `nav-cta` (1px auto #005fcc `measured.focus-ring`, offset 1px), `footer-link` (1px auto #005fcc `measured.focus-ring`, offset 1px). The other 1 show no change a keyboard user can see: `m-menu-button`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): the controls shrink ~3% on press (a Webflow press transform); black CTAs keep their fill. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease` | background-color | login-email |
| 0.2s | `ease` | all | header |
| 0.25s | `ease` | all | m-nav-link, nav-link, nav-login |
| 0.275s | `ease` | all | nav-cta |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|

## Components

### Shell and navigation

The Webflow top bar: logo, dropdowns, Pricing, Login and the black Start for Free pill.

#### Header
The Webflow top bar: logo, Platform, Solutions, Resources, For Business, Pricing, Login, Start for Free. Read as `header` on the home page.

**Values (default).** size 1440 x 64; padding 12px 12px 12px 20px; background transparent; text Instrument Sans 20/32 400, #ffffff `color.paper.white`; transition all 0.2s ease; icon 13 x 8, #1d1d1d `color.ink.brand`.

Child layers that carry the look: a 210x40 background #000000 `color.ink.black`; div 1199.7x450.2 background #ffffff `color.paper.white` radius 8px shadow rgba(36, 36, 36, 0.08) 0px 12px 16px -4px, rgba(0, 0, 0, 0.2) 0px 4px 6px -2px; div 36.8x36.8 background rgba(150, 113, 255, 0.2) radius 8px.

![Header default](components/crops/header-default.png)

#### Logo
Read as `logo` on the home page.

**Values (default).** size 134.73 x 23.5; background transparent; text Instrument Sans 16/24.8 400, #333333.

![Logo default](components/crops/logo-default.png)

#### Nav dropdown
Platform toggle. Opens a menu already in the DOM. Measured, then closed. Read as `nav-dropdown` on the home page.

Not on the page when it was captured.

#### Platform menu
The opened Platform dropdown. Crop is the list. Read as `nav-menu` on the home page.

Not on the page when it was captured.

#### Nav link
Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 67.16 x 30; padding 8px 10px; background transparent; text Instrument Sans 14/14 500, #1d1d1d `color.ink.brand`; transition all 0.25s ease |
| hover | text Instrument Sans 14/14 500, rgba(29, 29, 29, 0.6) |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring`, offset 1px |
| pressed | text Instrument Sans 14/14 500, rgba(29, 29, 29, 0.6) |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Login link
Header Login. Measured, never followed. It opens the studio wall. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 55.31 x 14; padding 0px 9px; background transparent; text Instrument Sans 14/14 500, #1d1d1d `color.ink.brand`; transition all 0.25s ease |
| hover | text Instrument Sans 14/14 500, rgba(29, 29, 29, 0.6) |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring`, offset 1px |
| pressed | text Instrument Sans 14/14 500, rgba(29, 29, 29, 0.6) |

![Login link default](components/crops/nav-login-default.png) ![Login link hover](components/crops/nav-login-hover.png) ![Login link focus-visible](components/crops/nav-login-focus-visible.png) ![Login link pressed](components/crops/nav-login-pressed.png)

#### Start for Free
Header CTA. Measured, never followed. It opens the register wall. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 128 x 40; padding 11px; border 1px solid #1d1d1d `color.ink.brand`; radius 300px; background #1d1d1d `color.ink.brand`; text Instrument Sans 14/16 500, #ffffff `color.paper.white`; transition all 0.275s ease |
| hover | background #000000 `color.ink.black` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring`, offset 1px |
| pressed | text Instrument Sans 14/16 500, #d2d2d2 `color.muted.tech-text` |

![Start for Free default](components/crops/nav-cta-default.png) ![Start for Free hover](components/crops/nav-cta-hover.png) ![Start for Free focus-visible](components/crops/nav-cta-focus-visible.png) ![Start for Free pressed](components/crops/nav-cta-pressed.png)

### Home

The Sharp Grotesk hero over a dark photograph. The header bar stays a white field.

#### Hero title
Read as `hero-title` on the home page.

**Values (default).** size 730 x 150; background transparent; text Sharp Grotesk 60/75 400, #000000 `color.ink.black`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero CTA
The hero Start for Free. Measured, never followed. Read as `hero-cta` on the home page.

Not on the page when it was captured.

### Pricing

The plan page. Monthly and Yearly are a local toggle. Checkout was never opened.

#### Pricing title
Read as `pricing-title` on the pricing page.

**Values (default).** size 870 x 62.5; background transparent; text Sharp Grotesk 50/62.5 400, #1d1d1d `color.ink.brand`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Plan tab
The Pro pricing tab. A local UI state. Checkout was never opened. Read as `plan-tab` on the pricing page.

Not on the page when it was captured.

#### Plan panel
Read as `plan-card` on the pricing page.

**Values (default).** size 1440 x 2282.83; background #f7f7f7; text Sharp Grotesk 50/62.5 400, #1d1d1d `color.ink.brand`; icon 9 x 7, #1d1d1d `color.ink.brand`.

![Plan panel default](components/crops/plan-card-default.png)

### FAQ

The public FAQ page.

#### FAQ title
Read as `faq-title` on the faq page.

**Values (default).** size 1380 x 40; background transparent; text Sharp Grotesk 32/40 500, #181b21.

![FAQ title default](components/crops/faq-title-default.png)

### Blog

The blog index and its email field. The field was focused, never submitted.

#### Blog title
Read as `blog-title` on the blog page.

Not on the page when it was captured.

#### Blog card
A published post card. Measured, never followed in this pass. Read as `blog-card` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 671 x 80; background transparent; text Instrument Sans 32/40 400, #151c22 `color.ink.navy` |

![Blog card default](components/crops/blog-card-default.png) ![Blog card hover](components/crops/blog-card-hover.png)

#### Newsletter field
Focused only. Nothing typed. Nothing submitted. Read as `newsletter-field` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 334 x 52; padding 8px 24px; border 1px solid #e6e6e6; radius 5px; background #ffffff `color.paper.white`; text Instrument Sans 14/20 400, #1d1d1d `color.ink.brand`; placeholder rgba(29, 29, 29, 0.6) |
| focused | border 1px solid #7d7aff |

![Newsletter field default](components/crops/newsletter-field-default.png) ![Newsletter field focused](components/crops/newsletter-field-focused.png)

### Login wall

https://riverside.com/login. Email and password, or Google, Apple and Spotify SSO. Nothing was typed or clicked through.

#### Login title
Read as `login-title` on the login page.

**Values (default).** size 320 x 28; background transparent; text Sharp Grotesk Book 20/28 400, #fafafa.

![Login title default](components/crops/login-title-default.png)

#### Login email
Focused only. Nothing typed. Nothing submitted. Read as `login-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 40; padding 8px 12px; radius 8px; background #222222 `measured.login-field`; text Inter 14/normal 400, #fafafa; transition background-color 0.1s ease; placeholder #888888 `color.muted.c300` |
| focused | shadow #b196ff 0px 0px 0px 1px inset |

![Login email default](components/crops/login-email-default.png) ![Login email focused](components/crops/login-email-focused.png)

#### Login password
Focused only. Nothing typed. Nothing submitted. Read as `login-password` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 320 x 33; padding 8px 0px 8px 12px; background transparent; text Inter 14/normal 400, #fafafa; placeholder #888888 `color.muted.c300` |

![Login password default](components/crops/login-password-default.png) ![Login password focused](components/crops/login-password-focused.png)

#### SSO button
Visible on the wall. Never clicked. Read as `login-sso` on the login page.

**Values (default).** size 320 x 20; background transparent; text Inter 12/20 700, #b196ff `color.accent.purple-500`; icon 20 x 20, #b196ff `color.accent.purple-500`.

![SSO button default](components/crops/login-sso-default.png)

### Footer

Footer legal links on the dark band.

#### Footer legal link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 41.17 x 13; border B: 1px solid transparent; background transparent; text Instrument Sans 12/12 400, #c7c7c7 |
| hover | border B: 1px solid #c7c7c7 |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring`, offset 1px |
| pressed | border B: 1px solid rgba(199, 199, 199, 0.6); text Instrument Sans 12/12 400, rgba(199, 199, 199, 0.6) |

Child layers that carry the look: a 41.2x13 border 1px solid transparent.

![Footer legal link default](components/crops/footer-link-default.png) ![Footer legal link hover](components/crops/footer-link-hover.png) ![Footer legal link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer legal link pressed](components/crops/footer-link-pressed.png)

#### Footer social icon
Read as `footer-social` on the home page.

Not on the page when it was captured.

### Mobile (390 wide)

The same homepage at phone width, with the hamburger open.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 60; padding 14px 12px 14px 16px; background transparent; text Instrument Sans 20/32 400, #ffffff `color.paper.white`.

Child layers that carry the look: a 210x40 background #000000 `color.ink.black`; nav 0x0 background #fafafa radius 0px 0px 8px 8px; div 0x0 background #ffffff `color.paper.white`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 32 x 32; padding 2px; background transparent; text Instrument Sans 24/24.8 400, #1d1d1d `color.ink.brand` |

Child layers that carry the look: div::before 24pxx2px background #1d1d1d `color.ink.brand`; div::after 24pxx2px background #1d1d1d `color.ink.brand`.

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button hover](components/crops/m-menu-button-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The hamburger after its own toggle. Read as `m-menu-open` on the home page at 390 wide.

**Values (opened).** size 32 x 32; padding 2px; background transparent; text Instrument Sans 24/24.8 400, #ffffff `color.paper.white`.

Child layers that carry the look: div::before 20pxx2px background #1d1d1d `color.ink.brand` radius 10px; div::after 20pxx2px background #1d1d1d `color.ink.brand` radius 10px.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav link
Read inside the open menu. Read as `m-nav-link` on the home page at 390 wide.

**Values (default).** size 390 x 46; padding 16px 20px; background transparent; text Instrument Sans 14/14 500, #1d1d1d `color.ink.brand`; transition all 0.25s ease.

![Mobile nav link default](components/crops/m-nav-link-default.png)

## Icons

No standalone SVG icon set was lifted on this pass. The wordmark and glyphs in the screenshots are Riverside's artwork. icons/ is a layout gap.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The studio behind login.** https://riverside.com/login shows email and password, or Google, Apple and Spotify SSO. Password was not submitted. SSO was not clicked. https://riverside.com/dashboard and https://riverside.com/start (register) are the same wall. The recording room, editor and account were not reached.
- **Forms were not submitted.** Newsletter, demo, community, name-generator and file-upload fields were left empty. Cookie settings and Allow all cookies were not clicked.
- **Nav dropdowns** (Platform, Solutions, Resources) are screenshots of the open Webflow lists. Element crops of those lists were not measured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The site paints one light theme on every captured route: no dark class or attribute is bound, so the dark set is not emitted. The :root palette is recorded in [raw/css-vars.json](raw/css-vars.json).

### Fonts

- **The faces** are Sharp Grotesk for display and Instrument Sans for UI on the marketing pages. The login wall uses Inter and Sharp Grotesk Book. None of the proprietary faces are committed. The style guide falls back to system sans.
- Illustration, video stills and the wordmark in the screenshots are Riverside's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- Tall pages are stitched from tiles when they exceed one GPU texture. Home was recaptured after the first full shot collapsed to the viewport.

### Content left out

- Customer logos, product stills and the wordmark are Riverside's content. Only frames and components were measured.
