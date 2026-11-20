# Cron components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from cron.com on 2026-11-12, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or downloaded; the mobile menu was opened locally and closed, and hover/focus/pressed states were forced. Login and Sign up were never followed, and the Docs and demo links were never opened. /changelog reports a 113,351px scroll height — the full-page capture is bounded at the first 112,000px, a documented boundary.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (28 components, 60 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (58 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: the home paints `dark`, the content pages `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home (dark) | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Changelog | `/changelog` | [default](screenshots/changelog-light-default.png), [full](screenshots/changelog-light-full.png) |
| Blog post | `/blog/2024-01-17-cron-is-now-notion-calendar` | [default](screenshots/post-light-default.png), [full](screenshots/post-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png), [menu](screenshots/mobile-home-dark-menu.png) |
| Blog, phone | `/blog` | [default](screenshots/mobile-blog-light-default.png), [full](screenshots/mobile-blog-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the hamburger button's own toggle (body.showing-menu) | [mobile-home-dark-menu](screenshots/mobile-home-dark-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-menu-row) |
| Intercom chat launcher | every page | hidden via the overlay hider, never answered | not captured |
| The Cron/Notion Calendar app | past Login / Sign up | the buttons were measured, never followed | boundary; see Gaps |
| /changelog full page | changelog | 113,351px scroll height | bounded at 112,000px — documented boundary |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 9 components were given a real keyboard focus. 8 draw an outline ring: `nav-link` (1px auto #005fcc, offset 1px), `login-link` (1px auto #005fcc, offset 1px), `signup-btn` (1px auto #005fcc, offset 1px), `footer-link` (1px auto #005fcc, offset 1px), `m-nav-item` (1px auto #005fcc, offset 1px), `m-signup-btn` (1px auto #005fcc, offset 1px), `post-back` (1px auto #005fcc, offset 1px), `demo-link` (1px auto #005fcc, offset 1px). The other 1 show no measured change: `banner`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.175s | `ease` | box-shadow, opacity | banner, m-signup-btn, signup-btn |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|

## Components

### Shell and navigation

The 120px dark site header: the Cron wordmark, Blog / Changelog / Docs / Login links and the 46px #ff4700 Sign up pill glowing under --glow; the #161412 banner below it announces Cron is now Notion Calendar.

#### Site header
The 120px header: the Cron logotype and the nav (Blog / Changelog / Docs / Login / Sign up). Read as `site-header` on the home page.

**Values (default).** size 1440 x 120; padding 0px 140px; background transparent; text Helvetica Neue 22/37.4 500, #ffffff `color.named.snow`; layers a.primary-link-button.glow 125.4x46.0 rgb(255, 71, 0) rgba(255, 71, 0, 0.2) 0px 0px 100px 0px 9999px.

Child layers that carry the look: a 125.4x46 background #ff4700 `color.brand.chronos` radius 9999px shadow rgba(255, 71, 0, 0.2) 0px 0px 100px 0px.

![Site header default](components/crops/site-header-default.png)

#### Logotype
The Cron logotype image (40px tall). Read as `logotype` on the home page.

**Values (default).** size 126.66 x 40; background transparent; text Helvetica Neue 22/37.4 500, #ffffff `color.named.snow`.

![Logotype default](components/crops/logotype-default.png)

#### Nav link
A top-nav link (Blog); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 46.89 x 37.41; background transparent; text Helvetica Neue 22/37.4 500, #ffffff `color.named.snow` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a 46.9x37.4 1px auto rgb(0, 95, 204) offset 1px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Login link
The Login link to calendar.notion.so; measured, never followed. Read as `login-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 56.66 x 37.41; background transparent; text Helvetica Neue 22/37.4 500, #ffffff `color.named.snow` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a 56.7x37.4 1px auto rgb(0, 95, 204) offset 1px |

![Login link default](components/crops/login-link-default.png) ![Login link hover](components/crops/login-link-hover.png) ![Login link focus-visible](components/crops/login-link-focus-visible.png) ![Login link pressed](components/crops/login-link-pressed.png)

#### Sign up button
The #ff4700 Sign up pill (9999px radius, the --glow shadow var); measured, never followed. Read as `signup-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 125.42 x 46; padding 12px 24px; radius 9999px; background #ff4700 `color.brand.chronos`; shadow rgba(255, 71, 0, 0.2) 0px 0px 100px 0px; text Helvetica Neue 22/22 500, #ffffff `color.named.snow`; transition opacity 0.175s ease, box-shadow 0.175s ease |
| hover | shadow rgba(255, 71, 0, 0.4) 0px 0px 25px 0px |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | shadow rgba(255, 71, 0, 0.4) 0px 0px 25px 0px |

![Sign up button default](components/crops/signup-btn-default.png) ![Sign up button hover](components/crops/signup-btn-hover.png) ![Sign up button focus-visible](components/crops/signup-btn-focus-visible.png) ![Sign up button pressed](components/crops/signup-btn-pressed.png)

### Home

The dark marketing surface: the 140px Helvetica Neue hero ("It’s about time."), the 22px sub, the Sign up CTA and the 180px #0f0d0a footer.

#### Rebrand banner
"Cron is now Notion Calendar →" — the #161412 pill with the orange inset ring and glow shadow; measured, never followed. Read as `banner` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 269.19 x 45; padding 0px 24px 1px 24px; radius 4px; background #161412; shadow rgba(255, 71, 0, 0.5) 0px 0px 0px 0.5px inset, rgba(255, 72, 0, 0.2) 0px 0px 28px 0px; text Helvetica Neue 15/15 400, #ffffff `color.named.snow`; transition box-shadow 0.175s ease |
| hover, pressed | shadow rgba(255, 71, 0, 0.75) 0px 0px 0px 0.5px inset, rgba(255, 72, 0, 0.2) 0px 0px 28px 0px |

![Rebrand banner default](components/crops/banner-default.png) ![Rebrand banner hover](components/crops/banner-hover.png) ![Rebrand banner focus-visible](components/crops/banner-focus-visible.png) ![Rebrand banner pressed](components/crops/banner-pressed.png)

#### Hero heading
"It's about time." — 140px/-3px tracking Helvetica at 90% leading. Read as `hero-h1` on the home page.

**Values (default).** size 1000 x 126; background transparent; text Helvetica Neue 140/126 700, #ffffff `color.named.snow`.

![Hero heading default](components/crops/hero-h1-default.png)

#### Hero subline
"Cron is the next-generation calendar for professionals and teams." Read as `hero-sub` on the home page.

**Values (default).** size 1000 x 37.41; background transparent; text Helvetica Neue 22/37.4 400, #cccccc `color.gray.200`.

![Hero subline default](components/crops/hero-sub-default.png)

### Blog

The light /blog index: the 40px heading and 676px article entries.

#### Blog heading
"Cron Blog" — the index heading. Read as `blog-h1` on the blog page.

**Values (default).** size 676 x 24; background transparent; text Helvetica Neue 40/24 700, #000000 `color.named.eclipse`.

![Blog heading default](components/crops/blog-h1-default.png)

#### Post entry
A blog index entry: date, title, byline and excerpt; measured, never followed. Read as `post-entry` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 676 x 987.53; background transparent; text Helvetica Neue 16/16 400, #616161 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Post entry default](components/crops/post-entry-default.png) ![Post entry hover](components/crops/post-entry-hover.png) ![Post entry pressed](components/crops/post-entry-pressed.png)

### Changelog

The light /changelog index: the 40px heading, the changelog <article> entries and the see-the-demo link.

#### Changelog heading
"Cron Changelog" — the index heading. Read as `changelog-h1` on the changelog page.

**Values (default).** size 676 x 24; background transparent; text Helvetica Neue 40/24 700, #000000 `color.named.eclipse`.

![Changelog heading default](components/crops/changelog-h1-default.png)

#### Changelog entry
A dated release entry (title + notes). Read as `changelog-entry` on the changelog page.

**Values (default).** size 676 x 1014.66; background transparent; text Helvetica Neue 16/16 400, #616161; layers div.Changelog_coverImage__bo_xl.emailFullWidth 676.0x450.7; code 32.5x19.0 rgb(204, 204, 204) 3px; code 19.4x19.0 rgb(204, 204, 204) 3px; code 14.3x19.0 rgb(204, 204, 204) 3px; code 32.5x19.0 rgb(204, 204, 204) 3px; code 19.4x19.0 rgb(204, 204, 204) 3px.

Child layers that carry the look: div 676x450.7 image linear-gradient(#fa6c38, #f44e25); code 32.5x19 background #cccccc `color.gray.200` radius 3px; code 19.4x19 background #cccccc `color.gray.200` radius 3px.

![Changelog entry default](components/crops/changelog-entry-default.png)

#### Feature heading
A feature title inside an entry ("New name"). Read as `feature-h2` on the changelog page.

**Values (default).** size 676 x 36; background transparent; text Helvetica Neue 24/36 400, #000000 `color.named.eclipse`.

![Feature heading default](components/crops/feature-h2-default.png)

#### Demo link
The "View demo" link inside a release entry; measured, never followed. Read as `demo-link` on the changelog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 79.13 x 18; background transparent; text Helvetica Neue 16/24 400, #ff4700 `color.brand.chronos` |
| hover | text Helvetica Neue 16/24 400, #ca3800 `color.brand.primary-700` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.Changelog_demo__Goa_z 79.1x18.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text Helvetica Neue 16/24 400, #ca3800 `color.brand.primary-700` |

![Demo link default](components/crops/demo-link-default.png) ![Demo link hover](components/crops/demo-link-hover.png) ![Demo link focus-visible](components/crops/demo-link-focus-visible.png) ![Demo link pressed](components/crops/demo-link-pressed.png)

### Post

A blog post ("Cron is now Notion Calendar"): the 32px title, #616161 meta, 16px body and the 676x451 media frame.

#### Post title
"Cron is now Notion Calendar" — the post heading. Read as `post-h1` on the post page.

**Values (default).** size 676 x 24; background transparent; text Helvetica Neue 32/24 700, #000000 `color.named.eclipse`.

![Post title default](components/crops/post-h1-default.png)

#### Post byline
The date + "By Raphael Schaad" byline. Read as `post-meta` on the post page.

**Values (default).** size 139.61 x 18; background transparent; text Helvetica Neue 16/24 400, #000000 `color.named.eclipse`.

![Post byline default](components/crops/post-meta-default.png)

#### Body paragraph
A body paragraph in the post (22px/170%). Read as `post-body` on the post page.

**Values (default).** size 676 x 24; background transparent; text Helvetica Neue 16/24 400, #000000 `color.named.eclipse`.

![Body paragraph default](components/crops/post-body-default.png)

#### Post media
The post's demo video/image (16px radius on desktop). Read as `post-video` on the post page.

Not on the page when it was captured.

#### Post media
The post's demo media (675x450). Read as `post-media` on the post page.

**Values (default).** size 675.98 x 450.66; background transparent; text Helvetica Neue 16/24 400, #ff4700 `color.brand.chronos`.

![Post media default](components/crops/post-media-default.png)

#### Back link
"← All blog posts" — the article back link; measured, never followed. Read as `post-back` on the post page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 117.94 x 16; background transparent; text Helvetica Neue 16/16 400, #616161 |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a 117.9x16.0 1px auto rgb(0, 95, 204) offset 1px |

![Back link default](components/crops/post-back-default.png) ![Back link hover](components/crops/post-back-hover.png) ![Back link focus-visible](components/crops/post-back-focus-visible.png) ![Back link pressed](components/crops/post-back-pressed.png)

### Footer

The 180px #0f0d0a footer band: social glyphs and the legal links.

#### Footer
The #0f0d0a footer: Privacy / Terms / Web app / Download links. Read as `footer` on the home page.

**Values (default).** size 1440 x 180; padding 20px 140px 40px 140px; background #0f0d0a; text Helvetica Neue 13/19.5 500, #ffffff `color.named.snow`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer link (Privacy Policy); measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 84.58 x 16; background transparent; text Helvetica Neue 13/19.5 500, #ffffff `color.named.snow` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a 84.6x16.0 1px auto rgb(0, 95, 204) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Mobile (390 wide)



#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 96; padding 28px 16px; background transparent; text Helvetica Neue 16/27.2 400, #cccccc `color.gray.200`; icon 24 x 24, #cccccc `color.gray.200`; layers ul.nav-menu 0.0x0.0 rgb(22, 20, 18); a.primary-link-button.glow 0.0x0.0 rgb(255, 71, 0) rgba(255, 71, 0, 0.2) 0px 0px 100px 0px 9999px.

Child layers that carry the look: ul 0x0 background #161412; a 0x0 background #ff4700 `color.brand.chronos` radius 9999px shadow rgba(255, 71, 0, 0.2) 0px 0px 100px 0px.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The 24x18 menu icon that toggles body.showing-menu. Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 18; background transparent; text Helvetica Neue 16/27.2 400, #cccccc `color.gray.200`; icon 24 x 24, #cccccc `color.gray.200` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Menu button default](components/crops/m-menu-button-default.png) ![Menu button hover](components/crops/m-menu-button-hover.png) ![Menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The opened nav overlay (.nav-menu over #161412). Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 768; padding 16px 0px; background #161412; text Helvetica Neue 24/27.2 500, #ffffff `color.named.snow`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile menu row
A 24px row inside the opened nav overlay. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 83.16 x 59.2; padding 16px; background transparent; text Helvetica Neue 24/27.2 500, #ffffff `color.named.snow` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a 83.2x59.2 1px auto rgb(0, 95, 204) offset 1px |

![Mobile menu row default](components/crops/m-nav-item-default.png) ![Mobile menu row hover](components/crops/m-nav-item-hover.png) ![Mobile menu row focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile menu row pressed](components/crops/m-nav-item-pressed.png)

#### Mobile sign up
The full-width Sign up pill inside the menu. Read as `m-signup-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 342 x 54; padding 16px; radius 9999px; background #ff4700 `color.brand.chronos`; shadow rgba(255, 71, 0, 0.2) 0px 0px 100px 0px; text Helvetica Neue 24/22 500, #ffffff `color.named.snow`; transition opacity 0.175s ease, box-shadow 0.175s ease |
| hover | shadow rgba(255, 71, 0, 0.4) 0px 0px 25px 0px |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | shadow rgba(255, 71, 0, 0.4) 0px 0px 25px 0px |

![Mobile sign up default](components/crops/m-signup-btn-default.png) ![Mobile sign up hover](components/crops/m-signup-btn-hover.png) ![Mobile sign up focus-visible](components/crops/m-signup-btn-focus-visible.png) ![Mobile sign up pressed](components/crops/m-signup-btn-pressed.png)

#### Mobile heading
Read as `m-heading` on the home page at 390 wide.

**Values (default).** size 358 x 144; background transparent; text Helvetica Neue 80/72 700, #ffffff `color.named.snow`.

![Mobile heading default](components/crops/m-heading-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Cron wordmark, the hamburger glyph, the social glyphs and the article media) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The Cron app itself — the calendar, the Notion Calendar successor it redirects to, docs and the demo — was never reached. Login and Sign up are a measured link and button, never followed; the home's only content surface is the marketing page. What the product looks like past the public marketing and content pages is not documented here.

### Pages

- **App and CTAs.** Login, Sign up, the Notion Calendar banner link, Docs and the see-the-demo link were measured or screenshotted, never followed; no account exists on this surface.
- **Changelog depth.** /changelog reports a 113,351px scroll height; the full-page capture is bounded at the first 112,000px (the kit's 8-chunk cap) — the tail is a documented boundary, not missing content.
- **External surfaces** (calendar.cron.com, the Notion Calendar product, docs.cron.com, social profiles) are linked from the site but were never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **The mobile menu** was opened and closed locally (body.showing-menu) for the open-state reading; its links were never followed.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

Two painted surfaces, no theme attribute: the marketing home is dark (#161412 over #0f0d0a, #ccc text, the orange Sign up pill) and the /blog /changelog /blog/<post> content pages are light (white, #1a1a1a text, orange links). tokens.json's light set holds the content pages' declared var layer; the dark set is the home's measured literals — the home declares no vars.

### Fonts

- **Helvetica Neue** (700 headings, 500 links/buttons, 400 body, -3px tracking on the 140px hero) is the declared --sans-serif-font with Helvetica/Arial fallbacks; no webfont is served or shipped.

### Screenshots

- The article media, masthead illustrations and the Cron wordmark in the screenshots are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The kit/template artwork, product previews, plan feature lists and marketing copy are the product's content; only frames and components were measured.
