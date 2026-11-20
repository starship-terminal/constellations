# Arcade components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from arcade.software on 2026-11-10, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent, submitted or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (49 components, 126 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (125 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [quote-next](screenshots/home-light-quote-next.png), [suggestion](screenshots/home-light-suggestion.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [faq](screenshots/pricing-light-faq.png), [full](screenshots/pricing-light-full.png) |
| Interactive demo | `/product/interactive-demo` | [default](screenshots/interactive-demo-light-default.png), [full](screenshots/interactive-demo-light-full.png) |
| Agents | `/agents` | [default](screenshots/agents-light-default.png), [full](screenshots/agents-light-full.png) |
| Enterprise | `/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| AI video examples | `/ai-video-examples` | [default](screenshots/video-examples-light-default.png), [full](screenshots/video-examples-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Changelog | `/changelog` | [default](screenshots/changelog-light-default.png), [full](screenshots/changelog-light-full.png) |
| Contact sales | `/contact-sales` | [default](screenshots/contact-sales-light-default.png), [full](screenshots/contact-sales-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Interactive demo, phone | `/product/interactive-demo` | [default](screenshots/mobile-interactive-demo-light-default.png), [full](screenshots/mobile-interactive-demo-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Prompt suggestion applied | hero, home | a chip's own tap swaps the prompt text | [home-light-suggestion](screenshots/home-light-suggestion.png) |
| Spotlight quote, next | home | the carousel arrow's own press | [home-light-quote-next](screenshots/home-light-quote-next.png), [spotlight-next](#spotlight-next) |
| Pricing FAQ, open | pricing | the accordion's own toggle | [faq-open](#faq-accordion-open), [pricing-light-faq](screenshots/pricing-light-faq.png) |
| Mobile menu, open | home, phone | the menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 22 components were given a real keyboard focus (a further 1 could not be driven: `form-submit`). 22 show a visible focus state: `nav-link` (1px auto #005fcc, offset 1px), `nav-login` (1px auto #005fcc, offset 1px), `nav-signup` (1px auto #005fcc, offset 1px), `prompt-send` (2px solid #000000 `brand.900`, offset 2px), `prompt-plus` (2px solid #000000 `brand.900`, offset 2px), `suggestion-chip` (2px solid #000000 `brand.900`, offset 2px), `scatter-card` (1px auto #005fcc, offset 1px), `spotlight-next` (1px auto #005fcc, offset 1px), `cta-large` (1px auto #005fcc, offset 1px), `cta-secondary` (1px auto #005fcc, offset 1px), `plan-cta-pro` (1px auto #005fcc, offset 1px), `plan-cta-neutral` (1px auto #005fcc, offset 1px), `faq-question` (2px solid #171717, offset -2px), `ask-ai` (1px auto #005fcc, offset 1px), `demo-signup` (1px auto #005fcc, offset 1px), `demo-tts` (1px auto #005fcc, offset 0.984375px), `url-button` (visible change in boxShadow/backgroundColor), `footer-link` (1px auto #005fcc, offset 1px), `footer-social` (1px auto #005fcc, offset 1px), `footer-legal` (1px auto #005fcc, offset 1px), `m-menu-button` (2px solid #000000 `brand.900`, offset -2px), `m-signup` (2px solid #000000 `brand.900`, offset 2px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): the controls shrink ~3% on press (a Webflow press transform); black CTAs keep their fill. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | all | logo |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | all, opacity, transform | cta-large, cta-secondary, m-nav-link, m-signup, nav-link, nav-login, nav-signup, plan-cta-neutral and more |
| 0.15s | `ease` | background-color, border-color, color | field-select, field-text, field-textarea, form-submit, model-radio |
| 0.15s | `ease-in` | all, background-color | ask-ai, footer-legal, footer-link, footer-social, header, m-header |
| 0.16s | `cubic-bezier(0.2, 0.8, 0.2, 1)` | transform | prompt-plus, prompt-send, suggestion-chip |
| 0.16s | `ease` | background-color, border-color, color, opacity | prompt-plus, prompt-send, suggestion-chip |
| 0.2s | `cubic-bezier(0.16, 1, 0.3, 1)` | all | url-button |
| 0.2s | `ease-out` | all | newsletter-field |
| 0.35s | `cubic-bezier(0.6, 0.6, 0, 1)` | all | demo-signup, demo-tts |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Pro plan card](#pro-plan-card) | 437.33 x 522 | - | 24px | #f4f4f4 `brand.100` | none | 2px |
| [Prompt box](#prompt-box) | 680 x 148 | - | 16px | #ffffff `brand.white` | rgba(0, 0, 0, 0.03) 0px 16px 16px 0px, rgba(0, 0, 0, 0.03) 0px 8px 8px 0px, rgba(0, 0, 0, 0.03) 0px 4px 4px 0px, rgba(0, 0, 0, 0.03) 0px 2px 2px -2px, rgba(0, 0, 0, 0.12) 0px 0px 0px 1px | 0 |
| [FAQ accordion button](#faq-accordion-button) | 700 x 56 | - | 16px | transparent | none | 16px 24px |
| [Text field](#text-field) | 199 x 40 | 1px solid #f4f4f4 `brand.100` | 12px | #f4f4f4 `brand.100` | none | 0px 12px |
| [Form card](#form-card) | 480 x 697 | 1px solid #e7e7e7 `brand.200` | 24px | #ffffff `brand.white` | none | 8px |

## Components

### Shell and navigation

The fixed top bar and its link and pill actions.

#### Header
The fixed top bar: logo, Product/Pricing/Blog/Enterprise links, Log in and Sign up. Read as `header` on the home page.

**Values (default).** size 1440 x 72; background rgba(255, 255, 255, 0); text Inter Variable 14/20 500, rgba(0, 0, 0, 0.7); transition background-color 0.15s ease-in; icon 98 x 26, #333333.

![Header default](components/crops/header-default.png)

#### Logo
Read as `logo` on the home page.

**Values (default).** size 106 x 32; background transparent; text Inter Variable 16/24 400, #333333; transition all 0.15s cubic-bezier(0.25, 0.46, 0.45, 0.94); icon 98 x 26, #333333.

![Logo default](components/crops/logo-default.png)

#### Nav link
Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 70.73 x 32; padding 0px 12px; radius 12px; background transparent; text Inter Variable 14/20 500, rgba(0, 0, 0, 0.7); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(0, 0, 0, 0.06) `measured.hover-wash`; text Inter Variable 14/20 500, #000000 `brand.900` |
| focus-visible | shadow rgba(0, 0, 0, 0.2) 0px 0px 0px 2px; outline 1px auto #005fcc, offset 1px |
| pressed | size 68.61 x 31.04; background rgba(0, 0, 0, 0.06) `measured.hover-wash`; text Inter Variable 14/20 500, #000000 `brand.900`; transform scale(0.97) |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log in button
The ghost nav action. Measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 64.73 x 32; padding 0px 12px; radius 12px; background transparent; text Inter Variable 14/20 500, #000000 `brand.900`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(0, 0, 0, 0.06) `measured.hover-wash` |
| focus-visible | shadow rgba(0, 0, 0, 0.2) 0px 0px 0px 2px; outline 1px auto #005fcc, offset 1px |
| pressed | size 62.79 x 31.04; background rgba(0, 0, 0, 0.06) `measured.hover-wash`; transform scale(0.97) |

![Log in button default](components/crops/nav-login-default.png) ![Log in button hover](components/crops/nav-login-hover.png) ![Log in button focus-visible](components/crops/nav-login-focus-visible.png) ![Log in button pressed](components/crops/nav-login-pressed.png)

#### Sign up button
The black pill nav action. Measured, never followed. Read as `nav-signup` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 74.48 x 32; padding 0px 12px; radius 12px; background #000000 `brand.900`; text Inter Variable 14/20 500, #ffffff `brand.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #404040 `brand.700` |
| focus-visible | shadow rgba(0, 0, 0, 0.2) 0px 0px 0px 2px; outline 1px auto #005fcc, offset 1px |
| pressed | size 72.25 x 31.04; background #404040 `brand.700`; transform scale(0.97) |

