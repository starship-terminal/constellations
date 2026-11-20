# DailyArt Magazine components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from dailyartmagazine.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or downloaded; the hamburger category menu and the self-mounting newsletter modal are local UI toggles, and hover/focus/pressed states were forced. Article cards, menu items and the Shop/Courses outbound links were measured, never followed; the newsletter and Contact Form 7 fields were typed into and cleared, never submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (71 components, 151 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (147 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every page paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at CSS scale (one CSS pixel per image pixel — mobile fulls are 390 wide); mobile viewport shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Latest | `/latest/` | [default](screenshots/latest-light-default.png), [full](screenshots/latest-light-full.png) |
| Impressionism category | `/category/art-movements/impressionism/` | [default](screenshots/category-light-default.png), [full](screenshots/category-light-full.png) |
| Article | `/10-japanese-woodblock-prints-you-need-to-see/` | [default](screenshots/article-light-default.png), [full](screenshots/article-light-full.png) |
| About | `/about-dailyart-magazine/` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Contact | `/contact/` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Search | `/?s=van+gogh` | [default](screenshots/search-light-default.png), [full](screenshots/search-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Article, phone | `/10-japanese-woodblock-prints-you-need-to-see/` | [default](screenshots/mobile-article-light-default.png), [full](screenshots/mobile-article-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Art Movements mega-menu | every page | the hamburger trigger, clicked locally | [cat-nav](#cat-nav) opened state + [home-light-menu](screenshots/home-light-menu.png) |
| Newsletter modal | every page | the site's own .modal-r--show open class | [nl-modal](#nl-modal) |
| Mobile menu | home, phone width | the mobile hamburger | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |
| Shop / Courses / social | the nav and footer | the outbound links were measured, never followed | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 18 components were given a real keyboard focus. 15 draw an outline ring: `nav-link` (1px dotted #ffffff `light.background.page`, offset 1px), `nav-outbound` (1px dotted #ffffff `light.background.page`, offset 1px), `cat-nav-item` (1px dotted #000000 `light.text.ink`, offset 1px), `browse-link` (1px dotted #c6002f `light.action.accent`, offset 1px), `post-card-title` (1px dotted #000000 `light.text.ink`, offset 1px), `post-card-cat` (1px dotted #ffffff `light.background.page`, offset 1px), `post-card-author` (1px dotted #f3003a `light.action.link-bright`, offset 1px), `footer-link` (1px dotted #c6002f `light.action.accent`, offset 1px), `social-link` (1px dotted #0000ee, offset 1px), `latest-link` (1px dotted #000000 `light.text.ink`, offset 1px), `cat-card-title` (1px dotted #000000 `light.text.ink`, offset 1px), `art-cat` (1px dotted #c6002f `light.action.accent`, offset 1px), `art-inline-link` (1px dotted #f3003a `light.action.link-bright`, offset 1px), `share-btn` (1px dotted #0000ee, offset 1px), `art-tag` (1px dotted #ffffff `light.background.page`, offset 1px). The other 3 show no measured change: `search-btn`, `load-more`, `nl-send`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.3s | `ease` | all | cat-nav-item, cat-nav-sub, cf7-email, cf7-message, cf7-name, cf7-send, load-more, m-nl-email and more |
| 0.3s | `ease-in` | all | share-btn |
| 0.5s | `ease` | all | browse-link, nav-bar |
| 0.5s | `ease-in-out` | all | hamburger, m-hamburger |
| 1s | `ease` | all | cat-nav |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Hero card](#hero-card) | 275.5 x 292.75 | B: 1px solid #2e2e32 `light.border.hairline-dark` | - | transparent | none | 0px 0px 20px 0px |
| [Post card (horizontal)](#post-card-horizontal) | 760 x 194 | B: 1px solid #ebeced | - | transparent | none | 0px 0px 16px 0px |
| [Post card (vertical)](#post-card-vertical) | 275.5 x 292.75 | B: 1px solid #2e2e32 `light.border.hairline-dark` | - | transparent | none | 0px 0px 20px 0px |
| [Archive card](#archive-card) | 760 x 194 | B: 1px solid #ebeced | - | transparent | none | 0px 0px 16px 0px |
| [Related card](#related-card) | 337 x 107 | B: 1px solid #ebeced | - | transparent | none | 12px 0px 16px 0px |
| [Result card](#result-card) | 760 x 194 | B: 1px solid #ebeced | - | transparent | none | 0px 0px 16px 0px |
| [Donation block](#donation-block) | 760 x 385.56 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The 65px fixed dark nav shared by every page: the 111px wordmark, 14px white Basier links (Stories, and the outbound Shop/Courses), the hamburger that opens the 1440x633 white Art-Movements mega-menu, the 87x38 ghost Search button — plus the newsletter form, the slide-down newsletter modal and the link-column footer.

#### Top header
The full-width top bar over the dark hero: hamburger, Stories/Shop/Courses, wordmark, social icons and the Search button. Read as `nav-bar` on the home page.

**Values (default).** size 1440 x 65; background #19191c `light.background.dark-band`; text Basier 14/17 600, #ffffff `light.background.page`; transition all 0.5s ease.

![Top header default](components/crops/nav-bar-default.png)

#### Logo
The DailyArt Magazine wordmark (inline SVG). Read as `nav-logo` on the home page.

**Values (default).** size 111 x 30.17; background transparent; text Basier 16/16 400, #0000ee; transform translate(-55.5px, -15.0859px); icon 111 x 28.17, #0000ee; ancestors div.wrapper bg #19191c `light.background.dark-band`.

![Logo default](components/crops/nav-logo-default.png)

#### Nav link
"Stories" — a primary-nav item; measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 46.48 x 18; background transparent; text Basier 14/17 600, #ffffff `light.background.page`; layers ::after rgb(255, 255, 255) 0px none 1; a::after 0pxx2px rgb(255, 255, 255) |
| hover | layers ::after rgb(255, 255, 255) 0px none 1; a::after 45.9844pxx2px rgb(255, 255, 255) |
| focus-visible | outline 1px dotted #ffffff `light.background.page`, offset 1px; layers ::after rgb(255, 255, 255) 0px none 1; a 46.5x18.0 1px dotted rgb(255, 255, 255) offset 1px; a::after 0pxx2px rgb(255, 255, 255) |
| pressed | layers ::after rgb(255, 255, 255) 0px none 1; a::after 43.3281pxx2px rgb(255, 255, 255) |

Child layers that carry the look: a::after 0pxx2px background #ffffff `light.background.page`.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Outbound nav link
"Shop" — outbound to shop.dailyartmagazine.com; measured, never followed. Read as `nav-outbound` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 33.28 x 18; background transparent; text Basier 14/17 600, #ffffff `light.background.page`; layers ::after rgb(255, 255, 255) 0px none 1; a::after 0pxx2px rgb(255, 255, 255) |
| hover | layers ::after rgb(255, 255, 255) 0px none 1; a::after 32.9062pxx2px rgb(255, 255, 255) |
| focus-visible | outline 1px dotted #ffffff `light.background.page`, offset 1px; layers ::after rgb(255, 255, 255) 0px none 1; a 33.3x18.0 1px dotted rgb(255, 255, 255) offset 1px; a::after 0pxx2px rgb(255, 255, 255) |
| pressed | layers ::after rgb(255, 255, 255) 0px none 1; a::after 32.1875pxx2px rgb(255, 255, 255) |

Child layers that carry the look: a::after 0pxx2px background #ffffff `light.background.page`.

![Outbound nav link default](components/crops/nav-outbound-default.png) ![Outbound nav link hover](components/crops/nav-outbound-hover.png) ![Outbound nav link focus-visible](components/crops/nav-outbound-focus-visible.png) ![Outbound nav link pressed](components/crops/nav-outbound-pressed.png)

#### Hamburger
The six-bar hamburger that toggles the fixed-nav category menu. Read as `hamburger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 20 x 15; background transparent; text Basier 16/16 400, #4d5761 `light.text.muted`; transition all 0.5s ease-in-out; layers span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); ancestors div.ham-border bg #19191c `light.background.dark-band` |
| hover | ancestors div.ham-border bg #c6002f `light.action.accent` |

Child layers that carry the look: span 10x2 background #ffffff `light.background.page`; span 10x2 background #ffffff `light.background.page`; span 10x2 background #ffffff `light.background.page`.

![Hamburger default](components/crops/hamburger-default.png) ![Hamburger hover](components/crops/hamburger-hover.png) ![Hamburger pressed](components/crops/hamburger-pressed.png)

#### Category nav
The fixed-nav category menu (Art Movements tree) opened by the hamburger. Read as `cat-nav` on the home page.

**Values (opened).** size 1440 x 633; padding 20px; background #ffffff `light.background.page`; shadow rgba(0, 0, 0, 0.25) 0px 16px 48px 0px; text RoslindaleNarrow 16/18 600, #000000 `light.text.ink`; transition all 1s ease; transform translate(-720px, 0px); layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1; ancestors header bg #19191c `light.background.dark-band`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Category nav item
A top-level category link ("Art Movements") in the opened nav; measured, never followed. Read as `cat-nav-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 298.3 x 59; padding 20px 0px; border B: 1px solid #2e2e32 `light.border.hairline-dark`; background transparent; text RoslindaleNarrow 16/18 600, #000000 `light.text.ink`; transition all 0.3s ease; layers a 298.3x59.0 B:1px solid rgb(46, 46, 50) |
| focus-visible | outline 1px dotted #000000 `light.text.ink`, offset 1px; layers a 298.3x59.0 B:1px solid rgb(46, 46, 50) 1px dotted rgb(0, 0, 0) offset 1px |

Child layers that carry the look: a 298.3x59 border 1px solid #2e2e32 `light.border.hairline-dark`.

![Category nav item default](components/crops/cat-nav-item-default.png) ![Category nav item focus-visible](components/crops/cat-nav-item-focus-visible.png) ![Category nav item pressed](components/crops/cat-nav-item-pressed.png)

#### Category sub-menu item
A sub-menu link ("Prehistoric Art") painted while its parent is hovered in the opened nav; measured, never followed. Read as `cat-nav-sub` on the home page.

**Values (opened).** size 92.25 x 18; background transparent; text Basier 14/18 400, #c6002f `light.action.accent`; transition all 0.3s ease.

![Category sub-menu item opened](components/crops/cat-nav-sub-opened.png)

#### Search button
The "Search" button in the header (a submit that GETs /?s=); measured, never submitted. Read as `search-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 87.5 x 38; padding 9px 20px; border 1px solid #c6002f `light.action.accent`; radius 3px; background transparent; text Basier 14/normal 600, #ffffff `light.background.page`; transition all 0.3s ease |
| hover, pressed | background #c6002f `light.action.accent` |

![Search button default](components/crops/search-btn-default.png) ![Search button hover](components/crops/search-btn-hover.png) ![Search button focus-visible](components/crops/search-btn-focus-visible.png) ![Search button pressed](components/crops/search-btn-pressed.png)

#### Newsletter form
The newsletter signup form (email + consent checkbox + send). Read as `nl-form` on the home page.

**Values (default).** size 368 x 180; background transparent; text Basier 14/18 400, #606a73; layers input.email.email-newsletter 368.0x40.0 rgb(255, 255, 255) T:1px solid rgb(152, 157, 167) / R:1px solid rgb(152, 157, 167) / B:1px solid rgb(152, 157, 167) / L:1px solid rgb(152, 157, 167) 3px; label::after 16pxx16px rgb(255, 255, 255) T:1px solid rgb(152, 157, 167) / R:1px solid rgb(152, 157, 167) / B:1px solid rgb(152, 157, 167) / L:1px solid rgb(152, 157, 167) 2px; button.primary.btn 368.0x38.0.

Child layers that carry the look: input 368x40 background #ffffff `light.background.page` border 1px solid #989da7 `light.border.submit-border` radius 3px; label::after 16pxx16px background #ffffff `light.background.page` border 1px solid #989da7 `light.border.submit-border` radius 2px; button 368x38 border 1px solid #c6002f `light.action.accent` radius 3px.

![Newsletter form default](components/crops/nl-form-default.png)

#### Newsletter email field
The newsletter email input; typed into for the filled state, then cleared — never submitted. Read as `nl-email` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 40; padding 10px; border 1px solid #989da7 `light.border.submit-border`; radius 3px; background #ffffff `light.background.page`; text Basier 14/18 400, #000000 `light.text.ink`; transition all 0.3s ease; placeholder #757575 |
| focused, filled | border 1px solid #000000 `light.text.ink` |

![Newsletter email field default](components/crops/nl-email-default.png) ![Newsletter email field focused](components/crops/nl-email-focused.png) ![Newsletter email field filled](components/crops/nl-email-filled.png)

#### Newsletter consent checkbox
The required consent checkbox; measured, never toggled. Read as `nl-checkbox` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 13 x 13; background transparent; text Basier 14/18 400, #000000 `light.text.ink`; transition all 0.3s ease; opacity 0; placeholder #000000 `light.text.ink` |

![Newsletter consent checkbox default](components/crops/nl-checkbox-default.png) ![Newsletter consent checkbox hover](components/crops/nl-checkbox-hover.png)

#### Newsletter send button
The newsletter submit; measured, never submitted. Read as `nl-send` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 368 x 38; padding 9px 20px; border 1px solid #c6002f `light.action.accent`; radius 3px; background transparent; text Basier 14/normal 600, #000000 `light.text.ink`; transition all 0.3s ease |
| hover, pressed | background #c6002f `light.action.accent`; text Basier 14/normal 600, #ffffff `light.background.page` |

![Newsletter send button default](components/crops/nl-send-default.png) ![Newsletter send button hover](components/crops/nl-send-hover.png) ![Newsletter send button focus-visible](components/crops/nl-send-focus-visible.png) ![Newsletter send button pressed](components/crops/nl-send-pressed.png)

#### Footer
The footer band: six link menus, social icons and the newsletter form. Read as `footer` on the home page.

**Values (default).** size 1440 x 842; padding 0px 20px 50px 20px; background transparent; text Basier 12/14 700, #000000 `light.text.ink`; layers div.separator 1152.0x1.0 rgb(0, 0, 0); div.separator 561.0x1.0 rgb(0, 0, 0); div.separator 561.0x1.0 rgb(0, 0, 0); input.email-newsletter 561.0x40.0 rgb(255, 255, 255) T:1px solid rgb(152, 157, 167) / R:1px solid rgb(152, 157, 167) / B:1px solid rgb(152, 157, 167) / L:1px solid rgb(152, 157, 167) 3px; label::after 16pxx16px rgb(255, 255, 255) T:1px solid rgb(152, 157, 167) / R:1px solid rgb(152, 1.

Child layers that carry the look: div 1152x1 background #000000 `light.text.ink`; div 561x1 background #000000 `light.text.ink`; div 561x1 background #000000 `light.text.ink`.

![Footer default](components/crops/footer-default.png)

#### Footer link
"About Us" — a footer menu link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 58.77 x 18; background transparent; text Basier 14/18 400, #c6002f `light.action.accent` |
| focus-visible | outline 1px dotted #c6002f `light.action.accent`, offset 1px; layers a 58.8x18.0 1px dotted rgb(198, 0, 47) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social icon link
A social-media icon link; measured, never followed. Read as `social-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 10 x 18; background transparent; text Basier 16/16 400, #0000ee; icon 10 x 16, #0000ee |
| hover | icon 13 x 20.8, #0000ee |
| focus-visible | outline 1px dotted #0000ee, offset 1px; layers a 10.0x18.0 1px dotted rgb(0, 0, 238) offset 1px |
| pressed | text Basier 16/16 400, #ff0000; icon 13 x 20.8, #ff0000 |

![Social icon link default](components/crops/social-link-default.png) ![Social icon link hover](components/crops/social-link-hover.png) ![Social icon link focus-visible](components/crops/social-link-focus-visible.png) ![Social icon link pressed](components/crops/social-link-pressed.png)

#### Newsletter modal
The newsletter dialog (720px white box on a 90%-black overlay); opened with the site's own .modal-r--show class — it never self-mounted during the public pass. Read as `nl-modal` on the home page.

**Values (default).** size 720 x 156.78; background #ffffff `light.background.page`; text Basier 16/21.6 400, #000000 `light.text.ink`; ancestors div.modal-r.modal-r--show bg rgba(0, 0, 0, 0.9) `light.background.scrim`.

![Newsletter modal default](components/crops/nl-modal-default.png)

#### Nav cluster
The left cluster inside the header: hamburger + the Stories/Shop/Courses menu. Read as `nav-cluster` on the home page.

**Values (default).** size 300.08 x 37; background transparent; text Basier 14/17 600, #ffffff `light.background.page`; layers div.ham-border 36.8x37.0 rgb(25, 25, 28) T:1px solid rgb(198, 0, 47) / R:1px solid rgb(198, 0, 47) / B:1px solid rgb(198, 0, 47) / L:1px solid rgb(198, 0, 47) 3px; span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); ancestors div.wrapper bg #19191c `light.background.dark-band`.

Child layers that carry the look: div 36.8x37 background #19191c `light.background.dark-band` border 1px solid #c6002f `light.action.accent` radius 3px; span 10x2 background #ffffff `light.background.page`; span 10x2 background #ffffff `light.background.page`.

![Nav cluster default](components/crops/nav-cluster-default.png)

### Home

The landing: a ~799px #19191c hero band (56px RoslindaleCondensed headline, crimson category tag with flanking rules, a featured card), then the Latest feed — 28px RoslindaleCondensed tabs, 760x194 horizontal cards with 260x177 thumbs, 275x293 vertical cards, the donation band, the 760x38 Load more ghost button and the ad slot.

#### Feed tab
The Latest/Trending tab label in the main feed heading. Read as `feed-tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 62.94 x 33; background transparent; text RoslindaleCondensed 28/32 500, #000000 `light.text.ink` |

![Feed tab default](components/crops/feed-tab-default.png) ![Feed tab hover](components/crops/feed-tab-hover.png)

#### Feed tab (active)
The active feed tab ("Latest"). Read as `feed-tab-active` on the home page.

**Values (default).** size 62.94 x 33; background transparent; text RoslindaleCondensed 28/32 500, #000000 `light.text.ink`.

![Feed tab (active) default](components/crops/feed-tab-active-default.png)

#### Browse-more link
"Browse More" beside the feed heading; measured, never followed. Read as `browse-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 86.73 x 14; background transparent; text Basier 12/14 700, #c6002f `light.action.accent`; transition all 0.5s ease; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | opacity 0.801133 |
| focus-visible | outline 1px dotted #c6002f `light.action.accent`, offset 1px; layers ::after rgba(0, 0, 0, 0) 0px none 1; a.link.link-browse-more-latest 86.7x14.0 1px dotted rgb(198, 0, 47) offset 1px |
| pressed | opacity 0.8068 |

![Browse-more link default](components/crops/browse-link-default.png) ![Browse-more link hover](components/crops/browse-link-hover.png) ![Browse-more link focus-visible](components/crops/browse-link-focus-visible.png) ![Browse-more link pressed](components/crops/browse-link-pressed.png)

#### Post card (horizontal)
A horizontal story card in the Latest feed. Read as `post-card-h` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 760 x 194; padding 0px 0px 16px 0px; border B: 1px solid #ebeced; background transparent; text Basier 10/12.25 700, #ffffff `light.background.page`; layers div.single-post.single-post__horizontal 760.0x194.0 B:1px solid rgb(235, 236, 237); a.category 30.9x20.3 rgb(198, 0, 47) 3px |

Child layers that carry the look: div 760x194 border 1px solid #ebeced; a 30.9x20.3 background #c6002f `light.action.accent` radius 3px.

![Post card (horizontal) default](components/crops/post-card-h-default.png) ![Post card (horizontal) hover](components/crops/post-card-h-hover.png)

#### Card image
The card's 264x177 thumbnail block. Read as `post-card-img` on the home page.

**Values (default).** size 260 x 177; background transparent; text Basier 10/12.25 700, #ffffff `light.background.page`; layers a.category 30.9x20.3 rgb(198, 0, 47) 3px.

Child layers that carry the look: a 30.9x20.3 background #c6002f `light.action.accent` radius 3px.

![Card image default](components/crops/post-card-img-default.png)

#### Card title link
A story title link inside a feed card; measured, never followed. Read as `post-card-title` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 412.23 x 48; background transparent; text RoslindaleNarrow 20/24 700, #000000 `light.text.ink` |
| focus-visible | outline 1px dotted #000000 `light.text.ink`, offset 1px; layers a 412.2x48.0 1px dotted rgb(0, 0, 0) offset 1px |

![Card title link default](components/crops/post-card-title-default.png) ![Card title link hover](components/crops/post-card-title-hover.png) ![Card title link focus-visible](components/crops/post-card-title-focus-visible.png) ![Card title link pressed](components/crops/post-card-title-pressed.png)

#### Card excerpt
The story excerpt paragraph under a card title. Read as `post-card-excerpt` on the home page.

**Values (default).** size 452 x 24; padding 4px 0px 20px 0px; background transparent; text Basier 16/24 400, #606a73.

![Card excerpt default](components/crops/post-card-excerpt-default.png)

#### Category chip
The pink category chip on a card image ("Quiz", "Asian Art"); measured, never followed. Read as `post-card-cat` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 119.31 x 20.25; padding 4px; radius 3px; background #c6002f `light.action.accent`; text Basier 10/12.25 700, #ffffff `light.background.page`; layers ::before rgb(46, 46, 50) 0px none 1; ::after rgb(46, 46, 50) 0px none 1 |
| focus-visible | outline 1px dotted #ffffff `light.background.page`, offset 1px |

![Category chip default](components/crops/post-card-cat-default.png) ![Category chip hover](components/crops/post-card-cat-hover.png) ![Category chip focus-visible](components/crops/post-card-cat-focus-visible.png) ![Category chip pressed](components/crops/post-card-cat-pressed.png)

#### Author link
A byline author link; measured, never followed. Read as `post-card-author` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 103.73 x 15; background transparent; text Basier 12/14 700, #f3003a `light.action.link-bright` |
| focus-visible | outline 1px dotted #f3003a `light.action.link-bright`, offset 1px; layers a.author-link 103.7x15.0 1px dotted rgb(243, 0, 58) offset 1px |

![Author link default](components/crops/post-card-author-default.png) ![Author link hover](components/crops/post-card-author-hover.png) ![Author link focus-visible](components/crops/post-card-author-focus-visible.png) ![Author link pressed](components/crops/post-card-author-pressed.png)

#### Card date
A card's publication date. Read as `post-card-date` on the home page.

**Values (default).** size 143.02 x 15; background transparent; text Basier 12/14 700, #000000 `light.text.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Card date default](components/crops/post-card-date-default.png)

#### Post card (vertical)
A vertical/small story card. Read as `post-card-v` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 275.5 x 292.75; padding 0px 0px 20px 0px; border B: 1px solid #2e2e32 `light.border.hairline-dark`; background transparent; text Basier 10/12.25 700, #ffffff `light.background.page`; layers div.single-post.single-post__vertical 275.5x292.8 B:1px solid rgb(46, 46, 50); a.category 119.3x20.3 rgb(198, 0, 47) 3px; a::before.category 41pxx1px rgb(46, 46, 50); a::after.category 41pxx1px rgb(46, 46, 50) |

Child layers that carry the look: div 275.5x292.8 border 1px solid #2e2e32 `light.border.hairline-dark`; a 119.3x20.3 background #c6002f `light.action.accent` radius 3px; a::before 41pxx1px background #2e2e32 `light.border.hairline-dark`.

![Post card (vertical) default](components/crops/post-card-v-default.png) ![Post card (vertical) hover](components/crops/post-card-v-hover.png)

#### Load-more button
The feed's "load more" control; measured, never clicked. Read as `load-more` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 760 x 38; padding 9px 20px; border 1px solid #c6002f `light.action.accent`; radius 3px; background transparent; text Basier 14/normal 600, #000000 `light.text.ink`; transition all 0.3s ease |
| hover, pressed | background #c6002f `light.action.accent`; text Basier 14/normal 600, #ffffff `light.background.page` |

![Load-more button default](components/crops/load-more-default.png) ![Load-more button hover](components/crops/load-more-hover.png) ![Load-more button focus-visible](components/crops/load-more-focus-visible.png) ![Load-more button pressed](components/crops/load-more-pressed.png)

#### Donation block
The donation call-out block. Read as `donation` on the home page.

**Values (default).** size 760 x 385.56; background transparent; text RoslindaleCondensed 28/33.6 500, #f997af; layers div::before.donate-row.is-bg-ready 760pxx385.562px rgb(198, 0, 47); a.btn 100.0x40.0 rgb(0, 0, 0) T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid rgb(0, 0, 0) 3px; a.btn 100.0x40.0 rgb(0, 0, 0) T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid rgb(0, 0, 0) 3px; a.btn 100.0x40.0 rgb(0, 0, 0) T:1px solid rgb(0, 0.

Child layers that carry the look: div::before 760pxx385.562px background #c6002f `light.action.accent`; a 100x40 background #000000 `light.text.ink` border 1px solid #000000 `light.text.ink` radius 3px; a 100x40 background #000000 `light.text.ink` border 1px solid #000000 `light.text.ink` radius 3px.

![Donation block default](components/crops/donation-default.png)

#### Ad slot
A painted a.pub.network ad placeholder (billboard/leaderboard/right-rail); read, never clicked. Read as `ad-slot` on the home page.

**Values (default).** size 760 x 98; background transparent; text Basier 16/0 400, #4d5761 `light.text.muted`; layers div.separator 760.0x1.0 rgb(235, 236, 237).

Child layers that carry the look: div 760x1 background #ebeced.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Hero block
The dark hero section over the white page ("Scandalous Rodin" featured story + side cards). Read as `hero-block` on the home page.

**Values (default).** size 1440 x 798.75; padding 63px 0px 0px 0px; background #19191c `light.background.dark-band`; text Basier 10/12.25 700, #ffffff `light.background.page`.

![Hero block default](components/crops/hero-block-default.png)

#### Hero tag
The "Featured Story" pink pill above the hero title. Read as `hero-tag` on the home page.

**Values (default).** size 93.34 x 20.25; padding 4px; radius 3px; background #c6002f `light.action.accent`; text Basier 10/12.25 700, #ffffff `light.background.page`; layers ::before rgb(46, 46, 50) 0px none 1; ::after rgb(46, 46, 50) 0px none 1.

![Hero tag default](components/crops/hero-tag-default.png)

#### Hero heading
"Scandalous Rodin" — the serif hero title on the dark block. Read as `hero-h1` on the home page.

**Values (default).** size 900 x 60; background transparent; text RoslindaleCondensed 56/60 500, #ffffff `light.background.page`.

![Hero heading default](components/crops/hero-h1-default.png)

#### Hero card
A story card inside the dark hero. Read as `hero-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 275.5 x 292.75; padding 0px 0px 20px 0px; border B: 1px solid #2e2e32 `light.border.hairline-dark`; background transparent; text Basier 10/12.25 700, #ffffff `light.background.page`; layers div.single-post.single-post__vertical 275.5x292.8 B:1px solid rgb(46, 46, 50); a.category 119.3x20.3 rgb(198, 0, 47) 3px; a::before.category 41pxx1px rgb(46, 46, 50); a::after.category 41pxx1px rgb(46, 46, 50) |

Child layers that carry the look: div 275.5x292.8 border 1px solid #2e2e32 `light.border.hairline-dark`; a 119.3x20.3 background #c6002f `light.action.accent` radius 3px; a::before 41pxx1px background #2e2e32 `light.border.hairline-dark`.

![Hero card default](components/crops/hero-card-default.png) ![Hero card hover](components/crops/hero-card-hover.png)

#### Section heading
A big serif section heading ("Latest" / "Long reads" / "Featured"). Read as `section-heading` on the home page.

**Values (default).** size 104.67 x 40; background transparent; text RoslindaleCondensed 32/40 500, #000000 `light.text.ink`.

![Section heading default](components/crops/section-heading-default.png)

### Latest

The /latest index: the page heading and its article rows/links, reusing the feed card layout.

#### Index heading
The stories index heading. Read as `latest-h1` on the latest page.

**Values (default).** size 125.39 x 60; background transparent; text RoslindaleCondensed 56/60 500, #000000 `light.text.ink`.

![Index heading default](components/crops/latest-h1-default.png)

#### Story row
A story row on the Latest index. Read as `latest-row` on the latest page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 760 x 194; padding 0px 0px 16px 0px; border B: 1px solid #ebeced; background transparent; text Basier 10/12.25 700, #ffffff `light.background.page`; layers div.single-post.single-post__horizontal 760.0x194.0 B:1px solid rgb(235, 236, 237); a.category 59.9x20.3 rgb(198, 0, 47) 3px |

Child layers that carry the look: div 760x194 border 1px solid #ebeced; a 59.9x20.3 background #c6002f `light.action.accent` radius 3px.

![Story row default](components/crops/latest-row-default.png) ![Story row hover](components/crops/latest-row-hover.png)

#### Story link
A story title link on the index; measured, never followed. Read as `latest-link` on the latest page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 407.2 x 48; background transparent; text RoslindaleNarrow 20/24 700, #000000 `light.text.ink` |
| focus-visible | outline 1px dotted #000000 `light.text.ink`, offset 1px; layers a 407.2x48.0 1px dotted rgb(0, 0, 0) offset 1px |

![Story link default](components/crops/latest-link-default.png) ![Story link hover](components/crops/latest-link-hover.png) ![Story link focus-visible](components/crops/latest-link-focus-visible.png) ![Story link pressed](components/crops/latest-link-pressed.png)

### Category

An Art Movements category index: the heading and the category post cards with their RoslindaleNarrow titles.

#### Category heading
"Impressionism" — the category archive heading. Read as `cat-h1` on the category page.

**Values (default).** size 304.38 x 60; background transparent; text RoslindaleCondensed 56/60 500, #000000 `light.text.ink`.

![Category heading default](components/crops/cat-h1-default.png)

#### Archive card
A story card in the category archive. Read as `cat-card` on the category page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 760 x 194; padding 0px 0px 16px 0px; border B: 1px solid #ebeced; background transparent; text Basier 10/12.25 700, #ffffff `light.background.page`; layers div.single-post.single-post__horizontal 760.0x194.0 B:1px solid rgb(235, 236, 237); a.category 85.7x20.3 rgb(198, 0, 47) 3px |

Child layers that carry the look: div 760x194 border 1px solid #ebeced; a 85.7x20.3 background #c6002f `light.action.accent` radius 3px.

![Archive card default](components/crops/cat-card-default.png) ![Archive card hover](components/crops/cat-card-hover.png)

#### Archive title link
An archive card title link; measured, never followed. Read as `cat-card-title` on the category page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 280.23 x 24; background transparent; text RoslindaleNarrow 20/24 700, #000000 `light.text.ink` |
| focus-visible | outline 1px dotted #000000 `light.text.ink`, offset 1px; layers a 280.2x24.0 1px dotted rgb(0, 0, 0) offset 1px |

![Archive title link default](components/crops/cat-card-title-default.png) ![Archive title link hover](components/crops/cat-card-title-hover.png) ![Archive title link focus-visible](components/crops/cat-card-title-focus-visible.png) ![Archive title link pressed](components/crops/cat-card-title-pressed.png)

### Article

A single post: the 1152px header row with 56px display headline, meta and category chip, the 648px text column (18px Basier, #f3003a inline links), figures with captions, share buttons, tag chips, the author box, related cards and the article newsletter form.

#### Article title
"10 Incredible Japanese Woodblock Prints You Need to See" — the article h1. Read as `art-h1` on the article page.

**Values (default).** size 1152 x 120; background transparent; text RoslindaleCondensed 56/60 500, #000000 `light.text.ink`.

![Article title default](components/crops/art-h1-default.png)

#### Article meta
The byline/date block under the title. Read as `art-meta` on the article page.

**Values (default).** size 1152 x 14.75; background transparent; text Basier 12/14 700, #c6002f `light.action.accent`.

![Article meta default](components/crops/art-meta-default.png)

#### Article category link
A category chip on the article; measured, never followed. Read as `art-cat` on the article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 61.7 x 15; background transparent; text Basier 12/14 700, #c6002f `light.action.accent` |
| focus-visible | outline 1px dotted #c6002f `light.action.accent`, offset 1px; layers a 61.7x15.0 1px dotted rgb(198, 0, 47) offset 1px |

![Article category link default](components/crops/art-cat-default.png) ![Article category link hover](components/crops/art-cat-hover.png) ![Article category link focus-visible](components/crops/art-cat-focus-visible.png) ![Article category link pressed](components/crops/art-cat-pressed.png)

#### Article paragraph
A body paragraph in the article flow. Read as `art-para` on the article page.

**Values (default).** size 648 x 168; background transparent; text Basier 18/24 400, #4d5761 `light.text.muted`.

![Article paragraph default](components/crops/art-para-default.png)

#### Inline link
An in-copy link inside the article; measured, never followed. Read as `art-inline-link` on the article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 163.73 x 23; background transparent; text Basier 18/24 400, #f3003a `light.action.link-bright` |
| focus-visible | outline 1px dotted #f3003a `light.action.link-bright`, offset 1px; layers a 163.7x23.0 1px dotted rgb(243, 0, 58) offset 1px |

![Inline link default](components/crops/art-inline-link-default.png) ![Inline link hover](components/crops/art-inline-link-hover.png) ![Inline link focus-visible](components/crops/art-inline-link-focus-visible.png) ![Inline link pressed](components/crops/art-inline-link-pressed.png)

#### Article figure
A figure block (image + caption) in the article flow; the lightgallery viewer is not opened. Read as `art-figure` on the article page.

**Values (default).** size 648 x 1013.75; background transparent; text Basier 12/16.2 400, #606a73; layers figcaption 648.0x27.2 B:1px solid rgb(235, 236, 237).

Child layers that carry the look: figcaption 648x27.2 border 1px solid #ebeced.

![Article figure default](components/crops/art-figure-default.png)

#### Figure caption
A figure caption under an article image. Read as `art-caption` on the article page.

**Values (default).** size 648 x 27.2; border B: 1px solid #ebeced; background transparent; text Basier 12/16.2 400, #606a73; layers figcaption 648.0x27.2 B:1px solid rgb(235, 236, 237).

Child layers that carry the look: figcaption 648x27.2 border 1px solid #ebeced.

![Figure caption default](components/crops/art-caption-default.png)

#### Share button
A share icon button in the article share-links row; measured, never followed. Read as `share-btn` on the article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 72 x 32; padding 7px 10px; border 1px solid #989da7 `light.border.submit-border`; radius 3px; background #ffffff `light.background.page`; text Basier 16/16 400, #0000ee; transition all 0.3s ease-in; icon 50 x 16, #0000ee |
| hover | border 1px solid #c6002f `light.action.accent`; background #c6002f `light.action.accent` |
| focus-visible | outline 1px dotted #0000ee, offset 1px |
| pressed | border 1px solid #c6002f `light.action.accent`; background #c6002f `light.action.accent`; text Basier 16/16 400, #ff0000; icon 50 x 16, #ff0000 |

![Share button default](components/crops/share-btn-default.png) ![Share button hover](components/crops/share-btn-hover.png) ![Share button focus-visible](components/crops/share-btn-focus-visible.png) ![Share button pressed](components/crops/share-btn-pressed.png)

#### Tag link
An article tag link in the tags-menu; measured, never followed. Read as `art-tag` on the article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 66.56 x 20.25; padding 4px; radius 3px; background #c6002f `light.action.accent`; text Basier 10/12.25 700, #ffffff `light.background.page` |
| focus-visible | outline 1px dotted #ffffff `light.background.page`, offset 1px |

![Tag link default](components/crops/art-tag-default.png) ![Tag link hover](components/crops/art-tag-hover.png) ![Tag link focus-visible](components/crops/art-tag-focus-visible.png) ![Tag link pressed](components/crops/art-tag-pressed.png)

#### Author box
The author bio box at the end of the article (avatar, name, bio). Read as `author-box` on the article page.

**Values (default).** size 1440 x 205; background transparent; text RoslindaleNarrow 20/24 700, #000000 `light.text.ink`; layers div.separator 560.0x1.0 rgb(0, 0, 0); div.separator 560.0x1.0 rgb(0, 0, 0).

Child layers that carry the look: div 560x1 background #000000 `light.text.ink`; div 560x1 background #000000 `light.text.ink`.

![Author box default](components/crops/author-box-default.png)

#### Related card
A related-stories card under the article. Read as `related-card` on the article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 337 x 107; padding 12px 0px 16px 0px; border B: 1px solid #ebeced; background transparent; text Basier 12/14 700, #c6002f `light.action.accent`; layers div.small-post 337.0x107.0 B:1px solid rgb(235, 236, 237) |

Child layers that carry the look: div 337x107 border 1px solid #ebeced.

![Related card default](components/crops/related-card-default.png) ![Related card hover](components/crops/related-card-hover.png)

#### Article newsletter form
The newsletter form under the article. Read as `nl-form-article` on the article page.

**Values (default).** size 561 x 146; background transparent; text Basier 14/18 400, #4d5761 `light.text.muted`; layers input.email-newsletter 561.0x40.0 rgb(255, 255, 255) T:1px solid rgb(152, 157, 167) / R:1px solid rgb(152, 157, 167) / B:1px solid rgb(152, 157, 167) / L:1px solid rgb(152, 157, 167) 3px; label::after 16pxx16px rgb(255, 255, 255) T:1px solid rgb(152, 157, 167) / R:1px solid rgb(152, 157, 167) / B:1px solid rgb(152, 157, 167) / L:1px solid rgb(152, 157, 167) 2px; button.primary.btn 561.0x38.0 T:1px.

Child layers that carry the look: input 561x40 background #ffffff `light.background.page` border 1px solid #989da7 `light.border.submit-border` radius 3px; label::after 16pxx16px background #ffffff `light.background.page` border 1px solid #989da7 `light.border.submit-border` radius 2px; button 561x38 border 1px solid #c6002f `light.action.accent` radius 3px.

![Article newsletter form default](components/crops/nl-form-article-default.png)

### About

The about page: the display heading and its text column.

#### About heading
The About page heading. Read as `about-h1` on the about page.

**Values (default).** size 770 x 60; background transparent; text RoslindaleCondensed 56/60 500, #000000 `light.text.ink`.

![About heading default](components/crops/about-h1-default.png)

#### About paragraph
A body paragraph in the About page content. Read as `about-para` on the about page.

**Values (default).** size 689 x 120; background transparent; text Basier 18/24 400, #606a73.

![About paragraph default](components/crops/about-para-default.png)

### Contact

The /contact page: the Contact Form 7 form — half-width name/email fields, the 202px message area, the acceptance control (native input hidden, box painted by the label) and the 669x46 black Send button, measured, never submitted.

#### Contact heading
The Contact page heading. Read as `contact-h1` on the contact page.

**Values (default).** size 750 x 60; background transparent; text RoslindaleCondensed 56/60 500, #000000 `light.text.ink`.

![Contact heading default](components/crops/contact-h1-default.png)

#### Contact form
The Contact Form 7 form (name, email, message, consent, Send). Read as `cf7-form` on the contact page.

**Values (default).** size 669 x 418; background transparent; text Basier 14/18 400, #606a73; layers input 0.0x0.0 T:1px solid rgb(152, 157, 167) / R:1px solid rgb(152, 157, 167) / B:1px solid rgb(152, 157, 167) / L:1px solid rgb(152, 157, 167) 2px; input 0.0x0.0 T:1px solid rgb(152, 157, 167) / R:1px solid rgb(152, 157, 167) / B:1px solid rgb(152, 157, 167) / L:1px solid rgb(152, 157, 167) 2px; input 0.0x0.0 T:1px solid rgb(152, 157, 167) / R:1px solid rgb(152, 157, 167) / B:1px solid rgb(152, 1.

Child layers that carry the look: input 0x0 border 1px solid #989da7 `light.border.submit-border` radius 2px; input 0x0 border 1px solid #989da7 `light.border.submit-border` radius 2px; input 0x0 border 1px solid #989da7 `light.border.submit-border` radius 2px.

![Contact form default](components/crops/cf7-form-default.png)

#### Text field
The "Your name" required text field; typed into for filled, then cleared — never submitted. Read as `cf7-name` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 319.5 x 40; padding 10px; border 1px solid #989da7 `light.border.submit-border`; radius 2px; background #ffffff `light.background.page`; text Basier 14/18 400, #000000 `light.text.ink`; transition all 0.3s ease; placeholder #757575 |

![Text field default](components/crops/cf7-name-default.png) ![Text field focused](components/crops/cf7-name-focused.png) ![Text field filled](components/crops/cf7-name-filled.png)

#### Email field
The "Your email" required email field; typed into for filled, then cleared — never submitted. Read as `cf7-email` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 319.5 x 40; padding 10px; border 1px solid #989da7 `light.border.submit-border`; radius 2px; background #ffffff `light.background.page`; text Basier 14/18 400, #000000 `light.text.ink`; transition all 0.3s ease; placeholder #757575 |

![Email field default](components/crops/cf7-email-default.png) ![Email field focused](components/crops/cf7-email-focused.png) ![Email field filled](components/crops/cf7-email-filled.png)

#### Textarea
The "Your message" textarea; typed into for filled, then cleared — never submitted. Read as `cf7-message` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 669 x 202; padding 10px; border 1px solid #989da7 `light.border.submit-border`; radius 2px; background #ffffff `light.background.page`; text Basier 14/18 400, #000000 `light.text.ink`; transition all 0.3s ease; placeholder #757575 |

![Textarea default](components/crops/cf7-message-default.png) ![Textarea focused](components/crops/cf7-message-focused.png) ![Textarea filled](components/crops/cf7-message-filled.png)

#### Acceptance checkbox
The wpcf7 acceptance control: the native input is visibility:hidden, the box is painted by the label span ::before; measured, never toggled. Read as `cf7-accept` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 669 x 42; background transparent; text Basier 14/18 400, #606a73; layers span::before.wpcf7-list-item-label 16pxx16px T:1px solid rgb(152, 157, 167) / R:1px solid rgb(152, 157, 167) / B:1px solid rgb(152, 157, 167) / L:1px solid rgb(152, 157, 167) 2px |

Child layers that carry the look: span::before 16pxx16px border 1px solid #989da7 `light.border.submit-border` radius 2px.

![Acceptance checkbox default](components/crops/cf7-accept-default.png) ![Acceptance checkbox hover](components/crops/cf7-accept-hover.png)

#### Send button
The wpcf7 "Send" submit; measured, never submitted. Read as `cf7-send` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 669 x 46; padding 15px 10px 12px 10px; border 1px solid #989da7 `light.border.submit-border`; radius 2px; background #000000 `light.text.ink`; text Basier 14/17 600, #ffffff `light.background.page`; transition all 0.3s ease; placeholder #ffffff `light.background.page` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Send button default](components/crops/cf7-send-default.png) ![Send button hover](components/crops/cf7-send-hover.png) ![Send button pressed](components/crops/cf7-send-pressed.png)

### Search

The search results page: the heading and its result cards.

#### Search heading
The results heading for ?s=van+gogh. Read as `search-h1` on the search page.

**Values (default).** size 750 x 60; background transparent; text RoslindaleCondensed 56/60 500, #000000 `light.text.ink`.

![Search heading default](components/crops/search-h1-default.png)

#### Result card
A search-result story card. Read as `search-card` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 760 x 194; padding 0px 0px 16px 0px; border B: 1px solid #ebeced; background transparent; text Basier 10/12.25 700, #ffffff `light.background.page`; layers div.single-post.single-post__horizontal 760.0x194.0 B:1px solid rgb(235, 236, 237); a.category 119.3x20.3 rgb(198, 0, 47) 3px |

Child layers that carry the look: div 760x194 border 1px solid #ebeced; a 119.3x20.3 background #c6002f `light.action.accent` radius 3px.

![Result card default](components/crops/search-card-default.png) ![Result card hover](components/crops/search-card-hover.png)

### Mobile (390 wide)

The home at phone width: the condensed nav, the hamburger and the full-width feed cards and newsletter field.

#### Mobile nav
Read as `m-nav-bar` on the home page at 390 wide.

**Values (default).** size 366 x 37; background transparent; text Basier 16/16 400, #4d5761 `light.text.muted`; icon 24 x 24, #000000 `light.text.ink`; layers div.ham-border 36.8x37.0 rgb(25, 25, 28) T:1px solid rgb(198, 0, 47) / R:1px solid rgb(198, 0, 47) / B:1px solid rgb(198, 0, 47) / L:1px solid rgb(198, 0, 47) 3px; span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); ancestors div.wrapper bg #19191c `light.background.dark-band`; header bg #19191c `light.background.dark-band`.

Child layers that carry the look: div 36.8x37 background #19191c `light.background.dark-band` border 1px solid #c6002f `light.action.accent` radius 3px; span 10x2 background #ffffff `light.background.page`; span 10x2 background #ffffff `light.background.page`.

![Mobile nav default](components/crops/m-nav-bar-default.png)

#### Mobile logo
Read as `m-logo` on the home page at 390 wide.

**Values (default).** size 111 x 30.17; background transparent; text Basier 16/16 400, #0000ee; transform translate(-55.5px, -15.0859px); icon 111 x 28.17, #0000ee; ancestors div.wrapper bg #19191c `light.background.dark-band`; header bg #19191c `light.background.dark-band`.

![Mobile logo default](components/crops/m-logo-default.png)

#### Mobile hamburger
The hamburger at 390px. Read as `m-hamburger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 20 x 15; background transparent; text Basier 16/16 400, #4d5761 `light.text.muted`; transition all 0.5s ease-in-out; layers span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); span 10.0x2.0 rgb(255, 255, 255); ancestors div.ham-border bg #19191c `light.background.dark-band` |

Child layers that carry the look: span 10x2 background #ffffff `light.background.page`; span 10x2 background #ffffff `light.background.page`; span 10x2 background #ffffff `light.background.page`.

![Mobile hamburger default](components/crops/m-hamburger-default.png) ![Mobile hamburger pressed](components/crops/m-hamburger-pressed.png)

#### Mobile post card
A story card at 390px. Read as `m-post-card` on the home page at 390 wide.

**Values (default).** size 366 x 346.75; padding 0px 0px 15px 0px; border B: 1px solid #2e2e32 `light.border.hairline-dark`; background transparent; text Basier 10/12.25 700, #ffffff `light.background.page`; layers div.single-post.single-post__vertical 366.0x346.8 B:1px solid rgb(46, 46, 50); a.category 65.1x20.3 rgb(198, 0, 47) 3px; a::before.category 41pxx1px rgb(46, 46, 50).

Child layers that carry the look: div 366x346.8 border 1px solid #2e2e32 `light.border.hairline-dark`; a 65.1x20.3 background #c6002f `light.action.accent` radius 3px; a::before 41pxx1px background #2e2e32 `light.border.hairline-dark`.

![Mobile post card default](components/crops/m-post-card-default.png)

#### Mobile newsletter field
The newsletter input at 390px; typed into for filled, then cleared — never submitted. Read as `m-nl-email` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 356 x 40; padding 10px; border 1px solid #989da7 `light.border.submit-border`; radius 3px; background #ffffff `light.background.page`; text Basier 14/18 400, #000000 `light.text.ink`; transition all 0.3s ease; placeholder #757575 |
| focused, filled | border 1px solid #000000 `light.text.ink` |

![Mobile newsletter field default](components/crops/m-nl-email-default.png) ![Mobile newsletter field focused](components/crops/m-nl-email-focused.png) ![Mobile newsletter field filled](components/crops/m-nl-email-filled.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the wordmark, the social icons, the share glyphs) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Members and external destinations

DailyArt Magazine is a read-only publication; there is no signed-in product on this domain. The 'Shop' and 'Courses' nav entries link to external stores (shop.dailyartmagazine.com, dailyartcourses.com) and were measured as outbound links, never followed. Comment threads, if present, live behind third-party widgets that were not opened.

### Pages

- **Outbound links.** 'Shop' and 'Courses' in the nav and every social link were measured, never followed — they leave the captured domain.
- **Article interior.** Only the first article was measured as a component set; other posts share the same templates but their blocks (galleries, pull quotes) are not individually documented.
- **Ad slots.** Third-party ad placements were measured as layout slots only; their injected content was left alone and is not part of the design evidence.
- **Author archives and tag indexes** exist but were not individually captured; they reuse the feed card layout.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **The category mega-menu and newsletter modal** were opened locally (the site's own classes/trigger); nothing was typed into or submitted anywhere.
- **Category-item hover** was not captured: the menu item leaves the viewport as the panel opens, and the miss is recorded rather than forced.
- **Disabled, error and loading states** were not seen on the public surface. The newsletter checkbox's native input is painted at opacity 0; its box is drawn by the label.

### Themes

One painted theme, no toggle: a white editorial field crossed by #19191c dark bands (top nav, hero, mid-page sections) with #c6002f crimson accents. The dark regions are recorded as surfaces inside the single theme; tokens.json emits light only (the only resolved :root vars are stock WordPress --wp--preset--* values).

### Fonts

- **Basier** (UI/body), **RoslindaleCondensed** (display) and **RoslindaleNarrow** (card titles, menu items) are self-hosted under the theme. Font files are not shipped in this package.

### Screenshots

- Article imagery, author names and the artwork shown in posts are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article text, headlines, captions and the artwork images are the product's content; only frames and components were measured.
