# Appwrite components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from appwrite.io on 2026-11-21, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (60 components, 161 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (162 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-dark-{state}.png`: the marketing site pins the dark theme on every captured route. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-dark-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-dark-default.png), [faq](screenshots/pricing-dark-faq.png), [full](screenshots/pricing-dark-full.png) |
| Product: Databases | `/products/databases` | [default](screenshots/product-dark-default.png), [full](screenshots/product-dark-full.png) |
| Docs home | `/docs` | [default](screenshots/docs-dark-default.png), [full](screenshots/docs-dark-full.png) |
| Docs: Start with React | `/docs/quick-starts/react` | [default](screenshots/docs-react-dark-default.png), [full](screenshots/docs-react-dark-full.png) |
| Blog | `/blog` | [default](screenshots/blog-dark-default.png), [full](screenshots/blog-dark-full.png) |
| Changelog | `/changelog` | [default](screenshots/changelog-dark-default.png), [full](screenshots/changelog-dark-full.png) |
| Integrations | `/integrations` | [default](screenshots/integrations-dark-default.png), [full](screenshots/integrations-dark-full.png) |
| Company | `/company` | [default](screenshots/company-dark-default.png), [full](screenshots/company-dark-full.png) |
| Brand assets | `/assets` | [default](screenshots/assets-dark-default.png), [full](screenshots/assets-dark-full.png) |
| Enterprise | `/enterprise` | [default](screenshots/enterprise-dark-default.png), [full](screenshots/enterprise-dark-full.png) |
| Startups | `/startups` | [default](screenshots/startups-dark-default.png), [full](screenshots/startups-dark-full.png) |
| Sign in | `/sign-in` | [default](screenshots/sign-in-dark-default.png), [full](screenshots/sign-in-dark-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png), [menu](screenshots/mobile-home-dark-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-dark-default.png), [full](screenshots/mobile-pricing-dark-full.png) |
| Docs quick-start, phone | `/docs/quick-starts/react` | [default](screenshots/mobile-docs-react-dark-default.png), [full](screenshots/mobile-docs-react-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Nav flyout, open | header, every page | the Products button's own toggle | [nav-menu-open](#nav-flyout-open) |
| Pricing FAQ, open | pricing | the accordion's own toggle | [faq-open](#faq-accordion-open), [pricing-dark-faq](screenshots/pricing-dark-faq.png) |
| Mobile menu sheet | home, phone | the menu button's own toggle | [m-menu-open](#mobile-menu-open), [mobile-home-dark-menu](screenshots/mobile-home-dark-menu.png) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 34 components were given a real keyboard focus. 17 draw an outline ring: `banner-dismiss` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 0px), `nav-link` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px), `nav-menu-button` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 0px), `nav-github` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px), `framework-icon` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px), `faq-question` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 0px), `compare-link` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px), `docs-search` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 0px), `docs-prose-link` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px), `author-link` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px), `blog-search` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 0px), `category-chip` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px), `forgot-link` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px), `tos-link` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px), `m-menu-button` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 0px), `footer-link` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px), `footer-social` (1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px). 16 draw a focus ring as a shadow instead: `signin-button`, `signup-button`, `announcement-pill`, `cta-primary`, `cta-secondary`, `product-card`, `plan-cta`, `plan-cta-contact`, `docs-nav-link`, `oauth-button`, `oauth-icon-button`, `google-button`, `passkey-button`, `show-password`, `login-button`, `m-cta-primary`. The other 1 show no measured change: `skip-link`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): controls deepen their fill or dim rather than scale; the nav flyout and framework icons keep their hover scale. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0, 0, 0.2, 1)` | rotate, scale, transform, translate | logo |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, box-shadow, color, fill, outline-color, stroke, text-decoration-color | announcement-pill, banner-dismiss, blog-search, cta-primary, cta-secondary, docs-nav-active, docs-nav-link, docs-prose-link and more |
| 0.15s | `ease` | color, text-decoration-color | compare-link, forgot-link, tos-link |
| 0.2s | `cubic-bezier(0, 0, 0.2, 1)` | opacity, transform | skip-link |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | rotate, scale, transform, translate | framework-icon |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 358.97 x 923.5 | 1px solid oklab(0.298707 0.00198022 -0.00687116 / 0.3) | 14px | oklab(0.298707 0.00198022 -0.00687116 / 0.08) | rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px | 28px |
| [Post card](#post-card) | 1232 x 333 | 1px solid lab(13.1873 0.517011 -1.80675) | 3.35544e+07px | #2d2d31 | none | 0 |
| [Product card](#product-card) | 430.33 x 379 | - | - | transparent | none | 0 |
| [Sign-in card](#sign-in-card) | 896 x 687.5 | 1px solid lab(13.1873 0.517011 -1.80675) | 14px | #1d1d21 | none | 0 |

## Components

### Shell and navigation

The fixed dark bar over every marketing page and the strip above it.

#### Announcement banner
The strip above the header carrying the current announcement and a dismiss button. Read as `banner` on the marketing home page.

Not on the page when it was captured.

#### Banner dismiss button
Read as `banner-dismiss` on the marketing home page.

Not on the page when it was captured.

#### Top bar
The fixed glass bar over every marketing page: logo, Products/Solutions flyout buttons, section links, GitHub stars, Sign in/up. Read as `header` on the marketing home page.

**Values (default).** size 1440 x 56; padding 0px 24px 0px 16px; border B: 1px solid lab(13.1873 0.517011 -1.80675); background #19191c; text -apple-system 13/19.5 500, lab(65.6464 1.53497 -5.42429).

![Top bar default](components/crops/header-default.png)

#### Logo
Read as `logo` on the marketing home page.

**Values (default).** size 126 x 40; padding 0px 8px; radius 10px; background transparent; text -apple-system 16/24 400, lab(98.26 0 0); transition transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1); icon 110 x 20, lab(98.26 0 0).

![Logo default](components/crops/logo-default.png)

#### Nav link
A top-level destination in the bar: 13px text in a 36px rounded-md row. Read as `nav-link` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 63.11 x 36; padding 0px 10px; radius 8px; background transparent; text -apple-system 13/19.5 500, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #2d2d31; text -apple-system 13/19.5 500, lab(98.26 0 0) |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px |
| pressed | background #2d2d31; text -apple-system 13/19.5 500, lab(98.26 0 0) |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Nav flyout button
Products and Solutions open a flyout; measured at rest, never opened (the flyout is captured in screenshots only when it mounts open). Read as `nav-menu-button` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 93.88 x 36; padding 0px 10px; radius 8px; background transparent; text -apple-system 13/19.5 500, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, lab(65.6464 1.53497 -5.42429) |
| hover | background #2d2d31; text -apple-system 13/19.5 500, lab(98.26 0 0); icon 14 x 14, lab(98.26 0 0) |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 0px |
| pressed | background #2d2d31; text -apple-system 13/19.5 500, lab(98.26 0 0); icon 14 x 14, lab(98.26 0 0) |

![Nav flyout button default](components/crops/nav-menu-button-default.png) ![Nav flyout button hover](components/crops/nav-menu-button-hover.png) ![Nav flyout button focus-visible](components/crops/nav-menu-button-focus-visible.png) ![Nav flyout button pressed](components/crops/nav-menu-button-pressed.png)

#### Nav flyout, open
The button after its own flyout toggle: the opened panel underneath (a popover-foreground div the toggle mounts) is what the crop shows. Read as `nav-menu-open` on the marketing home page.

**Values (opened).** size 93.88 x 36; padding 0px 10px; radius 8px; background #2d2d31; text -apple-system 13/19.5 500, lab(98.26 0 0); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, lab(98.26 0 0).

![Nav flyout, open opened](components/crops/nav-menu-open-opened.png)

#### GitHub stars link
The star-count link to the repo. Read as `nav-github` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 79.05 x 36; padding 0px 10px; radius 8px; background transparent; text -apple-system 13/19.5 500, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(65.6464 1.53497 -5.42429) |
| hover | background #2d2d31; text -apple-system 13/19.5 500, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |
| focus-visible | background #2d2d31; outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px; text -apple-system 13/19.5 500, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |
| pressed | background #2d2d31; text -apple-system 13/19.5 500, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |

![GitHub stars link default](components/crops/nav-github-default.png) ![GitHub stars link hover](components/crops/nav-github-hover.png) ![GitHub stars link focus-visible](components/crops/nav-github-focus-visible.png) ![GitHub stars link pressed](components/crops/nav-github-pressed.png)

#### Sign in button
Ghost-style header action. Measured, never followed. Read as `signin-button` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 67.88 x 36; padding 0px 12px; border 1px solid #2d2d31; radius 8px; background transparent; text -apple-system 13/19.5 500, lab(65.6464 1.53497 -5.42429); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #2d2d31; text -apple-system 13/19.5 500, lab(98.26 0 0) |
| focus-visible | shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |
| pressed | background #2d2d31; text -apple-system 13/19.5 500, lab(98.26 0 0) |

![Sign in button default](components/crops/signin-button-default.png) ![Sign in button hover](components/crops/signin-button-hover.png) ![Sign in button focus-visible](components/crops/signin-button-focus-visible.png) ![Sign in button pressed](components/crops/signin-button-pressed.png)

#### Sign up button
The filled header action. Measured, never followed. Read as `signup-button` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 72.59 x 36; padding 0px 12px; border 1px solid transparent; radius 8px; background #fd366e; text -apple-system 13/19.5 500, #ffffff; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.9 |
| focus-visible | border 1px solid lab(35.8321 1.55474 -5.40724); shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |
| pressed | opacity 0.9 |

![Sign up button default](components/crops/signup-button-default.png) ![Sign up button hover](components/crops/signup-button-hover.png) ![Sign up button focus-visible](components/crops/signup-button-focus-visible.png) ![Sign up button pressed](components/crops/signup-button-pressed.png)

#### Skip link
The off-screen accessibility link, revealed by keyboard focus. Read as `skip-link` on the marketing home page.

**Values (focus-visible).** size 127.98 x 41.5; padding 10px 16px; border 1px solid lab(13.1873 0.517011 -1.80675); radius 14px; background #19191c; shadow #19191c 0px 0px 0px 2px, lab(35.8321 1.55474 -5.40724) 0px 0px 0px 4px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px; text -apple-system 13/19.5 500, lab(98.26 0 0); transition opacity 0.2s cubic-bezier(0, 0, 0.2, 1), transform 0.2s cubic-bezier(0, 0, 0.2, 1).

![Skip link focus-visible](components/crops/skip-link-focus-visible.png)

### Home

The hero and product grid of appwrite.io.

#### Announcement pill
The "Breaking" link pill under the hero. Read as `announcement-pill` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 347.88 x 28; padding 0px 10px; border 1px solid #2d2d31; radius 3.35544e+07px; background transparent; text -apple-system 12/18 500, #fd366e; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, lab(65.6464 1.53497 -5.42429) |
| hover | background #2d2d31; icon 14 x 14, lab(98.26 0 0) |
| focus-visible | shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |
| pressed | background #2d2d31; icon 14 x 14, lab(98.26 0 0) |

![Announcement pill default](components/crops/announcement-pill-default.png) ![Announcement pill hover](components/crops/announcement-pill-hover.png) ![Announcement pill focus-visible](components/crops/announcement-pill-focus-visible.png) ![Announcement pill pressed](components/crops/announcement-pill-pressed.png)

#### Hero title
The 48px Aeonik headline with the brand gradient text. Read as `hero-title` on the marketing home page.

**Values (default).** size 870.05 x 164.14; padding 0px 5.7px 6.08px 0px; background transparent; image linear-gradient(145deg, oklch(0.804466 0.127483 10.8203) 0%, oklch(0.696146 0.203958 10.8203) 28%, lab(98.26 0 0) 62%); text Aeonik Pro 76/79.04 400, transparent.

![Hero title default](components/crops/hero-title-default.png)

#### Primary CTA
"Start project": the main action, brand pink. Measured, never followed. Read as `cta-primary` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 132.94 x 40; padding 0px 24px; border 1px solid transparent; radius 8px; background #fd366e; text -apple-system 14/21 500, #ffffff; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.9 |
| focus-visible | border 1px solid lab(35.8321 1.55474 -5.40724); shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |
| pressed | opacity 0.9 |

![Primary CTA default](components/crops/cta-primary-default.png) ![Primary CTA hover](components/crops/cta-primary-hover.png) ![Primary CTA focus-visible](components/crops/cta-primary-focus-visible.png) ![Primary CTA pressed](components/crops/cta-primary-pressed.png)

#### Secondary CTA
"View docs": the quiet sibling. Measured, never followed. Read as `cta-secondary` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 117.72 x 40; padding 0px 24px; border 1px solid #2d2d31; radius 8px; background transparent; text -apple-system 14/21 500, lab(65.6464 1.53497 -5.42429); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #2d2d31; text -apple-system 14/21 500, lab(98.26 0 0) |
| focus-visible | shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |
| pressed | background #2d2d31; text -apple-system 14/21 500, lab(98.26 0 0) |

![Secondary CTA default](components/crops/cta-secondary-default.png) ![Secondary CTA hover](components/crops/cta-secondary-hover.png) ![Secondary CTA focus-visible](components/crops/cta-secondary-focus-visible.png) ![Secondary CTA pressed](components/crops/cta-secondary-pressed.png)

#### Framework icon button
One of the 36px round framework icons under the hero strip. Read as `framework-icon` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; background transparent; text -apple-system 16/24 400, lab(98.26 0 0); transition transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), translate 0.2s cubic-bezier(0.4, 0, 0.2, 1), scale 0.2s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | size 39.6 x 39.6 |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px |
| pressed | size 39.6 x 39.6 |

![Framework icon button default](components/crops/framework-icon-default.png) ![Framework icon button hover](components/crops/framework-icon-hover.png) ![Framework icon button focus-visible](components/crops/framework-icon-focus-visible.png) ![Framework icon button pressed](components/crops/framework-icon-pressed.png)

#### Product card
A services-grid card (Auth/Databases/...): the overlay link covers the whole card, so the card edges are what the crop shows; painted fills come from the ancestors row. Read as `product-card` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 430.33 x 379; background transparent; text -apple-system 16/24 400, lab(98.26 0 0) |
| focus-visible | shadow #19191c 0px 0px 0px 2px, lab(35.8321 1.55474 -5.40724) 0px 0px 0px 4px |

![Product card default](components/crops/product-card-default.png) ![Product card hover](components/crops/product-card-hover.png) ![Product card focus-visible](components/crops/product-card-focus-visible.png)

#### Section headline
The 40px Aeonik section title. Read as `section-title` on the marketing home page.

**Values (default).** size 768 x 96; background transparent; text Aeonik Pro 48/48 400, lab(98.26 0 0).

![Section headline default](components/crops/section-title-default.png)

### Pricing

The plan columns and the FAQ accordion.

#### Pricing title
Read as `pricing-title` on the pricing page.

**Values (default).** size 768 x 132; background transparent; text Aeonik Pro 44/66 400, lab(98.26 0 0).

![Pricing title default](components/crops/pricing-title-default.png)

#### Plan card
One pricing column: name, price, feature list and its own CTA; an <article> with the muted-tint fill and hairline border. Read as `plan-card` on the pricing page.

**Values (default).** size 358.97 x 923.5; padding 28px; border 1px solid oklab(0.298707 0.00198022 -0.00687116 / 0.3); radius 14px; background oklab(0.298707 0.00198022 -0.00687116 / 0.08); shadow rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px; text -apple-system 14/21 600, lab(98.26 0 0); icon 16 x 16, #fd366e.

![Plan card default](components/crops/plan-card-default.png)

#### Plan price
Read as `plan-price` on the pricing page.

**Values (default).** size 37.58 x 48; background transparent; text Aeonik Pro 32/48 400, lab(98.26 0 0).

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
The per-card action. Measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 300.97 x 40; padding 8px 16px; border 1px solid #2d2d31; radius 8px; background transparent; text -apple-system 13/19.5 500, lab(65.6464 1.53497 -5.42429); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #2d2d31; text -apple-system 13/19.5 500, lab(98.26 0 0) |
| focus-visible | shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |
| pressed | background #2d2d31; text -apple-system 13/19.5 500, lab(98.26 0 0) |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Enterprise CTA
"Contact us" on the Enterprise card. Measured, never followed. Read as `plan-cta-contact` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 300.98 x 40; padding 8px 16px; border 1px solid #2d2d31; radius 8px; background transparent; text -apple-system 13/19.5 500, lab(65.6464 1.53497 -5.42429); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #2d2d31; text -apple-system 13/19.5 500, lab(98.26 0 0) |
| focus-visible | shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |
| pressed | background #2d2d31; text -apple-system 13/19.5 500, lab(98.26 0 0) |

![Enterprise CTA default](components/crops/plan-cta-contact-default.png) ![Enterprise CTA hover](components/crops/plan-cta-contact-hover.png) ![Enterprise CTA focus-visible](components/crops/plan-cta-contact-focus-visible.png) ![Enterprise CTA pressed](components/crops/plan-cta-contact-pressed.png)

#### FAQ accordion button
Read as `faq-question` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 8px; background transparent; text -apple-system 16/24 400, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #2d2d31; text -apple-system 16/24 400, lab(98.26 0 0) |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 0px |
| pressed | background #2d2d31; text -apple-system 16/24 400, lab(98.26 0 0) |

Child layers that carry the look: span 16x16 background lab(65.6464 1.53497 -5.42429).

![FAQ accordion button default](components/crops/faq-question-default.png) ![FAQ accordion button hover](components/crops/faq-question-hover.png) ![FAQ accordion button focus-visible](components/crops/faq-question-focus-visible.png) ![FAQ accordion button pressed](components/crops/faq-question-pressed.png)

#### FAQ accordion, open
The same item after its own toggle; the answer region shows in the crop. Read as `faq-open` on the pricing page.

**Values (opened).** size 32 x 32; radius 8px; background #2d2d31; text -apple-system 16/24 400, lab(98.26 0 0); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![FAQ accordion, open opened](components/crops/faq-open-opened.png)

#### Compare plans link
link-neutral text link. Read as `compare-link` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 93.03 x 16; background transparent; text -apple-system 13/20 500, oklch(0.984998 0.000024917 none / 0.85); transition text-decoration-color 0.15s ease, color 0.15s ease |
| hover | text -apple-system 13/20 500, lab(98.26 0 0) |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px |
| pressed | text -apple-system 13/20 500, lab(98.26 0 0) |

![Compare plans link default](components/crops/compare-link-default.png) ![Compare plans link hover](components/crops/compare-link-hover.png) ![Compare plans link focus-visible](components/crops/compare-link-focus-visible.png) ![Compare plans link pressed](components/crops/compare-link-pressed.png)

### Docs

The quick-start page's sidebar, prose and code.

#### Docs search button
The command-K search trigger in the docs header. Measured, never opened. Read as `docs-search` on the docs quick-start page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 36; padding 0px 12px; border 1px solid lab(13.1873 0.517011 -1.80675); radius 8px; background oklab(0.298707 0.00198022 -0.00687116 / 0.5); text -apple-system 13/19.5 400, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, lab(65.6464 1.53497 -5.42429) |
| hover | background #2d2d31 |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 0px |
| pressed | background #2d2d31 |

![Docs search button default](components/crops/docs-search-default.png) ![Docs search button hover](components/crops/docs-search-hover.png) ![Docs search button focus-visible](components/crops/docs-search-focus-visible.png) ![Docs search button pressed](components/crops/docs-search-pressed.png)

#### Docs sidebar link
Read as `docs-nav-link` on the docs quick-start page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 195 x 31.5; padding 6px 10px; radius 8px; background transparent; text -apple-system 13/19.5 500, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(65.6464 1.53497 -5.42429) |
| hover | background oklab(0.298707 0.00198022 -0.00687116 / 0.5); text -apple-system 13/19.5 500, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |
| focus-visible | shadow #19191c 0px 0px 0px 1px, lab(35.8321 1.55474 -5.40724) 0px 0px 0px 3px |
| pressed | background oklab(0.298707 0.00198022 -0.00687116 / 0.5); text -apple-system 13/19.5 500, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |

![Docs sidebar link default](components/crops/docs-nav-link-default.png) ![Docs sidebar link hover](components/crops/docs-nav-link-hover.png) ![Docs sidebar link focus-visible](components/crops/docs-nav-link-focus-visible.png) ![Docs sidebar link pressed](components/crops/docs-nav-link-pressed.png)

#### Docs sidebar item, current
The item the page marks current, if any. Read as `docs-nav-active` on the docs quick-start page.

**Values (default).** size 195 x 31.5; padding 6px 10px; radius 8px; background transparent; text -apple-system 13/19.5 500, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(65.6464 1.53497 -5.42429).

![Docs sidebar item, current default](components/crops/docs-nav-active-default.png)

#### Code block
The framed snippet on a quick-start page, with --code-* syntax colours. Read as `code-block` on the docs quick-start page.

**Values (default).** size 621 x 74.88; padding 16px; background transparent; text source-code-pro 13/21.45 400, #67a3fe.

![Code block default](components/crops/code-block-default.png)

#### Inline code
Read as `code-inline` on the docs quick-start page.

**Values (default).** size 83.77 x 21; padding 2px 6px; border 1px solid lab(13.1873 0.517011 -1.80675); radius 8px; background oklab(0.298707 0.00198022 -0.00687116 / 0.5); text source-code-pro 13/21.45 400, oklab(0.984998 -0.00000956655 0.0000230074 / 0.85).

![Inline code default](components/crops/code-inline-default.png)

#### Prose link
Read as `docs-prose-link` on the docs quick-start page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 97.53 x 15; background transparent; text -apple-system 12/18 600, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text -apple-system 12/18 600, oklab(0.984998 -0.00000956655 0.0000230074 / 0.85) |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px |
| pressed | text -apple-system 12/18 600, oklab(0.984998 -0.00000956655 0.0000230074 / 0.85) |

![Prose link default](components/crops/docs-prose-link-default.png) ![Prose link hover](components/crops/docs-prose-link-hover.png) ![Prose link focus-visible](components/crops/docs-prose-link-focus-visible.png) ![Prose link pressed](components/crops/docs-prose-link-pressed.png)

#### Docs page title
Read as `docs-h1` on the docs quick-start page.

**Values (default).** size 599 x 45; background transparent; text Aeonik Pro 36/45 400, lab(98.26 0 0).

![Docs page title default](components/crops/docs-h1-default.png)

#### Docs section heading
Read as `docs-h2` on the docs quick-start page.

**Values (default).** size 623 x 24.75; background transparent; text Aeonik Pro 18/24.75 500, oklab(0.984998 -0.00000956655 0.0000230074 / 0.95); icon 22.63 x 22.63, lab(65.6464 1.53497 -5.42429).

![Docs section heading default](components/crops/docs-h2-default.png)

### Blog

The index's story tiles.

#### Blog title
Read as `blog-title` on the blog index page.

**Values (default).** size 768 x 72; background transparent; text Aeonik Pro 48/72 400, lab(98.26 0 0).

![Blog title default](components/crops/blog-title-default.png)

#### Post card
A story tile: image, headline, author row. Read as `post-card` on the blog index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1232 x 333; background transparent; text Aeonik Pro 28/36.4 400, lab(98.26 0 0) |
| hover | text Aeonik Pro 28/36.4 400, oklab(0.984998 -0.00000956654 0.0000230074 / 0.8) |

Child layers that carry the look: div 592x333 background oklab(0.298707 0.00198022 -0.00687116 / 0.4); img 40x40 background #2d2d31 border 1px solid lab(13.1873 0.517011 -1.80675) radius 3.35544e+07px.

![Post card default](components/crops/post-card-default.png) ![Post card hover](components/crops/post-card-hover.png)

#### Post headline
Read as `post-headline` on the blog index page.

**Values (default).** size 592 x 72.78; background transparent; text Aeonik Pro 28/36.4 400, lab(98.26 0 0); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Post headline default](components/crops/post-headline-default.png)

#### Author link
Read as `author-link` on the blog index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 103.09 x 40; background transparent; text -apple-system 12/18 400, lab(65.6464 1.53497 -5.42429) |
| hover | text -apple-system 12/18 400, lab(98.26 0 0) |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px |

Child layers that carry the look: img 40x40 background #2d2d31 border 1px solid lab(13.1873 0.517011 -1.80675) radius 3.35544e+07px.

![Author link default](components/crops/author-link-default.png) ![Author link hover](components/crops/author-link-hover.png) ![Author link focus-visible](components/crops/author-link-focus-visible.png) ![Author link pressed](components/crops/author-link-pressed.png)

#### Blog search button
Measured, never opened. Read as `blog-search` on the blog index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 44; padding 0px 12px; border 1px solid lab(13.1873 0.517011 -1.80675); radius 8px; background oklab(0.298707 0.00198022 -0.00687116 / 0.5); text -apple-system 13/19.5 400, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(65.6464 1.53497 -5.42429) |
| hover | background #2d2d31 |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 0px |
| pressed | background #2d2d31 |

![Blog search button default](components/crops/blog-search-default.png) ![Blog search button hover](components/crops/blog-search-hover.png) ![Blog search button focus-visible](components/crops/blog-search-focus-visible.png) ![Blog search button pressed](components/crops/blog-search-pressed.png)

#### Category link
Read as `category-chip` on the blog index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 66.11 x 22; background transparent; text -apple-system 16/22 600, lab(98.26 0 0) |
| hover | text -apple-system 16/22 600, oklab(0.984998 -0.00000956654 0.0000230074 / 0.8) |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px |
| pressed | text -apple-system 16/22 600, oklab(0.984998 -0.00000956654 0.0000230074 / 0.8) |

![Category link default](components/crops/category-chip-default.png) ![Category link hover](components/crops/category-chip-hover.png) ![Category link focus-visible](components/crops/category-chip-focus-visible.png) ![Category link pressed](components/crops/category-chip-pressed.png)

### Sign-in gate

The public sign-in card; nothing was submitted.

#### Sign-in card
The centred auth panel. Read as `signin-card` on the sign-in gate page.

**Values (default).** size 896 x 687.5; border 1px solid lab(13.1873 0.517011 -1.80675); radius 14px; background #1d1d21; text -apple-system 24/32 600, lab(98.26 0 0); icon 16 x 16, lab(65.6464 1.53497 -5.42429).

![Sign-in card default](components/crops/signin-card-default.png)

#### Sign-in title
Read as `signin-title` on the sign-in gate page.

**Values (default).** size 367 x 32; background transparent; text -apple-system 24/32 600, lab(98.26 0 0).

![Sign-in title default](components/crops/signin-title-default.png)

#### OAuth button
"Login with GitHub": the wide identity-provider row. Measured, never pressed. Read as `oauth-button` on the sign-in gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 279 x 36; padding 8px 0px; border 1px solid #2d2d31; radius 8px; background transparent; text -apple-system 14/20 500, lab(65.6464 1.53497 -5.42429); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(65.6464 1.53497 -5.42429) |
| hover | background #2d2d31; text -apple-system 14/20 500, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |
| focus-visible | shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |
| pressed | background #2d2d31; text -apple-system 14/20 500, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |

![OAuth button default](components/crops/oauth-button-default.png) ![OAuth button hover](components/crops/oauth-button-hover.png) ![OAuth button focus-visible](components/crops/oauth-button-focus-visible.png) ![OAuth button pressed](components/crops/oauth-button-pressed.png)

#### OAuth icon button
The square GitLab/Bitbucket identity buttons. Measured, never pressed. Read as `oauth-icon-button` on the sign-in gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; padding 8px 0px; border 1px solid #2d2d31; radius 8px; background transparent; text -apple-system 14/20 500, lab(65.6464 1.53497 -5.42429); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(65.6464 1.53497 -5.42429) |
| hover | size 278.97 x 36; background #2d2d31; text -apple-system 14/20 500, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |
| focus-visible | size 279 x 36; shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |
| pressed | size 279 x 36; background #2d2d31; text -apple-system 14/20 500, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |

![OAuth icon button default](components/crops/oauth-icon-button-default.png) ![OAuth icon button hover](components/crops/oauth-icon-button-hover.png) ![OAuth icon button focus-visible](components/crops/oauth-icon-button-focus-visible.png) ![OAuth icon button pressed](components/crops/oauth-icon-button-pressed.png)

#### Google button
Measured, never pressed. Read as `google-button` on the sign-in gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 367 x 36; padding 8px 12px; border 1px solid #2d2d31; radius 8px; background transparent; text -apple-system 14/20 500, lab(65.6464 1.53497 -5.42429); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(65.6464 1.53497 -5.42429) |
| hover | background #2d2d31; text -apple-system 14/20 500, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |
| focus-visible | shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |
| pressed | background #2d2d31; text -apple-system 14/20 500, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |

![Google button default](components/crops/google-button-default.png) ![Google button hover](components/crops/google-button-hover.png) ![Google button focus-visible](components/crops/google-button-focus-visible.png) ![Google button pressed](components/crops/google-button-pressed.png)

#### Passkey button
Measured, never pressed. Read as `passkey-button` on the sign-in gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 367 x 36; padding 8px 12px; border 1px solid #2d2d31; radius 8px; background transparent; text -apple-system 14/20 500, lab(65.6464 1.53497 -5.42429); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(65.6464 1.53497 -5.42429) |
| hover | background #2d2d31; text -apple-system 14/20 500, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |
| focus-visible | shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |
| pressed | background #2d2d31; text -apple-system 14/20 500, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |

![Passkey button default](components/crops/passkey-button-default.png) ![Passkey button hover](components/crops/passkey-button-hover.png) ![Passkey button focus-visible](components/crops/passkey-button-focus-visible.png) ![Passkey button pressed](components/crops/passkey-button-pressed.png)

#### Email field
Focused with element.focus(). Nothing was typed and the form was never submitted. Read as `email-input` on the sign-in gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 367 x 36; padding 4px 12px; border 1px solid #2d2d31; radius 8px; background oklab(0.298707 0.00198022 -0.00687116 / 0.3); text -apple-system 14/20 400, lab(98.26 0 0); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder lab(65.6464 1.53497 -5.42429) |
| focused | border 1px solid lab(35.8321 1.55474 -5.40724); shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |

![Email field default](components/crops/email-input-default.png) ![Email field focused](components/crops/email-input-focused.png)

#### Password field
Focused only; nothing was typed. Read as `password-input` on the sign-in gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 367 x 36; padding 4px 40px 4px 12px; border 1px solid #2d2d31; radius 8px; background oklab(0.298707 0.00198022 -0.00687116 / 0.3); text -apple-system 14/20 400, lab(98.26 0 0); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder lab(65.6464 1.53497 -5.42429) |
| focused | border 1px solid lab(35.8321 1.55474 -5.40724); shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |

![Password field default](components/crops/password-input-default.png) ![Password field focused](components/crops/password-input-focused.png)

#### Show-password toggle
The eye inside the password field. Read as `show-password` on the sign-in gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 16 x 16; radius 6px; background transparent; text -apple-system 16/24 400, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(65.6464 1.53497 -5.42429) |
| hover | text -apple-system 16/24 400, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |
| focus-visible | shadow lab(35.8321 1.55474 -5.40724) 0px 0px 0px 2px |
| pressed | text -apple-system 16/24 400, lab(98.26 0 0); icon 16 x 16, lab(98.26 0 0) |

![Show-password toggle default](components/crops/show-password-default.png) ![Show-password toggle hover](components/crops/show-password-hover.png) ![Show-password toggle focus-visible](components/crops/show-password-focus-visible.png) ![Show-password toggle pressed](components/crops/show-password-pressed.png)

#### Forgot-password link
Read as `forgot-link` on the sign-in gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 367 x 20; background transparent; text -apple-system 14/20 500, oklch(0.984998 0.000024917 none / 0.85); transition text-decoration-color 0.15s ease, color 0.15s ease |
| hover | text -apple-system 14/20 500, lab(98.26 0 0) |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px |
| pressed | text -apple-system 14/20 500, lab(98.26 0 0) |

![Forgot-password link default](components/crops/forgot-link-default.png) ![Forgot-password link hover](components/crops/forgot-link-hover.png) ![Forgot-password link focus-visible](components/crops/forgot-link-focus-visible.png) ![Forgot-password link pressed](components/crops/forgot-link-pressed.png)

#### Login button
The submit button; measured in every state except a real press — the form was never submitted. Read as `login-button` on the sign-in gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 367 x 36; padding 8px 16px; border 1px solid transparent; radius 8px; background #fd366e; text -apple-system 14/20 500, #ffffff; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.9 |
| focus-visible | border 1px solid lab(35.8321 1.55474 -5.40724); shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |
| pressed | opacity 0.9 |

![Login button default](components/crops/login-button-default.png) ![Login button hover](components/crops/login-button-hover.png) ![Login button focus-visible](components/crops/login-button-focus-visible.png) ![Login button pressed](components/crops/login-button-pressed.png)

#### Legal link
Read as `tos-link` on the sign-in gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 97.09 x 15; background transparent; text -apple-system 12/16 500, oklch(0.984998 0.000024917 none / 0.85); transition text-decoration-color 0.15s ease, color 0.15s ease |
| hover | text -apple-system 12/16 500, lab(98.26 0 0) |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px |
| pressed | text -apple-system 12/16 500, lab(98.26 0 0) |

![Legal link default](components/crops/tos-link-default.png) ![Legal link hover](components/crops/tos-link-hover.png) ![Legal link focus-visible](components/crops/tos-link-focus-visible.png) ![Legal link pressed](components/crops/tos-link-pressed.png)

### Footer

The page footer.

#### Footer
Read as `footer` on the marketing home page.

**Values (default).** size 1440 x 718.5; border T: 1px solid lab(13.1873 0.517011 -1.80675); background #19191c; text -apple-system 11/16.5 600, lab(65.6464 1.53497 -5.42429).

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 27.14 x 20; background transparent; text -apple-system 13/20 400, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text -apple-system 13/20 400, lab(98.26 0 0) |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px |
| pressed | text -apple-system 13/20 400, lab(98.26 0 0) |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer social icon
Read as `footer-social` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 57.03 x 20; background transparent; text -apple-system 13/20 400, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text -apple-system 13/20 400, lab(98.26 0 0) |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 1px |
| pressed | text -apple-system 13/20 400, lab(98.26 0 0) |

![Footer social icon default](components/crops/footer-social-default.png) ![Footer social icon hover](components/crops/footer-social-hover.png) ![Footer social icon focus-visible](components/crops/footer-social-focus-visible.png) ![Footer social icon pressed](components/crops/footer-social-pressed.png)

### Mobile (390 wide)

The same surface at phone width, with the menu sheet open.

#### Mobile top bar
Read as `m-header` on the marketing home page at 390 wide.

**Values (default).** size 390 x 56; padding 0px 12px; border B: 1px solid lab(13.1873 0.517011 -1.80675); background #19191c; text -apple-system 13/19.5 500, lab(65.6464 1.53497 -5.42429); icon 16 x 16, lab(65.6464 1.53497 -5.42429).

![Mobile top bar default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the marketing home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 36 x 36; radius 8px; background transparent; text -apple-system 16/24 400, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(65.6464 1.53497 -5.42429) |
| focus-visible | outline 1px auto oklab(0.447998 0.00407566 -0.0144229 / 0.5), offset 0px |

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button hover](components/crops/m-menu-button-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The button after its own toggle; the open sheet (the data-state=open panel holding the nav links) shows in the crop. Read as `m-menu-open` on the marketing home page at 390 wide.

**Values (opened).** size 36 x 36; radius 8px; background transparent; text -apple-system 16/24 400, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(65.6464 1.53497 -5.42429).

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav link
A destination row inside the opened menu sheet. Read as `m-nav-link` on the marketing home page at 390 wide.

**Values (default).** size 283 x 40; padding 0px 12px; radius 8px; background transparent; text -apple-system 13/19.5 500, lab(65.6464 1.53497 -5.42429); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Mobile nav link default](components/crops/m-nav-link-default.png)

#### Mobile primary CTA
Read as `m-cta-primary` on the marketing home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 132.94 x 40; padding 0px 24px; border 1px solid transparent; radius 8px; background #fd366e; text -apple-system 14/21 500, #ffffff; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | border 1px solid lab(35.8321 1.55474 -5.40724); shadow oklab(0.447998 0.00407566 -0.0144229 / 0.5) 0px 0px 0px 3px |

![Mobile primary CTA default](components/crops/m-cta-primary-default.png) ![Mobile primary CTA hover](components/crops/m-cta-primary-hover.png) ![Mobile primary CTA focus-visible](components/crops/m-cta-primary-focus-visible.png) ![Mobile primary CTA pressed](components/crops/m-cta-primary-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Appwrite's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The console app.** Everything behind sign-in (projects, dashboards, account) is the product, not this marketing surface; the kit never signs in. The `/sign-in` card itself is public and is captured.
- **Anything that sends or creates.** No form was submitted (the sign-in fields were typed into and cleared), no search was run, no checkout or trial was started.
- **The nav flyout panels and the search palette** were toggled open for the screenshots but their innards were not measured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

Every captured marketing page pins `html.dark`: dark is the painted theme, the `dark` set in tokens.json is the measured one. The same stylesheet declares the light values on `:root` — the `light` set is the declared system the console app uses, never painted on the captured routes. The stylesheet also carries seven easter-egg console skins (.crazy, .stealth, .premium, .high-contrast, .barbie, .nineties, .legacy): recorded in [raw/css-vars.json](raw/css-vars.json) under the `skins` bin, never applied and not tokenised.

### Fonts

- **Aeonik Pro** (`--font-aeonik-pro`) is Appwrite's licensed face and is not distributed; the style guide falls back to the system sans.
- **Inter** (`--font-inter`) is the product face, free and substitutable.
- Code blocks use the ui-monospace stack (`--font-mono`).

### Screenshots

- Product renders, illustrations and logos in the screenshots are Appwrite's content. The page reports devicePixelRatio 1 to scripts while painting at 2x; the .capture.json sidecars record both (devicePixelRatio is the real one, reportedDevicePixelRatio the page's).
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article bodies, blog prose and docs copy are the product's content; only the frames and components were measured.
