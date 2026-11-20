# Visual (designstripe) components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from visual.app (the catalog's designstripe.com redirects here — 'Visual, formerly designstripe') on 2026-11-14, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted and no form was ever sent; the WAITLIST buttons, nav links, category tiles, tool cards and article links were measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (34 components, 78 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (68 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: every public surface paints `light` (the dark resolution is declared but never shown signed out). Desktop shots are 1440 x 900 at 1x; `-full` pages scroll inside a nested container rather than the document, so they are captured as viewport-tall `partN` tiles and capped at 8 tiles (an inner-scroller boundary recorded in the capture log); mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Asset library | `/assets` | [default](screenshots/assets-light-default.png), [full](screenshots/assets-light-full.png) |
| Avatar set | `/assets/avatars/replicants` | [default](screenshots/avatars-light-default.png), [full](screenshots/avatars-light-full.png) |
| Design tools | `/tools` | [default](screenshots/tools-light-default.png), [full](screenshots/tools-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Contact | `/contact` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Blog article | `/blog/branding-consistency` | [default](screenshots/post-light-default.png), [full](screenshots/post-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Asset library, phone | `/assets` | [default](screenshots/mobile-assets-light-default.png), [full](screenshots/mobile-assets-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Feature accordion | / | a local disclosure toggle — the second row was opened in place | [feature-acc](#feature-accordion), [feature-acc2](#accordion-closed) |
| Waitlist CTA | every surface | the nav WAITLIST button's hover/focus/pressed states; it was never pressed — it opens the waitlist flow | [waitlist-btn](#waitlist-cta) |
| The product app | a Visual account | the design agents themselves, asset downloads inside an account and every post-waitlist surface | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 13 components were given a real keyboard focus. 13 draw an outline ring: `nav-link` (1px auto #101010 `border.focus`, offset 1px), `waitlist-btn` (1px solid #ffffff `background.page`, offset -1px), `feature-acc` (1px auto #101010 `border.focus`, offset 0px), `ast-tile-hero` (1px auto #101010 `border.focus`, offset 1px), `ast-tile` (1px auto #101010 `border.focus`, offset 1px), `ast-kind-link` (1px auto #101010 `border.focus`, offset 1px), `av-back` (1px auto #101010 `border.focus`, offset 1px), `av-item` (1px auto #101010 `border.focus`, offset 1px), `tool-card` (1px auto #101010 `border.focus`, offset 1px), `tool-card2` (1px auto #101010 `border.focus`, offset 1px), `post-link` (1px auto #101010 `border.focus`, offset 1px), `m-acc` (1px auto #e59700, offset 0px), `av-kind` (1px auto #101010 `border.focus`, offset 1px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | feature-acc, feature-acc2, m-acc, mkt-logo, waitlist-btn |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | av-back, nav-link |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|

## Components

### Header and navigation

The fixed top bar on every surface: the VISUAL wordmark, mono section links and the cream WAITLIST pill.

#### Site nav
The fixed top nav: VISUAL wordmark, section links (WHY VISUAL? / ASSETS / TOOLS / BLOG) and the WAITLIST button. Read as `mkt-nav` on the assets page.

**Values (default).** size 1440 x 32; padding 0px 32px; background transparent; text fontMono 12/12 500, #ffffff `background.page`; icon 20 x 20, #ffffff `background.page`; layers a.ui:inline-flex.ui:items-center 88.0x32.0 #2c2c26 `background.ink` 4px; ul.items-center.ml-auto 256.0x32.0 #ffffff `background.page` T:1px solid rgb(208, 208, 200) / R:1px solid rgb(208, 208, 200) / B:1px solid rgb(208, 208, 200) / L:1px solid rgb(208, 208, 200) 4px; a.whitespace-nowrap.flex 93.0x24.0 #ffffff `background.page` 3px; a.whitespace-nowrap.flex 58.0x24.0 #ffffff `background.page` 3px;.

Child layers that carry the look: a 88x32 background #2c2c26 `background.ink` radius 4px; ul 256x32 background #ffffff `background.page` border 1px solid #d0d0c8 `border.hairline` radius 4px; a 93x24 background #ffffff `background.page` radius 3px.

![Site nav default](components/crops/mkt-nav-default.png)

#### Logo
The VISUAL wordmark at the left of the nav. Read as `mkt-logo` on the assets page.

**Values (default).** size 88 x 32; padding 0px 12px; radius 4px; background #2c2c26 `background.ink`; text fontMono 12/12 500, #ffffff `background.page`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #ffffff `background.page`.

![Logo default](components/crops/mkt-logo-default.png)

#### Nav link
A section link in the top nav ("WHY VISUAL?"); measured, never followed. Read as `nav-link` on the assets page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 93 x 24; padding 0px 8px; radius 3px; background #ffffff `background.page`; text fontMono 12/12 500, #000000 `text.black`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f6f6f4 `background.hover-fill` |
| focus-visible | outline 1px auto #101010 `border.focus`, offset 1px |
| pressed | background #f6f6f4 `background.hover-fill` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Waitlist CTA
The nav WAITLIST button — the product’s only conversion CTA on this surface; measured, never pressed (it joins a waitlist). Read as `waitlist-btn` on the assets page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 82 x 32; padding 0px 12px; border 1px solid #aaa674 `border.olive`; radius 3.35544e+07px; background #e8e7d9 `background.cream`; text fontMono 12/12 500, #2c2c26 `background.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #414238 `color.neutral.900` |
| focus-visible | shadow #2c2c26 0px 0px 0px 2px; outline 1px solid #ffffff `background.page`, offset -1px |
| pressed | background #414238 `color.neutral.900` |

![Waitlist CTA default](components/crops/waitlist-btn-default.png) ![Waitlist CTA hover](components/crops/waitlist-btn-hover.png) ![Waitlist CTA focus-visible](components/crops/waitlist-btn-focus-visible.png) ![Waitlist CTA pressed](components/crops/waitlist-btn-pressed.png)

### Home

The home hero: the 96px fontSerif display, the dark feature panel with its monospace accordion rows, the serif section headings and the ink footer.

#### Hero headline
"Design Agents for Revenue Teams" — the serif display heading. Read as `hero-h1` on the home page.

**Values (default).** size 708 x 180; background transparent; text fontSerif 96/90 400, #000000 `text.black`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Hero subcopy
The supporting paragraph under the hero heading. Read as `hero-sub` on the home page.

**Values (default).** size 640 x 39.56; background transparent; text fontMono 14/19.79 500, #6d6e5e `color.neutral.700`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Feature accordion
A monospace feature accordion row on the dark panel ("Chat-driven for everyone on the team"); its opened state is the already-expanded first row, measured as painted. Read as `feature-acc` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed, opened) | size 568.66 x 60.27; padding 16px 0px 16px 32px; background transparent; text fontMono 20/28.28 500, #ffffff `background.page`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #aaab9c `color.neutral.400`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 1px auto #101010 `border.focus`, offset 0px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.ui:flex.ui:flex-1 568.7x60.3 1px auto rgb(16, 16, 16) offset 0px |

![Feature accordion focus-visible](components/crops/feature-acc-focus-visible.png) ![Feature accordion pressed](components/crops/feature-acc-pressed.png) ![Feature accordion opened](components/crops/feature-acc-opened.png)

#### Section heading
A serif section heading ("Keep every slide on-brand"). Read as `sec-h2` on the home page.

**Values (default).** size 312.39 x 96; background transparent; text fontSerif 48/48 300, #000000 `text.black`.

![Section heading default](components/crops/sec-h2-default.png)

#### Dark-panel heading
The white serif heading inside the dark feature panel ("Every agent is an endpoint"). Read as `dark-h2` on the home page.

**Values (default).** size 312.39 x 96; background transparent; text fontSerif 48/48 300, #ffffff `background.page`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Accordion (closed)
The closed "Quickly personalize every presentation" accordion row; its opened state is toggled locally to reveal the panel copy. Read as `feature-acc2` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 568.66 x 60.27; padding 16px 0px 16px 32px; background transparent; text fontMono 20/28.28 500, #ffffff `background.page`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #aaab9c `color.neutral.400`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |

![Accordion (closed) default](components/crops/feature-acc2-default.png) ![Accordion (closed) opened](components/crops/feature-acc2-opened.png)

### Asset library

The /assets grid: the 96px serif Asset Library heading, the featured and standard aspect-square category tiles and the kind links.

#### Library heading
"Asset Library" — the 96px serif page heading in the olive ink. Read as `ast-h1` on the assets page.

**Values (default).** size 684 x 96; background transparent; text fontSerif 96/96 400, #2c2c26 `background.ink`.

![Library heading default](components/crops/ast-h1-default.png)

#### Hero category tile
The featured category tile (569px rounded-xl square, "/ REPLICANTS" label over a preview); measured, never followed. Read as `ast-tile-hero` on the assets page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 568.66 x 568.66; radius 8px; background #ffffff `background.page`; image linear-gradient(45deg, #e3e3de `color.neutral.100` 25%, transparent 25%, transparent 75%, #e3e3de `color.neutral.100` 75%, #e3e3de `color.neutral.100`), linear-gradient(45deg, #e3e3de `color.neutral.1; text fontMono 10/10 500, #6d6e5e `color.neutral.700`; icon 16 x 16, #6d6e5e `color.neutral.700` |
| focus-visible | outline 1px auto #101010 `border.focus`, offset 1px |

![Hero category tile default](components/crops/ast-tile-hero-default.png) ![Hero category tile hover](components/crops/ast-tile-hero-hover.png) ![Hero category tile focus-visible](components/crops/ast-tile-hero-focus-visible.png) ![Hero category tile pressed](components/crops/ast-tile-hero-pressed.png)

#### Category tile
A standard category tile (280px rounded-xl square); measured, never followed. Read as `ast-tile` on the assets page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 280.33 x 280.33; radius 8px; background #ffffff `background.page`; image linear-gradient(45deg, #e3e3de `color.neutral.100` 25%, transparent 25%, transparent 75%, #e3e3de `color.neutral.100` 75%, #e3e3de `color.neutral.100`), linear-gradient(45deg, #e3e3de `color.neutral.1; text fontMono 10/10 500, #6d6e5e `color.neutral.700`; icon 16 x 16, #6d6e5e `color.neutral.700` |
| focus-visible | outline 1px auto #101010 `border.focus`, offset 1px |

![Category tile default](components/crops/ast-tile-default.png) ![Category tile hover](components/crops/ast-tile-hover.png) ![Category tile focus-visible](components/crops/ast-tile-focus-visible.png) ![Category tile pressed](components/crops/ast-tile-pressed.png)

#### Tile preview
A category tile’s preview image (object-cover inside the rounded square). Read as `ast-tile-img` on the assets page.

**Values (default).** size 568.66 x 568.66; background transparent; text fontMono 16/24 400, #000000 `text.black`.

![Tile preview default](components/crops/ast-tile-img-default.png)

#### Kind link
A library kind link ("Illustrations" / "Avatars") that sections the grid; measured, never followed. Read as `ast-kind-link` on the assets page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 84 x 22; background transparent; text fontMono 20/28.28 500, #2c2c26 `background.ink` |
| focus-visible | outline 1px auto #101010 `border.focus`, offset 1px; layers a.text-primary 84.0x22.0 1px auto rgb(16, 16, 16) offset 1px |

![Kind link default](components/crops/ast-kind-link-default.png) ![Kind link hover](components/crops/ast-kind-link-hover.png) ![Kind link focus-visible](components/crops/ast-kind-link-focus-visible.png) ![Kind link pressed](components/crops/ast-kind-link-pressed.png)

### Avatar set gallery

A /assets/avatars/<set> gallery: the serif set heading, the avatar grid items and the kind crumb.

#### Set heading
The avatar-set page heading. Read as `av-h1` on the avatars page.

**Values (default).** size 684 x 96; background transparent; text fontSerif 96/96 400, #2c2c26 `background.ink`.

![Set heading default](components/crops/av-h1-default.png)

#### Back link
The link back to the asset library; measured, never followed. Read as `av-back` on the avatars page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 58 x 24; padding 0px 8px; radius 3px; background #ffffff `background.page`; text fontMono 12/12 500, #000000 `text.black`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f6f6f4 `background.hover-fill` |
| focus-visible | outline 1px auto #101010 `border.focus`, offset 1px |
| pressed | background #f6f6f4 `background.hover-fill` |

![Back link default](components/crops/av-back-default.png) ![Back link hover](components/crops/av-back-hover.png) ![Back link focus-visible](components/crops/av-back-focus-visible.png) ![Back link pressed](components/crops/av-back-pressed.png)

#### Avatar item
An avatar tile in the set grid (links to its detail page); measured, never followed. Read as `av-item` on the avatars page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 222.66 x 222.66; radius 8px; background #ffffff `background.page`; image linear-gradient(45deg, #e3e3de `color.neutral.100` 25%, transparent 25%, transparent 75%, #e3e3de `color.neutral.100` 75%, #e3e3de `color.neutral.100`), linear-gradient(45deg, #e3e3de `color.neutral.1; text fontMono 16/24 400, #000000 `text.black` |
| focus-visible | outline 1px auto #101010 `border.focus`, offset 1px |

![Avatar item default](components/crops/av-item-default.png) ![Avatar item hover](components/crops/av-item-hover.png) ![Avatar item focus-visible](components/crops/av-item-focus-visible.png) ![Avatar item pressed](components/crops/av-item-pressed.png)

#### Avatar image
An avatar preview image in the set grid. Read as `av-thumb` on the avatars page.

**Values (default).** size 222.66 x 222.66; background transparent; text fontMono 16/24 400, #000000 `text.black`.

![Avatar image default](components/crops/av-thumb-default.png)

#### Kind crumb
The AVATARS kind crumb over the set grid; measured, never followed. Read as `av-kind` on the avatars page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 49 x 12; background transparent; text fontMono 12/12 500, #6d6e5e `color.neutral.700` |
| hover | text fontMono 12/12 500, #2c2c26 `background.ink` |
| focus-visible | outline 1px auto #101010 `border.focus`, offset 1px; layers a.ui:text-neutral-700.ui:hover:text-foreground 49.0x12.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text fontMono 12/12 500, #2c2c26 `background.ink` |

![Kind crumb default](components/crops/av-kind-default.png) ![Kind crumb hover](components/crops/av-kind-hover.png) ![Kind crumb focus-visible](components/crops/av-kind-focus-visible.png) ![Kind crumb pressed](components/crops/av-kind-pressed.png)

### Design tools

The /tools grid: the 96px serif Design Tools heading and the bordered white tool cards with their mono crumbs.

#### Tools heading
"Design Tools" — the 96px serif page heading. Read as `tool-h1` on the tools page.

**Values (default).** size 684 x 96; background transparent; text fontSerif 96/96 400, #2c2c26 `background.ink`.

![Tools heading default](components/crops/tool-h1-default.png)

#### Tool card
A tool card ("Color Wheel" — bordered white card with a breadcrumb label, title and copy); measured, never followed. Read as `tool-card` on the tools page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 338 x 422.5; padding 24px 24px 20px 24px; border 1px solid #d0d0c8 `border.hairline`; radius 6px; background #ffffff `background.page`; text fontMono 12/12 500, #6d6e5e `color.neutral.700` |
| focus-visible | outline 1px auto #101010 `border.focus`, offset 1px |

![Tool card default](components/crops/tool-card-default.png) ![Tool card hover](components/crops/tool-card-hover.png)

#### Tool card 2
A second tool card ("Image Resizer"), sampled for consistency. Read as `tool-card2` on the tools page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 338 x 422.5; padding 24px 24px 20px 24px; border 1px solid #d0d0c8 `border.hairline`; radius 6px; background #ffffff `background.page`; text fontMono 12/12 500, #6d6e5e `color.neutral.700` |
| focus-visible | outline 1px auto #101010 `border.focus`, offset 1px |

![Tool card 2 default](components/crops/tool-card2-default.png) ![Tool card 2 hover](components/crops/tool-card2-hover.png) ![Tool card 2 focus-visible](components/crops/tool-card2-focus-visible.png)

#### Card breadcrumb
The "colors" kind crumb on a tool card (paired with its "Tools" label). Read as `tool-crumb` on the tools page.

**Values (default).** size 288 x 12; background transparent; text fontMono 12/12 500, #000000 `text.black`.

![Card breadcrumb default](components/crops/tool-crumb-default.png)

### Contact

The /contact page: the 96px serif heading and mono contact copy — no form exists on this surface.

#### Contact heading
"Contact" — the 96px serif page heading. Read as `ct-h1` on the contact page.

**Values (default).** size 684 x 96; background transparent; text fontSerif 96/96 400, #2c2c26 `background.ink`.

![Contact heading default](components/crops/ct-h1-default.png)

#### Contact copy
The supporting paragraph on the contact page. Read as `ct-copy` on the contact page.

**Values (default).** size 453.33 x 39.56; background transparent; text fontMono 14/19.79 500, #6d6e5e `color.neutral.700`.

![Contact copy default](components/crops/ct-copy-default.png)

### Blog article

A /blog article: the 64px serif title, mono body copy and olive-gold inline links.

#### Article heading
The article title heading. Read as `post-h1` on the post page.

**Values (default).** size 914.67 x 128; background transparent; text fontSerif 64/64 400, #2c2c26 `background.ink`.

![Article heading default](components/crops/post-h1-default.png)

#### Article paragraph
A body paragraph in the article. Read as `post-para` on the post page.

**Values (default).** size 453.33 x 19.78; background transparent; text fontMono 14/19.79 500, #6d6e5e `color.neutral.700`.

![Article paragraph default](components/crops/post-para-default.png)

#### Article link
An inline link inside the article body; measured, never followed. Read as `post-link` on the post page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 36.63 x 25; background transparent; text fontSerif 20/30 400, #7e7b4e `color.green.700` |
| focus-visible | outline 1px auto #101010 `border.focus`, offset 1px; layers a 36.6x25.0 1px auto rgb(16, 16, 16) offset 1px |

![Article link default](components/crops/post-link-default.png) ![Article link hover](components/crops/post-link-hover.png) ![Article link focus-visible](components/crops/post-link-focus-visible.png) ![Article link pressed](components/crops/post-link-pressed.png)

### Mobile (390 wide)

The phone surface at 390 wide: the 40px top bar, serif hero and accordion rows.

#### Mobile nav
The phone top bar: VISUAL wordmark and the WAITLIST button. Read as `m-nav` on the home page at 390 wide.

**Values (default).** size 390 x 40; padding 0px 16px; background transparent; text fontMono 12/12 500, #ffffff `background.page`; icon 20 x 20, #ffffff `background.page`; layers a.ui:inline-flex.ui:items-center 88.0x32.0 #2c2c26 `background.ink` 4px; a.whitespace-nowrap.flex 0.0x0.0 #ffffff `background.page` 3px; a.whitespace-nowrap.flex 0.0x0.0 #ffffff `background.page` 3px; a.whitespace-nowrap.flex 0.0x0.0 #ffffff `background.page` 3px; a.whitespace-nowrap.flex 0.0x0.0 #ffffff `background.page` 3px; button.ui:justify-center.ui:whitespace-nowrap 50.0x40.0 #ffffff `backgr.

Child layers that carry the look: a 88x32 background #2c2c26 `background.ink` radius 4px; a 0x0 background #ffffff `background.page` radius 3px; a 0x0 background #ffffff `background.page` radius 3px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile headline
The phone hero heading. Read as `m-h1` on the home page at 390 wide.

**Values (default).** size 374 x 90; background transparent; text fontSerif 48/45 400, #000000 `text.black`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile accordion
A feature accordion row on the phone; measured, never toggled here. Read as `m-acc` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 350 x 64; padding 16px 0px 16px 32px; background transparent; text fontMono 16/16 500, #ffffff `background.page`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #aaab9c `color.neutral.400`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 1px auto #e59700, offset 0px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.ui:flex.ui:flex-1 350.0x64.0 1px auto rgb(229, 151, 0) offset 0px |

![Mobile accordion hover](components/crops/m-acc-hover.png) ![Mobile accordion focus-visible](components/crops/m-acc-focus-visible.png) ![Mobile accordion pressed](components/crops/m-acc-pressed.png)

#### Mobile footer
The phone footer. Read as `m-footer` on the home page at 390 wide.

**Values (default).** size 390 x 316; padding 32px 16px; background #2c2c26 `background.ink`; text fontMono 12/12 500, #ffffff `background.page`.

![Mobile footer default](components/crops/m-footer-default.png)

### Footer

The olive-ink dark footer on every surface.

#### Site footer
The sitemap footer (BLOG / ASSET LIBRARY / DESIGN TOOLS / ABOUT / CONTACT / LINKEDIN). Read as `site-footer` on the home page.

**Values (default).** size 1440 x 320; padding 32px 24px; background #2c2c26 `background.ink`; text fontMono 12/12 500, #ffffff `background.page`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the VISUAL mark, tile badges, tool previews and avatar art) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The design agents themselves, asset downloads inside an account and every post-waitlist surface need an account and were never reached. What is genuinely public signed out: the marketing home, the /assets library and /assets/<kind>/<set> galleries (CC0 assets — tiles link to detail pages, never followed), /tools, /about, /contact and /blog articles. The WAITLIST buttons open the waitlist flow and were measured, never pressed.

### Pages

- **Waitlist.** The WAITLIST buttons open the waitlist flow; they were measured at default/hover/focus-visible/pressed, never pressed — no waitlist form exists in this capture.
- **Follow actions.** Nav links, category tiles, tool cards and article links were measured, never followed — tile detail pages and external destinations sit outside this pass.
- **designstripe.com redirects to visual.app** ('Visual, formerly designstripe'); the catalog keeps the product's listed domain and the package captures the redirect's destination.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

Every public surface paints the light theme signed out. The stylesheet genuinely declares both themes (96 resolved variables each over :root and a real .dark block — the dark surface is reachable in the app behind an account or preference), so tokens.json keeps real light and dark sets even though the dark values are declared, not painted.

### Fonts

- **fontSerif** (display headings, article links), **fontMono** (nav, crumbs, controls, body) and **fontSans** (declared @font-face, tools surfaces) are the served faces. They are served from Visual's CDN; the style guide falls back to system fonts.

### Screenshots

- Long pages scroll inside a nested container, not the document, so full-page shots are viewport-tall `partN` tiles capped at 8 tiles — the inner-scroller cap is a real capture boundary (home is ~8.7k px tall on mobile).
- Blog and mobile full-page shots hit screenshot timeouts on first pass and were retried with a 120s ceiling; no route stayed blocked.
- Asset art, avatar portraits and tool previews are the product's published content; screenshots are 256-colour PNGs, read exact colours from the tokens or the raw files.

### Content left out

- Expert names, quotes, bios and portraits are the product's content; only frames and components were measured.
