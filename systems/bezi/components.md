# Bezi components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from www.bezi.com on 2026-11-11, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (23 components, 50 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 14/21 500, #111827`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (48 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-dark-{state}.png`: the site paints one dark theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages (1x on desktop, 2x on mobile); mobile shots are `mobile-{page}-dark-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-dark-default.png), [full](screenshots/pricing-dark-full.png) |
| About | `/about` | [default](screenshots/about-dark-default.png), [full](screenshots/about-dark-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png), [menu-open](screenshots/mobile-home-dark-menu-open.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-dark-default.png), [full](screenshots/mobile-pricing-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu, open | header, phone | the menu trigger's own press | [mobile-home-dark-menu-open](screenshots/mobile-home-dark-menu-open.png), [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 8 components were given a real keyboard focus (a further 1 could not be driven: `plan-cta`). 8 show a visible focus state: `nav-link` (1px auto #005fcc, offset 1px), `nav-discord` (1px auto #005fcc, offset 1px), `cta` (1px auto rgb(0, 95, 204) offset 1px on a (child layer)), `tools-button` (1px solid #ffffff `color.ink.0`, offset 8px), `view-all` (1px auto #005fcc, offset 1px), `footer-link` (1px auto #005fcc, offset 1px), `footer-social` (1px auto #005fcc, offset 1px), `footer-legal` (1px auto #005fcc, offset 1px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): controls deepen their fill or dim rather than scale; the nav flyout and framework icons keep their hover scale. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.18s | `ease` | color, opacity | tools-button |
| 0.42s | `cubic-bezier(0.2, 0.8, 0.2, 1)` | transform | tools-button |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 366 x 499 | - | - | #1a1a1a | none | 24px |
| [Connected tools chip](#connected-tools-chip) | 117.8 x 142.5 | 1px solid rgba(242, 241, 236, 0.32) | - | - | none | 0 |

## Components

### Shell and navigation

The floating dark pill header, the announcement strip and the ghost-mark hero type.

#### Header
The floating dark pill bar: the Bezi mark, the nav links (Studios, Product, Pricing, Blog, Docs, Discord) and nothing else on it. Read as `header` on the home page.

**Values (default).** size 1124 x 80; padding 12px; background transparent; text Inter 16/22.4 400, #ffffff `color.ink.0`.

Child layers that carry the look: div 1100x56 background rgba(31, 31, 31, 0.84) radius 144px; div 154x39 background #f84503 `color.orange.600` radius 102.93px; div 9x6 image url(data:…)%22></path></svg>").

![Header default](components/crops/header-default.png)

#### Logo
Read as `logo` on the home page.

**Values (default).** size 107 x 18.92; background transparent; text sans-serif 12/normal 400, #0000ee.

![Logo default](components/crops/logo-default.png)

#### Nav link
Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 66.42 x 38.41; padding 8px; background transparent; text Inter 16/22.4 400, #ffffff `color.ink.0` |
| focus-visible | outline 1px auto #005fcc, offset 1px; child paint a.framer-Ae6d7.framer-t46sH: size 66.4x38.4; outline 1px auto rgb(0, 95, 204) offset 1px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Discord link
Read as `nav-discord` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 71.92 x 38.41; padding 8px; background transparent; text Inter 16/22.4 400, #ffffff `color.ink.0` |
| focus-visible | outline 1px auto #005fcc, offset 1px; child paint a.framer-Ae6d7.framer-t46sH: size 71.9x38.4; outline 1px auto rgb(0, 95, 204) offset 1px |

![Discord link default](components/crops/nav-discord-default.png) ![Discord link hover](components/crops/nav-discord-hover.png) ![Discord link focus-visible](components/crops/nav-discord-focus-visible.png) ![Discord link pressed](components/crops/nav-discord-pressed.png)

#### Hero title
"AI for building real games" in the display face. Read as `hero-title` on the home page.

**Values (default).** size 960 x 51.94; background transparent; text The Future Medium 53/51.94 500, #ffffff `color.ink.0`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero subcopy
Read as `hero-sub` on the home page.

**Values (default).** size 1100 x 43.19; background transparent; text Inter 16/21.6 400, rgba(255, 255, 255, 0.5).

![Hero subcopy default](components/crops/hero-sub-default.png)

#### TRY FOR FREE button
The orange CTA repeated across the page. Measured, never followed. Read as `cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 154 x 39; padding 14.04px; radius 102.93px; background #f84503 `color.orange.600`; text Space Mono 14/14 400, #ffffff `color.ink.0` |
| focus-visible | child paint a: size 102.8x14.0; outline 1px auto rgb(0, 95, 204) offset 1px |

![TRY FOR FREE button default](components/crops/cta-default.png) ![TRY FOR FREE button hover](components/crops/cta-hover.png) ![TRY FOR FREE button focus-visible](components/crops/cta-focus-visible.png) ![TRY FOR FREE button pressed](components/crops/cta-pressed.png)

#### Announcement line
The "NEW · Bezi for Unreal Engine is now publicly available" strip under the header. Read as `announcement` on the home page.

**Values (default).** size 643.88 x 32.2; padding 8px 12px 8px 8px; radius 2px; background #1c1c1c; text Space Mono 11/13.2 700, #ff9366; icon 9 x 9, #0000ee.

![Announcement line default](components/crops/announcement-default.png)

#### Section title
Read as `section-title` on the home page.

**Values (default).** size 444 x 35.89; padding 0px 0px 14px 0px; border B: 1px solid rgba(255, 255, 255, 0.05) `color.white-alpha.5`; background transparent; text Inter 19/20.9 700, #f4f1ea.

Child layers that carry the look: h2 444x35.9 border 1px solid rgba(255, 255, 255, 0.05) `color.white-alpha.5`.

![Section title default](components/crops/section-title-default.png)

#### Connected tools chip
The "02. CONNECTED TOOLS" index button on the home page. Read as `tools-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 117.8 x 142.5; background transparent; text The Future Mono 10/10 400, rgba(242, 241, 236, 0.32); transition opacity 0.18s ease, transform 0.42s cubic-bezier(0.2, 0.8, 0.2, 1), color 0.18s ease; transform scale(0.95); opacity 0.55; icon 23.75 x 23.75, #f2f1ec `measured.chip-text` |
| hover | size 124 x 150; text The Future Mono 10/10 400, #ffffff `color.ink.0`; transform none; opacity none; icon 25 x 25, #f2f1ec `measured.chip-text`; child paint span.pcfm-corner.pcfm-tl: size 26.0x26.0; border 1px solid #ffffff `color.ink.0`; span.pcfm-corner.pcfm-tr: size 26.0x26.0; border 1px solid #ffffff `color.ink.0`; span.pcfm-corner.pcfm-bl: size 26.0x26.0; border 1px solid #ffffff `color.ink.0`; span.pcfm-corner.pcfm-br: size 26.0x26.0; border 1px solid #ffffff `color.ink.0` |
| focus-visible | size 124 x 150; outline 1px solid #ffffff `color.ink.0`, offset 8px; text The Future Mono 10/10 400, #ffffff `color.ink.0`; transform none; opacity none; icon 25 x 25, #f2f1ec `measured.chip-text`; child paint button.pcfm-stage: size 124.0x150.0; outline 1px solid rgb(255, 255, 255) offset 8px; span.pcfm-corner.pcfm-tl: size 26.0x26.0; border 1px solid #ffffff `color.ink.0`; span.pcfm-corner.pcfm-tr: size 26.0x26.0; border 1px solid #ffffff `color.ink.0`; span.pcfm-corner.pcfm-bl: size 26.0x26.0; border 1px solid #ffffff `color.ink.0`; span.pcfm-corner.pcfm-br: size 26.0x26.0; border 1px solid #ffffff `color.ink.0` |
| pressed | size 124 x 150; text The Future Mono 10/10 400, #ffffff `color.ink.0`; transform none; opacity none; icon 25 x 25, #f2f1ec `measured.chip-text`; child paint span.pcfm-corner.pcfm-tl: size 26.0x26.0; border 1px solid #ffffff `color.ink.0`; span.pcfm-corner.pcfm-tr: size 26.0x26.0; border 1px solid #ffffff `color.ink.0`; span.pcfm-corner.pcfm-bl: size 26.0x26.0; border 1px solid #ffffff `color.ink.0`; span.pcfm-corner.pcfm-br: size 26.0x26.0; border 1px solid #ffffff `color.ink.0` |

Child layers that carry the look: span 19x19 border 1px solid rgba(242, 241, 236, 0.32); span 19x19 border 1px solid rgba(242, 241, 236, 0.32); span 19x19 border 1px solid rgba(242, 241, 236, 0.32).

![Connected tools chip default](components/crops/tools-button-default.png) ![Connected tools chip hover](components/crops/tools-button-hover.png) ![Connected tools chip focus-visible](components/crops/tools-button-focus-visible.png) ![Connected tools chip pressed](components/crops/tools-button-pressed.png)

#### View all link
The blog index link. Read as `view-all` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 110.34 x 43.2; padding 12px 16px; radius 2px; background rgba(255, 255, 255, 0.2) `color.white-alpha.20`; text Space Mono 16/19.2 400, #ffffff `color.ink.0` |
| hover | child paint div: size 110.3x43.2; background rgba(9, 9, 13, 0); div: size 15.8x14.4; div: size 15.8x14.4; div: size 15.8x14.4; div: size 15.8x14.4; div: size 15.8x14.4; div: size 15.8x14.4; div: size 15.8x14.4; div: size 15.8x14.4; div: size 15.8x14.4; div: size 15.8x14.4; div: size 15.8x14.4; div: size 15.8x14.4 |
| focus-visible | outline 1px auto #005fcc, offset 1px; child paint a.framer-18qb6ey.framer-ozzz8l: outline 1px auto rgb(0, 95, 204) offset 1px; div: size 110.3x43.2; background rgba(9, 9, 13, 0); div: size 9.4x8.6; div: size 9.4x8.6; div: size 9.4x8.6 |
| pressed | child paint div: size 110.3x43.2; background rgba(9, 9, 13, 0); div: size 9.4x8.6; div: size 9.4x8.6; div: size 9.4x8.6 |

![View all link default](components/crops/view-all-default.png) ![View all link hover](components/crops/view-all-hover.png) ![View all link focus-visible](components/crops/view-all-focus-visible.png) ![View all link pressed](components/crops/view-all-pressed.png)

#### Page ground
The near-black the whole page paints on. Read as `page-ground` on the home page.

**Values (default).** size 1440 x 7394.39; background #0d0d0d; text Inter 16/22.4 400, #ffffff `color.ink.0`; icon 6.91 x 6.91, #0000ee.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Pricing

The Individual/Studio billing toggle, the Free band and the plan columns.

#### Pricing title
Read as `pricing-title` on the pricing page.

**Values (default).** size 1100 x 70.41; background transparent; text Inter Display 64/70.4 500, #ffffff `color.ink.0`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Plan CTA
The action inside the Free trial band. Measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 126.7 x 48; padding 12px 20px; background rgba(0, 0, 0, 0.84) `measured.plancta-fill`; text Space Mono 12/14.4 400, #ffffff `color.ink.0` |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan card
Read as `plan-card` on the pricing page.

**Values (default).** size 366 x 499; padding 24px; background #1a1a1a; text Inter Display 20/28 400, #e8e8e8.

![Plan card default](components/crops/plan-card-default.png)

### Footer

The link columns, socials and legal.

#### Footer
Read as `footer` on the home page.

**Values (default).** size 1440 x 538.31; padding 72px 60px 50px 60px; background rgba(255, 255, 255, 0.05) `color.white-alpha.5`; text P-DOT Regular 12/18 400, rgba(242, 241, 236, 0.48); icon 20 x 20, #f2f1ec `measured.chip-text`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 50.42 x 20; background transparent; text Inter 16/22.4 400, #f2f1ec `measured.chip-text` |
| focus-visible | outline 1px auto #005fcc, offset 1px; child paint a.framer-text: size 50.4x20.0; outline 1px auto rgb(0, 95, 204) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer social icon
Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; padding 8px; background transparent; text sans-serif 12/normal 400, #0000ee; icon 20 x 20, #f2f1ec `measured.chip-text` |
| hover | size 39.6 x 39.6; background rgba(242, 241, 236, 0.08); transform scale(1.1); icon 22 x 22, #f2f1ec `measured.chip-text`; child paint a.framer-1sv7g11.framer-a97pow: size 39.6x39.6; background rgba(242, 241, 236, 0.08) |
| focus-visible | outline 1px auto #005fcc, offset 1px; child paint a.framer-1sv7g11.framer-a97pow: size 36.0x36.0; outline 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text sans-serif 12/normal 400, #ff0000 |

![Footer social icon default](components/crops/footer-social-default.png) ![Footer social icon focus-visible](components/crops/footer-social-focus-visible.png) ![Footer social icon pressed](components/crops/footer-social-pressed.png)

#### G2 rating badge
The "4.6 Star Rating" badge linking the G2 review page. Measured, never followed. Read as `footer-rating` on the home page.

Not on the page when it was captured.

#### Legal link
Read as `footer-legal` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 100.2 x 20; background transparent; text Inter 16/22.4 400, #f2f1ec `measured.chip-text` |
| focus-visible | outline 1px auto #005fcc, offset 1px; child paint a.framer-text: size 100.2x20.0; outline 1px auto rgb(0, 95, 204) offset 1px |

![Legal link default](components/crops/footer-legal-default.png) ![Legal link hover](components/crops/footer-legal-hover.png) ![Legal link focus-visible](components/crops/footer-legal-focus-visible.png) ![Legal link pressed](components/crops/footer-legal-pressed.png)

### Mobile (390 wide)

The same surface at phone width, with its hamburger menu.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 79; padding 16px; background transparent; text Inter 18/21.6 500, #ffffff `color.ink.0`.

Child layers that carry the look: div 358x54 background rgba(31, 31, 31, 0.84) radius 24px; div 14x1 background #ffffff `color.ink.0`; div 14x1 background #ffffff `color.ink.0`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
The 36px trigger at the right of the mobile bar; its own press opens the menu overlay. Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 14 x 14; background transparent; text sans-serif 12/normal 400, #000000 `color.ink.950` |

Child layers that carry the look: div 14x1 background #ffffff `color.ink.0`; div 14x1 background #ffffff `color.ink.0`; div 14x1 background #ffffff `color.ink.0`.

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The trigger after its own toggle; the open overlay shows in the crop. Read as `m-menu-open` on the home page at 390 wide.

**Values (opened).** size 14 x 14; background transparent; wrapper header.framer-UYLLm.framer-soqjxm: shadow rgba(0, 0, 0, 0.1) 0px 7.14px 20px 0px; text sans-serif 12/normal 400, #000000 `color.ink.950`.

Child layers that carry the look: div 10.6x10.6 background #ffffff `color.ink.0`; div 14x1 background #ffffff `color.ink.0`; div 10.6x10.6 background #ffffff `color.ink.0`.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Bezi's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The product itself.** Bezi is a desktop app download; no sign-in, account or app surface was reached, and the TRY FOR FREE links were never followed.
- **Anything that sends or signs in.** No form was submitted, no download started, no account was created; outbound links (Docs, Discord, socials, G2) were measured, never followed.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The site paints one dark theme on every captured route; the Framer bundle declares no light variant, so no light set is emitted.

### Fonts

- **The UI fonts** are Framer-served webfonts (the bundle declares 314 @font-face entries; `fonts` in [raw/css-vars.json](raw/css-vars.json)); the font files themselves are not committed.
- Illustration and wordmark artwork in the screenshots are Bezi's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The animated product-window imagery, the showcase game art and the wordmark are Bezi's content; only the frames and components were measured.
