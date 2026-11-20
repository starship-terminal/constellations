# Luma AI components

The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from lumalabs.ai on 2026-11-18, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or purchased.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (31 components, 71 states).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (71 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`. Inner pages are light. The home hero and /ray are dark. Desktop shots are 1440 x 900 at 1x. Phone shots are 390 x 844 at 2x, so the PNG is 780 wide.

| Surface | URL | Screenshots |
|---|---|---|
| Home. Dark video hero, Sign In, Try for free, prompt filled and cleared. | `https://lumalabs.ai/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [prompt-filled](screenshots/home-dark-prompt-filled.png) |
| Pricing. Monthly and Yearly, three plan cards. Start Now was not followed. | `https://lumalabs.ai/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [yearly](screenshots/pricing-light-yearly.png) |
| About. Editorial heading and company copy. | `https://lumalabs.ai/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| API. Use the API, Explore docs, Uni-1.1 tab. | `https://lumalabs.ai/api` | [default](screenshots/api-light-default.png), [full](screenshots/api-light-full.png), [uni](screenshots/api-light-uni.png) |
| Enterprise. Dark photograph hero. The form was not submitted. | `https://lumalabs.ai/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| Ray3.2. Dark cinematic page. | `https://lumalabs.ai/ray` | [default](screenshots/ray-dark-default.png), [full](screenshots/ray-dark-full.png) |
| Uni-1 product page. | `https://lumalabs.ai/uni-1` | [default](screenshots/uni-light-default.png), [full](screenshots/uni-light-full.png) |
| News index. Category filters and article cards. | `https://lumalabs.ai/news` | [default](screenshots/news-light-default.png) |
| MCP page. | `https://lumalabs.ai/mcp` | [default](screenshots/mcp-light-default.png), [full](screenshots/mcp-light-full.png) |
| Careers. | `https://lumalabs.ai/careers` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| Case studies. | `https://lumalabs.ai/case-studies` | [default](screenshots/cases-light-default.png), [full](screenshots/cases-light-full.png) |
| Learning center. | `https://lumalabs.ai/learning-center` | [default](screenshots/learning-light-default.png), [full](screenshots/learning-light-full.png) |
| AI video generator marketing page. | `https://lumalabs.ai/create/ai-video-generator` | [default](screenshots/create-light-default.png), [full](screenshots/create-light-full.png) |
| Dream Machine to Luma Agents. | `https://lumalabs.ai/models/luma-dream-machine-evolved-into-luma-agents` | [default](screenshots/agents-light-default.png), [full](screenshots/agents-light-full.png) |
| Terms of service. | `https://lumalabs.ai/legal/terms-of-service` | [default](screenshots/terms-light-default.png) |
| Docs hub (ReadMe). Sheets are not in the marketing tokens. | `https://docs.lumalabs.ai/docs/welcome` | [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png) |
| Home at 390, including the opened nav. Sign In was not followed. | `https://lumalabs.ai/` | [default](screenshots/mobile-home-dark-default.png), [nav](screenshots/mobile-home-dark-nav.png) |
| Pricing at 390. | `https://lumalabs.ai/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Ray at 390. | `https://lumalabs.ai/ray` | [default](screenshots/mobile-ray-dark-default.png) |
| News at 390. | `https://lumalabs.ai/news` | [default](screenshots/mobile-news-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Prompt filled | home | sample text typed, then deleted; Submit was not clicked | [home-dark-prompt-filled](screenshots/home-dark-prompt-filled.png) |
| Yearly interval | pricing | the Yearly button, a local toggle | [pricing-light-yearly](screenshots/pricing-light-yearly.png) |
| Phone nav | home at 390 | the menu button, a local toggle; Sign In was not followed | [mobile-home-dark-nav](screenshots/mobile-home-dark-nav.png) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 7 components were given a real keyboard focus. 7 draw a ring: `nav-product` (1px auto #005fcc, offset 4px), `nav-signin` (1px auto #005fcc, offset 4px), `hero-cta` (1px auto #005fcc, offset 4px), `idea-chip` (1px auto #005fcc, offset 4px), `price-cta` (1px auto #005fcc, offset 4px), `api-cta` (1px auto #005fcc, offset 4px), `api-docs` (1px auto #005fcc, offset 4px).

**Pressed.** Pressed on Sign In, Try for free, Start Now and Use the API was a forced :active:hover so the link was not followed. Monthly, Yearly and the news filter are local toggles.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, all, backdrop-filter, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | api-cta, api-docs, api-tab, ent-field, ent-submit, footer-link, hero-cta, idea-chip and more |

**Layout grid.** Not captured: `tools/capture/layout.mjs` was not run, so there is no `raw/layout.json`.

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Prompt field](#prompt-field) | 510 x 75.56 | - | - | transparent | none | 0 |
| [Sign In](#sign-in) | 69.41 x 32 | 1px solid transparent | 3.35544e+07px | #ffffff `light.surface.page` | none | 0px 12px |
| [Try for free](#try-for-free) | 155.39 x 48 | 1px solid transparent | 3.35544e+07px | #ffffff `light.surface.page` | none | 0px 32px |
| [News card](#news-card) | 253.52 x 58.8 | - | - | transparent | none | 0 |
| [Enterprise field](#enterprise-field) | 400 x 36 | 1px solid oklch(0.75 0 0) | 6px | transparent | rgba(0, 0, 0, 0.05) 0px 1px 2px 0px | 4px 10px |

## Components

### Marketing shell

The header shared by the public pages: a wordmark, uppercase nav labels, and a Sign In pill. Sign In was measured and never followed.

#### Nav link
The PRODUCT nav link. It points at /app, a marketing route, not the signed-in app. Uppercase Graphik label. Read as `nav-product` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 67.48 x 14; background transparent; text __graphik_7126cf 14/14 500, #ffffff `light.surface.page`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto #005fcc, offset 4px |

![Nav link default](components/crops/nav-product-default.png) ![Nav link hover](components/crops/nav-product-hover.png) ![Nav link focus-visible](components/crops/nav-product-focus-visible.png)

#### Sign In
The header Sign In pill. It links to app.lumalabs.ai, which redirects to the sign-up host. Measured, never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 69.41 x 32; padding 0px 12px; border 1px solid transparent; radius 3.35544e+07px; background #ffffff `light.surface.page`; text __graphik_7126cf 14/20 500, #000000 `light.surface.inverted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto #005fcc, offset 4px |
| pressed | background #d9d9d9 `dark.surface.inverted-subtle` |

![Sign In default](components/crops/nav-signin-default.png) ![Sign In hover](components/crops/nav-signin-hover.png) ![Sign In focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign In pressed](components/crops/nav-signin-pressed.png)

#### Footer link
A footer text link. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 42.88 x 18; background transparent; text __graphik_7126cf 14/24 400, #000000 `light.surface.inverted`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.7 |
| hover | opacity none |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png)

### Home

The dark video hero, the Try for free pill, and the prompt composer. The prompt was filled and cleared. Submit was not clicked.

#### Hero heading
The home hero heading. Read as `hero-h1` on the home page.

**Values (default).** size 576 x 124.78; background transparent; text __graphik_7126cf 52/62.4 500, #ffffff `light.surface.page`.

![Hero heading default](components/crops/hero-h1-default.png)

#### Try for free
The hero pill. Links to the app host. Measured, never followed. Following it is a sign-in. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 155.39 x 48; padding 0px 32px; border 1px solid transparent; radius 3.35544e+07px; background #ffffff `light.surface.page`; text __graphik_7126cf 18/28 500, #000000 `light.surface.inverted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #d9d9d9 `dark.surface.inverted-subtle` |
| focus-visible | outline 1px auto #005fcc, offset 4px |
| pressed | background #d9d9d9 `dark.surface.inverted-subtle` |

![Try for free default](components/crops/hero-cta-default.png) ![Try for free hover](components/crops/hero-cta-hover.png) ![Try for free focus-visible](components/crops/hero-cta-focus-visible.png) ![Try for free pressed](components/crops/hero-cta-pressed.png)

#### Prompt field
The home prompt. Sample text is typed and deleted. Submit is never pressed. Read as `prompt` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 510 x 75.56; background transparent; text __graphik_7126cf 18/25.2 400, #000000 `light.surface.inverted`; placeholder #000000 `light.surface.inverted` |

![Prompt field default](components/crops/prompt-default.png) ![Prompt field focused](components/crops/prompt-focused.png) ![Prompt field filled](components/crops/prompt-filled.png)

#### Submit prompt
The prompt submit control. Measured at rest and hover only. Never clicked, so no generation is started. Read as `prompt-submit` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; background transparent; text __graphik_7126cf 16/24 400, #ffffff `light.surface.page`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 44 x 44, #a6a6a6 `light.text.tertiary` |
| hover | opacity 0.7 |

![Submit prompt default](components/crops/prompt-submit-default.png) ![Submit prompt hover](components/crops/prompt-submit-hover.png)

#### Idea chip
A suggested-prompt chip. A local control. It was not used to submit a prompt. Read as `idea-chip` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 149.08 x 32; padding 0px 12px; border 1px solid transparent; radius 3.35544e+07px; background #ffffff `light.surface.page`; text __graphik_7126cf 14/20 500, #000000 `light.surface.inverted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #d9d9d9 `dark.surface.inverted-subtle` |
| focus-visible | outline 1px auto #005fcc, offset 4px |

![Idea chip default](components/crops/idea-chip-default.png) ![Idea chip hover](components/crops/idea-chip-hover.png) ![Idea chip focus-visible](components/crops/idea-chip-focus-visible.png)

### Pricing

A light page with a Monthly / Yearly toggle and three plan cards. Start Now was measured and never followed.

#### Pricing heading
Plans and Pricing heading. Read as `price-h1` on the pricing page.

**Values (default).** size 337.59 x 62.39; background transparent; text __graphik_7126cf 52/62.4 500, #000000 `light.surface.inverted`.

![Pricing heading default](components/crops/price-h1-default.png)

#### Monthly
The billing-interval button. A local toggle. Checkout is never opened. Read as `price-monthly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 131.14 x 50.39; padding 14px 36px; radius 3.35544e+07px; background transparent; text __graphik_7126cf 16/22.4 500, #ffffff `light.surface.page`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

Child layers that carry the look: div 131.1x50.4 background #000000 `light.surface.inverted` radius 3.35544e+07px.

![Monthly default](components/crops/price-monthly-default.png) ![Monthly hover](components/crops/price-monthly-hover.png) ![Monthly pressed](components/crops/price-monthly-pressed.png)

#### Yearly
The yearly interval button. A local toggle. Read as `price-yearly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 115.69 x 50.39; padding 14px 36px; radius 3.35544e+07px; background transparent; text __graphik_7126cf 16/22.4 500, #737373 `light.text.secondary`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text __graphik_7126cf 16/22.4 500, #000000 `light.surface.inverted` |

![Yearly default](components/crops/price-yearly-default.png) ![Yearly hover](components/crops/price-yearly-hover.png) ![Yearly pressed](components/crops/price-yearly-pressed.png)

#### Start Now
A plan CTA. Measured, never followed. Following it is a sign-in and a checkout. Read as `price-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 350 x 40; padding 0px 24px; border 1px solid transparent; radius 3.35544e+07px; background #ffffff `light.surface.page`; text __graphik_7126cf 16/24 500, #000000 `light.surface.inverted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f2f2f2 `light.surface.surface` |
| focus-visible | outline 1px auto #005fcc, offset 4px |
| pressed | background #f2f2f2 `light.surface.surface` |

![Start Now default](components/crops/price-cta-default.png) ![Start Now hover](components/crops/price-cta-hover.png) ![Start Now focus-visible](components/crops/price-cta-focus-visible.png) ![Start Now pressed](components/crops/price-cta-pressed.png)

#### Plan card
The Plus plan card. Cropped from the node whose text starts with Plus and whose box is card-sized. Read as `price-card` on the pricing page.

The computed values in the raw reading are the page `body`'s, not the plan card's: the capture's target was `body`, and only the crop was taken from the Plus card. They are left out here. Recapture needed (the pk-k recapture tracking issue, 2026-11 audit).

![Plan card default](components/crops/price-card-default.png)

#### FAQ row
A pricing FAQ button. A local toggle. Nothing is submitted. Read as `faq` on the pricing page.

Not on the page when it was captured.

### About

A light editorial page.

#### About heading
The about page heading. Read as `about-h1` on the about page.

**Values (default).** size 1024 x 287.97; background transparent; text __graphik_7126cf 48/57.6 500, #737373 `light.text.secondary`.

![About heading default](components/crops/about-h1-default.png)

#### About FAQ
An about FAQ button. A local toggle. Read as `about-faq` on the about page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 830 x 62.8; padding 16px 28px; background transparent; text __graphik_7126cf 22/30.8 500, #000000 `light.surface.inverted`; icon 28.28 x 28.28, #737373 `light.text.secondary` |
| hover | icon 28.28 x 28.28, #000000 `light.surface.inverted` |
| opened | icon 20 x 20, #000000 `light.surface.inverted` |

![About FAQ default](components/crops/about-faq-default.png) ![About FAQ hover](components/crops/about-faq-hover.png) ![About FAQ opened](components/crops/about-faq-opened.png)

### API

A light page with Use the API, Explore docs, and a model tab. Use the API was never followed.

#### API heading
Build with Luma APIs. Read as `api-h1` on the API page.

**Values (default).** size 464.42 x 62.39; background transparent; text __graphik_7126cf 52/62.4 500, #000000 `light.surface.inverted`.

![API heading default](components/crops/api-h1-default.png)

#### Use the API
The API CTA. Measured, never followed. Keys and billing sit behind sign-in. Read as `api-cta` on the API page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 97.81 x 32; padding 0px 12px; border 1px solid transparent; radius 3.35544e+07px; background #000000 `light.surface.inverted`; text __graphik_7126cf 14/20 500, #ffffff `light.surface.page`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #262626 `light.surface.inverted-subtle` |
| focus-visible | outline 1px auto #005fcc, offset 4px |
| pressed | background #262626 `light.surface.inverted-subtle` |

![Use the API default](components/crops/api-cta-default.png) ![Use the API hover](components/crops/api-cta-hover.png) ![Use the API focus-visible](components/crops/api-cta-focus-visible.png) ![Use the API pressed](components/crops/api-cta-pressed.png)

#### Model tab
A model switch on the API page. A local toggle. Read as `api-tab` on the API page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 94.64 x 40; padding 0px 24px; border 1px solid transparent; radius 3.35544e+07px; background #f2f2f2 `light.surface.surface`; text __graphik_7126cf 16/24 500, #000000 `light.surface.inverted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | background #ededed `light.surface.elevated` |

![Model tab default](components/crops/api-tab-default.png) ![Model tab hover](components/crops/api-tab-hover.png) ![Model tab pressed](components/crops/api-tab-pressed.png)

#### Explore docs
The docs link. Measured, never followed from this page. Docs were captured as their own route. Read as `api-docs` on the API page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 172.41 x 48; padding 0px 32px; border 1px solid transparent; radius 3.35544e+07px; background #f2f2f2 `light.surface.surface`; text __graphik_7126cf 18/28 500, #000000 `light.surface.inverted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #ededed `light.surface.elevated` |
| focus-visible | outline 1px auto #005fcc, offset 4px |

![Explore docs default](components/crops/api-docs-default.png) ![Explore docs hover](components/crops/api-docs-hover.png) ![Explore docs focus-visible](components/crops/api-docs-focus-visible.png)

### Ray

A dark cinematic page for Ray3.2.

#### Ray heading
The Ray3.2 page heading on the dark field. Read as `ray-h1` on the Ray page.

**Values (default).** size 767.06 x 62.39; background transparent; text __graphik_7126cf 52/62.4 500, #ffffff `light.surface.page`.

![Ray heading default](components/crops/ray-h1-default.png)

#### Ray FAQ
A Ray FAQ button. A local toggle. Read as `ray-faq` on the Ray page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 830 x 62.8; padding 16px 28px; background transparent; text __graphik_7126cf 22/30.8 500, #ffffff `light.surface.page`; icon 20 x 20, #8c8c8c `dark.text.secondary` |
| hover | icon 20 x 20, #ffffff `light.surface.page` |
| opened | icon 28.28 x 28.28, #ffffff `light.surface.page` |

![Ray FAQ default](components/crops/ray-faq-default.png) ![Ray FAQ hover](components/crops/ray-faq-hover.png) ![Ray FAQ opened](components/crops/ray-faq-opened.png)

### News

A light index with category filters and article cards. Subscribe was not clicked.

#### News heading
The news index heading. Read as `news-h1` on the news page.

**Values (default).** size 127.92 x 62.39; background transparent; text __graphik_7126cf 52/62.4 500, #000000 `light.surface.inverted`.

![News heading default](components/crops/news-h1-default.png)

#### News filter
A news category filter. A local toggle. Subscribe was not clicked. Read as `news-filter` on the news page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 107.78 x 40; padding 0px 24px; border 1px solid transparent; radius 3.35544e+07px; background #f2f2f2 `light.surface.surface`; text __graphik_7126cf 16/24 500, #000000 `light.surface.inverted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | background #ededed `light.surface.elevated` |

![News filter default](components/crops/news-filter-default.png) ![News filter hover](components/crops/news-filter-hover.png) ![News filter pressed](components/crops/news-filter-pressed.png)

#### News card
A published news card. A public article link. Read as `news-card` on the news page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 253.52 x 58.8; background transparent; text __graphik_7126cf 22/30.8 500, #000000 `light.surface.inverted` |

![News card default](components/crops/news-card-default.png) ![News card hover](components/crops/news-card-hover.png)

### Enterprise

A dark photograph hero and a sales form. The field was focused. Submit was never clicked.

#### Enterprise heading
The enterprise page heading. Read as `ent-h1` on the enterprise page.

**Values (default).** size 832 x 124.78; background transparent; text __graphik_7126cf 52/62.4 500, #ffffff `light.surface.page`.

![Enterprise heading default](components/crops/ent-h1-default.png)

#### Enterprise field
A field on the enterprise form. Focused only. Nothing is typed that would be submitted, and Submit is never clicked. Read as `ent-field` on the enterprise page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 36; padding 4px 10px; border 1px solid oklch(0.75 0 0); radius 6px; background transparent; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text __graphik_7126cf 14/20 400, #000000 `light.surface.inverted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #000000 `light.surface.inverted` |
| focused | border 1px solid oklch(0.708 0 0); shadow oklab(0.708 0 0 / 0.5) 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Enterprise field default](components/crops/ent-field-default.png) ![Enterprise field focused](components/crops/ent-field-focused.png)

#### Enterprise submit
The enterprise form submit. Measured at rest and hover. Never clicked, so no sales form is sent. Read as `ent-submit` on the enterprise page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 832 x 48; padding 0px 10px; border 1px solid transparent; radius 3.35544e+07px; background #000000 `light.surface.inverted`; text __graphik_7126cf 18/28 500, oklch(0.985 0 0); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0 0 0 / 0.8) |

![Enterprise submit default](components/crops/ent-submit-default.png) ![Enterprise submit hover](components/crops/ent-submit-hover.png)

### Phone (390 wide)

The home at 390: Sign In and a menu button that opens the nav. Sign In was not followed.

#### Phone menu
The mobile navigation toggle at 390px. A local control. Sign In inside it is not followed. Read as `m-menu` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 20 x 20; background transparent; text __graphik_7126cf 16/24 400, #ffffff `light.surface.page`; icon 20 x 20, #ffffff `light.surface.page` |

![Phone menu default](components/crops/m-menu-default.png) ![Phone menu hover](components/crops/m-menu-hover.png) ![Phone menu pressed](components/crops/m-menu-pressed.png) ![Phone menu opened](components/crops/m-menu-opened.png)

#### Phone heading
The home heading at 390px. Read as `m-h1` on the home page.

**Values (default).** size 390 x 76.78; background transparent; text __graphik_7126cf 32/38.4 500, #ffffff `light.surface.page`.

![Phone heading default](components/crops/m-h1-default.png)

#### Phone Sign In
Sign In at 390px. Measured, never followed. Read as `m-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 69.41 x 32; padding 0px 12px; border 1px solid transparent; radius 3.35544e+07px; background #ffffff `light.surface.page`; text __graphik_7126cf 14/20 500, #000000 `light.surface.inverted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

![Phone Sign In default](components/crops/m-signin-default.png) ![Phone Sign In hover](components/crops/m-signin-hover.png)

## Icons

No standalone SVG set was extracted. The wordmark and control glyphs are in the crops and screenshots. This is a layout gap.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **Signed-in app.** https://app.lumalabs.ai redirects to a WorkOS sign-up host. Generation, account, billing, API keys and checkout were not entered. Sign In, Try for free, Start Now and Use the API were measured and never followed.
- **Enterprise form.** The field was focused. Submit was hovered and never clicked, so no sales form was sent.
- **Public gallery.** There is no signed-out user gallery. Stills on /ray and the marketing pages are product demos.
- **404.** A missing path rendered a Vercel invalid-slug page, not a Luma 404. It was not kept.

### States

- **Pressed** on gated links was forced with DevTools, so a script that runs on mousedown was not observed.
- **Disabled, loading and error** states do not paint on the public pages.
- **Pricing FAQ** was not found as a stable button. About and Ray FAQ rows were measured.

### Themes

Two resolutions of the same marketing sheets are in tokens.json. Inner pages paint html.light. The home hero and /ray paint dark media, and html.dark resolves a black page with white text. There is no theme switch. Docs (docs.lumalabs.ai) is a ReadMe hub and its tokens are not folded in.

### Fonts

- **Graphik** is the computed body and h1 family, under a Next.js local-font class name. The file is not redistributed.
- **PP Editorial** is loaded on the page and was not the computed h1 family on this pass.

### Screenshots

- Generated stills and the home video are Luma's content and appear only inside screenshots and crops.
- The news index is very tall. The full-page news shot was dropped. The viewport shot was kept.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- No prompt was submitted and no account was created. The pages were read signed out.