![Sign up button default](components/crops/nav-signup-default.png) ![Sign up button hover](components/crops/nav-signup-hover.png) ![Sign up button focus-visible](components/crops/nav-signup-focus-visible.png) ![Sign up button pressed](components/crops/nav-signup-pressed.png)

### Home

The animated hero, the video prompt composer, suggestion chips, the scatter wall and the quote spotlight.

#### Hero title
One of the animated .heading-1 lines. Read as `hero-title` on the home page.

**Values (default).** size 305.06 x 67.2; background transparent; text Inter Display 56/67.2 400, #000000 `brand.900`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero subtitle
Read as `hero-subtitle` on the home page.

**Values (default).** size 403.95 x 24; background transparent; text Inter Variable 16/24 400, rgba(0, 0, 0, 0.8).

![Hero subtitle default](components/crops/hero-subtitle-default.png)

#### Prompt box
The "describe your video" composer on the hero: textarea, plus and send. Read as `prompt-box` on the home page.

**Values (default).** size 680 x 148; radius 16px; background #ffffff `brand.white`; shadow rgba(0, 0, 0, 0.03) 0px 16px 16px 0px, rgba(0, 0, 0, 0.03) 0px 8px 8px 0px, rgba(0, 0, 0, 0.03) 0px 4px 4px 0px, rgba(0, 0, 0, 0.03) 0px 2px 2px -2px, rgba(0, 0, 0, 0.12) 0px 0px 0px 1px; text Inter Variable 12/16 500, rgba(0, 0, 0, 0.6); icon 16 x 16, #000000 `brand.900`.

