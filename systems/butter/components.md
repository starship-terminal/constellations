# Butter components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from butter.video (reached via usebutter.com, which redirects to www.butter.video) on 2026-11-11, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the login page was never filled; the plan actions were never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (36 components, 83 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (82 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: the marketing pages paint `light`, the app-shell pages `dark`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Product | `/product` | [default](screenshots/product-light-default.png), [full](screenshots/product-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [monthly](screenshots/pricing-light-monthly.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| MCP | `/mcp` | [claude](screenshots/mcp-light-claude.png), [default](screenshots/mcp-light-default.png), [full](screenshots/mcp-light-full.png) |
| Contact | `/contact` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Terms of service | `/terms-of-service` | [default](screenshots/terms-light-default.png) |
| Explore (app shell) | `/explore` | [default](screenshots/explore-dark-default.png), [full](screenshots/explore-dark-full.png) |
| Blocks (app shell) | `/blocks` | [default](screenshots/blocks-dark-default.png), [full](screenshots/blocks-dark-full.png) |
| Templates (app shell) | `/templates` | [default](screenshots/templates-dark-default.png), [full](screenshots/templates-dark-full.png) |
| Log in | `/login` | [default](screenshots/login-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Explore, phone | `/explore` | [default](screenshots/mobile-explore-dark-default.png), [full](screenshots/mobile-explore-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-nav-item](#mobile-nav-item) |
| Desktop nav dropdown | every marketing page | the Co-Create/Product trigger's own toggle | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-dropdown), [menu-link](#nav-menu-link) |
| iubenda consent banner | every page | hidden, never answered (no consent button was ever clicked) | hidden before every shot and reading |
| Billing-period toggle | /pricing | the Monthly/Annually buttons' own toggle | [pricing-light-monthly](screenshots/pricing-light-monthly.png), [billing-toggle](#billing-toggle) |
| MCP agent tabs | /mcp | the Claude tab's own toggle | [mcp-light-claude](screenshots/mcp-light-claude.png) |
| Signed-in product | app.butter.video workspace | the editor lives behind /login | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 15 components were given a real keyboard focus. 4 draw an outline ring: `nav-cta` (on a child: 3px solid rgb(77, 197, 229) offset 3px), `hero-cta` (on a child: 3px solid rgb(77, 197, 229) offset 3px), `plan-cta` (on a child: 3px solid rgb(77, 197, 229) offset 3px), `d-card` (1px auto #99c8ff, offset 0px). 7 draw a focus ring as a shadow instead: `nav-link`, `nav-trigger`, `menu-link`, `billing-toggle`, `footer-link`, `social-icon`, `m-nav-item`. The other 4 show no measured change: `d-nav-link`, `d-login`, `d-signup`, `d-create`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.16s | `ease` | background-color, border-color, opacity, transform | d-block-card, d-card, d-create, d-login, d-signup |
| 0.2s | `ease` | opacity, transform | cursor-badge |
| 0.5s | `cubic-bezier(0.2, 0.715, 0.205, 0.99)` | clip-path, color, opacity, transform | billing-toggle, m-menu-open, nav-trigger |
| 0.8s | `cubic-bezier(0.2, 0.715, 0.205, 0.99)` | opacity | m-menu-open |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 308.2 x 1132.59 | - | - | transparent | none | 25px 25px 40px 25px |
| [Feature card](#feature-card) | 637.03 x 437 | 1px solid #212121 `color.app.card-border` | 32px | #151515 `color.app.card` | none | 0 |
| [Block card](#block-card) | 359 x 181 | - | 42px | #151515 `color.app.card` | none | 13px |
| [Cursor badge](#cursor-badge) | 62.54 x 25.82 | - | 12px | #0f0f0f `color.neutral.ink` | none | 10px 13px |
| [Mobile nav item](#mobile-nav-item) | 262.66 x 73 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The floating grey header island: wordmark, the Co-Create and Product dropdowns, plain links, Login and the dark Try-for-free pill.

#### Header
The marketing header: wordmark, the Co-Create/Product dropdown, plain links, Login and the Try-for-free pill. Read as `header` on the home page.

**Values (default).** size 1440 x 88; background transparent; text DieGrotesk 18/27 400, #fafafa `color.neutral.paper-warm`; icon 107 x 23, #1e1e1e `color.neutral.soft-ink`; layers a.index-style__SkipToContent-sc-d968d94e-2.gWhVeu 137.0x47.0 rgb(30, 30, 30) 8px; div::before.index-style__HeaderLeftInner-sc-d968d94e-5.ckqdyg 708.312pxx64px rgb(237, 237, 237) 16px; div.index-style__HeaderDropdown-sc-d968d94e-11.kVgSbW 694.1x382.7 rgb(237, 237, 237); hr.index-style__Hr-sc-a31f9adc-0.hAUIis 0.0x1.0 rgba(15, 15, 15, 0.15); hr.index-style__Hr-sc-a31f9adc-0.gTNDyN 0.0x1.0 rgba(15, 1.

Child layers that carry the look: a 137x47 background #1e1e1e `color.neutral.soft-ink` radius 8px; div::before 708.312pxx64px background #ededed `color.neutral.grey` radius 16px; div 694.1x382.7 background #ededed `color.neutral.grey`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Logo
The wordmark anchor (an unclassed <a> wrapping the Butter svg). Read as `logo` on the home page.

**Values (default).** size 107 x 23; background transparent; text DieGrotesk 18/27 400, #1e1e1e `color.neutral.soft-ink`; icon 107 x 23, #1e1e1e `color.neutral.soft-ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Nav link
A plain header link (Pricing/Blog). Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 49.58 x 20; background transparent; text DieGrotesk 16/20 400, #1e1e1e `color.neutral.soft-ink` |
| focus-visible | shadow #3c3c3c 0px 0px 0px 1px; layers a 49.6x20.0 rgb(60, 60, 60) 0px 0px 0px 1px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Nav CTA
The Try-for-free header action; links to /explore, measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 110.5 x 39; background transparent; text DieGrotesk 16/21 400, #ebebeb; layers span.index-style__ButtonContent-sc-482eeec2-1.kszsnD 110.5x39.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 10px; span::before.index-style__ButtonContent-sc-482eeec2-1.kszsnD 108.5pxx37px rgb(77, 197, 229) rgb(77, 197, 229) 0px 0px 4px 0px, rgb(77, 197, 229) 1px 1px 2px 0px, rgb(99, 173, 69) 1px 2px 2px 0px, rgb(233, 211 |
| focus-visible | shadow #3c3c3c 0px 0px 0px 1px; layers a 110.5x39.0 rgb(60, 60, 60) 0px 0px 0px 1px; span.index-style__ButtonContent-sc-482eeec2-1.kszsnD 110.5x39.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 3px solid rgb(77, 197, 229) offset 3px 10px; span::before.index-style__ButtonContent-sc-482eeec2-1.kszsnD 108.5pxx37px rgb(77, 197, 229) rgb(77, 197, 229) 0px 0px 4px 0 |

Child layers that carry the look: span 110.5x39 border 1px solid transparent radius 10px; span::before 108.5pxx37px background #4dc5e5 `color.brand.blue` radius 10px shadow #4dc5e5 `color.brand.blue` 0px 0px 4px 0px, #4dc5e5 `color.brand.blue` 1px 1px 2px 0px, #63ad45 `color.brand.green` 1px 2px 2px 0px, #e9d352 `color.brand.yellow` 1px 4px 6px 0px, #4dc5e5 `color.brand.blue` 1px 6px 10px 0px; span::after 108.5pxx37px background #1e1e1e `color.neutral.soft-ink` radius 10px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Nav trigger
The Co-Create button that opens the header dropdown; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73.13 x 20; background transparent; text DieGrotesk 16/20 400, #1e1e1e `color.neutral.soft-ink`; transition opacity 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99) |
| hover | opacity 0.4 |
| focus-visible | shadow #3c3c3c 0px 0px 0px 1px; layers button.index-style__CoCreateTrigger-sc-adb0d9eb-0.kOPflO 73.1x20.0 rgb(60, 60, 60) 0px 0px 0px 1px |
| pressed | opacity 0.4 |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Nav dropdown
The Product dropdown panel, opened by hovering its own trigger. Read as `nav-dropdown` on the home page.

**Values (default).** size 666.71 x 149.45; background transparent; text DieGrotesk 16/20 400, #1e1e1e `color.neutral.soft-ink`; layers hr.index-style__Hr-sc-a31f9adc-0.hAUIis 0.0x1.0 rgba(15, 15, 15, 0.15); hr.index-style__Hr-sc-a31f9adc-0.gTNDyN 0.0x1.0 rgba(15, 15, 15, 0.15); hr.index-style__Hr-sc-a31f9adc-0.fphVdi 0.0x1.0 rgba(15, 15, 15, 0.15); hr.index-style__Hr-sc-a31f9adc-0.gkleBz 0.0x1.0 rgba(15, 15, 15, 0.15).

Child layers that carry the look: hr 0x1 background rgba(15, 15, 15, 0.15) `color.neutral.hairline`; hr 0x1 background rgba(15, 15, 15, 0.15) `color.neutral.hairline`; hr 0x1 background rgba(15, 15, 15, 0.15) `color.neutral.hairline`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Menu link
A link inside the opened header dropdown. Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 666.71 x 28.42; background transparent; text DieGrotesk 16/20 400, #1e1e1e `color.neutral.soft-ink`; layers hr.index-style__Hr-sc-a31f9adc-0.hAUIis 0.0x1.0 rgba(15, 15, 15, 0.15) |
| focus-visible, pressed | shadow #3c3c3c 0px 0px 0px 1px; layers a 666.7x28.4 rgb(60, 60, 60) 0px 0px 0px 1px; hr.index-style__Hr-sc-a31f9adc-0.hAUIis 0.0x1.0 rgba(15, 15, 15, 0.15) |

Child layers that carry the look: hr 0x1 background rgba(15, 15, 15, 0.15) `color.neutral.hairline`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Home

The 107px hero over the keyring artwork, the dark Get-Started pill and the collaboration cursor badges.

#### Hero headline
The 108px display headline (TextStyles__Heading1Styled). Read as `hero-title` on the home page.

**Values (default).** size 1081.77 x 106.69; background transparent; text DieGrotesk 107.56/106.70 400, #0f0f0f `color.neutral.ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Hero CTA
The hero Get-Started action; measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 144.95 x 50; background transparent; text DieGrotesk 16/21 400, #ebebeb; layers span.index-style__ButtonContent-sc-482eeec2-1.bsawCq 145.0x50.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 16px; span::before.index-style__ButtonContent-sc-482eeec2-1.bsawCq 142.953pxx48px rgb(77, 197, 229) rgb(77, 197, 229) 0px 0px 4px 0px, rgb(77, 197, 229) 1px 1px 2px 0px, rgb(99, 173, 69) 1px 2px 2px 0px, rgb(233, 2 |
| focus-visible | shadow #3c3c3c 0px 0px 0px 1px; layers a 145.0x50.0 rgb(60, 60, 60) 0px 0px 0px 1px; span.index-style__ButtonContent-sc-482eeec2-1.bsawCq 145.0x50.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 3px solid rgb(77, 197, 229) offset 3px 16px; span::before.index-style__ButtonContent-sc-482eeec2-1.bsawCq 142.953pxx48px rgb(77, 197, 229) rgb(77, 197, 229) 0px 0px 4px |

Child layers that carry the look: span 145x50 border 1px solid transparent radius 16px; span::before 142.953pxx48px background #4dc5e5 `color.brand.blue` radius 16px shadow #4dc5e5 `color.brand.blue` 0px 0px 4px 0px, #4dc5e5 `color.brand.blue` 1px 1px 2px 0px, #63ad45 `color.brand.green` 1px 2px 2px 0px, #e9d352 `color.brand.yellow` 1px 4px 6px 0px, #4dc5e5 `color.brand.blue` 1px 6px 10px 0px; span::after 142.953pxx48px background #1e1e1e `color.neutral.soft-ink` radius 16px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Hero copy
The lede under the headline. Read as `hero-sub` on the home page.

**Values (default).** size 467.67 x 108.16; background transparent; text DieGrotesk 24.48/28.15 400, #0f0f0f `color.neutral.ink`; layers span.index-style__ButtonContent-sc-482eeec2-1.bsawCq 145.0x50.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 16px; span::before.index-style__ButtonContent-sc-482eeec2-1.bsawCq 142.953pxx48px rgb(77, 197, 229) rgb(77, 197, 229) 0px 0px 4px 0px, rgb(77, 197, 229) 1px 1px 2px 0px, rgb(99, 173, 69) 1px 2px 2px 0px, rgb(233, 2.

Child layers that carry the look: span 145x50 border 1px solid transparent radius 16px; span::before 142.953pxx48px background #4dc5e5 `color.brand.blue` radius 16px shadow #4dc5e5 `color.brand.blue` 0px 0px 4px 0px, #4dc5e5 `color.brand.blue` 1px 1px 2px 0px, #63ad45 `color.brand.green` 1px 2px 2px 0px, #e9d352 `color.brand.yellow` 1px 4px 6px 0px, #4dc5e5 `color.brand.blue` 1px 6px 10px 0px; span::after 142.953pxx48px background #1e1e1e `color.neutral.soft-ink` radius 16px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Cursor badge
The custom-cursor pill ("Add butter") that follows the pointer. Captured in its hidden state (opacity 0, scale .6): it only paints while a real pointer follows the page, which synthetic movement does not wake — the reported box is the shrunken pill, not its visible size. Read as `cursor-badge` on the home page.

**Values (default).** size 62.54 x 25.82; padding 10px 13px; radius 12px; background #0f0f0f `color.neutral.ink`; text DieGrotesk 16/21 400, #fafafa `color.neutral.paper-warm`; transition opacity 0.2s ease, transform 0.2s ease; transform scale(0.6); opacity 0.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Section heading
A 60px section heading (TextStyles__Heading2Styled). Read as `section-h2` on the home page.

**Values (default).** size 1077.59 x 185.86; background transparent; text DieGrotesk 60.4/58.58 400, transparent.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Pricing

The pricing surface: Monthly/Annually toggle, the four grey plan cards with their dark Choose actions, the feature-comparison rows and the FAQ accordion.

#### Pricing title
The "Unlimit your creativity." display heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 949.34 x 106.69; background transparent; text DieGrotesk 107.56/106.70 400, #0f0f0f `color.neutral.ink`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Billing toggle
A Monthly/Annually billing-period button; toggled, never checked out. Read as `billing-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 118.89 x 54; padding 15px 20px; background transparent; text DieGrotesk 20.74/24 400, #fafafa `color.neutral.paper-warm`; transition color 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99), opacity 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99) |
| focus-visible | shadow #3c3c3c 0px 0px 0px 1px; layers button.index-style__PricingToggle-sc-51b11a00-2.cEBaxH 118.9x54.0 rgb(60, 60, 60) 0px 0px 0px 1px |

![Billing toggle default](components/crops/billing-toggle-default.png) ![Billing toggle hover](components/crops/billing-toggle-hover.png) ![Billing toggle focus-visible](components/crops/billing-toggle-focus-visible.png) ![Billing toggle pressed](components/crops/billing-toggle-pressed.png)

#### Plan card
A pricing plan card (the Pro tier); the grey 32px-radius fill is a sibling Background layer, reported under Child layers. Read as `plan-card` on the pricing page.

**Values (default).** size 308.2 x 1132.59; padding 25px 25px 40px 25px; background transparent; text ABCDiatype 13.49/24 400, #0f0f0f `color.neutral.ink`; icon 13 x 9, #0f0f0f `color.neutral.ink`; layers div.index-style__PricingCardHighlightTooltip-sc-9eabdcbf-6.jPGyaI 123.0x35.5 rgb(237, 237, 237) 12px; div.index-style__PricingCardName-sc-9eabdcbf-7.dLZuhC 258.2x64.0 rgb(250, 250, 250) 16px; span.index-style__ButtonContent-sc-482eeec2-1.bsawCq 258.2x70.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 16px; span::before.ind.

Child layers that carry the look: div 123x35.5 background #ededed `color.neutral.grey` radius 12px; div 258.2x64 background #fafafa `color.neutral.paper-warm` radius 16px; span 258.2x70 border 1px solid transparent radius 16px.

![Plan card default](components/crops/plan-card-default.png)

#### Plan price
A plan card's price figure ($18 annually / $25 monthly). Read as `plan-price` on the pricing page.

**Values (default).** size 258.2 x 58.59; background transparent; text DieGrotesk 60.4/58.58 400, #0f0f0f `color.neutral.ink`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan Choose-Pro action; measured never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 258.2 x 70; background transparent; text DieGrotesk 16/21 400, #ebebeb; layers span.index-style__ButtonContent-sc-482eeec2-1.bsawCq 258.2x70.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 16px; span::before.index-style__ButtonContent-sc-482eeec2-1.bsawCq 256.203pxx68px rgb(77, 197, 229) rgb(77, 197, 229) 0px 0px 4px 0px, rgb(77, 197, 229) 1px 1px 2px 0px, rgb(99, 173, 69) 1px 2px 2px 0px, rgb(233, 2 |
| focus-visible | layers a 258.2x70.0 rgb(60, 60, 60) 0px 0px 0px 1px; span.index-style__ButtonContent-sc-482eeec2-1.bsawCq 258.2x70.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 3px solid rgb(77, 197, 229) offset 3px 16px; span::before.index-style__ButtonContent-sc-482eeec2-1.bsawCq 256.203pxx68px rgb(77, 197, 229) rgb(77, 197, 229) 0px 0px 4px |

Child layers that carry the look: span 258.2x70 border 1px solid transparent radius 16px; span::before 256.203pxx68px background #4dc5e5 `color.brand.blue` radius 16px shadow #4dc5e5 `color.brand.blue` 0px 0px 4px 0px, #4dc5e5 `color.brand.blue` 1px 1px 2px 0px, #63ad45 `color.brand.green` 1px 2px 2px 0px, #e9d352 `color.brand.yellow` 1px 4px 6px 0px, #4dc5e5 `color.brand.blue` 1px 6px 10px 0px; span::after 256.203pxx68px background #1e1e1e `color.neutral.soft-ink` radius 16px.

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### FAQ item
A Frequently-Asked accordion question (button.AccordionTrigger); toggled open would reveal the answer, never clicked. Read as `faq-item` on the pricing page.

**Values (default).** size 641.41 x 75; background transparent; text DieGrotesk 24.48/28.15 400, #0f0f0f `color.neutral.ink`; icon 14 x 8, #5a5a5a.

![FAQ item default](components/crops/faq-item-default.png)

#### Feature row
A feature-comparison accordion row (Free stock photos, Reseller rights, ...). Read as `feature-row` on the pricing page.

**Values (default).** size 1636.44 x 72; padding 25px 0px; border T: 1px solid rgba(15, 15, 15, 0.15) `color.neutral.hairline`; background transparent; text DieGrotesk 16/21 400, #0f0f0f `color.neutral.ink`.

![Feature row default](components/crops/feature-row-default.png)

### App shell (dark)

The dark MUI shell on /explore, /blocks and /templates: sidebar, nav pills, inverted buttons and the rounded template cards.

#### App sidebar
The dark app-shell rail: wordmark, Home/Explore/Templates/Blocks nav, Log-in/Sign-up at the foot. Read as `d-sidebar` on the explore page.

**Values (default).** size 283 x 900; background transparent; text dieGroteskA 12/16 400, #a1a1aa `color.app.muted`; icon 110 x 24, #f5f5f5 `color.app.text`; layers div.MuiStack-root.css-14i17xy-root 283.0x900.0 rgb(10, 9, 9); div.MuiStack-root.css-NavItem-content-ref 245.0x39.0 rgb(37, 37, 37) 12px; a.MuiButtonBase-root.css-1e0gtz4-button 251.0x38.0 rgb(29, 29, 29) 10px; a.MuiButtonBase-root.css-gqu8g2-button 251.0x38.0 rgb(245, 245, 245) 10px.

Child layers that carry the look: div 283x900 background #0a0909 `color.app.canvas`; div 245x39 background #252525 `color.app.active` radius 12px; a 251x38 background #1d1d1d `color.app.raised` radius 10px.

![App sidebar default](components/crops/d-sidebar-default.png)

#### Sidebar link
A nav link inside the dark sidebar. Read as `d-nav-link` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 245 x 39; radius 12px; background transparent; text dieGroteskA 14/20 400, #f5f5f5 `color.app.text`; icon 21 x 21, #f5f5f5 `color.app.text`; layers div.MuiStack-root.css-NavItem-content-ref 245.0x39.0 rgb(37, 37, 37) 12px |
| focus-visible | layers div.MuiStack-root.css-NavItem-content-ref 245.0x39.0 rgb(37, 37, 37) rgb(245, 245, 245) 0px 0px 0px 0.5px inset 12px |

Child layers that carry the look: div 245x39 background #252525 `color.app.active` radius 12px.

![Sidebar link default](components/crops/d-nav-link-default.png) ![Sidebar link hover](components/crops/d-nav-link-hover.png) ![Sidebar link focus-visible](components/crops/d-nav-link-focus-visible.png) ![Sidebar link pressed](components/crops/d-nav-link-pressed.png)

#### Sidebar login
The sidebar Log-in button (dark fill); measured never followed. Read as `d-login` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 251 x 38; padding 10px 16px; radius 10px; background #1d1d1d `color.app.raised`; text dieGroteskA 13/18 400, #f5f5f5 `color.app.text`; transition opacity 0.16s ease, background-color 0.16s ease, border-color 0.16s ease |
| hover, pressed | background #252525 `color.app.active`; opacity 0.9 |

![Sidebar login default](components/crops/d-login-default.png) ![Sidebar login hover](components/crops/d-login-hover.png) ![Sidebar login focus-visible](components/crops/d-login-focus-visible.png) ![Sidebar login pressed](components/crops/d-login-pressed.png)

#### Sidebar signup
The sidebar Sign-up button (white pill); measured never followed. Read as `d-signup` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 251 x 38; padding 10px 16px; radius 10px; background #f5f5f5 `color.app.text`; text dieGroteskA 13/18 400, #0a0909 `color.app.canvas`; transition opacity 0.16s ease, background-color 0.16s ease, border-color 0.16s ease |
| hover, pressed | opacity 0.9 |

![Sidebar signup default](components/crops/d-signup-default.png) ![Sidebar signup hover](components/crops/d-signup-hover.png) ![Sidebar signup focus-visible](components/crops/d-signup-focus-visible.png) ![Sidebar signup pressed](components/crops/d-signup-pressed.png)

#### Create button
The top-bar Create action (white pill on the dark shell); measured never followed. Read as `d-create` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 111.38 x 48; padding 12px 20px; radius 10px; background #f5f5f5 `color.app.text`; text dieGroteskA 14/20 400, #0a0909 `color.app.canvas`; transition opacity 0.16s ease, background-color 0.16s ease, border-color 0.16s ease; icon 16 x 16, #0a0909 `color.app.canvas` |
| hover, pressed | opacity 0.9 |

![Create button default](components/crops/d-create-default.png) ![Create button hover](components/crops/d-create-hover.png) ![Create button focus-visible](components/crops/d-create-focus-visible.png) ![Create button pressed](components/crops/d-create-pressed.png)

#### Search field
The shell search input, if one paints; never typed into. Read as `d-search` on the explore page.

Not on the page when it was captured.

#### Feature card
A large feature/release card on /explore. Read as `d-card` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 637.03 x 437; border 1px solid #212121 `color.app.card-border`; radius 32px; background #151515 `color.app.card`; text dieGroteskA 18/25 400, #f5f5f5 `color.app.text`; transition transform 0.16s ease |
| hover | size 624.29 x 428.26; transform scale(0.98) |
| focus-visible | outline 1px auto #99c8ff, offset 0px |
| pressed | size 624.29 x 428.26; transform scale(0.98) |

![Feature card default](components/crops/d-card-default.png) ![Feature card hover](components/crops/d-card-hover.png) ![Feature card focus-visible](components/crops/d-card-focus-visible.png) ![Feature card pressed](components/crops/d-card-pressed.png)

#### Block card
A block-preview card in the Featured Blocks row. Read as `d-block-card` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 359 x 181; padding 13px; radius 42px; background #151515 `color.app.card`; text dieGroteskA 14/20 400, #f5f5f5 `color.app.text`; transition transform 0.16s ease, background-color 0.16s ease |
| hover, pressed | size 351.82 x 177.38; transform scale(0.98) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Block card default](components/crops/d-block-card-default.png) ![Block card hover](components/crops/d-block-card-hover.png) ![Block card pressed](components/crops/d-block-card-pressed.png)

#### Section heading
An /explore section heading (24px). Read as `d-section` on the explore page.

**Values (default).** size 150 x 30; background transparent; text dieGroteskA 24/30 400, #f5f5f5 `color.app.text`.

![Section heading default](components/crops/d-section-default.png)

### Footer

The light-grey footer: link columns and social links.

#### Footer
The light-grey FooterMain: link columns, social, legal. Read as `footer` on the home page.

**Values (default).** size 1440 x 1126.81; padding 160px 0px 60px 0px; background #ededed `color.neutral.grey`; text ABCDiatype 13.49/24 400, rgba(15, 15, 15, 0.5) `color.neutral.faint`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 71.73 x 24; background transparent; text DieGrotesk 20.74/24 400, #1e1e1e `color.neutral.soft-ink` |
| focus-visible | shadow #3c3c3c 0px 0px 0px 1px; layers a 71.7x24.0 rgb(60, 60, 60) 0px 0px 0px 1px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Social link
A social link in the footer (text links, not glyphs). Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 90.73 x 24; background transparent; text DieGrotesk 20.74/24 400, #1e1e1e `color.neutral.soft-ink` |
| focus-visible | shadow #3c3c3c 0px 0px 0px 1px; layers a 90.7x24.0 rgb(60, 60, 60) 0px 0px 0px 1px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Mobile (390 wide)

The marketing surface at phone width: slimmer header island, stacked menu rows, smaller display type.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 76.2; background transparent; text DieGrotesk 18/27 400, #fafafa `color.neutral.paper-warm`; icon 107 x 23, #1e1e1e `color.neutral.soft-ink`; layers a.index-style__SkipToContent-sc-d968d94e-2.gWhVeu 137.0x47.0 rgb(30, 30, 30) 8px; div::before.index-style__HeaderLeftInner-sc-d968d94e-5.ckqdyg 290.656pxx64px rgb(237, 237, 237) 16px; div.index-style__HeaderDropdown-sc-d968d94e-11.kVgSbW 284.8x370.4 rgb(237, 237, 237); hr.index-style__Hr-sc-a31f9adc-0.hAUIis 0.0x1.0 rgba(15, 15, 15, 0.15); hr.index-style__Hr-sc-a31f9adc-0.gTNDyN 0.0x1.0 rgba(15, 1.

Child layers that carry the look: a 137x47 background #1e1e1e `color.neutral.soft-ink` radius 8px; div::before 290.656pxx64px background #ededed `color.neutral.grey` radius 16px; div 284.8x370.4 background #ededed `color.neutral.grey`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The menu toggle (button.MenuToggleMain). Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 23 x 31; padding 10px; radius 5px; background transparent; text DieGrotesk 16/20 400, #1e1e1e `color.neutral.soft-ink`; icon 3 x 11, #1e1e1e `color.neutral.soft-ink`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The whole header menu panel opened by its own toggle (div.index-style__HeaderDropdown). Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 290.66 x 554; padding 14px 14px 22px 14px; background #ededed `color.neutral.grey`; text DieGrotesk 16/20 400, #1e1e1e `color.neutral.soft-ink`; transition opacity 0.8s cubic-bezier(0.2, 0.715, 0.205, 0.99), transform 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99), clip-path 0.5s cubic-bezier(0.2, 0.715, 0.205, 0.99); transform translate(0px, 554px).

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
A link inside the opened header menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 262.66 x 73; background transparent; text DieGrotesk 16/20 400, #1e1e1e `color.neutral.soft-ink`; layers div::after.index-style__ButterBlockWrapper-sc-dca6eb83-0.kBcKnP 64pxx64px rgb(255, 255, 255) 0px 0px 11.7px 0px inset 22.4%; hr.index-style__Hr-sc-a31f9adc-0.hyIksl 262.7x1.0 rgba(15, 15, 15, 0.15) |
| focus-visible | shadow #3c3c3c 0px 0px 0px 1px; layers a 262.7x73.0 rgb(60, 60, 60) 0px 0px 0px 1px; div::after.index-style__ButterBlockWrapper-sc-dca6eb83-0.kBcKnP 64pxx64px rgb(255, 255, 255) 0px 0px 11.7px 0px inset 22.4%; hr.index-style__Hr-sc-a31f9adc-0.hyIksl 262.7x1.0 rgba(15, 15, 15, 0.15) |

Child layers that carry the look: div::after 64pxx64px radius 22.4% shadow #ffffff `color.neutral.paper` 0px 0px 11.7px 0px inset; hr 262.7x1 background rgba(15, 15, 15, 0.15) `color.neutral.hairline`.

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 338.3 x 123.63; background transparent; text DieGrotesk 56.72/61.83 400, #0f0f0f `color.neutral.ink`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Butter wordmark, social glyphs, the keyring/3-D artwork, the dark shell's glyphs) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The Butter editor itself lives behind /login — the signed-in workspace, projects, exports, billing and the API keys the /mcp page advertises all need an account and were never reached. The dark /explore, /blocks and /templates surfaces look like the product but are public marketing galleries of blocks and templates, signed out.

### Pages

- **The workspace.** Every post-login surface was never reached; /login was captured as a form and never filled or submitted.
- **Checkout and signup.** Every Try-for-free, Get-Started and Choose-plan action was measured, never followed.
- **The editor.** Blocks and templates open in the editor only inside the product; gallery cards were measured, never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **d-search** is recorded missing: the /explore shell paints no search input when signed out.
- **FAQ answers** stay closed: the accordion questions were measured, never expanded.

### Themes

The site paints two surfaces rather than a theme toggle: the marketing pages are light-only and the /explore, /blocks and /templates app shell is dark-only. tokens.json keeps the app-shell roles in the dark set.

### Fonts

- **DieGrotesk** (marketing pages), **ABCDiatype** (marketing meta/label text) and **dieGroteskA** (the dark app shell) are the served faces. They are served from the Butter CDN; the style guide falls back to system sans.

### Screenshots

- The keyring/3-D artwork, template thumbnails, the Butter wordmark and any photography in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Blog articles, template/block artwork and docs copy are the product's content; only frames and components were measured.
