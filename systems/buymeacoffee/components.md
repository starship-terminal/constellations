# Buy Me a Coffee components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from buymeacoffee.com on 2026-11-11, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought, supported or submitted; the login card's Email field was focused and filled once with a throwaway address, then cleared — nothing was submitted; the Support and Join actions were measured, never pressed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (62 components, 151 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (144 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every public surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png), [search](screenshots/home-light-search.png) |
| Creator page (Cara) | `/cara.app` | [default](screenshots/creator-light-default.png), [full](screenshots/creator-light-full.png), [menu](screenshots/creator-light-menu.png), [monthly](screenshots/creator-light-monthly.png), [three](screenshots/creator-light-three.png) |
| FAQ | `/faq` | [default](screenshots/faq-light-default.png), [full](screenshots/faq-light-full.png) |
| Wall of Love | `/reviews` | [default](screenshots/reviews-light-default.png), [full](screenshots/reviews-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Brand kit | `/brand` | [default](screenshots/brand-light-default.png), [full](screenshots/brand-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Stream alerts | `/stream-alerts` | [default](screenshots/stream-alerts-light-default.png), [full](screenshots/stream-alerts-light-full.png) |
| Log in | `/login` | [default](screenshots/login-light-default.png) |
| Sign up | `/signup` | [default](screenshots/signup-light-default.png) |
| Terms of use | `/terms` | [default](screenshots/terms-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Creator page, phone | `/cara.app` | [default](screenshots/mobile-creator-light-default.png), [full](screenshots/mobile-creator-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the burger's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-nav-item](#mobile-nav-item) |
| Apps nav dropdown | the marketing header | the Apps trigger's own click | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-dropdown), [menu-link](#menu-link) |
| Search-creators overlay | the marketing header | the fake field's own click | [home-light-search](screenshots/home-light-search.png), [nav-search](#search-field) |
| CookieYes consent banner | the pages it mounts on | hidden, never answered (no consent button was ever clicked) | hidden before every shot and reading |
| Coffee-count pills | the creator page | the 3-coffee radio's own toggle | [creator-light-three](screenshots/creator-light-three.png), [c-qty-on](#quantity-pill-selected) |
| Make-this-monthly checkbox | the creator page | the checkbox's own toggle, ticked then unticked | [creator-light-monthly](screenshots/creator-light-monthly.png), [c-monthly](#monthly-checkbox) |
| More-options menu | the creator page | the ellipsis trigger's own toggle | [creator-light-menu](screenshots/creator-light-menu.png), [c-context](#context-menu) |
| Signed-in product | the creator dashboard | the dashboard, membership/shop/extras managers and payouts live behind /login | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 24 components were given a real keyboard focus. 12 draw an outline ring: `nav-link` (1px auto #005fcc `color.focus.browser`, offset 1px), `menu-link` (1px auto #005fcc `color.focus.browser`, offset 1px), `nav-login` (1px auto #005fcc `color.focus.browser`, offset 1px), `nav-cta` (1px auto #005fcc `color.focus.browser`, offset 1px), `c-more` (1px auto #005fcc `color.focus.browser`, offset 0px), `c-follow` (1px auto #005fcc `color.focus.browser`, offset 0px), `c-share` (1px auto #005fcc `color.focus.browser`, offset 0px), `r-tweet` (1px auto #005fcc `color.focus.browser`, offset 1px), `f-cta` (1px auto #005fcc `color.focus.browser`, offset 1px), `footer-link` (1px auto #005fcc `color.focus.browser`, offset 1px), `footer-social` (1px auto #005fcc `color.focus.browser`, offset 1px), `m-nav-item` (1px auto #e59700, offset 1px). The other 12 show no measured change: `c-tab`, `c-login`, `c-qty-on`, `c-qty-off`, `c-monthly`, `c-private`, `c-support`, `c-join`, `l-cta`, `l-social`, `l-signup-link`, `r-slide`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.075s | `cubic-bezier(0.4, 0, 0.2, 1)` | -webkit-backdrop-filter, backdrop-filter, background-color, border-color, box-shadow, color, fill, filter, opacity, stroke, text-decoration-color, transform | l-email |
| 0.1s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | c-login, c-more |
| 0.1s | `ease-in-out` | all | footer-social |
| 0.1s | `linear` | all | r-tweet |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | l-social |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | c-tab |
| 0.2s | `ease` | all | creator-card |
| 0.25s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | c-amount, c-message, c-name |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | m-menu-open, r-slide |
| 0.8s | `cubic-bezier(0.2, 0.75, 0.28, 0.9)` | all | section-eyebrow, section-h2 |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Creator card](#creator-card) | 199.73 x 180.67 | - | 16px | #ffffff `color.neutral.paper` | rgba(0, 0, 0, 0.15) 0px 0px 2px 0px, rgba(0, 0, 0, 0.04) 0px 8px 40px 0px, rgba(0, 0, 0, 0.05) 0px 2px 5px 0px | 9px 14px |
| [Support widget](#support-widget) | 500 x 507 | - | 24px | #ffffff `color.neutral.paper` | none | 32px 40px |
| [About box](#about-box) | 452 x 321 | B: 1px solid rgba(221, 221, 221, 0.8) | - | transparent | none | 0px 0px 24px 0px |
| [Membership tier](#membership-tier) | 420 x 262 | B: 1px solid rgba(221, 221, 221, 0.8) | - | transparent | none | 0px 0px 12px 0px |
| [Tweet card](#tweet-card) | 371.09 x 306 | - | 24px | #ffffff `color.neutral.paper` | rgba(0, 0, 0, 0.05) 0px 1px 4px 0px | 0 |
| [Nav dropdown](#nav-dropdown) | 150 x 120 | - | 12px | #ffffff `color.neutral.paper` | rgba(0, 0, 0, 0.15) 0px 0px 2px 0px, rgba(0, 0, 0, 0.04) 0px 8px 40px 0px, rgba(0, 0, 0, 0.05) 0px 2px 5px 0px | 12px |
| [Mobile nav item](#mobile-nav-item) | 56.39 x 34 | - | - | transparent | none | 2px 8px |

## Components

### Shell and navigation

The white marketing header: FAQ and Wall-of-love links, the Apps and Resources dropdowns, the wordmark, the Search-creators pill, Log-in and the yellow Sign-up button.

#### Header
The white marketing header: FAQ and Wall-of-love links, the Apps and Resources dropdowns, the wordmark, a fake Search-creators field, Log-in and the yellow Sign-up pill. Read as `header` on the home page.

**Values (default).** size 1440 x 76; padding 14px 24px; background #ffffff `color.neutral.paper`; text Circular Medium 16/24 400, #222222 `color.neutral.ink`; icon 16 x 15, #000000.

![Header default](components/crops/header-default.png)

#### Logo
The coffee-cup + "Buy me a coffee" wordmark anchor in the header centre. Read as `logo` on the home page.

**Values (default).** size 175 x 30; background transparent; text ui-sans-serif 16/24 400, #000000; transform translate(-87.5px, 0px).

![Logo default](components/crops/logo-default.png)

#### Nav link
A plain header link (FAQ); hover paints a 5%-black pill (::before) that scales in. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 64.31 x 40; padding 8px 16px; background transparent; text Circular Medium 16/24 400, #222222 `color.neutral.ink`; layers ::before rgba(0, 0, 0, 0.05) 0px none 0; a::before.text-dark.btn-hover-bg 64.3125pxx40px rgba(0, 0, 0, 0.05) 40px |
| hover | layers ::before rgba(0, 0, 0, 0.05) 0px none 1; a::before.text-dark.btn-hover-bg 64.3125pxx40px rgba(0, 0, 0, 0.05) 40px |
| focus-visible | outline 1px auto #005fcc `color.focus.browser`, offset 1px; layers ::before rgba(0, 0, 0, 0.05) 0px none 0; a.text-dark.btn-hover-bg 64.3x40.0 1px auto rgb(0, 95, 204) offset 1px; a::before.text-dark.btn-hover-bg 64.3125pxx40px rgba(0, 0, 0, 0.05) 40px |
| pressed | layers ::before rgba(0, 0, 0, 0.05) 0px none 1; a::before.text-dark.btn-hover-bg 64.3125pxx40px rgba(0, 0, 0, 0.05) 40px |

Child layers that carry the look: a::before 64.3125pxx40px background rgba(0, 0, 0, 0.05) `color.neutral.hover-fill` radius 40px.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Nav trigger
The Apps label + chevron that opens the header dropdown; toggled by click, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 92.31 x 40; padding 8px 16px; background transparent; text Circular Medium 16/24 400, #000000; icon 20 x 20, #000000; layers ::before rgba(0, 0, 0, 0.05) 0px none 0; div::before.btn-hover-bg.cursor-pointer 92.3125pxx40px rgba(0, 0, 0, 0.05) 40px |
| hover, pressed | layers ::before rgba(0, 0, 0, 0.05) 0px none 1; div::before.btn-hover-bg.cursor-pointer 92.3125pxx40px rgba(0, 0, 0, 0.05) 40px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div::before 92.3125pxx40px background rgba(0, 0, 0, 0.05) `color.neutral.hover-fill` radius 40px.

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav dropdown
The white drop-up-or-down panel the Apps trigger opens (iOS/Android links). Read as `nav-dropdown` on the home page.

**Values (default).** size 150 x 120; padding 12px; radius 12px; background #ffffff `color.neutral.paper`; shadow rgba(0, 0, 0, 0.15) 0px 0px 2px 0px, rgba(0, 0, 0, 0.04) 0px 8px 40px 0px, rgba(0, 0, 0, 0.05) 0px 2px 5px 0px; text Circular Bold 16/24 400, #222222 `color.neutral.ink`; icon 24 x 24, #222222 `color.neutral.ink`.

![Nav dropdown default](components/crops/nav-dropdown-default.png)

#### Menu link
A link inside the opened header dropdown. Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 126 x 48; padding 12px; radius 10px; background transparent; text Circular Bold 16/24 400, #222222 `color.neutral.ink`; icon 24 x 24, #222222 `color.neutral.ink` |
| hover | background rgba(34, 34, 34, 0.05) |
| focus-visible, pressed | background rgba(34, 34, 34, 0.05); outline 1px auto #005fcc `color.focus.browser`, offset 1px |

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link focus-visible](components/crops/menu-link-focus-visible.png) ![Menu link pressed](components/crops/menu-link-pressed.png)

#### Search field
The "Search creators" pill in the header — a fake input that opens a Trending search overlay on click. Read as `nav-search` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 113.09 x 24; background transparent; text Circular Book 16/24 400, rgba(34, 34, 34, 0.7) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Search field default](components/crops/nav-search-default.png) ![Search field hover](components/crops/nav-search-hover.png) ![Search field pressed](components/crops/nav-search-pressed.png)

#### Nav login
The Log-in header link; measured never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 76.81 x 48; padding 8px 16px; background transparent; text Circular Medium 16/24 400, #222222 `color.neutral.ink`; layers ::before rgba(0, 0, 0, 0.05) 0px none 0; a::before.text-dark.btn-hover-bg 76.8125pxx48px rgba(0, 0, 0, 0.05) 40px |
| hover | layers ::before rgba(0, 0, 0, 0.05) 0px none 1; a::before.text-dark.btn-hover-bg 76.8125pxx48px rgba(0, 0, 0, 0.05) 40px |
| focus-visible | outline 1px auto #005fcc `color.focus.browser`, offset 1px; layers ::before rgba(0, 0, 0, 0.05) 0px none 0; a.text-dark.btn-hover-bg 76.8x48.0 1px auto rgb(0, 95, 204) offset 1px; a::before.text-dark.btn-hover-bg 76.8125pxx48px rgba(0, 0, 0, 0.05) 40px |
| pressed | layers ::before rgba(0, 0, 0, 0.05) 0px none 1; a::before.text-dark.btn-hover-bg 76.8125pxx48px rgba(0, 0, 0, 0.05) 40px |

Child layers that carry the look: a::before 76.8125pxx48px background rgba(0, 0, 0, 0.05) `color.neutral.hover-fill` radius 40px.

![Nav login default](components/crops/nav-login-default.png) ![Nav login hover](components/crops/nav-login-hover.png) ![Nav login focus-visible](components/crops/nav-login-focus-visible.png) ![Nav login pressed](components/crops/nav-login-pressed.png)

#### Nav CTA
The yellow Sign-up pill (a.bmc-btn whose ::before paints #fd0, scaling on hover). Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 87.16 x 48; padding 8px 16px; background transparent; text Circular Medium 16/24 400, #222222 `color.neutral.ink`; layers ::before rgb(255, 221, 0) 0px none 1; a::before.xs:hidden.bmc-btn 87.1562pxx48px rgb(255, 221, 0) 40px |
| focus-visible | outline 1px auto #005fcc `color.focus.browser`, offset 1px; layers ::before rgb(255, 221, 0) 0px none 1; a.xs:hidden.bmc-btn 87.2x48.0 1px auto rgb(0, 95, 204) offset 1px; a::before.xs:hidden.bmc-btn 87.1562pxx48px rgb(255, 221, 0) 40px |

Child layers that carry the look: a::before 87.1562pxx48px background #ffdd00 `color.brand.yellow` radius 40px.

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

### Home

The 96px hero over floating creator cards, the yellow Start-my-page pill and the five-star ratings row.

#### Rating row
The five stars + "Loved by 2,000,000+ creators" row over the hero. Read as `rating` on the home page.

**Values (default).** size 384.55 x 27; background transparent; text Circular Regular 18/27 400, #222222 `color.neutral.ink`; icon 24 x 24, #000000.

![Rating row default](components/crops/rating-default.png)

#### Hero headline
The 96px "Fund your creative work" display in Circular Bold. Read as `hero-title` on the home page.

**Values (default).** size 730 x 190; background transparent; text Circular Bold 96/95 400, #222222 `color.neutral.ink`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The 22px tagline under the headline. Read as `hero-sub` on the home page.

**Values (default).** size 600 x 66; background transparent; text Circular Regular 22/33 400, #222222 `color.neutral.ink`; transform translate(0px, -5.6px).

![Hero copy default](components/crops/hero-sub-default.png)

#### Hero CTA
The hero Start-my-page yellow pill (div.btn.header-anim, 74px tall); measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 255.55 x 74; padding 0px 50px; radius 9999px; background transparent; text Circular Bold 24/36 400, #000000; transform translate(0px, -28px); layers div.btn-bg.absolute 255.5x74.0 rgb(255, 221, 0) 9999px |
| hover | transform translate(0px, -23.6px); layers div.btn-bg.absolute 260.9x77.0 rgb(255, 221, 0) 9999px |
| pressed | transform translate(0px, -29.2px); layers div.btn-bg.absolute 260.9x77.0 rgb(255, 221, 0) 9999px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 255.5x74 background #ffdd00 `color.brand.yellow` radius 9999px.

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Creator card
A floating creator card in the hero artwork (white tile, avatar, supporter count). Read as `creator-card` on the home page.

**Values (default).** size 199.73 x 180.67; padding 9px 14px; radius 16px; background #ffffff `color.neutral.paper`; shadow rgba(0, 0, 0, 0.15) 0px 0px 2px 0px, rgba(0, 0, 0, 0.04) 0px 8px 40px 0px, rgba(0, 0, 0, 0.05) 0px 2px 5px 0px; text Circular Book 15/16 400, #222222 `color.neutral.ink`; transition all 0.2s ease; icon 12.54 x 12.54, #000000.

![Creator card default](components/crops/creator-card-default.png)

#### Eyebrow
The 16px section eyebrow (SUPPORT / MEMBERSHIPS / SHOP, CSS-uppercased). Read as `section-eyebrow` on the home page.

**Values (default).** size 936 x 16; background transparent; text Circular Bold 16/16 700, #717171 `color.neutral.grey`; transition all 0.8s cubic-bezier(0.2, 0.75, 0.28, 0.9).

![Eyebrow default](components/crops/section-eyebrow-default.png)

#### Section heading
A 64px section heading in Circular Bold. Read as `section-h2` on the home page.

**Values (default).** size 858 x 160; background transparent; text Circular Bold 64/80 400, #222222 `color.neutral.ink`; transition all 0.8s cubic-bezier(0.2, 0.75, 0.28, 0.9).

![Section heading default](components/crops/section-h2-default.png)

#### Section lede
The 24px Circular Regular lede under a section heading. Read as `section-lede` on the home page.

**Values (default).** size 936 x 64; padding 0px 24px; background transparent; text Circular Regular 24/32 400, #222222 `color.neutral.ink`.

![Section lede default](components/crops/section-lede-default.png)

#### Page field
The #faf8f0 cream wrapper the marketing pages paint on. Read as `page-field` on the home page.

**Values (default).** size 1440 x 5806.41; background #faf8f0 `color.neutral.cream`; text Circular Medium 16/24 400, #222222 `color.neutral.ink`; icon 16 x 15, #000000.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Creator page

The public creator page (/cara.app): sticky profile header with tabs, the About box, the coffee support widget with its quantity pills and fields, membership tiers and the supporters list.

#### Profile header
The sticky creator-page bar: avatar, name, supporter count, the Home/Membership/Wishlist tabs, more-options and Login. Read as `c-header` on the creator page.

**Values (default).** size 1440 x 64; background #ffffff `color.neutral.paper`; shadow rgba(0, 0, 0, 0.06) 0px 1px 1px 0px; text Circular Bold 19/28.5 400, #222222 `color.neutral.ink`; icon 16 x 4, #222222 `color.neutral.ink`.

![Profile header default](components/crops/c-header-default.png)

#### Tab link
A profile tab (Home/Membership/Wishlist); the active tab paints the theme-colour underline (::before). Read as `c-tab` on the creator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 49.34 x 31.5; padding 4px; radius 8px; background transparent; text Circular Medium 15/22.5 400, #ff813f `color.theme.accent`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1); transform translate(0px, 1px); layers ::after rgb(255, 129, 63) 0px none 1; a::after.tw-tab-each.border-before 41.3438pxx1px rgb(255, 129, 63) |

Child layers that carry the look: a::after 41.3438pxx1px background #ff813f `color.theme.accent`.

![Tab link default](components/crops/c-tab-default.png) ![Tab link hover](components/crops/c-tab-hover.png) ![Tab link focus-visible](components/crops/c-tab-focus-visible.png) ![Tab link pressed](components/crops/c-tab-pressed.png)

#### Header login
The Login link at the profile header's right edge; measured never followed. Read as `c-login` on the creator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 37.55 x 22.5; background transparent; text Circular Book 15/22.5 400, #222222 `color.neutral.ink`; transition all 0.1s cubic-bezier(0.4, 0, 0.2, 1); transform translate(0px, 1px) |

![Header login default](components/crops/c-login-default.png) ![Header login hover](components/crops/c-login-hover.png) ![Header login focus-visible](components/crops/c-login-focus-visible.png) ![Header login pressed](components/crops/c-login-pressed.png)

#### More options
The ellipsis trigger (aria-haspopup=menu) that opens the profile context menu. Read as `c-more` on the creator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 32; radius 9999px; background rgba(34, 34, 34, 0.05); text ui-sans-serif 16/24 400, #222222 `color.neutral.ink`; transition all 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 4, #222222 `color.neutral.ink` |
| focus-visible | outline 1px auto #005fcc `color.focus.browser`, offset 0px |
| pressed | background rgba(34, 34, 34, 0.1) |

![More options default](components/crops/c-more-default.png) ![More options hover](components/crops/c-more-hover.png) ![More options focus-visible](components/crops/c-more-focus-visible.png) ![More options pressed](components/crops/c-more-pressed.png)

#### Context menu
The small menu the more-options trigger opens: Follow, Share, Report. Read as `c-context` on the creator page.

**Values (default).** size 198 x 120; padding 6px; background transparent; text Circular Book 15/20 400, #222222 `color.neutral.ink`; icon 20 x 20, #222222 `color.neutral.ink`.

![Context menu default](components/crops/c-context-default.png)

#### About box
The "About Cara" sidebar box (aria region): bio copy, links, icon row. Read as `c-about` on the creator page.

**Values (default).** size 452 x 321; padding 0px 0px 24px 0px; border B: 1px solid rgba(221, 221, 221, 0.8); background transparent; text Circular Medium 16/24 400, #222222 `color.neutral.ink`; icon 20 x 20, #000000; layers div.pb-6.mb-6 452.0x321.0 B:1px solid rgba(221, 221, 221, 0.8).

Child layers that carry the look: div 452x321 border 1px solid rgba(221, 221, 221, 0.8).

![About box default](components/crops/c-about-default.png)

#### Support widget
The "Buy Cara a coffee" card (aria region): quantity pills, custom amount, name field, message, monthly checkbox, the orange Support button. Read as `c-widget` on the creator page.

**Values (default).** size 500 x 507; padding 32px 40px; radius 24px; background #ffffff `color.neutral.paper`; text Circular Bold 24/32 400, #222222 `color.neutral.ink`; icon 16 x 16, #000000.

![Support widget default](components/crops/c-widget-default.png)

#### Quantity pill, selected
The checked coffee-count pill: the theme-colour #FF813F fill with white count. Read as `c-qty-on` on the creator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 48 x 48; border 1px solid rgba(255, 129, 63, 0.25) `color.theme.accent-25`; radius 9999px; background #ff813f `color.theme.accent`; text Circular Bold 19/28.5 400, #ffffff `color.neutral.paper` |
| hover, pressed | border 1px solid #ff813f `color.theme.accent` |

![Quantity pill, selected default](components/crops/c-qty-on-default.png) ![Quantity pill, selected hover](components/crops/c-qty-on-hover.png) ![Quantity pill, selected focus-visible](components/crops/c-qty-on-focus-visible.png) ![Quantity pill, selected pressed](components/crops/c-qty-on-pressed.png)

#### Quantity pill
An unchecked coffee-count pill (white fill, theme-colour count and hairline border). Read as `c-qty-off` on the creator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 48 x 48; border 1px solid rgba(255, 129, 63, 0.25) `color.theme.accent-25`; radius 9999px; background #ffffff `color.neutral.paper`; text Circular Bold 19/28.5 400, #ff813f `color.theme.accent` |
| hover, pressed | border 1px solid #ff813f `color.theme.accent` |

![Quantity pill default](components/crops/c-qty-off-default.png) ![Quantity pill hover](components/crops/c-qty-off-hover.png) ![Quantity pill focus-visible](components/crops/c-qty-off-focus-visible.png) ![Quantity pill pressed](components/crops/c-qty-off-pressed.png)

#### Custom amount
The free-amount field inside the last quantity pill (number input, "20"). Read as `c-amount` on the creator page.

**Values (default).** size 48 x 48; padding 12px 4px; border 1px solid rgba(34, 34, 34, 0.1); radius 12px; background #ffffff `color.neutral.paper`; shadow #ffffff 0px 0px 0px 0px; outline 2px solid transparent, offset 2px; text Circular Medium 19/24 400, #222222 `color.neutral.ink`; transition all 0.25s cubic-bezier(0.4, 0, 0.2, 1); placeholder rgba(34, 34, 34, 0.3).

![Custom amount default](components/crops/c-amount-default.png)

#### Name field
The "Name or @yoursocial" text input in the support widget. Read as `c-name` on the creator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 52; padding 12px; border 2px solid transparent; radius 12px; background #f0f0f0 `color.neutral.field`; shadow #ffffff 0px 0px 0px 0px; outline 2px solid transparent, offset 2px; text Circular Book 17/24 400, #151515 `color.neutral.ink-v2`; transition all 0.25s cubic-bezier(0.4, 0, 0.2, 1); placeholder #6b7280 |
| focused, filled | border 2px solid #ff813f `color.theme.accent`; background #ffffff `color.neutral.paper` |

![Name field default](components/crops/c-name-default.png) ![Name field focused](components/crops/c-name-focused.png) ![Name field filled](components/crops/c-name-filled.png)

#### Message field
The "Say something nice..." textarea (tw-box-common-v2). Read as `c-message` on the creator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 416 x 100; padding 12px; radius 12px; background transparent; shadow #ffffff 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px; outline 2px solid transparent, offset 2px; text Circular Book 17/24 400, #151515 `color.neutral.ink-v2`; transition all 0.25s cubic-bezier(0.4, 0, 0.2, 1); placeholder #6b7280; layers ::before rgba(0, 0, 0, 0) 0px none 1; textarea.tw-box-common-v2.tw-input-common 416.0x100.0 rgb(255, 255, 255) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 12px |
| focused | shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px; layers ::before rgba(0, 0, 0, 0) 0px none 1; textarea.tw-box-common-v2.tw-input-common 416.0x100.0 rgb(255, 255, 255) 0px 0px 0px 0px, rgb(37, 99, 235) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 12px |

![Message field default](components/crops/c-message-default.png) ![Message field focused](components/crops/c-message-focused.png)

#### Monthly checkbox
The "Make this monthly" checkbox label; the visible box is a .tw-checkmark span. Read as `c-monthly` on the creator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 150.34 x 25.5; background transparent; text Circular Regular 15/22.5 400, #222222 `color.neutral.ink`; layers input.tw-checkbox.absolute 150.3x25.5 rgb(255, 255, 255) T:1px solid rgb(107, 114, 128) / R:1px solid rgb(107, 114, 128) / B:1px solid rgb(107, 114, 128) / L:1px solid rgb(107, 114, 128); span.border-dark/50.hover:border-dark/90 20.0x20.0 T:1px solid rgba(34, 34, 34, 0.5) / R:1px solid rgba(34, 34, 34, 0.5) / B:1px solid rgba(34, 34, 34, 0.5) / L:1px solid rgba(34, 34, 34, 0.5) rgb(255, 255, 255)  |
| focus-visible | layers input.tw-checkbox.absolute 150.3x25.5 rgb(255, 255, 255) T:1px solid rgb(107, 114, 128) / R:1px solid rgb(107, 114, 128) / B:1px solid rgb(107, 114, 128) / L:1px solid rgb(107, 114, 128) rgb(255, 255, 255) 0px 0px 0px 2px, rgb(37, 99, 235) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px; span.border-dark/50.hover:border-dark/90 20.0x20.0 T:1px solid rgba(34, 34, 34, 0.5) / R:1px solid rgba(34, 3 |

Child layers that carry the look: input 150.3x25.5 background #ffffff `color.neutral.paper` border 1px solid #6b7280; span 20x20 border 1px solid rgba(34, 34, 34, 0.5) radius 6px shadow #ffffff `color.neutral.paper` 0px 0px 0px 0px, #d1d5db 0px 0px 0px 0px, transparent 0px 0px 0px 0px; span::after 14pxx14px image url(data:…) shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px.

![Monthly checkbox default](components/crops/c-monthly-default.png) ![Monthly checkbox hover](components/crops/c-monthly-hover.png) ![Monthly checkbox focus-visible](components/crops/c-monthly-focus-visible.png) ![Monthly checkbox pressed](components/crops/c-monthly-pressed.png)

#### Private checkbox
The "Make this message private" checkbox label. Read as `c-private` on the creator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 204.59 x 25.5; background transparent; text Circular Regular 15/22.5 400, #222222 `color.neutral.ink`; layers input.tw-checkbox.absolute 204.6x25.5 rgb(255, 255, 255) T:1px solid rgb(107, 114, 128) / R:1px solid rgb(107, 114, 128) / B:1px solid rgb(107, 114, 128) / L:1px solid rgb(107, 114, 128); span.border-dark/50.hover:border-dark/90 20.0x20.0 T:1px solid rgba(34, 34, 34, 0.5) / R:1px solid rgba(34, 34, 34, 0.5) / B:1px solid rgba(34, 34, 34, 0.5) / L:1px solid rgba(34, 34, 34, 0.5) rgb(255, 255, 255)  |
| focus-visible | layers input.tw-checkbox.absolute 204.6x25.5 rgb(255, 255, 255) T:1px solid rgb(107, 114, 128) / R:1px solid rgb(107, 114, 128) / B:1px solid rgb(107, 114, 128) / L:1px solid rgb(107, 114, 128) rgb(255, 255, 255) 0px 0px 0px 2px, rgb(37, 99, 235) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px; span.border-dark/50.hover:border-dark/90 20.0x20.0 T:1px solid rgba(34, 34, 34, 0.5) / R:1px solid rgba(34, 3 |

Child layers that carry the look: input 204.6x25.5 background #ffffff `color.neutral.paper` border 1px solid #6b7280; span 20x20 border 1px solid rgba(34, 34, 34, 0.5) radius 6px shadow #ffffff `color.neutral.paper` 0px 0px 0px 0px, #d1d5db 0px 0px 0px 0px, transparent 0px 0px 0px 0px; span::after 14pxx14px image url(data:…) shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px.

![Private checkbox default](components/crops/c-private-default.png) ![Private checkbox hover](components/crops/c-private-hover.png) ![Private checkbox focus-visible](components/crops/c-private-focus-visible.png) ![Private checkbox pressed](components/crops/c-private-pressed.png)

#### Support button
The orange "Support $5" submit pill: a type=submit button measured in every state, never pressed. Read as `c-support` on the creator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 48; padding 0px 20px; background transparent; text Circular Bold 17/25.5 400, #ffffff `color.neutral.paper`; layers ::before rgb(255, 129, 63) 0px none 1; button::before.tw-btn-bg.relative 420pxx48px rgb(255, 129, 63) 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 rgba(255, 255, 255, 0.537) 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.64) 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.5) 9999px |
| hover | layers ::before rgb(255, 107, 28) 0px none 1; button::before.tw-btn-bg.relative 420pxx48px rgb(255, 107, 28) 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 rgba(255, 255, 255, 0.5) 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.5) 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.7) 9999px |
| focus-visible | outline 2px solid transparent, offset 2px; layers ::before rgb(255, 129, 63) 0px none 1; button.tw-btn-bg.relative 420.0x48.0 2px solid rgba(0, 0, 0, 0) offset 2px; button::before.tw-btn-bg.relative 420pxx48px rgb(255, 129, 63) 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 rgba(255, 255, 255, 0.5) 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.5) 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px r |
| pressed | layers ::before rgb(255, 107, 28) 0px none 1; button::before.tw-btn-bg.relative 420pxx48px rgb(255, 107, 28) 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 rgba(255, 255, 255, 0.92) 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.54) 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.5) 9999px |

Child layers that carry the look: button::before 420pxx48px background #ff813f `color.theme.accent` radius 9999px; span 8x8 background rgba(255, 255, 255, 0.537) radius 9999px; span::before 8pxx8px background rgba(255, 255, 255, 0.64) radius 9999px.

![Support button default](components/crops/c-support-default.png) ![Support button hover](components/crops/c-support-hover.png) ![Support button focus-visible](components/crops/c-support-focus-visible.png) ![Support button pressed](components/crops/c-support-pressed.png)

#### Supporter row
A row in the Recent-supporters list ("SolanaNami bought 2 coffees"), avatar + text + more icon. Read as `c-supporter` on the creator page.

**Values (default).** size 364 x 22.5; background transparent; text Circular Medium 15/22.5 400, #222222 `color.neutral.ink`.

![Supporter row default](components/crops/c-supporter-default.png)

#### Membership tier
A membership-level group in "Become a member": tier name, price, benefits list, Join button. Read as `c-tier` on the creator page.

**Values (default).** size 420 x 262; padding 0px 0px 12px 0px; border B: 1px solid rgba(221, 221, 221, 0.8); background transparent; text Circular Bold 20/28 400, #222222 `color.neutral.ink`; icon 18 x 18, #222222 `color.neutral.ink`; layers div.text-dark.relative 420.0x262.0 B:1px solid rgba(221, 221, 221, 0.8); button::before.tw-btn-bg.relative 420pxx48px rgb(255, 129, 63) 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 rgba(255, 255, 255, 0.5) 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.5) 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.57) 9999px; span.inli.

Child layers that carry the look: div 420x262 border 1px solid rgba(221, 221, 221, 0.8); button::before 420pxx48px background #ff813f `color.theme.accent` radius 9999px; span 8x8 background rgba(255, 255, 255, 0.5) radius 9999px.

![Membership tier default](components/crops/c-tier-default.png)

#### Join button
A membership tier's join action; measured never followed. Read as `c-join` on the creator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 48; padding 0px 32px; background transparent; text Circular Bold 16/24 400, #ffffff `color.neutral.paper`; layers ::before rgb(255, 129, 63) 0px none 1; button::before.tw-btn-bg.relative 420pxx48px rgb(255, 129, 63) 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 rgba(255, 255, 255, 0.576) 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.7) 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.5) 9999px |
| hover | layers ::before rgb(255, 107, 28) 0px none 1; button::before.tw-btn-bg.relative 420pxx48px rgb(255, 107, 28) 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 rgba(255, 255, 255, 0.5) 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.5) 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.78) 9999px |
| focus-visible | outline 2px solid transparent, offset 2px; layers ::before rgb(255, 129, 63) 0px none 1; button.tw-btn-bg.relative 420.0x48.0 2px solid rgba(0, 0, 0, 0) offset 2px; button::before.tw-btn-bg.relative 420pxx48px rgb(255, 129, 63) 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 rgba(255, 255, 255, 0.5) 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.518) 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px |
| pressed | layers ::before rgb(255, 107, 28) 0px none 1; button::before.tw-btn-bg.relative 420pxx48px rgb(255, 107, 28) 9999px; span.dot-flashing.bg-themeTextColor 8.0x8.0 rgba(255, 255, 255, 0.882) 9999px; span::before.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.525) 9999px; span::after.dot-flashing.bg-themeTextColor 8pxx8px rgba(255, 255, 255, 0.5) 9999px |

Child layers that carry the look: button::before 420pxx48px background #ff813f `color.theme.accent` radius 9999px; span 8x8 background rgba(255, 255, 255, 0.576) radius 9999px; span::before 8pxx8px background rgba(255, 255, 255, 0.7) radius 9999px.

![Join button default](components/crops/c-join-default.png) ![Join button hover](components/crops/c-join-hover.png) ![Join button focus-visible](components/crops/c-join-focus-visible.png) ![Join button pressed](components/crops/c-join-pressed.png)

#### Follow item
The Follow row inside the more-options menu (follow-user); measured never toggled — following needs an account. Read as `c-follow` on the creator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 186 x 36; background transparent; text Circular Book 15/20 400, #222222 `color.neutral.ink`; icon 20 x 20, #222222 `color.neutral.ink` |
| hover | layers div.px-3.py-2 186.0x36.0 rgba(34, 34, 34, 0.05) 8px |
| focus-visible, pressed | outline 1px auto #005fcc `color.focus.browser`, offset 0px; layers li.cursor-pointer.select-none 186.0x36.0 1px auto rgb(0, 95, 204) offset 0px; div.px-3.py-2 186.0x36.0 rgba(34, 34, 34, 0.05) 8px |

![Follow item default](components/crops/c-follow-default.png) ![Follow item hover](components/crops/c-follow-hover.png) ![Follow item focus-visible](components/crops/c-follow-focus-visible.png) ![Follow item pressed](components/crops/c-follow-pressed.png)

#### Share item
The Share row inside the more-options menu (px-3 py-2, dark/5 hover fill). Read as `c-share` on the creator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 186 x 36; background transparent; text Circular Book 15/20 400, #222222 `color.neutral.ink`; icon 18 x 18, #222222 `color.neutral.ink` |
| hover | layers div.px-3.py-2 186.0x36.0 rgba(34, 34, 34, 0.05) 8px |
| focus-visible, pressed | outline 1px auto #005fcc `color.focus.browser`, offset 0px; layers li.cursor-pointer 186.0x36.0 1px auto rgb(0, 95, 204) offset 0px; div.px-3.py-2 186.0x36.0 rgba(34, 34, 34, 0.05) 8px |

![Share item default](components/crops/c-share-default.png) ![Share item hover](components/crops/c-share-hover.png) ![Share item focus-visible](components/crops/c-share-focus-visible.png) ![Share item pressed](components/crops/c-share-pressed.png)

#### Page field
The white wrapper a creator page paints on (carries the inline --theme-color* vars). Read as `c-page-field` on the creator page.

**Values (default).** size 1440 x 2356.5; background #ffffff `color.neutral.paper`; text Circular Bold 19/28.5 400, #222222 `color.neutral.ink`; icon 16 x 4, #222222 `color.neutral.ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Login

The centred login card: the Email field, the yellow Continue pill, the social buttons and the signup link; the Password input lives in a second step behind the submit.

#### Login title
The "Welcome back" heading on the centred login card. Read as `l-title` on the login page.

**Values (default).** size 380 x 36; background transparent; text Circular Bold 30/36 400, #000000.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Email field
The Email input on the login card (grey fill, rounded); typed into and cleared, never submitted. Read as `l-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 380 x 48; padding 12px 16px; border 2px solid transparent; radius 12px; background #f0f0f0 `color.neutral.field`; text Circular Medium 16/24 400, #222222 `color.neutral.ink`; transition color 0.075s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), fill 0.075s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.075s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.075s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.075s cubic-bezier(0.4, 0, 0.2, 1), transform 0.075s cubic-bezier(0.4, 0, 0.2, 1), filter 0.075s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.075s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.075s cubic-bezier(0.4, 0, 0.2, 1); placeholder #717171 `color.neutral.grey` |
| focused, filled | border 2px solid #151515 `color.neutral.ink-v2`; background #ffffff `color.neutral.paper`; shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px; outline 2px solid transparent, offset 2px; transition color 0.075s cubic-bezier(0, 0, 0.2, 1), background-color 0.075s cubic-bezier(0, 0, 0.2, 1), border-color 0.075s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.075s cubic-bezier(0, 0, 0.2, 1), fill 0.075s cubic-bezier(0, 0, 0.2, 1), stroke 0.075s cubic-bezier(0, 0, 0.2, 1), opacity 0.075s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.075s cubic-bezier(0, 0, 0.2, 1), transform 0.075s cubic-bezier(0, 0, 0.2, 1), filter 0.075s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.075s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.075s cubic-bezier(0, 0, 0.2, 1) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Continue button
The yellow "Continue with email" pill (tw-btn-bg, theme-colour paint); a submit button measured, never pressed. Read as `l-cta` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 380 x 48; padding 0px 20px; background transparent; text Circular Medium 17/25.5 400, #000000; layers ::before rgb(255, 221, 0) 0px none 1; button::before.tw-btn-bg.relative 380pxx48px rgb(255, 221, 0) 9999px; span.dot-flashing-dark.bg-dark 8.0x8.0 rgb(34, 34, 34) 9999px; span::before.dot-flashing-dark.bg-dark 8pxx8px rgb(34, 34, 34) 9999px; span::after.dot-flashing-dark.bg-dark 8pxx8px rgb(34, 34, 34) 9999px |
| hover | layers ::before rgb(255, 200, 0) 0px none 1; button::before.tw-btn-bg.relative 380pxx48px rgb(255, 200, 0) 9999px; span.dot-flashing-dark.bg-dark 8.0x8.0 rgb(34, 34, 34) 9999px; span::before.dot-flashing-dark.bg-dark 8pxx8px rgb(34, 34, 34) 9999px; span::after.dot-flashing-dark.bg-dark 8pxx8px rgb(34, 34, 34) 9999px |
| focus-visible | outline 2px solid transparent, offset 2px; layers ::before rgb(255, 221, 0) 0px none 1; button.tw-btn-bg.relative 380.0x48.0 2px solid rgba(0, 0, 0, 0) offset 2px; button::before.tw-btn-bg.relative 380pxx48px rgb(255, 221, 0) 9999px; span.dot-flashing-dark.bg-dark 8.0x8.0 rgb(34, 34, 34) 9999px; span::before.dot-flashing-dark.bg-dark 8pxx8px rgb(34, 34, 34) 9999px; span::after.dot-flashing-dark.bg-dark 8pxx8px rgb(34, 34, 34) 9999px |
| pressed | layers ::before rgb(255, 200, 0) 0px none 1; button::before.tw-btn-bg.relative 380pxx48px rgb(255, 200, 0) 9999px; span.dot-flashing-dark.bg-dark 8.0x8.0 rgb(34, 34, 34) 9999px; span::before.dot-flashing-dark.bg-dark 8pxx8px rgb(34, 34, 34) 9999px; span::after.dot-flashing-dark.bg-dark 8pxx8px rgb(34, 34, 34) 9999px |

Child layers that carry the look: button::before 380pxx48px background #ffdd00 `color.brand.yellow` radius 9999px; span 8x8 background #222222 `color.neutral.ink` radius 9999px; span::before 8pxx8px background #222222 `color.neutral.ink` radius 9999px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Social button
A white "Continue with Google" button (greyE5 border, rounded-lg); measured never pressed. Read as `l-social` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 380 x 48; border 1px solid #e5e5e5 `color.neutral.divider`; radius 8px; background #ffffff `color.neutral.paper`; text Circular Book 15/22.5 400, #222222 `color.neutral.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 22 x 22, #222222 `color.neutral.ink` |
| hover | background rgba(34, 34, 34, 0.05) |
| focus-visible | outline 2px solid transparent, offset 2px |
| pressed | background rgba(34, 34, 34, 0.05) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Divider
The "or login with" divider between the email pill and the social buttons. Read as `l-divider` on the login page.

**Values (default).** size 380 x 65; padding 32px 0px; background transparent; text Circular Regular 15/22.5 400, #222222 `color.neutral.ink`; layers span.block.w-full 380.0x1.0 rgb(229, 229, 229); span.bg-white.py-2 114.3x38.5 rgb(255, 255, 255).

Child layers that carry the look: span 380x1 background #e5e5e5 `color.neutral.divider`; span 114.3x38.5 background #ffffff `color.neutral.paper`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Signup link
The "Sign up" link at the card's top right ("Don't have an account?"). Read as `l-signup-link` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 56.64 x 25.5; background transparent; text Circular Regular 17/25.5 400, #000000 |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Reviews

The Wall of Love: tweet-card testimonials and the bordered carousel slide buttons.

#### Wall title
The "Wall of ❤" page title. Read as `r-title` on the reviews page.

**Values (default).** size 239.38 x 96; background transparent; text Borel Regular 64/96 400, #1f2022.

![Wall title default](components/crops/r-title-default.png)

#### Tweet card
A testimonial card on the Wall of Love (white, shadow-sm, slight transform on hover). Read as `r-tweet` on the reviews page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 371.09 x 306; radius 24px; background #ffffff `color.neutral.paper`; shadow rgba(0, 0, 0, 0.05) 0px 1px 4px 0px; text Circular Medium 13/19.5 400, #222222 `color.neutral.ink`; transition all 0.1s linear |
| hover | size 381.55 x 318.76 |
| focus-visible | outline 1px auto #005fcc `color.focus.browser`, offset 1px |
| pressed | size 381.55 x 318.76 |

![Tweet card default](components/crops/r-tweet-default.png) ![Tweet card hover](components/crops/r-tweet-hover.png) ![Tweet card focus-visible](components/crops/r-tweet-focus-visible.png) ![Tweet card pressed](components/crops/r-tweet-pressed.png)

#### Slide button
A carousel "slide next" button: 40px square bordered control, dark fill on hover. Read as `r-slide` on the reviews page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 40 x 40; border 2px solid #000000; radius 9999px; background transparent; text ui-sans-serif 16/24 400, #000000; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 36 x 40, #000000 |
| hover, pressed | background #000000 |

![Slide button default](components/crops/r-slide-default.png) ![Slide button hover](components/crops/r-slide-hover.png) ![Slide button focus-visible](components/crops/r-slide-focus-visible.png) ![Slide button pressed](components/crops/r-slide-pressed.png)

### FAQ

The FAQ page: static question/answer blocks and the bordered Contact-support pills.

#### FAQ title
The "Frequently Asked Questions" heading. Read as `f-h1` on the faq page.

**Values (default).** size 674.17 x 72; background transparent; text Borel Regular 48/72 400, #222222 `color.neutral.ink`.

![FAQ title default](components/crops/f-h1-default.png)

#### FAQ question
A question heading (static, not an accordion). Read as `f-q` on the faq page.

**Values (default).** size 268.42 x 30; padding 0px 12px 0px 0px; background transparent; text Circular Medium 20/30 400, #222222 `color.neutral.ink`.

![FAQ question default](components/crops/f-q-default.png)

#### FAQ answer
An answer paragraph under a question. Read as `f-a` on the faq page.

**Values (default).** size 586 x 97; padding 0px 35px 16px 0px; background transparent; text Circular Regular 18/27 400, #222222 `color.neutral.ink`.

![FAQ answer default](components/crops/f-a-default.png)

#### FAQ CTA
A bordered "Contact support" pill (btn-with-br-2-dark variant); measured never followed. Read as `f-cta` on the faq page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 154.48 x 44; padding 10px 16px; radius 40px; background transparent; text Circular Bold 16/24 400, #222222 `color.neutral.ink`; layers ::before rgba(0, 0, 0, 0) 2px none 1; a::before.bmc-btn.btn-with-br-2-dark 154.484pxx44px T:2px solid rgb(34, 34, 34) / R:2px solid rgb(34, 34, 34) / B:2px solid rgb(34, 34, 34) / L:2px solid rgb(34, 34, 34) 40px |
| focus-visible | outline 1px auto #005fcc `color.focus.browser`, offset 1px; layers ::before rgba(0, 0, 0, 0) 2px none 1; a.bmc-btn.btn-with-br-2-dark 154.5x44.0 1px auto rgb(0, 95, 204) offset 1px 40px; a::before.bmc-btn.btn-with-br-2-dark 154.484pxx44px T:2px solid rgb(34, 34, 34) / R:2px solid rgb(34, 34, 34) / B:2px solid rgb(34, 34, 34) / L:2px solid rgb(34, 34, 34) 40px |

Child layers that carry the look: a::before 154.484pxx44px border 2px solid #222222 `color.neutral.ink` radius 40px.

![FAQ CTA default](components/crops/f-cta-default.png) ![FAQ CTA hover](components/crops/f-cta-hover.png) ![FAQ CTA focus-visible](components/crops/f-cta-focus-visible.png) ![FAQ CTA pressed](components/crops/f-cta-pressed.png)

### Footer

The marketing footer: Apps/Resources/Legal drop-up triggers, link lists, socials and the legal line.

#### Footer
The marketing footer bar (its own Vue component): the Apps/Resources/Legal drop-up triggers, socials and the legal line; the link lists live in the drop-up panels. Read as `footer` on the home page.

**Values (default).** size 1440 x 144; padding 48px 0px 70px 0px; background transparent; text Circular Regular 16/24 400, #717171 `color.neutral.grey`; icon 12 x 9, #222222 `color.neutral.ink`; layers div.hidden.min-w-150 0.0x0.0 rgb(255, 255, 255) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 2.65546px 95px 0px 16px; div.hidden.min-w-[220px] 0.0x0.0 rgb(255, 255, 255) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 2.65546px 95px 0px 16px; div.bg-white.shadow-x-xsm 0.0x0.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.

Child layers that carry the look: div 0x0 background #ffffff `color.neutral.paper` radius 16px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 2.65546px 95px 0px; div 0x0 background #ffffff `color.neutral.paper` radius 16px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 2.65546px 95px 0px; div 0x0 background #ffffff `color.neutral.paper` radius 16px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 2.65546px 95px 0px.

![Footer default](components/crops/footer-default.png)

#### Footer link
A legal link inside the opened footer drop-up panel. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 209.08 x 36; padding 8px 12px; radius 10px; background transparent; text Circular Bold 16/20 400, #222222 `color.neutral.ink` |
| hover | background rgba(34, 34, 34, 0.05) |
| focus-visible, pressed | background rgba(34, 34, 34, 0.05); outline 1px auto #005fcc `color.focus.browser`, offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A social icon link in the footer. Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 26; background transparent; text ui-sans-serif 16/24 400, #000000; transition all 0.1s ease-in-out; icon 24 x 24, #000000 |
| hover | size 26.4 x 28.6; transform scale(1.1); icon 26.4 x 26.4, #000000 |
| focus-visible | outline 1px auto #005fcc `color.focus.browser`, offset 1px; layers a.inline-block.icon-transition 24.0x26.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | size 26.4 x 28.6; transform scale(1.1); icon 26.4 x 26.4, #000000 |

![Social link default](components/crops/footer-social-default.png) ![Social link hover](components/crops/footer-social-hover.png) ![Social link focus-visible](components/crops/footer-social-focus-visible.png) ![Social link pressed](components/crops/footer-social-pressed.png)

#### Footer trigger
The "Legal" drop-up trigger in the footer bar; opens the legal link list. Read as `footer-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 57.83 x 24; background transparent; text Circular Medium 16/24 400, #222222 `color.neutral.ink`; icon 12 x 9, #222222 `color.neutral.ink` |
| hover, pressed | text Circular Medium 16/24 400, #777777; icon 12 x 9, #777777 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Footer trigger default](components/crops/footer-trigger-default.png) ![Footer trigger hover](components/crops/footer-trigger-hover.png) ![Footer trigger pressed](components/crops/footer-trigger-pressed.png)

#### Footer menu
The drop-up panel the Legal trigger opens (Terms of Use, Privacy Policy, Cookie Policy...). Read as `footer-menu` on the home page.

**Values (default).** size 225.08 x 268; padding 8px; radius 16px; background #ffffff `color.neutral.paper`; shadow rgba(0, 0, 0, 0.1) 0px 2.65546px 95px 0px; text Circular Bold 16/20 400, #222222 `color.neutral.ink`.

![Footer menu default](components/crops/footer-menu-default.png)

### Mobile (390 wide)

The marketing surface at phone width: slimmer header, full-screen slide-in menu, smaller display type.

#### Mobile header
The header at 390: wordmark, Log-in link, Start-my-page pill and the burger. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 65; padding 14px 16px; background #ffffff `color.neutral.paper`; text Circular Medium 14/21 400, #222222 `color.neutral.ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Menu button
The burger that slides the full-screen menu in (translate-x-full -> translate-x-0). Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 14 x 12; background transparent; text ui-sans-serif 16/24 400, #000000; icon 14 x 12, #000000.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile menu, open
The full-screen white panel the burger slides in (FAQ, Wall of, iOS, Android, Start my page). Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; padding 16px 12px 72px 12px; background #ffffff `color.neutral.paper`; text Circular Medium 20/30 400, #222222 `color.neutral.ink`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #000000.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile nav item
A link inside the opened mobile menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 56.39 x 34; padding 2px 8px; background transparent; text Circular Medium 20/30 400, #222222 `color.neutral.ink`; layers ::before rgba(0, 0, 0, 0.05) 0px none 0; a::before.text-dark.btn-hover-bg 56.3906pxx34px rgba(0, 0, 0, 0.05) 40px |
| hover | layers ::before rgba(0, 0, 0, 0.05) 0px none 1; a::before.text-dark.btn-hover-bg 56.3906pxx34px rgba(0, 0, 0, 0.05) 40px |
| focus-visible | outline 1px auto #e59700, offset 1px; layers ::before rgba(0, 0, 0, 0.05) 0px none 0; a.text-dark.btn-hover-bg 56.4x34.0 1px auto rgb(229, 151, 0) offset 1px; a::before.text-dark.btn-hover-bg 56.3906pxx34px rgba(0, 0, 0, 0.05) 40px |
| pressed | layers ::before rgba(0, 0, 0, 0.05) 0px none 1; a::before.text-dark.btn-hover-bg 56.3906pxx34px rgba(0, 0, 0, 0.05) 40px |

Child layers that carry the look: a::before 56.3906pxx34px background rgba(0, 0, 0, 0.05) `color.neutral.hover-fill` radius 40px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile headline
The hero display at 390. Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 326 x 110; background transparent; text Circular Bold 48/55 400, #222222 `color.neutral.ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the coffee-cup wordmark, heart and chevron glyphs, social icons, the payment brand marks) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The Buy Me a Coffee dashboard lives behind /login — the signed-in creator's page editor, membership and shop managers, extras, payouts, analytics and settings all need an account and were never reached. The public creator page (/cara.app) is a real product surface — the support widget, tabs and tier cards are the shipped components — but the payment checkout behind its Support button is Stripe's, and was never opened.

### Pages

- **The dashboard.** Every post-login surface was never reached; /login and /signup were captured as cards and never submitted.
- **Payment.** The Support and Join buttons are submits — measured in every state, never pressed. The Stripe checkout behind them was never opened.
- **Signup and start-my-page flows.** Every Sign-up, Start-my-page and login action was measured, never followed.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface (the login card's validation never ran — nothing was submitted).
- **The search overlay** was captured open ([home-light-search](screenshots/home-light-search.png)); its results were never typed for.
- **Membership tier join flow** stays at the tier card: the Join actions were measured, never followed.

### Themes

Every public surface paints light-only; no dark mode is offered. The one theme mechanism is per-creator: a creator page declares --theme-color* custom properties inline (orange #ff813f on /cara.app) and the widget, tabs and buttons repaint to match. tokens.json keeps that accent set under color.theme.*.

### Fonts

- **Circular** (Regular, Book, Medium, Bold, Black) runs both public frontends; **Borel Regular** is the display accent (the Wall-of-love heart script). They are served from buymeacoffee.com/_nuxt and cdn.buymeacoffee.com; the style guide falls back to system sans.

### Screenshots

- The creator avatars and names, cover artwork, supporter names, tweets, blog thumbnails and any photography in the screenshots are published content (creators' public pages and testimonials).
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Blog articles, creator page copy, tweets and docs text are the product's published content; only frames and components were measured.
