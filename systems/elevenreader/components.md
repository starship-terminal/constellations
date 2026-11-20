# ElevenReader components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from elevenreader.io on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. elevenreader.io is a Next.js site over Tailwind v4 (Inter for UI/body, Waldenburg for display) whose public surface is all light: the marketing pages, a public audiobook page and the /reader sign-in/sign-up cards. Nothing was signed into, bought or submitted; the email forms were revealed by their own '…with email' toggles and the fields were focused, never filled past sample text that was deleted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (77 components, 193 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (191 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x bounded to 8 chunks (every captured page fits); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [monthly](screenshots/pricing-light-monthly.png) |
| Explore | `/explore` | [default](screenshots/explore-light-default.png), [full](screenshots/explore-light-full.png) |
| Collections | `/collections` | [default](screenshots/collections-light-default.png), [full](screenshots/collections-light-full.png) |
| Genres | `/genres` | [default](screenshots/genres-light-default.png), [full](screenshots/genres-light-full.png) |
| Free audiobooks | `/free-audiobooks` | [default](screenshots/free-audiobooks-light-default.png), [full](screenshots/free-audiobooks-light-full.png) |
| Iconic voices | `/iconic-voices` | [default](screenshots/iconic-voices-light-default.png), [full](screenshots/iconic-voices-light-full.png) |
| Compare | `/compare` | [default](screenshots/compare-light-default.png), [full](screenshots/compare-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Audiobook detail | `/audiobooks/the-art-of-war-audiobook/CrZjqfHD4d1FYEemlTHB` | [default](screenshots/audiobook-light-default.png), [full](screenshots/audiobook-light-full.png) |
| Sign in | `/reader/sign-in` | [default](screenshots/sign-in-light-default.png) |
| Sign up | `/reader/sign-up?source=homepage` | [default](screenshots/sign-up-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Explore, phone | `/explore` | [default](screenshots/mobile-explore-light-default.png), [full](screenshots/mobile-explore-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the hamburger button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |
| Discover mega-menu | every page | the Discover trigger's own click | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-dropdown), [menu-link](#menu-link) |
| Cookiebot consent banner | every page | hidden, never answered (no consent button was ever clicked) | hidden before every shot and reading |
| Billing-period segments | /pricing | the Monthly/Annual segments' own toggle | [pricing-light-monthly](screenshots/pricing-light-monthly.png), [billing-off](#billing-option-idle), [billing-on](#billing-option-selected) |
| Email sign-in / sign-up forms | /reader/sign-in, /reader/sign-up | the '…with email' toggles' own click — fields were focused, never submitted | [email-field](#email-field), [signup-field](#signup-email-field) |
| The reader app | /reader/* behind auth | the library, upload and listening views need an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 34 components were given a real keyboard focus. 24 draw an outline ring: `promo-cta` (2px solid #000000 `color.black.default`, offset 2px), `nav-link` (2px solid #000000 `color.black.default`, offset 2px), `nav-discover` (2px solid #000000 `color.black.default`, offset 2px), `nav-signin` (2px solid #000000 `color.black.default`, offset 2px), `nav-cta` (2px solid #000000 `color.black.default`, offset 0px), `menu-link` (2px solid #000000 `color.black.default`, offset 2px), `hero-cta` (2px solid #000000 `color.black.default`, offset 2px), `hero-cta-2` (2px solid #000000 `color.black.default`, offset 2px), `genre-chip` (2px solid #000000 `color.black.default`, offset 2px), `view-all` (2px solid #000000 `color.black.default`, offset 2px), `try-cta` (2px solid #000000 `color.black.default`, offset 2px), `billing-off` (2px solid #000000 `color.black.default`, offset 2px), `billing-on` (2px solid #000000 `color.black.default`, offset 2px), `plan-cta` (2px solid #000000 `color.black.default`, offset 2px), `ab-preview` (2px solid #000000 `color.black.default`, offset 2px), `cmp-link` (2px solid #000000 `color.black.default`, offset 2px), `sso-google` (2px solid #000000 `color.black.default`, offset 0px), `sso-apple` (2px solid #000000 `color.black.default`, offset 0px), `forgot-btn` (2px solid #000000 `color.black.default`, offset 2px), `signin-submit` (2px solid #000000 `color.black.default`, offset 0px), `signin-secondary` (2px solid #000000 `color.black.default`, offset 2px), `m-nav-item` (2px solid #000000 `color.black.default`, offset 2px), `signup-google` (2px solid #000000 `color.black.default`, offset 0px), `signup-email-btn` (2px solid #000000 `color.black.default`, offset 2px). 7 change only their text decoration (none → underline): `book-link`, `footer-link`, `genre-link`, `ab-crumb`, `ab-author`, `create-link`, `cookie-btn`. The other 3 show no measured change: `faq-summary`, `book-title`, `ab-row`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | cmp-link, email-field, password-field, signup-field |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | menu-link |
| 0.2s | `ease` | all | nav-link |
| 0.3s | `cubic-bezier(0.31, 0.325, 0, 0.92)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, box-shadow, color, fill, outline-color, stroke, text-decoration-color, transform | ab-preview, billing-off, billing-on, forgot-btn, genre-chip, hero-cta, hero-cta-2, m-footer-summary and more |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | height, opacity, width | book-title, nav-dropdown |
| 0.5s | `cubic-bezier(0, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, backdrop-filter, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | m-menu-open |
| 0.65s | `cubic-bezier(0.22, 1, 0.36, 1)` | background-color, border-radius, box-shadow, margin | faq-item |
| 0.7s | `cubic-bezier(0.31, 0.325, 0, 0.92)` | all | ab-cover |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 584 x 721.94 | 1px solid #eae9e9 `color.painted.plan-card-border` | 40px | #fdfcfc `color.painted.plan-card` | none | 56px |
| [Sign-in card](#sign-in-card) | 360 x 900 | - | - | transparent | none | 96px 0px |
| [Sign-up card](#sign-up-card) | 360 x 900 | - | - | transparent | none | 96px 0px |
| [FAQ item](#faq-item) | 780 x 67 | - | 20px | #faf8f8 `color.painted.faq` | none | 0 |
| [Discover mega-menu](#discover-mega-menu) | 846 x 470 | 1px solid #f2f2f2 `color.neutral.50` | 24px | #ffffff `color.white.default` | rgba(16, 24, 40, 0.03) 0px 4px 6px -2px, rgba(16, 24, 40, 0.08) 0px 12px 16px -4px | 0 |
| [Coverflow card](#coverflow-card) | 300.16 x 564.23 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The site chrome on the white field: the #F5F3F1 promo band, wordmark, the Discover mega-menu, plain nav links, the outlined Sign-in pill and the black Start-listening pill.

#### Promo banner
The announcement strip above the header (a #F5F3F1 band, here the Black-Friday offer). Read as `promo-banner` on the home page.

**Values (default).** size 1440 x 49; padding 8px 16px; border B: 1px solid oklab(0 0 0 / 0.1); background #f5f3f1 `color.painted.banner`; text Inter 14/18 500, #000000 `color.black.default`.

![Promo banner default](components/crops/promo-banner-default.png)

#### Promo CTA
The Get-this-offer pill inside the banner; measured never followed (it opens the subscribe flow). Read as `promo-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106.78 x 32; padding 0px 12px; radius 9999px; background #ffffff `color.white.default`; shadow rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; outline 2px solid transparent, offset 2px; text Inter 13/18 400, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), transform 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) |
| hover | background #fdfcfc `color.painted.plan-card` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px |
| pressed | size 104.65 x 31.36; background #fdfcfc `color.painted.plan-card` |

![Promo CTA default](components/crops/promo-cta-default.png) ![Promo CTA hover](components/crops/promo-cta-hover.png) ![Promo CTA focus-visible](components/crops/promo-cta-focus-visible.png) ![Promo CTA pressed](components/crops/promo-cta-pressed.png)

#### Header
The top bar: wordmark, the Main nav (Explore, Discover, Pricing, For Authors, Upload & Listen), Sign in and the dark Start-listening pill. Read as `header` on the home page.

**Values (default).** size 1304 x 64; padding 0px 64px; background transparent; text Inter 16/24 400, #ffffff `color.white.default`; icon 16 x 16, #000000 `color.black.default`; layers a.inline-flex.items-center 158.8x44.0 rgb(0, 0, 0) 2px solid rgba(0, 0, 0, 0) offset 0px 9999px; a.inline-flex.justify-center 164.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; a.inline-flex.justify-center 74.3x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; button.inline-flex.items-center 40.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; a.inline-flex.justify-center 70.3x36.0 2px s.

Child layers that carry the look: a 158.8x44 background #000000 `color.black.default` radius 9999px; a 164x36 radius 9999px; a 74.3x36 radius 9999px.

![Header default](components/crops/header-default.png)

#### Logo
The ElevenReader wordmark anchor (a 140x15 webp). Read as `logo` on the home page.

**Values (default).** size 164 x 36; padding 0px 12px; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 18/28.8 400, #000000 `color.black.default`; layers a.inline-flex.justify-center 164.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px.

Child layers that carry the look: a 164x36 radius 9999px.

![Logo default](components/crops/logo-default.png)

#### Nav link
A plain header nav link (rounded-full, hover bg-surface). Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 70.27 x 36; padding 0px 12px; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/20 400, #000000 `color.black.default`; transition all 0.2s ease; layers a.inline-flex.justify-center 70.3x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px |
| hover | background #f6f6f6 `color.surface`; layers none |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px; layers a.inline-flex.justify-center 70.3x36.0 2px solid rgb(0, 0, 0) offset 2px 9999px |
| pressed | background #f6f6f6 `color.surface`; layers none |

Child layers that carry the look: a 70.3x36 radius 9999px.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Discover trigger
The chevron button that opens the Discover mega-menu; toggled for the panel readings, then closed. Read as `nav-discover` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 36; padding 2px 12px; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/20 400, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), outline-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), text-decoration-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), fill 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), stroke 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-from 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-via 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92); icon 16 x 16, #000000 `color.black.default`; layers button.inline-flex.items-center 40.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px |
| hover | background #f6f6f6 `color.surface`; layers none |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px; layers button.inline-flex.items-center 40.0x36.0 2px solid rgb(0, 0, 0) offset 2px 9999px |
| pressed | background #f6f6f6 `color.surface`; layers none |

Child layers that carry the look: button 40x36 radius 9999px.

![Discover trigger default](components/crops/nav-discover-default.png) ![Discover trigger hover](components/crops/nav-discover-hover.png) ![Discover trigger focus-visible](components/crops/nav-discover-focus-visible.png) ![Discover trigger pressed](components/crops/nav-discover-pressed.png)

#### Sign-in button
The outlined Sign-in pill (bg-default + border, hover bg-surface); measured never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 78.44 x 36; padding 0px 16px; border 1px solid #e5e5e5 `color.neutral.100`; radius 9999px; background #ffffff `color.white.default`; shadow rgba(16, 24, 40, 0.05) 0px 1px 2px 0px; outline 2px solid transparent, offset 2px; text Inter 14/20 400, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), outline-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), text-decoration-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), fill 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), stroke 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-from 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-via 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) |
| hover | background #f6f6f6 `color.surface` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px |
| pressed | background #f6f6f6 `color.surface` |

![Sign-in button default](components/crops/nav-signin-default.png) ![Sign-in button hover](components/crops/nav-signin-hover.png) ![Sign-in button focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign-in button pressed](components/crops/nav-signin-pressed.png)

#### Nav CTA
The dark Start-listening-free pill (bg-inverse text-inverse, hover bg-darkest); measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 154.27 x 36; padding 0px 16px; radius 9999px; background #000000 `color.black.default`; outline 2px solid transparent, offset 0px; text Inter 14/20 400, #ffffff `color.white.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), outline-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), text-decoration-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), fill 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), stroke 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-from 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-via 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) |
| hover | background #6e6e6e `color.neutral.600` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 0px |
| pressed | background #6e6e6e `color.neutral.600` |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Discover mega-menu
The Discover dropdown panel (Popular Genres, Trending Collections, Free Audiobooks cover grid), opened by its own trigger. Read as `nav-dropdown` on the home page.

**Values (default).** size 846 x 470; border 1px solid #f2f2f2 `color.neutral.50`; radius 24px; background #ffffff `color.white.default`; shadow rgba(16, 24, 40, 0.03) 0px 4px 6px -2px, rgba(16, 24, 40, 0.08) 0px 12px 16px -4px; text Inter 14/19.6 500, #6e6e6e `color.neutral.600`; transition width 0.3s cubic-bezier(0.4, 0, 0.2, 1), height 0.3s cubic-bezier(0.4, 0, 0.2, 1).

![Discover mega-menu default](components/crops/nav-dropdown-default.png)

#### Menu link
A genre link inside the opened mega-menu. Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 260 x 40; padding 10px; radius 6px; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/20 500, #000000 `color.black.default`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1); layers a.inline-flex.cursor-pointer 260.0x40.0 2px solid rgba(0, 0, 0, 0) offset 2px 6px |
| hover | background #f2f2f2 `color.neutral.50`; layers none |
| focus-visible, pressed | background #f2f2f2 `color.neutral.50`; outline 2px solid #000000 `color.black.default`, offset 2px; layers none |

Child layers that carry the look: a 260x40 radius 6px.

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link focus-visible](components/crops/menu-link-focus-visible.png) ![Menu link pressed](components/crops/menu-link-pressed.png)

#### Menu column heading
A column heading inside the mega-menu. Read as `menu-heading` on the home page.

**Values (default).** size 260 x 29.59; padding 10px 10px 0px 10px; background transparent; text Inter 14/19.6 500, #6e6e6e `color.neutral.600`.

![Menu column heading default](components/crops/menu-heading-default.png)

### Home hero

The 60px Waldenburg hero (40px at phone width), the two pills under the lede and the 3D book-orbit carousel.

#### Hero headline
The 60px Waldenburg display headline (40px under lg). Read as `hero-h1` on the home page.

**Values (default).** size 507.77 x 120; background transparent; text Waldenburg 60/60 400, #000000 `color.black.default`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero lede
The 18px opacity-60 lede under the headline. Read as `hero-lede` on the home page.

**Values (default).** size 472.5 x 52; background transparent; text Inter 18/26 400, #000000 `color.black.default`; opacity 0.6.

![Hero lede default](components/crops/hero-lede-default.png)

#### Hero CTA
The dark Start-listening-free pill under the lede; measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 190.94 x 52; padding 0px 24px; radius 9999px; background #000000 `color.black.default`; outline 2px solid transparent, offset 2px; text Inter 16/22.4 400, #ffffff `color.white.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), transform 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) |
| hover | background #6e6e6e `color.neutral.600` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px |
| pressed | size 187.12 x 50.96; background #6e6e6e `color.neutral.600` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero secondary CTA
The white shadowed pill beside the dark CTA (bg-default, layered ring shadow, active scale-98). Read as `hero-cta-2` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 163.91 x 52; padding 0px 24px; radius 9999px; background #ffffff `color.white.default`; shadow rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; outline 2px solid transparent, offset 2px; text Inter 16/22.4 400, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), transform 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) |
| hover | background #f2f2f2 `color.neutral.50` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px |
| pressed | size 160.63 x 50.96; background #f2f2f2 `color.neutral.50` |

![Hero secondary CTA default](components/crops/hero-cta-2-default.png) ![Hero secondary CTA hover](components/crops/hero-cta-2-hover.png) ![Hero secondary CTA focus-visible](components/crops/hero-cta-2-focus-visible.png) ![Hero secondary CTA pressed](components/crops/hero-cta-2-pressed.png)

#### Book cover card
A cover card in the hero orbit carousel (rounded-md, cover img on a gray-300 backing); the front-most (widest) card is read. Read as `book-cover` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 211.11 x 316.66; radius 16px; background transparent; text Inter 18/28.8 400, #000000 `color.black.default`; transform translate(0px, -12px) |

![Book cover card default](components/crops/book-cover-default.png) ![Book cover card hover](components/crops/book-cover-hover.png)

### Home sections

Mid-page sections: the Waldenburg headings, book rows, genre chips and the FAQ <details> accordions.

#### Section eyebrow
The small medium-weight section eyebrow (opacity-60). Read as `eyebrow` on the home page.

**Values (default).** size 548 x 32; background transparent; text Waldenburg 24/32 375, #000000 `color.black.default`.

![Section eyebrow default](components/crops/eyebrow-default.png)

#### Section heading
A 36px Waldenburg section heading (30px under lg). Read as `section-h3` on the home page.

**Values (default).** size 362 x 84; background transparent; text Waldenburg 36/42 375, #000000 `color.black.default`.

![Section heading default](components/crops/section-h3-default.png)

#### Book link
A title link in a book row (text-inherit, underline on hover/focus). Read as `book-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 257.56 x 19; background transparent; text Inter 15/22 500, #000000 `color.black.default` |
| hover, focus-visible, pressed | text Inter 15/22 500, #000000 `color.black.default`, underline offset 2px |

![Book link default](components/crops/book-link-default.png) ![Book link hover](components/crops/book-link-hover.png) ![Book link focus-visible](components/crops/book-link-focus-visible.png) ![Book link pressed](components/crops/book-link-pressed.png)

#### Genre chip
A genre filter chip in Trending genres (rounded-full); measured, never pressed (a press navigates). Read as `genre-chip` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 101.02 x 44; padding 0px 20px; radius 9999px; background #ffffff `color.white.default`; shadow rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; outline 2px solid transparent, offset 2px; text Inter 16/22.4 400, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), transform 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px |
| pressed | size 99 x 43.12 |

![Genre chip default](components/crops/genre-chip-default.png) ![Genre chip hover](components/crops/genre-chip-hover.png) ![Genre chip focus-visible](components/crops/genre-chip-focus-visible.png) ![Genre chip pressed](components/crops/genre-chip-pressed.png)

#### View-all link
The ghost View-all link on a section rail. Read as `view-all` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 99.33 x 44; padding 0px 20px; radius 9999px; background transparent; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 1px; outline 2px solid transparent, offset 2px; text Inter 16/22.4 400, oklab(0 0 0 / 0.6); transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), transform 0.3s cubic-bezier(0.31, 0.325, 0, 0.92); layers a.inline-flex.items-center 99.3x44.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.04) 0px 0px 0px 1px 2px solid rgba(0, 0, 0, 0) offset 2px 9999px |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px; layers a.inline-flex.items-center 99.3x44.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.04) 0px 0px 0px 1px 2px solid rgb(0, 0, 0) offset 2px 9999px |
| pressed | size 97.34 x 43.12; layers a.inline-flex.items-center 97.3x43.1 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.04) 0px 0px 0px 1px 2px solid rgba(0, 0, 0, 0) offset 2px 9999px |

![View-all link default](components/crops/view-all-default.png) ![View-all link hover](components/crops/view-all-hover.png) ![View-all link focus-visible](components/crops/view-all-focus-visible.png) ![View-all link pressed](components/crops/view-all-pressed.png)

#### Try-free CTA
A mid-page Try-it-free white pill (bg-default shadow, active scale-98); measured never followed. Read as `try-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 114.97 x 44; padding 0px 20px; radius 9999px; background #ffffff `color.white.default`; shadow rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; outline 2px solid transparent, offset 2px; text Inter 16/22.4 400, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), transform 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) |
| hover | background #f2f2f2 `color.neutral.50` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px |
| pressed | size 112.67 x 43.12; background #f2f2f2 `color.neutral.50` |

![Try-free CTA default](components/crops/try-cta-default.png) ![Try-free CTA hover](components/crops/try-cta-hover.png) ![Try-free CTA focus-visible](components/crops/try-cta-focus-visible.png) ![Try-free CTA pressed](components/crops/try-cta-pressed.png)

#### FAQ item
A homepage FAQ <details>; the open state is the item after its own summary was clicked. Read as `faq-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 780 x 67; radius 20px; background #faf8f8 `color.painted.faq`; text Waldenburg 20/27 400, #000000 `color.black.default`; transition box-shadow 0.65s cubic-bezier(0.22, 1, 0.36, 1), background-color 0.65s cubic-bezier(0.22, 1, 0.36, 1), margin 0.65s cubic-bezier(0.22, 1, 0.36, 1), border-radius 0.65s cubic-bezier(0.22, 1, 0.36, 1) |
| open | size 796 x 159; radius 24px; background #ffffff `color.white.default`; shadow rgba(0, 0, 0, 0.4) 0px 0px 1px 0px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px |

![FAQ item default](components/crops/faq-item-default.png) ![FAQ item open](components/crops/faq-item-open.png)

#### FAQ summary
The clickable FAQ question row (with the +/- indicator); a press toggles its details. Read as `faq-summary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 796 x 67; padding 20px 24px; background transparent; text Waldenburg 20/27 400, #000000 `color.black.default`; layers ::before rgba(0, 0, 0, 0) 2px none 0; summary::before.effect-focus-before.font-waldenburg 804pxx75px T:2px solid rgb(0, 0, 0) / R:2px solid rgb(0, 0, 0) / B:2px solid rgb(0, 0, 0) / L:2px solid rgb(0, 0, 0) 24px; div.absolute.h-0.5 14.0x2.0 rgb(100, 99, 99) 9999px; div.absolute.h-3.5 14.0x2.0 rgb(100, 99, 99) 9999px |
| focus-visible | layers ::before rgba(0, 0, 0, 0) 2px none 1; summary::before.effect-focus-before.font-waldenburg 804pxx75px T:2px solid rgb(0, 0, 0) / R:2px solid rgb(0, 0, 0) / B:2px solid rgb(0, 0, 0) / L:2px solid rgb(0, 0, 0) 24px; div.absolute.h-0.5 14.0x2.0 rgb(100, 99, 99) 9999px; div.absolute.h-3.5 14.0x2.0 rgb(100, 99, 99) 9999px |

Child layers that carry the look: summary::before 804pxx75px border 2px solid #000000 `color.black.default` radius 24px; div 14x2 background #646363 radius 9999px; div 14x2 background #646363 radius 9999px.

![FAQ summary default](components/crops/faq-summary-default.png) ![FAQ summary hover](components/crops/faq-summary-hover.png) ![FAQ summary focus-visible](components/crops/faq-summary-focus-visible.png) ![FAQ summary pressed](components/crops/faq-summary-pressed.png)

### Explore catalog

The catalog rails: coverflow cards, book title links and genre links.

#### Explore headline
The "Find your next audiobook" Waldenburg heading (text-4xl lg). Read as `explore-h1` on the explore page.

**Values (default).** size 399.83 x 40; background transparent; text Waldenburg 36/40 400, #000000 `color.black.default`.

![Explore headline default](components/crops/explore-h1-default.png)

#### Rail heading
A carousel rail heading (Top picks, What's trending). Read as `rail-h2` on the explore page.

**Values (default).** size 73.31 x 24; background transparent; text Inter 16/24 500, #000000 `color.black.default`.

![Rail heading default](components/crops/rail-h2-default.png)

#### Coverflow card
A cover card in an explore rail (2:3 cover on bg-hovered, rounded-md shadow-lg, group-hover scale-105). Read as `coverflow-card` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 300.16 x 564.23; background transparent; text Inter 16/24 500, #000000 `color.black.default`; layers div.transition-transform.[transition-duration:300ms] 300.2x450.2 rgb(240, 240, 240) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(16, 24, 40, 0.03) 0px 4px 6px -2px, rgba(16, 24, 40, 0.08) 0px 12px 16px -4px 6px |
| hover | layers div.transition-transform.[transition-duration:300ms] 315.2x472.7 rgb(240, 240, 240) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(16, 24, 40, 0.03) 0px 4px 6px -2px, rgba(16, 24, 40, 0.08) 0px 12px 16px -4px 6px |

Child layers that carry the look: div 300.2x450.2 background #f0f0f0 `color.hovered` radius 6px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(16, 24, 40, 0.03) 0px 4px 6px -2px, rgba(16, 24, 40, 0.08) 0px 12px 16px -4px.

![Coverflow card default](components/crops/coverflow-card-default.png) ![Coverflow card hover](components/crops/coverflow-card-hover.png)

#### Book title link
The title link under a cover (text-base font-medium, group-hover underline). Read as `book-title` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 300.16 x 114; padding 24px 0px 0px 0px; background transparent; text Inter 16/24 500, #000000 `color.black.default`; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) |

![Book title link default](components/crops/book-title-default.png) ![Book title link hover](components/crops/book-title-hover.png) ![Book title link focus-visible](components/crops/book-title-focus-visible.png) ![Book title link pressed](components/crops/book-title-pressed.png)

#### Book meta
An author/length label under a cover (variant=subtle, text-label). Read as `book-meta` on the explore page.

**Values (default).** size 85.23 x 20; background transparent; text Inter 14/20 400, #767676 `color.neutral.500`.

![Book meta default](components/crops/book-meta-default.png)

#### Genre link
A genre link in the catalog; measured never followed. Read as `genre-link` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 78.42 x 24; background transparent; text Inter 16/24 500, #000000 `color.black.default`; icon 20 x 20, #767676 `color.neutral.500` |
| hover, focus-visible, pressed | text Inter 16/24 500, #000000 `color.black.default`, underline |

![Genre link default](components/crops/genre-link-default.png) ![Genre link hover](components/crops/genre-link-hover.png) ![Genre link focus-visible](components/crops/genre-link-focus-visible.png) ![Genre link pressed](components/crops/genre-link-pressed.png)

### Pricing

The Monthly/Annual billing segments (with the green Save-25% chip) and the white plan cards.

#### Pricing title
The 60px Waldenburg pricing display heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 620 x 120; background transparent; text Waldenburg 60/60 375, #000000 `color.black.default`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Billing option (idle)
The unselected Monthly segment (#57534F text, hover black), read at rest, on hover, on keyboard focus and forced pressed; never clicked or checked out. Read as `billing-off` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101.3 x 48; padding 10px 20px; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #57534f; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), box-shadow 0.3s cubic-bezier(0.31, 0.325, 0, 0.92); layers button.ease-out-slow.effect-focus 101.3x48.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px |
| hover | text Inter 16/24 400, #000000 `color.black.default` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px; layers button.ease-out-slow.effect-focus 101.3x48.0 2px solid rgb(0, 0, 0) offset 2px 9999px |
| pressed | text Inter 16/24 400, #000000 `color.black.default` |

Child layers that carry the look: button 101.3x48 radius 9999px.

![Billing option (idle) default](components/crops/billing-off-default.png) ![Billing option (idle) hover](components/crops/billing-off-hover.png) ![Billing option (idle) focus-visible](components/crops/billing-off-focus-visible.png) ![Billing option (idle) pressed](components/crops/billing-off-pressed.png)

#### Billing option (selected)
The selected Annual segment (white pill, ring shadow, the green Save-25% chip). Read as `billing-on` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 188.83 x 48; padding 10px 20px; radius 9999px; background #ffffff `color.white.default`; shadow rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), box-shadow 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px |

![Billing option (selected) default](components/crops/billing-on-default.png) ![Billing option (selected) hover](components/crops/billing-on-hover.png) ![Billing option (selected) focus-visible](components/crops/billing-on-focus-visible.png) ![Billing option (selected) pressed](components/crops/billing-on-pressed.png)

#### Save badge
The green Save-25% chip inside the Annual segment (#E1F5E0 bg, #307D18 text). Read as `save-badge` on the pricing page.

**Values (default).** size 89.16 x 28; padding 4px 12px; radius 9999px; background #e1f5e0 `color.painted.save-badge-bg`; text Inter 14/20 500, #307d18 `color.painted.save-badge-fg`.

![Save badge default](components/crops/save-badge-default.png)

#### Plan card
A pricing plan card (the painted ancestor of the plan name). Read as `plan-card` on the pricing page.

**Values (default).** size 584 x 721.94; padding 56px; border 1px solid #eae9e9 `color.painted.plan-card-border`; radius 40px; background #fdfcfc `color.painted.plan-card`; text Waldenburg 22/28 375, #000000 `color.black.default`; icon 16 x 16, #000000 `color.black.default`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan name
A plan card's name. Read as `plan-name` on the pricing page.

**Values (default).** size 470 x 28; background transparent; text Waldenburg 22/28 375, #000000 `color.black.default`.

![Plan name default](components/crops/plan-name-default.png)

#### Plan price
A plan card's price figure. Read as `plan-price` on the pricing page.

**Values (default).** size 470 x 36; background transparent; text Waldenburg 36/36 375, #000000 `color.black.default`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan card's action (Start-3-day-free-trial pill); measured never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 472 x 52; padding 0px 24px; radius 9999px; background #000000 `color.black.default`; outline 2px solid transparent, offset 2px; text Inter 16/22.4 400, #ffffff `color.white.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), transform 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) |
| hover | background #6e6e6e `color.neutral.600` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px |
| pressed | size 462.56 x 50.96; background #6e6e6e `color.neutral.600` |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Feature row
A feature row inside a plan card or the "Everything you unlock" list. Read as `feature-li` on the pricing page.

**Values (default).** size 470 x 44.98; background transparent; text Waldenburg 18/23.4 375, #000000 `color.black.default`; icon 16 x 16, #000000 `color.black.default`.

![Feature row default](components/crops/feature-li-default.png)

### Audiobook page

A public audiobook detail page: cover, title, Preview button, format chip, breadcrumbs and related links.

#### Title
The audiobook title heading. Read as `ab-h1` on the audiobook page.

**Values (default).** size 568 x 40; background transparent; text Waldenburg 36/40 400, #000000 `color.black.default`.

![Title default](components/crops/ab-h1-default.png)

#### Cover
The square audiobook cover (8px radius, blurred-thumb placeholder). Read as `ab-cover` on the audiobook page.

**Values (default).** size 262 x 262; background transparent; image an image (data URI);' href='data:image/webp;base64,UklGRiwAAABXRUJQVlA4ICAAAAAwAQCdASoIAAgABUB8JYwAA3AA/vDKRTnSq0tsOsgAAA=='/%3E%3C/svg%3E"); text Inter 18/28.8 400, transparent; transition all 0.7s cubic-bezier(0.31, 0.325, 0, 0.92).

![Cover default](components/crops/ab-cover-default.png)

#### Preview button
The audio Preview button (speaker icon); measured, never pressed (a press plays audio). Read as `ab-preview` on the audiobook page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 264 x 48; padding 0px 20px; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/20 500, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), outline-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), text-decoration-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), fill 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), stroke 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-from 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-via 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92); icon 16 x 16, #000000 `color.black.default`; layers button.items-center.justify-center 264.0x48.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px |
| hover | text Inter 14/20 500, #767676 `color.neutral.500`; icon 16 x 16, #767676 `color.neutral.500` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px; layers button.items-center.justify-center 264.0x48.0 2px solid rgb(0, 0, 0) offset 2px 9999px |
| pressed | text Inter 14/20 500, #767676 `color.neutral.500`; icon 16 x 16, #767676 `color.neutral.500` |

Child layers that carry the look: button 264x48 radius 9999px.

![Preview button default](components/crops/ab-preview-default.png) ![Preview button hover](components/crops/ab-preview-hover.png) ![Preview button focus-visible](components/crops/ab-preview-focus-visible.png) ![Preview button pressed](components/crops/ab-preview-pressed.png)

#### Format chip
The "Audio only" format chip. Read as `ab-chip` on the audiobook page.

**Values (default).** size 568 x 30; background transparent; text Inter 14/20 400, #000000 `color.black.default`; layers div.flex-none.justify-center 87.6x30.0 rgb(242, 242, 242) T:1px solid rgb(229, 229, 229) / R:1px solid rgb(229, 229, 229) / B:1px solid rgb(229, 229, 229) / L:1px solid rgb(229, 229, 229) 9999px.

Child layers that carry the look: div 87.6x30 background #f2f2f2 `color.neutral.50` border 1px solid #e5e5e5 `color.neutral.100` radius 9999px.

![Format chip default](components/crops/ab-chip-default.png)

#### Breadcrumb link
A breadcrumb link (Explore / genre) above the title. Read as `ab-crumb` on the audiobook page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 50.05 x 20; radius 2px; background transparent; text Inter 14/20 500, #767676 `color.neutral.500` |
| hover | text Inter 14/20 500, #6e6e6e `color.neutral.600`, underline offset 2px |
| focus-visible | text Inter 14/20 500, #767676 `color.neutral.500`, underline offset 2px |
| pressed | text Inter 14/20 500, #6e6e6e `color.neutral.600`, underline offset 2px |

![Breadcrumb link default](components/crops/ab-crumb-default.png) ![Breadcrumb link hover](components/crops/ab-crumb-hover.png) ![Breadcrumb link focus-visible](components/crops/ab-crumb-focus-visible.png) ![Breadcrumb link pressed](components/crops/ab-crumb-pressed.png)

#### Author link
The By-author link under the title. Read as `ab-author` on the audiobook page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 61.64 x 20; background transparent; text Inter 16/24 500, #767676 `color.neutral.500` |
| hover, focus-visible, pressed | text Inter 16/24 500, #767676 `color.neutral.500`, underline offset 2px |

![Author link default](components/crops/ab-author-default.png) ![Author link hover](components/crops/ab-author-hover.png) ![Author link focus-visible](components/crops/ab-author-focus-visible.png) ![Author link pressed](components/crops/ab-author-pressed.png)

#### Related title link
A related-audiobook link in "More from" / "You may also like". Read as `ab-row` on the audiobook page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 264 x 152; background transparent; text Inter 16/24 500, #000000 `color.black.default`; icon 14 x 14, #949494 `color.neutral.400`; layers div.rounded-sm.shadow-lg 120.0x120.0 rgb(240, 240, 240) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(16, 24, 40, 0.03) 0px 4px 6px -2px, rgba(16, 24, 40, 0.08) 0px 12px 16px -4px 2px |
| hover, focus-visible, pressed | layers div.rounded-sm.shadow-lg 126.0x126.0 rgb(240, 240, 240) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(16, 24, 40, 0.03) 0px 4px 6px -2px, rgba(16, 24, 40, 0.08) 0px 12px 16px -4px 2px |

Child layers that carry the look: div 120x120 background #f0f0f0 `color.hovered` radius 2px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(16, 24, 40, 0.03) 0px 4px 6px -2px, rgba(16, 24, 40, 0.08) 0px 12px 16px -4px.

![Related title link default](components/crops/ab-row-default.png) ![Related title link hover](components/crops/ab-row-hover.png) ![Related title link focus-visible](components/crops/ab-row-focus-visible.png) ![Related title link pressed](components/crops/ab-row-pressed.png)

### Compare

The comparison page: its heading and the feature table.

#### Compare title
The "ElevenReader vs. other text to speech apps" heading. Read as `cmp-h1` on the compare page.

**Values (default).** size 760 x 95.03; background transparent; text Waldenburg 44/47.52 375, #000000 `color.black.default`.

![Compare title default](components/crops/cmp-h1-default.png)

#### Comparison table
The apps comparison table (header row + feature rows). Read as `cmp-table` on the compare page.

**Values (default).** size 932 x 538.5; background transparent; text Inter 11/16 500, oklab(0 0 0 / 0.55); layers th.align-top.font-medium 177.1x91.0 rgb(245, 243, 241) 12px 0px 0px 12px; td.flex.flex-col 251.6x91.0 rgb(245, 243, 241); td.flex.flex-col 205.0x91.0 rgb(245, 243, 241); td.flex.flex-col 298.3x91.0 rgb(245, 243, 241) 0px 12px 12px 0px; th.align-top.font-medium 177.1x71.0 T:1px solid rgb(232, 230, 229); a.inline-flex.justify-center 67.1x21.0 2px solid rgba(0, 0, 0, 0) offset 2px 2px.

Child layers that carry the look: th 177.1x91 background #f5f3f1 `color.painted.banner` radius 12px 0px 0px 12px; td 251.6x91 background #f5f3f1 `color.painted.banner`; td 205x91 background #f5f3f1 `color.painted.banner`.

![Comparison table default](components/crops/cmp-table-default.png)

#### Table head cell
A header cell in the comparison table. Read as `cmp-th` on the compare page.

**Values (default).** size 177.08 x 29.5; padding 0px 16px 10px 16px; background transparent; text Inter 11/16 500, oklab(0 0 0 / 0.55).

![Table head cell default](components/crops/cmp-th-default.png)

#### Table cell
A body cell in the comparison table (a check/cross or text). Read as `cmp-td` on the compare page.

**Values (default).** size 251.63 x 91; padding 14px 16px; background #f5f3f1 `color.painted.banner`; text Inter 14/21 400, #000000 `color.black.default`.

![Table cell default](components/crops/cmp-td-default.png)

#### Comparison link
A link to an in-depth comparison page. Read as `cmp-link` on the compare page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 191 x 48.44; padding 6px 12px; radius 10px; background transparent; outline 2px solid transparent, offset 2px; text Inter 13.5/18.22 400, oklab(0 0 0 / 0.6); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers a.items-center.cursor-pointer 191.0x48.4 2px solid rgba(0, 0, 0, 0) offset 2px 10px |
| hover | background #faf8f8 `color.painted.faq`; text Inter 13.5/18.22 400, #000000 `color.black.default`; layers none |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px; layers a.items-center.cursor-pointer 191.0x48.4 2px solid rgb(0, 0, 0) offset 2px 10px |
| pressed | background #faf8f8 `color.painted.faq`; text Inter 13.5/18.22 400, #000000 `color.black.default`; layers none |

Child layers that carry the look: a 191x48.4 radius 10px.

![Comparison link default](components/crops/cmp-link-default.png) ![Comparison link hover](components/crops/cmp-link-hover.png) ![Comparison link focus-visible](components/crops/cmp-link-focus-visible.png) ![Comparison link pressed](components/crops/cmp-link-pressed.png)

### Sign in and sign up

The auth boundary cards on /reader, measured but never submitted: the OAuth pills and the email forms revealed by their own toggles.

#### Sign-in card
The centred sign-in card column (max-w-90: logo, OAuth buttons, the revealed email form, the Create-account footer); never filled or submitted. Read as `signin-card` on the sign in page.

**Values (default).** size 360 x 900; padding 96px 0px; background transparent; text Inter 16/24 500, #000000 `color.black.default`; icon 20 x 20, #000000 `color.black.default`; layers button.justify-center.whitespace-nowrap 360.0x40.0 rgb(242, 242, 242) 2px solid rgba(0, 0, 0, 0) offset 0px 9999px; button.justify-center.whitespace-nowrap 360.0x40.0 rgb(0, 0, 0) 2px solid rgba(0, 0, 0, 0) offset 0px 9999px; div.w-full.border-b 0.0x1.0 B:1px solid rgb(229, 229, 229); div.w-full.border-b 0.0x1.0 B:1px solid rgb(229, 229, 229); input.border-gray-alpha-200.placeholder:text-subtle 26.

Child layers that carry the look: button 360x40 background #f2f2f2 `color.neutral.50` radius 9999px; button 360x40 background #000000 `color.black.default` radius 9999px; div 0x1 border 1px solid #e5e5e5 `color.neutral.100`.

![Sign-in card default](components/crops/signin-card-default.png)

#### Google button
The Sign-in-with-Google pill (bg-dark, hover bg-overlay-darker); measured never pressed. Read as `sso-google` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 40; padding 0px 16px; radius 9999px; background #f2f2f2 `color.neutral.50`; outline 2px solid transparent, offset 0px; text Inter 14/15.4 500, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), outline-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), text-decoration-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), fill 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), stroke 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-from 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-via 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92); icon 20 x 20, #000000 `color.black.default` |
| hover | background rgba(0, 0, 0, 0.1) `color.black.alpha.10` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 0px |
| pressed | background rgba(0, 0, 0, 0.1) `color.black.alpha.10` |

![Google button default](components/crops/sso-google-default.png) ![Google button hover](components/crops/sso-google-hover.png) ![Google button focus-visible](components/crops/sso-google-focus-visible.png) ![Google button pressed](components/crops/sso-google-pressed.png)

#### Apple button
The Sign-in-with-Apple pill (bg-inverse, hover opacity-80); measured never pressed. Read as `sso-apple` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 40; padding 0px 16px; radius 9999px; background #000000 `color.black.default`; outline 2px solid transparent, offset 0px; text Inter 14/15.4 500, #ffffff `color.white.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), outline-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), text-decoration-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), fill 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), stroke 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-from 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-via 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92); icon 18 x 18, #ffffff `color.white.default` |
| hover | background #6e6e6e `color.neutral.600`; opacity 0.8 |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 0px |
| pressed | background #6e6e6e `color.neutral.600`; opacity 0.8 |

![Apple button default](components/crops/sso-apple-default.png) ![Apple button hover](components/crops/sso-apple-hover.png) ![Apple button focus-visible](components/crops/sso-apple-focus-visible.png) ![Apple button pressed](components/crops/sso-apple-pressed.png)

#### Email field
The email input (rounded-full, border-gray-alpha-200, focus-ring) after the email toggle was pressed; sample text was typed and deleted, nothing sent. Read as `email-field` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 360 x 40; padding 8px 12px; border 1px solid #e5e5e5 `color.neutral.100`; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #000000 `color.black.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder oklab(0 0 0 / 0.5) |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png) ![Email field filled](components/crops/email-field-filled.png)

#### Password field
The password input after the email toggle; focused only, never filled or submitted. Read as `password-field` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 360 x 40; padding 8px 12px; border 1px solid #e5e5e5 `color.neutral.100`; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #000000 `color.black.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder oklab(0 0 0 / 0.5) |

![Password field default](components/crops/password-field-default.png) ![Password field focused](components/crops/password-field-focused.png)

#### Forgot-password button
The Forgot-password link-button beside the Password label (opens a dialog; measured, never pressed). Read as `forgot-btn` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 122.48 x 32; padding 0px 12px; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 12/13.2 700, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), outline-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), text-decoration-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), fill 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), stroke 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-from 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-via 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92); layers button.inline-flex.items-center 122.5x32.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px |
| hover | text Inter 12/13.2 700, #767676 `color.neutral.500` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px; layers button.inline-flex.items-center 122.5x32.0 2px solid rgb(0, 0, 0) offset 2px 9999px |
| pressed | text Inter 12/13.2 700, #767676 `color.neutral.500` |

Child layers that carry the look: button 122.5x32 radius 9999px.

![Forgot-password button default](components/crops/forgot-btn-default.png) ![Forgot-password button hover](components/crops/forgot-btn-hover.png) ![Forgot-password button focus-visible](components/crops/forgot-btn-focus-visible.png) ![Forgot-password button pressed](components/crops/forgot-btn-pressed.png)

#### Sign-in submit
The form's Sign-in submit (bg-inverse pill) after the email toggle; measured, never pressed (a press would submit). Read as `signin-submit` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 40; padding 0px 16px; radius 9999px; background #000000 `color.black.default`; outline 2px solid transparent, offset 0px; text Inter 14/15.4 500, #ffffff `color.white.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), outline-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), text-decoration-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), fill 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), stroke 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-from 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-via 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) |
| hover | background #6e6e6e `color.neutral.600` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 0px |
| pressed | background #6e6e6e `color.neutral.600` |

![Sign-in submit default](components/crops/signin-submit-default.png) ![Sign-in submit hover](components/crops/signin-submit-hover.png) ![Sign-in submit focus-visible](components/crops/signin-submit-focus-visible.png) ![Sign-in submit pressed](components/crops/signin-submit-pressed.png)

#### Email-signin button
The outlined Sign-in-with-email pill under the OAuth buttons; it toggles the credential form (pressed after its own readings). Read as `signin-secondary` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 40; padding 0px 16px; border 1px solid #e5e5e5 `color.neutral.100`; radius 9999px; background #ffffff `color.white.default`; outline 2px solid transparent, offset 2px; text Inter 14/15.4 500, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), outline-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), text-decoration-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), fill 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), stroke 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-from 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-via 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) |
| hover | background #f6f6f6 `color.surface` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px |
| pressed | background #f6f6f6 `color.surface` |

![Email-signin button default](components/crops/signin-secondary-default.png) ![Email-signin button hover](components/crops/signin-secondary-hover.png) ![Email-signin button focus-visible](components/crops/signin-secondary-focus-visible.png) ![Email-signin button pressed](components/crops/signin-secondary-pressed.png)

#### Create-account link
The card footer's Create-account link; measured never followed. Read as `create-link` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 102.86 x 19.59; radius 2px; background transparent; text Inter 14/19.6 500, #000000 `color.black.default` |
| hover | text Inter 14/19.6 500, #6e6e6e `color.neutral.600`, underline offset 2px |
| focus-visible | text Inter 14/19.6 500, #000000 `color.black.default`, underline offset 2px |
| pressed | text Inter 14/19.6 500, #6e6e6e `color.neutral.600`, underline offset 2px |

![Create-account link default](components/crops/create-link-default.png) ![Create-account link hover](components/crops/create-link-hover.png) ![Create-account link focus-visible](components/crops/create-link-focus-visible.png) ![Create-account link pressed](components/crops/create-link-pressed.png)

#### Sign-up card
The centred create-account card column (max-w-90: logo, heading, OAuth buttons, legal copy); never filled or submitted. Read as `signup-card` on the sign up page.

**Values (default).** size 360 x 900; padding 96px 0px; background transparent; text Inter 16/24 500, #000000 `color.black.default`; icon 14 x 14, #767676 `color.neutral.500`; layers span.border-dark.text-light 60.5x22.0 T:1px solid rgb(148, 148, 148) / R:1px solid rgb(148, 148, 148) / B:1px solid rgb(148, 148, 148) / L:1px solid rgb(148, 148, 148) 9999px; span.border-dark.text-light 47.8x22.0 T:1px solid rgb(148, 148, 148) / R:1px solid rgb(148, 148, 148) / B:1px solid rgb(148, 148, 148) / L:1px solid rgb(148, 148, 148) 9999px; span.border-dark.text-light 70.9x22.0 T:1px soli.

Child layers that carry the look: span 60.5x22 border 1px solid #949494 `color.neutral.400` radius 9999px; span 47.8x22 border 1px solid #949494 `color.neutral.400` radius 9999px; span 70.9x22 border 1px solid #949494 `color.neutral.400` radius 9999px.

![Sign-up card default](components/crops/signup-card-default.png)

#### Signup email field
The signup email input after the email toggle; focused only, never filled or submitted. Read as `signup-field` on the sign up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 360 x 40; padding 8px 12px; border 1px solid #e5e5e5 `color.neutral.100`; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #000000 `color.black.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder oklab(0 0 0 / 0.5) |

![Signup email field default](components/crops/signup-field-default.png) ![Signup email field focused](components/crops/signup-field-focused.png)

#### Google sign-up button
The Sign-up-with-Google pill; measured never pressed. Read as `signup-google` on the sign up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 40; padding 0px 16px; radius 9999px; background #f2f2f2 `color.neutral.50`; outline 2px solid transparent, offset 0px; text Inter 14/15.4 500, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), outline-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), text-decoration-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), fill 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), stroke 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-from 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-via 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92); icon 20 x 20, #000000 `color.black.default` |
| hover | background rgba(0, 0, 0, 0.1) `color.black.alpha.10` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 0px |
| pressed | background rgba(0, 0, 0, 0.1) `color.black.alpha.10` |

![Google sign-up button default](components/crops/signup-google-default.png) ![Google sign-up button hover](components/crops/signup-google-hover.png) ![Google sign-up button focus-visible](components/crops/signup-google-focus-visible.png) ![Google sign-up button pressed](components/crops/signup-google-pressed.png)

#### Legal copy
The small legal consent paragraph on the sign-up card. Read as `signup-legal` on the sign up page.

**Values (default).** size 360 x 50.39; background transparent; text Inter 12/16.8 500, #6e6e6e `color.neutral.600`.

![Legal copy default](components/crops/signup-legal-default.png)

#### Email-signup button
The outlined Sign-up-with-email pill; it toggles the credential form (pressed after its own readings). Read as `signup-email-btn` on the sign up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 40; padding 0px 16px; border 1px solid #e5e5e5 `color.neutral.100`; radius 9999px; background #ffffff `color.white.default`; outline 2px solid transparent, offset 2px; text Inter 14/15.4 500, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), outline-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), text-decoration-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), fill 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), stroke 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-from 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-via 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) |
| hover | background #f6f6f6 `color.surface` |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px |
| pressed | background #f6f6f6 `color.surface` |

![Email-signup button default](components/crops/signup-email-btn-default.png) ![Email-signup button hover](components/crops/signup-email-btn-hover.png) ![Email-signup button focus-visible](components/crops/signup-email-btn-focus-visible.png) ![Email-signup button pressed](components/crops/signup-email-btn-pressed.png)

### Footer

The footer: link columns over muted headings, legal row and app badges.

#### Footer
The footer: the big Footer heading, the <details> link columns, legal and app badges. Read as `footer` on the home page.

**Values (default).** size 1440 x 967.31; padding 120px 0px; background transparent; text Inter 13/18.2 500, #767676 `color.neutral.500`; layers summary::before.effect-color.effect-focus-before autoxauto T:2px solid rgb(0, 0, 0) / R:2px solid rgb(0, 0, 0) / B:2px solid rgb(0, 0, 0) / L:2px solid rgb(0, 0, 0) 24px; summary::before.effect-color.effect-focus-before autoxauto T:2px solid rgb(0, 0, 0) / R:2px solid rgb(0, 0, 0) / B:2px solid rgb(0, 0, 0) / L:2px solid rgb(0, 0, 0) 24px; summary::before.effect-color.effect-focus-before autoxauto.

Child layers that carry the look: summary::before autoxauto border 2px solid #000000 `color.black.default` radius 24px; summary::before autoxauto border 2px solid #000000 `color.black.default` radius 24px; summary::before autoxauto border 2px solid #000000 `color.black.default` radius 24px.

![Footer default](components/crops/footer-default.png)

#### Footer column heading
A muted column heading (text-lighter 13px) over a footer link list. Read as `footer-col` on the home page.

**Values (default).** size 279 x 18.19; background transparent; text Inter 13/18.2 500, #767676 `color.neutral.500`.

![Footer column heading default](components/crops/footer-col-default.png)

#### Footer link
A footer link (effect-focus-underline). Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 131.94 x 19.59; radius 2px; background transparent; text Inter 14/19.6 500, #000000 `color.black.default` |
| hover | text Inter 14/19.6 500, #6e6e6e `color.neutral.600`, underline offset 2px |
| focus-visible | text Inter 14/19.6 500, #000000 `color.black.default`, underline offset 2px |
| pressed | text Inter 14/19.6 500, #6e6e6e `color.neutral.600`, underline offset 2px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Cookie-settings button
The Cookie Settings text-button in the legal column; measured, never pressed (a press opens the consent preferences). Read as `cookie-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106.02 x 28.8; background transparent; text Inter 14/28.8 500, #000000 `color.black.default` |
| hover, focus-visible, pressed | text Inter 14/28.8 500, #000000 `color.black.default`, underline offset 2px |

![Cookie-settings button default](components/crops/cookie-btn-default.png) ![Cookie-settings button hover](components/crops/cookie-btn-hover.png) ![Cookie-settings button focus-visible](components/crops/cookie-btn-focus-visible.png) ![Cookie-settings button pressed](components/crops/cookie-btn-pressed.png)

### Mobile (390 wide)

The public surface at phone width: compact header, the full-height menu overlay, stacked hero and the footer accordions.

#### Mobile promo banner
Read as `m-promo` on the home page at 390 wide.

**Values (default).** size 390 x 53; padding 8px 16px; border B: 1px solid oklab(0 0 0 / 0.1); background #f5f3f1 `color.painted.banner`; text Inter 14/18 500, #000000 `color.black.default`.

![Mobile promo banner default](components/crops/m-promo-default.png)

#### Mobile header
The 390px top bar: wordmark and the Open-menu button. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 64; padding 0px 20px; background transparent; text Inter 16/24 400, #ffffff `color.white.default`; layers a.inline-flex.items-center 158.8x44.0 rgb(0, 0, 0) 2px solid rgba(0, 0, 0, 0) offset 0px 9999px; a.inline-flex.justify-center 164.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; a.inline-flex.justify-center 0.0x0.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; button.inline-flex.items-center 0.0x0.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; a.inline-flex.justify-center 0.0x0.0 2px solid r.

Child layers that carry the look: a 158.8x44 background #000000 `color.black.default` radius 9999px; a 164x36 radius 9999px; a 0x0 radius 9999px.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The hamburger button in the mobile header. Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40 x 40; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/15.4 700, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), outline-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), text-decoration-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), fill 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), stroke 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-from 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-via 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92); icon 24 x 24, #000000 `color.black.default`; layers button.inline-flex.items-center 40.0x40.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: button 40x40 radius 9999px.

![Menu button default](components/crops/m-menu-button-default.png) ![Menu button hover](components/crops/m-menu-button-hover.png) ![Menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The full-screen menu the hamburger opens (nav items plus Sign-in/Start-listening pills). Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; padding 0px 20px; background #ffffff `color.white.default`; shadow rgba(16, 24, 40, 0.03) 0px 4px 6px -2px, rgba(16, 24, 40, 0.08) 0px 12px 16px -4px; text Inter 14/20 400, #000000 `color.black.default`; transition color 0.5s cubic-bezier(0, 0, 0.2, 1), background-color 0.5s cubic-bezier(0, 0, 0.2, 1), border-color 0.5s cubic-bezier(0, 0, 0.2, 1), outline-color 0.5s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.5s cubic-bezier(0, 0, 0.2, 1), fill 0.5s cubic-bezier(0, 0, 0.2, 1), stroke 0.5s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.5s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.5s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.5s cubic-bezier(0, 0, 0.2, 1), opacity 0.5s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.5s cubic-bezier(0, 0, 0.2, 1), transform 0.5s cubic-bezier(0, 0, 0.2, 1), translate 0.5s cubic-bezier(0, 0, 0.2, 1), scale 0.5s cubic-bezier(0, 0, 0.2, 1), rotate 0.5s cubic-bezier(0, 0, 0.2, 1), filter 0.5s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.5s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.5s cubic-bezier(0, 0, 0.2, 1), display 0.5s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.5s cubic-bezier(0, 0, 0.2, 1), overlay 0.5s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.5s cubic-bezier(0, 0, 0.2, 1); icon 24 x 24, #000000 `color.black.default`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
An item inside the opened mobile menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 362 x 24; padding 0px 0px 0px 12px; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/20 400, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), outline-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), text-decoration-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), fill 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), stroke 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-from 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-via 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92); icon 24 x 24, #000000 `color.black.default`; layers button.effect-focus.effect-color 362.0x24.0 2px solid rgba(0, 0, 0, 0) offset 2px |
| focus-visible | outline 2px solid #000000 `color.black.default`, offset 2px; layers button.effect-focus.effect-color 362.0x24.0 2px solid rgb(0, 0, 0) offset 2px |

Child layers that carry the look: button 362x24.

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 338.52 x 80; background transparent; text Waldenburg 40/40 400, #000000 `color.black.default`.

![Mobile headline default](components/crops/m-hero-default.png)

#### Mobile footer column
A footer <details> link column (lg:hidden — the mobile-only accordion); the open state is the column after its own summary was tapped. Read as `m-footer-col` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 350 x 24; background transparent; text Inter 12/13.2 700, #000000 `color.black.default`; icon 24 x 24, #000000 `color.black.default`; layers summary::before.effect-color.effect-focus-before 358pxx32px T:2px solid rgb(0, 0, 0) / R:2px solid rgb(0, 0, 0) / B:2px solid rgb(0, 0, 0) / L:2px solid rgb(0, 0, 0) 24px |
| open | size 350 x 266.17; icon none |

Child layers that carry the look: summary::before 358pxx32px border 2px solid #000000 `color.black.default` radius 24px.

![Mobile footer column default](components/crops/m-footer-col-default.png) ![Mobile footer column open](components/crops/m-footer-col-open.png)

#### Mobile footer summary
The tappable footer column row (f-ui-04 with the chevron pair). Read as `m-footer-summary` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 350 x 24; padding 4px 0px; background transparent; text Inter 12/13.2 700, #000000 `color.black.default`; transition color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), background-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), border-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), outline-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), text-decoration-color 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), fill 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), stroke 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-from 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-via 0.3s cubic-bezier(0.31, 0.325, 0, 0.92), --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92); layers ::before rgba(0, 0, 0, 0) 2px none 0; summary::before.effect-color.effect-focus-before 358pxx32px T:2px solid rgb(0, 0, 0) / R:2px solid rgb(0, 0, 0) / B:2px solid rgb(0, 0, 0) / L:2px solid rgb(0, 0, 0) 24px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: summary::before 358pxx32px border 2px solid #000000 `color.black.default` radius 24px.

![Mobile footer summary default](components/crops/m-footer-summary-default.png) ![Mobile footer summary hover](components/crops/m-footer-summary-hover.png) ![Mobile footer summary pressed](components/crops/m-footer-summary-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the ElevenReader wordmark, the Google/Apple SSO glyphs, the Discover chevron, the footer arrows and the book-cover artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

ElevenReader's product — the reader/library app, upload flow, the in-app player and every account surface — lives behind /reader/sign-in and was never reached. The sign-in and sign-up cards were captured as forms: the OAuth buttons were never pressed, the '…with email' toggles revealed the credential forms (a local UI toggle, no request), fields were focused and sample text was typed and deleted — nothing was submitted, no account was created.

### Pages

- **The reader app.** The library, upload, settings, payments and the actual reading/listening views need an account and were never reached; /reader/sign-in and /reader/sign-up were captured as the boundary cards.
- **Checkout and onboarding.** Every Start-listening, Try-it-free, plan CTA and 'Get this offer' link was measured, never followed past its public landing.
- **External links.** App Store / Google Play badges, social links and the ElevenLabs footer links were captured, never followed.
- **Form outcomes.** No form was ever submitted: the sign-in error/success states, the forgot-password dialog and the create-account flow are uncaptured by design.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing. Forced presses shrink the pills (a scale-98 transform is painted on hero-cta, plan-cta, genre-chip, view-all, try-cta and promo-cta).
- **Disabled, error and loading states** were not seen on the public surface.
- **Hover on nav links** changes only the fill (transparent to the surface tint); every control that rings on its own box draws the same 2px solid #000000 outline, at 2px offset on 19 of 24 (0px on 5: `nav-cta`, `sso-google`, `sso-apple`, `signin-submit`, `signup-google`).

### Themes

Every captured surface paints light. The stylesheet declares a `.dark` scope that inverts the --themed-* triplets — captured in the dark set — but no public page applies it, so dark is a declared inversion, not a painted surface. The reader app's own --reader-* palette is declared on the same sheet and is unpainted here.

### Fonts

- **Inter** (UI, body, forms — served with an 'Inter Fallback' metrics clone), **Waldenburg** (the display face on h1s, pricing and audiobook titles, section heads, FAQ questions; 'WaldenburgHF' bold-semi-condensed is declared for hero use) are the served faces from elevenlabs.elevenreader.io's own CDN; the style guide falls back to system sans.

### Screenshots

- Book-cover artwork, the product illustrations and the ElevenReader wordmark in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, FAQ answers, blog posts and the audiobook's metadata are the product's content; only frames and components were measured.
