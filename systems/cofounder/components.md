# Cofounder components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from cofounder.co on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, paid for or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (39 components, 86 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `TT Neoris 15/23 410, #262323b3`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (87 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`; every public route paints the same light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages (1x on desktop, 2x on mobile); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| How-to: start | `/how-to/start` | [default](screenshots/howto-start-light-default.png), [full](screenshots/howto-start-light-full.png) |
| How-to: build | `/how-to/build` | [default](screenshots/howto-build-light-default.png), [full](screenshots/howto-build-light-full.png) |
| How-to: scale | `/how-to/scale` | [default](screenshots/howto-scale-light-default.png), [full](screenshots/howto-scale-light-full.png) |
| How-to: sell | `/how-to/sell` | [default](screenshots/howto-sell-light-default.png), [full](screenshots/howto-sell-light-full.png) |
| Resources | `/resources` | [default](screenshots/resources-light-default.png), [full](screenshots/resources-light-full.png) |
| Support | `/support` | [default](screenshots/support-light-default.png), [full](screenshots/support-light-full.png) |
| Privacy | `/privacy-policy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Terms | `/terms` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| Sign-in (boundary) | `app.cofounder.co/os/login` | [default](screenshots/signin-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| How-to start, phone | `/how-to/start` | [default](screenshots/mobile-howto-start-light-default.png), [full](screenshots/mobile-howto-start-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu, open | bar, phone | the hamburger's own press | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-open](#m-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 17 components were given a real keyboard focus. 16 show a visible focus state: `nav-item` (1px auto #101010, offset 1px), `nav-cta` (1px auto #101010, offset 1px), `hero-cta` (1px auto #101010, offset 1px), `hero-prompt-btn` (2px solid #ffffff `color.white`, offset 4px), `cta-dark` (2px solid rgba(38, 35, 35, 0.8) `color.ink.80`, offset 4px), `cta-light` (1px auto #101010, offset 1px), `tool-tab` (1px solid oklab(0.999994 0.0000455677 0.0000200868 / 0.8), offset 2px), `tool-tab-off` (1px solid oklab(0.999994 0.0000455677 0.0000200868 / 0.8), offset 2px), `tool-button` (2px solid rgba(38, 35, 35, 0.8) `color.ink.80`, offset 2px), `case-study` (1px auto #101010, offset 1px), `footer-link` (1px auto #101010, offset 1px), `footer-social` (1px auto #101010, offset 1px), `footer-cta` (1px auto #101010, offset 1px), `plan-card` (1px auto #101010, offset 1px), `signin-back` (visible change in boxShadow), `m-menu-link` (1px auto #e59700, offset 1px). The other 1 show no change a keyboard user can see: `signin-button`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): the controls hold their hover step through press on this surface — hover and pressed read as the same painted step. Nothing a real press would submit, navigate or write (the copy-prompt button writes the clipboard; the plan cards and CTAs navigate to the app) was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.02s | `ease-in-out` | border-color, box-shadow | header, m-header |
| 0.06s | `ease` | color, font-weight | nav-item |
| 0.12s | `ease-out` | background-color | header, m-header |
| 0.14s | `ease-out` | background-color, box-shadow | cta-light, footer-cta, footer-social, hero-cta |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color, transform | signin-back, tool-button |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, backdrop-filter, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | signin-button |
| 0.2s | `ease-out` | color | footer-link |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 640 x 594 | 1px solid #dee2de `color.borderCard` | 16px | #fbfbf8 `color.surfaceRaised` | rgba(255, 255, 255, 0.35) 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset, rgba(0, 0, 0, 0.25) 0px 0px 2px 0px, rgba(232, 231, 230, 0.32) 0px 0px 0px 4px | 0 |
| [Tool button](#tool-button) | 340 x 47 | 1px solid oklab(0 0 0 / 0.1) | 10px | oklab(0.999994 0.0000455677 0.0000200868 / 0.6) | rgba(255, 255, 255, 0.8) 0px 1px 0px 0px inset | 12px 16px |
| [Case study card](#case-study-card) | 182 x 96 | - | 10px | #f3f3f0 `color.tile` | #ffffff 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.12) 1px 1px 4px 0px inset, rgba(255, 255, 255, 0.7) -2px -2px 3px 0px inset | 6px |
| [Logo tile](#logo-tile) | 170 x 84 | - | 10px | #f3f3f0 `color.tile` | #ffffff 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.12) 1px 1px 4px 0px inset, rgba(255, 255, 255, 0.7) -2px -2px 3px 0px inset | 28px |

## Components

### Shell and navigation

The fixed glass site header: wordmark, the flat nav-link row and the Run-a-company CTA.

#### Nav bar
The fixed site header (position:fixed, transparent at top, border+shadow on scroll): logo, flat nav links, Run-a-company CTA. Read as `header` on the home page.

**Values (default).** size 1440 x 91; border B: 1px solid rgba(232, 231, 230, 0); background transparent; shadow rgba(255, 255, 255, 0) 0px 1px 0px 0px; text neoris 15/22.5 410, #fbfbf8 `color.surfaceRaised`; transition border-color 0.02s ease-in-out, box-shadow 0.02s ease-in-out, background-color 0.12s ease-out.

![Nav bar default](components/crops/header-default.png)

#### Logo
The Cofounder mark+wordmark home anchor in the header. Read as `logo` on the home page.

**Values (default).** size 126 x 26; background transparent; wrapper header.site-header.fixed: shadow rgba(255, 255, 255, 0) 0px 1px 0px 0px; text neoris 16/24 400, #171717 `color.ink.90`.

![Logo default](components/crops/logo-default.png)

#### Nav link
A flat nav link (nav-link, 15px/410 weight, text-surface-raised): Start/Build/Sell/Scale/Resources/Pricing. Read as `nav-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 46.75 x 22.5; padding 0px 6px; background transparent; text neoris 15/22.5 410, #fbfbf8 `color.surfaceRaised`; transition color 0.06s ease, font-weight 0.06s ease |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.nav-link.relative: size 46.8x22.5; outline 1px auto rgb(16, 16, 16) offset 1px |

