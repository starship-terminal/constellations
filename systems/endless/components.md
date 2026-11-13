# Endless components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from endless.app (what endless.io redirects to) on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. endless.app is one Next.js surface — marketing pages, ~70 free tools, the model catalog, social radar, /docs and /brand — over a single shadcn-style token layer (TikTok Sans + Geist Mono). Nothing was signed into, sent, generated, downloaded or submitted; the contact form and every tool's prompt field were never filled past a deleted sample; sign-in (clerk.endless.app) and sign-up (s.endless.app) were never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (74 components, 178 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (177 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: the site paints `light` on a light system and `dark` on a dark one (the `-dark` shots emulate prefers-color-scheme, the same trigger next-themes honours). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [composer](screenshots/home-dark-composer.png), [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [composer](screenshots/home-light-composer.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Pricing | `/pricing` | [annual](screenshots/pricing-dark-annual.png), [default](screenshots/pricing-dark-default.png), [full](screenshots/pricing-dark-full.png), [annual](screenshots/pricing-light-annual.png), [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Contact | `/contact` | [default](screenshots/contact-dark-default.png), [field](screenshots/contact-dark-field.png), [full](screenshots/contact-dark-full.png), [default](screenshots/contact-light-default.png), [field](screenshots/contact-light-field.png), [full](screenshots/contact-light-full.png) |
| Tools index | `/tools` | [default](screenshots/tools-light-default.png), [full](screenshots/tools-light-full.png) |
| AI image generator (a free tool) | `/tools/ai-image-generator` | [default](screenshots/toolgen-dark-default.png), [full](screenshots/toolgen-dark-full.png), [prompt](screenshots/toolgen-dark-prompt.png), [default](screenshots/toolgen-light-default.png), [full](screenshots/toolgen-light-full.png), [prompt](screenshots/toolgen-light-prompt.png) |
| Model catalog | `/models` | [default](screenshots/models-dark-default.png), [full](screenshots/models-dark-full.png), [default](screenshots/models-light-default.png), [full](screenshots/models-light-full.png) |
| Model index (pricing table) | `/model-index` | [default](screenshots/model-index-light-default.png), [full](screenshots/model-index-light-full.png) |
| Blog index | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Brand kit | `/brand` | [default](screenshots/brand-light-default.png), [full](screenshots/brand-light-full.png) |
| Documentation shell | `/docs` | [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png) |
| Social radar | `/radar` | [default](screenshots/radar-dark-default.png), [full](screenshots/radar-dark-full.png), [default](screenshots/radar-light-default.png), [full](screenshots/radar-light-full.png) |
| MCP server | `/mcp` | [default](screenshots/mcp-light-default.png), [full](screenshots/mcp-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Industries | `/industries` | [default](screenshots/industries-light-default.png), [full](screenshots/industries-light-full.png) |
| Compare | `/compare` | [default](screenshots/compare-light-default.png), [full](screenshots/compare-light-full.png) |
| Status | `/status` | [default](screenshots/status-light-default.png), [full](screenshots/status-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| AI image generator, phone | `/tools/ai-image-generator` | [default](screenshots/mobile-toolgen-light-default.png), [full](screenshots/mobile-toolgen-light-full.png) |
| Models, phone | `/models` | [default](screenshots/mobile-models-light-default.png), [full](screenshots/mobile-models-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the hamburger button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |
| Desktop header menu | every marketing page | not present: the desktop header is flat nav links, the Menu button only paints at phone width | [nav-dropdown](#nav-dropdown) recorded missing |
| Composer focus | home | clicking into the Ask-Endless textarea (nothing typed or sent) | [home-light-composer](screenshots/home-light-composer.png), [composer-input](#composer-input) |
| Billing segment | /pricing | the Monthly/Annual toggle's own press | [pricing-light-annual](screenshots/pricing-light-annual.png), [billing-toggle](#billing-toggle) |
| Field focus | /contact, free tools | clicking into a field; sample text typed and deleted, nothing sent | [contact-light-field](screenshots/contact-light-field.png), [toolgen-light-prompt](screenshots/toolgen-light-prompt.png) |
| Consent/chat overlays | every page | hidden, never answered (no consent button was ever clicked, no consent POST sent) | hidden before every shot and reading |
| Signed-in workspace | s.endless.app; auth on clerk.endless.app | the product's chat workspace lives behind sign-in | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 30 components were given a real keyboard focus. 7 draw an outline ring: `logo` (2px solid lab(70.8735 -22.234 -45.4927), offset 2px), `faq-item` (2px solid lab(70.8735 -22.234 -45.4927), offset 2px), `model-card` (2px solid lab(70.8735 -22.234 -45.4927), offset 2px), `blog-card` (on a child: 1px solid lab(0 0 0 / 0.1) offset -1px), `docs-nav-item` (1px auto oklab(0.747992 -0.0921395 -0.125864 / 0.5), offset 0px), `docs-search` (1px auto oklab(0.747992 -0.0921395 -0.125864 / 0.5), offset 0px), `footer-link` (2px solid lab(70.8735 -22.234 -45.4927), offset 2px). 21 draw a focus ring as a shadow instead: `nav-industries`, `nav-signin`, `nav-cta`, `composer-send`, `mode-pill`, `prompt-chip`, `billing-toggle`, `plan-cta`, `send-btn`, `tool-generate`, `mode-tab`, `model-link`, `radar-row`, `radar-copy`, `radar-why`, `brand-btn`, `blog-pill`, `mcp-copy`, `theme-toggle`, `cookie-btn`, `d-nav-cta`. The other 2 show no measured change: `nav-link`, `d-nav-link`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, backdrop-filter, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | billing-toggle, blog-pill, brand-btn, composer-send, d-nav-cta, field-company, field-email, field-name and more |
| 0.15s | `cubic-bezier(0.22, 1, 0.36, 1)` | background-color, border-bottom-color | d-header, header, m-header |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, backdrop-filter, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | blog-card, brand-swatch, cookie-btn, d-nav-link, docs-nav-item, docs-search, faq-item, field-message and more |
| 0.25s | `ease` | all | docs-sidebar |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Prompt composer](#prompt-composer) | 660 x 122 | - | 20px | lab(100 0 0) | lab(0 0 0 / 0.06) 0px 0px 0px 1px, lab(0 0 0 / 0.06) 0px 1px 2px -1px, lab(0 0 0 / 0.04) 0px 2px 4px 0px | 0 |
| [Plan card](#plan-card) | 273 x 612 | - | 16px | lab(100 0 0) | oklab(0.921998 -0.00000908971 0.0000215769 / 0.6) 0px 0px 0px 1px | 24px |
| [Contact form](#contact-form) | 640 x 436 | - | - | transparent | none | 0 |
| [Tool panel](#tool-panel) | 504 x 114 | - | 20px | lab(100 0 0) | lab(0 0 0 / 0.06) 0px 0px 0px 1px, lab(0 0 0 / 0.06) 0px 1px 2px -1px, lab(0 0 0 / 0.04) 0px 2px 4px 0px | 0 |
| [Model card](#model-card) | 354.66 x 200 | - | 20px | transparent | lab(90.952 0 -0.0000119209) 0px 0px 0px 1px | 24px |
| [Post card](#post-card) | 269.33 x 347.88 | 1px solid oklab(0.921998 -0.00000908971 0.0000215769 / 0.6) | 16px | lab(100 0 0) | none | 0 |
| [Logo block](#logo-block) | 436 x 208 | - | 20px | lab(100 0 0) | lab(90.952 0 -0.0000119209) 0px 0px 0px 1px inset | 0 |
| [Docs sidebar](#docs-sidebar) | 268 x 900 | R: 1px solid lab(90.952 0 -0.0000119209) | - | lab(98.956 0.0000298023 -0.0000119209) | none | 0 |
| [Code block](#code-block) | 470.94 x 20 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The marketing chrome: the logo mark, flat nav links, Sign in and the dark Sign-up-for-free pill on the near-white field. The desktop header has no dropdown menu; the nav is plain links at every width it was captured.

#### Header
The sticky 56px marketing header: logo mark, flat nav links, Sign in and the Sign-up-for-free pill. Read as `header` on the home page.

**Values (default).** size 1440 x 56; border B: 1px solid transparent; background oklch(0.990998 0.0000251858 none / 0.9); text TikTok Sans 14/20 500, lab(2.75381 0 0); transition background-color 0.15s cubic-bezier(0.22, 1, 0.36, 1), border-bottom-color 0.15s cubic-bezier(0.22, 1, 0.36, 1); icon 24 x 24, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Logo
The Endless mark anchor. Read as `logo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 109.39 x 32; padding 0px 8px 0px 4px; radius 8px; background transparent; text TikTok Sans 16/24 400, lab(2.75381 0 0); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, lab(2.75381 0 0); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 2px solid lab(70.8735 -22.234 -45.4927), offset 2px; layers ::after rgba(0, 0, 0, 0) 0px none 1; a.relative.flex 109.4x32.0 2px solid lab(70.8735 -22.234 -45.4927) offset 2px 8px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Nav link — Industries
The Industries header link (a plain link, not a dropdown trigger). Read as `nav-industries` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101.77 x 32; padding 6px 10px; radius 8px; background transparent; text TikTok Sans 14/20 400, lab(46.408 0 -0.0000119209); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, lab(46.408 0 -0.0000119209); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | background lab(96.52 -0.0000298023 0.0000119209); text TikTok Sans 14/20 400, lab(2.75381 0 0); icon 12 x 12, lab(2.75381 0 0) |
| focus-visible | shadow lab(70.8735 -22.234 -45.4927) 0px 0px 0px 2px; layers ::after rgba(0, 0, 0, 0) 0px none 1; a.group/navigation-menu-trigger.w-max 101.8x32.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, lab(70.8735 -22.234 -45.4927) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 8px |
| pressed | background lab(96.52 -0.0000298023 0.0000119209); text TikTok Sans 14/20 400, lab(2.75381 0 0); icon 12 x 12, lab(2.75381 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Nav link
The plain Pricing header link. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 65.91 x 32; padding 6px 10px; radius 8px; background transparent; text TikTok Sans 14/20 400, lab(46.408 0 -0.0000119209); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | background lab(96.52 -0.0000298023 0.0000119209); text TikTok Sans 14/20 400, lab(2.75381 0 0) |
| focus-visible | background lab(96.52 -0.0000298023 0.0000119209) |
| pressed | background lab(96.52 -0.0000298023 0.0000119209); text TikTok Sans 14/20 400, lab(2.75381 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Sign-in button
The Sign-in control (goes to clerk.endless.app; measured, never followed). Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 80.06 x 32; padding 0px 16px; border 1px solid transparent; radius 8px; background transparent; text TikTok Sans 14/20 600, lab(46.408 0 -0.0000119209); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | text TikTok Sans 14/20 600, lab(2.75381 0 0) |
| focus-visible | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 76.86 x 30.72; text TikTok Sans 14/20 600, lab(2.75381 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Sign-up CTA
The dark Sign-up-for-free pill (goes to s.endless.app; measured, never followed). Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 138.86 x 32; padding 0px 16px; border 1px solid transparent; radius 8px; background lab(2.75381 0 0); text TikTok Sans 14/20 600, lab(98.956 0.0000298023 -0.0000119209); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | background oklab(0.145 -0.00000143796 0.00000340492 / 0.9) |
| focus-visible | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 133.3 x 30.72; background oklab(0.145 -0.00000143796 0.00000340492 / 0.9) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Nav dropdown
No dropdown exists on the desktop header — recorded missing. Read as `nav-dropdown` on the home page.

Not on the page when it was captured.

#### Menu link
No dropdown menu on the desktop header — recorded missing. Read as `menu-link` on the home page.

Not on the page when it was captured.

### Home hero

The home hero: the display headline and the Ask-Endless prompt composer with its model pill, send control and prompt chips. Nothing was ever sent.

#### Hero headline
The home display headline. Read as `hero-title` on the home page.

**Values (default).** size 504.11 x 127.88; background transparent; text TikTok Sans 59.2/63.93 500, lab(2.75381 0 0); icon 52.75 x 52.75, lab(2.75381 0 0); layers div.home-sticker-frame.bg-surface-control 61.5x61.5 lab(96.52 -0.0000298023 0.0000119209) lab(0 0 0 / 0.05) 0px 1px 2px 0px, lab(0 0 0 / 0.15) 0px 8px 24px -12px calc(22.5% + 2.2px); span.relative.flex 52.8x52.8 lab(0 0 0 / 0.06) 0px 0px 0px 1px, lab(0 0 0 / 0.06) 0px 1px 2px -1px, lab(0 0 0 / 0.04) 0px 2px 4px 0px 22.5%; span::after.relative.flex 48pxx48px rgba(0, 0, 0, 0.14) 0px 0px 0px 0.5px in.

Child layers that carry the look: div 61.5x61.5 background lab(96.52 -0.0000298023 0.0000119209) radius calc(22.5% + 2.2px) shadow lab(0 0 0 / 0.05) 0px 1px 2px 0px, lab(0 0 0 / 0.15) 0px 8px 24px -12px; span 52.8x52.8 radius 22.5% shadow lab(0 0 0 / 0.06) 0px 0px 0px 1px, lab(0 0 0 / 0.06) 0px 1px 2px -1px, lab(0 0 0 / 0.04) 0px 2px 4px 0px; span::after 48pxx48px radius 22.5% shadow rgba(0, 0, 0, 0.14) 0px 0px 0px 0.5px inset, rgba(255, 255, 255, 0.62) 0px 0.75px 0px 0px inset.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Hero copy
The lede under the headline. Read as `hero-lede` on the home page.

**Values (default).** size 512 x 58.5; background transparent; text TikTok Sans 18/29.25 400, oklab(0.145 -0.00000143796 0.00000340492 / 0.75).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Prompt composer
The painted Ask-Endless prompt box (the hero's chat composer). Its send control is never pressed. Read as `composer` on the home page.

**Values (default).** size 660 x 122; radius 20px; background lab(100 0 0); shadow lab(0 0 0 / 0.06) 0px 0px 0px 1px, lab(0 0 0 / 0.06) 0px 1px 2px -1px, lab(0 0 0 / 0.04) 0px 2px 4px 0px; text TikTok Sans 14/20 500, lab(46.408 0 -0.0000119209); icon 16 x 16, lab(46.408 0 -0.0000119209).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Composer input
The "Ask Endless…" textarea; sample text was typed and deleted, nothing sent. Read as `composer-input` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 660 x 72; padding 16px 20px 4px 20px; background transparent; text TikTok Sans 16/24 400, lab(2.75381 0 0); placeholder lab(46.408 0 -0.0000119209) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Composer send
The send/generate control inside the composer; measured, never pressed. Read as `composer-send` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; border 1px solid transparent; radius 12px; background transparent; text TikTok Sans 14/20 500, lab(46.408 0 -0.0000119209); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, lab(46.408 0 -0.0000119209) |
| hover | background lab(96.52 -0.0000298023 0.0000119209); text TikTok Sans 14/20 500, lab(2.75381 0 0); icon 16 x 16, lab(2.75381 0 0) |
| focus-visible | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | background lab(96.52 -0.0000298023 0.0000119209); text TikTok Sans 14/20 500, lab(2.75381 0 0); icon 16 x 16, lab(2.75381 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Model pill
The model-picker pill on the composer ("GPT-6.1 Terra" on this pass). Read as `mode-pill` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 145.59 x 36; padding 0px 8px 0px 12px; border 1px solid transparent; radius 8px; background transparent; text TikTok Sans 14/20 500, lab(46.408 0 -0.0000119209); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, lab(46.408 0 -0.0000119209); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | background lab(96.52 -0.0000298023 0.0000119209); text TikTok Sans 14/20 500, lab(2.75381 0 0); icon 16 x 16, lab(2.75381 0 0) |
| focus-visible | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | background lab(96.52 -0.0000298023 0.0000119209); text TikTok Sans 14/20 500, lab(2.75381 0 0); icon 16 x 16, lab(2.75381 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Prompt chip
A suggestion chip under the composer; measured, never pressed. Read as `prompt-chip` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 156.05 x 36; padding 0px 10px; border 1px solid lab(90.952 0 -0.0000119209); radius 12px; background lab(100 0 0); text TikTok Sans 14/20 500, lab(2.75381 0 0); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, lab(46.408 0 -0.0000119209) |
| hover | background lab(96.52 -0.0000298023 0.0000119209) |
| focus-visible | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 149.8 x 34.56; background lab(96.52 -0.0000298023 0.0000119209); icon 15.36 x 15.36, lab(46.408 0 -0.0000119209) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Pricing

The pricing surface: the Monthly/Annual billing segment, the shared-credits slider, the plan cards with their CTAs and the FAQ rows.

#### Pricing title
The pricing page heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 672 x 120; background transparent; text TikTok Sans 48/60 500, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Billing toggle
The Monthly/Annual billing segment; Annual was toggled for the screenshot state, never checked out. Read as `billing-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 96 x 32; radius 3.35544e+07px; background transparent; text TikTok Sans 14/20 500, lab(2.75381 0 0); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | shadow lab(98.956 0.0000298023 -0.0000119209) 0px 0px 0px 2px, lab(70.8735 -22.234 -45.4927) 0px 0px 0px 4px; layers ::after rgba(0, 0, 0, 0) 0px none 1; button.relative.after:absolute 96.0x32.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, lab(98.956 0.0000298023 -0.0000119209) 0px 0px 0px 2px, lab(70.8735 -22.234 -45.4927) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 3.35544e+07px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Plan name
A plan card's name. Read as `plan-name` on the pricing page.

**Values (default).** size 225 x 28; background transparent; text TikTok Sans 18/28 600, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Plan price
A plan card's price figure. Read as `plan-price` on the pricing page.

**Values (default).** size 225 x 66; background transparent; text TikTok Sans 36/40 600, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Plan CTA
A plan card's action; measured never followed (sign-up goes to s.endless.app). Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 225 x 52; padding 12px 28px; border 1px solid transparent; radius 12px; background lab(98.956 0.0000298023 -0.0000119209); shadow lab(0 0 0 / 0.06) 0px 0px 0px 1px, lab(0 0 0 / 0.06) 0px 1px 2px -1px, lab(0 0 0 / 0.04) 0px 2px 4px 0px; text TikTok Sans 16/26 600, lab(2.75381 0 0); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) |
| hover | background lab(96.52 -0.0000298023 0.0000119209) |
| focus-visible | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 216 x 49.92; background lab(96.52 -0.0000298023 0.0000119209) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Plan card
A pricing plan card (the painted ancestor of the plan name). Read as `plan-card` on the pricing page.

**Values (default).** size 273 x 612; padding 24px; radius 16px; background lab(100 0 0); shadow oklab(0.921998 -0.00000908971 0.0000215769 / 0.6) 0px 0px 0px 1px; text TikTok Sans 18/28 600, lab(2.75381 0 0); icon 16 x 16, lab(46.408 0 -0.0000119209).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Credits slider
The shared-credits range input on /pricing; focused only, never dragged. Read as `credits-slider` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 18 x 18; background transparent; text TikTok Sans 16/24 400, lab(2.75381 0 0); placeholder lab(2.75381 0 0) |
| focused | outline 1px auto oklab(0.747992 -0.0921395 -0.125864 / 0.5), offset 0px; layers input 18.0x18.0 1px auto oklab(0.747992 -0.0921395 -0.125864 / 0.5) offset 0px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### FAQ row
A pricing FAQ accordion row; measured closed, never opened. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1152 x 64; padding 20px 0px; radius 8px; background transparent; text TikTok Sans 16/24 500, lab(2.75381 0 0); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(46.408 0 -0.0000119209) |
| focus-visible | outline 2px solid lab(70.8735 -22.234 -45.4927), offset 2px; layers summary.flex.w-full 1152.0x64.0 2px solid lab(70.8735 -22.234 -45.4927) offset 2px 8px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Contact form

The contact/sales form, measured but never submitted: text, email and company inputs, the message textarea and the Send-message button.

#### Contact form
The contact/sales form (an unpainted 640px column; the fields paint their own fills); never submitted. Read as `contact-form` on the contact page.

**Values (default).** size 640 x 436; background transparent; text TikTok Sans 14/20 500, lab(2.75381 0 0); layers input.w-full.min-w-0 640.0x40.0 oklab(0.921998 -0.00000908971 0.0000215769 / 0.5) T:1px rgba(0, 0, 0, 0) / R:1px rgba(0, 0, 0, 0) / B:1px rgba(0, 0, 0, 0) / L:1px rgba(0, 0, 0, 0) 8px; input.w-full.min-w-0 640.0x40.0 oklab(0.921998 -0.00000908971 0.0000215769 / 0.5) T:1px rgba(0, 0, 0, 0) / R:1px rgba(0, 0, 0, 0) / B:1px rgba(0, 0, 0, 0) / L:1px rgba(0, 0, 0, 0) 8px; input.w-full.min-w-0 640.0x40..

Child layers that carry the look: input 640x40 background oklab(0.921998 -0.00000908971 0.0000215769 / 0.5) border 1px transparent radius 8px; input 640x40 background oklab(0.921998 -0.00000908971 0.0000215769 / 0.5) border 1px transparent radius 8px; input 640x40 background oklab(0.921998 -0.00000908971 0.0000215769 / 0.5) border 1px transparent radius 8px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Name field
A text input on the contact form; sample text typed and deleted, nothing sent. Read as `field-name` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 640 x 40; padding 4px 12px; border 1px solid transparent; radius 8px; background oklab(0.921998 -0.00000908971 0.0000215769 / 0.5); text TikTok Sans 14/20 400, lab(2.75381 0 0); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); placeholder lab(2.75381 0 0) |
| focused, filled | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Email field
The email input; sample text typed and deleted, nothing sent. Read as `field-email` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 640 x 40; padding 4px 12px; border 1px solid transparent; radius 8px; background oklab(0.921998 -0.00000908971 0.0000215769 / 0.5); text TikTok Sans 14/20 400, lab(2.75381 0 0); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); placeholder lab(2.75381 0 0) |
| focused, filled | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Company field
The company/domain input ("acme.com" placeholder); focused only. Read as `field-company` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 640 x 40; padding 4px 12px; border 1px solid transparent; radius 8px; background oklab(0.921998 -0.00000908971 0.0000215769 / 0.5); text TikTok Sans 14/20 400, lab(2.75381 0 0); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); placeholder lab(46.408 0 -0.0000119209) |
| focused | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Message field
The message textarea; focused only, nothing typed. Read as `field-message` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 640 x 64; padding 12px; border 1px solid transparent; radius 8px; background oklab(0.921998 -0.00000908971 0.0000215769 / 0.5); text TikTok Sans 14/20 400, lab(2.75381 0 0); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder lab(2.75381 0 0) |
| focused | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Send button
The Send-message submit; measured, never pressed. Read as `send-btn` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 640 x 52; padding 12px 28px; border 1px solid transparent; radius 12px; background lab(2.75381 0 0); text TikTok Sans 16/26 600, lab(98.956 0.0000298023 -0.0000119209); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) |
| hover | background oklab(0.145 -0.00000143796 0.00000340492 / 0.9) |
| focus-visible | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 614.4 x 49.92; background oklab(0.145 -0.00000143796 0.00000340492 / 0.9) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### AI image generator (free tool)

One of the ~70 free tool pages: the prompt field and the Generate-the-image submit — measured, never run.

#### Tool title
The free-tool page heading (AI image generator). Read as `tool-title` on the AI image generator page.

**Values (default).** size 392.23 x 60; background transparent; text TikTok Sans 48/60 500, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Tool panel
The prompt panel of the free tool; Generate is never pressed. Read as `tool-panel` on the AI image generator page.

**Values (default).** size 504 x 114; radius 20px; background lab(100 0 0); shadow lab(0 0 0 / 0.06) 0px 0px 0px 1px, lab(0 0 0 / 0.06) 0px 1px 2px -1px, lab(0 0 0 / 0.04) 0px 2px 4px 0px; text TikTok Sans 14/21 500, lab(98.956 0.0000298023 -0.0000119209); icon 16 x 16, lab(98.956 0.0000298023 -0.0000119209).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Prompt field
The tool's prompt input ("e.g. a fox reading a map…" placeholder); sample text typed and deleted, nothing generated. Read as `tool-prompt` on the AI image generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 504 x 64; padding 16px 20px 24px 20px; background transparent; text TikTok Sans 16/24 400, lab(2.75381 0 0); placeholder lab(46.408 0 -0.0000119209) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Generate button
The Generate-the-image submit; measured, never pressed. Read as `tool-generate` on the AI image generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 177.55 x 36; padding 0px 12px 0px 10px; border 1px solid transparent; radius 12px; background lab(2.75381 0 0); text TikTok Sans 14/21 500, lab(98.956 0.0000298023 -0.0000119209); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, lab(98.956 0.0000298023 -0.0000119209) |
| hover | background oklab(0.145 -0.00000143796 0.00000340492 / 0.9) |
| focus-visible | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 170.44 x 34.56; background oklab(0.145 -0.00000143796 0.00000340492 / 0.9); icon 15.36 x 15.36, lab(98.956 0.0000298023 -0.0000119209) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### How-it-works heading
A how-it-works heading on the tool page. Read as `tool-step` on the AI image generator page.

**Values (default).** size 672 x 40; background transparent; text TikTok Sans 36/40 500, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Model catalog

The /models grid: search, the modality tabs and the model cards.

#### Models title
The model catalog heading. Read as `models-title` on the models page.

**Values (default).** size 636.8 x 120; background transparent; text TikTok Sans 48/60 500, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Search field
The catalog search input; sample text typed and deleted. Read as `models-search` on the models page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 256 x 32; padding 4px 32px; border 1px solid lab(90.952 0 -0.0000119209); radius 12px; background lab(98.956 0.0000298023 -0.0000119209); text TikTok Sans 14/20 400, lab(2.75381 0 0); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); placeholder lab(46.408 0 -0.0000119209) |
| focused, filled | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Modality tab
A modality filter pill ("All · 65", "Chat · 21", …); measured, never toggled. Read as `mode-tab` on the models page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 74.23 x 32; padding 6px 14px; radius 3.35544e+07px; background lab(2.75381 0 0); text TikTok Sans 14/20 500, lab(98.956 0.0000298023 -0.0000119209); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 71.27 x 30.72 |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Model card
A model tile in the catalog grid (the anchor is the card; 354x200, rounded 20px); measured, never followed. Read as `model-card` on the models page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 354.66 x 200; padding 24px; radius 20px; background transparent; shadow lab(90.952 0 -0.0000119209) 0px 0px 0px 1px; text TikTok Sans 18/28 500, lab(2.75381 0 0); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, lab(2.75381 0 0); layers a.group.flex 354.7x200.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, lab(90.952 0 -0.0000119209) 0px 0px 0px 1px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 20px |
| hover | background oklab(0.969998 -0.00000959635 0.0000227094 / 0.5); layers none |
| focus-visible | outline 2px solid lab(70.8735 -22.234 -45.4927), offset 2px; layers a.group.flex 354.7x200.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, lab(90.952 0 -0.0000119209) 0px 0px 0px 1px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid lab(70.8735 -22.234 -45.4927) offset 2px 20px |
| pressed | background oklab(0.969998 -0.00000959635 0.0000227094 / 0.5); layers none |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Model link
A model name link in the catalog; measured, never followed. Read as `model-link` on the models page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 86.81 x 32; padding 6px 14px; radius 3.35544e+07px; background lab(96.52 -0.0000298023 0.0000119209); text TikTok Sans 14/20 500, lab(46.408 0 -0.0000119209); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | text TikTok Sans 14/20 500, lab(2.75381 0 0) |
| focus-visible | shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 83.34 x 30.72; text TikTok Sans 14/20 500, lab(2.75381 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Radar trends

The social radar: live trend rows, Copy buttons and Find-out-why actions.

#### Radar title
The social radar heading. Read as `radar-title` on the radar page.

**Values (default).** size 512 x 180; background transparent; text TikTok Sans 48/60 500, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Radar search
The trend search input ("Search what's happening across…"); focused only. Read as `radar-search` on the radar page.

Not on the page when it was captured.

#### Trend row
A trend row in the live radar list; measured, never followed. Read as `radar-row` on the radar page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101.77 x 32; padding 6px 10px; radius 8px; background transparent; text TikTok Sans 14/20 400, lab(46.408 0 -0.0000119209); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, lab(46.408 0 -0.0000119209); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | background lab(96.52 -0.0000298023 0.0000119209); text TikTok Sans 14/20 400, lab(2.75381 0 0); icon 12 x 12, lab(2.75381 0 0) |
| focus-visible | shadow lab(70.8735 -22.234 -45.4927) 0px 0px 0px 2px; layers ::after rgba(0, 0, 0, 0) 0px none 1; a.group/navigation-menu-trigger.w-max 101.8x32.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, lab(70.8735 -22.234 -45.4927) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 8px |
| pressed | background lab(96.52 -0.0000298023 0.0000119209); text TikTok Sans 14/20 400, lab(2.75381 0 0); icon 12 x 12, lab(2.75381 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Copy button
A trend Copy button; measured, never pressed. Read as `radar-copy` on the radar page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73.06 x 32; padding 0px 8px; border 1px solid transparent; radius 8px; background lab(7.78201 -0.0000149012 0); text TikTok Sans 14/20 500, lab(98.26 0 0); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, lab(98.26 0 0); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | background oklab(0.205 -0.00000207871 0.00000478327 / 0.8) |
| focus-visible | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 70.14 x 30.72; background oklab(0.205 -0.00000207871 0.00000478327 / 0.8); icon 15.36 x 15.36, lab(98.26 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Why link
A trend's Find-out-why action; measured, never followed. Read as `radar-why` on the radar page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 87.94 x 32; border 1px solid transparent; radius 8px; background transparent; text TikTok Sans 14/20 600, lab(46.408 0 -0.0000119209); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) |
| hover | text TikTok Sans 14/20 600, lab(2.75381 0 0) |
| focus-visible | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 84.42 x 30.72; text TikTok Sans 14/20 600, lab(2.75381 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Brand kit

The /brand asset page: logo blocks, swatches and the Copy/Download buttons — measured, never downloaded.

#### Brand title
The brand-kit heading. Read as `brand-title` on the brand page.

**Values (default).** size 672 x 60; background transparent; text TikTok Sans 48/60 500, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Logo block
A logo asset card on the brand page (a rounded-2xl bg-card tile with On-light/On-dark variants and SVG/PNG download links). Read as `brand-logo-block` on the brand page.

**Values (default).** size 436 x 208; radius 20px; background lab(100 0 0); shadow lab(90.952 0 -0.0000119209) 0px 0px 0px 1px inset; text TikTok Sans 12/16 500, lab(46.408 0 -0.0000119209); icon 44 x 44, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Colour swatch
A brand colour swatch tile in the Colors section (285x174; the page names #0A0A0A, #FAFAFA, #01BCFF). Read as `brand-swatch` on the brand page.

**Values (default).** size 285.33 x 174; radius 20px; background lab(100 0 0); shadow lab(90.952 0 -0.0000119209) 0px 0px 0px 1px inset; text TikTok Sans 16/24 500, lab(2.75381 0 0); transition box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Asset button
An asset Download link; measured, never pressed. Read as `brand-btn` on the brand page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 180.45 x 40; padding 0px 12px; border 1px solid transparent; radius 12px; background lab(7.78201 -0.0000149012 0); text TikTok Sans 14/20 500, lab(98.26 0 0); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, lab(98.26 0 0) |
| hover | background oklab(0.205 -0.00000207871 0.00000478327 / 0.8) |
| focus-visible | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 173.23 x 38.4; background oklab(0.205 -0.00000207871 0.00000478327 / 0.8); icon 15.36 x 15.36, lab(98.26 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Docs shell

/docs is a separate documentation shell with its own sidebar and Search button, inside the same token layer.

#### Docs sidebar
The docs navigation sidebar — a separate shell from the marketing pages. Read as `docs-sidebar` on the docs page.

**Values (default).** size 268 x 900; border R: 1px solid lab(90.952 0 -0.0000119209); background lab(98.956 0.0000298023 -0.0000119209); text TikTok Sans 14/20 400, lab(36.2 0 0.00000596046); transition all 0.25s ease; icon 24 x 24, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Docs nav item
A sidebar section button in the docs shell; measured, never toggled. Read as `docs-nav-item` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 236 x 36; padding 8px; radius 12px; background transparent; text TikTok Sans 14/20 400, lab(8.476 0 0); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(8.476 0 0) |
| hover | background oklab(0.954998 -0.00000944734 0.0000222921 / 0.5); transition none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto oklab(0.747992 -0.0921395 -0.125864 / 0.5), offset 0px; layers button.relative.flex 236.0x36.0 1px auto oklab(0.747992 -0.0921395 -0.125864 / 0.5) offset 0px 12px |
| pressed | background oklab(0.954998 -0.00000944734 0.0000222921 / 0.5); transition none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Search button
The docs Search (⌘K) button; measured, never opened. Read as `docs-search` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 236 x 36; padding 6px 6px 6px 8px; border 1px solid lab(90.952 0 -0.0000119209); radius 12px; background oklab(0.954998 -0.00000944734 0.0000222921 / 0.5); text TikTok Sans 14/20 400, lab(36.2 0 0.00000596046); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(36.2 0 0.00000596046) |
| hover | background lab(94.78 0 0); text TikTok Sans 14/20 400, lab(8.476 0 0); icon 16 x 16, lab(8.476 0 0) |
| focus-visible | outline 1px auto oklab(0.747992 -0.0921395 -0.125864 / 0.5), offset 0px |
| pressed | background lab(94.78 0 0); text TikTok Sans 14/20 400, lab(8.476 0 0); icon 16 x 16, lab(8.476 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Docs heading
The docs page heading in the docs typeset. Read as `docs-h1` on the docs page.

**Values (default).** size 836 x 42; background transparent; text TikTok Sans 28/42 600, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### MCP page

The /mcp page: install code blocks and their Copy buttons.

#### MCP title
The MCP page heading. Read as `mcp-title` on the MCP page.

**Values (default).** size 768 x 120; background transparent; text TikTok Sans 48/60 500, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Code block
An install/config code block (monospace surface). Read as `mcp-code` on the MCP page.

**Values (default).** size 470.94 x 20; background transparent; text Geist Mono 14/20 400, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Copy button
A code Copy button; measured, never pressed. Read as `mcp-copy` on the MCP page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73.06 x 32; padding 0px 8px; border 1px solid transparent; radius 8px; background lab(7.78201 -0.0000149012 0); text TikTok Sans 14/20 500, lab(98.26 0 0); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, lab(98.26 0 0); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | background oklab(0.205 -0.00000207871 0.00000478327 / 0.8) |
| focus-visible | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 70.14 x 30.72; background oklab(0.205 -0.00000207871 0.00000478327 / 0.8); icon 15.36 x 15.36, lab(98.26 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Blog

The /blog index: category pills and post cards.

#### Blog title
The blog index heading. Read as `blog-title` on the blog page.

**Values (default).** size 768 x 120; background transparent; text TikTok Sans 48/60 500, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Category pill
A blog category filter pill; measured, never toggled. Read as `blog-pill` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 44.98 x 32; padding 6px 14px; radius 3.35544e+07px; background lab(2.75381 0 0); text TikTok Sans 14/20 500, lab(98.956 0.0000298023 -0.0000119209); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 43.18 x 30.72 |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Post card
A post card in the blog index; measured, never followed. Read as `blog-card` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 269.33 x 347.88; border 1px solid oklab(0.921998 -0.00000908971 0.0000215769 / 0.6); radius 16px; background lab(100 0 0); text TikTok Sans 11/16 500, lab(46.408 0 -0.0000119209); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid lab(90.952 0 -0.0000119209) |
| focus-visible | border 1px solid lab(90.952 0 -0.0000119209); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | border 1px solid lab(90.952 0 -0.0000119209) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Footer

The marketing footer: link columns, legal, and the Cookie-settings and Theme controls.

#### Footer
The marketing footer: link columns, legal, the Cookie-settings and Theme controls. Read as `footer` on the home page.

**Values (default).** size 1440 x 1452.36; border T: 1px solid oklab(0.921998 -0.00000908971 0.0000215769 / 0.6); background lab(98.956 0.0000298023 -0.0000119209); text TikTok Sans 14/20 400, lab(46.408 0 -0.0000119209); icon 16 x 16, lab(46.408 0 -0.0000119209).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44.55 x 24; padding 2px 0px; radius 4px; background transparent; text TikTok Sans 14/20 400, oklab(0.145 -0.00000143796 0.00000340492 / 0.8); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text TikTok Sans 14/20 400, lab(2.75381 0 0) |
| focus-visible | outline 2px solid lab(70.8735 -22.234 -45.4927), offset 2px; text TikTok Sans 14/20 400, lab(2.75381 0 0); layers a.inline-flex.items-center 44.5x24.0 2px solid lab(70.8735 -22.234 -45.4927) offset 2px 4px |
| pressed | text TikTok Sans 14/20 400, lab(2.75381 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Theme toggle
The footer Theme icon control ("Theme: system. Switch to light"; writes the .dark class the system scheme also drives); measured, never pressed. Read as `theme-toggle` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; border 1px solid transparent; radius 8px; background transparent; text TikTok Sans 14/20 500, lab(46.408 0 -0.0000119209); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, lab(46.408 0 -0.0000119209); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | background lab(96.52 -0.0000298023 0.0000119209); text TikTok Sans 14/20 500, lab(2.75381 0 0); icon 16 x 16, lab(2.75381 0 0) |
| focus-visible | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 30.72 x 30.72; background lab(96.52 -0.0000298023 0.0000119209); text TikTok Sans 14/20 500, lab(2.75381 0 0); icon 15.36 x 15.36, lab(2.75381 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Cookie settings button
The footer Cookie-settings button; measured, never pressed (a consent surface). Read as `cookie-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 102.64 x 24; padding 2px 0px; radius 4px; background transparent; text TikTok Sans 14/20 400, oklab(0.145 -0.00000143796 0.00000340492 / 0.8); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text TikTok Sans 14/20 400, lab(2.75381 0 0) |
| focus-visible | shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px; text TikTok Sans 14/20 400, lab(2.75381 0 0); layers button.inline-flex.items-center 102.6x24.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 4px |
| pressed | text TikTok Sans 14/20 400, lab(2.75381 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Dark theme (system dark)

The same home chrome re-measured under emulated prefers-color-scheme dark — the trigger next-themes honours, so these are the values a dark-system visitor gets.

#### Header (dark)
The sticky header painted by the dark token scope. Read as `d-header` on the home page.

**Values (default).** size 1440 x 56; border B: 1px solid transparent; background oklch(0 0 none / 0.9); text TikTok Sans 14/20 500, lab(98.26 0 0); transition background-color 0.15s cubic-bezier(0.22, 1, 0.36, 1), border-bottom-color 0.15s cubic-bezier(0.22, 1, 0.36, 1); icon 24 x 24, lab(98.26 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Sign-up CTA (dark)
The sign-up pill under .dark. Read as `d-nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 138.86 x 32; padding 0px 16px; border 1px solid transparent; radius 8px; background lab(98.26 0 0); text TikTok Sans 14/20 600, lab(0 0 0); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | background oklab(0.984998 -0.00000956655 0.0000230074 / 0.9) |
| focus-visible | border 1px solid lab(70.8735 -22.234 -45.4927); shadow oklab(0.747992 -0.0921395 -0.125864 / 0.3) 0px 0px 0px 3px |
| pressed | size 133.3 x 30.72; background oklab(0.984998 -0.00000956655 0.0000230074 / 0.9) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Hero headline (dark)
The display headline under .dark. Read as `d-hero-title` on the home page.

**Values (default).** size 504.11 x 127.88; background transparent; text TikTok Sans 59.2/63.93 500, lab(98.26 0 0); icon 35.17 x 35.17, lab(98.26 0 0); layers div.home-sticker-frame.bg-surface-control 52.8x52.8 lab(7.78201 -0.0000149012 0) lab(100 0 0 / 0.08) 0px 0px 0px 1px, lab(0 0 0 / 0.6) 0px 8px 24px -12px calc(22.5% + 2.2px); div.flex.size-10 44.0x44.0 lab(100 0 0) lab(100 0 0 / 0.08) 0px 0px 0px 1px 22.5%; div.rounded-xl.bg-surface-control 93.5x112.5 lab(7.78201 -0.0000149012 0) lab(100 0 0 / 0.08) 0px 0px 0px 1px, lab(0 0 0 / 0.6) 0px 8px 24px -.

Child layers that carry the look: div 52.8x52.8 background lab(7.78201 -0.0000149012 0) radius calc(22.5% + 2.2px) shadow lab(100 0 0 / 0.08) 0px 0px 0px 1px, lab(0 0 0 / 0.6) 0px 8px 24px -12px; div 44x44 background lab(100 0 0) radius 22.5% shadow lab(100 0 0 / 0.08) 0px 0px 0px 1px; div 93.5x112.5 background lab(7.78201 -0.0000149012 0) radius 16px shadow lab(100 0 0 / 0.08) 0px 0px 0px 1px, lab(0 0 0 / 0.6) 0px 8px 24px -12px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Composer input (dark)
The Ask-Endless textarea under .dark; focused, nothing typed or sent. Read as `d-composer-input` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 660 x 72; padding 16px 20px 4px 20px; background transparent; text TikTok Sans 16/24 400, lab(98.26 0 0); placeholder lab(66.128 -0.0000298023 0.0000119209) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Nav link (dark)
A header link under .dark. Read as `d-nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 65.91 x 32; padding 6px 10px; radius 8px; background transparent; text TikTok Sans 14/20 400, lab(66.128 -0.0000298023 0.0000119209); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | background oklab(0.268999 -0.00000260025 0.00000627339 / 0.5); text TikTok Sans 14/20 400, lab(98.26 0 0) |
| focus-visible | background lab(15.204 0 -0.00000596046) |
| pressed | background oklab(0.268999 -0.00000260025 0.00000627339 / 0.5); text TikTok Sans 14/20 400, lab(98.26 0 0) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Mobile (390 wide)

The marketing surface at phone width: the compact header, the menu overlay and the stacked hero.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 56; border B: 1px solid transparent; background oklch(0.990998 0.0000251858 none / 0.9); text TikTok Sans 14/20 600, lab(46.408 0 -0.0000119209); transition background-color 0.15s cubic-bezier(0.22, 1, 0.36, 1), border-bottom-color 0.15s cubic-bezier(0.22, 1, 0.36, 1); icon 24 x 24, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Menu button
The header menu toggle. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 36 x 36; border 1px solid transparent; radius 12px; background transparent; text TikTok Sans 14/20 500, lab(2.75381 0 0); transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 20 x 20, lab(2.75381 0 0); layers ::before rgba(0, 0, 0, 0) 0px none 1.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile menu, open
The header menu panel opened by its own toggle. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 904; background transparent; text TikTok Sans 16/24 500, lab(2.75381 0 0); icon 16 x 16, lab(46.408 0 -0.0000119209); layers div.bg-overlay/30.supports-backdrop-filter:backdrop-blur-sm 390.0x904.0 oklab(0 0 0 / 0.3); div.mx-auto.box-border 390.0x436.0 lab(100 0 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px 20px 20px 0px 0px; div.rounded-t-2xl.bg-inherit .

Child layers that carry the look: div 390x904 background oklab(0 0 0 / 0.3); div 390x436 background lab(100 0 0) radius 20px 20px 0px 0px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px; div 390x736 background lab(100 0 0) radius 20px 20px 0px 0px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile nav item
An item inside the opened header menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 44.55 x 24; padding 2px 0px; radius 4px; background transparent; text TikTok Sans 14/20 400, oklab(0.145 -0.00000143796 0.00000340492 / 0.8); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 358 x 81.19; background transparent; text TikTok Sans 37.6/40.60 500, lab(2.75381 0 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile composer
Read as `m-composer` on the home page at 390 wide.

**Values (default).** size 346 x 72; padding 16px 20px 4px 20px; background transparent; text TikTok Sans 16/24 400, lab(2.75381 0 0); placeholder lab(46.408 0 -0.0000119209).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Other



## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Endless mark, tool glyphs, model tiles and illustrations) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Endless's product — the chat workspace, canvas, projects, files, MCP connections and billing — lives behind sign-in (auth on clerk.endless.app, the app at s.endless.app) and was never reached. The public surface was captured fully: the marketing pages, the free tool pages (their prompt fields were measured, never submitted — a tool page renders a quota card signed out), the model catalog, radar, docs and brand.

### Pages

- **The workspace.** Every post-login surface (chat, canvas, projects, automations, settings) needs an account and was never reached; Sign-in and Sign-up-for-free were measured, never followed.
- **Tool results.** The free tools render their prompt field signed out, but pressing Generate was never done — the generated image/audio/video outputs are uncaptured.
- **Checkout and onboarding.** Every Start-free, Get-started and plan CTA was measured, never followed past its public landing; /contact was never submitted.
- **Model and tool detail pages.** The indexes were captured; ~70 tool pages and ~20 model detail pages share the same shell — one representative tool (/tools/ai-image-generator) and the catalog were measured, the rest are recorded as same-family.
- **Radar detail.** /radar/trends/<country> and /radar/tiktok/<country> deep links exist; the index was captured.
- **Localized routes.** /de, /es, /fr, /pt serve the same marketing surface in other languages; only English was captured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **Menu and dropdown states**: the desktop header has no dropdown (flat links; the menu is a phone-width overlay, captured open); nav-dropdown and menu-link are recorded missing.

### Themes

endless.app paints light on a light system and dark on a dark one via next-themes (a `.dark` class on the html element that re-binds every semantic role; a footer Theme control writes the same class). The `-dark` shots and the dark component group were taken under emulated prefers-color-scheme dark — the same trigger the site honours — so they are the theme a dark-system visitor gets, not a reconstruction.

### Fonts

- **TikTok Sans** (the UI sans) and **Geist Mono** (code and code blocks) are the served faces, via next/font; the style guide falls back to system sans and mono.

### Screenshots

- Product illustrations, tool previews, model tiles and the Endless artwork in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, blog posts, tool descriptions and radar trend text are the product's content; only frames and components were measured.
