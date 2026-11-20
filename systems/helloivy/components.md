# Hello Ivy components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Read from www.helloivy.co, app.helloivy.co and the hosted /docs on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Later recaptures merge into the same file, so every entry names the date its own states were read; a state a re-read missed keeps its earlier date and says so. Nothing was signed into, bought, searched, typed or submitted; the only presses were local UI toggles the pages' own chrome provides — the Framer 'Menu' overlay, the footer's real 'Change theme' control, the pricing FAQ accordion, the share page's settings popover and the phone's menu drawer; every link was measured, never followed.

**Where this was read.** Three public surfaces: www.helloivy.co — the Framer marketing site (home, about, features and its feature pages, pricing, project-management and collaboration landing pages, the Notion alternative page, blog, release notes, terms) — app.helloivy.co — the product, seen only at the /login boundary (at rest, never signed into) and the public share route a document link exposes — and the hosted /docs platform, a third surface with its own face (General Sans). Everything behind the login — the real workspace, projects, clients — was never entered. All of that is a boundary listed under Gaps, not captures.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (31 components, 66 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/20.8 400, #000000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (64 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png` where `{theme}` is the surface the page painted at capture: every page boots `light`; `{page}-dark-*` shots are the same marketing page after the footer's own 'Change theme' control repainted `html[toggle-theme=dark]`, verified by the painted surface and switched back after — dark shots exist only on pages where that real control demonstrably repaints (the marketing site); the app and docs surfaces paint light only and have no `dark` shots. Desktop shots are 1440 x 900 at 1x; `-full` shots are the whole page at 1x, bounded with the boundary recorded in the shot's `.capture.json` sidecar (a page whose scroll exceeds the bound is stitched from tiles); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x). `app-*` pages are on app.helloivy.co.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png), [theme-control](screenshots/home-light-theme-control.png) |
| About | `/about` | [default](screenshots/about-dark-default.png), [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Features | `/features` | [default](screenshots/features-dark-default.png), [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| Feature: tasks | `/features/tasks` | [default](screenshots/feature-tasks-light-default.png), [full](screenshots/feature-tasks-light-full.png) |
| Feature: annotate | `/features/annotate` | [default](screenshots/feature-annotate-light-default.png), [full](screenshots/feature-annotate-light-full.png) |
| Feature: client portal | `/features/client-portal` | [default](screenshots/feature-portal-light-default.png), [full](screenshots/feature-portal-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-dark-default.png), [default](screenshots/pricing-light-default.png), [faq-open](screenshots/pricing-light-faq-open.png), [full](screenshots/pricing-light-full.png) |
| Project management | `/project-management` | [default](screenshots/project-management-light-default.png), [full](screenshots/project-management-light-full.png) |
| Collaboration software | `/project-collaboration-software` | [default](screenshots/project-collab-light-default.png), [full](screenshots/project-collab-light-full.png) |
| Alternative: Notion | `/notion-alternative` | [default](screenshots/alt-notion-light-default.png), [full](screenshots/alt-notion-light-full.png) |
| Blog index | `/blog` | [default](screenshots/blog-dark-default.png), [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Blog article | `/blog/announcing-hello-ivy-2-0` | [default](screenshots/blog-post-light-default.png), [full](screenshots/blog-post-light-full.png) |
| Release notes | `/release-notes` | [default](screenshots/release-notes-light-default.png), [full](screenshots/release-notes-light-full.png) |
| Terms | `/terms` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| Docs index | `/docs` | [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png) |
| Docs article | `/docs/create-a-project` | [default](screenshots/doc-page-light-default.png), [full](screenshots/doc-page-light-full.png) |
| App login (rest only) | `app.helloivy.co/login` | [default](screenshots/app-login-light-default.png), [full](screenshots/app-login-light-full.png) |
| Public share document | `app.helloivy.co/…/share/…` | [default](screenshots/app-share-light-default.png), [full](screenshots/app-share-light-full.png), [settings-menu](screenshots/app-share-light-settings-menu.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Features, phone | `/features` | [default](screenshots/mobile-features-light-default.png), [full](screenshots/mobile-features-light-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Blog, phone | `/blog` | [default](screenshots/mobile-blog-light-default.png), [full](screenshots/mobile-blog-light-full.png) |
| App login, phone | `app.helloivy.co/login` | [default](screenshots/mobile-app-login-light-default.png), [full](screenshots/mobile-app-login-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Menu overlay | home | the nav 'Menu' control's own press — Framer's full-screen overlay opened, captured, closed through its own close control (it ignores Escape) | [home-light-menu](screenshots/home-light-menu.png) |
| Mobile menu drawer | home, phone width | the 'Menu' control's own tap at 390px | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |
| FAQ accordion | Pricing | a question row's own press — the answer expanded | [pricing-light-faq-open](screenshots/pricing-light-faq-open.png) |
| Settings popover | public share | the share header's own settings control — the popover opened and captured; nothing in it was submitted | [app-share-light-settings-menu](screenshots/app-share-light-settings-menu.png) |
| Change theme control | home footer | the footer's own 'Change theme' control — verified to repaint the page (html[toggle-theme=dark], body rgb(22,22,26)) before any dark reading; switched back after | [home-light-theme-control](screenshots/home-light-theme-control.png), [home-dark-default](screenshots/home-dark-default.png) |
| Dark theme | marketing pages | the same footer control's real repaint — captured on the pages where the repaint was verified | [home-dark-default](screenshots/home-dark-default.png), [about-dark-default](screenshots/about-dark-default.png), [features-dark-default](screenshots/features-dark-default.png), [pricing-dark-default](screenshots/pricing-dark-default.png), [blog-dark-default](screenshots/blog-dark-default.png) |
| Sign-in, dashboard, workspace | app.helloivy.co behind /login | the auth wall — the login card measured at rest, never signed into | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 5 components were given a real keyboard focus. 5 draw an outline ring: `nav-link` (1px auto #101010, offset 1px), `nav-cta` (1px auto #101010, offset 1px), `hero-cta` (1px auto #101010, offset 1px), `plan-cta` (1px auto #101010, offset 1px), `login-continue` (2px solid transparent, offset 2px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.05s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | login-continue, login-google, login-input-email, login-input-password |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | share-settings |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Top navigation bar](#top-navigation-bar) | 1392 x 116 | - | - | transparent | none | 0 |
| [Menu box](#menu-box) | 160 x 116 | - | - | transparent | none | 24px |
| [Plan card](#plan-card) | 464 x 571 | - | - | transparent | none | 0 |
| [Feature card](#feature-card) | 300 x 40.8 | - | - | transparent | none | 0 |
| [Post card](#post-card) | 464 x 607.08 | - | - | transparent | none | 0 |
| [Docs sidebar](#docs-sidebar) | 200 x 134.78 | - | - | transparent | none | 0 |
| [Login card](#login-card) | 500 x 498.84 | - | - | transparent | none | 0 |
| [Share page header](#share-page-header) | 1000 x 68.75 | - | - | transparent | none | 20px |
| [Media-kit document](#media-kit-document) | 795 x 3376.61 | - | - | transparent | none | 0px 0px 250px 20px |
| [Mobile nav bar](#mobile-nav-bar) | 358 x 116 | - | - | transparent | none | 0 |

## Components

### Site chrome

The marketing shell every www.helloivy.co page carries: the 116px top strip (wordmark, Framer-built nav links, the black pill 'Start for free' CTA, the 'Menu' control whose full-screen overlay is measured under 'opened'), the footer with its links and the real 'Change theme' control whose own press repaints the page dark — measured, never navigated.

#### Top navigation bar
The fixed top strip: the Hello Ivy wordmark, Features / Pricing / About / Docs / Blog links, the "Get Started" CTA and the bordered menu box. Read as `nav-bar` on the home page.
States read on 2026-11-17T12:58:00.620Z (default); 2026-11-17T12:58:03.977Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1392 x 116; background transparent; text Inter 16/19.2 600, #000000 `light.color.ink`; layers ::after transparent 1px none 1; div::after.framer-qTIUJ.framer-o0W2X 1392pxx116px T:1px solid / R:1px solid / B:1px solid / L:1px solid; div::after.framer-1n1l10e 1232pxx116px R:1px solid; a.framer-1lje3.framer-12mefgs 154.0x56.0 #000000 9999px; div::after.framer-p1xt7c 160pxx116px R:1px solid; div.framer-ig1a2v 104.0x1.0 #000000; div.framer-1wtprsd 64.0x1.0 #000000 |
| dark | text Inter 16/19.2 600, #edecda; layers ::after transparent 1px none 1; div::after.framer-qTIUJ.framer-o0W2X 1392pxx116px T:1px solid / R:1px solid / B:1px solid / L:1px solid; div::after.framer-1n1l10e 1232pxx116px R:1px solid; a.framer-1lje3.framer-12mefgs 154.0x56.0 #faf6f0 9999px; div::after.framer-p1xt7c 160pxx116px R:1px solid; div.framer-ig1a2v 104.0x1.0 #edecda; div.framer-1wtprsd 64.0x1.0 #edecda |

Child layers that carry the look: div::after 1392pxx116px border 1px solid; div::after 1232pxx116px border 1px solid; a 154x56 background #000000 `light.color.ink` radius 9999px.

![Top navigation bar default](components/crops/nav-bar-default.png) ![Top navigation bar dark](components/crops/nav-bar-dark.png)

#### Nav link
A nav item in the top strip ("Pricing"). Read as `nav-link` on the home page.
States read on 2026-11-17T12:58:07.203Z (default); 2026-11-17T12:58:09.072Z (hover); 2026-11-17T12:58:10.355Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 55 x 20; background transparent; text Inter 16/19.2 600, #000000 `light.color.ink` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-text.framer-styles-preset-16lr516 55.0x20.0 1px auto #101010 offset 1px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png)

#### "Get Started" nav button
The solid call-to-action at the right of the nav — links to app.helloivy.co; measured, never followed. Read as `nav-cta` on the home page.
States read on 2026-11-17T12:58:11.195Z (default); 2026-11-17T12:58:13.080Z (hover); 2026-11-17T12:58:14.400Z (focus-visible); 2026-11-17T12:58:16.026Z (pressed); 2026-11-17T12:58:19.279Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 154 x 56; padding 15px 30px; radius 9999px; background #000000 `light.color.ink`; text Inter 16/19.2 600, #ffffff `light.color.inverseSurface` |
| hover | opacity 0.8 |
| focus-visible | outline 1px auto #101010, offset 1px |
| dark | background #faf6f0 `light.color.ground`; text Inter 16/19.2 600, #000000 `light.color.ink` |

!["Get Started" nav button default](components/crops/nav-cta-default.png) !["Get Started" nav button hover](components/crops/nav-cta-hover.png) !["Get Started" nav button focus-visible](components/crops/nav-cta-focus-visible.png) !["Get Started" nav button pressed](components/crops/nav-cta-pressed.png) !["Get Started" nav button dark](components/crops/nav-cta-dark.png)

#### Menu box
The bordered hamburger box at the nav's right edge — opens the 01 HOME / 02 FEATURES … overlay. "opened" is its own press, closed with Escape. Read as `nav-menu-box` on the home page.
States read on 2026-11-17T12:58:22.567Z (default); 2026-11-17T12:58:24.454Z (hover); 2026-11-17T12:58:28.203Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 160 x 116; padding 24px; background transparent; text sans-serif 12/normal 400, #000000 `light.color.ink`; layers ::after transparent 0px none 1; div::after.framer-p1xt7c 160pxx116px R:1px solid; div.framer-ig1a2v 104.0x1.0 #000000; div.framer-1wtprsd 64.0x1.0 #000000; div.framer-4opjpw 104.0x1.0 #000000 |
| hover | layers ::after transparent 0px none 1; div::after.framer-p1xt7c 160pxx116px R:1px solid; div.framer-ig1a2v 104.0x1.0 #000000; div.framer-1wtprsd 104.0x1.0 #000000; div.framer-4opjpw 104.0x1.0 #000000 |
| opened | size 1440 x 381.02; padding 0px 0px 0px 48px; text Inter 24/33.6 500, #000000 `light.color.ink`; layers none |

Child layers that carry the look: div::after 160pxx116px border 1px solid; div 104x1 background #000000 `light.color.ink`; div 64x1 background #000000 `light.color.ink`.

![Menu box default](components/crops/nav-menu-box-default.png) ![Menu box hover](components/crops/nav-menu-box-hover.png) ![Menu box opened](components/crops/nav-menu-box-opened.png)

#### Footer
The page footer: product/resource columns, the social icons, the "Change theme" control and the "Try it for free" CTA. Read as `footer` on the home page.
States read on 2026-11-17T12:59:06.366Z (default); 2026-11-17T12:59:09.922Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1392 x 560.41; background transparent; text Unbounded 62/68.2 500, #000000 `light.color.ink`; icon 48 x 48, #000000 `light.color.ink`; layers ::after transparent 1px none 1; div::after.framer-MCeyU.framer-BAp5c 1392pxx560.406px T:1px solid / R:1px solid / B:1px solid / L:1px solid; div::after.framer-cmnq2x 1392pxx116.203px B:1px solid; div.framer-1r83dga 9.0x9.0 #000000 100px; div::after.framer-ivcetf 1392pxx377px B:1px solid; div::after.framer-1ddini9 278.391pxx377px R:1px solid; div::after.framer-14gy5od 278.406pxx377px R:1px solid |
| dark | text Unbounded 62/68.2 500, #edecda; icon 48 x 48, #edecda; layers ::after transparent 1px none 1; div::after.framer-MCeyU.framer-BAp5c 1392pxx560.406px T:1px solid / R:1px solid / B:1px solid / L:1px solid; div::after.framer-cmnq2x 1392pxx116.203px B:1px solid; div.framer-1r83dga 9.0x9.0 #edecda 100px; div::after.framer-ivcetf 1392pxx377px B:1px solid; div::after.framer-1ddini9 278.391pxx377px R:1px solid; div::after.framer-14gy5od 278.406pxx377px R:1px solid |

Child layers that carry the look: div::after 1392pxx560.406px border 1px solid; div::after 1392pxx116.203px border 1px solid; div 9x9 background #000000 `light.color.ink` radius 100px.

![Footer default](components/crops/footer-default.png) ![Footer dark](components/crops/footer-dark.png)

#### "Change theme" control
The footer's own theme toggle — the control that repaints html[toggle-theme] and writes localStorage.currentToggleState. Measured at rest; the painted dark pass lives on the `dark` states of other components. Read as `theme-control` on the home page.
States read on 2026-11-17T12:59:13.172Z (default); 2026-11-17T12:59:15.023Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 96 x 21; background transparent; text Inter 14/21 400, #000000 `light.color.ink` |

!["Change theme" control default](components/crops/theme-control-default.png) !["Change theme" control hover](components/crops/theme-control-hover.png)

#### Footer link
A footer column link (a product page) — an anchor inside the measured footer block. Read as `footer-link` on the home page.
States read on 2026-11-17T12:59:15.868Z (default); 2026-11-17T12:59:17.689Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 34 x 17; background transparent; text Inter 14/22 400, #000000 `light.color.ink` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png)

### Marketing

The home page's editorial layer: the Unbounded display hero (heading, lead copy, the pill CTA) and the mid-page section headings.

#### Hero heading (h1)
The page's headline — the largest display type on the site. Read as `hero-heading` on the home page.
States read on 2026-11-17T12:58:40.019Z (default); 2026-11-17T12:58:43.483Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1344 x 180.41; background transparent; text Unbounded 82/90.2 500, #000000 `light.color.ink` |
| dark | text Unbounded 82/90.2 500, #faf6f0 `light.color.ground` |

![Hero heading (h1) default](components/crops/hero-heading-default.png) ![Hero heading (h1) dark](components/crops/hero-heading-dark.png)

#### Hero paragraph
The supporting paragraph under the headline. Read as `hero-copy` on the home page.
Read on 2026-11-17T12:58:46.931Z.

**Values (default).** size 1238 x 121.5; background transparent; text Inter 27/40.5 400, #000000 `light.color.ink`.

![Hero paragraph default](components/crops/hero-copy-default.png)

#### Hero call-to-action
The trial CTA — the floating "Try it for free" pill painted bottom-right on the marketing pages — links to the app, measured never followed. Read as `hero-cta` on the home page.
States read on 2026-11-17T12:58:47.813Z (default); 2026-11-17T12:58:49.706Z (hover); 2026-11-17T12:58:51.025Z (focus-visible); 2026-11-17T12:58:52.712Z (pressed); 2026-11-17T12:58:55.969Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 196 x 56; padding 15px 30px; radius 9999px; background #000000 `light.color.ink`; text Inter 16/19.2 600, #ffffff `light.color.inverseSurface`; icon 17 x 22, #0000ee |
| hover | opacity 0.8 |
| focus-visible | outline 1px auto #101010, offset 1px |
| dark | background #faf6f0 `light.color.ground`; text Inter 16/19.2 600, #000000 `light.color.ink`; icon 17 x 22, #9e9eff |
| pressed | icon 17 x 22, #ff0000 |

![Hero call-to-action default](components/crops/hero-cta-default.png) ![Hero call-to-action hover](components/crops/hero-cta-hover.png) ![Hero call-to-action focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero call-to-action dark](components/crops/hero-cta-dark.png) ![Hero call-to-action pressed](components/crops/hero-cta-pressed.png)

#### Section heading (h3)
A mid-page section heading — the page's display type below the h1. Read as `section-heading` on the home page.
States read on 2026-11-17T12:58:59.409Z (default); 2026-11-17T12:59:02.785Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 800 x 136.41; background transparent; text Unbounded 62/68.2 500, #000000 `light.color.ink` |
| dark | text Unbounded 62/68.2 500, #edecda |

![Section heading (h3) default](components/crops/section-heading-default.png) ![Section heading (h3) dark](components/crops/section-heading-dark.png)

### Pricing

The /pricing page: the plan column cards, their pill CTAs, and the FAQ accordion whose question rows open answers locally.

#### Plan card
A pricing card ("Grow" / "Business" / "Enterprise"): name, price, allowance rows and its CTA. Read as `plan-card` on the pricing page.
States read on 2026-11-17T12:59:29.636Z (default); 2026-11-17T12:59:33.111Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 464 x 571; background transparent; text Unbounded 20/28 500, #000000 `light.color.ink`; icon 20 x 20, #000000 `light.color.ink`; layers div::after.framer-1fhyswc 464pxx166.391px B:1px solid; a.framer-vVI5g.framer-4vbkq 416.0x49.6 #000000 |
| dark | text Unbounded 20/28 500, #edecda; icon 20 x 20, #ffffff `light.color.inverseSurface`; layers div::after.framer-1fhyswc 464pxx166.391px B:1px solid; a.framer-vVI5g.framer-4vbkq 416.0x49.6 #edecda |

Child layers that carry the look: div::after 464pxx166.391px border 1px solid; a 416x49.6 background #000000 `light.color.ink`.

![Plan card default](components/crops/plan-card-default.png) ![Plan card dark](components/crops/plan-card-dark.png)

#### Plan CTA button
A plan's call-to-action inside the measured plan card — links to the app; measured, never followed. Read as `plan-cta` on the pricing page.
States read on 2026-11-17T12:59:58.779Z (default); 2026-11-17T13:00:00.630Z (hover); 2026-11-17T13:00:01.954Z (focus-visible); 2026-11-17T13:00:03.679Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 416 x 49.59; padding 12px 20px; background #000000 `light.color.ink`; text Unbounded 16/25.6 500, #faf6f0 `light.color.ground` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Plan CTA button default](components/crops/plan-cta-default.png) ![Plan CTA button hover](components/crops/plan-cta-hover.png) ![Plan CTA button focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA button pressed](components/crops/plan-cta-pressed.png)

#### FAQ accordion question
A question row in the pricing FAQ. "opened" is its own press revealing the answer, pressed again to close. Read as `faq-question` on the pricing page.
States read on 2026-11-17T13:00:04.637Z (default); 2026-11-17T13:00:06.530Z (hover); 2026-11-17T13:00:08.742Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, opened) | size 1300 x 25.59; background transparent; text Inter-Medium 16/25.6 500, #000000 `light.color.ink` |

![FAQ accordion question default](components/crops/faq-question-default.png) ![FAQ accordion question hover](components/crops/faq-question-hover.png) ![FAQ accordion question opened](components/crops/faq-question-opened.png)

### Features

The /features page's feature tile cards — measured at rest and hover.

#### Feature card
A feature tile on /features — an illustration, name and description. Read as `feature-card` on the features page.
States read on 2026-11-17T08:59:42.190Z (default); 2026-11-17T08:59:44.113Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 300 x 40.8; background transparent; text Unbounded 34/40.8 500, #000000 `light.color.ink` |

![Feature card default](components/crops/feature-card-default.png) ![Feature card hover](components/crops/feature-card-hover.png)

### Blog

The /blog index's post cards — measured at rest and hover, never followed.

#### Post card
A post row/card on the blog index — cover, title, excerpt, date. Read as `post-card` on the blog page.
States read on 2026-11-17T09:00:21.265Z (default); 2026-11-17T09:00:37.570Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 464 x 607.08; background transparent; text Inter-Medium 16/25.6 500, #999999; layers ::after transparent 1px none 1; a::after.framer-myzsC.framer-MJX7Q 464pxx607.078px T:1px solid / R:1px solid / B:1px solid / L:1px solid; div::after.framer-inu18k 464pxx424.703px B:1px solid |
| hover | layers ::after transparent 1px none 1; a::after.framer-myzsC.framer-MJX7Q 464pxx607.078px T:1px solid / R:1px solid / B:1px solid / L:1px solid; div::after.framer-inu18k 510.391pxx467.172px B:1px solid |

Child layers that carry the look: a::after 464pxx607.078px border 1px solid; div::after 464pxx424.703px border 1px solid.

![Post card hover](components/crops/post-card-hover.png)

### Docs

The hosted docs platform (a separate surface from the Framer site — General Sans, its own chrome): the left nav rail and its links.

#### Docs sidebar
The docs index navigation — the section list (Getting Started, Main tools, …) beside the content. Read as `docs-nav` on the docs article page.
Read on 2026-11-17T09:00:54.903Z.

**Values (default).** size 200 x 134.78; background transparent; text General Sans 14/19.6 600, #111111.

![Docs sidebar default](components/crops/docs-nav-default.png)

#### Docs nav link
A docs section/article link. Read as `docs-link` on the docs article page.
States read on 2026-11-17T09:01:04.460Z (default); 2026-11-17T09:01:06.262Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 117 x 19.59; background transparent; text General Sans 14/19.6 600, #111111 |

![Docs nav link default](components/crops/docs-link-default.png) ![Docs nav link hover](components/crops/docs-link-hover.png)

### App login

app.helloivy.co/login, at rest only: the centred card (heading, email/password fields, Continue, Google SSO, the sign-up and forgot-password links). Fields were measured, never typed into; Continue was never pressed.

#### Login card
The centred card on app.helloivy.co/login ("Welcome back", email/password fields, Continue, Google). The auth boundary: nothing is entered or submitted. Read as `login-card` on the app login page.
Read on 2026-11-17T12:50:07.120Z.

**Values (default).** size 500 x 498.84; background transparent; text Inter 23/27.6 600, #37352f `core.app.color.ink`; icon 30 x 20, #707b8b; layers input.w-full.outline-none 500.0x48.5 #fcfcfc T:1px solid / R:1px solid / B:1px solid / L:1px solid 2px solid transparent offset 2px 10px; input.w-full.outline-none 500.0x48.5 #fcfcfc T:1px solid / R:1px solid / B:1px solid / L:1px solid 2px solid transparent offset 2px 10px; button.inline-flex.items-center 500.0x53.3 #222222 10px; button.inline-flex.items-center 500.0x56.0 T:2px solid / R:2px soli.

Child layers that carry the look: input 500x48.5 background #fcfcfc `core.component.input.bg` border 1px solid radius 10px; input 500x48.5 background #fcfcfc `core.component.input.bg` border 1px solid radius 10px; button 500x53.3 background #222222 `core.component.button.app.bg` radius 10px.

![Login card default](components/crops/login-card-default.png)

#### Email input
The "Your email" field — measured at rest; nothing is entered. Read as `login-input-email` on the app login page.
States read on 2026-11-17T12:50:07.958Z (default); 2026-11-17T12:50:09.210Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 500 x 48.5; padding 12px 20px; border 1px solid #c4c4c4 `core.component.input.border`; radius 10px; background #fcfcfc `core.component.input.bg`; outline 2px solid transparent, offset 2px; text Inter 15/22.5 400, #222222 `core.component.button.app.bg`; transition all 0.05s cubic-bezier(0.4, 0, 0.2, 1); placeholder #bbbbbb |
| focused | border 1px solid #777777 `core.component.input.borderFocused`; shadow #777777 0px 0px 0px 0.5px; text Inter 15/22.5 400, #000000 `light.color.ink` |

![Email input default](components/crops/login-input-email-default.png) ![Email input focused](components/crops/login-input-email-focused.png)

#### Password input
The "Your password" field — measured at rest; nothing is entered. Read as `login-input-password` on the app login page.
Read on 2026-11-17T12:50:10.062Z.

**Values (default).** size 500 x 48.5; padding 12px 20px; border 1px solid #c4c4c4 `core.component.input.border`; radius 10px; background #fcfcfc `core.component.input.bg`; outline 2px solid transparent, offset 2px; text Inter 15/22.5 400, #222222 `core.component.button.app.bg`; transition all 0.05s cubic-bezier(0.4, 0, 0.2, 1); placeholder #bbbbbb.

![Password input default](components/crops/login-input-password-default.png)

#### "Continue" button
The form's submit — measured, never pressed (it would submit). Read as `login-continue` on the app login page.
States read on 2026-11-17T12:50:10.905Z (default); 2026-11-17T12:50:12.681Z (hover); 2026-11-17T12:50:13.922Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 500 x 53.25; padding 16px 0px; radius 10px; background #222222 `core.component.button.app.bg`; text Inter 17/21.25 500, #ffffff `light.color.inverseSurface`; transition all 0.05s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #000000 `light.color.ink` |
| focus-visible | outline 2px solid transparent, offset 2px |

!["Continue" button default](components/crops/login-continue-default.png) !["Continue" button hover](components/crops/login-continue-hover.png) !["Continue" button focus-visible](components/crops/login-continue-focus-visible.png)

#### "Login with Google" button
The OAuth button — measured, never pressed. Read as `login-google` on the app login page.
States read on 2026-11-17T12:50:14.786Z (default); 2026-11-17T12:50:16.602Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 500 x 56; padding 16px 10px; border 2px solid #000000 `light.color.ink`; radius 10px; background transparent; text Inter 15/18.75 400, #000000 `light.color.ink`; transition all 0.05s cubic-bezier(0.4, 0, 0.2, 1); icon 30 x 20, #707b8b |
| hover | background #fafafa |

!["Login with Google" button default](components/crops/login-google-default.png) !["Login with Google" button hover](components/crops/login-google-hover.png)

#### "Sign up" link
The "Don't have an account yet? Sign up" link — measured, never followed. Read as `login-signup` on the app login page.
States read on 2026-11-17T12:50:17.468Z (default); 2026-11-17T12:50:19.237Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 50 x 17; background transparent; text Inter 14/21 400, #111111 |

!["Sign up" link default](components/crops/login-signup-default.png) !["Sign up" link hover](components/crops/login-signup-hover.png)

#### "Forgot password?" link
The reset link — measured, never followed. Read as `login-forgot` on the app login page.
States read on 2026-11-17T12:50:20.089Z (default); 2026-11-17T12:50:21.881Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 112 x 19.5; background transparent; text Inter 13/19.5 400, #37352f `core.app.color.ink` |

!["Forgot password?" link default](components/crops/login-forgot-default.png) !["Forgot password?" link hover](components/crops/login-forgot-hover.png)

### Share document

The public share route (app.helloivy.co/…/share — a media-kit document anyone with the link can read): the header strip, the settings popover opened through its own control, and the document canvas itself. Nothing was submitted, printed or mailed.

#### Share page header
The document page's top strip — the "hello ivy" name and the Settings button. Read as `share-header` on the public share page.
Read on 2026-11-17T09:16:44.218Z.

**Values (default).** size 1000 x 68.75; padding 20px; background transparent; text Inter 15/22.5 500, #000000 `light.color.ink`.

![Share page header default](components/crops/share-header-default.png)

#### "Settings" button
The document's own settings control — a local UI toggle opening the document menu (Send to mail / Print / word count). "opened" is its own press, closed with Escape. Read as `share-settings` on the public share page.
States read on 2026-11-17T09:16:46.438Z (default); 2026-11-17T09:17:04.804Z (hover); 2026-11-17T09:17:16.018Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 91 x 28.75; padding 5px; background transparent; text Inter 15/18.75 400, #37352f `core.app.color.ink`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.5 |
| hover | opacity none |
| opened | outline 2px solid transparent, offset 2px; opacity none; layers button.inline-flex.items-center 91.0x28.8 2px solid transparent offset 2px |

!["Settings" button default](components/crops/share-settings-default.png) !["Settings" button hover](components/crops/share-settings-hover.png) !["Settings" button opened](components/crops/share-settings-opened.png)

#### Media-kit document
The document canvas — the public marketing disclaimer, the Hello Ivy logo and product screenshots the file carries. Read as `share-doc` on the public share page.
Read on 2026-11-17T09:18:11.413Z.

**Values (default).** size 795 x 3376.61; padding 0px 0px 250px 20px; background transparent; text Inter 16/25.6 400, #323235 `core.app.color.canvasInk`; layers div.relative.mr-10 739.5x557.4 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1.4px 6px 0px, rgba(0, 0, 0, 0.09) 0px 3.6px 12.6px 0px 8px; div.relative.mr-10 739.5x670.3 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1.4px 6px 0px, rgba(0, 0, 0, 0.09) 0px 3.6px 12.6px 0px 8px; div.relative.mr-10 739.5x557.4 transparent 0px 0px 0px.

Child layers that carry the look: div 739.5x557.4 radius 8px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1.4px 6px 0px, rgba(0, 0, 0, 0.09) 0px 3.6px 12.6px 0px; div 739.5x670.3 radius 8px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1.4px 6px 0px, rgba(0, 0, 0, 0.09) 0px 3.6px 12.6px 0px; div 739.5x557.4 radius 8px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1.4px 6px 0px, rgba(0, 0, 0, 0.09) 0px 3.6px 12.6px 0px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Site chrome (mobile)

The 390px surface: the compact top strip and the 'Menu' control's drawer, opened through its own tap.

#### Mobile nav bar
The top strip at 390px — wordmark and the menu box (the menu element's painted ancestor bar). Read as `m-nav-bar` on the home page.
Read on 2026-11-17T12:50:33.519Z.

**Values (default).** size 358 x 116; background transparent; text sans-serif 12/normal 400, #000000 `light.color.ink`; layers ::after transparent 1px none 1; div::after.framer-qTIUJ.framer-o0W2X 358pxx116px T:1px solid / R:1px solid / B:1px solid / L:1px solid; div::after.framer-1n1l10e 198pxx116px R:1px solid; div::after.framer-p1xt7c 160pxx116px R:1px solid; div.framer-ig1a2v 104.0x1.0 #000000; div.framer-1wtprsd 64.0x1.0 #000000; div.framer-4opjpw 104.0x1.0 #000000.

Child layers that carry the look: div::after 358pxx116px border 1px solid; div::after 198pxx116px border 1px solid; div::after 160pxx116px border 1px solid.

![Mobile nav bar default](components/crops/m-nav-bar-default.png)

#### Menu box (drawer open)
The nav menu box at 390px — a real tap opens the full-screen overlay (data-framer-name "Menu"). "opened" is its own tap, closed with Escape. Read as `m-menu-box` on the home page.
Read on 2026-11-17T12:50:37.200Z.

**Values (opened).** size 390 x 343.98; background transparent; text Inter-Medium 16/25.6 500, #000000 `light.color.ink`; layers div::after.framer-k36hk2 44pxx44px T:1px solid / R:1px solid / B:1px solid / L:1px solid; div.framer-13cooux 19.1x19.1 #000000; div.framer-1itw2xu 19.1x19.1 #000000.

Child layers that carry the look: div::after 44pxx44px border 1px solid; div 19.1x19.1 background #000000 `light.color.ink`; div 19.1x19.1 background #000000 `light.color.ink`.

![Menu box (drawer open) opened](components/crops/m-menu-box-opened.png)

### Marketing (mobile)

The 390px home hero — the display heading drops to 32px.

#### Hero heading at 390px
The headline on the phone — the display type compressed to the small width (an h3 at this width). Read as `m-hero-heading` on the home page.
Read on 2026-11-17T12:50:48.903Z.

**Values (default).** size 310 x 192.03; background transparent; text Unbounded 32/38.4 500, #000000 `light.color.ink`.

![Hero heading at 390px default](components/crops/m-hero-heading-default.png)

## Icons

49 distinct inline-SVG icons were collected from the live pages into [icons/](icons) by `tools/capture/icons.mjs`, indexed in [icons/INDEX.tsv](icons/INDEX.tsv): a file is named from `tools/capture/icon-names.tsv` where its geometry hash is listed, else the label or class of the control it sits in, else `icon-<hash>`; colour is kept as `currentColor` wherever it matched the text colour, so each icon recolours from CSS `color` the way it does on the site. The icons are the product's artwork — borrow the set's grammar (sizes, stroke-vs-fill, naming roles), never the artwork itself.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [icon-22e6e660](icons/icon-22e6e660.svg) | 17x17 |  | fill | home; features; feature-tasks; feature-annotate; feature-portal; pricing; about; blog; blog-post; release-notes; project-management; project-collab; alt-notion; terms; nav; dark |  |
| [looks-great-get-started](icons/looks-great-get-started.svg) | 20x20 44x44 48x48 | 0 0 256 256 | fill | home; features; feature-tasks; feature-annotate; feature-portal; pricing; about; blog; blog-post; release-notes; project-management; project-collab; alt-notion; terms; nav; dark | LOOKS GREAT GET STARTED / Sign up |
| [icon-4ec79d1e](icons/icon-4ec79d1e.svg) | 16x16 | 0 0 24 24 | stroke | home; features; feature-tasks; feature-annotate; feature-portal; pricing; about; blog; blog-post; release-notes; project-management; project-collab; alt-notion; terms; nav |  |
| [icon-fa065dc7](icons/icon-fa065dc7.svg) | 40x17 | 0 0 256 256 | fill | home; features; feature-tasks; feature-annotate; feature-portal; pricing; about; blog; blog-post; release-notes; project-management; project-collab; alt-notion; terms; nav |  |
| [try-it-for-free](icons/try-it-for-free.svg) | 17x22 |  | fill | home; features; pricing; nav; dark | Try it for free |
| [icon-10663c0e](icons/icon-10663c0e.svg) | 33x33 | 0 0 256 256 | fill | home; pricing; alt-notion; nav; dark |  |
| [icon-781f7e5f](icons/icon-781f7e5f.svg) | 31x41 |  | fill | home; nav; dark |  |
| [features](icons/features.svg) | 22x22 | 0 0 24 24 | stroke | feature-tasks; feature-annotate; feature-portal; blog-post | FEATURES / BLOG |
| [icon-1b2d580c](icons/icon-1b2d580c.svg) | 20x20 | 0 0 256 256 | fill | pricing |  |
| [icon-3a302b70](icons/icon-3a302b70.svg) | 60x60 | 0 0 24 24 | stroke | project-management; project-collab |  |
| [icon-80f86dad](icons/icon-80f86dad.svg) | 18x18 |  | fill | nav |  |
| [icon-a774d0d1](icons/icon-a774d0d1.svg) | 20x20 | 0 0 256 256 | fill | pricing |  |
| [icon-c97598f2](icons/icon-c97598f2.svg) | 20x20 |  | fill | pricing |  |
| [get-notified](icons/get-notified.svg) | 26x26 | 0 0 256 256 | fill | feature-annotate; feature-portal | Get notified / Real-time feedback and notifications |
| [icon-f167ab6b](icons/icon-f167ab6b.svg) | 26x26 | 0 0 256 256 | fill | feature-annotate; feature-portal | Resolve feedback and approve / Annotations and approvals |
| [drag-drop](icons/drag-drop.svg) | 26x26 | 0 0 256 256 | fill | feature-tasks | Drag & drop |
| [icon-0786a42a](icons/icon-0786a42a.svg) | 26x26 | 0 0 256 256 | fill | feature-portal | An interactive newspaper for your team a |
| [icon-0dcd37b5](icons/icon-0dcd37b5.svg) | 26x26 | 0 0 256 256 | fill | feature-annotate | Real-time image annotation |
| [minimize-task-columns](icons/minimize-task-columns.svg) | 26x26 | 0 0 256 256 | fill | feature-tasks | Minimize task columns |
| [icon-23d5ee50](icons/icon-23d5ee50.svg) | 36x36 |  | fill | alt-notion |  |
| [icon-249e8ecd](icons/icon-249e8ecd.svg) | 17x17 |  | fill | docs |  |
| [icon-31b6e6a5](icons/icon-31b6e6a5.svg) | 26x26 | 0 0 256 256 | fill | feature-tasks | Full-screen or modal view |
| [icon-36995227](icons/icon-36995227.svg) | 24x24 |  | fill | docs | What's new? See all Hello Ivy's latest r |
| [icon-380ae1e0](icons/icon-380ae1e0.svg) | 60x60 | 0 0 24 24 | stroke | feature-portal |  |
| [icon-3a5f6d01](icons/icon-3a5f6d01.svg) | 26x26 | 0 0 256 256 | fill | feature-annotate | From feedback to task in one click |
| [subtasks](icons/subtasks.svg) | 26x26 | 0 0 256 256 | fill | feature-tasks | Subtasks |
| [login-with-google](icons/login-with-google.svg) | 30x20 | 0 0 30 30 | fill | app-login | Login with Google |
| [icon-5fb959c8](icons/icon-5fb959c8.svg) | 60x60 | 0 0 24 24 | stroke | feature-tasks |  |
| [effortless-file-sharing](icons/effortless-file-sharing.svg) | 26x26 | 0 0 256 256 | fill | feature-portal | Effortless file sharing |
| [icon-64fc511b](icons/icon-64fc511b.svg) | 16x16 | 0 0 24 24 | stroke | dark |  |
| [icon-66d70966](icons/icon-66d70966.svg) | 24x24 |  | fill | docs | Just beginning? Start with a step by ste |
| [icon-68adee91](icons/icon-68adee91.svg) | 26x26 | 0 0 256 256 | fill | feature-tasks | Task activity and history |
| [icon-84fb7579](icons/icon-84fb7579.svg) | 24x24 | 0 0 24 24 | stroke | docs | Task management for experts How to manag |
| [icon-9296637f](icons/icon-9296637f.svg) | 40x17 41x17 43x18 44x19 | 0 0 256 256 | fill | dark |  |
| [icon-97a5ccb9](icons/icon-97a5ccb9.svg) | 17x17 |  | fill | doc-page |  |
| [label-tasks](icons/label-tasks.svg) | 26x26 | 0 0 256 256 | fill | feature-tasks | Label tasks |
| [more](icons/more.svg) | 22x22 | 0 0 24 24 | stroke | features | More |
| [icon-9f06f37b](icons/icon-9f06f37b.svg) | 24x24 | 0 0 24 24 | stroke | docs | Tips & Tricks Master the art of Hello Iv |
| [icon-a58786a0](icons/icon-a58786a0.svg) | 60x60 | 0 0 24 24 | stroke | about |  |
| [icon-a74dd1fc](icons/icon-a74dd1fc.svg) | 60x60 | 0 0 24 24 | stroke | feature-annotate |  |
| [shared-taskboards](icons/shared-taskboards.svg) | 26x26 | 0 0 256 256 | fill | feature-portal | Shared taskboards |
| [chat-in-context](icons/chat-in-context.svg) | 26x26 | 0 0 256 256 | fill | feature-tasks | Chat in context |
| [custom-branding](icons/custom-branding.svg) | 26x26 | 0 0 256 256 | fill | feature-portal | Custom branding |
| [mentions](icons/mentions.svg) | 26x26 | 0 0 256 256 | fill | feature-tasks | Mentions |
| [upload-from-figma](icons/upload-from-figma.svg) | 26x26 | 0 0 256 256 | fill | feature-annotate | Upload from Figma |
| [connect-everything](icons/connect-everything.svg) | 26x26 | 0 0 256 256 | fill | feature-tasks | Connect everything |
| [icon-d2a31722](icons/icon-d2a31722.svg) | 26x26 | 0 0 256 256 | fill | feature-tasks | Display options for tasks |
| [share-work-with-anyone](icons/share-work-with-anyone.svg) | 26x26 | 0 0 256 256 | fill | feature-annotate | Share work with anyone |
| [icon-f8edf7f1](icons/icon-f8edf7f1.svg) | 20x20 | 0 0 256 256 | fill | pricing |  |

## Gaps

### The blocked product surfaces

The signed-in product was never entered: **app.helloivy.co/login** and everything behind it (the real workspace, projects, clients, files, settings) stays outside — the login card's fields were measured at rest, never typed into, and 'Continue' was never pressed. The **public share route** is captured as far as a signed-out reader gets: the document, its header and the settings popover opened through its own control — nothing was submitted, printed, mailed or exported. All documented as boundaries, never faked.

### Pages

- **The workspace and every post-auth surface** — the auth wall, see above. The public share document is the only app interior a signed-out reader can reach.
- **/docs content beyond the index and one article** — the hosted docs platform was sampled at its index and the 'create a project' guide; it is a separate platform from the marketing site (its own chrome, General Sans) and light-only — no dark pass exists to capture.
- **Remaining marketing routes** — the other feature pages (feed, chat, docs, files, roadmap, calendar, version-control) and alternative pages (asana, basecamp, clickup, monday) were probed and share the same Framer chrome and theme layer; three feature pages and the Notion alternative were screenshotted as representatives rather than all crawled.
- **Blog articles beyond the sample** — /blog/announcing-hello-ivy-2-0 stands in for the article template.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.
- **The login fields were never typed into** — the email field was given a real keyboard focus for its focused state and nothing was entered; 'Continue', Google SSO and the sign-up/forgot links were measured, never activated.
- **The FAQ accordion and menu overlay** were opened and closed through their own controls — the Framer overlay ignores Escape and takes its own close control; captures were reloaded to a clean state after overlays.
- **The theme control** was pressed to paint dark for the `dark` states and shots, verified by the repainted surface, then switched back — no theme was held across navigations.

### Themes

www.helloivy.co boots `html[toggle-theme=light]` and the footer carries a real 'Change theme' control that repaints `html[toggle-theme=dark]` (persisted in `localStorage.currentToggleState`). `light` is the painted default; `dark` states and `{page}-dark-*` screenshots were painted through that control, verified by the painted surface (the html attribute and the computed background rgb(22,22,26)), and the theme was switched back afterwards. The same re-pointing exists under `@media (prefers-color-scheme: dark)` in the probe. app.helloivy.co has no theme control on its public routes and paints light only — no app dark values are inferred. /docs is light-only.

### Fonts

- **Unbounded** (marketing display), **Inter** (marketing UI + the whole app face, `--main-font-family`) and **General Sans** (docs platform) are declared and measured, not shipped — the style guide falls back to system faces.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The rendered brand strings on the captured pages (the wordmark and copy) are the product's published content.
- The public share document's contents are a published media kit the author chose to share by link; nothing private was captured.

### Content left out

- Marketing copy, blog prose and pricing text are the product's published content; only frames and components were measured.