![Prompt box default](components/crops/prompt-box-default.png)

#### Prompt field
Focused only; nothing was sent. Read as `prompt-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 680 x 148; padding 16px 16px 48px 16px; radius 16px; background transparent; text Inter Variable 16/24 400, #000000 `brand.900`; placeholder #a3a3a3 |

![Prompt field default](components/crops/prompt-field-default.png) ![Prompt field focused](components/crops/prompt-field-focused.png)

#### Prompt send
The composer submit. Measured, never pressed. Read as `prompt-send` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 12px; background #000000 `brand.900`; text Inter Variable 16/24 400, #ffffff `brand.white`; transition background-color 0.16s ease, opacity 0.16s ease, transform 0.16s cubic-bezier(0.2, 0.8, 0.2, 1); icon 18 x 18, #ffffff `brand.white` |
| hover | opacity 0.7 |
| focus-visible | outline 2px solid #000000 `brand.900`, offset 2px |
| pressed | size 31.04 x 31.04; transform scale(0.97); opacity 0.7; icon 17.46 x 17.46, #ffffff `brand.white` |

![Prompt send default](components/crops/prompt-send-default.png) ![Prompt send hover](components/crops/prompt-send-hover.png) ![Prompt send focus-visible](components/crops/prompt-send-focus-visible.png) ![Prompt send pressed](components/crops/prompt-send-pressed.png)

#### Prompt plus link
"Open Arcade" beside the composer. Measured, never followed. Read as `prompt-plus` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 12px; background transparent; text Inter Variable 16/24 400, #000000 `brand.900`; transition background-color 0.16s ease, opacity 0.16s ease, transform 0.16s cubic-bezier(0.2, 0.8, 0.2, 1); icon 16 x 16, #000000 `brand.900` |
| hover | background #f5f5f5 |
| focus-visible | outline 2px solid #000000 `brand.900`, offset 2px |
| pressed | size 31.04 x 31.04; background #f5f5f5; transform scale(0.97); icon 15.52 x 15.52, #000000 `brand.900` |

![Prompt plus link default](components/crops/prompt-plus-default.png) ![Prompt plus link hover](components/crops/prompt-plus-hover.png) ![Prompt plus link focus-visible](components/crops/prompt-plus-focus-visible.png) ![Prompt plus link pressed](components/crops/prompt-plus-pressed.png)

#### Suggestion chip
A prompt preset pill under the composer. Tapped in screenshots only; never submitted. Read as `suggestion-chip` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 103.02 x 32; padding 0px 12px; border 1px solid rgba(0, 0, 0, 0.2); radius 12px; background #ffffff `brand.white`; text Inter Variable 12/16 500, rgba(0, 0, 0, 0.6); transition color 0.16s ease, border-color 0.16s ease, transform 0.16s cubic-bezier(0.2, 0.8, 0.2, 1) |
| hover | border 1px solid rgba(0, 0, 0, 0.35); text Inter Variable 12/16 500, rgba(0, 0, 0, 0.8) |
| focus-visible | outline 2px solid #000000 `brand.900`, offset 2px |
| pressed | size 99.93 x 31.04; border 1px solid rgba(0, 0, 0, 0.35); text Inter Variable 12/16 500, rgba(0, 0, 0, 0.8); transform scale(0.97) |

![Suggestion chip default](components/crops/suggestion-chip-default.png) ![Suggestion chip hover](components/crops/suggestion-chip-hover.png) ![Suggestion chip focus-visible](components/crops/suggestion-chip-focus-visible.png) ![Suggestion chip pressed](components/crops/suggestion-chip-pressed.png)

#### Scatter card
A "Play <title>" video card in the Made-to-be-seen wall. Measured, never followed. Read as `scatter-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 276.65 x 168.8; background transparent; text Inter Variable 16/24 400, #0000ee |
| hover | size 291.56 x 198.52 |
| focus-visible | size 274.8 x 171.97; outline 1px auto #005fcc, offset 1px |
| pressed | size 272.22 x 175.34; text Inter Variable 16/24 400, #ff0000 |

![Scatter card default](components/crops/scatter-card-default.png) ![Scatter card hover](components/crops/scatter-card-hover.png) ![Scatter card focus-visible](components/crops/scatter-card-focus-visible.png) ![Scatter card pressed](components/crops/scatter-card-pressed.png)

#### Spotlight quote
Read as `spotlight-quote` on the home page.

**Values (default).** size 560 x 204; background transparent; text Inter Display 36/40 400, #000000 `brand.900`.

![Spotlight quote default](components/crops/spotlight-quote-default.png)

