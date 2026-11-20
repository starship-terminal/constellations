# Grok components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Read from docs.x.ai on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Later recaptures merge into the same file, so every entry names the date its own states were read; a state a re-read missed keeps its earlier date and says so. Nothing was signed into, bought, searched or submitted; the only presses were local UI toggles the page's own chrome provides — the ⌘K search dialog, the theme button, the product switcher, sidebar groups, SDK tabs and the phone's navigation sheet; every link was measured, never followed.

**Where this was read.** The Grok product itself — grok.com — sits behind a Cloudflare managed challenge that never cleared in headless or headed Chromium from the capture host, and x.ai, console.x.ai, status.x.ai and accounts.x.ai answer a Cloudflare 403 block page. The only publicly reachable Grok-family surface is the product documentation portal, docs.x.ai: one Next.js app holding the API docs, the grok.com help centre, and the Grok Bot, Grok Build and X Subscription sections. Everything in this package is measured there; the blocked surfaces are listed under Gaps.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (35 components, 69 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/20.8 400, #000000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (69 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png` where `{theme}` is the surface the page painted at capture: every docs.x.ai page loads `light`, and `{page}-dark-*` shots are the same page after the header's own 'Switch to dark theme' button repainted html.dark — the painted surface was verified before the shot and the theme switched back after. Desktop shots are 1440 x 900 at 1x; `-full` shots are the whole article at 1x — the docs shell scrolls the article inside its own pane, so the pane's ancestors are relaxed to natural height for the shot and restored after — bounded at eight chunks with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Docs overview | `/overview` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [search](screenshots/home-light-search.png), [sections](screenshots/home-light-sections.png) |
| Quickstart | `/developers/quickstart` | [default](screenshots/quickstart-dark-default.png), [full](screenshots/quickstart-dark-full.png), [default](screenshots/quickstart-light-default.png), [full](screenshots/quickstart-light-full.png), [nav-open](screenshots/quickstart-light-nav-open.png) |
| Models | `/developers/models` | [default](screenshots/models-light-default.png), [full](screenshots/models-light-full.png) |
| Pricing | `/developers/pricing` | [default](screenshots/pricing-dark-default.png), [full](screenshots/pricing-dark-full.png), [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Release notes | `/developers/release-notes` | [default](screenshots/release-notes-light-default.png), [full](screenshots/release-notes-light-full.png) |
| Generate text | `/developers/model-capabilities/text/generate-text` | [default](screenshots/generate-text-dark-default.png), [full](screenshots/generate-text-dark-full.png), [default](screenshots/generate-text-light-default.png), [full](screenshots/generate-text-light-full.png), [tab-python](screenshots/generate-text-light-tab-python.png) |
| API reference | `/developers/rest-api-reference/inference` | [default](screenshots/api-reference-dark-default.png), [full](screenshots/api-reference-dark-full.png), [default](screenshots/api-reference-light-default.png), [full](screenshots/api-reference-light-full.png) |
| FAQ | `/developers/faq/general` | [default](screenshots/faq-light-default.png), [full](screenshots/faq-light-full.png) |
| Cookbook | `/cookbook` | [default](screenshots/cookbook-light-default.png), [full](screenshots/cookbook-light-full.png) |
| Rate limits | `/developers/rate-limits` | [default](screenshots/rate-limits-light-default.png), [full](screenshots/rate-limits-light-full.png) |
| Grok help | `/grok/overview` | [default](screenshots/grok-home-dark-default.png), [full](screenshots/grok-home-dark-full.png), [default](screenshots/grok-home-light-default.png), [full](screenshots/grok-home-light-full.png) |
| Grok FAQ | `/grok/faq` | [default](screenshots/grok-faq-light-default.png), [full](screenshots/grok-faq-light-full.png) |
| Grok user guide | `/grok/user-guide` | [default](screenshots/grok-user-guide-light-default.png), [full](screenshots/grok-user-guide-light-full.png) |
| Grok Bot | `/grok-bot/overview` | [default](screenshots/grok-bot-light-default.png), [full](screenshots/grok-bot-light-full.png) |
| Grok Build | `/build/overview` | [default](screenshots/build-light-default.png), [full](screenshots/build-light-full.png) |
| X Subscription | `/x-subscription/overview` | [default](screenshots/x-subscription-light-default.png), [full](screenshots/x-subscription-light-full.png) |
| Docs overview, phone | `/overview` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Quickstart, phone | `/developers/quickstart` | [default](screenshots/mobile-quickstart-light-default.png), [full](screenshots/mobile-quickstart-light-full.png) |
| Grok help, phone | `/grok/overview` |  |
| Pricing, phone | `/developers/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Search dialog (⌘K) | docs overview | the page's own Ctrl+K shortcut — the cmdk menu opened, captured and closed with Escape; nothing was searched | [home-light-search](screenshots/home-light-search.png), [docs-search-dialog](#search-dialog-cmdk) |
| Product switcher | docs overview header | the switcher button's own press — the menu opened, captured, closed; its links were never followed | [home-light-sections](screenshots/home-light-sections.png) |
| Dark theme | every page header | the 'Switch to dark theme' button's own press; the painted surface was verified before each shot, then switched back | [home-dark-default](screenshots/home-dark-default.png), [docs-header](#fixed-header-bar), [docs-code-block](#code-block-shiki) |
| Sidebar group | quickstart sidebar | a collapsible group's own chevron press | [quickstart-light-nav-open](screenshots/quickstart-light-nav-open.png), [docs-sidebar-group](#sidebar-collapsible-group) |
| SDK tab | generate-text | a language tab's own activation — a local UI toggle that swaps the published snippet | [generate-text-light-tab-python](screenshots/generate-text-light-tab-python.png), [docs-code-tab](#sdk-tab) |
| Mobile nav sheet | docs overview, phone width | the 'Open navigation menu' button's own press | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-docs-drawer](#nav-sheet-open) |
| Grok app, console and marketing site | grok.com, x.ai, console.x.ai | Cloudflare-managed challenge (grok.com) and a Cloudflare 403 block (x.ai family) from the capture host — never reached | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 8 components were given a real keyboard focus. 5 draw an outline ring: `docs-section-link` (1px auto #101010, offset 1px), `docs-code-tab` (1px auto #101010, offset 0px), `docs-next-card` (1px auto #101010, offset 1px), `prose-copy-llm` (1px auto #101010, offset 0px), `prose-link` (1px auto #101010, offset 1px). 3 draw a focus ring as a shadow instead: `docs-search-pill`, `docs-sidebar-link`, `docs-cta`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | faq-question, prose-h1, prose-h2 |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, color, fill, filter, outline-color, stroke, text-decoration-color | docs-code-tab, docs-cta, docs-markdown-link, docs-search-item, docs-search-pill, docs-section-link, docs-theme-button, m-docs-hamburger and more |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | docs-next-card, docs-sidebar-active, docs-sidebar-group, docs-sidebar-link |
| 0.2s | `ease` | all | docs-header, m-docs-topbar |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Search dialog (cmdk)](#search-dialog-cmdk) | 1000 x 485 | - | 16px | #ffffff `light.bg.base` | oklab(0 0 0 / 0.35) 0px 32px 80px -24px | 0 |
| [Nav card](#nav-card) | 672 x 156 | - | 16px | #f9f8f6 `light.bg.card` | none | 28px |
| [Code block (shiki)](#code-block-shiki) | 549.19 x 200 | - | - | transparent | none | 0 |
| [Pricing table](#pricing-table) | 806 x 646.66 | - | - | transparent | none | 0 |
| [Grok Bot phone panel](#grok-bot-phone-panel) | 231 x 172.38 | - | - | transparent | none | 0 |
| [Section sidebar](#section-sidebar) | 272 x 828 | - | - | transparent | none | 0 |
| [Nav sheet (open)](#nav-sheet-open) | 390 x 844 | - | - | #ffffff `light.bg.base` | none | 56px 0px 0px 0px |

## Components

### Docs chrome

The fixed shell every docs.x.ai page carries: the 80px header (wordmark, product switcher, section links, the ⌘K search pill, theme button and GitHub link), the left sidebar nav with its collapsible groups and the sticky page footer with the previous/next pager and the 'View as Markdown' link.

#### Fixed header bar
The 80px bar fixed over every page: wordmark, product switcher, section links, the ⌘K search pill, theme button and GitHub link. Read as `docs-header` on the /overview page.
States read on 2026-11-16T21:38:10.539Z (default); 2026-11-16T21:38:12.516Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1440 x 80; background transparent; text xVf 14/20 500, #0a0a0a `light.fg.default`; transition all 0.2s ease; icon 49.22 x 20, #0a0a0a `light.fg.default`; layers div.from-background.lg:from-background/75 1440.0x96.0; button.focus-visible:ring-ring.items-center 208.0x36.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 3.35544e+07px; div.bg-primary.flex 145.0x36.0 rgb(10, 10, 10) 3.355 |
| dark | text xVf 14/20 500, #ffffff `light.bg.base`; icon 49.22 x 20, #ffffff `light.bg.base`; layers div.from-background.lg:from-background/75 1440.0x96.0; button.focus-visible:ring-ring.items-center 208.0x36.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 3.35544e+07px; div.bg-primary.flex 145.0x36.0 rgb(255, 255, 255) 3. |

Child layers that carry the look: div 1440x96 image linear-gradient(oklab(0.999994 0.0000455678 0.0000200868 / 0.75) 0%, transparent 100%); button 208x36 border 1px solid radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px; div 145x36 background #0a0a0a `light.fg.default` radius 3.35544e+07px.

![Fixed header bar default](components/crops/docs-header-default.png) ![Fixed header bar dark](components/crops/docs-header-dark.png)

#### Wordmark link
The svg wordmark in the header, coloured by the primary foreground role. Read as `docs-logo` on the /overview page.
Read on 2026-11-16T21:38:14.470Z.

**Values (default).** size 57.22 x 28; padding 4px; radius 6px; background transparent; text xVf 16/24 400, #000000 `core.color.scale.black`; icon 49.22 x 20, #0a0a0a `light.fg.default`.

![Wordmark link default](components/crops/docs-logo-default.png)

#### Header section link
A product-section link in the header nav ("Grok Bot" — an inactive pill-shaped label). Read as `docs-section-link` on the /overview page.
States read on 2026-11-16T21:38:15.349Z (default); 2026-11-16T21:38:17.144Z (hover); 2026-11-16T21:38:18.391Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85 x 32; padding 6px 12px; radius 6px; background transparent; text xVf 14/20 500, oklab(0.145746 0.00000663102 0.00000291318 / 0.6); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text xVf 14/20 500, #0a0a0a `light.fg.default` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.flex.items-center 85.0x32.0 1px auto rgb(16, 16, 16) offset 1px 6px |

![Header section link default](components/crops/docs-section-link-default.png) ![Header section link hover](components/crops/docs-section-link-hover.png) ![Header section link focus-visible](components/crops/docs-section-link-focus-visible.png)

#### Search pill (⌘K)
The rounded search field in the header that opens the cmdk dialog; carries the ⌘K hint. Read as `docs-search-pill` on the /overview page.
States read on 2026-11-16T21:38:19.232Z (default); 2026-11-16T21:38:21.023Z (hover); 2026-11-16T21:38:23.038Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 208 x 36; padding 0px 12px 0px 16px; border 1px solid oklab(0.145746 0.00000663102 0.00000291318 / 0.15); radius 3.35544e+07px; background transparent; text xVf 14/20 500, rgba(10, 10, 10, 0.6) `light.fg.muted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(10, 10, 10, 0.6) `light.fg.muted` |
| hover | background rgba(12, 12, 12, 0.03) |
| focus-visible | shadow #0a0a0a 0px 0px 0px 1px |

![Search pill (⌘K) default](components/crops/docs-search-pill-default.png) ![Search pill (⌘K) hover](components/crops/docs-search-pill-hover.png) ![Search pill (⌘K) focus-visible](components/crops/docs-search-pill-focus-visible.png)

#### Theme button
The round icon button that switches html.light/html.dark. "dark" shows it after its own press repaints the page. Read as `docs-theme-button` on the /overview page.
States read on 2026-11-16T21:38:24.602Z (default); 2026-11-16T21:38:26.352Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 28 x 28; radius 3.35544e+07px; background transparent; text xVf 16/24 400, oklab(0.145746 0.00000663102 0.00000291318 / 0.6); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, oklab(0.145746 0.00000663102 0.00000291318 / 0.6) |
| dark | text xVf 16/24 400, #ffffff `light.bg.base`; icon 16 x 16, #ffffff `light.bg.base` |

![Theme button default](components/crops/docs-theme-button-default.png) ![Theme button dark](components/crops/docs-theme-button-dark.png)

#### Section sidebar
The left nav column: product links, the collapsible page groups and the active-page marker. Read as `docs-sidebar` on the /overview page.
States read on 2026-11-16T21:38:28.414Z (default); 2026-11-16T21:38:30.476Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 272 x 828; background transparent; text xVf 13/19.5 500, #0a0a0a `light.fg.default`; icon 12 x 12, rgba(10, 10, 10, 0.6) `light.fg.muted`; layers a.peer/menu-button.group/menu-button 256.0x32.0 rgb(255, 255, 255) 10px; div.focus:ring-ring.gap-1 42.0x18.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px; div.focus:ring-ring.gap-1 36.0x18.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px; div.focus:ring-ring.gap-1 36.0x18.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px; div.focus:ri |
| dark | text xVf 13/19.5 500, #ffffff `light.bg.base`; icon 12 x 12, rgba(255, 255, 255, 0.6); layers a.peer/menu-button.group/menu-button 256.0x32.0 rgb(33, 33, 33) 10px; div.focus:ring-ring.gap-1 42.0x18.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px; div.focus:ring-ring.gap-1 36.0x18.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px; div.focus:ring-ring.gap-1 36.0x18.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px; div.focus:ring- |

Child layers that carry the look: a 256x32 background #ffffff `light.bg.base` radius 10px; div 42x18 border 1px solid radius 3.35544e+07px; div 36x18 border 1px solid radius 3.35544e+07px.

![Section sidebar default](components/crops/docs-sidebar-default.png) ![Section sidebar dark](components/crops/docs-sidebar-dark.png)

#### Sidebar page link
A single page link in the sidebar nav. Read as `docs-sidebar-link` on the /overview page.
States read on 2026-11-16T21:38:32.367Z (default); 2026-11-16T21:38:34.166Z (hover); 2026-11-16T21:38:35.406Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 256 x 32; padding 6px 8px; radius 10px; background transparent; text xVf 13/18.57 500, rgba(10, 10, 10, 0.6) `light.fg.muted`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(12, 12, 12, 0.03); text xVf 13/18.57 500, #0a0a0a `light.fg.default` |
| focus-visible | shadow #0a0a0a 0px 0px 0px 2px inset; layers a.peer/menu-button.group/menu-button 256.0x32.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(10, 10, 10) 0px 0px 0px 2px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 10px |

![Sidebar page link default](components/crops/docs-sidebar-link-default.png) ![Sidebar page link hover](components/crops/docs-sidebar-link-hover.png) ![Sidebar page link focus-visible](components/crops/docs-sidebar-link-focus-visible.png)

#### Sidebar active link
The link for the page being read, painted with the active style. Read as `docs-sidebar-active` on the /overview page.
Read on 2026-11-16T21:38:36.239Z.

**Values (default).** size 256 x 32; padding 6px 8px; radius 10px; background #ffffff `light.bg.base`; text xVf 13/18.57 500, #0a0a0a `light.fg.default`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1).

![Sidebar active link default](components/crops/docs-sidebar-active-default.png)

#### Sidebar collapsible group
A collapsible group row; "opened" is reached by its own chevron press. Read as `docs-sidebar-group` on the /overview page.
States read on 2026-11-16T21:38:37.072Z (default); 2026-11-16T21:38:38.643Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 256 x 32; padding 6px 8px; radius 10px; background transparent; text xVf 13/18.57 500, rgba(10, 10, 10, 0.6) `light.fg.muted`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, rgba(10, 10, 10, 0.6) `light.fg.muted` |
| opened | background rgba(12, 12, 12, 0.03); text xVf 13/18.57 500, #0a0a0a `light.fg.default`; icon 12 x 12, #0a0a0a `light.fg.default` |

![Sidebar collapsible group default](components/crops/docs-sidebar-group-default.png) ![Sidebar collapsible group opened](components/crops/docs-sidebar-group-opened.png)

#### Page footer bar
The sticky bottom bar (bg-base, border-border-l1) with the page actions. Read as `docs-page-footer` on the /developers/quickstart page.
Read on 2026-11-16T21:41:27.301Z.

**Values (default).** size 212 x 81; padding 16px 0px; border T: 1px solid rgba(213, 217, 226, 0.55) `light.border.muted`; background #ffffff `light.bg.base`; text xVf 14/20 400, rgba(10, 10, 10, 0.6) `light.fg.muted`; icon 16 x 16, rgba(10, 10, 10, 0.6) `light.fg.muted`.

![Page footer bar default](components/crops/docs-page-footer-default.png)

#### "View as Markdown" link
The small muted link that serves the page's raw markdown. Read as `docs-markdown-link` on the /developers/quickstart page.
States read on 2026-11-16T21:41:30.962Z (default); 2026-11-16T21:41:34.634Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 133 x 16; background transparent; text xVf 12/16 600, rgba(10, 10, 10, 0.6) `light.fg.muted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(10, 10, 10, 0.6) `light.fg.muted` |
| hover | text xVf 12/16 600, #0a0a0a `light.fg.default`; icon 16 x 16, #0a0a0a `light.fg.default` |

!["View as Markdown" link default](components/crops/docs-markdown-link-default.png) !["View as Markdown" link hover](components/crops/docs-markdown-link-hover.png)

#### "Share feedback" button
A footer action button in the sticky bar — measured, never pressed (it may open a feedback form). Read as `docs-footer-button` on the /developers/quickstart page.
States read on 2026-11-16T21:41:28.162Z (default); 2026-11-16T21:41:29.974Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 212 x 20; background transparent; text xVf 14/20 400, rgba(10, 10, 10, 0.6) `light.fg.muted`; icon 16 x 16, rgba(10, 10, 10, 0.6) `light.fg.muted` |
| hover | text xVf 14/20 400, #0a0a0a `light.fg.default`; icon 16 x 16, #0a0a0a `light.fg.default` |

!["Share feedback" button default](components/crops/docs-footer-button-default.png) !["Share feedback" button hover](components/crops/docs-footer-button-hover.png)

### Docs prose

The article layer: display-family headings, body paragraphs, inline code tinted by the solar accent, body-text links, FAQ question headings and the 'Copy for LLM' action.

#### Page title (h1)
The article title in font-display. Read as `prose-h1` on the /developers/quickstart page.
States read on 2026-11-16T21:41:36.166Z (default); 2026-11-16T21:41:38.065Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 672 x 52.8; background transparent; text xVf 48/52.8 450, #0a0a0a `light.fg.default`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| dark | text xVf 48/52.8 450, #ffffff `light.bg.base` |

![Page title (h1) default](components/crops/prose-h1-default.png) ![Page title (h1) dark](components/crops/prose-h1-dark.png)

#### Section heading (h2)
A numbered step heading. Read as `prose-h2` on the /developers/quickstart page.
Read on 2026-11-16T21:41:40.440Z.

**Values (default).** size 672 x 37.5; background transparent; text xVf 30/37.5 500, #0a0a0a `light.fg.default`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1).

![Section heading (h2) default](components/crops/prose-h2-default.png)

#### Body paragraph
A paragraph of the quickstart. Read as `prose-p` on the /developers/quickstart page.
Read on 2026-11-16T21:41:41.421Z.

**Values (default).** size 672 x 48; background transparent; text xVf 14/24 400, #0a0a0a `light.fg.default`.

![Body paragraph default](components/crops/prose-p-default.png)

#### Inline code span
A `code` span inside prose, tinted by the solar accent. Read as `prose-inline-code` on the /developers/quickstart page.
Read on 2026-11-16T21:41:42.692Z.

**Values (default).** size 32 x 16; background transparent; text xMono 13.3/24 400, #ff640a `core.color.brand.solar`.

![Inline code span default](components/crops/prose-inline-code-default.png)

#### "Copy for LLM" button
The small muted button that copies the page for an LLM — a local clipboard action, pressed only with forcePseudoState. Read as `prose-copy-llm` on the /developers/faq/general page.
States read on 2026-11-16T21:39:35.352Z (default); 2026-11-16T21:39:37.144Z (hover); 2026-11-16T21:39:38.791Z (focus-visible); 2026-11-16T21:39:40.046Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 102 x 16; background transparent; text xVf 12/16 600, rgba(10, 10, 10, 0.6) `light.fg.muted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(10, 10, 10, 0.6) `light.fg.muted` |
| hover | text xVf 12/16 600, #0a0a0a `light.fg.default`; icon 16 x 16, #0a0a0a `light.fg.default` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.text-muted.hover:text-primary 102.0x16.0 1px auto rgb(16, 16, 16) offset 0px |
| pressed | text xVf 12/16 600, #0a0a0a `light.fg.default`; icon 16 x 16, #0a0a0a `light.fg.default` |

!["Copy for LLM" button default](components/crops/prose-copy-llm-default.png) !["Copy for LLM" button hover](components/crops/prose-copy-llm-hover.png) !["Copy for LLM" button focus-visible](components/crops/prose-copy-llm-focus-visible.png) !["Copy for LLM" button pressed](components/crops/prose-copy-llm-pressed.png)

#### FAQ question (h3)
A question heading on the FAQ page — the FAQ lists plain headings, no accordion. Read as `faq-question` on the /developers/faq/general page.
Read on 2026-11-16T21:39:40.941Z.

**Values (default).** size 672 x 33; background transparent; text xVf 24/33 500, #0a0a0a `light.fg.default`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1).

![FAQ question (h3) default](components/crops/faq-question-default.png)

#### Prose link
A body-text link (the "Connectors" link on the Grok help page), underlined with the dotted solar decoration for code spans. Read as `prose-link` on the /grok/overview page.
States read on 2026-11-16T21:34:09.428Z (default); 2026-11-16T21:34:11.200Z (hover); 2026-11-16T21:34:12.441Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 62 x 16; background transparent; text xVf 14/24 500, #0a0a0a `light.fg.default` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.text-primary.underline 62.0x16.0 1px auto rgb(16, 16, 16) offset 1px |

![Prose link default](components/crops/prose-link-default.png) ![Prose link hover](components/crops/prose-link-hover.png) ![Prose link focus-visible](components/crops/prose-link-focus-visible.png)

### Docs widgets

The interactive furniture: shiki code blocks (a dark-tinted panel even in the light theme), the Radix language tabs, nav cards, the solid hero CTAs, pricing and parameter tables, and the Grok Bot phone mock.

#### Code block (shiki)
The shiki-highlighted sample under the hero: a dark-tinted panel even in the light theme. Read as `docs-code-block` on the /overview page.
States read on 2026-11-16T21:38:39.771Z (default); 2026-11-16T21:38:41.735Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: dark) | size 549.19 x 200; background transparent; text xMono 13/20 400, #f97583 |

![Code block (shiki) default](components/crops/docs-code-block-default.png) ![Code block (shiki) dark](components/crops/docs-code-block-dark.png)

#### Primary CTA link
A solid call-to-action in the hero ("Get Started" / "Create API key") — primary bg, primary-foreground text. Read as `docs-cta` on the /overview page.
States read on 2026-11-16T21:38:43.597Z (default); 2026-11-16T21:38:45.388Z (hover); 2026-11-16T21:38:46.645Z (focus-visible); 2026-11-16T21:38:47.897Z (pressed); 2026-11-16T21:38:49.764Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 151 x 40; padding 10px 18px; radius 3.35544e+07px; background #0a0a0a `light.fg.default`; text xVf 14/20 500, #f9f8f6 `light.bg.card`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #f9f8f6 `light.bg.card` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, oklab(0.145746 0.00000663102 0.00000291318 / 0.3) 0px 0px 0px 4px |
| dark | background #ffffff `light.bg.base`; text xVf 14/20 500, #0a0a0a `light.fg.default`; icon 16 x 16, #0a0a0a `light.fg.default` |

![Primary CTA link default](components/crops/docs-cta-default.png) ![Primary CTA link hover](components/crops/docs-cta-hover.png) ![Primary CTA link focus-visible](components/crops/docs-cta-focus-visible.png) ![Primary CTA link pressed](components/crops/docs-cta-pressed.png) ![Primary CTA link dark](components/crops/docs-cta-dark.png)

#### Inline feature link
A small underlined link inside a feature row (decoration-primary/30). Read as `docs-text-link` on the /overview page.
States read on 2026-11-16T21:38:51.763Z (default); 2026-11-16T21:38:53.546Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 97 x 18.56; background transparent; text xVf 13/18.57 400, #0a0a0a `light.fg.default`; icon 12 x 12, #0a0a0a `light.fg.default` |

![Inline feature link default](components/crops/docs-text-link-default.png) ![Inline feature link hover](components/crops/docs-text-link-hover.png)

#### SDK tabs
The language picker above a code sample ("Python", "TypeScript", "cURL", ...): a Radix tablist. Read as `docs-code-tabs` on the /developers/quickstart page.
Read on 2026-11-16T21:41:44.874Z.

**Values (default).** size 432 x 24; background transparent; text xVf 12/16 400, #0a0a0a `light.fg.default`; icon 16 x 16, #0a0a0a `light.fg.default`; layers span.bg-primary/[0.06].pointer-events-none 98.0x24.0 oklab(0.145746 0.00000663102 0.00000291318 / 0.06) 3.35544e+07px.

Child layers that carry the look: span 98x24 background oklab(0.145746 0.00000663102 0.00000291318 / 0.06) radius 3.35544e+07px.

![SDK tabs default](components/crops/docs-code-tabs-default.png)

#### SDK tab
One tab in the picker. "selected" is the tab's own activation — a local UI toggle that swaps the published snippet. Read as `docs-code-tab` on the /developers/quickstart page.
States read on 2026-11-16T21:41:45.719Z (default); 2026-11-16T21:41:47.522Z (hover); 2026-11-16T21:41:48.805Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 98 x 24; padding 4px 8px; radius 12px; background transparent; text xVf 12/16 400, #0a0a0a `light.fg.default`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #0a0a0a `light.fg.default` |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.mb-0.inline-flex 98.0x24.0 1px auto rgb(16, 16, 16) offset 0px 12px |

![SDK tab default](components/crops/docs-code-tab-default.png) ![SDK tab hover](components/crops/docs-code-tab-hover.png) ![SDK tab focus-visible](components/crops/docs-code-tab-focus-visible.png)

#### Nav card
A filled card link at the foot of a docs page (bg-card, hover:bg-card-hover). Read as `docs-next-card` on the /developers/quickstart page.
States read on 2026-11-16T21:41:49.795Z (default); 2026-11-16T21:41:51.687Z (hover); 2026-11-16T21:41:53.031Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 672 x 156; padding 28px; radius 16px; background #f9f8f6 `light.bg.card`; text xVf 20/28 500, #0a0a0a `light.fg.default`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, oklab(0.145746 0.00000663102 0.00000291318 / 0.6) |
| hover | background #edecea `light.color.cardHover`; icon 12 x 12, #0a0a0a `light.fg.default` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Nav card default](components/crops/docs-next-card-default.png) ![Nav card hover](components/crops/docs-next-card-hover.png) ![Nav card focus-visible](components/crops/docs-next-card-focus-visible.png)

#### Pricing table
A token-pricing table: header row with a bottom border, dense cells. Read as `pricing-table` on the /developers/pricing page.
States read on 2026-11-16T21:33:14.286Z (default); 2026-11-16T21:33:16.625Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 806 x 646.66; background transparent; text xVf 14/20 500, #0a0a0a `light.fg.default`; layers th.whitespace-nowrap.px-3 235.5x42.7 L:1px solid; tr.border-border.border-b 806.0x44.5 B:1px solid; th.text-secondary.whitespace-nowrap 81.5x44.5 L:1px solid; tr 806.0x70.0 B:1px solid; td.whitespace-nowrap.px-3 246.0x70.0 B:1px solid; td.whitespace-nowrap.px-3 81.0x70.0 B:1px solid |
| dark | text xVf 14/20 500, #d5d9e2 `light.border.subtle` |

Child layers that carry the look: th 235.5x42.7 border 1px solid; tr 806x44.5 border 1px solid; th 81.5x44.5 border 1px solid.

![Pricing table default](components/crops/pricing-table-default.png) ![Pricing table dark](components/crops/pricing-table-dark.png)

#### Table header cell
A th in the pricing table. Read as `pricing-th` on the /developers/pricing page.
Read on 2026-11-16T21:33:18.525Z.

**Values (default).** size 246 x 87.16; padding 8px 12px 16px 0px; background transparent; text xVf 14/20 500, #0a0a0a `light.fg.default`.

![Table header cell default](components/crops/pricing-th-default.png)

#### Table cell
A td in the pricing table. Read as `pricing-td` on the /developers/pricing page.
Read on 2026-11-16T21:33:19.355Z.

**Values (default).** size 246 x 70; padding 14px 12px 14px 0px; border B: 1px solid rgba(213, 217, 226, 0.55) `light.border.muted`; background transparent; text xVf 14/21 500, #0a0a0a `light.fg.default`; layers td.whitespace-nowrap.px-3 246.0x70.0 B:1px solid.

Child layers that carry the look: td 246x70 border 1px solid.

![Table cell default](components/crops/pricing-td-default.png)

#### Grok Bot phone panel
The phone-shaped routine panel (.gbm-panel) on the Grok Bot page — the product's illustrative mock. Read as `gbm-panel` on the /grok-bot/overview page.
States read on 2026-11-16T21:34:25.931Z (default); 2026-11-16T21:34:28.738Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 231 x 172.38; background transparent; text DejaVu Sans 12/18 700, #0a0a0a `light.fg.default` |
| dark | text DejaVu Sans 12/18 700, #f2f2f2 |

![Grok Bot phone panel default](components/crops/gbm-panel-default.png) ![Grok Bot phone panel dark](components/crops/gbm-panel-dark.png)

### Docs search

The ⌘K command menu (cmdk): the modal the header pill and the page's own shortcut open, its field and suggestion rows — opened and closed only through the page's own controls; nothing was searched.

#### Search dialog (cmdk)
The ⌘K command menu: "Ask Grok" plus page suggestions, painted by the page's own shortcut. Read as `docs-search-dialog` on the /overview page.
States read on 2026-11-16T21:39:59.235Z (default); 2026-11-16T21:40:24.082Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1000 x 485; radius 16px; background #ffffff `light.bg.base`; shadow oklab(0 0 0 / 0.35) 0px 32px 80px -24px; text xVf 14/20 400, rgba(10, 10, 10, 0.6) `light.fg.muted`; icon 16 x 16, rgba(10, 10, 10, 0.6) `light.fg.muted` |
| dark | background #0a0a0a `light.fg.default`; text xVf 14/20 400, rgba(255, 255, 255, 0.6); icon 16 x 16, rgba(255, 255, 255, 0.6) |

![Search dialog (cmdk) default](components/crops/docs-search-dialog-default.png) ![Search dialog (cmdk) dark](components/crops/docs-search-dialog-dark.png)

#### Search input
The command field; "focused" is the field clicked into — nothing is typed. Read as `docs-search-input` on the /overview page.
States read on 2026-11-16T21:39:53.859Z (default); 2026-11-16T21:39:55.192Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 1000 x 48; padding 12px; background transparent; text xVf 16/24 400, #000000 `core.color.scale.black`; placeholder rgba(10, 10, 10, 0.6) `light.fg.muted` |

![Search input default](components/crops/docs-search-input-default.png) ![Search input focused](components/crops/docs-search-input-focused.png)

#### Suggestion row
A suggestion row in the open menu ("Ask Grok anything", "Quickstart", ...). Read as `docs-search-item` on the /overview page.
States read on 2026-11-16T21:39:56.101Z (default); 2026-11-16T21:39:58.005Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 475 x 54; padding 8px 12px; radius 8px; background oklab(0.438999 -0.00000439584 0.0000102818 / 0.1); text xVf 14/20 500, #000000 `core.color.scale.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(10, 10, 10, 0.6) `light.fg.muted` |

![Suggestion row default](components/crops/docs-search-item-default.png) ![Suggestion row hover](components/crops/docs-search-item-hover.png)

### Docs chrome (mobile)

The 390px surface: the fixed bar with the 'Open navigation menu' button and the nav sheet it opens.

#### Mobile header
The fixed bar at 390px: hamburger, wordmark, search and theme icons. Read as `m-docs-topbar` on the /overview page.
Read on 2026-11-16T21:42:04.267Z.

**Values (default).** size 390 x 68; background transparent; text xVf 16/24 400, #000000 `core.color.scale.black`; transition all 0.2s ease; icon 49.22 x 20, #0a0a0a `light.fg.default`; layers div.from-background.lg:from-background/75 390.0x128.0; button.focus-visible:ring-ring.items-center 0.0x0.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 3.35544e+07px; div.bg-primary.flex 0.0x0.0 rgb(10, 10, 10) 3.35544e+07.

Child layers that carry the look: div 390x128 image linear-gradient(in oklab, #ffffff `light.bg.base` 0%, transparent 100%); button 0x0 border 1px solid radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px; div 0x0 background #0a0a0a `light.fg.default` radius 3.35544e+07px.

![Mobile header default](components/crops/m-docs-topbar-default.png)

#### "Open navigation menu" button
The hamburger that opens the nav sheet. Read as `m-docs-hamburger` on the /overview page.
States read on 2026-11-16T21:42:05.095Z (default); 2026-11-16T21:42:06.860Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 36 x 36; radius 3.35544e+07px; background transparent; text xVf 14/20 500, #0a0a0a `light.fg.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #0a0a0a `light.fg.default` |

!["Open navigation menu" button default](components/crops/m-docs-hamburger-default.png) !["Open navigation menu" button hover](components/crops/m-docs-hamburger-hover.png)

#### Nav sheet (open)
The opened navigation sheet — a full-screen fixed aside over the page. The "Open navigation menu" press happens in find(): the sheet is only visible once open, so the state itself is a no-op. Read as `m-docs-drawer` on the /overview page.
Read on 2026-11-16T21:42:09.342Z.

**Values (opened).** size 390 x 844; padding 56px 0px 0px 0px; background #ffffff `light.bg.base`; text xVf 16/24 500, #0a0a0a `light.fg.default`; icon 12 x 12, rgba(10, 10, 10, 0.6) `light.fg.muted`.

![Nav sheet (open) opened](components/crops/m-docs-drawer-opened.png)

## Icons

91 distinct inline-SVG icons were collected from the live pages into [icons/](icons) by `tools/capture/icons.mjs`, indexed in [icons/INDEX.tsv](icons/INDEX.tsv): a file is named from `tools/capture/icon-names.tsv` where its geometry hash is listed, else the label or class of the control it sits in, else `icon-<hash>`; colour is kept as `currentColor` wherever it matched the text colour, so each icon recolours from CSS `color` the way it does on the site. The icons are the product's artwork — borrow the set's grammar (sizes, stroke-vs-fill, naming roles), never the artwork itself.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [spacexsi-docs-home](icons/spacexsi-docs-home.svg) | 39x16 49x20 | 0 7.4 24 9.2 | fill | home; quickstart; models; pricing; generate-text; api-reference; release-notes; cookbook; faq; grok; grok-faq; grok-guide; grok-bot; build; x-subscription; search dialog; header; nav; dark | SpaceXSI Docs home |
| [open-api-sections](icons/open-api-sections-431f249f.svg) | 12x12 16x16 | 0 0 16 16 | stroke | home; quickstart; models; pricing; generate-text; api-reference; release-notes; cookbook; faq; grok; grok-faq; grok-guide; grok-bot; build; x-subscription; search dialog; header; dark | Open API sections / More links |
| [search-k](icons/search-k.svg) | 16x16 | 0 0 24 24 | fill | home; quickstart; models; pricing; generate-text; api-reference; release-notes; cookbook; faq; grok; grok-faq; grok-guide; grok-bot; build; x-subscription; search dialog; header; dark | Search ⌘ K |
| [copy-code](icons/copy-code.svg) | 16x16 | 0 0 24 24 | fill | home; quickstart; models; pricing; generate-text; api-reference; release-notes; faq; grok; grok-faq; grok-guide; grok-bot; build; x-subscription; search dialog; header; nav; dark | Copy code / Copy for LLM |
| [switch-to-dark-theme](icons/switch-to-dark-theme.svg) | 16x16 | 0 0 24 24 | fill | home; quickstart; models; pricing; generate-text; api-reference; release-notes; cookbook; faq; grok; grok-faq; grok-guide; grok-bot; build; x-subscription; search dialog; header; dark | Switch to dark theme / Switch to light theme |
| [agentic-coding](icons/agentic-coding.svg) | 16x16 | 0 0 24 24 | stroke | home; quickstart; models; pricing; generate-text; api-reference; release-notes; faq; grok; grok-faq; grok-guide; grok-bot; build; x-subscription; search dialog; header; nav; dark | Agentic coding / IDE & tool integrations / Powers Grok Build |
| [configurable](icons/configurable.svg) | 12x12 14x14 16x16 | 0 0 24 24 | stroke | home; quickstart; models; pricing; generate-text; api-reference; release-notes; faq; grok; grok-faq; grok-guide; search dialog; header; nav; dark | Configurable / Create an API key / Purchase credits |
| [view-as-markdown](icons/view-as-markdown.svg) | 16x16 | 0 0 24 24 | fill | quickstart; models; pricing; generate-text; api-reference; release-notes; faq; grok; grok-faq; grok-guide; grok-bot; build; x-subscription | View as Markdown |
| [speech-to-speech](icons/speech-to-speech.svg) | 12x12 | 0 0 24 24 | stroke | home; quickstart; models; pricing; generate-text; api-reference; release-notes; cookbook; faq; search dialog; header; nav; dark | Speech to Speech / Generated Media / In Depth |
| [share-feedback](icons/share-feedback.svg) | 16x16 | 0 0 24 24 | fill | quickstart; models; pricing; generate-text; api-reference; release-notes; faq; grok; grok-faq; grok-guide; grok-bot; build; x-subscription | Share feedback |
| [create-api-key](icons/create-api-key.svg) | 16x16 | 0 0 24 24 | stroke | home; quickstart; models; pricing; generate-text; api-reference; release-notes; faq; search dialog; header; nav; dark | Create API key |
| [icon-d0acd0c8](icons/icon-d0acd0c8.svg) | 16x16 | 0 0 24 24 | stroke | quickstart; models; pricing; generate-text; release-notes; faq; grok; grok-faq; grok-guide; grok-bot; build; x-subscription |  |
| [python](icons/python.svg) | 16x16 | 0 0 24 24 | fill | home; quickstart; generate-text; build; search dialog; header; nav; dark | Python |
| [javascript](icons/javascript.svg) | 16x16 | 0 0 24 24 | fill | home; quickstart; generate-text; build; search dialog; header; nav; dark | JavaScript |
| [copy-model-slug-grok-4-7](icons/copy-model-slug-grok-4-7.svg) | 12x24 | 0 0 15 15 | fill | home; models; search dialog; header; nav; dark | Copy model slug grok-4.7 |
| [image-video-api](icons/image-video-api.svg) | 24x24 | 0 0 24 24 | fill | home; models; search dialog; header; nav; dark | Image & Video API |
| [voice-api](icons/voice-api.svg) | 24x24 | 0 0 24 24 | stroke | home; models; search dialog; header; nav; dark | Voice API |
| [2-00-1m-input-tokens](icons/2-00-1m-input-tokens.svg) | 16x16 | 0 0 24 24 | stroke | home; search dialog; header; nav; dark | $2.00 / 1M input tokens / $6.00 / 1M output tokens |
| [icon-eee355e2](icons/icon-eee355e2.svg) | 14x14 | 0 0 24 24 | fill | models; pricing; generate-text; grok-guide | All tool names work in the Responses API |
| [icon-724f2cc9](icons/icon-724f2cc9.svg) | 12x12 | 0 0 24 24 | stroke | quickstart; cookbook | Code Agentic coding with grok-4.7 on the / Chat Multi-turn c |
| [bots-learn-quickly](icons/bots-learn-quickly.svg) | 27x27 | 0 0 100 100 | fill | grok-bot | Bots learn quickly |
| [agent-settings](icons/agent-settings.svg) | 15x15 | 0 0 300 300 | fill | grok-bot | Agent settings |
| [close-navigation-menu](icons/close-navigation-menu.svg) | 20x20 | 0 0 24 24 | stroke | nav | Close navigation menu |
| [icon-17824975](icons/icon-17824975.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Advanced Meeting to Action  |
| [icon-178bf7f6](icons/icon-178bf7f6.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate Prompt Injecti |
| [bots-remember-you](icons/bots-remember-you.svg) | 27x27 | 0 0 100 100 | fill | grok-bot | Bots remember you |
| [mark](icons/mark-1b0fb979.svg) | 48x48 | 0 0 100 100 | fill | grok-bot | Pitch Deck Coach Reviews a pitch deck an |
| [sign-ups](icons/sign-ups.svg) | 36x36 | 0 0 100 100 | fill | grok-bot | Sign-ups |
| [bot](icons/bot.svg) | 27x27 | 0 0 100 100 | fill | grok-bot | Talk to it like a teammate |
| [close-computer](icons/close-computer.svg) | 14x14 | 0 0 300 300 | fill | grok-bot | Close computer |
| [icon-21686ad4](icons/icon-21686ad4.svg) | 36x36 | 0 0 100 100 | fill | grok-bot | Fact check, Unread activity |
| [attach-docs-pages](icons/attach-docs-pages.svg) | 14x14 | 0 0 24 24 | fill | grok-bot | Attach docs pages |
| [icon-2724ca19](icons/icon-2724ca19.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate Prompt Caching |
| [icon-2743e385](icons/icon-2743e385.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Beginner Screenshot to Reac |
| [icon-29866ab6](icons/icon-29866ab6.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Advanced WebRTC Voice Agent |
| [icon-33f8fb69](icons/icon-33f8fb69.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Python · Intermediate Web V |
| [bots-hand-off-work](icons/bots-hand-off-work.svg) | 28x28 | 0 0 100 100 | fill | grok-bot | Bots hand off work |
| [icon-3841b800](icons/icon-3841b800.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate Receipts to Sp |
| [icon-3ba1f80b](icons/icon-3ba1f80b.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate CSV to Answers |
| [mark](icons/mark-3de7b627.svg) | 48x48 | 0 0 100 100 | fill | grok-bot | Tradbot Watches your personal email and  |
| [icon-4326270e](icons/icon-4326270e.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Beginner Photo to Talking C |
| [icon-479032ec](icons/icon-479032ec.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate Docs to Cited  |
| [chief-of-staff-main-bot](icons/chief-of-staff-main-bot.svg) | 24x24 36x36 40x40 | 0 0 100 100 | fill | grok-bot | Chief of Staff, Main Bot / Your primary Bot Ask your main Bo |
| [voice-message](icons/voice-message.svg) | 14x14 | 0 0 300 300 | fill | grok-bot | Voice message |
| [icon-4e1b62a1](icons/icon-4e1b62a1.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate Database over  |
| [icon-52340591](icons/icon-52340591.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate Reasoning Effo |
| [pause-carousel](icons/pause-carousel.svg) | 14x14 | 0 0 24 24 | fill | grok-bot | Pause carousel |
| [launch-drafts](icons/launch-drafts.svg) | 36x36 | 0 0 100 100 | fill | grok-bot | Launch drafts |
| [search](icons/search.svg) | 14x14 | 0 0 300 300 | fill | grok-bot | Search |
| [gmail](icons/gmail.svg) | 12x12 16x16 40x40 | 0.53 0.53 190.94 190.94 | fill | grok-bot | Gmail / Gmail, connected / checks inbox |
| [expenses](icons/expenses.svg) | 36x36 | 0 0 100 100 | fill | grok-bot | Expenses |
| [icon-70d5cda1](icons/icon-70d5cda1.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate Storyboard to  |
| [bots-share-a-computer](icons/bots-share-a-computer.svg) | 27x27 | 0 0 100 100 | fill | grok-bot | Bots share a computer |
| [icon-82496c18](icons/icon-82496c18.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate Company to Cal |
| [inbox](icons/inbox.svg) | 24x24 36x36 | 0 0 100 100 | fill | grok-bot | Inbox / Connect your tools Connect the apps you  |
| [icon-89e9bf2d](icons/icon-89e9bf2d.svg) | 14x14 | 0 0 24 24 | fill | grok-guide |  |
| [search-docs](icons/search-docs.svg) | 16x16 | 0 0 24 24 | fill | nav | Search docs |
| [works-where-you-are](icons/works-where-you-are.svg) | 27x27 | 0 0 100 100 | fill | grok-bot | Works where you are |
| [icon-999556fd](icons/icon-999556fd.svg) | 14x14 | 0 0 24 24 | fill | faq |  |
| [icon-a10955a1](icons/icon-a10955a1.svg) | 16x16 | 0 0 24 24 | fill | cookbook |  |
| [icon-a2a79be5](icons/icon-a2a79be5.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Beginner Podcast from a Lin |
| [icon-a2cc9f92](icons/icon-a2cc9f92.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate Topics to Morn |
| [leads-unread-activity](icons/leads-unread-activity.svg) | 24x24 36x36 | 0 0 100 100 | fill | grok-bot | Leads, Unread activity / Leads / Give a Bot a job Hand a Bot |
| [icon-a823dc70](icons/icon-a823dc70.svg) | 16x16 | 0 0 24 24 | fill | search dialog | Ask Grok anything Get an instant answer  |
| [send-message](icons/send-message.svg) | 16x16 | 0 0 24 24 | fill | grok-bot | Send message |
| [icon-a9683419](icons/icon-a9683419.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate Product Photo  |
| [icon-ab83386c](icons/icon-ab83386c.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate 𝕏 Sentiment T |
| [icon-acf23a82](icons/icon-acf23a82.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate Photo to Time- |
| [new-bot](icons/new-bot.svg) | 14x14 | 0 0 300 300 | fill | grok-bot | New Bot / Your primary Bot Ask your main Bot what' / A team  |
| [grok-bot-for-teams](icons/grok-bot-for-teams.svg) | 12x12 | 0 0 24 24 | fill | grok-bot | Grok Bot for teams / Browse all apps / Bots hand off work |
| [icon-b0fa2997](icons/icon-b0fa2997.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate Reviews to The |
| [google-calendar](icons/google-calendar.svg) | 12x12 16x16 40x40 | 7.03 1.03 177.94 177.94 | fill | grok-bot | Google Calendar / Google Calendar, connected / checks calend |
| [granola](icons/granola.svg) | 12x12 40x40 | -1.266 -1.266 34.531 34.531 | fill | grok-bot | Granola / Granola, not connected |
| [icon-bddbcc19](icons/icon-bddbcc19.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate 𝕏 Post to Fac |
| [notion](icons/notion.svg) | 12x12 40x40 | -21.74 -14.56 378.47 378.47 | fill | grok-bot | Notion / Notion, not connected |
| [open-api-sections](icons/open-api-sections-c6ea8231.svg) | 12x12 | 0 0 16 16 | stroke | header | Open API sections |
| [mark](icons/mark-cf664d23.svg) | 48x48 | 0 0 100 100 | fill | grok-bot | Overheard Watches Reddit, Hacker News, n |
| [icon-d1f57712](icons/icon-d1f57712.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Advanced Bug Report to Fix  |
| [mark](icons/mark-d58c5b44.svg) | 48x48 | 0 0 100 100 | fill | grok-bot | Meeting Recap Deck Turns your meeting no |
| [icon-da5d3e73](icons/icon-da5d3e73.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Advanced Video Dubbing Dub  |
| [icon-e2d205c4](icons/icon-e2d205c4.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Beginner Article to Read-Al |
| [icon-e81a461c](icons/icon-e81a461c.svg) | 14x14 | 0 0 24 24 | fill | grok-faq |  |
| [grok-bot](icons/grok-bot.svg) | 24x24 36x36 40x40 64x64 | 0 0 100 100 | fill | grok-bot | Grok Bot / Morning briefing Each morning, one Bot s / Dispat |
| [google-drive](icons/google-drive.svg) | 12x12 40x40 | 5.81 4.88 180.38 180.38 | fill | grok-bot | Google Drive / Google Drive, connected |
| [icon-f29ebf47](icons/icon-f29ebf47.svg) | 20x20 | 0 0 24 24 | fill | cookbook | Swift · Kotlin · Intermediate Mobile Voi |
| [icon-f2b0decc](icons/icon-f2b0decc.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Beginner Live Interpreter S |
| [slack](icons/slack.svg) | 12x12 16x16 40x40 | -2.246 -2.298 58.386 58.386 | fill | grok-bot | Slack / Slack, connected / posts to #design |
| [icon-f8c29f52](icons/icon-f8c29f52.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Intermediate Phone Voice Ag |
| [icon-fd11eecd](icons/icon-fd11eecd.svg) | 16x24 | 0 0 24 24 | stroke | search dialog |  |
| [icon-fd4cbba4](icons/icon-fd4cbba4.svg) | 20x20 | 0 0 24 24 | fill | cookbook | TypeScript · Advanced Refund Agent with  |
| [chevron](icons/chevron.svg) | 12x12 | 0 0 300 300 | fill | grok-bot | Your primary Bot Ask your main Bot what' / Morning briefing  |

## Gaps

### The blocked product surfaces

The Grok product itself was never reached from the capture host: **grok.com** answers every request with a Cloudflare managed challenge ('Verify you are human') that never cleared — headless Chromium, headed Chromium under Xvfb and a bounded Turnstile attempt all stayed on the interstitial — and **x.ai**, **console.x.ai**, **status.x.ai** and **accounts.x.ai** answer a Cloudflare 403 'Sorry, you have been blocked' page. The chat UI, the marketing site, the API console, login/signup cards and every post-login surface are therefore documented as boundaries, not captured. The challenge and block responses are recorded in the README; no workaround was attempted beyond the standard headed/headless passes.

### Pages

- **The Grok app (grok.com) and its login/signup boundary cards** — blocked at the edge, see above. The docs portal's own header links to grok.com but the link was never followed.
- **The API console (console.x.ai)** — blocked at the edge; it is also the signed-in surface for API keys and usage.
- **Sibling docs pages** — connector pages, management pages, per-model pages and the rest of the tree share the templates captured here (prose, code, tables, tabs, cards); they were not each measured.
- **The llms.txt and 'View as Markdown' bodies** — the markdown mirrors were listed, not crawled.

### States

- **Pressed** was forced with DevTools on the controls that carry it, so a state a script adds on mousedown (if any) is missing.
- **The search field was never typed into** — the ⌘K dialog was captured open with its resting suggestion list and closed with Escape; no query was run, so search results and the 'Ask Grok' answer pane are uncaptured.
- **The product switcher menu** was captured open at overview level; its destination sections were never followed from the menu.
- **Sidebar groups** were toggled once on the quickstart; the full expand/collapse matrix was not exercised.
- **The theme button** was pressed to paint dark for the `dark` states and shots, then pressed back — no theme was held across navigations.

### Themes

docs.x.ai boots `html.light` from `localStorage.theme` (next-themes) and the header carries a real theme button. `light` is the painted default; `dark` states and `{page}-dark-*` screenshots were painted through that button, verified by the painted surface (html class, color-scheme and the computed background), and the theme was switched back afterwards. Both token themes resolve from the same semantic declarations — `.dark` re-points them.

### Fonts

- **xVf** (variable, weight 200–800) is the product face — `--font-x-vf`, driving `--font-sans`/`--font-display`; **xMono** (variable, weight 200–800) draws code (`--font-x-mono`/`--font-mono`). Both are self-hosted woff2 under /_next/static/media, proprietary to xAI — declared and measured, not shipped. The style guide falls back to the system sans and mono.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The rendered brand strings on the captured pages (the wordmark and copy) are the product's published content.

### Content left out

- Article copy, prices, model names and recipe titles are the product's content; only frames and components were measured.
