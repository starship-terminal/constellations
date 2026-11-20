# Dock components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from dock.us on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, submitted or paid for; the auth cards were measured and their fields focused and given sample text that was deleted again, never sent; the Log in, sign-up, OAuth, demo-submit and sales actions were never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (54 components, 118 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (109 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Customers | `/customers` | [default](screenshots/customers-light-default.png), [full](screenshots/customers-light-full.png) |
| Library | `/library` | [default](screenshots/library-light-default.png), [full](screenshots/library-light-full.png) |
| Templates | `/templates` | [default](screenshots/templates-light-default.png), [full](screenshots/templates-light-full.png) |
| Product (Dock AI) | `/product/dock-ai` | [default](screenshots/product-light-default.png), [full](screenshots/product-light-full.png) |
| Solutions (Sales) | `/solutions/sales` | [default](screenshots/solutions-light-default.png), [full](screenshots/solutions-light-full.png) |
| About | `/about-us` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Demo request | `/demo` | [default](screenshots/demo-light-default.png), [full](screenshots/demo-light-full.png) |
| Log in card (auth.dock.us) | `auth.dock.us/login` | [default](screenshots/login-light-default.png) |
| Sign up card (auth.dock.us) | `auth.dock.us/sign-up` | [default](screenshots/signup-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Product mega-menu | every desktop page | the Product <summary> trigger's own click | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-dropdown), [menu-group](#menu-group-heading), [menu-link](#menu-link) |
| Mobile menu | home, phone width | the Menu <summary> toggle's own click | [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item) |
| Pricing FAQ rows | /pricing | a FAQ <summary>'s own toggle | [faq-item](#faq-item) |
| Customer filter pills | /customers | a filter pill's own toggle — a local UI filter | [filter-radio](#filter-radio) |
| Consent and chat overlays | every page | hidden, never answered (no consent or chat control was ever clicked) | hidden before every shot and reading |
| Auth card fields | auth.dock.us | the subdomain and email fields were focused and given sample text that was deleted again, never sent | [subdomain-field](#subdomain-field), [signup-field](#signup-email-field) |
| Demo form fields | /demo | read through the cross-origin HubSpot iframe; the focused state clicked into a field once, never filled or submitted | [demo-field](#demo-field), [demo-submit](#demo-submit) |
| The signed-in product | the Dock workspace app behind auth.dock.us | behind sign-in; the auth cards were measured, never used | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 11 components were given a real keyboard focus. 6 draw an outline ring: `hero-cta` (2px solid rgba(18, 23, 34, 0.6) `measured.focus-ring`, offset 4px), `hero-demo` (2px solid rgba(18, 23, 34, 0.6) `measured.focus-ring`, offset 4px), `plan-cta` (2px solid #0068f9 `color.brand.blue`, offset 4px), `faq-item` (2px solid #0068f9 `color.brand.blue`, offset 4px), `demo-submit` (2px solid #0068f9 `color.brand.blue`, offset 4px), `mcp-copy` (2px solid rgba(18, 23, 34, 0.6) `measured.focus-ring`, offset 4px). The other 5 show no measured change: `filter-radio`, `customer-card`, `sidebar-link`, `template-card`, `signup-submit`. Focus could not be captured on 9 more (keyboard focus never landed on them, so their readings are left out): `nav-trigger`, `nav-link`, `nav-login`, `nav-demo`, `nav-cta`, `menu-link`, `continue-btn`, `footer-link`, `m-nav-item`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.14s | `ease` | background-color, box-shadow | hero-cta, hero-demo, m-menu-button, mcp-copy, nav-cta, nav-demo, plan-cta |
| 0.15s | `ease` | background | demo-submit |
| 0.2s | `ease` | background-color, border-color, box-shadow, color, fill, opacity, stroke, transform | continue-btn, customer-card, sidebar-link, signup-field, signup-submit, subdomain-field, template-card |
| 0.24s | `cubic-bezier(0.22, 1, 0.36, 1)` | height, opacity, scale, translate, width | nav-dropdown |
| 0.25s | `ease` | transform | pr-sticky |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 225.75 x 300 | - | - | transparent | none | 44px 32px 32px 32px |
| [Nav dropdown](#nav-dropdown) | 1083 x 258 | - | 19.1px | #ffffff `color.neutral.white` | rgba(18, 23, 34, 0.2) 0px 0px 0px 0.5px, rgba(18, 23, 34, 0.05) 0px 1px 3px 0px, rgba(18, 23, 34, 0.05) 0px 3px 7px 0px | 0 |
| [Login card](#login-card) | 450 x 322.8 | - | 4px | #ffffff `color.neutral.white` | rgba(18, 23, 34, 0.25) 0px 20px 36px -18px, rgba(18, 23, 34, 0.1) 0px 0px 0px 0.5px, rgba(18, 23, 34, 0.2) 0px 1px 2px 0px | 64px |
| [Signup card](#signup-card) | 300 x 209.5 | - | - | transparent | none | 0 |
| [Customer card](#customer-card) | 580 x 375 | - | - | transparent | none | 0px 0px 1px 0px |
| [Testimonial](#testimonial) | 381.33 x 422.48 | - | 16px | #f4f0ff | none | 16px |
| [Template card](#template-card) | 338.13 x 307.67 | - | - | transparent | none | 0px 0px 1px 0px |
| [Mobile menu, open](#mobile-menu-open) | 350 x 386 | - | 19.1px | #ffffff `color.neutral.white` | rgba(18, 23, 34, 0.2) 0px 0px 0px 0.5px, rgba(18, 23, 34, 0.05) 0px 1px 3px 0px, rgba(18, 23, 34, 0.05) 0px 3px 7px 0px | 8px 24px 24px 24px |

## Components

### Shell and navigation

The sticky marketing header — the dock-site-header web component (its shadow DOM was pierced, never modified): the Dock wordmark, the Product and Resources <details> dropdowns, Pricing and Customers links, Log in, Request demo and the Start-for-free pill. The Product trigger opens a white mega-menu panel with grouped feature links.

#### Header
The sticky marketing header: the Dock logo, the Product and Resources <details> dropdowns, Pricing and Customers links, Log in, Request demo and the Start-for-free primary action. Read as `header` on the home page.

**Values (default).** size 1328 x 70.19; padding 16px 24px; background transparent; text DockWebflowNavigation 16/19.2 500, #121722 `color.neutral.ink`; layers summary.button.navigation-toggle 0.0x0.0 rgb(255, 255, 255) color(srgb 0.0705882 0.0901961 0.133333 / 0.2) 0px 0px 0px 0.5px inset 100px; div.menu-viewport 0.0x0.0 rgb(255, 255, 255) color(srgb 0.0705882 0.0901961 0.133333 / 0.2) 0px 0px 0px 0.5px, color(srgb 0.0705882 0.0901961 0.133333 / 0.05) 0px 1px 3px 0px, color(srgb 0.0705882 0.0901961 0.133333 / 0.05) 0px 3px 7px 0px 19.1px; a.button 137.0.

Child layers that carry the look: summary 0x0 background #ffffff `color.neutral.white` radius 100px shadow rgba(18, 23, 34, 0.2) `color.neutral.hairline` 0px 0px 0px 0.5px inset; div 0x0 background #ffffff `color.neutral.white` radius 19.1px shadow rgba(18, 23, 34, 0.2) `color.neutral.hairline` 0px 0px 0px 0.5px, rgba(18, 23, 34, 0.05) 0px 1px 3px 0px, rgba(18, 23, 34, 0.05) 0px 3px 7px 0px; a 137x38.2 background #ffffff `color.neutral.white` radius 100px shadow rgba(18, 23, 34, 0.2) `color.neutral.hairline` 0px 0px 0px 0.5px inset.

![Header default](components/crops/header-default.png)

#### Logo
The Dock wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 85.84 x 18; background transparent; text DockWebflowNavigation 16/24 400, #121722 `color.neutral.ink`.

![Logo default](components/crops/logo-default.png)

#### Nav trigger
The Product <summary> that opens the header mega-menu; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 105.7 x 38.19; padding 9px 14px 10px 16px; radius 100px; background transparent; text DockWebflowNavigation 16/19.2 500, #121722 `color.neutral.ink`; icon 12 x 12, #121722 `color.neutral.ink` |
| hover, pressed | background #f8f8f8 `color.neutral.wash-hover` |

**Focus not capturable.** A real keyboard focus could not be confirmed on this element (`focus-visible` recorded `via: focus failed`; the via was later rewritten by hand, not re-measured), so its focus look is uncaptured — not measured as absent.

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav link
The plain Pricing header link. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 81.98 x 38.19; padding 9px 16px 10px 16px; radius 100px; background transparent; text DockWebflowNavigation 16/19.2 500, #121722 `color.neutral.ink` |
| hover, pressed | background #f8f8f8 `color.neutral.wash-hover` |

**Focus not capturable.** A real keyboard focus could not be confirmed on this element (`focus-visible` recorded `via: focus failed`; the via was later rewritten by hand, not re-measured), so its focus look is uncaptured — not measured as absent.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log-in link
The Log-in header action (to auth.dock.us); measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 75.8 x 38.19; padding 9px 16px 10px 16px; radius 100px; background transparent; text DockWebflowNavigation 16/19.2 500, #121722 `color.neutral.ink` |
| hover, pressed | background #f8f8f8 `color.neutral.wash-hover` |

**Focus not capturable.** A real keyboard focus could not be confirmed on this element (`focus-visible` recorded `via: focus failed`; the via was later rewritten by hand, not re-measured), so its focus look is uncaptured — not measured as absent.

![Log-in link default](components/crops/nav-login-default.png) ![Log-in link hover](components/crops/nav-login-hover.png) ![Log-in link pressed](components/crops/nav-login-pressed.png)

#### Demo button
The Request-demo header action; measured, never followed. Read as `nav-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 137 x 38.19; padding 9px 16px 10px 16px; radius 100px; background #ffffff `color.neutral.white`; shadow rgba(18, 23, 34, 0.2) 0px 0px 0px 0.5px inset; text DockWebflowNavigation 16/19.2 500, #121722 `color.neutral.ink`; transition background-color 0.14s ease, box-shadow 0.14s ease |
| hover | background #f8f8f8 `color.neutral.wash-hover` |
| pressed | background #f2f2f3 `color.neutral.wash-pressed` |

**Focus not capturable.** A real keyboard focus could not be confirmed on this element (`focus-visible` recorded `via: focus failed`; the via was later rewritten by hand, not re-measured), so its focus look is uncaptured — not measured as absent.

![Demo button default](components/crops/nav-demo-default.png) ![Demo button hover](components/crops/nav-demo-hover.png) ![Demo button pressed](components/crops/nav-demo-pressed.png)

#### Nav CTA
The Start-for-free primary header action; measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 124.25 x 38.19; padding 9px 16px 10px 16px; radius 100px; background #0068f9 `color.brand.blue`; shadow rgba(11, 68, 147, 0.4) 0px 0px 0px 0.5px inset; text DockWebflowNavigation 16/19.2 500, #ffffff `color.neutral.white`; transition background-color 0.14s ease, box-shadow 0.14s ease |
| hover | background #0060eb `color.brand.blue-hover` |
| pressed | background #005fe4 `color.brand.blue-pressed` |

**Focus not capturable.** A real keyboard focus could not be confirmed on this element (`focus-visible` recorded `via: focus failed`; the via was later rewritten by hand, not re-measured), so its focus look is uncaptured — not measured as absent.

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Nav dropdown
The Product mega-menu panel inside dock-site-header, opened by its own <summary> trigger. Read as `nav-dropdown` on the home page.

**Values (default).** size 1083 x 258; radius 19.1px; background #ffffff `color.neutral.white`; shadow rgba(18, 23, 34, 0.2) 0px 0px 0px 0.5px, rgba(18, 23, 34, 0.05) 0px 1px 3px 0px, rgba(18, 23, 34, 0.05) 0px 3px 7px 0px; text DockWebflowNavigation 14.5/20 400, #121722 `color.neutral.ink`; transition translate 0.24s cubic-bezier(0.22, 1, 0.36, 1), scale 0.24s cubic-bezier(0.22, 1, 0.36, 1), width 0.24s cubic-bezier(0.22, 1, 0.36, 1), height 0.24s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.24s cubic-bezier(0.22, 1, 0.36, 1).

![Nav dropdown default](components/crops/nav-dropdown-default.png)

#### Menu group heading
A group heading inside the opened mega-menu (Sales / Customer success / Content / Learning / AI / Integrations). Read as `menu-group` on the home page.

**Values (default).** size 148.83 x 19.07; background transparent; text DockWebflowNavigation 14.5/20 400, #121722 `color.neutral.ink`; opacity 0.6.

![Menu group heading default](components/crops/menu-group-default.png)

#### Menu link
A feature link inside the opened mega-menu. Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 172.06 x 40; padding 8px; radius 8px; background transparent; text DockWebflowNavigation 15.5/20 500, #121722 `color.neutral.ink`; icon 16 x 16, #121722 `color.neutral.ink` |
| pressed | outline 2px solid rgba(18, 23, 34, 0.6) `measured.focus-ring`, offset 4px; layers a.menu-link 172.1x40.0 2px solid color(srgb 0.0705882 0.0901961 0.133333 / 0.6) offset 4px 8px |

**Focus not capturable.** A real keyboard focus could not be confirmed on this element (`focus-visible` recorded `via: focus failed`; the via was later rewritten by hand, not re-measured), so its focus look is uncaptured — not measured as absent.

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link pressed](components/crops/menu-link-pressed.png)

### Home

The deep-blue hero band with the 62px "Build high-performing sales teams" display, the ghost Request-demo and blue Start-for-free actions and the product-scene artwork; then light sections including the Dock-MCP prompt widget with its Copy action.

#### Hero headline
The "Build high-performing sales teams" display headline. Read as `hero-title` on the home page.

**Values (default).** size 1280 x 140.81; background transparent; text DockWebflowHome 62/70.4 600, #ffffff `color.neutral.white`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede under the hero headline. Read as `hero-lede` on the home page.

**Known wrong; recapture needed.** The reading and crop are the hero eyebrow pill ("AI Revenue Enablement", 202 x 38), not the lede under the headline. The committed script now marks the first sentence-length paragraph after the h1 instead; it has not been re-run.

**Note:** This run's reading and crop describe the hero eyebrow ('AI Revenue Enablement'), not the lede under the headline — the broad text match landed on p.hero-eyebrow. The selector was fixed in measure.mjs (the first sentence-length paragraph after the h1) and a re-measure is queued.

**Values (default).** size 202.23 x 38.19; padding 9px 16px 10px 16px; radius 100px; background #002fa6 `color.brand.blue-deep`; text DockWebflowHome 16/19.2 500, #ffffff `color.neutral.white`.

![Hero copy default](components/crops/hero-lede-default.png)

#### Hero CTA
The primary Start-for-free action in the hero; measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 151.78 x 44.59; padding 10px 24px 13px 24px; radius 100px; background #0068f9 `color.brand.blue`; shadow rgba(77, 181, 255, 0.3) 0px 0px 0px 0.5px inset; text DockWebflowHome 18/21.6 500, #ffffff `color.neutral.white`; transition background-color 0.14s ease, box-shadow 0.14s ease |
| hover | background #0060eb `color.brand.blue-hover` |
| focus-visible | outline 2px solid rgba(18, 23, 34, 0.6) `measured.focus-ring`, offset 4px |
| pressed | background #005fe4 `color.brand.blue-pressed` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero demo action
The secondary Request-demo action in the hero; measured, never followed. Read as `hero-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 166.13 x 44.59; padding 10px 24px 13px 24px; radius 100px; background transparent; shadow rgba(77, 181, 255, 0.4) 0px 0px 0px 0.5px inset; text DockWebflowHome 18/21.6 500, #ffffff `color.neutral.white`; transition background-color 0.14s ease, box-shadow 0.14s ease; layers a.dock-home-button 166.1x44.6 color(srgb 0.301961 0.709804 1 / 0.4) 0px 0px 0px 0.5px inset 100px |
| hover | background rgba(255, 255, 255, 0.06); layers none |
| focus-visible | outline 2px solid rgba(18, 23, 34, 0.6) `measured.focus-ring`, offset 4px; layers a.dock-home-button 166.1x44.6 color(srgb 0.301961 0.709804 1 / 0.4) 0px 0px 0px 0.5px inset 2px solid color(srgb 0.0705882 0.0901961 0.133333 / 0.6) offset 4px 100px |
| pressed | background rgba(255, 255, 255, 0.1); layers none |

![Hero demo action default](components/crops/hero-demo-default.png) ![Hero demo action hover](components/crops/hero-demo-hover.png) ![Hero demo action focus-visible](components/crops/hero-demo-focus-visible.png) ![Hero demo action pressed](components/crops/hero-demo-pressed.png)

#### Hero artwork
The painted product-scene layer behind the hero copy (the sales-room artwork panel). Read as `hero-card` on the home page.

**Values (default).** size 951.45 x 598.47; radius 18.93px; background #ffffff `color.neutral.white`; shadow rgba(18, 23, 34, 0.2) 0px 0px 0px 0.5px, rgba(18, 23, 34, 0.05) 0px 1px 3px 0px, rgba(18, 23, 34, 0.05) 0px 3px 7px 0px; text DockWebflowHome 16/19.2 500, #121722 `color.neutral.ink`; icon 15.86 x 15.86, rgba(18, 23, 34, 0.8) `color.neutral.muted`.

![Hero artwork default](components/crops/hero-card-default.png)

#### Section heading
A section heading in the light sections. Read as `section-h2` on the home page.

**Values (default).** size 239.3 x 21.59; padding 0px 16px; background #ffffff `color.neutral.white`; text DockWebflowHome 18/21.6 500, #121722 `color.neutral.ink`.

![Section heading default](components/crops/section-h2-default.png)

#### Prompt field
The read-only Dock-MCP setup prompt input; it paints inside the collapsed label.mcp-prompt-field, so only the hidden state is normally reachable. Read as `agent-field` on the home page.

Not on the page when it was captured.

#### Prompt area
The read-only selected-prompt textarea in the demo section. Read as `agent-area` on the home page.

Not on the page when it was captured.

#### MCP prompt
The Dock-MCP "install the prompt" widget in the MCP section: a prompt field, an Explore link and the Copy action. Read as `mcp-prompt` on the home page.

**Values (default).** size 381.2 x 44; background transparent; text DockWebflowHome 16/19.2 500, #ffffff `color.neutral.white`; icon 16 x 16, #ffffff `color.neutral.white`; layers a.dock-home-button.mcp-explore 161.5x44.0 color(srgb 0.301961 0.709804 1 / 0.4) 0px 0px 0px 0.5px inset 100px; button.dock-home-button.dock-home-button--primary 207.7x44.0 rgb(0, 104, 249) color(srgb 0.301961 0.709804 1 / 0.3) 0px 0px 0px 0.5px inset 100px; span 24.0x24.0 rgb(255, 255, 255) color(srgb 0.0705882 0.0901961 0.133333 / 0.2) 0px 0px 0px 0.5px 100px; span 24.0x24.0 rgb(255, 255, 255) co.

Child layers that carry the look: a 161.5x44 radius 100px shadow rgba(77, 181, 255, 0.4) 0px 0px 0px 0.5px inset; button 207.7x44 background #0068f9 `color.brand.blue` radius 100px shadow rgba(77, 181, 255, 0.3) 0px 0px 0px 0.5px inset; span 24x24 background #ffffff `color.neutral.white` radius 100px shadow rgba(18, 23, 34, 0.2) `color.neutral.hairline` 0px 0px 0px 0.5px.

![MCP prompt default](components/crops/mcp-prompt-default.png)

#### Copy prompt
The Copy-prompt action in the MCP widget; hover/focus/pressed read, the copy itself never clicked. Read as `mcp-copy` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 207.7 x 44; padding 10px 14px 10px 10px; radius 100px; background #0068f9 `color.brand.blue`; shadow rgba(77, 181, 255, 0.3) 0px 0px 0px 0.5px inset; text DockWebflowHome 16/19.2 500, #ffffff `color.neutral.white`; transition background-color 0.14s ease, box-shadow 0.14s ease; icon 16 x 16, #ffffff `color.neutral.white` |
| hover | background #0060eb `color.brand.blue-hover` |
| focus-visible | outline 2px solid rgba(18, 23, 34, 0.6) `measured.focus-ring`, offset 4px |
| pressed | background #005fe4 `color.brand.blue-pressed` |

![Copy prompt default](components/crops/mcp-copy-default.png) ![Copy prompt hover](components/crops/mcp-copy-hover.png) ![Copy prompt focus-visible](components/crops/mcp-copy-focus-visible.png) ![Copy prompt pressed](components/crops/mcp-copy-pressed.png)

### Pricing

The /pricing comparison surface: the Dock Pricing title, the Free / Standard / Premium / Enterprise plan columns with Get-started actions, the sticky plan bar that pins under the header, and the FAQ <details> rows.

#### Pricing title
The "Dock Pricing" display heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 376.95 x 64; background transparent; text Roobert 60/64 600, #121722 `color.neutral.ink`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Plan bar
The sticky plan summary bar that pins under the header while scrolling the plan comparison. Read as `pr-sticky` on the pricing page.

**Values (default).** size 1440 x 152; background #ffffff `color.neutral.white`; shadow #dedfe3 0px 0.5px 0px 0px; text Roobert 14/20 500, #121722 `color.neutral.ink`; transition transform 0.25s ease; transform translate(0px, -304px).

![Plan bar default](components/crops/pr-sticky-default.png)

#### Plan card
A pricing plan card (plan name, price and its action). Read as `plan-card` on the pricing page.

**Values (default).** size 225.75 x 300; padding 44px 32px 32px 32px; background transparent; text Roobert 20/28 500, #121722 `color.neutral.ink`; layers a.btn.btn-outline 161.8x40.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.08) 0px 0.5px 1px 0px, rgba(18, 23, 34, 0.1) 0px -1px 0px 0px inset, rgba(18, 23, 34, 0.15) 0px 0px 0px 0.5px inset 100px.

Child layers that carry the look: a 161.8x40 background #ffffff `color.neutral.white` radius 100px shadow rgba(0, 0, 0, 0.08) 0px 0.5px 1px 0px, rgba(18, 23, 34, 0.1) 0px -1px 0px 0px inset, rgba(18, 23, 34, 0.15) 0px 0px 0px 0.5px inset.

![Plan card default](components/crops/plan-card-default.png)

#### Plan name
A plan card's name (Free / Standard / Premium / Enterprise). Read as `plan-name` on the pricing page.

**Values (default).** size 39.47 x 28; background transparent; text Roobert 20/28 500, #121722 `color.neutral.ink`.

![Plan name default](components/crops/plan-name-default.png)

#### Plan price
A plan card's price figure. Read as `plan-price` on the pricing page.

**Values (default).** size 18.86 x 24; background transparent; text Roobert 12/0 600, #121722 `color.neutral.ink`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan card's Get-started action (not the fixed .pr-sticky summary bar); measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 161.75 x 40; padding 7px 20px 9px 20px; radius 100px; background #ffffff `color.neutral.white`; shadow rgba(0, 0, 0, 0.08) 0px 0.5px 1px 0px, rgba(18, 23, 34, 0.1) 0px -1px 0px 0px inset, rgba(18, 23, 34, 0.15) 0px 0px 0px 0.5px inset; text Roobert 17/22 500, #121722 `color.neutral.ink`; transition background-color 0.14s ease, box-shadow 0.14s ease |
| hover | background #fafafb |
| focus-visible | outline 2px solid #0068f9 `color.brand.blue`, offset 4px |
| pressed | background #f2f2f3 `color.neutral.wash-pressed`; shadow rgba(18, 23, 34, 0.15) 0px 0px 0px 0.5px inset, rgba(18, 23, 34, 0.12) 0px 2px 4px 0px inset |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### FAQ item
A pricing FAQ <details>/<summary> row; toggled open once for the opened state, a local UI toggle. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 706.23 x 80; padding 26px 4px; background transparent; text Roobert 20/28 500, #121722 `color.neutral.ink`; icon 20 x 20, transparent; layers span::before.faq-toggle 14pxx1.5px rgb(18, 23, 34); span::after.faq-toggle 1.5pxx14px rgb(18, 23, 34) |
| focus-visible | outline 2px solid #0068f9 `color.brand.blue`, offset 4px; layers summary 706.2x80.0 2px solid rgb(0, 104, 249) offset 4px; span::before.faq-toggle 14pxx1.5px rgb(18, 23, 34); span::after.faq-toggle 1.5pxx14px rgb(18, 23, 34) |

Child layers that carry the look: span::before 14pxx1.5px background #121722 `color.neutral.ink`; span::after 1.5pxx14px background #121722 `color.neutral.ink`.

![FAQ item default](components/crops/faq-item-default.png) ![FAQ item hover](components/crops/faq-item-hover.png) ![FAQ item focus-visible](components/crops/faq-item-focus-visible.png) ![FAQ item pressed](components/crops/faq-item-pressed.png) ![FAQ item opened](components/crops/faq-item-opened.png)

### Customers

The /customers wall of love: the "Why revenue teams love Dock" display, the category filter pills and the customer-story cards and testimonials.

#### Customers title
The "Why revenue teams love Dock" display heading. Read as `customers-h1` on the customers page.

**Values (default).** size 580 x 144; background transparent; text Roobert 70/72 700, #121722 `color.neutral.ink`.

![Customers title default](components/crops/customers-h1-default.png)

#### Filter radio
A category filter pill on the testimonial wall ("💙 All Dock love" / Sales / Enablement …); a local UI filter, one was toggled for the selected state. Read as `filter-radio` on the customers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 159.84 x 36; padding 4px 16px; radius 60px; background #d5ecff `color.brand.blue-tint`; text Roobert 18/28 400, #121722 `color.neutral.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |

![Filter radio default](components/crops/filter-radio-default.png) ![Filter radio hover](components/crops/filter-radio-hover.png) ![Filter radio focus-visible](components/crops/filter-radio-focus-visible.png) ![Filter radio pressed](components/crops/filter-radio-pressed.png)

#### Customer card
A customer-story card in the grid; measured, never followed. Read as `customer-card` on the customers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 580 x 375; padding 0px 0px 1px 0px; background transparent; text Roobert 28/30 600, #121722 `color.neutral.ink`; transition opacity 0.2s ease |
| hover, pressed | opacity 0.7 |

![Customer card default](components/crops/customer-card-default.png) ![Customer card hover](components/crops/customer-card-hover.png) ![Customer card focus-visible](components/crops/customer-card-focus-visible.png) ![Customer card pressed](components/crops/customer-card-pressed.png)

#### Testimonial
A testimonial block in the wall of love. Read as `testimonial` on the customers page.

**Values (default).** size 381.33 x 422.48; padding 16px; radius 16px; background #f4f0ff; text Roobert 18/28 400, #121722 `color.neutral.ink`; icon 67.83 x 43.41, #ffffff `color.neutral.white`.

![Testimonial default](components/crops/testimonial-default.png)

### Templates

The /templates gallery: the Templates title, the sticky category sidebar and the template cards.

#### Templates title
The "Templates" display heading. Read as `templates-h1` on the templates page.

**Values (default).** size 1062.41 x 44; background transparent; text Roobert 38/44 700, #121722 `color.neutral.ink`.

![Templates title default](components/crops/templates-h1-default.png)

#### Sidebar
The template category sidebar. Read as `templates-sidebar` on the templates page.

**Values (default).** size 264.59 x 202; padding 0px 32px 0px 0px; background transparent; text Roobert 16/20 400, #4058ff `color.brand.royal`; layers a.sidebar--link.is--current 232.6x28.0 rgba(230, 236, 252, 0.5) 8px.

Child layers that carry the look: a 232.6x28 background rgba(230, 236, 252, 0.5) radius 8px.

![Sidebar default](components/crops/templates-sidebar-default.png)

#### Sidebar link
A category link in the template sidebar; measured, never followed. Read as `sidebar-link` on the templates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 232.59 x 28; padding 3px 3px 5px 8px; radius 8px; background transparent; text Roobert 16/20 400, #121722 `color.neutral.ink`; transition opacity 0.2s ease |
| hover, pressed | background rgba(237, 237, 237, 0.48); opacity 0.7 |

![Sidebar link default](components/crops/sidebar-link-default.png) ![Sidebar link hover](components/crops/sidebar-link-hover.png) ![Sidebar link focus-visible](components/crops/sidebar-link-focus-visible.png) ![Sidebar link pressed](components/crops/sidebar-link-pressed.png)

#### Template card
A template card in the gallery; measured, never followed. Read as `template-card` on the templates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 338.13 x 307.67; padding 0px 0px 1px 0px; background transparent; text Roobert 18/23.4 500, #121722 `color.neutral.ink`; transition opacity 0.2s ease |
| hover, pressed | opacity 0.7 |

![Template card default](components/crops/template-card-default.png) ![Template card hover](components/crops/template-card-hover.png) ![Template card focus-visible](components/crops/template-card-focus-visible.png) ![Template card pressed](components/crops/template-card-pressed.png)

### Demo request

The /demo surface: the Request-a-Demo display and the HubSpot scheduler — its fields and the Schedule-demo submit paint inside a cross-origin hsforms iframe, read through the frame. Nothing was filled or submitted.

#### Demo title
The "Request a Demo" display heading. Read as `demo-h1` on the demo page.

**Values (default).** size 299.91 x 168.53; background transparent; text Roobert 80.64/84.26 600, #121722 `color.neutral.ink`.

![Demo title default](components/crops/demo-h1-default.png)

#### Demo form mount
The HubSpot scheduler mount on /demo; its fields paint inside the hsforms iframe, which is read through the frame below — nothing was ever submitted. Read as `demo-form` on the demo page.

**Values (default).** size 440 x 354; background transparent; text Roobert 16/normal 400, #121722 `color.neutral.ink`.

![Demo form mount default](components/crops/demo-form-default.png)

#### Demo field
A field inside the HubSpot demo form (read through the iframe); clicked into once for the focused state, never filled or submitted. Read as `demo-field` on the demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 411 x 48; padding 0px 18px; radius 6px; background #ffffff `color.neutral.white`; shadow rgba(18, 23, 34, 0.1) 0px 0px 0px 1px inset; text Roobert 16/normal 400, #121722 `color.neutral.ink`; placeholder rgba(18, 23, 34, 0.5) |
| focused | shadow #0068f9 0px 0px 0px 1.5px inset |

![Demo field default](components/crops/demo-field-default.png) ![Demo field focused](components/crops/demo-field-focused.png)

#### Demo submit
The Schedule-demo submit inside the HubSpot iframe; measured, never pressed. Read as `demo-submit` on the demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 411 x 48; padding 7px 14px 8px 16px; radius 6px; background #0068f9 `color.brand.blue`; shadow rgba(0, 0, 0, 0.25) 0px 0.5px 1px 0px, rgba(11, 68, 147, 0.22) 0px -1px 0px 0px inset, rgba(11, 68, 147, 0.25) 0px 0px 0px 0.5px inset; text Roobert 18/20 500, #ffffff `color.neutral.white`; transition background 0.15s ease; placeholder #ffffff `color.neutral.white` |
| hover | background #005fe4 `color.brand.blue-pressed` |
| focus-visible | outline 2px solid #0068f9 `color.brand.blue`, offset 4px |
| pressed | background #005fe4 `color.brand.blue-pressed` |

![Demo submit default](components/crops/demo-submit-default.png) ![Demo submit hover](components/crops/demo-submit-hover.png) ![Demo submit focus-visible](components/crops/demo-submit-focus-visible.png) ![Demo submit pressed](components/crops/demo-submit-pressed.png)

### Log in and sign up

The auth.dock.us cards: the login card's workspace-subdomain field + Continue (the field was focused and given sample text that was deleted again, never sent) and the signup card's email field, OAuth actions, Turnstile widget and submit — all measured, never used.

#### Login card
The sign-in card on auth.dock.us (a workspace-subdomain field + Continue); captured, never used. Read as `login-card` on the login page.

**Values (default).** size 450 x 322.8; padding 64px; radius 4px; background #ffffff `color.neutral.white`; shadow rgba(18, 23, 34, 0.25) 0px 20px 36px -18px, rgba(18, 23, 34, 0.1) 0px 0px 0px 0.5px, rgba(18, 23, 34, 0.2) 0px 1px 2px 0px; text -apple-system 24/28.8 600, #1a202c `color.neutral.ink-auth`.

![Login card default](components/crops/login-card-default.png)

#### Subdomain field
The workspace-subdomain input; focused and given sample text that was deleted again — nothing sent. Read as `subdomain-field` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 232 x 36; padding 0px 16px; background transparent; shadow rgba(0, 0, 0, 0.15) 0px 1px 2px 0px inset; outline 2px solid transparent, offset 2px; text Roobert 14/21 400, #1a202c `color.neutral.ink-auth`; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; placeholder #7d828e; layers input.chakra-input.css-1l0bxyc 232.0x36.0 rgba(0, 0, 0, 0.15) 0px 1px 2px 0px inset 2px solid rgba(0, 0, 0, 0) offset 2px |
| focused, filled | background #ffffff `color.neutral.white`; shadow none; layers none |

![Subdomain field default](components/crops/subdomain-field-default.png) ![Subdomain field focused](components/crops/subdomain-field-focused.png) ![Subdomain field filled](components/crops/subdomain-field-filled.png)

#### Continue button
The login form's Continue submit; measured, never pressed. Read as `continue-btn` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 322 x 36; padding 0px 16px; radius 4px; background #4058ff `color.brand.royal`; text Roobert 14/16.8 500, #ffffff `color.neutral.white`; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; opacity 0.4 |

**Focus not capturable.** A real keyboard focus could not be confirmed on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Continue button default](components/crops/continue-btn-default.png) ![Continue button hover](components/crops/continue-btn-hover.png) ![Continue button pressed](components/crops/continue-btn-pressed.png)

#### Signup card
The create-account card on auth.dock.us; captured, never used. Read as `signup-card` on the signup page.

**Values (default).** size 300 x 209.5; background transparent; text Roobert 13/19.5 400, #121722 `color.neutral.ink`; layers input.chakra-input.css-xw7nt4 300.0x36.0 rgb(255, 255, 255) T:1px solid rgb(193, 193, 193) / R:1px solid rgb(193, 193, 193) / B:1px solid rgb(193, 193, 193) / L:1px solid rgb(193, 193, 193) rgba(0, 0, 0, 0.15) 0px 1px 2px 0px inset 2px solid rgba(0, 0, 0, 0) offset 2px 4px; button.chakra-button.css-4f35md 300.0x43.0 rgb(64, 88, 255) T:1px solid rgb(50, 71, 207) / R:1px solid rgb(50, 71, 207) / B:1.

Child layers that carry the look: input 300x36 background #ffffff `color.neutral.white` border 1px solid #c1c1c1 radius 4px shadow rgba(0, 0, 0, 0.15) 0px 1px 2px 0px inset; button 300x43 background #4058ff `color.brand.royal` border 1px solid #3247cf radius 6px.

![Signup card default](components/crops/signup-card-default.png)

#### Signup email field
The signup email input; focused and given sample text that was deleted again — nothing sent. Read as `signup-field` on the signup page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 300 x 36; padding 0px 16px; border 1px solid #c1c1c1; radius 4px; background #ffffff `color.neutral.white`; shadow rgba(0, 0, 0, 0.15) 0px 1px 2px 0px inset; outline 2px solid transparent, offset 2px; text Roobert 14/21 400, #1a202c `color.neutral.ink-auth`; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; placeholder #7d828e |
| focused, filled | border 1px solid #4058ff `color.brand.royal`; shadow rgba(35, 60, 237, 0.17) 0px 0px 0px 2px, rgba(0, 0, 0, 0.1) 0px 1px 0px 0px inset |

![Signup email field default](components/crops/signup-field-default.png) ![Signup email field focused](components/crops/signup-field-focused.png) ![Signup email field filled](components/crops/signup-field-filled.png)

#### Human check
The Cloudflare Turnstile "Verify you are human" widget on the signup card (an iframe; its inner checkbox cannot be read and was never toggled). Read as `signup-check` on the signup page.

**Values (default).** size 1 x 1; background transparent; text Roobert 16/24 400, #1a202c `color.neutral.ink-auth`; opacity 0.

![Human check default](components/crops/signup-check-default.png)

#### Signup submit
The signup submit action; measured, never pressed. Read as `signup-submit` on the signup page.

**Known wrong; recapture needed.** The readings and crops are the "Continue with Google" OAuth button, not the email form's submit.

**Note:** This run's readings and crops describe the 'Continue with Google' OAuth action, not the email form's submit — the broad button+text selector matched it first. The selector was fixed in measure.mjs (button[type=submit] first, exact-label fallback) and a re-measure is queued.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 300 x 36; padding 0px 16px; border 1px solid #e2e8f0; radius 4px; background transparent; text Roobert 14/16.8 500, #000000; transition background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; icon 16 x 16, #000000 |
| hover, pressed | background rgba(239, 241, 255, 0.8) |

![Signup submit default](components/crops/signup-submit-default.png) ![Signup submit hover](components/crops/signup-submit-hover.png) ![Signup submit focus-visible](components/crops/signup-submit-focus-visible.png) ![Signup submit pressed](components/crops/signup-submit-pressed.png)

### Footer

The marketing footer: link columns, legal and the GDPR / SOC 2 trust badges.

#### Footer
The marketing footer: link columns, legal, social and the trust badges. Read as `footer` on the home page.

**Values (default).** size 1440 x 820.3; background #ffffff `color.neutral.white`; text DockWebflowNavigation 14.5/20 400, #121722 `color.neutral.ink`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 127.44 x 22.39; background transparent; text DockWebflowNavigation 16/22.4 400, #121722 `color.neutral.ink` |

**Focus not capturable.** A real keyboard focus could not be confirmed on this element (`focus-visible` recorded `via: focus failed`; the via was later rewritten by hand, not re-measured), so its focus look is uncaptured — not measured as absent.

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Trust badge
A compliance badge in the footer (GDPR / SOC 2 …). Read as `trust-badge` on the home page.

**Values (default).** size 96.33 x 16; background transparent; text DockWebflowNavigation 12.5/15 400, rgba(18, 23, 34, 0.8) `color.neutral.muted`; layers span.trust-badge-icon 16.0x16.0 color(srgb 0.0705882 0.0901961 0.133333 / 0.8).

Child layers that carry the look: span 16x16 background rgba(18, 23, 34, 0.8) `color.neutral.muted`.

![Trust badge default](components/crops/trust-badge-default.png)

### Mobile (390 wide)

The same surface at phone width: the header shrinks to logo + Menu toggle inside the same web component, and the menu opens as an expanded panel with nav rows and the auth actions.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 350 x 76; padding 16px 24px; background transparent; text DockWebflowNavigation 16/19.2 500, #121722 `color.neutral.ink`; icon 16 x 16, #121722 `color.neutral.ink`; layers summary.button.navigation-toggle 94.5x44.0 rgb(255, 255, 255) color(srgb 0.0705882 0.0901961 0.133333 / 0.2) 0px 0px 0px 0.5px inset 100px; div.navigation-content 94.5x386.0 rgb(255, 255, 255) color(srgb 0.0705882 0.0901961 0.133333 / 0.2) 0px 0px 0px 0.5px, color(srgb 0.0705882 0.0901961 0.133333 / 0.05) 0px 1px 3px 0px, color(srgb 0.0705882 0.0901961 0.133333 / 0.05) 0px 3px 7px 0px 19.1px; div..

Child layers that carry the look: summary 94.5x44 background #ffffff `color.neutral.white` radius 100px shadow rgba(18, 23, 34, 0.2) `color.neutral.hairline` 0px 0px 0px 0.5px inset; div 94.5x386 background #ffffff `color.neutral.white` radius 19.1px shadow rgba(18, 23, 34, 0.2) `color.neutral.hairline` 0px 0px 0px 0.5px, rgba(18, 23, 34, 0.05) 0px 1px 3px 0px, rgba(18, 23, 34, 0.05) 0px 3px 7px 0px; div 46.5x286.4 background #ffffff `color.neutral.white`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The header Menu <summary> toggle inside dock-site-header. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 94.53 x 44; padding 9px 14px 10px 16px; radius 100px; background #ffffff `color.neutral.white`; shadow rgba(18, 23, 34, 0.2) 0px 0px 0px 0.5px inset; text DockWebflowNavigation 16/19.2 500, #121722 `color.neutral.ink`; transition background-color 0.14s ease, box-shadow 0.14s ease; icon 16 x 16, #121722 `color.neutral.ink`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The opened mobile navigation panel inside dock-site-header (the expanded list of nav groups and actions). Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 350 x 386; padding 8px 24px 24px 24px; radius 19.1px; background #ffffff `color.neutral.white`; shadow rgba(18, 23, 34, 0.2) 0px 0px 0px 0.5px, rgba(18, 23, 34, 0.05) 0px 1px 3px 0px, rgba(18, 23, 34, 0.05) 0px 3px 7px 0px; text DockWebflowNavigation 18/21.6 500, #121722 `color.neutral.ink`; icon 12 x 12, #121722 `color.neutral.ink`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
A nav item inside the opened mobile menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 302 x 56; padding 16px 0px; background transparent; text DockWebflowNavigation 18/21.6 500, #121722 `color.neutral.ink`; icon 12 x 12, #121722 `color.neutral.ink` |
| pressed | outline 2px solid rgba(18, 23, 34, 0.6) `measured.focus-ring`, offset 4px; layers summary.nav-trigger 302.0x56.0 2px solid color(srgb 0.0705882 0.0901961 0.133333 / 0.6) offset 4px |

**Focus not capturable.** A real keyboard focus could not be confirmed on this element (`focus-visible` recorded `via: focus failed`; the via was later rewritten by hand, not re-measured), so its focus look is uncaptured — not measured as absent.

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Known wrong; recapture needed.** The mobile menu was still open when it was read (Escape does not close its `<details>`), so the crop can show the menu over the headline; the computed values are the h1's own.

**Values (default).** size 326 x 68.75; background transparent; text DockWebflowHome 29.25/34.37 600, #ffffff `color.neutral.white`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Dock wordmark, the mega-menu's feature glyphs, the Google/Microsoft provider glyphs, the Cloudflare mark and the social glyphs) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Everything behind the auth cards — the Dock workspace, its rooms, deal portals, content library, learning paths and account settings — was never reached. auth.dock.us/login shows only the workspace-subdomain card and auth.dock.us/sign-up the signup card; their fields were focused and given sample text that was deleted again, and the Continue / Continue-with-Email / OAuth actions were never pressed. What the workspace looks like or how it behaves is not documented here — the marketing pages' claims about it were never verified.

### Pages

- **Log in, sign up, demo and sales.** Log in, Start for free, Get started, Request demo, Schedule demo and Talk to sales were measured or screenshotted, never followed; no account was created and no form was submitted.
- **OAuth providers.** Continue with Google / Microsoft on the signup card were never pressed — they leave for the providers' flows.
- **Human check.** The Cloudflare Turnstile widget on the signup card stayed a 1px placeholder headless (it never painted its checkbox); recorded at its painted size, never toggled.
- **The read-only MCP prompt fields** (input/textarea aria-label "Dock setup prompt" / "Selected Dock AI prompt") stay display:none inside the collapsed label.mcp-prompt-field; the visible .mcp-prompt widget and its Copy action were measured instead.
- **External surfaces** (developers.dock.us, the help centre, Vanta trust, status and social profiles) are linked from the site but were never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface (the demo form's validation states inside its iframe were never triggered).
- **The mega-menu is inside a shadow root**: every state that needs it open re-opens the Product <summary> first; a state read while the panel had closed would be recorded missing, not absent.

### Themes

The public surface paints light only — the marketing pages and the auth cards are all white-surfaced, and the light/dark resolutions in raw/css-vars.json are identical apart from one menu value. What the export calls "dark" is the deep-blue islands the light site paints — the #002fa6 hero band (an oklch gradient) and the auth signup's #242d7d -> #3542af testimonial pane — with their white text, white-alpha ghost fills and 40% sky inset rings. Not a user toggle.

### Fonts

- **Roobert** (400/500/600/700 seen) is served same-origin as DockWebflowHome / DockWebflowNavigation subsets on the marketing site and under its own name on pricing, customers, templates, /demo and auth.dock.us; the @font-face src list is harvested in raw/css-vars.json. The style guide falls back to system sans — the webfonts are licensed, not shipped.

### Screenshots

- The hero band is a painted oklch gradient layer (page-placeholder / hero-intro), not a flat fill — the token is its #002fa6 base; the band's texture is the product's artwork.
- mobile-home's full-page capture exceeded one chunk and was stitched from parts (sidecars record the boundary).
- The customer-story imagery, template artwork, video thumbnails and testimonial portraits in the screenshots are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Template artwork, customer logos and quotes, plan feature lists, marketing copy and the terms text are the product's content; only frames and components were measured.