#### Spotlight next
The quote carousel arrow. Pressed once for the screenshot state. Read as `spotlight-next` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; border 1px solid #e5e7eb `neutral.200.default`; radius 14px; background #ffffff `brand.white`; text Inter Variable 16/24 400, #000000 `brand.900`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #000000 `brand.900` |
| hover | opacity 0.7 |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | size 38.8 x 38.8; transform scale(0.97); opacity 0.7; icon 19.4 x 19.4, #000000 `brand.900` |

![Spotlight next default](components/crops/spotlight-next-default.png) ![Spotlight next hover](components/crops/spotlight-next-hover.png) ![Spotlight next focus-visible](components/crops/spotlight-next-focus-visible.png) ![Spotlight next pressed](components/crops/spotlight-next-pressed.png)

#### Large CTA
The black Get started pill mid-page. Measured, never followed. Read as `cta-large` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106.66 x 42; padding 0px 16px; radius 16px; background #000000 `brand.900`; text Inter Variable 14/20 500, #ffffff `brand.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #404040 `brand.700` |
| focus-visible | shadow rgba(0, 0, 0, 0.2) 0px 0px 0px 2px; outline 1px auto #005fcc, offset 1px |
| pressed | size 103.46 x 40.74; background #404040 `brand.700`; transform scale(0.97) |

![Large CTA default](components/crops/cta-large-default.png) ![Large CTA hover](components/crops/cta-large-hover.png) ![Large CTA focus-visible](components/crops/cta-large-focus-visible.png) ![Large CTA pressed](components/crops/cta-large-pressed.png)

#### Secondary CTA
The outlined Talk to sales. Measured, never followed. Read as `cta-secondary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 130 x 42; padding 0px 16px; border 1px solid #e7e7e7 `brand.200`; radius 16px; background #ffffff `brand.white`; text Inter Variable 14/20 500, #000000 `brand.900`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #fafafa `brand.50` |
| focus-visible | shadow rgba(0, 0, 0, 0.2) 0px 0px 0px 2px; outline 1px auto #005fcc, offset 1px |
| pressed | size 126.1 x 40.74; background #fafafa `brand.50`; transform scale(0.97) |

![Secondary CTA default](components/crops/cta-secondary-default.png) ![Secondary CTA hover](components/crops/cta-secondary-hover.png) ![Secondary CTA focus-visible](components/crops/cta-secondary-focus-visible.png) ![Secondary CTA pressed](components/crops/cta-secondary-pressed.png)

### Pricing

The plan cards, plan CTAs, credit calculator radios and FAQ accordions.

#### Pricing title
Read as `pricing-title` on the pricing page.

**Values (default).** size 664 x 57.59; background transparent; text Inter Display 48/57.6 400, #000000 `brand.900`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Pro plan card
Read as `plan-card-pro` on the pricing page.

**Values (default).** size 437.33 x 522; padding 2px; radius 24px; background #f4f4f4 `brand.100`; text Inter Display 20/28 400, #000000 `brand.900`.

![Pro plan card default](components/crops/plan-card-pro-default.png)

#### Choose Pro button
The primary plan CTA. Measured, never followed. Read as `plan-cta-pro` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 385.33 x 42; padding 9px 12px; radius 12px; background #000000 `brand.900`; text Inter Variable 14/20 500, #ffffff `brand.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #404040 `brand.700` |
| focus-visible | shadow rgba(0, 0, 0, 0.2) 0px 0px 0px 2px; outline 1px auto #005fcc, offset 1px |
| pressed | size 373.77 x 40.74; background #404040 `brand.700`; transform scale(0.97) |

![Choose Pro button default](components/crops/plan-cta-pro-default.png) ![Choose Pro button hover](components/crops/plan-cta-pro-hover.png) ![Choose Pro button focus-visible](components/crops/plan-cta-pro-focus-visible.png) ![Choose Pro button pressed](components/crops/plan-cta-pro-pressed.png)

#### Choose Free button
The neutral plan CTA. Measured, never followed. Read as `plan-cta-neutral` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 385.33 x 42; padding 9px 12px; radius 12px; background #f4f4f4 `brand.100`; text Inter Variable 14/20 500, #000000 `brand.900`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #e7e7e7 `brand.200` |
| focus-visible | shadow rgba(0, 0, 0, 0.2) 0px 0px 0px 2px; outline 1px auto #005fcc, offset 1px |
| pressed | size 373.77 x 40.74; background #e7e7e7 `brand.200`; transform scale(0.97) |

![Choose Free button default](components/crops/plan-cta-neutral-default.png) ![Choose Free button hover](components/crops/plan-cta-neutral-hover.png) ![Choose Free button focus-visible](components/crops/plan-cta-neutral-focus-visible.png) ![Choose Free button pressed](components/crops/plan-cta-neutral-pressed.png)

#### Plan price
Read as `plan-price` on the pricing page.

