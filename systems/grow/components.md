# Grow with Google components

The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from grow.google on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, enrolled in, bought or submitted; the only presses were local UI toggles the page's own chrome provides — the Career Certificates mega-menu, the mobile navigation drawer, one FAQ expansion row and the hero video modal (opened and closed, the YouTube embed never played). Every link and CTA was measured, never followed; the footer's language <select> was never changed — its form posts to services.google.com.

**Where this was read.** The canonical surface is grow.google's **US edition**: bare headless contexts (no user agent, no locale) receive it. From this capture host, a request carrying a real browser user agent or an explicit locale is 302'd from `/` to the regional `/intl/ALL_sg/` edition — the APAC variant shots (`apac-*`) record that edition, and every deep link serves the US edition regardless. The cookie notification bar was removed from captures (hidden, never answered).

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (41 components, 106 states). The page layouts are described in [patterns.md](patterns.md) and the layout probe in [raw/layout.json](raw/layout.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one — grow.google's stylesheet declares only the `--glue-*-{50..900}` colour ramps as custom properties, so most entries label against that ramp. Text is written family size/line-height weight, then its colour, for example `Google Sans Flex 16/24 500, #3c4043`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (104 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (grow.google paints one theme — light only, no toggle and no applied dark media query; the certificate pages' dark hero is a section paint). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x); `apac-*` shots are the /intl/ALL_sg/ regional variant. Tall pages split the full shot into `.partN` tiles, bounded, with the clip in each `.capture.json` sidecar.

