# Handshake components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Read from joinhandshake.com's public pages (the App access group from app.joinhandshake.com/access) on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Later recaptures merge into the same file, so every entry names the date its own states were read; a state a re-read missed keeps its earlier date and says so. Nothing was signed into, bought, searched or submitted; the only presses were local UI toggles the pages' own chrome provides — the nav's hover-opened mega menu, the segment switcher, the FAQ and careers accordions, the feature-group tabs and the phone's 'Open menu' button; every link was measured, never followed; no form was submitted.

**Where this was read.** Handshake's signed-out web is two surfaces: the marketing site joinhandshake.com (a Next.js app, plus one Framer-built page at /research/ai/) that serves every public route to a plain load, and the consumer app app.joinhandshake.com whose 'Log in or sign up' page at /access sits behind a Cloudflare managed challenge that clears only intermittently — it was captured on the loads that cleared. The app's /explore feed, /signup, the student registration flow and support.joinhandshake.com never cleared their challenges and are documented boundaries, not captures.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (54 components, 118 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/20.8 400, #000000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (118 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: every page on both surfaces paints light only (no theme class, no control, no prefers-color-scheme rule), so there is no dark pass. Desktop shots are 1440 x 900 at 1x; `-full` shots are the whole document at 1x, bounded at eight 14000px chunks with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). The marketing pages scroll the document; the /learn/ page's 22,630px height is the tallest captured document.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [consent](screenshots/home-light-consent.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [nav-open](screenshots/home-light-nav-open.png) |
| Students | `/students/` | [default](screenshots/students-light-default.png), [full](screenshots/students-light-full.png) |
| Who's hiring | `/students/whos-hiring/` | [default](screenshots/whos-hiring-light-default.png), [full](screenshots/whos-hiring-light-full.png) |
| Employers | `/employers/` | [default](screenshots/employers-light-default.png), [faq-open](screenshots/employers-light-faq-open.png), [full](screenshots/employers-light-full.png), [tab-automate](screenshots/employers-light-tab-automate.png) |
| Pricing | `/employers/pricing/` | [default](screenshots/pricing-light-default.png), [faq-open](screenshots/pricing-light-faq-open.png), [full](screenshots/pricing-light-full.png) |
| Request a demo | `/employers/request-more-info/` | [default](screenshots/request-more-info-light-default.png), [full](screenshots/request-more-info-light-full.png) |
| Career centers | `/career-centers/` | [default](screenshots/career-centers-light-default.png), [full](screenshots/career-centers-light-full.png) |
| Career-centers contact | `/career-centers/contact/` | [default](screenshots/cc-contact-light-default.png), [full](screenshots/cc-contact-light-full.png) |
| Marketing toolkit | `/career-centers/marketing-toolkit/` | [default](screenshots/marketing-toolkit-light-default.png), [full](screenshots/marketing-toolkit-light-full.png) |
| Careers | `/careers/` | [default](screenshots/careers-light-default.png), [dept-open](screenshots/careers-light-dept-open.png), [full](screenshots/careers-light-full.png) |
| About | `/about/` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Handshake AI | `/ai/` | [default](screenshots/ai-light-default.png), [full](screenshots/ai-light-full.png) |
| AI for enterprise | `/ai/enterprise/` | [default](screenshots/ai-enterprise-light-default.png), [full](screenshots/ai-enterprise-light-full.png) |
| AI opportunities | `/ai/opportunities/` | [default](screenshots/ai-opportunities-light-default.png), [full](screenshots/ai-opportunities-light-full.png) |
| AI research | `/research/ai/` | [default](screenshots/research-ai-light-default.png), [full](screenshots/research-ai-light-full.png) |
| Blog | `/blog/` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Blog article | `/blog/students/how-to-search-for-jobs-on-handshake/` | [default](screenshots/blog-article-light-default.png), [full](screenshots/blog-article-light-full.png) |
| Learn | `/learn/` | [default](screenshots/learn-light-default.png), [full](screenshots/learn-light-full.png) |
| Terms of service | `/legal/tos/` | [default](screenshots/legal-light-default.png), [full](screenshots/legal-light-full.png) |
| Privacy policy | `/privacy-policy/` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Newsroom | `/newsroom/` | [default](screenshots/newsroom-light-default.png), [full](screenshots/newsroom-light-full.png) |
| Accessibility | `/accessibility/` | [default](screenshots/accessibility-light-default.png), [full](screenshots/accessibility-light-full.png) |
| Security | `/security/` | [default](screenshots/security-light-default.png), [full](screenshots/security-light-full.png) |
| App access (consumer login) | `app.joinhandshake.com/access` | [default](screenshots/access-light-default.png), [full](screenshots/access-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Students, phone | `/students/` | [default](screenshots/mobile-students-light-default.png), [full](screenshots/mobile-students-light-full.png) |
| Employers, phone | `/employers/` | [default](screenshots/mobile-employers-light-default.png), [full](screenshots/mobile-employers-light-full.png) |
| Pricing, phone | `/employers/pricing/` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Blog, phone | `/blog/` | [default](screenshots/mobile-blog-light-default.png), [full](screenshots/mobile-blog-light-full.png) |
| App access, phone | `app.joinhandshake.com/access` | [default](screenshots/mobile-access-light-default.png), [full](screenshots/mobile-access-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Nav mega menu | home nav | the 'Employers' item's own hover — the panel opened, captured, and closed by moving the pointer off; its links were never followed | [home-light-nav-open](screenshots/home-light-nav-open.png) |
| Segment switcher | employers | the 'Automate' tab's own press — a local UI toggle that swaps the published feature panel | [employers-light-tab-automate](screenshots/employers-light-tab-automate.png), [hs-segment-tab](#segment-switcher-tab) |
| FAQ accordion | employers, pricing | the question button's own press — the answer unfolded and folded back | [employers-light-faq-open](screenshots/employers-light-faq-open.png), [hs-faq](#faq-accordion-question) |
| Department accordion | careers | the department header's own press — the role list unfolded | [careers-light-dept-open](screenshots/careers-light-dept-open.png), [car-dept-button](#department-accordion) |
| Mobile nav sheet | home, phone width | the 'Open menu' button's own press | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-hs-drawer](#nav-sheet-open) |
| Consent banner | the pages where Ketch mounted it | the page's own Ketch banner, captured where it appeared, then hidden — never answered | [home-light-consent](screenshots/home-light-consent.png) if present |
| App feed, signup and support | app.joinhandshake.com/explore, /signup, support.joinhandshake.com | Cloudflare managed challenge from the capture host — never cleared | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 17 components were given a real keyboard focus. 16 draw an outline ring: `hs-nav-link` (1px auto #101010, offset 1px), `hs-signup-button` (1px auto #101010, offset 1px), `hs-login-link` (1px auto #101010, offset 1px), `hs-footer-link` (1px auto #101010, offset 1px), `hs-filter-pill` (1px auto #101010, offset 0px), `hs-banner-dismiss` (1px auto #101010, offset 0px), `hs-cta` (1px auto #101010, offset 1px), `hs-faq` (1px auto #101010, offset 0px), `mkto-submit` (1px auto #101010, offset 0px), `stu-signup-button` (1px auto #101010, offset 1px), `stu-text-link` (1px auto #101010, offset 1px), `blog-search-button` (1px auto #101010, offset 0px), `blog-category-link` (1px auto #101010, offset 1px), `car-page-button` (1px auto #101010, offset 0px), `legal-nav-link` (1px auto #101010, offset 1px), `app-continue-button` (2px solid #003bcc `access.rosettaBg.featureCallout`, offset 2px). The other 1 show no measured change: `hs-search-button`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | hs-filter-pill, hs-search-button |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, all, backdrop-filter, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | car-dept-button, car-page-button, car-search-input, hs-carousel-dot, hs-cta, hs-login-link, hs-segment-tab, hs-signup-button and more |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | blog-search-button, mkto-submit |
| 0.2s | `ease` | background-color, color | app-continue-button, hs-nav |
| 0.3s | `ease-in` | transform | app-email-field |
| 0.3s | `ease-in-out` | top | hs-nav |
| 0.4s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | hs-nav-link |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Job search form](#job-search-form) | 920 x 88 | - | - | transparent | none | 0 |
| [Article card](#article-card) | 536 x 159.22 | - | - | transparent | none | 0 |
| [Plan comparison table](#plan-comparison-table) | 1152 x 856.47 | - | - | #ffffff `light.fg.headline` | none | 0 |
| [Demo form shell](#demo-form-shell) | 502.67 x 466 | - | - | transparent | none | 0 |
| [Fixed nav bar](#fixed-nav-bar) | 1440 x 56 | - | - | transparent | none | 0 |
| [Nav sheet (open)](#nav-sheet-open) | 390 x 772 | - | - | #ffffff `light.fg.headline` | none | 8px 16px 24px 16px |
| [Login page shell](#login-page-shell) | 1440 x 900 | - | - | transparent | none | 72px 0px 76px 0px |

## Components

### Site chrome

The chrome every marketing page carries: the floating pill nav (wordmark, section items, 'Sign up', 'Log in') and the rounded-top footer with its link columns.

#### Fixed nav bar
The pill-shaped bar fixed under --desktop-nav-top-offset over every marketing page: wordmark, section items, "Sign up" and "Log in". Read as `hs-nav` on the home page.
Read on 2026-11-17T08:51:01.377Z.

**Values (default).** size 1440 x 56; background transparent; text NoiGrotesk 14/19.6 400, #ffffff `light.fg.headline`; transition top 0.3s ease-in-out, color 0.2s ease; layers div.flex.items-center 1392.0x56.0 rgba(255, 255, 255, 0) 16px; a.flex.flex-col 73.8x40.0 oklab(0 0 0 / 0) T:1px solid / R:1px solid / B:1px solid / L:1px solid 8px; a.flex.flex-col 80.5x40.0 rgb(211, 251, 82) 8px.

Child layers that carry the look: div 1392x56 background rgba(255, 255, 255, 0) radius 16px; a 73.8x40 background oklab(0 0 0 / 0) border 1px solid radius 8px; a 80.5x40 background #d3fb52 `light.button.primary.bg` radius 8px.

![Fixed nav bar default](components/crops/hs-nav-default.png)

#### Nav section item
A top-level nav item ("Employers") — opens the mega menu on hover. Read as `hs-nav-link` on the home page.
States read on 2026-11-17T08:51:02.879Z (default); 2026-11-17T08:51:05.133Z (hover); 2026-11-17T08:51:10.282Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 95.13 x 43.59; padding 12px 16px; radius 8px; background transparent; text NoiGrotesk 14/19.6 400, #ffffff `light.fg.headline`; transition color 0.4s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.4s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.4s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.4s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.4s cubic-bezier(0.4, 0, 0.2, 1), fill 0.4s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.4s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.4s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.4s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.4s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(1 0 5.96046e-8 / 0.1) |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.rounded-lg.px-4 95.1x43.6 1px auto rgb(16, 16, 16) offset 1px 8px |

![Nav section item default](components/crops/hs-nav-link-default.png) ![Nav section item hover](components/crops/hs-nav-link-hover.png) ![Nav section item focus-visible](components/crops/hs-nav-link-focus-visible.png)

#### "Sign up" button
The solid sign-up control in the nav's right rail. Read as `hs-signup-button` on the home page.
States read on 2026-11-17T08:51:11.660Z (default); 2026-11-17T08:51:13.889Z (hover); 2026-11-17T08:51:18.211Z (focus-visible); 2026-11-17T08:51:22.108Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 80.53 x 40; padding 12px 16px; radius 8px; background #d3fb52 `light.button.primary.bg`; text NoiGrotesk 14/15.4 500, #14151c `light.bg.footer`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #a1dd3b `light.button.primary.hover` |
| focus-visible | background #e7ff89 `core.color.framer.24ccea63-a288-4de4-8c94-07c5025e7e7e`; outline 1px auto #101010, offset 1px |
| pressed | background #a1dd3b `light.button.primary.hover` |

!["Sign up" button default](components/crops/hs-signup-button-default.png) !["Sign up" button hover](components/crops/hs-signup-button-hover.png) !["Sign up" button focus-visible](components/crops/hs-signup-button-focus-visible.png) !["Sign up" button pressed](components/crops/hs-signup-button-pressed.png)

#### "Log in" link
The outlined log-in control in the nav's right rail. Read as `hs-login-link` on the home page.
States read on 2026-11-17T08:51:30.378Z (default); 2026-11-17T08:51:32.784Z (hover); 2026-11-17T08:51:35.245Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73.75 x 40; padding 12px 16px; border 1px solid #ffffff `light.fg.headline`; radius 8px; background oklab(0 0 0 / 0); text NoiGrotesk 14/15.4 500, #ffffff `light.fg.headline`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid oklab(0 0 0 / 0); background #ffffff `light.fg.headline`; text NoiGrotesk 14/15.4 500, #14151c `light.bg.footer` |
| focus-visible | border 1px solid #f3f4fa `light.bg.muted`; outline 1px auto #101010, offset 1px; text NoiGrotesk 14/15.4 500, #f3f4fa `light.bg.muted` |

!["Log in" link default](components/crops/hs-login-link-default.png) !["Log in" link hover](components/crops/hs-login-link-hover.png) !["Log in" link focus-visible](components/crops/hs-login-link-focus-visible.png)

#### Nav mega menu (open)
The hover-opened panel under a nav section item. "opened" is the item's own hover: the pointer rests on it until aria-expanded flips. Read as `hs-nav-menu` on the home page.
Read on 2026-11-17T08:51:54.771Z.

**Values (opened).** size 774 x 249.68; radius 16px; background #ffffff `light.fg.headline`; shadow rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px; text NoiGrotesk 10/11 500, #d3fb52 `light.button.primary.bg`; transform matrix3d(0.9, 0, 0, 0, 0, 0.779423, -0.45, 0, 0, 0.5, 0.866025, 0, 0, 0, 0, 1); opacity 0; icon 14.4 x 12.47, #000000 `light.nav.legal`.

![Nav mega menu (open) opened](components/crops/hs-nav-menu-opened.png)

#### Footer
The rounded-top footer (rounded-t-3xl) with link columns. Read as `hs-footer` on the home page.
Read on 2026-11-17T08:52:14.383Z.

**Values (default).** size 1440 x 766.25; padding 24px; radius 24px 24px 0px 0px; background #14151c `light.bg.footer`; text NoiGrotesk 40/44 400, #ffffff `light.fg.headline`.

![Footer default](components/crops/hs-footer-default.png)

#### Footer link
A single link inside the footer columns. Read as `hs-footer-link` on the home page.
States read on 2026-11-17T08:52:15.245Z (default); 2026-11-17T08:52:17.009Z (hover); 2026-11-17T08:52:18.241Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 140 x 47.22; background transparent; text NoiGrotesk 16/24 400, #ffffff `light.fg.headline` |
| hover | text NoiGrotesk 16/24 400, #d3fb52 `light.button.primary.bg` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a 140.0x47.2 1px auto rgb(16, 16, 16) offset 1px |

![Footer link default](components/crops/hs-footer-link-default.png) ![Footer link hover](components/crops/hs-footer-link-hover.png) ![Footer link focus-visible](components/crops/hs-footer-link-focus-visible.png)

### Homepage hero

The home page's job-search surface: the brand-face headline, the rounded search field row and the job-type pills. The form was measured, never submitted.

#### Hero headline (h1)
"LET'S FIND YOUR NEXT JOB" — the hero title in the brand face. The page ships two hero copies (one per breakpoint); the visible one is picked, never the zero-rect twin. Read as `hs-hero-h1` on the home page.
Read on 2026-11-17T08:52:20.916Z.

**Values (default).** size 1392 x 274; padding 0px 0px 18px 0px; background transparent; text SansPlomb 160/128 600, #ffffff `light.fg.headline`.

![Hero headline (h1) default](components/crops/hs-hero-h1-default.png)

#### Job search form
The hero job-search field row — measured at rest; typing and submitting were never done (the form navigates to the app). Read as `hs-search-form` on the home page.
Read on 2026-11-17T08:52:22.719Z.

**Values (default).** size 920 x 88; background transparent; text NoiGrotesk 20/22 400, oklab(0.19794 0.0021212 -0.0139539 / 0.6); icon 32 x 32, #252630 `light.input.search.border`; layers input.hidden.size-full 920.0x88.0 rgb(255, 255, 255) 24px; textarea.block.size-full 0.0x0.0 rgb(255, 255, 255) 24px; button.absolute.right-(--mobile-input-padding) 56.0x56.0 oklab(0.271936 0.00340799 -0.0182189 / 0.1) 12px.

Child layers that carry the look: input 920x88 background #ffffff `light.fg.headline` radius 24px; textarea 0x0 background #ffffff `light.fg.headline` radius 24px; button 56x56 background oklab(0.271936 0.00340799 -0.0182189 / 0.1) radius 12px.

![Job search form default](components/crops/hs-search-form-default.png)

#### Job search input
The rounded text field inside the hero form. Read as `hs-search-input` on the home page.
States read on 2026-11-17T08:52:24.858Z (default); 2026-11-17T08:52:27.286Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 920 x 88; padding 0px 80px 0px 64px; radius 24px; background #ffffff `light.fg.headline`; text NoiGrotesk 20/22 400, #252630 `light.input.search.border`; placeholder #252630 `light.input.search.border` |
| focused | outline 1px auto #101010, offset 0px |

![Job search input default](components/crops/hs-search-input-default.png) ![Job search input focused](components/crops/hs-search-input-focused.png)

#### "Search jobs" button
The submit-styled button inside the hero form — pressed states are CDP-forced, so it never submits. Read as `hs-search-button` on the home page.
States read on 2026-11-17T08:52:28.639Z (default); 2026-11-17T08:52:31.136Z (hover); 2026-11-17T08:52:32.924Z (focus-visible); 2026-11-17T08:52:35.206Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 56 x 56; radius 12px; background oklab(0.271936 0.00340799 -0.0182189 / 0.1); text NoiGrotesk 16/24 400, #ffffff `light.fg.headline`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1); icon 13 x 20, #7b7b85 `core.color.framer.9bc81069-b7b8-4d87-8c24-886145b7c040` |

!["Search jobs" button default](components/crops/hs-search-button-default.png) !["Search jobs" button hover](components/crops/hs-search-button-hover.png) !["Search jobs" button focus-visible](components/crops/hs-search-button-focus-visible.png) !["Search jobs" button pressed](components/crops/hs-search-button-pressed.png)

#### Job-type pill
A selectable type pill under the search field ("Full-time"). Read as `hs-filter-pill` on the home page.
States read on 2026-11-17T08:52:37.209Z (default); 2026-11-17T08:52:50.590Z (hover); 2026-11-17T08:53:11.474Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 91.13 x 45.91; padding 16px; border 1px solid oklab(1 0 5.96046e-8 / 0.2); radius 8px; background transparent; text NoiGrotesk 14/11.9 500, #ffffff `light.fg.headline`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1) |
| hover | background oklab(1 0 5.96046e-8 / 0.1) |
| focus-visible | outline 1px auto #101010, offset 0px |

![Job-type pill default](components/crops/hs-filter-pill-default.png) ![Job-type pill hover](components/crops/hs-filter-pill-hover.png) ![Job-type pill focus-visible](components/crops/hs-filter-pill-focus-visible.png)

### Employers page

The /employers/ furniture: the top notification banner, the Source/Automate/Brand/Measure segment switcher, CTA pills, testimonial dots and the FAQ accordion.

#### Notification banner
The top banner (its height is --notification-banner-height); while it shows, the nav's top offset switches to --desktop-nav-top-offset-with-banner. Read as `hs-banner` on the employers page.
Read on 2026-11-17T05:07:07.852Z.

**Values (default).** size 1392 x 40; radius 8px; background #d3fb52 `light.button.primary.bg`; text NoiGrotesk 14/19.6 400, #252630 `light.input.search.border`; icon 16 x 16, #252630 `light.input.search.border`.

![Notification banner default](components/crops/hs-banner-default.png)

#### Banner dismiss button
The icon-only "Dismiss notification" control — measured, never pressed. Read as `hs-banner-dismiss` on the employers page.
States read on 2026-11-17T05:07:09.961Z (default); 2026-11-17T05:07:11.690Z (hover); 2026-11-17T05:07:12.933Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 16 x 16; background transparent; text NoiGrotesk 16/24 400, #252630 `light.input.search.border`; icon 16 x 16, #252630 `light.input.search.border` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.absolute.right-6 16.0x16.0 1px auto rgb(16, 16, 16) offset 0px |

![Banner dismiss button default](components/crops/hs-banner-dismiss-default.png) ![Banner dismiss button hover](components/crops/hs-banner-dismiss-hover.png) ![Banner dismiss button focus-visible](components/crops/hs-banner-dismiss-focus-visible.png)

#### Segment switcher tab
One of Source / Automate / Brand / Measure — opacity carries the selection. "selected" is the tab's own press: it swaps the feature panel. Read as `hs-segment-tab` on the employers page.
States read on 2026-11-17T05:07:13.863Z (default); 2026-11-17T05:07:15.636Z (hover); 2026-11-17T05:07:17.510Z (selected).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 120 x 44; background transparent; text NoiGrotesk 40/44 400, #a9aaae `light.tab.fg`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, selected | text NoiGrotesk 40/44 400, #252630 `light.input.search.border` |

![Segment switcher tab default](components/crops/hs-segment-tab-default.png) ![Segment switcher tab hover](components/crops/hs-segment-tab-hover.png) ![Segment switcher tab selected](components/crops/hs-segment-tab-selected.png)

#### CTA link-button
A solid call-to-action ("Post a job today" / "Get started" / "Contact sales") — the group.inline-flex pill. Read as `hs-cta` on the employers page.
States read on 2026-11-17T05:07:19.128Z (default); 2026-11-17T05:07:21.002Z (hover); 2026-11-17T05:07:22.288Z (focus-visible); 2026-11-17T05:07:23.619Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 120.38 x 40; padding 12px 16px; border 1px solid #ffffff `light.fg.headline`; radius 8px; background oklab(0 0 0 / 0); text NoiGrotesk 16/17.6 500, #ffffff `light.fg.headline`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid oklab(0 0 0 / 0); background #ffffff `light.fg.headline`; text NoiGrotesk 16/17.6 500, #14151c `light.bg.footer` |
| focus-visible | border 1px solid #f3f4fa `light.bg.muted`; outline 1px auto #101010, offset 1px; text NoiGrotesk 16/17.6 500, #f3f4fa `light.bg.muted` |

![CTA link-button default](components/crops/hs-cta-default.png) ![CTA link-button hover](components/crops/hs-cta-hover.png) ![CTA link-button focus-visible](components/crops/hs-cta-focus-visible.png) ![CTA link-button pressed](components/crops/hs-cta-pressed.png)

#### Testimonial dot
A carousel page dot ("Go to testimonial N"). Read as `hs-carousel-dot` on the employers page.
States read on 2026-11-17T05:07:24.460Z (default); 2026-11-17T05:07:26.181Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 8 x 8; radius 9999px; background #ffffff `light.fg.headline`; text NoiGrotesk 16/24 400, #ffffff `light.fg.headline`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

![Testimonial dot default](components/crops/hs-carousel-dot-default.png) ![Testimonial dot hover](components/crops/hs-carousel-dot-hover.png)

#### FAQ accordion question
A question row in the FAQ. "opened" is the question button's own press: it unfolds the answer. Read as `hs-faq` on the employers page.
States read on 2026-11-17T05:07:27.019Z (default); 2026-11-17T05:07:28.766Z (hover); 2026-11-17T05:07:30.009Z (focus-visible); 2026-11-17T05:07:31.857Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, opened) | size 597.33 x 25.2; background transparent; text NoiGrotesk 18/25.2 400, #ffffff `light.fg.headline`; icon 14 x 20, #ffffff `light.fg.headline`; layers div.flex.size-6 24.0x24.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 9999px |
| focus-visible | outline 1px auto #101010, offset 0px; layers button 597.3x25.2 1px auto rgb(16, 16, 16) offset 0px; div.flex.size-6 24.0x24.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 9999px |

Child layers that carry the look: div 24x24 border 1px solid radius 9999px.

![FAQ accordion question default](components/crops/hs-faq-default.png) ![FAQ accordion question hover](components/crops/hs-faq-hover.png) ![FAQ accordion question focus-visible](components/crops/hs-faq-focus-visible.png) ![FAQ accordion question opened](components/crops/hs-faq-opened.png)

### Pricing page

The /employers/pricing/ furniture: the plan cards, the feature-group tabs and the plan comparison tables.

#### Plan comparison table
One of the plan/feature tables on /employers/pricing/ (the page mounts four). Read as `pricing-table` on the pricing page.
Read on 2026-11-17T08:44:05.661Z.

**Values (default).** size 1152 x 856.47; background #ffffff `light.fg.headline`; text NoiGrotesk 16/24 700, #000000 `light.nav.legal`; icon 24 x 24, #00b1b5 `core.color.framer.089c3dbf-4f41-4221-b7d6-ae39d611e102`.

![Plan comparison table default](components/crops/pricing-table-default.png)

#### Table header cell
A th in the comparison table. Read as `pricing-th` on the pricing page.
Read on 2026-11-17T08:44:09.260Z.

**Values (default).** size 83 x 24; background transparent; text NoiGrotesk 16/24 700, #000000 `light.nav.legal`.

![Table header cell default](components/crops/pricing-th-default.png)

#### Table cell
A td in the comparison table. Read as `pricing-td` on the pricing page.
Read on 2026-11-17T08:44:18.302Z.

**Values (default).** size 493.7 x 92.81; padding 24px; background transparent; text NoiGrotesk 16/22.4 400, oklab(0.271936 0.00340799 -0.0182189 / 0.8).

![Table cell default](components/crops/pricing-td-default.png)

#### Plan card
A plan column/card on the pricing page. Read as `pricing-plan-card` on the pricing page.
Read on 2026-11-17T08:44:22.773Z.

**Values (default).** size 256 x 125.61; background transparent; text NoiGrotesk 32/35.2 400, #000000 `light.nav.legal`.

![Plan card default](components/crops/pricing-plan-card-default.png)

#### Feature group tab
A "Target & Connect" / "Centralize" / "Brand" / "Measure" group button that switches the comparison section. Read as `pricing-feature-tab` on the pricing page.
States read on 2026-11-17T08:44:25.222Z (default); 2026-11-17T08:44:27.053Z (hover); 2026-11-17T08:44:29.149Z (selected).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, selected) | size 1152 x 74.59; padding 24px; border B: 1px solid #878aae; background transparent; text NoiGrotesk 16/25.6 600, #000000 `light.nav.legal`; icon 16 x 16, #bebdbf `core.color.framer.7509cc64-b578-4e00-8e69-ea2d85bc1acc`; layers button.flex.w-full 1152.0x74.6 B:1px solid |

Child layers that carry the look: button 1152x74.6 border 1px solid.

![Feature group tab default](components/crops/pricing-feature-tab-default.png) ![Feature group tab hover](components/crops/pricing-feature-tab-hover.png) ![Feature group tab selected](components/crops/pricing-feature-tab-selected.png)

### Marketo forms

The 'Request a demo' and career-centers contact forms — vendor-rendered Marketo fields measured at rest; nothing was typed or submitted.

#### Demo form shell
The "Request a demo" Marketo form — its fields mount from go.joinhandshake.com vendor script. Read as `mkto-form` on the request a demo page.
Read on 2026-11-17T04:54:41.977Z.

**Values (default).** size 502.67 x 466; background transparent; text NoiGrotesk 18/18 400, #14151c `light.bg.footer`; layers input.mktoField.mktoEmailField 502.7x58.0 rgb(255, 255, 255) T:1px solid / R:1px solid / B:1px solid / L:1px solid 4px; input.mktoField.mktoTextField 243.3x58.0 rgb(255, 255, 255) T:1px solid / R:1px solid / B:1px solid / L:1px solid 4px; input.mktoField.mktoTextField 243.3x58.0 rgb(255, 255, 255) T:1px solid / R:1px solid / B:1px solid / L:1px solid 4px; input.mktoField.mktoTextField 502.7x58.0 r.

Child layers that carry the look: input 502.7x58 background #ffffff `light.fg.headline` border 1px solid radius 4px; input 243.3x58 background #ffffff `light.fg.headline` border 1px solid radius 4px; input 243.3x58 background #ffffff `light.fg.headline` border 1px solid radius 4px.

![Demo form shell default](components/crops/mkto-form-default.png)

#### Form text field
A text input inside the Marketo form. Read as `mkto-input` on the request a demo page.
States read on 2026-11-17T04:54:42.942Z (default); 2026-11-17T04:54:44.741Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 502.67 x 58; padding 16px; border 1px solid #484851 `core.color.framer.c5583c21-56ea-40f2-bd5f-aab56412a3da`; radius 4px; background #ffffff `light.fg.headline`; text NoiGrotesk 16/24 400, #252630 `light.input.search.border`; placeholder #bebdbf `core.color.framer.7509cc64-b578-4e00-8e69-ea2d85bc1acc` |
| focused | border 1px solid #ff455b `core.color.framer.6c621e68-cbf1-4faf-a500-3fc11fa7290d`; outline 1px auto #9b53f6 `core.color.framer.f8d4d9f2-c148-478e-9f1b-a43f8a3cc1fe`, offset 0px |

![Form text field default](components/crops/mkto-input-default.png) ![Form text field focused](components/crops/mkto-input-focused.png)

#### Form select
A select inside the Marketo form. Read as `mkto-select` on the request a demo page.

Not on the page when it was captured.

#### Form submit button
The form's submit control — measured, never pressed (pressed states are CDP-forced). Read as `mkto-submit` on the request a demo page.
States read on 2026-11-17T04:54:45.800Z (default); 2026-11-17T04:54:47.620Z (hover); 2026-11-17T04:54:49.901Z (focus-visible); 2026-11-17T04:54:56.605Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 502.67 x 48; padding 14px 16px; radius 4px; background #d3fb52 `light.button.primary.bg`; text NoiGrotesk 18/18 400, #14151c `light.bg.footer`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #ffffff `light.fg.headline` |
| focus-visible | outline 1px auto #101010, offset 0px |

![Form submit button default](components/crops/mkto-submit-default.png) ![Form submit button hover](components/crops/mkto-submit-hover.png) ![Form submit button focus-visible](components/crops/mkto-submit-focus-visible.png) ![Form submit button pressed](components/crops/mkto-submit-pressed.png)

#### Career-center contact form
The EDU contact form on /career-centers/contact/ — same Marketo stack. Read as `cc-form` on the career-centers contact page.
Read on 2026-11-17T04:55:31.878Z.

**Values (default).** size 728 x 921.75; background transparent; text NoiGrotesk 16/25.6 400, #000000 `light.nav.legal`; layers input.mktoField.mktoTextField 728.0x40.0 rgb(243, 244, 250) 3px; input.mktoField.mktoTextField 728.0x40.0 rgb(243, 244, 250) 3px; input.mktoField.mktoEmailField 728.0x40.0 rgb(243, 244, 250) 3px; input.mktoField.mktoTelField 728.0x40.0 rgb(243, 244, 250) 3px; input.mktoField.mktoTextField 728.0x40.0 rgb(243, 244, 250) 3px; select.mktoField.mktoHasWidth 728.0x35.0 rgb(243, 244, 250) 3px.

Child layers that carry the look: input 728x40 background #f3f4fa `light.bg.muted` radius 3px; input 728x40 background #f3f4fa `light.bg.muted` radius 3px; input 728x40 background #f3f4fa `light.bg.muted` radius 3px.

![Career-center contact form default](components/crops/cc-form-default.png)

### Students page

The /students/ page's email capture forms and sign-up CTAs — measured at rest, nothing typed.

#### Email capture field
The "Type school or personal email here" field in the hero — measured at rest, nothing typed. Read as `stu-email-input` on the students page.
States read on 2026-11-17T04:56:23.776Z (default); 2026-11-17T04:56:25.435Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 448 x 56; padding 8px 16px; radius 8px; background #ffffff `light.fg.headline`; text NoiGrotesk 18/25.2 400, #14151c `light.bg.footer`; placeholder oklab(0.19794 0.0021212 -0.0139539 / 0.6) |
| focused | outline 1px auto #101010, offset 0px |

![Email capture field default](components/crops/stu-email-input-default.png) ![Email capture field focused](components/crops/stu-email-input-focused.png)

#### "Sign up" CTA
The students sign-up button (group.inline-flex). Read as `stu-signup-button` on the students page.
States read on 2026-11-17T04:45:21.724Z (pressed); 2026-11-17T04:56:26.671Z (default); 2026-11-17T04:56:40.742Z (hover); 2026-11-17T04:56:44.376Z (focus-visible). `pressed` kept its 2026-11-17T04:45:21.724Z reading after a failed re-read (cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 82.53 x 40; padding 12px 16px; border 1px solid #252630 `light.input.search.border`; radius 8px; background oklab(0 0 0 / 0); text NoiGrotesk 14/15.4 500, #252630 `light.input.search.border`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid oklab(0 0 0 / 0); background oklab(0.19794 0.0021212 -0.0139539 / 0.1) |
| focus-visible | border 1px solid #14151c `light.bg.footer`; background #ffffff `light.fg.headline`; outline 1px auto #101010, offset 1px |
| pressed | border 1px solid oklab(0 0 0 / 0); background #ffffff `light.fg.headline`; text NoiGrotesk 14/15.4 500, #14151c `light.bg.footer` |

!["Sign up" CTA default](components/crops/stu-signup-button-default.png) !["Sign up" CTA hover](components/crops/stu-signup-button-hover.png) !["Sign up" CTA focus-visible](components/crops/stu-signup-button-focus-visible.png) !["Sign up" CTA pressed](components/crops/stu-signup-button-pressed.png)

#### Arrow text link
"Find jobs and internships →" — an arrow-suffixed text link in the brand face. Read as `stu-text-link` on the students page.
States read on 2026-11-17T04:45:24.325Z (default); 2026-11-17T04:45:27.061Z (hover); 2026-11-17T04:45:29.674Z (focus-visible). `default` kept its 2026-11-17T04:45:24.325Z reading after a failed re-read (locator.evaluate: Timeout 8000ms exceeded.). `hover` kept its 2026-11-17T04:45:27.061Z reading after a failed re-read (locator.boundingBox: Timeout 8000ms exceeded.). `focus-visible` kept its 2026-11-17T04:45:29.674Z reading after a failed re-read (locator.evaluate: Timeout 8000ms exceeded.).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 243.53 x 46.41; padding 12px 20px; radius 32px; background oklab(0.235795 -0.0320912 -0.0146041 / 0.8); text NoiGrotesk 16/22.4 500, #ffffff `light.fg.headline`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.352278 -0.0551743 -0.0235738 / 0.8) |
| focus-visible | outline 1px auto #101010, offset 1px |

![Arrow text link default](components/crops/stu-text-link-default.png) ![Arrow text link hover](components/crops/stu-text-link-hover.png) ![Arrow text link focus-visible](components/crops/stu-text-link-focus-visible.png)

#### Card carousel arrow
A "Slide to the next/previous card" arrow button. Read as `stu-carousel-btn` on the students page.
States read on 2026-11-17T04:57:26.817Z (default); 2026-11-17T04:57:36.283Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 48; background transparent; text NoiGrotesk 16/24 400, #ffffff `light.fg.headline`; icon 20 x 14, #ffffff `light.fg.headline`; layers div.flex.size-12 48.0x48.0 rgb(255, 255, 255) 9999px |
| hover | text NoiGrotesk 16/24 400, #14151c `light.bg.footer`; icon 20 x 14, #14151c `light.bg.footer`; layers div.flex.size-12 48.0x48.0 rgb(20, 21, 28) 9999px |

Child layers that carry the look: div 48x48 background #ffffff `light.fg.headline` radius 9999px.

![Card carousel arrow default](components/crops/stu-carousel-btn-default.png) ![Card carousel arrow hover](components/crops/stu-carousel-btn-hover.png)

### Blog

The blog index: the search field, the uppercase category links and the article cards.

#### Blog search field
The search input on the blog index — measured at rest, nothing typed. Read as `blog-search-input` on the blog page.
States read on 2026-11-17T04:57:57.374Z (default); 2026-11-17T04:57:58.776Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 343 x 27; padding 0px 0px 0px 8px; background #f3f4fa `light.bg.muted`; text NoiGrotesk 22/22 400, #000000 `light.nav.legal`; placeholder #000000 `light.nav.legal` |

![Blog search field default](components/crops/blog-search-input-default.png) ![Blog search field focused](components/crops/blog-search-input-focused.png)

#### Search button
The Search button beside the field — CDP-forced states only. Read as `blog-search-button` on the blog page.
States read on 2026-11-17T04:57:59.698Z (default); 2026-11-17T04:58:01.563Z (hover); 2026-11-17T04:58:03.283Z (focus-visible); 2026-11-17T04:58:04.826Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 88.92 x 48; padding 14px 16px; radius 4px; background #052326 `access.deprecated.backgroundInvertedSecondary`; text NoiGrotesk 18/18 400, #ffffff `light.fg.headline`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto #101010, offset 0px |

![Search button default](components/crops/blog-search-button-default.png) ![Search button hover](components/crops/blog-search-button-hover.png) ![Search button focus-visible](components/crops/blog-search-button-focus-visible.png) ![Search button pressed](components/crops/blog-search-button-pressed.png)

#### Category link
An uppercase category link ("AI SKILLS STUDIO"). Read as `blog-category-link` on the blog page.
States read on 2026-11-17T04:58:09.935Z (default); 2026-11-17T04:58:18.161Z (hover); 2026-11-17T04:58:21.289Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 137 x 17; background transparent; text NoiGrotesk 16/24 600, #2e6aff `core.color.site.cta` |
| hover | text NoiGrotesk 16/24 600, #1552d6 `core.color.site.ctaHover` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.uppercase.font-semibold 137.0x17.0 1px auto rgb(16, 16, 16) offset 1px |

![Category link default](components/crops/blog-category-link-default.png) ![Category link hover](components/crops/blog-category-link-hover.png) ![Category link focus-visible](components/crops/blog-category-link-focus-visible.png)

#### Article card
An article card link on the blog index. Read as `blog-card` on the blog page.
States read on 2026-11-17T04:58:29.342Z (default); 2026-11-17T04:58:32.429Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 536 x 159.22; background transparent; text NoiGrotesk 40/44 600, #000000 `light.nav.legal` |

![Article card default](components/crops/blog-card-default.png) ![Article card hover](components/crops/blog-card-hover.png)

#### "Read More" link
The Read More affordance on an article card. Read as `blog-readmore` on the blog page.
States read on 2026-11-17T04:58:50.495Z (default); 2026-11-17T04:58:54.647Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 536 x 25.5; background transparent; text NoiGrotesk 22/24.2 700, #000000 `light.nav.legal`; icon 14.11 x 24, #000000 `light.nav.legal` |

!["Read More" link default](components/crops/blog-readmore-default.png) !["Read More" link hover](components/crops/blog-readmore-hover.png)

### Careers page

The /careers/ page: the benefits tabs, the roles search field, the department accordions and the pagination.

#### Benefits tab
A benefits category button ("Health & wellness") — the tab's own press swaps the panel. Read as `car-benefit-tab` on the careers page.
States read on 2026-11-17T04:19:51.532Z (default); 2026-11-17T04:19:53.356Z (hover); 2026-11-17T04:19:55.748Z (selected).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, selected) | size 568 x 35.2; background transparent; text NoiGrotesk 32/35.2 400, #000000 `light.nav.legal`; icon 14 x 20, #000000 `light.nav.legal`; layers div.flex.size-6 24.0x24.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 9999px |

Child layers that carry the look: div 24x24 border 1px solid radius 9999px.

![Benefits tab default](components/crops/car-benefit-tab-default.png) ![Benefits tab hover](components/crops/car-benefit-tab-hover.png) ![Benefits tab selected](components/crops/car-benefit-tab-selected.png)

#### Roles search field
The open-roles search input — measured at rest, nothing typed. Read as `car-search-input` on the careers page.
States read on 2026-11-17T04:19:57.286Z (default); 2026-11-17T04:19:59.470Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 688 x 56; padding 16px 12px; border 1px solid oklab(0.271936 0.00340799 -0.0182189 / 0.1); radius 12px; background #ffffff `light.fg.headline`; text NoiGrotesk 16/22.4 400, #14151c `light.bg.footer`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #bebdbf `core.color.framer.7509cc64-b578-4e00-8e69-ea2d85bc1acc` |
| focused | border 1px solid #252630 `light.input.search.border`; shadow oklab(0.271924 0.003418 -0.0182035) 0px 0px 0px 1px |

![Roles search field default](components/crops/car-search-input-default.png) ![Roles search field focused](components/crops/car-search-input-focused.png)

#### Department filter button
The "All departments" filter dropdown in the roles list — "opened" is its own press. Read as `car-dept-button` on the careers page.
States read on 2026-11-17T04:20:00.423Z (default); 2026-11-17T04:20:09.265Z (hover); 2026-11-17T04:20:16.267Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 218.67 x 56; padding 16px 12px; border 1px solid oklab(0.271936 0.00340799 -0.0182189 / 0.1); radius 12px; background #ffffff `light.fg.headline`; text NoiGrotesk 14/19.6 400, #14151c `light.bg.footer`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #14151c `light.bg.footer` |
| hover | border 1px solid #bebdbf `core.color.framer.7509cc64-b578-4e00-8e69-ea2d85bc1acc` |
| opened | border 1px solid #252630 `light.input.search.border`; shadow oklab(0.271924 0.003418 -0.0182035) 0px 0px 0px 1px |

![Department filter button default](components/crops/car-dept-button-default.png) ![Department filter button hover](components/crops/car-dept-button-hover.png) ![Department filter button opened](components/crops/car-dept-button-opened.png)

#### Job row link
An open-role link in the list. Read as `car-job-link` on the careers page.
States read on 2026-11-17T04:20:18.048Z (default); 2026-11-17T04:20:19.959Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1392 x 122; background transparent; text NoiGrotesk 24/26.4 400, #000000 `light.nav.legal`; layers div.group.flex 1392.0x122.0 rgb(255, 255, 255) T:1px solid / R:1px solid / B:1px solid / L:1px solid 12px; div.group.inline-flex 73.8x40.0 rgb(37, 38, 48) 8px |
| hover | text NoiGrotesk 24/26.4 400, #ffffff `light.fg.headline`; layers div.group.flex 1392.0x122.0 rgb(37, 38, 48) T:1px solid / R:1px solid / B:1px solid / L:1px solid 12px; div.group.inline-flex 73.8x40.0 rgb(211, 251, 82) 8px |

Child layers that carry the look: div 1392x122 background #ffffff `light.fg.headline` border 1px solid radius 12px; div 73.8x40 background #252630 `light.input.search.border` radius 8px.

![Job row link default](components/crops/car-job-link-default.png) ![Job row link hover](components/crops/car-job-link-hover.png)

#### Pagination button
A page number in the roles pagination. Read as `car-page-button` on the careers page.
States read on 2026-11-17T04:20:21.184Z (default); 2026-11-17T04:20:22.916Z (hover); 2026-11-17T04:20:24.105Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 48 x 48; border 1px solid #14151c `light.bg.footer`; radius 12px; background #14151c `light.bg.footer`; text NoiGrotesk 16/24 400, #ffffff `light.fg.headline`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto #101010, offset 0px |

![Pagination button default](components/crops/car-page-button-default.png) ![Pagination button hover](components/crops/car-page-button-hover.png) ![Pagination button focus-visible](components/crops/car-page-button-focus-visible.png)

### Legal pages

The legal pages' left rail: the active and inactive section links.

#### Legal nav link (active)
The current section link in the legal left rail (opacity-100). Read as `legal-nav-active` on the legal page.
States read on 2026-11-17T04:59:18.678Z (default); 2026-11-17T04:59:20.762Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 305.5 x 22.41; background transparent; text NoiGrotesk 16/22.4 500, #000000 `light.nav.legal` |

![Legal nav link (active) default](components/crops/legal-nav-active-default.png) ![Legal nav link (active) hover](components/crops/legal-nav-active-hover.png)

#### Legal nav link
An inactive section link in the legal left rail (opacity-60). Read as `legal-nav-link` on the legal page.
States read on 2026-11-17T04:59:22.661Z (default); 2026-11-17T04:59:24.527Z (hover); 2026-11-17T04:59:26.545Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 305.5 x 22.41; background transparent; text NoiGrotesk 16/22.4 400, #000000 `light.nav.legal`; opacity 0.6 |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.opacity-60 305.5x22.4 1px auto rgb(16, 16, 16) offset 1px |

![Legal nav link default](components/crops/legal-nav-link-default.png) ![Legal nav link hover](components/crops/legal-nav-link-hover.png) ![Legal nav link focus-visible](components/crops/legal-nav-link-focus-visible.png)

### App access

The consumer app's 'Log in or sign up' page at app.joinhandshake.com/access — the Rosetta layer: locale select, email field, the rosetta-button, Google's SSO widget and the fine-print links.

#### Login page shell
The /access page body — the consumer app's signed-out entry. Read as `app-shell` on the https://app.joinhandshake.com/access page.
Read on 2026-11-17T05:07:48.814Z.

**Values (default).** size 1440 x 900; padding 72px 0px 76px 0px; background transparent; text Noi Grotesk 15/18 400, #121212 `access.rosettaBg.inverted`; icon 20 x 20, rgba(18, 18, 18, 0.7) `access.rosettaFg.secondary`; layers div.rosetta-field__base.sc-ezOQGI 137.0x36.0 rgb(255, 255, 255) T:1px solid / R:1px solid / B:1px solid / L:1px solid 8px; div.sc-bYMpWt.jDuFBQ 0.0x0.0 rgb(255, 255, 255) T:1px solid / R:1px solid / B:1px solid / L:1px solid rgba(0, 0, 0, 0.08) 0px 6px 30px 0px, rgba(0, 0, 0, 0.08) 0px 1px 3px 0px 8px; div.rosetta-select__option.rosetta-body-medium 0.0x0.0 color(srgb 0.905788 0.905788 0.905788) 8p.

Child layers that carry the look: div 137x36 background #ffffff `light.fg.headline` border 1px solid radius 8px; div 0x0 background #ffffff `light.fg.headline` border 1px solid radius 8px shadow rgba(0, 0, 0, 0.08) 0px 6px 30px 0px, rgba(0, 0, 0, 0.08) 0px 1px 3px 0px; div 0x0 background #e7e7e7 `access.deprecated.backgroundQuaternary` radius 8px.

![Login page shell default](components/crops/app-shell-default.png)

#### Locale select
The "English (US)" rosetta-select in the page chrome. Read as `app-locale-select` on the https://app.joinhandshake.com/access page.
Read on 2026-11-17T05:07:50.594Z.

**Values (default).** size 137 x 36; background transparent; text Noi Grotesk 15/18 400, #121212 `access.rosettaBg.inverted`; icon 20 x 20, rgba(18, 18, 18, 0.7) `access.rosettaFg.secondary`; layers div.rosetta-field__base.sc-ezOQGI 137.0x36.0 rgb(255, 255, 255) T:1px solid / R:1px solid / B:1px solid / L:1px solid 8px; div.sc-bYMpWt.jDuFBQ 0.0x0.0 rgb(255, 255, 255) T:1px solid / R:1px solid / B:1px solid / L:1px solid rgba(0, 0, 0, 0.08) 0px 6px 30px 0px, rgba(0, 0, 0, 0.08) 0px 1px 3px 0px 8px; div.rosetta-select__option.rosetta-body-medium 0.0x0.0 color(srgb 0.905788 0.905788 0.905788) 8p.

Child layers that carry the look: div 137x36 background #ffffff `light.fg.headline` border 1px solid radius 8px; div 0x0 background #ffffff `light.fg.headline` border 1px solid radius 8px shadow rgba(0, 0, 0, 0.08) 0px 6px 30px 0px, rgba(0, 0, 0, 0.08) 0px 1px 3px 0px; div 0x0 background #e7e7e7 `access.deprecated.backgroundQuaternary` radius 8px.

![Locale select default](components/crops/app-locale-select-default.png)

#### Email field
The "Enter your email" rosetta-field — measured at rest, nothing typed. Read as `app-email-field` on the https://app.joinhandshake.com/access page.
States read on 2026-11-17T05:07:51.887Z (default); 2026-11-17T05:07:55.605Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 344 x 48; padding 0px 16px; border 1px solid rgba(18, 18, 18, 0.12) `access.rosettaFg.border`; radius 8px; background #ffffff `light.fg.headline`; text Noi Grotesk 17/23.8 400, #121212 `access.rosettaBg.inverted`; transition transform 0.3s ease-in; placeholder rgba(18, 18, 18, 0.7) `access.rosettaFg.secondary` |
| focused | border 1px solid #04191b `access.rosettaInteractive.primary`; shadow #04191b 0px 0px 0px 1px inset; outline 1px solid transparent, offset 0px |

![Email field default](components/crops/app-email-field-default.png) ![Email field focused](components/crops/app-email-field-focused.png)

#### "Continue with email" button
The rosetta-button submit — pressed states are CDP-forced, so the form never submits. Read as `app-continue-button` on the https://app.joinhandshake.com/access page.
States read on 2026-11-17T05:08:00.961Z (default); 2026-11-17T05:08:04.863Z (hover); 2026-11-17T05:08:12.419Z (focus-visible); 2026-11-17T05:08:14.269Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 344 x 40; padding 0px 12px; radius 8px; background #04191b `access.rosettaInteractive.primary`; text Noi Grotesk 15/18 500, #ffffff `light.fg.headline`; transition background-color 0.2s ease |
| hover | image linear-gradient(rgba(255, 255, 255, 0.06) `access.rosettaInteractive.invertedHovered`, rgba(255, 255, 255, 0.06) `access.rosettaInteractive.invertedHovered`) |
| focus-visible | outline 2px solid #003bcc `access.rosettaBg.featureCallout`, offset 2px |
| pressed | image linear-gradient(rgba(255, 255, 255, 0.12) `access.rosettaInteractive.invertedPressed`, rgba(255, 255, 255, 0.12) `access.rosettaInteractive.invertedPressed`) |

!["Continue with email" button default](components/crops/app-continue-button-default.png) !["Continue with email" button hover](components/crops/app-continue-button-hover.png) !["Continue with email" button focus-visible](components/crops/app-continue-button-focus-visible.png) !["Continue with email" button pressed](components/crops/app-continue-button-pressed.png)

#### Google SSO button
The "Continue with Google" button — Google's own rendered widget (GSI), recorded as vendor. Read as `app-google-button` on the https://app.joinhandshake.com/access page.
Read on 2026-11-17T05:08:16.952Z.

**Values (default).** size 364 x 44; background transparent; text Noi Grotesk 15/18 400, #000000 `light.nav.legal`.

![Google SSO button default](components/crops/app-google-button-default.png)

#### "Sign up as an employer" link
The employer sign-up link under the login card. Read as `app-employer-link` on the https://app.joinhandshake.com/access page.
States read on 2026-11-17T05:08:20.413Z (default); 2026-11-17T05:08:22.978Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 61 x 16; background transparent; text Noi Grotesk 15/18 400, #1569e0 |
| hover | text Noi Grotesk 15/18 400, #0e489a |

!["Sign up as an employer" link default](components/crops/app-employer-link-default.png) !["Sign up as an employer" link hover](components/crops/app-employer-link-hover.png)

#### Terms link
The Terms of Service link in the fine print. Read as `app-tos-link` on the https://app.joinhandshake.com/access page.
States read on 2026-11-17T05:08:27.424Z (default); 2026-11-17T05:08:29.432Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106.09 x 14; background transparent; text Noi Grotesk 13/15.6 400, #1569e0 |
| hover | text Noi Grotesk 13/15.6 400, #0e489a |

![Terms link default](components/crops/app-tos-link-default.png) ![Terms link hover](components/crops/app-tos-link-hover.png)

### Site chrome (mobile)

The 390px surface: the compact header with the 'Open menu' button and the nav sheet it opens.

#### Mobile header pill
The floating pill at 390px: the mobile nav wrapper is a 0-height relative container; the painted bar is its fixed child (wordmark, links, the "Open menu" button). Read as `m-hs-topbar` on the home page.
Read on 2026-11-17T04:31:28.944Z.

**Values (default).** size 358 x 48; padding 8px; radius 12px; background #ffffff `light.fg.headline`; text NoiGrotesk 16/14.4 500, #252630 `light.input.search.border`; icon 32 x 32, #000000 `light.nav.legal`.

![Mobile header pill default](components/crops/m-hs-topbar-default.png)

#### "Open menu" button
The icon-only button (aria-label "Open menu", no text content) that opens the mobile nav sheet. Read as `m-hs-hamburger` on the home page.
States read on 2026-11-17T04:31:30.046Z (default); 2026-11-17T04:31:32.069Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 24 x 16; background transparent; text NoiGrotesk 16/24 400, #000000 `light.nav.legal`; icon 16 x 16, #000000 `light.nav.legal` |

!["Open menu" button default](components/crops/m-hs-hamburger-default.png) !["Open menu" button hover](components/crops/m-hs-hamburger-hover.png)

#### Nav sheet (open)
The opened mobile navigation sheet. The "Open menu" press happens in find(): the sheet is only reachable once open, so the state itself is a no-op. Read as `m-hs-drawer` on the home page.
Read on 2026-11-17T04:31:35.079Z.

**Values (opened).** size 390 x 772; padding 8px 16px 24px 16px; background #ffffff `light.fg.headline`; text NoiGrotesk 28/30.8 400, #000000 `light.nav.legal`; icon 16 x 16, #000000 `light.nav.legal`.

![Nav sheet (open) opened](components/crops/m-hs-drawer-opened.png)

## Icons

8 distinct inline-SVG icons were collected from the live pages into [icons/](icons) by `tools/capture/icons.mjs`, indexed in [icons/INDEX.tsv](icons/INDEX.tsv): a file is named from `tools/capture/icon-names.tsv` where its geometry hash is listed, else the label or class of the control it sits in, else `icon-<hash>`; colour is kept as `currentColor` wherever it matched the text colour, so each icon recolours from CSS `color` the way it does on the site. The icons are the product's artwork — borrow the set's grammar (sizes, stroke-vs-fill, naming roles), never the artwork itself.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [icon-191fac6a](icons/icon-191fac6a.svg) | 32x32 | 0 0 32 32 | fill | nav | Part-time jobs for students studying des |
| [linkedin-icon-large](icons/linkedin-icon-large.svg) | 24x24 | 0 0 24 24 | fill | nav | linkedin icon large |
| [icon-3d2a4102](icons/icon-3d2a4102.svg) | 46x54 | 0 0 46 54 | fill | nav |  |
| [icon-4efa6744](icons/icon-4efa6744.svg) | 50x43 | 0 0 50 43 | fill | nav |  |
| [search-jobs](icons/search-jobs.svg) | 13x20 | 0 0 13 20 | fill | nav | Search jobs |
| [tiktok-icon-large](icons/tiktok-icon-large.svg) | 24x24 | 0 0 24 24 | fill | nav | tiktok icon large |
| [instagram-icon-large](icons/instagram-icon-large.svg) | 24x24 | 0 0 24 24 | fill | nav | instagram icon large |
| [icon-f9457b73](icons/icon-f9457b73.svg) | 16x16 | 0 0 24 20 | stroke | nav | FREE DEMO See Handshake in action Discov |

## Gaps

### The blocked product surfaces

The consumer app's signed-in surfaces were never reached from the capture host: **app.joinhandshake.com/explore**, **/signup** and the student registration flow answer with a Cloudflare managed challenge that never cleared — fresh-context retries across several runs stayed on the interstitial — and **support.joinhandshake.com** answers a Cloudflare 403 'Just a moment...' page. The job feed, onboarding, dashboards, help centre articles and every post-login surface are therefore documented as boundaries, not captured. /access and /login clear the challenge intermittently and were captured when they did; no workaround was attempted beyond fresh-context retries.

### Pages

- **The app feed, signup flow and support centre** — blocked at the edge, see above. The login page's own links were measured, never followed.
- **Sibling marketing pages** — the remaining blog articles, legal sections, learn articles and campaign pages share the templates captured here (hero, cards, FAQ, nav, footer); they were not each measured.
- **The Marketo lead forms** — measured at rest; the vendor script mounts fields for a real human flow, and the form was never submitted.

### States

- **Pressed** was forced with DevTools on the controls that carry it, so a state a script adds on mousedown (if any) is missing.
- **The search fields were never typed into** — the hero job-search, blog search and careers search were measured at rest; no query was run, so results states are uncaptured.
- **The nav mega menu** was captured open on 'Employers'; its destination links were never followed, and the other items' panels were not each opened.
- **The segment switcher, feature-group tabs and accordions** were toggled once each; the full selection matrix was not exercised.
- **The Marketo and email-capture forms** were measured at rest — nothing was typed, focused submission states are uncaptured by design.
- **The Google SSO button** is Google's own rendered widget (GSI): its internals are vendor DOM, recorded as vendor, not Handshake design.
- **The Ketch consent banner** was captured where the page mounted it and hidden, never answered — the preference centre behind its buttons was never opened.

### Themes

Both surfaces paint light only: joinhandshake.com declares no theme class, no theme control and no prefers-color-scheme rule, and the app's /access page paints light through the Rosetta layer. `light` is the only token theme for each surface and every screenshot is the page as it loads — no dark pass exists because no dark surface exists.

### Fonts

- **NoiGrotesk** is the marketing site's display/brand face and **SansPlomb** its body face, both served woff2 under /_next/static/media — proprietary to Handshake, declared and measured, not shipped. The retro **Chicago FLF**/**Geneva** pair on the marketing-toolkit pages and the app's Rosetta family chain are declared likewise. The style guide falls back to the system sans.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The rendered brand strings on the captured pages (the wordmark and copy) are the product's published content.

### Content left out

- Article copy, plan prices, testimonial text and job titles are the product's published content; only frames and components were measured.