**Values (default).** size 62.28 x 36; background transparent; text Inter Display 36/36 400, #000000 `brand.900`.

![Plan price default](components/crops/plan-price-default.png)

#### Credit calculator radio
A model option on the video cost calculator; the input is visually hidden, the label paints it. Read as `model-radio` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 168.66 x 32; padding 4px 6px 4px 12px; border 1px solid #e5e5e5; radius 12px; background #ffffff `brand.white`; text Inter Variable 14/20 400, #171717; transition background-color 0.15s ease |
| selected | background #f5f5f5 |

![Credit calculator radio default](components/crops/model-radio-default.png) ![Credit calculator radio selected](components/crops/model-radio-selected.png)

#### FAQ accordion button
Read as `faq-question` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 700 x 56; padding 16px 24px; radius 16px; background transparent; text Inter Variable 14/20 400, #171717; icon 20 x 20, #a3a3a3 |
| focus-visible | outline 2px solid #171717, offset -2px |

![FAQ accordion button default](components/crops/faq-question-default.png) ![FAQ accordion button hover](components/crops/faq-question-hover.png) ![FAQ accordion button focus-visible](components/crops/faq-question-focus-visible.png) ![FAQ accordion button pressed](components/crops/faq-question-pressed.png)

#### FAQ accordion, open
The same item after its own toggle; the crop is the whole .avfaq-item, question and answer. Read as `faq-open` on the pricing page.

**Values (opened).** size 700 x 56; padding 16px 24px; radius 16px; background transparent; text Inter Variable 14/20 400, #171717.

![FAQ accordion, open opened](components/crops/faq-open-opened.png)

#### Ask AI button
The icon pill that opens an AI answer for a FAQ. Measured, never pressed. Read as `ask-ai` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 12px; background #f4f4f4 `brand.100`; text Inter Variable 14/20 400, #0000ee; transition all 0.15s ease-in |
| hover | background #e7e7e7 `brand.200` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #e7e7e7 `brand.200`; text Inter Variable 14/20 400, #ff0000 |

![Ask AI button default](components/crops/ask-ai-default.png) ![Ask AI button hover](components/crops/ask-ai-hover.png) ![Ask AI button focus-visible](components/crops/ask-ai-focus-visible.png) ![Ask AI button pressed](components/crops/ask-ai-pressed.png)

### Interactive demo page

The product page's own nav pair, the url-to-demo pill field and feature cards.

#### Demo title
Read as `demo-title` on the interactive-demo page.

**Values (default).** size 342.28 x 116; padding 6px 6px 6px 0px; background transparent; text Inter Variable 48/52 600, #111827 `arcade.dark.default`.

![Demo title default](components/crops/demo-title-default.png)

#### Sign up for free
The page's nav CTA. Measured, never followed. Read as `demo-signup` on the interactive-demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 136.42 x 40; padding 10px 16px; radius 12px; background #2142e7 `primary.600`; shadow rgba(17, 24, 39, 0.04) 0px 32px 32px 0px, rgba(17, 24, 39, 0.04) 0px 16px 16px 0px, rgba(17, 24, 39, 0.04) 0px 8px 8px 0px, rgba(17, 24, 39, 0.04) 0px 4px 4px -2px, rgba(17, 24, 39, 0.04) 0px 2px 2px -1px, #182fa5 0px 0px 0px 1px; text Inter Variable 14/20 600, #ffffff `brand.white`; transition all 0.35s cubic-bezier(0.6, 0.6, 0, 1) |
| hover | background #4460ed `primary.500`; shadow rgba(17, 24, 39, 0) 0px 32px 32px 0px, rgba(17, 24, 39, 0) 0px 16px 16px 0px, rgba(17, 24, 39, 0.04) 0px 8px 8px -4px, rgba(17, 24, 39, 0.04) 0px 4px 4px -2px, rgba(17, 24, 39, 0.04) 0px 2px 2px -1px, #2142e7 0px 0px 0px 1px |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #4460ed `primary.500`; shadow rgba(17, 24, 39, 0) 0px 32px 32px 0px, rgba(17, 24, 39, 0) 0px 16px 16px 0px, rgba(17, 24, 39, 0.04) 0px 8px 8px -4px, rgba(17, 24, 39, 0.04) 0px 4px 4px -2px, rgba(17, 24, 39, 0.04) 0px 2px 2px -1px, #2142e7 0px 0px 0px 1px |

![Sign up for free default](components/crops/demo-signup-default.png) ![Sign up for free hover](components/crops/demo-signup-hover.png) ![Sign up for free focus-visible](components/crops/demo-signup-focus-visible.png) ![Sign up for free pressed](components/crops/demo-signup-pressed.png)