| Surface | URL | Screenshots |
|---|---|---|
| Home (US). The promo banner, the video hero, the Career Certificate CTA, story sections and the footer; the menu, the video modal and the full page captured. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png), [video](screenshots/home-light-video.png) |
| Certificates catalog. Breadcrumb, heading, stats band, Learn more, jumplinks, the foundational certificate card grid. | `/certificates` | [default](screenshots/certificates-light-default.png), [full](screenshots/certificates-light-full.png) |
| UX Design certificate. The dark hero, Coursera CTA, graduate badge, curriculum tabs, expansion FAQ (opened captured). | `/certificates/ux-design/` | [default](screenshots/cert-ux-light-default.png), [faq-open](screenshots/cert-ux-light-faq-open.png), [full](screenshots/cert-ux-light-full.png) |
| Data Analytics certificate. The same detail template on a second certificate. | `/certificates/data-analytics/` | [default](screenshots/cert-data-light-default.png), [full](screenshots/cert-data-light-full.png) |
| AI training hub. The tinted heading band and the course cards. | `/ai/` | [default](screenshots/ai-light-default.png), [full](screenshots/ai-light-full.png) |
| AI Professional Certificate page. | `/ai-professional/` | [default](screenshots/ai-pro-light-default.png), [full](screenshots/ai-pro-light-full.png) |
| Stories. Graduate and business story cards. | `/stories/` | [default](screenshots/stories-light-default.png), [full](screenshots/stories-light-full.png) |
| Our mission. The program overview page. | `/our-mission/` | [default](screenshots/mission-light-default.png), [full](screenshots/mission-light-full.png) |
| For partners. The employer/consortium page. | `/partners/` | [default](screenshots/partners-light-default.png), [full](screenshots/partners-light-full.png) |
| For employers. The hire-graduates page. | `/employers/` | [default](screenshots/employers-light-default.png), [full](screenshots/employers-light-full.png) |
| News & insights. Press and update cards. | `/news-insights/` | [default](screenshots/news-light-default.png), [full](screenshots/news-light-full.png) |
| Home (APAC regional variant). The /intl/ALL_sg/ edition this host's real-UA requests are redirected to; retained as variant evidence, not the canonical surface. | `/intl/ALL_sg/` | [default](screenshots/apac-home-light-default.png), [full](screenshots/apac-home-light-full.png) |
| Home at 390: the compact header, the opened drawer and the full page in two tiles. | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Certificates catalog at 390. | `/certificates` | [default](screenshots/mobile-certificates-light-default.png), [full](screenshots/mobile-certificates-light-full.png) |
| UX Design certificate at 390. | `/certificates/ux-design/` | [default](screenshots/mobile-cert-ux-light-default.png), [full](screenshots/mobile-cert-ux-light-full.png) |
| AI training hub at 390. | `/ai/` | [default](screenshots/mobile-ai-light-default.png), [full](screenshots/mobile-ai-light-full.png) |
| APAC home at 390: the /intl/ALL_sg/ edition's drawer and full page. | `/intl/ALL_sg/` | [default](screenshots/apac-mobile-home-light-default.png), [drawer](screenshots/apac-mobile-home-light-drawer.png), [full](screenshots/apac-mobile-home-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Career Certificates mega-menu | site header | clicked the nav trigger — a local UI toggle that opens the three-column panel (Foundational / Advanced / Courses); its links were never followed | [home-light-menu](screenshots/home-light-menu.png), [nav-drop-trigger](#mega-menu-trigger), [mega-panel](#mega-menu-panel), [mega-item](#mega-menu-item) |
| Hero video modal | home hero | clicked the video teaser — a Glue modal opens a YouTube embed; captured and closed, the video never played | [home-light-video](screenshots/home-light-video.png), [video-teaser](#video-teaser) |
| FAQ expansion row | UX Design certificate | clicked the row header — the panel's own toggle; measured default and opened | [cert-ux-light-faq-open](screenshots/cert-ux-light-faq-open.png), [expansion-panel](#expansion-panel), [expansion-content](#expansion-content) |
| Mobile navigation drawer | home at 390 | the header hamburger's own press — the drawer slides in | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-drawer-btn](#drawer-toggle), [m-drawer-link](#drawer-link) |
| APAC regional edition | home, every request with a real UA or locale | a 302 from `/` to `/intl/ALL_sg/` — the canonical US surface comes from bare contexts; the APAC shots are variant evidence | [apac-home-light-default](screenshots/apac-home-light-default.png), [apac-mobile-home-light-drawer](screenshots/apac-mobile-home-light-drawer.png) |
| Language select | site footer | never changed — the form posts to services.google.com, an external action | measured as [footer-lang](#locale-select) |
| Enrolment and accounts | Coursera, Google accounts | every 'Get started on Coursera' and sign-in affordance leads off grow.google — measured, never followed | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 19 components were given a real keyboard focus. Glue's ring is a box-shadow, not an outline. 11 draw a 2px box-shadow ring in #1a73e8 `color.palette.blue.600`: `header-logo`, `nav-link`, `nav-drop-trigger`, `mega-item`, `promo-link`, `card-link`, `footer-link`, `breadcrumb`, `learn-more-btn`, `m-drawer-link`, `m-skip-link`. 5 draw a 2px box-shadow ring in #185abc `color.palette.blue.800`: `hero-cta`, `video-teaser`, `cert-cta`, `ai-link`, `m-hero-cta`. 1 draw a 1px auto outline in #101010 (offset 0px): `footer-lang`. 1 draw a 2px box-shadow ring in #4285f4 `color.palette.blue.500`: `tab`. 1 draw no ring, so a keyboard user sees no change: `m-drawer-btn`. 11 also set a transparent outline, which draws nothing: `promo-link`, `hero-cta`, `video-teaser`, `card-link`, `footer-link`, `breadcrumb`, `learn-more-btn`, `tab`, `cert-cta`, `ai-link`, `m-hero-cta`. Focus could not be captured on 1 more (keyboard focus never landed, so their readings are left out): `promo-banner`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover) — nothing a real press would submit or open was ever pressed. A pressed filled button keeps the hover's #185abc fill and deepens the elevation (0 1px 2px / 0 2px 6px rgba(60,64,67)); pressed text links keep the faint brand wash (rgba(26,115,232,0.1)); the 5px `outline: auto` Chrome draws on forced :active is the forced-state artifact, not a page style.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `ease-in` | opacity | mega-panel |
| 0.2s | `ease` | background-color, box-shadow, color | ai-link, breadcrumb, cert-cta, footer-link, header-logo, hero-cta, learn-more-btn, m-drawer-link and more |
| 0.2s | `ease-in` | height | expansion-content |
| 0.25s | `ease` | box-shadow | card-link |
| 0.3s | `ease` | top | tab-bar |

**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).

| Page | 1440 | 1920 | 1024 | 390 |
|---|---|---|---|---|
| home | content x 0, 1440 wide; grid 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 gap 64px | content x 0, 1920 wide; grid 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 gap 64px | content x 0, 1024 wide; grid 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 gap 48px | content x 0, 390 wide; grid 69.5 69.5 69.5 69.5 gap 28px |
| certificates | content x 0, 1440 wide; grid 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 gap 64px | content x 0, 1920 wide; grid 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 gap 64px | content x 0, 1024 wide; grid 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 gap 48px | content x 0, 390 wide; grid 69.5 69.5 69.5 69.5 gap 28px |
| cert-ux | content x 0, 1440 wide; grid 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 gap 64px | content x 0, 1920 wide; grid 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 gap 64px | content x 0, 1024 wide; grid 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 gap 48px | content x 0, 390 wide; grid 69.5 69.5 69.5 69.5 gap 28px |
| ai | content x 0, 1440 wide; grid 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 gap 64px | content x 0, 1920 wide; grid 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 101.3 gap 64px | content x 0, 1024 wide; grid 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 35.3 gap 48px | content x 0, 390 wide; grid 69.5 69.5 69.5 69.5 gap 28px |
| stories | content x 0, 1440 wide; grid 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 gap 64px | - | - | - |
| mission | content x 0, 1440 wide; grid 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 61.3 gap 64px | - | - | - |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Promo banner](#promo-banner) | 575.83 x 25 | - | - | transparent | none | 1px 0px 0px 0px |
| [Video teaser](#video-teaser) | 616 x 346.5 | - | - | transparent | none | 0 |
| [Content card](#content-card) | 1296 x 285 | - | - | transparent | none | 0 |
| [Card link](#card-link) | 616 x 205 | - | 8px | #ffffff `color.palette.grey.0` | none | 0 |
| [Mega-menu panel](#mega-menu-panel) | 1440 x 623 | - | 0px 0px 50px 50px | #ffffff `color.palette.grey.0` | rgba(60, 64, 67, 0.2) 0px 15px 20px 0px | 5px 0px |
| [Section tabs](#section-tabs) | 721 x 48 | - | 120px | #ffffff `color.palette.grey.0` | rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 1px 3px 1px | 0 |
| [Certificate card](#certificate-card) | 369.75 x 386 | - | - | transparent | none | 0 |
| [Dark hero](#dark-hero) | 1440 x 720 | - | - | #18191d | none | 0 |
| [Graduate badge card](#graduate-badge-card) | 377.91 x 68 | - | - | transparent | none | 0 |
| [Expansion panel](#expansion-panel) | 1296 x 93 | T: 1px solid #dadce0 `color.palette.grey.300` | - | transparent | none | 0 |
| [AI card](#ai-card) | 1069.33 x 702.25 | - | - | transparent | none | 0 |
| [Footer](#footer) | 1440 x 837 | - | - | #eff2f7 | none | 0 |

## Components

### Site chrome

The header on every page: the "Grow with Google" lockup, the Career Certificates / AI Training / For Partners / Stories & Resources nav, its dropdown mega-menus and the promo banner. The fixed header is white at every scroll depth; the mega-menu is a full-bleed 1440px panel under it.

#### Site header
The glue top bar: the "Grow with Google" wordmark, the Career Certificates / AI Training / For Partners / Stories & Resources nav and its dropdown mega-menus. Read as `header` on the home page.

**Values (default).** size 1440 x 64; background #ffffff `color.palette.grey.0`; text Google Sans Flex 16/24 500, #3c4043 `color.palette.grey.800`.

![Site header default](components/crops/header-default.png)

#### Logo
The "Grow with Google" lockup in the header (a .glue-header__logo-link anchor in the desktop bar — the Google mark plus the "Grow with Google" img wordmark, 210x48; the mobile bar carries a second display:none copy). Read as `header-logo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 210 x 48; padding 0px 9px; radius 4px; background transparent; text Google Sans Flex 16/24 500, #5f6368 `color.palette.grey.700`; transition background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease |
| hover | text Google Sans Flex 16/24 500, #202124 `color.palette.grey.900` |
| focus-visible | background #f8f9fa `color.palette.grey.50`; shadow #1a73e8 0px 0px 0px 2px; text Google Sans Flex 16/24 500, #3186ff |
| pressed | text Google Sans Flex 16/24 500, #202124 `color.palette.grey.900` |

![Logo default](components/crops/header-logo-default.png) ![Logo focus-visible](components/crops/header-logo-focus-visible.png) ![Logo pressed](components/crops/header-logo-pressed.png)

#### Nav link
A header nav link (AI Training); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 107.75 x 48; padding 0px 12px; radius 4px; background transparent; text Google Sans Flex 16/24 500, #3c4043 `color.palette.grey.800`; transition background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease |
| focus-visible | background #f8f9fa `color.palette.grey.50`; shadow #1a73e8 0px 0px 0px 2px; text Google Sans Flex 16/24 500, #3186ff |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Mega-menu trigger
The "Career Certificates" nav item that opens the three-column mega-menu (Foundational / Advanced / Courses). opened was measured after clicking it — a local UI toggle. Read as `nav-drop-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 174.75 x 48; padding 0px 12px; radius 4px; background transparent; text Google Sans Flex 16/24 500, #3c4043 `color.palette.grey.800`; transition background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease |
| focus-visible | background #f8f9fa `color.palette.grey.50`; shadow #1a73e8 0px 0px 0px 2px; text Google Sans Flex 16/24 500, #3186ff |

![Mega-menu trigger default](components/crops/nav-drop-trigger-default.png) ![Mega-menu trigger hover](components/crops/nav-drop-trigger-hover.png) ![Mega-menu trigger focus-visible](components/crops/nav-drop-trigger-focus-visible.png) ![Mega-menu trigger pressed](components/crops/nav-drop-trigger-pressed.png) ![Mega-menu trigger opened](components/crops/nav-drop-trigger-opened.png)

#### Mega-menu panel
The opened mega-menu panel: Foundational, Advanced and Courses columns. Read as `mega-panel` on the home page.

**Values (default).** size 1440 x 623; padding 5px 0px; radius 0px 0px 50px 50px; background #ffffff `color.palette.grey.0`; shadow rgba(60, 64, 67, 0.2) 0px 15px 20px 0px; outline 1px solid transparent, offset 0px; text Google Sans Flex 18/27 400, #202124 `color.palette.grey.900`; transition opacity 0.15s ease-in.

![Mega-menu panel default](components/crops/mega-panel-default.png)

#### Mega-menu item
A certificate link inside the opened mega-menu; measured while the menu was held open, never followed. Read as `mega-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 272 x 48; padding 8px 0px; border L: 2px solid transparent; radius 4px 0px 0px 4px; background transparent; text Google Sans Flex 16/24 400, #202124 `color.palette.grey.900`; transition background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease |
| hover | background #f8f9fa `color.palette.grey.50`; text Google Sans Flex 16/24 400, #3186ff |
| focus-visible | background #f8f9fa `color.palette.grey.50`; shadow #1a73e8 0px 0px 0px 2px; text Google Sans Flex 16/24 400, #3186ff |
| pressed | background #f8f9fa `color.palette.grey.50`; text Google Sans Flex 16/24 400, #3186ff |

Child layers that carry the look: a 272x48 border 2px transparent radius 4px 0px 0px 4px.

![Mega-menu item default](components/crops/mega-item-default.png) ![Mega-menu item hover](components/crops/mega-item-hover.png) ![Mega-menu item focus-visible](components/crops/mega-item-focus-visible.png) ![Mega-menu item pressed](components/crops/mega-item-pressed.png)

### Home

The US home page: the promo banner, a video-led hero ("Grow your career or business"), the Career Certificate CTA, a sectioned story and the announcement card row.

#### Promo banner
The blue "New! Enroll in the AI Certificate and learn vibe coding…" promotion banner under the header — the whole banner is one anchor. Read as `promo-banner` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 575.83 x 25; padding 1px 0px 0px 0px; background transparent; text Google Sans Flex 16/24 500, #ffffff `color.palette.grey.0` |

![Promo banner default](components/crops/promo-banner-default.png) ![Promo banner hover](components/crops/promo-banner-hover.png) ![Promo banner pressed](components/crops/promo-banner-pressed.png)

#### Promo link
The banner's "Enroll now →" tail; measured, never followed. Read as `promo-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 119 x 26; padding 0px 1px; border 1px solid transparent; radius 4px; background transparent; text Google Sans Flex 16/24 700, #ffffff `color.palette.grey.0`; transition background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease; icon 18 x 18, #ffffff `color.palette.grey.0` |
| focus-visible | shadow #1a73e8 0px 0px 0px 2px; outline 2px solid transparent, offset 1px; transition none |
| pressed | background rgba(26, 115, 232, 0.04); outline 5px auto #101010, offset 0px; text Google Sans Flex 16/24 700, #3186ff; icon 18 x 18, #3186ff |

![Promo link default](components/crops/promo-link-default.png) ![Promo link hover](components/crops/promo-link-hover.png) ![Promo link focus-visible](components/crops/promo-link-focus-visible.png) ![Promo link pressed](components/crops/promo-link-pressed.png)

#### Hero headline
The home display heading. Read as `hero-h1` on the home page.

**Values (default).** size 616 x 88; background transparent; text Google Sans Flex 36/44 400, #202124 `color.palette.grey.900`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero CTA
The hero's blue pill action (glue-button--high-emphasis); measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 142.5 x 50; padding 12px 24px; border 1px solid transparent; radius 48px; background #3186ff; text Google Sans Flex 16/24 500, #ffffff `color.palette.grey.0`; transition background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease |
| focus-visible | border 1px solid #ffffff `color.palette.grey.0`; background #185abc `color.palette.blue.800`; shadow #185abc 0px 0px 0px 2px; outline 2px solid transparent, offset 1px; transition none |
| pressed | background #185abc `color.palette.blue.800`; shadow rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 2px 6px 2px; outline 5px auto #101010, offset 0px |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Video teaser
The hero video preview with the 48px play overlay; clicking it opens a glue-modal carrying a YouTube embed. Measured at rest; the modal was screenshotted in the capture pass and closed. Read as `video-teaser` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 616 x 346.5; background transparent; text Google Sans Flex 11/16 500, #202124 `color.palette.grey.900`; icon 48 x 48, #ffffff `color.palette.grey.0` |
| focus-visible | radius 4px; shadow #185abc 0px 0px 0px 2px; outline 2px solid transparent, offset 0px |

Child layers that carry the look: span 61.5x20 background rgba(255, 255, 255, 0.62) radius 100px.

![Video teaser default](components/crops/video-teaser-default.png) ![Video teaser hover](components/crops/video-teaser-hover.png) ![Video teaser focus-visible](components/crops/video-teaser-focus-visible.png) ![Video teaser pressed](components/crops/video-teaser-pressed.png)

#### Section heading
A section heading on the marketing home. Read as `h2` on the home page.

**Values (default).** size 575 x 46.28; background transparent; text Google Sans Flex 36/46.28 400, #202124 `color.palette.grey.900`.

![Section heading default](components/crops/h2-default.png)

#### Body paragraph
A body paragraph on the marketing home. Read as `body-p` on the home page.

**Values (default).** size 394.66 x 42; background transparent; text Google Sans Flex 14/21 400, #3c4043 `color.palette.grey.800`.

![Body paragraph default](components/crops/body-p-default.png)

#### Content card
A bordered content card on the home (the "New vibe coding course…" announcement cards). Read as `card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1296 x 285; background transparent; text Google Sans Flex 20/28 400, #202124 `color.palette.grey.900`; icon 24 x 24, #336ef3 |

Child layers that carry the look: a 616x205 background #ffffff `color.palette.grey.0` radius 8px shadow transparent 0px 0px 0px 0px; div 616x205 border 1px #202124 `color.palette.grey.900` radius 32px; a 616x205 background #ffffff `color.palette.grey.0` radius 8px shadow transparent 0px 0px 0px 0px.

![Content card default](components/crops/card-default.png) ![Content card hover](components/crops/card-hover.png)

#### Card link
The "Learn more →" link inside a card; measured, never followed. Read as `card-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 616 x 205; radius 8px; background #ffffff `color.palette.grey.0`; text Google Sans Flex 20/28 400, #202124 `color.palette.grey.900`; transition box-shadow 0.25s ease; icon 24 x 24, #336ef3 |
| focus-visible | shadow #1a73e8 0px 0px 0px 2px; outline 2px solid transparent, offset 1px |
| pressed | outline 2px solid transparent, offset 0px |

![Card link default](components/crops/card-link-default.png) ![Card link hover](components/crops/card-link-hover.png) ![Card link focus-visible](components/crops/card-link-focus-visible.png) ![Card link pressed](components/crops/card-link-pressed.png)

### Certificates

The /certificates catalog: the breadcrumb, the display heading, the statistics band, the Learn more anchor, the glue-jumplinks pill tab bar and the certificate card grid on the light-blue band.

#### Breadcrumb link
The "Grow with Google" link opening the breadcrumb trail above the catalog heading. Read as `breadcrumb` on the certificates catalog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 111.2 x 15; radius 4px; background transparent; text Google Sans Flex 12/20 400, #3186ff; transition background-color 0.2s ease, color 0.2s ease |
| hover | background rgba(26, 115, 232, 0.04) |
| focus-visible | background rgba(26, 115, 232, 0.12); shadow #1a73e8 0px 0px 0px 2px; outline 2px solid transparent, offset 1px |
| pressed | background rgba(26, 115, 232, 0.1); outline 5px auto #101010, offset 0px |

![Breadcrumb link default](components/crops/breadcrumb-default.png) ![Breadcrumb link hover](components/crops/breadcrumb-hover.png) ![Breadcrumb link focus-visible](components/crops/breadcrumb-focus-visible.png) ![Breadcrumb link pressed](components/crops/breadcrumb-pressed.png)

#### Eyebrow
The "GOOGLE CAREER CERTIFICATES" eyebrow over the page heading. Read as `eyebrow` on the certificates catalog page.

**Values (default).** size 502.66 x 24; background transparent; text Google Sans Flex 14/24 500, #202124 `color.palette.grey.900`.

![Eyebrow default](components/crops/eyebrow-default.png)

#### Certificates headline
"Job-ready skills you can put to work" — the catalog display heading with a coloured first phrase. Read as `certs-h1` on the certificates catalog page.

**Values (default).** size 502.66 x 112; background transparent; text Google Sans Flex 48/56 400, #336ef3.

![Certificates headline default](components/crops/certs-h1-default.png)

#### Stat number
A coloured stat figure in the certificates statistics band (3-6 mos / 70%+ / $102,000+ / 1.7M+ — red, blue, yellow and green numbers over captions). Read as `stat-chip` on the certificates catalog page.

**Values (default).** size 276 x 57.59; background transparent; text Google Sans Flex 48/57.6 400, #c5221f `color.palette.red.700`.

![Stat number default](components/crops/stat-chip-default.png)

#### Learn more button
The blue pill "Learn more ↓" anchor that scrolls to the catalog; measured, never followed. Read as `learn-more-btn` on the certificates catalog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 84 x 20; radius 4px; background transparent; text Google Sans Flex 16/24 400, #3186ff; transition background-color 0.2s ease, color 0.2s ease |
| hover | background rgba(26, 115, 232, 0.04) |
| focus-visible | background rgba(26, 115, 232, 0.12); shadow #1a73e8 0px 0px 0px 2px; outline 2px solid transparent, offset 1px |
| pressed | background rgba(26, 115, 232, 0.1); outline 5px auto #101010, offset 0px |

![Learn more button default](components/crops/learn-more-btn-default.png) ![Learn more button hover](components/crops/learn-more-btn-hover.png) ![Learn more button focus-visible](components/crops/learn-more-btn-focus-visible.png) ![Learn more button pressed](components/crops/learn-more-btn-pressed.png)

#### Section tabs
The pill tab bar (Overview / Professional Certificates / Path to jobs / AI training / FAQs) — glue-jumplinks in-page anchors. Read as `tab-bar` on the certificates catalog page.

**Values (default).** size 721 x 48; radius 120px; background #ffffff `color.palette.grey.0`; shadow rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 1px 3px 1px; text Google Sans Flex 16/20 500, #3c4043 `color.palette.grey.800`; transition top 0.3s ease; icon 18 x 18, #5f6368 `color.palette.grey.700`.

![Section tabs default](components/crops/tab-bar-default.png)

#### Tab item
One pill tab in the jumplinks bar; measured, never followed. Read as `tab` on the certificates catalog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 97 x 38; padding 7px 8px; border 2px solid transparent; background transparent; text Google Sans Flex 16/20 500, #3c4043 `color.palette.grey.800`; transition background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease |
| hover | background #f8f9fa `color.palette.grey.50`; text Google Sans Flex 16/20 500, #202124 `color.palette.grey.900` |
| focus-visible | radius 4px; background #ffffff `color.palette.grey.0`; shadow #4285f4 0px 0px 0px 2px; outline 2px solid transparent, offset 1px; text Google Sans Flex 16/20 500, #202124 `color.palette.grey.900` |
| pressed | background #f1f3f4 `color.palette.grey.100`; text Google Sans Flex 16/20 500, #202124 `color.palette.grey.900` |

![Tab item default](components/crops/tab-default.png) ![Tab item hover](components/crops/tab-hover.png) ![Tab item focus-visible](components/crops/tab-focus-visible.png) ![Tab item pressed](components/crops/tab-pressed.png)

#### Certificate card
A certificate card in the "Foundational certificates" grid — a glue-grid__col cell painted as a white rounded card on the light-blue band: icon, title, rating, blurb, "If you like:" line and a "Get started on Coursera" pill. Read as `cert-card` on the certificates catalog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 369.75 x 386; background transparent; text Google Sans Flex 28/36 400, #202124 `color.palette.grey.900` |

Child layers that carry the look: a 248.5x50 background #3186ff border 1px transparent radius 48px.

![Certificate card default](components/crops/cert-card-default.png) ![Certificate card hover](components/crops/cert-card-hover.png)

### Certificate detail

A certificate page (/certificates/ux-design/): the dark editorial hero, the Coursera enrol CTA, the graduate badge and the FAQ expansion rows. Every enrolment link was measured, never followed.

#### Dark hero
The certificate page's dark hero band — an editorial dark section on a light-only site. Read as `cert-hero` on the UX Design certificate page.

**Values (default).** size 1440 x 720; background #18191d; text Google Sans Flex 60/72 400, #ffffff `color.palette.grey.0`; icon 25.36 x 25.36, #ffffff `color.palette.grey.0`.

![Dark hero default](components/crops/cert-hero-default.png)

#### Certificate headline
"Google UX Design Certificate" — white display type on the dark hero. Read as `cert-h1` on the UX Design certificate page.

**Values (default).** size 616 x 144; background transparent; text Google Sans Flex 60/72 400, #ffffff `color.palette.grey.0`.

![Certificate headline default](components/crops/cert-h1-default.png)

#### Coursera CTA
The "Get started on Coursera →" button — an outbound enrolment link; its states were measured but it was never followed (no enrolment, no external navigation). Read as `cert-cta` on the UX Design certificate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 254.5 x 50; padding 12px 12px 12px 16px; border 1px solid transparent; radius 48px; background #3186ff; text Google Sans Flex 16/24 500, #ffffff `color.palette.grey.0`; transition background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease; icon 25.36 x 25.36, #ffffff `color.palette.grey.0` |
| hover | background #185abc `color.palette.blue.800`; shadow rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 1px 3px 1px |
| focus-visible | border 1px solid #ffffff `color.palette.grey.0`; background #185abc `color.palette.blue.800`; shadow #185abc 0px 0px 0px 2px; outline 2px solid transparent, offset 1px; transition none |
| pressed | background #185abc `color.palette.blue.800`; shadow rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 2px 6px 2px; outline 5px auto #101010, offset 0px |

![Coursera CTA default](components/crops/cert-cta-default.png) ![Coursera CTA hover](components/crops/cert-cta-hover.png) ![Coursera CTA focus-visible](components/crops/cert-cta-focus-visible.png) ![Coursera CTA pressed](components/crops/cert-cta-pressed.png)

#### Graduate badge card
The "GABE — GOOGLE UX DESIGN GRADUATE" overlay card on the hero photo. Read as `badge-card` on the UX Design certificate page.

**Values (default).** size 377.91 x 68; background transparent; text Google Sans Flex 16/24 400, #3c4043 `color.palette.grey.800`.

![Graduate badge card default](components/crops/badge-card-default.png)

#### Expansion panel
One glue-expansion-panel FAQ row; opened was measured after clicking its header — a local UI toggle. Read as `expansion-panel` on the UX Design certificate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1296 x 93; border T: 1px solid #dadce0 `color.palette.grey.300`; background transparent; text Google Sans Flex 20/30 400, #202124 `color.palette.grey.900`; icon 36 x 36, #202124 `color.palette.grey.900` |
| opened | size 1296 x 213; text Google Sans Flex 20/30 400, #000000; icon 36 x 36, #000000 |

![Expansion panel default](components/crops/expansion-panel-default.png) ![Expansion panel opened](components/crops/expansion-panel-opened.png)

#### Expansion content
An expanded panel's answer block (1296x120, the .glue-expansion-panel__content of the glue-is-expanded row); measured while the row above was held open. Read as `expansion-content` on the UX Design certificate page.

**Values (default).** size 1296 x 120; padding 0px 0px 0px 2px; background transparent; text Google Sans Flex 16/24 400, #3c4043 `color.palette.grey.800`; transition height 0.2s ease-in.

![Expansion content default](components/crops/expansion-content-default.png)

### AI training

The /ai hub: a tinted heading band and the large AI course cards.

#### AI page headline
"Essential AI skills for everyone" — the AI training page heading. Read as `ai-h1` on the AI training page.

**Values (default).** size 502.67 x 144; background transparent; text Google Sans Flex 48/57.6 400, #ffffff `color.palette.grey.0`.

Child layers that carry the look: span 197.5x57.6 image linear-gradient(to right, #3186ff, #7f9cff) radius 50px.

![AI page headline default](components/crops/ai-h1-default.png)

#### AI card
A training/course card on the AI page. Read as `ai-card` on the AI training page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1069.33 x 702.25; background transparent; text Google Sans Flex 20/28 400, #202124 `color.palette.grey.900` |

Child layers that carry the look: button 0x0 background #ffffff `color.palette.grey.0` radius 34px; div 340.3x632.3 radius 8px shadow transparent 0px 0px 0px 0px; div 340.3x632.3 radius 8px shadow transparent 0px 0px 0px 0px.

![AI card default](components/crops/ai-card-default.png) ![AI card hover](components/crops/ai-card-hover.png)

#### AI page CTA
An action on the AI training page; measured, never followed. Read as `ai-link` on the AI training page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 150 x 50; padding 12px 12px 12px 16px; border 1px solid transparent; radius 48px; background #3186ff; text Google Sans Flex 16/24 500, #ffffff `color.palette.grey.0`; transition background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease; icon 18 x 18, #ffffff `color.palette.grey.0` |
| hover | background #185abc `color.palette.blue.800`; shadow rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 1px 3px 1px |
| focus-visible | border 1px solid #ffffff `color.palette.grey.0`; background #185abc `color.palette.blue.800`; shadow #185abc 0px 0px 0px 2px; outline 2px solid transparent, offset 1px; transition none |
| pressed | background #185abc `color.palette.blue.800`; shadow rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 2px 6px 2px; outline 5px auto #101010, offset 0px |

![AI page CTA default](components/crops/ai-link-default.png) ![AI page CTA hover](components/crops/ai-link-hover.png) ![AI page CTA focus-visible](components/crops/ai-link-focus-visible.png) ![AI page CTA pressed](components/crops/ai-link-pressed.png)

### Footer

The site footer: link columns, the legal row and the region/language <select> — measured, never changed (its form posts to services.google.com).

#### Footer
The marketing footer: link columns, social marks, legal links and the locale <select>. Read as `footer` on the home page.

**Values (default).** size 1440 x 837; background #eff2f7; text Google Sans Flex 16/24 500, #202124 `color.palette.grey.900`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 107 x 24; radius 4px; background #eff2f7; text Google Sans Flex 16/24 500, #3c4043 `color.palette.grey.800`; transition background-color 0.2s ease, color 0.2s ease |
| focus-visible | shadow #1a73e8 0px 0px 0px 2px; outline 2px solid transparent, offset 1px |
| pressed | outline 5px auto #101010, offset 0px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Locale select
The footer region/language <select>; measured, never changed — its form posts to services.google.com. Read as `footer-lang` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 233 x 24; padding 0px 24px 0px 2px; background #eff2f7; image an image (data URI); text Google Sans Flex 16/24 500, #3c4043 `color.palette.grey.800` |
| focus-visible | outline 1px auto #101010, offset 0px |

![Locale select default](components/crops/footer-lang-default.png) ![Locale select hover](components/crops/footer-lang-hover.png) ![Locale select focus-visible](components/crops/footer-lang-focus-visible.png) ![Locale select pressed](components/crops/footer-lang-pressed.png)

### Mobile (390 wide)

A few components as a phone draws them, at 390 x 844: the compact header, the drawer toggle, the opened navigation drawer.

#### Mobile top bar
The phone header at 390 wide: wordmark and the drawer toggle. Read as `m-header` on the home (390 wide) page at 390 wide.

**Values (default).** size 362 x 64; background #ffffff `color.palette.grey.0`; text Google Sans Flex 16/24 500, #3c4043 `color.palette.grey.800`; icon 24 x 24, #5f6368 `color.palette.grey.700`.

![Mobile top bar default](components/crops/m-header-default.png)

#### Mobile hero headline
The home display heading at 390 wide. Read as `m-hero-h1` on the home (390 wide) page at 390 wide.

**Values (default).** size 334 x 64; background transparent; text Google Sans Flex 24/32 400, #202124 `color.palette.grey.900`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The hero action at 390 wide; measured, never followed. Read as `m-hero-cta` on the home (390 wide) page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 142.5 x 50; padding 12px 24px; border 1px solid transparent; radius 48px; background #3186ff; text Google Sans Flex 16/24 500, #ffffff `color.palette.grey.0`; transition background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease |
| hover | background #185abc `color.palette.blue.800`; shadow rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 1px 3px 1px |
| focus-visible | border 1px solid #ffffff `color.palette.grey.0`; background #185abc `color.palette.blue.800`; shadow #185abc 0px 0px 0px 2px; outline 2px solid transparent, offset 1px; transition none |
| pressed | background #185abc `color.palette.blue.800`; shadow rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 2px 6px 2px; outline 5px auto #e59700, offset 0px |

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

#### Drawer toggle
The header button that opens the navigation drawer at 390 wide; opened was measured after tapping it — a local UI toggle. Read as `m-drawer-btn` on the home (390 wide) page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed, opened) | size 48 x 48; radius 4px; background transparent; text Google Sans Flex 16/normal 400, #5f6368 `color.palette.grey.700`; icon 24 x 24, #5f6368 `color.palette.grey.700` |

![Drawer toggle default](components/crops/m-drawer-btn-default.png) ![Drawer toggle hover](components/crops/m-drawer-btn-hover.png) ![Drawer toggle focus-visible](components/crops/m-drawer-btn-focus-visible.png) ![Drawer toggle pressed](components/crops/m-drawer-btn-pressed.png) ![Drawer toggle opened](components/crops/m-drawer-btn-opened.png)

#### Drawer link
A link inside the opened navigation drawer (Career Certificates, 326x50); measured while the drawer was held open, never followed. Read as `m-drawer-link` on the home (390 wide) page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 326 x 50; padding 13px 16px 13px 24px; radius 4px 100px 100px 4px; background transparent; text Google Sans Flex 16/24 500, #3c4043 `color.palette.grey.800`; transition background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease; icon 18 x 18, #3c4043 `color.palette.grey.800` |
| focus-visible | shadow #1a73e8 0px 0px 0px 2px; text Google Sans Flex 16/24 500, #3186ff; icon 18 x 18, #3186ff |
| pressed | text Google Sans Flex 16/24 500, #3186ff; icon 18 x 18, #3186ff |

![Drawer link default](components/crops/m-drawer-link-default.png) ![Drawer link hover](components/crops/m-drawer-link-hover.png) ![Drawer link focus-visible](components/crops/m-drawer-link-focus-visible.png) ![Drawer link pressed](components/crops/m-drawer-link-pressed.png)

#### Skip link
The "Jump to Content" skip link — parked off-canvas at y -999, revealed at 39,8 (160x48) by keyboard focus; hover does not apply to a hidden element. Read as `m-skip-link` on the home (390 wide) page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 134.75 x 48; radius 4px 100px 100px 4px; background transparent; text Google Sans Flex 16/24 500, #3c4043 `color.palette.grey.800`; transition background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease |
| focus-visible | size 160 x 48; radius 4px; background #f8f9fa `color.palette.grey.50`; shadow #1a73e8 0px 0px 0px 2px; text Google Sans Flex 16/24 500, #3186ff |

![Skip link default](components/crops/m-skip-link-default.png) ![Skip link focus-visible](components/crops/m-skip-link-focus-visible.png) ![Skip link pressed](components/crops/m-skip-link-pressed.png)

## Icons

31 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Photography and certificate artwork were left out; these are the interface icons. The SVGs are Google's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [back-to-top](icons/back-to-top.svg) | 18x18 |  | fill | home; certificates; cert-ux; cert-data; ai; ai-pro; stories; mission; partners; employers; news; header; nav | Back To Top |
| [help](icons/help.svg) | 24x24 |  | fill | home; certificates; cert-ux; cert-data; ai; ai-pro; stories; mission; partners; employers; news; header; nav | Help |
| [enroll-now](icons/enroll-now.svg) | 18x18 |  | fill | home; certificates; cert-ux; cert-data; ai; stories; mission; partners; employers; news; header; nav | Enroll now |
| [header-arrow](icons/header-arrow-5130363a.svg) | 36x36 |  | fill | certificates; cert-ux; cert-data; ai; ai-pro; mission | What background knowledge is necessary? / What is a Google C |
| [toggle-all-panels](icons/toggle-all-panels.svg) | 18x18 |  | fill | certificates; cert-ux; cert-data; ai; ai-pro; mission | Toggle all panels |
| [01-05](icons/01-05-0cac1acf.svg) | 12x12 |  | fill | home; cert-ux; cert-data; ai-pro; nav | 01:05 / Watch the video 31:59 / 00:16 |
| [icon-22cc3795](icons/icon-22cc3795.svg) | 24x24 |  | fill | home; news; header; nav | New vibe coding course in the AI Certifi / New Google AI for |
| [01-05](icons/01-05-ac567e7c.svg) | 48x48 |  | fill | home; cert-ux; header; nav | 01:05 / Watch the video 31:59 / Watch the course preview 00: |
| [learn-more](icons/learn-more-439b7c47.svg) | 18x18 |  | fill | certificates; ai; stories | Learn more / Explore stories |
| [play-pause](icons/play-pause-a7bebbe0.svg) | 16x16 |  | fill | certificates; cert-ux; employers | Play/Pause |
| [get-started-on-coursera](icons/get-started-on-coursera-b17716ce.svg) | 25x25 |  | fill | cert-ux; cert-data; ai-pro | Get started on Coursera / Get started |
| [icon-b4f58707](icons/icon-b4f58707.svg) | 24x24 |  | fill | home; header; nav | Google Cybersecurity Certificate Earn a  / Google Data Analy |
| [watch-the-video-17-48](icons/watch-the-video-17-48.svg) | 48x48 |  | fill | cert-data; ai; ai-pro | Watch the video 17:48 / 00:16 / Watch the course preview 01: |
| [icon-f2b58d44](icons/icon-f2b58d44.svg) | 34x34 |  | fill | home; header; nav | Learning on YouTube AI tutorials from sm / Growth Stories Le |
| [get-started-on-coursera](icons/get-started-on-coursera-7d924399.svg) | 25x25 |  | fill | cert-ux; ai-pro | Get started on Coursera |
| [get-started-on-coursera](icons/get-started-on-coursera-e528fbf2.svg) | 25x25 |  | fill | cert-data; ai-pro | Get started on Coursera / View course details |
| [button-prev](icons/button-prev.svg) | 18x18 |  | fill | certificates |  |
| [header-arrow](icons/header-arrow-0cc9dec5.svg) | 24x24 |  | fill | nav | Career Certificates and Courses / AI Training / For Partners |
| [play-pause](icons/play-pause-15aec9e2.svg) | 16x16 |  | fill | cert-data | Play/Pause |
| [go-to-the-next-page](icons/go-to-the-next-page-18bb3a15.svg) | 32x32 |  | fill | news | Go to the next page |
| [drawer-toggle-btn](icons/drawer-toggle-btn.svg) | 24x24 |  | fill | nav | Open the navigation drawer |
| [button-next](icons/button-next.svg) | 18x18 |  | fill | certificates |  |
| [download-the-guide](icons/download-the-guide.svg) | 18x18 |  | fill | ai | Download the guide |
| [course-1-ai-fundamentals](icons/course-1-ai-fundamentals.svg) | 36x36 |  | fill | ai-pro | COURSE 1 AI Fundamentals / COURSE 2 AI for Brainstorming and |
| [get-started](icons/get-started.svg) | 25x25 |  | fill | ai-pro | Get started |
| [learn-more](icons/learn-more-8a704586.svg) | 18x18 |  | fill | news | Learn more |
| [career-certificates](icons/career-certificates-9031c028.svg) | 18x18 |  | fill | nav | Career Certificates / AI Training / For Partners |
| [video-play-pause](icons/video-play-pause.svg) | 16x16 |  | fill | ai | Video Play/pause |
| [go-to-the-next-page](icons/go-to-the-next-page-dd7ffab0.svg) | 32x32 |  | fill | partners | Go to the next page |
| [career-certificates](icons/career-certificates-fcb2de3a.svg) | 18x18 |  | fill | nav | Career Certificates / AI Training / For Partners |
| [load-more](icons/load-more.svg) | 18x18 |  | fill | stories | Load More |

## Gaps

### Pages

- **Enrolment.** Every 'Get started on Coursera' CTA leads to coursera.org — measured in every state, never followed; no course was enrolled in or previewed past grow.google's own pages.
- **Accounts.** grow.google itself has no sign-in (the program pages are fully public); the Google-account and Coursera surfaces its links reach are off-product and were never visited.
- **The hero video.** The teaser opens a Glue modal with a YouTube embed — captured open and closed; the video was never played, so the player controls are not captured.
- **The regional split.** `/` with a real user agent or locale 302s to `/intl/<locale>/` (here, `/intl/ALL_sg/` — the Singapore/global-English edition with a different promo and fewer sections); the package's canonical surface is the US edition bare contexts receive, and the APAC shots are kept as variant evidence, not a second token surface.
- **Other certificate detail pages.** /certificates/data-analytics/ and /certificates/ai-essentials/ share the same template; two were captured whole, the rest are catalog cards.
- **Outbound resources.** The links to grow.google's YouTube channel, the Google for Employers and social marks leave the product; they were never followed.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing; the `outline: auto` ring in a pressed state is Chrome's forced-pseudo artifact, not a page style.
- **Disabled states** were not seen on any public control — the site has no forms to disable.
- **Hover** is a real pointer hover; a handful of controls (the footer links, the mega-menu items) change nothing measurable and read 'same'.

### Themes

grow.google paints light only: no theme control exists in the header, footer or any menu, `prefers-color-scheme: dark` repaints nothing the probe saw, and the stylesheets declare no dark block beyond the glue ramps. The certificate pages' dark hero (`#18191d`) is a section paint — an editorial band, not a theme — and is kept inside the light set as `color.surface.dark`; no dark tokens were inferred from it. The token file therefore ships no dark set.

### Fonts

- **Google Sans Flex** is the variable face (opsz 6-144, wght 100-1000) the whole site paints; the font sheet also requests Google Sans Text, Google Sans, Google Sans Display and Product Sans faces — declared evidence, the computed fontFamily is always the Flex stack.
- The faces are served from fonts.googleapis.com; the style guide falls back to system sans when the variable face is unavailable.

### Screenshots

- Photos, portraits and certificate artwork are Google's content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files. Tall pages split `-full` shots into `.partN` tiles; each `.capture.json` sidecar records the clip.

### Content left out

- Video and animation frames are the one thing screenshots can't carry; the video modal's capture is the closed state plus the open frame.
- No personal data was captured: every page was read signed out and no field was ever filled.
