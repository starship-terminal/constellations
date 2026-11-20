# 1Password components

The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from 1password.com on 2026-11-10, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was bought, downloaded, signed into, sent or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (44 components, 97 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `agileSans 16/24 350, #303136`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (97 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (1password.com serves one light theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home. Tan announcement strip, white nav bar, the navy gradient hero and product collage. Nav flyout and full page captured. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Pricing. Plan-selector pill, the platform/product column grid, a FAQ row open; full page. | `/pricing` | [default](screenshots/pricing-light-default.png), [faq](screenshots/pricing-light-faq.png), [full](screenshots/pricing-light-full.png) |
| Enterprise Password Manager product page. | `/product/enterprise-password-manager` | [default](screenshots/product-light-default.png), [full](screenshots/product-light-full.png) |
| Download 1Password for macOS: platform pill and download button. | `/downloads/mac` | [default](screenshots/download-light-default.png), [full](screenshots/download-light-full.png) |
| Developer Security page. | `/developer-security` | [default](screenshots/developer-light-default.png), [full](screenshots/developer-light-full.png) |
| Contact sales: the embedded Marketo form (cross-origin). | `/contact-sales` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| start.1password.com under a headless browser redirects to its unsupported-browser page. | `https://start.1password.com/unsupported?l=en` | [default](screenshots/account-light-default.png) |
| Home at 390: header, hamburger, hero, full page. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing at 390; full page. | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Nav flyout | desktop nav | click on the Business group button | [menu](screenshots/home-light-menu.png), [nav-flyout](#nav-flyout) |
| FAQ accordion | pricing | the first collapsed row toggled open | [faq](screenshots/pricing-light-faq.png), [faq-answer](#faq-answer) |
| Mobile menu drawer | mobile home | the hamburger button | [m-nav-drawer](#mobile-nav-drawer) |
| OneTrust consent card | first visit, any page | an OptanonAlertBoxClosed cookie is pre-seeded so it never mounts; a closed-shadow sweep hides it if it still appears | dismissed before every capture |
| Vimeo embed | home hero | a cross-origin player.vimeo.com iframe | measured as an element box only; contents unreachable |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 17 components were given a real keyboard focus. 15 show a visible change (outline, or a border/fill change where the outline stays transparent): `promo-link` (1px auto #005fcc, offset 4px), `signin-link` (1px auto #005fcc, offset 4px), `nav-flyout-button` (1px auto #005fcc, offset 3px), `nav-link` (1px auto #005fcc, offset 4px), `cta-header-primary` (1px solid #145fe4, offset 3px), `cta-header-sales` (1px auto #005fcc, offset 4px), `cta-hero-primary` (1px solid #ffffff `paper.DEFAULT`, offset 3px), `cta-hero-secondary` (1px solid #ffffff `paper.DEFAULT`, offset 3px), `cta-quote` (1px solid #145fe4, offset 3px), `cta-product-primary` (1px solid #145fe4, offset 3px), `download-button` (1px solid #145fe4, offset 3px), `platform-link` (2px solid #3b66bc, offset 2px), `dev-cta` (1px solid #ffffff `paper.DEFAULT`, offset 3px), `cta-marketplace` (1px auto #005fcc, offset 1px), `platform-pill` (border/fill change, no visible outline). The other 2 draw none, so a keyboard user sees no change: `plan-selector`, `faq-row`.

**Pressed.** 1Password's CTAs darken a step (secure-blue to its pressed navy) or hold flat; the segment-selector pills take a filled state — see the per-component state rows.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.3s | `cubic-bezier(0, 0, 0.2, 1)` | all | nav-flyout |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | all, background-color, background-size, border-color, color, fill, stroke, text-decoration-color, transform | cta-header-primary, cta-hero-primary, cta-hero-secondary, cta-product-primary, cta-quote, dev-cta, download-button, logo and more |
| 0.5s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | faq-answer |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Header](#header) | 1440 x 132 | - | - | #ffffff `paper.DEFAULT` | none | 0 |
| [Mobile header](#mobile-header) | 390 x 825.56 | - | - | #1d1d21 `ink.footer` | none | 128px 0px 0px 0px |

## Components

### Shell and navigation

The chrome on every public page: the tan announcement strip, then the white `header-navigation` bar (wordmark, nav-group flyout buttons, Pricing link, Talk to sales, the blue Get started free pill), and the dark footer.

#### Announcement strip
The tan strip above the header: "1Password for Agents" copy with a Learn more link and a Sign in link at the far right. Read as `promo-strip` on the home page.

**Values (default).** size 587.69 x 24; background transparent; text agileSans 16/24 350, #303136 `ink.DEFAULT`.

Child layers that carry the look: span 587.7x23 image linear-gradient(#303136 `ink.DEFAULT`, #303136 `ink.DEFAULT`); span::after 12pxx12px background #303136 `ink.DEFAULT`.

![Announcement strip default](components/crops/promo-strip-default.png)

#### Announcement link
Read as `promo-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 587.69 x 24; background transparent; text agileSans 16/24 350, #303136 `ink.DEFAULT` |
| focus-visible | outline 1px auto #005fcc, offset 4px |

Child layers that carry the look: span 587.7x23 image linear-gradient(#303136 `ink.DEFAULT`, #303136 `ink.DEFAULT`); span::after 12pxx12px background #303136 `ink.DEFAULT`.

![Announcement link default](components/crops/promo-link-default.png) ![Announcement link hover](components/crops/promo-link-hover.png) ![Announcement link focus-visible](components/crops/promo-link-focus-visible.png) ![Announcement link pressed](components/crops/promo-link-pressed.png)

#### Sign in link
The sign-in link at the strip's far right; points at my.1password.com. Read as `signin-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 49.2 x 24; background transparent; text agileSans 16/24 350, #303136 `ink.DEFAULT` |
| focus-visible | outline 1px auto #005fcc, offset 4px |

Child layers that carry the look: span 49.2x23 image linear-gradient(#303136 `ink.DEFAULT`, #303136 `ink.DEFAULT`).

![Sign in link default](components/crops/signin-link-default.png) ![Sign in link hover](components/crops/signin-link-hover.png) ![Sign in link focus-visible](components/crops/signin-link-focus-visible.png) ![Sign in link pressed](components/crops/signin-link-pressed.png)

#### Header
The white sticky bar (header-navigation): wordmark, Business/Personal/Developers/Partners/Resources flyout buttons, Pricing link, then Talk to sales and the blue Get started free pill. Read as `header` on the home page.

**Values (default).** size 1440 x 132; background #ffffff `paper.DEFAULT`; text agileSans 16/24 350, #303136 `ink.DEFAULT`; icon 12 x 12, #303136 `ink.DEFAULT`.

![Header default](components/crops/header-default.png)

#### Wordmark
Read as `logo` on the home page.

**Values (default).** size 143 x 27.33; background transparent; text agileSans 16/24 350, #000000; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1).

![Wordmark default](components/crops/logo-default.png)

#### Nav flyout button
A group/nav-item button (Business, Personal, Developers, Partners, Resources); opens the mega flyout on hover. Read as `nav-flyout-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 78.09 x 28; padding 2px 0px; background transparent; image linear-gradient(#000000, #000000); text agileSans 16/24 400, #303136 `ink.DEFAULT`; transition background-size 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, #303136 `ink.DEFAULT` |
| focus-visible | outline 1px auto #005fcc, offset 3px |

![Nav flyout button default](components/crops/nav-flyout-button-default.png) ![Nav flyout button hover](components/crops/nav-flyout-button-hover.png) ![Nav flyout button focus-visible](components/crops/nav-flyout-button-focus-visible.png) ![Nav flyout button pressed](components/crops/nav-flyout-button-pressed.png)

#### Nav flyout
The mega panel a nav group opens on click (Business, Personal, ...): product and feature links in columns. Read as `nav-flyout` on the home page.

**Values (open).** size 1248 x 675; background transparent; text agileSans 16/20 300, #6c6e7a; transition all 0.3s cubic-bezier(0, 0, 0.2, 1).

Child layers that carry the look: div 1248x675 background #ffffff `paper.DEFAULT` border 1px solid #e7e7e9 radius 12px shadow rgba(0, 0, 0, 0.1) 0px 6px 14px 0px, rgba(0, 0, 0, 0.09) 0px 26px 26px 0px, rgba(0, 0, 0, 0.05) 0px 58px 35px 0px, rgba(0, 0, 0, 0.01) 0px 104px 41px 0px, transparent 0px 162px 45px 0px; div 20x26 background #303136 `ink.DEFAULT`; span 62.1x23 image linear-gradient(#303136 `ink.DEFAULT`, #303136 `ink.DEFAULT`).

![Nav flyout open](components/crops/nav-flyout-open.png)

#### Nav link
A plain text nav item (Pricing). Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 155.98 x 21; background transparent; text agileSans 16/24 400, #303136 `ink.DEFAULT` |
| hover | text agileSans 16/24 400, #145fe4 |
| focus-visible | outline 1px auto #005fcc, offset 4px |
| pressed | text agileSans 16/24 400, #145fe4 |

Child layers that carry the look: div 20x26 background #303136 `ink.DEFAULT`; span 48.2x23 image linear-gradient(#303136 `ink.DEFAULT`, #303136 `ink.DEFAULT`).

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Header primary CTA
The blue cta-btn pill at the header's far right ("Get started free"). Read as `cta-header-primary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 168.53 x 46; padding 10px 24px; border 1px solid transparent; radius 9999px; background transparent; text agileSans 16/24 400, #ffffff `paper.DEFAULT`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text agileSans 16/24 400, #145fe4 |
| focus-visible | border 1px solid #145fe4; outline 1px solid #145fe4, offset 3px; text agileSans 16/24 400, #145fe4; transition none 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| pressed | text agileSans 16/24 400, #145fe4 |

![Header primary CTA default](components/crops/cta-header-primary-default.png) ![Header primary CTA hover](components/crops/cta-header-primary-hover.png) ![Header primary CTA focus-visible](components/crops/cta-header-primary-focus-visible.png) ![Header primary CTA pressed](components/crops/cta-header-primary-pressed.png)

#### Header sales link
Read as `cta-header-sales` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 86.83 x 28; padding 2px 0px; background transparent; text agileSans 16/24 400, #303136 `ink.DEFAULT` |
| focus-visible | outline 1px auto #005fcc, offset 4px |

Child layers that carry the look: span 86.8x23 image linear-gradient(#303136 `ink.DEFAULT`, #303136 `ink.DEFAULT`).

![Header sales link default](components/crops/cta-header-sales-default.png) ![Header sales link hover](components/crops/cta-header-sales-hover.png) ![Header sales link focus-visible](components/crops/cta-header-sales-focus-visible.png) ![Header sales link pressed](components/crops/cta-header-sales-pressed.png)

#### Footer
The footer: link columns, legal row, social icons. Read as `footer` on the home page.

**Values (default).** size 1440 x 1276.66; background #1d1d21 `ink.footer`; text agileSans 16/24 300, #ffffff `paper.DEFAULT`; icon 16 x 16, rgba(255, 255, 255, 0.8).

![Footer default](components/crops/footer-default.png)

### Home

The marketing home page: the navy gradient hero with the 88px display headline and the product collage below, plus section bands down the page.

#### Hero
The opening band on bg-hero-gradient-blue: oversized display headline, sub copy and the CTA row on a dark field above the product collage. Read as `hero` on the home page.

**Values (default).** size 1392 x 1222.39; padding 0px 24px; radius 0px 0px 48px 48px; background transparent; image linear-gradient(#1d1d21 `ink.footer` 0px, #1d1d21 `ink.footer` 25%, #145fe4 70%, #99beff 100%); text agileSans 88/96.8 300, #ffffff `paper.DEFAULT`; icon 16 x 16, #ffffff `paper.DEFAULT`.

![Hero default](components/crops/hero-default.png)

#### Hero title
Display copy in agileSans, ~88px light. Read as `hero-title` on the home page.

**Values (default).** size 822 x 290.39; background transparent; text agileSans 88/96.8 300, #ffffff `paper.DEFAULT`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero primary CTA
The white cta-btn pill in the hero ("Talk to sales"). Read as `cta-hero-primary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 204 x 46; padding 10px 24px; border 1px solid transparent; radius 9999px; background transparent; text agileSans 16/24 400, #145fe4; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text agileSans 16/24 400, #ffffff `paper.DEFAULT` |
| focus-visible | border 1px solid #ffffff `paper.DEFAULT`; outline 1px solid #ffffff `paper.DEFAULT`, offset 3px; text agileSans 16/24 400, #ffffff `paper.DEFAULT`; transition none 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| pressed | text agileSans 16/24 400, #ffffff `paper.DEFAULT` |

![Hero primary CTA default](components/crops/cta-hero-primary-default.png) ![Hero primary CTA hover](components/crops/cta-hero-primary-hover.png) ![Hero primary CTA focus-visible](components/crops/cta-hero-primary-focus-visible.png) ![Hero primary CTA pressed](components/crops/cta-hero-primary-pressed.png)

#### Hero secondary CTA
The bordered outline pill beside the primary ("View plans"). Read as `cta-hero-secondary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 204 x 46; padding 10px 24px; border 1px solid transparent; radius 9999px; background transparent; text agileSans 16/24 400, #ffffff `paper.DEFAULT`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text agileSans 16/24 400, #1d1d21 `ink.footer` |
| focus-visible | outline 1px solid #ffffff `paper.DEFAULT`, offset 3px; text agileSans 16/24 400, #1d1d21 `ink.footer`; transition none 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| pressed | text agileSans 16/24 400, #1d1d21 `ink.footer` |

![Hero secondary CTA default](components/crops/cta-hero-secondary-default.png) ![Hero secondary CTA hover](components/crops/cta-hero-secondary-hover.png) ![Hero secondary CTA focus-visible](components/crops/cta-hero-secondary-focus-visible.png) ![Hero secondary CTA pressed](components/crops/cta-hero-secondary-pressed.png)

#### Video embed
The hero product video: a cross-origin Vimeo iframe. The element's box and style were measured; its contents are unreachable (cross-origin), so nothing inside is claimed. Read as `video-embed` on the home page.

**Values (default).** size 1248 x 702; background transparent; text agileSans 16/24 350, #000000.

![Video embed default](components/crops/video-embed-default.png)

#### Section title
Read as `section-title` on the home page.

**Values (default).** size 822 x 211.22; background transparent; text agileSans 64/70.4 300, #ffffff `paper.DEFAULT`.

![Section title default](components/crops/section-title-default.png)

### Pricing

The pricing page: the `segment-selector` plan pill (Enterprise/Business/Individual) beside the title, the five-column platform/product grid with Request a quote pills, and the FAQ accordions.

#### Pricing title
Read as `pricing-title` on the pricing page.

**Values (default).** size 571.03 x 70.41; background transparent; text agileSans 64/70.4 300, #303136 `ink.DEFAULT`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Plan selector
The large bordered pill beside the h1 that switches the grid between Enterprise / Business / Individual & Family. Read as `plan-selector` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 378.53 x 98.41; background transparent; text agileSans 64/70.4 300, #145fe4; icon 48 x 48, #145fe4 |
| focus-visible | outline 2px solid transparent, offset 2px |

Child layers that carry the look: div 378.5x98.4 border 2px solid #145fe4 radius 20px 20px 0px 0px; div 378.5x309.2 border 2px solid #145fe4 radius 0px 0px 20px 20px; div 378.5x98.4 border 2px solid #145fe4 radius 20px 20px 0px 0px.

![Plan selector default](components/crops/plan-selector-default.png) ![Plan selector hover](components/crops/plan-selector-hover.png) ![Plan selector focus-visible](components/crops/plan-selector-focus-visible.png) ![Plan selector pressed](components/crops/plan-selector-pressed.png)

#### Product column
One column of the platform/product pricing grid: kicker, product name, blurb, CTA pill and a feature list. Read as `product-column` on the pricing page.

**Values (default).** size 248.8 x 563.59; padding 24px 0px 0px 0px; border R: 2px solid #e7e7e9; background transparent; text agileSans 16/20 300, #303136 `ink.DEFAULT`.

Child layers that carry the look: div 248.8x563.6 border 2px solid #e7e7e9; a 217.2x46 border 1px solid transparent radius 9999px; a::before 215.172pxx44px background #145fe4 radius 9999px.

![Product column default](components/crops/product-column-default.png)

#### Product name
Read as `product-name` on the pricing page.

**Values (default).** size 217.17 x 57.59; background transparent; text agileSans 24/28.8 400, #303136 `ink.DEFAULT`.

![Product name default](components/crops/product-name-default.png)

#### Request a quote CTA
Read as `cta-quote` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 217.17 x 46; padding 10px 24px; border 1px solid transparent; radius 9999px; background transparent; text agileSans 16/24 400, #ffffff `paper.DEFAULT`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text agileSans 16/24 400, #145fe4 |
| focus-visible | border 1px solid #145fe4; outline 1px solid #145fe4, offset 3px; text agileSans 16/24 400, #145fe4; transition none 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| pressed | text agileSans 16/24 400, #145fe4 |

![Request a quote CTA default](components/crops/cta-quote-default.png) ![Request a quote CTA hover](components/crops/cta-quote-hover.png) ![Request a quote CTA focus-visible](components/crops/cta-quote-focus-visible.png) ![Request a quote CTA pressed](components/crops/cta-quote-pressed.png)

#### FAQ row
A collapsible question row in the dark FAQ band; focus lands on its "Answer to" toggle. Read as `faq-row` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 604 x 121.59; padding 32px 0px; background transparent; text agileSans 24/28.8 400, #ffffff `paper.DEFAULT`; icon 24 x 24, #ffffff `paper.DEFAULT` |

![FAQ row default](components/crops/faq-row-default.png) ![FAQ row hover](components/crops/faq-row-hover.png) ![FAQ row focus-visible](components/crops/faq-row-focus-visible.png) ![FAQ row pressed](components/crops/faq-row-pressed.png)

#### FAQ answer
The expanded answer body under a FAQ row. Read as `faq-answer` on the pricing page.

**Values (open).** size 604 x 104; padding 0px 48px 32px 0px; background transparent; text agileSans 16/24 300, #ffffff `paper.DEFAULT`; transition all 0.5s cubic-bezier(0.4, 0, 0.2, 1).

![FAQ answer open](components/crops/faq-answer-open.png)

### Product page

The enterprise-password-manager marketing page: title, CTAs, feature cards and the Marketplace link.

#### Product title
Read as `product-title` on the product page.

**Values (default).** size 640 x 140.81; background transparent; text agileSans 64/70.4 300, #ffffff `paper.DEFAULT`.

![Product title default](components/crops/product-title-default.png)

#### Product primary CTA
Read as `cta-product-primary` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 168.53 x 46; padding 10px 24px; border 1px solid transparent; radius 9999px; background transparent; text agileSans 16/24 400, #ffffff `paper.DEFAULT`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text agileSans 16/24 400, #145fe4 |
| focus-visible | border 1px solid #145fe4; outline 1px solid #145fe4, offset 3px; text agileSans 16/24 400, #145fe4; transition none 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| pressed | text agileSans 16/24 400, #145fe4 |

![Product primary CTA default](components/crops/cta-product-primary-default.png) ![Product primary CTA hover](components/crops/cta-product-primary-hover.png) ![Product primary CTA focus-visible](components/crops/cta-product-primary-focus-visible.png) ![Product primary CTA pressed](components/crops/cta-product-primary-pressed.png)

#### Feature card
A product-feature card on the marketing page. Read as `feature-card` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1392 x 726.41; radius 25px; background transparent; text agileSans 64/70.4 300, #303136 `ink.DEFAULT` |

![Feature card default](components/crops/feature-card-default.png) ![Feature card hover](components/crops/feature-card-hover.png)

#### Marketplace link
The link to the 1Password Marketplace (marketplace.1password.com) on the product page. Read as `cta-marketplace` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 163.83 x 21; background transparent; text agileSans 16/25.6 350, rgba(255, 255, 255, 0.8) |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Marketplace link default](components/crops/cta-marketplace-default.png) ![Marketplace link hover](components/crops/cta-marketplace-hover.png) ![Marketplace link focus-visible](components/crops/cta-marketplace-focus-visible.png) ![Marketplace link pressed](components/crops/cta-marketplace-pressed.png)

### Downloads

The per-platform download page: title, the macOS platform pill and the download button. Clicking it starts a download, which was never done.

#### Download title
The display heading "Download 1Password for macOS": the h1 itself is sr-only, so the styled text block was measured instead. Read as `download-title` on the download page.

**Values (default).** size 678.52 x 70.41; background transparent; text agileSans 64/70.4 300, #303136 `ink.DEFAULT`.

![Download title default](components/crops/download-title-default.png)

#### Download button
Read as `download-button` on the download page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 266.52 x 46; padding 10px 24px; border 1px solid transparent; radius 9999px; background transparent; text agileSans 16/24 400, #ffffff `paper.DEFAULT`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text agileSans 16/24 400, #145fe4 |
| focus-visible | border 1px solid #145fe4; outline 1px solid #145fe4, offset 3px; text agileSans 16/24 400, #145fe4; transition none 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| pressed | text agileSans 16/24 400, #145fe4 |

![Download button default](components/crops/download-button-default.png) ![Download button hover](components/crops/download-button-hover.png) ![Download button focus-visible](components/crops/download-button-focus-visible.png) ![Download button pressed](components/crops/download-button-pressed.png)

#### Platform link
A link to another platform's download page. Read as `platform-link` on the download page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 96 x 130.5; radius 12px; background transparent; text agileSans 15/22.5 350, #303136 `ink.DEFAULT` |
| focus-visible | outline 2px solid #3b66bc, offset 2px |

Child layers that carry the look: div 96x96 background #f6f8fc radius 12px.

![Platform link default](components/crops/platform-link-default.png) ![Platform link hover](components/crops/platform-link-hover.png) ![Platform link focus-visible](components/crops/platform-link-focus-visible.png) ![Platform link pressed](components/crops/platform-link-pressed.png)

#### Platform pill
The macOS platform selector under the title, same segment-selector control as the pricing plan pill. Read as `platform-pill` on the download page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 377.19 x 121.41; padding 8px 8px 0px 8px; border 4px solid transparent; background transparent; text agileSans 64/70.4 350, #3b66bc |
| focus-visible | border 4px solid #3b66bc; radius 12px; outline 2px solid transparent, offset 2px |

![Platform pill default](components/crops/platform-pill-default.png) ![Platform pill hover](components/crops/platform-pill-hover.png) ![Platform pill focus-visible](components/crops/platform-pill-focus-visible.png) ![Platform pill pressed](components/crops/platform-pill-pressed.png)

### Developer

The developer-security page: title, feature/link cards and docs CTAs.

#### Developer title
Read as `dev-title` on the developer page.

**Values (default).** size 640 x 140.81; background transparent; text agileSans 64/70.4 300, #ffffff `paper.DEFAULT`.

![Developer title default](components/crops/dev-title-default.png)

#### Developer CTA
Read as `dev-cta` on the developer page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 168.53 x 46; padding 10px 24px; border 1px solid transparent; radius 9999px; background transparent; text agileSans 16/24 400, #ffffff `paper.DEFAULT`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | border 1px solid #ffffff `paper.DEFAULT`; outline 1px solid #ffffff `paper.DEFAULT`, offset 3px; transition none 0.3s cubic-bezier(0.4, 0, 0.2, 1) |

![Developer CTA default](components/crops/dev-cta-default.png) ![Developer CTA hover](components/crops/dev-cta-hover.png) ![Developer CTA focus-visible](components/crops/dev-cta-focus-visible.png) ![Developer CTA pressed](components/crops/dev-cta-pressed.png)

#### Developer card
A feature/link card on the developer page. Read as `dev-card` on the developer page.

**Values (default).** size 405.33 x 384.81; border 1px solid #d7d7db; radius 25px; background #f2f2f3; text agileSans 32/38.4 300, #303136 `ink.DEFAULT`.

![Developer card default](components/crops/dev-card-default.png)

### Forms

Fields reachable signed out: the contact-sales page's embedded Marketo form (cross-origin, measured as a frame only).

#### Contact title
Read as `contact-title` on the contact page.

**Values (default).** size 584 x 140.81; background transparent; text agileSans 64/70.4 300, #303136 `ink.DEFAULT`.

![Contact title default](components/crops/contact-title-default.png)

#### Select field
Read as `field-select` on the contact page.

**Values (default).** size 128 x 50; radius 4px; background transparent; text agileSans 16/24 300, #ffffff `paper.DEFAULT`.

Child layers that carry the look: div 0x0 background #ffffff `paper.DEFAULT` border 1px solid #f2f2f3 radius 4px; div 0x0 background #f6f8fc radius 4px; div 0x0 background #ffffff `paper.DEFAULT`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Sales form embed
The contact form is a Marketo iframe hosted on integrations.1passwordservices.com. The element box was measured; the fields inside are cross-origin and were neither introspected nor submitted. Read as `form-embed` on the contact page.

**Values (default).** size 504 x 915; background transparent; text agileSans 16/24 350, #000000.

![Sales form embed default](components/crops/form-embed-default.png)

### Mobile (390 wide)

The same chrome as a phone draws it, at 390 x 844 with an iPhone user agent.

#### Mobile header
The 390-wide header bar. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 825.56; padding 128px 0px 0px 0px; background #1d1d21 `ink.footer`; text agileSans 48/52.8 300, #ffffff `paper.DEFAULT`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
Opens the mobile nav drawer. Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 20 x 20; background transparent; outline 2px solid transparent, offset 2px; text agileSans 16/24 350, #000000 |

Child layers that carry the look: button 20x20; span 20x2 background #303136 `ink.DEFAULT` radius 2px; span::before 20pxx2px background #303136 `ink.DEFAULT` radius 2px.

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile nav drawer
The sheet the menu button opens. Read as `m-nav-drawer` on the home page at 390 wide.

**Values (open).** size 390 x 615; background transparent; text agileSans 24/28.8 350, #303136 `ink.DEFAULT`; transition transform 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #303136 `ink.DEFAULT`.

Child layers that carry the look: div 92.7x31 image linear-gradient(#000000, #000000); span 92.7x33 image linear-gradient(#303136 `ink.DEFAULT`, #303136 `ink.DEFAULT`); div 90.6x31 image linear-gradient(#000000, #000000).

![Mobile nav drawer open](components/crops/m-nav-drawer-open.png)

#### Mobile hero title
Read as `m-hero-title` on the home page at 390 wide.

**Values (default).** size 342 x 211.19; background transparent; text agileSans 48/52.8 300, #ffffff `paper.DEFAULT`.

![Mobile hero title default](components/crops/m-hero-title-default.png)

### Sign-in boundary

start.1password.com under a headless browser: it redirects to /unsupported, captured as the honest edge of the public surface. The vault needs an account, a secret key and a master password.

#### Unsupported-browser page
start.1password.com gates headless/unsupported browsers here instead of the sign-in form. Measured as the honest edge of the public surface; the vault itself is credential-gated and out of scope. Read as `unsupported-card` on the signin page.

**Values (default).** size 1440 x 900; background transparent; text Inter V 18.75/21 600, rgba(0, 0, 0, 0.82); icon 16 x 16, rgba(0, 0, 0, 0.82).

Child layers that carry the look: div 1440x900 background #f6f7f8; div::before 32pxx96594px background #ffffff `paper.DEFAULT` shadow #ffffff `paper.DEFAULT` -1px 0px 0px 0px, rgba(0, 0, 0, 0.13) 1px 0px 0px 0px inset, rgba(0, 0, 0, 0.13) -1px 0px 0px 0px inset, #ffffff `paper.DEFAULT` -2px 0px 0px 0px inset; div::after 32pxx96594px background #ffffff `paper.DEFAULT` shadow #ffffff `paper.DEFAULT` 1px 0px 0px 0px, rgba(0, 0, 0, 0.13) 1px 0px 0px 0px inset, rgba(0, 0, 0, 0.13) -1px 0px 0px 0px inset, #ffffff `paper.DEFAULT` 2px 0px 0px 0px inset.

![Unsupported-browser page default](components/crops/unsupported-card-default.png)

#### Unsupported title
Read as `unsupported-title` on the signin page.

**Values (default).** size 420 x 21; background transparent; text Inter V 18.75/21 600, rgba(0, 0, 0, 0.82).

![Unsupported title default](components/crops/unsupported-title-default.png)
## Gaps

### Pages

- **The vault and everything behind sign-in.** The product itself is credential-gated (account + secret key + master password, not OAuth): app views, the admin console, settings and billing were never reached. start.1password.com gates headless browsers to /unsupported, which was captured instead.
- **Anything that sends.** No form was submitted, nothing bought, nothing downloaded; the contact form's fields live inside a cross-origin Marketo iframe and were neither introspected nor submitted.
- **The OneTrust consent card** mounts on first visits only (it renders in a closed shadow root, invisible to DOM queries). An OptanonAlertBoxClosed cookie is seeded before navigation and a geometric sweep hides any residual overlay, so it has no component entry.
- **The nav flyout's other tabs** (Personal, Developers, Partners, Resources) were not opened; only the Business panel was measured.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover), so a state a script adds on mousedown (if any) is missing.
- **The Vimeo player and Marketo form** are cross-origin iframes: their element boxes are measured (video-embed, form-embed) but their contents are unreachable, so nothing inside them is claimed.
- **The sign-in card itself** never renders headlessly (start.1password.com redirects to /unsupported), so only the unsupported page carries measurements.

### Themes

1password.com serves one light theme: no dark attribute is set anywhere, the Tailwind build declares no dark variant, and nothing in the capture hints at a toggle. The token file therefore ships no dark set.

### Fonts

- **Agile Sans Variable** and **Agile Mono Variable** are 1Password's own faces, served as woff/woff2 from `/_next/static/media/` (`fonts` in [raw/css-vars.json](raw/css-vars.json)). The style guide falls back to the system sans/mono for them.
- The **Marketo iframe** and **start.1password.com** use their own faces, which are not part of this token set.

### Screenshots

- Screens and product imagery are 1Password's content and appears only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- No personal data was captured: every page was read signed out with an empty session, and the only fields touched were the consent sweep and UI toggles; no text was ever typed into a form.