#### Talk to sales
The page's secondary nav CTA. Measured, never followed. Read as `demo-tts` on the interactive-demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 115.64 x 40; padding 10px 16px; radius 12px; background #ffffff `brand.white`; shadow rgba(17, 24, 39, 0.04) 0px 32px 32px 0px, rgba(17, 24, 39, 0.04) 0px 16px 16px 0px, rgba(17, 24, 39, 0.04) 0px 8px 8px 0px, rgba(17, 24, 39, 0.04) 0px 4px 4px -2px, rgba(17, 24, 39, 0.04) 0px 2px 2px -1px, rgba(17, 24, 39, 0.16) 0px 0px 0px 1px; text Inter Variable 14/20 600, #111827 `arcade.dark.default`; transition all 0.35s cubic-bezier(0.6, 0.6, 0, 1) |
| hover | background #f9fafb `card.bg.white`; shadow rgba(17, 24, 39, 0) 0px 32px 32px 0px, rgba(17, 24, 39, 0) 0px 16px 16px 0px, rgba(17, 24, 39, 0.04) 0px 8px 8px -4px, rgba(17, 24, 39, 0.04) 0px 4px 4px -2px, rgba(17, 24, 39, 0.04) 0px 2px 2px -1px, rgba(17, 24, 39, 0.16) 0px 0px 0px 1px |
| focus-visible | outline 1px auto #005fcc, offset 0.984375px |
| pressed | background #f9fafb `card.bg.white`; shadow rgba(17, 24, 39, 0) 0px 32px 32px 0px, rgba(17, 24, 39, 0) 0px 16px 16px 0px, rgba(17, 24, 39, 0.04) 0px 8px 8px -4px, rgba(17, 24, 39, 0.04) 0px 4px 4px -2px, rgba(17, 24, 39, 0.04) 0px 2px 2px -1px, rgba(17, 24, 39, 0.16) 0px 0px 0px 1px |

![Talk to sales default](components/crops/demo-tts-default.png) ![Talk to sales hover](components/crops/demo-tts-hover.png) ![Talk to sales focus-visible](components/crops/demo-tts-focus-visible.png) ![Talk to sales pressed](components/crops/demo-tts-pressed.png)

#### URL-to-demo field
Focused only; nothing was typed or submitted. Read as `url-field` on the interactive-demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 364.8 x 68.4; padding 0px 8px 0px 0px; background transparent; text Inter Variable 18/72 400, #111827 `arcade.dark.default`; placeholder #9ca3af |
| focused | size 384 x 72 |

![URL-to-demo field default](components/crops/url-field-default.png) ![URL-to-demo field focused](components/crops/url-field-focused.png)

#### URL-to-demo button
The field's arrow submit. Measured, never pressed. Read as `url-button` on the interactive-demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 34.2 x 34.2; radius 72px; background #2142e7 `primary.600`; shadow #182fa5 0px 0px 0px 1px, rgba(17, 24, 39, 0.04) 0px 2px 2px -2px, rgba(17, 24, 39, 0.04) 0px 4px 4px 0px, rgba(17, 24, 39, 0.04) 0px 8px 8px 0px, rgba(17, 24, 39, 0.04) 0px 16px 16px 0px, rgba(17, 24, 39, 0.04) 0px 32px 32px 0px; text Inter Variable 18/28 400, #111827 `arcade.dark.default`; transition all 0.2s cubic-bezier(0.16, 1, 0.3, 1); icon 19 x 19, #111827 `arcade.dark.default` |
| hover, focus-visible | size 36 x 36; background #4460ed `primary.500`; shadow #2142e7 0px 0px 0px 1px, rgba(17, 24, 39, 0.04) 0px 2px 2px -2px, rgba(17, 24, 39, 0.04) 0px 4px 4px 0px, rgba(17, 24, 39, 0.04) 0px 8px 8px 0px, rgba(17, 24, 39, 0.04) 0px 16px 16px 0px, rgba(17, 24, 39, 0.04) 0px 32px 32px 0px; icon 20 x 20, #111827 `arcade.dark.default` |
| pressed | background #4460ed `primary.500`; shadow #2142e7 0px 0px 0px 1px, rgba(17, 24, 39, 0.04) 0px 2px 2px -2px, rgba(17, 24, 39, 0.04) 0px 4px 4px 0px, rgba(17, 24, 39, 0.04) 0px 8px 8px 0px, rgba(17, 24, 39, 0.04) 0px 16px 16px 0px, rgba(17, 24, 39, 0.04) 0px 32px 32px 0px |

![URL-to-demo button default](components/crops/url-button-default.png) ![URL-to-demo button hover](components/crops/url-button-hover.png) ![URL-to-demo button focus-visible](components/crops/url-button-focus-visible.png) ![URL-to-demo button pressed](components/crops/url-button-pressed.png)

#### Feature card
Read as `demo-card` on the interactive-demo page.

