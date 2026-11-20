# Epidemic Sound components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from epidemicsound.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought, downloaded or submitted; the login and signup forms were never sent; the plan, trial and playback actions were never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (56 components, 147 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (145 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: the marketing pages paint `light` (ecru), the catalog and account surfaces paint `dark`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home (ecru) | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Pricing (ecru) | `/pricing/` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Music landing (ecru) | `/music/` | [default](screenshots/music-light-default.png), [full](screenshots/music-light-full.png) |
| Sound effects landing (ecru) | `/sound-effects/` | [default](screenshots/soundfx-light-default.png), [full](screenshots/soundfx-light-full.png) |
| How it works (ecru) | `/how-it-works/` | [default](screenshots/how-light-default.png), [full](screenshots/how-light-full.png) |
| Genre catalog (dark) | `/music/genres/pop/` | [default](screenshots/genre-dark-default.png), [full](screenshots/genre-dark-full.png) |
| Artist catalog (dark) | `/artists/ooyy/` | [default](screenshots/artist-dark-default.png), [full](screenshots/artist-dark-full.png) |
| Theme catalog (dark) | `/music/themes/vlogs/lifestyle-vlog/` | [default](screenshots/theme-dark-default.png), [full](screenshots/theme-dark-full.png) |
| SFX category (dark) | `/sound-effects/categories/ambience/` | [default](screenshots/sfxcat-dark-default.png), [full](screenshots/sfxcat-dark-full.png) |
| Log in (Keycloak) | `login.epidemicsound.com` | [default](screenshots/login-dark-default.png) |
| Sign up (Keycloak) | `login.epidemicsound.com` | [default](screenshots/signup-dark-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Genre, phone | `/music/genres/pop/` | [default](screenshots/mobile-genre-dark-default.png), [drawer](screenshots/mobile-genre-dark-drawer.png), [full](screenshots/mobile-genre-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent card | every page | hidden, never answered (no consent button was ever clicked) | hidden before every shot and reading |
| Header mega menu | / | the 'Music' trigger's own disclosure | [nav-menu](#mega-menu), [nav-menu-item](#mega-menu-item) |
| Billing-period switch | /pricing/ | the Monthly/Yearly switch's own toggle | [billing-switch](#billing-switch) |
| FAQ accordion | /music/genres/pop/ | the heading's own disclosure | [faq-row](#faq-accordion-row) |
| Mobile nav overlay | genre page, phone width | the hamburger's own toggle | [mobile-genre-dark-drawer](screenshots/mobile-genre-dark-drawer.png), [m-hamburger](#mobile-hamburger) |
| Signed-in product | an Epidemic Sound account | every post-login surface needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 25 components were given a real keyboard focus. 25 draw an outline ring: `nav-trigger` (2px solid #000000 `color.brand.black`, offset 2px), `nav-pricing` (2px solid #000000 `color.brand.black`, offset 2px), `btn-login` (2px solid #000000 `color.brand.black`, offset 2px), `btn-signup` (2px solid #000000 `color.brand.black`, offset 2px), `hero-cta` (2px solid #000000 `color.brand.black`, offset 2px), `billing-switch` (2px solid #000000 `color.brand.black`, offset 2px), `plan-cta` (2px solid #000000 `color.brand.black`, offset 2px), `c-signup` (2px solid #20afff `color.background.beta`, offset 2px), `track-play` (1px auto #101010, offset 0px), `track-like` (2px solid #20afff `color.background.beta`, offset 2px), `track-similar` (2px solid #20afff `color.background.beta`, offset 2px), `track-add` (2px solid #20afff `color.background.beta`, offset 2px), `track-download` (2px solid #20afff `color.background.beta`, offset 2px), `wantmore-cta` (2px solid #20afff `color.background.beta`, offset 2px), `social-icon` (2px solid #20afff `color.background.beta`, offset 2px), `sfx-play` (1px auto #101010, offset 0px), `sfx-category-card` (1px auto #101010, offset 1px), `kc-social-google` (2px solid #ffffff `color.brand.white`, offset 2px), `kc-show-pass` (1px auto #101010, offset 0px), `kc-submit` (2px solid #ffffff `color.brand.white`, offset 2px), `kc-signup-link` (1px auto #101010, offset 1px), `kc-forgot` (1px auto #101010, offset 1px), `su-submit` (2px solid #ffffff `color.brand.white`, offset 2px), `m-hamburger` (2px solid #20afff `color.background.beta`, offset 2px), `m-cta` (2px solid #20afff `color.background.beta`, offset 2px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease` | background-color | kc-show-pass |
| 0.125s | `ease-in-out` | background-color | billing-switch |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | m-nav-item, nav-menu-item, nav-pricing, nav-trigger |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Genre banner](#genre-banner) | 1328 x 204 | - | 16px 16px 0px 0px | #ff82c2 `color.action.accent.default` | none | 0 |
| [Want-more banner](#want-more-banner) | 1328 x 244 | - | - | transparent | none | 0 |
| [Login card](#login-card) | 416 x 882.81 | - | - | transparent | none | 0 |
| [Mega menu](#mega-menu) | 1359 x 331 | - | 16px | #ffffff `color.brand.white` | rgba(0, 0, 0, 0.16) 0px 4px 24px 0px | 24px 24px 40px 24px |
| [Site header](#site-header) | 1440 x 100 | - | - | transparent | none | 0 |
| [Mobile header](#mobile-header) | 390 x 100 | - | - | transparent | none | 0 |

## Components

### App shell and navigation

The sticky 100px header both themes share: the ES logotype, the mega-menu triggers (Music / Sound effects / Tools / License / Resources / For business), Pricing, the secondary Log-in pill and the primary Create-free-account pill — black-filled on ecru, white-filled on dark.

#### Site header
The sticky top bar: ES logotype, mega-menu triggers (Music / Sound effects / Tools / License / Resources / For business), Pricing, Log in and Create free account. Read as `header` on the home page.

**Values (default).** size 1440 x 100; background transparent; text Inter 14/24 600, #000000 `color.brand.black`; icon 20 x 24, #0000ee; layers div.relative.mx-auto 1359.0x68.0 rgb(255, 255, 255) 10000px; button.no-default-focus.focus-visible 76.0x44.0 rgba(61, 77, 116, 0) 10000px; div.flex.w-full 0.0x0.0 rgb(255, 255, 255) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.16) 0px 4px 24px 0px 16px; span.flex.size-10 0.0x0.0 rgba(61, 77, .

Child layers that carry the look: div 1359x68 background #ffffff `color.brand.white` radius 10000px; button 76x44 background rgba(61, 77, 116, 0) `color.action.ghost.default` radius 10000px; div 0x0 background #ffffff `color.brand.white` radius 16px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.16) 0px 4px 24px 0px.

![Site header default](components/crops/header-default.png)

#### Logo
The Epidemic Sound glyph + wordmark link. Read as `logo` on the home page.

**Values (default).** size 40 x 44; radius 4px; background transparent; text Inter 16/16 400, #0000ee; icon 20 x 24, #0000ee.

![Logo default](components/crops/logo-default.png)

#### Nav menu trigger
The "Music" ghost button that opens the mega menu — a local disclosure; the opened state was measured after clicking it, its links never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 76 x 44; padding 4px 16px; radius 10000px; background rgba(61, 77, 116, 0) `color.action.ghost.default`; text Inter 14/24 600, #000000 `color.brand.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(61, 77, 116, 0.06) `color.action.accent.disabled` |
| focus-visible | outline 2px solid #000000 `color.brand.black`, offset 2px |
| pressed | background rgba(61, 77, 116, 0.12) `color.action.ghost.pressed` |
| opened | background rgba(61, 77, 116, 0.06) `color.action.accent.disabled` |

![Nav menu trigger default](components/crops/nav-trigger-default.png) ![Nav menu trigger hover](components/crops/nav-trigger-hover.png) ![Nav menu trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav menu trigger pressed](components/crops/nav-trigger-pressed.png) ![Nav menu trigger opened](components/crops/nav-trigger-opened.png)

#### Mega menu
The dropdown opened by the "Music" trigger; its links were never followed. Read as `nav-menu` on the home page.

**Values (default).** size 1359 x 331; padding 24px 24px 40px 24px; radius 16px; background #ffffff `color.brand.white`; shadow rgba(0, 0, 0, 0.16) 0px 4px 24px 0px; text Inter 10/11 600, rgba(0, 0, 0, 0.6) `color.icon.secondary`; icon 16 x 16, #000000 `color.brand.black`.

![Mega menu default](components/crops/nav-menu-default.png)

#### Mega menu item
A genre link inside the opened mega menu; measured, never followed. Read as `nav-menu-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 356 x 56; padding 8px; radius 4px; background transparent; text Inter 14/24 600, #000000 `color.brand.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #000000 `color.brand.black`; layers span.flex.size-10 40.0x40.0 rgba(61, 77, 116, 0.12) 4px |
| hover | background rgba(61, 77, 116, 0.06) `color.action.accent.disabled`; layers none |

Child layers that carry the look: span 40x40 background rgba(61, 77, 116, 0.12) `color.action.ghost.pressed` radius 4px.

![Mega menu item default](components/crops/nav-menu-item-default.png) ![Mega menu item hover](components/crops/nav-menu-item-hover.png)

#### Pricing link
The header Pricing link; measured, never followed. Read as `nav-pricing` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 109 x 44; padding 0px 16px; radius 10000px; background transparent; text Inter 14/24 600, #000000 `color.brand.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #000000 `color.brand.black` |
| focus-visible | outline 2px solid #000000 `color.brand.black`, offset 2px; layers a.group/pricing.flex 109.0x44.0 2px solid rgb(0, 0, 0) offset 2px 10000px |
| pressed | background rgba(61, 77, 116, 0.06) `color.action.accent.disabled` |

![Pricing link default](components/crops/nav-pricing-default.png) ![Pricing link hover](components/crops/nav-pricing-hover.png) ![Pricing link focus-visible](components/crops/nav-pricing-focus-visible.png) ![Pricing link pressed](components/crops/nav-pricing-pressed.png)

#### Log in button
The secondary "Log in" button; links to login.epidemicsound.com, measured never followed. The header ships a hidden twin of the same link before the painted one, so the visible copy is the last match. Read as `btn-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 76 x 44; padding 4px 16px; radius 10000px; background rgba(61, 77, 116, 0.12) `color.action.ghost.pressed`; text Inter 14/24 600, #000000 `color.brand.black` |
| hover | background rgba(61, 77, 116, 0.18) `color.action.secondary.hovered` |
| focus-visible | outline 2px solid #000000 `color.brand.black`, offset 2px |
| pressed | background rgba(61, 77, 116, 0.24) `color.action.secondary.pressed` |

![Log in button default](components/crops/btn-login-default.png) ![Log in button hover](components/crops/btn-login-hover.png) ![Log in button focus-visible](components/crops/btn-login-focus-visible.png) ![Log in button pressed](components/crops/btn-login-pressed.png)

#### Create account button
The primary "Create free account" button — black fill on the light marketing theme; measured never followed. Read as `btn-signup` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 173 x 44; padding 4px 16px; radius 10000px; background #000000 `color.brand.black`; text Inter 14/24 600, #ffffff `color.brand.white` |
| hover | background #272727 `color.action.primary.hovered` |
| focus-visible | outline 2px solid #000000 `color.brand.black`, offset 2px |
| pressed | background #333333 `color.action.primary.pressed` |

![Create account button default](components/crops/btn-signup-default.png) ![Create account button hover](components/crops/btn-signup-hover.png) ![Create account button focus-visible](components/crops/btn-signup-focus-visible.png) ![Create account button pressed](components/crops/btn-signup-pressed.png)

#### Header (dark)
The sticky header on the dark catalog theme (header.sticky.top-0); primary button reads white here. Read as `c-header` on the genre page.

**Values (default).** size 1440 x 100; background transparent; text Inter 14/24 600, #ffffff `color.brand.white`; icon 20 x 24, #9e9eff; layers div.relative.mx-auto 1359.0x68.0 rgb(41, 44, 51) 10000px; button.no-default-focus.focus-visible 76.0x44.0 rgba(207, 214, 229, 0) 10000px; div.flex.w-full 0.0x0.0 rgb(41, 44, 51) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.16) 0px 4px 24px 0px 16px; span.flex.size-10 0.0x0.0 rgba(207, 214, 22.

Child layers that carry the look: div 1359x68 background #292c33 `color.background.brand.off.black` radius 10000px; button 76x44 background rgba(207, 214, 229, 0) `color.action.ghost.default` radius 10000px; div 0x0 background #292c33 `color.background.brand.off.black` radius 16px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.16) 0px 4px 24px 0px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Create account button (dark)
The primary button on the dark theme — white fill, black text; measured never followed. Scoped to the sticky header so a lower banner of the same label cannot match. Read as `c-signup` on the genre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 173 x 44; padding 4px 16px; radius 10000px; background #ffffff `color.brand.white`; text Inter 14/24 600, #000000 `color.brand.black` |
| hover | background #e7e7e7 `color.action.primary.hovered` |
| focus-visible | outline 2px solid #20afff `color.background.beta`, offset 2px |
| pressed | background #cfcfcf `color.action.primary.pressed` |

![Create account button (dark) default](components/crops/c-signup-default.png) ![Create account button (dark) hover](components/crops/c-signup-hover.png) ![Create account button (dark) focus-visible](components/crops/c-signup-focus-visible.png) ![Create account button (dark) pressed](components/crops/c-signup-pressed.png)

### Home (alternative-light marketing)

The ecru home hero: the Sebenta display headline, the primary CTA and the section headings.

#### Hero headline
The home hero display heading (es-heading class). Read as `hero-h1` on the home page.

**Values (default).** size 1104 x 160; background transparent; text Sebenta 80/80 500, #000000 `color.brand.black`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero CTA
The primary call-to-action inside the hero; measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 213 x 56; padding 9.6px 24px; radius 10000px; background #000000 `color.brand.black`; text Inter 16/24 600, #ffffff `color.brand.white` |
| hover | background #272727 `color.action.primary.hovered` |
| focus-visible | outline 2px solid #000000 `color.brand.black`, offset 2px |
| pressed | background #333333 `color.action.primary.pressed` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Section heading
A marketing section heading further down the home page. Read as `section-h2` on the home page.

**Values (default).** size 472 x 96; background transparent; text Sebenta 40/48 500, #000000 `color.brand.black`.

![Section heading default](components/crops/section-h2-default.png)

### Pricing (alternative-light)

The ecru pricing surface: 'Our subscriptions', the Monthly/Yearly switch, the Creator/Pro/Pro-Plus plan columns with Get-30-days-free actions, Compare plans and the FAQ.

#### Pricing headline
"Our subscriptions" — the es-heading-xl display heading over the plan columns. Read as `pr-h1` on the pricing page.

**Values (default).** size 1328 x 68; background transparent; text Sebenta 64/68 500, #000000 `color.brand.black`.

![Pricing headline default](components/crops/pr-h1-default.png)

#### Billing switch
The Monthly/Yearly billing switch above the plans — a local toggle; the opened state is the toggled position after clicking it, never checked out. Read as `billing-switch` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 24; radius 1000px; background #000000 `color.brand.black`; text Inter 16/18.4 400, #000000 `color.brand.black`; transition background-color 0.125s ease-in-out; placeholder #000000 `color.brand.black`; layers ::after rgb(255, 255, 255) 0px none 1 |
| hover | background #272727 `color.action.primary.hovered` |
| focus-visible | outline 2px solid #000000 `color.brand.black`, offset 2px |
| pressed | background #333333 `color.action.primary.pressed` |
| opened | background rgba(61, 77, 116, 0.12) `color.action.ghost.pressed` |

![Billing switch default](components/crops/billing-switch-default.png) ![Billing switch hover](components/crops/billing-switch-hover.png) ![Billing switch focus-visible](components/crops/billing-switch-focus-visible.png) ![Billing switch pressed](components/crops/billing-switch-pressed.png) ![Billing switch opened](components/crops/billing-switch-opened.png)

#### Plan name
The "Creator" plan heading (es-subheading-l) over a plan column. Read as `plan-name` on the pricing page.

**Values (default).** size 368 x 24; background transparent; text Inter 20/24 500, #000000 `color.brand.black`.

![Plan name default](components/crops/plan-name-default.png)

#### Plan price line
The price line inside a plan column. Read as `plan-price` on the pricing page.

**Wrong element.** These readings are an empty 688 x 384 div far down the pricing page (y 6525), not a plan's price line: the `main, section, div` union with `.last()` matched it. Recapture needed.

**Values (default).** size 688 x 384; padding 24px; background transparent; text Inter 16/24 500, rgba(0, 0, 0, 0.6) `color.icon.secondary`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Plan CTA
The primary "Get 30 days free" button inside a plan column — starts a trial; measured never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 56; padding 9.6px 24px; radius 10000px; background #000000 `color.brand.black`; text Inter 16/24 600, #ffffff `color.brand.white` |
| hover | background #272727 `color.action.primary.hovered` |
| focus-visible | outline 2px solid #000000 `color.brand.black`, offset 2px |
| pressed | background #333333 `color.action.primary.pressed` |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Compare plans heading
The "Compare plans" heading over the feature matrix; a hidden copy precedes it in the DOM, so the painted one is the last match. Read as `compare-h2` on the pricing page.

**Values (default).** size 490.8 x 64; padding 0px 0px 16px 0px; background transparent; text Sebenta 40/48 500, #000000 `color.brand.black`.

![Compare plans heading default](components/crops/compare-h2-default.png)

### Genre page (dark catalog)

The dark catalog genre page: breadcrumbs, the pink genre banner with the 40px heading, the 56px track rows with their album-cover play buttons and row actions, the FAQ accordion.

#### Breadcrumbs
The MUSIC / GENRES / POP breadcrumb row over the genre banner. Read as `breadcrumbs` on the genre page.

**Values (default).** size 46 x 16; background transparent; text Inter 12/16 500, rgba(255, 255, 255, 0.72) `color.icon.secondary`.

![Breadcrumbs default](components/crops/breadcrumbs-default.png)

#### Genre banner
The coloured genre header card (#ff82c2 pink for pop) holding the GENRE kicker and the h1; the _genre_ module class is what paints the colour. Read as `genre-banner` on the genre page.

**Values (default).** size 1328 x 204; radius 16px 16px 0px 0px; background #ff82c2 `color.action.accent.default`; text Inter 12/16 500, #000000 `color.brand.black`.

![Genre banner default](components/crops/genre-banner-default.png)

#### Genre heading
"Pop music" — es-heading-m, black on the pink banner. Read as `genre-h1` on the genre page.

**Values (default).** size 204.2 x 48; background transparent; text Sebenta 40/48 500, #000000 `color.brand.black`.

![Genre heading default](components/crops/genre-h1-default.png)

#### Track list
The genre page track list (ul.TrackList); rows virtualise as it scrolls. Read as `track-list` on the genre page.

**Values (default).** size 1328 x 704; background transparent; text Inter 14/24 600, #ffffff `color.brand.white`; layers button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 56.0x56.0 rgb(107, 107, 107) 4px; button.TrackRowPlayButton_albumCover__Pv48J.rounded-(--es-radius-detail) 0.0x0.0 rgba(207, 214, 229, 0.16) 4px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 rgba(207, 214, 229, 0) 10000px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 rgba(207, 214, 229, 0) 10000px; button.focus-visible._iconBu.

Child layers that carry the look: button 56x56 background #6b6b6b radius 4px; button 0x0 background rgba(207, 214, 229, 0.16) `color.action.accent.disabled` radius 4px; button 44x44 background rgba(207, 214, 229, 0) `color.action.ghost.default` radius 10000px.

![Track list default](components/crops/track-list-default.png)

#### Track row
A 56px track row: album-cover play button, title, artist, duration, BPM, genre/mood tags; hover reveals row actions. Read as `track-row` on the genre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1328 x 56; padding 0px 8px 0px 0px; radius 8px; background transparent; text Inter 14/24 600, #ffffff `color.brand.white`; layers button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 56.0x56.0 rgb(107, 107, 107) 4px; button.TrackRowPlayButton_albumCover__Pv48J.rounded-(--es-radius-detail) 0.0x0.0 rgba(207, 214, 229, 0.16) 4px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 rgba(207, 214, 229, 0) 10000px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 rgba(207, 214, 229, 0) 10000px; button.focus-visible._iconBu |
| hover | background rgba(207, 214, 229, 0.08) `color.action.ghost.hovered`; icon 24 x 24, #ffffff `color.brand.white`; layers none |

Child layers that carry the look: button 56x56 background #6b6b6b radius 4px; button 0x0 background rgba(207, 214, 229, 0.16) `color.action.accent.disabled` radius 4px; button 44x44 background rgba(207, 214, 229, 0) `color.action.ghost.default` radius 10000px.

![Track row default](components/crops/track-row-default.png) ![Track row hover](components/crops/track-row-hover.png)

#### Track play button
A row's album-cover play button; measured, never pressed (signed-out playback is gated anyway). On row hover the cover button is swapped out of the layout entirely — its hover-state box is a real 0x0, not a missed selector. Read as `track-play` on the genre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 56 x 56; radius 4px; background #6b6b6b; text Inter 16/18.4 400, #ffffff `color.brand.white` |
| focus-visible | outline 1px auto #101010, offset 0px |

**Not a reading.** In `hover` this element's box is 0 x 0 (it leaves the layout), so that state's look is on its container, not measured here.

![Track play button default](components/crops/track-play-default.png) ![Track play button focus-visible](components/crops/track-play-focus-visible.png) ![Track play button pressed](components/crops/track-play-pressed.png)

#### Like button
A row's heart icon button; measured, never toggled (needs an account). Read as `track-like` on the genre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; radius 10000px; background rgba(207, 214, 229, 0) `color.action.ghost.default`; text Inter 16/18.4 400, rgba(255, 255, 255, 0.72) `color.icon.secondary`; icon 20 x 20, rgba(255, 255, 255, 0.72) `color.icon.secondary` |
| hover | background rgba(207, 214, 229, 0.08) `color.action.ghost.hovered`; text Inter 16/18.4 400, #ffffff `color.brand.white`; icon 20 x 20, #ffffff `color.brand.white` |
| focus-visible | background rgba(207, 214, 229, 0.08) `color.action.ghost.hovered`; outline 2px solid #20afff `color.background.beta`, offset 2px |
| pressed | background rgba(207, 214, 229, 0.16) `color.action.accent.disabled`; text Inter 16/18.4 400, #ffffff `color.brand.white`; icon 20 x 20, #ffffff `color.brand.white` |

![Like button default](components/crops/track-like-default.png) ![Like button hover](components/crops/track-like-hover.png) ![Like button focus-visible](components/crops/track-like-focus-visible.png) ![Like button pressed](components/crops/track-like-pressed.png)

#### Find similar button
A row's Find-similar icon button; measured, never followed. Read as `track-similar` on the genre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; radius 10000px; background rgba(207, 214, 229, 0) `color.action.ghost.default`; text Inter 16/18.4 400, rgba(255, 255, 255, 0.72) `color.icon.secondary`; icon 20 x 20, rgba(255, 255, 255, 0.72) `color.icon.secondary` |
| hover | background rgba(207, 214, 229, 0.08) `color.action.ghost.hovered`; text Inter 16/18.4 400, #ffffff `color.brand.white`; icon 20 x 20, #ffffff `color.brand.white` |
| focus-visible | background rgba(207, 214, 229, 0.08) `color.action.ghost.hovered`; outline 2px solid #20afff `color.background.beta`, offset 2px |
| pressed | background rgba(207, 214, 229, 0.16) `color.action.accent.disabled`; text Inter 16/18.4 400, #ffffff `color.brand.white`; icon 20 x 20, #ffffff `color.brand.white` |

![Find similar button default](components/crops/track-similar-default.png) ![Find similar button hover](components/crops/track-similar-hover.png) ![Find similar button focus-visible](components/crops/track-similar-focus-visible.png) ![Find similar button pressed](components/crops/track-similar-pressed.png)

#### Add to playlist button
A row's Add-to-playlist icon button; measured, never toggled (needs an account). Read as `track-add` on the genre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; radius 10000px; background rgba(207, 214, 229, 0) `color.action.ghost.default`; text Inter 16/18.4 400, rgba(255, 255, 255, 0.72) `color.icon.secondary`; icon 20 x 20, rgba(255, 255, 255, 0.72) `color.icon.secondary` |
| hover | background rgba(207, 214, 229, 0.08) `color.action.ghost.hovered`; text Inter 16/18.4 400, #ffffff `color.brand.white`; icon 20 x 20, #ffffff `color.brand.white` |
| focus-visible | background rgba(207, 214, 229, 0.08) `color.action.ghost.hovered`; outline 2px solid #20afff `color.background.beta`, offset 2px |
| pressed | background rgba(207, 214, 229, 0.16) `color.action.accent.disabled`; text Inter 16/18.4 400, #ffffff `color.brand.white`; icon 20 x 20, #ffffff `color.brand.white` |

![Add to playlist button default](components/crops/track-add-default.png) ![Add to playlist button hover](components/crops/track-add-hover.png) ![Add to playlist button focus-visible](components/crops/track-add-focus-visible.png) ![Add to playlist button pressed](components/crops/track-add-pressed.png)

#### Download button
A row's Download icon button; measured, never pressed (licensed download). Read as `track-download` on the genre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; radius 10000px; background rgba(207, 214, 229, 0) `color.action.ghost.default`; text Inter 16/18.4 400, rgba(255, 255, 255, 0.72) `color.icon.secondary`; icon 20 x 20, rgba(255, 255, 255, 0.72) `color.icon.secondary` |
| hover | background rgba(207, 214, 229, 0.08) `color.action.ghost.hovered`; text Inter 16/18.4 400, #ffffff `color.brand.white`; icon 20 x 20, #ffffff `color.brand.white` |
| focus-visible | background rgba(207, 214, 229, 0.08) `color.action.ghost.hovered`; outline 2px solid #20afff `color.background.beta`, offset 2px |
| pressed | background rgba(207, 214, 229, 0.16) `color.action.accent.disabled`; text Inter 16/18.4 400, #ffffff `color.brand.white`; icon 20 x 20, #ffffff `color.brand.white` |

![Download button default](components/crops/track-download-default.png) ![Download button hover](components/crops/track-download-hover.png) ![Download button focus-visible](components/crops/track-download-focus-visible.png) ![Download button pressed](components/crops/track-download-pressed.png)

#### FAQ accordion row
An FAQ accordion heading at the bottom of the catalog page — a local disclosure; the opened state was measured after clicking it. Read as `faq-row` on the genre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 289 x 24; background transparent; text Inter 16/24 600, #ffffff `color.brand.white` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![FAQ accordion row default](components/crops/faq-row-default.png) ![FAQ accordion row hover](components/crops/faq-row-hover.png) ![FAQ accordion row pressed](components/crops/faq-row-pressed.png) ![FAQ accordion row opened](components/crops/faq-row-opened.png)

### Sound-effects category (dark catalog)

The dark SFX category page: heading, category links and SFX track rows.

#### SFX category heading
The sound-effects category page heading on the dark theme. Read as `sfx-h1` on the sound-effects category page.

**Values (default).** size 624.61 x 48; background transparent; text Sebenta 40/48 500, #000000 `color.brand.black`.

![SFX category heading default](components/crops/sfx-h1-default.png)

#### SFX track row
An SFX track row (name, category tags, duration). Read as `sfx-row` on the sound-effects category page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1328 x 56; padding 0px 8px 0px 0px; radius 8px; background transparent; text Inter 14/24 600, #ffffff `color.brand.white`; layers button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 56.0x56.0 rgb(107, 107, 107) 4px; button.TrackRowPlayButton_albumCover__Pv48J.rounded-(--es-radius-detail) 0.0x0.0 rgba(207, 214, 229, 0.16) 4px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 rgba(207, 214, 229, 0) 10000px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 rgba(207, 214, 229, 0) 10000px; button.focus-visible._iconBu |
| hover | background rgba(207, 214, 229, 0.08) `color.action.ghost.hovered`; icon 24 x 24, #ffffff `color.brand.white`; layers none |

Child layers that carry the look: button 56x56 background #6b6b6b radius 4px; button 0x0 background rgba(207, 214, 229, 0.16) `color.action.accent.disabled` radius 4px; button 44x44 background rgba(207, 214, 229, 0) `color.action.ghost.default` radius 10000px.

![SFX track row default](components/crops/sfx-row-default.png) ![SFX track row hover](components/crops/sfx-row-hover.png)

#### SFX play button
An SFX row's play button; measured, never pressed. As on the genre list, row hover swaps the cover button out — the hover-state box is a real 0x0. Read as `sfx-play` on the sound-effects category page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 56 x 56; radius 4px; background #6b6b6b; text Inter 16/18.4 400, #ffffff `color.brand.white` |
| focus-visible | outline 1px auto #101010, offset 0px |

**Not a reading.** In `hover` this element's box is 0 x 0 (it leaves the layout), so that state's look is on its container, not measured here.

![SFX play button default](components/crops/sfx-play-default.png) ![SFX play button focus-visible](components/crops/sfx-play-focus-visible.png) ![SFX play button pressed](components/crops/sfx-play-pressed.png)

#### SFX subcategory link
A subcategory link inside a row's categories column (e.g. "Suburban" under Ambience) — this page has no large category card, the in-row text link is the real subcategory surface; measured, never followed. Read as `sfx-category-card` on the sound-effects category page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 39 x 20; background transparent; text Inter 12/16 400, rgba(255, 255, 255, 0.72) `color.icon.secondary` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.TrackRow_scrollingText__fQwVK.TrackRow_trackRowScrollableLink__n7oIr 39.0x20.0 1px auto rgb(16, 16, 16) offset 1px |

![SFX subcategory link default](components/crops/sfx-category-card-default.png) ![SFX subcategory link hover](components/crops/sfx-category-card-hover.png) ![SFX subcategory link focus-visible](components/crops/sfx-category-card-focus-visible.png) ![SFX subcategory link pressed](components/crops/sfx-category-card-pressed.png)

### Signup upsell

The #ff82c2 pink 'Want more music?' upsell card inside the dark catalog — an accent-coloured island.

#### Want-more banner
The #ff82c2 pink "Want more music?" upsell card between the list and the FAQ — an accent-coloured island on the dark page. Read as `wantmore` on the genre page.

**Values (default).** size 1328 x 244; background transparent; text Sebenta 40/48 500, #000000 `color.brand.black`; layers div.WantMoreBanner_wrapper__XCHly.dark-theme-override 1328.0x244.0 rgb(255, 130, 194); a.no-default-focus.focus-visible 173.0x44.0 rgb(255, 255, 255) 10000px.

Child layers that carry the look: div 1328x244 background #ff82c2 `color.action.accent.default`; a 173x44 background #ffffff `color.brand.white` radius 10000px.

![Want-more banner default](components/crops/wantmore-default.png)

#### Upsell CTA
The banner's Create-free-account button; measured never followed. Read as `wantmore-cta` on the genre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 173 x 44; padding 4px 16px; radius 10000px; background #ffffff `color.brand.white`; text Inter 14/24 600, #000000 `color.brand.black` |
| hover | background #e7e7e7 `color.action.primary.hovered` |
| focus-visible | outline 2px solid #20afff `color.background.beta`, offset 2px |
| pressed | background #cfcfcf `color.action.primary.pressed` |

![Upsell CTA default](components/crops/wantmore-cta-default.png) ![Upsell CTA hover](components/crops/wantmore-cta-hover.png) ![Upsell CTA focus-visible](components/crops/wantmore-cta-focus-visible.png) ![Upsell CTA pressed](components/crops/wantmore-cta-pressed.png)

### Login and signup (Keycloak, dark)

The dark login.epidemicsound.com Keycloak cards: social buttons, email/password fields, show-password, submit, forgot-password and create-account links — measured, never submitted.

#### Login card
The dark Keycloak form-card on login.epidemicsound.com: logo, social buttons, email/password form, links. Read as `kc-card` on the login page.

**Values (default).** size 416 x 882.81; background transparent; text Sebenta 48/56 500, #ffffff `color.brand.white`; layers a.button.primary 416.0x56.0 rgb(255, 255, 255) T:1px solid rgb(116, 119, 117) / R:1px solid rgb(116, 119, 117) / B:1px solid rgb(116, 119, 117) / L:1px solid rgb(116, 119, 117) 10000px; a.button.primary 416.0x56.0 rgb(255, 255, 255) T:1px solid rgb(116, 119, 117) / R:1px solid rgb(116, 119, 117) / B:1px solid rgb(116, 119, 117) / L:1px solid rgb(116, 119, 117) 10000px; div.socialLine 188.5x1.0 rgb.

Child layers that carry the look: a 416x56 background #ffffff `color.brand.white` border 1px solid #747775 radius 10000px; a 416x56 background #ffffff `color.brand.white` border 1px solid #747775 radius 10000px; div 188.5x1 background rgba(207, 214, 229, 0.16) `color.action.accent.disabled`.

![Login card default](components/crops/kc-card-default.png)

#### Login heading
The "Log in" heading over the form. Read as `kc-h1` on the login page.

**Values (default).** size 148.25 x 56; background transparent; text Sebenta 48/56 500, #ffffff `color.brand.white`.

![Login heading default](components/crops/kc-h1-default.png)

#### Social button
The "Continue with Google" social button; measured, never followed. Read as `kc-social-google` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 416 x 56; border 1px solid #747775; radius 10000px; background #ffffff `color.brand.white`; text Inter 16/18 600, #0f0f0f |
| hover | background #e7e7e7 `color.action.primary.hovered` |
| focus-visible | outline 2px solid #ffffff `color.brand.white`, offset 2px |
| pressed | background #cfcfcf `color.action.primary.pressed` |

![Social button default](components/crops/kc-social-google-default.png) ![Social button hover](components/crops/kc-social-google-hover.png) ![Social button focus-visible](components/crops/kc-social-google-focus-visible.png) ![Social button pressed](components/crops/kc-social-google-pressed.png)

#### Email field
The login email input; focused and typed into then cleared — never submitted. Read as `kc-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 414 x 54; padding 15px 16px; background transparent; text Inter 16/24 400, #ffffff `color.brand.white`; placeholder #757575 |
| filled | size 414 x 56; padding 25px 16px 7px 16px |

![Email field default](components/crops/kc-email-default.png) ![Email field focused](components/crops/kc-email-focused.png) ![Email field filled](components/crops/kc-email-filled.png)

#### Password field
The login password input; focused and typed into then cleared — never submitted. Read as `kc-password` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 414 x 54; padding 15px 52px 15px 16px; background transparent; text Inter 16/24 400, #ffffff `color.brand.white`; placeholder #757575 |
| filled | size 414 x 56; padding 25px 52px 7px 16px |

![Password field default](components/crops/kc-password-default.png) ![Password field focused](components/crops/kc-password-focused.png) ![Password field filled](components/crops/kc-password-filled.png)

#### Show-password button
The eye icon button inside the password field (a local reveal toggle); measured, never clicked. Read as `kc-show-pass` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; radius 10000px; background transparent; text Inter 16/26.56 400, #000000 `color.brand.black`; transition background-color 0.1s ease; transform translate(0px, -22px) |
| hover | background rgba(255, 255, 255, 0.08) |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.password-visibility-toggle 44.0x44.0 1px auto rgb(16, 16, 16) offset 0px 10000px |
| pressed | background rgba(255, 255, 255, 0.16) |

![Show-password button default](components/crops/kc-show-pass-default.png) ![Show-password button hover](components/crops/kc-show-pass-hover.png) ![Show-password button focus-visible](components/crops/kc-show-pass-focus-visible.png) ![Show-password button pressed](components/crops/kc-show-pass-pressed.png)

#### Log in submit
The white primary submit button; its states were measured but it was never clicked — nothing was submitted. Read as `kc-submit` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 416 x 56; padding 1px 6px; radius 10000px; background #ffffff `color.brand.white`; text Inter 16/18 600, #0f0f0f |
| hover | background #e7e7e7 `color.action.primary.hovered` |
| focus-visible | outline 2px solid #ffffff `color.brand.white`, offset 2px |
| pressed | background #cfcfcf `color.action.primary.pressed` |

![Log in submit default](components/crops/kc-submit-default.png) ![Log in submit hover](components/crops/kc-submit-hover.png) ![Log in submit focus-visible](components/crops/kc-submit-focus-visible.png) ![Log in submit pressed](components/crops/kc-submit-pressed.png)

#### Create-account link
The "Create account" link over the form; measured, never followed. Read as `kc-signup-link` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 112 x 20; background transparent; text Inter 16/26.56 400, #ffffff `color.brand.white` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a 112.0x20.0 1px auto rgb(16, 16, 16) offset 1px |

![Create-account link default](components/crops/kc-signup-link-default.png) ![Create-account link hover](components/crops/kc-signup-link-hover.png) ![Create-account link focus-visible](components/crops/kc-signup-link-focus-visible.png) ![Create-account link pressed](components/crops/kc-signup-link-pressed.png)

#### Forgot-password link
The "Forgot password?" link; measured, never followed. Read as `kc-forgot` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 131 x 26.55; background transparent; text Inter 16/26.56 400, #ffffff `color.brand.white` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a 131.0x26.5 1px auto rgb(16, 16, 16) offset 1px |

![Forgot-password link default](components/crops/kc-forgot-default.png) ![Forgot-password link hover](components/crops/kc-forgot-hover.png) ![Forgot-password link focus-visible](components/crops/kc-forgot-focus-visible.png) ![Forgot-password link pressed](components/crops/kc-forgot-pressed.png)

#### Signup card
The Keycloak registration card; measured at rest only. Read as `su-card` on the signup page.

**Values (default).** size 416 x 864.88; background transparent; text Sebenta 48/56 500, #ffffff `color.brand.white`; icon 16.45 x 12.8, rgba(255, 255, 255, 0.72) `color.icon.secondary`; layers a.button.primary 416.0x56.0 rgb(255, 255, 255) T:1px solid rgb(116, 119, 117) / R:1px solid rgb(116, 119, 117) / B:1px solid rgb(116, 119, 117) / L:1px solid rgb(116, 119, 117) 10000px; a.button.primary 416.0x56.0 rgb(255, 255, 255) T:1px solid rgb(116, 119, 117) / R:1px solid rgb(116, 119, 117) / B:1px solid rgb(116, 119, 117) / L:1px solid rgb(116, 119, 117) 10000px; div.socialLine 188.5x1.0 rgb.

Child layers that carry the look: a 416x56 background #ffffff `color.brand.white` border 1px solid #747775 radius 10000px; a 416x56 background #ffffff `color.brand.white` border 1px solid #747775 radius 10000px; div 188.5x1 background rgba(207, 214, 229, 0.16) `color.action.accent.disabled`.

![Signup card default](components/crops/su-card-default.png)

#### Signup field
A registration form input; focused and typed into then cleared — never submitted. Read as `su-field` on the signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 414 x 54; padding 15px 16px; background transparent; text Inter 16/24 400, #ffffff `color.brand.white`; placeholder #757575 |
| filled | size 414 x 56; padding 25px 16px 7px 16px |

![Signup field default](components/crops/su-field-default.png) ![Signup field focused](components/crops/su-field-focused.png) ![Signup field filled](components/crops/su-field-filled.png)

#### Signup submit
The registration form's submit action; its states were measured but it was never clicked — nothing was submitted. Read as `su-submit` on the signup page.

**Wrong element.** These readings are the "Continue with Google" link, not the registration form's submit: the `a.button` alternative matched it first. Recapture needed.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 416 x 56; border 1px solid #747775; radius 10000px; background #ffffff `color.brand.white`; text Inter 16/18 600, #0f0f0f |
| hover | background #e7e7e7 `color.action.primary.hovered` |
| focus-visible | outline 2px solid #ffffff `color.brand.white`, offset 2px |
| pressed | background #cfcfcf `color.action.primary.pressed` |

![Signup submit default](components/crops/su-submit-default.png) ![Signup submit hover](components/crops/su-submit-hover.png) ![Signup submit focus-visible](components/crops/su-submit-focus-visible.png) ![Signup submit pressed](components/crops/su-submit-pressed.png)

### Mobile (390 wide)

The phone surface at 390 wide: the 100px top bar, the hamburger nav overlay, the genre banner and track rows.

#### Mobile header
The phone top bar: ES glyph, Create free account, hamburger. Read as `m-header` on the genre page at 390 wide.

**Values (default).** size 390 x 100; background transparent; text Inter 14/24 600, #000000 `color.brand.black`; icon 20 x 24, #9e9eff; layers div.relative.mx-auto 358.0x68.0 rgb(41, 44, 51) 10000px; ul.my-0.list-none 0.0x0.0 rgb(41, 44, 51) 16px; span.flex.size-10 0.0x0.0 rgba(207, 214, 229, 0.16) 4px; span.flex.size-10 0.0x0.0 rgba(207, 214, 229, 0.16) 4px; span.flex.size-10 0.0x0.0 rgba(207, 214, 229, 0.16) 4px; span.flex.size-10 0.0x0.0 rgba(207, 214, 229, 0.16) 4px.

Child layers that carry the look: div 358x68 background #292c33 `color.background.brand.off.black` radius 10000px; ul 0x0 background #292c33 `color.background.brand.off.black` radius 16px; span 0x0 background rgba(207, 214, 229, 0.16) `color.action.accent.disabled` radius 4px.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile hamburger
The "Show navigation menu" icon button — a local disclosure; the opened state was measured after clicking it. Read as `m-hamburger` on the genre page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 44 x 44; radius 10000px; background transparent; text Inter 16/18.4 400, #ffffff `color.brand.white`; icon 20 x 20, #ffffff `color.brand.white` |
| focus-visible, opened | outline 2px solid #20afff `color.background.beta`, offset 2px; layers button.focus-visible._iconButton_wmtv6_1 44.0x44.0 2px solid rgb(32, 175, 255) offset 2px 10000px |

![Mobile hamburger default](components/crops/m-hamburger-default.png) ![Mobile hamburger hover](components/crops/m-hamburger-hover.png) ![Mobile hamburger focus-visible](components/crops/m-hamburger-focus-visible.png) ![Mobile hamburger pressed](components/crops/m-hamburger-pressed.png) ![Mobile hamburger opened](components/crops/m-hamburger-opened.png)

#### Mobile nav link
A link inside the opened phone nav; measured, never followed. Read as `m-nav-item` on the genre page at 390 wide.

**Values (default).** size 326 x 44; radius 10000px; background transparent; text Inter 14/24 600, #ffffff `color.brand.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #ffffff `color.brand.white`.

![Mobile nav link default](components/crops/m-nav-item-default.png)

#### Mobile CTA
The Create-free-account button in the phone header; measured never followed. Read as `m-cta` on the genre page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 173 x 44; padding 4px 16px; radius 10000px; background #ffffff `color.brand.white`; text Inter 14/24 600, #000000 `color.brand.black` |
| focus-visible | outline 2px solid #20afff `color.background.beta`, offset 2px |

![Mobile CTA default](components/crops/m-cta-default.png) ![Mobile CTA hover](components/crops/m-cta-hover.png) ![Mobile CTA focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile CTA pressed](components/crops/m-cta-pressed.png)

#### Mobile genre heading
"Pop music" on the phone genre banner. Read as `m-genre-h1` on the genre page at 390 wide.

**Values (default).** size 125.69 x 30; background transparent; text Sebenta 24/30 500, #000000 `color.brand.black`.

![Mobile genre heading default](components/crops/m-genre-h1-default.png)

#### Mobile track row
A 56px track row in the phone list (cover, title, artist). Read as `m-track-row` on the genre page at 390 wide.

**Values (default).** size 358 x 56; padding 0px 8px 0px 0px; radius 8px; background transparent; text Inter 14/24 600, #ffffff `color.brand.white`; layers button.TrackRowPlayButton_albumCover__Pv48J.overflow-hidden 56.0x56.0 rgb(107, 107, 107) 4px; button.TrackRowPlayButton_albumCover__Pv48J.rounded-(--es-radius-detail) 0.0x0.0 rgba(207, 214, 229, 0.16) 4px; button.focus-visible._iconButton_wmtv6_1 0.0x0.0 rgba(207, 214, 229, 0) 10000px; button.focus-visible._iconButton_wmtv6_1 44.0x44.0 rgba(207, 214, 229, 0) 10000px; button.focus-visible._iconButt.

Child layers that carry the look: button 56x56 background #6b6b6b radius 4px; button 0x0 background rgba(207, 214, 229, 0.16) `color.action.accent.disabled` radius 4px; button 0x0 background rgba(207, 214, 229, 0) `color.action.ghost.default` radius 10000px.

![Mobile track row default](components/crops/m-track-row-default.png)

### Footer

The page footers: link columns and the social icon buttons.

#### Footer
The catalog page footer: link columns, social icon buttons, locale line. Read as `footer` on the genre page.

**Values (default).** size 1440 x 681; padding 80px 0px 0px 0px; background transparent; text Inter 12/16 500, rgba(255, 255, 255, 0.72) `color.icon.secondary`; layers div.m-0.border-b-1 0.0x0.0 B:1px solid rgba(207, 214, 229, 0.16); summary.no-default-focus.focus-visible 0.0x0.0 rgb(18, 20, 24) 8px; div.m-0.border-b-1 0.0x0.0 B:1px solid rgba(207, 214, 229, 0.16); summary.no-default-focus.focus-visible 0.0x0.0 rgb(18, 20, 24) 8px; div.m-0.border-b-1 0.0x0.0 B:1px solid rgba(207, 214, 229, 0.16); summary.no-default-focus.focus-visible 0.0x0.0 rgb(18, 20, 24) 8px.

Child layers that carry the look: div 0x0 border 1px solid rgba(207, 214, 229, 0.16) `color.action.accent.disabled`; summary 0x0 background #121418 `color.background.base` radius 8px; div 0x0 border 1px solid rgba(207, 214, 229, 0.16) `color.action.accent.disabled`.

![Footer default](components/crops/footer-default.png)

#### Social icon button
A footer social icon button (ghost, _m_ size); measured never followed. Read as `social-icon` on the genre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 56 x 56; radius 10000px; background rgba(207, 214, 229, 0) `color.action.ghost.default`; text Inter 16/16 400, rgba(255, 255, 255, 0.72) `color.icon.secondary`; icon 24 x 24, rgba(255, 255, 255, 0.72) `color.icon.secondary` |
| hover | background rgba(207, 214, 229, 0.08) `color.action.ghost.hovered` |
| focus-visible | background rgba(207, 214, 229, 0.08) `color.action.ghost.hovered`; outline 2px solid #20afff `color.background.beta`, offset 2px |
| pressed | background rgba(207, 214, 229, 0.16) `color.action.accent.disabled` |

![Social icon button default](components/crops/social-icon-default.png) ![Social icon button focus-visible](components/crops/social-icon-focus-visible.png) ![Social icon button pressed](components/crops/social-icon-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Epidemic Sound logotype, the row action glyphs, the social icons, the catalogue artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The signed-in Epidemic Sound lives behind login.epidemicsound.com — the library, playlists, downloads, stems, the Eclipse/Studio tools, billing and account settings all need an account and were never reached. The catalog pages (/music/genres, /music/themes, /artists, /sound-effects) are genuinely public signed-out surfaces; playback itself was never started, so what happens after Play is unverified.

### Pages

- **The account.** Every post-login surface was never reached; the login and signup forms were measured as forms and never submitted.
- **Checkout and trials.** Every Create-free-account, Get-30-days-free and Pricing action was measured, never followed.
- **Playback and downloads.** The track-row Play, Find-similar, Like, Add-to-playlist, Download and Copy-link controls were measured, never activated; what playing or downloading a track does signed out is unverified.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover), so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

Epidemic Sound paints an alternative-light (ecru) marketing surface and a dark catalog/account surface via body theme classes (`alternative-light-theme-override`, `dark-theme-override`, bare `:root`) rather than a user toggle — but the stylesheets genuinely declare light/dark/alternative/alternative-light/system/plugin/premiere-pro scopes, so tokens.json keeps real light and dark sets (light resolves the alternative-light values the marketing pages paint).

### Fonts

- **Inter** (all UI text and buttons) and **Sebenta** (every es-heading/es-subheading, weight 500 with serif fallbacks) are the served faces. They are served from cdn.epidemicsound.com as woff2 (Sebenta-Medium, Inter) plus local() fallbacks; the style guide falls back to system sans.

### Screenshots

- The track/artist names, album covers, the Epidemic Sound wordmark and any photography in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Track titles, artist names and catalogue artwork are the product's content; only frames and components were measured. The Keycloak login/signup cards are the product's own branded forms; nothing was entered into them beyond a cleared sample string.
