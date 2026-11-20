# Missive components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from missiveapp.com on 2026-11-20, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was sent, submitted or signed into.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (26 components, 57 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (57 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [demo](screenshots/home-light-demo.png), [full](screenshots/home-light-full.png), [product-menu](screenshots/home-light-product-menu.png), [resources-menu](screenshots/home-light-resources-menu.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [faq](screenshots/pricing-light-faq.png), [full](screenshots/pricing-light-full.png) |
| Features | `/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| Collaborate | `/collaborate` | [default](screenshots/collaborate-light-default.png), [full](screenshots/collaborate-light-full.png) |
| Integrations | `/integrations` | [default](screenshots/integrations-light-default.png), [full](screenshots/integrations-light-full.png) |
| AI assistant | `/ai-assistant` | [default](screenshots/ai-assistant-light-default.png), [full](screenshots/ai-assistant-light-full.png) |
| Customers | `/customers` | [default](screenshots/customers-light-default.png), [full](screenshots/customers-light-full.png) |
| Docs | `/docs` | [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Privacy | `/privacy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| French home | `/fr` | [default](screenshots/fr-home-light-default.png), [full](screenshots/fr-home-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Docs, phone | `/docs` | [default](screenshots/mobile-docs-light-default.png), [full](screenshots/mobile-docs-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Product menu, open | home | hover on Product | [home-light-product-menu](screenshots/home-light-product-menu.png) |
| Resources menu, open | home | hover on Resources | [home-light-resources-menu](screenshots/home-light-resources-menu.png) |
| Demo lightbox | home | Watch demo, not submitted | [home-light-demo](screenshots/home-light-demo.png) |
| Pricing FAQ, open | pricing | the accordion's own toggle | [pricing-light-faq](screenshots/pricing-light-faq.png) |
| Mobile menu, open | home, phone | the menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 9 components were given a real keyboard focus. 7 show a visible focus state: `nav-link` (1px auto #005fcc, offset 1px), `nav-login` (1px auto #005fcc, offset 1px), `nav-demo` (1px auto #005fcc, offset 1px), `nav-cta` (1px auto #005fcc, offset 1px), `hero-cta` (1px auto #005fcc, offset 1px), `footer-link` (1px auto #005fcc, offset 1px), `m-menu-button` (visible change in borderTopColor). The other 2 show no change a keyboard user can see: `flyout-trigger`, `faq-question`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): nothing that would submit, sign in or navigate was pressed. Log in, Try for free, plan CTAs and the form submits were measured, never followed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease-in-out` | padding | faq-open, faq-question |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Header](#header) | 1440 x 61 | - | 8px | #2266ed `color.swatch.blue.600` | none | 0 |
| [Hero title](#hero-title) | 768 x 120 | - | - | transparent | none | 0 |
| [Try for free](#try-for-free) | 99.22 x 44 | - | 8px | #2266ed `color.swatch.blue.600` | none | 12px |
| [Plan card](#plan-card) | 401 x 422 | 1px solid #e4e6e9 `color.swatch.neutral.100` | 16px 0px 0px 16px | - | none | 32px |
| [Docs search](#docs-search) | 337.77 x 37 | - | - | transparent | none | 8px |
| [Footer](#footer) | 1440 x 621 | 1px solid #34363a `color.swatch.neutral.900` | 12px | #16171a | none | 80px 32px |

## Components

### Shell and navigation

The desktop nav: logo, Product menu, Pricing, Customers, Resources, Log in, Book a demo, Try for free.

#### Header
The desktop nav: logo, Product, Pricing, Customers, Resources, Log in, Book a demo, Try for free. Read as `header` on the home page.

**Values (default).** size 1440 x 61; background transparent; text Inter 14/20 400, #34363a `color.swatch.neutral.900`.

Child layers that carry the look: div 1440x61 background #ffffff `color.swatch.white` border 1px solid #f5f6f6 `color.swatch.neutral.050`; nav 0x0 background #dddddd; div 0x0 background #ffffff `color.swatch.white` shadow #e4e6e9 `color.swatch.neutral.100` 0px 1px 1px 0px, rgba(0, 0, 0, 0.05) 0px 48px 56px -8px.

![Header default](components/crops/header-default.png)

#### Logo
Read as `logo` on the home page.

**Values (default).** size 144 x 36; background transparent; text Arial 14/20 400, #2266ed `color.swatch.blue.600`.

![Logo default](components/crops/logo-default.png)

#### Nav link
A top-level nav link. Measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 70 x 44; padding 12px; radius 8px; background transparent; text Inter 14/20 400, #34363a `color.swatch.neutral.900` |
| hover | background #f5f6f6 `color.swatch.neutral.050` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #e4e6e9 `color.swatch.neutral.100` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log in link
Opens the mail.missiveapp.com login wall. Measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 64.5 x 44; padding 12px; radius 8px; background transparent; text Inter 14/20 400, #34363a `color.swatch.neutral.900` |
| hover | background #f5f6f6 `color.swatch.neutral.050` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #e4e6e9 `color.swatch.neutral.100` |

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Book a demo
Opens an external Calendly page. Measured, never followed. Read as `nav-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 110.77 x 44; padding 12px; radius 8px; background transparent; text Inter 14/20 400, #34363a `color.swatch.neutral.900` |
| hover | background #f5f6f6 `color.swatch.neutral.050` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #e4e6e9 `color.swatch.neutral.100` |

![Book a demo default](components/crops/nav-demo-default.png) ![Book a demo hover](components/crops/nav-demo-hover.png) ![Book a demo focus-visible](components/crops/nav-demo-focus-visible.png) ![Book a demo pressed](components/crops/nav-demo-pressed.png)

#### Try for free
Opens the signup wall. Measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 99.22 x 44; padding 12px; radius 8px; background #2266ed `color.swatch.blue.600`; text Inter 14/20 500, #ffffff `color.swatch.white` |
| hover | image linear-gradient(rgba(0, 0, 0, 0.15), rgba(0, 0, 0, 0.15)) |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | image linear-gradient(rgba(0, 0, 0, 0.25), rgba(0, 0, 0, 0.25)) |

![Try for free default](components/crops/nav-cta-default.png) ![Try for free hover](components/crops/nav-cta-hover.png) ![Try for free focus-visible](components/crops/nav-cta-focus-visible.png) ![Try for free pressed](components/crops/nav-cta-pressed.png)

#### Product menu trigger
The nav item that opens the Product mega menu. Read as `flyout-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 95.81 x 44; padding 12px; radius 8px; background transparent; text Inter 14/20 400, #34363a `color.swatch.neutral.900`; icon 16 x 16, #34363a `color.swatch.neutral.900` |
| hover | background #f5f6f6 `color.swatch.neutral.050` |
| pressed | background #e4e6e9 `color.swatch.neutral.100` |

![Product menu trigger default](components/crops/flyout-trigger-default.png) ![Product menu trigger hover](components/crops/flyout-trigger-hover.png) ![Product menu trigger focus-visible](components/crops/flyout-trigger-focus-visible.png) ![Product menu trigger pressed](components/crops/flyout-trigger-pressed.png)

#### Product menu, open
The Product mega menu after hover. Links are recorded in site-tree.md and not followed here. Read as `flyout-open` on the home page.

**Values (opened).** size 95.81 x 44; padding 12px; radius 8px; background #f5f6f6 `color.swatch.neutral.050`; text Inter 14/20 400, #34363a `color.swatch.neutral.900`; icon 16 x 16, #34363a `color.swatch.neutral.900`.

![Product menu, open opened](components/crops/flyout-open-opened.png)

### Home

The landing: serif hero, blue primary CTA, grey Watch demo, feature tabs, story cards.

#### Hero title
Read as `hero-title` on the home page.

**Values (default).** size 768 x 120; background transparent; text Tiempos Headline 56/60 400, #34363a `color.swatch.neutral.900`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero CTA
The hero Try for free. Measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 143.84 x 52; padding 16px 24px; radius 8px; background #2266ed `color.swatch.blue.600`; text Inter 17.84/20 500, #ffffff `color.swatch.white` |
| hover | image linear-gradient(rgba(0, 0, 0, 0.15), rgba(0, 0, 0, 0.15)) |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | image linear-gradient(rgba(0, 0, 0, 0.25), rgba(0, 0, 0, 0.25)) |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Watch demo
Opens the on-page demo lightbox. Measured, not submitted. Read as `hero-secondary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 156.89 x 54; padding 16px 24px; border 1px solid #e4e6e9 `color.swatch.neutral.100`; radius 8px; background #f5f6f6 `color.swatch.neutral.050`; text Inter 17.84/20 500, #34363a `color.swatch.neutral.900` |
| hover | border 1px solid #cdd0d4 `color.swatch.neutral.200`; image linear-gradient(rgba(0, 0, 0, 0.03), rgba(0, 0, 0, 0.03)) |

![Watch demo default](components/crops/hero-secondary-default.png) ![Watch demo hover](components/crops/hero-secondary-hover.png)

#### Section heading
Read as `section-title` on the home page.

**Values (default).** size 626.23 x 36; background transparent; text Inter 30/36 400, #34363a `color.swatch.neutral.900`.

![Section heading default](components/crops/section-title-default.png)

#### Feature tab
An in-page tab. Selecting it does not navigate. Read as `tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 592 x 174; padding 16px; border 1px solid #ffffff `color.swatch.white`; radius 24px; background transparent; text Inter 20/28 500, #34363a `color.swatch.neutral.900`; icon 24 x 24, #34363a `color.swatch.neutral.900` |
| hover | border 1px solid #e4e6e9 `color.swatch.neutral.100`; background #ffffff `color.swatch.white` |

![Feature tab default](components/crops/tab-default.png) ![Feature tab hover](components/crops/tab-hover.png)

#### Customer story card
A story card. Measured, not opened in this pass. Read as `card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 143.53 x 54; padding 16px 24px; border 1px solid #e4e6e9 `color.swatch.neutral.100`; radius 8px; background #f5f6f6 `color.swatch.neutral.050`; text Inter 17.84/20 500, #34363a `color.swatch.neutral.900` |
| hover | border 1px solid #cdd0d4 `color.swatch.neutral.200`; image linear-gradient(rgba(0, 0, 0, 0.03), rgba(0, 0, 0, 0.03)) |

![Customer story card default](components/crops/card-default.png) ![Customer story card hover](components/crops/card-hover.png)

### Pricing

Plan columns and the FAQ accordion. Plan CTAs go to the signup wall and were not followed.

#### Pricing title
Read as `pricing-title` on the pricing page.

**Values (default).** size 708.42 x 60; background transparent; text Tiempos Headline 56/60 400, #34363a `color.swatch.neutral.900`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Plan card
A pricing plan column. Its CTA goes to the signup wall and is not followed. Read as `plan-card` on the pricing page.

**Values (default).** size 401 x 422; padding 32px; border 1px solid #e4e6e9 `color.swatch.neutral.100`; radius 16px 0px 0px 16px; background transparent; text Inter 30/36 400, #34363a `color.swatch.neutral.900`; icon 16 x 16, #333333.

![Plan card default](components/crops/plan-card-default.png)

#### FAQ question
Read as `faq-question` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 800 x 60; padding 16px; background transparent; text Inter 20/28 500, #34363a `color.swatch.neutral.900`; transition padding 0.2s ease-in-out; icon 24 x 24, #34363a `color.swatch.neutral.900` |
| hover, pressed | padding 16px 16px 16px 24px; radius 16px; background #f5f6f6 `color.swatch.neutral.050` |

![FAQ question default](components/crops/faq-question-default.png) ![FAQ question hover](components/crops/faq-question-hover.png) ![FAQ question focus-visible](components/crops/faq-question-focus-visible.png) ![FAQ question pressed](components/crops/faq-question-pressed.png)

#### FAQ, open
The pricing FAQ after its own toggle. Read as `faq-open` on the pricing page.

**Values (opened).** size 800 x 60; padding 16px 16px 16px 24px; radius 16px; background #f5f6f6 `color.swatch.neutral.050`; text Inter 20/28 500, #34363a `color.swatch.neutral.900`; transition padding 0.2s ease-in-out; icon 33.94 x 33.94, #34363a `color.swatch.neutral.900`.

![FAQ, open opened](components/crops/faq-open-opened.png)

### Docs

The public help center: a search field and a chat field, focused, never submitted.

#### Docs title
Read as `docs-title` on the docs page.

**Values (default).** size 768 x 45; background transparent; text Inter 36/45 700, #1d1d1e.

![Docs title default](components/crops/docs-title-default.png)

#### Docs search
Focused only. Nothing typed, nothing submitted. Read as `docs-search` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 337.77 x 37; padding 8px; background transparent; text Inter 14/21 400, #1d1d1e; placeholder oklab(0.537428 -0.00104021 -0.0051524 / 0.72) |
| focused | size 379.77 x 37 |

![Docs search default](components/crops/docs-search-default.png) ![Docs search focused](components/crops/docs-search-focused.png)

### Footer

Link columns, legal, language switch.

#### Footer
Read as `footer` on the home page.

**Values (default).** size 1440 x 621; padding 80px 32px; border T: 1px solid #34363a `color.swatch.neutral.900`; background #050607 `color.swatch.neutral.1000`; text Inter 16/24 500, #ffffff `color.swatch.white`; icon 16 x 16, #34363a `color.swatch.neutral.900`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 65.52 x 24; background transparent; text Inter 16/24 400, #cdd0d4 `color.swatch.neutral.200` |
| hover | text Inter 16/24 400, #e4e6e9 `color.swatch.neutral.100` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Mobile (390 wide)

The phone nav and the opened menu.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 57; background transparent; text Inter 14/20 400, #34363a `color.swatch.neutral.900`.

Child layers that carry the look: div 390x57 background #ffffff `color.swatch.white` border 1px solid #f5f6f6 `color.swatch.neutral.050`; a 74.5x36 background #2266ed `color.swatch.blue.600` radius 8px; nav 0x0 background #dddddd.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 40 x 40; padding 8px; radius 8px; background transparent; text Arial 14/20 400, #222222; icon 24 x 24, #34363a `color.swatch.neutral.900` |
| hover, pressed | background #f5f6f6 `color.swatch.neutral.050` |

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button hover](components/crops/m-menu-button-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The phone menu after its own toggle. Read as `m-menu-open` on the home page at 390 wide.

**Values (opened).** size 40 x 40; padding 8px; radius 8px; background #f5f6f6 `color.swatch.neutral.050`; text Arial 14/20 400, #222222.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav link
Read inside the open menu. Read as `m-nav-link` on the home page at 390 wide.

**Values (default).** size 76.09 x 44; padding 8px; background transparent; text Inter 18/28 500, #34363a `color.swatch.neutral.900`.

![Mobile nav link default](components/crops/m-nav-link-default.png)

## Icons

No standalone SVG icon set was lifted. The wordmark and icons stay in the screenshots. This package has no `icons/` folder. The catalog was not edited, so that gap is recorded here and in the README.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **Login wall.** https://mail.missiveapp.com/#login asks for a work email and password, or Google, Apple, or SSO. That branch was not entered. Try for free and Sign up go to #signup and were not followed.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading, selected, checkbox, radio, switch, toast and table** were not on the public marketing surface.

### Themes

The site paints one light theme. No dark theme switch and no dark custom-property set were found. Ketch consent variables (`--k-*`) are vendor and are not product tokens. The product token layer is in [raw/css-vars.json](raw/css-vars.json).

### Fonts

- **Inter** is the UI face and **Tiempos Headline** is the display face. Both are webfonts the site loads. The files are not committed. The style guide names the stacks and falls back to system fonts.
- Product imagery and the Missive wordmark in the screenshots are Missive's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- Full-page shots taller than 12000 px were capped after the stitch: changelog, compare, features, mobile-features, and mobile-home. The viewport shots of those pages are complete.

### Content left out

- Product imagery and the wordmark are Missive's content; only the frames and components were measured.
- The home feature-tab screenshot timed out. The three panes are mapped in [site-tree.md](site-tree.md) and were not captured as a separate state.
- `flyout-open` and `m-menu-open` measured the trigger, not the open panel. The open panels are in [home-light-product-menu](screenshots/home-light-product-menu.png) and [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).
- `card` matched a small chip, not a customer-story card. Story cards are in the home and customers screenshots.
- The docs chat field was not measured. The docs search field was. Neither was submitted.
- Radius, shadow and motion are computed styles. The site does not declare those as custom properties.
- Sitemap copies (blog, changelog, stories, integrations, partners, compare, French) are one template each, not every URL.
