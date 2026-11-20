# Artboard Studio components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from artboard.studio on 2026-11-11, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was sent, submitted or signed into.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (25 components, 54 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (54 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [tab](screenshots/home-light-tab.png) |
| Mockup library | `/mockup` | [default](screenshots/mockup-light-default.png), [full](screenshots/mockup-light-full.png), [scrolled](screenshots/mockup-light-scrolled.png), [scrolled2](screenshots/mockup-light-scrolled2.png) |
| Figma plugin | `/figma-mockup` | [default](screenshots/figma-mockup-light-default.png), [full](screenshots/figma-mockup-light-full.png) |
| iPhone mockups | `/iphone-mockup` | [default](screenshots/iphone-mockup-light-default.png), [full](screenshots/iphone-mockup-light-full.png), [scrolled](screenshots/iphone-mockup-light-scrolled.png) |
| Business card mockups | `/business-card-mockup` | [default](screenshots/business-card-mockup-light-default.png), [full](screenshots/business-card-mockup-light-full.png), [scrolled](screenshots/business-card-mockup-light-scrolled.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Category tab switched | home | a tab's own toggle; the selection moves locally | [home-light-tab](screenshots/home-light-tab.png), [tab-switched](#tab-switched) |
| Library, mid-scroll | mockup library | the inner .container-category-pages pane scrolled | [mockup-light-scrolled](screenshots/mockup-light-scrolled.png), [mockup-light-scrolled2](screenshots/mockup-light-scrolled2.png) |
| Mobile menu, open | home, phone | the menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 9 components were given a real keyboard focus. 8 show a visible focus state: `nav-link` (1px auto #005fcc, offset 1px), `nav-signup` (1px auto #005fcc, offset 1px), `plugin-cta` (1px auto #005fcc, offset 1px), `contact-cta` (1px auto #005fcc, offset 1px), `filter-chip` (1px auto #005fcc, offset 1px), `figma-cta` (1px auto #005fcc, offset 1px), `m-menu-button` (2px solid #4d65ff, offset 2px), `footer-link` (1px auto #005fcc, offset 1px). The other 1 show no change a keyboard user can see: `tab`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover) on 9 components; nothing that would submit or navigate was pressed. 7 change from default: `nav-link` (text system-ui 16/16 400, #aaaaaa); `nav-signup` (text system-ui 16/16 400, #aaaaaa); `plugin-cta` (background #222222); `contact-cta` (background #222222); `filter-chip` (background #222222); `figma-cta` (background #222222); `footer-link` (text system-ui 16/16 400, #aaaaaa). The other 2 read the same as default.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Header](#header) | 1440 x 106 | - | - | transparent | none | 0 |
| [Hero title](#hero-title) | 768 x 145.91 | - | - | transparent | none | 0 |
| [Category tab](#category-tab) | 200.27 x 50 | 1px solid rgba(13, 20, 0, 0.1) | 8px | #0d1400 `color.scheme.1..accent` | none | 12px 24px |
| [Mockup card](#mockup-card) | 199.27 x 199.27 | 1px solid rgba(13, 20, 0, 0.1) | 8px | transparent | none | 0 |
| [Library search field](#library-search-field) | 1005 x 64.69 | 1px solid rgba(13, 20, 0, 0.1) | 8px | #ffffff `base.color.neutral..white` | none | 16px 16px 16px 44px |
| [Filter chip](#filter-chip) | 317 x 50 | - | 12px | #0d1400 `color.scheme.1..accent` | none | 0 |
| [Footer](#footer) | 1440 x 1102 | - | - | #ffffff `base.color.neutral..white` | none | 48px |

## Components

### Shell and navigation

The nav bar: wordmark, Mockup Library / Figma plugin / Signup links.

#### Header
The top nav: wordmark, Mockup Library and Figma plugin links, Signup. Read as `header` on the home page.

**Values (default).** size 1440 x 106; background transparent; text system-ui 18/27 700, #0d1400 `color.scheme.1..accent`.

Child layers that carry the look: div 40x40 background #aaff00 `mg.gree` border 1px solid #dfff9f radius 8px; nav 0x0 background #ffffff `base.color.neutral..white` radius 12px.

![Header default](components/crops/header-default.png)

#### Logo
Read as `logo` on the home page.

**Values (default).** size 179.31 x 40; background transparent; text system-ui 18/27 700, #0d1400 `color.scheme.1..accent`.

Child layers that carry the look: div 40x40 background #aaff00 `mg.gree` border 1px solid #dfff9f radius 8px.

![Logo default](components/crops/logo-default.png)

#### Nav link
A .button.is-link nav item. Measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 112.95 x 42; padding 4px 0px; radius 8px; background transparent; text system-ui 16/16 400, #0d1400 `color.scheme.1..accent` |
| hover | text system-ui 16/16 400, #aaaaaa |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | text system-ui 16/16 400, #aaaaaa |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Signup link
The signup nav action. Measured, never followed. Read as `nav-signup` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 50.47 x 42; padding 4px 0px; radius 8px; background transparent; text system-ui 16/16 400, #0d1400 `color.scheme.1..accent` |
| hover | text system-ui 16/16 400, #aaaaaa |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | text system-ui 16/16 400, #aaaaaa |

![Signup link default](components/crops/nav-signup-default.png) ![Signup link hover](components/crops/nav-signup-hover.png) ![Signup link focus-visible](components/crops/nav-signup-focus-visible.png) ![Signup link pressed](components/crops/nav-signup-pressed.png)

#### Version card
The New version / Legacy version picker card. Read as `version-card` on the home page.

Not on the page when it was captured.

### Home

The landing: hero, mockup-category tabs and the tile grids.

#### Hero title
Read as `hero-title` on the home page.

**Values (default).** size 768 x 145.91; background transparent; text Vend Sans 60.8/72.96 700, #0d1400 `color.scheme.1..accent`.

![Hero title default](components/crops/hero-title-default.png)

#### Category tab
A mockup-category tab (Most Popular is the selected one). Read as `tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 200.27 x 50; padding 12px 24px; border 1px solid rgba(13, 20, 0, 0.1); radius 8px; background #0d1400 `color.scheme.1..accent`; text system-ui 16/24 400, #ffffff `base.color.neutral..white` |

![Category tab default](components/crops/tab-default.png) ![Category tab hover](components/crops/tab-hover.png) ![Category tab focus-visible](components/crops/tab-focus-visible.png) ![Category tab pressed](components/crops/tab-pressed.png)

#### Tab, selected
Read as `tab-selected` on the home page.

**Values (default).** size 200.27 x 50; padding 12px 24px; border 1px solid rgba(13, 20, 0, 0.1); radius 8px; background #0d1400 `color.scheme.1..accent`; text system-ui 16/24 400, #ffffff `base.color.neutral..white`.

![Tab, selected default](components/crops/tab-selected-default.png)

#### Tab, switched
A tab after its own toggle; the selection moves locally. Read as `tab-switched` on the home page.

**Values (selected).** size 200.27 x 50; padding 12px 24px; border 1px solid rgba(13, 20, 0, 0.1); radius 8px; background #ffffff `base.color.neutral..white`; text system-ui 16/24 400, #0d1400 `color.scheme.1..accent`.

![Tab, switched selected](components/crops/tab-switched-selected.png)

#### Section heading
Read as `section-title` on the home page.

**Values (default).** size 154.73 x 23.03; padding 0px 0px 0px 12px; background transparent; text Vend Sans 19.2/23.04 600, #0d1400 `color.scheme.1..accent`.

![Section heading default](components/crops/section-title-default.png)

#### Mockup card
A mockup preview tile link. Read as `mockup-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 199.27 x 199.27; border 1px solid rgba(13, 20, 0, 0.1); radius 8px; background transparent; text system-ui 16/24 400, #0d1400 `color.scheme.1..accent` |

![Mockup card default](components/crops/mockup-card-default.png) ![Mockup card hover](components/crops/mockup-card-hover.png)

#### Plugin CTA
The "Install Figma plugin" icon action. Measured, never followed. Read as `plugin-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 229.58 x 42; padding 8px 19.2px; border 1px solid #0d1400 `color.scheme.1..accent`; radius 8px; background #0d1400 `color.scheme.1..accent`; text system-ui 16/24 400, #ffffff `base.color.neutral..white`; icon 13 x 20, #ffffff `base.color.neutral..white` |
| hover | background #222222 |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #222222 |

![Plugin CTA default](components/crops/plugin-cta-default.png) ![Plugin CTA hover](components/crops/plugin-cta-hover.png) ![Plugin CTA focus-visible](components/crops/plugin-cta-focus-visible.png) ![Plugin CTA pressed](components/crops/plugin-cta-pressed.png)

#### Contact CTA
The Contact icon action. Measured, never followed. Read as `contact-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 133.5 x 42; padding 8px 19.2px; border 1px solid #0d1400 `color.scheme.1..accent`; radius 8px; background #0d1400 `color.scheme.1..accent`; text system-ui 16/24 400, #ffffff `base.color.neutral..white`; icon 20 x 20, #ffffff `base.color.neutral..white` |
| hover | background #222222 |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #222222 |

![Contact CTA default](components/crops/contact-cta-default.png) ![Contact CTA hover](components/crops/contact-cta-hover.png) ![Contact CTA focus-visible](components/crops/contact-cta-focus-visible.png) ![Contact CTA pressed](components/crops/contact-cta-pressed.png)

### Mockup library

The /mockup library pane: search field, filter chips and thumbnail cards in an inner scroller.

#### Library title
Read as `lib-title` on the mockup library page.

**Values (default).** size 852.94 x 67.19; background transparent; text Vend Sans 56/67.2 700, #0d1400 `color.scheme.1..accent`.

![Library title default](components/crops/lib-title-default.png)

#### Library search field
Focused only; nothing typed or sent. Read as `search-field` on the mockup library page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 1005 x 64.69; padding 16px 16px 16px 44px; border 1px solid rgba(13, 20, 0, 0.1); radius 8px; background #ffffff `base.color.neutral..white`; text system-ui 19.2/30.72 400, #0d1400 `color.scheme.1..accent`; placeholder rgba(0, 0, 0, 0.6) |

![Library search field default](components/crops/search-field-default.png) ![Library search field focused](components/crops/search-field-focused.png)

#### Filter chip
A category filter on the library. Measured, never selected. Read as `filter-chip` on the mockup library page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 317 x 50; radius 12px; background #0d1400 `color.scheme.1..accent`; text Vend Sans 16/24 400, #ffffff `base.color.neutral..white` |
| hover | background #222222 |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #222222 |

![Filter chip default](components/crops/filter-chip-default.png) ![Filter chip hover](components/crops/filter-chip-hover.png) ![Filter chip focus-visible](components/crops/filter-chip-focus-visible.png) ![Filter chip pressed](components/crops/filter-chip-pressed.png)

#### Library card
A mockup thumbnail tile. Read as `lib-card` on the mockup library page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 317 x 50; radius 12px; background transparent; text system-ui 16/24 400, #0d1400 `color.scheme.1..accent` |
| hover | background #f4f3f2 |

Child layers that carry the look: div 317x50 border 1px solid transparent radius 12px; div 40x40 background #ffffff `base.color.neutral..white` border 1px solid rgba(13, 20, 0, 0.1) radius 8px.

![Library card default](components/crops/lib-card-default.png) ![Library card hover](components/crops/lib-card-hover.png)

### Figma plugin page

The Figma-plugin page's title and install action.

#### Figma page title
Read as `figma-title` on the figma plugin page page.

**Values (default).** size 768 x 145.91; background transparent; text Vend Sans 60.8/72.96 700, #0d1400 `color.scheme.1..accent`.

![Figma page title default](components/crops/figma-title-default.png)

#### Figma install CTA
The page primary action. Measured, never followed. Read as `figma-cta` on the figma plugin page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 206.45 x 42; padding 8px 19.2px; border 1px solid #0d1400 `color.scheme.1..accent`; radius 8px; background #0d1400 `color.scheme.1..accent`; text system-ui 16/24 400, #ffffff `base.color.neutral..white`; icon 20 x 20, #ffffff `base.color.neutral..white` |
| hover | background #222222 |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #222222 |

![Figma install CTA default](components/crops/figma-cta-default.png) ![Figma install CTA hover](components/crops/figma-cta-hover.png) ![Figma install CTA focus-visible](components/crops/figma-cta-focus-visible.png) ![Figma install CTA pressed](components/crops/figma-cta-pressed.png)

### Footer

The link columns, headings and legal.

#### Footer
Read as `footer` on the home page.

**Values (default).** size 1440 x 1102; padding 48px; background #ffffff `base.color.neutral..white`; text system-ui 18/27 700, #0d1400 `color.scheme.1..accent`; icon 24 x 24, #0d1400 `color.scheme.1..accent`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 112.95 x 42; padding 4px 0px; radius 8px; background transparent; text system-ui 16/16 400, #0d1400 `color.scheme.1..accent` |
| hover | text system-ui 16/16 400, #aaaaaa |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | text system-ui 16/16 400, #aaaaaa |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Mobile (390 wide)

The same surface at phone width, with the menu open.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 88; background transparent; text system-ui 18/27 700, #0d1400 `color.scheme.1..accent`.

Child layers that carry the look: div 0x0 background #aaff00 `mg.gree` border 1px solid #dfff9f radius 8px; ul 0x0 background #ffffff `base.color.neutral..white`; nav 0x0 background #ffffff `base.color.neutral..white` radius 12px.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 48 x 48; padding 12px; background transparent; text system-ui 24/36 400, #0d1400 `color.scheme.1..accent` |
| focus-visible | outline 2px solid #4d65ff, offset 2px |

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button hover](components/crops/m-menu-button-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The bar after its own toggle; the crop is the opened nav panel. Read as `m-menu-open` on the home page at 390 wide.

**Values (opened).** size 48 x 48; padding 12px; background #a6b1bf; text system-ui 24/36 400, #ffffff `base.color.neutral..white`.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav link
Read inside the open menu. Read as `m-nav-link` on the home page at 390 wide.

**Values (default).** size 112.95 x 42; padding 4px 0px; radius 8px; background transparent; text system-ui 16/16 400, #0d1400 `color.scheme.1..accent`.

![Mobile nav link default](components/crops/m-nav-link-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Artboard Studio's artwork. Declared under layoutGaps in the catalog entry.

## Gaps

### Pages

- **Anything that sends, submits or signs in.** No form was submitted, no prompt was sent, no account was created. `search-field` was focused only; nothing was typed into it.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface. The library and category grids scroll inside an inner .container-category-pages pane, so document-level full-page captures only show the first viewport; the scrolled frames are kept as separate shots.

### Themes

The site paints one light theme on every captured route: no dark class or attribute is bound, so the dark set is not emitted. The Relume/Webflow palette is recorded in [raw/css-vars.json](raw/css-vars.json).

### Fonts

- **The face** is Vend Sans on headings (300-700 from Google Fonts); body and controls paint with a generic sans stack. The style guide renders with system fallbacks.
- Mockup imagery and the Artboard Studio mark in the screenshots are Artboard Studio's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The changelog page is 91,833 px tall; its -full shot is the whole page stitched from 7 tiles.

### Content left out

- Mockup photography and the wordmark are Artboard Studio's content; only the frames and components were measured.
