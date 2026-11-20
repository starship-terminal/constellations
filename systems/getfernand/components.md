# Fernand components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from getfernand.com, app.getfernand.com and help.getfernand.com on 2026-11-15, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the login and signup forms were never sent; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (87 components, 183 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value in the component's own surface set (light / help / app / dark — the hosts remap the shared palette names), when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/24 500, #131e40`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (181 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the surface painted at capture: `light` for every marketing page, the signed-out app forms and the docs site in light — getfernand.com is light-only (`color-scheme: light`); `dark` for the docs article painted under `body.dark-mode` by the site's own 'Switch to dark mode' link. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [ai-menu](screenshots/home-light-ai-menu.png), [default](screenshots/home-light-default.png), [demo-modal](screenshots/home-light-demo-modal.png), [full](screenshots/home-light-full.png), [launcher-open](screenshots/home-light-launcher-open.png) |
| Pricing | `/pricing/` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| About | `/about-us/` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Blog | `/blog/` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Updates | `/updates/` | [default](screenshots/updates-light-default.png), [full](screenshots/updates-light-full.png) |
| Updates article | `/updates/dodo-payments-integration/` | [default](screenshots/updates-article-light-default.png), [full](screenshots/updates-article-light-full.png) |
| Integrations | `/integrations/` | [default](screenshots/integrations-light-default.png), [full](screenshots/integrations-light-full.png) |
| Integration (Slack) | `/integrations/slack/` | [default](screenshots/integration-slack-light-default.png), [full](screenshots/integration-slack-light-full.png) |
| AI agents | `/feature/ai-agents/` | [default](screenshots/feature-ai-light-default.png), [full](screenshots/feature-ai-light-full.png) |
| Headless support | `/feature/headless-customer-support/` | [default](screenshots/feature-headless-light-default.png), [full](screenshots/feature-headless-light-full.png) |
| Intercom alternative | `/alternative/intercom/` | [default](screenshots/alternative-intercom-light-default.png), [full](screenshots/alternative-intercom-light-full.png) |
| Privacy | `/privacy/` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| App sign-in | `app.getfernand.com/auth/login` | [default](screenshots/login-light-default.png) |
| App signup | `app.getfernand.com/create` | [default](screenshots/signup-light-default.png) |
| Docs home | `help.getfernand.com` | [dark-default](screenshots/help-dark-dark-default.png), [dark-full](screenshots/help-dark-dark-full.png), [default](screenshots/help-light-default.png), [full](screenshots/help-light-full.png), [search](screenshots/help-light-search.png) |
| Docs article | `help.getfernand.com/getting-started` | [default](screenshots/help-article-light-default.png), [full](screenshots/help-article-light-full.png) |
| Docs article, dark | `help.getfernand.com/getting-started` | [default](screenshots/help-dark-dark-default.png), [full](screenshots/help-dark-dark-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `/pricing/` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Docs article, phone | `help.getfernand.com/getting-started` | [default](screenshots/mobile-help-light-default.png), [full](screenshots/mobile-help-light-full.png), [menu](screenshots/mobile-help-light-menu.png) |
| App sign-in, phone | `app.getfernand.com/auth/login` | [default](screenshots/mobile-login-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Consent overlay | every page | no consent banner was observed on any of the three hosts; any layer would be hidden, never answered | hidden before every shot and reading |
| Install-with-AI menu | home hero | clicked the 'Install with AI' aria-haspopup button | [home-light-ai-menu](screenshots/home-light-ai-menu.png), [ai-setup-toggle](#install-with-ai-menu-button), [ai-setup-item](#ai-setup-menu-item) |
| Demo dialog | home hero | clicked 'Watch a 2 minute demo'; the video pauses for the shot and Escape closes it | [home-light-demo-modal](screenshots/home-light-demo-modal.png), [demo-dialog](#demo-dialog) |
| Widget panel | every marketing page | clicked the Fernand chat-widget launcher — the product's own embed; never typed into | [home-light-launcher-open](screenshots/home-light-launcher-open.png), [launcher](#widget-launcher), [launcher-panel](#widget-panel) |
| Docs search | help.getfernand.com | typed 'channel' into #search-field then cleared it | [help-light-search](screenshots/help-light-search.png), [help-search-pop](#search-popover) |
| Docs dark mode | help.getfernand.com | clicked the site's own 'Switch to dark mode' link | [help-dark-default](screenshots/help-dark-dark-default.png), [help-dark-toggle](#dark-mode-switch) |
| Mobile menu | docs article, phone width | the docs site's menu toggle | [mobile-help-light-menu](screenshots/mobile-help-light-menu.png) |
| Login/signup fields | app.getfernand.com | typed into then cleared — nothing sent | [login-field](#email-field-login), [create-field](#email-field-signup) |
| Cal.com booking | every marketing page | the 'Book a demo' action loads the Cal.com scheduler; measured, never activated | boundary; see Gaps |
| Signed-in product | a Fernand account | every post-login surface (the inbox workspace, settings, API keys) needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 25 components were given a real keyboard focus. 19 draw an outline ring: `nav-link` (1px auto #121213, offset 0.96875px), `nav-login` (1px auto #121213, offset 0.96875px), `nav-demo` (1px auto #1e2024, offset 0px), `nav-cta` (1px auto #161616 `border.focus-ring`, offset 0.96875px), `hero-cta` (1px auto #151515, offset 0.96875px), `hero-cta2` (1px auto #101011, offset 0px), `ai-setup-toggle` (2px solid #1a2035 `text.ink`, offset 2px), `footer-cta` (1px auto #171717, offset 0.96875px), `footer-link` (1px auto rgba(19, 19, 19, 0.99), offset 0.96875px), `pricing-cta` (1px auto #161616 `border.focus-ring`, offset 0.96875px), `ag-switch` (2px solid #1a2035 `text.ink`, offset 2px), `login-link` (1px auto #131414, offset 0.96875px), `create-continue` (1px auto #121212, offset 0px), `help-nav-item` (1px auto #111111, offset 0.984375px), `help-dark-toggle` (1px auto #121212, offset 0.96875px), `help-goto` (1px auto #101011, offset 0.984375px), `help-content-link` (1px auto #101011, offset 0.96875px), `m-cta` (1px auto #e69a06, offset 0.96875px), `m-hero-cta` (1px auto #e69905, offset 0.96875px). 1 draw a focus ring as a shadow instead: `login-submit`. The other 5 show no measured change: `hero-demo-btn`, `channels-arrow`, `wpg-color`, `alt-faq-summary`, `ag-replay`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.12s | `ease-out` | background | ai-setup-item |
| 0.15s | `ease` | box-shadow, color | ag-replay, wpg-color |
| 0.15s | `ease-out` | background, color | ai-setup-item, ai-setup-toggle |
| 0.16s | `cubic-bezier(0.23, 1, 0.32, 1)` | transform | ai-setup-toggle, hero-demo-btn |
| 0.16s | `ease-out` | transform | ag-replay |
| 0.2s | `ease` | background-color, box-shadow, color, opacity, transform | ag-switch, channels-arrow, wpg-tab |
| 0.25s | `ease` | color | wpg-article |
| 0.3s | `ease-in-out` | opacity | create-panel |
| 0.75s | `cubic-bezier(0.19, 1, 0.22, 1)` | all | create-checkbox, create-continue, create-field, create-field-name, footer-cta, footer-link, hd-card, hd-nav-item and more |
| 1.5s | `cubic-bezier(0.19, 1, 0.22, 1)` | all | alt-h1, hero-h1, int-card, int-eyebrow, m-hero-h1, nav-demo, upd-h1 |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Channel card](#channel-card) | 300 x 256 | - | 10px | #f7fafc `surface.card` | none | 24px |
| [Free plan card](#free-plan-card) | 636 x 573.16 | - | 16px | #ffffff `white` | rgba(0, 160, 255, 0.18) 16px 22px 64px 0px, rgba(0, 160, 255, 0.4) 0px 0px 0px 1px, rgba(18, 55, 105, 0.06) 0px 8px 24px 0px | 0 |
| [Paid plan card](#paid-plan-card) | 424 x 573.16 | - | 16px | #ffffff `white` | rgba(18, 55, 105, 0.08) 0px 2px 4px 0px, rgba(18, 55, 105, 0.04) 0px 1px 1px 0px, rgba(18, 55, 105, 0.08) 0px 0px 0px 1px | 0 |
| [Feature card](#feature-card) | 416.67 x 569.61 | - | 8px | #ffffff `white` | #f0f0f5 0px 0px 0px 1px | 0 |
| [Essential integration card](#essential-integration-card) | 324.67 x 551.61 | - | 8px | #ffffff `white` | #f0f0f5 0px 0px 0px 1px | 0 |
| [Collection card](#collection-card) | 310 x 146.78 | 1px solid #eaecf8 `border.default` | 5px | transparent | none | 22px |
| [Trusted-by card](#trusted-by-card) | 147 x 60.48 | - | - | transparent | none | 0 |
| [Login card](#login-card) | 350 x 216.25 | - | - | transparent | none | 0 |

## Components

### Site chrome

The fixed header on every marketing page: wordmark, About us / Pricing / Log in links, the 'Book a demo' Cal.com action and the 'Start for free' button.

#### Site header
The fixed top bar: wordmark, About us / Pricing / Log in nav links, the "Book a demo" Cal.com action and the "Start for free" button. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 71.5; padding 12px 0px; background transparent; shadow rgba(25, 30, 90, 0) 0px -1px 0px 0px inset; text Inter 14/14 500, #6f7b96 `text.link`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); icon 35 x 45.5, #0000ee; layers header.transit.transit--slow 1440.0x71.5 rgba(25, 30, 90, 0) 0px -1px 0px 0px inset; a 115.0x30.0 rgb(255, 255, 255) rgba(18, 55, 105, 0.08) 0px 2px 4px 0px, rgba(18, 55, 105, 0.04) 0px 1px 1px 0px, rgba(18, 55, 105, 0.08) 0px 0px 0px 1px 6px; a 115.0x30.0 rgb(0, 160, 255) 6px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Fernand mark-and-wordmark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 35 x 20; background transparent; text Inter 16/16 400, #0000ee; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); icon 35 x 45.5, #0000ee.

![Logo default](components/crops/mkt-logo-default.png)

#### Nav link
A marketing header nav link (About us); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 84 x 37; padding 10px; background transparent; text Inter 14/14 500, #6f7b96 `text.link`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| hover | text Inter 14/14 500, #00a0ff `blue.default` |
| focus-visible | outline 1px auto #121213, offset 0.96875px; layers a 84.0x37.0 1px auto rgb(18, 18, 19) offset 0.96875px |
| pressed | text Inter 14/14 500, #3f8bc4 |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log in link
The "Log in" nav link to app.getfernand.com; measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 62 x 37; padding 10px; background transparent; text Inter 14/14 500, #6f7b96 `text.link`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| hover | text Inter 14/14 500, #01a0ff |
| focus-visible | outline 1px auto #121213, offset 0.96875px; layers a 62.0x37.0 1px auto rgb(18, 18, 19) offset 0.96875px |
| pressed | text Inter 14/14 500, #029ffe |

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Book a demo action
The "Book a demo" header action — a Cal.com scheduler link (data-cal-link, role="button"); measured, never activated. Read as `nav-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 115 x 30; padding 8px 12px; radius 6px; background #ffffff `white`; shadow rgba(18, 55, 105, 0.08) 0px 2px 4px 0px, rgba(18, 55, 105, 0.04) 0px 1px 1px 0px, rgba(18, 55, 105, 0.08) 0px 0px 0px 1px; text Inter 14/14 500, #6f7b96 `text.link`; transition all 1.5s cubic-bezier(0.19, 1, 0.22, 1) |
| hover | text Inter 14/14 500, #5a657f |
| focus-visible | outline 1px auto #1e2024, offset 0px; text Inter 14/14 500, #6e7a95 |
| pressed | text Inter 14/14 500, #5b6680 |

![Book a demo action default](components/crops/nav-demo-default.png) ![Book a demo action hover](components/crops/nav-demo-hover.png) ![Book a demo action focus-visible](components/crops/nav-demo-focus-visible.png) ![Book a demo action pressed](components/crops/nav-demo-pressed.png)

#### Header CTA
The "Start for free" header button linking to the signup; measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 115 x 30; padding 8px 12px; radius 6px; background #00a0ff `blue.default`; text Inter 14/14 500, #ffffff `white`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| focus-visible | outline 1px auto #161616 `border.focus-ring`, offset 0.96875px |

![Header CTA default](components/crops/nav-cta-default.png) ![Header CTA hover](components/crops/nav-cta-hover.png) ![Header CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Header CTA pressed](components/crops/nav-cta-pressed.png)

### Home

The light home page: the 38px 'The free customer support platform for SaaS teams' masthead, the dated changelog eyebrow pill, the dark 'Start for free' CTA and 'Book a demo' action, the Install-with-AI menu, the demo dialog, the channels carousel, feature cards, the widget playground and testimonials.

#### Update eyebrow pill
The dated changelog pill above the masthead ("Oct. 27 — Dodo Payments integration"); measured, never followed. Read as `hero-eyebrow` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 259 x 30; padding 5px 12px 5px 5px; radius 40px; background #ffffff `white`; shadow rgba(18, 55, 105, 0.08) 0px 2px 4px 0px, rgba(18, 55, 105, 0.04) 0px 1px 1px 0px, rgba(18, 55, 105, 0.08) 0px 0px 0px 1px; text Inter 12/12 600, #00a0ff `blue.default`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |

![Update eyebrow pill default](components/crops/hero-eyebrow-default.png) ![Update eyebrow pill hover](components/crops/hero-eyebrow-hover.png)

#### Hero headline
"The free customer support platform for SaaS teams" — the 38px display heading. Read as `hero-h1` on the home page.

**Values (default).** size 1290 x 96; background transparent; text Inter 38/48 400, #1a2035 `text.ink`; transition all 1.5s cubic-bezier(0.19, 1, 0.22, 1).

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero lede
The hero standfirst under the masthead. Read as `hero-sub` on the home page.

**Values (default).** size 640 x 84.14; background transparent; text Inter 17/28.05 400, #717583 `grey.medium`.

![Hero lede default](components/crops/hero-sub-default.png)

#### Hero CTA
The dark "Start for free" hero button (8px radius); measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 170 x 49; padding 13px 20px; border 1px solid #1a2035 `text.ink`; radius 8px; background #1a2035 `text.ink`; text Inter 15/20 500, #ffffff `white`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| focus-visible | outline 1px auto #151515, offset 0.96875px |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero demo link
The "Book a demo" secondary action in the hero — a Cal.com link; measured, never activated. Read as `hero-cta2` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 137 x 48; padding 13px 20px; border 1px solid rgba(18, 55, 105, 0.12); radius 8px; background #ffffff `white`; shadow rgba(18, 55, 105, 0.08) 0px 2px 4px 0px, rgba(18, 55, 105, 0.04) 0px 1px 1px 0px; text Inter 15/20 500, #1a2035 `text.ink`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| focus-visible | outline 1px auto #101011, offset 0px |

![Hero demo link default](components/crops/hero-cta2-default.png) ![Hero demo link hover](components/crops/hero-cta2-hover.png) ![Hero demo link focus-visible](components/crops/hero-cta2-focus-visible.png) ![Hero demo link pressed](components/crops/hero-cta2-pressed.png)

#### Demo button
The "Watch a 2 minute demo" play button — a local UI toggle opening the video dialog. The opened state measured the dialog it mounts. Read as `hero-demo-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed, opened) | size 240 x 50; padding 16px 20px; radius 40px; background #ffffff `white`; shadow rgba(18, 55, 105, 0.08) 0px 2px 4px 0px, rgba(18, 55, 105, 0.04) 0px 1px 1px 0px, rgba(18, 55, 105, 0.08) 0px 0px 0px 1px; text Inter 15/15 500, #3d4259 `grey.strong`; transition transform 0.16s cubic-bezier(0.23, 1, 0.32, 1); icon 18 x 18, #3d4259 `grey.strong` |

![Demo button default](components/crops/hero-demo-btn-default.png) ![Demo button hover](components/crops/hero-demo-btn-hover.png) ![Demo button focus-visible](components/crops/hero-demo-btn-focus-visible.png) ![Demo button pressed](components/crops/hero-demo-btn-pressed.png) ![Demo button opened](components/crops/hero-demo-btn-opened.png)

#### Demo dialog
The video dialog mounted by the demo button — a YouTube-nocookie embed over .demo-modal__backdrop; opened by its own toggle, closed with Escape. Read as `demo-dialog` on the home page.

**Values (default).** size 1280 x 720; radius 4px; background #eef2f4; text Inter 16/16 400, #3a5571.

![Demo dialog default](components/crops/demo-dialog-default.png)

#### Install-with-AI menu button
The "Install with AI" button — an aria-haspopup="menu" trigger whose menu copies a setup prompt per agent. The opened state was measured after clicking it. Read as `ai-setup-toggle` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 183 x 47; padding 13px 20px; radius 8px; background transparent; text Inter 15/21 500, #6f7b96 `text.link`; transition color 0.15s ease-out, background 0.15s ease-out, transform 0.16s cubic-bezier(0.23, 1, 0.32, 1); icon 15 x 15, #6f7b96 `text.link` |
| hover | background rgba(0, 0, 0, 0.04); text Inter 15/21 500, #1a2035 `text.ink`; icon 15 x 15, #1a2035 `text.ink` |
| focus-visible | outline 2px solid #1a2035 `text.ink`, offset 2px; layers button.ai-setup__toggle 183.0x47.0 2px solid rgb(26, 32, 53) offset 2px 8px |
| pressed | size 177.51 x 45.59; background rgba(0, 0, 0, 0.04); text Inter 15/21 500, #1a2035 `text.ink`; transform scale(0.97); icon 14.55 x 14.55, #1a2035 `text.ink` |
| opened | background rgba(0, 0, 0, 0.04); text Inter 15/21 500, #1a2035 `text.ink`; icon 15 x 15, #1a2035 `text.ink` |

![Install-with-AI menu button default](components/crops/ai-setup-toggle-default.png) ![Install-with-AI menu button hover](components/crops/ai-setup-toggle-hover.png) ![Install-with-AI menu button focus-visible](components/crops/ai-setup-toggle-focus-visible.png) ![Install-with-AI menu button pressed](components/crops/ai-setup-toggle-pressed.png) ![Install-with-AI menu button opened](components/crops/ai-setup-toggle-opened.png)

#### AI-setup menu item
One item in the Install-with-AI menu (an agent prompt to copy); the menu was opened by its own toggle; the item was never activated. Read as `ai-setup-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 332 x 29.59; padding 7px 8px; radius 7px; background transparent; text Inter 13/15.6 500, #1a2035 `text.ink`; transition background 0.12s ease-out, color 0.15s ease-out; icon 14 x 14, #3a4154 |
| hover | background rgba(26, 32, 53, 0.043) |

![AI-setup menu item default](components/crops/ai-setup-item-default.png) ![AI-setup menu item hover](components/crops/ai-setup-item-hover.png)

#### Section tag pill
The small white eyebrow pill labelling each marketing section. Read as `section-tag` on the home page.

**Values (default).** size 132 x 28; padding 7px 14px; radius 40px; background #ffffff `white`; shadow rgba(18, 55, 105, 0.08) 0px 2px 4px 0px, rgba(18, 55, 105, 0.04) 0px 1px 1px 0px, rgba(18, 55, 105, 0.08) 0px 0px 0px 1px; text Inter 13/13 500, #1a2035 `text.ink`; icon 14 x 14, #1a2035 `text.ink`.

![Section tag pill default](components/crops/section-tag-default.png)

#### Channel card
A card in the "Consolidate all your support channels" carousel (300px, #f7fafc, 10px radius). Read as `channels-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 300 x 256; padding 24px; radius 10px; background #f7fafc `surface.card`; text Inter 18/30 400, #1a2035 `text.ink`; icon 18 x 18, #1a2035 `text.ink` |

![Channel card default](components/crops/channels-card-default.png) ![Channel card hover](components/crops/channels-card-hover.png)

#### Carousel arrow
The channels carousel's "Scroll right" arrow button; measured, never used to page the carousel. Read as `channels-arrow` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; padding 1px 6px; border 1px solid #e8e8f0; radius 50%; background #ffffff `white`; shadow rgba(0, 0, 0, 0.1) 0px 2px 12px 0px; text Inter 16/18.4 400, #1a2035 `text.ink`; transition opacity 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease; transform translate(0px, -22px); icon 16 x 16, #1a2035 `text.ink` |
| hover | shadow rgba(0, 0, 0, 0.15) 0px 4px 20px 0px |
| focus-visible | size 37.4 x 37.4; transform matrix(0.85, 0, 0, 0.85, 0, -22); opacity 0; icon 13.6 x 13.6, #1a2035 `text.ink` |
| pressed | size 37.4 x 37.4; shadow rgba(0, 0, 0, 0.15) 0px 4px 20px 0px; transform matrix(0.85, 0, 0, 0.85, 0, -22); opacity 0; icon 13.6 x 13.6, #1a2035 `text.ink` |

![Carousel arrow default](components/crops/channels-arrow-default.png) ![Carousel arrow hover](components/crops/channels-arrow-hover.png) ![Carousel arrow focus-visible](components/crops/channels-arrow-focus-visible.png) ![Carousel arrow pressed](components/crops/channels-arrow-pressed.png)

#### Feature card
A feat3 feature card in "Support finally connects with your team and product strategy" — product-mock tiles; measured, never followed. Read as `feat-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 416.67 x 569.61; radius 8px; background #ffffff `white`; shadow #f0f0f5 0px 0px 0px 1px; text Inter 14/14 400, #3b82f6; icon 16 x 16, #858ba6 |

![Feature card default](components/crops/feat-card-default.png) ![Feature card hover](components/crops/feat-card-hover.png)

#### Product-mock button
The "View account" primary button inside the "Build your product" product illustration — a drawn mock control, not a live action. Read as `why-btn` on the home page.

Not on the page when it was captured.

#### Product-mock ghost button
The "Upgrade plan" ghost button inside the same product illustration. Read as `why-ghost` on the home page.

Not on the page when it was captured.

#### Testimonial
A customer quote block (22px/1.55 display copy). Read as `testimonial` on the home page.

**Values (default).** size 720 x 293.47; background transparent; text Inter 22/34.1 400, #1a2035 `text.ink`.

![Testimonial default](components/crops/testimonial-default.png)

#### Trusted-by card
A "trusted by" customer card in the dark strip (name + company). Read as `trusted-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 147 x 60.48; background transparent; text Inter 13/16.9 600, #ffffff `white` |

![Trusted-by card default](components/crops/trusted-card-default.png) ![Trusted-by card hover](components/crops/trusted-card-hover.png)

#### Integration logo tile
One logo tile in the "Integrates with your entire stack" grid. Read as `int-logo` on the home page.

**Values (default).** size 28 x 28; background transparent; text Inter 16/16 400, #131e40 `black`; icon 28 x 28, #131e40 `black`.

![Integration logo tile default](components/crops/int-logo-default.png)

#### Widget playground
The "Live chat and AI, embedded in your product" interactive widget playground — an in-page demo of the embeddable widget. Read as `wpg-playground` on the home page.

Not on the page when it was captured.

#### Widget colour swatch
A brand-colour swatch in the widget playground (the selected one carries the double ring); clicking retints the demo widget. Read as `wpg-color` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 22 x 22; padding 1px 6px; radius 50%; background #00a0ff `blue.default`; shadow #ffffff 0px 0px 0px 2px, #00a0ff 0px 0px 0px 4px; text Inter 16/18.4 400, #000000; transition box-shadow 0.15s ease |

![Widget colour swatch default](components/crops/wpg-color-default.png) ![Widget colour swatch hover](components/crops/wpg-color-hover.png) ![Widget colour swatch focus-visible](components/crops/wpg-color-focus-visible.png) ![Widget colour swatch pressed](components/crops/wpg-color-pressed.png)

#### Widget tab
A tab in the playground widget preview (Home / Chat / Articles). Read as `wpg-tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 81.33 x 31; padding 4px 2px; background transparent; text Inter 10/10 400, #00a0ff `blue.default`; transition color 0.2s ease; icon 11 x 11, #00a0ff `blue.default` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Widget tab default](components/crops/wpg-tab-default.png) ![Widget tab hover](components/crops/wpg-tab-hover.png) ![Widget tab pressed](components/crops/wpg-tab-pressed.png)

#### Widget article row
A knowledge-base article row inside the playground widget preview. Read as `wpg-article` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 252 x 23; padding 6px 11px; background transparent; text Inter 11/11 400, #2c3145; transition color 0.25s ease; icon 8 x 8, #9498a5 |

![Widget article row default](components/crops/wpg-article-default.png) ![Widget article row hover](components/crops/wpg-article-hover.png)

### Pricing

The /pricing/ page: the FREE/PAID plan cards ($0 and $29 per active human per month), plan feature rows, the large Start-for-free button and the questions-&-answers list.

#### Plan eyebrow
The blue "FREE" eyebrow over a plan price. Read as `pricing-eyebrow` on the pricing page.

**Values (default).** size 580 x 12; background transparent; text Inter 12/12 600, #00a0ff `blue.default`.

![Plan eyebrow default](components/crops/pricing-eyebrow-default.png)

#### Free plan card
The $0 plan card — the blue radial-gradient fill and ringed shadow variant. Read as `price-free` on the pricing page.

**Values (default).** size 636 x 573.16; radius 16px; background #ffffff `white`; image radial-gradient(115% 78% at 100% 100%, rgba(0, 160, 255, 0.34), rgba(159, 227, 255, 0.18) 46%, rgba(255, 255, 255, 0) 78%), none; shadow rgba(0, 160, 255, 0.18) 16px 22px 64px 0px, rgba(0, 160, 255, 0.4) 0px 0px 0px 1px, rgba(18, 55, 105, 0.06) 0px 8px 24px 0px; text Inter 12/12 600, #00a0ff `blue.default`; icon 16 x 16, #00a0ff `blue.default`.

![Free plan card default](components/crops/price-free-default.png)

#### Paid plan card
The paid plan card ($29 per active human per month). Read as `price-paid` on the pricing page.

**Values (default).** size 424 x 573.16; radius 16px; background #ffffff `white`; shadow rgba(18, 55, 105, 0.08) 0px 2px 4px 0px, rgba(18, 55, 105, 0.04) 0px 1px 1px 0px, rgba(18, 55, 105, 0.08) 0px 0px 0px 1px; text Inter 12/12 600, #8c8f9a; icon 16 x 16, #00a0ff `blue.default`.

![Paid plan card default](components/crops/price-paid-default.png)

#### Plan feature row
One feature line inside a plan card. Read as `pricing-line` on the pricing page.

**Values (default).** size 636 x 43.59; padding 12px 28px; background transparent; text Inter 14/19.6 500, #1a2035 `text.ink`; icon 16 x 16, #00a0ff `blue.default`.

![Plan feature row default](components/crops/pricing-line-default.png)

#### Pricing CTA
The large "Start for free" button on the pricing hero; measured, never followed. Read as `pricing-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 136 x 48; padding 16px; radius 6px; background #00a0ff `blue.default`; text Inter 16/16 500, #ffffff `white`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| focus-visible | outline 1px auto #161616 `border.focus-ring`, offset 0.96875px |

![Pricing CTA default](components/crops/pricing-cta-default.png) ![Pricing CTA hover](components/crops/pricing-cta-hover.png) ![Pricing CTA focus-visible](components/crops/pricing-cta-focus-visible.png) ![Pricing CTA pressed](components/crops/pricing-cta-pressed.png)

#### FAQ question
A question in the "Questions & answers" list (dt/dd pairs). Read as `faq-dt` on the pricing page.

**Values (default).** size 508 x 16; background transparent; text Inter 17/16 500, #131e40 `black`.

![FAQ question default](components/crops/faq-dt-default.png)

#### FAQ answer
An answer in the same FAQ list. Read as `faq-dd` on the pricing page.

**Values (default).** size 508 x 72; background transparent; text Inter 15/24 400, #717583 `grey.medium`.

![FAQ answer default](components/crops/faq-dd-default.png)

### Updates

The /updates changelog: sticky entry titles and article bodies.

#### Updates headline
The /updates changelog masthead. Read as `upd-h1` on the updates page.

**Values (default).** size 1080 x 48; background transparent; text Inter 38/48 400, #1a2035 `text.ink`; transition all 1.5s cubic-bezier(0.19, 1, 0.22, 1).

![Updates headline default](components/crops/upd-h1-default.png)

#### Update entry
One changelog entry on /updates (title column + body). Read as `upd-article` on the updates page.

**Values (default).** size 1080 x 1206.14; background transparent; text Inter 18/25 600, #1a2035 `text.ink`; layers img.wp-image-324 770.0x330.1 T:1px solid rgb(200, 217, 232) / R:1px solid rgb(200, 217, 232) / B:1px solid rgb(200, 217, 232) / L:1px solid rgb(200, 217, 232) 5px; a 125.0x21.0 B:1px solid rgb(0, 160, 255); code 17.8x21.0 rgb(255, 255, 255) T:1px solid rgb(224, 224, 224) / R:1px solid rgb(224, 224, 224) / B:1px solid rgb(224, 224, 224) / L:1px solid rgb(224, 224, 224) 4px; code 17.8x21.0 rgb(255, .

Child layers that carry the look: img 770x330.1 border 1px solid #c8d9e8 radius 5px; a 125x21 border 1px solid #00a0ff `blue.default`; code 17.8x21 background #ffffff `white` border 1px solid #e0e0e0 radius 4px.

![Update entry default](components/crops/upd-article-default.png)

#### Update title
The sticky title cell of a changelog entry. Read as `upd-title` on the updates page.

**Values (default).** size 280 x 1206.14; background transparent; text Inter 18/25 600, #1a2035 `text.ink`.

![Update title default](components/crops/upd-title-default.png)

### Integrations

The /integrations catalogue: Essentials cards with product mocks and the grouped integration grids.

#### Essential integration card
An "Essentials" integration card with a product mock (the Stripe plan card); measured, never followed. Read as `int-essential` on the integrations page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 324.67 x 551.61; radius 8px; background #ffffff `white`; shadow #f0f0f5 0px 0px 0px 1px; text Inter 14/14 400, #d97706; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); icon 18 x 18, #1a2035 `text.ink` |

![Essential integration card default](components/crops/int-essential-default.png) ![Essential integration card hover](components/crops/int-essential-hover.png)

#### Integration card
A grid card linking to one integration page (Stripe / Paddle / Polar / Dodo); measured, never followed. Read as `int-card` on the integrations page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 324.66 x 236; padding 24px; radius 8px; background #ffffff `white`; shadow #f2f2f6 0px 0px 0px 1px; text Inter 18/30 400, #1a2035 `text.ink`; transition all 1.5s cubic-bezier(0.19, 1, 0.22, 1); icon 18 x 18, #1a2035 `text.ink` |

![Integration card default](components/crops/int-card-default.png) ![Integration card hover](components/crops/int-card-hover.png)

#### Group eyebrow
An all-caps group label (ESSENTIALS / PAYMENTS / PRODUCT AND ENGINEERING). Read as `int-eyebrow` on the integrations page.

**Values (default).** size 276.66 x 30; background transparent; text Inter 18/30 400, #1a2035 `text.ink`; transition all 1.5s cubic-bezier(0.19, 1, 0.22, 1).

![Group eyebrow default](components/crops/int-eyebrow-default.png)

### Alternative page

The /alternative/intercom comparison page: the Intercom-vs-Fernand data table and the FAQ accordion.

#### Alternative headline
The comparison page masthead ("The fast, calm Intercom alternative…"). Read as `alt-h1` on the comparison (alternative/intercom) page.

**Values (default).** size 1290 x 96; background transparent; text Inter 38/48 400, #1a2035 `text.ink`; transition all 1.5s cubic-bezier(0.19, 1, 0.22, 1).

![Alternative headline default](components/crops/alt-h1-default.png)

#### Comparison table
The "Intercom vs Fernand comparison" table — a real data table on the public site. Read as `alt-table` on the comparison (alternative/intercom) page.

**Values (default).** size 1290 x 756.22; background transparent; text Inter 12/18.6 600, #9aa3b8; layers th 186.0x47.6 B:1px solid rgb(238, 240, 246); th 547.4x47.6 B:1px solid rgb(238, 240, 246); th.alt-table__fernand 556.6x47.6 rgb(240, 248, 255) B:1px solid rgb(238, 240, 246) 8px 8px 0px 0px; td 186.0x50.7 B:1px solid rgb(240, 241, 246); td 547.4x50.7 B:1px solid rgb(240, 241, 246); td.alt-table__fernand 556.6x50.7 rgb(240, 248, 255) B:1px solid rgb(240, 241, 246).

Child layers that carry the look: th 186x47.6 border 1px solid #eef0f6; th 547.4x47.6 border 1px solid #eef0f6; th 556.6x47.6 background #f0f8ff border 1px solid #eef0f6 radius 8px 8px 0px 0px.

![Comparison table default](components/crops/alt-table-default.png)

#### FAQ accordion item
One item in the comparison FAQ accordion. Read as `alt-faq` on the comparison (alternative/intercom) page.

**Values (default).** size 584 x 54.25; border B: 1px solid #f0f1f6; background transparent; text Inter 15/17.25 500, #1a2035 `text.ink`; icon 14 x 14, #9aa3b8; layers div.alt-faq__item 584.0x54.3 B:1px solid rgb(240, 241, 246).

Child layers that carry the look: div 584x54.3 border 1px solid #f0f1f6.

![FAQ accordion item default](components/crops/alt-faq-default.png)

#### FAQ disclosure
A disclosure button in the comparison FAQ; the opened state was measured after clicking it (a local UI toggle). Read as `alt-faq-summary` on the comparison (alternative/intercom) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed, opened) | size 584 x 53.25; padding 18px 0px; background transparent; text Inter 15/17.25 500, #1a2035 `text.ink`; icon 14 x 14, #9aa3b8 |

![FAQ disclosure default](components/crops/alt-faq-summary-default.png) ![FAQ disclosure hover](components/crops/alt-faq-summary-hover.png) ![FAQ disclosure focus-visible](components/crops/alt-faq-summary-focus-visible.png) ![FAQ disclosure pressed](components/crops/alt-faq-summary-pressed.png) ![FAQ disclosure opened](components/crops/alt-faq-summary-opened.png)

### Feature page

The /feature/ai-agents product page: the permissions switches and replay control of the agent demo.

#### Permission switch
An on/off switch in the "Every key only does what you allow" permissions demo — a local UI toggle flipping the demo. Read as `ag-switch` on the ai-agents feature page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 18; radius 40px; background #16a34a; text Inter 13/14.95 400, #000000; transition background-color 0.2s ease |
| focus-visible | outline 2px solid #1a2035 `text.ink`, offset 2px |

![Permission switch default](components/crops/ag-switch-default.png) ![Permission switch hover](components/crops/ag-switch-hover.png) ![Permission switch focus-visible](components/crops/ag-switch-focus-visible.png) ![Permission switch pressed](components/crops/ag-switch-pressed.png)

#### Replay button
The "↻ Replay" control on the agent animation demo. Read as `ag-replay` on the ai-agents feature page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 81 x 26.94; padding 6px 12px; radius 6px; background #ffffff `white`; shadow rgba(18, 55, 105, 0.08) 0px 2px 4px 0px, rgba(18, 55, 105, 0.04) 0px 1px 1px 0px, rgba(18, 55, 105, 0.08) 0px 0px 0px 1px; text Inter 13/14.95 500, #6f7b96 `text.link`; transition color 0.15s ease, transform 0.16s ease-out |
| hover | text Inter 13/14.95 500, #58637d |
| pressed | size 78.57 x 26.13; text Inter 13/14.95 500, #58637d; transform scale(0.97) |

![Replay button default](components/crops/ag-replay-default.png) ![Replay button hover](components/crops/ag-replay-hover.png) ![Replay button focus-visible](components/crops/ag-replay-focus-visible.png) ![Replay button pressed](components/crops/ag-replay-pressed.png)

### App login

app.getfernand.com/auth/login — the signed-out Vue SPA sign-in card: e-mail and password fields, the primary 'Login' submit and the account links. Measured as a form, never submitted.

#### Login headline
"Welcome back" — the 25px sign-in heading. Read as `login-h1` on the app sign-in page.

**Values (default).** size 350 x 30; background transparent; text Inter 25/30 400, #131e40 `black`.

![Login headline default](components/crops/login-h1-default.png)

#### Login card
The sign-in card on app.getfernand.com/auth/login — e-mail and password fields, the primary submit and the account links. Read as `login-card` on the app sign-in page.

**Values (default).** size 350 x 216.25; background transparent; text Inter 15/17.25 400, #9fa3b5 `grey.strong`; icon 20 x 20, #0000ee; layers input 350.0x46.0 rgb(255, 255, 255) T:1px solid rgb(209, 213, 230) / R:1px solid rgb(209, 213, 230) / B:1px solid rgb(209, 213, 230) / L:1px solid rgb(209, 213, 230) 4px; input 350.0x46.0 rgb(255, 255, 255) T:1px solid rgb(209, 213, 230) / R:1px solid rgb(209, 213, 230) / B:1px solid rgb(209, 213, 230) / L:1px solid rgb(209, 213, 230) 4px; input.button.button--primary 350.0x46.0 rgb(0, 160, 255) T.

Child layers that carry the look: input 350x46 background #ffffff `white` border 1px solid #d1d5e6 radius 4px; input 350x46 background #ffffff `white` border 1px solid #d1d5e6 radius 4px; input 350x46 background #00a0ff `blue.default` border 2px solid #00a0ff `blue.default` radius 4px.

![Login card default](components/crops/login-card-default.png)

#### Email field (login)
The "Your work email" input; focused and typed into then cleared — never submitted. Read as `login-field` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 350 x 46; padding 0px 14px; border 1px solid #d1d5e6; radius 4px; background #ffffff `white`; text Inter 15/17.25 400, #131e40 `black`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); placeholder #9fa3b5 `grey.strong` |
| focused | border 1px solid #01a0ff; shadow rgba(16, 166, 255, 0.416) 0px 0px 4.97644px 0px |
| filled | border 1px solid #00a0ff `blue.default`; shadow rgba(16, 166, 255, 0.42) 0px 0px 5px 0px |

![Email field (login) default](components/crops/login-field-default.png) ![Email field (login) focused](components/crops/login-field-focused.png) ![Email field (login) filled](components/crops/login-field-filled.png)

#### Password field (login)
The "Your password" input; focused and typed into then cleared — never submitted. Read as `login-pass` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 350 x 46; padding 0px 14px; border 1px solid #d1d5e6; radius 4px; background #ffffff `white`; text Inter 15/17.25 400, #131e40 `black`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); placeholder #9fa3b5 `grey.strong` |
| focused | border 1px solid #03a1ff; shadow rgba(16, 166, 255, 0.416) 0px 0px 4.93091px 0px |
| filled | border 1px solid #00a0ff `blue.default`; shadow rgba(16, 166, 255, 0.42) 0px 0px 5px 0px |

![Password field (login) default](components/crops/login-pass-default.png) ![Password field (login) focused](components/crops/login-pass-focused.png) ![Password field (login) filled](components/crops/login-pass-filled.png)

#### Login submit
The primary "Login" submit; its states were measured but the button was never clicked — nothing was submitted. Read as `login-submit` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 350 x 46; padding 12px 18px; border 2px solid #00a0ff `blue.default`; radius 4px; background #00a0ff `blue.default`; text Inter 15/17.25 500, #ffffff `white`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); placeholder #ffffff `white` |
| hover | shadow rgba(231, 235, 243, 0.718) 0px 1.98512px 1.98512px 0px, rgba(54, 61, 84, 0.05) 0px 0px 14.8884px 0px |
| focus-visible | shadow rgba(17, 166, 255, 0.408) 0px 0.00339661px 4.85793px 0px, rgba(54, 61, 84, 0) 0px 0px 0.0254746px 0px |
| pressed | shadow rgba(231, 235, 243, 0.71) 0px 1.96646px 1.97135px 0px, rgba(54, 61, 84, 0.05) 0px 0px 14.7485px 0px |

![Login submit default](components/crops/login-submit-default.png) ![Login submit hover](components/crops/login-submit-hover.png) ![Login submit focus-visible](components/crops/login-submit-focus-visible.png) ![Login submit pressed](components/crops/login-submit-pressed.png)

#### Login link
The "Create an account" / "Lost password?" link beside the form; measured, never followed. Read as `login-link` on the app sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 127 x 19; background transparent; text Inter 15/17.25 400, #9fa3b5 `grey.strong`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| hover | text Inter 15/17.25 400, #01a0fe |
| focus-visible | outline 1px auto #131414, offset 0.96875px; layers a 127.0x19.0 1px auto rgb(19, 20, 20) offset 0.96875px |
| pressed | text Inter 15/17.25 400, #03a0fe |

![Login link default](components/crops/login-link-default.png) ![Login link hover](components/crops/login-link-hover.png) ![Login link focus-visible](components/crops/login-link-focus-visible.png) ![Login link pressed](components/crops/login-link-pressed.png)

### App signup

app.getfernand.com/create — the signed-out signup: the 'Bonjour, I'm Fernand' intro panel, work-email and product-name fields, the terms checkbox and the 'Continue' button. Measured as a form, never submitted.

#### Signup intro panel
The left intro panel of /create — "Bonjour, I'm Fernand. The better, faster and calmer helpdesk experience." Read as `create-panel` on the app signup page.

**Values (default).** size 720 x 900; background transparent; text Inter 16/18.4 400, #131e40 `black`; transition opacity 0.3s ease-in-out.

![Signup intro panel default](components/crops/create-panel-default.png)

#### Signup headline
The signup greeting heading. Read as `create-h1` on the app signup page.

**Values (default).** size 599 x 90; background transparent; text Inter 25/30 400, #636d83.

![Signup headline default](components/crops/create-h1-default.png)

#### Email field (signup)
The "Your work email" signup input; focused and typed into then cleared — never submitted. Read as `create-field` on the app signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 599 x 46; padding 0px 14px; border 1px solid #d1d5e6; radius 4px; background #ffffff `white`; text Inter 15/17.25 400, #131e40 `black`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); placeholder #9fa3b5 `grey.strong` |
| focused | border 1px solid #02a1ff; shadow rgba(16, 166, 255, 0.416) 0px 0px 4.94347px 0px |
| filled | border 1px solid #00a0ff `blue.default`; shadow rgba(16, 166, 255, 0.42) 0px 0px 5px 0px |

![Email field (signup) default](components/crops/create-field-default.png) ![Email field (signup) focused](components/crops/create-field-focused.png) ![Email field (signup) filled](components/crops/create-field-filled.png)

#### Product name field
The "Your product's name" input; focused and typed into then cleared — never submitted. Read as `create-field-name` on the app signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 599 x 46; padding 0px 14px; border 1px solid #d1d5e6; radius 4px; background #ffffff `white`; text Inter 15/17.25 400, #131e40 `black`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); placeholder #9fa3b5 `grey.strong` |
| focused | border 1px solid #02a1ff; shadow rgba(16, 166, 255, 0.416) 0px 0px 4.94347px 0px |
| filled | border 1px solid #00a0ff `blue.default`; shadow rgba(16, 166, 255, 0.42) 0px 1.20147e-08px 5px 0px, rgba(54, 61, 84, 0) 0px 0px 9.01104e-08px 0px |

![Product name field default](components/crops/create-field-name-default.png) ![Product name field focused](components/crops/create-field-name-focused.png) ![Product name field filled](components/crops/create-field-name-filled.png)

#### Terms checkbox
The terms-of-service checkbox (a styled .fake__checkbox over the native input); measured, never toggled. Read as `create-checkbox` on the app signup page.

**Values (default).** size 18 x 18; border 1px solid #d1d5e6; radius 5px; background #ffffff `white`; text Inter 15/17.25 400, #00a0ff `blue.default`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); placeholder #00a0ff `blue.default`.

![Terms checkbox default](components/crops/create-checkbox-default.png)

#### Terms text
The "Accept our terms of service" line; its link was never followed. Read as `create-tos` on the app signup page.

**Values (default).** size 599 x 18.19; background transparent; text Inter 14/16.1 400, #5e6271 `grey.medium`; layers input 18.0x18.0 rgb(255, 255, 255) T:1px solid rgb(209, 213, 230) / R:1px solid rgb(209, 213, 230) / B:1px solid rgb(209, 213, 230) / L:1px solid rgb(209, 213, 230) 5px.

Child layers that carry the look: input 18x18 background #ffffff `white` border 1px solid #d1d5e6 radius 5px.

![Terms text default](components/crops/create-tos-default.png)

#### Continue button
The primary "Continue" submit; its states were measured but the button was never clicked — nothing was submitted. Read as `create-continue` on the app signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 153 x 47; padding 12px 18px; border 2px solid #00a0ff `blue.default`; radius 4px; background #00a0ff `blue.default`; text Inter 15/17.25 500, #ffffff `white`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| focus-visible | outline 1px auto #121212, offset 0px |

![Continue button default](components/crops/create-continue-default.png) ![Continue button hover](components/crops/create-continue-hover.png) ![Continue button focus-visible](components/crops/create-continue-focus-visible.png) ![Continue button pressed](components/crops/create-continue-pressed.png)

### Help center

help.getfernand.com — the Nuxt docs site on the same palette: header nav, the search field and results popover, collection cards and article rows, and the 'Switch to dark mode' link.

#### Docs header
The docs site header: logo, the collection nav, the search and menu toggles and the dark-mode switch. Read as `help-header` on the docs home page.

**Values (default).** size 350 x 900; padding 22px; border R: 1px solid #eaecf8 `border.default`; background #f7fafc; text Inter 14/22.4 400, #00a0ff `blue.default`.

![Docs header default](components/crops/help-header-default.png)

#### Docs logo
The Fernand Docs wordmark. Read as `help-logo` on the docs home page.

**Values (default).** size 290 x 42; background transparent; text Inter 16/25.6 400, #131e40 `black`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1).

![Docs logo default](components/crops/help-logo-default.png)

#### Docs nav item
A collection link in the docs nav; measured, never followed. Read as `help-nav-item` on the docs home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 290 x 40.39; padding 8px 0px 8px 12px; border 1px solid transparent; radius 5px; background transparent; text Inter 14/22.4 400, #454c65; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); icon 20 x 20, #9fa3b5 `grey.default` |
| focus-visible | outline 1px auto #111111, offset 0.984375px |

![Docs nav item default](components/crops/help-nav-item-default.png) ![Docs nav item hover](components/crops/help-nav-item-hover.png) ![Docs nav item focus-visible](components/crops/help-nav-item-focus-visible.png) ![Docs nav item pressed](components/crops/help-nav-item-pressed.png)

#### Search field
The docs search field ("Start typing to search an article, collection…", ⌘K hint); focused and typed into — a local filter, nothing sent. Read as `help-search` on the docs home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 480 x 42; padding 1px 2px 1px 40px; border 1px solid #eaecf8 `border.default`; radius 5px; background #ffffff `white`; shadow rgba(26, 28, 33, 0.03) 0px 2px 3px 0px; text Inter 14/16.1 400, #131e40 `black`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); placeholder #5f667d |
| focused | border 1px solid #01a0ff |

![Search field default](components/crops/help-search-default.png) ![Search field focused](components/crops/help-search-focused.png)

#### Search popover
The results popover the docs search opens while typing. Read as `help-search-pop` on the docs home page.

**Values (default).** size 480 x 350; padding 10px 20px; radius 5px; background #ffffff `white`; shadow rgba(83, 87, 101, 0.17) 0px 1px 4px 0px, rgba(54, 61, 84, 0.15) 0px 9px 50px 0px; text Inter 14/22.4 400, #9fa3b5 `grey.default`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1).

![Search popover default](components/crops/help-search-pop-default.png)

#### Dark-mode switch
The docs site's own "Switch to dark mode" link — the real user-facing toggle that sets body.dark-mode; its states were measured but it was only toggled on the helpdark pass. Read as `help-dark-toggle` on the docs home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 30 x 30; radius 20px; background transparent; text Inter 16/25.6 400, #5f667d; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); icon 18 x 24, #9fa3b5 `grey.default` |
| hover | text Inter 16/25.6 400, #01a0fe |
| focus-visible | outline 1px auto #121212, offset 0.96875px; layers a.switch__dark 30.0x30.0 1px auto rgb(18, 18, 18) offset 0.96875px 20px |
| pressed | text Inter 16/25.6 400, #029ffd |

![Dark-mode switch default](components/crops/help-dark-toggle-default.png) ![Dark-mode switch hover](components/crops/help-dark-toggle-hover.png) ![Dark-mode switch focus-visible](components/crops/help-dark-toggle-focus-visible.png) ![Dark-mode switch pressed](components/crops/help-dark-toggle-pressed.png)

#### Collection card
A collection card on the docs home (emoji glyph, title, article count, description); measured, never followed. Read as `help-card` on the docs home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 310 x 146.78; padding 22px; border 1px solid #eaecf8 `border.default`; radius 5px; background transparent; text Inter 16/25.6 400, #9fa3b5 `grey.default`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| hover | border 1px solid #d1d5e6 |

![Collection card default](components/crops/help-card-default.png) ![Collection card hover](components/crops/help-card-hover.png)

#### Article row
An article row inside a collection (title + standfirst); measured, never followed. Read as `help-article-item` on the docs home page.

Not on the page when it was captured.

#### Go-to-Fernand link
The "→ Go to Fernand" link in the sticky search bar; measured, never followed. Read as `help-goto` on the docs home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 114 x 17; background transparent; text Inter 14/22.4 400, #131e40 `black`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| hover | text Inter 14/22.4 400, #009ffe |
| focus-visible | outline 1px auto #101011, offset 0.984375px; layers a.u--fs14 114.0x17.0 1px auto rgb(16, 16, 17) offset 0.984375px |
| pressed | text Inter 14/22.4 400, #009efc |

![Go-to-Fernand link default](components/crops/help-goto-default.png) ![Go-to-Fernand link hover](components/crops/help-goto-hover.png) ![Go-to-Fernand link focus-visible](components/crops/help-goto-focus-visible.png) ![Go-to-Fernand link pressed](components/crops/help-goto-pressed.png)

#### Article headline
The article title on a docs page ("Getting started"). Read as `help-h1` on the docs article page.

**Values (default).** size 962 x 50; background transparent; text Inter 42/50 500, #131e40 `black`.

![Article headline default](components/crops/help-h1-default.png)

#### Article body
A body paragraph in a docs article. Read as `help-prose` on the docs article page.

**Values (default).** size 962 x 25.59; background transparent; text Inter 16/25.6 400, #131e40 `black`.

![Article body default](components/crops/help-prose-default.png)

#### Article link
An in-content link inside a docs article; measured, never followed. Read as `help-content-link` on the docs article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 58 x 17; background transparent; text Inter 14/22.4 400, #131e40 `black`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| hover | text Inter 14/22.4 400, #009ffd |
| focus-visible | outline 1px auto #101011, offset 0.96875px; layers a.u--fs14 58.0x17.0 1px auto rgb(16, 16, 17) offset 0.96875px |
| pressed | text Inter 14/22.4 400, #009efc |

![Article link default](components/crops/help-content-link-default.png) ![Article link hover](components/crops/help-content-link-hover.png) ![Article link focus-visible](components/crops/help-content-link-focus-visible.png) ![Article link pressed](components/crops/help-content-link-pressed.png)

### Help center (dark)

The same docs site under body.dark-mode, painted by its own 'Switch to dark mode' link — the real user-facing toggle, not a reconstruction.

#### Docs page (dark)
The docs article surface under body.dark-mode — reached through the site's own "Switch to dark mode" link, not a reconstruction. Read as `hd-page` on the docs article page.

**Values (default).** size 1090 x 1506.81; background transparent; text Inter 12/23 400, #8a8f98 `grey.medium`; icon 20 x 20, #a1a1aa `text.muted`; layers div::after.wrapper.wrapper__pageheader 1090pxx120px; input.transit 480.0x42.0 rgb(22, 22, 24) T:1px solid rgba(255, 255, 255, 0.1) / R:1px solid rgba(255, 255, 255, 0.1) / B:1px solid rgba(255, 255, 255, 0.1) / L:1px solid rgba(255, 255, 255, 0.1) rgba(26, 28, 33, 0.03) 0px 2px 3px 0px 5px; kbd.transit.m--hide 30.0x28.0 rgb(24, 24, 27) T:1px solid rgba(255, 255, 255, 0.1) / R:1px solid rgba(255, 2.

Child layers that carry the look: div::after 1090pxx120px image linear-gradient(#161618 `white`, #161618 `white` 60%, rgba(18, 18, 18, 0)); input 480x42 background #161618 `white` border 1px solid rgba(255, 255, 255, 0.1) `border.default` radius 5px shadow rgba(26, 28, 33, 0.03) 0px 2px 3px 0px; kbd 30x28 background #18181b `grey.light` border 1px solid rgba(255, 255, 255, 0.1) `border.default` radius 4px.

![Docs page (dark) default](components/crops/hd-page-default.png)

#### Article headline (dark)
The article title under dark-mode. Read as `hd-h1` on the docs article page.

**Values (default).** size 962 x 50; background transparent; text Inter 42/50 500, #ffffff `text.ink`.

![Article headline (dark) default](components/crops/hd-h1-default.png)

#### Docs nav item (dark)
A collection link in the docs nav under dark-mode. Read as `hd-nav-item` on the docs article page.

**Values (default).** size 290 x 40.39; padding 8px 0px 8px 12px; border 1px solid #232326 `surface.raised`; radius 5px; background #232326 `surface.raised`; text Inter 14/22.4 400, #00a0ff `blue.default`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); icon 20 x 20, #f7f8f8 `black`.

![Docs nav item (dark) default](components/crops/hd-nav-item-default.png)

#### Search field (dark)
The docs search field under dark-mode. Read as `hd-search` on the docs article page.

**Values (default).** size 480 x 42; padding 1px 2px 1px 40px; border 1px solid rgba(255, 255, 255, 0.1) `border.default`; radius 5px; background #161618 `white`; shadow rgba(26, 28, 33, 0.03) 0px 2px 3px 0px; text Inter 14/16.1 400, #f7f8f8 `black`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); placeholder #8a8f98 `grey.medium`.

![Search field (dark) default](components/crops/hd-search-default.png)

#### Collection card (dark)
A collection card under dark-mode. Read as `hd-card` on the docs article page.

**Values (default).** size 310 x 184.77; padding 22px; border 1px solid rgba(255, 255, 255, 0.1) `border.default`; radius 5px; background transparent; text Inter 16/25.6 400, #e6e9eb `grey.default`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1).

![Collection card (dark) default](components/crops/hd-card-default.png)

#### Article body (dark)
A body paragraph in a docs article under dark-mode. Read as `hd-prose` on the docs article page.

**Values (default).** size 962 x 25.59; background transparent; text Inter 16/25.6 400, #a1a1aa `text.muted`.

![Article body (dark) default](components/crops/hd-prose-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the header, the masthead and the hero CTA.

#### Mobile top bar
The phone header: Fernand mark, nav links and "Start for free" (Book a demo hides at this width). Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 390 x 71.5; padding 12px 0px; background transparent; shadow rgba(25, 30, 90, 0) 0px -1px 0px 0px inset; text Inter 14/14 500, #6f7b96 `text.link`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); icon 35 x 45.5, #0000ee; layers header.transit.transit--slow 390.0x71.5 rgba(25, 30, 90, 0) 0px -1px 0px 0px inset; a 0.0x0.0 rgb(255, 255, 255) rgba(18, 55, 105, 0.08) 0px 2px 4px 0px, rgba(18, 55, 105, 0.04) 0px 1px 1px 0px, rgba(18, 55, 105, 0.08) 0px 0px 0px 1px 6px; a 115.0x30.0 rgb(0, 160, 255) 6px.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile header CTA
The header "Start for free" button at 390 wide; measured never followed. Read as `m-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 115 x 30; padding 8px 12px; radius 6px; background #00a0ff `blue.default`; text Inter 14/14 500, #ffffff `white`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| focus-visible | outline 1px auto #e69a06, offset 0.96875px |

![Mobile header CTA default](components/crops/m-cta-default.png) ![Mobile header CTA hover](components/crops/m-cta-hover.png) ![Mobile header CTA focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile header CTA pressed](components/crops/m-cta-pressed.png)

#### Mobile hero headline
The masthead at 390 wide — the 38px display heading drops to 26px. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 350 x 66; background transparent; text Inter 26/33 400, #1a2035 `text.ink`; transition all 1.5s cubic-bezier(0.19, 1, 0.22, 1).

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The hero "Start for free" button at 390 wide; measured never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 169 x 49; padding 13px 12px; border 1px solid #1a2035 `text.ink`; radius 8px; background #1a2035 `text.ink`; text Inter 15/20 500, #ffffff `white`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| focus-visible | outline 1px auto #e69905, offset 0.96875px |

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

### Footer

The marketing footer: the 'Start free. Email included.' closing CTA, sitemap columns, legal links and social icons.

#### Footer CTA
The "Start free. Email included." call-to-action button in the closing section; measured, never followed. Read as `footer-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 170 x 49; padding 13px 20px; border 1px solid #1a2035 `text.ink`; radius 8px; background #1a2035 `text.ink`; text Inter 15/20 500, #ffffff `white`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| focus-visible | outline 1px auto #171717, offset 0.96875px |

![Footer CTA default](components/crops/footer-cta-default.png) ![Footer CTA hover](components/crops/footer-cta-hover.png) ![Footer CTA focus-visible](components/crops/footer-cta-focus-visible.png) ![Footer CTA pressed](components/crops/footer-cta-pressed.png)

#### Footer
The page footer: sitemap columns, legal links, status/social links. Read as `footer` on the home page.

**Values (default).** size 1440 x 417; background #151618; text Inter 15/15 400, #ffffff `white`; layers ::before rgb(21, 22, 24) 0px none 1.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 194 x 25; padding 5px 0px; background transparent; text Inter 15/15 400, rgba(255, 255, 255, 0.5); transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1) |
| hover | text Inter 15/15 400, rgba(255, 255, 255, 0.996) |
| focus-visible | outline 1px auto rgba(19, 19, 19, 0.99), offset 0.96875px; layers a 194.0x25.0 1px auto rgba(19, 19, 19, 0.99) offset 0.96875px |
| pressed | text Inter 15/15 400, rgba(255, 255, 255, 0.992) |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Fernand widget

The product's own embeddable chat widget on the marketing site — the 48px launcher bubble and the panel it opens; opened once, never typed into.

#### Widget launcher
The Fernand chat-widget launcher on the marketing site — the product's own embeddable widget at rest (48px bubble). Read as `launcher` on the home page.

**Values (default).** size 48 x 48; radius 100%; background transparent; shadow rgba(0, 0, 0, 0.1) 0px 5px 18px -5px, rgba(0, 0, 0, 0.1) 0px 8px 8px -6px; text Inter 16/16 400, #131e40 `black`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1); icon 24 x 24, #5f667d; layers div.fernand__launcher.transit 48.0x48.0 rgba(0, 0, 0, 0.1) 0px 5px 18px -5px, rgba(0, 0, 0, 0.1) 0px 8px 8px -6px 100%; div.fernand__launcher__icon 48.0x48.0 rgb(255, 255, 255) 100%.

![Widget launcher default](components/crops/launcher-default.png)

#### Widget panel
The chat-widget panel opened by its own launcher click — the product's public widget UI; never typed into. Read as `launcher-panel` on the home page.

**Values (default).** size 400 x 900; background transparent; image radial-gradient(at right bottom, rgba(29, 39, 54, 0.1) 0px, rgba(29, 39, 54, 0) 70%); text Inter 16/16 400, #131e40 `black`; transition all 0.75s cubic-bezier(0.19, 1, 0.22, 1).

![Widget panel default](components/crops/launcher-panel-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Fernand wordmark, the channel and feature glyphs, the widget launcher mark, the emoji glyphs on the docs collection cards) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Fernand's product is the support workspace: every post-login surface — the inbox, conversation views, settings, API keys, the team/AI-agent configuration — needs an account and was never reached. app.getfernand.com/auth/login and /create are the only app surfaces a signed-out visitor sees, and they were measured as forms, never submitted. The product mocks inside the marketing cards and the widget playground are illustrations, not the product.

### Pages

- **The account.** Every post-login surface was never reached; the sign-in and signup forms were measured and typed into then cleared — 'Login'/'Continue' were never pressed, the terms checkbox was never toggled, and what a submitted form returns is unverified.
- **Book a demo.** The 'Book a demo' action is a Cal.com scheduling link; opening it starts a real booking flow, so it was measured at rest and never activated.
- **Alternative pages** beyond /alternative/intercom, the rest of the feature pages, and the other integrations are the same templates, unmeasured; one example of each family was captured.
- **/updates/ is a ~44k-px changelog** — captured in full, stitched from 4 contiguous parts (the part clips are recorded in the `.capture.json` sidecar).
- **blog articles** — the /blog index was captured; individual posts are the same template, unmeasured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **The widget panel's inner states** (an open conversation, the chat input) were not reached — the panel was opened and shot, never typed into.

### Themes

The marketing site and the signed-out app paint light only — no toggle, no `prefers-color-scheme` switch was observed on them (`color-scheme: light` on :root). The docs site ships a real 'Switch to dark mode' link that sets body.dark-mode and persists it in localStorage; the dark set and the Help-center-(dark) measurements are that genuinely-toggled surface. The SPA's stylesheet also declares a body.dark-mode remap — captured in raw/css-vars.json — but nothing signed out paints it.

### Fonts

- **Inter** (self-hosted woff2, weights 300–700 plus italics on the marketing site) is the served face on all three hosts. The style guide falls back to system sans.

### Screenshots

- The product mocks, screenshots-in-screenshots and logo walls are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article copy, testimonial names and the changelog text are the product's content; only frames and components were measured.
