# Cushion components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from cushion.so on 2026-11-12, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or downloaded; the FAQ accordion was toggled locally, and hover/focus/pressed states were forced. The 'Log in', 'Sign up', 'Get started' and 'Talk to a human' controls were measured, never followed. The embedded 'Acme Inc' inbox is a marketing mock, not the authenticated app.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (35 components, 72 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (70 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every page paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Updates | `/updates` | [default](screenshots/updates-light-default.png), [full](screenshots/updates-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Download | `/download` | [default](screenshots/download-light-default.png), [full](screenshots/download-light-full.png) |
| Integrations | `/integrations` | [default](screenshots/integrations-light-default.png), [full](screenshots/integrations-light-full.png) |
| Slack alternative | `/slack-alternative` | [default](screenshots/slackalt-light-default.png), [full](screenshots/slackalt-light-full.png) |
| Terms | `/terms` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| FAQ answer | pricing | the accordion row toggled locally | [faq-item](#faq-item) opened state |
| Mobile menu | home, phone width | the mobile menu button | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |
| The signed-in app | past 'Log in' / 'Sign up' / 'Get started' | the controls were measured, never followed | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 10 components were given a real keyboard focus. 2 draw an outline ring: `mock-channel` (1px auto #005fcc, offset 0px), `footer-link` (1px auto #005fcc, offset 1px). 8 draw a focus ring as a shadow instead: `nav-link`, `nav-login`, `signup-btn`, `cta-start`, `cta-human`, `mock-newpost`, `pricing-cta`, `m-cta-start`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | cta-human, cta-start, m-cta-start, mock-channel, mock-newpost, nav-link, nav-login, pricing-cta and more |
| 0.5s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | mock-post |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan panel](#plan-panel) | 1240 x 354 | 1px solid rgba(33, 33, 33, 0.1) | 16px | #fafafa `color.gray.1` | none | 24px |
| [Blog card](#blog-card) | 397.33 x 403.5 | - | 12px | transparent | none | 0 |
| [Featured post](#featured-post) | 1240 x 339.75 | - | - | transparent | none | 0 |
| [Mock: post card](#mock-post-card) | 606 x 108 | - | - | transparent | none | 16px |
| [App mock frame](#app-mock-frame) | 1280 x 720 | 1px solid rgba(33, 33, 33, 0.1) | 12px 12px 0px 0px | #fcfcfc `color.cushion.background` | none | 0 |
| [Update entry](#update-entry) | 1024 x 1719.88 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The 72px sticky top nav shared by every page: wordmark, 40px text links that take a 5% black fill on hover/press, the 'Log in' link and the 91x40 #00a6f4 'Sign up' button — plus the two hero CTAs and the 1240px link-columns footer.

#### Nav bar
The 72px sticky top nav (Pricing / Updates / Blog / Log in / Sign up). Read as `nav-bar` on the home page.

**Values (default).** size 1440 x 72; background transparent; text ui-sans-serif 16/16 500, #1f1f1f `color.gray.12`; icon 112 x 25, #1f1f1f `color.gray.12`; layers a.inline-flex.items-center 91.8x40.0 rgb(0, 166, 244) 8px.

Child layers that carry the look: a 91.8x40 background #00a6f4 `color.cushion.accent` radius 8px.

![Nav bar default](components/crops/nav-bar-default.png)

#### Nav logo
The Cushion wordmark link. Read as `nav-logo` on the home page.

**Values (default).** size 112 x 25; radius 8px; background transparent; text ui-sans-serif 16/24 400, #1f1f1f `color.gray.12`; icon 112 x 25, #1f1f1f `color.gray.12`.

![Nav logo default](components/crops/nav-logo-default.png)

#### Nav link
A 40px nav link (Pricing); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 87.52 x 40; padding 0px 18px; radius 8px; background transparent; text ui-sans-serif 16/16 500, #1f1f1f `color.gray.12`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0 0 0 / 0.05) |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px; layers a.inline-flex.items-center 87.5x40.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, rgb(194, 194, 194) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 8px |
| pressed | size 85.77 x 39.2; background oklab(0 0 0 / 0.05) |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Login link
"Log in" — the header auth link; measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 80.63 x 40; padding 0px 18px; radius 8px; background transparent; text ui-sans-serif 16/16 500, #1f1f1f `color.gray.12`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0 0 0 / 0.05) |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px; layers a.inline-flex.items-center 80.6x40.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, rgb(194, 194, 194) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 8px |
| pressed | size 79.01 x 39.2; background oklab(0 0 0 / 0.05) |

![Login link default](components/crops/nav-login-default.png) ![Login link hover](components/crops/nav-login-hover.png) ![Login link focus-visible](components/crops/nav-login-focus-visible.png) ![Login link pressed](components/crops/nav-login-pressed.png)

#### Sign-up button
"Sign up" — the 91x40 #00a6f4 nav CTA; measured, never followed. Read as `signup-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 91.8 x 40; padding 0px 18px; radius 8px; background #00a6f4 `color.cushion.accent`; text ui-sans-serif 16/16 500, #ffffff `color.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #0085c3 `color.cushion.accent-dark` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px |
| pressed | size 89.96 x 39.2; background #0085c3 `color.cushion.accent-dark` |

![Sign-up button default](components/crops/signup-btn-default.png) ![Sign-up button hover](components/crops/signup-btn-hover.png) ![Sign-up button focus-visible](components/crops/signup-btn-focus-visible.png) ![Sign-up button pressed](components/crops/signup-btn-pressed.png)

#### Get-started CTA
"Get started" — the 119x44 #00a6f4 primary CTA; measured, never followed. Read as `cta-start` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 119.83 x 44; padding 0px 18px; radius 12px; background #00a6f4 `color.cushion.accent`; text ui-sans-serif 16/24 500, #ffffff `color.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #0085c3 `color.cushion.accent-dark` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px |
| pressed | size 117.43 x 43.12; background #0085c3 `color.cushion.accent-dark` |

![Get-started CTA default](components/crops/cta-start-default.png) ![Get-started CTA hover](components/crops/cta-start-hover.png) ![Get-started CTA focus-visible](components/crops/cta-start-focus-visible.png) ![Get-started CTA pressed](components/crops/cta-start-pressed.png)

#### Secondary CTA
"Talk to a human" — the 154x44 #fcfcfc secondary CTA; measured, never followed. Read as `cta-human` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 154.14 x 44; padding 0px 18px; border 1px solid rgba(33, 33, 33, 0.1); radius 12px; background #fcfcfc `color.cushion.background`; text ui-sans-serif 16/24 500, #1f1f1f `color.gray.12`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f5f5f5 `color.gray.2` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px |
| pressed | size 151.06 x 43.12; background #f5f5f5 `color.gray.2` |

![Secondary CTA default](components/crops/cta-human-default.png) ![Secondary CTA hover](components/crops/cta-human-hover.png) ![Secondary CTA focus-visible](components/crops/cta-human-focus-visible.png) ![Secondary CTA pressed](components/crops/cta-human-pressed.png)

#### Footer
The 1240x184 link-columns footer band. Read as `footer` on the home page.

**Values (default).** size 1240 x 184; background transparent; text ui-sans-serif 16/24 400, #1f1f1f `color.gray.12`; icon 89.59 x 20, #1f1f1f `color.gray.12`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer link (Privacy); measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 52.86 x 18; background transparent; text ui-sans-serif 16/24 400, #858585 `color.gray.10` |
| hover | text ui-sans-serif 16/24 400, #1f1f1f `color.gray.12` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.hover:text-gray-12 52.9x18.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text ui-sans-serif 16/24 400, #1f1f1f `color.gray.12` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Home

The landing: 60px Inter Tight hero, the 36px 'Workspace messaging is broken' problem statement, the feature headings and the embedded 'Acme Inc' inbox mock — a marketing component with a 1280px frame, 209x32 sidebar rows and a 606px post card.

#### Hero heading
"Work messaging that keeps your team organised" — the 60px Inter Tight hero. Read as `hero-h1` on the home page.

**Values (default).** size 768 x 120; background transparent; text Inter Tight 60/60 600, #1f1f1f `color.gray.12`.

![Hero heading default](components/crops/hero-h1-default.png)

#### Hero subhead
"Cushion is the async messaging app for small, distributed teams." Read as `hero-sub` on the home page.

**Values (default).** size 768 x 56; background transparent; text ui-sans-serif 20/28 500, #858585 `color.gray.10`.

![Hero subhead default](components/crops/hero-sub-default.png)

#### Problem heading
"Workspace messaging is broken" — the animated problem statement. Read as `problem-h2` on the home page.

**Values (default).** size 728 x 562; background transparent; text ui-sans-serif 36/54 600, #1f1f1f `color.gray.12`; icon 31.5 x 31.5, #1f1f1f `color.gray.12`; layers span.relative.inline-flex 49.1x33.7 oklch(0.637 0.237 25.331) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px 3.35544e+07px; div.pointer-events-none.select-none 167.9x54.0; div.h-[2px].w-[16px] 16.0x2.0 rgb(209, 209, 209) 3.35544e+07px; di.

Child layers that carry the look: span 49.1x33.7 background oklch(0.637 0.237 25.331) radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px; div 167.9x54 image linear-gradient(to right in oklab, transparent 0%, #fafafa `color.gray.1` 100%); div 16x2 background #d1d1d1 `color.gray.6` radius 3.35544e+07px.

![Problem heading default](components/crops/problem-h2-default.png)

#### Feature heading
"Collaborate without the chaos" — the feature section heading. Read as `feature-h2` on the home page.

**Values (default).** size 608 x 40; background transparent; text Inter Tight 36/40 600, #1f1f1f `color.gray.12`.

![Feature heading default](components/crops/feature-h2-default.png)

#### App mock frame
The embedded "Acme Inc" inbox product mock. Read as `mock-frame` on the home page.

**Values (default).** size 1280 x 720; border 1px solid rgba(33, 33, 33, 0.1); radius 12px 12px 0px 0px; background #fcfcfc `color.cushion.background`; text ui-sans-serif 10/15 600, oklch(0.398 0.07 227.392); icon 16 x 16, #1f1f1f `color.gray.12`.

![App mock frame default](components/crops/mock-frame-default.png)

#### Mock: New post
The mock inbox "New post" button (209x32). Read as `mock-newpost` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 209 x 32; padding 0px 10px; border 1px solid rgba(33, 33, 33, 0.1); radius 6px; background #fcfcfc `color.cushion.background`; text ui-sans-serif 14/20 500, #1f1f1f `color.gray.12`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #1f1f1f `color.gray.12` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px |
| pressed | size 204.82 x 31.36; background #f5f5f5 `color.gray.2`; icon 15.68 x 15.68, #1f1f1f `color.gray.12` |

![Mock: New post default](components/crops/mock-newpost-default.png) ![Mock: New post hover](components/crops/mock-newpost-hover.png) ![Mock: New post focus-visible](components/crops/mock-newpost-focus-visible.png) ![Mock: New post pressed](components/crops/mock-newpost-pressed.png)

#### Mock: channel
A mock sidebar channel button (209x32). Read as `mock-channel` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 209 x 32; padding 0px 8px; radius 6px; background transparent; text ui-sans-serif 16/24 500, #1f1f1f `color.gray.12`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto #005fcc, offset 0px; layers button.w-full.flex 209.0x32.0 1px auto rgb(0, 95, 204) offset 0px 6px |
| pressed | background #f5f5f5 `color.gray.2` |

![Mock: channel default](components/crops/mock-channel-default.png) ![Mock: channel hover](components/crops/mock-channel-hover.png) ![Mock: channel focus-visible](components/crops/mock-channel-focus-visible.png) ![Mock: channel pressed](components/crops/mock-channel-pressed.png)

#### Mock: post card
A mock post card in the inbox mock (606x108). Read as `mock-post` on the home page.

**Values (default).** size 606 x 108; padding 16px; background transparent; text ui-sans-serif 14/20 500, #1f1f1f `color.gray.12`; transition color 0.5s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), fill 0.5s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.5s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.5s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.5s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.5s cubic-bezier(0.4, 0, 0.2, 1); layers span.px-1.5.rounded-md 87.0x18.0 rgb(235, 235, 235) 6px.

Child layers that carry the look: span 87x18 background #ebebeb `color.gray.3` radius 6px.

![Mock: post card default](components/crops/mock-post-default.png)

#### Mock: post footer
The mock post action bar ("Save for later" / "Post"). Read as `mock-post-bar` on the home page.

**Values (default).** size 655.08 x 48; padding 0px 12px; border T: 1px solid rgba(33, 33, 33, 0.1); background transparent; text ui-sans-serif 16/20 500, #1f1f1f `color.gray.12`; icon 16 x 16, #1f1f1f `color.gray.12`.

![Mock: post footer default](components/crops/mock-post-bar-default.png)

#### Comparison heading
"The best Slack alternative for async teams". Read as `cmp-h1` on the slack-alternative page.

**Values (default).** size 768 x 120; background transparent; text Inter Tight 60/60 600, #1f1f1f `color.gray.12`.

![Comparison heading default](components/crops/cmp-h1-default.png)

#### Comparison section
A comparison page section/article. Read as `cmp-article` on the slack-alternative page.

**Values (default).** size 366 x 148; radius 8px; background #fcfcfc `color.cushion.background`; shadow oklab(0 0 0 / 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text ui-sans-serif 14/20 500, #1f1f1f `color.gray.12`.

![Comparison section default](components/crops/cmp-article-default.png)

### Pricing

The /pricing page: the '$8/mo/user' single-plan panel (1240x354, 16px radius), the 143x56 Get-started CTA and the 72px FAQ accordion rows, opened and closed locally.

#### Pricing heading
"Everything you need for just $8/mo/user." Read as `pricing-h2` on the pricing page.

**Values (default).** size 579 x 160; background transparent; text ui-sans-serif 36/40 600, #1f1f1f `color.gray.12`; layers mark.bg-accent/30.rounded-md 188.8x43.0 oklab(0.69202 -0.0788308 -0.138685 / 0.3) 6px.

Child layers that carry the look: mark 188.8x43 background oklab(0.69202 -0.0788308 -0.138685 / 0.3) radius 6px.

![Pricing heading default](components/crops/pricing-h2-default.png)

#### Plan panel
The single-plan panel ($8/mo/user + 30-day trial copy). Read as `plan-panel` on the pricing page.

**Values (default).** size 1240 x 354; padding 24px; border 1px solid rgba(33, 33, 33, 0.1); radius 16px; background #fafafa `color.gray.1`; text ui-sans-serif 36/40 600, #1f1f1f `color.gray.12`; icon 20 x 20, #00a6f4 `color.cushion.accent`.

![Plan panel default](components/crops/plan-panel-default.png)

#### Pricing CTA
"Get started" — the pricing-page CTA; measured, never followed. Read as `pricing-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 143.81 x 56; padding 0px 20px; radius 16px; background #00a6f4 `color.cushion.accent`; text ui-sans-serif 20/28 600, #ffffff `color.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #0085c3 `color.cushion.accent-dark` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px |
| pressed | size 140.94 x 54.88; background #0085c3 `color.cushion.accent-dark` |

![Pricing CTA default](components/crops/pricing-cta-default.png) ![Pricing CTA hover](components/crops/pricing-cta-hover.png) ![Pricing CTA focus-visible](components/crops/pricing-cta-focus-visible.png) ![Pricing CTA pressed](components/crops/pricing-cta-pressed.png)

#### FAQ item
A FAQ accordion row ("How's this different from Slack?"); opened and closed locally. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1238 x 72; padding 0px 16px; border B: 1px solid rgba(33, 33, 33, 0.1); background #fcfcfc `color.cushion.background`; text ui-sans-serif 18/28 500, #1f1f1f `color.gray.12`; icon 16 x 16, #1f1f1f `color.gray.12` |
| opened | background #ebebeb `color.gray.3` |

![FAQ item default](components/crops/faq-item-default.png) ![FAQ item opened](components/crops/faq-item-opened.png)

### Updates

The /updates changelog: release entries (~1024x1720) with a 32px release title and item headings.

#### Update entry
A changelog entry (date + items, ~1024x1719). Read as `update-entry` on the updates page.

**Values (default).** size 1024 x 1719.88; background transparent; text ui-sans-serif 14/20 400, #8f8f8f `color.gray.9`.

![Update entry default](components/crops/update-entry-default.png)

#### Update title
A release title ("Post Redesign, Slack Sync Upgrades, and more"). Read as `update-h2` on the updates page.

**Values (default).** size 840 x 32; background transparent; text ui-sans-serif 24/32 600, #000000 `color.cushion.foreground`.

![Update title default](components/crops/update-h2-default.png)

#### Update item
A release item heading. Read as `update-h3` on the updates page.

**Values (default).** size 840 x 35.19; background transparent; text ui-sans-serif 22/35.2 600, #1f1f1f `color.gray.12`.

![Update item default](components/crops/update-h3-default.png)

### Blog

The /blog list: the 1240x339 featured row and the 397x403 post cards (12px radius).

#### Featured post
The featured blog row (1240x339); measured, never followed. Read as `blog-featured` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1240 x 339.75; background transparent; text ui-sans-serif 12/16 400, #666666 `color.gray.11` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Featured post default](components/crops/blog-featured-default.png) ![Featured post hover](components/crops/blog-featured-hover.png) ![Featured post pressed](components/crops/blog-featured-pressed.png)

#### Blog card
A 397x403 post card; measured, never followed. Read as `blog-card` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 397.33 x 403.5; radius 12px; background transparent; text ui-sans-serif 12/16 400, #666666 `color.gray.11` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Blog card default](components/crops/blog-card-default.png) ![Blog card hover](components/crops/blog-card-hover.png) ![Blog card pressed](components/crops/blog-card-pressed.png)

#### Card title
A post card title (text-lg). Read as `blog-card-title` on the blog page.

**Values (default).** size 604 x 36; background transparent; text Inter Tight 30/36 600, #000000 `color.cushion.foreground`.

![Card title default](components/crops/blog-card-title-default.png)

### Legal

The /terms page: the heading and body column.

#### Legal heading
"Terms of Service" — the legal page heading. Read as `legal-h1` on the terms page.

**Values (default).** size 736 x 40; background transparent; text ui-sans-serif 36/40 700, #1f1f1f `color.gray.12`.

![Legal heading default](components/crops/legal-h1-default.png)

#### Legal paragraph
A body paragraph of the terms text. Read as `legal-body` on the terms page.

**Values (default).** size 736 x 26; background transparent; text ui-sans-serif 16/26 400, #1f1f1f `color.gray.12`.

![Legal paragraph default](components/crops/legal-body-default.png)

### Mobile (390 wide)

The home at phone width: the same 72px nav, the 48px hero and the full-width CTA.

#### Mobile nav
Read as `m-nav-bar` on the home page at 390 wide.

**Values (default).** size 390 x 72; background #fcfcfc `color.cushion.background`; text ui-sans-serif 16/24 400, #1f1f1f `color.gray.12`; icon 112 x 25, #1f1f1f `color.gray.12`.

![Mobile nav default](components/crops/m-nav-bar-default.png)

#### Mobile hero
The hero at 390px. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 350 x 192; background transparent; text Inter Tight 48/48 600, #1f1f1f `color.gray.12`.

![Mobile hero default](components/crops/m-hero-h1-default.png)

#### Mobile CTA
"Get started" at 390px; measured, never followed. Read as `m-cta-start` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 350 x 44; padding 0px 18px; radius 12px; background #00a6f4 `color.cushion.accent`; text ui-sans-serif 16/24 500, #ffffff `color.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #c2c2c2 0px 0px 0px 4px |
| pressed | size 343 x 43.12 |

![Mobile CTA default](components/crops/m-cta-start-default.png) ![Mobile CTA hover](components/crops/m-cta-start-hover.png) ![Mobile CTA focus-visible](components/crops/m-cta-start-focus-visible.png) ![Mobile CTA pressed](components/crops/m-cta-start-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the wordmark, the mock emoji channel markers, the post avatars) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The signed-in Cushion app — real inboxes, posting, check-ins, settings, and the desktop download — was never reached. 'Log in', 'Sign up', 'Get started', 'Talk to a human' and every download/store link are measured controls, never followed; every public surface is read-only. The 'Acme Inc' inbox on the home page is a rendered marketing mock, not the product. What the product looks like past sign-up is not documented here.

### Pages

- **App and CTAs.** 'Log in', 'Sign up', 'Get started', 'Talk to a human' and the download links were measured, never followed; no account exists on this surface.
- **The app mock is a mock.** The 'Acme Inc' inbox on the home page is a marketing component; its buttons, channels and post cards were measured as DOM, but they are not the authenticated product.
- **Other pages.** /download and /integrations were screenshotted but their cards were not measured as components; /privacy was not captured (same legal layout as /terms).
- **External surfaces** (Crisp chat widget, app-store links, social links) are present on the page but were never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **The FAQ accordion** was toggled locally; nothing was typed or submitted anywhere.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

One painted theme, no toggle: every page paints light (#f5f5f5 page, #fcfcfc/#fafafa surfaces, #1f1f1f ink, #00a6f4 accent). The stylesheets do declare a `.dark` block, but no element on the public pages carries the class and nothing paints it — it is a declared, unpainted layer, so tokens.json emits light only (185 resolved :root vars).

### Fonts

- **Inter Tight** (600, headings only) is the product's display face, loaded from Google Fonts; body, nav, buttons and cards use the system-ui stack. Font files are not shipped in this package.

### Screenshots

- The mock inbox contents (channel names, post text, avatars) and the blog/update imagery in the screenshots are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The blog post titles, update entries, FAQ copy and marketing illustrations are the product's content; only frames and components were measured.