**Values (default).** size 460 x 100; background transparent; text Inter Variable 32/36 500, #111827 `arcade.dark.default`.

![Feature card default](components/crops/demo-card-default.png)

#### Newsletter field
Focused only; nothing was typed or submitted. Read as `newsletter-field` on the interactive-demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 56; padding 0px 114px 0px 16px; border 1px solid #e5e7eb `neutral.200.default`; radius 16px; background #ffffff `brand.white`; text Inter Variable 14/14 400, #111827 `arcade.dark.default`; transition all 0.2s ease-out; placeholder #999999 |
| focused | border 1px solid #d1d5db `neutral.300` |

![Newsletter field default](components/crops/newsletter-field-default.png) ![Newsletter field focused](components/crops/newsletter-field-focused.png)

### Contact sales

The contact form's .ds-input fields and submit.

#### Contact title
Read as `contact-title` on the contact-sales page.

**Values (default).** size 544 x 115.19; background transparent; text Inter Display 48/57.6 400, #000000 `brand.900`.

![Contact title default](components/crops/contact-title-default.png)

#### Form card
Read as `form-card` on the contact-sales page.

**Values (default).** size 480 x 697; padding 8px; border 1px solid #e7e7e7 `brand.200`; radius 24px; background #ffffff `brand.white`; text Inter Variable 14/20 500, #000000 `brand.900`.

![Form card default](components/crops/form-card-default.png)

#### Text field
One .ds-input (First name). A sample value was typed, measured, then deleted; the form was never submitted. Read as `field-text` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 199 x 40; padding 0px 12px; border 1px solid #f4f4f4 `brand.100`; radius 12px; background #f4f4f4 `brand.100`; text Inter Variable 14/20 400, #404040 `brand.700`; transition background-color 0.15s ease, border-color 0.15s ease, color 0.15s ease; placeholder #a2a2a2 `brand.400` |
| focused, filled | border 1px solid #d4d4d4 `brand.300`; background #ffffff `brand.white`; text Inter Variable 14/20 400, #000000 `brand.900` |

![Text field default](components/crops/field-text-default.png) ![Text field focused](components/crops/field-text-focused.png) ![Text field filled](components/crops/field-text-filled.png)

#### Select
Company-size select; focused only, never changed. Read as `field-select` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 414 x 40; padding 0px 42px 0px 12px; border 1px solid #f4f4f4 `brand.100`; radius 12px; background #f4f4f4 `brand.100`; image an image (data URI); text Inter Variable 14/20 400, #404040 `brand.700`; transition background-color 0.15s ease, border-color 0.15s ease, color 0.15s ease |
| focused | border 1px solid #d4d4d4 `brand.300`; background #ffffff `brand.white`; image none; text Inter Variable 14/20 400, #000000 `brand.900` |

![Select default](components/crops/field-select-default.png) ![Select focused](components/crops/field-select-focused.png)

#### Textarea
Focused only; nothing was typed. Read as `field-textarea` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 414 x 96; padding 8px 12px; border 1px solid #f4f4f4 `brand.100`; radius 12px; background #f4f4f4 `brand.100`; text Inter Variable 14/20 400, #404040 `brand.700`; transition background-color 0.15s ease, border-color 0.15s ease, color 0.15s ease; placeholder #a2a2a2 `brand.400` |
| focused | border 1px solid #d4d4d4 `brand.300`; background #ffffff `brand.white`; text Inter Variable 14/20 400, #000000 `brand.900` |

![Textarea default](components/crops/field-textarea-default.png) ![Textarea focused](components/crops/field-textarea-focused.png)

#### Submit button
The Talk to sales submit. Measured, never pressed. Read as `form-submit` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 414 x 40; padding 0px 12px; radius 12px; background #000000 `brand.900`; text Inter Variable 14/20 500, #ffffff `brand.white`; transition background-color 0.15s ease |

![Submit button default](components/crops/form-submit-default.png) ![Submit button hover](components/crops/form-submit-hover.png) ![Submit button pressed](components/crops/form-submit-pressed.png)

### Footer

The link columns, socials and legal.

#### Footer
Read as `footer` on the home page.

**Values (default).** size 1440 x 670.09; padding 80px 0px 0px 0px; background #ffffff `brand.white`; shadow rgba(0, 0, 0, 0.12) 0px -1px 0px 0px; text Inter Display 24/28.8 400, #000000 `brand.900`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 62.94 x 17.5; background transparent; text Inter Variable 14/17.5 400, #717171 `brand.500`; transition all 0.15s ease-in |
| hover | text Inter Variable 14/17.5 400, #000000 `brand.900` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | text Inter Variable 14/17.5 400, #000000 `brand.900` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer social icon
Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 12px; background #f4f4f4 `brand.100`; text Inter Variable 14/17.5 400, #0000ee; transition all 0.15s ease-in |
| hover | background #e7e7e7 `brand.200` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #e7e7e7 `brand.200`; text Inter Variable 14/17.5 400, #ff0000 |

