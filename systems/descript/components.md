# Descript components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from descript.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or downloaded; the home workflow tabs and the pricing Monthly/Annual toggle are local UI switches clicked for their opened states, and hover/focus/pressed states were forced. Sign in, Sign up, Get started, every plan CTA and the auth card's buttons/field were measured, never followed or submitted. No consent overlay was seen.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (45 components, 106 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (106 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every page paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at CSS scale (one CSS pixel per image pixel — mobile fulls are 390 wide); mobile viewport shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [workflow](screenshots/home-light-workflow.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [monthly](screenshots/pricing-light-monthly.png) |
| Video editing | `/video-editing` | [default](screenshots/video-light-default.png), [full](screenshots/video-light-full.png) |
| Templates | `/templates` | [default](screenshots/templates-light-default.png), [full](screenshots/templates-light-full.png) |
| Customer story (SaaStr) | `/customers/saastr` | [default](screenshots/story-light-default.png), [full](screenshots/story-light-full.png) |
| Underlord | `/underlord` | [default](screenshots/underlord-light-default.png), [full](screenshots/underlord-light-full.png) |
| Sign-in card (boundary) | `web.descript.com/authenticate` | [default](screenshots/auth-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Features mega dropdown | the nav | the nav item is a hover panel; items were read off the DOM, not separately componentized | boundary; see Gaps |
| Workflow tabs | the home hero band | the 'Edit' tab clicked locally | [flow-tab](#flow-tab) opened state |
| Monthly/Annual billing | pricing | the 'Annual' option clicked locally | [pr-toggle-annual](#pr-toggle-annual) opened state |
| Sign in / Sign up | the nav | the links were measured, never followed | boundary; see Gaps |
| Auth card actions | web.descript.com/authenticate | every button and the email field measured, never submitted | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 19 components were given a real keyboard focus. 13 draw an outline ring: `nav-link` (1px auto #101010 `light.border.focus`, offset 1px), `signin-link` (1px auto #101010 `light.border.focus`, offset 1px), `signup-cta` (1px auto #101010 `light.border.focus`, offset 1px), `flow-tab` (1px auto #101010 `light.border.focus`, offset 0px), `flow-tab-rest` (1px auto #101010 `light.border.focus`, offset 0px), `pr-toggle-month` (1px auto #101010 `light.border.focus`, offset 0px), `pr-toggle-annual` (1px auto #101010 `light.border.focus`, offset 0px), `pr-cta` (1px auto #101010 `light.border.focus`, offset 1px), `vid-cta` (1px auto #101010 `light.border.focus`, offset 1px), `st-cta` (1px auto #101010 `light.border.focus`, offset 1px), `ul-cta` (1px auto #101010 `light.border.focus`, offset 1px), `mp-toggle` (1px auto #e59700, offset 0px), `mp-cta` (1px auto #e59700, offset 1px). 6 draw a focus ring as a shadow instead: `tpl-link`, `au-google`, `au-sso`, `au-email-btn`, `au-password`, `au-terms`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | flow-tab, flow-tab-rest |
| 0.15s | `ease-in-out` | background-color, border-color | au-email-btn, au-google, au-password, au-sso |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | tpl-card |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|

## Components

### Header and navigation

The floating chrome shared by every page: the 102px #fff7fa nav bar (98px wordmark, 16px/600 Booton items — Features, Pricing, Contact sales, Sign in — and the 108x54 #772a4d maroon Sign up button), and the ~1146px #110a0d near-black footer with its link columns.

#### Site header
The top bar: Descript wordmark, nav (Features / Pricing / Contact sales), Sign in and the Sign up button. Read as `mkt-header` on the home page.

**Values (default).** size 1400 x 102.08; padding 24px; radius 12px; background #fff7fa `core.color.neutral.0`; text booton 16/24 600, #26171d `core.color.neutral.900`; transform translate(-700px, 0px).

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Descript wordmark at the left of the header. Read as `mkt-logo` on the home page.

**Values (default).** size 98 x 23.88; background transparent; text booton 16/24 600, #26171d `core.color.neutral.900`; transform translate(0px, 1px).

![Logo default](components/crops/mkt-logo-default.png)

#### Nav link
A header nav link ("Pricing"); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 76 x 32; padding 4px 8px; radius 4px; background transparent; text booton 16/24 600, #26171d `core.color.neutral.900` |
| hover | background #f1eaed `core.color.neutral.50` |
| focus-visible | outline 1px auto #101010 `light.border.focus`, offset 1px; layers a.flex.gap-2 76.0x32.0 1px auto rgb(16, 16, 16) offset 1px 4px |
| pressed | background #f1eaed `core.color.neutral.50` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Sign in
The header "Sign in" link; measured, never followed (it leads to the auth card measured on the auth page). Read as `signin-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73 x 32; padding 4px 8px; radius 4px; background transparent; text booton 16/24 600, #26171d `core.color.neutral.900` |
| hover | background #f1eaed `core.color.neutral.50` |
| focus-visible | outline 1px auto #101010 `light.border.focus`, offset 1px; layers a.flex.gap-2 73.0x32.0 1px auto rgb(16, 16, 16) offset 1px 4px |
| pressed | background #f1eaed `core.color.neutral.50` |

![Sign in default](components/crops/signin-link-default.png) ![Sign in hover](components/crops/signin-link-hover.png) ![Sign in focus-visible](components/crops/signin-link-focus-visible.png) ![Sign in pressed](components/crops/signin-link-pressed.png)

#### Sign up button
The maroon "Sign up" button in the header; measured, never followed. Read as `signup-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 108 x 54.08; padding 16px 24px; radius 12px; background #772a4d `core.color.maroon.700`; shadow rgba(0, 0, 0, 0.16) 0px 2px 4px 0px; text booton 16/22.08 600, #ffffff |
| hover | background #5b142e `core.color.maroon.800` |
| focus-visible | outline 1px auto #101010 `light.border.focus`, offset 1px |
| pressed | background #5b142e `core.color.maroon.800` |

![Sign up button default](components/crops/signup-cta-default.png) ![Sign up button hover](components/crops/signup-cta-hover.png) ![Sign up button focus-visible](components/crops/signup-cta-focus-visible.png) ![Sign up button pressed](components/crops/signup-cta-pressed.png)

### Home

The landing: a dark-maroon hero band (88px Gamuth display headline in #fff8f4, the 18px Brett red eyebrow, the 610px workflow tab strip — Record / Edit / Refine / Share / Multiply — whose selected tab paints #5b142e), then the AI-tools, workflow and testimonial sections on the #fff7fa blush field, and the footer.

#### Eyebrow
The small uppercase red eyebrow above the display headline ("AI VIDEO EDITOR"). Read as `hero-eyebrow` on the home page.

**Values (default).** size 892 x 18; background transparent; text brett 18/18 400, #f73b3b `core.color.red.450`.

![Eyebrow default](components/crops/hero-eyebrow-default.png)

#### Display headline
The gamuthDisplay display headline on the home hero. Read as `hero-display` on the home page.

**Values (default).** size 892 x 210; background transparent; text gamuthDisplay 88/normal 400, #fff8f4 `core.color.red.0`.

![Display headline default](components/crops/hero-display-default.png)

#### Workflow tabs
The Record / Edit / Refine / Share / Multiply workflow tab strip in "The whole workflow, right here". Read as `flow-tabs` on the home page.

**Values (default).** size 610 x 44; background transparent; text booton 16/16 600, #fff7fd `core.color.maroon.0`; layers button.shrink-0.flex 121.0x44.0 rgb(91, 20, 46) 8px; span.absolute.inset-0 16.0x16.0 rgb(213, 151, 191); span.absolute.inset-0 16.0x16.0 rgb(213, 151, 191); span.absolute.inset-0 16.0x16.0 rgb(213, 151, 191); span.absolute.inset-0 16.0x16.0 rgb(213, 151, 191); span.absolute.inset-0 16.0x16.0 rgb(213, 151, 191).

Child layers that carry the look: button 121x44 background #5b142e `core.color.maroon.800` radius 8px; span 16x16 background #d597bf `core.color.maroon.300`; span 16x16 background #d597bf `core.color.maroon.300`.

![Workflow tabs default](components/crops/flow-tabs-default.png)

#### Workflow tab
A workflow tab ("Edit"); its opened state is a local tab selection, never a navigation. Read as `flow-tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 97 x 44; padding 14px 24px 14px 16px; radius 8px; background transparent; text booton 16/16 400, #c4b5bb `light.text.muted-on-dark`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers span.absolute.inset-0 16.0x16.0 rgb(213, 151, 191) |
| hover | background #26171d `core.color.neutral.900`; layers none |
| focus-visible | outline 1px auto #101010 `light.border.focus`, offset 0px; layers button.shrink-0.flex 97.0x44.0 1px auto rgb(16, 16, 16) offset 0px 8px; span.absolute.inset-0 16.0x16.0 rgb(213, 151, 191) |
| pressed | background #26171d `core.color.neutral.900`; layers none |
| opened | size 98 x 44; background #5b142e `core.color.maroon.800`; text booton 16/16 600, #fff7fd `core.color.maroon.0`; layers none |

Child layers that carry the look: span 16x16 background #d597bf `core.color.maroon.300`.

![Workflow tab default](components/crops/flow-tab-default.png) ![Workflow tab hover](components/crops/flow-tab-hover.png) ![Workflow tab focus-visible](components/crops/flow-tab-focus-visible.png) ![Workflow tab pressed](components/crops/flow-tab-pressed.png) ![Workflow tab opened](components/crops/flow-tab-opened.png)

#### Workflow tab (rest)
A second workflow tab measured at rest for the unselected style. Read as `flow-tab-rest` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 133 x 44; padding 14px 24px 14px 16px; radius 8px; background transparent; text booton 16/16 400, #c4b5bb `light.text.muted-on-dark`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers span.absolute.inset-0 16.0x16.0 rgb(213, 151, 191) |
| hover | background #26171d `core.color.neutral.900`; layers none |
| focus-visible | outline 1px auto #101010 `light.border.focus`, offset 0px; layers button.shrink-0.flex 133.0x44.0 1px auto rgb(16, 16, 16) offset 0px 8px; span.absolute.inset-0 16.0x16.0 rgb(213, 151, 191) |
| pressed | background #26171d `core.color.neutral.900`; layers none |

Child layers that carry the look: span 16x16 background #d597bf `core.color.maroon.300`.

![Workflow tab (rest) default](components/crops/flow-tab-rest-default.png) ![Workflow tab (rest) hover](components/crops/flow-tab-rest-hover.png) ![Workflow tab (rest) focus-visible](components/crops/flow-tab-rest-focus-visible.png) ![Workflow tab (rest) pressed](components/crops/flow-tab-rest-pressed.png)

#### Section heading
A home section heading ("The whole workflow, right here"). Read as `section-h2` on the home page.

**Values (default).** size 1080 x 61.59; background transparent; text gamuthDisplay 56/61.6 700, #fff7fa `core.color.neutral.0`.

![Section heading default](components/crops/section-h2-default.png)

### Pricing

The /pricing page: the 56px Gamuth heading, the 228x50 Monthly/Annual billing toggle on its #f1eaed track, the 284x708 plan cards with 284x56 #390a1a maroon CTAs, the plan-comparison table and the FAQ.

#### Page eyebrow
The uppercase "PRICING" eyebrow heading. Read as `pr-eyebrow` on the pricing page.

**Values (default).** size 1396 x 18; background transparent; text brett 18/18 400, #f73b3b `core.color.red.450`.

![Page eyebrow default](components/crops/pr-eyebrow-default.png)

#### Pricing headline
The display heading "A plan for whatever you create". Read as `pr-display` on the pricing page.

**Values (default).** size 1396 x 61.59; background transparent; text gamuthDisplay 56/61.6 400, #390a1a `core.color.maroon.900`.

![Pricing headline default](components/crops/pr-display-default.png)

#### Billing toggle
The Monthly / Annual billing switch above the plan cards. Read as `pr-toggle` on the pricing page.

**Values (default).** size 228 x 50; padding 8px; radius 42px; background #f1eaed `core.color.neutral.50`; text booton 16/24 400, #1a1a1a `core.color.gray.900`.

![Billing toggle default](components/crops/pr-toggle-default.png)

#### Monthly option
The "Monthly" toggle option; measured, the Annual side is toggled below. Read as `pr-toggle-month` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 106 x 34; padding 5px 20px; background transparent; text booton 16/24 400, #1a1a1a `core.color.gray.900`; ancestors div.relative.mx-auto bg #f1eaed `core.color.neutral.50` |
| focus-visible | outline 1px auto #101010 `light.border.focus`, offset 0px; layers button.relative.z-20 106.0x34.0 1px auto rgb(16, 16, 16) offset 0px |

![Monthly option default](components/crops/pr-toggle-month-default.png) ![Monthly option hover](components/crops/pr-toggle-month-hover.png) ![Monthly option focus-visible](components/crops/pr-toggle-month-focus-visible.png) ![Monthly option pressed](components/crops/pr-toggle-month-pressed.png)

#### Annual option
The "Annual" toggle option — a local billing switch; its opened state is the selected-annual style, never a purchase. Read as `pr-toggle-annual` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 106 x 34; padding 5px 20px; background transparent; text booton 16/24 600, #1a1a1a `core.color.gray.900`; ancestors div.relative.mx-auto bg #f1eaed `core.color.neutral.50` |
| focus-visible | outline 1px auto #101010 `light.border.focus`, offset 0px; layers button.relative.z-20 106.0x34.0 1px auto rgb(16, 16, 16) offset 0px |

![Annual option default](components/crops/pr-toggle-annual-default.png) ![Annual option hover](components/crops/pr-toggle-annual-hover.png) ![Annual option focus-visible](components/crops/pr-toggle-annual-focus-visible.png) ![Annual option pressed](components/crops/pr-toggle-annual-pressed.png) ![Annual option opened](components/crops/pr-toggle-annual-opened.png)

#### Plan card
A pricing plan card (name, price, feature list, CTA). Read as `pr-card` on the pricing page.

**Values (default).** size 284 x 708.19; background transparent; text booton 16/24 600, #fff7fa `core.color.neutral.0`; layers a.flex.w-full 284.0x56.0 rgb(57, 10, 26) 12px; ancestors div.relative.row-span-2 bg #f1eaed `core.color.neutral.50`.

Child layers that carry the look: a 284x56 background #390a1a `core.color.maroon.900` radius 12px.

![Plan card default](components/crops/pr-card-default.png)

#### Plan CTA
A plan card’s CTA; measured, never followed (it starts signup/checkout). Read as `pr-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 284 x 56; padding 16px 32px; radius 12px; background #390a1a `core.color.maroon.900`; text booton 16/24 600, #fff7fa `core.color.neutral.0` |
| focus-visible | outline 1px auto #101010 `light.border.focus`, offset 1px |

![Plan CTA default](components/crops/pr-cta-default.png) ![Plan CTA hover](components/crops/pr-cta-hover.png) ![Plan CTA focus-visible](components/crops/pr-cta-focus-visible.png) ![Plan CTA pressed](components/crops/pr-cta-pressed.png)

#### Comparison heading
The "What’s the difference?" heading over the plan comparison table. Read as `pr-compare-h2` on the pricing page.

**Values (default).** size 1400 x 61.59; background transparent; text gamuthDisplay 56/61.6 400, #390a1a `core.color.maroon.900`.

![Comparison heading default](components/crops/pr-compare-h2-default.png)

#### FAQ heading
The "Frequently asked questions" section heading. Read as `pr-faq` on the pricing page.

**Values (default).** size 651.97 x 123.19; background transparent; text gamuthDisplay 56/61.6 400, #190308 `core.color.maroon.950`.

![FAQ heading default](components/crops/pr-faq-default.png)

### Video editing page

The /video-editing page: the 72px Gamuth 'All-in-one video editing' heading and the 222x56 #f73b3b red CTA.

#### Page headline
The "All-in-one video editing" display heading. Read as `vid-h1` on the video-editing page.

**Values (default).** size 500 x 158.38; background transparent; text gamuthDisplay 72/79.2 600, #390a1a `core.color.maroon.900`.

![Page headline default](components/crops/vid-h1-default.png)

#### Page CTA
The video page hero CTA; measured, never followed. Read as `vid-cta` on the video-editing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 222 x 56; padding 16px 32px; radius 12px; background #f73b3b `core.color.red.450`; text booton 16/24 600, #fff7fd `core.color.maroon.0` |
| hover | background #b81b1e `core.color.red.600` |
| focus-visible | outline 1px auto #101010 `light.border.focus`, offset 1px |
| pressed | background #8f0c10 `core.color.red.700` |

![Page CTA default](components/crops/vid-cta-default.png) ![Page CTA hover](components/crops/vid-cta-hover.png) ![Page CTA focus-visible](components/crops/vid-cta-focus-visible.png) ![Page CTA pressed](components/crops/vid-cta-pressed.png)

#### Section heading
A feature section heading on the video page. Read as `vid-h2` on the video-editing page.

**Values (default).** size 1006 x 61.59; background transparent; text gamuthDisplay 56/61.6 400, #fff8f4 `core.color.red.0`.

![Section heading default](components/crops/vid-h2-default.png)

### Templates gallery

The /templates page: the 72px Gamuth heading and the grid of 336x381 template cards whose overlay links carry a 2px inset focus ring.

#### Gallery heading
The templates gallery heading. Read as `tpl-h1` on the templates page.

**Values (default).** size 1200 x 158.38; background transparent; text gamuthDisplay 72/79.2 600, #3f2a32 `core.color.neutral.800`.

![Gallery heading default](components/crops/tpl-h1-default.png)

#### Template card
A template card in the gallery grid (thumbnail, name, category); the overlay link was measured, never followed. Read as `tpl-card` on the templates page.

**Values (default).** size 338 x 382.56; border 1px solid #b8a5ad `core.color.neutral.300`; radius 8px; background #f1eaed `core.color.neutral.50`; text booton 14/20 400, #6b7280; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1).

![Template card default](components/crops/tpl-card-default.png)

#### Template link
A template card’s overlay link; measured, never followed. Read as `tpl-link` on the templates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 336 x 380.56; radius 8px; background transparent; text booton 16/24 400, #1a1a1a `core.color.gray.900`; ancestors div.group.relative bg #f1eaed `core.color.neutral.50` |
| hover | ancestors div.group.relative bg #e4dde0 `core.color.neutral.100` |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, #f73b3b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px; layers a.absolute.inset-0 336.0x380.6 rgb(255, 255, 255) 0px 0px 0px 0px inset, rgb(247, 59, 59) 0px 0px 0px 2px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 8px |

![Template link default](components/crops/tpl-link-default.png) ![Template link hover](components/crops/tpl-link-hover.png) ![Template link focus-visible](components/crops/tpl-link-focus-visible.png) ![Template link pressed](components/crops/tpl-link-pressed.png)

### Customer story

The /customers/saastr story: the long-form headline, 16px/600 Booton prose and the 'Request a demo' CTA.

#### Story headline
The SaaStr customer story headline. Read as `st-h1` on the customers/saastr page.

**Values (default).** size 604 x 246.38; background transparent; text gamuthDisplay 56/61.6 400, #390a1a `core.color.maroon.900`.

![Story headline default](components/crops/st-h1-default.png)

#### Story prose
Body copy in the customer story. Read as `st-prose` on the customers/saastr page.

**Values (default).** size 600 x 216; background transparent; text booton 18/27 400, #fff7fa `core.color.neutral.0`.

![Story prose default](components/crops/st-prose-default.png)

#### Story CTA
The "Request a demo" CTA in the customer story; measured, never followed. Read as `st-cta` on the customers/saastr page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 191 x 56; padding 16px 32px; radius 12px; background #f73b3b `core.color.red.450`; text booton 16/24 600, #fff7fd `core.color.maroon.0` |
| hover | background #b81b1e `core.color.red.600` |
| focus-visible | outline 1px auto #101010 `light.border.focus`, offset 1px |
| pressed | background #8f0c10 `core.color.red.700` |

![Story CTA default](components/crops/st-cta-default.png) ![Story CTA hover](components/crops/st-cta-hover.png) ![Story CTA focus-visible](components/crops/st-cta-focus-visible.png) ![Story CTA pressed](components/crops/st-cta-pressed.png)

### Underlord

The /underlord AI co-editor page: the 72px Gamuth headline and CTA.

#### Underlord headline
The Underlord AI co-editor page headline. Read as `ul-h1` on the underlord page.

**Values (default).** size 700 x 158.38; background transparent; text gamuthDisplay 72/79.2 600, #390a1a `core.color.maroon.900`.

![Underlord headline default](components/crops/ul-h1-default.png)

#### Underlord CTA
The Underlord page CTA; measured, never followed. Read as `ul-cta` on the underlord page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 222 x 56; padding 16px 32px; radius 12px; background #f73b3b `core.color.red.450`; text booton 16/24 600, #fff7fd `core.color.maroon.0` |
| hover | background #b81b1e `core.color.red.600` |
| focus-visible | outline 1px auto #101010 `light.border.focus`, offset 1px |
| pressed | background #8f0c10 `core.color.red.700` |

![Underlord CTA default](components/crops/ul-cta-default.png) ![Underlord CTA hover](components/crops/ul-cta-hover.png) ![Underlord CTA focus-visible](components/crops/ul-cta-focus-visible.png) ![Underlord CTA pressed](components/crops/ul-cta-pressed.png)

### Auth card

The sign-in boundary at web.descript.com/authenticate: the 308x40 'Continue with Google'/'Use single sign-on' outline buttons, the email field, the #3f2a32 'Continue with email' primary and the ghost 'Use a password instead'. Every control measured, never submitted.

#### Auth card
The sign-in card on web.descript.com/authenticate (SSO buttons, email field, terms links). Read as `au-card` on the auth page.

**Values (default).** size 1440 x 900; background transparent; text Booton VF 15.75/22.5 500, #26171d `core.color.neutral.900`; icon 20 x 20, #26171d `core.color.neutral.900`; layers div.stack.h-screen 1440.0x900.0 rgb(244, 241, 240); div.rounded-xl.p-2 400.0x460.7 rgb(253, 252, 252) T:1px solid rgba(88, 63, 74, 0.1) / R:1px solid rgba(88, 63, 74, 0.1) / B:1px solid rgba(88, 63, 74, 0.1) / L:1px solid rgba(88, 63, 74, 0.1) rgba(38, 23, 29, 0.12) 0px 16px 38px 0px, rgba(38, 23, 29, 0.12) 0px 120px 136px 0px 12px; div.text-brand-logo-mark.icon-token 40.0x40.0 rgb(247, 59, 59); d; ancestors div bg #ffffff.

Child layers that carry the look: div 1440x900 background #f4f1f0; div 400x460.7 background #fdfcfc `light.action.auth-outline` border 1px solid rgba(88, 63, 74, 0.1) radius 12px shadow rgba(38, 23, 29, 0.12) 0px 16px 38px 0px, rgba(38, 23, 29, 0.12) 0px 120px 136px 0px; div 40x40 background #f73b3b `core.color.red.450`.

![Auth card default](components/crops/au-card-default.png)

#### Google SSO
"Continue with Google" — the outline SSO button; measured, never pressed. Read as `au-google` on the auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 308 x 40.48; padding 8px 12px; border 1px solid rgba(17, 10, 13, 0.45); radius 8px; background #fdfcfc `light.action.auth-outline`; shadow #26171d 0px 0px 0px 0px; text Booton VF 15.75/22.5 500, #26171d `core.color.neutral.900`; transition background-color 0.15s ease-in-out, border-color 0.15s ease-in-out; icon 20 x 20, #26171d `core.color.neutral.900` |
| hover | background #f4f1f0 |
| focus-visible | border 1px solid #3434ab `core.color.lilac.700`; shadow #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px |
| pressed | background #f4f1f0 |

![Google SSO default](components/crops/au-google-default.png) ![Google SSO hover](components/crops/au-google-hover.png) ![Google SSO focus-visible](components/crops/au-google-focus-visible.png) ![Google SSO pressed](components/crops/au-google-pressed.png)

#### SSO button
"Use single sign-on" — the second outline auth option; measured, never pressed. Read as `au-sso` on the auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 308 x 40.48; padding 8px 12px; border 1px solid rgba(17, 10, 13, 0.45); radius 8px; background #fdfcfc `light.action.auth-outline`; shadow #26171d 0px 0px 0px 0px; text Booton VF 15.75/22.5 500, #26171d `core.color.neutral.900`; transition background-color 0.15s ease-in-out, border-color 0.15s ease-in-out |
| hover | background #f4f1f0 |
| focus-visible | border 1px solid #3434ab `core.color.lilac.700`; shadow #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px |
| pressed | background #f4f1f0 |

![SSO button default](components/crops/au-sso-default.png) ![SSO button hover](components/crops/au-sso-hover.png) ![SSO button focus-visible](components/crops/au-sso-focus-visible.png) ![SSO button pressed](components/crops/au-sso-pressed.png)

#### Email field
The auth email input; focused and typed into then cleared, never submitted. Read as `au-email` on the auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 308 x 40.48; padding 8px 12px; border 1px solid rgba(63, 42, 50, 0.16); radius 8px; background #fdfcfc `light.action.auth-outline`; shadow #26171d 0px 0px 0px 0px; text Booton VF 15.75/22.5 400, #26171d `core.color.neutral.900`; placeholder rgba(22, 5, 12, 0.6) |
| focused, filled | border 1px solid #3434ab `core.color.lilac.700`; shadow #26171d 0px 0px 0px 0px, oklab(0.410426 0.0150268 -0.183218 / 0.5) 0px 0px 0px 3px |

![Email field default](components/crops/au-email-default.png) ![Email field focused](components/crops/au-email-focused.png) ![Email field filled](components/crops/au-email-filled.png)

#### Email button
"Continue with email" — the primary auth button; measured, never pressed. Read as `au-email-btn` on the auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 308 x 40.48; padding 8px 12px; border 1px solid #3f2a32 `core.color.neutral.800`; radius 8px; background #3f2a32 `core.color.neutral.800`; shadow #ffffff 0px 0px 0px 0px; text Booton VF 15.75/22.5 500, #ffffff; transition background-color 0.15s ease-in-out, border-color 0.15s ease-in-out |
| hover | border 1px solid oklab(0.313067 0.0335334 -0.00314325 / 0.9); background oklab(0.313067 0.0335334 -0.00314325 / 0.9) |
| focus-visible | border 1px solid #3434ab `core.color.lilac.700`; shadow #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px |
| pressed | border 1px solid oklab(0.313067 0.0335334 -0.00314325 / 0.9); background oklab(0.313067 0.0335334 -0.00314325 / 0.9) |

![Email button default](components/crops/au-email-btn-default.png) ![Email button hover](components/crops/au-email-btn-hover.png) ![Email button focus-visible](components/crops/au-email-btn-focus-visible.png) ![Email button pressed](components/crops/au-email-btn-pressed.png)

#### Password link
"Use a password instead" — the ghost fallback; measured, never pressed. Read as `au-password` on the auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 308 x 40.48; padding 8px 12px; border 1px solid #fdfcfc `light.action.auth-outline`; radius 8px; background #fdfcfc `light.action.auth-outline`; text Booton VF 15.75/22.5 500, #26171d `core.color.neutral.900`; transition background-color 0.15s ease-in-out, border-color 0.15s ease-in-out |
| hover | background #f4f1f0 |
| focus-visible | border 1px solid #3434ab `core.color.lilac.700`; shadow #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px |
| pressed | background #f4f1f0 |

![Password link default](components/crops/au-password-default.png) ![Password link hover](components/crops/au-password-hover.png) ![Password link focus-visible](components/crops/au-password-focus-visible.png) ![Password link pressed](components/crops/au-password-pressed.png)

#### Terms link
The "Terms of Service" link under the auth card; measured, never followed. Read as `au-terms` on the auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 103.03 x 16; background transparent; text Booton VF 12/16 475, rgba(22, 5, 12, 0.6) |
| focus-visible | radius 6px; shadow #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px; layers a.Link-module--Oc8GoN.cursor-pointer 103.0x16.0 rgb(163, 163, 238) 0px 0px 0px 1px, rgb(52, 52, 171) 0px 0px 0px 2px 6px |

![Terms link default](components/crops/au-terms-default.png) ![Terms link hover](components/crops/au-terms-hover.png) ![Terms link focus-visible](components/crops/au-terms-focus-visible.png) ![Terms link pressed](components/crops/au-terms-pressed.png)

### Mobile (390 wide)

The home and /pricing at phone width: the 84px nav, the 48px display heading, the billing toggle and full-width plan CTAs.

#### Mobile header
The phone top bar: wordmark and sign-in/sign-up actions. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 84; padding 84px 18.75px 0px 18.75px; background transparent; text booton 15/22.5 600, #ffffff; layers ul.flex.gap-6 390.0x84.5 rgb(255, 247, 250) B:2px solid rgb(241, 234, 237); a.bg-[var(--Maroon-750)].hover:bg-[var(--Maroon-800)] 104.0x52.5 rgb(101, 26, 57) rgba(0, 0, 0, 0.16) 0px 2px 4px 0px 11.25px; div.h-[calc(100dvh-84px)].sm:h-[calc(100dvh-90px)] 0.0x0.0 rgb(255, 247, 250); a.mt-4.bg-[var(--Maroon-750)] 0.0x0.0 rgb(101, 26, 57) rgba(0, 0, 0, 0.16) 0px 2px 4px 0px 11.25px; ancestors section.lg:h-[92px].relative bg #ffffff.

Child layers that carry the look: ul 390x84.5 background #fff7fa `core.color.neutral.0` border 2px solid #f1eaed `core.color.neutral.50`; a 104x52.5 background #651a39 `core.color.maroon.750` radius 11.25px shadow rgba(0, 0, 0, 0.16) 0px 2px 4px 0px; div 0x0 background #fff7fa `core.color.neutral.0`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile eyebrow
The phone hero eyebrow heading. Read as `m-eyebrow` on the home page at 390 wide.

**Values (default).** size 342 x 18; background transparent; text brett 18/18 400, #f73b3b `core.color.red.450`.

![Mobile eyebrow default](components/crops/m-eyebrow-default.png)

#### Mobile display
The phone display headline. Read as `m-display` on the home page at 390 wide.

**Values (default).** size 342 x 171; background transparent; text gamuthDisplay 48/normal 400, #fff8f4 `core.color.red.0`.

![Mobile display default](components/crops/m-display-default.png)

#### Mobile footer
The phone footer. Read as `m-footer` on the home page at 390 wide.

**Values (default).** size 390 x 1858.69; padding 45px 18.75px 52.5px 18.75px; background #110a0d `core.color.neutral.950`; text booton 18/25.2 400, #d1c7cb `core.color.neutral.200`.

![Mobile footer default](components/crops/m-footer-default.png)

#### Mobile billing toggle
The Annual option of the billing toggle on the phone. Read as `mp-toggle` on the pricing page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 98.5 x 32.5; padding 5px 18.75px; background transparent; text booton 15/22.5 600, #1a1a1a `core.color.gray.900`; ancestors div.relative.mx-auto bg #f1eaed `core.color.neutral.50` |
| focus-visible | outline 1px auto #e59700, offset 0px; layers button.relative.z-20 98.5x32.5 1px auto rgb(229, 151, 0) offset 0px |

![Mobile billing toggle default](components/crops/mp-toggle-default.png) ![Mobile billing toggle hover](components/crops/mp-toggle-hover.png) ![Mobile billing toggle focus-visible](components/crops/mp-toggle-focus-visible.png) ![Mobile billing toggle pressed](components/crops/mp-toggle-pressed.png)

#### Mobile plan CTA
A plan CTA on the phone pricing page; measured, never followed. Read as `mp-cta` on the pricing page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 307.5 x 52.5; padding 15px 30px; radius 11.25px; background #390a1a `core.color.maroon.900`; text booton 15/22.5 600, #fff7fa `core.color.neutral.0` |
| focus-visible | outline 1px auto #e59700, offset 1px |

![Mobile plan CTA default](components/crops/mp-cta-default.png) ![Mobile plan CTA hover](components/crops/mp-cta-hover.png) ![Mobile plan CTA focus-visible](components/crops/mp-cta-focus-visible.png) ![Mobile plan CTA pressed](components/crops/mp-cta-pressed.png)

### Footer



#### Site footer
The sitemap footer (product links, resources, company). Read as `site-footer` on the home page.

**Values (default).** size 1440 x 1145.81; padding 86px 64px 104px 64px; background #110a0d `core.color.neutral.950`; text booton 18/25.2 400, #d1c7cb `core.color.neutral.200`.

![Site footer default](components/crops/site-footer-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the wordmark, the social icons, the hero tile glyphs) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Members and external destinations

Descript's product lives behind web.descript.com — its public sign-in card was captured as the authenticated boundary and never submitted: this package covers the public marketing site at www.descript.com plus that auth surface. The 'Sign in'/'Sign up' links, every 'Get started'/'Try free'/plan CTA and the auth card's 'Continue with Google'/'Use single sign-on'/'Continue with email' buttons were measured, never followed or pressed. The email field was typed into and cleared, never submitted.

### Pages

- **Outbound links.** 'Sign in', 'Sign up' (web.descript.com), 'Get started', 'Try free', 'Request a demo', every plan CTA and every product/social link were measured, never followed — they leave the captured surface or start signup/checkout.
- **The Features dropdown** opens on hover as a mega panel of product links; the panel was read off the DOM but its items were not individually componentized.
- **Other marketing pages.** /video-editing, /templates, /customers/saastr and /underlord were captured; the dozens of other product/resource pages share the same chrome and hero/card vocabulary but are not individually documented.
- **The auth card** is a boundary: its buttons and field were measured and the field typed/cleared, but nothing was submitted and no authenticated page was reached.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **The nav dropdowns, hero action tiles and FAQ accordions** were toggled locally (the site's own triggers); nothing was typed into or submitted anywhere.
- **The only form is the auth card's email field** — it was typed into and cleared, never submitted; validation, disabled and error states are absent rather than measured.
- **The workflow tab strip switches the hero's preview panel** — the selected tab was measured open; the panels behind the other tabs were not individually measured.

### Themes

One painted theme, no toggle: a #fff7fa blush field, a deep-maroon hero band and #110a0d footer, maroon CTAs ramping #772a4d to #390a1a, and #f73b3b red accents on eyebrows and secondary CTAs. The dark regions are recorded as surfaces inside the single theme; tokens.json emits light only.

### Fonts

- **gamuthDisplay** (every display heading), **booton** (UI/body, incl. the auth card's 'Booton VF' reading) and **brett** (the 18px uppercase eyebrows) are served by the site. Font files are not shipped in this package.

### Screenshots

- Customer names, faces and quotes in the review carousel and the artwork inside hero panels are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Testimonial copy, pricing figures and the artwork inside panels are the product's content; only frames and components were measured.
