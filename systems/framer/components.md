# Framer components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from framer.com on 2026-11-15, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the login form and gallery search were typed into then cleared and never sent; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (37 components, 99 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/19.2 500, #ffffff`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (97 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture: `dark` for every www page — the marketing pages paint the body-declared `--token-<uuid>` dark palette and ship no theme switcher; the community/marketplace stack paints dark too — and `light` for /login, the auth shell's own light stack. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages bounded at eight chunks — the gallery grid grows without bound and was truncated with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [menu-platform](screenshots/home-dark-menu-platform.png), [menu-resources](screenshots/home-dark-menu-resources.png), [menu-solutions](screenshots/home-dark-menu-solutions.png) |
| Framer AI | `/ai/` | [default](screenshots/ai-dark-default.png), [full](screenshots/ai-dark-full.png) |
| Agents | `/agents/` | [default](screenshots/agents-dark-default.png), [full](screenshots/agents-dark-full.png) |
| Design | `/design/` | [default](screenshots/design-dark-default.png), [full](screenshots/design-dark-full.png) |
| MCP | `/mcp/` | [default](screenshots/mcp-dark-default.png), [full](screenshots/mcp-dark-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-dark-default.png), [full](screenshots/pricing-dark-full.png) |
| Enterprise | `/enterprise/` | [default](screenshots/enterprise-dark-default.png), [full](screenshots/enterprise-dark-full.png) |
| About | `/about` | [default](screenshots/about-dark-default.png), [full](screenshots/about-dark-full.png) |
| Updates | `/updates` | [default](screenshots/updates-dark-default.png), [full](screenshots/updates-dark-full.png) |
| Academy | `/academy/` | [default](screenshots/academy-dark-default.png), [full](screenshots/academy-dark-full.png) |
| Developers | `/developers/` | [default](screenshots/developers-dark-default.png), [full](screenshots/developers-dark-full.png) |
| Blog | `/blog/` | [default](screenshots/blog-dark-default.png), [full](screenshots/blog-dark-full.png) |
| Customer stories | `/stories/` | [default](screenshots/stories-dark-default.png), [full](screenshots/stories-dark-full.png) |
| Careers | `/careers/` | [default](screenshots/careers-dark-default.png), [full](screenshots/careers-dark-full.png) |
| Contact | `/contact/` | [default](screenshots/contact-dark-default.png), [full](screenshots/contact-dark-full.png) |
| Downloads | `/downloads/` | [default](screenshots/downloads-dark-default.png), [full](screenshots/downloads-dark-full.png) |
| Compare | `/compare` | [default](screenshots/compare-dark-default.png), [full](screenshots/compare-dark-full.png) |
| For designers | `/solutions/designers/` | [default](screenshots/solutions-designers-dark-default.png), [full](screenshots/solutions-designers-dark-full.png) |
| Community gallery | `/community/gallery/` | [default](screenshots/community-gallery-dark-default.png), [full](screenshots/community-gallery-dark-full.png) |
| Marketplace templates | `/marketplace/templates/` | [default](screenshots/marketplace-templates-dark-default.png), [full](screenshots/marketplace-templates-dark-full.png) |
| Sign in (auth shell) | `/login` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [drawer](screenshots/mobile-home-dark-drawer.png), [full](screenshots/mobile-home-dark-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-dark-default.png), [full](screenshots/mobile-pricing-dark-full.png) |
| Community gallery, phone | `/community/gallery/` | [default](screenshots/mobile-community-gallery-dark-default.png), [full](screenshots/mobile-community-gallery-dark-full.png) |
| Contact, phone | `/contact/` | [default](screenshots/mobile-contact-dark-default.png), [full](screenshots/mobile-contact-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent | every www page | the 'We use cookies to enhance your experience…' card is hidden before every shot and reading — 'Ok' and 'Cookie Policy' were never clicked | hidden, never answered |
| Platform dropdown | every page header | hovered the 'Platform' trigger — the mega-dropdown opens on pointer hover; its links were never followed | [home-dark-menu-platform](screenshots/home-dark-menu-platform.png), [nav-panel](#platform-dropdown-panel) |
| Solutions / Resources dropdowns | every page header | the same hover on 'Solutions' and 'Resources' | [home-dark-menu-solutions](screenshots/home-dark-menu-solutions.png), [home-dark-menu-resources](screenshots/home-dark-menu-resources.png) |
| Mobile nav overlay | home page, phone width | the header nav toggle's own activation | [mobile-home-dark-drawer](screenshots/mobile-home-dark-drawer.png), [m-drawer](#mobile-nav-overlay) |
| Pricing controls | /pricing | the 'Yearly billing' switch and 'Credits per month' selects were measured at rest — switching re-prices the grid, so they were never flipped | [billing-toggle](#billing-toggle), [credits-select](#credits-select) |
| Login field | /login | typed into then cleared — nothing sent | [login-email](#email-field-login) |
| Gallery search | /community/gallery | typed into then cleared — nothing searched | [gal-search](#gallery-search) |
| Signed-in product | a Framer account | the dashboard, editor and every post-login surface needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 17 components were given a real keyboard focus. 11 draw an outline ring: `nav-dropdown-btn` (1px auto #101010 `dark.color.border.focusRing`, offset 0px), `nav-pricing` (1px auto #101010 `dark.color.border.focusRing`, offset 1px), `nav-login` (1px auto #101010 `dark.color.border.focusRing`, offset 1px), `nav-cta` (1px auto #101010 `dark.color.border.focusRing`, offset 1px), `hero-cta` (1px auto #101010 `dark.color.border.focusRing`, offset 1px), `hero-mcp` (1px auto #101010 `dark.color.border.focusRing`, offset 1px), `footer-link` (1px auto #101010 `dark.color.border.focusRing`, offset 1px), `locale-select` (1px auto #101010 `dark.color.border.focusRing`, offset 0px), `plan-cta` (1px auto #101010 `dark.color.border.focusRing`, offset 1px), `contact-link` (1px auto #101010 `dark.color.border.focusRing`, offset 0px), `m-hero-cta` (1px auto #e59700, offset 1px). 2 change only their fill or ink: `login-google`, `login-submit`. The other 4 show no ring, border or fill change: `credits-select`, `gal-filter`, `gal-open`, `gal-comm`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, box-shadow, color, opacity | gal-filter, gal-open |
| 0.2s | `ease` | background-color | login-google, login-submit |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Platform dropdown panel](#platform-dropdown-panel) | 650 x 156.78 | - | - | transparent | none | 0 |
| [Plan card](#plan-card) | 300 x 552.23 | - | - | transparent | none | 20px |
| [Login panel](#login-panel) | 1440 x 900 | - | - | #ffffff `core.color.palette.neutral-ff` | none | 0 |
| [Contact card](#contact-card) | 1200 x 186.89 | - | - | rgba(255, 255, 255, 0) | none | 30px |
| [Mobile nav overlay](#mobile-nav-overlay) | 390 x 844 | - | - | transparent | none | 0 |

## Components

### Site chrome

The header on every marketing page: the Framer mark, the Platform/Solutions/Resources mega-dropdown triggers (an `a` without href whose panel opens on hover), Pricing and Enterprise links, Log in and Sign up; the mega-dropdown panel opens under the trigger.

#### Site header
The bar on every marketing page: the Framer mark, the Platform/Solutions/Resources mega-dropdown triggers, Pricing, Enterprise, "Log in" and "Sign up". Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 64; padding 0px 20px; background transparent; text Inter Variable 14/14 400, #ffffff `core.color.palette.neutral-ff`; icon 8 x 8, #000000 `core.color.palette.neutral-00`; layers div.framer-ngytjn 16.0x24.0; div.framer-4mgnl8 87.2x35.6 rgba(255, 255, 255, 0.1) 8px; div.framer-4mgnl8 92.1x35.6 rgba(255, 255, 255, 0.1) 8px; div.framer-4mgnl8 102.1x35.6 rgba(255, 255, 255, 0.1) 8px; div.framer-4mgnl8 86.0x35.6 rgba(255, 255, 255, 0.1) 8px; div.framer-4mgnl8 64.3x35.6 rgba(255, 255, 255, 0.1) 8px.

Child layers that carry the look: div 16x24 image url(data:…)%22></path></svg>"); div 87.2x35.6 background rgba(255, 255, 255, 0.1) `core.color.palette.alpha-white.10` radius 8px; div 92.1x35.6 background rgba(255, 255, 255, 0.1) `core.color.palette.alpha-white.10` radius 8px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Framer mark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 76.95 x 26; background transparent; text Inter Variable 14/14 400, #ffffff `core.color.palette.neutral-ff`; layers div.framer-ngytjn 16.0x24.0.

Child layers that carry the look: div 16x24 image url(data:…)%22></path></svg>").

![Logo default](components/crops/mkt-logo-default.png)

#### Nav dropdown trigger
The "Platform" header item — an `a` without href whose mega-dropdown opens on hover (never followed). Read as `nav-dropdown-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 91.2 x 39.59; background transparent; text Inter Variable 14/19.6 400, rgba(255, 255, 255, 0.8) `core.color.palette.alpha-white.80`; icon 8 x 8, #000000 `core.color.palette.neutral-00`; layers div.framer-4mgnl8 87.2x35.6 rgba(255, 255, 255, 0.1) 8px |
| hover | text Inter Variable 14/19.6 400, #ffffff `core.color.palette.neutral-ff` |
| focus-visible | outline 1px auto #101010 `dark.color.border.focusRing`, offset 0px; text Inter Variable 14/19.6 400, #ffffff `core.color.palette.neutral-ff`; layers a.framer-uTdPy.framer-aZ6KF 91.2x39.6 1px auto rgb(16, 16, 16) offset 0px; div.framer-4mgnl8 87.2x35.6 rgba(255, 255, 255, 0.1) 8px |
| pressed | text Inter Variable 14/19.6 400, #ffffff `core.color.palette.neutral-ff` |

Child layers that carry the look: div 87.2x35.6 background rgba(255, 255, 255, 0.1) `core.color.palette.alpha-white.10` radius 8px.

![Nav dropdown trigger default](components/crops/nav-dropdown-btn-default.png) ![Nav dropdown trigger hover](components/crops/nav-dropdown-btn-hover.png) ![Nav dropdown trigger focus-visible](components/crops/nav-dropdown-btn-focus-visible.png) ![Nav dropdown trigger pressed](components/crops/nav-dropdown-btn-pressed.png)

#### Platform dropdown panel
The mega-dropdown panel opened by hovering "Platform" (Create/Build/Grow columns and the Updates thumbnail); its links were never followed. Read as `nav-panel` on the home page.

**Values (default).** size 650 x 156.78; background transparent; text Inter Variable 14/19.6 400, rgba(255, 255, 255, 0.6) `core.color.palette.alpha-white.60`; layers div.framer-4mgnl8 12.6x20.3 rgba(255, 255, 255, 0.1) 8px; div.framer-4mgnl8 55.8x20.3 rgba(255, 255, 255, 0.1) 8px; div.framer-4mgnl8 53.8x20.3 rgba(255, 255, 255, 0.1) 8px; div.framer-4mgnl8 34.4x20.3 rgba(255, 255, 255, 0.1) 8px; div.framer-4mgnl8 35.4x20.3 rgba(255, 255, 255, 0.1) 8px; div.framer-4mgnl8 58.6x20.3 rgba(255, 255, 255, 0.1) 8px.

Child layers that carry the look: div 12.6x20.3 background rgba(255, 255, 255, 0.1) `core.color.palette.alpha-white.10` radius 8px; div 55.8x20.3 background rgba(255, 255, 255, 0.1) `core.color.palette.alpha-white.10` radius 8px; div 53.8x20.3 background rgba(255, 255, 255, 0.1) `core.color.palette.alpha-white.10` radius 8px.

![Platform dropdown panel default](components/crops/nav-panel-default.png)

#### Nav link
The "Pricing" header link; measured, never followed. Read as `nav-pricing` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 68.31 x 39.59; background transparent; text Inter Variable 14/19.6 400, rgba(255, 255, 255, 0.8) `core.color.palette.alpha-white.80`; layers div.framer-4mgnl8 64.3x35.6 rgba(255, 255, 255, 0.1) 8px |
| hover | text Inter Variable 14/19.6 400, #ffffff `core.color.palette.neutral-ff` |
| focus-visible | outline 1px auto #101010 `dark.color.border.focusRing`, offset 1px; layers a.framer-uTdPy.framer-aZ6KF 68.3x39.6 1px auto rgb(16, 16, 16) offset 1px; div.framer-4mgnl8 64.3x35.6 rgba(255, 255, 255, 0.1) 8px |

Child layers that carry the look: div 64.3x35.6 background rgba(255, 255, 255, 0.1) `core.color.palette.alpha-white.10` radius 8px.

![Nav link default](components/crops/nav-pricing-default.png) ![Nav link hover](components/crops/nav-pricing-hover.png) ![Nav link focus-visible](components/crops/nav-pricing-focus-visible.png) ![Nav link pressed](components/crops/nav-pricing-pressed.png)

#### Log in link
The "Log in" header link to /login; measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 39.41 x 17; background transparent; text Inter Variable 14/19.6 400, rgba(255, 255, 255, 0.6) `core.color.palette.alpha-white.60` |
| hover | text Inter Variable 14/19.6 400, #ffffff `core.color.palette.neutral-ff` |
| focus-visible | outline 1px auto #101010 `dark.color.border.focusRing`, offset 1px; layers a.framer-text.framer-styles-preset-1si2ozi 39.4x17.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Inter Variable 14/19.6 400, #ffffff `core.color.palette.neutral-ff` |

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Header CTA
The "Sign up" header button; links to the auth shell, measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 64.09 x 30; padding 8px 10px; radius 8px; background #ffffff `core.color.palette.neutral-ff`; text Inter Variable 14/14 400, #000000 `core.color.palette.neutral-00` |
| focus-visible | outline 1px auto #101010 `dark.color.border.focusRing`, offset 1px |

![Header CTA default](components/crops/nav-cta-default.png) ![Header CTA hover](components/crops/nav-cta-hover.png) ![Header CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Header CTA pressed](components/crops/nav-cta-pressed.png)

### Home

The home hero: the display masthead over the live editor-demo canvas, the white 'Get started for free' pill beside the ghost 'Install the MCP' button, and section headings.

#### Hero headline
"Framer is the pro website builder with a world-class design agent" — the www.framer.com hero display heading. Read as `hero-h1` on the home page.

**Values (default).** size 782 x 108; background transparent; text GT Walsheim Medium 54/54 500, #ffffff `core.color.palette.neutral-ff`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero CTA
The white "Get started for free" pill in the hero; links to the auth shell, measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 149.41 x 34; padding 10px 14px; radius 8px; background #ffffff `core.color.palette.neutral-ff`; text Inter Variable 14/14 400, #000000 `core.color.palette.neutral-00` |
| hover | opacity 0.6 |
| focus-visible | outline 1px auto #101010 `dark.color.border.focusRing`, offset 1px |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero secondary button
The "Install the MCP" ghost button beside the hero CTA; measured, never followed. Read as `hero-mcp` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 123.81 x 34; padding 10px 14px; radius 8px; background rgba(255, 255, 255, 0.1) `core.color.palette.alpha-white.10`; text Inter Variable 14/14 400, #ffffff `core.color.palette.neutral-ff` |
| hover | opacity 0.6 |
| focus-visible | outline 1px auto #101010 `dark.color.border.focusRing`, offset 1px |

![Hero secondary button default](components/crops/hero-mcp-default.png) ![Hero secondary button hover](components/crops/hero-mcp-hover.png) ![Hero secondary button focus-visible](components/crops/hero-mcp-focus-visible.png) ![Hero secondary button pressed](components/crops/hero-mcp-pressed.png)

#### Section heading
A marketing section heading further down the home page. Read as `section-h2` on the home page.

**Values (default).** size 520 x 96.81; background transparent; text GT Walsheim Medium 44/48.4 500, #ffffff `core.color.palette.neutral-ff`.

![Section heading default](components/crops/section-h2-default.png)

### Pricing

The /pricing grid: the 'Yearly billing' switch and the 'Credits per month' selects that re-price the cards, the Free/Basic/Pro/Enterprise columns and their CTAs, and the FAQ rows below.

#### Pricing headline
"Start free, then scale your site" — the /pricing masthead. Read as `price-h1` on the pricing page.

**Values (default).** size 420 x 108; background transparent; text GT Walsheim Medium 54/54 500, #ffffff `core.color.palette.neutral-ff`.

![Pricing headline default](components/crops/price-h1-default.png)

#### Billing toggle
The "Yearly billing" switch beside the plan names; measured at rest, never toggled (toggling would re-price the grid). Read as `billing-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 85.61 x 19.59; background transparent; text Inter Variable 14/19.6 400, rgba(255, 255, 255, 0.6) `core.color.palette.alpha-white.60` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Billing toggle default](components/crops/billing-toggle-default.png) ![Billing toggle hover](components/crops/billing-toggle-hover.png) ![Billing toggle pressed](components/crops/billing-toggle-pressed.png)

#### Credits select
The "Credits per month" select on a plan card (1,000–10,000 AI credits); measured at rest, never opened (its options recompute prices). Read as `credits-select` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 250 x 34; padding 8px 10px; background transparent; text Inter 14/18.2 500, rgba(255, 255, 255, 0.8) `core.color.palette.alpha-white.80` |

![Credits select default](components/crops/credits-select-default.png) ![Credits select hover](components/crops/credits-select-hover.png) ![Credits select focus-visible](components/crops/credits-select-focus-visible.png) ![Credits select pressed](components/crops/credits-select-pressed.png)

#### Plan card
The Pro plan column: name, price, feature list and its CTA. Read as `plan-card` on the pricing page.

**Values (default).** size 300 x 552.23; padding 20px; background transparent; text Inter Variable 18/24.3 400, #ffffff `core.color.palette.neutral-ff`; icon 12 x 12, #000000 `core.color.palette.neutral-00`; layers div.framer-f267wx 260.0x1.0 rgb(26, 26, 26); div::before.framer-form-input-wrapper.framer-form-select-wrapper 16pxx18px rgba(255, 255, 255, 0.8); div::after.framer-form-input-wrapper.framer-form-select-wrapper 260pxx34px T:1px solid rgb(26, 26, 26) / R:1px solid rgb(26, 26, 26) / B:1px solid rgb(26, 26, 26) / L:1px solid rgb(26, 26, 26) 8px; div.framer-xmqd09 260.0x1.0 rgb(26, 26, 26); a.framer-R3.

Child layers that carry the look: div 260x1 background #1a1a1a `core.color.palette.neutral-1a`; div::before 16pxx18px background rgba(255, 255, 255, 0.8) `core.color.palette.alpha-white.80`; div::after 260pxx34px border 1px solid #1a1a1a `core.color.palette.neutral-1a` radius 8px.

![Plan card default](components/crops/plan-card-default.png)

#### Plan CTA
The Pro plan card's action button; measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 260 x 34; padding 10px 14px; radius 8px; background #0099ff `core.color.palette.accent.blue`; text Inter Variable 14/14 400, #ffffff `core.color.palette.neutral-ff` |
| hover | opacity 0.6 |
| focus-visible | outline 1px auto #101010 `dark.color.border.focusRing`, offset 1px |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### FAQ row
A question row in the /pricing FAQ ("What are credits?"); measured at rest and on hover, never toggled. Read as `faq-acc` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 420 x 24.3; background transparent; text Inter Variable 18/24.3 400, #ffffff `core.color.palette.neutral-ff` |

![FAQ row default](components/crops/faq-acc-default.png) ![FAQ row hover](components/crops/faq-acc-hover.png)

### Contact

The /contact directory: the masthead over the Support / Billing / Emergency / Sales / Abuse cards — a contact surface, not a form.

#### Contact headline
"Get in touch with the team" — the /contact masthead over the support/billing/sales directory. Read as `contact-h1` on the contact page.

**Values (default).** size 369 x 108; background transparent; text GT Walsheim Medium 54/54 500, #ffffff `core.color.palette.neutral-ff`.

![Contact headline default](components/crops/contact-h1-default.png)

#### Contact card
The Support directory card; a contact surface, not a form. Read as `contact-card` on the contact page.

**Values (default).** size 1200 x 186.89; padding 30px; background rgba(255, 255, 255, 0); text Inter Variable 18/24.3 400, #ffffff `core.color.palette.neutral-ff`; icon 12 x 12, #0000ee; layers ::after rgba(0, 0, 0, 0) 0px none 1.

![Contact card default](components/crops/contact-card-default.png)

#### Contact link
A link inside a contact directory card; measured, never followed. Read as `contact-link` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 92.02 x 34; padding 10px 14px; radius 8px; background #ffffff `core.color.palette.neutral-ff`; text Inter Variable 15/15 400, #000000 `core.color.palette.neutral-00` |
| hover | opacity 0.6 |
| focus-visible | outline 1px auto #101010 `dark.color.border.focusRing`, offset 0px |

![Contact link default](components/crops/contact-link-default.png) ![Contact link hover](components/crops/contact-link-hover.png) ![Contact link focus-visible](components/crops/contact-link-focus-visible.png) ![Contact link pressed](components/crops/contact-link-pressed.png)

### Login (auth shell)

/login — the auth shell's sign-in card ('Welcome to Framer', Google SSO and a work-e-mail field + Continue), a light third stack that does not share the --token-<uuid> layer. Measured as a form, never submitted.

#### Login panel
The auth-shell sign-in card on /login: "Welcome to Framer" with Google SSO and an e-mail field. The auth shell is a light third stack. Read as `login-panel` on the login page.

**Values (default).** size 1440 x 900; background #ffffff `core.color.palette.neutral-ff`; text Inter Variable UI 20/24 550, #222222 `core.color.palette.neutral-22`; icon 16 x 24, #222222 `core.color.palette.neutral-22`.

![Login panel default](components/crops/login-panel-default.png)

#### Google SSO button
The "Continue with Google" button; measured, never pressed. Read as `login-google` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 230 x 30; padding 0px 10px; radius 8px; background #222222 `core.color.palette.neutral-22`; text Inter Variable UI 12/normal 450, #ffffff `core.color.palette.neutral-ff`; transition background-color 0.2s ease; icon 11 x 11, #ffffff `core.color.palette.neutral-ff` |
| hover, focus-visible, pressed | background #333333 `core.color.palette.neutral-33` |

![Google SSO button default](components/crops/login-google-default.png) ![Google SSO button hover](components/crops/login-google-hover.png) ![Google SSO button focus-visible](components/crops/login-google-focus-visible.png) ![Google SSO button pressed](components/crops/login-google-pressed.png)

#### Email field (login)
The work e-mail input on the sign-in card; focused and typed into then cleared — never submitted. Read as `login-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 228 x 30; padding 0px 7px 1px 7px; radius 8px; background transparent; text Inter Variable UI 12/normal 450, #222222 `core.color.palette.neutral-22`; placeholder #999999 `core.color.palette.neutral-99`; ancestor 1 up div.i1ubxgci bg rgba(0, 0, 0, 0.05) `core.color.palette.alpha-black.5` |

![Email field (login) default](components/crops/login-email-default.png) ![Email field (login) focused](components/crops/login-email-focused.png) ![Email field (login) filled](components/crops/login-email-filled.png)

#### Continue submit
The "Continue" submit button; its states were measured but the button was never clicked — nothing was submitted. Read as `login-submit` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 230 x 30; padding 0px 10px; radius 8px; background rgba(0, 0, 0, 0.05) `core.color.palette.alpha-black.5`; text Inter Variable UI 12/normal 450, #333333 `core.color.palette.neutral-33`; transition background-color 0.2s ease |
| hover, focus-visible, pressed | background rgba(0, 0, 0, 0.07) `core.color.palette.alpha-black.7` |

![Continue submit default](components/crops/login-submit-default.png) ![Continue submit hover](components/crops/login-submit-hover.png) ![Continue submit focus-visible](components/crops/login-submit-focus-visible.png) ![Continue submit pressed](components/crops/login-submit-pressed.png)

### Community gallery (product stack)

/community/gallery — the public showcase index inside the community stack: the 'Search Gallery' input, the Trending/Recent/Vibe sort buttons, the per-card 'Open' buttons and the 'Community' header menu — a different app that also paints dark.

#### Gallery headline
"Gallery" — the /community/gallery masthead in the community stack (a different app that also paints dark). Read as `gal-h1` on the community-gallery page.

**Values (default).** size 92.61 x 30; background transparent; text walsheim 30/30 500, #ffffff `core.color.palette.neutral-ff`.

![Gallery headline default](components/crops/gal-h1-default.png)

#### Gallery search
The "Search Gallery" input; focused and typed into then cleared — never searched. Read as `gal-search` on the community-gallery page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 203 x 14.39; padding 0px 0px 0px 1px; background transparent; text inter 12/14.4 450, #ffffff `core.color.palette.neutral-ff`; placeholder #999999 `core.color.palette.neutral-99`; ancestor 1 up label.Wf6zXG_field bg #1f1f1f `core.color.palette.neutral-1f` |
| focused | ancestor 1 up label.Wf6zXG_field bg #1f1f1f `core.color.palette.neutral-1f` shadow #333333 0px 0px 0px 1px inset |

![Gallery search default](components/crops/gal-search-default.png) ![Gallery search focused](components/crops/gal-search-focused.png)

#### Filter button
A gallery sort button (Trending / Recent / Vibe); measured at rest, never toggled (toggling would re-sort the grid). Read as `gal-filter` on the community-gallery page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 74 x 30; padding 0px 10px; radius 8px; background #1f1f1f `core.color.palette.neutral-1f`; text inter 12/12 450, #ffffff `core.color.palette.neutral-ff`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

![Filter button default](components/crops/gal-filter-default.png) ![Filter button hover](components/crops/gal-filter-hover.png) ![Filter button focus-visible](components/crops/gal-filter-focus-visible.png) ![Filter button pressed](components/crops/gal-filter-pressed.png)

#### Card Open button
An "Open" button on a gallery card; measured, never followed (it would open the site's page). Read as `gal-open` on the community-gallery page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 55 x 30; padding 0px 10px; border 1px solid transparent; radius 8px; background #1f1f1f `core.color.palette.neutral-1f`; text inter 12/12 450, #ffffff `core.color.palette.neutral-ff`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #262626 |
| pressed | background #262626; opacity 0.8 |

![Card Open button default](components/crops/gal-open-default.png) ![Card Open button hover](components/crops/gal-open-hover.png) ![Card Open button focus-visible](components/crops/gal-open-focus-visible.png) ![Card Open button pressed](components/crops/gal-open-pressed.png)

#### Community menu button
The "Community" dropdown button in the gallery header — a local UI toggle; measured, never toggled. Read as `gal-comm` on the community-gallery page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 117 x 30; padding 0px 8px; radius 8px; background #1f1f1f `core.color.palette.neutral-1f`; text inter 12/normal 450, #ffffff `core.color.palette.neutral-ff`; icon 10 x 15, #ffffff `core.color.palette.neutral-ff` |
| hover, pressed | background #262626 |

![Community menu button default](components/crops/gal-comm-default.png) ![Community menu button hover](components/crops/gal-comm-hover.png) ![Community menu button focus-visible](components/crops/gal-comm-focus-visible.png) ![Community menu button pressed](components/crops/gal-comm-pressed.png)

### Mobile (390 wide)

The phone surface at 390 wide: the header with the nav toggle, the nav overlay, the hero and CTA.

#### Mobile top bar
The phone header at 390 wide: the Framer mark and the nav toggle. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 390 x 64; background transparent; text Inter Variable 14/14 400, #ffffff `core.color.palette.neutral-ff`; layers div.framer-ngytjn 16.0x24.0; a.framer-16mrjhl.framer-enysp5 64.1x30.0 rgb(255, 255, 255) 8px; div.framer-cw6b3u 20.0x2.0 rgb(255, 255, 255) 10px; div.framer-1ctjw9m 20.0x2.0 rgb(255, 255, 255) 10px; div.framer-1gyv5v7 390.0x64.0 rgb(0, 0, 0).

Child layers that carry the look: div 16x24 image url(data:…)%22></path></svg>"); a 64.1x30 background #ffffff `core.color.palette.neutral-ff` radius 8px; div 20x2 background #ffffff `core.color.palette.neutral-ff` radius 10px.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile menu button
The header nav toggle at 390 wide — a local UI toggle; the opened state was measured after activating it. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 64 x 64; background transparent; text sans-serif 12/normal 400, #000000 `core.color.palette.neutral-00`; transform translate(0px, -32px); layers div.framer-cw6b3u 20.0x2.0 rgb(255, 255, 255) 10px; div.framer-1ctjw9m 20.0x2.0 rgb(255, 255, 255) 10px |
| opened | transform matrix(1, 0, 0, 6.72655, 0, 183.25); layers div.framer-cw6b3u 20.0x2.0 rgb(255, 255, 255) 50% / 500%; div.framer-1ctjw9m 20.0x2.0 rgb(255, 255, 255) 50% / 500% |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 20x2 background #ffffff `core.color.palette.neutral-ff` radius 10px; div 20x2 background #ffffff `core.color.palette.neutral-ff` radius 10px.

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png) ![Mobile menu button opened](components/crops/m-menu-btn-opened.png)

#### Mobile nav overlay
The nav overlay opened by the menu button (the page links plus Log in/Sign up); its links were never followed. Read as `m-drawer` on the home page at 390 wide.

**Values (default).** size 390 x 844; background transparent; text Inter Variable 14/14 400, #ffffff `core.color.palette.neutral-ff`; layers nav.framer-vzLJR.framer-140pdlc 390.0x844.0 rgb(0, 0, 0); div.framer-z96yy7 390.0x844.0 rgb(0, 0, 0); div.framer-ngytjn 16.0x24.0; a.framer-uTdPy.framer-aZ6KF 55.2x19.6 rgba(255, 255, 255, 0) 8px; div.framer-4mgnl8 51.2x15.6 rgba(255, 255, 255, 0.1) 8px; a.framer-uTdPy.framer-aZ6KF 60.1x19.6 rgba(255, 255, 255, 0) 8px; ancestor 1 up div.framer-nwUvx.framer-k4Apk bg #000000 `core.color.palette.neutral-00`.

Child layers that carry the look: nav 390x844 background #000000 `core.color.palette.neutral-00`; div 390x844 background #000000 `core.color.palette.neutral-00`; div 16x24 image url(data:…)%22></path></svg>").

![Mobile nav overlay default](components/crops/m-drawer-default.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 350 x 144; background transparent; text GT Walsheim Medium 36/36 500, #ffffff `core.color.palette.neutral-ff`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The hero "Get started for free" pill at 390 wide; measured never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 137.81 x 29; padding 8px 12px; radius 8px; background #ffffff `core.color.palette.neutral-ff`; text Inter Variable 13/13 400, #000000 `core.color.palette.neutral-00` |
| focus-visible | outline 1px auto #e59700, offset 1px |

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

### Footer

The page footer: sitemap columns, social icons and the 'English'/'Japanese' locale select.

#### Footer
The page footer: product/solutions/resources/company columns, social icons and the English/Japanese locale select. Read as `footer` on the home page.

**Values (default).** size 1240 x 638; padding 20px; background #000000 `core.color.palette.neutral-00`; text Inter Variable 14/19.6 400, #ffffff `core.color.palette.neutral-ff`; icon 12 x 12, #ffffff `core.color.palette.neutral-ff`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 53.31 x 22; radius 8px; background transparent; text Inter Variable 14/19.6 400, rgba(255, 255, 255, 0.6) `core.color.palette.alpha-white.60` |
| hover | text Inter Variable 14/19.6 400, #ffffff `core.color.palette.neutral-ff` |
| focus-visible | outline 1px auto #101010 `dark.color.border.focusRing`, offset 1px; layers a.framer-UNEfR.framer-aZ6KF 53.3x22.0 1px auto rgb(16, 16, 16) offset 1px 8px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Locale select
The "English" locale select in the footer — a local UI control; measured, never changed. Read as `locale-select` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 78 x 18; border 1px solid #767676; background #efefef; text sans-serif 12/normal 400, #000000 `core.color.palette.neutral-00`; opacity 0 |
| focus-visible | outline 1px auto #101010 `dark.color.border.focusRing`, offset 0px |

![Locale select default](components/crops/locale-select-default.png) ![Locale select hover](components/crops/locale-select-hover.png) ![Locale select focus-visible](components/crops/locale-select-focus-visible.png) ![Locale select pressed](components/crops/locale-select-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Framer mark, the mega-dropdown glyphs, social glyphs, gallery thumbnails) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Framer's product is the site editor and dashboard: projects, the canvas, CMS collections, publishing, analytics, workspaces — every surface after `Log in` needs an account and was never reached. /login is the only app surface a signed-out visitor sees, and it was measured as a form, never submitted. The editor-like canvas embedded in the marketing pages is a demo surface of the public site, not the signed-in product.

### Pages

- **The account.** The dashboard, editor and every post-login surface (projects, the canvas, CMS, publishing, workspaces, the gallery upload flow) was never reached; the /login form was measured as a form and never submitted; 'Continue with Google' was never followed.
- **Forms.** The /login e-mail field and the gallery 'Search Gallery' input were measured at rest and typed into then cleared — nothing was sent; what a submission returns is unverified.
- **Gallery and marketplace item pages** (a showcased site, a template's detail page) were not captured — the grids are index surfaces; 'Open' buttons lead off-site or to gated remixes.
- **Blog posts, updates entries and customer stories** are index-level captures only; individual articles are the same templates, unmeasured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **The 'Yearly billing' switch and 'Credits per month' selects** on /pricing re-price the grid when changed; they were measured at rest and never switched, so the monthly prices and alternate credit tiers are uncaptured.
- **The mega-dropdown panel items' focus/hover** is partially covered: the panel opens on hover and closes on blur, so a real keyboard focus inside it could not be held.

### Themes

Every www.framer.com page paints one surface — the dark palette the `body`-declared `--token-<uuid>` colour styles resolve to; no theme switcher or alternate layer exists on the marketing site. The /community/gallery and /marketplace surfaces are the product's community stack, a different app that also paints dark; /login is the auth shell, a light third stack whose values are component tokens, not a marketing light theme. There is no painted light variant of the marketing site.

### Fonts

- The marketing pages set **Inter** (self-hosted, with GT Walsheim Bold/Medium for display presets and Azeret Mono for code styling — the @font-face list is in raw/css-vars.json); the measured face on each component is in its entry. The style guide falls back to system sans.

### Screenshots

- The product demos, video frames, community thumbnails and photography in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, plan prices, job titles, plugin names and community author names are the product's content; only frames and components were measured.