![Footer social icon default](components/crops/footer-social-default.png) ![Footer social icon hover](components/crops/footer-social-hover.png) ![Footer social icon focus-visible](components/crops/footer-social-focus-visible.png) ![Footer social icon pressed](components/crops/footer-social-pressed.png)

#### Legal link
Read as `footer-legal` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 92.58 x 17.5; background transparent; text Inter Variable 14/17.5 400, #717171 `brand.500`; transition all 0.15s ease-in |
| hover | text Inter Variable 14/17.5 400, #000000 `brand.900` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | text Inter Variable 14/17.5 400, #000000 `brand.900` |

![Legal link default](components/crops/footer-legal-default.png) ![Legal link hover](components/crops/footer-legal-hover.png) ![Legal link focus-visible](components/crops/footer-legal-focus-visible.png) ![Legal link pressed](components/crops/footer-legal-pressed.png)

### Mobile (390 wide)

The same surface at phone width, with the menu open.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 72; background rgba(255, 255, 255, 0); text Inter Variable 14/24 500, #000000 `brand.900`; transition background-color 0.15s ease-in; icon 98 x 26, #333333.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 66.03 x 32; padding 0px 14px; radius 12px; background transparent; text Inter Variable 14/24 500, #000000 `brand.900` |
| focus-visible | outline 2px solid #000000 `brand.900`, offset -2px |

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button hover](components/crops/m-menu-button-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The bar after its own toggle; the crop is the opened sheet (the nav panel's grandparent div) that holds the links and actions. Read as `m-menu-open` on the home page at 390 wide.

**Values (opened).** size 66.03 x 32; padding 0px 14px; radius 12px; background transparent; text Inter Variable 14/24 500, #000000 `brand.900`.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav link
Read inside the open menu. Read as `m-nav-link` on the home page at 390 wide.

**Values (default).** size 358 x 52; background transparent; text Inter Variable 24/26.4 400, #717171 `brand.500`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Mobile nav link default](components/crops/m-nav-link-default.png)

#### Mobile prompt box
Read as `m-prompt` on the home page at 390 wide.

**Values (default).** size 342 x 148; radius 16px; background #ffffff `brand.white`; shadow rgba(0, 0, 0, 0.03) 0px 16px 16px 0px, rgba(0, 0, 0, 0.03) 0px 8px 8px 0px, rgba(0, 0, 0, 0.03) 0px 4px 4px 0px, rgba(0, 0, 0, 0.03) 0px 2px 2px -2px, rgba(0, 0, 0, 0.12) 0px 0px 0px 1px; text Inter Variable 12/16 500, rgba(0, 0, 0, 0.6); icon 16 x 16, #000000 `brand.900`.

![Mobile prompt box default](components/crops/m-prompt-default.png)

#### Mobile Sign up
Read inside the open menu. Read as `m-signup` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 175 x 48; padding 14px 16px; radius 14px; background #000000 `brand.900`; text Inter Variable 15/20 500, #ffffff `brand.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #404040 `brand.700` |
| focus-visible | shadow rgba(0, 0, 0, 0.2) 0px 0px 0px 2px; outline 2px solid #000000 `brand.900`, offset 2px |
| pressed | background #404040 `brand.700` |

![Mobile Sign up default](components/crops/m-signup-default.png) ![Mobile Sign up hover](components/crops/m-signup-hover.png) ![Mobile Sign up focus-visible](components/crops/m-signup-focus-visible.png) ![Mobile Sign up pressed](components/crops/m-signup-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Arcade's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The app behind login.** Arcade's product (the demo editor, agents) sits behind sign-up/sign-in and was never reached; Log in, Sign up, Get started, Choose Pro/Free, Talk to sales and the url-to-demo and prompt submits were measured, never followed or pressed.
- **Anything that sends, submits or signs in.** No form was submitted, no prompt was sent, no account was created. The contact-sales .ds-input fields were focused and one sample value typed and deleted, never submitted.
- **The scatter cards' videos** play inside an overlay player that was not opened; the cards are measured as links, the video surface is not.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The site paints one light theme on every captured route: no dark class or attribute is bound, so the dark set is not emitted. The :root palette is recorded in [raw/css-vars.json](raw/css-vars.json).

### Fonts

- **The faces** are Inter Display (headings) and Inter Variable (UI), both self-hosted; Geist Mono Variable, Balig Script and Ptserif also ship. The style guide renders with system fallbacks.
- Illustration, video stills and wordmark artwork in the screenshots are Arcade's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The changelog page is 91,833 px tall; its -full shot is the whole page stitched from 7 tiles.

### Content left out

- Video stills, the animated scatter wall, customer logos and the wordmark are Arcade's content; only the frames and components were measured.
