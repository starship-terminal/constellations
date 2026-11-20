# Endless components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from endless.app (what endless.io redirects to) on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. endless.app is one Next.js surface — marketing pages, ~70 free tools, the model catalog, social radar, /docs and /brand — over a single shadcn-style token layer (TikTok Sans + Geist Mono). Nothing was signed into, sent, generated, downloaded or submitted; the contact form and every tool's prompt field were never filled past a deleted sample; sign-in (clerk.endless.app) and sign-up (s.endless.app) were never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (74 components, 178 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (178 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

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

**Focus.** 31 components were given a real keyboard focus. 9 draw an outline ring: `logo` (2px solid #01bcff `color.brand.accent`, offset 2px), `faq-item` (2px solid #01bcff `color.brand.accent`, offset 2px), `model-card` (2px solid #01bcff `color.brand.accent`, offset 2px), `radar-row` (2px solid #01bcff `color.brand.accent`, offset 4px), `blog-card` (on a child: 1px solid rgba(0, 0, 0, 0.1) offset -1px), `docs-nav-item` (1px auto rgba(1, 188, 255, 0.5), offset 0px), `docs-search` (1px auto rgba(1, 188, 255, 0.5), offset 0px), `footer-link` (2px solid #01bcff `color.brand.accent`, offset 2px), `m-nav-item` (2px solid #01bcff `color.brand.accent`, offset -2px). 20 draw a focus ring as a shadow instead: `nav-industries`, `nav-signin`, `nav-cta`, `composer-send`, `mode-pill`, `prompt-chip`, `billing-toggle`, `plan-cta`, `send-btn`, `tool-generate`, `mode-tab`, `model-link`, `radar-copy`, `radar-why`, `brand-btn`, `blog-pill`, `mcp-copy`, `theme-toggle`, `cookie-btn`, `d-nav-cta`. The other 2 show no measured change: `nav-link`, `d-nav-link`.

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
| [Prompt composer](#prompt-composer) | 660 x 122 | - | 20px | #ffffff `color.tailwind.white` | rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 1px 2px -1px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px | 0 |
| [Plan card](#plan-card) | 273 x 612 | - | 16px | #ffffff `color.tailwind.white` | rgba(229, 229, 229, 0.6) 0px 0px 0px 1px | 24px |
| [Contact form](#contact-form) | 640 x 436 | - | - | transparent | none | 0 |
| [Tool panel](#tool-panel) | 504 x 114 | - | 20px | #ffffff `color.tailwind.white` | rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 1px 2px -1px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px | 0 |
| [Model card](#model-card) | 354.66 x 200 | - | 20px | transparent | #e5e5e5 0px 0px 0px 1px | 24px |
| [Post card](#post-card) | 269.33 x 347.88 | 1px solid rgba(229, 229, 229, 0.6) | 16px | #ffffff `color.tailwind.white` | none | 0 |
| [Logo block](#logo-block) | 436 x 208 | - | 20px | #ffffff `color.tailwind.white` | #e5e5e5 0px 0px 0px 1px inset | 0 |
| [Docs sidebar](#docs-sidebar) | 268 x 900 | R: 1px solid #e5e5e5 `light.warning.border` | - | #fcfcfc `light.background` | none | 0 |
| [Code block](#code-block) | 470.94 x 20 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The marketing chrome: the logo mark, flat nav links, Sign in and the dark Sign-up-for-free pill on the near-white field. The desktop header has no dropdown menu; the nav is plain links at every width it was captured.

#### Header
The sticky 56px marketing header: logo mark, flat nav links, Sign in and the Sign-up-for-free pill. Read as `header` on the home page.

**Values (default).** size 1440 x 56; border B: 1px solid transparent; background rgba(252, 252, 252, 0.9) `measured.header-veil`; text TikTok Sans 14/20 500, #0a0a0a `light.foreground`; transition background-color 0.15s cubic-bezier(0.22, 1, 0.36, 1), border-bottom-color 0.15s cubic-bezier(0.22, 1, 0.36, 1); icon 24 x 24, #0a0a0a `light.foreground`.

![Header default](components/crops/header-default.png)

#### Logo
The Endless mark anchor. Read as `logo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 109.39 x 32; padding 0px 8px 0px 4px; radius 8px; background transparent; text TikTok Sans 16/24 400, #0a0a0a `light.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #0a0a0a `light.foreground`; layers ::after transparent 0px none 1 |
| focus-visible | outline 2px solid #01bcff `color.brand.accent`, offset 2px; layers ::after transparent 0px none 1; a.relative.flex 109.4x32.0 2px solid #01bcff `color.brand.accent` offset 2px 8px |

![Logo default](components/crops/logo-default.png) ![Logo hover](components/crops/logo-hover.png) ![Logo focus-visible](components/crops/logo-focus-visible.png) ![Logo pressed](components/crops/logo-pressed.png)

#### Nav link — Industries
The Industries header link (a plain link, not a dropdown trigger). Read as `nav-industries` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101.77 x 32; padding 6px 10px; radius 8px; background transparent; text TikTok Sans 14/20 400, #6e6e6e `light.muted.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, #6e6e6e `light.muted.foreground`; layers ::after transparent 0px none 1 |
| hover | background #f5f5f5 `light.secondary.default`; text TikTok Sans 14/20 400, #0a0a0a `light.foreground`; icon 12 x 12, #0a0a0a `light.foreground` |
| focus-visible | shadow #01bcff 0px 0px 0px 2px; layers ::after transparent 0px none 1; a.group/navigation-menu-trigger.w-max 101.8x32.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #01bcff `color.brand.accent` 0px 0px 0px 2px, transparent 0px 0px 0px 0px 8px |
| pressed | background #f5f5f5 `light.secondary.default`; text TikTok Sans 14/20 400, #0a0a0a `light.foreground`; icon 12 x 12, #0a0a0a `light.foreground` |

![Nav link — Industries default](components/crops/nav-industries-default.png) ![Nav link — Industries hover](components/crops/nav-industries-hover.png) ![Nav link — Industries focus-visible](components/crops/nav-industries-focus-visible.png) ![Nav link — Industries pressed](components/crops/nav-industries-pressed.png)

#### Nav link
The plain Pricing header link. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 65.91 x 32; padding 6px 10px; radius 8px; background transparent; text TikTok Sans 14/20 400, #6e6e6e `light.muted.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::after transparent 0px none 1 |
| hover | background #f5f5f5 `light.secondary.default`; text TikTok Sans 14/20 400, #0a0a0a `light.foreground` |
| focus-visible | background #f5f5f5 `light.secondary.default` |
| pressed | background #f5f5f5 `light.secondary.default`; text TikTok Sans 14/20 400, #0a0a0a `light.foreground` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Sign-in button
The Sign-in control (goes to clerk.endless.app; measured, never followed). Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 80.06 x 32; padding 0px 16px; border 1px solid transparent; radius 8px; background transparent; text TikTok Sans 14/20 600, #6e6e6e `light.muted.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::before transparent 0px none 1 |
| hover | text TikTok Sans 14/20 600, #0a0a0a `light.foreground` |
| focus-visible | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 76.86 x 30.72; text TikTok Sans 14/20 600, #0a0a0a `light.foreground` |

![Sign-in button default](components/crops/nav-signin-default.png) ![Sign-in button hover](components/crops/nav-signin-hover.png) ![Sign-in button focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign-in button pressed](components/crops/nav-signin-pressed.png)

#### Sign-up CTA
The dark Sign-up-for-free pill (goes to s.endless.app; measured, never followed). Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 138.86 x 32; padding 0px 16px; border 1px solid transparent; radius 8px; background #0a0a0a `light.foreground`; text TikTok Sans 14/20 600, #fcfcfc `light.background`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::before transparent 0px none 1 |
| hover | background rgba(10, 10, 10, 0.9) |
| focus-visible | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 133.3 x 30.72; background rgba(10, 10, 10, 0.9) |

![Sign-up CTA default](components/crops/nav-cta-default.png) ![Sign-up CTA hover](components/crops/nav-cta-hover.png) ![Sign-up CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Sign-up CTA pressed](components/crops/nav-cta-pressed.png)

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

**Values (default).** size 504.11 x 127.88; background transparent; text TikTok Sans 59.2/63.93 500, #0a0a0a `light.foreground`; icon 35.17 x 35.17, #0a0a0a `light.foreground`; layers div.rounded-xl.bg-surface-control 135.2x88.5 #f5f5f5 `light.secondary.default` rgba(0, 0, 0, 0.05) 0px 1px 2px 0px, rgba(0, 0, 0, 0.15) 0px 8px 24px -12px 16px; div.overflow-hidden.rounded-lg 126.4x79.7 rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 1px 2px -1px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px 12px; div.home-sticker-frame.bg-surface-control 52.7x52.7 #f5f5f5 `light.secondary.def.

Child layers that carry the look: div 135.2x88.5 background #f5f5f5 `light.secondary.default` radius 16px shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px, rgba(0, 0, 0, 0.15) 0px 8px 24px -12px; div 126.4x79.7 radius 12px shadow rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 1px 2px -1px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; div 52.7x52.7 background #f5f5f5 `light.secondary.default` radius calc(22.5% + 2.2px) shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px, rgba(0, 0, 0, 0.15) 0px 8px 24px -12px.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede under the headline. Read as `hero-lede` on the home page.

**Values (default).** size 512 x 58.5; background transparent; text TikTok Sans 18/29.25 400, rgba(10, 10, 10, 0.75).

![Hero copy default](components/crops/hero-lede-default.png)

#### Prompt composer
The painted Ask-Endless prompt box (the hero's chat composer). Its send control is never pressed. Read as `composer` on the home page.

**Values (default).** size 660 x 122; radius 20px; background #ffffff `color.tailwind.white`; shadow rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 1px 2px -1px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; text TikTok Sans 14/20 500, #6e6e6e `light.muted.foreground`; icon 16 x 16, #6e6e6e `light.muted.foreground`.

![Prompt composer default](components/crops/composer-default.png)

#### Composer input
The "Ask Endless…" textarea; sample text was typed and deleted, nothing sent. Read as `composer-input` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 660 x 72; padding 16px 20px 4px 20px; background transparent; text TikTok Sans 16/24 400, #0a0a0a `light.foreground`; placeholder #6e6e6e `light.muted.foreground` |

![Composer input default](components/crops/composer-input-default.png) ![Composer input focused](components/crops/composer-input-focused.png) ![Composer input filled](components/crops/composer-input-filled.png)

#### Composer send
The send/generate control inside the composer; measured, never pressed. Read as `composer-send` on the home page.

**Wrong element.** These readings are the composer's "Add to prompt" attach button, not the send control: the selector's `form button` fallback matched it first. Recapture needed.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; border 1px solid transparent; radius 12px; background transparent; text TikTok Sans 14/20 500, #6e6e6e `light.muted.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #6e6e6e `light.muted.foreground` |
| hover | background #f5f5f5 `light.secondary.default`; text TikTok Sans 14/20 500, #0a0a0a `light.foreground`; icon 16 x 16, #0a0a0a `light.foreground` |
| focus-visible | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | background #f5f5f5 `light.secondary.default`; text TikTok Sans 14/20 500, #0a0a0a `light.foreground`; icon 16 x 16, #0a0a0a `light.foreground` |

![Composer send default](components/crops/composer-send-default.png) ![Composer send hover](components/crops/composer-send-hover.png) ![Composer send focus-visible](components/crops/composer-send-focus-visible.png) ![Composer send pressed](components/crops/composer-send-pressed.png)

#### Model pill
The model-picker pill on the composer ("GPT-6.1 Terra" on this pass). Read as `mode-pill` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 145.59 x 36; padding 0px 8px 0px 12px; border 1px solid transparent; radius 8px; background transparent; text TikTok Sans 14/20 500, #6e6e6e `light.muted.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #6e6e6e `light.muted.foreground`; layers ::before transparent 0px none 1 |
| hover | background #f5f5f5 `light.secondary.default`; text TikTok Sans 14/20 500, #0a0a0a `light.foreground`; icon 16 x 16, #0a0a0a `light.foreground` |
| focus-visible | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | background #f5f5f5 `light.secondary.default`; text TikTok Sans 14/20 500, #0a0a0a `light.foreground`; icon 16 x 16, #0a0a0a `light.foreground` |

![Model pill default](components/crops/mode-pill-default.png) ![Model pill hover](components/crops/mode-pill-hover.png) ![Model pill focus-visible](components/crops/mode-pill-focus-visible.png) ![Model pill pressed](components/crops/mode-pill-pressed.png)

#### Prompt chip
A suggestion chip under the composer; measured, never pressed. Read as `prompt-chip` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 156.05 x 36; padding 0px 10px; border 1px solid #e5e5e5 `light.warning.border`; radius 12px; background #ffffff `color.tailwind.white`; text TikTok Sans 14/20 500, #0a0a0a `light.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #6e6e6e `light.muted.foreground` |
| hover | background #f5f5f5 `light.secondary.default` |
| focus-visible | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 149.8 x 34.56; background #f5f5f5 `light.secondary.default`; icon 15.36 x 15.36, #6e6e6e `light.muted.foreground` |

![Prompt chip default](components/crops/prompt-chip-default.png) ![Prompt chip hover](components/crops/prompt-chip-hover.png) ![Prompt chip focus-visible](components/crops/prompt-chip-focus-visible.png) ![Prompt chip pressed](components/crops/prompt-chip-pressed.png)

### Home

Sections of the home page.

#### Section heading
A home section heading. Read as `h2-section` on the home page.

**Values (default).** size 672 x 40; background transparent; text TikTok Sans 36/40 500, #0a0a0a `light.foreground`.

![Section heading default](components/crops/h2-section-default.png)

### Pricing

The pricing surface: the Monthly/Annual billing segment, the shared-credits slider, the plan cards with their CTAs and the FAQ rows.

#### Pricing title
The pricing page heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 672 x 120; background transparent; text TikTok Sans 48/60 500, #0a0a0a `light.foreground`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Billing toggle
The Monthly/Annual billing segment; Annual was toggled for the screenshot state, never checked out. Read as `billing-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 96 x 32; radius 3.35544e+07px; background transparent; text TikTok Sans 14/20 500, #0a0a0a `light.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::after transparent 0px none 1 |
| focus-visible | shadow #fcfcfc 0px 0px 0px 2px, #01bcff 0px 0px 0px 4px; layers ::after transparent 0px none 1; button.relative.after:absolute 96.0x32.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #fcfcfc `light.background` 0px 0px 0px 2px, #01bcff `color.brand.accent` 0px 0px 0px 4px, transparent 0px 0px 0px 0px 3.35544e+07px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Plan name
A plan card's name. Read as `plan-name` on the pricing page.

**Values (default).** size 225 x 28; background transparent; text TikTok Sans 18/28 600, #0a0a0a `light.foreground`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Plan price
A plan card's price figure. Read as `plan-price` on the pricing page.

**Values (default).** size 225 x 66; background transparent; text TikTok Sans 36/40 600, #0a0a0a `light.foreground`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Plan CTA
A plan card's action; measured never followed (sign-up goes to s.endless.app). Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 225 x 52; padding 12px 28px; border 1px solid transparent; radius 12px; background #fcfcfc `light.background`; shadow rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 1px 2px -1px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; text TikTok Sans 16/26 600, #0a0a0a `light.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) |
| hover | background #f5f5f5 `light.secondary.default` |
| focus-visible | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 216 x 49.92; background #f5f5f5 `light.secondary.default` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Plan card
A pricing plan card (the painted ancestor of the plan name). Read as `plan-card` on the pricing page.

**Values (default).** size 273 x 612; padding 24px; radius 16px; background #ffffff `color.tailwind.white`; shadow rgba(229, 229, 229, 0.6) 0px 0px 0px 1px; text TikTok Sans 18/28 600, #0a0a0a `light.foreground`; icon 16 x 16, #6e6e6e `light.muted.foreground`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Credits slider
The shared-credits range input on /pricing; focused only, never dragged. Read as `credits-slider` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 18 x 18; background transparent; text TikTok Sans 16/24 400, #0a0a0a `light.foreground`; placeholder #0a0a0a `light.foreground` |
| focused | outline 1px auto rgba(1, 188, 255, 0.5), offset 0px; layers input 18.0x18.0 1px auto rgba(1, 188, 255, 0.5) offset 0px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### FAQ row
A pricing FAQ accordion row; measured closed, never opened. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1152 x 64; padding 20px 0px; radius 8px; background transparent; text TikTok Sans 16/24 500, #0a0a0a `light.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #6e6e6e `light.muted.foreground` |
| focus-visible | outline 2px solid #01bcff `color.brand.accent`, offset 2px; layers summary.flex.w-full 1152.0x64.0 2px solid #01bcff `color.brand.accent` offset 2px 8px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Contact form

The contact/sales form, measured but never submitted: text, email and company inputs, the message textarea and the Send-message button.

#### Contact form
The contact/sales form (an unpainted 640px column; the fields paint their own fills); never submitted. Read as `contact-form` on the contact page.

**Values (default).** size 640 x 436; background transparent; text TikTok Sans 14/20 500, #0a0a0a `light.foreground`; layers input.w-full.min-w-0 640.0x40.0 rgba(229, 229, 229, 0.5) `measured.field-fill` T:1px transparent / R:1px transparent / B:1px transparent / L:1px transparent 8px; input.w-full.min-w-0 640.0x40.0 rgba(229, 229, 229, 0.5) `measured.field-fill` T:1px transparent / R:1px transparent / B:1px transparent / L:1px transparent 8px; input.w-full.min-w-0 640.0x40.0 rgba(229, 229, 229, 0.5) `measured.field-fil.

Child layers that carry the look: input 640x40 background rgba(229, 229, 229, 0.5) `measured.field-fill` border 1px transparent radius 8px; input 640x40 background rgba(229, 229, 229, 0.5) `measured.field-fill` border 1px transparent radius 8px; input 640x40 background rgba(229, 229, 229, 0.5) `measured.field-fill` border 1px transparent radius 8px.

![Contact form default](components/crops/contact-form-default.png)

#### Name field
A text input on the contact form; sample text typed and deleted, nothing sent. Read as `field-name` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 640 x 40; padding 4px 12px; border 1px solid transparent; radius 8px; background rgba(229, 229, 229, 0.5) `measured.field-fill`; text TikTok Sans 14/20 400, #0a0a0a `light.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); placeholder #0a0a0a `light.foreground` |
| focused, filled | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |

![Name field default](components/crops/field-name-default.png) ![Name field focused](components/crops/field-name-focused.png) ![Name field filled](components/crops/field-name-filled.png)

#### Email field
The email input; sample text typed and deleted, nothing sent. Read as `field-email` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 640 x 40; padding 4px 12px; border 1px solid transparent; radius 8px; background rgba(229, 229, 229, 0.5) `measured.field-fill`; text TikTok Sans 14/20 400, #0a0a0a `light.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); placeholder #0a0a0a `light.foreground` |
| focused, filled | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |

![Email field default](components/crops/field-email-default.png) ![Email field focused](components/crops/field-email-focused.png) ![Email field filled](components/crops/field-email-filled.png)

#### Company field
The company/domain input ("acme.com" placeholder); focused only. Read as `field-company` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 640 x 40; padding 4px 12px; border 1px solid transparent; radius 8px; background rgba(229, 229, 229, 0.5) `measured.field-fill`; text TikTok Sans 14/20 400, #0a0a0a `light.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); placeholder #6e6e6e `light.muted.foreground` |
| focused | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |

![Company field default](components/crops/field-company-default.png) ![Company field focused](components/crops/field-company-focused.png)

#### Message field
The message textarea; focused only, nothing typed. Read as `field-message` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 640 x 64; padding 12px; border 1px solid transparent; radius 8px; background rgba(229, 229, 229, 0.5) `measured.field-fill`; text TikTok Sans 14/20 400, #0a0a0a `light.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #0a0a0a `light.foreground` |
| focused | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |

![Message field default](components/crops/field-message-default.png) ![Message field focused](components/crops/field-message-focused.png)

#### Send button
The Send-message submit; measured, never pressed. Read as `send-btn` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 640 x 52; padding 12px 28px; border 1px solid transparent; radius 12px; background #0a0a0a `light.foreground`; text TikTok Sans 16/26 600, #fcfcfc `light.background`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) |
| hover | background rgba(10, 10, 10, 0.9) |
| focus-visible | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 614.4 x 49.92; background rgba(10, 10, 10, 0.9) |

![Send button default](components/crops/send-btn-default.png) ![Send button hover](components/crops/send-btn-hover.png) ![Send button focus-visible](components/crops/send-btn-focus-visible.png) ![Send button pressed](components/crops/send-btn-pressed.png)

### AI image generator (free tool)

One of the ~70 free tool pages: the prompt field and the Generate-the-image submit — measured, never run.

#### Tool title
The free-tool page heading (AI image generator). Read as `tool-title` on the AI image generator page.

**Values (default).** size 392.23 x 60; background transparent; text TikTok Sans 48/60 500, #0a0a0a `light.foreground`.

![Tool title default](components/crops/tool-title-default.png)

#### Tool panel
The prompt panel of the free tool; Generate is never pressed. Read as `tool-panel` on the AI image generator page.

**Values (default).** size 504 x 114; radius 20px; background #ffffff `color.tailwind.white`; shadow rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 1px 2px -1px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; text TikTok Sans 14/21 500, #fcfcfc `light.background`; icon 16 x 16, #fcfcfc `light.background`.

![Tool panel default](components/crops/tool-panel-default.png)

#### Prompt field
The tool's prompt input ("e.g. a fox reading a map…" placeholder); sample text typed and deleted, nothing generated. Read as `tool-prompt` on the AI image generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 504 x 64; padding 16px 20px 24px 20px; background transparent; text TikTok Sans 16/24 400, #0a0a0a `light.foreground`; placeholder #6e6e6e `light.muted.foreground` |

![Prompt field default](components/crops/tool-prompt-default.png) ![Prompt field focused](components/crops/tool-prompt-focused.png) ![Prompt field filled](components/crops/tool-prompt-filled.png)

#### Generate button
The Generate-the-image submit; measured, never pressed. Read as `tool-generate` on the AI image generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 177.55 x 36; padding 0px 12px 0px 10px; border 1px solid transparent; radius 12px; background #0a0a0a `light.foreground`; text TikTok Sans 14/21 500, #fcfcfc `light.background`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #fcfcfc `light.background` |
| hover | background rgba(10, 10, 10, 0.9) |
| focus-visible | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 170.44 x 34.56; background rgba(10, 10, 10, 0.9); icon 15.36 x 15.36, #fcfcfc `light.background` |

![Generate button default](components/crops/tool-generate-default.png) ![Generate button hover](components/crops/tool-generate-hover.png) ![Generate button focus-visible](components/crops/tool-generate-focus-visible.png) ![Generate button pressed](components/crops/tool-generate-pressed.png)

#### How-it-works heading
A how-it-works heading on the tool page. Read as `tool-step` on the AI image generator page.

**Values (default).** size 672 x 40; background transparent; text TikTok Sans 36/40 500, #0a0a0a `light.foreground`.

![How-it-works heading default](components/crops/tool-step-default.png)

### Model catalog

The /models grid: search, the modality tabs and the model cards.

#### Models title
The model catalog heading. Read as `models-title` on the models page.

**Values (default).** size 636.8 x 120; background transparent; text TikTok Sans 48/60 500, #0a0a0a `light.foreground`.

![Models title default](components/crops/models-title-default.png)

#### Search field
The catalog search input; sample text typed and deleted. Read as `models-search` on the models page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 256 x 32; padding 4px 32px; border 1px solid #e5e5e5 `light.warning.border`; radius 12px; background #fcfcfc `light.background`; text TikTok Sans 14/20 400, #0a0a0a `light.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); placeholder #6e6e6e `light.muted.foreground` |
| focused, filled | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |

![Search field default](components/crops/models-search-default.png) ![Search field focused](components/crops/models-search-focused.png) ![Search field filled](components/crops/models-search-filled.png)

#### Modality tab
A modality filter pill ("All · 65", "Chat · 21", …); measured, never toggled. Read as `mode-tab` on the models page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 74.23 x 32; padding 6px 14px; radius 3.35544e+07px; background #0a0a0a `light.foreground`; text TikTok Sans 14/20 500, #fcfcfc `light.background`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::after transparent 0px none 1 |
| focus-visible | shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 71.27 x 30.72 |

![Modality tab default](components/crops/mode-tab-default.png) ![Modality tab hover](components/crops/mode-tab-hover.png) ![Modality tab focus-visible](components/crops/mode-tab-focus-visible.png) ![Modality tab pressed](components/crops/mode-tab-pressed.png)

#### Model card
A model tile in the catalog grid (the anchor is the card; 354x200, rounded 20px); measured, never followed. Read as `model-card` on the models page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 354.66 x 200; padding 24px; radius 20px; background transparent; shadow #e5e5e5 0px 0px 0px 1px; text TikTok Sans 18/28 500, #0a0a0a `light.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #0a0a0a `light.foreground`; layers a.group.flex 354.7x200.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #e5e5e5 `light.warning.border` 0px 0px 0px 1px, transparent 0px 0px 0px 0px 20px |
| hover | background rgba(245, 245, 245, 0.5); layers none |
| focus-visible | outline 2px solid #01bcff `color.brand.accent`, offset 2px; layers a.group.flex 354.7x200.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #e5e5e5 `light.warning.border` 0px 0px 0px 1px, transparent 0px 0px 0px 0px 2px solid #01bcff `color.brand.accent` offset 2px 20px |
| pressed | background rgba(245, 245, 245, 0.5); layers none |

![Model card default](components/crops/model-card-default.png) ![Model card hover](components/crops/model-card-hover.png) ![Model card focus-visible](components/crops/model-card-focus-visible.png) ![Model card pressed](components/crops/model-card-pressed.png)

#### Model link
A model name link in the catalog; measured, never followed. Read as `model-link` on the models page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 86.81 x 32; padding 6px 14px; radius 3.35544e+07px; background #f5f5f5 `light.secondary.default`; text TikTok Sans 14/20 500, #6e6e6e `light.muted.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::after transparent 0px none 1 |
| hover | text TikTok Sans 14/20 500, #0a0a0a `light.foreground` |
| focus-visible | shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 83.34 x 30.72; text TikTok Sans 14/20 500, #0a0a0a `light.foreground` |

![Model link default](components/crops/model-link-default.png) ![Model link hover](components/crops/model-link-hover.png) ![Model link focus-visible](components/crops/model-link-focus-visible.png) ![Model link pressed](components/crops/model-link-pressed.png)

### Radar trends

The social radar: live trend rows, Copy buttons and Find-out-why actions.

#### Radar title
The social radar heading. Read as `radar-title` on the radar page.

**Values (default).** size 512 x 180; background transparent; text TikTok Sans 48/60 500, #0a0a0a `light.foreground`.

![Radar title default](components/crops/radar-title-default.png)

#### Radar search
No search input exists on /radar — recorded missing. Read as `radar-search` on the radar page.

Not on the page when it was captured.

#### Trend row
A trend row in the live radar list (a link to a trend detail page); measured, never followed. Read as `radar-row` on the radar page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 184.81 x 44; radius 8px; background transparent; text TikTok Sans 14/20 500, #0a0a0a `light.foreground`; icon 16 x 16, #0a0a0a `light.foreground` |
| focus-visible | outline 2px solid #01bcff `color.brand.accent`, offset 4px; layers a.mt-8.inline-flex 184.8x44.0 2px solid #01bcff `color.brand.accent` offset 4px 8px |

![Trend row default](components/crops/radar-row-default.png) ![Trend row hover](components/crops/radar-row-hover.png) ![Trend row focus-visible](components/crops/radar-row-focus-visible.png) ![Trend row pressed](components/crops/radar-row-pressed.png)

#### Copy button
A trend Copy button; measured, never pressed. Read as `radar-copy` on the radar page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73.06 x 32; padding 0px 8px; border 1px solid transparent; radius 8px; background #171717 `light.primary.default`; text TikTok Sans 14/20 500, #fafafa `light.primary.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #fafafa `light.primary.foreground`; layers ::before transparent 0px none 1 |
| hover | background rgba(23, 23, 23, 0.8) |
| focus-visible | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 70.14 x 30.72; background rgba(23, 23, 23, 0.8); icon 15.36 x 15.36, #fafafa `light.primary.foreground` |

![Copy button default](components/crops/radar-copy-default.png) ![Copy button hover](components/crops/radar-copy-hover.png) ![Copy button focus-visible](components/crops/radar-copy-focus-visible.png) ![Copy button pressed](components/crops/radar-copy-pressed.png)

#### Why link
A trend's Find-out-why action; measured, never followed. Read as `radar-why` on the radar page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 87.94 x 32; border 1px solid transparent; radius 8px; background transparent; text TikTok Sans 14/20 600, #6e6e6e `light.muted.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) |
| hover | text TikTok Sans 14/20 600, #0a0a0a `light.foreground` |
| focus-visible | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 84.42 x 30.72; text TikTok Sans 14/20 600, #0a0a0a `light.foreground` |

![Why link default](components/crops/radar-why-default.png) ![Why link hover](components/crops/radar-why-hover.png) ![Why link focus-visible](components/crops/radar-why-focus-visible.png) ![Why link pressed](components/crops/radar-why-pressed.png)

### Brand kit

The /brand asset page: logo blocks, swatches and the Copy/Download buttons — measured, never downloaded.

#### Brand title
The brand-kit heading. Read as `brand-title` on the brand page.

**Values (default).** size 672 x 60; background transparent; text TikTok Sans 48/60 500, #0a0a0a `light.foreground`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Logo block
A logo asset card on the brand page (a rounded-2xl bg-card tile with On-light/On-dark variants and SVG/PNG download links). Read as `brand-logo-block` on the brand page.

**Values (default).** size 436 x 208; radius 20px; background #ffffff `color.tailwind.white`; shadow #e5e5e5 0px 0px 0px 1px inset; text TikTok Sans 12/16 500, #6e6e6e `light.muted.foreground`; icon 44 x 44, #0a0a0a `light.foreground`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Colour swatch
A brand colour swatch tile in the Colors section (285x174; the page names #0A0A0A, #FAFAFA, #01BCFF). Read as `brand-swatch` on the brand page.

**Values (default).** size 285.33 x 174; radius 20px; background #ffffff `color.tailwind.white`; shadow #e5e5e5 0px 0px 0px 1px inset; text TikTok Sans 16/24 500, #0a0a0a `light.foreground`; transition box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Asset button
An asset Download link; measured, never pressed. Read as `brand-btn` on the brand page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 180.45 x 40; padding 0px 12px; border 1px solid transparent; radius 12px; background #171717 `light.primary.default`; text TikTok Sans 14/20 500, #fafafa `light.primary.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #fafafa `light.primary.foreground` |
| hover | background rgba(23, 23, 23, 0.8) |
| focus-visible | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 173.23 x 38.4; background rgba(23, 23, 23, 0.8); icon 15.36 x 15.36, #fafafa `light.primary.foreground` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Docs shell

/docs is a separate documentation shell with its own sidebar and Search button, inside the same token layer.

#### Docs sidebar
The docs navigation sidebar — a separate shell from the marketing pages. Read as `docs-sidebar` on the docs page.

**Values (default).** size 268 x 900; border R: 1px solid #e5e5e5 `light.warning.border`; background #fcfcfc `light.background`; text TikTok Sans 14/20 400, #555555 `light.sidebar.foreground.muted`; transition all 0.25s ease; icon 24 x 24, #0a0a0a `light.foreground`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Docs nav item
A sidebar section button in the docs shell; measured, never toggled. Read as `docs-nav-item` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 236 x 36; padding 8px; radius 12px; background transparent; text TikTok Sans 14/20 400, #181818 `light.sidebar.foreground.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #181818 `light.sidebar.foreground.default` |
| hover | background rgba(240, 240, 240, 0.5); transition none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto rgba(1, 188, 255, 0.5), offset 0px; layers button.relative.flex 236.0x36.0 1px auto rgba(1, 188, 255, 0.5) offset 0px 12px |
| pressed | background rgba(240, 240, 240, 0.5); transition none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Search button
The docs Search (⌘K) button; measured, never opened. Read as `docs-search` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 236 x 36; padding 6px 6px 6px 8px; border 1px solid #e5e5e5 `light.warning.border`; radius 12px; background rgba(240, 240, 240, 0.5); text TikTok Sans 14/20 400, #555555 `light.sidebar.foreground.muted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #555555 `light.sidebar.foreground.muted` |
| hover | background #f0f0f0 `light.sidebar.accent.default`; text TikTok Sans 14/20 400, #181818 `light.sidebar.foreground.default`; icon 16 x 16, #181818 `light.sidebar.foreground.default` |
| focus-visible | outline 1px auto rgba(1, 188, 255, 0.5), offset 0px |
| pressed | background #f0f0f0 `light.sidebar.accent.default`; text TikTok Sans 14/20 400, #181818 `light.sidebar.foreground.default`; icon 16 x 16, #181818 `light.sidebar.foreground.default` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Docs heading
The docs page heading in the docs typeset. Read as `docs-h1` on the docs page.

**Values (default).** size 836 x 42; background transparent; text TikTok Sans 28/42 600, #0a0a0a `light.foreground`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### MCP page

The /mcp page: install code blocks and their Copy buttons.

#### MCP title
The MCP page heading. Read as `mcp-title` on the MCP page.

**Values (default).** size 768 x 120; background transparent; text TikTok Sans 48/60 500, #0a0a0a `light.foreground`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Code block
An install/config code block (monospace surface). Read as `mcp-code` on the MCP page.

**Values (default).** size 470.94 x 20; background transparent; text Geist Mono 14/20 400, #0a0a0a `light.foreground`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Copy button
A code Copy button; measured, never pressed. Read as `mcp-copy` on the MCP page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73.06 x 32; padding 0px 8px; border 1px solid transparent; radius 8px; background #171717 `light.primary.default`; text TikTok Sans 14/20 500, #fafafa `light.primary.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #fafafa `light.primary.foreground`; layers ::before transparent 0px none 1 |
| hover | background rgba(23, 23, 23, 0.8) |
| focus-visible | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 70.14 x 30.72; background rgba(23, 23, 23, 0.8); icon 15.36 x 15.36, #fafafa `light.primary.foreground` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Blog

The /blog index: category pills and post cards.

#### Blog title
The blog index heading. Read as `blog-title` on the blog page.

**Values (default).** size 768 x 120; background transparent; text TikTok Sans 48/60 500, #0a0a0a `light.foreground`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Category pill
A blog category filter pill; measured, never toggled. Read as `blog-pill` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 44.98 x 32; padding 6px 14px; radius 3.35544e+07px; background #0a0a0a `light.foreground`; text TikTok Sans 14/20 500, #fcfcfc `light.background`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::after transparent 0px none 1 |
| focus-visible | shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 43.18 x 30.72 |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Post card
A post card in the blog index; measured, never followed. Read as `blog-card` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 269.33 x 347.88; border 1px solid rgba(229, 229, 229, 0.6); radius 16px; background #ffffff `color.tailwind.white`; text TikTok Sans 11/16 500, #6e6e6e `light.muted.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #e5e5e5 `light.warning.border` |
| focus-visible | border 1px solid #e5e5e5 `light.warning.border`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | border 1px solid #e5e5e5 `light.warning.border` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Footer

The marketing footer: link columns, legal, and the Cookie-settings and Theme controls.

#### Footer
The marketing footer: link columns, legal, the Cookie-settings and Theme controls. Read as `footer` on the home page.

**Values (default).** size 1440 x 1452.36; border T: 1px solid rgba(229, 229, 229, 0.6); background #fcfcfc `light.background`; text TikTok Sans 14/20 400, #6e6e6e `light.muted.foreground`; icon 16 x 16, #6e6e6e `light.muted.foreground`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44.55 x 24; padding 2px 0px; radius 4px; background transparent; text TikTok Sans 14/20 400, rgba(10, 10, 10, 0.8); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text TikTok Sans 14/20 400, #0a0a0a `light.foreground` |
| focus-visible | outline 2px solid #01bcff `color.brand.accent`, offset 2px; text TikTok Sans 14/20 400, #0a0a0a `light.foreground`; layers a.inline-flex.items-center 44.5x24.0 2px solid #01bcff `color.brand.accent` offset 2px 4px |
| pressed | text TikTok Sans 14/20 400, #0a0a0a `light.foreground` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Theme toggle
The footer Theme icon control ("Theme: system. Switch to light"; writes the .dark class the system scheme also drives); measured, never pressed. Read as `theme-toggle` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; border 1px solid transparent; radius 8px; background transparent; text TikTok Sans 14/20 500, #6e6e6e `light.muted.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #6e6e6e `light.muted.foreground`; layers ::before transparent 0px none 1 |
| hover | background #f5f5f5 `light.secondary.default`; text TikTok Sans 14/20 500, #0a0a0a `light.foreground`; icon 16 x 16, #0a0a0a `light.foreground` |
| focus-visible | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 30.72 x 30.72; background #f5f5f5 `light.secondary.default`; text TikTok Sans 14/20 500, #0a0a0a `light.foreground`; icon 15.36 x 15.36, #0a0a0a `light.foreground` |

![Theme toggle default](components/crops/theme-toggle-default.png) ![Theme toggle hover](components/crops/theme-toggle-hover.png) ![Theme toggle focus-visible](components/crops/theme-toggle-focus-visible.png) ![Theme toggle pressed](components/crops/theme-toggle-pressed.png)

#### Cookie settings button
The footer Cookie-settings button; measured, never pressed (a consent surface). Read as `cookie-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 102.64 x 24; padding 2px 0px; radius 4px; background transparent; text TikTok Sans 14/20 400, rgba(10, 10, 10, 0.8); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text TikTok Sans 14/20 400, #0a0a0a `light.foreground` |
| focus-visible | shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px; text TikTok Sans 14/20 400, #0a0a0a `light.foreground`; layers button.inline-flex.items-center 102.6x24.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(1, 188, 255, 0.3) 0px 0px 0px 3px, transparent 0px 0px 0px 0px 4px |
| pressed | text TikTok Sans 14/20 400, #0a0a0a `light.foreground` |

![Cookie settings button default](components/crops/cookie-btn-default.png) ![Cookie settings button hover](components/crops/cookie-btn-hover.png) ![Cookie settings button focus-visible](components/crops/cookie-btn-focus-visible.png) ![Cookie settings button pressed](components/crops/cookie-btn-pressed.png)

### Dark theme (system dark)

The same home chrome re-measured under emulated prefers-color-scheme dark — the trigger next-themes honours, so these are the values a dark-system visitor gets.

#### Header (dark)
The sticky header painted by the dark token scope. Read as `d-header` on the home page.

**Values (default).** size 1440 x 56; border B: 1px solid transparent; background rgba(0, 0, 0, 0.9); text TikTok Sans 14/20 500, #fafafa `dark.foreground`; transition background-color 0.15s cubic-bezier(0.22, 1, 0.36, 1), border-bottom-color 0.15s cubic-bezier(0.22, 1, 0.36, 1); icon 24 x 24, #fafafa `dark.foreground`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Sign-up CTA (dark)
The sign-up pill under .dark. Read as `d-nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 138.86 x 32; padding 0px 16px; border 1px solid transparent; radius 8px; background #fafafa `dark.foreground`; text TikTok Sans 14/20 600, #000000 `color.tailwind.black`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); layers ::before transparent 0px none 1 |
| hover | background rgba(250, 250, 250, 0.9) |
| focus-visible | border 1px solid #01bcff `color.brand.accent`; shadow rgba(1, 188, 255, 0.3) 0px 0px 0px 3px |
| pressed | size 133.3 x 30.72; background rgba(250, 250, 250, 0.9) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Hero headline (dark)
The display headline under .dark. Read as `d-hero-title` on the home page.

**Values (default).** size 504.11 x 127.88; background transparent; text TikTok Sans 59.2/63.93 500, #fafafa `dark.foreground`; icon 35.17 x 35.17, #fafafa `dark.foreground`; layers div.home-sticker-frame.bg-surface-control 52.8x52.8 #171717 `dark.card.default` rgba(255, 255, 255, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.6) 0px 8px 24px -12px calc(22.5% + 2.2px); div.flex.size-10 44.0x44.0 #ffffff `color.tailwind.white` rgba(255, 255, 255, 0.08) 0px 0px 0px 1px 22.5%; div.rounded-xl.bg-surface-control 93.5x112.5 #171717 `dark.card.default` rgba(255, 255, 255, 0.08) 0px 0px 0px .

Child layers that carry the look: div 52.8x52.8 background #171717 `dark.card.default` radius calc(22.5% + 2.2px) shadow rgba(255, 255, 255, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.6) 0px 8px 24px -12px; div 44x44 background #ffffff `color.tailwind.white` radius 22.5% shadow rgba(255, 255, 255, 0.08) 0px 0px 0px 1px; div 93.5x112.5 background #171717 `dark.card.default` radius 16px shadow rgba(255, 255, 255, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.6) 0px 8px 24px -12px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Composer input (dark)
The Ask-Endless textarea under .dark; focused, nothing typed or sent. Read as `d-composer-input` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 660 x 72; padding 16px 20px 4px 20px; background transparent; text TikTok Sans 16/24 400, #fafafa `dark.foreground`; placeholder #a1a1a1 `dark.muted.foreground` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Nav link (dark)
A header link under .dark. Read as `d-nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 65.91 x 32; padding 6px 10px; radius 8px; background transparent; text TikTok Sans 14/20 400, #a1a1a1 `dark.muted.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::after transparent 0px none 1 |
| hover | background rgba(38, 38, 38, 0.5) `dark.muted.hover`; text TikTok Sans 14/20 400, #fafafa `dark.foreground` |
| focus-visible | background #262626 `color.tailwind.neutral-800` |
| pressed | background rgba(38, 38, 38, 0.5) `dark.muted.hover`; text TikTok Sans 14/20 400, #fafafa `dark.foreground` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Mobile (390 wide)

The marketing surface at phone width: the compact header, the menu overlay and the stacked hero.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 56; border B: 1px solid transparent; background rgba(252, 252, 252, 0.9) `measured.header-veil`; text TikTok Sans 14/20 600, #6e6e6e `light.muted.foreground`; transition background-color 0.15s cubic-bezier(0.22, 1, 0.36, 1), border-bottom-color 0.15s cubic-bezier(0.22, 1, 0.36, 1); icon 24 x 24, #0a0a0a `light.foreground`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The header menu toggle. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 36 x 36; border 1px solid transparent; radius 12px; background transparent; text TikTok Sans 14/20 500, #0a0a0a `light.foreground`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1), opacity 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), translate 0.15s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), rotate 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0, 0, 0.2, 1), display 0.15s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0, 0, 0.2, 1), overlay 0.15s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1); icon 20 x 20, #0a0a0a `light.foreground`; layers ::before transparent 0px none 1.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The header menu panel opened by its own toggle. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 904; background transparent; text TikTok Sans 16/24 500, #0a0a0a `light.foreground`; icon 16 x 16, #6e6e6e `light.muted.foreground`; layers div.bg-overlay/30.supports-backdrop-filter:backdrop-blur-sm 390.0x904.0 rgba(0, 0, 0, 0.3); div.mx-auto.box-border 390.0x436.0 #ffffff `color.tailwind.white` transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px 20px 20px 0px 0px; div.rounded-t-2xl.bg-inherit 39.

Child layers that carry the look: div 390x904 background rgba(0, 0, 0, 0.3); div 390x436 background #ffffff `color.tailwind.white` radius 20px 20px 0px 0px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px; div 390x736 background #ffffff `color.tailwind.white` radius 20px 20px 0px 0px.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
An item inside the opened header menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 374 x 44; padding 0px 12px; radius 8px; background transparent; text TikTok Sans 16/24 400, #0a0a0a `light.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 2px solid #01bcff `color.brand.accent`, offset -2px; layers a.flex.min-h-11 374.0x44.0 2px solid #01bcff `color.brand.accent` offset -2px 8px |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 358 x 81.19; background transparent; text TikTok Sans 37.6/40.60 500, #0a0a0a `light.foreground`.

![Mobile headline default](components/crops/m-hero-default.png)

#### Mobile composer
Read as `m-composer` on the home page at 390 wide.

**Values (default).** size 346 x 72; padding 16px 20px 4px 20px; background transparent; text TikTok Sans 16/24 400, #0a0a0a `light.foreground`; placeholder #6e6e6e `light.muted.foreground`.

![Mobile composer default](components/crops/m-composer-default.png)

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