![Nav link default](components/crops/nav-item-default.png) ![Nav link hover](components/crops/nav-item-hover.png) ![Nav link focus-visible](components/crops/nav-item-focus-visible.png) ![Nav link pressed](components/crops/nav-item-pressed.png)

#### Nav CTA
The header "Run a company" pill linking to app.cofounder.co/os; measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 130 x 41; padding 0px 12px; radius 8px; background transparent; text neoris 15/22.5 460, #1a1a1a |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.group.relative: size 130.0x41.0; radius 8px; outline 1px auto rgb(16, 16, 16) offset 1px |

Child layers that carry the look: span 130x41 image linear-gradient(rgba(32, 32, 32, 0.1) 0%, rgba(32, 32, 32, 0.1) 100%), linear-gradient(#4f border 1px solid #383838 radius 8px shadow rgba(64, 64, 64, 0.12) 0px 0px 0px 1px, rgba(255, 255, 255, 0.24) 0px 2px 0px 0px inset, rgba(0, 0, 0, 0.25) 0px -0.5px 2px 0px inset, rgba(0, 0, 0, 0.03) 0px 2px 8px 0px, rgba(0, 0, 0, 0.16) 0px 3px 4px 0px; span 130x41 background #f1f1ee border 1px solid rgba(32, 32, 32, 0.1) radius 8px shadow rgba(0, 0, 0, 0.5) 0px 1px 1px 0px, rgba(255, 255, 255, 0.23) 0px 0px 0px 1px; span 130x41 background #e7e7e1 border 1px solid rgba(32, 32, 32, 0.1) radius 8px shadow rgba(255, 255, 255, 0.35) 0px 0px 0.357px 1.5px inset.

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

### Home

The pixel-art hero (Run an entire company with AI), the white and glass hero buttons, the #1a6fd1 tools band with its tab toggles, the tool picker buttons, case-study cards, the campaign carousel and the logo rows.

#### Hero title
"Cofounder lets you run an entire company with AI" — the hero headline (hero-gradient-text, 46px/108%). Read as `hero-title` on the home page.

**Values (default).** size 580 x 99.38; background transparent; image linear-gradient(#ffffff `color.white` 0%, rgba(255, 255, 255, 0.9) 100%); text neoris 46/49.68 400, #ffffff `color.white`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero CTA
The hero "Run a company" anchor linking to app.cofounder.co/os; measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 127.95 x 41; padding 0px 12px; border 1px solid rgba(32, 32, 32, 0.1); radius 8px; background #f5f5f2 `color.surface`; shadow rgba(0, 0, 0, 0.06) 0px 2px 3px 0px, rgba(255, 255, 255, 0.35) 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset; text neoris 15/22.5 460, #171717 `color.ink.90`; transition background-color 0.14s ease-out, box-shadow 0.14s ease-out |
| hover | background #ededea; child paint a.group.relative: background #ededea |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.group.relative: outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | background #ededea; child paint a.group.relative: background #ededea |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Prompt button
The glass "copy the setup prompt" hero button (glass-hero-btn, backdrop-blur 24px); never pressed — it writes the clipboard. Hover/focus/forced states only. Read as `hero-prompt-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 179.56 x 41; padding 0px 10px; radius 8px; background transparent; text neoris 15/22.5 460, #ffffff `color.white`; icon 16 x 16, #ffffff `color.white` |
| focus-visible | outline 2px solid #ffffff `color.white`, offset 4px; child paint button.group.relative: size 179.6x41.0; radius 8px; outline 2px solid rgb(255, 255, 255) offset 4px |

Child layers that carry the look: span 179.6x41 background rgba(255, 255, 255, 0.05) radius 8px; span 179.6x41 image linear-gradient(rgba(0, 0, 0, 0.12), rgba(0, 0, 0, 0.2)) radius 8px shadow rgba(0, 0, 0, 0.12) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.1) 0px -1px 2px 0px inset, rgba(255, 255, 255, 0.24) 0px 1px 1px 0px inset; span 179.6x41 image linear-gradient(rgba(0, 0, 0, 0.08), rgba(0, 0, 0, 0.15)) radius 8px shadow rgba(0, 0, 0, 0.12) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.1) 0px -1px 2px 0px inset, rgba(255, 255, 255, 0.6) 0px 2px 1px 0px inset.

![Prompt button default](components/crops/hero-prompt-btn-default.png) ![Prompt button hover](components/crops/hero-prompt-btn-hover.png) ![Prompt button focus-visible](components/crops/hero-prompt-btn-focus-visible.png) ![Prompt button pressed](components/crops/hero-prompt-btn-pressed.png)

#### Dark CTA
A cta-btn-dark control — the dark button style used for mid-page actions. Read as `cta-dark` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 183.7 x 44; padding 0px 16px; border 1px solid #383838; radius 8px; background transparent; image linear-gradient(rgba(32, 32, 32, 0.1) 0%, rgba(32, 32, 32, 0.1) 100%), linear-gradient(#4f4f4f 0%, rgba(32, 32, 32, 0.85) `color.ctaDark` 100%); shadow rgba(64, 64, 64, 0.12) 0px 0px 0px 1px, rgba(255, 255, 255, 0.24) 0px 2px 0px 0px inset, rgba(0, 0, 0, 0.25) 0px -0.5px 2px 0px inset, rgba(0, 0, 0, 0.03) 0px 2px 8px 0px, rgba(0, 0, 0, 0.16) 0px 3px 4px 0px; text neoris 15/22.5 460, rgba(255, 255, 255, 0.9); icon 16 x 16, rgba(255, 255, 255, 0.9) |
| focus-visible | outline 2px solid rgba(38, 35, 35, 0.8) `color.ink.80`, offset 4px; child paint a.group.relative: outline 2px solid rgba(38, 35, 35, 0.8) offset 4px |

![Dark CTA default](components/crops/cta-dark-default.png) ![Dark CTA hover](components/crops/cta-dark-hover.png) ![Dark CTA focus-visible](components/crops/cta-dark-focus-visible.png) ![Dark CTA pressed](components/crops/cta-dark-pressed.png)

#### Light CTA
A btn-light-surface control — the light pill button style. Read as `cta-light` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 127.95 x 41; padding 0px 12px; border 1px solid rgba(32, 32, 32, 0.1); radius 8px; background #f5f5f2 `color.surface`; shadow rgba(0, 0, 0, 0.06) 0px 2px 3px 0px, rgba(255, 255, 255, 0.35) 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset; text neoris 15/22.5 460, #171717 `color.ink.90`; transition background-color 0.14s ease-out, box-shadow 0.14s ease-out |
| hover | background #ededea; child paint a.group.relative: background #ededea |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.group.relative: outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | background #ededea; child paint a.group.relative: background #ededea |

![Light CTA default](components/crops/cta-light-default.png) ![Light CTA hover](components/crops/cta-light-hover.png) ![Light CTA focus-visible](components/crops/cta-light-focus-visible.png) ![Light CTA pressed](components/crops/cta-light-pressed.png)

#### Tools band
The #1a6fd1 "All the tools and systems" band with the tools diagram and tab toggles. Read as `blue-section` on the home page.

**Values (default).** size 1425 x 1221.81; background #1a6fd1 `color.band`; image url(…); text neoris 40/46 400, #ffffff `color.white`; icon 110 x 6, #ffffff `color.white`.

![Tools band default](components/crops/blue-section-default.png)

#### Tools tab (selected)
The selected aria-pressed tab in the tools band (text-white selected). Read as `tool-tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 234.66 x 44.81; background transparent; text neoris 16/22.4 460, #ffffff `color.white` |
| focus-visible | size 234.67 x 44.81; outline 1px solid oklab(0.999994 0.0000455677 0.0000200868 / 0.8), offset 2px; child paint button.group.min-w-0: size 234.7x44.8; outline 1px solid oklab(0.999994 0.0000455677 0.0000200868 / 0.8) offset 2px; span.absolute.left-0: size 1.0x7.8 |

Child layers that carry the look: span 1x44 background rgba(255, 255, 255, 0.35); span::after 1pxx44px background #2688dd; span 1x11 background #ffffff `color.white`.

![Tools tab (selected) default](components/crops/tool-tab-default.png) ![Tools tab (selected) focus-visible](components/crops/tool-tab-focus-visible.png)

#### Tools tab (unselected)
An unselected aria-pressed tab (text-white/40, hover white/60); never pressed — it swaps the diagram. Read as `tool-tab-off` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 234.66 x 44.81; background transparent; text neoris 16/22.4 460, oklab(0.999994 0.0000455678 0.0000200868 / 0.4) |
| hover | text neoris 16/22.4 460, oklab(0.999994 0.0000455677 0.0000200868 / 0.6) |
| focus-visible | outline 1px solid oklab(0.999994 0.0000455677 0.0000200868 / 0.8), offset 2px; child paint button.group.min-w-0: size 234.7x44.8; outline 1px solid oklab(0.999994 0.0000455677 0.0000200868 / 0.8) offset 2px |

Child layers that carry the look: span 1x44 background rgba(255, 255, 255, 0.35); span::after 1pxx44px background #2688dd.

![Tools tab (unselected) default](components/crops/tool-tab-off-default.png) ![Tools tab (unselected) hover](components/crops/tool-tab-off-hover.png) ![Tools tab (unselected) focus-visible](components/crops/tool-tab-off-focus-visible.png)

#### Tool button
A tool/agent picker button (border-black/10 bg-white/60 rounded-[10px], hover white-fill swap). Read as `tool-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 340 x 47; padding 12px 16px; border 1px solid oklab(0 0 0 / 0.1); radius 10px; background oklab(0.999994 0.0000455677 0.0000200868 / 0.6); shadow rgba(255, 255, 255, 0.8) 0px 1px 0px 0px inset; text IBM Plex Mono 10/15 400, rgba(38, 35, 35, 0.5) `color.ink.50`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(38, 35, 35, 0.5) `color.ink.50` |
| hover | border 1px solid oklab(0 0 0 / 0.2); background #ffffff `color.white`; child paint button.group.flex: background #ffffff `color.white`; border 1px solid oklab(0 0 0 / 0.2) |
| focus-visible | outline 2px solid rgba(38, 35, 35, 0.8) `color.ink.80`, offset 2px; child paint button.group.flex: outline 2px solid rgba(38, 35, 35, 0.8) offset 2px |
| pressed | border 1px solid oklab(0 0 0 / 0.2); background #ffffff `color.white`; child paint button.group.flex: background #ffffff `color.white`; border 1px solid oklab(0 0 0 / 0.2) |

![Tool button default](components/crops/tool-button-default.png) ![Tool button hover](components/crops/tool-button-hover.png) ![Tool button focus-visible](components/crops/tool-button-focus-visible.png) ![Tool button pressed](components/crops/tool-button-pressed.png)

#### Case study card
A case-study card anchor. Read as `case-study` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 182 x 96; padding 6px; background transparent; text neoris 16/24 400, #171717 `color.ink.90` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.flex.items-center: size 182.0x96.0; outline 1px auto rgb(16, 16, 16) offset 1px |

Child layers that carry the look: div 170x84 background #f3f3f0 `color.tile` radius 10px shadow #ffffff `color.white` 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.12) 1px 1px 4px 0px inset, rgba(255, 255, 255, 0.7) -2px -2px 3px 0px inset.

![Case study card default](components/crops/case-study-default.png) ![Case study card hover](components/crops/case-study-hover.png) ![Case study card focus-visible](components/crops/case-study-focus-visible.png) ![Case study card pressed](components/crops/case-study-pressed.png)

#### Carousel arrow
A campaign-carousel arrow button. Read as `carousel-prev` on the home page.

Not on the page when it was captured.

#### Logo tile
A customer logo tile (170x84) in the social-proof row. Read as `logo-tile` on the home page.

**Values (default).** size 170 x 84; padding 28px; radius 10px; background #f3f3f0 `color.tile`; shadow #ffffff 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.12) 1px 1px 4px 0px inset, rgba(255, 255, 255, 0.7) -2px -2px 3px 0px inset; text neoris 16/24 400, #171717 `color.ink.90`.

![Logo tile default](components/crops/logo-tile-default.png)

#### Tool logo pill
An agent-tool logo pill (ChatGPT/Claude/Cursor/Codex icons in /agent-icons/). Read as `logo-pill` on the home page.

**Values (default).** size 92.45 x 24.16; padding 5px 10px; border 1px solid #383838; radius 20px; background transparent; image linear-gradient(rgba(32, 32, 32, 0.1) 0%, rgba(32, 32, 32, 0.1) 100%), linear-gradient(#4f4f4f 0%, rgba(32, 32, 32, 0.85) `color.ctaDark` 100%); shadow rgba(64, 64, 64, 0.12) 0px 0px 0px 1px, rgba(255, 255, 255, 0.24) 0px 2px 0px 0px inset, rgba(0, 0, 0, 0.25) 0px -0.5px 2px 0px inset, rgba(0, 0, 0, 0.03) 0px 2px 8px 0px, rgba(0, 0, 0, 0.16) 0px 3px 4px 0px; text neoris 13/18.2 460, oklab(0.999994 0.0000455678 0.0000200868 / 0.9); icon 9.6 x 9.6, #171717 `color.ink.90`.

![Tool logo pill default](components/crops/logo-pill-default.png)

#### Section title
A section heading under the hero (Neoris, 28-40px responsive). Read as `section-title` on the home page.

**Values (default).** size 1052 x 92; background transparent; text neoris 40/46 400, rgba(38, 35, 35, 0.8) `color.ink.80`.

![Section title default](components/crops/section-title-default.png)

#### Page ground
The body element painted fill — the page ground (--background #f5f5f2). Read as `page-ground` on the home page.

**Values (default).** size 1425 x 9446.42; background #f5f5f2 `color.surface`; text neoris 15/22.5 460, rgba(32, 32, 32, 0.4).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Pricing

The pricing route: the whole-card plan anchors with the hover-revealed CTA chip.

#### Pricing title
The visible pricing headline (the h1 is sr-only). Read as `pricing-title` on the pricing page.

**Values (default).** size 1032 x 69; background transparent; text neoris 46/69 400, rgba(38, 35, 35, 0.8) `color.ink.80`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Plan card
A whole-card plan anchor (pricing-card-group -> pricing-card): border-border-card bg-surface-raised rounded-2xl, hover reveals the hidden CTA chip (no lift transition - the anchor computes 0s). Links to app.cofounder.co; never followed. Read as `plan-card` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 640 x 594; background transparent; text neoris 15/21 460, rgba(38, 35, 35, 0.7) `color.ink.70`; icon 21 x 21, #171717 `color.ink.90` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.pricing-card-group.group: size 640.0x594.0; outline 1px auto rgb(16, 16, 16) offset 1px |

Child layers that carry the look: div 640x594 background #fbfbf8 `color.surfaceRaised` border 1px solid #dee2de `color.borderCard` radius 16px shadow rgba(255, 255, 255, 0.35) 0px 0px 0.357px 1.5px inset, #ffffff `color.white` 0px 2px 0px 0px inset, rgba(0, 0, 0, 0.25) 0px 0px 2px 0px, rgba(232, 231, 230, 0.32) 0px 0px 0px 4px; span 89.3x30.8 image linear-gradient(rgba(32, 32, 32, 0.1) 0%, rgba(32, 32, 32, 0.1) 100%), linear-gradient(#4f border 1px solid #383838 radius 8px shadow rgba(64, 64, 64, 0.12) 0px 0px 0px 1px, rgba(255, 255, 255, 0.24) 0px 2px 0px 0px inset, rgba(0, 0, 0, 0.25) 0px -0.5px 2px 0px inset, rgba(0, 0, 0, 0.03) 0px 2px 8px 0px, rgba(0, 0, 0, 0.16) 0px 3px 4px 0px; div 614x220 background #f5f5f2 `color.surface` border 1px solid #dee2de `color.borderCard` radius 8px.

![Plan card default](components/crops/plan-card-default.png) ![Plan card hover](components/crops/plan-card-hover.png) ![Plan card focus-visible](components/crops/plan-card-focus-visible.png) ![Plan card pressed](components/crops/plan-card-pressed.png)

#### Plan name
The plan label row inside a pricing card (15px ink-muted). Read as `plan-name` on the pricing page.

**Values (default).** size 71.36 x 21; background transparent; wrapper div.pricing-card.relative: shadow rgba(255, 255, 255, 0.35) 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset, rgba(0, 0, 0, 0.25) 0px 0px 2px 0px, rgba(232, 231, 230, 0.32) 0px 0px 0px 4px; text neoris 15/21 460, rgba(38, 35, 35, 0.7) `color.ink.70`.

![Plan name default](components/crops/plan-name-default.png)

#### Revealed CTA chip
The "Get started" cta-btn-dark chip a plan card reveals on hover; exists only while the card is hovered — held open by the card's own hover, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 89.33 x 30.8; padding 6px 12px; border 1px solid #383838; radius 8px; background transparent; image linear-gradient(rgba(32, 32, 32, 0.1) 0%, rgba(32, 32, 32, 0.1) 100%), linear-gradient(#4f4f4f 0%, rgba(32, 32, 32, 0.85) `color.ctaDark` 100%); shadow rgba(64, 64, 64, 0.12) 0px 0px 0px 1px, rgba(255, 255, 255, 0.24) 0px 2px 0px 0px inset, rgba(0, 0, 0, 0.25) 0px -0.5px 2px 0px inset, rgba(0, 0, 0, 0.03) 0px 2px 8px 0px, rgba(0, 0, 0, 0.16) 0px 3px 4px 0px; text neoris 12/16.8 460, oklab(0.999994 0.0000455678 0.0000200868 / 0.9) |

![Revealed CTA chip default](components/crops/plan-cta-default.png) ![Revealed CTA chip pressed](components/crops/plan-cta-pressed.png)

### How-to guides

The how-to guides: headlines, content sections and the Neoris card titles.

#### Guide title
The how-to guide headline (40px Neoris at 1440). Read as `howto-title` on the how-to page.

**Values (default).** size 620 x 46; background transparent; text neoris 40/46 400, rgba(38, 35, 35, 0.8) `color.ink.80`.

![Guide title default](components/crops/howto-title-default.png)

#### Guide section
The how-to guide content column. Read as `howto-section` on the how-to page.

Not on the page when it was captured.

#### Guide heading
A section heading inside the guide (24px/530). Read as `howto-heading` on the how-to page.

**Values (default).** size 620 x 33.59; background transparent; text neoris 24/33.6 530, rgba(38, 35, 35, 0.8) `color.ink.80`.

![Guide heading default](components/crops/howto-heading-default.png)

#### Card title
A step/card title inside the guide (15px/530). Read as `howto-card-title` on the how-to page.

**Values (default).** size 620 x 21; background transparent; text neoris 15/21 530, rgba(38, 35, 35, 0.8) `color.ink.80`.

![Card title default](components/crops/howto-card-title-default.png)

### App sign-in (boundary)

app.cofounder.co/os's public login surface — measured at rest; nothing was typed, signed into or submitted.

#### Sign-in card
The app.cofounder.co/os login surface: the sign-in card the app paints. Measured at rest, never submitted. Read as `signin-card` on the sign-in page.

**Values (default).** size 1430 x 900; background #fcfcf9; text mondwest 32/38 400, #202020 `color.ink.ui`; icon 16 x 16, rgba(32, 32, 32, 0.72).

![Sign-in card default](components/crops/signin-card-default.png)

#### Continue button
A "Continue with" OAuth button on the sign-in card; measured never pressed. Read as `signin-button` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 384 x 52; padding 24px; border 2px solid #4f4f4f; radius 3.35544e+07px; background transparent; image linear-gradient(to top, #0f0f0f, #262626); shadow rgba(0, 0, 0, 0.03) 0px 13px 5px 0px, rgba(0, 0, 0, 0.07) 0px 7px 4px 0px, rgba(0, 0, 0, 0.14) 0px 3px 3px 0px, rgba(0, 0, 0, 0.19) 0px 1px 2px 0px, rgba(255, 255, 255, 0.2) 0px 0px 0.357px 1.071px inset, rgba(255, 255, 255, 0.15) 0px 0px 0.357px 1.071px inset; text ttNeoris 14/19.6 500, #ffffff `color.white`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1), transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), translate 0.2s cubic-bezier(0.4, 0, 0.2, 1), scale 0.2s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.2s cubic-bezier(0.4, 0, 0.2, 1), filter 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.2s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.2s cubic-bezier(0.4, 0, 0.2, 1), display 0.2s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.2s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.2s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #ffffff `color.white` |
| hover, pressed | shadow none; opacity 0.9 |

![Continue button default](components/crops/signin-button-default.png) ![Continue button hover](components/crops/signin-button-hover.png) ![Continue button focus-visible](components/crops/signin-button-focus-visible.png) ![Continue button pressed](components/crops/signin-button-pressed.png)

#### Back link
The "Back to Cofounder" link returning to the marketing site. Read as `signin-back` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; radius 3.35544e+07px; background transparent; text anotherSans 14/19.6 400, rgba(32, 32, 32, 0.72); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(32, 32, 32, 0.72) |
| hover | background rgba(32, 32, 32, 0.05); text anotherSans 14/19.6 400, #202020 `color.ink.ui`; icon 16 x 16, #202020 `color.ink.ui`; child paint a.absolute.left-4: size 40.0x40.0; background rgba(32, 32, 32, 0.05); radius 3.35544e+07px |
| focus-visible | shadow rgba(32, 32, 32, 0.1) 0px 0px 0px 2px; child paint a.absolute.left-4: size 40.0x40.0; radius 3.35544e+07px; shadow rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(32, 32, 32, 0.1) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px |
| pressed | background rgba(32, 32, 32, 0.05); text anotherSans 14/19.6 400, #202020 `color.ink.ui`; icon 16 x 16, #202020 `color.ink.ui`; child paint a.absolute.left-4: size 40.0x40.0; background rgba(32, 32, 32, 0.05); radius 3.35544e+07px |

![Back link default](components/crops/signin-back-default.png) ![Back link hover](components/crops/signin-back-hover.png) ![Back link focus-visible](components/crops/signin-back-focus-visible.png) ![Back link pressed](components/crops/signin-back-pressed.png)

### Footer

The footer band: the Run-a-company CTA card, link columns and social icons.

#### Footer
The footer band (footer-bg): the Run-a-company CTA card, link columns, social icons and legal row. Read as `footer` on the home page.

**Values (default).** size 1425 x 749.39; background transparent; text neoris 40/46 400, rgba(38, 35, 35, 0.8) `color.ink.80`; icon 15 x 15, rgba(38, 35, 35, 0.5) `color.ink.50`.

Child layers that carry the look: div 1052x610.3 image radial-gradient(circle, rgba(255, 255, 255, 0) 30%, #f5f5f2 `color.surface` 80%); div 0x0 background rgba(251, 251, 248, 0.8) radius 16px shadow rgba(255, 255, 255, 0.35) 0px 0px 0.357px 1.5px inset, #ffffff `color.white` 0px 2px 0px 0px inset, rgba(0, 0, 0, 0.25) 0px 0px 2px 0px, rgba(232, 231, 230, 0.32) 0px 0px 0px 4px; div 0x0 image linear-gradient(rgba(255, 255, 255, 0.06) 0%, rgba(255, 255, 255, 0.03) 100%) radius 8px shadow rgba(0, 0, 0, 0.12) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.1) 0px -1px 2px 0px inset, rgba(255, 255, 255, 0.24) 0px 1px 1px 0px inset.

![Footer default](components/crops/footer-default.png)

#### Footer link
A link in a footer link column (footer-link) — the md:hidden mobile CTA copy is skipped. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 46.06 x 19; background transparent; text neoris 15/21 460, rgba(38, 35, 35, 0.8) `color.ink.80`; transition color 0.2s ease-out |
| hover | child paint el::before: opacity 1 |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.footer-link.text-ink: size 46.1x19.0; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | child paint el::before: opacity 1 |

Child layers that carry the look: a::before 58.0625pxx23px background rgba(231, 231, 227, 0.8) radius 4px.

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A footer social icon link (X/LinkedIn). Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; border 1px solid rgba(32, 32, 32, 0.1); radius 8px; background #f5f5f2 `color.surface`; shadow rgba(0, 0, 0, 0.06) 0px 2px 3px 0px, rgba(255, 255, 255, 0.35) 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset; text neoris 16/24 400, rgba(38, 35, 35, 0.5) `color.ink.50`; transition background-color 0.14s ease-out, box-shadow 0.14s ease-out; icon 15 x 15, rgba(38, 35, 35, 0.5) `color.ink.50` |
| hover | background #ededea; text neoris 16/24 400, #e1e8e7; icon 15 x 15, #e1e8e7; child paint a.group.relative: background #ededea |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.group.relative: outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | background #ededea; text neoris 16/24 400, #e1e8e7; icon 15 x 15, #e1e8e7; child paint a.group.relative: background #ededea |

![Social link default](components/crops/footer-social-default.png) ![Social link hover](components/crops/footer-social-hover.png) ![Social link focus-visible](components/crops/footer-social-focus-visible.png) ![Social link pressed](components/crops/footer-social-pressed.png)

#### Footer CTA
The footer CTA card "Run a company" button (btn-light-surface) linking to app.cofounder.co/os; measured never followed. Read as `footer-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 127.96 x 41; padding 0px 12px; border 1px solid rgba(32, 32, 32, 0.1); radius 8px; background #f5f5f2 `color.surface`; shadow rgba(0, 0, 0, 0.06) 0px 2px 3px 0px, rgba(255, 255, 255, 0.35) 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset; wrapper div.-mt-[232px].md:-mt-[200px]: shadow rgba(0, 0, 0, 0.12) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.1) 0px -1px 2px 0px inset, rgba(255, 255, 255, 0.24) 0px 1px 1px 0px inset / div.block.p-[12px]: shadow rgba(255, 255, 255, 0.35) 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset, rgba(0, 0, 0, 0.25) 0px 0px 2px 0px, rgba(232, 231, 230, 0.32) 0px 0px 0px 4px; text neoris 15/22.5 460, #171717 `color.ink.90`; transition background-color 0.14s ease-out, box-shadow 0.14s ease-out |
| hover | size 129.04 x 41.83; background #f2f2ef; child paint a.group.relative: size 129.0x41.8; background #f2f2ef |
| focus-visible | size 128.28 x 41.25; outline 1px auto #101010, offset 1px; child paint a.group.relative: size 128.3x41.3; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | background #ededea; child paint a.group.relative: background #ededea |

![Footer CTA default](components/crops/footer-cta-default.png) ![Footer CTA hover](components/crops/footer-cta-hover.png) ![Footer CTA focus-visible](components/crops/footer-cta-focus-visible.png) ![Footer CTA pressed](components/crops/footer-cta-pressed.png)

### Mobile (390 wide)

The same surface at phone width: the collapsed bar and the open menu panel.

#### Mobile bar
The 390 mobile header bar: logo + menu toggle. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 78; border B: 1px solid rgba(232, 231, 230, 0); background transparent; shadow rgba(255, 255, 255, 0) 0px 1px 0px 0px; text neoris 15/22.5 460, #1a1a1a; transition border-color 0.02s ease-in-out, box-shadow 0.02s ease-in-out, background-color 0.12s ease-out; icon 87.22 x 18, #171717 `color.ink.90`.

![Mobile bar default](components/crops/m-header-default.png)

#### Menu button
The hamburger (aria-label="Open menu", 41x41 rounded-8); its own press opens the menu. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 41 x 41; radius 8px; background transparent; wrapper header.site-header.fixed: shadow rgba(255, 255, 255, 0) 0px 1px 0px 0px; text neoris 16/24 400, #171717 `color.ink.90`.

Child layers that carry the look: span 41x41 image linear-gradient(rgba(255, 255, 255, 0.16) 0%, rgba(255, 255, 255, 0.08) 100%) border 1px solid transparent radius 8px shadow rgba(0, 0, 0, 0.12) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.1) 0px -1px 2px 0px inset, rgba(255, 255, 255, 0.24) 0px 1px 1px 0px inset; span 41x41 background #f5f5f2 `color.surface` border 1px solid rgba(32, 32, 32, 0.1) radius 8px shadow rgba(0, 0, 0, 0.06) 0px 2px 3px 0px, rgba(255, 255, 255, 0.35) 0px 0px 0.357px 1.5px inset, #ffffff `color.white` 0px 2px 0px 0px inset; span 18x1.5 background #fbfbf8 `color.surfaceRaised` radius 3.35544e+07px.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The full-screen menu overlay after the hamburger press. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; background #f5f5f2 `color.surface`; text neoris 24/36 410, #bfbfbf `color.feature.neutral`; icon 15 x 15, #171717 `color.ink.90`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Menu link
A link row inside the open mobile menu. Read as `m-menu-link` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 83.52 x 64; background transparent; text neoris 40/64 400, rgba(38, 35, 35, 0.8) `color.ink.80` |
| focus-visible | outline 1px auto #e59700, offset 1px; child paint a.text-[40px].[@media(max-height:600px)]:text-[24px]: size 83.5x64.0; outline 1px auto rgb(229, 151, 0) offset 1px |

![Menu link default](components/crops/m-menu-link-default.png) ![Menu link hover](components/crops/m-menu-link-hover.png) ![Menu link focus-visible](components/crops/m-menu-link-focus-visible.png) ![Menu link pressed](components/crops/m-menu-link-pressed.png)

#### Mobile headline
The hero headline at 390. Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 350 x 112.22; background transparent; image linear-gradient(#ffffff `color.white` 0%, rgba(255, 255, 255, 0.9) 100%); text neoris 34/37.4 400, #ffffff `color.white`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Cofounder's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The product itself.** Cofounder's OS — the agent workspace, integrations, settings and billing — lives behind app.cofounder.co sign-in; the public login surface was measured but never submitted, and no checkout was ever entered.
- **The app itself is a different stack.** The marketing site is a Next.js/Tailwind build; the Cofounder OS UI behind app.cofounder.co sign-in is not reachable signed out and is not claimed here. docs.cofounder.co (the docs/CLI surface) was not captured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

One theme: the whole public surface paints light. Coloured bands exist inside the theme (the #1a6fd1 tools band, the pixel-art hero art), but no second theme is offered.

### Fonts

- **The UI fonts** are webfonts the site ships (TT Neoris variable, Inter, Departure Mono and IBM Plex Mono via the `--font-*` variables; `fonts` in [raw/css-vars.json](raw/css-vars.json) holds the @font-face records); the font files themselves are not committed.
- Illustrations, the pixel-art scenery, badge artwork and the wordmark in the screenshots are Cofounder's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The pixel-art illustrations and the wordmark are Cofounder's content; only the frames and components were measured. The /agent-icons/ marks (ChatGPT, Claude, Cursor, Codex, Grok) are their owners' artwork.
