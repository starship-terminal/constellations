# Awwwards components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from b150.ai on 2026-11-11, signed out, in headless Chrome at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was joined, signed into, created, sent or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (30 components, 61 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (59 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one theme. Desktop shots are 1440 x 900 at 1x, including the `-full` whole-page shots; mobile shots are `mobile-{page}-light-{state}.png` at 2x, so a 390-wide viewport — and a 390-wide full page — comes out 780 pixels wide. Read mobile sizes at half the pixels.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [arrival](screenshots/home-light-arrival.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Winners grid | `/websites/` |  |
| Site detail | `first site card on the winners grid` |  |
| Collections | `/collections/` |  |
| Submit gate | `/submit/` |  |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Winners grid, phone | `/websites/` |  |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Arrival view | home, on load | the page as it arrives, before any consent or promo layer is hidden (nothing is ever answered) | [home-light-arrival](screenshots/home-light-arrival.png) |
| Card hover layer | home site cards | the card held under the pointer; the Vote Now layer shows | [home-light-card-hover](screenshots/home-light-card-hover.png) |
| Filter dropdown | winners grid | the first filter tab's own toggle | [websites-light-filter-open](screenshots/websites-light-filter-open.png), [filter-dropdown](#filter-dropdown) |
| Mobile menu | home, phone | the menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 9 components were given a real keyboard focus. 9 draw an outline ring: `nav-item` (1px auto #005fcc, offset 1px), `login-link` (1px auto #005fcc, offset 1px), `signup-btn` (1px auto #005fcc, offset 1px), `hero-cta` (1px auto #005fcc, offset 1px), `vibe-cta` (1px auto #005fcc, offset 1px), `talent-cta` (1px auto #005fcc, offset 1px), `contact-button` (1px auto #005fcc, offset 0px), `footer-link` (1px auto #005fcc, offset 1px), `m-menu-button` (1px auto #e59700, offset 0px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): controls keep their shape — Awwwards answers hover with fill and outline swaps rather than scale or shadow. Nothing a real press would vote, submit or sign in was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, opacity, outline-color, stroke, text-decoration-color | contact-button, contact-email, contact-input, contact-textarea, footer-link, login-link, nav-item, signup-btn |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | hero-cta, talent-cta |
| 0.9s | `cubic-bezier(0.25, 1, 0.5, 1)` | opacity, transform | about-body, contact-title |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|

## Components

### Shell and navigation

The header (wordmark, Explore/Directory/Academy/Jobs/Market nav, Log in / Sign Up, Be Pro, Submit Website).

#### Header
The top bar: wordmark, VIBEATHON/EVENTS/JOBS/MARKETPLACE/TALENT/FREE RESOURCES nav, LOGIN, SIGN UP. Read as `header` on the the home page page.

**Values (default).** size 1440 x 65; background transparent; text Fragment Mono 10/13.33 700, #90a684; icon 30 x 10, #fffdf6 `color.neutral.ink`; layers a.label.ml-1 79.4x40.0 rgb(255, 255, 255) T:1px solid rgb(230, 227, 221) / R:1px solid rgb(230, 227, 221) / B:1px solid rgb(230, 227, 221) / L:1px solid rgb(230, 227, 221) 3.35544e+07px; div.border-t.border-rule 0.0x0.0 rgb(242, 239, 233) T:1px solid rgb(230, 227, 221); a.label.mt-3 0.0x0.0 rgb(255, 255, 255) T:1px solid rgb(230, 227, 221) / R:1px solid rgb(230, 227, 221) / B:1px solid rgb(230, 22.

Child layers that carry the look: a 79.4x40 background #ffffff `color.accent.primary` border 1px solid #e6e3dd radius 3.35544e+07px; div 0x0 background #f2efe9 `color.accent.hover` border 1px solid #e6e3dd; a 0x0 background #ffffff `color.accent.primary` border 1px solid #e6e3dd radius 3.35544e+07px.

![Header default](components/crops/header-default.png)

#### Logo
The wordmark link back to /. Read as `logo` on the the home page page.

**Values (default).** size 30 x 10; background transparent; text Geist Variable 10/15 500, #fffdf6 `color.neutral.ink`; icon 30 x 10, #fffdf6 `color.neutral.ink`.

![Logo default](components/crops/logo-default.png)

#### Nav link
A top-level nav link (EVENTS). Measured, never followed. Read as `nav-item` on the the home page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 38.89 x 13.33; background transparent; text Fragment Mono 10/13.33 400, #fffdf6 `color.neutral.ink`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.6 |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.label.transition-opacity 38.9x13.3 |
| pressed | opacity 0.6 |

![Nav link default](components/crops/nav-item-default.png) ![Nav link hover](components/crops/nav-item-hover.png) ![Nav link focus-visible](components/crops/nav-item-focus-visible.png) ![Nav link pressed](components/crops/nav-item-pressed.png)

#### Login link
LOGIN in the header, pointing at app.b150.ai — the app gate rate-limits; measured, never followed. Read as `login-link` on the the home page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32.41 x 13.33; background transparent; text Fragment Mono 10/13.33 400, #fffdf6 `color.neutral.ink`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.6 |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.label.transition-opacity 32.4x13.3 |
| pressed | opacity 0.6 |

![Login link default](components/crops/login-link-default.png) ![Login link hover](components/crops/login-link-hover.png) ![Login link focus-visible](components/crops/login-link-focus-visible.png) ![Login link pressed](components/crops/login-link-pressed.png)

#### Sign Up button
The SIGN UP pill to app.b150.ai/auth/signup. Measured, never followed. Read as `signup-btn` on the the home page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 79.38 x 40; padding 0px 16px; border 1px solid #e6e3dd; radius 3.35544e+07px; background #ffffff `color.accent.primary`; text Fragment Mono 10/13.33 400, #1f1915 `color.accent.primaryText`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f2efe9 `color.accent.hover` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #f2efe9 `color.accent.hover` |

![Sign Up button default](components/crops/signup-btn-default.png) ![Sign Up button hover](components/crops/signup-btn-hover.png) ![Sign Up button focus-visible](components/crops/signup-btn-focus-visible.png) ![Sign Up button pressed](components/crops/signup-btn-pressed.png)

### Home

The Site of the Day hero card and the nominee cards below.

#### Hero heading
"Don't wait for the future. Build it." Read as `hero` on the the home page page.

**Values (default).** size 740 x 335.86; background transparent; text Geist Variable 120/111.96 400, #f7f5f1.

![Hero heading default](components/crops/hero-default.png)

#### Hero CTA
JOIN THE BETA — the primary call-to-action. Measured, never followed. Read as `hero-cta` on the the home page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 126.25 x 41; padding 0px 20px; border 1px solid #e6e3dd; radius 3.35544e+07px; background #fffdf6 `color.neutral.ink`; text Fragment Mono 10/13.33 400, #1f1915 `color.accent.primaryText`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #e6e3dd |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #e6e3dd |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Home section
A content section below the hero. Read as `home-section` on the the home page page.

**Values (default).** size 1440 x 968.98; padding 80px 0px; background #f2efe9 `color.accent.hover`; text Fragment Mono 10/12 400, #1f1915 `color.accent.primaryText`; icon 15 x 15, #1f1915 `color.accent.primaryText`.

![Home section default](components/crops/home-section-default.png)

### Footer

The page footer and section links.

#### Footer
Read as `footer` on the the home page page.

**Values (default).** size 1440 x 1063.78; padding 0px 0px 48px 0px; background #000000 `color.neutral.wash`; text Geist Variable 12/20.4 400, #fffdf6 `color.neutral.ink`; icon 30 x 10, #fffdf6 `color.neutral.ink`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the the home page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 100.33 x 41; padding 0px 20px; border 1px solid #e6e3dd; radius 3.35544e+07px; background #fffdf6 `color.neutral.ink`; text Fragment Mono 10/13.33 400, #1f1915 `color.accent.primaryText`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #e6e3dd |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #e6e3dd |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Mobile (390 wide)

The same surface at phone width, with the menu layer open.

#### Mobile header
Read as `m-header` on the the home page page at 390 wide.

**Values (default).** size 390 x 65; background transparent; text Geist Variable 10/15 500, #1f1915 `color.accent.primaryText`; icon 30 x 10, #1f1915 `color.accent.primaryText`; layers a.label.ml-1 0.0x0.0 rgb(255, 255, 255) T:1px solid rgb(230, 227, 221) / R:1px solid rgb(230, 227, 221) / B:1px solid rgb(230, 227, 221) / L:1px solid rgb(230, 227, 221) 3.35544e+07px; div.border-t.border-rule 0.0x0.0 rgb(242, 239, 233) T:1px solid rgb(230, 227, 221); a.label.mt-3 0.0x0.0 rgb(255, 255, 255) T:1px solid rgb(230, 227, 221) / R:1px solid rgb(230, 227, 221) / B:1px solid rgb(230, 227,.

Child layers that carry the look: a 0x0 background #ffffff `color.accent.primary` border 1px solid #e6e3dd radius 3.35544e+07px; div 0x0 background #f2efe9 `color.accent.hover` border 1px solid #e6e3dd; a 0x0 background #ffffff `color.accent.primary` border 1px solid #e6e3dd radius 3.35544e+07px.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the the home page page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40 x 40; background transparent; text Geist Variable 10/15 500, #1f1915 `color.accent.primaryText`; icon 24 x 24, #1f1915 `color.accent.primaryText` |
| focus-visible | outline 1px auto #e59700, offset 0px; layers button.grid.size-10 40.0x40.0 |

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button hover](components/crops/m-menu-button-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The menu button after its own toggle; the crop is the open menu layer. Read as `m-menu-open` on the the home page page at 390 wide.

**Values (opened).** size 40 x 40; background transparent; text Geist Variable 10/15 500, #1f1915 `color.accent.primaryText`.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav link
A row inside the opened menu. Read as `m-nav-link` on the the home page page at 390 wide.

**Values (default).** size 358 x 29.33; padding 8px 0px; background transparent; text Fragment Mono 10/13.33 700, #9ea4a8.

![Mobile nav link default](components/crops/m-nav-link-default.png)

#### Mobile CTA
A JOIN/SIGN UP button on mobile. Read as `m-cta` on the the home page page at 390 wide.

**Values (default).** size 79.38 x 40; padding 0px 16px; border 1px solid #e6e3dd; radius 3.35544e+07px; background #ffffff `color.accent.primary`; text Fragment Mono 10/13.33 400, #1f1915 `color.accent.primaryText`.

![Mobile CTA default](components/crops/m-cta-default.png)

### Vibeathon



#### Vibeathon title
Read as `vibe-title` on the vibeathon page.

**Values (default).** size 1220 x 439.61; background transparent; text Geist Variable 96/87.93 500, #1f1915 `color.accent.primaryText`; icon 100 x 100, #fa725a.

![Vibeathon title default](components/crops/vibe-title-default.png)

#### Vibeathon block
The first card/section on the vibeathon page. Read as `vibe-card` on the vibeathon page.

**Values (default).** size 1440 x 920.61; padding 103px 0px 80px 0px; background #f2efe9 `color.accent.hover`; text Fragment Mono 10/12 400, #1f1915 `color.accent.primaryText`; icon 15 x 15, #1f1915 `color.accent.primaryText`.

![Vibeathon block default](components/crops/vibe-card-default.png)

#### Vibeathon CTA
The first call-to-action on /vibeathon. Measured, never followed. Read as `vibe-cta` on the vibeathon page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 52.53 x 16; background transparent; text Geist Variable 12/20.4 400, #1f1915 `color.accent.primaryText` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.text-ink.underline 52.5x16.0 |

![Vibeathon CTA default](components/crops/vibe-cta-default.png) ![Vibeathon CTA hover](components/crops/vibe-cta-hover.png) ![Vibeathon CTA focus-visible](components/crops/vibe-cta-focus-visible.png) ![Vibeathon CTA pressed](components/crops/vibe-cta-pressed.png)

### Talent



#### Talent title
Read as `talent-title` on the talent page.

**Values (default).** size 740 x 334.78; background transparent; text Geist Variable 120/111.6 400, #f7f5f1.

![Talent title default](components/crops/talent-title-default.png)

#### Talent card
A talent/profile card on the talent surface. Measured, never followed. Read as `talent-card` on the talent page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 512 x 700; padding 40px; radius 8px; background #e6e3dd; text Fragment Mono 10/12 400, #1f1915 `color.accent.primaryText` |

![Talent card default](components/crops/talent-card-default.png) ![Talent card hover](components/crops/talent-card-hover.png)

#### Talent CTA
The first call-to-action on /talent. Measured, never followed. Read as `talent-cta` on the talent page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106.81 x 41; padding 0px 20px; border 1px solid #e6e3dd; radius 3.35544e+07px; background #fffdf6 `color.neutral.ink`; text Fragment Mono 10/13.33 400, #1f1915 `color.accent.primaryText`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #e6e3dd |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #e6e3dd |

![Talent CTA default](components/crops/talent-cta-default.png) ![Talent CTA hover](components/crops/talent-cta-hover.png) ![Talent CTA focus-visible](components/crops/talent-cta-focus-visible.png) ![Talent CTA pressed](components/crops/talent-cta-pressed.png)

### Free resources



#### Resources title
Read as `res-title` on the resources page.

**Values (default).** size 1220 x 263.77; background transparent; text Geist Variable 96/87.93 500, #1f1915 `color.accent.primaryText`.

![Resources title default](components/crops/res-title-default.png)

#### Resource card
A free-resource card. Measured, never followed. Read as `res-card` on the resources page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 412.8 x 595.72; background transparent; text Fragment Mono 10/13.33 400, #1f1915 `color.accent.primaryText`; layers div.h-[360px].overflow-hidden 412.8x493.0 T:1px solid rgb(230, 227, 221) / R:1px solid rgb(230, 227, 221) / B:1px solid rgb(230, 227, 221) / L:1px solid rgb(230, 227, 221) 16px; a.label.inline-flex 123.8x41.0 rgb(255, 255, 255) T:1px solid rgb(230, 227, 221) / R:1px solid rgb(230, 227, 221) / B:1px solid rgb(230, 227, 221) / L:1px solid rgb(230, 227, 221) 3.35544e+07px |

Child layers that carry the look: div 412.8x493 border 1px solid #e6e3dd radius 16px; a 123.8x41 background #ffffff `color.accent.primary` border 1px solid #e6e3dd radius 3.35544e+07px.

![Resource card default](components/crops/res-card-default.png) ![Resource card hover](components/crops/res-card-hover.png)

### About



#### About title
Read as `about-title` on the about page.

**Values (default).** size 1220 x 263.77; background transparent; text Geist Variable 96/87.93 500, #1f1915 `color.accent.primaryText`.

![About title default](components/crops/about-title-default.png)

#### About body
A body-copy block on /about. Read as `about-body` on the about page.

**Values (default).** size 800 x 540; background transparent; text Geist Variable 32/36 500, #1f1915 `color.accent.primaryText`; transition opacity 0.9s cubic-bezier(0.25, 1, 0.5, 1), transform 0.9s cubic-bezier(0.25, 1, 0.5, 1); transform translate(0px, 5.21885px); opacity 0.782548.

![About body default](components/crops/about-body-default.png)

### Contact



#### Contact title
Read as `contact-title` on the contact page.

**Values (default).** size 300.13 x 111.95; background transparent; text Geist Variable 120/111.96 400, #1f1915 `color.accent.primaryText`; transition opacity 0.9s cubic-bezier(0.25, 1, 0.5, 1), transform 0.9s cubic-bezier(0.25, 1, 0.5, 1).

![Contact title default](components/crops/contact-title-default.png)

#### Contact field
A contact form field; focused only, never submitted. Read as `contact-input` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 300 x 56; padding 0px 16px; border 1px solid #e6e3dd; radius 8px; background #e6e3dd; text Geist Variable 12/18 500, #1f1915 `color.accent.primaryText`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder oklab(0.219135 0.00691891 0.0101172 / 0.48) |
| focused | border 1px solid oklab(0.219135 0.00691891 0.0101172 / 0.32); background #f7f5f1 |

![Contact field default](components/crops/contact-input-default.png) ![Contact field focused](components/crops/contact-input-focused.png)

#### Contact email field
The email input; focused only, never submitted. Read as `contact-textarea` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 300 x 56; padding 0px 16px; border 1px solid #e6e3dd; radius 8px; background #e6e3dd; text Geist Variable 12/18 500, #1f1915 `color.accent.primaryText`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder oklab(0.219135 0.00691891 0.0101172 / 0.48) |
| focused | border 1px solid oklab(0.219135 0.00691891 0.0101172 / 0.32); background #f7f5f1 |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Contact button
The submit; measured except a real press — the form was never submitted. Read as `contact-button` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 111.77 x 40; padding 0px 16px; border 1px solid #e6e3dd; radius 3.35544e+07px; background #ffffff `color.accent.primary`; text Fragment Mono 10/13.33 400, #1f1915 `color.accent.primaryText`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f2efe9 `color.accent.hover` |
| focus-visible | outline 1px auto #005fcc, offset 0px |

![Contact button default](components/crops/contact-button-default.png) ![Contact button hover](components/crops/contact-button-hover.png) ![Contact button focus-visible](components/crops/contact-button-focus-visible.png)

#### Contact email field
The email input; focused only, never submitted. Read as `contact-email` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 300 x 56; padding 0px 16px; border 1px solid #e6e3dd; radius 8px; background #e6e3dd; text Geist Variable 12/18 500, #1f1915 `color.accent.primaryText`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder oklab(0.219135 0.00691891 0.0101172 / 0.48) |
| focused | border 1px solid oklab(0.219135 0.00691891 0.0101172 / 0.32); background #f7f5f1 |

![Contact email field default](components/crops/contact-email-default.png) ![Contact email field focused](components/crops/contact-email-focused.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Awwwards' artwork (inline SVG). Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **Voting, submitting and anything behind sign-in.** The Vote button was measured but never clicked (a vote records a score), /submit/ was never submitted, and Log in / Sign Up did not render on the headless loads — no public login page exists signed-out. Jury tools, Pro dashboards and account pages were never reached.
- **Anything that sends or joins.** No form was submitted, no vote cast, no search was run, no account was created, no consent choice was made.
- **The filter dropdown's innards** were measured at the first option only; Academy, Jobs, Market, Directory and Jury pages are outside this pass.
- **The card hover layer.** The Vote Now overlay on grid cards stayed `display:none` under headless hover on the measured runs (recorded as a gap on `card-cta`/`card-action`, not fabricated); the screenshot `home-light-card-hover` shows it.
- **Headless access.** b150.ai serves headless Chrome a 200 on every captured route.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Keyboard focus on the mobile menu button** did not land (recorded as an error state on `m-menu-button`, not as evidence).
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The site paints one theme on every captured route; a `.dark` probe resolves every custom property identically. No dark or reduced-contrast mode is offered.

### Fonts

- **Inter Tight** is the single family — every measured component resolves to it, at declared weights 300-800 (`--font-light` to `--font-black`). Only one `@font-face` rule was captured; the variable font is self-hosted.

### Screenshots

- Winning-site thumbnails, nominee artwork and the Awwwards wordmark in the screenshots are third-party/site content. The site detail captured is whichever `/websites/` card first had open voting at run time (recorded as `site_url` in components-computed.json); another run may land on a different entry.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Winning-site thumbnails and nominee artwork are the entrants' content; only the frames and components were measured.
