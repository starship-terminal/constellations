# Cohere components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from cohere.com on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, paid for or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (39 components, 97 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Unica77 Cohere Web 16/22.4 400, #212121`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (93 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`; every public route paints the same light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages (1x on desktop, 2x on mobile); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| North | `/north` | [default](screenshots/north-light-default.png), [full](screenshots/north-light-full.png) |
| Command | `/command` | [default](screenshots/command-light-default.png), [full](screenshots/command-light-full.png) |
| Models | `/models-overview` | [default](screenshots/models-light-default.png), [full](screenshots/models-light-full.png) |
| Developers | `/developers` | [default](screenshots/developers-light-default.png), [full](screenshots/developers-light-full.png) |
| Customer stories | `/customer-stories` | [default](screenshots/stories-light-default.png), [full](screenshots/stories-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Privacy | `/privacy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Terms | `/terms-of-use` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| Sign-in (boundary) | `dashboard.cohere.com/welcome/login` | [default](screenshots/signin-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| North, phone | `/north` | [default](screenshots/mobile-north-light-default.png), [full](screenshots/mobile-north-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu, open | bar, phone | the hamburger's own press | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-open](#m-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 18 components were given a real keyboard focus (a further 1 could not be driven: `footer-social`). 17 show a visible focus state: `banner-close` (1px auto #101010, offset 0px), `nav-item` (1px auto #101010, offset 1px), `nav-signin` (2px solid #4c6ee6 `color.blue.500`, offset 2px), `nav-cta` (visible change in boxShadow/borderTopColor), `hero-cta` (visible change in boxShadow), `cta-dark` (visible change in boxShadow/borderTopColor), `cta-light` (visible change in boxShadow), `callout-card` (1px auto #101010, offset 1px), `price-tab` (1px auto #101010, offset 0px), `price-tab-off` (1px auto #101010, offset 0px), `faq-item` (1px auto #101010, offset 0px), `north-cta` (visible change in boxShadow), `command-cta` (visible change in boxShadow), `signin-oauth` (1px solid #616161 `color.volcanic.700`, offset 4px), `footer-link` (1px auto #101010, offset 1px), `footer-cta` (visible change in boxShadow), `m-menu-link` (1px auto #e59700, offset 0px). The other 1 show no change a keyboard user can see: `signin-submit`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). On 12 of 18 measured controls pressed reads as the same painted step as hover; the rest differ — `nav-cta`, `hero-cta`, `cta-light`, `north-cta`, `command-cta`, `signin-oauth` (their rows show the diff). Nothing a real press would submit, navigate or write (the CTAs navigate onward, the sign-in OAuth and Log-in controls submit) was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | backdrop-filter, background-color, border-color, box-shadow, color, fill, filter, opacity, stroke, text-decoration-color, transform | faq-item-open, signin-oauth |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | nav-item |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | all, background-color, color, transform | banner-close, header, m-header, nav-signin |
| 0.3s | `ease` | background-color, color | command-cta, cta-dark, cta-light, footer-cta, hero-cta, nav-cta, north-cta |
| 0.5s | `cubic-bezier(0.4, 0, 0.2, 1)` | clip-path | m-menu-open |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Callout card](#callout-card) | 437.33 x 492.81 | - | 22px | transparent | none | 0 |
| [FAQ row](#faq-row) | 660 x 61.2 | - | - | transparent | none | 0px 0px 36px 0px |
| [Sign-in card](#sign-in-card) | 566 x 235 | - | - | transparent | none | 0 |
| [Dark CTA](#dark-cta) | 146 x 53.2 | 2px solid transparent | 9999px | #17171c `color.neutral.15` | none | 12px 24px |

## Components

### Shell and navigation

The dismissible pureBlack promo banner and the fixed site nav: the Cohere mark, the roll-hover nav links, the Sign-in ghost and the dark Request-a-demo pill.

#### Promo banner
The dismissible announcement strip above the nav ("Rerank 5 is here…"), bg-pureBlack, with its Learn-more link and close control. Read as `promo-banner` on the home page.

**Values (default).** size 1440 x 48; padding 12px; background #000000 `color.pureBlack`; text Unica77 Cohere Web 16/22.4 400, #ffffff `color.pureWhite`.

![Promo banner default](components/crops/promo-banner-default.png)

#### Banner close
The promo banner close button (icon-close, hover rotate-90). A local dismiss toggle — pressing it only hides the banner. Read as `banner-close` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 16 x 24; background transparent; text Unica77 Cohere Web 16/24 400, #ffffff `color.pureWhite`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | size 24 x 16; transform matrix(0, 1, -1, 0, 0, 0) |
| focus-visible | outline 1px auto #101010, offset 0px; child paint button.mt-1.self-start: size 16.0x24.0; outline 1px auto rgb(16, 16, 16) offset 0px |
| pressed | size 24 x 16; transform matrix(0, 1, -1, 0, 0, 0) |

![Banner close default](components/crops/banner-close-default.png) ![Banner close hover](components/crops/banner-close-hover.png) ![Banner close focus-visible](components/crops/banner-close-focus-visible.png) ![Banner close pressed](components/crops/banner-close-pressed.png)

#### Nav bar
The fixed site nav (nav.z-nav, h-[60px] inner bar): Cohere mark, roll-hover nav links, Sign in + Request-a-demo CTAs. Read as `header` on the home page.

**Values (default).** size 1440 x 60; background transparent; text Unica77 Cohere Web 14/19.6 400, #000000 `color.pureBlack`; transition transform 0.3s cubic-bezier(0.4, 0, 0.2, 1).

Child layers that carry the look: div 1440x60 background #ffffff `color.pureWhite`; a 42x31.6; div 0x1 image linear-gradient(to right, #ff7759 `color.coral.500`, #7670c5, #4c6ee6 `color.blue.500`).

![Nav bar default](components/crops/header-default.png)

#### Logo
The Cohere mark home anchor in the nav (h-5 w-[118px] svg). Read as `logo` on the home page.

**Values (default).** size 118 x 24; background transparent; text Unica77 Cohere Web 16/24 400, #000000 `color.pureBlack`.

![Logo default](components/crops/logo-default.png)

#### Nav link
A flat nav link with the roll-hover duplicate text (group/nav-link, hover translates the label -100%). Read as `nav-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 81 x 31.59; padding 6px 12px; radius 9999px; background transparent; text Unica77 Cohere Web 14/19.6 400, #000000 `color.pureBlack`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | background rgba(242, 242, 242, 0.93); outline 1px auto #101010, offset 1px; child paint a.group/nav-link.inline-flex: size 81.0x31.6; background rgba(242, 242, 242, 0.93); radius 9999px; outline 1px auto rgb(16, 16, 16) offset 1px |

![Nav link default](components/crops/nav-item-default.png) ![Nav link hover](components/crops/nav-item-hover.png) ![Nav link focus-visible](components/crops/nav-item-focus-visible.png) ![Nav link pressed](components/crops/nav-item-pressed.png)

#### Nav sign-in
The transparent "Sign in" ghost control linking to dashboard.cohere.com; measured never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 42 x 31.59; padding 6px 0px; background transparent; outline 2px solid transparent, offset 2px; text Unica77 Cohere Web 14/19.6 400, #212121 `color.volcanic.900`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | child paint div.ease-button-gradient.absolute: size 42.0x1.0 |
| focus-visible | outline 2px solid #4c6ee6 `color.blue.500`, offset 2px; child paint a.whitespace-nowrap.pt-1.5: outline 2px solid rgb(76, 110, 230) offset 2px |

Child layers that carry the look: a 42x31.6; div 0x1 image linear-gradient(to right, #ff7759 `color.coral.500`, #7670c5, #4c6ee6 `color.blue.500`).

![Nav sign-in default](components/crops/nav-signin-default.png) ![Nav sign-in hover](components/crops/nav-signin-hover.png) ![Nav sign-in focus-visible](components/crops/nav-signin-focus-visible.png) ![Nav sign-in pressed](components/crops/nav-signin-pressed.png)

#### Nav CTA
The dark "Request a demo" ease-button-gradient pill in the nav; links to the contact form, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 139 x 36; padding 0px 16px; border 2px solid transparent; radius 9999px; background #17171c `color.neutral.15`; outline 2px solid transparent, offset 2px; text Unica77 Cohere Web 14/19.6 400, #ffffff `color.pureWhite`; transition background-color 0.3s ease, color 0.3s ease |
| hover | background #000000 `color.pureBlack`; child paint a.whitespace-nowrap.relative: background #000000 `color.pureBlack`; el::before: opacity 0.994343 |
| focus-visible | border 2px solid #fafafa `color.neutral.95`; shadow #4c6ee6 0px 0px 0px 2px; child paint a.whitespace-nowrap.relative: border 2px solid #fafafa `color.neutral.95`; shadow rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(76, 110, 230) 0px 0px 0px 2px |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

### Home

The hero ("Your AI. Your rules."), the ease-button-gradient CTAs, the callout-module cards and the customer-logo marquee.

#### Hero title
"Your AI. Your rules." — the hero headline (web3 display scale). Read as `hero-title` on the home page.

**Values (default).** size 1128 x 192; background transparent; text CohereText 96/96 400, #212121 `color.volcanic.900`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero CTA
The first ease-button-gradient CTA in page content ("Explore now"-style pill); links onward, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 152 x 53.2; padding 12px 24px; border 2px solid transparent; radius 9999px; background #ffffff `color.pureWhite`; outline 2px solid transparent, offset 2px; text Unica77 Cohere Web 18/25.2 400, #17171c `color.neutral.15`; transition background-color 0.3s ease, color 0.3s ease |
| hover | text Unica77 Cohere Web 18/25.2 400, #000000 `color.pureBlack`; child paint el::before: opacity 0.989676 |
| focus-visible | shadow #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px; child paint a.relative.flex: shadow rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 2px, rgb(76, 110, 230) 0px 0px 0px 4px, rgb(255, 255, 255) 0px 0px 0px 6px |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Dark CTA
A dark ease-button-gradient pill (bg-neutral-15 text-pureWhite, gradient hover sweep) in page content. Read as `cta-dark` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 146 x 53.2; padding 12px 24px; border 2px solid transparent; radius 9999px; background #17171c `color.neutral.15`; outline 2px solid transparent, offset 2px; text Unica77 Cohere Web 18/25.2 400, #ffffff `color.pureWhite`; transition background-color 0.3s ease, color 0.3s ease |
| focus-visible | border 2px solid #fafafa `color.neutral.95`; shadow #4c6ee6 0px 0px 0px 2px; child paint a.relative.flex: border 2px solid #fafafa `color.neutral.95`; shadow rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(76, 110, 230) 0px 0px 0px 2px |
| hover | size unmeasured — the capture failed on this pass |

![Dark CTA default](components/crops/cta-dark-default.png) ![Dark CTA focus-visible](components/crops/cta-dark-focus-visible.png) ![Dark CTA pressed](components/crops/cta-dark-pressed.png)

#### Light CTA
A light ease-button-gradient pill (bg-pureWhite text-neutral-15) in page content. Read as `cta-light` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 152 x 53.2; padding 12px 24px; border 2px solid transparent; radius 9999px; background #ffffff `color.pureWhite`; outline 2px solid transparent, offset 2px; text Unica77 Cohere Web 18/25.2 400, #17171c `color.neutral.15`; transition background-color 0.3s ease, color 0.3s ease |
| hover | text Unica77 Cohere Web 18/25.2 400, #000000 `color.pureBlack`; child paint el::before: opacity 0.994343 |
| focus-visible | shadow #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px; child paint a.relative.flex: shadow rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 2px, rgb(76, 110, 230) 0px 0px 0px 4px, rgb(255, 255, 255) 0px 0px 0px 6px |

![Light CTA default](components/crops/cta-light-default.png) ![Light CTA hover](components/crops/cta-light-hover.png) ![Light CTA focus-visible](components/crops/cta-light-focus-visible.png) ![Light CTA pressed](components/crops/cta-light-pressed.png)

#### Callout card
A callout-module card anchor (group/calloutCard, rounded-lg/xl). Read as `callout-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 437.33 x 492.81; radius 22px; background transparent; text CohereMono 14/19.6 400, #212121 `color.volcanic.900` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.group/calloutCard.relative: size 437.3x492.8; radius 22px; outline 1px auto rgb(16, 16, 16) offset 1px |

Child layers that carry the look: div 437.3x421.2 background #f0eee9 radius 22px 22px 0px 0px.

![Callout card default](components/crops/callout-card-default.png) ![Callout card hover](components/crops/callout-card-hover.png) ![Callout card focus-visible](components/crops/callout-card-focus-visible.png) ![Callout card pressed](components/crops/callout-card-pressed.png)

#### Customer logo
A logo in the customer marquee (Oracle/Dell/RBC row, rendered twice for the loop). Read as `marquee-logo` on the home page.

**Values (default).** size 148 x 52; background transparent; text Unica77 Cohere Web 16/24 400, #212121 `color.volcanic.900`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Section title
A section heading under the hero (web3 display scale). Read as `section-title` on the home page.

**Values (default).** size 675.2 x 60; background transparent; text CohereText 60/60 400, #ffffff `color.pureWhite`.

![Section title default](components/crops/section-title-default.png)

#### Page ground
The body element painted fill — the page ground. Read as `page-ground` on the home page.

**Values (default).** size 1440 x 8680.09; background #ffffff `color.pureWhite`; text Unica77 Cohere Web 16/24 400, #000000 `color.pureBlack`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Pricing

The pricing route: the model-category tablist and the per-model rate table, plus the FAQ accordion.

#### Pricing title
The pricing headline. Read as `pricing-title` on the pricing page.

**Values (default).** size 1128 x 144; background transparent; text CohereText 72/72 400, #212121 `color.volcanic.900`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Category tab (selected)
The selected model-category tab (role=tab aria-selected=true — "Workplace systems") switching the rate table. Measured at rest, never switched. Read as `price-tab` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 160 x 34; padding 4px 0px; background transparent; text Unica77 Cohere Web 18/25.2 400, #17171c `color.neutral.15` |
| focus-visible | outline 1px auto #101010, offset 0px; child paint button.relative.py-1: size 160.0x34.0; outline 1px auto rgb(16, 16, 16) offset 0px |

![Category tab (selected) default](components/crops/price-tab-default.png) ![Category tab (selected) hover](components/crops/price-tab-hover.png) ![Category tab (selected) focus-visible](components/crops/price-tab-focus-visible.png) ![Category tab (selected) pressed](components/crops/price-tab-pressed.png)

#### Category tab (unselected)
An unselected model-category tab (aria-selected=false); never pressed — it would swap the rate table. Read as `price-tab-off` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 153 x 34; padding 4px 0px; background transparent; text Unica77 Cohere Web 18/25.2 400, #17171c `color.neutral.15` |
| focus-visible | outline 1px auto #101010, offset 0px; child paint button.relative.py-1: size 153.0x34.0; outline 1px auto rgb(16, 16, 16) offset 0px |

![Category tab (unselected) default](components/crops/price-tab-off-default.png) ![Category tab (unselected) hover](components/crops/price-tab-off-hover.png) ![Category tab (unselected) focus-visible](components/crops/price-tab-off-focus-visible.png) ![Category tab (unselected) pressed](components/crops/price-tab-off-pressed.png)

#### Rate figure
A per-model rate figure in the pricing table (the "$3.00"-style cells). Read as `price-rate` on the pricing page.

**Values (default).** size 46 x 21; background transparent; text Unica77 Cohere Web 18/25.2 400, #212121 `color.volcanic.900`.

![Rate figure default](components/crops/price-rate-default.png)

#### FAQ row
A pricing-FAQ accordion row (closed state; its own press opens the answer — a local toggle). Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 660 x 61.2; padding 0px 0px 36px 0px; background transparent; text Unica77 Cohere Web 18/25.2 400, #17171c `color.neutral.15` |
| focus-visible | outline 1px auto #101010, offset 0px; child paint button.flex.w-full: size 660.0x61.2; outline 1px auto rgb(16, 16, 16) offset 0px |

![FAQ row default](components/crops/faq-item-default.png) ![FAQ row hover](components/crops/faq-item-hover.png) ![FAQ row focus-visible](components/crops/faq-item-focus-visible.png) ![FAQ row pressed](components/crops/faq-item-pressed.png)

#### FAQ row, open
The FAQ item after its question button's own press (a local UI toggle) — the enclosing row is measured so the expanded answer lands in the state, not just the toggle. Read as `faq-item-open` on the pricing page.

**Values (opened).** size 660 x 206.2; padding 8px 0px 0px 0px; background transparent; image linear-gradient(to right, #ff7759 `color.coral.500`, #7670c5, #4c6ee6 `color.blue.500`); text Unica77 Cohere Web 18/25.2 400, #17171c `color.neutral.15`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![FAQ row, open opened](components/crops/faq-item-open-opened.png)

### North product page

The /north route: the North 2 headline and its CTA.

#### North title
"North 2: Enterprise AI without compromises" — the product page headline. Read as `north-title` on the north page.

**Values (default).** size 1128 x 144; background transparent; text CohereText 72/72 400, #ffffff `color.pureWhite`.

![North title default](components/crops/north-title-default.png)

#### North CTA
The first ease-button-gradient CTA on the North page; links onward, never followed. Read as `north-cta` on the north page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 146 x 53.2; padding 12px 24px; border 2px solid transparent; radius 9999px; background #ffffff `color.pureWhite`; outline 2px solid transparent, offset 2px; text Unica77 Cohere Web 18/25.2 400, #17171c `color.neutral.15`; transition background-color 0.3s ease, color 0.3s ease |
| hover | text Unica77 Cohere Web 18/25.2 400, #000000 `color.pureBlack`; child paint el::before: opacity 0.997558 |
| focus-visible | shadow #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px; child paint a.relative.flex: shadow rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 2px, rgb(76, 110, 230) 0px 0px 0px 4px, rgb(255, 255, 255) 0px 0px 0px 6px |

![North CTA default](components/crops/north-cta-default.png) ![North CTA hover](components/crops/north-cta-hover.png) ![North CTA focus-visible](components/crops/north-cta-focus-visible.png) ![North CTA pressed](components/crops/north-cta-pressed.png)

### Command model page

The /command route: the Command headline and its CTA.

#### Command title
"Secure, production-ready efficiency for agentic intelligence" — the model page headline. Read as `command-title` on the command page.

**Values (default).** size 1128 x 216; background transparent; text CohereText 72/72 400, #ffffff `color.pureWhite`.

![Command title default](components/crops/command-title-default.png)

#### Command CTA
The first ease-button-gradient CTA on the Command page; links onward, never followed. Read as `command-cta` on the command page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 185 x 53.2; padding 12px 24px; border 2px solid transparent; radius 9999px; background #ffffff `color.pureWhite`; outline 2px solid transparent, offset 2px; text Unica77 Cohere Web 18/25.2 400, #17171c `color.neutral.15`; transition background-color 0.3s ease, color 0.3s ease |
| hover | text Unica77 Cohere Web 18/25.2 400, #000000 `color.pureBlack`; child paint el::before: opacity 0.997558 |
| focus-visible | shadow #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px; child paint a.relative.flex: shadow rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 2px, rgb(76, 110, 230) 0px 0px 0px 4px, rgb(255, 255, 255) 0px 0px 0px 6px |

![Command CTA default](components/crops/command-cta-default.png) ![Command CTA hover](components/crops/command-cta-hover.png) ![Command CTA focus-visible](components/crops/command-cta-focus-visible.png) ![Command CTA pressed](components/crops/command-cta-pressed.png)

### App sign-in (boundary)

dashboard.cohere.com/welcome/login — the product's public login surface, measured at rest; nothing was typed, signed into or submitted.

#### Sign-in card
The dashboard.cohere.com/welcome/login surface: the sign-in card the app paints. Measured at rest, never submitted. Read as `signin-card` on the sign-in page.

**Values (default).** size 566 x 235; background transparent; text CohereMono 12/16.32 400, #212121 `color.volcanic.900`.

Child layers that carry the look: input 566x60 background #fafafa `color.neutral.95` border 1px solid #bdbdbd radius 8px 8px 0px 0px; input 566x61 background #fafafa `color.neutral.95` border 1px solid #bdbdbd radius 0px 0px 8px 8px; a 133x26 border 1px solid transparent.

![Sign-in card default](components/crops/signin-card-default.png)

#### OAuth button
A "Continue with" OAuth button on the sign-in card; measured never pressed. Read as `signin-oauth` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 281 x 40; padding 8px 12px; border 1px solid #dadce0; radius 4px; background #ffffff `color.pureWhite`; text CohereText 14/21 400, #212121 `color.volcanic.900`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #212121 `color.volcanic.900` |
| hover | border 1px solid #757575 `color.volcanic.600`; background #f5f5f5 `color.marble.200`; child paint button.group.items-center: background #f5f5f5 `color.marble.200`; border 1px solid #757575 `color.volcanic.600` |
| focus-visible | outline 1px solid #616161 `color.volcanic.700`, offset 4px; child paint button.group.items-center: outline 1px solid rgb(97, 97, 97) offset 4px |
| pressed | border 1px solid #212121 `color.volcanic.900`; background #fafafa `color.neutral.95`; child paint button.group.items-center: background #fafafa `color.neutral.95`; border 1px solid #212121 `color.volcanic.900` |

![OAuth button default](components/crops/signin-oauth-default.png) ![OAuth button hover](components/crops/signin-oauth-hover.png) ![OAuth button focus-visible](components/crops/signin-oauth-focus-visible.png) ![OAuth button pressed](components/crops/signin-oauth-pressed.png)

#### Email field
The sign-in email input — a focus reading only; nothing typed, nothing sent. Read as `signin-field` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 566 x 60; padding 28px 12px 10px 12px; border T: 1px solid #bdbdbd; R: 1px solid #bdbdbd; L: 1px solid #bdbdbd; radius 8px 8px 0px 0px; background #fafafa `color.neutral.95`; text CohereText 14/21 400, #000000 `color.pureBlack`; placeholder #9ca3af |
| focused | outline 2px solid transparent, offset 2px; child paint input.disabled:text-volcanic-700.[-moz-appearance:_textfield]: outline 2px solid rgba(0, 0, 0, 0) offset 2px |

![Email field default](components/crops/signin-field-default.png) ![Email field focused](components/crops/signin-field-focused.png)

#### Log-in button
The "Log in" submit on the sign-in card; measured never pressed — it would submit the form. Read as `signin-submit` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 130.22 x 40; background transparent; text CohereText 14/21 400, #fafafa `color.neutral.95` |
| hover | child paint span.bg-green-900.h-full: size 12.0x40.0; background #16211c `color.green.900`; radius 6px 0px 0px 6px; div.bg-green-900.text-white: size 40.2x40.0; background #16211c `color.green.900`; span.bg-green-900.h-full: size 39.4x40.0; background #16211c `color.green.900`; radius 0px 10px 4px 0px; span.bg-green-900.h-full: size 39.4x40.0; background #16211c `color.green.900`; radius 4px 0px 0px 10px; div.bg-green-900.text-white: size 32.0x40.0; background #16211c `color.green.900`; span.bg-green-900.h-full: size 12.0x40.0; background #16211c `color.green.900`; radius 0px 6px 6px 0px |
| focus-visible | outline 2px solid transparent, offset 2px; child paint button.mt-10.w-full: size 130.2x40.0; outline 2px solid rgba(0, 0, 0, 0) offset 2px; span.border-volcanic-800.bg-marble-100: size 12.0x52.0; background #fafafa `color.neutral.95`; border 1px solid #424242 `color.volcanic.800`; radius 6px 0px 0px 6px; div.text-volcanic-800.border-volcanic-800: size 122.2x52.0; background #fafafa `color.neutral.95`; border 1px solid #424242 `color.volcanic.800`; span.border-volcanic-800.bg-marble-100: size 12.0x52.0; background #fafafa `color.neutral.95`; border 1px solid #424242 `color.volcanic.800`; radius 0px 6px 6px 0px |

Child layers that carry the look: span 12x40 background #39594d `color.green.700` radius 6px 0px 0px 6px; div 56.2x40 background #39594d `color.green.700`; span 39.4x40 background #39594d `color.green.700` radius 0px 10px 4px 0px.

![Log-in button default](components/crops/signin-submit-default.png) ![Log-in button hover](components/crops/signin-submit-hover.png) ![Log-in button focus-visible](components/crops/signin-submit-focus-visible.png) ![Log-in button pressed](components/crops/signin-submit-pressed.png)

### Footer

The dark footer band: the CTA block, accordion link columns, social icons and the legal/certification row.

#### Footer
The dark footer band (bg near-black): link columns (Platforms/Models/…), social icons and the legal row; the certification strip sits just above it on the home page. Read as `footer` on the home page.

**Values (default).** size 1440 x 1430.39; background transparent; text CohereText 60/60 400, #ffffff `color.pureWhite`.

Child layers that carry the look: section 1440x600 background #355146 `color.green.650`; a 185x53.2 background #ffffff `color.pureWhite` border 2px solid transparent radius 9999px; a::before 181pxx49.2031px image linear-gradient(270deg, #d18ee2 `color.quartz.500`, #ff7759 `color.coral.500`) radius 32px.

![Footer default](components/crops/footer-default.png)

#### Footer link
A link in a footer link column (group/footer-link text-white, inside the lg:flex desktop block; the md:hidden accordion copies measure 0x0). Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 36 x 19.59; background transparent; text Unica77 Cohere Web 14/19.6 400, #fafafa `color.neutral.95` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.group/footer-link.inline-flex: size 36.0x19.6; outline 1px auto rgb(16, 16, 16) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A footer social icon (LinkedIn/X) — the img inside the social anchor. Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 24; background transparent; text Unica77 Cohere Web 16/24 400, #212121 `color.volcanic.900` |

![Social link default](components/crops/footer-social-default.png) ![Social link hover](components/crops/footer-social-hover.png) ![Social link pressed](components/crops/footer-social-pressed.png)

#### Footer CTA
The footer "Request a demo" ease-button-gradient pill; links to the contact form, never followed. Read as `footer-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 185 x 53.2; padding 12px 24px; border 2px solid transparent; radius 9999px; background #ffffff `color.pureWhite`; outline 2px solid transparent, offset 2px; text Unica77 Cohere Web 18/25.2 400, #17171c `color.neutral.15`; transition background-color 0.3s ease, color 0.3s ease |
| focus-visible | shadow #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px; child paint a.relative.flex: shadow rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 2px, rgb(76, 110, 230) 0px 0px 0px 4px, rgb(255, 255, 255) 0px 0px 0px 6px |

![Footer CTA default](components/crops/footer-cta-default.png) ![Footer CTA hover](components/crops/footer-cta-hover.png) ![Footer CTA focus-visible](components/crops/footer-cta-focus-visible.png) ![Footer CTA pressed](components/crops/footer-cta-pressed.png)

#### Trust badge
A certification badge anchor in the compliance strip on the home page (SOC2/GDPR/ISO/CCPA, w-[120px]). Read as `footer-badge` on the home page.

**Values (default).** size 120 x 139.59; background transparent; outline 2px solid transparent, offset 2px; text Unica77 Cohere Web 14/19.6 400, #ffffff `color.pureWhite`.

Child layers that carry the look: a 120x139.6.

![Trust badge default](components/crops/footer-badge-default.png)

### Mobile (390 wide)

The same surface at phone width: the collapsed bar and the open menu overlay.

#### Mobile bar
The 390 mobile nav bar (aria-label="Mobile navigation"): logo + menu toggle; the desktop nav unmounts to 0x0 at this width. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 60; padding 0px 16px; background #ffffff `color.pureWhite`; text Unica77 Cohere Web 16/24 400, #000000 `color.pureBlack`; transition transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), color 0.3s cubic-bezier(0.4, 0, 0.2, 1).

![Mobile bar default](components/crops/m-header-default.png)

#### Menu button
The hamburger (aria-label="Open navigation menu"); its own press opens the drawer. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 32 x 32; background transparent; text Unica77 Cohere Web 16/24 400, #000000 `color.pureBlack`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The menu overlay after the hamburger press (min-h-[100vh] bg-black/20 backdrop-blur scrim + panel). Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 682.59; background #ffffff `color.pureWhite`; text Unica77 Cohere Web 24/28.8 400, #000000 `color.pureBlack`; transition clip-path 0.5s cubic-bezier(0.4, 0, 0.2, 1).

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Menu link
A link/accordion row inside the open mobile menu (min-h-[44px] rows). Read as `m-menu-link` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 358 x 44; background transparent; text Unica77 Cohere Web 24/28.8 400, #000000 `color.pureBlack` |
| focus-visible | outline 1px auto #e59700, offset 0px; child paint button.flex.min-h-[44px]: size 358.0x44.0; outline 1px auto rgb(229, 151, 0) offset 0px |

![Menu link default](components/crops/m-menu-link-default.png) ![Menu link hover](components/crops/m-menu-link-hover.png) ![Menu link focus-visible](components/crops/m-menu-link-focus-visible.png) ![Menu link pressed](components/crops/m-menu-link-pressed.png)

#### Mobile headline
The hero headline at 390. Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 358 x 120; background transparent; text CohereText 60/60 400, #212121 `color.volcanic.900`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Cohere's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The product itself.** Cohere's platform — the dashboard, API keys, usage and billing — lives behind dashboard.cohere.com sign-in; the public login surface was measured but never submitted, and no checkout was ever entered.
- **The app itself is a different surface.** The marketing site is a Next.js/Tailwind + Sanity build; the dashboard UI behind dashboard.cohere.com sign-in is not reachable signed out and is not claimed here. docs.cohere.com (the API docs surface) was not captured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

One theme: the whole public surface paints light. Dark islands exist inside the theme (the pureBlack promo banner, the dark footer band), but no second theme is offered.

### Fonts

- **The UI fonts** are webfonts the site ships (Unica77 Cohere Web, CohereMono and CohereVariable via the .font-* utility stacks; `fonts` in [raw/css-vars.json](raw/css-vars.json) holds the @font-face records); the font files themselves are not committed.
- Illustrations, photography, the hero graphic and the wordmark in the screenshots are Cohere's property; customer logos (Oracle, Dell, RBC and the rest) are their owners' marks.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The hero artwork, illustrations and the Cohere wordmark are Cohere's content; only the frames and components were measured. The customer-logo marquee marks are their owners' artwork.
