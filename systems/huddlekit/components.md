# Huddlekit components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Read from huddlekit.com and app.huddlekit.com on 2026-11-18, signed out, in headless Chromium at 1440 x 900 (the mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought, searched or submitted; the only presses were local UI toggles the pages' own chrome provides — the consent banner's Decline, the nav's hover-open menus, FAQ accordions, the billing switch, the feature tabs, the testimonials 'Show more', the login's 'Continue with email' reveal and the phone's menu button; every link was measured, never followed.

**Where this was read.** Two public surfaces carry the system: huddlekit.com itself — the signed-out marketing site (home, features, solutions, pricing, integrations, compare, MCP, manifesto, blog, support, tools, contact, legal) — and app.huddlekit.com/login, the one surface the app serves anonymously. The marketing site paints light only; its `.dark` rules re-point the same custom properties inside nested dark panels (the footer, the dark testimonials, the MCP card), measured as their own components. The app paints `html.dark` under prefers-color-scheme — the login's `dark` states are measured on that painted dark surface. Everything past /login redirects an anonymous visitor back to it; try./demo./status./docs./help. hosts and app.huddlekit.io do not resolve. All of those are boundaries listed under Gaps, not captures.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (48 components, 105 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/20.8 400, #000000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (105 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png` where `{theme}` is the surface the page painted at capture: every marketing page boots `light` (huddlekit.com has no theme control — its `.dark` panels are component-level surfaces, not a page theme); `app-login-dark-*` shots are the login painted dark by emulated `prefers-color-scheme: dark` + reload — the signal the app honours — each verified against the painted surface (html class, data-theme attribute, color-scheme). Desktop shots are 1440 x 900 at 1x; `-full` shots are the whole page at 1x, bounded at eight chunks with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 390 wide (a mobile `-full` taller than one GPU texture is stitched from `part` tiles, the stitched sheet's sidecar rebuilt from the tiles').

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [consent](screenshots/home-light-consent.png), [default](screenshots/home-light-default.png), [faq-open](screenshots/home-light-faq-open.png), [feature-tab](screenshots/home-light-feature-tab.png), [full](screenshots/home-light-full.png), [menu-resources](screenshots/home-light-menu-resources.png), [menu-solutions](screenshots/home-light-menu-solutions.png), [testimonials-open](screenshots/home-light-testimonials-open.png) |
| Features | `/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| For agencies | `/agencies` | [default](screenshots/agencies-light-default.png), [full](screenshots/agencies-light-full.png) |
| Customers | `/customers` | [default](screenshots/customers-light-default.png), [full](screenshots/customers-light-full.png) |
| Case study | `/customers/leadfront` | [default](screenshots/case-study-light-default.png), [full](screenshots/case-study-light-full.png) |
| Pricing | `/pricing` | [billing-toggle](screenshots/pricing-light-billing-toggle.png), [default](screenshots/pricing-light-default.png), [faq-open](screenshots/pricing-light-faq-open.png), [full](screenshots/pricing-light-full.png) |
| Integrations | `/integrations` | [default](screenshots/integrations-light-default.png), [full](screenshots/integrations-light-full.png) |
| Integration: Linear | `/integrations/linear` | [default](screenshots/integration-linear-light-default.png), [full](screenshots/integration-linear-light-full.png) |
| Compare index | `/compare` | [default](screenshots/compare-light-default.png), [full](screenshots/compare-light-full.png) |
| Compare: Pastel | `/compare/pastel-alternative` | [default](screenshots/compare-page-light-default.png), [full](screenshots/compare-page-light-full.png) |
| MCP | `/mcp` | [default](screenshots/mcp-light-default.png), [full](screenshots/mcp-light-full.png) |
| Manifesto | `/manifesto` | [default](screenshots/manifesto-light-default.png), [full](screenshots/manifesto-light-full.png) |
| Blog index | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Blog article | `/blog/introducing-huddlekit` | [default](screenshots/blog-post-light-default.png), [full](screenshots/blog-post-light-full.png) |
| Support centre | `/support` | [default](screenshots/support-light-default.png), [full](screenshots/support-light-full.png) |
| Support article | `/support/getting-started` | [default](screenshots/support-article-light-default.png), [full](screenshots/support-article-light-full.png) |
| Tools index | `/tools` | [default](screenshots/tools-light-default.png), [full](screenshots/tools-light-full.png) |
| Contrast checker | `/tools/color-contrast-checker` | [default](screenshots/tool-contrast-light-default.png), [full](screenshots/tool-contrast-light-full.png) |
| Contact | `/contact` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Privacy | `/privacy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| App login | `app.huddlekit.com/login` | [default](screenshots/app-login-dark-default.png), [email-open](screenshots/app-login-dark-email-open.png), [consent](screenshots/app-login-light-consent.png), [default](screenshots/app-login-light-default.png), [email-open](screenshots/app-login-light-email-open.png) |
| Home, phone | `/` | [consent](screenshots/mobile-home-light-consent.png), [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Contrast checker, phone | `/tools/color-contrast-checker` | [default](screenshots/mobile-tool-contrast-light-default.png), [full](screenshots/mobile-tool-contrast-light-full.png) |
| App login, phone | `app.huddlekit.com/login` | [default](screenshots/mobile-app-login-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Consent banner | home, app login, phone home | the first-visit banner's own presence; 'Decline' pressed once to dismiss it, 'Accept' never pressed | [home-light-consent](screenshots/home-light-consent.png), [app-login-light-consent](screenshots/app-login-light-consent.png), [mobile-home-light-consent](screenshots/mobile-home-light-consent.png) |
| Nav menus | home header | hovering the header's own 'Solutions' / 'Resources' buttons — the menu surface opened, captured, left | [home-light-menu-solutions](screenshots/home-light-menu-solutions.png), [home-light-menu-resources](screenshots/home-light-menu-resources.png) |
| FAQ accordion | home, pricing | a question row's own press — the answer expanded | [home-light-faq-open](screenshots/home-light-faq-open.png), [pricing-light-faq-open](screenshots/pricing-light-faq-open.png) |
| Feature tabs | home | a tab's own activation — a local UI toggle | [home-light-feature-tab](screenshots/home-light-feature-tab.png) |
| Testimonials 'Show more' | home | the toggle's own press — the hidden testimonial cards expanded | [home-light-testimonials-open](screenshots/home-light-testimonials-open.png) |
| Billing switch | pricing | the monthly/annual switch's own press — a local UI toggle | [pricing-light-billing-toggle](screenshots/pricing-light-billing-toggle.png) |
| Email form reveal | app login | the 'Continue with email' button's own press — the form opened; nothing typed or submitted | [app-login-light-email-open](screenshots/app-login-light-email-open.png), [app-login-dark-email-open](screenshots/app-login-dark-email-open.png) |
| Mobile nav drawer | home, phone width | the 'Toggle menu' button's own press | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png) |
| Dark theme | app login | emulated prefers-color-scheme: dark + reload — the app's own OS-preference path, verified against the painted surface | [app-login-dark-default](screenshots/app-login-dark-default.png), [app-login-dark-email-open](screenshots/app-login-dark-email-open.png) |
| The signed-in product | everything past /login | the auth wall — app.huddlekit.com redirects an anonymous visitor to /login; never entered, Google OAuth and email Continue never submitted | boundary; see Gaps |
| Sibling hosts | try./demo./status./docs./help. + app.huddlekit.io | NXDOMAIN from the capture host — never reached | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 18 components were given a real keyboard focus. 2 draw an outline ring: `nav-link` (1px auto rgba(255, 105, 0, 0.5), offset 1px), `tool-color-input` (1px auto rgba(255, 105, 0, 0.5), offset 0px). 15 draw a focus ring as a shadow instead: `consent-decline`, `consent-accept`, `cta-primary`, `cta-secondary`, `cta-outline`, `testimonial-card-dark`, `show-more`, `billing-switch`, `plan-cta`, `support-search`, `tool-text-input`, `contact-copy`, `app-google-button`, `app-email-button`, `m-menu-button`. The other 1 show no measured change: `app-continue-button`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, box-shadow, color, fill, outline-color, stroke, text-decoration-color | app-back-button, app-continue-button, app-email-button, app-email-input, app-google-button, billing-switch, consent-accept, consent-decline and more |
| 0.2s | `cubic-bezier(0.22, 1, 0.36, 1)` | height, translate, width | nav-menu-surface |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Site header](#site-header) | 976 x 64 | - | - | transparent | none | 0 |
| [Nav popover (open)](#nav-popover-open) | 194 x 154 | 1px solid #e4e4e7 `light.border.default` | 16px | #ffffff `light.card.default` | rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px | 0 |
| [Cookie consent banner](#cookie-consent-banner) | 352 x 174 | 1px solid #e4e4e7 `light.border.default` | 16px | #ffffff `light.card.default` | rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px | 8px |
| [Integration card](#integration-card) | 314.66 x 196 | - | 16px | #ffffff `light.card.default` | rgba(0, 0, 0, 0.05) 0px 1px 2px 0px | 24px |
| [Integration page card](#integration-page-card) | 314.66 x 196 | - | 16px | #ffffff `light.card.default` | rgba(0, 0, 0, 0.05) 0px 1px 2px 0px | 24px |
| [Dark testimonial card](#dark-testimonial-card) | 645.33 x 384 | - | 16px | #0e0b0d `core.component.component.footer.bg` | rgba(0, 0, 0, 0.05) 0px 1px 2px 0px | 24px |
| [Dark MCP panel](#dark-mcp-panel) | 976 x 88 | - | 16px | #0e0b0d `core.component.component.footer.bg` | rgba(0, 0, 0, 0.05) 0px 1px 2px 0px | 24px |
| [Support category card](#support-category-card) | 480 x 172 | - | 16px | #ffffff `light.card.default` | rgba(0, 0, 0, 0.05) 0px 1px 2px 0px | 24px |
| [Sign-in panel](#sign-in-panel) | 320 x 168 | - | - | transparent | none | 0 |
| [Site footer (dark)](#site-footer-dark) | 1440 x 860.02 | T: 1px solid rgba(255, 255, 255, 0.08) | - | #0e0b0d `core.component.component.footer.bg` | none | 0 |

## Components

### Consent

The cookie-consent banner every first visit paints: the banner card and its Decline / Accept buttons — Decline was pressed once to dismiss it, Accept measured but never pressed.

#### Cookie consent banner
The fixed bottom consent banner ("We'd like to use cookies…"): bg-background rounded-2xl border shadow-lg with Decline / Accept. Read as `consent-banner` on the home page.
Read on 2026-11-17T15:06:44.253Z.

**Values (default).** size 352 x 174; padding 8px; border 1px solid #e4e4e7 `light.border.default`; radius 16px; background #ffffff `light.card.default`; shadow rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px; text Inter 14/20 400, #747170 `light.muted.foreground`.

![Cookie consent banner default](components/crops/consent-banner-default.png)

#### Consent "Decline" button
The decline control in the consent banner (secondary style). Read as `consent-decline` on the home page.
States read on 2026-11-17T15:06:45.591Z (default); 2026-11-17T15:06:48.541Z (hover); 2026-11-17T15:06:50.449Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 163 x 36; padding 8px 12px; border 1px solid #e4e4e7 `light.border.default`; radius 12px; background #ffffff `light.card.default`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 14/20 500, #111827 `light.root.foreground`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f6f3f2 `light.color.page`; text Inter 14/20 500, #18181b `light.accent.foreground` |
| focus-visible | border 1px solid rgba(17, 24, 39, 0.2); shadow rgba(17, 24, 39, 0.2) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Consent "Decline" button default](components/crops/consent-decline-default.png) ![Consent "Decline" button hover](components/crops/consent-decline-hover.png) ![Consent "Decline" button focus-visible](components/crops/consent-decline-focus-visible.png)

#### Consent "Accept" button
The accept control in the consent banner (bg-primary). Read as `consent-accept` on the home page.
States read on 2026-11-17T15:06:54.590Z (default); 2026-11-17T15:06:57.124Z (hover); 2026-11-17T15:06:58.597Z (focus-visible); 2026-11-17T15:07:01.913Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 163 x 36; padding 8px 12px; border 1px solid #e4e4e7 `light.border.default`; radius 12px; background #ffffff `light.card.default`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 14/20 500, #111827 `light.root.foreground`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f6f3f2 `light.color.page`; text Inter 14/20 500, #18181b `light.accent.foreground` |
| focus-visible | border 1px solid rgba(17, 24, 39, 0.2); shadow rgba(17, 24, 39, 0.2) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |
| pressed | background #f6f3f2 `light.color.page`; text Inter 14/20 500, #18181b `light.accent.foreground` |

![Consent "Accept" button default](components/crops/consent-accept-default.png) ![Consent "Accept" button hover](components/crops/consent-accept-hover.png) ![Consent "Accept" button focus-visible](components/crops/consent-accept-focus-visible.png) ![Consent "Accept" button pressed](components/crops/consent-accept-pressed.png)

### Chrome

The marketing chrome every huddlekit.com page carries: the announcement bar, the sticky header (wordmark, Features / Solutions / Resources / Pricing links, Sign in and 'Get started'), the hover-open nav menus and their surface, the call-to-action buttons, the footer and the cookie-settings control that re-opens the banner.

#### Announcement bar
The top "New: hand feedback to your AI agent over MCP" announcement link — border-b over the header. Read as `announce-bar` on the home page.
States read on 2026-11-17T16:28:54.758Z (default); 2026-11-17T16:28:56.683Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1440 x 40; padding 8px 16px; border B: 1px solid #e4e4e7 `light.border.default`; background transparent; text Inter 14/20 500, #111827 `light.root.foreground`; icon 16 x 16, #111827 `light.root.foreground`; layers a.group.text-foreground 1440.0x40.0 B:1px solid |

Child layers that carry the look: a 1440x40 border 1px solid.

![Announcement bar default](components/crops/announce-bar-default.png) ![Announcement bar hover](components/crops/announce-bar-hover.png)

#### Site header
The header holding the logo, the Features / Solutions / Resources / Pricing / Sign in nav and the "Get started" button. Read as `nav-header` on the home page.
Read on 2026-11-17T16:28:57.644Z.

**Values (default).** size 976 x 64; background transparent; text Inter 14/20 500, #111827 `light.root.foreground`; icon 104 x 28, #111827 `light.root.foreground`; layers a.inline-flex.items-center 104.0x32.0 #ede9e7 T:1px solid / R:1px solid / B:1px solid / L:1px solid transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px 12px; butto.

Child layers that carry the look: a 104x32 background #ede9e7 `light.secondary.default` border 1px solid radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px; button 0x0 background #ffffff `light.card.default` border 1px solid radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px.

![Site header default](components/crops/nav-header-default.png)

#### Nav link
A plain nav link ("Features"), text-foreground with hover:text-foreground/70. Read as `nav-link` on the home page.
States read on 2026-11-17T16:28:58.635Z (default); 2026-11-17T16:29:00.478Z (hover); 2026-11-17T16:29:02.464Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 62 x 20; background transparent; text Inter 14/20 500, #111827 `light.root.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 14/20 500, rgba(17, 24, 39, 0.7) `core.component.type.linkHover.color` |
| focus-visible | outline 1px auto rgba(255, 105, 0, 0.5), offset 1px; layers a.hover:text-foreground/70.text-foreground 62.0x20.0 1px auto rgba(255, 105, 0, 0.5) offset 1px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png)

#### Nav menu trigger
The "Solutions" button that opens a nav-surface popover on hover. "opened" is after the real hover that opened it. Read as `nav-menu-button` on the home page.
States read on 2026-11-17T16:29:03.334Z (default); 2026-11-17T16:29:05.155Z (hover); 2026-11-17T16:29:08.802Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85 x 20; background transparent; text Inter 14/20 500, #111827 `light.root.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, #111827 `light.root.foreground` |
| hover, opened | text Inter 14/20 500, rgba(17, 24, 39, 0.7) `core.component.type.linkHover.color`; icon 14 x 14, rgba(17, 24, 39, 0.7) `core.component.type.linkHover.color` |

![Nav menu trigger default](components/crops/nav-menu-button-default.png) ![Nav menu trigger hover](components/crops/nav-menu-button-hover.png) ![Nav menu trigger opened](components/crops/nav-menu-button-opened.png)

#### Nav popover (open)
The open nav-surface popover under the header — the Solutions menu the hover shows. Read as `nav-menu-surface` on the home page.
Read on 2026-11-17T16:29:12.607Z.

**Values (opened).** size 194 x 154; border 1px solid #e4e4e7 `light.border.default`; radius 16px; background #ffffff `light.card.default`; shadow rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px; text Inter 14/20 500, #111827 `light.root.foreground`; transition translate 0.2s cubic-bezier(0.22, 1, 0.36, 1), width 0.2s cubic-bezier(0.22, 1, 0.36, 1), height 0.2s cubic-bezier(0.22, 1, 0.36, 1); icon 16 x 16, #747170 `light.muted.foreground`.

![Nav popover (open) opened](components/crops/nav-menu-surface-opened.png)

#### "Sign in" link
The header sign-in link — measured, never followed (it leads to app.huddlekit.com, which was captured separately). Read as `nav-signin` on the home page.
States read on 2026-11-17T16:29:14.014Z (default); 2026-11-17T16:29:15.866Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 20; background transparent; text Inter 14/20 500, #111827 `light.root.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 14/20 500, rgba(17, 24, 39, 0.7) `core.component.type.linkHover.color` |

!["Sign in" link default](components/crops/nav-signin-default.png) !["Sign in" link hover](components/crops/nav-signin-hover.png)

#### Primary CTA button
The solid "Get started for free" call-to-action (bg-primary text-primary-foreground, the inner-shadow stack) — links to the app, measured never followed. Read as `cta-primary` on the home page.
States read on 2026-11-17T16:29:17.171Z (default); 2026-11-17T16:29:19.360Z (hover); 2026-11-17T16:29:20.830Z (focus-visible); 2026-11-17T16:29:22.151Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 169 x 40; padding 0px 14px; radius 12px; background #ea580d `light.primary.default`; shadow rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px; text Inter 14/20 500, #fff7ed `light.primary.foreground`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(234, 88, 13, 0.9) |
| focus-visible | shadow rgba(17, 24, 39, 0.2) 0px 0px 0px 1px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px |
| pressed | background rgba(234, 88, 13, 0.9) |

![Primary CTA button default](components/crops/cta-primary-default.png) ![Primary CTA button hover](components/crops/cta-primary-hover.png) ![Primary CTA button focus-visible](components/crops/cta-primary-focus-visible.png) ![Primary CTA button pressed](components/crops/cta-primary-pressed.png)

#### Secondary button
The header's "Get started" button (bg-secondary with the same inner-shadow stack). Read as `cta-secondary` on the home page.
States read on 2026-11-17T16:29:23.050Z (default); 2026-11-17T16:29:25.076Z (hover); 2026-11-17T16:29:27.530Z (focus-visible); 2026-11-17T16:29:28.803Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 104 x 32; padding 0px 10px; border 1px solid transparent; radius 12px; background #ede9e7 `light.secondary.default`; shadow rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px; text Inter 14/20 500, #18181b `light.accent.foreground`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(237, 233, 231, 0.8) |
| focus-visible | border 1px solid rgba(17, 24, 39, 0.2); shadow rgba(17, 24, 39, 0.2) 0px 0px 0px 1px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px |
| pressed | background rgba(237, 233, 231, 0.8) |

![Secondary button default](components/crops/cta-secondary-default.png) ![Secondary button hover](components/crops/cta-secondary-hover.png) ![Secondary button focus-visible](components/crops/cta-secondary-focus-visible.png) ![Secondary button pressed](components/crops/cta-secondary-pressed.png)

#### Outline button
A bordered ghost action in the hero ("5-star reviews"): border + transparent fill, hover:bg-accent. Read as `cta-outline` on the home page.
States read on 2026-11-17T16:29:29.715Z (default); 2026-11-17T16:29:31.563Z (hover); 2026-11-17T16:29:32.868Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 152 x 40; padding 0px 14px; border 1px solid transparent; radius 12px; background transparent; text Inter 14/20 500, transparent; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, #ea580d `light.primary.default` |
| hover | background rgba(17, 24, 39, 0.05) |
| focus-visible | border 1px solid rgba(17, 24, 39, 0.2); shadow rgba(17, 24, 39, 0.2) 0px 0px 0px 1px |

![Outline button default](components/crops/cta-outline-default.png) ![Outline button hover](components/crops/cta-outline-hover.png) ![Outline button focus-visible](components/crops/cta-outline-focus-visible.png)

#### Site footer (dark)
The .dark footer (bg-background text-foreground inside .dark): Product / Solutions / Resources columns, "Cookie settings" button and the social links. Read as `footer` on the home page.
Read on 2026-11-17T16:30:04.949Z.

**Values (default).** size 1440 x 860.02; border T: 1px solid rgba(255, 255, 255, 0.08); background #0e0b0d `core.component.component.footer.bg`; text Inter 14/20 600, #e3e0df; icon 16 x 16, #e3e0df.

![Site footer (dark) default](components/crops/footer-default.png)

#### Footer link
A muted footer link (text-muted-foreground) inside the dark footer. Read as `footer-link` on the home page.
States read on 2026-11-17T16:30:05.798Z (default); 2026-11-17T16:30:07.586Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 62 x 17; background transparent; text Inter 14/20 500, #a3a09f |
| hover | text Inter 14/20 500, #e3e0df |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png)

#### "Cookie settings" button
The footer control that re-shows the consent banner — a local UI toggle. Read as `cookie-settings` on the home page.
States read on 2026-11-17T16:30:08.424Z (default); 2026-11-17T16:30:10.229Z (hover); 2026-11-17T16:30:12.286Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 112 x 20; background transparent; text Inter 14/20 500, #a3a09f |
| hover, opened | text Inter 14/20 500, #e3e0df |

!["Cookie settings" button default](components/crops/cookie-settings-default.png) !["Cookie settings" button hover](components/crops/cookie-settings-hover.png) !["Cookie settings" button opened](components/crops/cookie-settings-opened.png)

### Home

The landing page's own layer: the feature tablist, the integration cards, the dark MCP and testimonial panels (the site's nested .dark surfaces, measured at rest), the 'Show more' testimonials toggle and the FAQ accordion.

#### Feature tab (vertical)
One row of the vertical feature tabs ("Draw on the page"): role=tab, muted until selected. "selected" is the tab's own activation. Read as `feature-tab` on the home page.
States read on 2026-11-17T16:29:33.718Z (default); 2026-11-17T16:29:35.559Z (hover); 2026-11-17T16:29:37.497Z (selected).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 282.67 x 57; padding 16px 0px; border B: 1px solid #e4e4e7 `light.border.default`; background transparent; text Inter 16/24 500, #747170 `light.muted.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers button.group.text-muted-foreground 282.7x57.0 B:1px solid |
| hover | text Inter 16/24 500, #111827 `light.root.foreground` |
| selected | size 282.67 x 111; text Inter 16/24 500, #111827 `light.root.foreground`; layers button.group.text-muted-foreground 282.7x111.0 B:1px solid |

Child layers that carry the look: button 282.7x57 border 1px solid.

![Feature tab (vertical) default](components/crops/feature-tab-default.png) ![Feature tab (vertical) hover](components/crops/feature-tab-hover.png) ![Feature tab (vertical) selected](components/crops/feature-tab-selected.png)

#### Integration card
An integration card on the home grid ("Linear" — icon, name, one line): bg-background rounded-xl shadow-xs. Read as `integration-card` on the home page.
States read on 2026-11-17T16:29:38.568Z (default); 2026-11-17T16:29:41.467Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 314.66 x 196; padding 24px; radius 16px; background #ffffff `light.card.default`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 20/28 500, #111827 `light.root.foreground`; icon 20 x 20, #111827 `light.root.foreground` |

![Integration card default](components/crops/integration-card-default.png) ![Integration card hover](components/crops/integration-card-hover.png)

#### Dark MCP panel
The .dark "Let your AI agent fix comments over MCP" card — the marketing page's painted-dark surface evidence: bg-background/text-foreground inside .dark re-point to the dark palette. Read as `mcp-card-dark` on the home page.
States read on 2026-11-17T16:29:42.933Z (default); 2026-11-17T16:29:44.850Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 976 x 88; padding 24px; radius 16px; background #0e0b0d `core.component.component.footer.bg`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 20/28 500, #e3e0df; icon 20 x 20, #e3e0df |

![Dark MCP panel default](components/crops/mcp-card-dark-default.png) ![Dark MCP panel hover](components/crops/mcp-card-dark-hover.png)

#### Dark testimonial card
A large .dark testimonial card (quote + attribution) in the testimonials grid. Read as `testimonial-card-dark` on the home page.
States read on 2026-11-17T16:29:46.320Z (default); 2026-11-17T16:29:49.067Z (hover); 2026-11-17T16:29:51.322Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 645.33 x 384; padding 24px; radius 16px; background #0e0b0d `core.component.component.footer.bg`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 26/31.2 500, #e3e0df |
| focus-visible | shadow rgba(245, 73, 0, 0.5) 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Dark testimonial card default](components/crops/testimonial-card-dark-default.png) ![Dark testimonial card hover](components/crops/testimonial-card-dark-hover.png) ![Dark testimonial card focus-visible](components/crops/testimonial-card-dark-focus-visible.png)

#### "Show more testimonials" button
The ghost expander under the testimonial grid. "opened" is its own press (the grid grows). Read as `show-more` on the home page.
States read on 2026-11-17T16:29:52.186Z (default); 2026-11-17T16:29:54.019Z (hover); 2026-11-17T16:29:55.353Z (focus-visible); 2026-11-17T16:29:57.172Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 218 x 36; padding 8px 12px; border 1px solid transparent; radius 12px; background transparent; text Inter 14/20 500, #111827 `light.root.foreground`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #111827 `light.root.foreground` |
| hover | background rgba(17, 24, 39, 0.05); text Inter 14/20 500, #18181b `light.accent.foreground`; icon 16 x 16, #18181b `light.accent.foreground` |
| focus-visible | border 1px solid rgba(17, 24, 39, 0.2); shadow rgba(17, 24, 39, 0.2) 0px 0px 0px 1px |
| opened | size 120 x 36 |

!["Show more testimonials" button default](components/crops/show-more-default.png) !["Show more testimonials" button hover](components/crops/show-more-hover.png) !["Show more testimonials" button focus-visible](components/crops/show-more-focus-visible.png) !["Show more testimonials" button opened](components/crops/show-more-opened.png)

#### FAQ accordion question
A question row in the page FAQ accordion. "opened" is its own press revealing the answer. Read as `faq-question` on the home page.

The saved states read the header Solutions trigger (85x20), not a question row. Selectors are scoped to main button[aria-expanded] whose label contains "?". Not remeasured: no live recapture.

### Pricing

The /pricing page: the plan cards, the monthly/annual billing switch, the per-plan call-to-action buttons and the compare-alternatives link cards.

#### Plan card
A pricing plan card on /pricing (name, price, feature list, CTA). Read as `plan-card` on the pricing page.

The saved state reads the "Free forever" label (274.66x16), not a plan card. The picker now requires a price, a call to action, several lines and height of at least 160. Not remeasured: no live recapture.

#### Billing switch
A monthly/annual switch on the plan cards (role=switch, data-state=checked, bg-primary on). "off" is its own press — then pressed back. Read as `billing-switch` on the pricing page.
States read on 2026-11-17T15:10:11.658Z (default); 2026-11-17T15:10:13.727Z (hover); 2026-11-17T15:10:19.407Z (focus-visible); 2026-11-17T15:10:21.584Z (off).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 18.39; border 1px solid transparent; radius 3.35544e+07px; background #ea580d `light.primary.default`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 16/24 400, #111827 `light.root.foreground`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | border 1px solid #ff6900 `light.border.ring`; shadow rgba(255, 105, 0, 0.5) 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |
| off | background #e4e4e7 `light.border.default` |

![Billing switch default](components/crops/billing-switch-default.png) ![Billing switch hover](components/crops/billing-switch-hover.png) ![Billing switch focus-visible](components/crops/billing-switch-focus-visible.png) ![Billing switch off](components/crops/billing-switch-off.png)

#### "Sign up free" button
A plan call-to-action — links to the app sign-up, measured never followed. Read as `plan-cta` on the pricing page.
States read on 2026-11-17T15:10:40.751Z (default); 2026-11-17T15:10:42.657Z (hover); 2026-11-17T15:10:44.030Z (focus-visible); 2026-11-17T15:10:45.548Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 306.66 x 36; padding 8px 12px; radius 12px; background #ea580d `light.primary.default`; shadow rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px; text Inter 14/20 500, #fff7ed `light.primary.foreground`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(234, 88, 13, 0.9) |
| focus-visible | shadow rgba(17, 24, 39, 0.2) 0px 0px 0px 1px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px |

!["Sign up free" button default](components/crops/plan-cta-default.png) !["Sign up free" button hover](components/crops/plan-cta-hover.png) !["Sign up free" button focus-visible](components/crops/plan-cta-focus-visible.png) !["Sign up free" button pressed](components/crops/plan-cta-pressed.png)

#### Alternative-comparison card
A "… alternative" card under the pricing grid, same card grammar as the integration cards. Read as `compare-link-card` on the pricing page.
States read on 2026-11-17T15:10:54.438Z (default); 2026-11-17T15:10:56.761Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 314.66 x 56; padding 16px; radius 16px; background #ffffff `light.card.default`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 16/24 500, #111827 `light.root.foreground`; icon 16 x 16, #747170 `light.muted.foreground` |
| hover | icon 16 x 16, #111827 `light.root.foreground` |

![Alternative-comparison card default](components/crops/compare-link-card-default.png) ![Alternative-comparison card hover](components/crops/compare-link-card-hover.png)

### Support

The /support centre's search field (focused, never typed into) and the category cards.

#### Support search input
The "Search…" field at the top of /support. "focused" is the field clicked into — nothing is typed. Read as `support-search` on the support page.
States read on 2026-11-17T15:11:08.608Z (default); 2026-11-17T15:11:11.236Z (focused); 2026-11-17T15:11:18.291Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 976 x 48; padding 4px 12px 4px 40px; border 1px solid #e4e4e7 `light.border.default`; radius 3.35544e+07px; background #ffffff `light.card.default`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 14/20 500, #111827 `light.root.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #747170 `light.muted.foreground` |
| focused, focus-visible | border 1px solid #ff6900 `light.border.ring`; shadow rgba(255, 105, 0, 0.5) 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Support search input default](components/crops/support-search-default.png) ![Support search input focused](components/crops/support-search-focused.png) ![Support search input focus-visible](components/crops/support-search-focus-visible.png)

#### Support category card
A category card on the support index ("Getting started" — heading + one line). Read as `support-category` on the support page.
States read on 2026-11-17T15:11:34.808Z (default); 2026-11-17T15:11:37.472Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 480 x 172; padding 24px; radius 16px; background #ffffff `light.card.default`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 20/28 500, #111827 `light.root.foreground`; icon 20 x 20, #111827 `light.root.foreground` |

![Support category card default](components/crops/support-category-default.png) ![Support category card hover](components/crops/support-category-hover.png)

### Tools

The free-tools layer, read on /tools/color-contrast-checker: the colour input (with its swatch) and the text field — focused, never typed into.

#### Colour input
The native colour swatch input on the contrast checker (input[type=color]) — measured at rest. Read as `tool-color-input` on the contrast-checker tool page.
States read on 2026-11-17T16:34:08.514Z (default); 2026-11-17T16:34:09.907Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; border 1px solid #e4e4e7 `light.border.default`; radius 10px; background #ffffff `light.card.default`; text Inter 16/24 400, #111827 `light.root.foreground`; placeholder #111827 `light.root.foreground` |
| focus-visible | outline 1px auto rgba(255, 105, 0, 0.5), offset 0px |

![Colour input default](components/crops/tool-color-input-default.png) ![Colour input focus-visible](components/crops/tool-color-input-focus-visible.png)

#### Hex text input
The hex value text field beside the colour input (#000000) — measured at rest; nothing is typed. Read as `tool-text-input` on the contrast-checker tool page.
States read on 2026-11-17T16:34:10.846Z (default); 2026-11-17T16:34:12.356Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 282 x 36; padding 4px 12px; border 1px solid #e4e4e7 `light.border.default`; radius 10px; background transparent; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text ui-monospace 14/20 400, #111827 `light.root.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #747170 `light.muted.foreground` |
| focus-visible | border 1px solid #ff6900 `light.border.ring`; shadow rgba(255, 105, 0, 0.5) 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Hex text input default](components/crops/tool-text-input-default.png) ![Hex text input focus-visible](components/crops/tool-text-input-focus-visible.png)

### Contact

The /contact page's email rows and copy-to-clipboard buttons — measured, never pressed.

#### "Copy" icon button
The copy button beside a published contact email — measured, never pressed (it writes to the clipboard). Read as `contact-copy` on the contact page.
States read on 2026-11-17T15:12:08.753Z (default); 2026-11-17T15:12:10.724Z (hover); 2026-11-17T15:12:12.913Z (focus-visible); 2026-11-17T15:12:14.143Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 84 x 36; padding 8px 12px; border 1px solid #e4e4e7 `light.border.default`; radius 12px; background #ffffff `light.card.default`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 14/20 500, #111827 `light.root.foreground`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #111827 `light.root.foreground` |
| hover | background #f6f3f2 `light.color.page`; text Inter 14/20 500, #18181b `light.accent.foreground`; icon 16 x 16, #18181b `light.accent.foreground` |
| focus-visible | border 1px solid rgba(17, 24, 39, 0.2); shadow rgba(17, 24, 39, 0.2) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |
| pressed | background #f6f3f2 `light.color.page`; text Inter 14/20 500, #18181b `light.accent.foreground`; icon 16 x 16, #18181b `light.accent.foreground` |

!["Copy" icon button default](components/crops/contact-copy-default.png) !["Copy" icon button hover](components/crops/contact-copy-hover.png) !["Copy" icon button focus-visible](components/crops/contact-copy-focus-visible.png) !["Copy" icon button pressed](components/crops/contact-copy-pressed.png)

#### Contact channel row
A contact row on /contact ("Sales, inquiries & partnerships" + the published hello@huddlekit.com). Read as `contact-row` on the contact page.

The saved state reads only hello@huddlekit.com (179x28), not the channel row. The picker now requires the channel name and the address together. Not remeasured: no live recapture.

### Prose

The blog article layer on /blog/introducing-huddlekit: the h1, the meta row, body paragraphs and links, and the breadcrumb.

#### Article title (h1)
The post title on a blog article. Read as `prose-h1` on the blog article page.
Read on 2026-11-17T15:12:26.102Z.

**Values (default).** size 634.66 x 48.39; background transparent; text Inter 44/48.4 500, #111827 `light.root.foreground`.

![Article title (h1) default](components/crops/prose-h1-default.png)

#### Article meta line
The date / updated / read-time / author line under the title. Read as `prose-meta` on the blog article page.
Read on 2026-11-17T15:12:28.311Z.

**Values (default).** size 274.66 x 20; background transparent; text Inter 14/20 500, #747170 `light.muted.foreground`.

![Article meta line default](components/crops/prose-meta-default.png)

#### Body paragraph
A paragraph of article prose. Read as `prose-p` on the blog article page.
Read on 2026-11-17T15:12:33.572Z.

**Values (default).** size 634.66 x 72; background transparent; text Inter 16/24 400, #747170 `light.muted.foreground`.

![Body paragraph default](components/crops/prose-p-default.png)

#### Prose link
A body-text link inside the article. Read as `prose-link` on the blog article page.

The saved states read the breadcrumb "Home" (40x20), not a link in the article. The selector is now article :is(p, li) a. Not remeasured: no live recapture.

#### Breadcrumb
The Home / Blog / … breadcrumb above the article. Read as `breadcrumb` on the blog article page.
Read on 2026-11-17T15:12:47.390Z.

**Values (default).** size 634.66 x 20; background transparent; text Inter 14/20 500, #747170 `light.muted.foreground`; icon 14 x 14, #747170 `light.muted.foreground`.

![Breadcrumb default](components/crops/breadcrumb-default.png)

### Integrations

The /integrations grid's cards — measured, never followed.

#### Integration page card
A card on the /integrations index (Slack — icon, name, description). Read as `integration-grid-card` on the integrations page.
States read on 2026-11-17T15:13:02.473Z (default); 2026-11-17T15:13:04.465Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 314.66 x 196; padding 24px; radius 16px; background #ffffff `light.card.default`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 20/28 500, #111827 `light.root.foreground`; icon 20 x 20, #111827 `light.root.foreground` |

![Integration page card default](components/crops/integration-grid-card-default.png) ![Integration page card hover](components/crops/integration-grid-card-hover.png)

### Compare

The /compare/pastel-alternative page's table-of-contents rail and checklist rows — measured, never followed.

#### "Contents" rail
The Contents navigation on a comparison page. Read as `compare-toc` on the compare page page.
Read on 2026-11-17T15:13:23.572Z.

**Values (default).** size 293.33 x 12086.48; background transparent; text Inter 16/24 500, #111827 `light.root.foreground`; icon 16 x 16, #fff7ed `light.primary.foreground`; layers div.bg-card.rounded-md 293.3x304.0 #ffffff 10px; div.bg-card.rounded-lg 293.3x156.0 #ffffff transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px 12px; button.inline-flex.items-center 261.3x36.0 #ea580d transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, trans.

Child layers that carry the look: div 293.3x304 background #ffffff `light.card.default` radius 10px; div 293.3x156 background #ffffff `light.card.default` radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px; button 261.3x36 background #ea580d `light.primary.default` radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px.

!["Contents" rail default](components/crops/compare-toc-default.png)

#### Feature-check list row
A checklist row in the comparison (a lucide check / badge icon + capability line). Read as `compare-check-item` on the compare page page.

The saved state reads the breadcrumb "Home", not a checklist row. The selector now requires a list item that holds an svg and a longer label. Not remeasured: no live recapture.

### App login

app.huddlekit.com/login — the only surface the app serves anonymously: the login card, the 'Continue with Google' and 'Continue with email' buttons, the email field the reveal opens (focused, never typed into, never submitted), its Continue and back buttons. Dark states are the app's own painted dark login under an emulated dark OS preference.

#### Sign-in panel
The centred "Sign in to Huddlekit" panel: wordmark, heading, the Google and email buttons, and the privacy/terms line. Read as `app-login-card` on the app login page.
States read on 2026-11-17T16:30:38.411Z (default); 2026-11-17T16:30:46.279Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 168; background transparent; text inter 18/28 600, #111827 `light.root.foreground`; icon 16 x 16, #fff7ed `light.primary.foreground`; layers button.inline-flex.items-center 320.0x40.0 #ea580d transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px 12px; button.inline-flex.items-center 320.0x40.0 #ede9e7 T:1 |
| dark | text inter 18/28 600, #e3e0df; layers button.inline-flex.items-center 320.0x40.0 #ea580d transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px 12px; button.inline-flex.items-center 320.0x40.0 #2a2625 T:1 |

Child layers that carry the look: button 320x40 background #ea580d `light.primary.default` radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px; button 320x40 background #ede9e7 `light.secondary.default` border 1px solid radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px.

![Sign-in panel default](components/crops/app-login-card-default.png) ![Sign-in panel dark](components/crops/app-login-card-dark.png)

#### "Continue with Google" button
The primary OAuth button (bg-primary). Never pressed — it would leave for Google sign-in. Read as `app-google-button` on the app login page.
States read on 2026-11-17T16:30:52.663Z (default); 2026-11-17T16:30:54.479Z (hover); 2026-11-17T16:30:55.725Z (focus-visible); 2026-11-17T16:30:56.964Z (pressed); 2026-11-17T16:31:03.284Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: dark) | size 320 x 40; padding 0px 16px; radius 12px; background #ea580d `light.primary.default`; shadow rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px; text inter 14/20 500, #fff7ed `light.primary.foreground`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #fff7ed `light.primary.foreground` |
| hover | background rgba(234, 88, 13, 0.9) |
| focus-visible | shadow rgba(17, 24, 39, 0.2) 0px 0px 0px 1px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px |
| pressed | background rgba(234, 88, 13, 0.9) |

!["Continue with Google" button default](components/crops/app-google-button-default.png) !["Continue with Google" button hover](components/crops/app-google-button-hover.png) !["Continue with Google" button focus-visible](components/crops/app-google-button-focus-visible.png) !["Continue with Google" button pressed](components/crops/app-google-button-pressed.png) !["Continue with Google" button dark](components/crops/app-google-button-dark.png)

#### "Continue with email" button
The secondary sign-in button (bg-secondary). "pressed" is the CDP-forced pseudo-state only; the real press is the email-reveal spec below. Read as `app-email-button` on the app login page.
States read on 2026-11-17T16:31:09.632Z (default); 2026-11-17T16:31:11.570Z (hover); 2026-11-17T16:31:12.842Z (focus-visible); 2026-11-17T16:31:14.100Z (pressed); 2026-11-17T16:31:20.412Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 40; padding 0px 16px; border 1px solid transparent; radius 12px; background #ede9e7 `light.secondary.default`; shadow rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px; text inter 14/20 500, #18181b `light.accent.foreground`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #18181b `light.accent.foreground` |
| hover | background rgba(237, 233, 231, 0.8) |
| focus-visible | border 1px solid rgba(17, 24, 39, 0.2); shadow rgba(17, 24, 39, 0.2) 0px 0px 0px 1px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px |
| pressed | background rgba(237, 233, 231, 0.8) |
| dark | background #2a2625; text inter 14/20 500, #fafafa; icon 16 x 16, #fafafa |

!["Continue with email" button default](components/crops/app-email-button-default.png) !["Continue with email" button hover](components/crops/app-email-button-hover.png) !["Continue with email" button focus-visible](components/crops/app-email-button-focus-visible.png) !["Continue with email" button pressed](components/crops/app-email-button-pressed.png) !["Continue with email" button dark](components/crops/app-email-button-dark.png)

#### Email input
The "Enter your email" field the Continue-with-email press reveals — a local state change; nothing is typed and Continue is never pressed. Read as `app-email-input` on the app login page.
States read on 2026-11-17T16:31:28.305Z (default); 2026-11-17T16:31:29.952Z (focused); 2026-11-17T16:31:37.839Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 36; padding 4px 12px; border 1px solid #e4e4e7 `light.border.default`; radius 12px; background #ffffff `light.card.default`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text inter 14/20 400, #111827 `light.root.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #747170 `light.muted.foreground` |
| focused | border 1px solid #ff6900 `light.border.ring`; shadow rgba(255, 105, 0, 0.5) 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |
| dark | border 1px solid rgba(255, 255, 255, 0.16); background rgba(255, 255, 255, 0.048); text inter 14/20 400, #e3e0df; placeholder #a3a09f |

![Email input default](components/crops/app-email-input-default.png) ![Email input focused](components/crops/app-email-input-focused.png) ![Email input dark](components/crops/app-email-input-dark.png)

#### Email "Continue" submit
The primary submit under the email field — measured, never pressed (it would send a sign-in code). Read as `app-continue-button` on the app login page.
States read on 2026-11-17T16:31:46.471Z (default); 2026-11-17T16:31:48.244Z (hover); 2026-11-17T16:31:49.495Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 320 x 40; padding 0px 24px; radius 12px; background #ea580d `light.primary.default`; shadow rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px; text inter 14/20 500, #fff7ed `light.primary.foreground`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.5 |

![Email "Continue" submit default](components/crops/app-continue-button-default.png) ![Email "Continue" submit hover](components/crops/app-continue-button-hover.png) ![Email "Continue" submit focus-visible](components/crops/app-continue-button-focus-visible.png)

#### "Back to login" button
The ghost return control under the email form. Read as `app-back-button` on the app login page.
States read on 2026-11-17T16:31:55.549Z (default); 2026-11-17T16:31:57.338Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 40; padding 0px 16px; border 1px solid transparent; radius 12px; background transparent; text inter 14/20 500, #111827 `light.root.foreground`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #111827 `light.root.foreground` |
| hover | background #f6f3f2 `light.color.page`; text inter 14/20 500, #18181b `light.accent.foreground`; icon 16 x 16, #18181b `light.accent.foreground` |

!["Back to login" button default](components/crops/app-back-button-default.png) !["Back to login" button hover](components/crops/app-back-button-hover.png)

### Chrome (mobile)

The 390px chrome: the compact header, the 'Toggle menu' button and the nav drawer it opens.

#### Mobile header
The header at 390px: logo, the "Toggle menu" button and the "Get started" link. Read as `m-header` on the home page.
Read on 2026-11-17T16:34:23.406Z.

**Values (default).** size 358 x 64; background transparent; text Inter 16/24 400, #111827 `light.root.foreground`; icon 104 x 28, #111827 `light.root.foreground`; layers a.inline-flex.items-center 0.0x0.0 #ede9e7 T:1px solid / R:1px solid / B:1px solid / L:1px solid transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px 12px; button.i.

Child layers that carry the look: a 0x0 background #ede9e7 `light.secondary.default` border 1px solid radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.19) 0px 6px 9px -7px inset, rgba(0, 0, 0, 0.12) 0px 1px 2px 0px, rgba(0, 0, 0, 0.09) 0px 2px 5px -1px; button 36x36 background #ffffff `light.card.default` border 1px solid radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px.

![Mobile header default](components/crops/m-header-default.png)

#### "Toggle menu" button
The hamburger that opens the phone nav. Read as `m-menu-button` on the home page.
States read on 2026-11-17T16:34:24.451Z (default); 2026-11-17T16:34:26.497Z (hover); 2026-11-17T16:34:27.877Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 36 x 36; border 1px solid #e4e4e7 `light.border.default`; radius 12px; background #ffffff `light.card.default`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Inter 14/20 500, #111827 `light.root.foreground`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #111827 `light.root.foreground` |
| focus-visible | border 1px solid rgba(17, 24, 39, 0.2); shadow rgba(17, 24, 39, 0.2) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

!["Toggle menu" button default](components/crops/m-menu-button-default.png) !["Toggle menu" button hover](components/crops/m-menu-button-hover.png) !["Toggle menu" button focus-visible](components/crops/m-menu-button-focus-visible.png)

#### Nav sheet (open)
The opened navigation panel — the "Toggle menu" press drops an absolute rounded-md sheet under the sticky header; the press happens in find(). Read as `m-nav-drawer` on the home page.

The saved state reads the Features link (62x17). domFind no longer falls back to that link when the drawer ancestor is absent. Not remeasured: no live recapture. 62px is not the drawer width.

## Icons

84 distinct inline-SVG icons were collected from the live pages into [icons/](icons) by `tools/capture/icons.mjs`, indexed in [icons/INDEX.tsv](icons/INDEX.tsv): a file is named from `tools/capture/icon-names.tsv` where its geometry hash is listed, else the label or class of the control it sits in, else `icon-<hash>`; colour is kept as `currentColor` wherever it matched the text colour, so each icon recolours from CSS `color` the way it does on the site. The icons are the product's artwork — borrow the set's grammar (sizes, stroke-vs-fill, naming roles), never the artwork itself.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [icon-4f0f75d5](icons/icon-4f0f75d5.svg) | 14x14 16x16 | 0 0 24 24 | stroke | home; pricing; features; blog; blog-post; contact; tools; tool-contrast; mcp; manifesto; integrations; compare; support; nav; feature tabs; faq | New: hand feedback to your AI agent over / Color converters  |
| [huddlekit-on-x](icons/huddlekit-on-x.svg) | 16x16 | 0 0 24 24 | stroke | home; pricing; features; blog; blog-post; contact; tools; tool-contrast; mcp; manifesto; integrations; compare; support; nav; feature tabs; faq | Huddlekit on X |
| [huddlekit-on-instagram](icons/huddlekit-on-instagram.svg) | 16x16 | 0 0 24 24 | stroke | home; pricing; features; blog; blog-post; contact; tools; tool-contrast; mcp; manifesto; integrations; compare; support; nav; feature tabs; faq | Huddlekit on Instagram |
| [get-started-for-free](icons/get-started-for-free.svg) | 16x16 | 0 0 24 24 | stroke | home; pricing; features; blog; blog-post; contact; tools; tool-contrast; mcp; manifesto; integrations; compare; support; nav; feature tabs; faq | Get started for free / Try Huddlekit / Get started |
| [huddlekit-on-linkedin](icons/huddlekit-on-linkedin.svg) | 16x16 | 0 0 24 24 | stroke | home; pricing; features; blog; blog-post; contact; tools; tool-contrast; mcp; manifesto; integrations; compare; support; nav; feature tabs; faq | Huddlekit on LinkedIn / Kevin Larsson on LinkedIn |
| [solutions](icons/solutions.svg) | 14x14 16x16 20x20 | 0 0 24 24 | stroke | home; pricing; features; blog; blog-post; contact; tools; tool-contrast; mcp; manifesto; integrations; compare; support; nav; feature tabs; faq | Solutions / Resources / What is Huddlekit? |
| [icon-4817e690](icons/icon-4817e690.svg) | 16x16 | 0 0 24 24 | stroke | home; pricing; features; mcp; integrations; compare; nav; feature tabs; faq | Linear Turn comments into Linear issues  / ClickUp Turn comm |
| [show-more-testimonials](icons/show-more-testimonials.svg) | 16x16 | 0 0 24 24 | stroke | home; pricing; features; nav; feature tabs; faq | Show more testimonials / Explore all detailed features per p |
| [icon-338378d2](icons/icon-338378d2.svg) | 20x20 | 0 0 24 24 | fill | home; features; integrations; nav; feature tabs; faq | Let your AI agent fix comments over MCP / Claude Add it as a |
| [icon-4c946c22](icons/icon-4c946c22.svg) | 20x20 | 0 0 24 24 | fill | home; features; integrations; nav; feature tabs; faq | Trello Turn comments into Trello cards a |
| [icon-51ced1df](icons/icon-51ced1df.svg) | 20x20 | 0 0 24 24 | fill | home; features; integrations; nav; feature tabs; faq | Slack Post comments to a channel and res |
| [icon-8d3437ac](icons/icon-8d3437ac.svg) | 20x20 | 0 0 24 24 | fill | home; features; integrations; nav; feature tabs; faq | Notion Turn comments into Notion pages a |
| [icon-94705b62](icons/icon-94705b62.svg) | 20x20 | 0 0 24 24 | fill | home; features; integrations; nav; feature tabs; faq | ClickUp Turn comments into ClickUp tasks |
| [icon-a57926b6](icons/icon-a57926b6.svg) | 20x20 | 0 0 24 24 | fill | home; features; integrations; nav; feature tabs; faq | Let your AI agent fix comments over MCP / Claude Code Add th |
| [icon-c9903777](icons/icon-c9903777.svg) | 20x20 | 0 0 24 24 | fill | home; features; integrations; nav; feature tabs; faq | Linear Turn comments into Linear issues  |
| [icon-f4c6796c](icons/icon-f4c6796c.svg) | 20x20 | 0 0 24 24 | fill | home; features; integrations; nav; feature tabs; faq | Let your AI agent fix comments over MCP / Cursor Add the ser |
| [icon-f9ebb370](icons/icon-f9ebb370.svg) | 20x20 | 0 0 24 24 | fill | home; features; integrations; nav; feature tabs; faq | Asana Turn comments into Asana tasks and |
| [saved-and-pasted-by-hand](icons/saved-and-pasted-by-hand.svg) | 16x16 20x20 | 0 0 24 24 | stroke | home; mcp; nav; feature tabs; faq | Saved and pasted by hand / Described in words / Asked for an |
| [icon-1c626323](icons/icon-1c626323.svg) | 16x16 | 0 0 24 24 | fill | home; nav; feature tabs; faq |  |
| [icon-2351a02d](icons/icon-2351a02d.svg) | 16x16 | 0 0 24 24 | fill | home; nav; feature tabs; faq |  |
| [pdf](icons/pdf.svg) | 16x16 | 0 0 24 24 | fill | home; nav; feature tabs; faq | PDF |
| [icon-25077bdf](icons/icon-25077bdf.svg) | 16x16 | 52 42 88 66 | fill | home; nav; feature tabs; faq |  |
| [icon-5ea02472](icons/icon-5ea02472.svg) | 14x14 15x15 16x16 17x17 | 0 0 24 24 | stroke | home; nav; feature tabs; faq |  |
| [icon-96e7c74e](icons/icon-96e7c74e.svg) | 16x16 | 0 0 127 127 | fill | home; nav; feature tabs; faq |  |
| [icon-98b0d58e](icons/icon-98b0d58e.svg) | 16x16 | 0 0 24 24 | fill | home; nav; feature tabs; faq |  |
| [5-star-reviews](icons/5-star-reviews.svg) | 14x14 | 0 0 24 24 | fill | home; nav; feature tabs; faq | 5-star reviews |
| [icon-ebe05e52](icons/icon-ebe05e52.svg) | 16x16 | 0 0 87.5 72 | fill | home; nav; feature tabs; faq |  |
| [icon-3999abc0](icons/icon-3999abc0.svg) | 62x62 | 0 0 56 56 | stroke | home; nav; feature tabs; faq | Devs & designers love this / See how they did it |
| [icon-4747feea](icons/icon-4747feea.svg) | 16x16 20x20 | 0 0 24 24 | stroke | features; nav; faq | Screenshots and debug details Every comm / QA teams |
| [3-team-members](icons/3-team-members.svg) | 14x14 16x16 | 0 0 24 24 | stroke | pricing; tool-contrast; mcp | 3 team members / 1 project / Unlimited guests |
| [integrations](icons/integrations.svg) | 16x16 | 0 0 24 24 | stroke | nav; faq | Integrations |
| [blog](icons/blog.svg) | 16x16 | 0 0 24 24 | stroke | nav; faq | Blog |
| [icon-3fcb0bde](icons/icon-3fcb0bde.svg) | 16x16 20x20 | 0 0 24 24 | stroke | features; support | Dive deeper into the details Open inspec |
| [continue-with-google](icons/continue-with-google.svg) | 16x16 | 0 0 24 24 | fill | app-login; app dark | Continue with Google |
| [freelancers](icons/freelancers.svg) | 16x16 | 0 0 24 24 | stroke | nav; faq | Freelancers |
| [continue-with-email](icons/continue-with-email.svg) | 16x16 | 0 0 24 24 | stroke | app-login; app dark | Continue with email |
| [customers](icons/customers.svg) | 16x16 | 0 0 24 24 | stroke | nav; faq | Customers |
| [tools](icons/tools.svg) | 16x16 | 0 0 24 24 | stroke | nav; faq | Tools |
| [agencies](icons/agencies.svg) | 16x16 | 0 0 24 24 | stroke | nav; faq | Agencies |
| [support](icons/support.svg) | 16x16 | 0 0 24 24 | stroke | nav; faq | Support |
| [icon-da73dca6](icons/icon-da73dca6.svg) | 20x20 | 0 0 24 24 | fill | features; mcp | Works on staging, not just live sites Re / Your own sign-in  |
| [product-teams](icons/product-teams.svg) | 16x16 | 0 0 24 24 | stroke | nav; faq | Product teams |
| [compare](icons/compare.svg) | 16x16 | 0 0 24 24 | stroke | nav; faq | Compare |
| [icon-04365b51](icons/icon-04365b51.svg) | 20x20 | 0 0 24 24 | stroke | features | Folders for every client Group projects  |
| [svg-pointer-events-none](icons/svg-pointer-events-none.svg) | 16x16 | 0 0 24 24 | stroke | contact | Copy hello@huddlekit.com to clipboard / Copy support@huddlek |
| [icon-0f961521](icons/icon-0f961521.svg) | 20x20 | 0 0 24 24 | stroke | features | Replies, mentions, and email alerts Repl |
| [icon-15494c5f](icons/icon-15494c5f.svg) | 20x20 | 0 0 24 24 | stroke | features | Draw on the page Box, circle, arrow, or  |
| [icon-1e361edf](icons/icon-1e361edf.svg) | 20x20 | 0 0 24 24 | stroke | features | Comments pinned to the element Click any |
| [icon-1fc46369](icons/icon-1fc46369.svg) | 24x24 | 0 0 24 24 | stroke | tools | Checklists & QA Launch, redesign, access |
| [icon-20c76def](icons/icon-20c76def.svg) | 20x20 | 0 0 24 24 | stroke | features | Share links that expire Give a link a de |
| [icon-2dc306a4](icons/icon-2dc306a4.svg) | 20x20 | 0 0 24 24 | stroke | features | Review apps behind a login Add a one-lin |
| [sent-with-the-comment](icons/sent-with-the-comment.svg) | 20x20 | 0 0 24 24 | stroke | mcp | Sent with the comment / Exact selector / Captured automatica |
| [icon-3f82afcf](icons/icon-3f82afcf.svg) | 20x20 | 0 0 24 24 | stroke | support | Account Profile, security, and notificat |
| [icon-48872d73](icons/icon-48872d73.svg) | 20x20 | 0 0 24 24 | stroke | features | One task list across all projects See op |
| [icon-4a3b35e1](icons/icon-4a3b35e1.svg) | 20x20 | 0 0 24 24 | stroke | support | Projects Create and manage website, medi |
| [icon-4cb15977](icons/icon-4cb15977.svg) | 20x20 | 0 0 24 24 | fill | integrations | Zapier Send comments to thousands of oth |
| [show-less](icons/show-less.svg) | 16x16 | 0 0 24 24 | stroke | faq | Show less |
| [icon-5444fba7](icons/icon-5444fba7.svg) | 20x20 | 0 0 24 24 | stroke | support | Workspace Manage workspace settings, mem |
| [icon-5c12df2b](icons/icon-5c12df2b.svg) | 20x20 | 0 0 24 24 | stroke | mcp | Read only by default Grant write access  |
| [icon-76a6f97c](icons/icon-76a6f97c.svg) | 20x20 | 0 0 24 24 | stroke | features | Review breakpoints side-by-side See your |
| [icon-7b95e0e2](icons/icon-7b95e0e2.svg) | 20x20 | 0 0 24 24 | stroke | features | Review documents, images, and videos Upl |
| [icon-7cc27a31](icons/icon-7cc27a31.svg) | 20x20 | 0 0 24 24 | stroke | support | Getting started New to Huddlekit? Start  |
| [icon-8282bccf](icons/icon-8282bccf.svg) | 20x20 | 0 0 24 24 | stroke | support | Integrations Connect trackers, Slack, Za |
| [icon-87ab8fb5](icons/icon-87ab8fb5.svg) | 20x20 | 0 0 24 24 | stroke | features | Pause comments between rounds Freeze fee |
| [icon-88259324](icons/icon-88259324.svg) | 20x20 | 0 0 24 24 | stroke | integrations | Send comments to your own code with webh |
| [icon-9889617a](icons/icon-9889617a.svg) | 20x20 | 0 0 24 24 | stroke | support | Troubleshooting Common issues and how to |
| [icon-99739999](icons/icon-99739999.svg) | 20x20 | 0 0 24 24 | stroke | features | A Kanban board for every project Feedbac |
| [icon-a12beb9f](icons/icon-a12beb9f.svg) | 24x24 | 0 0 24 24 | stroke | tools | Proposals & SOWs Web design proposal, SO |
| [icon-b2a060de](icons/icon-b2a060de.svg) | 20x20 | 0 0 24 24 | stroke | features | Custom breakpoints per project Pick the  |
| [icon-b41738f6](icons/icon-b41738f6.svg) | 20x20 | 0 0 24 24 | stroke | features | Layout grids and x-ray, on the live page |
| [icon-ba40db92](icons/icon-ba40db92.svg) | 24x24 | 0 0 24 24 | fill | tools | Color converters HEX, RGB, HSL, and CMYK |
| [icon-c795a586](icons/icon-c795a586.svg) | 20x20 | 0 0 24 24 | stroke | integrations | Send comments to your own code with webh |
| [icon-d02c3231](icons/icon-d02c3231.svg) | 20x20 | 0 0 24 24 | stroke | features | Owners, priorities, and due dates Assign |
| [icon-d069a9ac](icons/icon-d069a9ac.svg) | 20x20 | 0 0 24 24 | stroke | features | Attach files to any comment Add up to fi |
| [icon-da945614](icons/icon-da945614.svg) | 20x20 | 0 0 24 24 | stroke | mcp | Changes apply right away Make a connecti |
| [icon-dcfdeccf](icons/icon-dcfdeccf.svg) | 24x24 | 0 0 24 24 | stroke | tools | CSS & units Convert between px, rem, and |
| [icon-dd6a849a](icons/icon-dd6a849a.svg) | 20x20 | 0 0 24 24 | stroke | support | Billing Plans, invoices, and payment met |
| [icon-dfc4d9c7](icons/icon-dfc4d9c7.svg) | 20x20 | 0 0 24 24 | stroke | features | Private notes beside client feedback Mar |
| [icon-eced62d9](icons/icon-eced62d9.svg) | 20x20 | 0 0 24 24 | stroke | features | Paste a URL and start reviewing No brows |
| [icon-f09f9e0a](icons/icon-f09f9e0a.svg) | 20x20 | 0 0 24 24 | fill | features | Custom tags for your workflow Label feed |
| [icon-f0bce3f9](icons/icon-f0bce3f9.svg) | 20x20 | 0 0 24 24 | stroke | support | Feedback & Comments Leave feedback, mana |
| [toggle-menu](icons/toggle-menu.svg) | 16x16 | 0 0 24 24 | stroke | nav | Toggle menu |
| [icon-fb940f2e](icons/icon-fb940f2e.svg) | 20x20 | 0 0 24 24 | stroke | features | Client-friendly sharing and reviews Send |
| [icon-fd51656b](icons/icon-fd51656b.svg) | 24x24 | 0 0 24 24 | stroke | tools | Browser & device Live readouts of your v |

## Gaps

### The blocked product surfaces

The signed-in product was never entered: everything on **app.huddlekit.com** past **/login** — the project dashboard, the annotation widget on a real site, workspaces, settings, billing — 307-redirects an anonymous visitor back to /login and stays outside. The 'Sign in' and 'Get started' links were measured, never followed; 'Continue with Google' (OAuth) and the email form's 'Continue' were never submitted. The sibling hosts **try.huddlekit.com**, **demo.huddlekit.com**, **status.huddlekit.com**, **docs.huddlekit.com**, **help.huddlekit.com** and **app.huddlekit.io** do not resolve (NXDOMAIN from the capture host, 2026-11-17). All are documented as boundaries, never faked.

### Pages

- **app.huddlekit.com past /login** — the auth wall, see above; the annotation widget, dashboard and workspace UI are uncaptured.
- **try. / demo. / status. / docs. / help. hosts and app.huddlekit.io** — NXDOMAIN or unreachable; documented boundaries.
- **The sitemap's long tail** — huddlekit.com serves ~140 public URLs; the capture holds the one instance of each template that differs (one blog article of twelve, one compare page of sixteen, one support article of ~40, one integration page of eight, one case study of two, the contrast checker of ~30 tools, /privacy standing in for /terms and /dpa, /agencies standing in for /freelancers, /product-teams and /qa-teams). The rest share these templates and were not each crawled.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover) on the controls that carry it, so a state a script adds on mousedown (if any) is missing.
- **These lookups matched the wrong node and are marked missing, not republished:** `faq-question` read the header Solutions trigger; `prose-link` and `compare-check-item` read the breadcrumb Home; `plan-card` read the Free forever label; `contact-row` read only the email; `m-nav-drawer` read the Features link (62px is not the drawer width). The selectors now refuse those nodes. No live recapture was run, so no replacement measurements were invented.
- **The fields were never typed into** — the support search, the contrast checker's inputs and the login's email field were focused for their focus look; nothing was entered, so validation and suggestion states are uncaptured.
- **The login's 'Continue' and 'Continue with Google'** were never pressed (they submit); the email form's resting open state is captured, its submit states are not.
- **Copy-to-clipboard and 'Get started'** — measured, never pressed (clipboard and sign-up flows).
- **The consent banner's 'Accept'** was never pressed; 'Decline' was pressed once to dismiss the banner for the remaining shots.

### Themes

huddlekit.com paints `light` only and offers no theme control — its `.dark` rules re-point the same custom properties inside nested dark panels (the footer, the dark testimonial cards, the MCP card), captured as component-level dark surfaces at rest, never a page theme. app.huddlekit.com paints `html.dark` + `data-theme="dark"` under prefers-color-scheme — the login's `dark` states and `app-login-dark-*` screenshots come from emulating that signal and reloading, verified against the painted surface. Both token themes resolve from the same declarations; `dark` is the re-pointed set the app renders under a dark OS preference.

### Fonts

- **Inter** is the product face (`--font-sans` / `--font-inter`, loaded through next/font with a metrics-matched 'inter Fallback'); **Geist Mono** is the code face (`--font-geist-mono`, next/font) and `--font-mono` the ui-monospace system stack. The woff2 files under /_next/static/media are the licensed files — declared and measured, not shipped. The style guide falls back to the system sans and mono.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The rendered brand strings on the captured pages (the wordmark and copy) are the product's published content.
- Public author names, handles and avatars on captured posts and cards are published content and are kept; nothing private was captured.

### Content left out

- Article copy, post titles, author bios and pricing text are the product's published content; only frames and components were measured.
