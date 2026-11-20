# Base44 components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from base44.com on 2026-11-11, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (44 components, 115 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 14/21 500, #111827`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (115 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [product-menu](screenshots/home-light-product-menu.png) |
| Features | `/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| Use cases | `/use-cases` | [default](screenshots/use-cases-light-default.png), [full](screenshots/use-cases-light-full.png) |
| Enterprise | `/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [monthly](screenshots/pricing-light-monthly.png), [yearly](screenshots/pricing-light-yearly.png) |
| Superagents | `/superagents` | [default](screenshots/superagents-light-default.png), [full](screenshots/superagents-light-full.png) |
| Sign in | `app.base44.com/login` | [default](screenshots/signin-light-default.png), [full](screenshots/signin-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Product menu, open | header, home | the nav button's own press | [home-light-product-menu](screenshots/home-light-product-menu.png), [nav-product-open](#product-menu-open) |
| Billing on Monthly | pricing | the segment's own press | [pricing-light-monthly](screenshots/pricing-light-monthly.png) |
| FAQ item, expanded | home | the question row's own press | [faq-open](#faq-item-expanded) |
| Mobile menu, open | header, phone | the menu trigger's own press | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 22 components were given a real keyboard focus. 22 show a visible focus state: `nav-menu-button` (2px solid #1e1e24 `color.ink.800`, offset 4px), `nav-link` (2px solid #1e1e24 `color.ink.800`, offset 4px), `nav-superagents` (2px solid #1e1e24 `color.ink.800`, offset 4px), `nav-locale` (2px solid #1e1e24 `color.ink.800`, offset 4px), `nav-cta` (2px solid #1e1e24 `color.ink.800`, offset 4px), `prompt-attach` (2px solid #1e1e24 `color.ink.800`, offset 4px), `prompt-mode` (2px solid #1e1e24 `color.ink.800`, offset 4px), `prompt-mic` (2px solid #1e1e24 `color.ink.800`, offset 4px), `prompt-submit` (2px solid #1e1e24 `color.ink.800`, offset 4px), `build-tile` (2px solid #1e1e24 `color.ink.800`, offset 4px), `faq-item` (2px solid #1e1e24 `color.ink.800`, offset 4px), `footer-link` (2px solid #1e1e24 `color.ink.800`, offset 4px), `footer-social` (2px solid #1e1e24 `color.ink.800`, offset 4px), `footer-legal` (2px solid #1e1e24 `color.ink.800`, offset 4px), `billing-yearly` (2px solid #1e1e24 `color.ink.800`, offset 4px), `billing-monthly` (2px solid #1e1e24 `color.ink.800`, offset 4px), `plan-cta` (2px solid #1e1e24 `color.ink.800`, offset 4px), `signin-google` (2px solid #3b51e5 `color.blue.500`, offset -1px), `signin-apple` (2px solid #3b51e5 `color.blue.500`, offset -1px), `signin-github` (2px solid #3b51e5 `color.blue.500`, offset -1px), `signin-signup` (visible change in boxShadow/color), `signin-legal` (1px auto #005fcc, offset 1px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): controls deepen their fill or dim rather than scale; the nav flyout and framework icons keep their hover scale. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease` | transform | prompt-submit |
| 0.12s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | signin-apple, signin-github, signin-google, signin-signup, signin-submit |
| 0.16s | `ease` | background-color, border-color, color, opacity | footer-legal, footer-link, footer-social, logo, nav-link, nav-superagents, prompt-attach, prompt-mic and more |
| 0.2s | `cubic-bezier(0.22, 1, 0.36, 1)` | background-color, border-color, color | build-tile, plan-cta |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | nav-cta |
| 0.26s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, box-shadow | signin-field-wrap |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color | header, m-header |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 420 x 691.42 | - | - | #ffffff `color.brand.white` | none | 30px 20px |
| [Prompt box](#prompt-box) | 555 x 150 | - | 8px | #ffffff `color.brand.white` | none | 0 |
| [Build-type tile](#build-type-tile) | 120 x 66 | - | 4px | #f9f7f4 `color.surface.cardWarm` | none | 14px 12px |

## Components

### Shell and navigation

The fixed header: the nav menus and links, the language globe and the Start building pill.

#### Header
The fixed bar: logo, the nav (Product, Use Cases, Solutions, Resources menus; Pricing, Enterprise, Superagents links), the language globe and the dark Start building pill. Read as `header` on the home page.

**Values (default).** size 1440 x 86; background transparent; text Dazzed 16/24 500, #1e1e24 `color.ink.800`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 111 x 26, #0f0f0f `color.ink.900`.

Child layers that carry the look: span::after 62.4531pxx1px background #1e1e24 `color.ink.800`; span::after 83.3906pxx1px background #1e1e24 `color.ink.800`; span::after 73.3594pxx1px background #1e1e24 `color.ink.800`.

![Header default](components/crops/header-default.png)

#### Logo
Read as `logo` on the home page.

**Values (default).** size 111 x 26; background transparent; text Geist 16/24 400, #0f0f0f `color.ink.900`; transition color 0.16s ease, background-color 0.16s ease, border-color 0.16s ease, opacity 0.16s ease; icon 111 x 26, #0f0f0f `color.ink.900`.

![Logo default](components/crops/logo-default.png)

#### Nav menu button
A top-level nav item that opens a mega menu (Product; Use Cases, Solutions and Resources are the same control). Read as `nav-menu-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 81.45 x 24; background transparent; text Dazzed 16/24 500, #1e1e24 `color.ink.800`; icon 10 x 4, #1e1e24 `color.ink.800` |
| focus-visible | radius 6px; outline 2px solid #1e1e24 `color.ink.800`, offset 4px |

Child layers that carry the look: span::after 62.4531pxx1px background #1e1e24 `color.ink.800`.

![Nav menu button default](components/crops/nav-menu-button-default.png) ![Nav menu button hover](components/crops/nav-menu-button-hover.png) ![Nav menu button focus-visible](components/crops/nav-menu-button-focus-visible.png) ![Nav menu button pressed](components/crops/nav-menu-button-pressed.png)

#### Product menu, open
The nav button after its own press opens the full-width product panel; the crop holds the opened panel. Read as `nav-product-open` on the home page.

**Values (opened).** size 81.45 x 24; background transparent; text Dazzed 16/24 500, #1e1e24 `color.ink.800`; icon 10 x 4, #1e1e24 `color.ink.800`.

Child layers that carry the look: span::after 62.4531pxx1px background #1e1e24 `color.ink.800`.

![Product menu, open opened](components/crops/nav-product-open-opened.png)

#### Nav link
Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 54.66 x 24; background transparent; text Dazzed 16/24 500, #1e1e24 `color.ink.800`; transition color 0.16s ease, background-color 0.16s ease, border-color 0.16s ease, opacity 0.16s ease |
| focus-visible | radius 6px; outline 2px solid #1e1e24 `color.ink.800`, offset 4px |

Child layers that carry the look: span::after 54.6562pxx1px background #1e1e24 `color.ink.800`.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Superagents link
The highlighted nav item, dotted either side and painted blue. Read as `nav-superagents` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 145.45 x 24; padding 0px 8px; radius 2px; background transparent; text Dazzed 16/24 600, #3950e6 `color.blue.accent`; transition color 0.16s ease, background-color 0.16s ease, border-color 0.16s ease, opacity 0.16s ease |
| focus-visible | outline 2px solid #1e1e24 `color.ink.800`, offset 4px |

Child layers that carry the look: span 4x4 background #3950e6 `color.blue.accent`; span::after 101.453pxx1px background #3950e6 `color.blue.accent`; span 4x4 background #3950e6 `color.blue.accent`.

![Superagents link default](components/crops/nav-superagents-default.png) ![Superagents link hover](components/crops/nav-superagents-hover.png) ![Superagents link focus-visible](components/crops/nav-superagents-focus-visible.png) ![Superagents link pressed](components/crops/nav-superagents-pressed.png)

#### Language button
The globe icon left of the CTA. Read as `nav-locale` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 24; background transparent; text Geist 16/24 400, #0f0f0f `color.ink.900` |
| focus-visible | radius 6px; outline 2px solid #1e1e24 `color.ink.800`, offset 4px |

![Language button default](components/crops/nav-locale-default.png) ![Language button hover](components/crops/nav-locale-hover.png) ![Language button focus-visible](components/crops/nav-locale-focus-visible.png) ![Language button pressed](components/crops/nav-locale-pressed.png)

#### Start building button
The dark pill on the right of the nav, repeated through the site. Measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 129.17 x 38; padding 0px 15px; radius 8px; background #312f2f `color.cta.black`; text Geist 16/16 600, #ffffff `color.brand.white`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #433f3f `color.cta.blackHover` |
| focus-visible | outline 2px solid #1e1e24 `color.ink.800`, offset 4px |
| pressed | background #433f3f `color.cta.blackHover` |

![Start building button default](components/crops/nav-cta-default.png) ![Start building button hover](components/crops/nav-cta-hover.png) ![Start building button focus-visible](components/crops/nav-cta-focus-visible.png) ![Start building button pressed](components/crops/nav-cta-pressed.png)

### Home

The Dazzed hero, the prompt composer, the build-type tiles and the FAQ accordion.

#### Hero title
"Every builder needs a base" in the site's display face (Dazzed). Read as `hero-title` on the home page.

**Values (default).** size 1135.47 x 98.44; background transparent; text Dazzed 93.74/98.43 600, #1e1e24 `color.ink.800`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero subcopy
Read as `hero-sub` on the home page.

**Values (default).** size 726.77 x 58.44; background transparent; text Geist 21.02/29.22 400, #1e1e24 `color.ink.800`.

![Hero subcopy default](components/crops/hero-sub-default.png)

#### Section title
Read as `section-title` on the home page.

**Values (default).** size 535.05 x 119.75; background transparent; text Dazzed 57.02/59.87 600, #1e1e24 `color.ink.800`.

![Section title default](components/crops/section-title-default.png)

#### Prompt box
The hero's "I want to build…" composer: a white rounded card with the textarea and its button row. Read as `prompt-box` on the home page.

**Values (default).** size 555 x 150; radius 8px; background #ffffff `color.brand.white`; text Geist 17/26 400, #6d6a67 `color.neutral.500`; icon 14 x 14, #1e1e24 `color.ink.800`.

![Prompt box default](components/crops/prompt-box-default.png)

#### Prompt field
The composer's textarea; sample text was typed and deleted, nothing sent. Read as `prompt-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 541 x 84; padding 20px 12px 12px 24px; background transparent; text Geist 17/26 400, #000000; placeholder #000000 |
| filled | placeholder #6d6a67 `color.neutral.500` |

![Prompt field default](components/crops/prompt-field-default.png) ![Prompt field focused](components/crops/prompt-field-focused.png) ![Prompt field filled](components/crops/prompt-field-filled.png)

#### Attach button
The "+" button at the composer's left. Measured, never pressed. Read as `prompt-attach` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; radius 8px; background transparent; text Geist 16/24 400, #1e1e24 `color.ink.800`; transition background-color 0.16s ease; icon 14 x 14, #1e1e24 `color.ink.800` |
| hover | background #f1eeea |
| focus-visible | outline 2px solid #1e1e24 `color.ink.800`, offset 4px |
| pressed | background #f1eeea |

![Attach button default](components/crops/prompt-attach-default.png) ![Attach button hover](components/crops/prompt-attach-hover.png) ![Attach button focus-visible](components/crops/prompt-attach-focus-visible.png) ![Attach button pressed](components/crops/prompt-attach-pressed.png)

#### Mode trigger
The "Build" dropdown inside the composer; its menu was not opened. Read as `prompt-mode` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 80.09 x 40; padding 0px 12px; radius 8px; background transparent; text Geist 16/16 500, #1e1e24 `color.ink.800`; transition background-color 0.16s ease; icon 14 x 14, #1e1e24 `color.ink.800` |
| hover | background #f1eeea |
| focus-visible | outline 2px solid #1e1e24 `color.ink.800`, offset 4px |
| pressed | background #f1eeea |

![Mode trigger default](components/crops/prompt-mode-default.png) ![Mode trigger hover](components/crops/prompt-mode-hover.png) ![Mode trigger focus-visible](components/crops/prompt-mode-focus-visible.png) ![Mode trigger pressed](components/crops/prompt-mode-pressed.png)

#### Voice button
The microphone button. Measured, never pressed. Read as `prompt-mic` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; radius 8px; background transparent; text Geist 16/24 400, #1e1e24 `color.ink.800`; transition background-color 0.16s ease; icon 16 x 20, #1e1e24 `color.ink.800` |
| hover | background #f1eeea |
| focus-visible | outline 2px solid #1e1e24 `color.ink.800`, offset 4px |
| pressed | background #f1eeea |

![Voice button default](components/crops/prompt-mic-default.png) ![Voice button hover](components/crops/prompt-mic-hover.png) ![Voice button focus-visible](components/crops/prompt-mic-focus-visible.png) ![Voice button pressed](components/crops/prompt-mic-pressed.png)

#### Send button
The orange send button. Measured in all states except pressed for real — nothing was sent. Read as `prompt-submit` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; radius 8px; background #ff773c `color.cta.orange`; text Geist 16/24 400, #1e1e24 `color.ink.800`; transition background-color 0.16s ease, transform 0.1s ease; icon 12 x 12, #1e1e24 `color.ink.800` |
| hover | background #ff8f5c `measured.send-hover` |
| focus-visible | outline 2px solid #1e1e24 `color.ink.800`, offset 4px |
| pressed | size 38.8 x 38.8; background #ff8f5c `measured.send-hover`; transform scale(0.97); icon 11.64 x 11.64, #1e1e24 `color.ink.800` |

![Send button default](components/crops/prompt-submit-default.png) ![Send button hover](components/crops/prompt-submit-hover.png) ![Send button focus-visible](components/crops/prompt-submit-focus-visible.png) ![Send button pressed](components/crops/prompt-submit-pressed.png)

#### Build-type tile
One of the five "What will you build?" tiles under the composer (App; Dashboard, Website, Mobile app and Online store are the same control). Read as `build-tile` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 120 x 66; padding 14px 12px; radius 4px; background #f9f7f4 `color.surface.cardWarm`; text Geist 16/16 400, #1e1e24 `color.ink.800`; transition background-color 0.2s cubic-bezier(0.22, 1, 0.36, 1), color 0.2s cubic-bezier(0.22, 1, 0.36, 1); icon 16 x 16, #6073f0 |
| hover | background #e2ded7 `color.surface.warm` |
| focus-visible | outline 2px solid #1e1e24 `color.ink.800`, offset 4px |
| pressed | background #e2ded7 `color.surface.warm` |

![Build-type tile default](components/crops/build-tile-default.png) ![Build-type tile hover](components/crops/build-tile-hover.png) ![Build-type tile focus-visible](components/crops/build-tile-focus-visible.png) ![Build-type tile pressed](components/crops/build-tile-pressed.png)

#### FAQ item
A collapsed row of the FAQ accordion. Read as `faq-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 712.47 x 66.97; padding 32.976px 0px 0px 0px; background transparent; text Dazzed 24.00/30.00 600, #1e1e24 `color.ink.800` |
| focus-visible | radius 6px; outline 2px solid #1e1e24 `color.ink.800`, offset 4px |

![FAQ item default](components/crops/faq-item-default.png) ![FAQ item hover](components/crops/faq-item-hover.png) ![FAQ item focus-visible](components/crops/faq-item-focus-visible.png) ![FAQ item pressed](components/crops/faq-item-pressed.png)

#### FAQ item, expanded
The same row after its own press; the crop holds the item and its answer. Read as `faq-open` on the home page.

**Values (expanded).** size 712.47 x 66.97; padding 32.976px 0px 0px 0px; background transparent; text Dazzed 24.00/30.00 600, #1e1e24 `color.ink.800`.

![FAQ item, expanded expanded](components/crops/faq-open-expanded.png)

### Pricing

The billing toggle, the plan cards and their Start building CTAs, and the Popular badge.

#### Pricing title
Read as `pricing-title` on the pricing page.

**Values (default).** size 1278.86 x 93.17; background transparent; text Dazzed 87.90/93.17 600, #1e1e24 `color.ink.800`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Billing toggle
The Yearly/Monthly segment control over the plan cards. Read as `billing-toggle` on the pricing page.

**Values (default).** size 283.05 x 56; padding 4px; radius 12px; background rgba(255, 255, 255, 0.6) `measured.toggle-shell`; text Geist 20/28 500, #1e1e24 `color.ink.800`.

![Billing toggle default](components/crops/billing-toggle-default.png)

#### Yearly segment
The selected segment ("Yearly SAVE 20%"), painted orange. Read as `billing-yearly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 170 x 48; padding 10px 16px; radius 8px; background transparent; text Geist 17/17 400, #1e1e24 `color.ink.800` |
| focus-visible | outline 2px solid #1e1e24 `color.ink.800`, offset 4px |

![Yearly segment default](components/crops/billing-yearly-default.png) ![Yearly segment hover](components/crops/billing-yearly-hover.png) ![Yearly segment focus-visible](components/crops/billing-yearly-focus-visible.png) ![Yearly segment pressed](components/crops/billing-yearly-pressed.png)

#### Monthly segment
The unselected segment; switching it is a local toggle, no purchase. Read as `billing-monthly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 105.05 x 48; padding 10px 16px; radius 8px; background transparent; text Geist 20/28 500, #1e1e24 `color.ink.800` |
| focus-visible | outline 2px solid #1e1e24 `color.ink.800`, offset 4px |

![Monthly segment default](components/crops/billing-monthly-default.png) ![Monthly segment hover](components/crops/billing-monthly-hover.png) ![Monthly segment focus-visible](components/crops/billing-monthly-focus-visible.png) ![Monthly segment pressed](components/crops/billing-monthly-pressed.png)

#### Plan CTA
The full-width "Start building" button inside a plan card. Measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 380 x 50; padding 0px 26px; border 1px solid transparent; radius 10px; background #312f2f `color.cta.black`; text Geist 18/normal 500, #ffffff `color.brand.white`; transition background-color 0.2s cubic-bezier(0.22, 1, 0.36, 1), color 0.2s cubic-bezier(0.22, 1, 0.36, 1), border-color 0.2s cubic-bezier(0.22, 1, 0.36, 1) |
| hover | background #433f3f `color.cta.blackHover` |
| focus-visible | outline 2px solid #1e1e24 `color.ink.800`, offset 4px |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan card
Read as `plan-card` on the pricing page.

**Values (default).** size 420 x 691.42; padding 30px 20px; background #ffffff `color.brand.white`; text Dazzed 36/39.6 600, #1e1e24 `color.ink.800`; icon 14 x 14, #1e1e24 `color.ink.800`.

![Plan card default](components/crops/plan-card-default.png)

#### Popular badge
The blue chip on the Builder plan card. Read as `popular-badge` on the pricing page.

**Values (default).** size 70.81 x 28; padding 7px 10px; radius 4px; background #3b51e5 `color.blue.500`; text Geist 14/14 500, #ffffff `color.brand.white`.

![Popular badge default](components/crops/popular-badge-default.png)

#### Price figure
A plan's price ("$160" on Elite at yearly billing). Read as `price` on the pricing page.

**Values (default).** size 380.02 x 48; background transparent; text Geist 48/48 400, #1e1e24 `color.ink.800`.

![Price figure default](components/crops/price-default.png)

### Sign in

The OAuth buttons, the email field and its disabled submit on app.base44.com/login.

#### Sign-in title
"Welcome to Base44" on app.base44.com/login. Read as `signin-title` on the sign-in (app.base44.com/login) page.

**Values (default).** size 384 x 32; background transparent; text Dazzed 28/32 560, #0f0e0e.

![Sign-in title default](components/crops/signin-title-default.png)

#### Log in with Google
The OAuth button. Measured, never pressed — no sign-in was attempted. Read as `signin-google` on the sign-in (app.base44.com/login) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 36; padding 0px 16px; border 1px solid #c9c3bc; radius 6px; background transparent; text Wix Madefor Text 14/18 460, #0f0e0e; transition color 0.12s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), fill 0.12s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.12s cubic-bezier(0.4, 0, 0.2, 1); icon 25.2 x 25.2, #0f0e0e |
| hover | border 1px solid #99928b; background #e9e6e0 |
| focus-visible | border 1px solid #99928b; outline 2px solid #3b51e5 `color.blue.500`, offset -1px |
| pressed | border 1px solid #99928b; background #ddd8d2 `color.border.warm` |

![Log in with Google default](components/crops/signin-google-default.png) ![Log in with Google hover](components/crops/signin-google-hover.png) ![Log in with Google focus-visible](components/crops/signin-google-focus-visible.png) ![Log in with Google pressed](components/crops/signin-google-pressed.png)

#### Log in with Apple
The OAuth button. Measured, never pressed. Read as `signin-apple` on the sign-in (app.base44.com/login) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 36; padding 0px 16px; border 1px solid #c9c3bc; radius 6px; background transparent; text Wix Madefor Text 14/18 460, #0f0e0e; transition color 0.12s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), fill 0.12s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.12s cubic-bezier(0.4, 0, 0.2, 1); icon 18 x 18, #0f0e0e |
| hover | border 1px solid #99928b; background #e9e6e0 |
| focus-visible | border 1px solid #99928b; outline 2px solid #3b51e5 `color.blue.500`, offset -1px |
| pressed | border 1px solid #99928b; background #ddd8d2 `color.border.warm` |

![Log in with Apple default](components/crops/signin-apple-default.png) ![Log in with Apple hover](components/crops/signin-apple-hover.png) ![Log in with Apple focus-visible](components/crops/signin-apple-focus-visible.png) ![Log in with Apple pressed](components/crops/signin-apple-pressed.png)

#### Log in with GitHub
The OAuth button. Measured, never pressed. Read as `signin-github` on the sign-in (app.base44.com/login) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 36; padding 0px 16px; border 1px solid #c9c3bc; radius 6px; background transparent; text Wix Madefor Text 14/18 460, #0f0e0e; transition color 0.12s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), fill 0.12s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.12s cubic-bezier(0.4, 0, 0.2, 1); icon 18 x 18, #0f0e0e |
| hover | border 1px solid #99928b; background #e9e6e0 |
| focus-visible | border 1px solid #99928b; outline 2px solid #3b51e5 `color.blue.500`, offset -1px |
| pressed | border 1px solid #99928b; background #ddd8d2 `color.border.warm` |

![Log in with GitHub default](components/crops/signin-github-default.png) ![Log in with GitHub hover](components/crops/signin-github-hover.png) ![Log in with GitHub focus-visible](components/crops/signin-github-focus-visible.png) ![Log in with GitHub pressed](components/crops/signin-github-pressed.png)

#### Email field shell
The bordered box holding the email input. Read as `signin-field-wrap` on the sign-in (app.base44.com/login) page.

**Values (default).** size 384 x 36; padding 8px 12px; border 1px solid #99928b; radius 6px; background transparent; text Wix Madefor Text 16/24 400, #0f0e0e; transition background-color 0.26s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.26s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.26s cubic-bezier(0.4, 0, 0.2, 1).

![Email field shell default](components/crops/signin-field-wrap-default.png)

#### Email field
The sign-in email input; sample text was typed and deleted, nothing sent. Read as `signin-field` on the sign-in (app.base44.com/login) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 358 x 18; background transparent; outline 2px solid transparent, offset 2px; text Wix Madefor Text 14/18 460, #0f0e0e; placeholder #99928b |

Child layers that carry the look: input 358x18.

![Email field default](components/crops/signin-field-default.png) ![Email field focused](components/crops/signin-field-focused.png) ![Email field filled](components/crops/signin-field-filled.png)

#### Continue with email button
The email sign-in submit, captured disabled as painted for an empty field (the state was measured, never enabled or pressed). Read as `signin-submit` on the sign-in (app.base44.com/login) page.

**Values (default).** size 384 x 36; padding 0px 16px; radius 6px; background #ebebeb `measured.submit-disabled-bg`; text Wix Madefor Text 14/18 460, #929292; transition color 0.12s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), fill 0.12s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.12s cubic-bezier(0.4, 0, 0.2, 1).

![Continue with email button default](components/crops/signin-submit-default.png)

#### Sign up link
The register link under the form. Measured, never followed. Read as `signin-signup` on the sign-in (app.base44.com/login) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 50.2 x 18; radius 4px; background transparent; text Wix Madefor Text 14/18 460, #0f0e0e; transition color 0.12s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.12s cubic-bezier(0.4, 0, 0.2, 1), fill 0.12s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.12s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Wix Madefor Text 14/18 460, #3a3939 |
| focus-visible | shadow #3b51e5 0px 0px 0px 3px; outline 2px solid transparent, offset 2px; text Wix Madefor Text 14/18 460, #5d5d5d |
| pressed | text Wix Madefor Text 14/18 460, #3a3939 |

![Sign up link default](components/crops/signin-signup-default.png) ![Sign up link hover](components/crops/signin-signup-hover.png) ![Sign up link focus-visible](components/crops/signin-signup-focus-visible.png) ![Sign up link pressed](components/crops/signin-signup-pressed.png)

#### Legal link
Read as `signin-legal` on the sign-in (app.base44.com/login) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 93.61 x 15; background transparent; text Wix Madefor Text 12/16 460, #5d5d5d |
| hover | text Wix Madefor Text 12/16 460, #0f0e0e |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | text Wix Madefor Text 12/16 460, #0f0e0e |

![Legal link default](components/crops/signin-legal-default.png) ![Legal link hover](components/crops/signin-legal-hover.png) ![Legal link focus-visible](components/crops/signin-legal-focus-visible.png) ![Legal link pressed](components/crops/signin-legal-pressed.png)

### Footer

The link columns and social icons.

#### Footer
Read as `footer` on the home page.

**Values (default).** size 1440 x 790; background #ffffff `color.brand.white`; text Geist 16/24 400, #1e1e24 `color.ink.800`; icon 111 x 26, #1e1e24 `color.ink.800`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 67.02 x 21; background transparent; text Geist 16/32 400, #1e1e24 `color.ink.800`; transition color 0.16s ease, background-color 0.16s ease, border-color 0.16s ease, opacity 0.16s ease |
| focus-visible | radius 6px; outline 2px solid #1e1e24 `color.ink.800`, offset 4px |

Child layers that carry the look: span::after 67156pxx1px background #1e1e24 `color.ink.800`.

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer social icon
One of the social icon links (X; Discord, LinkedIn and Reddit are the same control). Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 26 x 26; background transparent; text Geist 16/24 400, #1e1e24 `color.ink.800`; transition color 0.16s ease, background-color 0.16s ease, border-color 0.16s ease, opacity 0.16s ease; icon 26 x 26, #1e1e24 `color.ink.800` |
| focus-visible | radius 6px; outline 2px solid #1e1e24 `color.ink.800`, offset 4px |

![Footer social icon default](components/crops/footer-social-default.png) ![Footer social icon hover](components/crops/footer-social-hover.png) ![Footer social icon focus-visible](components/crops/footer-social-focus-visible.png) ![Footer social icon pressed](components/crops/footer-social-pressed.png)

#### Legal link
Read as `footer-legal` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 101.3 x 21; background transparent; text Geist 16/32 400, #1e1e24 `color.ink.800`; transition color 0.16s ease, background-color 0.16s ease, border-color 0.16s ease, opacity 0.16s ease |
| focus-visible | radius 6px; outline 2px solid #1e1e24 `color.ink.800`, offset 4px |

Child layers that carry the look: span::after 101.297pxx1px background #1e1e24 `color.ink.800`.

![Legal link default](components/crops/footer-legal-default.png) ![Legal link hover](components/crops/footer-legal-hover.png) ![Legal link focus-visible](components/crops/footer-legal-focus-visible.png) ![Legal link pressed](components/crops/footer-legal-pressed.png)

### Mobile (390 wide)

The same surface at phone width, with its full-sheet menu.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 54; background transparent; text Geist 14/14 500, #ffffff `color.brand.white`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 94 x 22, #0f0f0f `color.ink.900`.

Child layers that carry the look: span::after autox1px background #1e1e24 `color.ink.800`; span::after autox1px background #1e1e24 `color.ink.800`; span::after autox1px background #1e1e24 `color.ink.800`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
The hamburger trigger at the right of the mobile bar; its own press opens the full-sheet menu. Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 24 x 24; background transparent; text Geist 16/24 400, #1e1e24 `color.ink.800` |

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The trigger after its own toggle; the open sheet shows in the crop. Read as `m-menu-open` on the home page at 390 wide.

**Values (opened).** size 24 x 24; background transparent; text Geist 16/24 400, #1e1e24 `color.ink.800`; icon 24 x 24, #1e1e24 `color.ink.800`.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Base44's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The app behind sign-in.** Base44's product sits behind app.base44.com and was never signed into; the OAuth buttons and the email flow were measured, never used.
- **Anything that sends or signs in.** No form was submitted, no account was created, the prompt box was never sent and no nav item was followed.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The public routes paint one light theme. The bundle declares a standard shadcn `.dark` block (channel roles, charts, sidebar) that is never painted on them; the dark token set is emitted from those declared values, labelled declared-not-painted.

### Fonts

- **The UI fonts** are webfonts declared in the bundle (Dazzed for display, Geist for UI, JetBrains Mono, WixMadeforText; `fonts` in [raw/css-vars.json](raw/css-vars.json)); the font files themselves are not committed.
- Illustration and wordmark artwork in the screenshots are Base44's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- App imagery, the generated-app strip and the wordmark are Base44's content; only the frames and components were measured.
